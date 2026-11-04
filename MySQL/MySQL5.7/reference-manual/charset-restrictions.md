---
title: "10.11 Restrictions on Character Sets"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/charset-restrictions.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

- Identifiers are stored in `mysql` database tables (`user`, `db`, and so forth) using `utf8`, but identifiers can contain only characters in the Basic Multilingual Plane (BMP). Supplementary characters are not permitted in identifiers.
- The `ucs2`, `utf16`, `utf16le`, and `utf32` character sets have the following restrictions:
	- None of them can be used as the client character set. See [Impermissible Client Character Sets](charset-connection.md).
	- It is currently not possible to use [`LOAD DATA`](load-data.md) to load data files that use these character sets.
	- `FULLTEXT` indexes cannot be created on a column that uses any of these character sets. However, you can perform `IN BOOLEAN MODE` searches on the column without an index.
	- The use of [`ENCRYPT()`](encryption-functions.md) with these character sets is not recommended because the underlying system call expects a string terminated by a zero byte.
- The [`REGEXP`](regexp.md) and [`RLIKE`](regexp.md) operators work in byte-wise fashion, so they are not multibyte safe and may produce unexpected results with multibyte character sets. In addition, these operators compare characters by their byte values and accented characters may not compare as equal even if a given collation treats them as equal.