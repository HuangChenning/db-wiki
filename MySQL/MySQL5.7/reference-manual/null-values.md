---
title: "9.1.7 NULL Values"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/null-values.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 9.1.7 NULL Values

The `NULL` value means “no data.” `NULL` can be written in any lettercase. A synonym is `\N` (case-sensitive). Treatment of `\N` as a synonym for `NULL` in SQL statements is deprecated as of MySQL 5.7.18 and is removed in MySQL 8.0; use `NULL` instead.

Be aware that the `NULL` value is different from values such as `0` for numeric types or the empty string for string types. For more information, see [Section B.3.4.3, “Problems with NULL Values”](problems-with-null.md).

For text file import or export operations performed with [`LOAD DATA`](load-data.md) or [`SELECT ... INTO         OUTFILE`](select-into.md), `NULL` is represented by the `\N` sequence. See [Section 13.2.6, “LOAD DATA Statement”](load-data.md). Use of `\N` in text files is unaffected by the deprecation of `\N` in SQL statements.

For sorting with `ORDER BY`, `NULL` values sort before other values for ascending sorts, after other values for descending sorts.