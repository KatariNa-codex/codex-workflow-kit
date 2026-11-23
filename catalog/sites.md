# Интерфейсы и сайты для Codex

Четыре скилла для структуры сайта, рекомендаций по UI, генеративной графики и проверки поведения страницы.

[Скачать ZIP](downloads/workflow-kit-sites-1.0.0.zip) · [Контрольная сумма SHA-256](downloads/workflow-kit-sites-1.0.0.zip.sha256).

## Установить

Распакуйте ZIP и откройте проект в Codex. Попросите Codex скопировать выбранные папки из skills в .agents/skills проекта. Вручную можно скопировать папки целиком. Если одноимённая папка уже существует, сперва сравните версии.

## Состав

| Скилл | Зависимости | Что проверено |
| --- | --- | --- |
| [site-architecture](../skills/site-architecture/SKILL.md) | Codex. Для планирования публикация сайта не требуется | На учебном брифе составлены и сверены иерархия, навигация и перенаправления |
| [ui-ux-pro-max](../skills/ui-ux-pro-max/SKILL.md) | Python для поиска по CSV | Поиск выдал рекомендации по доступности, а помощник сформировал подборку для учебного сайта |
| [algorithmic-art](../skills/algorithmic-art/SKILL.md) | Браузер с p5.js | Шаблон отрисовался. Проверены повторяемость изображения при одинаковом начальном числе и изменение изображения при другом |
| [webapp-testing](../skills/webapp-testing/SKILL.md) | Python с Playwright и совместимый Chromium | Учебная HTML-кнопка изменила статус на PASS. Создан PNG, повторная запись отклонена |

У каждого скилла есть лицензия и описание изменений. Codex CLI обнаружил четыре скилла после распаковки архива и установки в отдельный проект. Проверки выполнены на вымышленных материалах и локальных страницах.

## Источники и лицензии

- site-architecture · [Лицензия](../skills/site-architecture/LICENSE) · [Происхождение и изменения](../skills/site-architecture/CHANGES.md).
- ui-ux-pro-max · [Лицензия](../skills/ui-ux-pro-max/LICENSE) · [Происхождение и изменения](../skills/ui-ux-pro-max/CHANGES.md).
- algorithmic-art · [Лицензия](../skills/algorithmic-art/LICENSE) · [Происхождение и изменения](../skills/algorithmic-art/CHANGES.md).
- webapp-testing · [Лицензия](../skills/webapp-testing/LICENSE) · [Происхождение и изменения](../skills/webapp-testing/CHANGES.md).

Design First и Site Audit доступны по ссылкам на исходники. Полный сценарий Design First и условия распространения всех файлов Site Audit ещё требуют отдельной сверки. [Скиллы по задачам](skills-by-topic.md#интерфейсы-и-сайты)

[Каталог дополнений](README.md)
