# AppSec Writeups & Labs

This repository contains my practical writeups and solutions for web security labs, primarily from **PortSwigger Web Security Academy**. 

It is part of my self-paced AppSec learning roadmap. The goal of this repository is to document my progress, demonstrate hands-on skills in identifying and exploiting web vulnerabilities, and serve as a personal knowledge base.

## 🛠 Skills Demonstrated

- **SQL Injection (SQLi):** UNION-based attacks, Authentication Bypass, Data Exfiltration, determining query structure.
- *More to come: Blind SQLi, XSS, CSRF, SSRF, etc.*

## 📂 Repository Structure

The repository is organized by vulnerability type, following the OWASP categorization:

```text
appsec-writeups/
├── sql-injection/          # SQLi writeups
│   ├── screenshots/        # Evidence and PoC images
│   ├── 01-where-clause.md
│   └── ...
└── README.md
```

## 📝 Methodology

For each lab, the writeup follows a standard structure:
1. **Vulnerability Analysis:** Understanding the root cause and the backend query.
2. **Exploitation Steps:** The exact payloads used and the logic behind them.
3. **Evidence:** Proof-of-concept (PoC) screenshots demonstrating the successful attack.
4. **Mitigation:** How the vulnerability should be fixed in the source code (e.g., Prepared Statements).

## 📚 Lab Index

### SQL Injection
| # | Lab Name | Difficulty | Link |
|---|----------|------------|------|
| 01 | SQL injection in WHERE clause (Hidden Data) | Apprentice | [View Writeup](sql-injection/01-where-clause.md) |
| 02 | Login Bypass | Apprentice | [View Writeup](sql-injection/02-login-bypass.md) |
| 03 | Determining the number of columns | Practitioner | [View Writeup](sql-injection/03-union-columns.md) |
| 04 | Finding a column containing text | Practitioner | [View Writeup](sql-injection/04-union-find-text.md) |
| 05 | Retrieving data from other tables | Practitioner | [View Writeup](sql-injection/05-union-retrieve-data.md) |
| 06 | Retrieving multiple values in a single column | Practitioner | [View Writeup](sql-injection/06-union-single-column.md) |

---

*Disclaimer: All attacks were performed on legal, intentionally vulnerable environments provided by PortSwigger Web Security Academy. This knowledge is intended for educational and defensive purposes only.*