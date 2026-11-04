---
title: "28.3.40 The INFORMATION_SCHEMA TABLESPACES_EXTENSIONS Table"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/information-schema-tablespaces-extensions-table.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 28.3.40 The INFORMATION\_SCHEMA TABLESPACES\_EXTENSIONS Table

The `TABLESPACES_EXTENSIONS` table provides information about tablespace attributes defined for primary storage engines.

Note

The `TABLESPACES_EXTENSIONS` table is reserved for future use.

The `TABLESPACES_EXTENSIONS` table has these columns:

- `TABLESPACE_NAME`
	The name of the tablespace.
- `ENGINE_ATTRIBUTE`
	Tablespace attributes defined for the primary storage engine. Reserved for future use.