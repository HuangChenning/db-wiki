---
title: SQL Language Reference
book: SQL Language Reference
doc_id: F31301-19
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/COUNT.html
tags:
  - oracle
  - 21c
  - sql-language-reference
---

## COUNT

Syntax

![count](img/count.gif)

> ```
> COUNT({ * | [ DISTINCT | ALL ] expr }) [ OVER (analytic_clause) ]
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2025, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


See Also:

[Analytic Functions](Analytic-Functions.md) for information on syntax, semantics, and restrictions

Purpose

`COUNT` returns the number of rows returned by the query. You can use it as an aggregate or analytic function.

If you specify `DISTINCT`, then you can specify only the `query_partition_clause` of the `analytic_clause`. The `order_by_clause` and `windowing_clause` are not allowed.

If you specify `expr`, then `COUNT` returns the number of rows where `expr` is not null. You can count either all rows, or only distinct values of `expr`.

If you specify the asterisk (\*), then this function returns all rows, including duplicates and nulls. `COUNT` never returns null.

Note:

Before performing a `COUNT` `(DISTINCT` `expr``)` operation on a large amount of data, consider using one of the following methods to obtain approximate results more quickly than exact results:

- Set the `APPROX_FOR_COUNT_DISTINCT` initialization parameter to true before using the `COUNT` `(DISTINCT` `expr``)` function. Refer to [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlrf&id=REFRN-GUID-D2A8A53F-113A-4E6F-AC2E-37139460EF8D) for more information on this parameter.
- Use the `APPROX_COUNT_DISTINCT` function instead of the `COUNT` `(DISTINCT` `expr``)` function. Refer to [APPROX\_COUNT\_DISTINCT](APPROX_COUNT_DISTINCT.md).

See Also:

- " [About SQL Expressions](About-SQL-Expressions.md) " for information on valid forms of `expr` and [Aggregate Functions](Aggregate-Functions.md)
- Appendix C in [Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlrf&id=NLSPG-GUID-AFCE41ED-775B-4A00-AF38-C436776AE0C5) for the collation determination rules, which define the collation `COUNT` uses to compare character values for the `DISTINCT` clause

Aggregate Examples

The following examples use `COUNT` as an aggregate function:

```
SELECT COUNT(*) "Total"
  FROM employees;

     Total
----------
       107

SELECT COUNT(*) "Allstars"
  FROM employees
  WHERE commission_pct > 0;

 Allstars
---------
       35

SELECT COUNT(commission_pct) "Count"
  FROM employees;

     Count
----------
        35

SELECT COUNT(DISTINCT manager_id) "Managers"
  FROM employees;

  Managers
----------
        18
```

Analytic Example

The following example calculates, for each employee in the `employees` table, the moving count of employees earning salaries in the range 50 less than through 150 greater than the employee's salary.

```
SELECT last_name, salary,
       COUNT(*) OVER (ORDER BY salary RANGE BETWEEN 50 PRECEDING AND
                      150 FOLLOWING) AS mov_count
  FROM employees
  ORDER BY salary, last_name;

LAST_NAME                     SALARY  MOV_COUNT
------------------------- ---------- ----------
Olson                           2100          3
Markle                          2200          2
Philtanker                      2200          2
Gee                             2400          8
Landry                          2400          8
Colmenares                      2500         10
Marlow                          2500         10
Patel                           2500         10
. . .
```