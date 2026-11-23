# Изменения mermaid-tools

Рабочая версия рендерит через переносимый Python-скрипт, проверяет PNG и использует новый каталог. Старый shell-вход оставлен для подсказки. Для репозитория восстановлена атрибуция и обновлены памятки и справка под действующий Python-запуск.

Основа — скилл daymade, MIT. Рабочая копия сверена с [закреплённым промежуточным снимком](https://github.com/GuruDevvv/my-claude-skills/tree/b5c44a9b7ec4a2620d7c7824cc4df22b940ae6dd/external/mermaid-tools). Точный исходный коммит daymade для этого снимка не установлен. Авторское уведомление сохранено в [LICENSE](LICENSE).

## Контрольные суммы рабочей копии на 22 ноября 2026 года

- `README.md` · `fcdaa07ee1c9cd02ebb9a1326a67f608812f9304b25bc4c94ccd87d22c63a428`
- `references/setup_and_troubleshooting.md` · `eb9e2958d559b0b14947fdf4020e2920184d9525fbb74e2dafcd561d882d8b77`
- `scripts/extract-and-generate.sh` · `a53f595e56ff6682f55eb9ca9e709b2090a3d6a8f01b79abecd0efa89543fb87`
- `scripts/extract_and_generate.py` · `55d4a6384adfe4caac099cde2420720af22e7f1827adae3efcad297902406f29`
- `scripts/extract_diagrams.py` · `545d812272d9627959f84e5827900ec9b156ab6952856efeff5a0383bbdf8389`
- `scripts/puppeteer-config.json` · `62868aec744a24c6f548047cb718692d35d14c768c0edfe23964e7796e4ed0bf`
- `SKILL.md` · `0535309e4577a043e1629c66ecb08fb93d490dd9161c954a8d87bf86cafd289d`
- `КАК_ИСПОЛЬЗОВАТЬ.md` · `fcdaa07ee1c9cd02ebb9a1326a67f608812f9304b25bc4c94ccd87d22c63a428`

The Windows launcher now also resolves the Mermaid CLI package next to npm’s project-local .bin directory. It invokes the Node entry directly.
