---
name: multi-layer-review
description: >
  Multi-layer technical review for specs, ТЗ, and implementation plans using up to five
  independent reviewer perspectives (architecture, code-level, user POV, robustness, goals).
  Use when reviewing specs or technical designs before coding, or when user mentions
  "multi-layer review", "four reviewers", "несколько ревьюеров", "devil's advocate",
  "codex reviewer", "отдай на проверку", "проверь ТЗ", "review the spec", "review this design".
  Do NOT use for reviewing finished code or general Q&A.
---

# Multi-Layer Technical Review

## Overview

Проверь ТЗ с пяти ракурсов. При доступной делегации рецензенты работают независимо, с опорой на фактические файлы. Совпадения независимых выводов учитываются при синтезе.

---

## Step 0 — Согласовать ракурсы

Используй ракурсы, которые уже выбрал пользователь. Если ему важно сузить проверку, предложи назвать номера или ответить «все». При общей просьбе о полном ревью используй все пять. Слово «пропусти» означает пропуск, пустого выбора для запуска не требуется.

1. Цель и критерии успеха.
2. Архитектура и интерфейсы.
3. Практическая реализация и зависимости.
4. Сценарии пользователя и граничные случаи.
5. Надёжность и проверяемость.

## Step 0.5 — Получить и проверить спек

Перед запуском ревьюеров.

1. Определить источник спека:
   - Файл приложен к сообщению → прочитать доступным инструментом чтения
   - Путь к файлу указан → прочитать доступным инструментом чтения
   - Текст вставлен напрямую → использовать как есть
   - Ничего не приложено → спросить: "Пришли спек — файл или текст"

2. Проверить на PII/секреты:
   - Убери ключи, пароли и ненужные персональные данные из брифа и выдержек для рецензентов. Если без закрытых деталей независимая проверка невозможна, используй разрешённую локальную проверку координатора или обозначь пропуск.

3. Сохранить спек как переменную SPEC_CONTENT для подстановки в промпты.
   Во всех reviewer prompts заменять `[SPEC CONTENT]` на реальное содержимое спека.

4. Если спек > 10 000 символов — предупредить пользователя о возможно долгом ревью.

---

## Step 0.6 — Review Brief (автоматический)

**Формируется автоматически** после получения спека. Цель — дать ревьюерам полную картину, а не голый текст.

**Что собрать:**

1. **Что за проект** — название, стек, стадия (из структуры проекта, манифестов)
2. **Что за документ** — определить тип (спек, ТЗ, план, RFC, дизайн-док) по содержимому и заголовкам. Указать заголовок и размер
3. **Стадия по теме спека** — поиск по файлам по ключевым сущностям спека (модули, классы, API endpoints). Есть ли уже код по этой теме, или это с нуля?
4. **Связанные файлы** — какие файлы в проекте уже относятся к теме спека (результат поиска из п.3)

**Формат:** свободный текст, 3-5 предложений. Как если бы ты объяснял коллеге контекст перед ревью.

**Пример:**
```
REVIEW_BRIEF:
Проект TGmanager — Python CLI для работы с Telegram через Telethon. Проект в продакшне,
основной код в tg.py. Спек описывает новый модуль рассылки (broadcast). Кода рассылки
пока нет — это новый функционал. Связанные файлы: tg.py (точка входа, 200 строк),
config.py (конфиг сессии Telethon).
```

**Этот блок подставляется в `[REVIEW BRIEF]`** в каждом промпте ревьюера вместе с `[PROJECT CONTEXT]` и `[SPEC CONTENT]`.

---

## Step 0.7 — Spec Ambiguity Gate (автоматический)

**Запускается всегда** после получения спека, перед ревьюерами.

Проверить спек на:
- Неопределённые термины ("быстро", "много", "удобно" без критериев)
- Противоречия между секциями
- Отсутствующие ограничения (лимиты, тайм-ауты, объёмы данных)
- Неоднозначные требования (одну фразу можно понять двумя способами)

**Если проблем нет** — продолжить без сообщений.

**Если найдены проблемы** — показать список и спросить:
> "Спек содержит [N] неоднозначностей: [список]. Уточнить перед ревью или продолжить как есть?"

- Если уточняет → обновить SPEC_CONTENT и продолжить
- Если "продолжить" → добавить в начало каждого reviewer prompt:
  ```
  Note: spec has known ambiguities: [список]. Flag assumptions you make about them.
  ```

---

## Step 0.8 — Project Context Snapshot (одноразовый)

**Запускается один раз** после Ambiguity Gate, перед ревьюерами. Цель — собрать контекст проекта, чтобы ревьюеры работали с реальными данными, а не рассуждали в вакууме.

**Сбор контекста:**

1. **Структура проекта** — ограниченный список папок верхнего уровня для верхнеуровневой карты
2. **Манифесты** — чтение package.json / pyproject.toml / Cargo.toml / go.mod (что есть)
3. **Entry points** — чтение main/index файлы, точки входа
4. **Релевантный код** — поиск по файлам по ключевым сущностям из спека (имена модулей, API endpoints, классы). Читать найденные файлы через чтение
5. **Конфиги** — `.env.example`, docker-compose, CI configs (если упомянуты в спеке)

**Результат:** компактный блок `PROJECT_CONTEXT` (до ~2000 символов):

```
PROJECT_CONTEXT:
- Structure: [top-level dirs and key files]
- Stack: [language, framework, dependencies relevant to spec]
- Existing code: [summaries of files related to spec topics]
- Patterns: [architecture patterns found — e.g. "MVC", "event-driven", "monorepo"]
```

**Если проект пустой** (спек до начала разработки) — собрать только то что есть (может быть только README или ничего). Указать: "Project is empty — no existing code to reference."

**Этот блок подставляется в `[PROJECT CONTEXT]`** в каждом промпте ревьюера.

---

## Steps 1–5 — Проверить выбранные ракурсы

Каждому независимому рецензенту передай только свою роль, спек, бриф и относящийся к задаче снимок проекта. Используй штатную делегацию Codex в пределах текущих разрешений и настроек выбора моделей. Передавай самодостаточный запрос в отдельном контексте без истории основного чата. Если нет способа выделить такой контекст, применяй проверку координатора. Не передавай один ответ другому рецензенту. Рецензент читает указанные файлы и возвращает заключение. Изменения проекта и дальнейшая делегация ему не поручаются.

Запускай независимые вызовы параллельно в пределах доступных слотов или последовательно с раздельными контекстами. Если один ракурс недоступен независимо, обработай его сам по тем же вопросам и явно обозначь его как проверку координатора. Если делегация недоступна целиком, проверь выбранные ракурсы последовательно и не повышай важность находок за счёт якобы независимого совпадения. Отметь в отчёте, кто проверял каждый ракурс, что удалось прочитать и что пропущено.

### Common prompt block (подставляется в каждый промпт ревьюера)

```
Context:
[REVIEW BRIEF]

Project context:
[PROJECT CONTEXT]

Use the available read-only file and search tools. If the spec references existing
modules, APIs, or files — look them up in the project to verify claims.
Do NOT just reason abstractly — ground your review in actual project state.

OUTPUT FORMAT — for each finding, output EXACTLY:
- **[Critical/Important/Minor]** Section: "<spec section name>" — <finding in 1-2 sentences>

OUTPUT RULES:
- Maximum 10 findings, sorted by severity (Critical first)
- Every finding MUST reference a specific section of the spec
- Do NOT invent problems that don't exist in the spec
- Do NOT give generic advice ("add logging", "consider edge cases", "add tests")
- Only flag concrete, specific problems you can point to in the spec text
- If you find no issues in your area — say "No issues found" (this is a valid outcome)

Spec:
[SPEC CONTENT]
```

---

### Reviewer 1 — Requirements Traceability

**Role:** Проверяет что спек решает правильную задачу, а не просто правильно написан.

**Задание рецензенту:**
```
You are a requirements analyst. Your job is NOT to find bugs in the design —
it's to verify the design solves the actual problem.

[COMMON PROMPT BLOCK]

Additionally, for this spec answer:
1. What is the stated business/user goal? Is it explicitly defined?
2. Does the proposed solution actually achieve that goal? Or does it solve a related but different problem?
3. What does success look like? Are there measurable criteria?
4. What simpler solution was NOT considered? Why is this complexity justified?
5. Who is the user? Is the spec written for the right audience?

Be direct and proportional. Report facts, not fears.
```

**What it finds:** Solution solving wrong problem, missing success criteria, unjustified complexity, undefined target user.

**Когда использовать:** всегда — особенно когда ты сам формулируешь задачу на ходу, или когда не уверен что правильно понял что нужно сделать.

---

### Reviewer 2 — Architecture

**Role:** Structure, completeness, API design, trade-offs, edge cases.

**Задание рецензенту:**
```
You are a technical architect.

[COMMON PROMPT BLOCK]

Before reviewing, examine the project structure and existing code.
Check how existing modules are organized, what patterns are used, what dependencies
are already in place.

Review the spec for:
- Structural gaps and missing components
- API/interface design quality
- Trade-offs not considered
- Edge cases not covered
- Contradictions between sections
- Compatibility with existing project architecture (check actual files!)

Be proportional — distinguish real architectural problems from stylistic preferences.
```

**What it finds:** Missing abstractions, wrong layering, unclear contracts.

---

### Reviewer 3 — Практическая реализация

Проверить зависимости, пограничные условия API, ошибки и места, где план расходится с фактическим устройством проекта. Передай этот ракурс тем же способом, что и остальные. Дай рецензенту относящиеся к реализации фрагменты спека и пути к файлам. Используй формат из общего блока и приведи пути и строки фактически проверенных файлов. В проекте без кода оцени применимость ракурса и объясни пропуск.

### Reviewer 4 — Devil's Advocate Agent

**Role:** End-user perspective. Tries to break it.

**Задание рецензенту:**
```
You are a skeptical end user and QA engineer.

[COMMON PROMPT BLOCK]

Before reviewing: check the project for existing UX patterns, error messages,
user-facing flows. If there's existing UI code or CLI — read it to understand
the current user experience.

For each section of the spec, ask:
1. What happens when this fails?
2. What did the user NOT ask for but will expect?
3. What edge case will hit on day 1?

Be adversarial but proportional. Flag real user-facing problems.
Do NOT inflate hypothetical edge cases into critical issues — mark unlikely
scenarios as Minor unless they cause data loss or security problems.
```

**What it finds:** Missing UX flows, wrong defaults, surprise behaviors, missing "happy to sad path" transitions.

---

### Reviewer 5 — Robustness Checklist

**Role:** Systematic scan against known failure modes.

**Задание рецензенту:**
```
You are a reliability engineer.

[COMMON PROMPT BLOCK]

Before scoring: check the project for existing error handling patterns,
test infrastructure, logging setup, security measures. Score based on what
the spec ADDS or CHANGES relative to what already exists in the project.

Score each area 0-3. Flag areas scoring 0 or 1 as required fixes.

Areas: Error handling / Concurrency / Resource cleanup / Data integrity /
Performance / Security / Observability / Testability

For each area: score (0-3) + 1-line explanation of what's missing or present.
Base scores on evidence from the spec and project, not worst-case imagination.
A score of 0-1 means you found a concrete gap, not a theoretical one.

Additionally, output findings in the standard format (see OUTPUT FORMAT above).
```

Reference table for what each area checks:

| Area | Check |
|------|-------|
| **Error handling** | All external calls wrapped? Errors surface cleanly? |
| **Concurrency** | Thread safety? Race conditions? GUI/worker separation? |
| **Resource cleanup** | Temp files deleted? Connections closed? `finally` blocks? |
| **Data integrity** | Atomic writes? Partial failure leaves consistent state? |
| **Performance** | Blocking calls identified? Memory bounds for large inputs? |
| **Security** | User input sanitized? No path traversal? No shell injection? |
| **Observability** | Logging? Progress feedback? Error messages actionable? |
| **Testability** | Logic separated from I/O? Pure functions identifiable? |

---

### Independence Rule (BLIND REVIEW)

**DO NOT pass findings from one reviewer to another.** Each reviewer works
independently with only the spec + project context. This is by design:

- Eliminates confirmation bias and panic escalation
- Independent findings that converge = strong signal
- Independent findings that conflict = valuable for user to decide
- Deduplication happens in Synthesis (Step 6), not during review

---

## Step 6 — Synthesis

1. Собрать все findings от запущенных ревьюеров в один список.

2. **Дедупликация и валидация силой независимости:**
   Ревьюеры работали слепо — совпадения значат больше, чем раньше.
   - Если 2+ ревьюера **независимо** нашли одно и то же — это сильный сигнал.
     Пометить "(independently confirmed by N reviewers)" и повысить severity на один уровень
     (Minor→Important, Important→Critical). Но не выше Critical.
   - Если только 1 ревьюер нашёл — оставить его severity как есть.
   - **Не завышать severity при синтезе.** Задача синтеза — агрегировать, а не нагнетать.

3. **Разрешение противоречий:** если два ревьюера противоречат друг другу —
   отметить как "CONFLICT: [позиция A] vs [позиция B]" и вынести на решение пользователя.
   Не выбирать победителя самостоятельно.

4. **Категоризировать по критериям:**
   - **Critical**: ломает функциональность / данные / безопасность. Нельзя мержить.
   - **Important**: деградирует качество, есть workaround. Исправить до релиза.
   - **Minor**: улучшение UX, стиль, nice-to-have. Можно отложить.

5. Для каждого finding указать traceability:
   - Из какой секции спека (например: "Section 3 — API Design")
   - Какой ревьюер нашёл

6. Показать синтез пользователю. Отдельно назвать независимые вызовы, проверки координатора и пропуски.

7. **НЕ перезаписывать оригинальный спек.**
   Вместо этого: предложить список изменений и спросить:
   "Применить Critical + Important исправления к спеку? (y/n)"
   Если да — создать новую версию: `<original-name>-revised.md`

8. **Definition of Done:** ревью считается завершённым когда:
   - Все Critical issues либо исправлены либо явно приняты пользователем
   - Synthesis показан пользователю
   - Отчёт сохранён (Step 7), либо явно названа причина, по которой запись невозможна.

Скажи пользователю: не начинай разработку пока Critical issues не решены.

---

## Step 7 — Save to Disk

After presenting the synthesis, save the results to disk — the next session finds past reviews only there.

### Куда сохранять

1. Используй место, которое указал пользователь или которое задано действующими инструкциями проекта.
2. По умолчанию в проекте Codex сохраняй в `docs/reviews/` от подтверждённого корня проекта. Определи корень по текущему проекту, его инструкциям и Git, если он есть. Из вложенной папки используй корень нужного проекта, включая явно указанную вложенную область. При неоднозначности уточни, куда сохранить.
3. Если инструкции проекта задают папку проверок в памяти, убедись, что она относится к текущему проекту. Для memory-kit используй `projects_dir` из `memory-kit.json` активного профиля и существующую папку `<slug>/memory/reviews/`. В slug каждый символ полного пути, кроме ASCII-букв и цифр, заменяется дефисом. На Windows сопоставляй без учёта регистра. Если соответствие не подтверждено, используй папку проекта. Не создавай новую папку памяти по догадке.
4. Создай папку отчётов при необходимости и проверь, что она доступна. Выбери новое имя при совпадении.

### Slug rule for filename

- If spec has a filename → strip extension, lowercase, replace spaces/special chars with `-`, truncate to 40 chars
- If spec is inline text → take the first H1 heading (`# Title`), or the first non-empty line
- Strip Windows-illegal chars: `/ \ : * ? " < > |`
- Example: `"Auth Module ТЗ v2.pdf"` → `auth-module-v2`

Final filename: `YYYY-MM-DD-<slug>.md`

If a file with the same name already exists — append `-2`, `-3`, etc. Never silently overwrite.

### File format

```markdown
# Review: <spec name>
Date: YYYY-MM-DD
Skill version: 3.0
Reviewers run: [список запущенных]
Reviewers skipped: [список с причинами, или "none"]
Spec source: <filename or "inline text">

## Robustness Scores
| Area | Score |
|------|-------|
| Error handling | N/3 |
| Concurrency | N/3 |
| Resource cleanup | N/3 |
| Data integrity | N/3 |
| Performance | N/3 |
| Security | N/3 |
| Observability | N/3 |
| Testability | N/3 |

## Critical
- [finding] *(Section: X, Reviewer: Y)*

## Important
- [finding] *(Section: X, Reviewer: Y)*

## Minor
N issues. [one-sentence summary]

## Conflicts (требуют решения пользователя)
- [conflict description]

## Verdict
[Ready / Not ready / With fixes — one sentence]
```

Keep the file under 80 lines. This is a reference summary, not a transcript.

### Verification

Перечитай сохранённый файл и подтверди его полный путь. При ошибке записи сообщи причину.

### Tell the user

After successful save, say:
> Ревью сохранено: `<full-path>`

---

## Finding Past Reviews

Используй тот же путь поиска, что и для сохранения. Найди отчёт по имени спека или дате. При нескольких совпадениях покажи варианты. Проверяй только папку подтверждённого проекта.

## When to Skip a Reviewer

Если пользователь исключил ракурс или назначение документа делает его неприменимым, укажи это в отчёте. Недоступный независимый запуск замени проверкой координатора либо отметь пропуск с причиной. Для короткого спека смежные ракурсы можно объединить, если затем указать, что это один голос.

## Common Mistakes

- **Свести ревью к архитектуре** — теряются вопросы реализации и пользовательских сценариев
- **Skipping implementation review because it feels redundant** — it finds different things (dependency conflicts, unsafe string ops, missing exception types)
- **Not synthesizing** — presenting four separate reviews without reconciling them confuses the user
- **Passing findings between reviewers** — causes confirmation bias and panic escalation. Reviewers MUST work blind
- **Not deduplicating findings** — the list looks bigger but has less value
- **Overwriting original spec** — always create `-revised.md` instead
- **Reviewers reasoning without reading files** — every reviewer should use available read-only tools to ground analysis in actual project state
- **Inflating severity** — hypothetical edge cases are Minor unless they cause data loss or security issues. Be proportional
