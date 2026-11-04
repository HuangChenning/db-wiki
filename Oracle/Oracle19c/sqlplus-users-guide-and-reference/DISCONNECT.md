---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: E96459-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqpug/DISCONNECT.html
tags:
  - oracle
  - 19c
  - sqlplus-users-guide-and-reference
---

## 12.20 DISCONNECT

Syntax

```
DISC[ONNECT]
```

Commits pending changes to the database and logs the current username out of Oracle Database, but does not exit SQL\*Plus.

Usage

Use DISCONNECT within a script to prevent user access to the database when you want to log the user out of Oracle Database but have the user remain in SQL\*Plus. In SQL\*Plus command-line, use EXIT or QUIT to log out of Oracle Database and return control to your computer's operating system.

Examples

Your script might begin with a CONNECT command and end with a DISCONNECT, as shown later.

```
CONNECT HR
SELECT LAST_NAME, DEPARTMENT_NAME FROM EMP_DETAILS_VIEW;
DISCONNECT
SET INSTANCE FIN2
CONNECT HR2
```