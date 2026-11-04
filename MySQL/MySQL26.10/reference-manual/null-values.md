---
title: "MySQL :: MySQL 26.10 Reference Manual :: 11.1.7 NULL Values"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/null-values.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 11.1.7 NULL Values

The `NULL` value means “no data.” `NULL` can be written in any lettercase.

Be aware that the `NULL` value is different from values such as `0` for numeric types or the empty string for string types. For more information, see [Section B.3.4.3, “Problems with NULL Values”](problems-with-null.md).

For text file import or export operations performed with [`LOAD DATA`](load-data.md) or [`SELECT ... INTO         OUTFILE`](select-into.md), `NULL` is represented by the `\N` sequence. See [Section 15.2.9, “LOAD DATA Statement”](load-data.md).

For sorting with `ORDER BY`, `NULL` values sort before other values for ascending sorts, after other values for descending sorts.