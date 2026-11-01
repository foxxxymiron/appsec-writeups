# AppSec Writeups & Labs

[English version](README.md)

Этот репозиторий содержит мои практические отчеты (writeups) и решения для лабораторий по веб-безопасности, в основном с **PortSwigger Web Security Academy**. 

Это часть моего самостоятельного учебного плана по AppSec. Цель репозитория — документировать прогресс, демонстрировать практические навыки поиска и эксплуатации уязвимостей, а также служить личной базой знаний.

## 🎯 Прогресс по роудмапу

- [x] **Этап 3:** Клиентская часть (HTML + CSS + JS) - *Завершено (репозиторий `appsec-messenger`)*
- [x] **Этап 4:** Flask Backend & Auth - *Завершено (репозиторий `appsec-messenger-flask`)*
- [x] **Этап 5:** SQLite Database & CRUD - *Завершено (репозиторий `appsec-messenger-flask`)*
- [x] **Этап 6:** SQL Injection (In-band / UNION) - *Завершено (папка `sql-injection/`)*
- [x] **Этап 7:** Blind SQL Injection (Time, Boolean, Error) - *Завершено (папка `blind-sql-injection/`)*
- [x] **Этап 8:** Cross-Site Scripting (XSS) - *Завершено (папка `xss/`)*
- [x] **Этап 9:** DOM-based XSS - *Завершено (папка `dom-xss/`)*
- [ ] **Этап 10+:** CSRF, SSRF и др. - *В процессе*

## 🛠 Продемонстрированные навыки

- **SQL-инъекции (SQLi):** UNION-атаки, обход авторизации, эксфильтрация данных.
- **Слепые SQL-инъекции (Blind SQLi):** Вывод данных на основе времени (Time-based), логики (Boolean-based) и ошибок (Error-based). Автоматизация через Python-скрипты.
- **Cross-Site Scripting (XSS):** Отраженный, Сохраненный, DOM-based. Разрыв контекста, обход HTML-кодирования, jQuery-стоки (sinks).
- *В планах: CSRF, SSRF и др.*

## 📂 Структура репозитория

```text
appsec-writeups/
├── sql-injection/          # Отчеты по In-band SQLi
│   ├── screenshots/
│   └── 01-where-clause.md ...
├── blind-sql-injection/    # Отчеты по слепым SQLi (Inferential)
│   ├── screenshots/
│   ├── scripts/            # Скрипты для автоматизации эксплуатации
│   ├── 01-blind-time-retrieval.md
│   └── ...
├── xss/                    # Отчеты по Cross-Site Scripting (Reflected / Stored)
│   ├── screenshots/
│   ├── 01-reflected-xss.md
│   ├── 02-stored-xss.md
│   ├── 03-dom-xss.md
│   └── 04-attribute-xss.md
├── dom-xss/                # Отчеты по DOM-based XSS
│   ├── screenshots/
│   ├── 01-dom-innerhtml.md
│   ├── 02-dom-jquery.md
│   ├── 03-dom-jquery-selector.md
│   └── 04-document-write-select.md
└── README.md
```

## 📝 Методология

Для каждой лаборатории отчет имеет стандартную структуру:
1. **Анализ уязвимости:** Понимание корневой причины и уязвимого кода.
2. **Шаги эксплуатации:** Точные пейлоады и логика их работы.
3. **Доказательства (PoC):** Скриншоты, демонстрирующие успешную атаку.
4. **Меры защиты (Mitigation):** Как уязвимость должна быть исправлена в исходном коде.

## 📚 Индекс лабораторий

### SQL-инъекции (In-band)
| # | Название | Сложность | Ссылка |
|---|----------|------------|------|
| 01 | SQL injection in WHERE clause (Hidden Data) | Apprentice | [View Writeup](sql-injection/01-where-clause.md) |
| 02 | Login Bypass | Apprentice | [View Writeup](sql-injection/02-login-bypass.md) |
| 03 | Determining the number of columns | Practitioner | [View Writeup](sql-injection/03-union-columns.md) |
| 04 | Finding a column containing text | Practitioner | [View Writeup](sql-injection/04-union-find-text.md) |
| 05 | Retrieving data from other tables | Practitioner | [View Writeup](sql-injection/05-union-retrieve-data.md) |
| 06 | Retrieving multiple values in a single column | Practitioner | [View Writeup](sql-injection/06-union-single-column.md) |

### Слепые SQL-инъекции (Inferential)
| # | Название | Сложность | Ссылка |
|---|----------|------------|------|
| 01 | Time delays and information retrieval | Practitioner | [View Writeup](blind-sql-injection/01-blind-time-retrieval.md) |
| 02 | Conditional responses (Boolean-based) | Practitioner | [View Writeup](blind-sql-injection/02-blind-boolean.md) |
| 03 | Conditional errors (Error-based) | Practitioner | [View Writeup](blind-sql-injection/03-blind-error.md) |
| 04 | Full Database Dump (Automation) | Custom | [View Writeup](blind-sql-injection/04-full-db-dump.md) |
| 05 | Protection Methods Comparison | Theory | [View Writeup](blind-sql-injection/05-protection-methods.md) |

### Cross-Site Scripting (XSS)
| # | Название | Сложность | Ссылка |
|---|----------|------------|------|
| 01 | Reflected XSS into HTML context | Apprentice | [View Writeup](xss/01-reflected-xss.md) |
| 02 | Stored XSS into HTML context | Apprentice | [View Writeup](xss/02-stored-xss.md) |
| 03 | DOM XSS in document.write sink | Apprentice | [View Writeup](xss/03-dom-xss.md) |
| 04 | Reflected XSS into attribute | Practitioner | [View Writeup](xss/04-attribute-xss.md) |

### DOM-based XSS
| # | Название | Сложность | Ссылка |
|---|----------|------------|------|
| 01 | DOM XSS in innerHTML sink using source location.search | Apprentice | [View Writeup](dom-xss/01-dom-innerhtml.md) |
| 02 | DOM XSS in jQuery anchor href attribute sink using location.search source | Apprentice | [View Writeup](dom-xss/02-dom-jquery.md) |
| 03 | DOM XSS in jQuery selector sink using a hashchange event | Apprentice | [View Writeup](dom-xss/03-dom-jquery-selector.md) |
| 04 | DOM XSS in document.write sink using source location.search inside a select element | Practitioner | [View Writeup](dom-xss/04-document-write-select.md) |

---

*Отказ от ответственности: Все атаки проводились на легальных, намеренно уязвимых средах, предоставленных PortSwigger Web Security Academy. Эти знания предназначены исключительно для образовательных и защитных целей.*