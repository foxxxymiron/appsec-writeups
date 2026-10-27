# Comparison of SQL Injection Mitigation Methods

## Introduction
This report compares approaches to protecting against SQL injections (specifically Blind SQLi). The core AppSec principle is **Defense in Depth**. Therefore, we compare methods of preventing injections with methods of mitigating damage from side-channels.

## 1. Injection Prevention
### Parameterized Queries (Prepared Statements)
- **Concept:** Data and code are passed to the DBMS separately.
- **Effectiveness against Blind SQLi:** **100%**. If the code is parameterized, the attacker cannot inject `SLEEP()`, `pg_sleep()`, or conditions like `1=1`.
- **Verdict:** **Gold standard.** Mandatory for use.

### Escaping Special Characters
- **Concept:** Manual replacement of quotes and special characters.
- **Effectiveness:** **Low.** Easily bypassed using Unicode, Hex encoding, or specific DBMS operators.
- **Verdict:** Outdated and dangerous approach.

## 2. Side-Channel Mitigation
Even with parameterization, DBMS response time can vary depending on the data (e.g., the difference between a Full Table Scan and an Index Seek). To combat Blind SQLi, the following are applied:
- **Query Timeout:** A hard limit on query execution time (e.g., 2 seconds). If an attacker injects `SLEEP(10)`, the query is killed. Response time becomes constant.
- **Rate Limiting:** Limiting the number of requests from a single IP (e.g., 10 requests per minute). Blind SQLi requires thousands of requests, making the attack infeasible.
- **Constant-Time Responses:** Artificial response delays on the backend to hide differences in SQL query execution time.

## 3. Additional Layers (Defense in Depth)
- **WAF (Web Application Firewall):** Can block known signatures (`SLEEP`, `UNION`), but is easily bypassed. Not a replacement for parameterization.
- **Principle of Least Privilege:** The DB user should only have `SELECT` rights to the necessary tables. Even if Blind SQLi succeeds, the attacker cannot drop the database (`DROP`).

## Conclusion
**Parameterization** is the only way to *prevent* an injection. 
**Timeouts and Rate Limiting** are mandatory measures to *prevent the exploitation* of Blind SQLi (side-channels).
Using only a WAF or escaping creates a false sense of security.