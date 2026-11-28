# Проверка проектов в Codex

Четыре скилла для сравнения вариантов, проверки ТЗ и структуры проекта и разбора экспорта сессии Codex.

[Скачать ZIP 1.0.0](downloads/workflow-kit-project-review-1.0.0.zip) · [Контрольная сумма SHA-256](downloads/workflow-kit-project-review-1.0.0.zip.sha256)

## Установить

Распакуйте ZIP и откройте папку проекта в Codex. Скопируйте выбранные папки из `skills` в `.agents/skills` проекта или попросите об этом Codex. Если одноимённый скилл уже установлен, сначала сравните версии. Для Agent Eval нужен Python. Для полного ревью Multi-Layer Review могут понадобиться доступные подагенты.

## Состав

| Скилл | Назначение |
| --- | --- |
| [idea-storm](../skills/idea-storm/SKILL.md) | Помогает сравнить варианты, проверить финалистов и выбрать следующий шаг |
| [multi-layer-review](../skills/multi-layer-review/SKILL.md) | Проверяет ТЗ, архитектуру или план реализации с нескольких сторон |
| [project-audit](../skills/project-audit/SKILL.md) | Проверяет структуру проекта, действующие инструкции и состояние HANDOFF |
| [agent-eval](../skills/agent-eval/SKILL.md) | Разбирает заранее разрешённый экспорт сессии Codex и сверяет заявленные результаты с журналом |

## Что проверено

Codex CLI обнаружил все четыре скилла после установки из распакованного ZIP в учебный проект. Agent Eval обработал вымышленный экспорт из той же копии. Этот проход не включал запуск в окне Codex Desktop.

Для первой пробы можно попросить Codex: «Примени project-audit в режиме Quick к этому учебному проекту. Найди действующий AGENTS.md и покажи следующее действие из HANDOFF.md».

## Источники и лицензии

- idea-storm · [MIT](../skills/idea-storm/LICENSE) · [Происхождение и изменения](../skills/idea-storm/CHANGES.md).
- multi-layer-review · [MIT](../skills/multi-layer-review/LICENSE) · [Происхождение и изменения](../skills/multi-layer-review/CHANGES.md).
- project-audit · [MIT](../skills/project-audit/LICENSE) · [Происхождение и изменения](../skills/project-audit/CHANGES.md).
- agent-eval · [MIT](../skills/agent-eval/LICENSE) · [Происхождение и изменения](../skills/agent-eval/CHANGES.md).

[Каталог дополнений](README.md)
