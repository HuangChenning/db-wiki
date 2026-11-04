---
title: ASCII
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/ASCII.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

## Syntax

![ascii](img/ascii.gif)

> ```
> ASCII(char)
> ```
>
> [Copyright ©](https://docs.oracle.com/pls/topic/lookup?ctx=en/legal&id=cpyr) 2026,1996, Oracle and/or its affiliates.


[Description of the illustration ascii.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/ascii.html)

## Purpose

`ASCII` returns the decimal representation in the database character set of the first character of *char*.

*char* can be of data type `CHAR`, `VARCHAR2`, `NCHAR`, or `NVARCHAR2`. The value returned is of data type `NUMBER`. If your database character set is 7-bit ASCII, then this function returns an ASCII value. If your database character set is EBCDIC Code, then this function returns an EBCDIC value. There is no corresponding EBCDIC character function.

This function does not support `CLOB` data directly. However, `CLOB` s can be passed in as arguments through implicit data conversion.

**See Also:** [Data Type Comparison Rules](Data-Type-Comparison-Rules.md) for more information

## Examples

The following example returns employees whose last names begin with the letter L, whose ASCII equivalent is 76:

```md
SELECT last_name
  FROM employees
  WHERE ASCII(SUBSTR(last_name, 1, 1)) = 76
  ORDER BY last_name;

LAST_NAME
-------------------------
Ladwig
Landry
Lee
Livingston
Lorentz
```