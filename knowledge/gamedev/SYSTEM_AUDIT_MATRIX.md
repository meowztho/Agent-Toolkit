# System-Destillation — Prüfmatrix und Beweiskette (v1.0)

## 1. Status, der **immer** gesetzt werden muss

- **VERIFIED_RUNTIME:** definierte Aktion und erwarteter Zustand im echten Spiel beobachtet. Genaue Umgebung/Revision/Testschritte nennen.
- **VERIFIED_TEST:** gezielter automatisierter Test wurde durchgeführt, jedoch nicht der vollständige Nutzungsweg.
- **STATIC_ONLY:** Quellen oder Daten weisen die Fähigkeit aus; keine Laufzeitaussage.
- **PARTIAL:** ein konkreter Vertrag funktioniert, ein anderer ist unvollständig oder widersprüchlich.
- **SIMULATED:** Stub/Mock/Placeholder oder reine Anzeige ohne echte Wirkung.
- **FAILED:** reproduzierbarer Gegenbeleg.
- **UNKNOWN:** nicht hinreichend geprüft.
- **NOT_REQUIRED:** gemäß expliziten Zielen aktuell nicht benötigt; kein Defekt.

Eine reine automatische Smoke-Prüfung wird nicht zu VERIFIED_RUNTIME aufgewertet. User-Spielgefühl ist eine zusätzliche eigene Evidenzklasse, nicht Ersatz für funktionalen Test.

## 2. Eine Zeile je geprüftem System / Ressourcentyp

| Feld | Inhalt |
|---|---|
| ID / Kurzname | Katalog-ID 01–24 + konkreter Teilbereich |
| Ziel | Nutzerentscheidung/Spielverhalten, nicht aus Code erfunden |
| Definition / Producer | Datei, Registry, Datenformat, erzeugende Funktion |
| Instanz / Owner | Konkreter Runtimebesitzer, instanzierender Pfad |
| Interpreter / Consumer | Welche Funktion wendet Daten tatsächlich an? |
| Outcome / Präsentation | Sichtbare/spielrelevante Wirkung und Anzeige |
| Persistence | Was wird durch welchen Owner gespeichert? |
| Abhängigkeiten | Aufrufer, Nachbarsysteme, Schnittstellen |
| Negativfall | Mindestens ein Fehlerfall, ungültiger Wert oder Abbruch |
| Nachweis / Revision | Testbefehl, Laufzeitbeobachtung, Datum, Seed, Beleg |
| Status | Eine der obigen Kategorien + genaue Evidenzgrenze |
| Befund / Schwere | Konkreter Fehler, Risiko oder kein Handlungsbedarf |
| Minimalmaßnahme | Wiederverwenden, konfigurieren, ergänzen, reparieren, entfernen oder bewusst ignorieren |

## 3. Drei Ebenen der Discovery

**Gesamtbild A:** Bestehende Systeme grob identifizieren. Pro Bereich maximal wenige relevante Pfade, keine große Quellcode-Autopsie. Ergebnis: Abdeckungsmatrix, unbekannte Risiken, kreative Möglichkeiten.

**Gesamtbild B:** Nach weiterem Creative-Zyklus Unterschiede zur vorherigen Matrix ausweisen: hinzugefügt, geändert, ersetzt, behoben, neu gebrochen, weiterhin unknown. Nur tatsächlich relevante Vertiefungen beauftragen.

**Bereichs-Destillation:** End-to-End-Ketten mit Negativfällen, abgeleiteten Verträgen, Zustands-/Owner-Grenzen und echten Tests untersuchen; nach Notwendigkeit Konsolidierungsmaßnahme vorschlagen, nicht sofort umbauen.

## 4. Prüfschablone „Ressource wirklich nutzbar?“

1. Gibt es eine Definition mit eindeutiger ID, gültigem Wertebereich und zulässigen Fremdreferenzen?
2. Wird sie beim normalen Start tatsächlich geladen (nicht nur in Tests importiert)?
3. Erzeugt der Producer das konkrete Objekt oder Outcome?
4. Interpretiert ein Runtime-Consumer die Ressource? Welche Teile ihres Schemas?
5. Hat der zustandsändernde Pfad eine eindeutige Autorität? Wer verwirft ungültige Commands?
6. Kann das Ergebnis vom Spieler ausgelöst und beobachtet werden?
7. Werden relevante Änderungen konsistent gespeichert und wieder geladen?
8. Was passiert bei fehlender ID, Retry, Abbruch, Pause, Szenenwechsel, KO/Tod und Neustart (nur relevante Fälle)?
9. Hat der Agent einen realen Nutzungsweg getestet? Wenn nein, welche Behauptung ist noch offen?
10. Muss ein neues System entstehen oder genügt ein neuer Inhalt/eine neue Konfiguration?

## 5. Kleiner exemplarischer Audit: vier Monster-Drop-IDs

**Quelle:** Auremon-Bericht vom 19.10.2026, kein hier erneut ausgeführter Spieltest.

- **Producer:** Species-Drop-Definitionen verweisen auf `perlkern`.
- **Referenzsystem:** registriert ist `perlkorn`; die ID `perlkern` ist unbekannt.
- **Consumer:** Loot-Pickup und Rendering greifen auf `ITEMS[v].name` zu.
- **Korrektur laut Bericht:** vier Drop-IDs angepasst und Alt-Save-Inventar nach `perlkorn` migriert.
- **Beleg laut Bericht:** negativer Node-Smoke zunächst rot; danach Smoke/Validator grün.
- **Grenze:** sichtbar ausgeführter Pickup im Browser nicht belegt.

**Lernpunkt:** Falsche *Contentreferenz* statt fehlendes Inventar-/Lootsystem. Kleinste Behebung: korrekte ID + referenzielle Regression + Save-Migration; keine zweite Itemdatenbank.

## 6. Trennung der Verantwortlichkeiten

- **Creative Agent:** Funktionen entwickeln, Varianten ausprobieren, die eigentliche Spielfreude erhöhen.
- **Analytischer Agent / Gesamtbild:** nachweisbare Struktur, Schwächen und Möglichkeiten erkennen; Code zunächst read-only.
- **Vertiefender Agent:** präzise Ketten, Fehler, Datenverträge und Prüfgrenzen.
- **Implementation/Konsolidierung:** nur begründet priorisierte Änderungen.
- **Independent Reviewer:** unabhängig gegen Produkt-/Laufzeitanforderungen verifizieren.
- **User:** tatsächliches Spielgefühl, gewünschtes Verhalten, Prioritäten, kreative Richtungsentscheidungen.

APC, RORE, Core-First, Blueprint und bestehender Agent-Workflow bleiben eigenständige Verfahren; dieser Katalog ordnet nur GameDev-Fachfragen zu.
