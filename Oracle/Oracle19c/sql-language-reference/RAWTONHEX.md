---
title: RAWTONHEX
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/RAWTONHEX.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

## Syntax

![rawtonhex](img/rawtonhex.gif)

> ```
> RAWTONHEX(raw)
> ```
>
> [Copyright ©](https://docs.oracle.com/pls/topic/lookup?ctx=en/legal&id=cpyr) 2026,1996, Oracle and/or its affiliates.


[Description of the illustration rawtonhex.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/rawtonhex.html)

## Purpose

`RAWTONHEX` converts *raw* to a character value containing its hexadecimal representation. `RAWTONHEX(`*raw*`)` is equivalent to `TO_NCHAR(RAWTOHEX(`*raw*`))`. The value returned is always in the national character set.

**Note:** `RAWTONHEX` functions differently when used as a PL/SQL built-in function. Refer to [*Oracle Database Development Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/sqlrf&id=ADFNS00308) for more information.

## Examples

The following hypothetical example returns the hexadecimal equivalent of a `RAW` column value:

```md
SELECT RAWTONHEX(raw_column),
   DUMP ( RAWTONHEX (raw_column) ) "DUMP"
   FROM graphics;

RAWTONHEX(RA)           DUMP
----------------------- ------------------------------
7D                      Typ=1 Len=4: 0,55,0,68
```