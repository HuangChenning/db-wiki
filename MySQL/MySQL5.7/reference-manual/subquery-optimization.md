---
title: "8.2.2 Optimizing Subqueries, Derived Tables, and View References"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/subquery-optimization.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 8.2.2 Optimizing Subqueries, Derived Tables, and View References

The MySQL query optimizer has different strategies available to evaluate subqueries:

- For `IN` (or `=ANY`) subqueries, the optimizer has these choices:
- For `NOT IN` (or `<>ALL`) subqueries, the optimizer has these choices:

For derived tables, the optimizer has these choices (which also apply to view references):

- Merge the derived table into the outer query block
- Materialize the derived table to an internal temporary table

The following discussion provides more information about the preceding optimization strategies.

Note

A limitation on [`UPDATE`](update.md) and [`DELETE`](delete.md) statements that use a subquery to modify a single table is that the optimizer does not use semijoin or materialization subquery optimizations. As a workaround, try rewriting them as multiple-table [`UPDATE`](update.md) and [`DELETE`](delete.md) statements that use a join rather than a subquery.