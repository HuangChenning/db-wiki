---
title: "28.3.46 The INFORMATION_SCHEMA TABLESPACES_EXTENSIONS Table"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/information-schema-tablespaces-extensions-table.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 28.3.46 The INFORMATION\_SCHEMA TABLESPACES\_EXTENSIONS Table

The `TABLESPACES_EXTENSIONS` table provides information about tablespace attributes defined for primary storage engines.

Note

The `TABLESPACES_EXTENSIONS` table is reserved for future use.

The `TABLESPACES_EXTENSIONS` table has these columns:

- `TABLESPACE_NAME`
	The name of the tablespace.
- `ENGINE_ATTRIBUTE`
	Tablespace attributes defined for the primary storage engine. Reserved for future use.