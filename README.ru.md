# AppSec Writeups & Labs

[English Version](README.md)

Этот репозиторий содержит мои практические отчёты и решения лабораторных работ по веб-безопасности, в основном из **PortSwigger Web Security Academy** и **Root-Me**.

Это часть моего самостоятельного плана обучения AppSec. Цель этого репозитория — документировать мой прогресс, демонстрировать практические навыки поиска и эксплуатации веб-уязвимостей, а также служить личной базой знаний.

## 🎯 Прогресс по дорожной карте

- [x] **Этап 3:** Клиентская часть (HTML + CSS + JS) - *Завершено в репозитории `appsec-messenger`*
- [x] **Этап 4:** Flask Backend и Аутентификация - *Завершено в репозитории `appsec-messenger-flask`*
- [x] **Этап 5:** База данных SQLite и CRUD - *Завершено в репозитории `appsec-messenger-flask`*
- [x] **Этап 6:** SQL-инъекции (In-band / UNION) - *Завершено (см. папку `sql-injection/`)*
- [x] **Этап 7:** Слепые SQL-инъекции (Time, Boolean, Error) - *Завершено (см. папку `blind-sql-injection/`)*
- [x] **Этап 8:** Межсайтовый скриптинг (XSS) - *Завершено (см. папку `xss/`)*
- [x] **Этап 9:** DOM-based XSS - *Завершено (см. папку `dom-xss/`)*
- [x] **Этап 10:** Подделка межсайтовых запросов (CSRF) - *Завершено (см. папку `csrf/`)*
- [x] **Этап 11:** Подделка запросов на стороне сервера (SSRF) - *Завершено (см. папку `ssrf/`)*
- [x] **Этап 12:** Уязвимости бизнес-логики - *Завершено (см. папку `blv/`)*
- [x] **Этап 13:** Обход путей (Path Traversal) - *Завершено (см. папку `dt/`)*
- [x] **Этап 14:** Локальное включение файлов (LFI) - *Завершено (см. папку `lfi/`)*
- [x] **Этап 15:** Кликджекинг (UI Redressing) - *Завершено (см. папку `clickjacking/`)*
- [ ] **Этап 16+:** RFI, XXE, Десериализация и др. - *В процессе*

## 🛠 Продемонстрированные навыки

- **SQL-инъекции (SQLi):** Атаки через UNION, обход аутентификации, эксфильтрация данных.
- **Слепые SQL-инъекции:** Вывод данных через временные задержки, булевы условия и ошибки. Автоматизация через Python-скрипты.
- **Межсайтовый скриптинг (XSS):** Отражённый, хранимый и DOM-based. Разрыв контекстов, обход HTML-кодирования, jQuery sinks.
- **Подделка межсайтовых запросов (CSRF):** Обход отсутствующих защит, трюки с переопределением методов, уязвимости токенов сессии, обход SameSite/Referer.
- **Подделка запросов на стороне сервера (SSRF):** Сканирование внутренних сетей, обход чёрных и белых списков, эксплуатация открытых редиректов.
- **Уязвимости бизнес-логики:** Изменение цен, отрицательные количества, обход рабочих процессов, логические ошибки «бесконечных денег».
- **Обход путей (Path Traversal):** Обход фильтров через абсолютные пути, нерекурсивную очистку, URL-кодирование, проверку префиксов и нулевые байты.
- **Локальное включение файлов (LFI):** Обход ограничений `open_basedir`, двойное URL-кодирование для победы над фильтрами, PHP stream wrappers (`zip://`, `php://`, `data://`) для чтения произвольных файлов и выполнения кода через цепочки загрузки + включения.
- **Кликджекинг (UI Redressing):** Обход CSRF-токенов через iframe-наложения, манипуляция предзаполненными формами, обход frame-buster скриптов (`sandbox`), комбинирование кликджекинга с DOM-based XSS и многоэтапные атаки.
- *Далее: Удалённое включение файлов (RFI), XXE, Десериализация и др.*

## 📂 Структура репозитория

```text
appsec-writeups/
├── sql-injection/            # Отчёты по In-band SQLi
│   ├── screenshots/
│   └── 01-where-clause.md ...
├── blind-sql-injection/      # Отчёты по слепым SQLi
│   ├── screenshots/
│   ├── scripts/              # Скрипты автоматизации эксплойтов
│   ├── 01-blind-time-retrieval.md
│   └── ...
├── xss/                      # Отчёты по XSS (Reflected / Stored)
│   ├── screenshots/
│   ├── 01-reflected-xss.md
│   ├── 02-stored-xss.md
│   ├── 03-dom-xss.md
│   └── 04-attribute-xss.md
├── dom-xss/                  # Отчёты по DOM-based XSS
│   ├── screenshots/
│   ├── 01-dom-innerhtml.md
│   ├── 02-dom-jquery.md
│   ├── 03-dom-jquery-selector.md
│   └── 04-document-write-select.md
├── csrf/                     # Отчёты по CSRF
│   ├── screenshots/
│   ├── 01-csrf-no-defenses.md
│   ├── 02-csrf-method-override.md
│   ├── 03-csrf-token-session.md
│   ├── 04-csrf-samesite-lax.md
│   └── 05-csrf-referer-validation.md
├── ssrf/                     # Отчёты по SSRF
│   ├── screenshots/
│   ├── 01-basic-ssrf-local.md
│   ├── 02-basic-ssrf-backend.md
│   ├── 03-ssrf-blacklist.md
│   ├── 04-ssrf-open-redirect.md
│   └── 05-ssrf-whitelist.md
├── blv/                      # Уязвимости бизнес-логики
│   ├── screenshots/
│   ├── 01-excessive-trust.md
│   ├── 02-high-level-logic.md
│   ├── 03-workflow-validation.md
│   └── 04-infinite-money.md
├── dt/                       # Отчёты по Path Traversal
│   ├── screenshots/
│   ├── 01-simple-case.md
│   ├── 02-absolute-path.md
│   ├── 03-prefix-validation.md
│   ├── 04-non-recursive.md
│   ├── 05-url-decode.md
│   └── 06-null-byte.md
├── lfi/                      # Отчёты по LFI (Root-Me)
│   ├── screenshots/
│   ├── 01-lfi.md
│   ├── 01-lfi.ru.md
│   ├── 02-lfi-double-encoding.md
│   ├── 02-lfi-double-encoding.ru.md
│   ├── 03-lfi-wrappers.md
│   └── 03-lfi-wrappers.ru.md
├── clickjacking/             # Отчёты по кликджекингу (PortSwigger)
│   ├── screenshots/
│   ├── 01-basic-clickjacking-csrf.md
│   ├── 01-basic-clickjacking-csrf.ru.md
│   ├── 02-clickjacking-prefilled.md
│   ├── 02-clickjacking-prefilled.ru.md
│   ├── 03-clickjacking-frame-buster.md
│   ├── 03-clickjacking-frame-buster.ru.md
│   ├── 04-clickjacking-dom-xss.md
│   ├── 04-clickjacking-dom-xss.ru.md
│   ├── 05-multistep-clickjacking.md
│   └── 05-multistep-clickjacking.ru.md
└── README.md
```
## 📝 Методология

Для каждой лабы отчёт следует стандартной структуре:
1. **Анализ уязвимости:** Понимание первопричины и backend-запроса.
2. **Шаги эксплуатации:** Точные пейлоады и логика их работы.
3. **Доказательства:** Скриншоты Proof-of-concept (PoC), демонстрирующие успешную атаку.
4. **Меры по устранению:** Как уязвимость должна быть исправлена в исходном коде.

## 📚 Индекс лабораторных работ

### SQL-инъекции (In-band)
| # | Название лабы | Сложность | Ссылка |
|---|----------|------------|------|
| 01 | SQL-инъекция в WHERE clause (Hidden Data) | Apprentice | [Смотреть отчёт](sql-injection/01-where-clause.md) |
| 02 | Обход входа в систему | Apprentice | [Смотреть отчёт](sql-injection/02-login-bypass.md) |
| 03 | Определение количества столбцов | Practitioner | [Смотреть отчёт](sql-injection/03-union-columns.md) |
| 04 | Поиск столбца с текстом | Practitioner | [Смотреть отчёт](sql-injection/04-union-find-text.md) |
| 05 | Получение данных из других таблиц | Practitioner | [Смотреть отчёт](sql-injection/05-union-retrieve-data.md) |
| 06 | Получение нескольких значений в одном столбце | Practitioner | [Смотреть отчёт](sql-injection/06-union-single-column.md) |

### Слепые SQL-инъекции (Inferential)
| # | Название лабы | Сложность | Ссылка |
|---|----------|------------|------|
| 01 | Временные задержки и получение информации | Practitioner | [Смотреть отчёт](blind-sql-injection/01-blind-time-retrieval.md) |
| 02 | Условные ответы (Boolean-based) | Practitioner | [Смотреть отчёт](blind-sql-injection/02-blind-boolean.md) |
| 03 | Условные ошибки (Error-based) | Practitioner | [Смотреть отчёт](blind-sql-injection/03-blind-error.md) |
| 04 | Полный дамп БД (Автоматизация) | Custom | [Смотреть отчёт](blind-sql-injection/04-full-db-dump.md) |
| 05 | Сравнение методов защиты | Theory | [Смотреть отчёт](blind-sql-injection/05-protection-methods.md) |

### Межсайтовый скриптинг (XSS)
| # | Название лабы | Сложность | Ссылка |
|---|----------|------------|------|
| 01 | Отражённый XSS в HTML-контексте | Apprentice | [Смотреть отчёт](xss/01-reflected-xss.md) |
| 02 | Хранимый XSS в HTML-контексте | Apprentice | [Смотреть отчёт](xss/02-stored-xss.md) |
| 03 | DOM XSS в sink document.write | Apprentice | [Смотреть отчёт](xss/03-dom-xss.md) |
| 04 | Отражённый XSS в атрибуте | Practitioner | [Смотреть отчёт](xss/04-attribute-xss.md) |

### DOM-based XSS
| # | Название лабы | Сложность | Ссылка |
|---|----------|------------|------|
| 01 | DOM XSS в innerHTML sink через source location.search | Apprentice | [Смотреть отчёт](dom-xss/01-dom-innerhtml.md) |
| 02 | DOM XSS в jQuery anchor href attribute sink через source location.search | Apprentice | [Смотреть отчёт](dom-xss/02-dom-jquery.md) |
| 03 | DOM XSS в jQuery selector sink через событие hashchange | Apprentice | [Смотреть отчёт](dom-xss/03-dom-jquery-selector.md) |
| 04 | DOM XSS в document.write sink через source location.search внутри select | Practitioner | [Смотреть отчёт](dom-xss/04-document-write-select.md) |

### Подделка межсайтовых запросов (CSRF)
| # | Название лабы | Сложность | Ссылка |
|---|----------|------------|------|
| 01 | CSRF без защит | Apprentice | [Смотреть отчёт](csrf/01-csrf-no-defenses.md) |
| 02 | CSRF, где валидация токена зависит от метода запроса | Practitioner | [Смотреть отчёт](csrf/02-csrf-method-override.md) |
| 03 | CSRF, где токен не привязан к сессии пользователя | Practitioner | [Смотреть отчёт](csrf/03-csrf-token-session.md) |
| 04 | Обход SameSite Lax через переопределение метода | Practitioner | [Смотреть отчёт](csrf/04-csrf-samesite-lax.md) |
| 05 | CSRF, где валидация Referer зависит от наличия заголовка | Practitioner | [Смотреть отчёт](csrf/05-csrf-referer-validation.md) |

### Подделка запросов на стороне сервера (SSRF)
| # | Название лабы | Сложность | Ссылка |
|---|----------|------------|------|
| 01 | Базовый SSRF против локального сервера | Apprentice | [Смотреть отчёт](ssrf/01-basic-ssrf-local.md) |
| 02 | Базовый SSRF против другой бэкенд-системы | Apprentice | [Смотреть отчёт](ssrf/02-basic-ssrf-backend.md) |
| 03 | SSRF с фильтром на основе чёрного списка | Practitioner | [Смотреть отчёт](ssrf/03-ssrf-blacklist.md) |
| 04 | SSRF с обходом фильтра через открытый редирект | Practitioner | [Смотреть отчёт](ssrf/04-ssrf-open-redirect.md) |
| 05 | SSRF с фильтром на основе белого списка | Expert | [Смотреть отчёт](ssrf/05-ssrf-whitelist.md) |

### Уязвимости бизнес-логики
| # | Название лабы | Сложность | Ссылка |
|---|----------|------------|------|
| 01 | Чрезмерное доверие клиентским элементам управления | Apprentice | [Смотреть отчёт](blv/01-excessive-trust.md) |
| 02 | Уязвимость высокоуровневой логики | Apprentice | [Смотреть отчёт](blv/02-high-level-logic.md) |
| 03 | Недостаточная проверка рабочего процесса | Practitioner | [Смотреть отчёт](blv/03-workflow-validation.md) |
| 04 | Логическая ошибка «бесконечных денег» | Practitioner | [Смотреть отчёт](blv/04-infinite-money.md) |

### Обход путей (Path Traversal)
| # | Название лабы | Сложность | Ссылка |
|---|----------|------------|------|
| 01 | Обход пути к файлу, простой случай | Apprentice | [Смотреть отчёт](dt/01-simple-case.md) |
| 02 | Обход пути, блокировка последовательностей с обходом абсолютным путём | Practitioner | [Смотреть отчёт](dt/02-absolute-path.md) |
| 03 | Обход пути, проверка начала пути | Practitioner | [Смотреть отчёт](dt/03-prefix-validation.md) |
| 04 | Обход пути, нерекурсивная очистка последовательностей | Practitioner | [Смотреть отчёт](dt/04-non-recursive.md) |
| 05 | Обход пути, очистка последовательностей с избыточным URL-декодированием | Practitioner | [Смотреть отчёт](dt/05-url-decode.md) |
| 06 | Обход пути, проверка расширения файла с обходом нулевым байтом | Practitioner | [Смотреть отчёт](dt/06-null-byte.md) |

### Локальное включение файлов (LFI) — Root-Me
| # | Название лабы | Сложность | Ссылка |
|---|----------|------------|------|
| 01 | Локальное включение файлов (обход open_basedir) | 30 pts | [Смотреть отчёт](lfi/01-lfi.md) |
| 02 | Локальное включение файлов - Двойное кодирование | 30 pts | [Смотреть отчёт](lfi/02-lfi-double-encoding.md) |
| 03 | Локальное включение файлов - Врапперы (zip://) | 40 pts | [Смотреть отчёт](lfi/03-lfi-wrappers.md) |

### Кликджекинг (UI Redressing) — PortSwigger
| # | Название лабы | Сложность | Ссылка |
|---|----------|------------|------|
| 01 | Базовый кликджекинг с защитой CSRF-токеном | Practitioner | [Смотреть отчёт](clickjacking/01-basic-clickjacking-csrf.md) |
| 02 | Кликджекинг с предзаполнением формы из параметра URL | Practitioner | [Смотреть отчёт](clickjacking/02-clickjacking-prefilled.md) |
| 03 | Кликджекинг со скриптом frame buster | Practitioner | [Смотреть отчёт](clickjacking/03-clickjacking-frame-buster.md) |
| 04 | Эксплуатация кликджекинга для запуска DOM-based XSS | Practitioner | [Смотреть отчёт](clickjacking/04-clickjacking-dom-xss.md) |
| 05 | Многоэтапный кликджекинг | Practitioner | [Смотреть отчёт](clickjacking/05-multistep-clickjacking.md) |

---

*Отказ от ответственности: Все атаки проводились на легальных, преднамеренно уязвимых средах, предоставленных PortSwigger Web Security Academy и Root-Me. Эти знания предназначены исключительно для образовательных и защитных целей.*