---
title: SQRT
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/functions168.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Syntax

  
[Description of the illustration ''sqrt.gif''](https://docs.oracle.com/cd/E11882_01/server.112/e41084/img_text/sqrt.htm)  
  

Purpose

`SQRT` returns the square root of `n`.

This function takes as an argument any numeric data type or any nonnumeric data type that can be implicitly converted to a numeric data type. The function returns the same data type as the numeric data type of the argument.

See Also:

[Table 3-10, "Implicit Type Conversion Matrix"](sql_elements002.md) for more information on implicit conversion

- If `n` resolves to a `NUMBER`, then the value `n` cannot be negative. `SQRT` returns a real number.
- If `n` resolves to a binary floating-point number (`BINARY_FLOAT` or `BINARY_DOUBLE`):
	- If `n` >= 0, then the result is positive.
		- If `n` = -0, then the result is -0.
		- If `n` < 0, then the result is `NaN`.

Examples

The following example returns the square root of 26:

```
SELECT SQRT(26) "Square root" FROM DUAL;

Square root
-----------
5.09901951
```