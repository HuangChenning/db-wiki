---
title: PREVIOUS
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/PREVIOUS.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

## Syntax

![previous](img/previous.gif)

> ```
> PREVIOUS(cell_reference)
> ```
>
> [Copyright ©](https://docs.oracle.com/pls/topic/lookup?ctx=en/legal&id=cpyr) 2026,1996, Oracle and/or its affiliates.


[Description of the illustration previous.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/previous.html)

## Purpose

The `PREVIOUS` function can be used only in the *model\_clause* of the `SELECT` statement and then only in the `ITERATE` … \[ `UNTIL` `]` clause of the *model\_rules\_clause*. It returns the value of *cell\_reference* at the beginning of each iteration.

**See Also:**

- *[model\_clause](SELECT.md)* and “ [Model Expressions](Model-Expressions.md) ” for the syntax and semantics
- in [*Oracle Database Globalization Support Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/sqlrf&id=NLSPG-GUID-AFCE41ED-775B-4A00-AF38-C436776AE0C5) for the collation derivation rules, which define the collation assigned to the return value of `PREVIOUS` when it is a character value

## Examples

The following example repeats the rules, up to 1000 times, until the difference between the values of `cur_val` at the beginning and at the end of an iteration is less than one:

```md
SELECT dim_col, cur_val, num_of_iterations
  FROM (SELECT 1 AS dim_col, 10 AS cur_val FROM dual)
  MODEL
    DIMENSION BY (dim_col)
    MEASURES (cur_val, 0 num_of_iterations)
    IGNORE NAV
    UNIQUE DIMENSION
    RULES ITERATE (1000) UNTIL (PREVIOUS(cur_val[1]) - cur_val[1] < 1)
    (
      cur_val[1] = cur_val[1]/2,
      num_of_iterations[1] = num_of_iterations[1] + 1
    );

   DIM_COL    CUR_VAL NUM_OF_ITERATIONS
---------- ---------- -----------------
         1       .625                 4
```