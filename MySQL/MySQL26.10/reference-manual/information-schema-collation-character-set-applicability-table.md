---
title: "MySQL :: MySQL 26.10 Reference Manual :: 28.3.7 The INFORMATION_SCHEMA COLLATION_CHARACTER_SET_APPLICABILITY Table"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/information-schema-collation-character-set-applicability-table.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 28.3.7 The INFORMATION\_SCHEMA COLLATION\_CHARACTER\_SET\_APPLICABILITY Table

The `COLLATION_CHARACTER_SET_APPLICABILITY` table indicates what character set is applicable for what collation.

The `COLLATION_CHARACTER_SET_APPLICABILITY` table has these columns:

- `COLLATION_NAME`
	The collation name.
- `CHARACTER_SET_NAME`
	The name of the character set with which the collation is associated.

#### Notes

The `COLLATION_CHARACTER_SET_APPLICABILITY` columns are equivalent to the first two columns displayed by the [`SHOW COLLATION`](show-collation.md) statement.