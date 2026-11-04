---
title: "MySQL :: MySQL 26.7 Reference Manual :: 15.2.4 EXCEPT Clause"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/except.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 15.2.4 EXCEPT Clause

```sql
query_expression_body EXCEPT [ALL | DISTINCT] query_expression_body
    [EXCEPT [ALL | DISTINCT] query_expression_body]
    [...]

query_expression_body:
    See Section 15.2.14, “Set Operations with UNION, INTERSECT, and EXCEPT”
```

`EXCEPT` limits the result from the first query block to those rows which are (also) not found in the second. As with [`UNION`](union.md) and [`INTERSECT`](intersect.md), either query block can make use of any of [`SELECT`](select.md), [`TABLE`](table.md), or [`VALUES`](values.md). An example using the tables `a`, `b`, and `c` defined in [Section 15.2.8, “INTERSECT Clause”](intersect.md), is shown here:

```sql
mysql> TABLE a EXCEPT TABLE b;
+------+------+
| m    | n    |
+------+------+
|    2 |    3 |
+------+------+
1 row in set (0.00 sec)

mysql> TABLE a EXCEPT TABLE c;
+------+------+
| m    | n    |
+------+------+
|    1 |    2 |
|    2 |    3 |
+------+------+
2 rows in set (0.00 sec)

mysql> TABLE b EXCEPT TABLE c;
+------+------+
| m    | n    |
+------+------+
|    1 |    2 |
+------+------+
1 row in set (0.00 sec)
```

As with [`UNION`](union.md) and [`INTERSECT`](intersect.md), if neither `DISTINCT` nor `ALL` is specified, the default is `DISTINCT`.

`DISTINCT` removes duplicates found on either side of the relation, as shown here:

```sql
mysql> TABLE c EXCEPT DISTINCT TABLE a;
+------+------+
| m    | n    |
+------+------+
|    1 |    3 |
+------+------+
1 row in set (0.00 sec)

mysql> TABLE c EXCEPT ALL TABLE a;
+------+------+
| m    | n    |
+------+------+
|    1 |    3 |
|    1 |    3 |
+------+------+
2 rows in set (0.00 sec)
```

(The first statement has the same effect as `TABLE c       EXCEPT TABLE a`.)

Unlike `UNION` or `INTERSECT`, `EXCEPT` is *not* commutative—that is, the result depends on the order of the operands, as shown here:

```sql
mysql> TABLE a EXCEPT TABLE c;
+------+------+
| m    | n    |
+------+------+
|    1 |    2 |
|    2 |    3 |
+------+------+
2 rows in set (0.00 sec)

mysql> TABLE c EXCEPT TABLE a;
+------+------+
| m    | n    |
+------+------+
|    1 |    3 |
+------+------+
1 row in set (0.00 sec)
```

As with `UNION`, the result sets to be compared must have the same number of columns. Result set column types are also determined as for `UNION`.