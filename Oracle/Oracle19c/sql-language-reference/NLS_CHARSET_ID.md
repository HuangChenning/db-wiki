---
title: NLS_CHARSET_ID
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/NLS_CHARSET_ID.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

## Syntax

![nls_charset_id](img/nls_charset_id.gif)

> ```
> NLS_CHARSET_ID(string)
> ```
>
> [Copyright ©](https://docs.oracle.com/pls/topic/lookup?ctx=en/legal&id=cpyr) 2026,1996, Oracle and/or its affiliates.


[Description of the illustration nls\_charset\_id.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/nls_charset_id.html)

## Purpose

`NLS_CHARSET_ID` returns the character set ID number corresponding to character set name *string*. The *string* argument is a run-time `VARCHAR2` value. The *string* value ‘ `CHAR_CS` ’ returns the database character set ID number of the server. The *string* value ‘ `NCHAR_CS` ’ returns the national character set ID number of the server.

Invalid character set names return null.

**See Also:** [*Oracle Database Globalization Support Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/sqlrf&id=NLSPG584) for a list of character sets

## Examples

The following example returns the character set ID of a character set:

```md
SELECT NLS_CHARSET_ID('ja16euc')
  FROM DUAL;

NLS_CHARSET_ID('JA16EUC')
-------------------------
                      830
```