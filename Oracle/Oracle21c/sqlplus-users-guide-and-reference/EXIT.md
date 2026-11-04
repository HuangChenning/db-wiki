---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/EXIT.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

Syntax

```
{EXIT | QUIT} [SUCCESS
 | FAILURE | WARNING | n | variable | :BindVariable] [COMMIT
 | ROLLBACK]
```

Commits or rolls back all pending changes, logs out of Oracle Database, terminates SQL\*Plus and returns control to the operating system.

Terms

```
{EXIT | QUIT}
```

Can be used interchangeably (QUIT is a synonym for EXIT).

```
SUCCESS
```

Exits normally.

```
FAILURE
```

Exits with a return code indicating failure.

```
WARNING
```

Exits with a return code indicating warning.

```
COMMIT
```

Saves pending changes to the database before exiting.

```
n
```

Represents an integer you specify as the return code.

```
variable
```

Represents a user-defined or system variable (but not a bind variable), such as SQL.SQLCODE. EXIT variable exits with the value of variable as the return code.

```
:BindVariable
```

Represents a variable created in SQL\*Plus with the VARIABLE command, and then referenced in PL/SQL, or other subprograms.:BindVariable exits the subprogram and returns you to SQL\*Plus.

```
ROLLBACK
```

Executes a ROLLBACK statement and abandons pending changes to the database before exiting.

EXIT with no clauses commits and exits with a value of SUCCESS.

Usage

EXIT enables you to specify an operating system return code. This enables you to run SQL\*Plus scripts in batch mode and to detect programmatically the occurrence of an unexpected event. The manner of detection is operating-system specific.

The key words SUCCESS, WARNING, and FAILURE represent operating-system dependent values. On some systems, WARNING and FAILURE may be indistinguishable.

The range of operating system return codes is also restricted on some operating systems. This limits the portability of EXIT n and EXIT variable between platforms. For example, on UNIX there is only one byte of storage for return codes; therefore, the range for return codes is limited to zero to 255.

If you make a syntax error in the EXIT options or use a non-numeric variable, SQL\*Plus performs an EXIT FAILURE COMMIT.

For information on exiting conditionally, see the [WHENEVER SQLERROR](WHENEVER-SQLERROR.md) and [WHENEVER OSERROR](WHENEVER-OSERROR.md) commands.

Examples

The following example commits all uncommitted transactions and returns the error code of the last executed SQL command or PL/SQL block:

```
EXIT SQL.SQLCODE
```