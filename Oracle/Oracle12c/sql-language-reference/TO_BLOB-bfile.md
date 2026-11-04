---
title: SQL Language Reference
book: SQL Language Reference
doc_id: E83703-08
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/sqlrf/TO_BLOB-bfile.html
tags:
  - oracle
  - 12c
  - sql-language-reference
---

Syntax

to\_blob\_bfile::=

![to_blob_bfile](img/to_blob_bfile.gif)

> ```
> TO_BLOB( bfile [, mime_type] )
> ```


Purpose

`TO_BLOB` (bfile) converts a `BFILE` value to a `BLOB` value.

For `mime_type`, specify the MIME type to be set on the `BLOB` value returned by this function. If you omit `mime_type`, then a MIME type will not be set on the `BLOB` value.

Example

The following hypothetical example returns the `BLOB` of a `BFILE` column value `media_col` in table `media_tab`. It sets the MIME type to `JPEG` on the resulting `BLOB`.

```
SELECT TO_BLOB(media_col, 'JPEG') FROM media_tab;
```