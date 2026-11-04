---
title: "27.5.1 View Syntax"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/view-syntax.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 27.5.1 View Syntax

The [`CREATE VIEW`](create-view.md) statement creates a new view (see [Section 15.1.23, “CREATE VIEW Statement”](create-view.md)). To alter the definition of a view or drop a view, use [`ALTER VIEW`](alter-view.md) (see [Section 15.1.11, “ALTER VIEW Statement”](alter-view.md)), or [`DROP       VIEW`](drop-view.md) (see [Section 15.1.35, “DROP VIEW Statement”](drop-view.md)).

A view can be created from many kinds of [`SELECT`](select.md) statements. It can refer to base tables or other views. It can use joins, [`UNION`](union.md), and subqueries. The [`SELECT`](select.md) need not even refer to any tables. The following example defines a view that selects two columns from another table, as well as an expression calculated from those columns:

```
mysql> CREATE TABLE t (qty INT, price INT);
mysql> INSERT INTO t VALUES(3, 50), (5, 60);
mysql> CREATE VIEW v AS SELECT qty, price, qty*price AS value FROM t;
mysql> SELECT * FROM v;
+------+-------+-------+
| qty  | price | value |
+------+-------+-------+
|    3 |    50 |   150 |
|    5 |    60 |   300 |
+------+-------+-------+
mysql> SELECT * FROM v WHERE qty = 5;
+------+-------+-------+
| qty  | price | value |
+------+-------+-------+
|    5 |    60 |   300 |
+------+-------+-------+
```