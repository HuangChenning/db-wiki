---
title: APPROX_COUNT
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/APPROX_COUNT.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

## Syntax

[Description of the illustration approx\_count.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/approx_count.html)

## Purpose

`APPROX_COUNT` returns the approximate count of an expression. If you supply `MAX_ERROR` as the second argument, then the function returns the maximum error between the actual and approximate count.

You must use this function with a corresponding `APPROX_RANK` function in the `HAVING` clause. If a query uses `APPROX_COUNT`, `APPROX_SUM`, or `APPROX_RANK`, then the query must not use any other aggregation functions.

## Examples

The following query returns the 10 most common jobs within every department:

```md
SELECT department_id, job_id,
       APPROX_COUNT(*)
FROM   employees
GROUP BY department_id, job_id
HAVING
  APPROX_RANK (
  PARTITION BY department_id
  ORDER BY APPROX_COUNT(*)
  DESC ) <= 10;
```