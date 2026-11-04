---
title: COMPOSE
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/functions032.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Syntax

  
[Description of the illustration ''compose.gif''](https://docs.oracle.com/cd/E11882_01/server.112/e41084/img_text/compose.htm)  
  

Purpose

`COMPOSE` takes as its argument a string, or an expression that resolves to a string, in any data type, and returns a Unicode string in the same character set as the input. `char` can be any of the data types `CHAR`, `VARCHAR2`, `NCHAR`, `NVARCHAR2`, `CLOB`, or `NCLOB`. For example, an `o` code point qualified by an umlaut code point will be returned as the o-umlaut code point.

`COMPOSE` returns the string in NFC normal form. For a more exclusive setting, you can first call `DECOMPOSE` with the `CANONICAL` setting and then `COMPOSE`. This combination returns the string in NFKC normal form.

`CLOB` and `NCLOB` values are supported through implicit conversion. If `char` is a character LOB value, then it is converted to a `VARCHAR` value before the `COMPOSE` operation. The operation will fail if the size of the LOB value exceeds the supported length of the `VARCHAR` in the particular development environment.

See Also:

- [Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/ch6unicode.htm#NLSPG006) for information on Unicode character sets and character semantics
- [DECOMPOSE](functions050.md)

Examples

The following example returns the o-umlaut code point:

```
SELECT COMPOSE( 'o' || UNISTR('\0308') )
  FROM DUAL; 

CO 
-- 
ö
```

See Also:

[UNISTR](functions224.md)