---
title: "14.1.3 Verifying that InnoDB is the Default Storage Engine"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/innodb-check-availability.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 14.1.3 Verifying that InnoDB is the Default Storage Engine

Issue the [`SHOW ENGINES`](show-engines.md) statement to view the available MySQL storage engines. Look for `DEFAULT` in the `SUPPORT` column.

```
mysql> SHOW ENGINES;
```

Alternatively, query the Information Schema [`ENGINES`](information-schema-engines-table.md) table.

```
mysql> SELECT * FROM INFORMATION_SCHEMA.ENGINES;
```