---
title: NLS_CHARSET_ID
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/functions108.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Syntax

  
[Description of the illustration ''nls\_charset\_id.gif''](https://docs.oracle.com/cd/E11882_01/server.112/e41084/img_text/nls_charset_id.htm)  
  

Purpose

`NLS_CHARSET_ID` returns the character set ID number corresponding to character set name `string`. The `string` argument is a run-time `VARCHAR2` value. The `string` value ' `CHAR_CS` ' returns the database character set ID number of the server. The `string` value ' `NCHAR_CS` ' returns the national character set ID number of the server.

Invalid character set names return null.

Examples

The following example returns the character set ID of a character set:

```
SELECT NLS_CHARSET_ID('ja16euc') 
  FROM DUAL; 

NLS_CHARSET_ID('JA16EUC')
------------------------- 
                      830
```

See Also:

[Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/applocaledata.htm#NLSPG584) for a list of character sets