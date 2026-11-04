---
title: SQL Language Reference
book: SQL Language Reference
doc_id: F31301-19
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/Set-Operators.html
tags:
  - oracle
  - 21c
  - sql-language-reference
---

## Set Operators

Set operators combine the results of two component queries into a single result. Queries containing set operators are called compound queries. Table 4-5 lists the SQL set operators. They are fully described with examples in [The Set Operators](The-UNION-ALL-INTERSECT-MINUS-Operators.md).

Table 4-5 Set Operators

| Operator | Returns |
| --- | --- |
| `UNION` | All distinct rows selected by either query |
| `UNION ALL` | All rows selected by either query, including duplicates |
| `INTERSECT ` | All distinct rows selected by both queries |
| `INTERSECT ALL` | All rows selected by both queries including duplicates |
| `MINUS ` | All distinct rows selected by the first query but not the second |
| `MINUS ALL ` | All rows selected by the first query but not the second including duplicates |
| `EXCEPT ` | All distinct rows selected by the first query but not the second |
| `EXCEPT ALL` | All rows selected by the first query but not the second including duplicates |