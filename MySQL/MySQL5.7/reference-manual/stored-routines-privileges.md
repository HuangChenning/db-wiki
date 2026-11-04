---
title: "23.2.2 Stored Routines and MySQL Privileges"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/stored-routines-privileges.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 23.2.2 Stored Routines and MySQL Privileges

The MySQL grant system takes stored routines into account as follows:

- The [`CREATE ROUTINE`](privileges-provided.md) privilege is needed to create stored routines.
- The [`ALTER ROUTINE`](privileges-provided.md) privilege is needed to alter or drop stored routines. This privilege is granted automatically to the creator of a routine if necessary, and dropped from the creator when the routine is dropped.
- The [`EXECUTE`](privileges-provided.md) privilege is required to execute stored routines. However, this privilege is granted automatically to the creator of a routine if necessary (and dropped from the creator when the routine is dropped). Also, the default `SQL SECURITY` characteristic for a routine is `DEFINER`, which enables users who have access to the database with which the routine is associated to execute the routine.
- If the [`automatic_sp_privileges`](server-system-variables.md) system variable is 0, the [`EXECUTE`](privileges-provided.md) and [`ALTER ROUTINE`](privileges-provided.md) privileges are not automatically granted to and dropped from the routine creator.
- The creator of a routine is the account used to execute the `CREATE` statement for it. This might not be the same as the account named as the `DEFINER` in the routine definition.

The server manipulates the `mysql.proc` table in response to statements that create, alter, or drop stored routines. Manual manipulation of this table is not supported.