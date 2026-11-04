---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/REMARK.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

Syntax

```
REM[ARK]
```

Begins a comment in a script. SQL\*Plus does not interpret the comment as a command.

Usage

The REMARK command must appear at the beginning of a line, and the comment ends at the end of the line. A line cannot contain both a comment and a command.

A "–" at the end of a REMARK line is treated as a line continuation character.

For details on entering comments in scripts using the SQL comment delimiters, /\*... \*/, or the ANSI/ISO comment delimiter, - -, see [About Placing Comments in Scripts](using-scripts-in-SQL-Plus.md).

Examples

The following script contains some typical comments:

```
REM COMPUTE uses BREAK ON REPORT to break on end of table
BREAK ON REPORT
COMPUTE SUM OF "DEPARTMENT 10" "DEPARTMENT 20" -
"DEPARTMENT 30" "TOTAL BY JOB_ID" ON REPORT
REM Each column displays the sums of salaries by job for
REM one of the departments 10, 20, 30.
SELECT JOB_ID,
SUM(DECODE( DEPARTMENT_ID, 10, SALARY, 0)) "DEPARTMENT 10",
SUM(DECODE( DEPARTMENT_ID, 20, SALARY, 0)) "DEPARTMENT 20",
SUM(DECODE( DEPARTMENT_ID, 30, SALARY, 0)) "DEPARTMENT 30",
SUM(SALARY) "TOTAL BY JOB_ID"
FROM EMP_DETAILS_VIEW
GROUP BY JOB_ID;
```