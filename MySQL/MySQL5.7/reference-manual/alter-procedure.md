---
title: "13.1.6 ALTER PROCEDURE Statement"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/alter-procedure.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 13.1.6 ALTER PROCEDURE Statement

```
ALTER PROCEDURE proc_name [characteristic ...]

characteristic: {
    COMMENT 'string'
  | LANGUAGE SQL
  | { CONTAINS SQL | NO SQL | READS SQL DATA | MODIFIES SQL DATA }
  | SQL SECURITY { DEFINER | INVOKER }
}
```

This statement can be used to change the characteristics of a stored procedure. More than one change may be specified in an `ALTER PROCEDURE` statement. However, you cannot change the parameters or body of a stored procedure using this statement; to make such changes, you must drop and re-create the procedure using [`DROP       PROCEDURE`](drop-procedure.md) and [`CREATE       PROCEDURE`](create-procedure.md).

You must have the [`ALTER ROUTINE`](privileges-provided.md) privilege for the procedure. By default, that privilege is granted automatically to the procedure creator. This behavior can be changed by disabling the [`automatic_sp_privileges`](server-system-variables.md) system variable. See [Section 23.2.2, “Stored Routines and MySQL Privileges”](stored-routines-privileges.md).