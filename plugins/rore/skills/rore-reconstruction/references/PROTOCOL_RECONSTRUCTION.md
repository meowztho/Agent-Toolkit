# Protocol Reconstruction

Recover message framing, state transitions and serialization semantics from captures, logs, binaries, clients or other authorized evidence.

## Acquisition / triage
Record direction, connection/session identity, handshake/heartbeat/reconnect behavior, candidate magic/fixed headers, lengths, TLV/fixed layout, compression and encryption indicators.

## Frame/layout recovery
Align comparable messages and identify invariant vs changing bytes. Test endianness, length semantics, sequence IDs, checksums/MAC positions and message/opcode identity.

## State model
Reconstruct a protocol state machine such as:

```text
Connect → Authenticate → Ready → Request/Response → Close/Recover
```

Use only states supported by evidence; keep unknown transitions explicit.

## Serialization / transforms
Recover protobuf/JSON/custom binary structures, compression and encryption/key-derivation relationships where observable. A decoder producing output does not prove the schema or object identity is correct.

Controlled replay/field variation is allowed in authorized environments when needed to understand semantics, beginning with low-impact changes and stopping once the mechanism is understood.

Produce message identities (`PROTO-###`), field hypotheses, sample evidence and reproducible decode steps/scripts when useful.

For saved HAR, packet captures or logs, preserve producer identity/version, original record order and raw payload representation. Inspect offline captures as historical evidence; recorded URLs or historical process IDs are not live targets. Distinguish missing body, empty body, decoded text and authenticated raw bytes. Redaction can remove fields needed for a conclusion, so mark their coverage unknown. For asynchronous exchanges, represent required happens-before relationships and alternative valid orderings instead of forcing one observed total sequence into the protocol model.
