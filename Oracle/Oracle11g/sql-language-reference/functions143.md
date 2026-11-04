---
title: RAWTOHEX
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/functions143.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Syntax

  
[Description of the illustration ''rawtohex.gif''](https://docs.oracle.com/cd/E11882_01/server.112/e41084/img_text/rawtohex.htm)  
  

Purpose

`RAWTOHEX` converts `raw` to a character value containing its hexadecimal representation.

As a SQL built-in function, `RAWTOHEX` accepts an argument of any scalar data type other than `LONG`, `LONG` `RAW`, `CLOB`, `BLOB`, or `BFILE`. It returns a `VARCHAR2` value with the hexadecimal representation of bytes that make up the value of `raw`. Each byte is represented by two hexadecimal digits.

Note:

`RAWTOHEX` behaves differently when used as a PL/SQL built-in function. Refer to [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/fundamentals.htm#LNPLS00212) for more information.

Examples

The following hypothetical example returns the hexadecimal equivalent of a `RAW` column value:

```
SELECT RAWTOHEX(raw_column) "Graphics"
   FROM graphics;

Graphics
--------
7D
```

See Also:

["RAW and LONG RAW Data Types"](sql_elements001.md) and [HEXTORAW](functions073.md)