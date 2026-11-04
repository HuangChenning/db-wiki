---
title: "17.11.5 Reclaiming Disk Space with TRUNCATE TABLE"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/innodb-truncate-table-reclaim-space.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 17.11.5 Reclaiming Disk Space with TRUNCATE TABLE

To reclaim operating system disk space when [truncating](glossary.md) an `InnoDB` table, the table must be stored in its own [.ibd](glossary.md) file. For a table to be stored in its own [.ibd](glossary.md) file, [`innodb_file_per_table`](innodb-parameters.md) must enabled when the table is created. Additionally, there cannot be a [foreign key](glossary.md) constraint between the table being truncated and other tables, otherwise the `TRUNCATE TABLE` operation fails. A foreign key constraint between two columns in the same table, however, is permitted.

When a table is truncated, it is dropped and re-created in a new `.ibd` file, and the freed space is returned to the operating system. This is in contrast to truncating `InnoDB` tables that are stored within the `InnoDB` [system tablespace](glossary.md) (tables created when `innodb_file_per_table=OFF`) and tables stored in shared [general tablespaces](glossary.md), where only `InnoDB` can use the freed space after the table is truncated.

The ability to truncate tables and return disk space to the operating system also means that [physical backups](glossary.md) can be smaller. Truncating tables that are stored in the system tablespace (tables created when `innodb_file_per_table=OFF`) or in a general tablespace leaves blocks of unused space in the tablespace.