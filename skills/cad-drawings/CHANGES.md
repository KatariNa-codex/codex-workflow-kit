# Подготовка адаптации

В рабочей копии уточнены ограничения CAD/COM и добавлена проверка путей и точек соединения каталогов при очистке.

Сохранены текущие проверки путей, ограничения CAD/COM и выбор ODA. Вместо путей владельца конфигурация требует явно указать Python получателя и при необходимости ODA.

[Исходная версия](https://github.com/numikel/cad-drawings/tree/1522c9937bc1451d003b4474136461cf805578db/skills/cad-drawings). Лицензия сохранена в LICENSE. Отпечаток рабочей копии до подготовки: `01a9fbeb451c9a54301164f6c9a250418454134b42bb39995378e9bb60002563`.

The thematic release includes the current ODA-aware launcher workflow. The Python and ODA paths start empty for the recipient. The launcher retains explicit validation of the configured Python path.
