---
title: TO_BLOB (bfile)
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/TO_BLOB-bfile.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

## Syntax

## to\_blob\_bfile::=

![to_blob_bfile](img/to_blob_bfile.gif)

> ```
> TO_BLOB( bfile [, mime_type] )
> ```
>
> [Copyright ©](https://docs.oracle.com/pls/topic/lookup?ctx=en/legal&id=cpyr) 2026,1996, Oracle and/or its affiliates.


[Description of the illustration to\_blob\_bfile.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/to_blob_bfile.html)

## Purpose

`TO_BLOB` (bfile) converts a `BFILE` value to a `BLOB` value.

For *mime\_type*, specify the MIME type to be set on the `BLOB` value returned by this function. If you omit *mime\_type*, then a MIME type will not be set on the `BLOB` value.

## Example

The following hypothetical example returns the `BLOB` of a `BFILE` column value `media_col` in table `media_tab`. It sets the MIME type to `JPEG` on the resulting `BLOB`.

```md
SELECT TO_BLOB(media_col, 'JPEG') FROM media_tab;
```