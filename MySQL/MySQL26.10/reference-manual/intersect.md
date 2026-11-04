---
title: "MySQL :: MySQL 26.10 Reference Manual :: 15.2.8 INTERSECT Clause"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/intersect.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 15.2.8 INTERSECT Clause

```sql
query_expression_body INTERSECT [ALL | DISTINCT] query_expression_body
    [INTERSECT [ALL | DISTINCT] query_expression_body]
    [...]

query_expression_body:
    See Section 15.2.14, “Set Operations with UNION, INTERSECT, and EXCEPT”
```

`INTERSECT` limits the result from multiple query blocks to those rows which are common to all. Example:

```sql
mysql> TABLE a;
+------+------+
| m    | n    |
+------+------+
|    1 |    2 |
|    2 |    3 |
|    3 |    4 |
+------+------+
3 rows in set (0.00 sec)

mysql> TABLE b;
+------+------+
| m    | n    |
+------+------+
|    1 |    2 |
|    1 |    3 |
|    3 |    4 |
+------+------+
3 rows in set (0.00 sec)

mysql> TABLE c;
+------+------+
| m    | n    |
+------+------+
|    1 |    3 |
|    1 |    3 |
|    3 |    4 |
+------+------+
3 rows in set (0.00 sec)

mysql> TABLE a INTERSECT TABLE b;
+------+------+
| m    | n    |
+------+------+
|    1 |    2 |
|    3 |    4 |
+------+------+
2 rows in set (0.00 sec)

mysql> TABLE a INTERSECT TABLE c;
+------+------+
| m    | n    |
+------+------+
|    3 |    4 |
+------+------+
1 row in set (0.00 sec)
```

As with [`UNION`](union.md) and [`EXCEPT`](except.md), if neither `DISTINCT` nor `ALL` is specified, the default is `DISTINCT`.

`DISTINCT` can remove duplicates from either side of the intersection, as shown here:

```sql
mysql> TABLE c INTERSECT DISTINCT TABLE c;
+------+------+
| m    | n    |
+------+------+
|    1 |    3 |
|    3 |    4 |
+------+------+
2 rows in set (0.00 sec)

mysql> TABLE c INTERSECT ALL TABLE c;
+------+------+
| m    | n    |
+------+------+
|    1 |    3 |
|    1 |    3 |
|    3 |    4 |
+------+------+
3 rows in set (0.00 sec)
```

(`TABLE c INTERSECT TABLE c` is the equivalent of the first of the two statements just shown.)

As with `UNION`, the operands must have the same number of columns. Result set column types are also determined as for `UNION`.

`INTERSECT` has greater precedence than and is evaluated before `UNION` and `EXCEPT`, so that the two statements shown here are equivalent:

```svg
TABLE r EXCEPT TABLE s INTERSECT TABLE t;

TABLE r EXCEPT (TABLE s INTERSECT TABLE t);
```

For `INTERSECT ALL`, the maximum supported number of duplicates of any unique row in the left hand table is `4294967295`.