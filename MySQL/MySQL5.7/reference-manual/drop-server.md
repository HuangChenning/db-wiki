---
title: "13.1.28 DROP SERVER Statement"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/drop-server.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 13.1.28 DROP SERVER Statement

```
DROP SERVER [ IF EXISTS ] server_name
```

Drops the server definition for the server named ``*`server_name`*``. The corresponding row in the `mysql.servers` table is deleted. This statement requires the [`SUPER`](privileges-provided.md) privilege.

Dropping a server for a table does not affect any `FEDERATED` tables that used this connection information when they were created. See [Section 13.1.17, “CREATE SERVER Statement”](create-server.md).

`DROP SERVER` causes an implicit commit. See [Section 13.3.3, “Statements That Cause an Implicit Commit”](implicit-commit.md).

`DROP SERVER` is not written to the binary log, regardless of the logging format that is in use.