---
title: TO_MULTI_BYTE
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/functions206.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Syntax

  
[Description of the illustration ''to\_multi\_byte.gif''](https://docs.oracle.com/cd/E11882_01/server.112/e41084/img_text/to_multi_byte.htm)  
  

Purpose

`TO_MULTI_BYTE` returns `char` with all of its single-byte characters converted to their corresponding multibyte characters. `char` can be of data type `CHAR`, `VARCHAR2`, `NCHAR`, or `NVARCHAR2`. The value returned is in the same data type as `char`.

Any single-byte characters in `char` that have no multibyte equivalents appear in the output string as single-byte characters. This function is useful only if your database character set contains both single-byte and multibyte characters.

This function does not support `CLOB` data directly. However, `CLOB` s can be passed in as arguments through implicit data conversion.

See Also:

["Data Type Comparison Rules"](sql_elements002.md) for more information.

Examples

The following example illustrates converting from a single byte `A` to a multibyte `A` in UTF8:

```
SELECT dump(TO_MULTI_BYTE( 'A')) FROM DUAL; 

DUMP(TO_MULTI_BYTE('A')) 
------------------------ 
Typ=1 Len=3: 239,188,161
```