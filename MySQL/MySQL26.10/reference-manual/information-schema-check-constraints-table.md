---
title: "MySQL :: MySQL 26.10 Reference Manual :: 28.3.5 The INFORMATION_SCHEMA CHECK_CONSTRAINTS Table"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/information-schema-check-constraints-table.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 28.3.5 The INFORMATION\_SCHEMA CHECK\_CONSTRAINTS Table

[`CREATE TABLE`](create-table.md) supports the core features of table and column `CHECK` constraints; the `CHECK_CONSTRAINTS` table provides information about these constraints.

The `CHECK_CONSTRAINTS` table has these columns:

- `CONSTRAINT_CATALOG`
	The name of the catalog to which the constraint belongs. This value is always `def`.
- `CONSTRAINT_SCHEMA`
	The name of the schema (database) to which the constraint belongs.
- `CONSTRAINT_NAME`
	The name of the constraint.
- `CHECK_CLAUSE`
	The expression that specifies the constraint condition.