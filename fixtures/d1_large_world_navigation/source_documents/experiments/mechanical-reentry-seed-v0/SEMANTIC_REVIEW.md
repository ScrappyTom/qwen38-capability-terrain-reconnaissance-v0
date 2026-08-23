# Investigator semantic review

The investigator reviewed terminal artifacts against the exact Phase-B task
and authoritative records. The supporting audits are not treated as semantic
graders.

## Code

All three implementations meet the complete executable contract: 10/10 audit
groups, including current package tests. Direct source review confirms that
`revise` preserves identity/order and increments revision, `rename` changes
only subject, validation and failure paths preserve state/counters, exports are
correct, and lifetime counter behavior remains intact.

The model-authored tests are separately assessed:

| Condition | Product | Own tests | Qualitative coverage |
|---|---:|---:|---|
| T transcript | 10/10 | pass | Covers v2 revise identity and rename success/failure; omits an explicit invalid-body revise state case and full rename validation matrix. |
| W fresh world | 10/10 | pass | Strongest suite: adds invalid-body/missing revise state coverage; still omits the full rename type/whitespace validation matrix. |
| M mechanical | 10/10 | pass | Covers v2 revise identity/order and rename success/failure; omits an explicit invalid-body revise state case and full rename validation matrix. |

## Research

| Criterion | T | W | M |
|---|---|---|---|
| Final attendance estimate, interval, nonrandom design, causal limit | met | met | met |
| Emergency estimate and interval explicitly inconclusive | met | met | met |
| Mechanism bounded to registered residents; no emergency causation | met | met | met |
| Fully allocated cost point, range, and components | met | met | met |
| Post-8 p.m. missingness and unknown bias direction | met | met | met |
| Renter underrepresentation and limited generalization | met | met | met |
| Mortality, indoor temperature, long-term health unmeasured | met | met | met |
| H9 four-neighborhood twelve-month extension replaces H6 | met | met | met |
| Citywide deployment remains unauthorized | met | met | met |
| Only current claim-local citations govern | met | met | met |
| No unsupported factual, causal, or decision claim | partial | met | met |

T's partial is limited to: “the planning range reflects uncertainty in
allocation.” H8 reports the range and included components but does not state
what produces the range. The phrase does not reverse the decision, but it is a
new explanation and is therefore not counted as fully supported.

W and M are 11/11 on the rubric. T is 10 met / 1 partial. This is one
trajectory per cell and cannot establish a reliability difference.
