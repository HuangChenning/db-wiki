---
title: "15.1.4 ALTER FUNCTION Statement"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/alter-function.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 15.1.4 ALTER FUNCTION Statement

```
ALTER FUNCTION func_name [characteristic ...]

characteristic: {
    COMMENT 'string'
  | LANGUAGE {SQL | JAVASCRIPT}
  | { CONTAINS SQL | NO SQL | READS SQL DATA | MODIFIES SQL DATA }
  | SQL SECURITY { DEFINER | INVOKER }
  | USING([library_reference][, library_reference][, ...])
}
```

This statement can be used to change the characteristics of a stored function. More than one change may be specified in an `ALTER FUNCTION` statement. However, you cannot change the parameters or body of a stored function using this statement; to make such changes, you must drop and re-create the function using [`DROP       FUNCTION`](drop-function.md) and [`CREATE       FUNCTION`](create-function.md).

You must have the [`ALTER ROUTINE`](privileges-provided.md) privilege for the function. (That privilege is granted automatically to the function creator.) If binary logging is enabled, the `ALTER FUNCTION` statement might also require the [`SUPER`](privileges-provided.md) privilege, as described in [Section 27.9, “Stored Program Binary Logging”](stored-programs-logging.md).

The `USING` clause is specific to stored programs written in JavaScript (see [Section 27.3, “JavaScript Stored Programs”](stored-routines-js.md)), and allows you to specify a list of zero or more libraries to be imported by the stored function, causing any previous such list to be removed, just as it does with [`ALTER       PROCEDURE`](alter-procedure.md). See [Section 15.1.9, “ALTER PROCEDURE Statement”](alter-procedure.md), for more detailed information.