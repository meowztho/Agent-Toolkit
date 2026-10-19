# KI-Agenten-Workflow – Cheatsheet

**Prinzip:** Kreativ entwickeln, Erkenntnisse sichern, unabhängig rekonstruieren und prüfen. Die Projektwahrheit liegt im Repository, nicht im Chat. Die sieben Phasen sind ein Werkzeugkasten, keine starre Pflichtkette.

## Manuell steuern – ohne Orchestrator oder Subagenten

Du wählst selbst den nächsten Arbeitsschritt. Bei einem Rollenwechsel startest du **einen Chat mit der benötigten Rolle** aus der Schnellwahl unten; zusammenhängende Arbeit kann im selben Chat bleiben. Du musst nicht alle Phasen durchlaufen und keine Subagenten starten. Bei einem laufenden Projekt beginnst du direkt bei der aktuellen Lücke. Für eine unabhängige Prüfung (05) nimmst du immer einen frischen Chat, der die Ergebnisse des Bau-Agenten selbst überprüft.

1. **Projekt und Ziel festlegen:** vollständigen Projektpfad und die aktuelle Aufgabe bereithalten. Prüfe, ob bereits APC-Unterlagen, ein `domain-specialist/`-Ordner, RORE-Befunde oder ein Prüfbericht im Projekt liegen.
2. **Passenden Prompt starten:** Beim Rollenwechsel die Datei aus `Agent/` im neuen Chat vollständig einfügen oder ihren absoluten Pfad nennen, wenn der Chat Dateizugriff hat. Platzhalter wie `Project`, `Domain`, `Output Directory` und `Current goal` konkret ausfüllen. Die benötigten Plugins/Skills müssen für den jeweiligen Chat verfügbar sein.
3. **Ergebnis abnehmen:** Lass dir die tatsächlichen Dateipfade, Änderungen, ausgeführten Prüfungen und offenen Punkte nennen. Lies bei wichtigen Entscheidungen die erzeugte Projektdatei, nicht nur die Chat-Zusammenfassung.
4. **Nächsten Schritt wählen:** Ist das Ziel erfüllt und belegt, fertig oder mit 07 weiterentwickeln. Fehlt eine Produktentscheidung, zu 03; fehlt Wissen über ein fremdes/bestehendes System, zu 02; liegt ein konkreter Fehler vor, zu 04/07 oder für schwierige Ursachen zu 05b. Nach einer wesentlichen Korrektur 05 frisch prüfen lassen.

**Kopierbarer Start für einen neuen Chat** (den passenden Agent-Prompt zusätzlich einfügen oder als Datei angeben):

```text
Projekt: <vollständiger Pfad>
Aktuelles Ziel: <konkretes Ergebnis oder zu prüfende Frage>
Prompt/Rolle: <vollständiger Pfad zu Agent/XX-...md>
Vorhandene Übergaben: <Pfad zu APC, domain-specialist, RORE oder Prüfbericht; sonst "keine">
Arbeite in diesem Chat selbst, ohne Subagenten. Nutze nur die für das Ziel nötigen Quellen.
Berichte am Ende: Ergebnisdateien, tatsächlich geprüfte Funktion, offene Entscheidungen und den sinnvollsten nächsten Schritt.
```

**Spezielle Übergaben:** Für 01b `Output Directory` auf den Projektordner setzen, wenn APC das Ergebnis dort finden soll; `Domain` und bei einem konkreten Vorhaben dessen Ziel/Anwendungsfall angeben. Danach APC (03) im frischen Chat den Projektpfad und den erzeugten Pfad zu `domain-specialist/<domäne>/PROJECT_SYSTEM_NEEDS.md` mitgeben. RORE-Befunde ebenfalls als Pfad übergeben. Einen FAIL-Bericht aus 05 an 04 oder 07 zur gezielten Reparatur geben; danach nur die betroffenen Behauptungen erneut unabhängig prüfen lassen.

## Schnellwahl: Welcher Agent wann?

| Situation | Prompt / Rolle | Neuer Chat? |
| --- | --- | --- |
| Neue Idee, ungeklärte Machbarkeit, erster Prototyp | `Agent/01-exploration yoloXD.md` – Creative Coding Agent | Ja, zum Start |
| Fachwissen und benötigte Systemfähigkeiten für eine Domäne klären | `Agent/01b-Domain Knowledge Architect.md` – Domain Knowledge Architect | Eigener Rechercheauftrag bei Bedarf |
| Fremder, chaotischer oder schwer verständlicher Code | `Agent/02-reconstruction-rore.md` – Analytical Reasoning Agent | Ja; RORE nur bei echtem Erkenntnisbedarf |
| Produktziele, Verträge, Reihenfolge und Akzeptanzkriterien fehlen | `Agent/03-project-compiler-apc.md` – Architecture/Planning Agent | Ja bei erstmaliger Projektübernahme |
| Fehler oder architektonische Altlasten gezielt beheben | `Agent/04-consolidation-core-first.md` – Coding/Reasoning Agent | Bei Rollenwechsel ja |
| Unabhängig Architektur und Funktionalität prüfen | `Agent/05-independent-verification.md` – Critical Reviewer | **Immer frisch**, möglichst anderer Kontext/Modell |
| Blueprint für neue Agenten/isolierte Änderungen erstellen | `Agent/06-agent-blueprint.md` – Blueprint Agent | Eigenständig oder zum Dokumentationsagenten zurück |
| Nach Konsolidierung weiterentwickeln | `Agent/07-continuous-development.md` – Development Agent | Nur bei Rollenwechsel oder überladenem Kontext |
| Bestehende UI, Shell, UX oder Grafik gezielt hochwertiger gestalten | `Agent/07a-experience-style-upgrade.md` – Experience/Style Upgrade Agent | Neuer Fokus-Chat bei größerem Stilwechsel; sonst bestehender Design-Chat |
| Intermittierender Fehler, Leaks, Polling, visueller Bug, Race, Datenfehler | `Agent/05b-specialist-debugger.md` – Runtime Debugger | **Frischer Diagnose-Chat**; Profil per JIT |

## Einmalige Projektübernahme

1. Im Roh-Chat (01) Ideen besprechen, bauen und die Machbarkeit so weit wie nötig prüfen.
   Bei unklaren fachlichen Systemgrundlagen kann 01b parallel oder anschließend einen domänenneutralen Baukasten unter `domain-specialist/<domäne>/` erstellen. Für ein konkretes Vorhaben hält `PROJECT_SYSTEM_NEEDS.md` begründete Systemkandidaten, Abhängigkeiten und einen ersten durchgehenden Funktionsnachweis fest.
2. RORE (02) nur bei echter Erkenntnislücke in einem frischen Chat zur Rekonstruktion einsetzen.
3. Der Explorer übergibt Machbarkeitsbefunde, Nutzerziele und offene Fragen an APC (03). APC berücksichtigt vorhandene `domain-specialist/`-Ergebnisse als fachliche Vorschläge und erfasst daraus nach Abgleich mit Nutzerwillen und Projektstand die Produktwahrheit und Prüfziele.
4. Danach übernimmt der erste Core-First-Agent (04) die Konsolidierung und Korrektur.
5. Unabhängig verifizieren (05); gezieltes Debugging (05b) nach Risikoprofil.
6. Blueprint als knappen Einstieg ergänzen (06).
7. Weiterentwickeln (07); Spezialisten nur bei konkretem Trigger.

**Normalbetrieb:** 07 → eigene Tests → Commit; für gezielte UI/UX/Shell-/Grafikaufwertung 07A; bei materialer Änderung 05, bei ungeklärtem Defekt 05b, bei geänderten Produktzielen 03, bei unklarer Legacy-Semantik 02.

## Umgang mit Chats und Skills

- **Neuer Chat:** unabhängige Prüfung, von Implementierung zu RORE/APC/Blueprint/Debugger, signifikanter Kontextverlust oder wesentlicher Aufgabenwechsel.
- **Gleicher Chat:** zusammenhängende Implementierung und ihre eigenen Tests; kleine iterative Korrekturen.
- **Skills nicht pauschal zusammenladen.** RORE erhebt *beobachtete Wahrheit*; APC pflegt *Produkt-/Realisierungs-/Akzeptanzwahrheit*; Core-First klärt kanonische Owner und Änderungen; Blueprint verweist kompakt auf diese Quellen.
- APC darf Core-First bei relevanten Architekturfragen JIT verwenden. Ein implementierender Hauptagent muss Core-First selbst anwenden, wenn die Ownership-Frage material ist.
- Verifier/Debugger beurteilen und dokumentieren, sie verändern keinen Produktcode. Reparaturen zurück zu 04 oder 07.
- Bei **07A** ist der bisherige Stil nicht automatisch die Zielvorgabe. Bestehende Assets liefern zunächst Funktions-/Identitätskontext; explizite Nutzerwünsche und Referenzbilder bestimmen die gewünschte visuelle Richtung. Vorher/Nachher am echten Produkt prüfen.

## Tool-/Referenzbedarf: nur bei echtem Bedarf

Fehlt für die nächste wesentliche Aktion eine Fähigkeit, soll der Agent **gezielt** fragen und nicht pauschal eine Programmliste verlangen:

- **Need now:** genaues Tool, Zugriff, Referenzbild, Asset oder Entscheidung; wofür es erforderlich ist und welche kleinste Nutzeraktion nötig wäre.
- **Helpful optional:** konkrete Referenzen oder Werkzeuge mit erkennbarem Qualitätsgewinn.
- **Can proceed without:** mögliche sichere Alternative und welche Ergebnisse damit noch nicht verifizierbar sind.

Nur bei materiellen Hindernissen ausgeben. Vor Installationsvorschlägen vorhandene Werkzeuge/Alternativen prüfen. Keine optionalen Rückfragen als Pflichtblocker behandeln; bei relevanten Kosten, Lizenzen oder Eingriffen vorher um Zustimmung bitten.

## Runtime-Debugger: passende Spezialprüfung

| Symptom | JIT-Profil |
| --- | --- |
| Sichtbarer Fehler, UI reagiert nicht, falsches Layout | VISUAL_INTERACTION |
| Langsam nach Stunden, Log wächst, Idle-CPU/GPU, Timer | PERFORMANCE_LONG_RUN |
| Fehler sporadisch, Events in falscher Reihenfolge, Race | CONCURRENCY_STATE |
| Daten fehlen oder unterscheiden sich über Layer hinweg | INTEGRATION_DATA |
| Crash, Retry-Schleife, Restart/Shutdown defekt | FAILURE_RECOVERY |
| Funktioniert nur in Dev, Release/Installation defekt | BUILD_ENVIRONMENT |

Der Debugger wählt zunächst **ein** relevantes Profil. Weitere nur bei konkreter Evidenz. Ein Timer alle 80 ms oder ein Logeintrag alle 5 Sekunden ist noch kein Beweis für einen Leistungsfehler.

## Jede Übergabe in 30 Sekunden

1. Im neuen Chat den **vollständigen Projektpfad** und den passenden Prompt angeben.
2. Agent liest Root, Anweisungen, Git-Status/Diffs und nur relevante Projektverträge.
3. Nach der Arbeit: nachvollziehbare Ergebnisse, ausgeführte Tests und verbleibende Unsicherheit; **nur eigene Änderungen lokal committen, nie pushen**.
4. Git-Identität folgt den geltenden Projekt- und Harness-Anweisungen; der Rollenname ist keine Commit-Identität. **Keine globale Git-Konfiguration ändern**.
5. Uncommitted Änderungen anderer nicht überschreiben; laufende Daten, externe Einstellungen und unversionierte Artefakte gesondert berücksichtigen.
6. Ohne reale Beobachtung kein PASS für UI/Laufzeit oder Langzeitstabilität. UNVERIFIED/INCONCLUSIVE ausweisen.

## Aufbau

- `Agent/`: kopierbare englische Agenten-Startprompts – kein zusätzliches Plugin.
- `runtime-debugger` ist ein separates, optionales JIT-Skill-Plugin; es liegt aktuell nicht in diesem Workflow-Ordner. Der Prompt `05b` dokumentiert fehlende Skill-Verfügbarkeit und erlaubt eine begrenzte evidenzbasierte Prüfung ohne Installation.
- Vorhandene APC-, RORE-, Core-First- und Blueprint-Plugins bleiben selbstständig. Dieses Paket ersetzt oder kopiert ihre Verfahren nicht.
