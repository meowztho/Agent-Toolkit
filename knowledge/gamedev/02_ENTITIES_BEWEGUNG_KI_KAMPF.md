# Teil II — Lebendige Welt und Gameplay (Bereiche 05–09)

## 05 · Entities, Komponenten und Interaktion

**Wozu?** Eine Karte enthält konkrete Figuren, Türen, Truhen, Gegner, Projektile und Deko. Ein Entity-System verwaltet deren Identität und Lebensdauer, nicht zwingend über Vererbung.

**Varianten:** Objekt/Klassenmodell, Szenenknoten, Komponenten-Komposition, Entity-Component-System (ECS), einfache Listen/Maps. Ein kleiner Prototyp braucht nicht zwingend ECS. *Eine spielinterne Trainerklasse* ist meist ein Datentyp, keine Programmklasse.

**Daten und Instanzen:** Definition/PrefabRef, `entityId`, `position`, Komponenten wie Transform, Collision, Interaction, Health, RenderRef, Lifetime, Tags, Owner; nicht jede Komponente gehört in den Save.

**Verarbeitung:** Spawnregel → Definition auflösen → gültige ID vergeben → benötigte Komponenten erstellen → Systeme aktualisieren sie → Interaktionsprüfung (Nähe, Berechtigung, Zustand) → Despawn/Cleanup → ggf. Zustand speichern.

**Beziehungen:** Welt (04), Status/Events (03), Bewegung (07), KI (08), Kampf (09), Darstellung (13–14).

**Risiken:** doppelte Entity-ID, unsichtbare Kollision nach Despawn, verwaiste Listener, Objekt in falscher Szene, persistente Tür setzt sich beim Neuladen zurück.

**Tests:** zweimal spawnen/despawnen, identische Prefabs mit abweichendem Zustand, Interaktion außerhalb Reichweite, Szene verlassen/wiederbetreten, Eventlistener/Collider bereinigt.

**Promptfrage:** „Welche Objekte sind Definition, Runtime-Entity oder nur Grafik? Wer erzeugt und entfernt sie, und wer prüft Interaktionen?“

## 06 · Spieler, NPCs und Kreaturen

**Wozu?** Charakterdaten, individuelle Exemplare und ihre Regeln bilden die Grundlage für Spielergesteuerte und KI-gesteuerte Wesen. Beispiel: Artbeschreibung und ein gefangenes Monster sind unterschiedliche Daten.

**Varianten:** PlayerProfile, CharacterStats, SpeciesDefinition, MonsterInstance, Party/Box, NPCProfile, Rollen/Fraktionen, Fähigkeiten, Typen, Level, Evolution, Status, Dialogbezug. Optionale IV/EV, Zucht, Hunger usw. nur bei gewünschtem Gameplay.

**Daten:** Species: `speciesId`, Typen, Basisstats, Lernliste, Entwicklungsregeln, Animations-/Spriterefs; Instanz: `instanceId`, speciesRef, Level, XP, HP, bekannte Moves, Status, Team-/Besitzbezug. NPC: Rolle, Spawn, Team-/Dialog-/Interaktionsrefs.

**Laufzeitkette:** Species-/NPC-Daten lesen → konkrete Instanz erzeugen → Stats ableiten → Kontrolle (Spieler/KI) zuordnen → Welt-/Kampfregeln nutzen → Erfahrung/Status/Team verändern → persistente Eigenschaften speichern.

**Abhängigkeiten:** Daten (02), KI (08), Kampfeffekte (09), Items (10), Progression (11), Animationsrefs (13), Save (17).

**Risiken:** alle Monster einer Art teilen versehentlich HP; Leveländerung aktualisiert Stats inkonsistent; Wechsel zwischen Mensch/Monster teleportiert Begleiter; zerstörte Entity löscht ungewollt Party-Monster.

**Tests:** zwei Instanzen derselben Art mit unterschiedlichen HP/Level; Teamwechsel in und außerhalb Kampf; Entwicklung und Learnset; Neustart/Reload; Besitzer-/Followerzustände.

**ROM-Referenz:** PGE stellt Species-/Attacken-/Evolutions-/Trainer-/Itemtabellen aus dem GBA-Kontext gegenüber. Das belegt Datenfelder und Relationen, nicht Original-Klassenstruktur.

**Promptfrage:** „Welche Eigenschaften gehören zur Art, welche zum Individuum, welche zum aktiven Körper? Verfolge Level/HP/Status über Welt, beide Kampfarten und Save.“

## 07 · Input, Bewegung, Navigation und Kollision

**Wozu?** Spielabsichten müssen zu legaler Bewegung werden. Bildschirmanimation allein bewegt noch keine Figur durch eine konsistente Welt.

**Varianten:** Grid-Schritte, freie 2D-/3D-Bewegung, Rigidbody/Kinematic/Character Controller, Wegpunkte, Navmesh, A*, Steering, Follower-Leash, bewegungsspezifische Profile (Wasser, Tunnel, Fliegen).

**Daten und Zustand:** Aktion/Richtung, gewünschtes Ziel, Geschwindigkeit, Bewegungslimits, Kollisionskörper, Navigationsprofil, Pfad, Nachlaufabstand, Blocker-/Terrainflags.

**Verarbeitung:** Input/KI-Ziel → gewünschte Bewegung → physikalischer/nav-basierter Resolver → gültige neue Position → Trigger/Interaktion → Animationsparameter → Kamera. Renderposition sollte konsistent mit der Gameplayposition bleiben.

**Abhängigkeiten:** Welt (04) liefert Passierbarkeit; Entities (05) liefern Kollisionskörper; KI (08) Pfadziele; Animation (13), UI (16).

**Risiken:** Spieler wird geblockt, Gegner gehen durch Wand; Sprint umgeht Collision; Follower teleportiert; Aufzug/Treppe ist visuell begehbar, physikalisch nicht; Wegsuche hängt durch unpassierbaren Bereich.

**Tests:** jede Bewegungsart auf jeder Terrainklasse, Treppe/Tür/Kartengrenze, dynamisch öffnende Tür, „Follower kann nicht folgen“ und Wiedervereinigung ohne Teleport, Pathfinding bei Hindernissen.

**Promptfrage:** „Leite für jede Figuren-/Gegnerklasse die tatsächlichen Bewegungsprofile her. Stelle Bild, Kollision, Navigation und Trigger gegenüber.“

## 08 · KI, Wahrnehmung und Simulation

**Wozu?** Nicht-Spieler-Akteure wählen aufgrund ihrer Informationen Aktionen. Beispiel: Ein wildes Monster patrouilliert, bemerkt den Spieler, verfolgt ihn und greift nur in Reichweite an.

**Varianten:** endliche Zustandsmaschine (FSM), Utility AI, Behavior Tree, GOAP/Planung, geskriptete Sequenzen, einfache Heuristiken. Entscheidung und physische Ausführung sind verschiedene Verantwortungen.

**Daten und Zustand:** `aiProfileId`, Wahrnehmungsradius, Sicht-/Hörregeln, Fraktion, Aggressivität, Prioritäten, aktueller Modus, Ziel-ID, Cooldowns, Pfadstatus, RNG-/Spawnkontext.

**Verarbeitung:** Wahrnehmungsdaten → Kandidaten/Ziele → Entscheidung → Command (z.B. „verfolge“) → Navigation/Kampf führt aus → Ergebnis zurück an KI → Neubewertung. Fernsimulation braucht nur bei Spielanforderung eine Sonderstrategie.

**Abhängigkeiten:** Welt/Navigation (04/07), Entities/Stats (05/06), Kampf (09), Spawn/Generierung (18), Performance (20).

**Risiken:** KI sieht durch Mauern; Zustand bleibt nach Tod aktiv; mehrere Gegner überlasten Frame; Gegner verfolgen unerreichbares Ziel endlos; zufällige Entscheidungen sind nicht reproduzierbar.

**Tests:** Sichtlinie/Hindernis, Zielverlust, Aggro-/Leashgrenze, Verfolgung/Abbruch, Tod während Pfadberechnung, viele Akteure, gleiche Seed-Replays soweit zugesichert.

**Promptfrage:** „Rekonstruiere Wahrnehmung → Entscheidung → Ausführung → Feedback an einem echten NPC. Welche KI existiert, welche ist nur Animationssimulation?“

## 09 · Kampf, Attacken und Effekte

**Wozu?** Kampf übersetzt Angriffsabsichten in gültige, nachvollziehbare Auswirkungen. Die gleiche Attackendefinition kann in Echtzeit und rundenbasiert verwendet werden, die Ausführungslogik jedoch unterschiedlich sein.

**Varianten:** Runden-/Prioritätsqueue, Echtzeit mit Cooldowns/Hitboxen/Projektile, Action Points, gemeinsame Effektauflösung. Nicht jede Attacke muss überall erlaubt sein; Unterschiede müssen explizit benannt sein.

**Daten:** `moveId`, Typ, Schadenskategorie, Stärke, Präzision, Kosten/PP, Zielart, Reichweite, Status-/Effektliste, Hitbox-/Animationsref; Runtime: Akteur, Ziel, Zeit, Ressourcenvorrat, aktive Effekte.

**Laufzeitkette:** Auswahl → Legalitätsprüfung → Kosten/Timing reservieren → Ziel/Treffer bestimmen → gemeinsame Effekte (Schaden, Heilung, Status, Knockback) berechnen → Zustandsänderung/KO/Rewards → Events → Animation/UI/Audio. Hitbox-Events können Treffer auslösen, aber die Kampfregeln bewerten ihn.

**Abhängigkeiten:** Monsterstats (06), Zeit (01), Zustand (03), Navigation (07), KI (08), Items (10), Progression (11), Animation (13).

**Risiken:** Schadensformeln dupliziert, „Move existiert“ aber ohne Runtime-Effekt, PP/Cooldown im falschen Kampftyp, Flächenangriff trifft tote Entities, KO vergibt Beute zweimal.

**Tests:** Treffer/Fehlschlag, Typenschwäche, Kostenmangel, Immunität, paralleler KO, Statusdauer, Pause, beide Kampfarten, Kampfende mit Reload und Reward-Wiederholung.

**ROM-Referenz:** PGE dokumentiert Attacken-/Effekt-/Kompatibilitätstabellen; KM nennt entsprechende Datenkategorien, aber beide belegen nicht die exakte Original-Laufzeitauflösung.

**Promptfrage:** „Verfolge dieselbe Attacke in jedem vorhandenen Kampfmodus vom Command bis zu HP, Status, UI und Save. Wo divergieren Regeln gewollt oder ungewollt?“
