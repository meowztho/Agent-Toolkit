#!/usr/bin/env python3
from pathlib import Path
import hashlib, json, sys

ROOT = Path(__file__).resolve().parent
EXPECTED_VERSION = "0.11.7"
EXPECTED_SKILLS = {
    "core-first-orchestration",
    "core-first-extension-architecture",
    "observable-product-verification",
    "core-first-verifier",
    "independent-review",
}
PROTECTED_HASHES = {'core-first-governance/skills/core-first-extension-architecture/SKILL.md': '4872a4a1c3fc4a37f895608a2b1558ca67a90d379da039a96c41ec38dcac4e09', 'core-first-governance/skills/core-first-extension-architecture/agents/openai.yaml': '558b26d5e24e7dbdd2b87f98963521ed1b0ada85ad5d7a33fa727ab7e0031e26', 'core-first-governance/skills/core-first-extension-architecture/evals/evals.json': '70d38acfa30812acdca4793c73442d6847b0ca215a3c33f6cdd268600636bc2b', 'core-first-governance/skills/core-first-extension-architecture/references/CONDITIONAL_PROFILES.md': 'ad856fefe2a61fdb126cb26d6bf5c0d5f870fd6c5f1855ce774e21d2546b4d17', 'core-first-governance/skills/core-first-extension-architecture/references/EXTENSION_ARCHITECTURE_METHOD.md': '55ba875d5d2e1b2ba42bef92ce5cbaf08c38008a9a4ee45fbbd990261730248f', 'core-first-governance/skills/core-first-orchestration/SKILL.md': 'd29e8601a90b51c9fe7cbc023f2652a2702e9d645424263c648acba73c201ec6', 'core-first-governance/skills/core-first-orchestration/agents/openai.yaml': '7d134d23fd60466e3f665f5d67ca11abcc6ba90bba59592a0ef8eca45db23299', 'core-first-governance/skills/core-first-orchestration/evals/evals.json': '4cede292e10a3bd57ea5d197098671558e6d6ae7912fb135cbf624b9fd35385b', 'core-first-governance/skills/core-first-orchestration/references/ADAPTIVE_EXECUTION_AND_CONTEXT.md': 'fd1e900163e6ca59e783d0ed5100cecad0e2fe19690cb9d54e21c62f97a27efc', 'core-first-governance/skills/core-first-orchestration/references/DELEGATION_CONTEXT.md': 'a64004b279b978151f314a2ef832b6702408c0ce09d95abc4314f11c28185672', 'core-first-governance/skills/core-first-orchestration/references/EVIDENCE_DRIVEN_DEBUGGING.md': '642335262f885bc7c82abee2544932242c2ca2007385216558dea332ad4ff885', 'core-first-governance/skills/core-first-orchestration/references/GROUNDED_EXECUTION_PREFLIGHT.md': '4bcb77ddaaa59eb5b8e1d4826d94ef1c6d28c168e0f10e037ad67ba4c0ca6799', 'core-first-governance/skills/core-first-orchestration/references/VERIFICATION_AND_COMPLETION_ROUTING.md': '02c6bc80510ccbebd3ee6042106e8142e44ddf183cb5021755639ea4c39566aa', 'core-first-governance/skills/core-first-verifier/SKILL.md': 'f2c5066e7f04765d60dbea68684e4a43a1f8d2f4fe90837e966865d8046c1810', 'core-first-governance/skills/core-first-verifier/agents/openai.yaml': '5fa79868ff709338383f1275273997f4e3acef64598c4506072d4c5788673661', 'core-first-governance/skills/core-first-verifier/evals/evals.json': 'c9126e734cfd141b6ef38877716b4f363b609d5e7b8a316f5914f7b35c24d0f5', 'core-first-governance/skills/independent-review/SKILL.md': 'dbf58c8527931ae32b647dbd865a190f02f64f62d71e741659f1f6ba13ef0dc4', 'core-first-governance/skills/independent-review/agents/openai.yaml': 'c34fc1ee88d8e42f07e90c797264607244a66a4b853465145e2c640190807057', 'core-first-governance/skills/independent-review/evals/evals.json': 'dc03ea10b4acef05cd3e308cda44f62ab0eb43e95b3c481ed601b244e3848292', 'core-first-governance/skills/observable-product-verification/SKILL.md': '1d2f4531089fa2ac3ccbbfa1c878475b0401433d9e8b3d842c67ac1bfa7404cb', 'core-first-governance/skills/observable-product-verification/agents/openai.yaml': '21ec5b33ced01466f91acdd9166765bb422f0004b95ffe4c9f24143cf5c7c2b8', 'core-first-governance/skills/observable-product-verification/evals/evals.json': 'b973dbccbafe8c4237c2e5c4af45c5f9276235b6bea2239c56202cb4c2e13ac7'}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fail(message: str) -> None:
    print(f"RELEASE VALIDATION: FAIL\n{message}")
    raise SystemExit(1)


def main() -> None:
    manifest_path = ROOT / "core-first-governance/.codex-plugin/plugin.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("version") != EXPECTED_VERSION:
        fail(f"plugin_version={manifest.get('version')!r}, expected {EXPECTED_VERSION}")

    prompt = str(manifest.get("interface", {}).get("defaultPrompt", "")).lower()
    if "non-trivial" in prompt or "nontrivial" in prompt:
        fail("defaultPrompt reintroduces removed subjective non-trivial routing language")

    skills_root = ROOT / "core-first-governance/skills"
    skills = {p.name for p in skills_root.iterdir() if p.is_dir() and (p / "SKILL.md").is_file()}
    if skills != EXPECTED_SKILLS:
        fail(f"skills={sorted(skills)!r}, expected {sorted(EXPECTED_SKILLS)!r}")

    for rel, expected in PROTECTED_HASHES.items():
        path = ROOT / rel
        if not path.is_file():
            fail(f"protected file missing: {rel}")
        actual = sha256(path)
        if actual != expected:
            fail(f"protected hash mismatch: {rel}\nexpected={expected}\nactual={actual}")

    orchestration = skills_root / "core-first-orchestration"
    kernel_bytes = (orchestration / "SKILL.md").stat().st_size
    jit_refs = sorted((orchestration / "references").glob("*.md"))
    total_proc_bytes = kernel_bytes + sum(p.stat().st_size for p in jit_refs)
    if kernel_bytes != 10998:
        fail(f"orchestration_kernel_bytes={kernel_bytes}, expected 10998")
    if total_proc_bytes != 27335:
        fail(f"orchestration_total_procedure_bytes={total_proc_bytes}, expected 27335")

    opv_eval_path = skills_root / "observable-product-verification/evals/evals.json"
    opv_evals = json.loads(opv_eval_path.read_text(encoding="utf-8"))
    serialized = json.dumps(opv_evals)
    required = [
        "fresh-capture-does-not-prove-oracle-liveness",
        "identical-static-observations-do-not-prove-dead-oracle",
    ]
    for eval_id in required:
        if eval_id not in serialized:
            fail(f"missing OPV regression eval: {eval_id}")

    handoff = ROOT / "CONTEXT_HANDOFF_2026-10-06_v0.11.6.md"
    if not handoff.is_file():
        fail("v0.11.6 context handoff missing")

    sums = ROOT / "SHA256SUMS.txt"
    if not sums.is_file():
        fail("SHA256SUMS.txt missing")
    for raw in sums.read_text(encoding="utf-8").splitlines():
        raw = raw.strip()
        if not raw:
            continue
        expected, rel = raw.split(None, 1)
        rel = rel.removeprefix("./")
        path = ROOT / rel
        if not path.is_file():
            fail(f"SHA256SUMS entry missing: {rel}")
        actual = sha256(path)
        if actual != expected:
            fail(f"SHA256SUMS mismatch: {rel}")

    print("RELEASE VALIDATION: PASS")
    print(f"plugin_version={EXPECTED_VERSION}")
    print(f"skills={len(skills)}")
    print(f"orchestration_kernel_bytes={kernel_bytes}")
    print(f"orchestration_total_procedure_bytes={total_proc_bytes}")
    print("oracle_liveness_current_state_guard=PASS")
    print("identical_static_samples_reverse_guard=PASS")


if __name__ == "__main__":
    main()
