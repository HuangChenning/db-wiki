---
title: "8.5.10 Optimizing InnoDB for Systems with Many Tables"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/optimizing-innodb-many-tables.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 8.5.10 Optimizing InnoDB for Systems with Many Tables

- If you have configured [non-persistent optimizer statistics](innodb-statistics-estimation.md) (a non-default configuration), `InnoDB` computes index [cardinality](glossary.md) values for a table the first time that table is accessed after startup, instead of storing such values in the table. This step can take significant time on systems that partition the data into many tables. Since this overhead only applies to the initial table open operation, to “warm up” a table for later use, access it immediately after startup by issuing a statement such as ``SELECT 1 FROM             *`tbl_name`* LIMIT 1``.
	Optimizer statistics are persisted to disk by default, enabled by the [`innodb_stats_persistent`](innodb-parameters.md) configuration option. For information about persistent optimizer statistics, see [Section 14.8.11.1, “Configuring Persistent Optimizer Statistics Parameters”](innodb-persistent-stats.md).