# AppSec Writeups & Labs

[English version](README.md)

Этот репозиторий содержит мои практические отчеты (writeups) и решения для лабораторий по веб-безопасности, в основном с **PortSwigger Web Security Academy**. 

Это часть моего самостоятельного учебного плана по AppSec. Цель репозитория — документировать прогресс и демонстрировать практические навыки поиска и эксплуатации уязвимостей.

## 🎯 Прогресс по роудмапу

- [x] **Этап 3:** Клиентская часть (HTML/CSS/JS) - *Завершено (репозиторий `appsec-messenger`)*
- [x] **Этап 4:** Flask Backend & Auth - *Завершено (репозиторий `appsec-messenger-flask`)*
- [x] **Этап 5:** SQLite Database & CRUD - *Завершено (репозиторий `appsec-messenger-flask`)*
- [x] **Этап 6:** SQL Injection (In-band / UNION) - *Завершено (папка `sql-injection/`)*
- [x] **Этап 7:** Blind SQL Injection (Time, Boolean, Error) - *Завершено (папка `blind-sql-injection/`)*
- [x] **Этап 8:** Cross-Site Scripting (XSS) - *Завершено (папка `xss/`)*
- [ ] **Этап 9+:** CSRF, SSRF и др. - *В процессе*

## 🛠 Продемонстрированные навыки

- **SQL-инъекции:** UNION-атаки, обход авторизации, эксфильтрация данных.
- **Слепые SQL-инъекции:** Вывод данных на основе времени (Time-based), логики (Boolean-based) и ошибок (Error-based). Автоматизация через Python-скрипты.
- **Cross-Site Scripting (XSS):** Отраженный, Сохраненный, DOM-based. Разрыв контекста, обход HTML-кодирования.
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
├── xss/                    # Отчеты по Cross-Site Scripting
│   ├── screenshots/
│   ├── 01-reflected-xss.md
│   ├── 02-stored-xss.md
│   ├── 03-dom-xss.md
│   └── 04-attribute-xss.md
└── README.md
```

## 📝 Методология

Для каждой лаборатории отчет имеет стандартную структуру:
1. **Анализ уязвимости:** Понимание корневой причины и SQL-запроса на бэкенде.
2. **Шаги эксплуатации:** Точные пейлоады и логика их работы.
3. **Доказательства (PoC):** Скриншоты, демонстрирующие успешную атаку.
4. **Меры защиты (Mitigation):** Как уязвимость должна быть исправлена в исходном коде.

## 📚 Индекс лабораторий

### SQL-инъекции (In-band)
| # | Название | Сложность | Ссылка |
|---|----------|------------|------|
| 01 | SQL injection in WHERE clause | Apprentice | [View](sql-injection/01-where-clause.md) |
| 02 | Login Bypass | Apprentice | [View](sql-injection/02-login-bypass.md) |
| 03 | Determining the number of columns | Practitioner | [View](sql-injection/03-union-columns.md) |
| 04 | Finding a column containing text | Practitioner | [View](sql-injection/04-union-find-text.md) |
| 05 | Retrieving data from other tables | Practitioner | [View](sql-injection/05-union-retrieve-data.md) |
| 06 | Retrieving multiple values in a single column | Practitioner | [View](sql-injection/06-union-single-column.md) |

### Слепые SQL-инъекции (Inferential)
| # | Название | Сложность | Ссылка |
|---|----------|------------|------|
| 01 | Time delays and information retrieval | Practitioner | [View](blind-sql-injection/01-blind-time-retrieval.md) |
| 02 | Conditional responses (Boolean-based) | Practitioner | [View](blind-sql-injection/02-blind-boolean.md) |
| 03 | Conditional errors (Error-based) | Practitioner | [View](blind-sql-injection/03-blind-error.md) |
| 04 | Full Database Dump | Custom | [View](blind-sql-injection/04-full-db-dump.ru.md) |
| 05 | Protection Methods | Theory | [View](blind-sql-injection/05-protection-methods.ru.md) |

### Cross-Site Scripting (XSS)
| # | Название | Сложность | Ссылка |
|---|----------|------------|------|
| 01 | Reflected XSS into HTML context | Apprentice | [View](xss/01-reflected-xss.md) |
| 02 | Stored XSS into HTML context | Apprentice | [View](xss/02-stored-xss.md) |
| 03 | DOM XSS in document.write sink | Apprentice | [View](xss/03-dom-xss.md) |
| 04 | Reflected XSS into attribute | Practitioner | [View](xss/04-attribute-xss.md) |

---
*Отказ от ответственности: Все атаки проводились на легальных, намеренно уязвимых средах.*