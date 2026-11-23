# Каталог дополнений Workflow Kit

Дополнения подключаются отдельно. Для начала работы достаточно [основного Workflow Kit](../README.md).

| Дополнение | Для чего | Как подключить |
| --- | --- | --- |
| [Browser и Computer Use](browser-computer-use.md) | Работа с веб-страницами и приложениями Windows | Настройка Edge и Any App с простыми проверками |
| [GitHub](github.md) | Чтение репозиториев, задач и запросов на слияние | Подключение аккаунта и проверка доступа к репозиторию |
| [Gmail](gmail.md) | Поиск и чтение почты в Codex | Необязательное подключение аккаунта с проверкой на учебном письме |
| [nlm-skill](nlm-skill.md) | Работа с источниками и материалами NotebookLM в Codex | Официальная установка скилла и подключение MCP. MIT, содержимое сверено с `v0.16.6` |
| Скиллы Codex | Готовые инструкции для задач с документами, кодом и другими материалами | [Официальный каталог скиллов Codex](https://github.com/openai/skills) |
| [Family Tree Starter](https://github.com/KatariNa-codex/family-tree-starter) | Демонстрационный шаблон семейного древа с карточками, картой и журналом | [Отдельный форк](https://github.com/KatariNa-codex/family-tree-starter) с вымышленными данными · [MIT](https://github.com/KatariNa-codex/family-tree-starter/blob/main/LICENSE) · [Доработки](https://github.com/KatariNa-codex/family-tree-starter/blob/main/CHANGES.md) |

## Выбрать дополнения

- [Скиллы по задачам](skills-by-topic.md) — 67 позиций со ссылками на опубликованную версию Workflow Kit или исходник.
- [Плагины, MCP и другие надстройки](integrations.md) — подключение, условия и что уже проверено.

## Скачать тематические наборы

**[Русские тексты и встречи](text-meetings.md)** — пять скиллов с учебными проверками. [ZIP 1.0.0](downloads/workflow-kit-text-meetings-1.0.0.zip) · [Контрольная сумма](downloads/workflow-kit-text-meetings-1.0.0.zip.sha256)

**[Сопровождение проектов](project-maintenance.md)** — 13 скиллов с учебными проверками. [ZIP 1.0.0](downloads/workflow-kit-project-maintenance-1.0.0.zip) · [Контрольная сумма](downloads/workflow-kit-project-maintenance-1.0.0.zip.sha256)

**[Скиллы, MCP и инструменты](skill-tools.md)** — четыре проверенных скилла. [ZIP 1.0.0](downloads/workflow-kit-skill-tools-1.0.0.zip) · [Контрольная сумма](downloads/workflow-kit-skill-tools-1.0.0.zip.sha256)

**[Исследования и работа с продуктом](product-research.md)** — восемь скиллов с проверками на учебных сценариях. [ZIP 1.0.0](downloads/workflow-kit-product-research-1.0.0.zip) · [Контрольная сумма](downloads/workflow-kit-product-research-1.0.0.zip.sha256)

**[Интерфейсы и сайты](sites.md)** — четыре проверенных скилла. [ZIP 1.0.0](downloads/workflow-kit-sites-1.0.0.zip) · [Контрольная сумма](downloads/workflow-kit-sites-1.0.0.zip.sha256)

**[Презентации и мультимедиа](media.md)** — четыре проверенных скилла. [ZIP 1.0.0](downloads/workflow-kit-media-1.0.0.zip) · [Контрольная сумма](downloads/workflow-kit-media-1.0.0.zip.sha256)

**[Документы, PDF и таблицы](documents.md)** — четыре проверенных скилла. [ZIP 1.0.0](downloads/workflow-kit-documents-1.0.0.zip) · [Контрольная сумма](downloads/workflow-kit-documents-1.0.0.zip.sha256)

**[Чертежи и геоданные в Codex](cad-geo.md)** — 7 проверенных скиллов. [ZIP 1.0.0](downloads/workflow-kit-cad-geo-1.0.0.zip) · [Контрольная сумма](downloads/workflow-kit-cad-geo-1.0.0.zip.sha256)

[Проверка проектов в Codex, ZIP 1.0.0](downloads/workflow-kit-project-review-1.0.0.zip) · [Контрольная сумма](downloads/workflow-kit-project-review-1.0.0.zip.sha256)

В архиве Idea Storm, Multi-Layer Review, Project Audit и Agent Eval с инструкцией по установке в один проект. Codex CLI обнаружил все четыре после распаковки и копирования в учебный проект. Agent Eval обработал вымышленный экспорт из этой копии. Запуск в окне Desktop в этой проверке не проводился.

## Скиллы из этого репозитория

Выберите папку скилла целиком. Для установки можно передать Codex ссылку на неё и попросить установить только выбранный скилл. Для ручного подключения к одному проекту положите папку в `.agents/skills/` внутри проекта. Загляните в `SKILL.md` выбранного скилла, чтобы узнать его требования. [Официальная справка по скиллам](https://learn.chatgpt.com/docs/build-skills)

| Скилл | Для чего | Зависимости и проверка | Лицензия и история |
| --- | --- | --- | --- |
| [agent-eval](../skills/agent-eval/) | Разбор разрешённого экспорта сессии Codex | Python. Проверен разбор вымышленного экспорта JSONL. | [MIT](../skills/agent-eval/LICENSE) · [Изменения](../skills/agent-eval/CHANGES.md) |
| [cad-drawings](../skills/cad-drawings/) | Работа с DWG и DXF | Нужен отдельный Python с зависимостями. ODA и CAD устанавливаются отдельно. Проверен запуск помощника с учебной конфигурацией. | [MIT](../skills/cad-drawings/LICENSE) · [Изменения](../skills/cad-drawings/CHANGES.md) |
| [deep-research](../skills/deep-research/) | Исследование с источниками и итоговым отчётом | Для поиска и независимых проверок нужны доступные в сеансе инструменты. Проверена структура инструкции. | [MIT](../skills/deep-research/LICENSE) · [Изменения](../skills/deep-research/CHANGES.md) |
| [doc-to-markdown](../skills/doc-to-markdown/) | Преобразование офисных документов в Markdown | Нужны установленные конвертеры. Проверена защита существующего файла от перезаписи. | [MIT](../skills/doc-to-markdown/LICENSE) · [Изменения](../skills/doc-to-markdown/CHANGES.md) |
| [human-text](../skills/human-text/) | Редактура и подготовка русскоязычных текстов | Проверен запуск локального помощника на учебном тексте. | [MIT](../skills/human-text/LICENSE) · [Изменения](../skills/human-text/CHANGES.md) |
| [idea-storm](../skills/idea-storm/) | Штурм вариантов и проверка финалистов | Штатная делегация Codex, при ограничениях — явно отмеченная самопроверка. Проверен нейтральный бриф. | [MIT](../skills/idea-storm/LICENSE) · [Изменения](../skills/idea-storm/CHANGES.md) |
| [mermaid-tools](../skills/mermaid-tools/) | Рендеринг диаграмм Mermaid из Markdown | Нужен установленный Mermaid CLI. Проверена защита существующей папки вывода. | [MIT](../skills/mermaid-tools/LICENSE) · [Изменения](../skills/mermaid-tools/CHANGES.md) |
| [multi-layer-review](../skills/multi-layer-review/) | Ревью ТЗ и планов по пяти ракурсам | Независимые рецензенты при доступной делегации. Проверена находка по учебному ТЗ и файлу. | [MIT](../skills/multi-layer-review/LICENSE) · [Изменения](../skills/multi-layer-review/CHANGES.md) |
| [project-audit](../skills/project-audit/) | Аудит инструкций, структуры и памяти проекта | Quick и Full. Проверено определение области и папки памяти на временных профилях Windows. | [MIT](../skills/project-audit/LICENSE) · [Изменения](../skills/project-audit/CHANGES.md) |
| [ru-writing](../skills/ru-writing/) | Подготовка и вычитка русских текстов | Нужны [human-text](../skills/human-text/) и [ru-text](../skills/ru-text/). Проверена структура инструкции. | [MIT](../skills/ru-writing/LICENSE) · [Изменения](../skills/ru-writing/CHANGES.md) |
| [spec-first](../skills/spec-first/) | Согласование Vision и Blueprint перед сборкой | В выпуске добавлена развилка для AGENTS.md в Codex и CLAUDE.md в Claude Code. Проверена структура инструкции. | [MIT](../skills/spec-first/LICENSE) · [Изменения](../skills/spec-first/CHANGES.md) |
| [youtube-downloader](../skills/youtube-downloader/) | Работа с разрешёнными видео и аудио | Нужны установленные yt-dlp и ffmpeg. Проверен запуск справки, без загрузки видео. | [MIT](../skills/youtube-downloader/LICENSE) · [Изменения](../skills/youtube-downloader/CHANGES.md) |

Проверки выполнены на локальных файлах и учебных данных. Автоматическое срабатывание скиллов в Codex Desktop, CAD/COM, полная конвертация документов, реальный рендеринг Mermaid и загрузка видео в этом проходе не проверялись.

Другие тематические архивы появятся после проверки зависимостей, установки и лицензий. До этого выбирайте отдельные скиллы в каталоге.
