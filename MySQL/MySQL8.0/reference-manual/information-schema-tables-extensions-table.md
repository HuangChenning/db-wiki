---
title: "28.3.39 The INFORMATION_SCHEMA TABLES_EXTENSIONS Table"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/information-schema-tables-extensions-table.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 28.3.39 The INFORMATION\_SCHEMA TABLES\_EXTENSIONS Table

The `TABLES_EXTENSIONS` table (available as of MySQL 8.0.21) provides information about table attributes defined for primary and secondary storage engines.

Note

The `TABLES_EXTENSIONS` table is reserved for future use.

The `TABLES_EXTENSIONS` table has these columns:

- `TABLE_CATALOG`
	The name of the catalog to which the table belongs. This value is always `def`.
- `TABLE_SCHEMA`
	The name of the schema (database) to which the table belongs.
- `TABLE_NAME`
	The name of the table.
- `ENGINE_ATTRIBUTE`
	Table attributes defined for the primary storage engine. Reserved for future use.
- `SECONDARY_ENGINE_ATTRIBUTE`
	Table attributes defined for the secondary storage engine. Reserved for future use.