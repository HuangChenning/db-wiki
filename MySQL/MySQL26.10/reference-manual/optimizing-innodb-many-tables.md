---
title: "MySQL :: MySQL 26.10 Reference Manual :: 10.5.10 Optimizing InnoDB for Systems with Many Tables"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/optimizing-innodb-many-tables.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 10.5.10 Optimizing InnoDB for Systems with Many Tables

- If you have configured [non-persistent optimizer statistics](innodb-statistics-estimation.md) (a non-default configuration), `InnoDB` computes index [cardinality](glossary.md) values for a table the first time that table is accessed after startup, instead of storing such values in the table. This step can take significant time on systems that partition the data into many tables. Since this overhead only applies to the initial table open operation, to “warm up” a table for later use, access it immediately after startup by issuing a statement such as ``SELECT 1 FROM             *`tbl_name`* LIMIT 1``.
	Optimizer statistics are persisted to disk by default, enabled by the [`innodb_stats_persistent`](innodb-parameters.md) configuration option. For information about persistent optimizer statistics, see [Section 17.8.10.1, “Configuring Persistent Optimizer Statistics Parameters”](innodb-persistent-stats.md).