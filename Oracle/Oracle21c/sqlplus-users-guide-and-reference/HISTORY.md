---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/HISTORY.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

Syntax

```
HIST[ORY] [[[N] {R[UN] | E[DIT] | D[ELETE]}] | CLEAR | LIST ]
```

Enables users to run, edit, or delete previously used SQL\*Plus, SQL, or PL/SQL commands from the history list in the current session. You can enable or disable the recording of history in the current SQL\*Plus session by using the SET HISTORY command.

The HISTORY command enables you to:

- List all entries in the command history list.
- Run an entry in the command history list.
- Edit an entry in the command history list.
- Delete an entry from the command history list.
- Clear all entries in the command history list.

Terms

```
HIST[ORY]
```

Lists all entries in the command history list.

```
N
```

Represents an entry in the command history list. An asterisk (\*) indicates the last used command in the command history list. If N is omitted, the RUN, EDIT OR DELETE operation is executed in the last used command.

```
R[UN]
```

Enables you to execute entry N or the last used command from the command history list.

```
E[DIT]
```

Enables you to edit entry N or the last used command in the command history list, using the default text editor. After you edit entry N in the command history list and save the changes, a new entry is created at the end of the list. When the number of entries in the command history list reaches the maximum limit, the oldest entry in the list will be cleared to accommodate the new entry.

```
D[ELETE]
```

Enables you to delete entry N or the last used command from the command history list. After you delete an entry from the history list, the list is reordered to reflect the most recent changes.

```
CLEAR
```

Enables you to clear all entries in the history list. Once cleared, the history list cannot be recovered.

```
LIST
```

Lists all entries in the history list. This is the same as using the HIST\[ORY\] command by itself.

Usage

You can use the SQL\*Plus DEFINE command to define the variable, \_EDITOR, to hold the name of your preferred text editor. For example, to define the editor used by EDIT to be vi, enter the following command:

```
DEFINE _EDITOR = vi
```

EDIT attempts to run the default operating system editor if \_EDITOR is undefined. See the [DEFINE](DEFINE.md) command for more information.

Example 13-1 Examples

The following example executes the fifth entry in the history list:

```
SQL>history 5 run
```

The following example allows you to edit the third entry in the history list:

```
SQL>history 3 edit
```

The following example allows you to delete the second entry from the history list:

```
SQL>history 2 delete
```

The following example allows you to delete all entries from the history list:

```
SQL>history clear
```

The following example shows you how to edit and run the last used command in the history list:

```
SQL>history edit
SQL>history run
```

The following example shows you how to enable or disable command history, and how to check the command history status:

```
SQL> set history on
SQL> show history
History is ON and set to "100"
SQL> set history off
SQL> show history
History is OFF
SQL> set history 1000
SQL> show history
History is ON and set to "1000"
```

The following example shows you how to list all entries in the history list:

```
SQL> history
  1  show history
  2  show user
  3  desc dual
* 4  select * from dual;
```

An asterisk (\*) indicates the last used command in the command history list.

The following example shows you how to list all entries in the history list, and then execute the second entry:

```
SQL> history
  1  show history
  2  show user
  3  desc dual
* 4  select * from dual;
SQL> history 2 run
USER is "SYSTEM"
SQL> history
  1  show hist
* 2  show user
  3  desc dual
  4  select * from dual;
```