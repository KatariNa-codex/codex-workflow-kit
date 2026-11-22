# Каталог дополнений Workflow Kit

Дополнения подключаются отдельно. Для начала работы достаточно [основного Workflow Kit](../README.md).

| Дополнение | Для чего | Как подключить |
| --- | --- | --- |
| [nlm-skill](nlm-skill.md) | Работа с источниками и материалами NotebookLM в Codex | Официальная установка автора. MIT, содержимое сверено с `v0.16.6` |
| Скиллы Codex | Готовые инструкции для задач с документами, кодом и другими материалами | [Официальный каталог скиллов Codex](https://github.com/openai/skills) |

## Скиллы из этого репозитория

Выберите папку скилла целиком. Для установки можно передать Codex ссылку на неё и попросить установить только выбранный скилл. Для ручного подключения к одному проекту положите папку в `.agents/skills/` внутри проекта. Загляните в `SKILL.md` выбранного скилла, чтобы узнать его требования. [Официальная справка по скиллам](https://learn.chatgpt.com/docs/build-skills)

| Скилл | Для чего | Зависимости и проверка | Лицензия и история |
| --- | --- | --- | --- |
| [agent-eval](../skills/agent-eval/) | Разбор разрешённого экспорта сессии Codex | Python. Проверен разбор вымышленного экспорта JSONL. | [MIT](../skills/agent-eval/LICENSE) · [Изменения](../skills/agent-eval/CHANGES.md) |
| [cad-drawings](../skills/cad-drawings/) | Работа с DWG и DXF | Нужен отдельный Python с зависимостями. ODA и CAD устанавливаются отдельно. Проверен запуск помощника с учебной конфигурацией. | [MIT](../skills/cad-drawings/LICENSE) · [Изменения](../skills/cad-drawings/CHANGES.md) |
| [deep-research](../skills/deep-research/) | Исследование с источниками и итоговым отчётом | Для поиска и независимых проверок нужны доступные в сеансе инструменты. Проверена структура инструкции. | [MIT](../skills/deep-research/LICENSE) · [Изменения](../skills/deep-research/CHANGES.md) |
| [doc-to-markdown](../skills/doc-to-markdown/) | Преобразование офисных документов в Markdown | Нужны установленные конвертеры. Проверена защита существующего файла от перезаписи. | [MIT](../skills/doc-to-markdown/LICENSE) · [Изменения](../skills/doc-to-markdown/CHANGES.md) |
| [human-text](../skills/human-text/) | Редактура и подготовка русскоязычных текстов | Проверен запуск локального помощника на учебном тексте. | [MIT](../skills/human-text/LICENSE) · [Изменения](../skills/human-text/CHANGES.md) |
| [mermaid-tools](../skills/mermaid-tools/) | Рендеринг диаграмм Mermaid из Markdown | Нужен установленный Mermaid CLI. Проверена защита существующей папки вывода. | [MIT](../skills/mermaid-tools/LICENSE) · [Изменения](../skills/mermaid-tools/CHANGES.md) |
| [ru-writing](../skills/ru-writing/) | Подготовка и вычитка русских текстов | Нужны [human-text](../skills/human-text/) и [ru-text](https://github.com/talkstream/ru-text/tree/main/skills/ru-text). Проверена структура инструкции. | [MIT](../skills/ru-writing/LICENSE) · [Изменения](../skills/ru-writing/CHANGES.md) |
| [spec-first](../skills/spec-first/) | Согласование Vision и Blueprint перед сборкой | В выпуске добавлена развилка для AGENTS.md в Codex и CLAUDE.md в Claude Code. Проверена структура инструкции. | [MIT](../skills/spec-first/LICENSE) · [Изменения](../skills/spec-first/CHANGES.md) |
| [youtube-downloader](../skills/youtube-downloader/) | Работа с разрешёнными видео и аудио | Нужны установленные yt-dlp и ffmpeg. Проверен запуск справки, без загрузки видео. | [MIT](../skills/youtube-downloader/LICENSE) · [Изменения](../skills/youtube-downloader/CHANGES.md) |

Проверки выполнены на локальных файлах и учебных данных. Автоматическое срабатывание скиллов в Codex Desktop, CAD/COM, полная конвертация документов, реальный рендеринг Mermaid и загрузка видео в этом проходе не проверялись.

Тематические наборы для чертежей, геоданных, документов и других задач будут добавляться после проверки установки и лицензий. Для Family Tree Starter запланирован отдельный форк с описанием доработок и вымышленными примерами.
