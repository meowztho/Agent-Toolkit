# Integration & Data Integrity Debugger

**Trigger:** inconsistent frontend/backend behavior, lost data, stale state, API/schema mismatch, persistence or cache issues.

1. Trace one representative real input through producers, validation, public contracts, translations, persistence, consumers and externally visible output.
2. Check schema/default drift, optional/null handling, serialization, units, identity/versioning, request/response ordering, retries, duplicate writes, transaction boundaries, cache invalidation and read-back.
3. Distinguish legitimate language-specific DTOs from duplicated independent ownership of domain rules.
4. Exercise success and negative/retry paths with isolated reversible test data. Include save → reload/read-back when persistence is part of the claim.
5. Do not use production mutations, real external payments/messages or destructive actions merely for evidence. Mark unavailable external evidence UNVERIFIED.
6. Report exact broken contract/transition, traceable inputs/outputs and the smallest canonical fix direction without editing product code.
