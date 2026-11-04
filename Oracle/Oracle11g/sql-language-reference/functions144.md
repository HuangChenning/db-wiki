---
title: RAWTONHEX
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/functions144.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Syntax

  
[Description of the illustration ''rawtonhex.gif''](https://docs.oracle.com/cd/E11882_01/server.112/e41084/img_text/rawtonhex.htm)  
  

Purpose

`RAWTONHEX` converts `raw` to a character value containing its hexadecimal representation. `RAWTONHEX` (`raw`) is equivalent to `TO_NCHAR` (`RAWTOHEX` (`raw`)). The value returned is always in the national character set.

Examples

The following hypothetical example returns the hexadecimal equivalent of a `RAW` column value:

```
SELECT RAWTONHEX(raw_column),
   DUMP ( RAWTONHEX (raw_column) ) "DUMP" 
   FROM graphics; 

RAWTONHEX(RA)           DUMP 
----------------------- ------------------------------ 
7D                      Typ=1 Len=4: 0,55,0,68
```

See Also:

[RAWTOHEX](functions143.md)