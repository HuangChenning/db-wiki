---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/slash.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

Syntax

/(slash)

Executes the most recently executed SQL command or PL/SQL block which is stored in the SQL buffer.

Usage

You can enter a slash (/) at the command prompt or at a line number prompt of a multi-line command.

The slash command functions similarly to RUN, but does not list the command.

Executing a SQL command or PL/SQL block using the slash command will not cause the current line number in the SQL buffer to change unless the command in the buffer contains an error. In that case, SQL\*Plus changes the current line number to the number of the line containing the error.

Examples

Type the following SQL script:

```
SELECT CITY, COUNTRY_NAMEFROM EMP_DETAILS_VIEWWHERE SALARY=12000;
```

Enter a slash (/) to re-execute the command in the buffer:

```
/
```
```
CITY                           COUNTRY_NAME
------------------------------ ----------------------------------------
Seattle                        United States of America
Oxford                         United Kingdom
Seattle                        United States of America
```