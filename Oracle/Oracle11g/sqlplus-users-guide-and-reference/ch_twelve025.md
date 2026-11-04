---
title: HELP
book: "SQL*Plus User's Guide and Reference"
doc_id: E16604-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e16604/ch_twelve025.htm
tags:
  - oracle
  - 11g
  - sqlplus-users-guide-and-reference
---

---

Syntax

HELP |? \[topic\]

where topic represents a SQL\*Plus help topic, for example, COLUMN.

Accesses the SQL\*Plus command-line help system. Enter HELP INDEX or? INDEX for a list of topics. You can view SQL\*Plus resources at `http://www.oracle.com/technology/tech/sql_plus/` and the Oracle Database Library at `http://www.oracle.com/technology/documentation/`.

Enter HELP or? without topic to get help on the help system.

Usage

You can only enter one topic after HELP. You can abbreviate the topic (for example, COL for COLUMN). However, if you enter only an abbreviated topic and the abbreviation is ambiguous, SQL\*Plus displays help for all topics that match the abbreviation. For example, if you enter

```
HELP EX
```

SQL\*Plus displays the syntax for the EXECUTE command followed by the syntax for the EXIT command.

If you get a response indicating that help is not available, consult your database administrator.

Examples

To see a list of SQL\*Plus commands for which help is available, enter

```
HELP INDEX
```

or

```
? INDEX
```

To see a single column list of SQL\*Plus commands for which help is available, enter

```
HELP TOPICS
```