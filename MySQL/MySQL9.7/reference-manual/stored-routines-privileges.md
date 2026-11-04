---
title: "27.2.2 Stored Routines and MySQL Privileges"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/stored-routines-privileges.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 27.2.2 Stored Routines and MySQL Privileges

The MySQL grant system takes stored routines into account as follows:

- The [`CREATE ROUTINE`](privileges-provided.md) privilege is needed to create stored routines.
- The [`ALTER ROUTINE`](privileges-provided.md) privilege is needed to alter or drop stored routines. This privilege is granted automatically to the creator of a routine if necessary, and dropped from the creator when the routine is dropped.
- The [`EXECUTE`](privileges-provided.md) privilege is required to execute stored routines. However, this privilege is granted automatically to the creator of a routine if necessary (and dropped from the creator when the routine is dropped). Also, the default `SQL SECURITY` characteristic for a routine is `DEFINER`, which enables users who have access to the database with which the routine is associated to execute the routine.
- If the [`automatic_sp_privileges`](server-system-variables.md) system variable is 0, the [`EXECUTE`](privileges-provided.md) and [`ALTER ROUTINE`](privileges-provided.md) privileges are not automatically granted to and dropped from the routine creator.
- The creator of a routine is the account used to execute the `CREATE` statement for it. This might not be the same as the account named as the `DEFINER` in the routine definition.
- The account named as a routine `DEFINER` can see all routine properties, including its definition. The account thus has full access to the routine output as produced by:
	- The contents of the Information Schema [`ROUTINES`](information-schema-routines-table.md) table.
	- The [`SHOW CREATE FUNCTION`](show-create-function.md) and [`SHOW CREATE PROCEDURE`](show-create-procedure.md) statements.
	- The [`SHOW FUNCTION CODE`](show-function-code.md) and [`SHOW PROCEDURE CODE`](show-procedure-code.md) statements.
	- The [`SHOW FUNCTION STATUS`](show-function-status.md) and [`SHOW PROCEDURE STATUS`](show-procedure-status.md) statements.
- For an account other than the account named as the routine `DEFINER`, access to routine properties depends on the privileges granted to the account:
	- With the [`SHOW_ROUTINE`](privileges-provided.md) privilege or the global [`SELECT`](privileges-provided.md) privilege, the account can see all routine properties, including its definition.
	- With the [`CREATE ROUTINE`](privileges-provided.md), [`ALTER ROUTINE`](privileges-provided.md) or [`EXECUTE`](privileges-provided.md) privilege granted at a scope that includes the routine, the account can see all routine properties except its definition.