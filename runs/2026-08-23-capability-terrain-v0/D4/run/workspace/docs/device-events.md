# Device event folding contract

`foldDeviceEvents(events)` returns a new array describing the latest active state of every device.

- `events` must be an array. Every event must be a non-null, non-array object with a non-empty, already-trimmed string `deviceId`, a positive integer `sequence`, and `kind` equal to `snapshot`, `patch`, or `delete`.
- Process each device independently by ascending `sequence`, regardless of input order. Its sequence must start at 1 and remain contiguous. Duplicate or missing sequence numbers are errors.
- The first event for a device must be `snapshot` and must contain a plain-object `state`. No later event may be a snapshot.
- A `patch` must contain a plain-object `changes`. A change whose value is `null` deletes that key; every other value replaces or adds the key.
- A `delete` removes the device from the result and must be its final event.
- Return active devices in the order each `deviceId` first appeared in the original input. Each entry is `{ deviceId, sequence, state }`, where `sequence` is the last applied sequence.
- Do not mutate or retain nested object references from caller-owned events, states, or changes.

Invalid container, identifier, kind, state, or changes shapes throw `TypeError`. Invalid sequence numbers or event-protocol order throw `RangeError`.
