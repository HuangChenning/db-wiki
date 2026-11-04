---
title: VSIZE
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/functions233.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Syntax

  
[Description of the illustration ''vsize.gif''](https://docs.oracle.com/cd/E11882_01/server.112/e41084/img_text/vsize.htm)  
  

Purpose

`VSIZE` returns the number of bytes in the internal representation of `expr`. If `expr` is null, then this function returns null.

This function does not support `CLOB` data directly. However, `CLOB` s can be passed in as arguments through implicit data conversion.

See Also:

["Data Type Comparison Rules"](sql_elements002.md) for more information

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