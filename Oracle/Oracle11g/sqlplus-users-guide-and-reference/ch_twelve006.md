---
title: APPEND
book: "SQL*Plus User's Guide and Reference"
doc_id: E16604-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e16604/ch_twelve006.htm
tags:
  - oracle
  - 11g
  - sqlplus-users-guide-and-reference
---

---

Syntax

A\[PPEND\] text

where text represents the text to append.

Adds specified text to the end of the current line in the SQL buffer. The buffer has no command history list and does not record SQL\*Plus commands.

To separate text from the preceding characters with a space, enter two spaces between APPEND and text.

To APPEND text that ends with a semicolon, end the command with two semicolons (SQL\*Plus interprets a single semicolon as an optional command terminator).

Examples

To append a comma delimiter, a space and the column name CITY to the first line of the buffer, make that line the current line by listing the line as follows:

```
1
```

```
1* SELECT DEPARTMENT_ID
```

Now enter APPEND:

```
APPEND , CITY
1
```

```
1* SELECT DEPARTMENT_ID, CITY
```

To append a semicolon to the line, enter

```
APPEND ;;
```

SQL\*Plus appends the first semicolon to the line and interprets the second as the terminator for the APPEND command.