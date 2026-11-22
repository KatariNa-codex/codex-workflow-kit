# Full audit workstreams

Use these workstreams with or without delegates. The coordinator keeps the scope and synthesizes the report.

| Workstream | Checks |
|---|---|
| Instructions | Effective rules and scoped overrides, stale procedures, paths and contradictions |
| Memory | Verified project-only memory, index links, entry freshness and duplication when memory exists |
| Structure | Type-specific organization, representative subtrees and file metadata |
| Git | Read-only local status and tracked-file names within scope, ignore coverage, recent history when relevant |
| Automations | Project declarations, sanitized fields, in-scope references and intended role |

If delegating is authorized, consult active host and project rules before using actual available tools. Group workstreams to fit current slots. Give each reviewer a bounded independent assignment. Include the checklist, scope, explicit read-only constraints, and output format. Keep raw configuration, credentials, personal profile details, and unrelated paths local. Perform any necessary active-profile lookup and configuration sanitization with the coordinator rather than delegates. Prohibit onward delegation. A rejected, unavailable or failed workstream falls back to the coordinator when feasible. State any actual gaps.

Use this prompt outline:

```text
Read-only project audit. Inspect only [scope] for [workstream].
Apply [checklist] and [applicable host and project rules].
Use bounded metadata and approved text only. Skip secret-bearing files.
Avoid writes, hooks, remote operations, and onward delegation.
Return Checked, Findings, and Skipped.
For each finding give severity, path or safe evidence, impact, and recommendation.
For skipped checks give the reason. Omit sensitive values.
```

The coordinator verifies material evidence, merges duplicate findings, records coverage, and rates severity against observed impact.
