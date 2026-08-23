# GPU authorization boundary

Stage 0 performs no model inference.

After this repository has a frozen, pushed commit, a measured run requires a
new owner authorization naming that exact commit. The external authorization
receipt must bind:

- `scope`: `qwen38-capability-terrain-reconnaissance-v0`;
- the exact frozen commit;
- one exact run ID;
- at most 42 actor calls across D1-D6;
- `one_attempt_per_call`: `true`; and
- zero retries.

D6 uses zero model calls when the prospective null condition fires. Unused
calls are not reassigned. No cell is extended and no second seed follows from
this authorization.

The authorization also covers execution of model-authored JavaScript for D3,
D4, and D5 by the exact locked Node runtime. Evaluation runs against a
disposable candidate copy, uses a disposable evaluator copy, records pre/post
manifests, and kills the evaluator process tree on timeout. This is an
integrity boundary, not an operating-system security sandbox: the process has
the host user's ambient OS permissions. Do not authorize the measured tranche
unless that residual execution risk is acceptable on this machine.
