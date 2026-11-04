---
title: SQL Language Reference
book: SQL Language Reference
doc_id: E83703-08
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/sqlrf/TO_BLOB-raw.html
tags:
  - oracle
  - 12c
  - sql-language-reference
---

Syntax

to\_blob::=

![to_blob](img/to_blob.gif)

> ```
> TO_BLOB ( raw_value )
> ```


Purpose

`TO_BLOB` (raw) converts `LONG` `RAW` and `RAW` values to `BLOB` values.

From within a PL/SQL package, you can use `TO_BLOB` (raw) to convert `RAW` and `BLOB` values to `BLOB`.

Examples

The following hypothetical example returns the `BLOB` of a `RAW` column value:

```
SELECT TO_BLOB(raw_column) blob FROM raw_table;

BLOB
-----------------------
00AADD343CDBBD
```