#!/usr/bin/env python3
import json, os, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = {"rore-orchestration", "rore-reconstruction", "rore-evidence-review"}
REQUIRED = [
    "plugin.json", ".codex-plugin/plugin.json", "README.md", "SOURCE_PROVENANCE.md",
    "mcp.json", "pyproject.toml", "uv.lock", "scripts/rore.py", "scripts/rore_mcp.py",
    "scripts/rore_provider_mcp.py", "rore_runtime/provider_jobs.py",
    "rore_runtime/bundle.py", "rore_runtime/rea_bridge.py", "docs/EVIDENCE_BUNDLE_V1.md",
    "rore_runtime/artifact_tools.py", "rore_runtime/binary_layout.py", "docs/NATIVE_ARTIFACT_TOOLS.md",
    "skills/rore-reconstruction/references/GHIDRA_STATIC_PROVIDER.md",
    "docs/GHIDRA_PROVIDER_ADAPTER.md", "scripts/rore_ghidra.py",
    "rore_runtime/ghidra_adapter.py", "providers/ghidra/ROREExport.java",
    "docs/PROVIDER_SETUP.md", "scripts/rore_setup.py", "rore_runtime/provider_setup.py",
    "skills/rore-reconstruction/references/PROVIDER_PROVISIONING.md",
    "skills/rore-reconstruction/references/PROVIDER_SEEDS.md",
    "skills/rore-orchestration/references/BROAD_COVERAGE_CAMPAIGN.md",
    "skills/rore-reconstruction/references/MULTI_REFERENCE_EXTENSION_SEAMS.md",
    "scripts/rore_imgdiff.py",
    "THIRD_PARTY_NOTICES.md", "LICENSE-UPSTREAM", "LICENSE-REVERSE-SKILL", "LICENSE-REA", "LICENSE-COREREPLICA",
    "docs/USER_VISION.md", "docs/INTERVIEW_LEDGER.md", "docs/SYSTEM_MAP.yaml", "docs/CAPABILITY_GRAPH.yaml",
    "docs/ARCHITECTURE_GUARDRAILS.yaml", "docs/DECISION_COMPENDIUM.md",
    "docs/ACCEPTANCE.yaml", "docs/PROJECT_INDEX.yaml", "docs/SYSTEM_INTEGRATION.yaml",
    "skills/rore-orchestration/SKILL.md", "skills/rore-reconstruction/SKILL.md",
    "skills/rore-evidence-review/SKILL.md",
]


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def fail(msgs, msg):
    msgs.append(msg)


def structural_checks():
    e=[]
    for path in ROOT.rglob("*"):
        if ".venv" in path.parts or ".git" in path.parts:
            continue
        if "__pycache__" in path.parts or path.suffix in {".pyc", ".pyo"}:
            # Local ignored bytecode may exist after running tests; it is not a
            # package member. An extracted release without Git still rejects it.
            if subprocess.run(["git", "check-ignore", "-q", "--", str(path)], cwd=ROOT,
                              stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0:
                continue
            fail(e, f"generated Python artifact must not ship: {path.relative_to(ROOT)}")
    for rel in REQUIRED:
        if not (ROOT/rel).is_file(): fail(e, f"missing {rel}")
    try:
        p=json.loads(read("plugin.json"))
        c=json.loads(read(".codex-plugin/plugin.json"))
    except Exception as exc:
        return [f"manifest parse: {exc}"]
    if p.get("name") != "rore": fail(e, "backend plugin identity must be rore")
    if c.get("name") != p.get("name"): fail(e, "compatibility manifest identity differs")
    if not re.fullmatch(r"\d+\.\d+\.\d+", str(p.get("version", ""))): fail(e, "version must be semantic x.y.z")
    if c.get("version") != p.get("version"): fail(e, "compatibility manifest version differs")
    try:
        mcp=json.loads(read("mcp.json"))
        runtime_version=re.search(r'^version\s*=\s*"([^"]+)"',read("pyproject.toml"),re.M)
        if not runtime_version or runtime_version.group(1) != p.get("version"): fail(e, "runtime version differs")
        server=mcp["mcpServers"]["rore-evidence"]
        if server.get("type") != "stdio" or "${PLUGIN_ROOT}/scripts/rore_mcp.py" not in server.get("args", []):
            fail(e, "MCP launch does not point to packaged read-only adapter")
        provider=mcp["mcpServers"]["rore-providers"]
        if provider.get("type") != "stdio" or "${PLUGIN_ROOT}/scripts/rore_provider_mcp.py" not in provider.get("args", []):
            fail(e, "provider MCP launch does not point to packaged adapter")
    except Exception as exc:
        fail(e, f"runtime manifest parse: {exc}")
    iface=p.get("extensions",{}).get("com.openai",{}).get("interface",{})
    if iface.get("displayName") != "RORE": fail(e, "displayName must be RORE")
    if c.get("interface",{}).get("displayName") != "RORE": fail(e, "codex displayName must be RORE")

    found={d.name for d in (ROOT/"skills").iterdir() if (d/"SKILL.md").is_file()}
    if found != SKILLS: fail(e, f"skill set mismatch: {sorted(found)}")

    active="\n".join(read(x) for x in [
        "skills/rore-orchestration/SKILL.md",
        "skills/rore-reconstruction/SKILL.md",
        "skills/rore-evidence-review/SKILL.md",
        "docs/SYSTEM_MAP.yaml", "docs/CAPABILITY_GRAPH.yaml", "docs/SYSTEM_INTEGRATION.yaml"
    ])
    for forbidden in ("corereplica-product", "corereplica-build", "corereplica-release", "CR_PRODUCT", "CR_BUILD", "CR_RELEASE"):
        if forbidden in active: fail(e, f"active downstream owner residue: {forbidden}")
    if "Agent Project Compiler" in active or re.search(r"\bAPC\b", active):
        fail(e, "active RORE architecture must not depend on APC")

    recon=read("skills/rore-reconstruction/SKILL.md")
    for phrase in (
        "reference's own structure", "Negative Evidence", "continue | switch | stop",
        "sufficient mechanism understanding", "Evidence", "Finding", "Path", "Model"
    ):
        if phrase not in recon: fail(e, f"reconstruction contract missing: {phrase}")

    perturb=read("skills/rore-reconstruction/references/PERTURBATION_AND_CAUSAL_PROBING.md")
    for phrase in ("baseline", "one material dimension", "trace", "restore", "sufficient mechanism understanding", "not exploit"):
        if phrase.lower() not in perturb.lower(): fail(e, f"perturbation contract missing: {phrase}")

    review=read("skills/rore-evidence-review/SKILL.md")
    for phrase in ("read-only", "do not mutate", "do not silently", "Path integrity", "Reference-native fidelity"):
        if phrase.lower() not in review.lower(): fail(e, f"review contract missing: {phrase}")

    model=read("skills/rore-reconstruction/assets/reference-model.md")
    for ident in ("SUR-###", "FLOW-###", "STATE-###", "COMP-###", "ENT-###", "PROTO-###"):
        if ident not in model and ident == "STATE-###":
            # STATE identity is documented in the reconstruction skill; template may represent it through models.
            if ident not in recon: fail(e, f"stable identity missing: {ident}")
        elif ident not in model: fail(e, f"stable identity missing: {ident}")

    return e


def run_tests():
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    return subprocess.run([sys.executable,"-m","unittest","discover","-s","tests","-v"],cwd=ROOT,env=env).returncode


def main():
    errors=structural_checks()
    if errors:
        print("RORE structural gate: FAIL")
        for x in errors: print("-",x)
        return 1
    print("RORE structural gate: PASS")
    code=run_tests()
    if code:
        print("RORE regression gate: FAIL")
        return code
    print("RORE regression gate: PASS")
    return 0

if __name__=="__main__": raise SystemExit(main())
