---
title: "17.7.2 InnoDB Transaction Model"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/innodb-transaction-model.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 17.7.2 InnoDB Transaction Model

The `InnoDB` transaction model aims to combine the best properties of a [multi-versioning](glossary.md) database with traditional two-phase locking. `InnoDB` performs locking at the row level and runs queries as nonlocking [consistent reads](glossary.md) by default, in the style of Oracle. The lock information in `InnoDB` is stored space-efficiently so that lock escalation is not needed. Typically, several users are permitted to lock every row in `InnoDB` tables, or any random subset of the rows, without causing `InnoDB` memory exhaustion.