---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/EXECUTE.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

Syntax

```
EXEC[UTE] statement
```

where statement represents a PL/SQL statement.

Executes a single PL/SQL statement. The EXECUTE command is often useful when you want to execute a PL/SQL statement that references a stored procedure. For more information on PL/SQL, see your [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=LNPLS).

Usage

If your EXECUTE command cannot fit on one line because of the PL/SQL statement, use the SQL\*Plus continuation character (a hyphen).

The length of the command and the PL/SQL statement cannot exceed the length defined by SET LINESIZE.

You can suppress printing of the message "PL/SQL procedure successfully completed" with SET FEEDBACK OFF.

Examples

If the variable:n has been defined with:

```
VARIABLE n NUMBER
```

The following EXECUTE command assigns a value to the bind variable n:

```
EXECUTE :n := 1
```
```
PL/SQL procedure successfully completed.
```

For information on how to create a bind variable, see the [VARIABLE](VARIABLE.md) command.