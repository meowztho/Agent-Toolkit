# [Product Name] — Blueprint

> Canonical, compact entry point for reconstructing the product. Read this file first.
> For structured APC projects, `PROJECT_INDEX.yaml` remains the canonical JIT authority router;
> this overview links to existing authorities rather than duplicating their rules.

## Identity & intended experience
- **Purpose:** [Which problem does this product solve?]
- **Users & environment:** [Who uses it, where and with what constraints?]
- **Experience/design identity:** [Distinctive behavior and visual style; reference canonical design authority when present.]
- **Scope & exclusions:** [Required result; explicitly excluded or deferred behaviors.]

## Representative user behavior
- **Primary scenario:** [Trigger → observable outcome; link canonical flow if present.]
- **Important failure/recovery:** [What the user sees and how the system responds.]
- **Critical prohibitions:** [What must never happen, or link to existing guardrail authority.]

## Required capabilities
| ID | Observable outcome | Governing authority / scoped contract | Acceptance |
| --- | --- | --- | --- |
| CAP-001 | [What the user can do] | [ID/path] | [AC-ID] |

## Responsibility boundaries
| Responsibility | Canonical runtime owner | Public capability / contract | May not own |
| --- | --- | --- | --- |
| [Specific rule or state] | [SYS-ID] | [CONTRACT-ID] | [Forbidden foreign responsibilities] |

## End-to-end behavior
- **Entry → result:** [Minimal complete primary-user path; link to canonical APP_FLOW when present.]
- **Recovery / error path:** [Important observable failures and how to recover.]
- **Persistence / lifecycle:** [What survives restarts, sessions or state changes.]

## Design and external dependencies
- **Design:** [Canonical UI/style/reference IDs and paths; material whole-surface qualities.]
- **Data/assets:** [Canonical schema/asset IDs and paths, including sources/licensing where material.]
- **External systems:** [Contract IDs, availability/failure assumptions and substitution policy.]
- **Runtime / installation:** [Supported platforms, required dependencies and bootstrap authority.]

## Scoped reconstruction
To work on one area, resolve its stable contract ID (via `PROJECT_INDEX.yaml` / existing
registry if available), then load that contract, applicable project-wide invariants,
transitive *public dependency contracts*, and relevant acceptance + references. Do not
load unrelated implementation internals or silently implement another owner's rules.

## Verification & unknowns
- **Evidence boundary:** [Verified against which build/revision/environment; separate claimed vs independently checked.]
- **Acceptance entry:** [Canonical acceptance matrix / tests, or local acceptance IDs.]
- **Observed evidence:** [Evidence index / representative product paths, if available.]
- **Known gaps:** [Unresolved behavior / external facts; never silently assume.]
- **Reconstruction target:** [Functional / behavioral / visual / operational, scoped as needed.]

<!-- Project rules:
     1. Each fact has one normative owner; link rather than repeat.
     2. Keep this file as short as an agent can read to form the correct product model.
     3. Only split a domain when its boundary warrants independent understanding,
        change, verification, reuse, or separate handoff.
     4. Remove instructions/placeholders that do not apply.
-->
