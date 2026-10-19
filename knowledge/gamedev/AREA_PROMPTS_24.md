# Bereichs-Prompts — Game Systems Catalog v1.0

Diese 24 Prompts sind **Ergänzungen** zu `PROMPTS.md`. Für die frühe kreative Phase nicht alle gleichzeitig abarbeiten. Bei Gesamtbild zuerst nur `A` in PROMPTS.md verwenden; erst nach Priorisierung genau die betroffenen Bereiche vertiefen.

## Generische Spielregel für alle Bereiche

Starte im Projekt mit Root/Anweisungen/Git-Status und relevanten Verträgen. Nutze den Bereichseintrag aus dem passenden Kapitel 01–06 als **Fragenkatalog, nicht als Implementierungsauftrag**. Untersuche vorhandene Daten, tatsächliche Laufzeitkonsumenten, Zustände, Abhängigkeiten, Fehlerpfade und nur die relevanten Tests. Kennzeichne nach `SYSTEM_AUDIT_MATRIX.md`. Berichte menschlich lesbar und nenne Beweise. **Produktcode bleibt während der Analyse read-only.** Schreibe Ergebnisse nur in erlaubte Berichtsbereiche.

## 01 · Runtime/Lebenszyklus

> Untersuche Katalogbereich 01 (Runtime/Lebenszyklus) am vorhandenen Spiel. Verfolge Startup, Game Loop, Tick-Reihenfolge, Pausen, Szenenwechsel und Cleanup; prüfe unterschiedliche FPS und Neustart. Trenne vorhandene Fähigkeiten, fehlende Inhalte, echte Funktionslücken und nicht benötigte Varianten. Nenne die kleinste sinnvolle nächste Aktion mit Nachweis.

## 02 · Daten/IDs

> Untersuche Katalogbereich 02 (Daten/IDs) am vorhandenen Spiel. Verfolge eine Monster-, Item- und Mapressource von Definition und ID-Auflösung bis tatsächlichem Outcome und Save; teste fehlende und doppelte IDs. Trenne vorhandene Fähigkeiten, fehlende Inhalte, echte Funktionslücken und nicht benötigte Varianten. Nenne die kleinste sinnvolle nächste Aktion mit Nachweis.

## 03 · Zustände/Events

> Untersuche Katalogbereich 03 (Zustände/Events) am vorhandenen Spiel. Zeige Command, Berechtigungsprüfung, zuständigen State-Owner, Änderungen und Folgeevents. Prüfe Retry/Abbruch/doppelte Zustellung. Trenne vorhandene Fähigkeiten, fehlende Inhalte, echte Funktionslücken und nicht benötigte Varianten. Nenne die kleinste sinnvolle nächste Aktion mit Nachweis.

## 04 · Welt/Maps

> Untersuche Katalogbereich 04 (Welt/Maps) am vorhandenen Spiel. Prüfe Mapgraph, Tiles/Layer, wirksame Kollisionssicht, NPC-Spawns, Warps, Backtracking und persistente World-Overlays. Trenne vorhandene Fähigkeiten, fehlende Inhalte, echte Funktionslücken und nicht benötigte Varianten. Nenne die kleinste sinnvolle nächste Aktion mit Nachweis.

## 05 · Entities/Interaktionen

> Untersuche Katalogbereich 05 (Entities/Interaktionen) am vorhandenen Spiel. Prüfe Definition/Prefab, Spawn, Komponenten, gültige Interaktion, Despawn und Cleanup an zwei unterschiedlichen Objekten. Trenne vorhandene Fähigkeiten, fehlende Inhalte, echte Funktionslücken und nicht benötigte Varianten. Nenne die kleinste sinnvolle nächste Aktion mit Nachweis.

## 06 · Charaktere/Monster

> Untersuche Katalogbereich 06 (Charaktere/Monster) am vorhandenen Spiel. Vergleiche Artdefinition, individuelle Monster, NPC/Profile, Stats, Teamwechsel, Entwicklung und die zu speichernden Eigenschaften. Trenne vorhandene Fähigkeiten, fehlende Inhalte, echte Funktionslücken und nicht benötigte Varianten. Nenne die kleinste sinnvolle nächste Aktion mit Nachweis.

## 07 · Bewegung/Navigation

> Untersuche Katalogbereich 07 (Bewegung/Navigation) am vorhandenen Spiel. Teste Player, NPC und Follower gegen dieselben physikalischen Grenzen, verschiedene Terrainprofile und dynamische Hindernisse. Trenne vorhandene Fähigkeiten, fehlende Inhalte, echte Funktionslücken und nicht benötigte Varianten. Nenne die kleinste sinnvolle nächste Aktion mit Nachweis.

## 08 · KI/Simulation

> Untersuche Katalogbereich 08 (KI/Simulation) am vorhandenen Spiel. Rekonstruiere für einen Gegner Wahrnehmung → Entscheidung → Navigation/Attacke → Feedback, einschließlich Zielverlust und KO. Trenne vorhandene Fähigkeiten, fehlende Inhalte, echte Funktionslücken und nicht benötigte Varianten. Nenne die kleinste sinnvolle nächste Aktion mit Nachweis.

## 09 · Kampf/Effekte

> Untersuche Katalogbereich 09 (Kampf/Effekte) am vorhandenen Spiel. Verfolge dieselbe Attackendefinition in allen Kampfarten bis zu Schaden, Status, Kosten, KO, Belohnung und UI. Trenne vorhandene Fähigkeiten, fehlende Inhalte, echte Funktionslücken und nicht benötigte Varianten. Nenne die kleinste sinnvolle nächste Aktion mit Nachweis.

## 10 · Inventar/Wirtschaft

> Untersuche Katalogbereich 10 (Inventar/Wirtschaft) am vorhandenen Spiel. Teste Itemquelle → Aufnahme → Stapel/Verbrauch → Transaktion → Save; zusätzlich falsche IDs, volle Kapazität und doppelte Belohnung. Trenne vorhandene Fähigkeiten, fehlende Inhalte, echte Funktionslücken und nicht benötigte Varianten. Nenne die kleinste sinnvolle nächste Aktion mit Nachweis.

## 11 · Fortschritt

> Untersuche Katalogbereich 11 (Fortschritt) am vorhandenen Spiel. Untersuche XP, Level, Learnsets, Evolution, Unlocks und Balanceprofile bei Schwellen und mehrfachen Levelanstiegen. Trenne vorhandene Fähigkeiten, fehlende Inhalte, echte Funktionslücken und nicht benötigte Varianten. Nenne die kleinste sinnvolle nächste Aktion mit Nachweis.

## 12 · Story/Quests

> Untersuche Katalogbereich 12 (Story/Quests) am vorhandenen Spiel. Verfolge einen Dialog-/Questtrigger über Conditions, Outcome, Worldstate, einmalige Rewards und Reload; teste falsche Reihenfolgen. Trenne vorhandene Fähigkeiten, fehlende Inhalte, echte Funktionslücken und nicht benötigte Varianten. Nenne die kleinste sinnvolle nächste Aktion mit Nachweis.

## 13 · Animation

> Untersuche Katalogbereich 13 (Animation) am vorhandenen Spiel. Prüfe Zustände, Richtung, Clip-/Statewechsel, Trefferfenster, Unterbrechung, KO und Synchronisation mit dem Gameplay. Trenne vorhandene Fähigkeiten, fehlende Inhalte, echte Funktionslücken und nicht benötigte Varianten. Nenne die kleinste sinnvolle nächste Aktion mit Nachweis.

## 14 · Rendering/Kamera

> Untersuche Katalogbereich 14 (Rendering/Kamera) am vorhandenen Spiel. Rekonstruiere Gameplaystate → sichtbare Objekte → Layer/Kamera/Material/VFX; prüfe Occlusion und Abweichungen von Collision. Trenne vorhandene Fähigkeiten, fehlende Inhalte, echte Funktionslücken und nicht benötigte Varianten. Nenne die kleinste sinnvolle nächste Aktion mit Nachweis.

## 15 · Audio

> Untersuche Katalogbereich 15 (Audio) am vorhandenen Spiel. Verfolge Treffer-/UI-/Umgebungsereignisse bis zur hörbaren Ausgabe, Mixer, Pause, Fokusverlust und Szenenwechsel. Trenne vorhandene Fähigkeiten, fehlende Inhalte, echte Funktionslücken und nicht benötigte Varianten. Nenne die kleinste sinnvolle nächste Aktion mit Nachweis.

## 16 · UI/UX/Input

> Untersuche Katalogbereich 16 (UI/UX/Input) am vorhandenen Spiel. Teste reale Benutzeraktionen mit Tastatur und soweit verfügbar Controller, Modal-/Fokusstack, Fehlermeldungen und angezeigtes Ergebnis. Trenne vorhandene Fähigkeiten, fehlende Inhalte, echte Funktionslücken und nicht benötigte Varianten. Nenne die kleinste sinnvolle nächste Aktion mit Nachweis.

## 17 · Persistenz

> Untersuche Katalogbereich 17 (Persistenz) am vorhandenen Spiel. Prüfe pro Savefeld Owner, Schreiben, Laden, Legacy-Migration, unterbrochenen Save und Retry/Quest-/Loot-Claims. Trenne vorhandene Fähigkeiten, fehlende Inhalte, echte Funktionslücken und nicht benötigte Varianten. Nenne die kleinste sinnvolle nächste Aktion mit Nachweis.

## 18 · Generierung

> Untersuche Katalogbereich 18 (Generierung) am vorhandenen Spiel. Teste Seeds, gültige Raum-/Spawn-/Exit-Geometrie, Wiederholbarkeit, World-Overlays, Instanzeintritt und Rückkehr. Trenne vorhandene Fähigkeiten, fehlende Inhalte, echte Funktionslücken und nicht benötigte Varianten. Nenne die kleinste sinnvolle nächste Aktion mit Nachweis.

## 19 · Netzwerk

> Untersuche Katalogbereich 19 (Netzwerk) am vorhandenen Spiel. Prüfe zuerst, ob Multiplayer zum Scope gehört; falls ja, Autorität, Command-Transport, Replikation, Reconnect und Konflikte. Trenne vorhandene Fähigkeiten, fehlende Inhalte, echte Funktionslücken und nicht benötigte Varianten. Nenne die kleinste sinnvolle nächste Aktion mit Nachweis.

## 20 · Performance

> Untersuche Katalogbereich 20 (Performance) am vorhandenen Spiel. Miss reproduzierbare Framezeit-, Speicher- oder Ladespitzen und teste kleinste Verbesserungen ohne Gameplayänderung. Trenne vorhandene Fähigkeiten, fehlende Inhalte, echte Funktionslücken und nicht benötigte Varianten. Nenne die kleinste sinnvolle nächste Aktion mit Nachweis.

## 21 · Tests/Debug

> Untersuche Katalogbereich 21 (Tests/Debug) am vorhandenen Spiel. Vergleiche Quellcodebefund, automatische Tests, echten Gameplaypfad und Nutzerbeobachtung; dokumentiere offene Beweisgrenzen. Trenne vorhandene Fähigkeiten, fehlende Inhalte, echte Funktionslücken und nicht benötigte Varianten. Nenne die kleinste sinnvolle nächste Aktion mit Nachweis.

## 22 · Assets/Content

> Untersuche Katalogbereich 22 (Assets/Content) am vorhandenen Spiel. Prüfe eine Grafik-/Audioressource von Ursprung/Lizenz über Import/IDs bis Runtime-Darstellung und fehlendem Asset. Trenne vorhandene Fähigkeiten, fehlende Inhalte, echte Funktionslücken und nicht benötigte Varianten. Nenne die kleinste sinnvolle nächste Aktion mit Nachweis.

## 23 · Build/Release

> Untersuche Katalogbereich 23 (Build/Release) am vorhandenen Spiel. Prüfe frischen Build/Package, Start im Zielsystem, Assetvollständigkeit und Save nach Neuinstallation/Update. Trenne vorhandene Fähigkeiten, fehlende Inhalte, echte Funktionslücken und nicht benötigte Varianten. Nenne die kleinste sinnvolle nächste Aktion mit Nachweis.

## 24 · Gamefeel/Kernloop

> Untersuche Katalogbereich 24 (Gamefeel/Kernloop) am vorhandenen Spiel. Spiele Ziel → Entscheidung → Handlung → Feedback → Belohnung und trenne technische Funktion von Fairness, Verständlichkeit und Spaß. Trenne vorhandene Fähigkeiten, fehlende Inhalte, echte Funktionslücken und nicht benötigte Varianten. Nenne die kleinste sinnvolle nächste Aktion mit Nachweis.

## Nach der Bereichsprüfung

Wenn ein echter Defekt bestätigt ist: Mit `PROMPTS.md` Abschnitt G die kleinste autorisierte Änderung beauftragen, danach gezielte Regression und reale Produktgrenze. Für neue kreative Mechaniken Abschnitt B oder H verwenden. Keine ungeprüfte automatische Total-Konsolidierung.
