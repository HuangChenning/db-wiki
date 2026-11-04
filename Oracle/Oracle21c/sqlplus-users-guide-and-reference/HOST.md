---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/HOST.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

Syntax

```
HO[ST] [command]
```

where command represents an operating system command.

Executes an operating system command without leaving SQL\*Plus.

Enter HOST without command to display an operating system prompt. You can then enter multiple operating system commands. For information on returning to SQL\*Plus, refer to the platform-specific Oracle documentation provided for your operating system.

Note:

Operating system commands entered from a SQL\*Plus session using the HOST command do not affect the current SQL\*Plus session. For example, setting an operating system environment variable only affects SQL\*Plus sessions started subsequently.

You can disable HOST. For more information about disabling HOST, see [SQL\*Plus Security](SQL-Plus-security.md).

Usage

In some operating systems, you can use a character in place of HOST such as "$" in Windows or "!" in UNIX, or you may not have access to the HOST command. See the platform-specific Oracle documentation provided for your operating system or ask your DBA for more information.

On some platforms, an \_RC substitution variable may be created with a HOST return value that is operation system dependent. It is recommended that you do not use the \_RC substitution variable in scripts as it is not portable.

SQL\*Plus removes the SQLTERMINATOR (a semicolon by default) before the HOST command is issued. A workaround for this is to add another SQLTERMINATOR. See [SET SQLT\[ERMINATOR\] {; | c | ON | OFF}](https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/SET-system-variable-summary.html#GUID-5D91A9A9-13A2-4F62-B02A-AD2F3AFF8BB7) for more information.

Examples

To execute a UNIX operating system command, ls \*.sql, enter

```
HOST ls *.sql
```

To execute a Windows operating system command, dir \*.sql, enter

```
HOST dir *.sql
```