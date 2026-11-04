---
title: "MySQL :: MySQL 26.7 Reference Manual :: 15.1.10 ALTER SERVER Statement"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/alter-server.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 15.1.10 ALTER SERVER Statement

```sql
ALTER SERVER  server_name
    OPTIONS (option[, option] ...)
```

Alters the server information for ``*`server_name`*``, adjusting any of the options permitted in the [`CREATE SERVER`](create-server.md) statement. The corresponding fields in the `mysql.servers` table are updated accordingly. This statement requires the [`SUPER`](privileges-provided.md) privilege.

For example, to update the `USER` option:

```sql
ALTER SERVER s OPTIONS (USER 'sally');
```

`ALTER SERVER` causes an implicit commit. See [Section 15.3.3, “Statements That Cause an Implicit Commit”](implicit-commit.md).

`ALTER SERVER` is not written to the binary log, regardless of the logging format that is in use.