---
title: NLS_CHARSET_NAME
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/functions109.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Syntax

  
[Description of the illustration ''nls\_charset\_name.gif''](https://docs.oracle.com/cd/E11882_01/server.112/e41084/img_text/nls_charset_name.htm)  
  

Purpose

`NLS_CHARSET_NAME` returns the name of the character set corresponding to ID number `number`. The character set name is returned as a `VARCHAR2` value in the database character set.

If `number` is not recognized as a valid character set ID, then this function returns null.

Examples

The following example returns the character set corresponding to character set ID number 2:

```
SELECT NLS_CHARSET_NAME(2)
  FROM DUAL;

NLS_CH 
------ 
WE8DEC
```