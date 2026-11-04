---
title: "17.11.5 Reclaiming Disk Space with TRUNCATE TABLE"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/innodb-truncate-table-reclaim-space.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 17.11.5 Reclaiming Disk Space with TRUNCATE TABLE

To reclaim operating system disk space when [truncating](glossary.md) an `InnoDB` table, the table must be stored in its own [.ibd](https://docs.oracle.com/cd/E17952_01/mysql-8.4-en/glossary.html#glos_ibd_file) file. For a table to be stored in its own [.ibd](https://docs.oracle.com/cd/E17952_01/mysql-8.4-en/glossary.html#glos_ibd_file) file, [`innodb_file_per_table`](innodb-parameters.md) must enabled when the table is created. Additionally, there cannot be a [foreign key](glossary.md) constraint between the table being truncated and other tables, otherwise the `TRUNCATE TABLE` operation fails. A foreign key constraint between two columns in the same table, however, is permitted.

When a table is truncated, it is dropped and re-created in a new `.ibd` file, and the freed space is returned to the operating system. This is in contrast to truncating `InnoDB` tables that are stored within the `InnoDB` [system tablespace](https://docs.oracle.com/cd/E17952_01/mysql-8.4-en/glossary.html#glos_system_tablespace) (tables created when `innodb_file_per_table=OFF`) and tables stored in shared [general tablespaces](glossary.md), where only `InnoDB` can use the freed space after the table is truncated.

The ability to truncate tables and return disk space to the operating system also means that [physical backups](glossary.md) can be smaller. Truncating tables that are stored in the system tablespace (tables created when `innodb_file_per_table=OFF`) or in a general tablespace leaves blocks of unused space in the tablespace.