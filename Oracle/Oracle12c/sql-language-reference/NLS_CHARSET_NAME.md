---
title: SQL Language Reference
book: SQL Language Reference
doc_id: E83703-08
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/sqlrf/NLS_CHARSET_NAME.html
tags:
  - oracle
  - 12c
  - sql-language-reference
---

Syntax

![nls_charset_name](img/nls_charset_name.gif)

> ```
> NLS_CHARSET_NAME(number)
> ```


Purpose

`NLS_CHARSET_NAME` returns the name of the character set corresponding to ID number `number`. The character set name is returned as a `VARCHAR2` value in the database character set. If `number` is not recognized as a valid character set ID, then this function returns null.

This function returns a `VARCHAR2` value.

Examples

The following example returns the character set corresponding to character set ID number 2:

```
SELECT NLS_CHARSET_NAME(2)
  FROM DUAL;

NLS_CH 
------ 
WE8DEC
```