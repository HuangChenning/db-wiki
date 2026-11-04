---
title: "28.3.6 The INFORMATION_SCHEMA COLLATIONS Table"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/information-schema-collations-table.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 28.3.6 The INFORMATION\_SCHEMA COLLATIONS Table

The `COLLATIONS` table provides information about collations for each character set.

The `COLLATIONS` table has these columns:

- `COLLATION_NAME`
	The collation name.
- `CHARACTER_SET_NAME`
	The name of the character set with which the collation is associated.
- `ID`
	The collation ID.
- `IS_DEFAULT`
	Whether the collation is the default for its character set.
- `IS_COMPILED`
	Whether the character set is compiled into the server.
- `SORTLEN`
	This is related to the amount of memory required to sort strings expressed in the character set.
- `PAD_ATTRIBUTE`
	The collation pad attribute, either `NO PAD` or `PAD SPACE`. This attribute affects whether trailing spaces are significant in string comparisons; see [Trailing Space Handling in Comparisons](charset-binary-collations.md).

#### Notes

Collation information is also available from the [`SHOW COLLATION`](show-collation.md) statement. See [Section 15.7.7.4, “SHOW COLLATION Statement”](show-collation.md). The following statements are equivalent:

```
SELECT COLLATION_NAME FROM INFORMATION_SCHEMA.COLLATIONS
  [WHERE COLLATION_NAME LIKE 'wild']

SHOW COLLATION
  [LIKE 'wild']
```