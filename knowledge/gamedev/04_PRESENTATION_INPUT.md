# Teil IV — Darstellung und Spielereingabe (Bereiche 13–16)

## 13 · Animation

**Wozu?** Bewegung und Aktionen müssen sichtbar zeitlich zusammenhängen. Eine Attackenanimation ist nicht gleich ihre Kampfregel; bestimmte Animationsereignisse können den erlaubten Trefferzeitpunkt steuern.

**Varianten:** Spritesheets/Frameanimation, Skelett/Rig, Blend Trees, State Machines, Root Motion, additive Animationen, Directional Sets, Animation Events, Procedural Animation, IK.

**Daten:** AnimationClipRef, Frame-/Bone-Daten, Framerate, Loop, Transition, Direction, Anchor, HitMoment, optional RootMotion. Aktive Zustände: Clip/State, Blendgewicht, Playbackposition und Geschwindigkeit.

**Laufzeit:** Gameplaystatus/Input → Präsentationszustand (idle, walk, attack, hurt) → Clip/Transition wählen → zeitlich abspielen → Renderpose; ggf. definierter Callback zur Gameplay-Hitbox. Gameplay und Bild müssen nach Unterbrechung/KO korrekt übereinstimmen.

**Beziehungen:** Entities (05), Bewegung (07), Kampf (09), Rendering (14), Audio (15), Ressourcen (22).

**Fehler:** Attackenschaden vor/nach falschem Frame; visuelles Gleiten bei Kollisionsstopp; Rotation/Hitbox entkoppelt; ein fehlender Clip friert Actor; Animation-Lock nach Unterbrechung.

**Tests:** Bewegungsstart/-stopp, Angriff abbrechen, KO während Animation, Clip fehlt, Richtungswechsel, FPS-Wechsel, Wechsel Mensch/Monster. Nur ein Screenshot belegt keine zeitliche Synchronisation.

**Prompt:** „Trenne spielmechanischen Zustand von Animationsstatus und zeige die Synchronisationspunkte. Teste Interrupts, Trefferfenster, Richtungen und fehlende Assets.“

## 14 · Rendering, Kamera und visuelle Effekte

**Wozu?** Aus Weltzustand und Assets wird ein Bild. Perspektive, Kamera, Tiefe, Ebenen, Schatten und Lichteffekte beeinflussen Lesbarkeit und Game Feel, dürfen aber keine heimlichen zweiten Gameplayregeln sein.

**Varianten:** 2D Canvas/Sprite Renderer, 2.5D, 3D Rasterisierung, Forward/Deferred, Shader, Particle Systems, Tilemaps, Renderlayers, Culling, LOD, Postprocessing, Kameramodi.

**Daten:** AssetRefs, Sprite/Material/Mesh, Transform, Z-Order/Depth, Camera Projection/FOV/Zoom, Blend, Light, VFX Trigger. Visuelle LOD-Infos müssen nicht den autoritativen Kollisionskörper ersetzen.

**Laufzeit:** authoritative World-/ActorState → Sichtbarkeit/Interpolation → Kamera/Transformation → Renderables nach Layer/Material sortieren → Render-/VFX-Ausgabe → Display. Renderer soll keine Species- oder Kampfwerte neu berechnen.

**Beziehungen:** Map (04), Entities (05), Bewegung (07), Animation (13), UI (16), Performance (20), Assetpipeline (22).

**Fehler:** Sprite überlagert Tür oder Spieler falsch; falsches Tile-Layer verdeckt Hindernis; Camera jitter; sichtbarer Kran ohne Collision; Shader verursacht Z-Fighting; Renderlogik erschafft zweite Tile-Wahrheit.

**Tests:** Zoom/Resolution/Aspect Ratio; überlappende Entities; schneller Mapwechsel; Last mit vielen Objekten; Animation und Collision nebeneinander; Stil-/Sprite-Tausch bei gleichbleibenden Spielregeln.

**Prompt:** „Leite Renderdaten vom Gameplay-Zustand ab, prüfe Kamera, Layer, Occlusion und Sichtbarkeit. Zeige, ob Grafik und Kollision unterschiedliche Wahrheiten verwenden.“

## 15 · Audio, Musik und akustisches Feedback

**Wozu?** Töne vermitteln Interaktion, Gefahr, Treffer, Umgebung, Stimmung und Rhythmus. Klangdaten können prozedural oder aus importierten Dateien stammen.

**Varianten:** SFX-Player, WebAudio/Oszillatoren, Mixer-Busse, Musiklayer, adaptive Musik, räumliches Audio, Voice, Ducking, Reverb, UI-Sounds.

**Daten:** AudioCueId, Source/Generator, Lautstärke, Pitchvarianten, Loop, Bus/Group, Position/Radius, Priorität, Übergänge, Benutzer-Einstellungen.

**Laufzeit:** bestätigter Spiel-/UI-Event → AudioCue auswählen → Ressourcen bereitstellen → Abspielen/Mischen/Priorisieren → Pause/Fokus/Stop behandeln. Audio darf nicht eigenständig Schaden/Rewards erzeugen.

**Beziehungen:** Events (03), World (04), Combat (09), Animation (13), UI (16), Assetpipeline (22).

**Fehler:** Sound feuert mehrfach pro Treffer; Musik bleibt aus alter Szene aktiv; Browser blockiert Audio vor Interaktion; zu viele Sounds clippen; Pause stoppt Musik nicht; fehlende Cue wird zur Exception.

**Tests:** Fokusverlust/Resume, zwei gleichzeitige Ereignisse, Übergänge, Volume=0, fehlende Quelle, Audio entsperren nach erster Interaktion und echte Hörprobe. Frequenzspektrum allein ist kein subjektiver Klangtest.

**Prompt:** „Verfolge Event → AudioCue → Mixer → gehörtes Ergebnis. Prüfe Prioritäten, Szenenwechsel, stumme Modi, Fokus und doppelte Wiedergabe.“

## 16 · UI, UX, Eingabe und Accessibility

**Wozu?** Der Spieler formuliert Absichten und versteht Ergebnisse. Menüs sind nicht nur Grafiken; sie müssen die gleichen autoritativen Spielregeln verwenden wie Tastatur und Gamepad.

**Varianten:** Action-Mapping, Context-Actions, Keyboard/Mouse, Controller/Touch, HUD, Inventarmenü, Dialog, Auswahlrad, Fokus-/Modalstack, Tooltips, Remapping, Accessibility-Optionen.

**Daten:** ActionBindings, InputContext, UI-ViewModel/Projection, Fokusziel, SelectedItem/ActorRef, Settings (Textgröße, Kontrast, Remapping), Modalstatus.

**Laufzeit:** physische Eingabe → Binding/Context → Intent/Command → autoritatives Gameplay-System → Event/Result → UI-Projektion/Feedback; UI-Fokus kann Weltaktionen blockieren. UI darf bei Buttonklick nicht heimlich einen zweiten Inventarbestand pflegen.

**Beziehungen:** Runtime (01), Zustände (03), Kampf (09), Inventar (10), Quest (12), Rendering (14), Save/Settings (17).

**Fehler:** Menü offen, aber Bewegung läuft weiter; Gamepad kann den Fokus nicht erreichen; UI zeigt alten HP-Wert; doppelte Klicks kaufen zweimal; Remapping kollidiert; Texte sind nicht lesbar.

**Tests:** Tastatur/Controller und Fokuswechsel; Escape/Back; Modal vor Weltinput; falsche/fehlende Daten; kleine Auflösung; lesbare Zustandsrückmeldungen; echte Bedienung durch Agent und Nutzer getrennt bewerten.

**Prompt:** „Gehe eine Benutzeraktion durch: Eingabe → Intent → validiertes Ergebnis → UI. Teste Fokus, Modal, Controller, Fehlermeldungen und tatsächliche Lesbarkeit.“
