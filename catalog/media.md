# Презентации и мультимедиа для Codex

Шесть скиллов для презентаций, диаграмм, анимации и работы с разрешённым видео.

[Скачать ZIP 1.2.1](downloads/workflow-kit-media-1.2.1.zip) · [Контрольная сумма SHA-256](downloads/workflow-kit-media-1.2.1.zip.sha256)

## Установить

Распакуйте ZIP. Откройте учебный или рабочий проект в Codex и попросите скопировать выбранные папки скиллов из skills в .agents/skills проекта. Вручную можно скопировать те же папки. Если одноимённый скилл уже есть, сперва сравните версии. Откройте SKILL.md выбранного скилла и установите зависимости в отдельной среде.

## Состав

| Скилл | Зависимости | Что проверено на учебных данных |
| --- | --- | --- |
| [ppt-creator](../skills/ppt-creator/SKILL.md) | Python с pandas, matplotlib и python-pptx | Из CSV построен график. Изображение и заметки вставлены в PPTX и прочитаны после открытия файла |
| [mermaid-tools](../skills/mermaid-tools/SKILL.md) | Python, Node.js, Mermaid CLI и совместимый браузер для Puppeteer | Из Markdown извлечена схема. Создан PNG, повторная запись в занятую папку отклонена |
| [lottie](../skills/lottie/SKILL.md) | Python. Pillow и NumPy нужны только дополнительным помощникам | Записаны и повторно прочитаны JSON и TGS. Повторная запись отклонена |
| [youtube-downloader](../skills/youtube-downloader/SKILL.md) | Python и yt-dlp. FFmpeg нужен для объединения дорожек и извлечения аудио | Скачан вымышленный MP4 с локального адреса, сверено содержимое |
| video-by-code | FFmpeg, Node.js и Playwright для Canvas, Python для нарезки | На Windows отрендерены вертикальная Canvas-анимация и нарезка синтетического видео. Проверены листы кадров и декодирование H.264/AAC. |
| reels-console | FFmpeg и ffprobe, локальный Whisper для титров, OpenCV 4.x для лица | На Windows проверены монтаж с русскими титрами, громкость −14,69 LUFS и привязка фронтального лица к вертикальному кадру без InsightFace. |

Проверки не включали вход в YouTube, извлечение аудио, публикацию в Telegram, визуальную приёмку Lottie и озвучку video-by-code. Лицензия и история изменений есть в каждой папке. Codex CLI обнаружил все скиллы после копирования из распакованного ZIP.

## Монтаж и объясняющие ролики

- **[Мультик](../skills/multik/SKILL.md)** собирает вертикальный объясняющий ролик 1080×1920 с персонажем, голосом и анимацией на Remotion. Чтобы установить скилл в проект, скопируйте папку `skills/multik` целиком в `.agents/skills/`. Для пробы используйте локальное демо из `kit`. На Windows проверены кадр и тестовый MP4. Подключение внешних сервисов и отправка в Telegram в этой пробе не проверялись. [Исходник](https://github.com/artemiimillier/skill-multik/tree/1d6c7b71167c365080e6e65dad6dfc0f25504617) · [MIT](../skills/multik/LICENSE).
- **reels-montazh** монтирует вертикальное видео из записи с телефона или голоса. Добавляет субтитры, карточки и смены плана и предлагает пять стилей. Установку выполняйте по инструкции автора. На Windows проверены рендер MP4 1080×1920 и локальное распознавание русской фразы. Полный монтаж пользовательской записи пока не проверялся. [Исходник и установка](https://github.com/LeraLumiAi/reels-montazh/tree/250e00f470951a6fb4dddc6227c2549165c33ef4).

## Источники и лицензии

- ppt-creator · [Лицензия](../skills/ppt-creator/LICENSE) · [Происхождение и изменения](../skills/ppt-creator/CHANGES.md).
- mermaid-tools · [Лицензия](../skills/mermaid-tools/LICENSE) · [Происхождение и изменения](../skills/mermaid-tools/CHANGES.md).
- lottie · [Лицензия](../skills/lottie/LICENSE) · [Происхождение и изменения](../skills/lottie/CHANGES.md).
- youtube-downloader · [Лицензия](../skills/youtube-downloader/LICENSE) · [Происхождение и изменения](../skills/youtube-downloader/CHANGES.md).
- video-by-code · [Исходник](https://github.com/GuruDevvv/my-claude-skills/tree/b5c44a9b7ec4a2620d7c7824cc4df22b940ae6dd/mine/video-by-code). Лицензия и описание изменений находятся в ZIP 1.2.0.
- reels-console · [Исходник](https://github.com/GuruDevvv/my-claude-skills/tree/b5c44a9b7ec4a2620d7c7824cc4df22b940ae6dd/mine/reels-console). Лицензия и описание изменений находятся в ZIP 1.2.0.

[Каталог дополнений](README.md)
