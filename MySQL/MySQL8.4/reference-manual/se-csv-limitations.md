---
title: "18.4.2 CSV Limitations"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/se-csv-limitations.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

Skip to Main Content

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 18.4.2 CSV Limitations

The `CSV` storage engine does not support indexing.

The `CSV` storage engine does not support partitioning.

All tables that you create using the `CSV` storage engine must have the `NOT NULL` attribute on all columns.

[MySQL Documentation Library](https://docs.oracle.com/cd/E17952_01/index.html "Go to MySQL Doc Library")