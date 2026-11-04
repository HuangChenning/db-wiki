---
title: "28.3.42 The INFORMATION_SCHEMA TABLE_CONSTRAINTS Table"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/information-schema-table-constraints-table.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 28.3.42 The INFORMATION\_SCHEMA TABLE\_CONSTRAINTS Table

The `TABLE_CONSTRAINTS` table describes which tables have constraints.

The `TABLE_CONSTRAINTS` table has these columns:

- `CONSTRAINT_CATALOG`
	The name of the catalog to which the constraint belongs. This value is always `def`.
- `CONSTRAINT_SCHEMA`
	The name of the schema (database) to which the constraint belongs.
- `CONSTRAINT_NAME`
	The name of the constraint.
- `TABLE_SCHEMA`
	The name of the schema (database) to which the table belongs.
- `TABLE_NAME`
	The name of the table.
- `CONSTRAINT_TYPE`
	The type of constraint. The value can be `UNIQUE`, `PRIMARY KEY`, `FOREIGN KEY`, or (as of MySQL 8.0.16) `CHECK`. This is a [`CHAR`](char.md) (not [`ENUM`](enum.md)) column.
	The `UNIQUE` and `PRIMARY           KEY` information is about the same as what you get from the `Key_name` column in the output from [`SHOW INDEX`](show-index.md) when the `Non_unique` column is `0`.
- `ENFORCED`
	For `CHECK` constraints, the value is `YES` or `NO` to indicate whether the constraint is enforced. For other constraints, the value is always `YES`.
	This column was added in MySQL 8.0.16.