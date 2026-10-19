# Teil III — Besitz, Fortschritt und Erzählung (Bereiche 10–12)

## 10 · Items, Inventar und Wirtschaft

**Wozu?** Gegenstände sind wiederverwendbare Definitionen; tatsächlicher Besitz, Stapelmengen und Ausrüstung sind veränderliche Zustände. Im Monster-RPG wird ein gefundener Heiltrank erst nach legaler Aufnahme Teil des Inventars.

**Varianten:** reine Zählbestände, Slotinventar, Grid, Gewicht/Volumen, individuelle Instanzen mit Haltbarkeit oder Zufallswerten, Equipment, Craftingrezepte, Shops, Handel und Währungen. Kleine RPGs brauchen selten all diese Varianten gleichzeitig.

**Daten:** ItemDefinition (ID, Kategorie, Wirkungsreferenz, Stacklimit, Preis, Tags, AssetRef); InventorySlot (Item-ID/Instanz-ID, Menge); Recipe (Inputs, Outputs, Station, Voraussetzungen); ShopStock; LootTable (Gewichte, Min/Max); CurrencyBalance.

**Laufzeit:** Quelle/Drop/Shop → Item-ID validieren → Kapazität, Rechte und Ressourcen prüfen → Bestandsänderung als konsistente Transaktion → Effekt/Equipment/Quest-Ereignis → UI → Save. Crafting prüft vor der Bestandsmutation sämtliche Inputs/Outputs. Bei einem einmaligen Questreward braucht die Vergabe eine Wiederholsperre.

**Beziehungen:** Charaktere (06), Kampf (09), Progression (11), Story (12), Saves (17), Content (22). Ein Item kann im Inventar existieren, ohne dass seine Benutzungsregel implementiert ist.

**Fehler:** Drop verweist auf fehlende Item-ID; Menge wird negativ; Crafting verbraucht Zutaten ohne Ergebnis; Stapelung verliert individuelle Eigenschaften; Shop verdoppelt Kauf; alte Saves behalten verwaiste IDs.

**Tests:** Pickup/Drop/Consume und Reset; volles Inventar; negative/überlaufende Mengen; Crafting-Abbruch; Kauf ohne Geld; wiederholte Belohnung; Reload nach Transaktion. Konkreter Auremon-Fall: vier verwaiste Species-Drop-IDs samt Alt-Save-Migration.

**ROM-Hinweis:** PGE dokumentiert Item-, TM-/HM- und Trainerdaten; KM beschreibt Shops/Gifts/Trades als Kategorien. Das sind Contentrelationen, kein Beweis für Transaktionsverhalten der Zielspiele.

**Prompt:** „Zeige pro Itemtyp den vollständigen Weg von Definition und Herkunft über Inventartransaktion und Anwendung bis Save/Reload; prüfe illegale Mengen und doppelte Vergabe.“

## 11 · Progression, Erfahrung und Balancing

**Wozu?** Fortschritt macht Handlungen bedeutsam: Monster gewinnen Level, Spieler erhalten Fähigkeiten, Regionen öffnen sich und Gegner passen zum Entwicklungsstand.

**Varianten:** XP-/Levelkurven, Skilltrees, Ruf, Meisterschaften, Evolutionsstufen, Freischaltflags, Battle Pass, Ausrüstungspower, adaptive/konstante Gegnerstärke. Keines dieser Systeme ist universal verpflichtend.

**Daten:** XP-Kurve, Levelschwellen, Stat-Skalierungsformel, Learnsets, UnlockCondition, Evolutionsregeln, Rewards, DifficultyProfile, BalanceParameter; zur Instanz gehören XP, Level, freigeschaltete Fähigkeiten und Belohnungsansprüche.

**Laufzeit:** gültiges Ergebnis (Sieg, Quest, Entdeckung) → Reward-Kriterien und Wiederholbarkeit prüfen → XP/Ressourcen vergeben → Schwelle überschreiten → Stats/Skills/Events aktualisieren → Optionen präsentieren → Save. Bei mehreren Levelanstiegen müssen alle überquerten Schwellen berücksichtigt werden.

**Beziehungen:** Monster (06), Kampf (09), Items (10), Quests (12), Weltzugang (04), UI (16), Persistenz (17).

**Fehler:** XP wird doppelt beansprucht; Evolution referenziert fehlende Species; Level steigt ohne HP-/Statupdate; Moves fehlen nach schneller Levelüberschreitung; Story-/Gegenstandsfreischaltung lässt sich nicht erneut laden; Difficulty skaliert gegen beabsichtigtes Spielgefühl.

**Tests:** Schwelle exakt davor/danach; mehrere Levels in einem Event; Max-Level; Entwicklung mit fehlendem Item; Reward-Wiederholung; Save/Reload; Balance-Szenarien mit reproduzierbaren Builds. Spielspaß nur durch tatsächlichen Spieltest bewertbar.

**Prompt:** „Leite alle Fortschrittsachsen ab, verfolge ihren Trigger bis zum gespeicherten Ergebnis und simuliere Grenzwerte. Trenne numerische Korrektheit von motivierender Progression.“

## 12 · Story, Dialog und Quests

**Wozu?** Die Erzählung verbindet Bedingungen, Entscheidungen, Ereignisse und bleibende Konsequenzen. Ein NPC, der eine Brücke freigibt, benötigt nicht zwingend ein eigenes Questframework, wohl aber einen eindeutigen Zustandsvertrag.

**Varianten:** lineare Missionsfolge, Questgraph mit Voraussetzungen, Dialogbäume, Eventskripte, World-Flags, Reputationssystem, Cutscenes, emergente Story und einmalige/wiederholbare Ereignisse.

**Daten:** NPC/DialogDefinition, ConversationNodes, Condition/Predicate, QuestId/Stage, StoryFlag, Objective, Action/Effect, RewardClaimId, Interaktionsreichweite, Eventtrigger, Textlokalisierung. Persistente Flags nicht mit Dialog-UI-Zustand verwechseln.

**Laufzeit:** Spieler erreicht Trigger/Interaktion → Form/Ort/Flags/Items prüfen → Dialog/Encounter → Ergebnis → berechtigte Eventaktionen ausführen → Quest-/WorldState ändern → Reward einmalig beanspruchen → UI/Save. Typisierte Aktionen können genügende Ausdruckskraft bieten; frei ausführbarer Code in Content erschwert Analyse.

**Beziehungen:** Welt (04), Entities/NPC (05–06), Kampf (09), Inventar (10), Progression (11), UI (16), Save (17).

**Fehler:** Questflag wird gesetzt, obwohl Kampf verloren; unendliche/unerreichbare Questbedingung; Storyblockade nach WorldEdit; mehrfacher Reward; Dialog referenziert gelöschte Map oder Figur; Rückkehrpunkt bei Cutscene ungültig.

**Tests:** Erfolg/Niederlage/Abbruch; Quest in falscher Reihenfolge; zweimal sprechen; Save mitten in Folge; Unmöglichkeits-/Erreichbarkeitsprüfungen; Storypfad mit getrennten Körpern. Prüfe eine tatsächliche Benutzerhandlung mit bleibendem Ergebnis.

**ROM-Hinweis:** Porymap erfasst NPC-/Warp-/Trigger-/Signpost-Ereignisdaten samt Skriptreferenzen. Das sagt nichts darüber aus, wie alle Originalstoryskripte ihre Laufzeitaktionen implementieren.

**Prompt:** „Untersuche vom konkreten Auslöser bis zu Dialog, Kampf-/Itemaktion, World-Flag und gespeichertem Outcome. Finde unerreichbare und doppelt belohnbare Wege.“
