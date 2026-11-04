---
title: "MySQL :: MySQL 26.10 Reference Manual :: 12.11 Restrictions on Character Sets"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/charset-restrictions.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

## 12.11 Restrictions on Character Sets

- Identifiers are stored in `mysql` database tables (`user`, `db`, and so forth) using `utf8mb3`, but identifiers can contain only characters in the Basic Multilingual Plane (BMP). Supplementary characters are not permitted in identifiers.
- The `ucs2`, `utf16`, `utf16le`, and `utf32` character sets have the following restrictions:
	- None of them can be used as the client character set. See [Impermissible Client Character Sets](charset-connection.md).
	- It is currently not possible to use [`LOAD DATA`](load-data.md) to load data files that use these character sets.
	- `FULLTEXT` indexes cannot be created on a column that uses any of these character sets. However, you can perform `IN BOOLEAN MODE` searches on the column without an index.
- The [`REGEXP`](regexp.md) and [`RLIKE`](regexp.md) operators work in byte-wise fashion, so they are not multibyte safe and may produce unexpected results with multibyte character sets. In addition, these operators compare characters by their byte values and accented characters may not compare as equal even if a given collation treats them as equal.