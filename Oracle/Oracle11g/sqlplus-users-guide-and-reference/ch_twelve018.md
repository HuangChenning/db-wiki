---
title: DEL
book: "SQL*Plus User's Guide and Reference"
doc_id: E16604-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e16604/ch_twelve018.htm
tags:
  - oracle
  - 11g
  - sqlplus-users-guide-and-reference
---

---

Syntax

DEL \[n | n m | n \* | n LAST | \* | \* n | \* LAST | LAST\]

Deletes one or more lines of the buffer.

SQL\*Plus commands are not stored in the buffer. There is no history of commands previously entered in the buffer.

Terms

| Term | Description |
| --- | --- |
| n | Deletes line n. |
| n m | Deletes lines n through m. |
| n \* | Deletes line n through the current line. |
| n LAST | Deletes line n through the last line. |
| \* | Deletes the current line. |
| \* n | Deletes the current line through line n. |
| \* LAST | Deletes the current line through the last line. |
| LAST | Deletes the last line. |

Enter DEL with no clauses to delete the current line of the buffer.

Usage

DEL makes the following line of the buffer (if any) the current line. You can enter DEL several times to delete several consecutive lines.

Note:

DEL is a SQL\*Plus command and DELETE is a SQL command. For more information about the SQL DELETE command, see the [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm).

Examples

Assume the SQL buffer contains the following query:

```
SELECT LAST_NAME, DEPARTMENT_ID
FROM EMP_DETAILS_VIEW
WHERE JOB_ID = 'SA_MAN'
ORDER BY DEPARTMENT_ID;
```

To make the line containing the WHERE clause the current line, you could enter

```
LIST 3
```

```
3* WHERE JOB_ID = 'SA_MAN'
```

followed by

```
DEL
```

The SQL buffer now contains the following lines:

```
SELECT LAST_NAME, DEPARTMENT_ID
FROM EMP_DETAILS_VIEW
ORDER BY DEPARTMENT_ID
```

To delete the third line of the buffer, enter

```
DEL 3
```

The SQL buffer now contains the following lines:

```
SELECT LAST_NAME, DEPARTMENT_ID
FROM EMP_DETAILS_VIEW
```