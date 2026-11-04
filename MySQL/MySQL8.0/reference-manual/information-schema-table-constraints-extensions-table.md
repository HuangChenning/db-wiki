---
title: "28.3.43 The INFORMATION_SCHEMA TABLE_CONSTRAINTS_EXTENSIONS Table"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/information-schema-table-constraints-extensions-table.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 28.3.43 The INFORMATION\_SCHEMA TABLE\_CONSTRAINTS\_EXTENSIONS Table

The `TABLE_CONSTRAINTS_EXTENSIONS` table (available as of MySQL 8.0.21) provides information about table constraint attributes defined for primary and secondary storage engines.

Note

The `TABLE_CONSTRAINTS_EXTENSIONS` table is reserved for future use.

The `TABLE_CONSTRAINTS_EXTENSIONS` table has these columns:

- `CONSTRAINT_CATALOG`
	The name of the catalog to which the table belongs.
- `CONSTRAINT_SCHEMA`
	The name of the schema (database) to which the table belongs.
- `CONSTRAINT_NAME`
	The name of the constraint.
- `TABLE_NAME`
	The name of the table.
- `ENGINE_ATTRIBUTE`
	Constraint attributes defined for the primary storage engine. Reserved for future use.
- `SECONDARY_ENGINE_ATTRIBUTE`
	Constraint attributes defined for the secondary storage engine. Reserved for future use.