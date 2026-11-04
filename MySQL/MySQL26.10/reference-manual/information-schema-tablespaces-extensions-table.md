---
title: "MySQL :: MySQL 26.10 Reference Manual :: 28.3.46 The INFORMATION_SCHEMA TABLESPACES_EXTENSIONS Table"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/information-schema-tablespaces-extensions-table.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 28.3.46 The INFORMATION\_SCHEMA TABLESPACES\_EXTENSIONS Table

The `TABLESPACES_EXTENSIONS` table provides information about tablespace attributes defined for primary storage engines.

Note

The `TABLESPACES_EXTENSIONS` table is reserved for future use.

The `TABLESPACES_EXTENSIONS` table has these columns:

- `TABLESPACE_NAME`
	The name of the tablespace.
- `ENGINE_ATTRIBUTE`
	Tablespace attributes defined for the primary storage engine. Reserved for future use.