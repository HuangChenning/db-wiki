---
title: "/ (slash)"
book: "SQL*Plus User's Guide and Reference"
doc_id: E16604-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e16604/ch_twelve004.htm
tags:
  - oracle
  - 11g
  - sqlplus-users-guide-and-reference
---

---

Syntax

/(slash)

Executes the most recently executed SQL command or PL/SQL block which is stored in the SQL buffer.

The buffer has no command history and does not record SQL\*Plus commands.

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