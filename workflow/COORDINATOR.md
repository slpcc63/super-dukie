# Central coordinator
This conversation is the initial coordinator. A replacement coordinator starts from START-HERE.md.
Shannon can request: "This thread failed. Give me the handoff to continue Issue 4."
The coordinator reads current main, verifies issue state, selects the exact next task and creates the handoff.
A handoff contains repository URL, pinned base commit, issue/stage/page, source paths, scoped references with availability and hashes, approvals/exceptions, corrections, attempt counters, usage scope, blockers, next action and stop condition.
A handoff is an assignment, not a new approval or a substitute for actual reference bytes.
Only ask Shannon for a missing decision or inaccessible item after using available records. Never require Shannon to reconstruct the story or assemble phone ZIPs.

## Checkpoint transaction
1. Pull/read current main and record expected parent.
2. Save immutable candidate and its prompt, inputs, review/error, and source hashes.
3. On Shannon approval, add exact wording, message/source and scope to the approval ledger, tied to the candidate hash.
4. Update status and dependencies without promoting acceptance to QA/print-ready.
5. Validate and commit all related changes in one transaction; update main without force, then verify.
6. Supply commit and next action. If remote save is unavailable, package local changes and state that remote sync is pending.
Do not consume an approved retry after terminal failure unless its remaining authorization is established.

## Recovery
Recover the last durable checkpoint. Inventory any explicitly identified unsaved work before discarding or replacing it.
Carry the minimum actual visual inputs. A path in a historic cloud workspace is provenance, not an accessible asset.
No-loss continuity depends on durable saved checkpoints; interruption before saving may require recovering that pending output.
