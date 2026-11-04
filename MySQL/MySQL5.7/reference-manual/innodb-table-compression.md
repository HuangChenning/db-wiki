---
title: "14.9.1 InnoDB Table Compression"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/innodb-table-compression.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 14.9.1 InnoDB Table Compression

This section describes `InnoDB` table compression, which is supported with `InnoDB` tables that reside in [file\_per\_table](glossary.md) tablespaces or [general tablespaces](glossary.md). Table compression is enabled using the `ROW_FORMAT=COMPRESSED` attribute with [`CREATE TABLE`](create-table.md) or [`ALTER TABLE`](alter-table.md).