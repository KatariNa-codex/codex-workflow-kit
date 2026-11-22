# nlm-skill — NotebookLM в Codex

Скилл помогает Codex работать с источниками, задавать вопросы по материалам блокнота и готовить обзоры. Для выполнения команд понадобится `nlm`. Вход в NotebookLM пользователь настраивает на своём компьютере.

## Как подключить

Установите `nlm` по инструкции автора, затем выполните `nlm skill install codex`. Скилл устанавливается отдельно от основного ZIP Workflow Kit. [Установка CLI](https://github.com/jacob-bd/gemini-notebook-mcp-cli/blob/main/docs/CLI_GUIDE.md) · [Подключение скилла к Codex](https://github.com/jacob-bd/gemini-notebook-mcp-cli/blob/main/docs/CLI_GUIDE.md#skills-ai-assistant-integration)

## Подключить MCP

MCP нужен, если вы хотите пользоваться инструментами NotebookLM прямо в Codex. CLI и сервер входят в один пакет.

1. Если `nlm` ещё отсутствует, установите его по инструкции автора. Затем запустите `nlm login` и войдите в свой Google-аккаунт в открывшемся браузере.
2. Запустите `nlm setup`, выберите добавление MCP и отметьте **Codex**. Если сервер не появился в Desktop, перезапустите Codex.
3. Откройте **Настройки → MCP servers** и убедитесь, что включён `gemini-notebook-mcp`.

**Проверка.** Создайте в NotebookLM пустой учебный блокнот. В новом чате попросите Codex найти его по названию через MCP NotebookLM и вернуть только название. [Установка и вход](https://github.com/jacob-bd/gemini-notebook-mcp-cli#-quick-start) · [Мастер настройки](https://github.com/jacob-bd/gemini-notebook-mcp-cli/blob/main/docs/CLI_GUIDE.md#setup-mcp-server-configuration) · [Настройки MCP](https://learn.chatgpt.com/docs/extend/mcp)

## Лицензия и сверка

Лицензия [MIT](https://github.com/jacob-bd/gemini-notebook-mcp-cli/blob/v0.16.6/LICENSE). 22 ноября 2026 года сверили содержимое с [выпуском v0.16.6](https://github.com/jacob-bd/gemini-notebook-mcp-cli/releases/tag/v0.16.6). Новую установку и синхронизацию в этой проверке не запускали. Уточнения по синхронизации Google Drive описаны в [исходной правке](https://github.com/jacob-bd/gemini-notebook-mcp-cli/pull/396).
