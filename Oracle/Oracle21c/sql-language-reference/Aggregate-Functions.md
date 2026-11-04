---
title: SQL Language Reference
book: SQL Language Reference
doc_id: F31301-19
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/Aggregate-Functions.html
tags:
  - oracle
  - 21c
  - sql-language-reference
---

## Aggregate Functions

Aggregate functions return a single result row based on groups of rows, rather than on single rows. Aggregate functions can appear in select lists and in `ORDER` `BY` and `HAVING` clauses. They are commonly used with the `GROUP` `BY` clause in a `SELECT` statement, where Oracle Database divides the rows of a queried table or view into groups. In a query containing a `GROUP` `BY` clause, the elements of the select list can be aggregate functions, `GROUP` `BY` expressions, constants, or expressions involving one of these. Oracle applies the aggregate functions to each group of rows and returns a single result row for each group.

If you omit the `GROUP` `BY` clause, then Oracle applies aggregate functions in the select list to all the rows in the queried table or view. You use aggregate functions in the `HAVING` clause to eliminate groups from the output based on the results of the aggregate functions, rather than on the values of the individual rows of the queried table or view.

See Also:

- [Using the GROUP BY Clause: Examples](SELECT.md) and the [HAVING Clause](SELECT.md) for more information on the `GROUP` `BY` clause and `HAVING` clauses in queries and subqueries
- Appendix C in [Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlrf&id=NLSPG-GUID-AFCE41ED-775B-4A00-AF38-C436776AE0C5) for the collation determination rules for expressions in the `ORDER` `BY` clause of an aggregate function

Many (but not all) aggregate functions that take a single argument accept these clauses:

- `DISTINCT` and `UNIQUE`, which are synonymous, cause an aggregate function to consider only distinct values of the argument expression. The syntax diagrams for aggregate functions in this chapter use the keyword `DISTINCT` for simplicity.
- `ALL` causes an aggregate function to consider all values, including all duplicates.

For example, the `DISTINCT` average of 1, 1, 1, and 3 is 2. The `ALL` average is 1.5. If you specify neither, then the default is `ALL`.

Some aggregate functions allow the `windowing_clause`, which is part of the syntax of analytic functions. Refer to [windowing\_clause](Analytic-Functions.md) for information about this clause.

All aggregate functions except `COUNT` (\*), `GROUPING`, and `GROUPING_ID` ignore nulls. You can use the `NVL` function in the argument to an aggregate function to substitute a value for a null. `COUNT` and `REGR_COUNT` never return null, but return either a number or zero. For all the remaining aggregate functions, if the data set contains no rows, or contains only rows with nulls as arguments to the aggregate function, then the function returns null.

The aggregate functions `MIN`, `MAX`, `SUM`, `AVG`, `COUNT`, `VARIANCE`, and `STDDEV`, when followed by the `KEEP` keyword, can be used in conjunction with the `FIRST` or `LAST` function to operate on a set of values from a set of rows that rank as the `FIRST` or `LAST` with respect to a given sorting specification. Refer to [FIRST](FIRST.md) for more information.

You can nest aggregate functions. For example, the following example calculates the average of the maximum salaries of all the departments in the sample schema `hr`:

```
SELECT AVG(MAX(salary))
  FROM employees
  GROUP BY department_id;

AVG(MAX(SALARY))
----------------
      10926.3333
```

This calculation evaluates the inner aggregate (`MAX` (`salary`)) for each group defined by the `GROUP` `BY` clause (`department_id`), and aggregates the results again.

- [ANY\_VALUE](ANY_VALUE.md)
- [APPROX\_COUNT](APPROX_COUNT.md)
- [APPROX\_COUNT\_DISTINCT](APPROX_COUNT_DISTINCT.md)
- [APPROX\_COUNT\_DISTINCT\_AGG](APPROX_COUNT_DISTINCT_AGG.md)
- [APPROX\_COUNT\_DISTINCT\_DETAIL](APPROX_COUNT_DISTINCT_DETAIL.md)
- [APPROX\_MEDIAN](APPROX_MEDIAN.md)
- [APPROX\_PERCENTILE](APPROX_PERCENTILE.md)
- [APPROX\_PERCENTILE\_AGG](APPROX_PERCENTILE_AGG.md)
- [APPROX\_PERCENTILE\_DETAIL](APPROX_PERCENTILE_DETAIL.md)
- [APPROX\_RANK](APPROX_RANK.md)
- [APPROX\_SUM](APPROX_SUM.md)
- [AVG](AVG.md)
- [BIT\_AND\_AGG](BIT_AND_AGG.md)
- [BIT\_OR\_AGG](BIT_OR_AGG.md)
- [BIT\_XOR\_AGG](BIT_XOR_AGG.md)
- [CHECKSUM](checksum.md)
- [COLLECT](COLLECT.md)
- [CORR](CORR.md)
- [CORR\_\*](CORR_A.md)
- [COUNT](COUNT.md)
- [COVAR\_POP](COVAR_POP.md)
- [COVAR\_SAMP](COVAR_SAMP.md)
- [CUME\_DIST](CUME_DIST.md)
- [DENSE\_RANK](DENSE_RANK.md)
- [FIRST](FIRST.md)
- [GROUP\_ID](GROUP_ID.md)
- [GROUPING](GROUPING.md)
- [GROUPING\_ID](GROUPING_ID.md)
- [JSON\_ARRAYAGG](JSON_ARRAYAGG.md)
- [JSON\_OBJECTAGG](JSON_OBJECTAGG.md)
- [KURTOSIS\_POP](KURTOSIS_POP.md)
- [KURTOSIS\_SAMP](KURTOSIS_SAMP.md)
- [LAST](LAST.md)
- [LISTAGG](LISTAGG.md)
- [MAX](MAX.md)
- [MEDIAN](MEDIAN.md)
- [MIN](MIN.md)
- [PERCENT\_RANK](PERCENT_RANK.md)
- [PERCENTILE\_CONT](PERCENTILE_CONT.md)
- [PERCENTILE\_DISC](PERCENTILE_DISC.md)
- [RANK](RANK.md)
- [REGR\_ (Linear Regression) Functions](REGR_-Linear-Regression-Functions.md)
- [SKEWNESS\_POP](SKEWNESS_POP.md)
- [SKEWNESS\_SAMP](SKEWNESS_SAMP.md)
- [STATS\_BINOMIAL\_TEST](STATS_BINOMIAL_TEST.md)
- [STATS\_CROSSTAB](STATS_CROSSTAB.md)
- [STATS\_F\_TEST](STATS_F_TEST.md)
- [STATS\_KS\_TEST](STATS_KS_TEST.md)
- [STATS\_MODE](STATS_MODE.md)
- [STATS\_MW\_TEST](STATS_MW_TEST.md)
- [STATS\_ONE\_WAY\_ANOVA](STATS_ONE_WAY_ANOVA.md)
- [STATS\_T\_TEST\_\*](STATS_T_TEST_.md)
- [STATS\_WSR\_TEST](STATS_WSR_TEST.md)
- [STDDEV](STDDEV.md)
- [STDDEV\_POP](STDDEV_POP.md)
- [STDDEV\_SAMP](STDDEV_SAMP.md)
- [SUM](SUM.md)
- [SYS\_OP\_ZONE\_ID](SYS_OP_ZONE_ID.md)
- [SYS\_XMLAGG](SYS_XMLAGG.md)
- [TO\_APPROX\_COUNT\_DISTINCT](TO_APPROX_COUNT_DISTINCT.md)
- [TO\_APPROX\_PERCENTILE](TO_APPROX_PERCENTILE.md)
- [VAR\_POP](VAR_POP.md)
- [VAR\_SAMP](VAR_SAMP.md)
- [VARIANCE](VARIANCE.md)
- [XMLAGG](XMLAGG.md)