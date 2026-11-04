---
title: "B.3.5 Optimizer-Related Issues"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/optimizer-issues.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### B.3.5 Optimizer-Related Issues

MySQL uses a cost-based optimizer to determine the best way to resolve a query. In many cases, MySQL can calculate the best possible query plan, but sometimes MySQL does not have enough information about the data at hand and has to make “educated” guesses about the data.

For the cases when MySQL does not do the "right" thing, tools that you have available to help MySQL are:

- Use the [`EXPLAIN`](explain.md) statement to get information about how MySQL processes a query. To use it, just add the keyword [`EXPLAIN`](explain.md) to the front of your [`SELECT`](select.md) statement:
	```
	mysql> EXPLAIN SELECT * FROM t1, t2 WHERE t1.i = t2.i;
	```
	[`EXPLAIN`](explain.md) is discussed in more detail in [Section 13.8.2, “EXPLAIN Statement”](explain.md).
- Use ``ANALYZE TABLE             *`tbl_name`*`` to update the key distributions for the scanned table. See [Section 13.7.2.1, “ANALYZE TABLE Statement”](analyze-table.md).
- Use `FORCE INDEX` for the scanned table to tell MySQL that table scans are very expensive compared to using the given index:
	```
	SELECT * FROM t1, t2 FORCE INDEX (index_for_column)
	WHERE t1.col_name=t2.col_name;
	```
	`USE INDEX` and `IGNORE             INDEX` may also be useful. See [Section 8.9.4, “Index Hints”](index-hints.md).
- Global and table-level `STRAIGHT_JOIN`. See [Section 13.2.9, “SELECT Statement”](select.md).
- You can tune global or thread-specific system variables. For example, start [**mysqld**](mysqld.md) with the [`--max-seeks-for-key=1000`](server-system-variables.md) option or use `SET max_seeks_for_key=1000` to tell the optimizer to assume that no key scan causes more than 1,000 key seeks. See [Section 5.1.7, “Server System Variables”](server-system-variables.md).