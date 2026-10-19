# Game Systems Handbook — menschlicher Katalog (v1.0)

**Zweck:** Menschen einen verständlichen, engine- und genreunabhängigen Überblick geben, welche Systeme Spiele besitzen können; Agenten gezielt nachprüfbare Fragen stellen. **Kein** zweites Governance-Verfahren, keine technische Pflicht-Architektur, kein automatischer Implementierungsplan.

## So nutzt du den Katalog

**Während Creative:** Den Agenten frei Mechaniken entwickeln und prüfen lassen. Nicht sämtliche 24 Bereiche als Pflichten übergeben.

**Nach dem ersten spielbaren Abschnitt:** `PROMPTS.md` → **A** (Gesamtbild). Neue Entdeckungen und Probleme an einen Creative Agent mit **B** geben.

**Wenn das grobe Spiel steht:** **C** (zweites Gesamtbild), anschließend nur priorisierte Bereiche mit `AREA_PROMPTS_24.md` vertiefen. Danach **E** (AI-Spieltest), **F** (User-Spieltest), **G** (konsolidieren inkl. kreativer Fixes) und **H** (Übergabe) nutzen. Zyklus erneut starten.

**Ergebnisformat:** `SYSTEM_AUDIT_MATRIX.md` erklärt Status, Nachweisstufen, Definition→Outcome-Kette, Ownership, negative Fälle und die Unterscheidung zwischen fehlendem Inhalt und fehlender Fähigkeit.

## Das zentrale Denkmodell

```text
CREATIVE IDEE / SPIELERABSICHT
  → statische Definitionen (Monster, Move, Item, Map, Quest)
  → geprüfte ID-/Assetreferenzen
  → konkrete Instanz (Monster, NPC, Projektil, Dungeonlauf)
  → Runtime-System / Regelinterpreter
  → erlaubte Zustandsänderung + Ergebnis
  → sichtbare / hörbare Präsentation
  → persistierter Zustand, falls relevant
  → Reload / erneuter Runtime-Verbrauch
```

**Definition ≠ Instanz ≠ veränderlicher Zustand ≠ Darstellung.** Ein Datenobjekt ist kein Beweis für implementiertes Gameplay. Wenn eine Karte sichtbar ist, muss Kollision/Navigation deswegen noch nicht stimmen. Ein Game-System muss nicht aus einer einzigen Klasse bestehen. Arrays, Dictionaries, JSON, Engine-Ressourcen, SQLite und binäre Formate sind **unterschiedliche Speichermittel** und keine universelle Hierarchie.

## Die 24 vertieften Systembereiche

| Bereich | Thema | Datei |
|---|---|---|
| 01–04 | Runtime, Daten/IDs, Events, Welt/Maps | `01_GRUNDLAGEN_LAUFZEIT_DATEN_WELT.md` |
| 05–09 | Entities, Charaktere, Bewegung, KI, Kampf | `02_ENTITIES_BEWEGUNG_KI_KAMPF.md` |
| 10–12 | Items, Wirtschaft, Progression, Quests | `03_ITEMS_PROGRESS_STORY.md` |
| 13–16 | Animation, Rendering/Kamera, Audio, UI/Input | `04_PRESENTATION_INPUT.md` |
| 17–19 | Save/Migration, Generierung, Netzwerk (optional) | `05_PERSISTENZ_GENERIERUNG_NETZWERK.md` |
| 20–24 | Performance, Testing, Assetpipeline, Build, Gamefeel | `06_QUALITAET_PRODUKTION_GAMEFEEL.md` |

In **jedem** Bereich findest du: Zweck und Beispiel, mögliche Varianten, Daten/Runtimezustand, Verarbeitungskette, Beziehungen, Fehlerbilder, Tests und eine einfache Formulierung für den Agenten.

## Wissensquellen und Praxisbeispiele

- `RUNTIME_DATAFLOW_LESSONS.md`: Auremon-Analyse der tatsächlichen Daten- und Laufzeitpfade (Definition, Instanz, Consumer, Outcome, Save) und deren Nachweisgrenzen.
- `ROM_EDITOR_SYSTEM_INSIGHTS.md`: Porymap, Pokémon Game Editor (PGE), KM Editor — Datenmodelle, Karten, Regeln, Sicherheitsmechanismen, aber **keine** angeblich bewiesene Original-Runtime.
- `SYSTEM_AUDIT_MATRIX.md`: Statusmatrix und vollständige Prüfung eines Ressourcensystems.
- `PROMPTS.md`: acht Phasenprompts für die iterative Entwicklung.
- `AREA_PROMPTS_24.md`: 24 spezifische, kopierbare Bereichsfragen.

**Quellnachweise (schreibgeschützte Projektberichte):** `D:\Projekte\simulation\project\docs\RUNTIME_RESOURCE_DATAFLOW_2026-10-19.md` und `ROM_EDITOR_ANALYSIS_2026-10-19.md` sowie `AUREMON_GAME_SYSTEM_ATLAS_2026-10-19.md`. Ihre Beobachtungsgrenzen gelten weiterhin; Aussagen über Originalspiele nicht daraus erfinden.

## Was man beim Prompten vermeiden sollte

- „Implementiere alle Systeme aus der Liste.“ → Stattdessen vorhandene Produktmechaniken auf echte Lücken prüfen.
- „Refactore alles nach Best Practice.“ → Stattdessen nachweisbare Ursachen und kleinste reversible Verbesserung.
- „Ein Test ist grün, also ist das Gameplay vollständig.“ → Testebene und echtes Benutzerergebnis unterscheiden.
- „Jeder neue Datentyp braucht eine Klasse und einen Editor.“ → Nach vorhandenen Registries, Komponenten und Interpretern fragen.
- „Die ROM-Editoren beweisen die Originalengine.“ → Sie liefern Belege zu bearbeitbaren Feldern/Dateien, nicht automatisch zu Laufzeitklassen oder Formeln.

## Verbindung zu vorhandenen Plugins

`agent-workflow` bestimmt weiterhin die Rolle (Creative, RORE, APC, Core-First, independent verification und Weiterentwicklung). Der bestehende `gamedev-jit-skills-v0.3.0.zip`-Router bleibt **unverändert** und liefert technische Engine-/Disziplinverfahren auf Bedarf. Dieser Katalog ist eine separat lesbare **menschliche Wissensschicht**. Kein automatisches Laden aller Dateien, keine Änderung an anderen Plugins und keine JIT-Installation durch diese Dokumentation.

**Stand:** Nachschlagewerk v1.0; alle 24 Bereiche dokumentiert. Die Reife der **hier beschriebenen Beispiele** darf nicht mit der Vollständigkeit eines realen Spiels verwechselt werden.
