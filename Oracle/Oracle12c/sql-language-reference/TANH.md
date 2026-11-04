---
title: SQL Language Reference
book: SQL Language Reference
doc_id: E83703-08
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/sqlrf/TANH.html
tags:
  - oracle
  - 12c
  - sql-language-reference
---

Syntax

![tanh](img/tanh.gif)

> ```
> TANH(n)
> ```


Purpose

`TANH` returns the hyperbolic tangent of `n`.

This function takes as an argument any numeric data type or any nonnumeric data type that can be implicitly converted to a numeric data type. If the argument is `BINARY_FLOAT`, then the function returns `BINARY_DOUBLE`. Otherwise the function returns the same numeric data type as the argument.

Examples

The following example returns the hyperbolic tangent of.5:

```
SELECT TANH(.5) "Hyperbolic tangent of .5" 
   FROM DUAL;

Hyperbolic tangent of .5
------------------------
              .462117157
```