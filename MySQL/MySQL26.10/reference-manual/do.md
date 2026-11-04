---
title: "MySQL :: MySQL 26.10 Reference Manual :: 15.2.3 DO Statement"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/do.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 15.2.3 DO Statement

```sql
DO expr [, expr] ...
```

`DO` executes the expressions but does not return any results. In most respects, `DO` is shorthand for ``SELECT       *`expr`*, ...``, but has the advantage that it is slightly faster when you do not care about the result.

`DO` is useful primarily with functions that have side effects, such as [`RELEASE_LOCK()`](locking-functions.md).

Example: This [`SELECT`](select.md) statement pauses, but also produces a result set:

```sql
mysql> SELECT SLEEP(5);
+----------+
| SLEEP(5) |
+----------+
|        0 |
+----------+
1 row in set (5.02 sec)
```

`DO`, on the other hand, pauses without producing a result set.:

```sql
mysql> DO SLEEP(5);
Query OK, 0 rows affected (4.99 sec)
```

This could be useful, for example in a stored function or trigger, which prohibit statements that produce result sets.

`DO` only executes expressions. It cannot be used in all cases where `SELECT` can be used. For example, `DO id FROM t1` is invalid because it references a table.