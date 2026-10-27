# AppSec Writeups & Labs

[English version](README.md)

Этот репозиторий содержит мои практические отчеты (writeups) и решения для лабораторий по веб-безопасности, в основном с **PortSwigger Web Security Academy**. 

Это часть моего самостоятельного учебного плана по AppSec. Цель репозитория — документировать прогресс, демонстрировать практические навыки поиска и эксплуатации уязвимостей и служить личной базой знаний.

## 🎯 Прогресс по роудмапу

- [x] **Этап 3:** Клиентская часть (HTML + CSS + JS) - *Завершено (репозиторий `appsec-messenger`)*
- [x] **Этап 4:** Flask Backend & Auth - *Завершено (репозиторий `appsec-messenger-flask`)*
- [x] **Этап 5:** SQLite Database & CRUD - *Завершено (репозиторий `appsec-messenger-flask`)*
- [x] **Этап 6:** SQL Injection (In-band / UNION) - *Завершено (папка `sql-injection/`)*
- [x] **Этап 7:** Blind SQL Injection (Time, Boolean, Error) - *Завершено (папка `blind-sql-injection/`)*
- [ ] **Этап 8+:** XSS, CSRF, SSRF и др. - *В процессе*

## 🛠 Продемонстрированные навыки

- **SQL-инъекции (SQLi):** UNION-атаки, обход авторизации, эксфильтрация данных.
- **Слепые SQL-инъекции (Blind SQLi):** Вывод данных на основе времени (Time-based), логики (Boolean-based) и ошибок (Error-based). Автоматизация через Python-скрипты.
- *В планах: XSS, CSRF, SSRF и др.*

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
│   ├── 02-blind-boolean.md
│   ├── 03-blind-error.md
│   ├── 04-full-db-dump.md
│   └── 05-protection-methods.ru.md
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
| # | Название лаборатории | Сложность | Ссылка |
|---|----------|------------|------|
| 01 | SQL injection in WHERE clause (Hidden Data) | Apprentice | [View Writeup](sql-injection/01-where-clause.md) |
| 02 | Login Bypass | Apprentice | [View Writeup](sql-injection/02-login-bypass.md) |
| 03 | Determining the number of columns | Practitioner | [View Writeup](sql-injection/03-union-columns.md) |
| 04 | Finding a column containing text | Practitioner | [View Writeup](sql-injection/04-union-find-text.md) |
| 05 | Retrieving data from other tables | Practitioner | [View Writeup](sql-injection/05-union-retrieve-data.md) |
| 06 | Retrieving multiple values in a single column | Practitioner | [View Writeup](sql-injection/06-union-single-column.md) |

### Слепые SQL-инъекции (Inferential)
| # | Название лаборатории | Сложность | Ссылка |
|---|----------|------------|------|
| 01 | Time delays and information retrieval | Practitioner | [View Writeup](blind-sql-injection/01-blind-time-retrieval.md) |
| 02 | Conditional responses (Boolean-based) | Practitioner | [View Writeup](blind-sql-injection/02-blind-boolean.md) |
| 03 | Conditional errors (Error-based) | Practitioner | [View Writeup](blind-sql-injection/03-blind-error.md) |
| 04 | Полный дамп базы данных (Автоматизация) | Custom | [View Writeup](blind-sql-injection/04-full-db-dump.md) |
| 05 | Сравнение методов защиты | Theory | [View Writeup](blind-sql-injection/05-protection-methods.ru.md) |

---

*Отказ от ответственности: Все атаки проводились на легальных, намеренно уязвимых средах, предоставленных PortSwigger Web Security Academy. Эти знания предназначены исключительно для образовательных и защитных целей.*