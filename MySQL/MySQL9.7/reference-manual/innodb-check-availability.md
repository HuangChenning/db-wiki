---
title: "17.1.3 Verifying that InnoDB is the Default Storage Engine"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/innodb-check-availability.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 17.1.3 Verifying that InnoDB is the Default Storage Engine

Issue a [`SHOW ENGINES`](show-engines.md) statement to view the available MySQL storage engines. Look for `DEFAULT` in the `SUPPORT` column.

```
mysql> SHOW ENGINES;
```

Alternatively, query the Information Schema [`ENGINES`](information-schema-engines-table.md) table.

```
mysql> SELECT * FROM INFORMATION_SCHEMA.ENGINES;
```