---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/LIST.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

Syntax

```
L[IST] [n | n m | n * | n LAST | * | * n | * LAST | LAST]
```

Lists one or more lines of the SQL buffer.

In SQL\*Plus command-line you can also use ";" to list all the lines in the SQL buffer.

Terms

| Term | Description |
| --- | --- |
| ``` n ``` | Lists line n. |
| ``` n m ``` | Lists lines n through m. |
| ``` n * ``` | Lists line n through the current line. |
| ``` n LAST ``` | Lists line n through the last line. |
| ``` * ``` | Lists the current line. |
| ``` * n ``` | Lists the current line through line n. |
| ``` * LAST ``` | Lists the current line through the last line. |
| ``` LAST ``` | Lists the last line. |

Enter LIST with no clauses, or ";" to list all lines. The last line listed becomes the new current line (marked by an asterisk).

Examples

To list the contents of the buffer, enter

```
LIST
```

or enter

```
;
```
```
1 SELECT LAST_NAME, DEPARTMENT_ID, JOB_ID
2 FROM EMP_DETAILS_VIEW
3 WHERE JOB_ID = 'SH_CLERK'
4* ORDER BY DEPARTMENT_ID
```

The asterisk indicates that line 4 is the current line.

To list the second line only, enter

```
LIST 2
```

The second line is displayed:

```
2* FROM EMP_DETAILS_VIEW
```

To list from the current line (now line 2) to the last line, enter

```
LIST * LAST
```

You will then see this:

```
2 FROM EMP_DETAILS_VIEW
3 WHERE JOB_ID = 'SH_CLERK'
4* ORDER BY DEPARTMENT_ID
```