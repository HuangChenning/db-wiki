---
title: PREVIOUS
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/functions140.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Syntax

  
[Description of the illustration ''previous.gif''](https://docs.oracle.com/cd/E11882_01/server.112/e41084/img_text/previous.htm)  
  

Purpose

The `PREVIOUS` function can be used only in the `model_clause` of the `SELECT` statement and then only in the `ITERATE`... \[ `UNTIL` `]` clause of the `model_rules_clause`. It returns the value of `cell_reference` at the beginning of each iteration.

See Also:

[model\_clause](statements_10002.md) and ["Model Expressions"](expressions010.md) for the syntax and semantics

Examples

The following example repeats the rules, up to 1000 times, until the difference between the values of `cur_val` at the beginning and at the end of an iteration is less than one:

```
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