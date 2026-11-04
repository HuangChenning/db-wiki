---
title: "28.3.4 The INFORMATION_SCHEMA CHARACTER_SETS Table"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/information-schema-character-sets-table.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 28.3.4 The INFORMATION\_SCHEMA CHARACTER\_SETS Table

The `CHARACTER_SETS` table provides information about available character sets.

The `CHARACTER_SETS` table has these columns:

- `CHARACTER_SET_NAME`
	The character set name.
- `DEFAULT_COLLATE_NAME`
	The default collation for the character set.
- `DESCRIPTION`
	A description of the character set.
- `MAXLEN`
	The maximum number of bytes required to store one character.

#### Notes

Character set information is also available from the [`SHOW CHARACTER SET`](show-character-set.md) statement. See [Section 15.7.7.4, “SHOW CHARACTER SET Statement”](show-character-set.md). The following statements are equivalent:

```
SELECT * FROM INFORMATION_SCHEMA.CHARACTER_SETS
  [WHERE CHARACTER_SET_NAME LIKE 'wild']

SHOW CHARACTER SET
  [LIKE 'wild']
```