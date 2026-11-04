---
title: SQL Language Reference
book: SQL Language Reference
doc_id: F31301-19
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/COVAR_SAMP.html
tags:
  - oracle
  - 21c
  - sql-language-reference
---

## COVAR\_SAMP

Syntax

![covar_samp](img/covar_samp.gif)

> ```
> COVAR_SAMP(expr1, expr2) [ OVER (analytic_clause) ]
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2025, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


See Also:

[Analytic Functions](Analytic-Functions.md) for information on syntax, semantics, and restrictions

Purpose

`COVAR_SAMP` returns the sample covariance of a set of number pairs. You can use it as an aggregate or analytic function.

This function takes as arguments any numeric data type or any nonnumeric data type that can be implicitly converted to a numeric data type. Oracle determines the argument with the highest numeric precedence, implicitly converts the remaining arguments to that data type, and returns that data type.

See Also:

[Table 2-8](Data-Type-Comparison-Rules.md) for more information on implicit conversion and [Numeric Precedence](Data-Types.md) for information on numeric precedence

Oracle Database applies the function to the set of (`expr1`, `expr2`) pairs after eliminating all pairs for which either `expr1` or `expr2` is null. Then Oracle makes the following computation:

```
(SUM(expr1 * expr2) - SUM(expr1) * SUM(expr2) / n) / (n-1)
```

where `n` is the number of (`expr1`, `expr2`) pairs where neither `expr1` nor `expr2` is null.

The function returns a value of type `NUMBER`. If the function is applied to an empty set, then it returns null.

See Also:

[About SQL Expressions](About-SQL-Expressions.md) for information on valid forms of `expr` and [Aggregate Functions](Aggregate-Functions.md)

Aggregate Example

Refer to the aggregate example for [COVAR\_POP](COVAR_POP.md).

Analytic Example

Refer to the analytic example for [COVAR\_POP](COVAR_POP.md).