# Документы, PDF и таблицы для Codex

Три скилла для преобразования документов и проверки таблиц. Human Text входит в [«Русские тексты и встречи»](text-meetings.md).

[Скачать ZIP](downloads/workflow-kit-documents-1.0.1.zip) · [Контрольная сумма SHA-256](downloads/workflow-kit-documents-1.0.1.zip.sha256).

## Установить

1. Распакуйте ZIP. Откройте свой проект в Codex.
2. Попросите Codex скопировать выбранные папки из распакованной папки skills в .agents/skills проекта либо скопируйте их вручную. Если одноимённая папка уже существует, сначала сравните версии.
3. Откройте SKILL.md выбранного скилла. Установите нужные зависимости в отдельной среде проекта, затем начните новый чат в том же проекте.

## Состав

| Скилл | Что делает | Что нужно | Что проверено |
| --- | --- | --- | --- |
| [doc-to-markdown](../skills/doc-to-markdown/SKILL.md) | Преобразует документы в Markdown | Python, Pandoc для DOCX и MarkItDown с поддержкой PDF для проверенного маршрута PDF | DOCX с заголовком и PDF с текстовым слоем преобразованы. Исходники сохранились |
| [libreoffice-calc](../skills/libreoffice-calc/SKILL.md) | Редактирует таблицы ODS через LibreOffice | Установленный LibreOffice и его Python с UNO | В отдельном скрытом экземпляре записаны формула и значение, ODS сохранён и открыт заново |
| [spreadsheet-auditor](../skills/spreadsheet-auditor/SKILL.md) | Ищет вероятные ошибки в таблицах XLSX | Python 3.11+ с openpyxl | Статический аудит указал ячейку с #REF!. Контрольная сумма исходника сохранилась |

У каждого скилла в папке лежат LICENSE и CHANGES.md. Codex CLI обнаружил все три скилла после распаковки и копирования в учебный проект. Проверки выполнены на вымышленных данных в Windows. Проверьте отдельно нужный режим, если работаете со сканами без текстового слоя, сложной вёрсткой, слайдами, макросами или связанными таблицами.

## Источники и лицензии

- doc-to-markdown · [Лицензия](../skills/doc-to-markdown/LICENSE) · [Происхождение и изменения](../skills/doc-to-markdown/CHANGES.md).
- libreoffice-calc · [Лицензия](../skills/libreoffice-calc/LICENSE) · [Происхождение и изменения](../skills/libreoffice-calc/CHANGES.md).
- spreadsheet-auditor · [Лицензия](../skills/spreadsheet-auditor/LICENSE) · [Происхождение и изменения](../skills/spreadsheet-auditor/CHANGES.md).

[Каталог дополнений](README.md)
