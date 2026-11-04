---
title: TANH
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/functions194.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Syntax

  
[Description of the illustration ''tanh.gif''](https://docs.oracle.com/cd/E11882_01/server.112/e41084/img_text/tanh.htm)  
  

Purpose

`TANH` returns the hyperbolic tangent of `n`.

This function takes as an argument any numeric data type or any nonnumeric data type that can be implicitly converted to a numeric data type. If the argument is `BINARY_FLOAT`, then the function returns `BINARY_DOUBLE`. Otherwise the function returns the same numeric data type as the argument.

See Also:

[Table 3-10, "Implicit Type Conversion Matrix"](sql_elements002.md) for more information on implicit conversion

Examples

The following example returns the hyperbolic tangent of.5:

```
SELECT TANH(.5) "Hyperbolic tangent of .5" 
   FROM DUAL;

Hyperbolic tangent of .5
------------------------
              .462117157
```