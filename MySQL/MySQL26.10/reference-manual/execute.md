---
title: "MySQL :: MySQL 26.10 Reference Manual :: 15.5.2 EXECUTE Statement"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/execute.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 15.5.2 EXECUTE Statement

```sql
EXECUTE stmt_name
    [USING @var_name [, @var_name] ...]
```

After preparing a statement with [`PREPARE`](prepare.md), you execute it with an `EXECUTE` statement that refers to the prepared statement name. If the prepared statement contains any parameter markers, you must supply a `USING` clause that lists user variables containing the values to be bound to the parameters. Parameter values can be supplied only by user variables, and the `USING` clause must name exactly as many variables as the number of parameter markers in the statement.

You can execute a given prepared statement multiple times, passing different variables to it or setting the variables to different values before each execution.

For examples, see [Section 15.5, “Prepared Statements”](sql-prepared-statements.md).