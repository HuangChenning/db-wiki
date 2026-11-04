---
title: "1.6.2 MySQL Differences from Standard SQL"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/differences-from-ansi.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 1.6.2 MySQL Differences from Standard SQL

We try to make MySQL Server follow the ANSI SQL standard and the ODBC SQL standard, but MySQL Server performs operations differently in some cases:

- There are several differences between the MySQL and standard SQL privilege systems. For example, in MySQL, privileges for a table are not automatically revoked when you delete a table. You must explicitly issue a [`REVOKE`](revoke.md) statement to revoke privileges for a table. For more information, see [Section 13.7.1.6, “REVOKE Statement”](revoke.md).
- The [`CAST()`](cast-functions.md) function does not support cast to [`REAL`](floating-point-types.md) or [`BIGINT`](integer-types.md). See [Section 12.10, “Cast Functions and Operators”](cast-functions.md).