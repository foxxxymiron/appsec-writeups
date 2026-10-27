# AppSec Writeups & Labs

[Русская версия](README.ru.md)

This repository contains my practical writeups and solutions for web security labs, primarily from **PortSwigger Web Security Academy**. 

It is part of my self-paced AppSec learning roadmap. The goal of this repository is to document my progress, demonstrate hands-on skills in identifying and exploiting web vulnerabilities, and serve as a personal knowledge base.

## 🎯 Roadmap Progress

- [x] **Stage 3:** Client-side part (HTML + CSS + JS) - *Completed in `appsec-messenger` repo*
- [x] **Stage 4:** Flask Backend & Auth - *Completed in `appsec-messenger-flask` repo*
- [x] **Stage 5:** SQLite Database & CRUD - *Completed in `appsec-messenger-flask` repo*
- [x] **Stage 6:** SQL Injection (In-band / UNION) - *Completed (see `sql-injection/` folder)*
- [x] **Stage 7:** Blind SQL Injection (Time, Boolean, Error) - *Completed (see `blind-sql-injection/` folder)*
- [ ] **Stage 8+:** XSS, CSRF, SSRF, etc. - *In progress*

## 🛠 Skills Demonstrated

- **SQL Injection (SQLi):** UNION-based attacks, Authentication Bypass, Data Exfiltration.
- **Blind SQL Injection:** Time-based, Boolean-based, and Error-based inference. Automation via Python scripts.
- *More to come: XSS, CSRF, SSRF, etc.*

## 📂 Repository Structure

```text
appsec-writeups/
├── sql-injection/          # In-band SQLi writeups
│   ├── screenshots/
│   └── 01-where-clause.md ...
├── blind-sql-injection/    # Inferential (Blind) SQLi writeups
│   ├── screenshots/
│   ├── scripts/            # Exploit automation scripts
│   ├── 01-blind-time-retrieval.md
│   ├── 02-blind-boolean.md
│   ├── 03-blind-error.md
│   ├── 04-full-db-dump.md
│   └── 05-protection-methods.md
└── README.md
```

## 📝 Methodology

For each lab, the writeup follows a standard structure:
1. **Vulnerability Analysis:** Understanding the root cause and the backend query.
2. **Exploitation Steps:** The exact payloads used and the logic behind them.
3. **Evidence:** Proof-of-concept (PoC) screenshots demonstrating the successful attack.
4. **Mitigation:** How the vulnerability should be fixed in the source code.

## 📚 Lab Index

### SQL Injection (In-band)
| # | Lab Name | Difficulty | Link |
|---|----------|------------|------|
| 01 | SQL injection in WHERE clause (Hidden Data) | Apprentice | [View Writeup](sql-injection/01-where-clause.md) |
| 02 | Login Bypass | Apprentice | [View Writeup](sql-injection/02-login-bypass.md) |
| 03 | Determining the number of columns | Practitioner | [View Writeup](sql-injection/03-union-columns.md) |
| 04 | Finding a column containing text | Practitioner | [View Writeup](sql-injection/04-union-find-text.md) |
| 05 | Retrieving data from other tables | Practitioner | [View Writeup](sql-injection/05-union-retrieve-data.md) |
| 06 | Retrieving multiple values in a single column | Practitioner | [View Writeup](sql-injection/06-union-single-column.md) |

### Blind SQL Injection (Inferential)
| # | Lab Name | Difficulty | Link |
|---|----------|------------|------|
| 01 | Time delays and information retrieval | Practitioner | [View Writeup](blind-sql-injection/01-blind-time-retrieval.md) |
| 02 | Conditional responses (Boolean-based) | Practitioner | [View Writeup](blind-sql-injection/02-blind-boolean.md) |
| 03 | Conditional errors (Error-based) | Practitioner | [View Writeup](blind-sql-injection/03-blind-error.md) |
| 04 | Full Database Dump (Automation) | Custom | [View Writeup](blind-sql-injection/04-full-db-dump.md) |
| 05 | Protection Methods Comparison | Theory | [View Writeup](blind-sql-injection/05-protection-methods.md) |

---

*Disclaimer: All attacks were performed on legal, intentionally vulnerable environments provided by PortSwigger Web Security Academy. This knowledge is intended for educational and defensive purposes only.*