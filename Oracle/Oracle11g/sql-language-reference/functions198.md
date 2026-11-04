---
title: TO_BLOB
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/functions198.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Syntax

to\_blob::=

  
[Description of the illustration ''to\_blob.gif''](https://docs.oracle.com/cd/E11882_01/server.112/e41084/img_text/to_blob.htm)  
  

Purpose

`TO_BLOB` converts `LONG` `RAW` and `RAW` values to `BLOB` values.

From within a PL/SQL package, you can use `TO_BLOB` to convert `RAW` and `BLOB` values to `BLOB`.

Examples

The following hypothetical example returns the `BLOB` of a `RAW` column value:

```
SELECT TO_BLOB(raw_column) blob FROM raw_table;

BLOB
-----------------------
00AADD343CDBBD
```