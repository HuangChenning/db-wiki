---
title: "28.3.5 The INFORMATION_SCHEMA CHECK_CONSTRAINTS Table"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/information-schema-check-constraints-table.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 28.3.5 The INFORMATION\_SCHEMA CHECK\_CONSTRAINTS Table

As of MySQL 8.0.16, [`CREATE TABLE`](create-table.md) permits the core features of table and column `CHECK` constraints, and the `CHECK_CONSTRAINTS` table provides information about these constraints.

The `CHECK_CONSTRAINTS` table has these columns:

- `CONSTRAINT_CATALOG`
	The name of the catalog to which the constraint belongs. This value is always `def`.
- `CONSTRAINT_SCHEMA`
	The name of the schema (database) to which the constraint belongs.
- `CONSTRAINT_NAME`
	The name of the constraint.
- `CHECK_CLAUSE`
	The expression that specifies the constraint condition.