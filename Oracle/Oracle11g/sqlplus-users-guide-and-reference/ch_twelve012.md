---
title: CLEAR
book: "SQL*Plus User's Guide and Reference"
doc_id: E16604-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e16604/ch_twelve012.htm
tags:
  - oracle
  - 11g
  - sqlplus-users-guide-and-reference
---

---

Syntax

CL\[EAR\] option...

where option represents one of the following clauses:

BRE\[AKS\]BUFF\[ER\]COL\[UMNS\]COMP\[UTES\]SCR\[EEN\]SQL TIMI\[NG\]

Resets or erases the current value or setting for the specified option.

Terms

BRE\[AKS\]

Removes the break definition set by the BREAK command.

BUFF\[ER\]

Clears text from the buffer. CLEAR BUFFER has the same effect as CLEAR SQL, unless you are using multiple buffers.

See [SET BUF\[FER\] {buffer|SQL} (obsolete)](https://docs.oracle.com/cd/E11882_01/server.112/e16604/apc.htm#i656796) for more information about the obsolete form of this command.

COL\[UMNS\]

Resets column display attributes set by the COLUMN command to default settings for all columns. To reset display attributes for a single column, use the CLEAR clause of the COLUMN command. CLEAR COLUMNS also clears the ATTRIBUTEs for that column.

COMP\[UTES\]

Removes all COMPUTE definitions set by the COMPUTE command.

SCR\[EEN\]

Clears your screen.

SQL

Clears the text from SQL buffer. CLEAR SQL has the same effect as CLEAR BUFFER, unless you are using multiple buffers.

See [SET BUF\[FER\] {buffer|SQL} (obsolete)](https://docs.oracle.com/cd/E11882_01/server.112/e16604/apc.htm#i656796) for more information about the obsolete form of this command.

TIMI\[NG\]

Deletes all timers created by the TIMING command.

Examples

To clear breaks, enter

```
CLEAR BREAKS
```

To clear column definitions, enter

```
CLEAR COLUMNS
```