# ROM-Hack-Editoren als Hinweise auf Spielsysteme (v1.0)

**Quellen (nur gelesen):** `D:\Projekte\simulation\project\docs\ROM_EDITOR_ANALYSIS_2026-10-19.md`, `AUREMON_GAME_SYSTEM_ATLAS_2026-10-19.md`, `RUNTIME_RESOURCE_DATAFLOW_2026-10-19.md`, `AUREMON_EDITOR_PROPOSAL_2026-10-19.md`.

**Befundqualität:** Grundlage sind dort dokumentierte statische Archiv-/README-/Konfigurationsinspektionen. Es wurden laut Bericht **keine** ROMs geöffnet und keine Editor-EXE interaktiv ausgeführt. Die folgenden Aussagen belegen dokumentierte Bearbeitungsflächen und plausibel ableitbare Datenbeziehungen, **nicht** exakte Original-Laufzeitalgorithmen. Versionsabhängige Angaben bleiben snapshotgebunden. Allgemeine Architekturvorschläge sind eigene Ableitungen, keine Beobachtungen.

## Porymap: Kartensystem als Komposition

Porymap bearbeitet Gen-3-Decomp-Projektdateien (pokeruby, pokeemerald, pokefirered); laut untersuchter Dokumentation nicht direkt die binäre ROM.

| Belegte Bearbeitungsfläche | Ableitbare Spielsystemfrage |
|---|---|
| Maps, Gruppen, Layout-ID, Größe, Rand, Tilesets | Wie bildet das Spiel den Weltgraphen, Maps und Layer ab? |
| 8x8-Pixel-Tilegrafiken → Metatiles → Layout | Wie sind Darstellung und Terrainattribute gekoppelt/getrennt? |
| Kollisionsarten, Höhen und Verhalten pro Metatile | Welcher physische Bewegungsmodus darf wohin? |
| Map Header (Wetter, Standort, Spezialregeln) | Welche ortsbezogenen Regelprofile werden geladen? |
| Verbindungen, Richtung, Offset, Zielmap, Mirror | Ist die Grenze gerichtet/beidseitig? Wie wird ein Rückweg validiert? |
| Objekt/NPC/Trigger/Warp/Schild/Hidden-Item-Events | Welche Definition triggert welchen autoritativen Runtime-Outcome? |
| Land-/Wasser-/Fishing-/Rock-Smash-Encounter-Slots | Wie werden Begegnungen aus Ort, Methode, Gewicht und Level ausgewählt? |
| Regionenübersicht | Ist das eine Projektion des Weltgraphs oder eigene Spiellogik? |

**Lehre:** Eine visuelle Karte sagt wenig über physische, interaktive oder narrative Semantik. Editor kann Eigenschaften anbieten, doch erst die Runtime entscheidet, was sie bewirken. Event-Undo/Redo laut Dokumentationsbefund nicht durchgängig: daraus folgen keine Aussagen zu unserem Code.

## Pokémon Game Editor (PGE): Spielregeln als Tabellengraph

PGE ist ein historisches GBA-ROM-Werkzeug mit ROM-spezifischen Offsets/INI-Tabellen. Der untersuchte Fund enthält ein Legacy-Programm und Dokumentation, aber keinen vollständigen Programmquellcode. Ein vollständiger Overworld-Editor ist laut README TODO, **nicht nachgewiesen**.

| Dokumentierte Bearbeitungsfläche | Ableitbare Relation |
|---|---|
| Species/Basiswerte/Typen/Fang- und Wachstumseigenschaften | SpeciesDefinition → MonsterInstance/Stats |
| Moves, PP, Typ, Ziel, Effekt, Priorität, Animation | MoveDefinition → EffectInterpreter/Kampfexecutor |
| Evolutionsdaten und -methoden | Species → EvolutionRule → Ziel-Species |
| Egg Moves, Tutor, TM/HM | Species × LearnMethod × Move |
| Items und Kompatibilität | Item/Move/Species und Wirkungsberechtigung |
| Trainer/Trainerklassen/-Teams | TrainerProfile → Party/AI-/Encounterprofil |
| Sprites/Icons/Footprints/Rufe (Export) | Species/Actor → Präsentationsressourcen |
| Dex/Starter/Trades/Frontier (teils unfertig) | optionale Gameplay-Features, nicht universale Notwendigkeit |

**Lehre:** Editor-Felder sind gute Kandidaten für einen Fachkatalog. Sie beweisen weder Programmklassen noch ob ein Effekt im Original tatsächlich so ausgeführt wird. ROM-Offsets sind Speicheradressierung eines Zielbuilds, keine engine-neutralen Geschäftsregeln.

## KM Editor: moderne Content- und Sicherheitsverträge

Laut Archivdokumentation sind mehrere moderne Pokémon-Spiele mit **unterschiedlicher** Kategorieabdeckung vorgesehen. Implementierungsflächen sind statisch sichtbar; UX-Livefunktion blieb ungeprüft.

| Dokumentierte Fläche | Ableitbare Prüfung |
|---|---|
| Species, Moves, Items, Trainers, Encounters | Stabile IDs, Feldtypen und referenzielle Konsistenz |
| Gifts, Trades, Shops, Static Encounters | Wer darf Outcome/Reward genau einmal oder mehrfach vergeben? |
| Raids, Rewards, Bosse und spielabhängige Profile | Contentvariante vs neue allgemeine Laufzeitregel |
| Modell-/Audio-/Texture-Viewer | Darstellung bindet Ressourcen, nicht Gameplay-Wahrheit |
| YAML-Dumps mit Formatversion, IDs, Source-Fingerprint und read_only | Sind Definitionen versioniert, rückverfolgbar und überschreibsicher? |
| Preflight, Validierungsabbruch bei Fehler, Change Sets | Können Daten vor Übernahme geprüft und rückgängig gemacht werden? |
| 3-Wege-Merge (Base/Left/Right) | Welche Felder wurden parallel unabhängig oder widersprüchlich geändert? |

**Lehre:** Diese Daten- und Änderungsverträge sind wertvoll, selbst wenn überhaupt kein Editor gebaut wird: Agenten erzeugen ebenso Datenänderungen und können gleichzeitige Änderungen überschreiben. Content darf nie die einzige ungesicherte Wahrheit sein.

## Was ROM-Editoren NICHT beweisen

- Exakte Update-/Renderreihenfolge, Speicherlayout aller Runtime-Objekte, Klassendiagramme und KI-Algorithmen.
- Ob eine dokumentierte Eigenschaft in jeder unterstützten Spielversion aktiv ist.
- Save-, Netzwerk-, Transaktions- oder Crash-Sicherheit der Originalspiele.
- Dass jedes sichtbare Editor-Feld ein eigenständiges Engine-System oder Programmklasse erfordert.
- Dass Datenänderung automatisch neue Fähigkeiten freischaltet. Neue Effekte brauchen einen vorhandenen Interpreter oder eine gezielte Erweiterung.

## Bestmögliche Nutzung bei kreativer Spieleentwicklung

1. Ein Feature im Editor als **Hinweis auf Datenfelder und Beziehungen** aufnehmen.
2. Den möglichen Runtime-Consumer benennen, ohne sein tatsächliches Innenleben zu behaupten.
3. Im eigenen Spiel die Kette Definition → Instanz → Consumer → Outcome → Save **nachweisen**.
4. Fehlende Inhalte von fehlenden Ausdrucksmöglichkeiten unterscheiden.
5. Nur die **abstrakten Regeln** übernehmen; keine geschützten Sprites, Töne, Monster, Texte, Karten oder ungeprüften Quellcodes übernehmen.

**Provenienz laut Ausgangsbericht:** Porymap (Qt/C++, LGPL-3.0), KM Editor (.NET/Tauri/React, GPL-3.0-only), PGE (Legacy/VB.NET, eigenständige Lizenzbedingungen). Archive und mitgelieferte Fremdassets können abweichende Rechte haben. Diese Notiz gibt keine Nutzungsfreigabe.
