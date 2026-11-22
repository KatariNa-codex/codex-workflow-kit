---
name: project-audit
description: >
  Read-only audit of project organization in Quick or Full mode. Reviews
  applicable AGENTS.md, project memory when present, and file structure.
  Full also reviews local Git hygiene and automation configuration. Use when
  asked for "аудит проекта", "проверь структуру", "проверь AGENTS.md", "аудит
  памяти", "audit project organization", "project health check", or pre-share
  organization review. Do not use for code review, debugging, or design review.
---

# Project Audit

Deliver a severity-grouped report on the actual project. Quick reviews instructions, memory, and structure. Full adds deeper checks of those areas, local Git hygiene, and automation declarations.

## Audit boundary

- Use read-only tools during discovery and review. Apply no fixes. Never start jobs, execute hooks, contact remotes, or change configuration. The report is the only output file. If the user asks for chat-only or read-only delivery, return it in chat.
- Skip secret-bearing files (for example `.env*`, private keys, credentials and authentication stores), binaries, private sessions, and unrelated projects. Review secret-like filenames as metadata only. If an approved document contains an apparent secret, omit the value and use `[REDACTED]`. Never echo raw configuration or sensitive snippets into tool output, agent prompts, or the report.
- Bound traversal and output. Exclude dependencies, generated output, VCS internals, and linked directories that escape scope. Use the active shell and native paths. Separate observed facts from hypotheses and mark partial coverage.

## Reconnaissance

1. Use the user-specified path when given. Otherwise identify the project from the active working directory, workspace metadata, applicable instructions, and markers such as `HANDOFF.md`, a manifest or Git root. An umbrella projects folder or host workspace can contain distinct projects. Confirm which applies when signals conflict. Ask for a concrete project if the only candidate is a filesystem root or broad workspace. Never substitute a parent repository for a nested project.
2. Identify effective Codex instructions in host context and along the path into the target. Take account of applicable `AGENTS.md` and `AGENTS.override.md`, host precedence, and child instructions for directories under review. For nested files, preserve directory scope when checking apparent conflicts. Report absent instructions as a finding only if a project requirement or observed workflow depends on them.
3. Locate relevant memory using [profile discovery](references/checklists.md#project-memory-discovery). Treat absence as a skipped area. Locate earlier audits only in a verified current-project destination or a user-supplied location. Compare an earlier report if the user asks or comparison is part of the task. Mark issues fixed only after rechecking them.
4. Map the top two directory levels, locate the entry point, and estimate file count with exclusions stated. Use [project type signals](references/project-type-checklists.md#1-project-type-detection). For an unusual project, use its documented workflow and state the inferred type or limits of the classification.

Use the requested mode if named. For a general request, use Quick unless the scope explicitly includes deeper Git or automation checks. State the mode. Git root discovery in Quick establishes scope only.

## Quick

Work sequentially through the [checklists](references/checklists.md) for instructions, memory, and file structure. Read instructions within scope, compare documented layout to actual paths, and follow relevant project references. Sample memory and structure on large projects, naming the sample and any omitted checks. Omit Git hygiene and automation review.

## Full

Cover Quick plus deeper structure inspection, read-only Git hygiene, and configured automation declarations. Use the same checklists and the [Full workstream reference](references/agent-prompts.md). When active rules authorize delegation and appropriate host tools are available, assign independent read-only workstreams using applicable routing policy and available slots. Share only scoped paths, safe context, and the applicable checklist. For the remaining areas or when no delegates are available, perform the same checks sequentially and state actual coverage. Recheck material findings with local evidence before reporting. Report exactly which checks remain incomplete when access or tooling limits coverage.

## Report

Use the user's language. Start with project, date, mode, project type and audited scope. Summarize each applicable area in a table with its status and finding count. Then provide short sections for instructions, memory, structure, Git, and automations as applicable. For each, give checks performed, observed findings with evidence, and concrete recommendations. Report skipped checks, limitations, and their reasons separately. Use project-relative paths with line numbers where possible and omit sensitive values.

- **Critical** means verified risk of significant disclosure, data loss, or a blocked essential workflow.
- **Warning** means a material, verified workflow degradation with a workaround.
- **Low** means a minor verified issue that can wait.

Apply [type-specific severity guidance](references/project-type-checklists.md#5-severity-modifiers-table). Prioritize Critical and Warning actions. If comparing an earlier audit, summarize fixed, new, and persisting findings separately and identify any previous checks omitted this time.

Show the report in chat. Save a copy to the user-specified path or to the destination set by project instructions. Otherwise use `docs/audits/` under the verified project root. Use a memory audit folder only if it is explicitly designated and the association with this project is confirmed. For chat-only or strictly read-only requests, or if no safe project root is known, leave the report in chat. Resolve the destination before creating anything. Keep links to project files relative to the report location when possible. Use a dated report name and a numbered suffix if it already exists. Create exclusively or use an equivalent no-overwrite operation. Reopen and verify the complete report, then give its path.
