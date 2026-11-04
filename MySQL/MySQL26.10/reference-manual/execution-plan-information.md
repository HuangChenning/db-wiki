---
title: "MySQL :: MySQL 26.10 Reference Manual :: 10.8 Understanding the Query Execution Plan"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/execution-plan-information.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

## 10.8 Understanding the Query Execution Plan

Depending on the details of your tables, columns, indexes, and the conditions in your `WHERE` clause, the MySQL optimizer considers many techniques to efficiently perform the lookups involved in an SQL query. A query on a huge table can be performed without reading all the rows; a join involving several tables can be performed without comparing every combination of rows. The set of operations that the optimizer chooses to perform the most efficient query is called the “query execution plan”, also known as the [`EXPLAIN`](explain.md) plan. Your goals are to recognize the aspects of the [`EXPLAIN`](explain.md) plan that indicate a query is optimized well, and to learn the SQL syntax and indexing techniques to improve the plan if you see some inefficient operations.