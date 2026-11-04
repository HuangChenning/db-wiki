---
title: "13.2.10 Subqueries"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/subqueries.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 13.2.10 Subqueries

A subquery is a [`SELECT`](select.md) statement within another statement.

All subquery forms and operations that the SQL standard requires are supported, as well as a few features that are MySQL-specific.

Here is an example of a subquery:

```
SELECT * FROM t1 WHERE column1 = (SELECT column1 FROM t2);
```

In this example, `SELECT * FROM t1 ...` is the *outer query* (or *outer statement*), and `(SELECT column1 FROM       t2)` is the *subquery*. We say that the subquery is *nested* within the outer query, and in fact it is possible to nest subqueries within other subqueries, to a considerable depth. A subquery must always appear within parentheses.

The main advantages of subqueries are:

- They allow queries that are *structured* so that it is possible to isolate each part of a statement.
- They provide alternative ways to perform operations that would otherwise require complex joins and unions.
- Many people find subqueries more readable than complex joins or unions. Indeed, it was the innovation of subqueries that gave people the original idea of calling the early SQL “Structured Query Language.”

Here is an example statement that shows the major points about subquery syntax as specified by the SQL standard and supported in MySQL:

```
DELETE FROM t1
WHERE s11 > ANY
 (SELECT COUNT(*) /* no hint */ FROM t2
  WHERE NOT EXISTS
   (SELECT * FROM t3
    WHERE ROW(5*t2.s1,77)=
     (SELECT 50,11*s1 FROM t4 UNION SELECT 50,77 FROM
      (SELECT * FROM t5) AS t5)));
```

A subquery can return a scalar (a single value), a single row, a single column, or a table (one or more rows of one or more columns). These are called scalar, column, row, and table subqueries. Subqueries that return a particular kind of result often can be used only in certain contexts, as described in the following sections.

There are few restrictions on the type of statements in which subqueries can be used. A subquery can contain many of the keywords or clauses that an ordinary [`SELECT`](select.md) can contain: `DISTINCT`, `GROUP BY`, `ORDER BY`, `LIMIT`, joins, index hints, [`UNION`](union.md) constructs, comments, functions, and so on.

A subquery's outer statement can be any one of: [`SELECT`](select.md), [`INSERT`](insert.md), [`UPDATE`](update.md), [`DELETE`](delete.md), [`SET`](set-variable.md), or [`DO`](do.md).

In MySQL, you cannot modify a table and select from the same table in a subquery. This applies to statements such as [`DELETE`](delete.md), [`INSERT`](insert.md), [`REPLACE`](replace.md), [`UPDATE`](update.md), and (because subqueries can be used in the `SET` clause) [`LOAD DATA`](load-data.md).

For information about how the optimizer handles subqueries, see [Section 8.2.2, “Optimizing Subqueries, Derived Tables, and View References”](subquery-optimization.md). For a discussion of restrictions on subquery use, including performance issues for certain forms of subquery syntax, see [Section 13.2.10.12, “Restrictions on Subqueries”](subquery-restrictions.md).