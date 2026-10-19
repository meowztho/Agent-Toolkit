# Teil V — Dauerhafte Welten und komplexe Simulation (Bereiche 17–19)

## 17 · Savegames, Persistenz und Migration

**Wozu?** Was der Spieler verändert, muss nach Neustart noch stimmen. Die häufigste Verwechslung ist, einen aktuellen UI-Wert zu speichern, obwohl der eigentliche Runtime-Owner einen anderen Wert besitzt.

**Varianten:** Save-Snapshot; inkrementelles Journal; mehrere Slots; Checkpoints; Autosave; Cloudsave; Session Persistence; server-authoritative Speicherung. Ein Offline-Spiel braucht keine Server-Datenbank.

**Daten:** Save-Version, Spieler-/Monsterinstanzen, Party/Box, Inventar, Welt-/Questflags, Orts-/Körperpositionen, World-Overlays, einmalige RewardClaims, RNG/Instanzkontext soweit Fortsetzung erforderlich. Keine nutzlosen Rendercaches/Listener speichern.

**Laufzeit:** Speicheranlass → von Ownern konsistenten Snapshot gewinnen → Schema/IDs/Bereiche validieren → sicher schreiben/Commit → Rückmeldung; Laden → Version erkennen → Migration/Validierung → Instanzen rekonstruieren → Szenen/Assets binden → Welt fortsetzen. „In-Memory erfolgreich“ ist nicht gleich „auf Datenträger erfolgreich“.

**Abhängigkeiten:** praktisch jedes zustandsführende System; besonders Welt (04), Monster (06), Loot (10), Quests (12), Generator (18).

**Fehler:** halbe Writes, zwei verteilte Save-Owner, Spielstand enthält gelöschte Item-ID, einmalige Rewards doppelt, Dungeon Exit verliert Position, altes Schema nicht migriert, In-Memory-Commit trotz Savefehler.

**Tests:** Save→Neustart→Load→identische relevante Zustände; abgeschnittener/ungültiger Save; Legacy-Version; Speicherfehler; zwei schnell folgende Saves; Quest nach Reload nicht doppelt; Dungeon verlassen/fortsetzen. Cloud-Kollisionen nur, wenn vorhanden.

**Praxisbeleg:** Auremon-Datenfix `perlkern→perlkorn` benötigte Migration bereits bestehender Inventare. Die Datei beschreibt keinen bestätigten vollständigen Crash-Atomizitätsvertrag.

**Prompt:** „Zeige von jedem Savefeld den Gameplay-Owner und einen wirklichen Save/Reload-Test. Prüfe Migration, Wiederholung und Speicherfehler; markiere nicht getestete Crash-Sicherheit.“

## 18 · Prozedurale Generierung, Spawns und Instanzen

**Wozu?** Inhalte können Regeln folgen statt einzeln gezeichnet zu werden. Ein Dungeon-Generator braucht nicht nur Zufall, sondern spielbare, gültige Räume.

**Varianten:** Seed-basierte Noise-Karten, Room Graphs, WFC, grammatikalische Generatoren, Templates + Variation, Spawn-/Loot-Tabellen, authored Grundstruktur plus prozedurale Wildnis, Instanzdungeons.

**Daten:** GeneratorProfile, Seed, Kartenbounds, Terrain-/Biome-Parameter, SpawnGewichte, Constraints, Entry/Exit, Encounter-/LootProfile, Instanz-/Run-ID, WorldOverlay. Seed allein reproduziert nur, was ausschließlich von ihm und stabilen deterministischen Inputs abhängt.

**Laufzeit:** Generatoranfrage → Konfiguration/Seed → Basislayout → Constraints prüfen (Wege, Spawn, Grenzen, Storyschutz) → validierte Karte/Instanz → NPC/Monsterspawns → Gameplay → Outcome → definierte persistente Änderungen/Rewards → Cleanup oder Resume.

**Abhängigkeiten:** Maps (04), Navigation (07), KI (08), Kampf (09), Items (10), Quests (12), Save (17), Performance (20).

**Fehler:** unzugänglicher Ausgang, Spawn im Hindernis, Generator überschreibt handgebaute Storyroute, derselbe Seed erzeugt andere Gegner durch Math.random, Exit teleportiert Begleiter, Dungeonreward doppelt.

**Tests:** viele Seeds mit automatisierter Erreichbarkeit, Minimal-/Maximalraumgröße, Spawnpfade, wiederholte Seeds, Retry/Exit/KO, Save/Reload, Gamefeel im realen Dungeon (Simulation reicht dafür nicht).

**Prompt:** „Trenne authored Inhalte, generierte Basis und persistierte Änderungen. Prüfe Seeds, Erreichbarkeit, Spawns, Rückkehr und Reward-Claims in echten Instanzen.“

## 19 · Multiplayer und Netzwerk (optional)

**Wozu?** Mehrere Clients benötigen gemeinsame Regeln dafür, wem ein Zustand gehört, welche Aktionen erlaubt sind und wann andere Spieler Änderungen sehen. Für ein Offline-Spiel ist dieser Bereich bewusst *nicht benötigt*.

**Varianten:** Peer-to-Peer, Host-authoritative, Dedicated Server, lockstep, client prediction/server reconciliation, snapshot replication, RPC/Event-Replikation, rollback netcode. Auswahl abhängig von Spieltempo, Cheat-Risiko und Produktionsaufwand.

**Daten:** Session/PlayerId, Tick/Sequenz, Commands, AuthoritativeState, ReplicatedState, Versions, InputBuffer, Ownership, Interest/Visibility, NetworkErrorState.

**Laufzeit:** Client-Intent → Übertragung → Server-/Host-Autorisierung → Simulation → Outcome/Snapshot → Clients rezipieren/entschärfen Latenz → lokale Darstellung. Rendering darf eine vorhergesagte Sicht zeigen, aber sie ist nicht autoritativ.

**Abhängigkeiten:** Runtime (01), Zustände (03), Kampf (09), Movement (07), Saves/Accounts (17), Performance/Tests (20–21).

**Fehler:** Client darf Inventar autoritativ erhöhen; doppelte RPCs belohnen zweimal; desynchronisierte Positionen; verlorene/reorderte Nachrichten; Disconnect verliert Fortschritt; Cheating/Datenschutz.

**Tests:** Latenz/Paketverlust, Reconnect, mehrere Spieler gleichzeitig looten, gleichzeitige Treffer, Client/Server-Desync und Recovery; nur bei tatsächlich geplanten Multiplayeranforderungen.

**Prompt:** „Ist Networking im Zielspiel überhaupt vorgesehen? Falls ja: zeichne Ownership, Request→Authority→Replication→Clientzustand und teste Latenz sowie doppelte Commands.“
