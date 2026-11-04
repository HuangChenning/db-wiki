---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/RUN.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

Syntax

```
R[UN]
```

Lists and executes the SQL command or PL/SQL block currently stored in the SQL buffer.

Usage

RUN causes the last line of the SQL buffer to become the current line.

The slash command (/) functions similarly to RUN, but does not list the command in the SQL buffer on your screen. The SQL buffer always contains the last SQL statement or PL/SQL block entered.

Examples

Assume the SQL buffer contains the following script:

```
SELECT DEPARTMENT_ID
FROM EMP_DETAILS_VIEW
WHERE SALARY>12000
```

To RUN the script, enter

```
RUN
```
```
1  SELECT DEPARTMENT_ID
  2  FROM EMP_DETAILS_VIEW
  3 WHERE SALARY>12000

DEPARTMENT_ID
-------------
           90
           90
           90
           80
           80
           20

6 rows selected.
```