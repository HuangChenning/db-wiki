---
title: "MySQL :: MySQL 26.7 Reference Manual :: 15.1.36 DROP PROCEDURE and DROP FUNCTION Statements"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/drop-procedure.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 15.1.36 DROP PROCEDURE and DROP FUNCTION Statements

```sql
DROP {PROCEDURE | FUNCTION} [IF EXISTS] sp_name
```

These statements are used to drop a stored routine (a stored procedure or function). That is, the specified routine is removed from the server. (`DROP FUNCTION` is also used to drop loadable functions; see [Section 15.7.4.2, “DROP FUNCTION Statement for Loadable Functions”](drop-function-loadable.md).)

To drop a stored routine, you must have the [`ALTER ROUTINE`](privileges-provided.md) privilege for it. (If the [`automatic_sp_privileges`](server-system-variables.md) system variable is enabled, that privilege and [`EXECUTE`](privileges-provided.md) are granted automatically to the routine creator when the routine is created and dropped from the creator when the routine is dropped. See [Section 27.2.2, “Stored Routines and MySQL Privileges”](stored-routines-privileges.md).)

In addition, if the definer of the routine has the [`SYSTEM_USER`](privileges-provided.md) privilege, the user dropping it must also have this privilege.

The `IF EXISTS` clause is a MySQL extension. It prevents an error from occurring if the procedure or function does not exist. A warning is produced that can be viewed with [`SHOW WARNINGS`](show-warnings.md).

[`DROP FUNCTION`](drop-function.md) is also used to drop loadable functions (see [Section 15.7.4.2, “DROP FUNCTION Statement for Loadable Functions”](drop-function-loadable.md)).