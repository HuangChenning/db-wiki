---
title: "MySQL :: MySQL 26.10 Reference Manual :: 15.2.16 TABLE Statement"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/table.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 15.2.16 TABLE Statement

`TABLE` is a DML statement which returns rows and columns of the named table.

```sql
TABLE table_name 
    [ORDER BY column_name] 
    [LIMIT number [OFFSET number]]
    [INTO OUTFILE 'file_name'
        [{FIELDS | COLUMNS}
            [TERMINATED BY 'string']
            [[OPTIONALLY] ENCLOSED BY 'char']
            [ESCAPED BY 'char']
        ]
        [LINES
            [STARTING BY 'string']
            [TERMINATED BY 'string']
        ]
    | INTO DUMPFILE 'file_name'
    | INTO var_name [, var_name] ...]
```

The `TABLE` statement in some ways acts like [`SELECT`](select.md). Given the existence of a table named `t`, the following two statements produce identical output:

```sql
TABLE t;

SELECT * FROM t;
```

You can order and limit the number of rows produced by `TABLE` using `ORDER BY` and `LIMIT` clauses, respectively. These function identically to the same clauses when used with `SELECT` (including an optional `OFFSET` clause with `LIMIT`), as you can see here:

```sql
mysql> TABLE t;
+----+----+
| a  | b  |
+----+----+
|  1 |  2 |
|  6 |  7 |
|  9 |  5 |
| 10 | -4 |
| 11 | -1 |
| 13 |  3 |
| 14 |  6 |
+----+----+
7 rows in set (0.00 sec)

mysql> TABLE t ORDER BY b;
+----+----+
| a  | b  |
+----+----+
| 10 | -4 |
| 11 | -1 |
|  1 |  2 |
| 13 |  3 |
|  9 |  5 |
| 14 |  6 |
|  6 |  7 |
+----+----+
7 rows in set (0.00 sec)

mysql> TABLE t LIMIT 3;
+---+---+
| a | b |
+---+---+
| 1 | 2 |
| 6 | 7 |
| 9 | 5 |
+---+---+
3 rows in set (0.00 sec)

mysql> TABLE t ORDER BY b LIMIT 3;
+----+----+
| a  | b  |
+----+----+
| 10 | -4 |
| 11 | -1 |
|  1 |  2 |
+----+----+
3 rows in set (0.00 sec)

mysql> TABLE t ORDER BY b LIMIT 3 OFFSET 2;
+----+----+
| a  | b  |
+----+----+
|  1 |  2 |
| 13 |  3 |
|  9 |  5 |
+----+----+
3 rows in set (0.00 sec)
```

`TABLE` differs from `SELECT` in two key respects:

- `TABLE` always displays all columns of the table.
	*Exception*: The output of `TABLE` does *not* include invisible columns. See [Section 15.1.25.10, “Invisible Columns”](invisible-columns.md).
- `TABLE` does not allow for any arbitrary filtering of rows; that is, `TABLE` does not support any `WHERE` clause.

For limiting which table columns are returned, filtering rows beyond what can be accomplished using `ORDER BY` and `LIMIT`, or both, use `SELECT`.

`TABLE` can be used with temporary tables.

`TABLE` can also be used in place of `SELECT` in a number of other constructs, including those listed here:

- With set operators such as [`UNION`](union.md), as shown here:
	```sql
	mysql> TABLE t1;
	+---+----+
	| a | b  |
	+---+----+
	| 2 | 10 |
	| 5 |  3 |
	| 7 |  8 |
	+---+----+
	3 rows in set (0.00 sec)
	mysql> TABLE t2;
	+---+---+
	| a | b |
	+---+---+
	| 1 | 2 |
	| 3 | 4 |
	| 6 | 7 |
	+---+---+
	3 rows in set (0.00 sec)
	mysql> TABLE t1 UNION TABLE t2;
	+---+----+
	| a | b  |
	+---+----+
	| 2 | 10 |
	| 5 |  3 |
	| 7 |  8 |
	| 1 |  2 |
	| 3 |  4 |
	| 6 |  7 |
	+---+----+
	6 rows in set (0.00 sec)
	```
	The [`UNION`](union.md) just shown is equivalent to the following statement:
	```sql
	mysql> SELECT * FROM t1 UNION SELECT * FROM t2;
	+---+----+
	| a | b  |
	+---+----+
	| 2 | 10 |
	| 5 |  3 |
	| 7 |  8 |
	| 1 |  2 |
	| 3 |  4 |
	| 6 |  7 |
	+---+----+
	6 rows in set (0.00 sec)
	```
	`TABLE` can also be used together in set operations with `SELECT` statements, [`VALUES`](values.md) statements, or both. See [Section 15.2.18, “UNION Clause”](union.md), [Section 15.2.4, “EXCEPT Clause”](except.md), and [Section 15.2.8, “INTERSECT Clause”](intersect.md), for more information and examples. See also [Section 15.2.14, “Set Operations with UNION, INTERSECT, and EXCEPT”](set-operations.md).
- With `INTO` to populate user variables, and with `INTO OUTFILE` or `INTO           DUMPFILE` to write table data to a file. See [Section 15.2.13.1, “SELECT... INTO Statement”](select-into.md), for more specific information and examples.
- In many cases where you can employ subqueries. Given any table `t1` with a column named `a`, and a second table `t2` having a single column, statements such as the following are possible:
	```sql
	SELECT * FROM t1 WHERE a IN (TABLE t2);
	```
	Assuming that the single column of table `t1` is named `x`, the preceding is equivalent to each of the statements shown here (and produces exactly the same result in either case):
	```sql
	SELECT * FROM t1 WHERE a IN (SELECT x FROM t2);
	SELECT * FROM t1 WHERE a IN (SELECT * FROM t2);
	```
	See [Section 15.2.15, “Subqueries”](subqueries.md), for more information.
- With [`INSERT`](insert.md) and [`REPLACE`](replace.md) statements, where you would otherwise use [`SELECT *`](select.md). See [Section 15.2.7.1, “INSERT... SELECT Statement”](insert-select.md), for more information and examples.
- `TABLE` can also be used in many cases in place of the [`SELECT`](select.md) in [`CREATE           TABLE ... SELECT`](create-table-select.md) or [`CREATE VIEW ...           SELECT`](create-view.md). See the descriptions of these statements for more information and examples.