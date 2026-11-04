---
title: Sorting Query Results
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/queries005.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Use the `ORDER` `BY` clause to order the rows selected by a query. Sorting by position is useful in the following cases:

- To order by a lengthy select list expression, you can specify its position in the `ORDER` `BY` clause rather than duplicate the entire expression.
- For compound queries containing set operators `UNION`, `INTERSECT`, `MINUS`, or `UNION` `ALL`, the `ORDER` `BY` clause must specify positions or aliases rather than explicit expressions. Also, the `ORDER` `BY` clause can appear only in the last component query. The `ORDER` `BY` clause orders all rows returned by the entire compound query.

The mechanism by which Oracle Database sorts character values for the `ORDER` `BY` clause, also known as the collation, is specified by the `NLS_SORT` session parameter. If this parameter is not set, then its default is derived from the `NLS_LANGUAGE` session parameter. You can change the collation dynamically using the `ALTER` `SESSION` `SET` `NLS_SORT` statement. You can also apply a specific collation by including the character expressions to be sorted as arguments to the `NLSSORT` function, with the collation specified in the second parameter.

When character values are compared linguistically for the `ORDER` `BY` clause, they are first transformed to collation keys and then compared like `RAW` values. The collation keys are generated either explicitly as specified in `NLSSORT` or implicitly using the same method that `NLSSORT` uses. Both explicitly and implicitly generated collation keys are subject to the same restrictions that are described in ["NLSSORT"](functions113.md). As a result of these restrictions, two values may compare as linguistically equal if they do not differ in the prefix that was used to produce the collation key, even if they differ in the rest of the value.

See Also:

[NLSSORT](functions113.md) and [Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/ch3globenv.htm#NLSPG003) for information on the NLS parameters