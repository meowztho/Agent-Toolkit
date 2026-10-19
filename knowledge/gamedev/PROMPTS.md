# Game Systems — kopierbare Kurzprompts (v1.0)

Diese Prompts ergänzen den vorhandenen Agent-Workflow, sie ersetzen ihn nicht. Die detaillierten 24 Bereiche stehen in `AREA_PROMPTS_24.md`. Jede technische Aussage mit angemessener Evidenz belegen (siehe `SYSTEM_AUDIT_MATRIX.md`).

## A — Gesamtbild / Discovery (read-only)

Analysiere das bestehende Spiel anhand von GAME_SYSTEMS_HANDBOOK.md. Rekonstruiere reale Mechaniken, Daten, Laufzeit, Zustände, Verantwortlichkeiten und Abhängigkeiten. Ordne Systeme ein als nachgewiesen, teilweise, simuliert, fehlend, nicht geprüft oder für dieses Spiel nicht benötigt. Belege Aussagen durch konkrete Quellen und geeignete Tests; unterscheide Codebefund von beobachtetem Gameplay. Identifiziere neue kreative Möglichkeiten, Probleme und Doppelungen. Priorisiere nur relevante Vertiefungen. Produktcode nicht ändern; keine automatische Umstrukturierung.

## B — Neue Erkenntnisse kreativ verarbeiten

Nutze die dokumentierten Entdeckungen und Probleme als Ausgangspunkt für weitere kreative Gameplay-Entwicklung. Bewahre funktionierende Mechaniken. Experimentiere mit kleinen reversiblen Änderungen, teste in der tatsächlichen Runtime und dokumentiere Neues sowie Unsicherheiten. Nicht den gesamten Katalog implementieren.

## C — Zweites Gesamtbild bei spielbarem Grundgerüst

Erstelle eine neue Bestandsaufnahme wie in A und vergleiche sie mit der vorherigen. Zeige neu entstandene Systeme, veränderte Verträge, behobene/offene Probleme und nur die Bereiche, deren vertiefte Prüfung jetzt einen konkreten Nutzen hat. Keine Produktcodeänderungen.

## D — Einzelbereich destillieren (read-only)

Untersuche Katalogbereich [ID/THEMA] in der aktuellen Implementierung. Erkläre mir verständlich Zweck, Varianten, Definitionen, Instanzen, Laufzeitzustände, Datenflüsse, Owner, Schnittstellen, Abhängigkeiten, Randfälle und Persistenz. Belege tatsächliches Verhalten mit gezielten Tests. Trenne nachgewiesen, teilweise, simuliert, nicht geprüft und nicht benötigt. Schlage die kleinsten notwendigen Korrekturen vor, aber ändere noch keinen Produktcode.

## E — AI-Spieltest

Teste die priorisierten Mechaniken selbst im realen Spiel, soweit Tools und Zugriff dies erlauben. Prüfe Interaktion UND resultierenden Zustand, nicht nur Screenshots oder Unit-Tests. Verwende isolierte Teststände/Cheats, falls nötig und zulässig. Dokumentiere Schritte, erwartetes/observiertes Verhalten, Reproduktion und offene Nachweislücken. Behaupte keinen PASS ohne Beobachtung.

## F — User-Spieltest vorbereiten

Erstelle eine kurze manuelle Testliste der nicht automatisiert belegbaren oder spielgefühlabhängigen Funktionen. Nenne je Test Aktion, erwartetes Ergebnis und die konkrete Rückmeldung, die du von mir brauchst. Unterscheide technische Korrektheit und Spielgefühl.

## G — Konsolidierung + Creative Fixes

Setze nur die priorisierten und freigegebenen Befunde um. Prüfe zuerst Wiederverwendung, Konfiguration oder Entfernung statt Neuentwicklung. Bewahre vorhandenes Gameplay und fremde Änderungen. Teste die kleinsten relevanten Grenzen, bei Gameplay zusätzlich die reale Runtime. Dokumentiere Änderungen, Regressionen und den aktuellen Zustand für den nächsten Creative Agent.

## H — Übergabe an nächsten Creative Agent

Fasse knapp zusammen: spielbare Kernmechaniken, bestätigte Verträge/Owner, verfügbare Daten und APIs, nachgewiesene Tests, kreative Chancen, offene Defekte und bewusste Nicht-Ziele. Trenne Beobachtung von Annahme. Der neue Agent soll frei weiterentwickeln können, ohne bestätigte Mechaniken versehentlich zu beschädigen.

## I — Vollständige Verarbeitungsketten (ohne Editor)

Verwende SYSTEM_AUDIT_MATRIX.md und die Kapitel 01–06. Erstelle für die tatsächlichen Ressourcenklassen konkrete Tabellen: Definition/ID → Producer → Instanz/Owner → Runtime-Consumer → Outcome/UI → Persistenz → Reload. Finde fehlende Referenzen und nicht verarbeitete Datenfelder. Gib nur belegte Fehler und die kleinsten Korrekturmöglichkeiten aus. Produktcode read-only.

## J — ROM-Editor-Beobachtungen nutzen

Lies ROM_EDITOR_SYSTEM_INSIGHTS.md. Vergleiche nur die belegten Datenrelationen aus Porymap, PGE und KM Editor mit unserem konkreten Spiel. Unterscheide reine Contentfelder, echte Runtime-Semantik und Editor-/Import-Sicherheit. Identifiziere Lücken, ohne Original-Klassen, Funktionen, Lizenzrechte oder Implementierungsstatus zu erfinden. Ein Editor ist keine Voraussetzung für Systemfunktionalität.

## K — Systems-Baseline für neuen Creative Agent

Nutze die neueste Systemmatrix und die geprüften Gameplaytests. Gib dem nächsten Agenten nur bestehende Runtimeverträge, funktionierende öffentliche Schnittstellen, beabsichtigtes Spielerlebnis, konkrete offene Bugs und kreative Optionen. Nicht geprüfte Fähigkeiten als UNKNOWN markieren. Der Agent soll frei entwickeln können, ohne bekannte funktionierende Regeln zu brechen.
