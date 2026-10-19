# Praxiswissen: Auremon Runtime-Ressourcen und ROM-Hack-Editoren (v0.1)

Quelle (read-only): `D:\Projekte\simulation\project\docs\RUNTIME_RESOURCE_DATAFLOW_2026-10-19.md`, Stand 19.10.2026. Dort dokumentierte statische Inspektion, Node-Proben und Projekt-Gates; kein vollständiger sichtbarer Browser-/Kampagnentest.

**Evidenzgrenze:** Diese Quelle beschreibt die Auremon-Laufzeit. Sie ist **kein** direkter Funktionsvergleich der drei ROM-Hack-Editoren. Editor-spezifische Aussagen sind daraus nicht belegt und bleiben bis zur gesonderten Analyse offen.

## Wiederverwendbare Erkenntnisse

1. **Ressourcenkette:** Definition → referenzielle Validierung → Instanz/Regelinterpreter → Konsument/Szene → Outcome → persistenter State/Save → erneutes Laden. Jede Kante kann unabhängig fehlschlagen.
2. **Definition ≠ Instanz ≠ Zustand:** Species/Move/Item-Registries sind keine individuellen Monster, aktiven Projektile oder Inventarbestände. Laufzeit darf kanonische Definitionen nicht versehentlich mutieren.
3. **Autoritativer Owner:** Schaden, Welt-/Kollisionssicht und Save-Änderungen benötigen jeweils einen eindeutigen zuständigen Verarbeitungspfad. Zusätzliche Editoren oder Datenformate erzeugen keine zweite Wahrheit.
4. **Datenintegrität:** Referenzierte IDs, Typen, Mengen, Wertebereiche, Evolutionen, Drops, Warps, Spawnziele, Rezepte und Belohnungen müssen am Producer UND Consumer überprüft werden.
5. **Änderungsfolgen:** Datenfixes können bestehende Saves betreffen. Migration, ungültige Altwerte, doppelte Rewards, Retry, Abbruch, Crash und Reload gehören zur Prüfung.
6. **Kollision/World-Overlay:** Darstellung, Navigation und Interaktion müssen dieselbe wirksame Weltzustandsprojektion verwenden; sonst drohen visuelle Widersprüche und Softlocks.
7. **Zwei Kampfmodi:** Gemeinsame Daten und Battle-Math sind wiederverwendbar; rundenbasierte und Echtzeit-Ausführung können unterschiedliche Scheduling-, Ziel- und Interaktionsregeln besitzen.
8. **Seed und Replay:** Deterministischer Worldgen-Seed genügt nicht, wenn einzelne KI- oder Loot-Pfade nichtdeterministische Zufallsquellen verwenden.
9. **Content-Lücke ≠ Engine-Lücke:** Neue Quests, Regionen, Trainer oder Gegner können vorhandene Fähigkeiten konfigurieren; erst nachgewiesenes Ausdrucksdefizit rechtfertigt neue universelle Systeme.
10. **Renderer und Audio sind austauschbare Konsumenten:** Ein Grafikstilwechsel sollte nicht heimlich Gameplay-, Kollisions- oder Schadensregeln ändern.
11. **Editor zuletzt:** Vor einem Dateneditor müssen Content-IDs, Referenzintegrität, Runtime-Verarbeitung und Save-/Outcome-Roundtrips des jeweiligen Systems verstanden sein.

## Konkretes Beispiel aus dem Bericht

Vier Species-Drops verwiesen auf `perlkern`, registriert war `perlkorn`. Der neue Referenztest scheiterte zunächst; anschließend wurden vier IDs korrigiert und eine kontrollierte Alt-Save-Migration ergänzt. Node-Smoke und Projektvalidator bestanden. **Nicht belegt** ist dadurch ein vollständiger sichtbarer Loot-Pickup-End-to-End-Test.

## Fragen, die ein Mensch dem Agenten stellen sollte

- Wo wird die Ressource definiert, wer erzeugt sie, wer konsumiert sie, was sieht der Spieler?
- Welche ID- und Wertefehler können entlang der Kette auftreten?
- Wer ist Owner des wirksamen Zustands, und gibt es eine zweite widersprüchliche Sicht?
- Was passiert bei Abbruch, Retry, Neustart, Speichern und Laden?
- Fehlt wirklich eine Systemfähigkeit oder nur ein weiterer Inhalt?
- Welche Beweise stammen aus Unit/Node-Tests, welche aus echter Runtime, welche aus Nutzerbeobachtung?

## Für spätere ROM-Editor-Rekonstruktion

Pro Editor getrennt nachweisen: unterstützte Spielversionen/ROMs, tatsächliche bearbeitbare Tabellen/Felder, Pointer-/Bank-/Adressierungsmodell, Maps/Events/Warps, Tiles/Sprites/Animationen, Attacken/Stats/Items/Trainer/AI, Skripte, Kompression, Repacking, Checksums, Laufzeitverbrauch der geänderten Daten und Risiken. **Keine** Editor-Fähigkeit ohne tatsächliche Tool-/Datei-/ROM-Evidenz behaupten.

## Anwendung auf den Entwicklungszyklus

Creative → Gesamtbild (Definition→Outcome-Ketten inventarisieren) → neue Erkenntnisse kreativ nutzen → zweites Gesamtbild → einzelne Daten-/Runtime-Grenzen vertiefen → Agent testet → User testet → kleinste Konsolidierung → Creative. Das ist eine Erkenntnismethode, keine Pflicht, alle Katalogsysteme zu bauen.
