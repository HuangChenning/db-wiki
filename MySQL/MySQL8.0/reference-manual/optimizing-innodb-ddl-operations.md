---
title: "10.5.7 Optimizing InnoDB DDL Operations"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/optimizing-innodb-ddl-operations.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 10.5.7 Optimizing InnoDB DDL Operations

- Many DDL operations on tables and indexes (`CREATE`, `ALTER`, and `DROP` statements) can be performed online. See [Section 17.12, “InnoDB and Online DDL”](innodb-online-ddl.md) for details.
- Online DDL support for adding secondary indexes means that you can generally speed up the process of creating and loading a table and associated indexes by creating the table without secondary indexes, then adding secondary indexes after the data is loaded.
- Use [`TRUNCATE TABLE`](truncate-table.md) to empty a table, not ``DELETE FROM             *`tbl_name`*``. Foreign key constraints can make a `TRUNCATE` statement work like a regular `DELETE` statement, in which case a sequence of commands like [`DROP TABLE`](drop-table.md) and [`CREATE TABLE`](create-table.md) might be fastest.
- Because the primary key is integral to the storage layout of each `InnoDB` table, and changing the definition of the primary key involves reorganizing the whole table, always set up the primary key as part of the [`CREATE TABLE`](create-table.md) statement, and plan ahead so that you do not need to `ALTER` or `DROP` the primary key afterward.