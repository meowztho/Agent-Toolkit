# Mobile / Platform Reconstruction

Use when APK/IPA/mobile runtime or platform packaging materially shapes the reference.

Combine as applicable:
- package/manifest/entitlement/permission inventory;
- Java/Kotlin/Swift/ObjC/native library static analysis;
- resources/layout/assets;
- component/lifecycle/IPC/deep-link relationships;
- runtime observation and hooks;
- network/API behavior;
- persistent storage/keychain/preferences/databases;
- native `.so`/framework handoff to static/runtime analysis.

Rebuild/re-sign/reinstall or hook an authorized local copy only when the intervention is needed to test a reconstruction hypothesis. A bypass technique is not itself a RORE goal; use the smallest intervention that reveals hidden behavior or enables observation, then record the changed boundary.

Separate platform/framework behavior from application-specific findings.

For Android, preserve the exact APK/split identity, manifest/component declarations, resources, DEX classes and overload signatures, and native-library handoffs. A Java-like decompiler view is a projection; inspect bytecode/Smali or raw resources when the source-like view is ambiguous, malformed or omits a material branch. Distinguish declared permissions and exported components from exercised behavior. For Apple packages, path conventions may identify candidate extensions, frameworks or helpers, while parsed plists, entitlements, load commands and runtime observation establish their actual roles. Keep missing split packages, external frameworks and protected resources visible as coverage gaps.
