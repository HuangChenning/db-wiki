---
title: "28.4 INFORMATION_SCHEMA InnoDB Tables"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/innodb-information-schema-tables.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

This section provides table definitions for `INFORMATION_SCHEMA` `InnoDB` tables. For related information and examples, see [Section 17.15, “InnoDB INFORMATION\_SCHEMA Tables”](innodb-information-schema.md).

`INFORMATION_SCHEMA` `InnoDB` tables can be used to monitor ongoing `InnoDB` activity, to detect inefficiencies before they turn into issues, or to troubleshoot performance and capacity issues. As your database becomes bigger and busier, running up against the limits of your hardware capacity, you monitor and tune these aspects to keep the database running smoothly.