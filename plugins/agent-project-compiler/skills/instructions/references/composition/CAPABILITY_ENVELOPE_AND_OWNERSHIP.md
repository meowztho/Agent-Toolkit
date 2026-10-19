# 7. Product Capability Envelope + system discovery protocol

Before the final `SYSTEM_MAP`, infer a provisional **Product Archetype** and **Expected Capability/Responsibility Envelope** from the confirmed vision, reference traits, product modality and general domain knowledge. This lets the compiler contribute knowledge the later implementation agent may not have in active context.

The envelope is a coverage surface, not a class/file/service list. It answers: *what ordinary responsibilities/capabilities should a competent designer/engineer at least consider for this requested product?* A responsibility may ultimately live inside an existing owner, be configuration/content, be deferred, be not applicable, or require a user decision. Do not create systems merely to make the envelope look complete.

A useful decomposition test is to expand user-visible outcomes until the required semantic supports become visible. For example, a multi-participant interactive flow implies participant/slot instances and some source of control/actions; an actor that can perform actions normally implies state, action mapping and presentation/runtime consequences. These are inference prompts, not mandated names/mechanics. Continue only as deep as needed to expose durable responsibilities, reuse seams and integration paths.

During project compilation:

1. preserve the whole user vision/reference semantics;
2. infer a provisional product archetype + expected capability/responsibility envelope;
3. run the domain-expert omission challenge and disposition every material envelope item;
4. identify user-visible product areas/workflows and required actors/instances/providers;
5. identify authoritative state/decisions, repeated/stateful and cross-cutting responsibilities;
6. identify future variation that should be data/config/module/provider rather than new owners;
7. propose canonical Responsibility Owners/master systems and capability contracts;
8. inspect relationships, producer convergence and ownership conflicts;
9. ask the user only if boundaries/behavior materially change user-owned product semantics;
10. challenge the map with representative/adversarial cases when reuse/extensibility matters;
11. compile `contracts/SYSTEM_MAP.yaml` and `CAPABILITY_GRAPH.yaml` where needed;
12. require Fresh-Agent Reconstruction before final fine-grained task decomposition;
13. create bounded Blueprints/specs beneath those systems.

Do not let the coding agent decide the fundamental system topology from scratch when the compiler can derive it from confirmed intent.

Reversible implementation details inside a system remain delegated.

---

# 8. Ownership and runtime integration layer

`SYSTEM_MAP.yaml` says which master system owns a durable responsibility. For material cross-system rules/state/configuration, also generate `contracts/SYSTEM_INTEGRATION.yaml` using `SYSTEM_INTEGRATION_AND_RUNTIME_TRACE_GUIDE.md`.

This second contract distinguishes decision owner, state owner, producers, allowed writers and consumers; it records producer -> contract/data -> consumer paths and prevents two locally plausible systems from implementing the same rule independently.

A composition is not proven reusable merely because it references shared systems in YAML; runtime must actually consume those systems/data through the canonical path.

---

# 9. System-level acceptance

A master system is not proven merely because one consumer works.

Where important, acceptance should prove:
- the canonical owner exists;
- consumers use it through the intended interface;
- no duplicate owner exists;
- configuration/profiles/modifiers work without forking the system and relative modifiers inherit canonical base changes;
- at least one additional representative consumer can reuse it where relevant.

Example:

```text
AC-SYS-INPUT-01
- UI and external/API producers both route through the same semantic command registry
- consumer A and B do not own separate command parsers
- mapping/config changes update behavior without consumer-local code changes
```

---

# 10. Skill boundary

System composition determines **which capabilities are needed**, but skill lifecycle/routing is a separate authority. Use `SKILL_NATIVE_COMPILER_GUIDE.md` for `contracts/SKILL_REQUIREMENTS.yaml`, installed/global/project/harness discovery, external GitHub review, minimal JIT activation, and project-local skill generation.

Invariant:

```text
SYSTEM_MAP / system authorities = what exists and how it must behave
SKILL_REQUIREMENTS / skills       = how an agent performs recurring work
```

Never put project truth into a skill, and never duplicate skill-resolution policy in this guide.

---

# 11. Bootstrap prompt boundary

System composition must be visible in the initial implementation context, but this guide does not own prompt construction. `BOOTSTRAP_PROMPT_AND_GOAL_GUIDE.md` defines the context-rich START/GOAL/CONTINUE policy.

Invariant: a fresh implementation agent should see the master-system/composition model directly in its initial orientation instead of having to infer it from a pointer chain.

---

