# Teil VI — Verlässlichkeit, Produktion und Spielerfahrung (Bereiche 20–24)

## 20 · Performance und Ressourcenbudgets

**Wozu?** Selbst korrektes Gameplay kann durch Framedrops, Speicherlecks, lange Ladezeiten oder zu viele KI-Berechnungen unspielbar werden.

**Varianten:** Profiler, CPU/GPU-Budgets, Pooling, Culling/LOD, Chunk-/Assetstreaming, Job-Systeme, Cache, Update-Throttling, Instancing. Optimierungen erst auf Messbefund stützen.

**Daten/Zustand:** Framezeiten und P95/P99, Speicherverbrauch, Entitycounts, Draw Calls, Updatefrequenzen, Cache Hit/Miss, Ladezeiten, Testhardware/-version.

**Verarbeitung:** Nutzer-/Runtime-Szenario reproduzieren → Messpunkte/Profiling → Hotspot und Ursache finden → kleine gezielte Änderung → selben Test wiederholen → auf Nebenwirkungen prüfen.

**Beziehungen:** Loop (01), Navigation/KI (07–08), Rendering (14), Audio (15), Generator (18), Assets (22).

**Fehler:** scheinbar optimierte Logik verändert Trefferzeit; Culling deaktiviert Gameplay; Pooling lässt alten Zustand stehen; unnötige asynchrone Laderace; kein nachvollziehbares Vorher/Nachher.

**Tests:** Leerlauf, viele Akteure, Szenenwechsel, längere Laufzeit, schwächere Zielhardware; Profil vor und nach Eingriff; Regression von Zeit/Gameplay.

**Prompt:** „Miss den konkreten Freeze/Hotspot mit reproduzierbarem Szenario, leite die Ursache ab und teste die kleinste Änderung gegen dieselben Gameplayregeln.“

## 21 · Tests, Debugging und Beobachtbarkeit

**Wozu?** Ein bestehendes System ist nur soweit bestätigt, wie Beweise es tragen. Codeexistenz, Smoke-Test, simulierter Host, UI-Screenshot und echter Spieltest haben unterschiedliche Aussagekraft.

**Varianten:** Schema-/Referenztests; Unit; Integration; Simulation mit fixem Seed; Runtime Smoke; UI/Controller-Tests; manuelle Spielerbeobachtung; Regression; Fuzzing/Property Tests; Telemetrie.

**Daten:** Testfall-ID, Revision, Plattform, Seed, Fixture, Schritte, erwartetes/beobachtetes Resultat, Evidenzort, Grenzen, pass/fail/inconclusive.

**Laufzeit:** bekannte Anforderungen/Bugs → kleiner isolierter Test → tatsächliche relevante Schnittstelle ausüben → Ergebnis vergleichen → Belege sichern → negative Randfälle → Produkt-/Nutzerpfad nachprüfen.

**Beziehungen:** alle Systeme; eigene Testhooks/Fixtures dürfen Produktzustand nicht korrumpieren.

**Fehler:** „PASS“ nur weil Datei existiert; Screenshot ohne Interaktion; Mock beweist echte Hostintegration nicht; Test verändert Nutzer-Spielstand; keine Reproduktion von Zufall; Flaky Test wird ignoriert.

**Tests:** Defekt zuerst reproduzieren, negative Fixture; bei Gameplay mindestens Ergebnis und Zustand nach realer Aktion prüfen; Save/Reload separat; Erkenntnisse nach Evidenzstärke benennen.

**Prompt:** „Ordne jeden Befund statisch, automatisiert, real-runtime oder user-getestet ein. Teste die kleinste Grenze und deklariere alles Ungeprüfte ausdrücklich.“

## 22 · Asset- und Content-Pipeline

**Wozu?** Ressourcen entstehen als Rohdaten, werden importiert/transformiert und zur Laufzeit geladen. Ein Sprite im Ordner ist erst dann spielbar, wenn seine Referenzen und Verbraucher korrekt sind.

**Varianten:** prozedurale Grafik/Sounds; PNG/Atlas; Mesh/Material/Rig; Audiofiles; Engine-Import; Build-Time-Kompilierung; Hot Reload; Lokalisierung; DLC/Mods. Ein eigenes Assetformat ist optional.

**Daten:** SourceAssetId, Lizenz/Herkunft, ImportSettings, Metadaten, Version/Hash, kompilierte ResourceId, Atlas/Clip/Cue-Referenzen, Plattformvarianten.

**Laufzeit:** originäre Quelle → Import/Build → Validierung → Registrierung/Packaging → Load/Cache → Rendering/Audio/Animation → Unload; die Spielregeln sollten stabile semantische IDs nutzen statt Dateinamenlogik.

**Beziehungen:** Daten (02), Entities (05), Animation (13), Rendering (14), Audio (15), Build (23).

**Fehler:** Ressource fehlt im Release; Sprite falsch skaliert und Hitbox gekoppelt; Lizenz unklar; Grafikaustausch ändert Spielregel; veralteter Atlas; Import zerstört Referenzen; Assets werden nie entladen.

**Tests:** Asset-ID-Auflösung, eine echte Import→Runtime-Probe, fehlende Datei, Rechte-/Provenienzprüfung, Releasepaket und Rückwärtskompatibilität. Bei einem Spiel mit rein prozeduralem Canvas/WebAudio noch keine aufwendige Dateipipeline erfinden.

**ROM-Hinweis:** Porymap unterscheidet Tiles/Metatiles/Paletten; KM Editor bietet dokumentierte Model-/Audio-/Texture-Ansichten, aber keine generische Erstellung vollständiger Animationen und Geometrie.

**Prompt:** „Verfolge ein konkretes Bild und einen Ton von Quelle bis tatsächlicher Darstellung; prüfe Lizenz, ID, Import, Ladefehler und Stilunabhängigkeit der Regeln.“

## 23 · Build, Plattform und Auslieferung

**Wozu?** Der Entwicklungsstand muss auf der vorgesehenen Plattform startbar, reproduzierbar und aktualisierbar sein.

**Varianten:** Web-Bundle, Desktop Build, mobile Packages, Konsolenprojekte, Steam/itch, Debug/Release-Konfiguration, CI, Crashreporting, Migration; plattform- und zielabhängig.

**Daten:** Buildrevision, Runtime-/Engineversion, Dependency Locks, Buildprofil, Assetmanifest, Save-Schema, VersionInfo, FeatureFlags, Releaseartefakt.

**Verarbeitung:** gepinnte Quellen → Abhängigkeitsauflösung → Contentvalidate → Build/Package → Smoke im tatsächlichen Release → Installation/Start → Laden alter Saves → Diagnose und Rollback.

**Beziehungen:** fast alle, insbesondere Daten (02), Save (17), Performance (20), Testing (21), Assets (22).

**Fehler:** funktioniert nur im Editor; Assets im Release fehlen; Debug-Saves inkompatibel; Browser-Cache lädt Mischversionen; Engine-Update bricht Shader; Release nimmt Testfixtures auf.

**Tests:** frischer Checkout und Build, Installation ohne Entwicklerwerkzeuge, Start/Interaktion/Save/Reload, Updatepfad, Offlinebetrieb soweit gefordert, echte Zielgeräte.

**Prompt:** „Beweise den definierten Nutzer-Releasepfad auf dem Zielsystem mit Start, Interaktion, Daten und Save. Markiere ungetestete Plattformen.“

## 24 · Game Design, Core Loop und Game Feel

**Wozu?** Ein Spiel kann technisch fehlerfrei und trotzdem unverständlich, langweilig oder frustrierend sein. Der Core Loop verbindet Entscheidung, Aktion, Feedback und Motivation.

**Varianten:** Exploration, Kampf, Sammeln, Crafting, Aufbau, Progression, Puzzle, Roguelite-Runs, soziale Mechanik, emergente Simulation. Nicht jedes erfolgreiche Spiel benötigt alle.

**Daten:** Gameplayregeln, Tuningparameter, Ressourcen-/Belohnungsraten, Ziele, Schwierigkeitskurve, Onboarding, Spielerfeedback; Messwerte (Abbrüche/Fehler) nur kontextbewusst und datensparsam.

**Laufzeit:** Spieler erkennt Ziel → trifft Entscheidung → System reagiert → visuelles/akustisches Feedback → Zustand/Belohnung → neue Wahl. Ein technischer Test belegt nur Korrektheit, nicht Spielspaß.

**Beziehungen:** alle nutzerwirksamen Systeme, besonders Kampf, Bewegung, Welt, Progression und UI.

**Fehler:** zu viel Content ohne tragfähige Spielschleife; Reward ohne sichtbares Feedback; Skillspam statt Entscheidungen; KI ist technisch korrekt, aber unfair; Bildschirm ist unleserlich.

**Tests:** AI kann Mechaniken reproduzierbar durchspielen; User testet Verständlichkeit, Tempo, Gefühl, Fairness, Spaß und Frustrationspunkte. Feedback als Beobachtung erhalten, nicht automatisch als Änderungsbefehl behandeln.

**Prompt:** „Spiele die Kernschleife selbst, dokumentiere technische Ergebnisse und bereite gezielte Spielerfragen vor. Trenne deinen Test von meiner Bewertung des Spielgefühls.“
