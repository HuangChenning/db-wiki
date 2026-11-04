---
title: "MySQL :: MySQL 26.10 Reference Manual :: 15.6.4 Variables in Stored Programs"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/stored-program-variables.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 15.6.4 Variables in Stored Programs

System variables and user-defined variables can be used in stored programs, just as they can be used outside stored-program context. In addition, stored programs can use `DECLARE` to define local variables, and stored routines (procedures and functions) can be declared to take parameters that communicate values between the routine and its caller.

- To declare local variables, use the [`DECLARE`](declare-local-variable.md) statement, as described in [Section 15.6.4.1, “Local Variable DECLARE Statement”](declare-local-variable.md).
- Variables can be set directly with the [`SET`](set-variable.md) statement. See [Section 15.7.6.1, “SET Syntax for Variable Assignment”](set-variable.md).
- Results from queries can be retrieved into local variables using [``SELECT ...           INTO *`var_list`*``](select-into.md) or by opening a cursor and using [``FETCH ... INTO           *`var_list`*``](fetch.md). See [Section 15.2.13.1, “SELECT... INTO Statement”](select-into.md), and [Section 15.6.6, “Cursors”](cursors.md).

For information about the scope of local variables and how MySQL resolves ambiguous names, see [Section 15.6.4.2, “Local Variable Scope and Resolution”](local-variable-scope.md).

It is not permitted to assign the value `DEFAULT` to stored procedure or function parameters or stored program local variables (for example with a ``SET       *`var_name`* = DEFAULT`` statement). In MySQL 26.10, this results in a syntax error.