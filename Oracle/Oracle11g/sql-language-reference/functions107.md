---
title: NLS_CHARSET_DECL_LEN
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/functions107.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Syntax

  
[Description of the illustration ''nls\_charset\_decl\_len.gif''](https://docs.oracle.com/cd/E11882_01/server.112/e41084/img_text/nls_charset_decl_len.htm)  
  

Purpose

`NLS_CHARSET_DECL_LEN` returns the declaration length (in number of characters) of an `NCHAR` column. The `byte_count` argument is the width of the column. The `char_set_id` argument is the character set ID of the column.

Examples

The following example returns the number of characters that are in a 200-byte column when you are using a multibyte character set:

```
SELECT NLS_CHARSET_DECL_LEN(200, nls_charset_id('ja16eucfixed')) 
  FROM DUAL; 

NLS_CHARSET_DECL_LEN(200,NLS_CHARSET_ID('JA16EUCFIXED'))
--------------------------------------------------------
                                                     100
```