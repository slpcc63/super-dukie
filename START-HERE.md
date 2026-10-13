# Start here
1. Read AGENTS.md and workflow/COORDINATOR.md.
2. Read PROJECT-STATUS.json and the requested issue's status.json and production/QA dependencies.json.
3. Confirm the remote repository and current main commit, or the supplied package manifest. Report that version.
4. Read the exact script, approval ledger, and scoped references required by the assigned task.
5. Run python3 tools/checkpoint.py --check. For production readiness also use --production-ready.
6. State the current stop point and next authorized action. Preserve unresolved states and scope exceptions.
7. Continue only within the handoff and current Shannon authorization.
Repository files outrank chat memory. New explicit Shannon decisions must be recorded with their scope before dependent work.
If GitHub is inaccessible, read one supplied checkpoint package. Do not invent repository access or silently resume from an older copy.
