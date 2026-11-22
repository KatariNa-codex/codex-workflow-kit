# Project Audit for Codex

Project organization review for code, documentation, product, and mixed workspaces.

- **Quick** reviews applicable Codex instructions, optional project memory, and file structure.
- **Full** adds deeper checks, local Git hygiene, and configured automations. It can use authorized independent read-only reviewers or run the same checks sequentially.

Example prompts

> Проверь организацию проекта в быстром режиме. Покажи подтверждённые проблемы в AGENTS.md, структуре и памяти, если она есть.

> Сделай полный аудит текущего проекта. Проверь также Git и описанные автоматизации и сравни результат с прошлым аудитом в docs/audits.

The report includes evidence and prioritized fixes. The audit leaves existing project files untouched. A new report defaults to `docs/audits/` inside the verified project, with chat-only delivery when requested. Previous reports are preserved.

Read [SKILL.md](SKILL.md) for the workflow, [CHANGES.md](CHANGES.md) for adaptation notes, and [LICENSE](LICENSE) for the upstream license.
