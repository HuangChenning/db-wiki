---
title: "28.3.41 The INFORMATION_SCHEMA TABLESPACES_EXTENSIONS Table"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/information-schema-tablespaces-extensions-table.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 28.3.41 The INFORMATION\_SCHEMA TABLESPACES\_EXTENSIONS Table

The `TABLESPACES_EXTENSIONS` table (available as of MySQL 8.0.21) provides information about tablespace attributes defined for primary storage engines.

Note

The `TABLESPACES_EXTENSIONS` table is reserved for future use.

The `TABLESPACES_EXTENSIONS` table has these columns:

- `TABLESPACE_NAME`
	The name of the tablespace.
- `ENGINE_ATTRIBUTE`
	Tablespace attributes defined for the primary storage engine. Reserved for future use.