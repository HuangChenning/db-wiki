---
title: FLOOR
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/functions067.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Syntax

  
[Description of the illustration ''floor.gif''](https://docs.oracle.com/cd/E11882_01/server.112/e41084/img_text/floor.htm)  
  

Purpose

`FLOOR` returns the largest integer equal to or less than `n`. The number `n` can always be written as the sum of an integer `k` and a positive fraction `f` such that 0 <= `f` < 1 and `n` = `k` + `f`. The value of `FLOOR` is the integer `k`. Thus, the value of `FLOOR` is `n` itself if and only if `n` is precisely an integer.

This function takes as an argument any numeric data type or any nonnumeric data type that can be implicitly converted to a numeric data type. The function returns the same data type as the numeric data type of the argument.

See Also:

[Table 3-10, "Implicit Type Conversion Matrix"](sql_elements002.md) for more information on implicit conversion and [CEIL](functions024.md)

Examples

The following example returns the largest integer equal to or less than 15.7:

```
SELECT FLOOR(15.7) "Floor"
  FROM DUAL;

     Floor
----------
        15
```