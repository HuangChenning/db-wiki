---
title: "17.9.1 InnoDB Table Compression"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/innodb-table-compression.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

Skip to Main Content

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 17.9.1 InnoDB Table Compression

This section describes `InnoDB` table compression, which is supported with `InnoDB` tables that reside in [file\_per\_table](glossary.md) tablespaces or [general tablespaces](glossary.md). Table compression is enabled using the `ROW_FORMAT=COMPRESSED` attribute with [`CREATE TABLE`](create-table.md) or [`ALTER TABLE`](alter-table.md).

[MySQL Documentation Library](https://docs.oracle.com/cd/E17952_01/index.html "Go to MySQL Doc Library")