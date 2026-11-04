---
title: "15.1.9 ALTER PROCEDURE Statement"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/alter-procedure.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 15.1.9 ALTER PROCEDURE Statement

```
ALTER PROCEDURE proc_name [characteristic ...]

characteristic: {
    COMMENT 'string'
  | LANGUAGE {SQL | JAVASCRIPT}
  | { CONTAINS SQL | NO SQL | READS SQL DATA | MODIFIES SQL DATA }
  | SQL SECURITY { DEFINER | INVOKER }
  | USING([library_reference][, library_reference][, ...])
}
```

This statement can be used to change the characteristics of a stored procedure. More than one change may be specified in an `ALTER PROCEDURE` statement. However, you cannot change the parameters or body of a stored procedure using this statement; to make such changes, you must drop and re-create the procedure using [`DROP       PROCEDURE`](drop-procedure.md) and [`CREATE       PROCEDURE`](create-procedure.md).

You must have the [`ALTER ROUTINE`](privileges-provided.md) privilege for the procedure. By default, that privilege is granted automatically to the procedure creator. This behavior can be changed by disabling the [`automatic_sp_privileges`](server-system-variables.md) system variable. See [Section 27.2.2, “Stored Routines and MySQL Privileges”](stored-routines-privileges.md).

The `USING` clause is specific to stored programs written in JavaScript (see [Section 27.3, “JavaScript Stored Programs”](stored-routines-js.md)), and allows you to specify a list of zero or more libraries to be imported by the stored procedure, causing any previous such list to be removed (just as it does with [`ALTER       FUNCTION`](alter-function.md)). Possible results are listed here:

- *A `USING` clause is employed, and lists one or more libraries*: Following execution of the `ALTER PROCEDURE` statement, the procedure imports only those libraries listed in the `ALTER FUNCTION` statement; any libraries listed previously are removed from the list and no longer imported.
- *The statement includes an empty `USING` clause*: All libraries previously imported are removed from the list; the function no longer imports any libraries.
- *`USING` is not used*: No changes are made to the list of libraries specified when the procedure was created.

Examples:

- `ALTER PROCEDURE myproc USING(lib1, lib2);`
	(`USING` with a non-empty list:) Following execution, `myproc` imports *only* the libraries `lib1` and `lib2`, and no other libraries.
- `ALTER PROCEDURE myproc USING();`
	(`USING` with an empty list:) Following execution, `myproc` no longer imports any libraries at all.
- `ALTER PROCEDURE myproc COMMENT "This procedure was           altered";`
	(No `USING` clause:) The procedure continues to import the same libraries as it did before this was issued.