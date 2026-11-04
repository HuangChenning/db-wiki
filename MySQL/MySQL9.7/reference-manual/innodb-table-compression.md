---
title: "17.9.1 InnoDB Table Compression"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/innodb-table-compression.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

Skip to Main Content

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 17.9.1 InnoDB Table Compression

This section describes `InnoDB` table compression, which is supported with `InnoDB` tables that reside in [file\_per\_table](glossary.md) tablespaces or [general tablespaces](glossary.md). Table compression is enabled using the `ROW_FORMAT=COMPRESSED` attribute with [`CREATE TABLE`](create-table.md) or [`ALTER TABLE`](alter-table.md).

[MySQL Documentation Library](https://docs.oracle.com/cd/E17952_01/index.html "Go to MySQL Doc Library")