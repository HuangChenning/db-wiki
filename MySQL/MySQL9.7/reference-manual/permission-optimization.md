---
title: "10.2.6 Optimizing Database Privileges"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/permission-optimization.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 10.2.6 Optimizing Database Privileges

The more complex your privilege setup, the more overhead applies to all SQL statements. Simplifying the privileges established by [`GRANT`](grant.md) statements enables MySQL to reduce permission-checking overhead when clients execute statements. For example, if you do not grant any table-level or column-level privileges, the server need not ever check the contents of the `tables_priv` and `columns_priv` tables. Similarly, if you place no resource limits on any accounts, the server does not have to perform resource counting. If you have a very high statement-processing load, consider using a simplified grant structure to reduce permission-checking overhead.