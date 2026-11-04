---
title: NLS_UPPER
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/functions112.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Syntax

![nls_upper](img/nls_upper.gif)

> ```
> NLS_UPPER(char [, 'nlsparam' ])
> ```
  
  

Purpose

`NLS_UPPER` returns `char`, with all letters uppercase.

Both `char` and `'nlsparam'` can be any of the data types `CHAR`, `VARCHAR2`, `NCHAR`, `NVARCHAR2`, `CLOB`, or `NCLOB`. The string returned is of `VARCHAR2` data type if `char` is a character data type and a LOB if `char` is a LOB data type. The return string is in the same character set as `char`.

The `'nlsparam'` can have the same form and serve the same purpose as in the `NLS_INITCAP` function.

Examples

The following example returns a string with all the letters converted to uppercase:

```
SELECT NLS_UPPER('große') "Uppercase"
  FROM DUAL;

Upper
-----
GROßE

SELECT NLS_UPPER('große', 'NLS_SORT = XGerman') "Uppercase" 
  FROM DUAL;

Upperc
------
GROSSE
```

See Also:

[NLS\_INITCAP](functions110.md)