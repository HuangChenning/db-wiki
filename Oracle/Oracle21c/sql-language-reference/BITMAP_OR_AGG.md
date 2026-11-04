---
title: SQL Language Reference
book: SQL Language Reference
doc_id: F31301-19
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/BITMAP_OR_AGG.html
tags:
  - oracle
  - 21c
  - sql-language-reference
---

## BITMAP\_OR\_AGG

Syntax

![bitmap_or_agg](img/bitmap_or_agg.gif)

> ```
> BITMAP_OR_AGG ( expr )
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2025, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Purpose

`BITMAP_OR_AGG` is an aggregation function that operates on bitmaps and computes the OR of its inputs.

The argument `expr` must be of type `BLOB`.

The return type is of type `BLOB`. It returns the bitmap representing the OR of all the bitmaps it has aggregated.

The output of `BITMAP_OR_AGG` is not human-readable. It is meant to be processed by further aggregations via `BITMAP_OR_AGG` or by the scalar function `BITMAP_COUNT`.

If `expr` is NULL, the function returns NULL.

Restrictions

The argument must be of type `BLOB`. The argument is expected to be a bitmap produced by `BITMAP_CONSTRUCT_AGG` or, recursively, by `BITMAP_OR_AGG`. Any other input results in `ORA-62578`:
```
62578, 00000, "The input is not a valid bitmap produced by BITMAP COUNT DISTINCT related operators."
// *Cause: An attempt was made to pass a bitmap that was not produced by one of the BITMAP COUNT DISTINCT operators.
// *Action: Only pass bitmaps constructed via BITMAP_CONSTRUCT_AGG or BITMAP_OR_AGG to BITMAP COUNT DISTINCT related operators.
```