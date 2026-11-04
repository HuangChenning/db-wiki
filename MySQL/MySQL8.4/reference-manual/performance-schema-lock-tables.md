---
title: "29.12.13 Performance Schema Lock Tables"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/performance-schema-lock-tables.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 29.12.13 Performance Schema Lock Tables

The Performance Schema exposes lock information through these tables:

- [`data_locks`](performance-schema-data-locks-table.md): Data locks held and requested
- [`data_lock_waits`](performance-schema-data-lock-waits-table.md): Relationships between data lock owners and data lock requestors blocked by those owners
- [`metadata_locks`](performance-schema-metadata-locks-table.md): Metadata locks held and requested
- [`table_handles`](performance-schema-table-handles-table.md): Table locks held and requested

The following sections describe these tables in more detail.