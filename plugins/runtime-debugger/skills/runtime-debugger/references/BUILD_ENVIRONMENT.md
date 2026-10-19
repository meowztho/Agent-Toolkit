# Build & Environment Debugger

**Trigger:** works in developer environment but fails in clean install, release, package, service or another supported platform.

1. Identify supported targets, pinned dependencies, toolchain/runtime versions, configuration precedence, environment variables, path/permission assumptions and generated artifacts.
2. Compare real source → build → package → install → start → user-visible/CLI/API behavior. Ensure the running binary matches the expected revision/build identity.
3. Test applicable conditions: clean build, missing dependency, cache contamination, stale artifacts, release flags, bundled assets, file encodings, paths, cross-platform differences and service launch context.
4. Reuse the project's existing build/CI process and an isolated disposable install location. Avoid changing user-wide dependencies or settings unless explicitly authorized.
5. A successful compile alone does not prove that the packaged application starts or behaves correctly.
6. Report exact reproducible command/environment differences, artifact identity, observed failure and smallest correction; keep product code read-only.
