# v2.30 Project-native engine model

For products with repeatable objects/records/workflows/surfaces/providers, compile a **project-native engine model** from existing owners rather than creating a new universal Engine system.

The model should identify:

```text
reusable Definition Type contract
definition/profile source
capabilities/modules it may compose
allowed modifiers/replacements
generic runtime/surface consumer
mutable instance-state owner
authoring/registration path
```

A project can therefore expand by registering/authoring definitions and composing existing modules.

Generic pattern:

```yaml
definition_type:
  id: TYPE-...
  owner: SYS-...
  public_contract: CAP-...
  definition_schema: DATA-...
  allowed_capabilities: [CAP-...]
  allowed_modifiers: [MOD-...]
  runtime_consumer: MOD-...
  surface_consumer: MOD-...
  instance_state_owner: SYS-...
```

Use only the fields that are material. This is a semantic relationship, not a requirement to create one physical file/class per field.

## Generic consumer invariant

When a consumer can render/execute any valid definition of a reusable Definition Type, adding a new definition must not require duplicating that consumer.

Examples of generic consumers include detail surfaces, workflow runners, exporters, schedulers, renderers, evaluators and runtime hosts. The exact form is domain-specific.

Consumer Composition != Definition Ownership != Runtime State Ownership.

## Category / grouping invariant

If grouping/taxonomy is data-driven, adding an item to an existing category should normally change the item's definition/reference or category registry, not create another category implementation. Creating a new category normally creates another definition/registry entry unless the category itself introduces new reusable behavior requiring a Capability change.


# v2.31 Definition-Type authority boundary

`Product Archetype` is only a compiler discovery hypothesis about the kind of product being built.

`Reusable Definition Type` is a project architecture concept for repeatable domain instances.

Never conflate them.

Do **not** create a universal `ARCHETYPES.yaml` / `DEFINITION_TYPES.yaml` merely because v2.30/v2.31 uses this semantic model. Store Definition-Type metadata in the existing canonical domain/content/definition/Blueprint authority that already owns those definitions. Create a dedicated contract only when no existing authority can own the semantics without ambiguity and the project materially needs it.

# v2.31 Composition coherence

A composition may be structurally valid yet product-incoherent if its dependent projections disagree.

For material relationships, route to `SYSTEM_INTEGRATION`:

```text
canonical source owner
→ declared relation/derivation
→ dependent consumer/projection A
→ dependent consumer/projection B
→ Acceptance evidence
```

The composition definition may reference the invariant ID; it must not duplicate the invariant's owner/derivation semantics.
