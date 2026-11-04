---
title: SQL Language Reference
book: SQL Language Reference
doc_id: F31301-19
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/COALESCE.html
tags:
  - oracle
  - 21c
  - sql-language-reference
---

## COALESCE

Syntax

![coalesce](img/coalesce.gif)

> ```
> COALESCE(expr [, expr ]...)
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2025, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Purpose

`COALESCE` returns the first non-null `expr` in the expression list. You must specify at least two expressions. If all occurrences of `expr` evaluate to null, then the function returns null.

Oracle Database uses short-circuit evaluation. The database evaluates each `expr` value and determines whether it is `NULL`, rather than evaluating all of the `expr` values before determining whether any of them is `NULL`.

If all occurrences of `expr` are numeric data type or any nonnumeric data type that can be implicitly converted to a numeric data type, then Oracle Database determines the argument with the highest numeric precedence, implicitly converts the remaining arguments to that data type, and returns that data type.

See Also:

- [Table 2-8](Data-Type-Comparison-Rules.md) for more information on implicit conversion and [Numeric Precedence](Data-Types.md) for information on numeric precedence
- Appendix C in [Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlrf&id=NLSPG-GUID-AFCE41ED-775B-4A00-AF38-C436776AE0C5) for the collation derivation rules, which define the collation assigned to the return value of `COALESCE` when it is a character value

This function is a generalization of the `NVL` function.

You can also use `COALESCE` as a variety of the `CASE` expression. For example,

```
COALESCE(expr1, expr2)
```

is equivalent to:

```
CASE WHEN expr1 IS NOT NULL THEN expr1 ELSE expr2 END
```

Similarly,

```
COALESCE(expr1, expr2, ..., exprn)
```

where `n` >= 3, is equivalent to:

```
CASE WHEN expr1 IS NOT NULL THEN expr1 
   ELSE COALESCE (expr2, ..., exprn) END
```

See Also:

[NVL](NVL.md) and [CASE Expressions](CASE-Expressions.md)

Examples

The following example uses the sample `oe.product_information` table to organize a clearance sale of products. It gives a 10% discount to all products with a list price. If there is no list price, then the sale price is the minimum price. If there is no minimum price, then the sale price is "5":

```
SELECT product_id, list_price, min_price,
       COALESCE(0.9*list_price, min_price, 5) "Sale"
  FROM product_information
  WHERE supplier_id = 102050
  ORDER BY product_id;

PRODUCT_ID LIST_PRICE  MIN_PRICE       Sale
---------- ---------- ---------- ----------
      1769         48                  43.2
      1770                    73         73
      2378        305        247      274.5
      2382        850        731        765
      3355                                5
```