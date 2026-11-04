---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/PRINT.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

Syntax

```
PRINT [variable ...]
```

where variable... represents names of bind variables whose values you want to display.

Displays the current values of bind variables.

Enter PRINT with no variables to print all bind variables.

Usage

Bind variables are created using the VARIABLE command. See [VARIABLE](VARIABLE.md) for more information and examples.

You can control the formatting of the PRINT output just as you would query output. For more information, see the formatting techniques described in [Formatting SQL\*Plus Reports](formatting-SQL-Plus-reports.md).

To automatically display bind variables referenced in a successful PL/SQL block or used in an EXECUTE command, use the AUTOPRINT clause of the SET command. See [SET](SET.md) for more information.

Examples

The following example illustrates a PRINT command:

```
VARIABLE n NUMBER
BEGIN
:n := 1;
END;
/
```
```
PL/SQL procedure successfully completed.
```
```
PRINT n
```
```
N
----------
1
```