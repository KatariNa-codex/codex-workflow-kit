# Каталог дополнений Workflow Kit

Дополнения подключаются отдельно. Для начала работы достаточно [основного Workflow Kit](../README.md).

| Дополнение | Для чего | Как подключить |
| --- | --- | --- |
| [Browser и Computer Use](browser-computer-use.md) | Работа с веб-страницами и приложениями Windows | Настройка Edge и Any App с простыми проверками |
| [GitHub](github.md) | Чтение репозиториев, задач и запросов на слияние | Подключение аккаунта и проверка доступа к репозиторию |
| [Gmail](gmail.md) | Поиск и чтение почты в Codex | Необязательное подключение аккаунта с проверкой на учебном письме |
| [nlm-skill](nlm-skill.md) | Работа с источниками и материалами NotebookLM в Codex | Официальная установка скилла и подключение MCP. MIT, содержимое сверено с `v0.16.6` |
| Скиллы Codex | Готовые инструкции для задач с документами, кодом и другими материалами | [Официальный каталог скиллов Codex](https://github.com/openai/skills) |
| [Генеалогия](kinship.md) | Исследование источников и оформление семейного древа | Две самостоятельные части под одной карточкой |

## Выбрать дополнения

- [Скиллы по задачам](skills-by-topic.md) — 64 позиции со ссылками на опубликованную версию Workflow Kit или исходник.
- [Плагины, MCP и другие надстройки](integrations.md) — подключение, условия и что уже проверено.

## Скачать тематические наборы

Можно установить весь набор или выбрать отдельные папки скиллов из ZIP. В карточках указаны зависимости, способ установки и результаты проверок.

### Чертежи и геоданные

Проверить DWG и DXF, пересчитать координаты, обработать слой в QGIS или показать данные на веб-карте.

**Скиллы:** `cad-drawings`, `gdal`, `geopandas`, `image-compare`, `leaflet`, `proj`, `pyqgis`, `qgis-process`, `shapely`.

[Карточка набора](cad-geo.md) · [ZIP 1.1.0](downloads/workflow-kit-cad-geo-1.1.0.zip) · [SHA-256](downloads/workflow-kit-cad-geo-1.1.0.zip.sha256)

### Документы, PDF и таблицы

Перевести документ в Markdown, обработать таблицу в LibreOffice Calc или проверить формулы в Excel.

**Скиллы:** `doc-to-markdown`, `libreoffice-calc`, `spreadsheet-auditor`.

[Карточка набора](documents.md) · [ZIP 1.0.1](downloads/workflow-kit-documents-1.0.1.zip) · [SHA-256](downloads/workflow-kit-documents-1.0.1.zip.sha256)

### Русские тексты и встречи

Вычитать русский текст, составить протокол встречи и выделить решения из расшифровки.

**Скиллы:** `human-text`, `ru-text`, `ru-writing`, `meeting-minutes-taker`, `meeting-insights-analyzer`.

[Карточка набора](text-meetings.md) · [ZIP 1.0.0](downloads/workflow-kit-text-meetings-1.0.0.zip) · [SHA-256](downloads/workflow-kit-text-meetings-1.0.0.zip.sha256)

### Презентации и мультимедиа

Собрать презентацию, превратить схему Mermaid в изображение, смонтировать ролик или сделать анимацию.

**Скиллы:** `ppt-creator`, `mermaid-tools`, `lottie`, `youtube-downloader`, `video-by-code`, `reels-console`.

[Карточка набора](media.md) · [ZIP 1.2.0](downloads/workflow-kit-media-1.2.0.zip) · [SHA-256](downloads/workflow-kit-media-1.2.0.zip.sha256)

### Интерфейсы и сайты

Спроектировать структуру сайта, выбрать оформление и проверить веб-интерфейс.

**Скиллы:** `site-architecture`, `ui-ux-pro-max`, `webapp-testing`, `algorithmic-art`, `design-first`.

[Карточка набора](sites.md) · [ZIP 1.1.0](downloads/workflow-kit-sites-1.1.0.zip) · [SHA-256](downloads/workflow-kit-sites-1.1.0.zip.sha256)

### Исследования и работа с продуктом

Изучить потребности клиентов, проверить идею, подобрать цену или спланировать запуск.

**Скиллы:** `deep-research`, `customer-research`, `product-check`, `analytics`, `ab-testing`, `pricing`, `marketing-plan`, `launch`.

[Карточка набора](product-research.md) · [ZIP 1.0.0](downloads/workflow-kit-product-research-1.0.0.zip) · [SHA-256](downloads/workflow-kit-product-research-1.0.0.zip.sha256)

### Проверка проектов

Сравнить варианты решения, проверить ТЗ или структуру проекта, разобрать экспорт сессии Codex.

**Скиллы:** `idea-storm`, `multi-layer-review`, `project-audit`, `agent-eval`.

[Карточка набора](project-review.md) · [ZIP 1.0.0](downloads/workflow-kit-project-review-1.0.0.zip) · [SHA-256](downloads/workflow-kit-project-review-1.0.0.zip.sha256)

### Сопровождение проектов

Разобраться с ошибкой, проверить код и тесты, вести ветки Git и подготовить список изменений.

**Скиллы:** `changelog-generator`, `codex-windows-doctor`, `context-degradation`, `file-organizer`, `finishing-a-development-branch`, `python-testing-patterns`, `receiving-code-review`, `security-best-practices`, `security-threat-model`, `systematic-debugging`, `test-driven-development`, `using-git-worktrees`, `verification-before-completion`.

[Карточка набора](project-maintenance.md) · [ZIP 1.0.0](downloads/workflow-kit-project-maintenance-1.0.0.zip) · [SHA-256](downloads/workflow-kit-project-maintenance-1.0.0.zip.sha256)

### Скиллы, MCP и инструменты

Создать или проверить скилл, собрать MCP-сервер или спроектировать команды для агента.

**Скиллы:** `mcp-builder`, `skill-conductor`, `skill-eval`, `tool-design`.

[Карточка набора](skill-tools.md) · [ZIP 1.0.0](downloads/workflow-kit-skill-tools-1.0.0.zip) · [SHA-256](downloads/workflow-kit-skill-tools-1.0.0.zip.sha256)

### Генеалогия

Искать семейные документы, сопоставлять архивные записи и оформлять доказательства родственных связей.

**Скиллы:** `ex-ussr-kinship-research`.

[Карточка набора](kinship.md) · [ZIP 1.0.0](downloads/workflow-kit-kinship-1.0.0.zip) · [SHA-256](downloads/workflow-kit-kinship-1.0.0.zip.sha256) · [Family Tree Starter](https://github.com/KatariNa-codex/family-tree-starter)

## Скиллы по ссылкам на исходники

`transcribe`, `speech`, `site-audit` и `gh-fix-ci` доступны у авторов. [Ссылки в указателе скиллов](skills-by-topic.md).

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
| [spec-first](../skills/spec-first/) | Согласование Vision и Blueprint перед сборкой | Проверена структура инструкции. Скилл подключается отдельно от комплекта. | [MIT](../skills/spec-first/LICENSE) · [Изменения](../skills/spec-first/CHANGES.md) |
| [youtube-downloader](../skills/youtube-downloader/) | Работа с разрешёнными видео и аудио | Нужны установленные yt-dlp и ffmpeg. Проверен запуск справки, без загрузки видео. | [MIT](../skills/youtube-downloader/LICENSE) · [Изменения](../skills/youtube-downloader/CHANGES.md) |

Проверки выполнены на локальных файлах и учебных данных. Автоматическое срабатывание скиллов в Codex Desktop, CAD/COM, полная конвертация документов, реальный рендеринг Mermaid и загрузка видео в этом проходе не проверялись.

Другие тематические архивы появятся после проверки зависимостей, установки и лицензий. До этого выбирайте отдельные скиллы в каталоге.
