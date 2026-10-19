# Teil I — Die unsichtbare Spielmaschine (Bereiche 01–04)

**Für Menschen:** Jede Karte, Figur oder Attacke ist am Ende eine Kombination aus Daten, aktivem Zustand und Regeln. Die Grafik zeigt nur, was daraus entsteht. Keine der folgenden Umsetzungen ist für jedes Genre verpflichtend.

## 01 · Runtime & Lebenszyklus

**Wozu?** Die Runtime sorgt dafür, dass das Spiel startet, Eingaben verarbeitet, die Welt fortschreibt und wieder sauber beendet. Beispiel: Ein Monster geht nur weiter, wenn Zeit verstreicht und seine Bewegung aktualisiert wird.

**Bausteine / Varianten:** Bootstrap; Hauptschleife (Game Loop); variable Renderfrequenz und optional fester Simulationsschritt; Szenen- oder Moduswechsel; Pause; Erzeugen/Entfernen aktiver Objekte; Laden/Entladen von Ressourcen; Fokusverlust; Fehler- und Shutdownpfad. Browser, Godot oder Unreal stellen große Teile bereits bereit.

**Daten und Zustand:** Spielkonfiguration, Zeitfaktor, aktive Szene, Update-Reihenfolge, Warteschlangen, Objekt-IDs, geladene Ressourcen, Timer; meistens flüchtig. Zum Save gehören nur gezielt ausgewählte für die Fortsetzung relevante Zustände.

**Laufzeitkette:** Start → Content/Assets laden → Zustand initialisieren → Eingabe lesen → gültige Aktionen prüfen → Simulation (mit delta time / fixed tick) → Ereignisse/Outcomes → Darstellung → nächster Frame → Pause/Speichern/Beenden. Nicht jede Engine verwendet exakt diese Reihenfolge.

**Verträge/Beziehungen:** Input (16) liefert Aktionen; Welt/Entities (04–05) werden aktualisiert; KI (08) und Kampf (09) benötigen Zeit; Animation/Rendering (13–14) konsumieren Ergebnisse; Save (17) benötigt einen konsistenten Zustand.

**Häufige Fehler:** Bildrate bestimmt Laufgeschwindigkeit; Timer laufen während Pause; Szene lädt Ressourcen mehrfach; Spawn wird im selben Frame ungewollt wieder gelöscht; Neustart hinterlässt Listener; Fokusverlust hält Tasten gedrückt.

**Prüfen:** Bewegung bei unterschiedlichen FPS; Pause/Resume; schneller Kartenwechsel; mehrfaches Neustarten; zeitgleich Spawn/Despawn; Shutdown nach Speicherfehler. **Nicht nötig:** eine zweite selbstgebaute Game Loop, wenn die Engine eine belastbare besitzt.

**An den Agenten:** „Zeige mir, wer Zeit und Update-Reihenfolge besitzt, wie Pause und Szenenwechsel funktionieren und welche sichtbaren Fehler bei FPS-Wechsel auftreten können. Teste das gezielt.“

## 02 · Daten, IDs und Ressourcen

**Wozu?** Gemeinsam genutzte Fakten sollen nur einmal festgelegt sein. Beispiel: Alle wilden und gefangenen Exemplare derselben Monsterart verwenden eine Species-Definition, behalten aber jeweils eigenen Level und HP.

**Begriffe:** *Definition* = wiederverwendbare Vorlage; *Instanz* = konkretes Exemplar; *Runtime-Zustand* = momentaner Wert; *Persistenz* = gespeicherter Fortschritt; *Asset* = Bild/Ton/Modell/Material oder andere Ressource; *Registry* = Nachschlagetabelle nach stabiler ID; *Schema* = erlaubte Felder und Werte.

**Daten / Speicher:** `speciesId`, `moveId`, `itemId`, `mapId`, `instanceId`, `assetRef`, Verweise und Versionsfelder. JSON/YAML, Code-Registries, Engine-Ressourcen oder relationale Tabellen sind Varianten; Arrays, Maps und Sets dienen als **Laufzeitstrukturen**, nicht automatisch als persistente Datenbanken.

**Laufzeitkette:** Content lesen → Schema/IDs prüfen → Registry aufbauen → Definition per ID auflösen → Instanz erzeugen → Gameplay-System interpretiert Regeln → gültige Zustandsänderung → relevante Instanzdaten speichern. Ein Loader allein beweist keine tatsächliche Verarbeitung.

**Verträge/Beziehungen:** Alle Systeme 01–24 lesen Daten; ein definierter Besitzer verantwortet die kanonische Definition und ggf. die persistente Zustandsart. Mehrere Leser sind erlaubt, konkurrierende Schreiber müssen geregelt sein.

**Häufige Fehler:** fehlende Drop-ID, doppelte ID, fehlender Spriteref, unzulässige Evolutionsschleife, Save referenziert umbenannte Species, gleiche Definition wird von einer Instanz versehentlich mutiert.

**Prüfen:** ID-Graph auflösen; negative Fixtures (unbekannte ID, falscher Datentyp, Werte außerhalb Grenzen); Einfügen und Löschen; Save-Migration; einen konkreten Producer→Consumer-Pfad im echten Spiel verfolgen.

**An den Agenten:** „Verfolge eine komplette Ressource vom Datensatz bis zum Ergebnis. Nenne Erzeuger, Konsumenten, Owner, IDs, Fehlerverhalten und Savefolgen.“

## 03 · Zustand, Aktionen und Ereignisse

**Wozu?** Ein Spiel muss unterscheiden, was gerade gilt, was jemand *versucht*, und was nach einer gültigen Aktion *passiert ist*. Beispiel: „Spieler versucht Truhe zu öffnen“ ist nicht identisch mit „Truhe geöffnet und Beute vergeben“.

**Varianten:** direkte Methodenaufrufe, Zustandsmaschinen, Commands, Domain Events, Event Queue, Message Bus; nicht automatisch alles zusammen einführen. Zustandsübergänge können `idle → chasing → attacking` oder `quest_open → completed → reward_claimed` lauten.

**Daten und Zustand:** Entity-/Quest-/Kampfstatus, Event-Typ, Actor-ID, Ziel-ID, Zeit/Sequenz, Korrelation/Claim-ID, Fehlergrund; Eventlog nur wenn Replay/Debug/Netzwerk konkret benötigt wird.

**Laufzeitkette:** Command → Berechtigungen/Voraussetzungen → autoritativer Owner → atomare Zustandsänderung → Outcome/Event → UI/Audio/Quest reagieren → optional speichern. Ereignisse beschreiben Änderungen; das Event allein ist nicht zwingend der zuständige State.

**Verträge/Beziehungen:** Kampf (09), Quest (12), Inventar (10), Welt (04), Save (17). Eventreihenfolge und Mehrfachzustellung sind wichtig, wenn Belohnungen/Transaktionen beteiligt sind.

**Häufige Fehler:** Dialog vergibt zweimal Item, Listener bleibt nach Szenenwechsel aktiv, Animation setzt Gameplayzustand eigenständig, Event verläuft vor Validierung, Race im Gameover, unbekannte Event-IDs verschwinden still.

**Prüfen:** gleiche Aktion zweimal; Abbruch zwischen Prüfung und Änderung; Wiederholung nach Reload; Fehler beim Persistieren; zwei konkurrierende Auslöser; Event-Listener entfernen. Spezifische Idempotenz-/Transaktionsregeln nur dort, wo erforderlich.

**An den Agenten:** „Finde die autoritativen Zustandsbesitzer. Dokumentiere Commands, Guards, Übergänge und Outcomes; teste Wiederholung, Abbruch und Reload.“

## 04 · Welt, Maps und Raumübergänge

**Wozu?** Die Welt ist mehr als ein Bild: Sie definiert, *wo* Bewegung, Begegnung, Interaktion und Übergänge möglich sind. Beispiel: Eine Tür verbindet zwei Karten; eine Waldkachel kann zugleich Grasgrafik, Kollision und Begegnungsregel besitzen.

**Begriffe / Varianten:** Weltgraph (Regionen/Karten); Map-/Chunkdaten; Tiles, Metatiles, Terrain, Layer; Collision/Passability; Höhen und Bewegungsprofile; Spawns; Warps/Map-Connections; Instanzen; authored vs prozedural; World-Overlays durch Spielerhandlungen.

**Daten:** `mapId`, Bounds, Layer, TilesetRef, Terrain-/BehaviorTags, CollisionProfile, Spawnpunkte, Trigger, `from/to`-Verbindungen, Bedingungen und Rückkehranker. Prozedurale Maps speichern ggf. Seed und persistente Abweichungen statt jedes Tile.

**Laufzeitkette:** Karte/Seed → Basisgeometrie und Tileverhalten → erlaubte gespeicherte Weltänderungen → **wirksame Weltansicht** → Rendering, Passierbarkeit, Navigation, Interaktion, Spawns → Übergang mit gültigem Ziel/Rückkehr. Dieselbe Sicht ist für alle Konsumenten wichtig.

**Verträge/Beziehungen:** Bewegung (07), KI (08), Kampfgebiete (09), Quests (12), Rendering (14), Generierung (18), Save (17). Ein Warp ist eine räumliche und häufig auch eine Zustands-Transaktion.

**Häufige Fehler:** Tile sieht begehbar aus, blockiert aber; Karte erreicht Sackgasse/Softlock; nur eine von zwei Richtungen verbunden; Spawn liegt im Hindernis; gespeicherter Brückenbau wird nicht in Pathfinding übernommen; Companion teleportiert.

**Prüfen:** grafische, physische und Navigationssicht derselben Zelle; Ein-/Ausgang und Rückweg; Spawnlegalität für alle Bewegungsprofile; Türen bei geänderten Questflags; Reload nach Weltänderung; erreichbare Pflichtziele.

**ROM-Referenz:** Porymap zeigt getrennte Map-Layouts, Metatile-Verhalten, Kollision, Eventobjekte, Headerdaten und Kartenverbindungen. Es beweist damit bearbeitbare *Datenverträge*, nicht die exakten Interna der Original-Engine.

**An den Agenten:** „Zeige Weltgraph, effektive Tile-Abfrage, Warp-/Spawn-Verträge und Unterschiede zwischen Bild, Kollision und Navigation. Prüfe Rückwege und Softlocks.“
