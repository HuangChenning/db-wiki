---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/WHENEVER-SQLERROR.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

Syntax

```
WHENEVER SQLERROR {EXIT [SUCCESS
 | FAILURE | WARNING | n | variable  | :BindVariable] [COMMIT 
| ROLLBACK] | CONTINUE [COMMIT | ROLLBACK | NONE
]}
```

Performs the specified action (exits SQL\*Plus by default) if a SQL command or PL/SQL block generates an error.

Terms

```
[SUCCESS | FAILURE | WARNING | n | variable | :BindVariable]
```

Directs SQL\*Plus to perform the specified action as soon as it detects a SQL command or PL/SQL block error (but after printing the error message). SQL\*Plus will not exit on a SQL\*Plus error.

```
EXIT [SUCCESS | FAILURE | WARNING | n | variable | :BindVariable]
```

Directs SQL\*Plus to exit as soon as it detects a SQL command or PL/SQL block error (but after printing the error message). SQL\*Plus will not exit on a SQL\*Plus error. The EXIT clause of WHENEVER SQLERROR follows the same syntax as the EXIT command. See [EXIT](EXIT.md) for more information.

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

The WHENEVER SQLERROR command is triggered by SQL command or PL/SQL block errors, and not by SQL\*Plus command errors.

Examples

The commands in the following script cause SQL\*Plus to exit and return the SQL error code if the SQL UPDATE command fails:

```
WHENEVER SQLERROR EXIT SQL.SQLCODE
UPDATE EMP_DETAILS_VIEW SET SALARY = SALARY*1.1;
```

The following examples show that the WHENEVER SQLERROR command is not executed after errors with SQL\*Plus commands, but it is executed if SQL commands or PL/SQL blocks cause errors:

```
WHENEVER SQLERROR EXIT SQL.SQLCODE
column LAST_name headIing "Employee Name"
```
```
Unknown COLUMN option "headiing"

SHOW non_existed_option
```

The following PL/SQL block error causes SQL\*Plus to exit and return the SQL error code:

```
WHENEVER SQLERROR EXIT SQL.SQLCODE
begin
  SELECT COLUMN_DOES_NOT_EXIST FROM DUAL;
END;
/
```
```
SELECT COLUMN_DOES_NOT_EXIST FROM DUAL;
       *
ERROR at line 2:
ORA-06550: line 2, column 10:
PLS-00201: identifier 'COLUMN_DOES_NOT_EXIST' must be declared
ORA-06550: line 2, column 3:
PL/SQL: SQL Statement ignored

Disconnected from Oracle.....
```