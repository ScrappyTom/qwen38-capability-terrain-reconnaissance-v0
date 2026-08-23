# Direct transcript audit

## Exact continuation boundary

Call 21 contained 42 messages: the updated system message, the unchanged task,
and the exact 40-message action/result history from calls 1 through 20. Its
last two messages were the call-20 `check` action and the literal failed-check
result showing:

```text
expected beta-1
observed acme-1
```

The task hash remained
`01d842aae5603fc02f1394323bed7c4278fb542c2724e8bcd30e77997827060d`.
The only model-facing change was `at most 20 model calls` to `at most 28 model
calls`. The request still contained the earlier exact issue text stating that
expired jobs return to pending in their original ordering position and that
pending work is dispatched by descending priority and FIFO tie order.

## Literal eight-call trajectory

The continuation performed three reads of `tests/test_dispatcher.py`, three
admitted patches to that file, and two failed visible checks. It made no
product-code change, no rejected action, no submission, and no reread of the
issue, API, or dispatcher implementation.

1. Call 21 reread the complete failing test file.
2. Call 22 swapped `acme-1` from priority 9 to 8 and `beta-1` from 8 to 9 so
   that beta would win after expiry. This made beta win the *first* lease, and
   call 23's exact check exposed that new failure.
3. Call 24 reread the test. Call 25 restored priorities 9 and 8 but asserted in
   its comment that expired `acme-1` was still active and tenant `a` remained
   at its limit. Call 26 again showed the original mismatch: the implementation
   returned `acme-1`, not `beta-1`.
4. Call 27 reread the test. Call 28 changed the second lease time from 30 to 31
   while retaining the beta expectation. Because `expires_at <= now` expires
   the lease at both times, this did not change the governing state. The
   external audit confirms the final test still fails.

The three patches were not byte-identical no-ops. They were distinct local
attempts organized around one invariant but false semantic conclusion. Qwen
adapted test inputs and timing to preserve the expected `beta-1` result rather
than comparing that expectation with the governing priority-plus-original-
position rule.

## Artifact and verification audit

The continuation began at candidate
`e3dc07130fe13716ff9e36fa7ce9b73e32e51bfe77057e4ba0cd627f81107441`
and ended at
`3a6cc5a3110df45258233488010c4c7219d94521da86532477b193187aba97e9`.
The complete phase diff changes only the one test's comment and second lease
time. The external audit remains 13/14: all 13 product-behavior groups pass,
and 22 of 23 candidate tests pass. The sole failure remains the same incorrect
beta expectation.

The continuation verifier independently reproduced all 40 checkpoint
messages, all eight new requests, eight strict actions, eight tool results,
41 custody records, 289 artifact references, 45 snapshot references, and the
final candidate identity.

## Behavioral interpretation

The administrative continuation did not improve quality or establish natural
closure. The actor was still changing bytes at call 28, so `turn_limit`
remains an administrative status. But its marginal work had become a repeated
semantic mechanism: three changes preserved the same wrong expected outcome,
two exact checks contradicted it, and no action returned to the governing
record.

This is more specific than either “not enough turns” or “truth was absent.”
The required rule and the failing observation were both present. The current
decision environment foregrounded the local failing test, and the model
optimized that test around a fixed interpretation instead of reopening the
relationship between expiration, pending restoration, and priority.
