---
title: "17.1.3 Verifying that InnoDB is the Default Storage Engine"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/innodb-check-availability.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 17.1.3 Verifying that InnoDB is the Default Storage Engine

Issue the [`SHOW ENGINES`](show-engines.md) statement to view the available MySQL storage engines. Look for `DEFAULT` in the `SUPPORT` column.

```
mysql> SHOW ENGINES;
```

Alternatively, query the Information Schema [`ENGINES`](information-schema-engines-table.md) table.

```
mysql> SELECT * FROM INFORMATION_SCHEMA.ENGINES;
```