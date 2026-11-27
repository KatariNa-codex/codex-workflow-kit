# Чертежи и геоданные для Codex

В наборе 9 скиллов для чертежей, геометрии и карт. Можно установить один или несколько скиллов в учебный или рабочий проект.

[Скачать ZIP](downloads/workflow-kit-cad-geo-1.1.0.zip) · [Контрольная сумма SHA-256](downloads/workflow-kit-cad-geo-1.1.0.zip.sha256)

## Установить

1. Распакуйте ZIP. Откройте папку будущего проекта в Codex.
2. Попросите Codex скопировать выбранные папки из распакованной папки skills в .agents/skills проекта. Для ручной установки скопируйте те же папки сами. Если одноимённая папка уже существует, сначала сравните версии.
3. Откройте SKILL.md нужного скилла. Подготовьте зависимости из таблицы. Для cad-drawings и image-compare в копии скилла заполните поле python в scripts/local-runtime.json абсолютным путём к своему изолированному Python. Для DWG укажите установленный ODA File Converter в поле oda.
4. Начните новый чат в том же проекте. Например, попросите «Примени cad-drawings: прочитай единицы, слои и версию формата этого учебного DXF».

## Состав и проверка

| Скилл | Назначение | Зависимости | Что проверено на учебных данных |
| --- | --- | --- | --- |
| [cad-drawings](../skills/cad-drawings/SKILL.md) | Разбор DXF и преобразование DWG | Python 3.10+, ezdxf, pypdfium2 и Pillow. Для проверенного маршрута DWG нужен отдельно установленный ODA File Converter. | Прочитаны единицы и слой учебного DXF. После DXF → DWG → DXF сохранены слой и длина линии. Контрольная сумма исходника совпала. |
| [gdal](../skills/gdal/SKILL.md) | Конвертация растровых и векторных данных | Отдельная среда с утилитами GDAL. | Учебная сетка преобразована в GeoTIFF. Сверены размер и система координат. |
| [geopandas](../skills/geopandas/SKILL.md) | Чтение и преобразование векторных данных | Python с GeoPandas. | Вымышленная точка записана в GeoJSON, прочитана и преобразована в EPSG:32633. |
| [leaflet](../skills/leaflet/SKILL.md) | Интерактивные карты в веб-странице | Leaflet 1.9.4. Для самостоятельной разработки доступен npm. | Маркер GeoJSON и всплывающая подпись проверены в браузерном окружении без внешних карт. |
| [proj](../skills/proj/SKILL.md) | Проверка систем координат и преобразование точек | Отдельная среда с PROJ и базой EPSG. | cs2cs преобразовал точку с проверенным порядком осей. Сверены обе координаты. |
| [shapely](../skills/shapely/SKILL.md) | Операции над геометрией | Python с Shapely 2.2. | Проверены площадь пересечения и третья координата точки при сериализации. |
| [image-compare](../skills/image-compare/SKILL.md) | Сравнение снимков и визуальных экспортов | Python 3.12+, Pillow, NumPy, scikit-image. | Найден один заранее изменённый пиксель. Проверен отказ от перезаписи готового результата. |
| [pyqgis](../skills/pyqgis/SKILL.md) | Работа со слоями и Processing из Python | QGIS с комплектным Python. | QGIS 3.44.15 LTR на Windows: создан учебный слой EPSG:3857, записан GeoPackage и построен буфер 10 м. |
| [qgis-process](../skills/qgis-process/SKILL.md) | Запуск алгоритмов Processing из терминала | Утилита qgis_process из QGIS. | QGIS 3.44.15 LTR на Windows: буфер 10 м записан в GeoPackage и проверен через PyQGIS. Система координат, атрибут, границы и площадь совпали с результатом Python. |

Codex CLI нашёл эти скиллы после распаковки и копирования в отдельный проект. Проверки выполнены на вымышленных файлах. CAD/COM, точную печать, загрузку фоновых карт и интерактивные окна Codex Desktop и QGIS в этой серии не проверяли.

Зависимости и CAD-программы устанавливаются отдельно. В ZIP входят инструкции и помощники скиллов. У каждого скилла есть LICENSE и CHANGES.md со ссылкой на исходную ревизию.

## Источники и лицензии

- cad-drawings · [Лицензия](../skills/cad-drawings/LICENSE) · [Исходная ревизия и изменения](../skills/cad-drawings/CHANGES.md)
- gdal · [Лицензия](../skills/gdal/LICENSE) · [Исходная ревизия и изменения](../skills/gdal/CHANGES.md)
- geopandas · [Лицензия](../skills/geopandas/LICENSE) · [Исходная ревизия и изменения](../skills/geopandas/CHANGES.md)
- leaflet · [Лицензия](../skills/leaflet/LICENSE) · [Исходная ревизия и изменения](../skills/leaflet/CHANGES.md)
- proj · [Лицензия](../skills/proj/LICENSE) · [Исходная ревизия и изменения](../skills/proj/CHANGES.md)
- shapely · [Лицензия](../skills/shapely/LICENSE) · [Исходная ревизия и изменения](../skills/shapely/CHANGES.md)
- image-compare · [Лицензия](../skills/image-compare/LICENSE) · [Исходная ревизия и изменения](../skills/image-compare/CHANGES.md)

- pyqgis · [Лицензия](../skills/pyqgis/LICENSE) · [Исходная ревизия и изменения](../skills/pyqgis/CHANGES.md)
- qgis-process · [Лицензия](../skills/qgis-process/LICENSE) · [Исходная ревизия и изменения](../skills/qgis-process/CHANGES.md)

[Каталог дополнений](README.md)
