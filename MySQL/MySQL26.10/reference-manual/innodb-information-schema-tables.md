---
title: "MySQL :: MySQL 26.10 Reference Manual :: 28.4 INFORMATION_SCHEMA InnoDB Tables"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/innodb-information-schema-tables.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

## 28.4 INFORMATION\_SCHEMA InnoDB Tables

This section provides table definitions for `INFORMATION_SCHEMA` `InnoDB` tables. For related information and examples, see [Section 17.15, “InnoDB INFORMATION\_SCHEMA Tables”](innodb-information-schema.md).

`INFORMATION_SCHEMA` `InnoDB` tables can be used to monitor ongoing `InnoDB` activity, to detect inefficiencies before they turn into issues, or to troubleshoot performance and capacity issues. As your database becomes bigger and busier, running up against the limits of your hardware capacity, you monitor and tune these aspects to keep the database running smoothly.