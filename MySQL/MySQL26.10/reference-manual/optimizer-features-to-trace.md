---
title: "MySQL :: MySQL 26.10 Reference Manual :: 10.15.10 Selecting Optimizer Features to Trace"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/optimizer-features-to-trace.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 10.15.10 Selecting Optimizer Features to Trace

Some features in the optimizer can be invoked many times during statement optimization and execution, and thus can make the trace grow beyond reason. They are:

- *Greedy search*: With an *`N`* -table join, this could explore factorial(*`N`*) plans.
- *Range optimizer*
- *Dynamic range optimization*: Shown as `range checked for each record` in [`EXPLAIN`](explain.md) output; each outer row causes a re-run of the range optimizer.
- *Subqueries*: A subquery in which the `WHERE` clause may be executed once per row.

Those features can be excluded from tracing by setting one or more switches of the [`optimizer_trace_features`](server-system-variables.md) system variable to `OFF`. These switches are listed here:

- `greedy_search`: Greedy search is not traced.
- `range_optimizer`: The range optimizer is not traced.
- `dynamic_range`: Only the first call to the range optimizer on this `JOIN_TAB::SQL_SELECT` is traced.
- `repeated_subselect`: Only the first execution of this `Item_subselect` is traced.