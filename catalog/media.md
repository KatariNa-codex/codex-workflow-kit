# Презентации и мультимедиа для Codex

Четыре скилла для презентаций, диаграмм, анимации и работы с разрешённым видео.

[Скачать ZIP](downloads/workflow-kit-media-1.0.0.zip) · [Контрольная сумма SHA-256](downloads/workflow-kit-media-1.0.0.zip.sha256).

## Установить

Распакуйте ZIP. Откройте учебный или рабочий проект в Codex и попросите скопировать выбранные папки скиллов из skills в .agents/skills проекта. Вручную можно скопировать те же папки. Если одноимённый скилл уже есть, сперва сравните версии. Откройте SKILL.md выбранного скилла и установите зависимости в отдельной среде.

## Состав

| Скилл | Зависимости | Что проверено на учебных данных |
| --- | --- | --- |
| [ppt-creator](../skills/ppt-creator/SKILL.md) | Python с pandas, matplotlib и python-pptx | Из CSV построен график. Изображение и заметки вставлены в PPTX и прочитаны после открытия файла |
| [mermaid-tools](../skills/mermaid-tools/SKILL.md) | Python, Node.js, Mermaid CLI и совместимый браузер для Puppeteer | Из Markdown извлечена схема. Создан PNG, повторная запись в занятую папку отклонена |
| [lottie](../skills/lottie/SKILL.md) | Python. Pillow и NumPy нужны только дополнительным помощникам | Записаны и повторно прочитаны JSON и TGS. Повторная запись отклонена |
| [youtube-downloader](../skills/youtube-downloader/SKILL.md) | Python и yt-dlp. FFmpeg нужен для объединения дорожек и извлечения аудио | Скачан вымышленный MP4 с локального адреса, сверено содержимое |

Проверки не включали вход в YouTube, извлечение аудио, публикацию в Telegram и визуальную приёмку анимации. Лицензия и история изменений есть в каждой папке. Codex CLI обнаружил все скиллы после копирования из распакованного ZIP.

## Источники и лицензии

- ppt-creator · [Лицензия](../skills/ppt-creator/LICENSE) · [Происхождение и изменения](../skills/ppt-creator/CHANGES.md).
- mermaid-tools · [Лицензия](../skills/mermaid-tools/LICENSE) · [Происхождение и изменения](../skills/mermaid-tools/CHANGES.md).
- lottie · [Лицензия](../skills/lottie/LICENSE) · [Происхождение и изменения](../skills/lottie/CHANGES.md).
- youtube-downloader · [Лицензия](../skills/youtube-downloader/LICENSE) · [Происхождение и изменения](../skills/youtube-downloader/CHANGES.md).

[Каталог дополнений](README.md)
