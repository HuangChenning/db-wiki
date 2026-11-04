---
title: Set Operators
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/Set-Operators.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

Set operators combine the results of two component queries into a single result. Queries containing set operators are called compound queries. Table 4-5 lists SQL set operators. They are fully described, including examples and restrictions on these operators, in [The UNION \[ALL\], INTERSECT, MINUS Operators](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/The-UNION-ALL-INTERSECT-MINUS-Operators.html#GUID-B64FE747-586E-4513-945F-80CB197125EE).

Table 5 Set Operators

| Operator | Returns |
| --- | --- |
| `UNION` | All distinct rows selected by either query |
| `UNION ALL` | All rows selected by either query, including all duplicates |
| `INTERSECT` | All distinct rows selected by both queries |
| `MINUS` | All distinct rows selected by the first query but not the second |