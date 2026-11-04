---
title: SQL Language Reference
book: SQL Language Reference
doc_id: F31301-19
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/VSIZE.html
tags:
  - oracle
  - 21c
  - sql-language-reference
---

## VSIZE

Syntax

![vsize](img/vsize.gif)

> ```
> VSIZE(expr)
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2025, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Purpose

`VSIZE` returns the number of bytes in the internal representation of `expr`. If `expr` is null, then this function returns null.

This function does not support `CLOB` data directly. However, `CLOB` s can be passed in as arguments through implicit data conversion.

See Also:

" [Data Type Comparison Rules](Data-Type-Comparison-Rules.md) " for more information

Examples

The following example returns the number of bytes in the `last_name` column of the employees in department 10:

```
SELECT last_name, VSIZE (last_name) "BYTES"      
  FROM employees
  WHERE department_id = 10
  ORDER BY employee_id;
 
LAST_NAME            BYTES
--------------- ----------
Whalen                   6
```