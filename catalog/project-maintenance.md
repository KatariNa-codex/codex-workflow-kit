# Сопровождение проектов в Codex

Тринадцать скиллов для Git, тестов, диагностики, ревью и работы с файлами проекта.

[Скачать ZIP](downloads/workflow-kit-project-maintenance-1.0.0.zip) · [Контрольная сумма SHA-256](downloads/workflow-kit-project-maintenance-1.0.0.zip.sha256).

## Установить

Распакуйте ZIP и откройте проект в Codex. Попросите скопировать выбранные папки из skills в .agents/skills проекта или сделайте это вручную. Существующие одноимённые папки сначала сравните. Откройте SKILL.md нужного скилла, чтобы узнать его назначение и требования.

## Состав и проверка

| Скилл | Для чего | Что проверено |
| --- | --- | --- |
| [changelog-generator](../skills/changelog-generator/SKILL.md) | Заметки о выпуске по истории изменений | Из вымышленных коммитов составлены пользовательские пункты |
| [codex-windows-doctor](../skills/codex-windows-doctor/SKILL.md) | Диагностика среды Codex на Windows | Из учебного журнала получены счётчики сигналов без строки журнала |
| [context-degradation](../skills/context-degradation/SKILL.md) | Разбор потери решений при длинном контексте | По короткому журналу найдены две подтверждённые потери решений без оценки внимания модели |
| [file-organizer](../skills/file-organizer/SKILL.md) | План размещения файлов и поиск дублей | На отдельной папке предложены места и отмечены побайтные дубли |
| [finishing-a-development-branch](../skills/finishing-a-development-branch/SKILL.md) | Выбор дальнейшего действия для готовой ветки | Для тестовой ветки проверено, когда можно предложить интеграцию |
| [python-testing-patterns](../skills/python-testing-patterns/SKILL.md) | Шаблоны тестов Python | Выполнены параметризованные тесты pytest |
| [receiving-code-review](../skills/receiving-code-review/SKILL.md) | Проверка замечаний ревью | Принято обоснованное замечание и отвергнуто неприменимое |
| [security-best-practices](../skills/security-best-practices/SKILL.md) | Ревью мер защиты | На учебном примере проверены серверные ограничения доступа и минимальное раскрытие данных |
| [security-threat-model](../skills/security-threat-model/SKILL.md) | Модель угроз с мерами защиты | По учебной архитектуре определены активы, границы доверия и меры |
| [systematic-debugging](../skills/systematic-debugging/SKILL.md) | Поиск причины сбоя | Провал теста воспроизведён, причина найдена и проверена после исправления |
| [test-driven-development](../skills/test-driven-development/SKILL.md) | Разработка через тест | Выполнен цикл падающего теста и исправления |
| [using-git-worktrees](../skills/using-git-worktrees/SKILL.md) | Изолированная рабочая папка Git | Временная ветка создана в отдельном worktree. Основная копия сохранилась |
| [verification-before-completion](../skills/verification-before-completion/SKILL.md) | Проверка основания для отчёта о готовности | Свежий запуск тестов подтвердил ровно заявленный результат |

В комплекте инструкции и исходные вспомогательные файлы. Для приведённых сценариев с Git нужен Git, для тестов Python — Python и pytest, для диагностики Windows — PowerShell. Профиль, сетевые сервисы и удалённые Git-репозитории в проверках не изменялись.

Codex CLI обнаружил все тринадцать скиллов после установки из распакованного ZIP. Лицензия и сведения об исходной версии есть в каждой папке.

## Источники и лицензии

- changelog-generator · [Лицензия](../skills/changelog-generator/LICENSE) · [Происхождение и изменения](../skills/changelog-generator/CHANGES.md).
- codex-windows-doctor · [Лицензия](../skills/codex-windows-doctor/LICENSE) · [Происхождение и изменения](../skills/codex-windows-doctor/CHANGES.md).
- context-degradation · [Лицензия](../skills/context-degradation/LICENSE) · [Происхождение и изменения](../skills/context-degradation/CHANGES.md).
- file-organizer · [Лицензия](../skills/file-organizer/LICENSE) · [Происхождение и изменения](../skills/file-organizer/CHANGES.md).
- finishing-a-development-branch · [Лицензия](../skills/finishing-a-development-branch/LICENSE) · [Происхождение и изменения](../skills/finishing-a-development-branch/CHANGES.md).
- python-testing-patterns · [Лицензия](../skills/python-testing-patterns/LICENSE) · [Происхождение и изменения](../skills/python-testing-patterns/CHANGES.md).
- receiving-code-review · [Лицензия](../skills/receiving-code-review/LICENSE) · [Происхождение и изменения](../skills/receiving-code-review/CHANGES.md).
- security-best-practices · [Лицензия](../skills/security-best-practices/LICENSE) · [Происхождение и изменения](../skills/security-best-practices/CHANGES.md).
- security-threat-model · [Лицензия](../skills/security-threat-model/LICENSE) · [Происхождение и изменения](../skills/security-threat-model/CHANGES.md).
- systematic-debugging · [Лицензия](../skills/systematic-debugging/LICENSE) · [Происхождение и изменения](../skills/systematic-debugging/CHANGES.md).
- test-driven-development · [Лицензия](../skills/test-driven-development/LICENSE) · [Происхождение и изменения](../skills/test-driven-development/CHANGES.md).
- using-git-worktrees · [Лицензия](../skills/using-git-worktrees/LICENSE) · [Происхождение и изменения](../skills/using-git-worktrees/CHANGES.md).
- verification-before-completion · [Лицензия](../skills/verification-before-completion/LICENSE) · [Происхождение и изменения](../skills/verification-before-completion/CHANGES.md).

GH Fix CI доступен по исходной ссылке. Проверку с действующими GitHub Actions в этот проход не включали. [Скиллы по задачам](skills-by-topic.md#проверка-и-сопровождение-проектов)

[Каталог дополнений](README.md)
