---
title: "17.1.3 Verifying that InnoDB is the Default Storage Engine"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/innodb-check-availability.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 17.1.3 Verifying that InnoDB is the Default Storage Engine

Issue a [`SHOW ENGINES`](show-engines.md) statement to view the available MySQL storage engines. Look for `DEFAULT` in the `SUPPORT` column.

```
mysql> SHOW ENGINES;
```

Alternatively, query the Information Schema [`ENGINES`](information-schema-engines-table.md) table.

```
mysql> SELECT * FROM INFORMATION_SCHEMA.ENGINES;
```