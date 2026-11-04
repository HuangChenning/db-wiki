---
title: "13.6.4 Variables in Stored Programs"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/stored-program-variables.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 13.6.4 Variables in Stored Programs

System variables and user-defined variables can be used in stored programs, just as they can be used outside stored-program context. In addition, stored programs can use `DECLARE` to define local variables, and stored routines (procedures and functions) can be declared to take parameters that communicate values between the routine and its caller.

- To declare local variables, use the [`DECLARE`](declare-local-variable.md) statement, as described in [Section 13.6.4.1, “Local Variable DECLARE Statement”](declare-local-variable.md).
- Variables can be set directly with the [`SET`](set-variable.md) statement. See [Section 13.7.4.1, “SET Syntax for Variable Assignment”](set-variable.md).
- Results from queries can be retrieved into local variables using [``SELECT ...           INTO *`var_list`*``](select-into.md) or by opening a cursor and using [``FETCH ... INTO           *`var_list`*``](fetch.md). See [Section 13.2.9.1, “SELECT... INTO Statement”](select-into.md), and [Section 13.6.6, “Cursors”](cursors.md).

For information about the scope of local variables and how MySQL resolves ambiguous names, see [Section 13.6.4.2, “Local Variable Scope and Resolution”](local-variable-scope.md).

It is not permitted to assign the value `DEFAULT` to stored procedure or function parameters or stored program local variables (for example with a ``SET       *`var_name`* = DEFAULT`` statement). In MySQL 5.7, this results in a syntax error.