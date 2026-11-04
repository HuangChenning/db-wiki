---
title: SQL Language Reference
book: SQL Language Reference
doc_id: F31301-19
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/LAST.html
tags:
  - oracle
  - 21c
  - sql-language-reference
---

## LAST

Syntax

last::=

![last](img/last.gif)

> ```
> aggregate_function KEEP
>   (DENSE_RANK LAST ORDER BY
>     expr [ DESC | ASC ]
>          [ NULLS { FIRST | LAST } ]
>     [, expr [ DESC | ASC ]
>             [ NULLS { FIRST | LAST } ]
>     ]...
>   )
>   [ OVER ( [query_partition_clause] ) ]
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2025, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


See Also:

" [Analytic Functions](Analytic-Functions.md) " for information on syntax, semantics, and restrictions of the `query_partitioning_clause`

Purpose

`FIRST` and `LAST` are very similar functions. Both are aggregate and analytic functions that operate on a set of values from a set of rows that rank as the `FIRST` or `LAST` with respect to a given sorting specification. If only one row ranks as `FIRST` or `LAST`, then the aggregate operates on the set with only one element.

Refer to [FIRST](FIRST.md) for complete information on this function and for examples of its use.