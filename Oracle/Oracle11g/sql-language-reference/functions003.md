---
title: Aggregate Functions
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/functions003.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Aggregate functions return a single result row based on groups of rows, rather than on single rows. Aggregate functions can appear in select lists and in `ORDER` `BY` and `HAVING` clauses. They are commonly used with the `GROUP` `BY` clause in a `SELECT` statement, where Oracle Database divides the rows of a queried table or view into groups. In a query containing a `GROUP` `BY` clause, the elements of the select list can be aggregate functions, `GROUP` `BY` expressions, constants, or expressions involving one of these. Oracle applies the aggregate functions to each group of rows and returns a single result row for each group.

If you omit the `GROUP` `BY` clause, then Oracle applies aggregate functions in the select list to all the rows in the queried table or view. You use aggregate functions in the `HAVING` clause to eliminate groups from the output based on the results of the aggregate functions, rather than on the values of the individual rows of the queried table or view.

See Also:

["Using the GROUP BY Clause: Examples"](statements_10002.md) and the ["HAVING Clause"](statements_10002.md) for more information on the `GROUP` `BY` clause and `HAVING` clauses in queries and subqueries

Many (but not all) aggregate functions that take a single argument accept these clauses:

- `DISTINCT` and `UNIQUE`, which are synonymous, cause an aggregate function to consider only distinct values of the argument expression. The syntax diagrams for aggregate functions in this chapter use the keyword `DISTINCT` for simplicity.
- `ALL` causes an aggregate function to consider all values, including all duplicates.

For example, the `DISTINCT` average of 1, 1, 1, and 3 is 2. The `ALL` average is 1.5. If you specify neither, then the default is `ALL`.

Some aggregate functions allow the `windowing_clause`, which is part of the syntax of analytic functions. Refer to [windowing\_clause](functions004.md) for information about this clause. In the listing of aggregate functions at the end of this section, the functions that allow the `windowing_clause` are followed by an asterisk (\*)

All aggregate functions except `COUNT` (\*), `GROUPING`, and `GROUPING_ID` ignore nulls. You can use the `NVL` function in the argument to an aggregate function to substitute a value for a null. `COUNT` and `REGR_COUNT` never return null, but return either a number or zero. For all the remaining aggregate functions, if the data set contains no rows, or contains only rows with nulls as arguments to the aggregate function, then the function returns null.

The aggregate functions `MIN`, `MAX`, `SUM`, `AVG`, `COUNT`, `VARIANCE`, and `STDDEV`, when followed by the `KEEP` keyword, can be used in conjunction with the `FIRST` or `LAST` function to operate on a set of values from a set of rows that rank as the `FIRST` or `LAST` with respect to a given sorting specification. Refer to [FIRST](functions065.md) for more information.

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

In the list of aggregate functions that follows, functions followed by an asterisk (\*) allow the `windowing_clause`.

  
[AVG](functions018.md)  
[COLLECT](functions031.md)  
[CORR](functions035.md)  
[CORR\_\*](functions036.md)  
[COUNT](functions039.md)  
[COVAR\_POP](functions040.md)  
[COVAR\_SAMP](functions041.md)  
[CUME\_DIST](functions043.md)  
[DENSE\_RANK](functions052.md)  
[FIRST](functions065.md)  
[GROUP\_ID](functions070.md)  
[GROUPING](functions071.md)  
[GROUPING\_ID](functions072.md)  
[LAST](functions083.md)  
[LISTAGG](functions089.md)  
[MAX](functions098.md)  
[MEDIAN](functions099.md)  
[MIN](functions100.md)  
[PERCENT\_RANK](functions126.md)  
[PERCENTILE\_CONT](functions127.md)  
[PERCENTILE\_DISC](functions128.md)  
[RANK](functions141.md)  
[REGR\_ (Linear Regression) Functions](functions151.md)  
[STATS\_BINOMIAL\_TEST](functions169.md)  
[STATS\_CROSSTAB](functions170.md)  
[STATS\_F\_TEST](functions171.md)  
[STATS\_KS\_TEST](functions172.md)  
[STATS\_MODE](functions173.md)  
[STATS\_MW\_TEST](functions174.md)  
[STATS\_ONE\_WAY\_ANOVA](functions175.md)  
[STATS\_T\_TEST\_\*](functions176.md)  
[STATS\_WSR\_TEST](functions177.md)  
[STDDEV](functions178.md)  
[STDDEV\_POP](functions179.md)  
[STDDEV\_SAMP](functions180.md)  
[SUM](functions182.md)  
[SYS\_XMLAGG](functions189.md)  
[VAR\_POP](functions230.md)  
[VAR\_SAMP](functions231.md)  
[VARIANCE](functions232.md)  
[XMLAGG](functions235.md)