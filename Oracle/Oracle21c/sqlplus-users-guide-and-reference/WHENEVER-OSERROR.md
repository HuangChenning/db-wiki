---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/WHENEVER-OSERROR.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

Syntax

```
WHENEVER OSERROR {EXIT [SUCCESS 
| FAILURE | n | variable | :BindVariable]  [COMMIT 
| ROLLBACK] | CONTINUE [COMMIT | ROLLBACK | NONE
]}
```

Performs the specified action (exits SQL\*Plus by default) if an operating system error occurs (such as a file writing error).

Terms

```
[SUCCESS | FAILURE | n | variable | :BindVariable]
```

Directs SQL\*Plus to perform the specified action as soon as an operating system error is detected. You can also specify that SQL\*Plus return a success or failure code, the operating system failure code, or a number or variable of your choice.

```
EXIT [SUCCESS | FAILURE | n | variable | :BindVariable]
```

Directs SQL\*Plus to exit as soon as an operating system error is detected. You can also specify that SQL\*Plus return a success or failure code, the operating system failure code, or a number or variable of your choice. See [EXIT](EXIT.md) for more information.

```
CONTINUE
```

Turns off the EXIT option.

```
COMMIT
```

Directs SQL\*Plus to execute a COMMIT before exiting or continuing and save pending changes to the database.

```
ROLLBACK
```

Directs SQL\*Plus to execute a ROLLBACK before exiting or continuing and abandon pending changes to the database.

```
NONE
```

Directs SQL\*Plus to take no action before continuing.

Usage

If you do not enter the WHENEVER OSERROR command, the default behavior of SQL\*Plus is to continue and take no action when an operating system error occurs.

If you do not enter the WHENEVER SQLERROR command, the default behavior of SQL\*Plus is to continue and take no action when a SQL error occurs.

Examples

If a failure occurs when reading from the output file, the commands in the following script cause SQL\*Plus to exit and COMMIT any pending changes:

```
WHENEVER OSERROR EXIT
START no_such_file
```
```
OS Message: No such file or directory
Disconnected from Oracle......
```