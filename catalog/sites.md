# Интерфейсы и сайты для Codex

Пять скиллов для макетов, структуры сайта, рекомендаций по UI, генеративной графики и проверки поведения страницы.

[Скачать ZIP 1.1.0](downloads/workflow-kit-sites-1.1.0.zip) · [Контрольная сумма SHA-256](downloads/workflow-kit-sites-1.1.0.zip.sha256).

## Установить

Распакуйте ZIP и откройте проект в Codex. Попросите Codex скопировать выбранные папки из skills в .agents/skills проекта. Вручную можно скопировать папки целиком. Если одноимённая папка уже существует, сперва сравните версии.

## Состав

| Скилл | Зависимости | Что проверено |
| --- | --- | --- |
| [site-architecture](../skills/site-architecture/SKILL.md) | Codex. Для планирования публикация сайта не требуется | На учебном брифе составлены и сверены иерархия, навигация и перенаправления |
| [ui-ux-pro-max](../skills/ui-ux-pro-max/SKILL.md) | Python для поиска по CSV | Поиск выдал рекомендации по доступности, а помощник сформировал подборку для учебного сайта |
| [algorithmic-art](../skills/algorithmic-art/SKILL.md) | Браузер с p5.js | Шаблон отрисовался. Проверены повторяемость изображения при одинаковом начальном числе и изменение изображения при другом |
| [webapp-testing](../skills/webapp-testing/SKILL.md) | Python с Playwright и совместимый Chromium | Учебная HTML-кнопка изменила статус на PASS. Создан PNG, повторная запись отклонена |
| [design-first](../skills/design-first/SKILL.md) | Python, Codex CLI с доступом к ImageGen, Node 22+ и Chrome или Edge | Штатный генератор создал мобильный макет по образцу. Учебная страница проверена в Edge на 390, 1440 и 1920 px |

У каждого скилла есть лицензия и описание изменений. Codex CLI обнаружил пять скиллов после распаковки архива и установки в отдельный проект. Проверки выполнены на вымышленных материалах и локальных страницах.

## Источники и лицензии

- site-architecture · [Лицензия](../skills/site-architecture/LICENSE) · [Происхождение и изменения](../skills/site-architecture/CHANGES.md).
- ui-ux-pro-max · [Лицензия](../skills/ui-ux-pro-max/LICENSE) · [Происхождение и изменения](../skills/ui-ux-pro-max/CHANGES.md).
- algorithmic-art · [Лицензия](../skills/algorithmic-art/LICENSE) · [Происхождение и изменения](../skills/algorithmic-art/CHANGES.md).
- webapp-testing · [Лицензия](../skills/webapp-testing/LICENSE) · [Происхождение и изменения](../skills/webapp-testing/CHANGES.md).

- design-first · [Лицензия](../skills/design-first/LICENSE) · [Происхождение и изменения](../skills/design-first/CHANGES.md).

Проверка Design First охватила одно направление. Мобильный экран эмулирован в Edge. Site Audit доступен по ссылке на исходник. [Скиллы по задачам](skills-by-topic.md#интерфейсы-и-сайты)

[Каталог дополнений](README.md)
