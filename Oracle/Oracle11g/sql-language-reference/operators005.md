---
title: Set Operators
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/operators005.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Set operators combine the results of two component queries into a single result. Queries containing set operators are called compound queries. Table 4-4 lists SQL set operators. They are fully described, including examples and restrictions on these operators, in ["The UNION \[ALL\], INTERSECT, MINUS Operators"](https://docs.oracle.com/cd/E11882_01/server.112/e41084/queries004.htm#i2054381).

Table 4-4 Set Operators

| Operator | Returns |
| --- | --- |
| `UNION` | All distinct rows selected by either query |
| `UNION ALL` | All rows selected by either query, including all duplicates |
| `INTERSECT` | All distinct rows selected by both queries |
| `MINUS` | All distinct rows selected by the first query but not the second |