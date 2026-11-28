# Скиллы Эмиля Ковальски для интерфейсов

Установите нужные скиллы из каталога [skills](../skills/). В Codex можно попросить: «Установи `emil-design-eng`, `mobile-native` и `break-ui` из репозитория `KatariNa-codex/codex-workflow-kit`, папки `skills/<имя>`». Для установки в одном проекте скопируйте папки целиком в `.agents/skills/`. Если скилл с таким именем уже установлен, сравните версии. Для `ask-emil` оставьте рядом остальные скиллы набора, чтобы он мог читать их инструкции.

## Порядок работы

1. Для нового сайта определите структуру, главное действие и основные надписи. Авторский текст можно подготовить через [ru-writing](text-meetings.md#черновик-редактура-и-вычитка). Для визуального направления всей страницы используйте [design-first](../skills/design-first/SKILL.md).
2. Для отдельного меню, формы или карточки сравните рабочие варианты через `prototype`. После выбора доведите поведение через `emil-design-eng` или узкий скилл из таблицы.
3. Проверьте длинные заголовки, пустые списки и крайние значения через `break-ui`. Для мобильного веба добавьте `mobile-native`. Работу кнопок и форм проверьте через [webapp-testing](../skills/webapp-testing/SKILL.md).
4. Для готового интерфейса начните с наблюдаемой проблемы: рывки — `animation-performance`, лишнее движение — `remove-animations`, план улучшений — `improve-animations`.

Пример: «Проверь мобильную панель через `emil-design-eng` и `mobile-native`. Через `break-ui` проверь длинные русские заголовки и пустой список. После правок проверь, что кнопки работают».

## Состав

| Задача | Скилл | Когда использовать |
| --- | --- | --- |
| Выбор скилла и общая доводка | [ask-emil](../skills/ask-emil/SKILL.md) | Выберите один скилл или короткую связку для текущей задачи. |
| Выбор скилла и общая доводка | [emil-design-eng](../skills/emil-design-eng/SKILL.md) | Доработайте нажатия, подсказки, меню и другие детали взаимодействия. |
| Компоненты и прототипы | [prototype](../skills/prototype/SKILL.md) | Сравните несколько рабочих вариантов одного элемента. |
| Компоненты и прототипы | [pick-ui-library](../skills/pick-ui-library/SKILL.md) | Выберите библиотеку для нужного компонента. |
| Компоненты и прототипы | [ask-sonner](../skills/ask-sonner/SKILL.md) | Настройте уведомления в проекте с Sonner. |
| Веб-анимация | [animate](../skills/animate/SKILL.md) | Сделайте один переход или эффект. |
| Веб-анимация | [choreograph](../skills/choreograph/SKILL.md) | Согласуйте движения нескольких элементов. |
| Веб-анимация | [gestures](../skills/gestures/SKILL.md) | Настройте перетаскивание, свайпы и мобильные панели. |
| Веб-анимация | [animation-vocabulary](../skills/animation-vocabulary/SKILL.md) | Подберите точное название эффекта. |
| Проверка анимации | [review-animations](../skills/review-animations/SKILL.md) | Проверьте конкретную реализацию. |
| Проверка анимации | [improve-animations](../skills/improve-animations/SKILL.md) | Составьте план улучшений для существующего интерфейса. |
| Проверка анимации | [find-animation-opportunities](../skills/find-animation-opportunities/SKILL.md) | Найдите места, где движение поможет пользователю. |
| Проверка анимации | [remove-animations](../skills/remove-animations/SKILL.md) | Уберите движения, которые мешают работе. |
| Проверка анимации | [animation-performance](../skills/animation-performance/SKILL.md) | Найдите причину рывков и пропущенных кадров. |
| Мобильный интерфейс | [mobile-native](../skills/mobile-native/SKILL.md) | Проверьте клавиатуру, прокрутку и касания на мобильном вебе. |
| Мобильный интерфейс | [apple-design](../skills/apple-design/SKILL.md) | Примените принципы Apple к жестам и движению в вебе. |
| Мобильный интерфейс | [animate-expo](../skills/animate-expo/SKILL.md) | Добавьте анимацию в React Native или Expo. |
| Мобильный интерфейс | [write-swift](../skills/write-swift/SKILL.md) | Примените рекомендации к проекту на Swift. |
| Проверка экрана и фиксация решений | [break-ui](../skills/break-ui/SKILL.md) | Проверьте длинные надписи, пустые списки и другие крайние случаи. |
| Проверка экрана и фиксация решений | [learn-taste](../skills/learn-taste/SKILL.md) | Сохраните согласованные решения и их причины для следующих задач. |

Все 20 скиллов обнаружились в локальном Codex на Windows. На реальном интерфейсе этот набор пока не проверялся. [Исходник Эмиля Ковальски](https://github.com/emilkowalski/skills/tree/64eb3deb9a5fbfa041faf783e0bc3fd635872e9c) · [MIT](../skills/emil-design-eng/LICENSE).
