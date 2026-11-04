---
title: "15.8.2 EXPLAIN Statement"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/explain.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 15.8.2 EXPLAIN Statement

```
{EXPLAIN | DESCRIBE | DESC}
    tbl_name [col_name | wild]

{EXPLAIN | DESCRIBE | DESC}
    [explain_type] [INTO variable]
    {[schema_spec] explainable_stmt | FOR CONNECTION connection_id}

{EXPLAIN | DESCRIBE | DESC} ANALYZE [FORMAT = TREE] [schema_spec] select_statement

explain_type: {
    FORMAT = format_name
}

format_name: {
    TRADITIONAL
  | JSON
  | TREE
}

explainable_stmt: {
    SELECT statement
  | TABLE statement
  | DELETE statement
  | INSERT statement
  | REPLACE statement
  | UPDATE statement
}

schema_spec:
FOR {SCHEMA | DATABASE} schema_name
```

The [`DESCRIBE`](describe.md) and `EXPLAIN` statements are synonyms. In practice, the [`DESCRIBE`](describe.md) keyword is more often used to obtain information about table structure, whereas `EXPLAIN` is used to obtain a query execution plan (that is, an explanation of how MySQL would execute a query).

The following discussion uses the [`DESCRIBE`](describe.md) and `EXPLAIN` keywords in accordance with those uses, but the MySQL parser treats them as completely synonymous.

#### Obtaining Table Structure Information

[`DESCRIBE`](describe.md) provides information about the columns in a table:

```
mysql> DESCRIBE City;
+------------+----------+------+-----+---------+----------------+
| Field      | Type     | Null | Key | Default | Extra          |
+------------+----------+------+-----+---------+----------------+
| Id         | int(11)  | NO   | PRI | NULL    | auto_increment |
| Name       | char(35) | NO   |     |         |                |
| Country    | char(3)  | NO   | UNI |         |                |
| District   | char(20) | YES  | MUL |         |                |
| Population | int(11)  | NO   |     | 0       |                |
+------------+----------+------+-----+---------+----------------+
```

[`DESCRIBE`](describe.md) is a shortcut for [`SHOW COLUMNS`](show-columns.md). These statements also display information for views. The description for [`SHOW COLUMNS`](show-columns.md) provides more information about the output columns. See [Section 15.7.7.6, “SHOW COLUMNS Statement”](show-columns.md).

By default, [`DESCRIBE`](describe.md) displays information about all columns in the table. *`col_name`*, if given, is the name of a column in the table. In this case, the statement displays information only for the named column. *`wild`*, if given, is a pattern string. It can contain the SQL `%` and `_` wildcard characters. In this case, the statement displays output only for the columns with names matching the string. There is no need to enclose the string within quotation marks unless it contains spaces or other special characters.

The [`DESCRIBE`](describe.md) statement is provided for compatibility with Oracle.

The [`SHOW CREATE TABLE`](show-create-table.md), [`SHOW TABLE STATUS`](show-table-status.md), and [`SHOW INDEX`](show-index.md) statements also provide information about tables. See [Section 15.7.7, “SHOW Statements”](show.md).

The [`explain_format`](server-system-variables.md) system variable has no effect on the output of `EXPLAIN` when used to obtain information about table columns.

#### Obtaining Execution Plan Information

The `EXPLAIN` statement provides information about how MySQL executes statements:

- `EXPLAIN` works with [`SELECT`](select.md), [`DELETE`](delete.md), [`INSERT`](insert.md), [`REPLACE`](replace.md), [`UPDATE`](update.md), and [`TABLE`](table.md) statements.
- When `EXPLAIN` is used with an explainable statement, MySQL displays information from the optimizer about the statement execution plan. That is, MySQL explains how it would process the statement, including information about how tables are joined and in which order. For information about using `EXPLAIN` to obtain execution plan information, see [Section 10.8.2, “EXPLAIN Output Format”](explain-output.md).
- When `EXPLAIN` is used with ``FOR CONNECTION             *`connection_id`*`` rather than an explainable statement, it displays the execution plan for the statement executing in the named connection. See [Section 10.8.4, “Obtaining Execution Plan Information for a Named Connection”](explain-for-connection.md).
- For explainable statements, `EXPLAIN` produces additional execution plan information that can be displayed using [`SHOW WARNINGS`](show-warnings.md). See [Section 10.8.3, “Extended EXPLAIN Output Format”](explain-extended.md).
- `EXPLAIN` is useful for examining queries involving partitioned tables. See [Section 26.3.5, “Obtaining Information About Partitions”](partitioning-info.md).
- The `FORMAT` option can be used to select the output format. `TRADITIONAL` presents the output in tabular format. This is the default if no `FORMAT` option is present. `JSON` format displays the information in JSON format. `TREE` provides tree-like output with more precise descriptions of query handling than the `TRADITIONAL` format; it is the only format which shows hash join usage (see [Section 10.2.1.4, “Hash Join Optimization”](hash-joins.md)) and is always used for `EXPLAIN ANALYZE`.
	In MySQL 8.4, the default output format used by `EXPLAIN` (that is, when it has no `FORMAT` option) is determined by the value of the [`explain_format`](server-system-variables.md) system variable. The precise effects of this variable are described later in this section.
	MySQL 8.4 supports an additional `INTO` option with `EXPLAIN             FORMAT=JSON`, which enables saving the JSON formatted output into a user variable, like this:
	```
	mysql> EXPLAIN FORMAT=JSON INTO @myselect 
	    ->     SELECT name FROM a WHERE id = 2;
	Query OK, 0 rows affected (0.00 sec)
	mysql> SELECT @myselect\G
	*************************** 1. row ***************************
	@myex: {
	  "query_block": {
	    "select_id": 1,
	    "cost_info": {
	      "query_cost": "1.00"
	    },
	    "table": {
	      "table_name": "a",
	      "access_type": "const",
	      "possible_keys": [
	        "PRIMARY"
	      ],
	      "key": "PRIMARY",
	      "used_key_parts": [
	        "id"
	      ],
	      "key_length": "4",
	      "ref": [
	        "const"
	      ],
	      "rows_examined_per_scan": 1,
	      "rows_produced_per_join": 1,
	      "filtered": "100.00",
	      "cost_info": {
	        "read_cost": "0.00",
	        "eval_cost": "0.10",
	        "prefix_cost": "0.00",
	        "data_read_per_join": "408"
	      },
	      "used_columns": [
	        "id",
	        "name"
	      ]
	    }
	  }
	}
	1 row in set (0.00 sec)
	```
	This works with any explainable statement ([`SELECT`](select.md), [`TABLE`](table.md), [`INSERT`](insert.md), [`UPDATE`](update.md), [`REPLACE`](replace.md), or [`DELETE`](delete.md)). Examples using `UPDATE` and `DELETE` statements are shown here:
	```
	mysql> EXPLAIN FORMAT=JSON INTO @myupdate 
	    ->   UPDATE a SET name2 = "garcia" WHERE id = 3;              
	Query OK, 0 rows affected (0.00 sec)
	mysql> EXPLAIN FORMAT=JSON INTO @mydelete 
	    ->     DELETE FROM a WHERE name1 LIKE '%e%';
	Query OK, 0 rows affected (0.00 sec)
	mysql> SELECT @myupdate, @mydelete\G
	*************************** 1. row ***************************
	@myupdate: {
	  "query_block": {
	    "select_id": 1,
	    "table": {
	      "update": true,
	      "table_name": "a",
	      "access_type": "range",
	      "possible_keys": [
	        "PRIMARY"
	      ],
	      "key": "PRIMARY",
	      "used_key_parts": [
	        "id"
	      ],
	      "key_length": "4",
	      "ref": [
	        "const"
	      ],
	      "rows_examined_per_scan": 1,
	      "filtered": "100.00",
	      "attached_condition": "(\`db\`.\`a\`.\`id\` = 3)"
	    }
	  }
	}
	@mydelete: {
	  "query_block": {
	    "select_id": 1,
	    "table": {
	      "delete": true,
	      "table_name": "a",
	      "access_type": "ALL",
	      "rows_examined_per_scan": 2,
	      "filtered": "100.00",
	      "attached_condition": "(\`db\`.\`a\`.\`name1\` like '%e%')"
	    }
	  }
	}
	1 row in set (0.00 sec)
	```
	You can work with this value using MySQL JSON functions as you would with any other JSON value, as in these examples using [`JSON_EXTRACT()`](json-search-functions.md):
	```
	mysql> SELECT JSON_EXTRACT(@myselect, "$.query_block.table.key");
	+----------------------------------------------------+
	| JSON_EXTRACT(@myselect, "$.query_block.table.key") |
	+----------------------------------------------------+
	| "PRIMARY"                                          |
	+----------------------------------------------------+
	1 row in set (0.01 sec)
	mysql> SELECT JSON_EXTRACT(@myupdate, "$.query_block.table.access_type") AS U_acc,
	    ->        JSON_EXTRACT(@mydelete, "$.query_block.table.access_type") AS D_acc;
	+---------+-------+
	| U_acc   | D_acc |
	+---------+-------+
	| "range" | "ALL" |
	+---------+-------+
	1 row in set (0.00 sec)
	```
	For complex statements, the JSON output can be quite large; in particular, it can be difficult when reading it to pair the closing bracket and opening brackets; to cause the JSON structure's key, if it has one, to be repeated near the closing bracket, set [`end_markers_in_json=ON`](server-system-variables.md). You should be aware that while this makes the output easier to read, it also renders the JSON invalid, causing JSON functions to raise an error.
	See also [Section 14.17, “JSON Functions”](json-functions.md).
	Trying to use an `INTO` clause without explicitly including `FORMAT=JSON` causes `EXPLAIN` to be rejected with [`ER_EXPLAIN_INTO_IMPLICIT_FORMAT_NOT_SUPPORTED`](https://docs.oracle.com/cd/E17952_01/mysql-errors-8.4-en/server-error-reference.html#error_er_explain_into_implicit_format_not_supported). This is true regardless of the current value of the [`explain_format`](server-system-variables.md) system variable.
	The `INTO` clause is not supported with `FOR CONNECTION`.
	`INTO` is also not supported with `EXPLAIN ANALYZE` when [`explain_json_format_version=1`](server-system-variables.md).
	Important
	If, for any reason, the statement to be analyzed is rejected, the user variable is not updated.
- MySQL 8.4 supports a `FOR             SCHEMA` clause, which causes `EXPLAIN` to behave as if the statement to be analyzed had been executed in the named database; `FOR DATABASE` is supported as a synonym. A simple example of use is shown here:
	```
	mysql> USE b;
	Database changed
	mysql> CREATE SCHEMA s1;
	Query OK, 1 row affected (0.01 sec)
	mysql> CREATE SCHEMA s2;
	Query OK, 1 row affected (0.01 sec)
	mysql> USE s1;
	Database changed
	mysql> CREATE TABLE t (c1 INT NOT NULL AUTO_INCREMENT PRIMARY KEY, c2 INT NOT NULL);
	Query OK, 0 rows affected (0.04 sec)
	mysql> USE s2;
	Database changed
	mysql> CREATE TABLE t (c1 INT NOT NULL AUTO_INCREMENT PRIMARY KEY, c2 INT NOT NULL, KEY i1 (c2));
	Query OK, 0 rows affected (0.04 sec)
	mysql> USE b;
	Database changed
	mysql> EXPLAIN FORMAT=TREE FOR SCHEMA s1 SELECT * FROM t WHERE c2 > 50\G
	*************************** 1. row ***************************
	EXPLAIN: -> Filter: (t.c2 > 50)  (cost=0.35 rows=1)
	    -> Table scan on t  (cost=0.35 rows=1)
	1 row in set (0.00 sec)
	mysql> EXPLAIN FORMAT=TREE FOR SCHEMA s2 SELECT * FROM t WHERE c2 > 50\G
	*************************** 1. row ***************************
	EXPLAIN: -> Filter: (t.c2 > 50)  (cost=0.35 rows=1)
	    -> Covering index scan on t using i1  (cost=0.35 rows=1)
	1 row in set (0.00 sec)
	```
	If the database does not exist, the statement is rejected with [`ER_BAD_DB_ERROR`](https://docs.oracle.com/cd/E17952_01/mysql-errors-8.4-en/server-error-reference.html#error_er_bad_db_error). If the user does not have the necessary privileges to run the statement, it is rejected with [`ER_DBACCESS_DENIED_ERROR`](https://docs.oracle.com/cd/E17952_01/mysql-errors-8.4-en/server-error-reference.html#error_er_dbaccess_denied_error).
	`FOR SCHEMA` is not compatible with `FOR CONNECTION`.

`EXPLAIN` requires the same privileges required to execute the explained statement. Additionally, `EXPLAIN` also requires the [`SHOW VIEW`](privileges-provided.md) privilege for any explained view. `EXPLAIN ... FOR         CONNECTION` also requires the [`PROCESS`](privileges-provided.md) privilege if the specified connection belongs to a different user.

The [`explain_format`](server-system-variables.md) system variable determines the format of the output from `EXPLAIN` when used to display a query execution plan. This variable can take any of the values used with the `FORMAT` option, with the addition of `DEFAULT` as a synonym for `TRADITIONAL`. The following example uses the `country` table from the `world` database which can be obtained from [MySQL: Other Downloads](https://dev.mysql.com/doc/index-other.html):

```
mysql> USE world; # Make world the current database
Database changed
```

Checking the value of `explain_format`, we see that it has the default value, and that `EXPLAIN` (with no `FORMAT` option) therefore uses the traditional tabular output:

```
mysql> SELECT @@explain_format;
+------------------+
| @@explain_format |
+------------------+
| TRADITIONAL      |
+------------------+
1 row in set (0.00 sec)

mysql> EXPLAIN SELECT Name FROM country WHERE Code Like 'A%';
+----+-------------+---------+------------+-------+---------------+---------+---------+------+------+----------+-------------+
| id | select_type | table   | partitions | type  | possible_keys | key     | key_len | ref  | rows | filtered | Extra       |
+----+-------------+---------+------------+-------+---------------+---------+---------+------+------+----------+-------------+
|  1 | SIMPLE      | country | NULL       | range | PRIMARY       | PRIMARY | 12      | NULL |   17 |   100.00 | Using where |
+----+-------------+---------+------------+-------+---------------+---------+---------+------+------+----------+-------------+
1 row in set, 1 warning (0.00 sec)
```

If we set the value of `explain_format` to `TREE`, then rerun the same `EXPLAIN` statement, the output uses the tree-like format:

```
mysql> SET @@explain_format=TREE;
Query OK, 0 rows affected (0.00 sec)

mysql> SELECT @@explain_format;
+------------------+
| @@explain_format |
+------------------+
| TREE             |
+------------------+
1 row in set (0.00 sec)

mysql> EXPLAIN SELECT Name FROM country WHERE Code LIKE 'A%';
+--------------------------------------------------------------------------------------------------------------+
| EXPLAIN                                                                                                      |
+--------------------------------------------------------------------------------------------------------------+
| -> Filter: (country.\`Code\` like 'A%')  (cost=3.67 rows=17)
    -> Index range scan on country using PRIMARY over ('A' <= Code <= 'A????????')  (cost=3.67 rows=17)  |
+--------------------------------------------------------------------------------------------------------------+
1 row in set, 1 warning (0.00 sec)
```

As stated previously, the `FORMAT` option overrides this setting. Executing the same `EXPLAIN` statement using `FORMAT=JSON` instead of `FORMAT=TREE` shows that this is the case:

```
mysql> EXPLAIN FORMAT=JSON SELECT Name FROM country WHERE Code LIKE 'A%';
+------------------------------------------------------------------------------+
| EXPLAIN                                                                      |
+------------------------------------------------------------------------------+
| {
  "query_block": {
    "select_id": 1,
    "cost_info": {
      "query_cost": "3.67"
    },
    "table": {
      "table_name": "country",
      "access_type": "range",
      "possible_keys": [
        "PRIMARY"
      ],
      "key": "PRIMARY",
      "used_key_parts": [
        "Code"
      ],
      "key_length": "12",
      "rows_examined_per_scan": 17,
      "rows_produced_per_join": 17,
      "filtered": "100.00",
      "cost_info": {
        "read_cost": "1.97",
        "eval_cost": "1.70",
        "prefix_cost": "3.67",
        "data_read_per_join": "16K"
      },
      "used_columns": [
        "Code",
        "Name"
      ],
      "attached_condition": "(\`world\`.\`country\`.\`Code\` like 'A%')"
    }
  }
}                                                                              |
+------------------------------------------------------------------------------+
1 row in set, 1 warning (0.00 sec)
```

To return the default output of `EXPLAIN` to the tabular format, set `explain_format` to `TRADITIONAL`. Alternatively, you can set it to `DEFAULT`, which has the same effect, as shown here:

```
mysql> SET @@explain_format=DEFAULT;
Query OK, 0 rows affected (0.00 sec)

mysql> SELECT @@explain_format;
+------------------+
| @@explain_format |
+------------------+
| TRADITIONAL      |
+------------------+
1 row in set (0.00 sec)
```

MySQL 8.4 supports two versions of the JSON output format. Version 1 is the linear format always used in MySQL 8.2 and earlier; this remains the default in MySQL 8.4, and is used in the examples already shown in this section. Version 2 of the JSON output format is based on access paths, and is intended to provide compatibility with future versions of the MySQL Optimizer. You can switch to the Version 2 format by setting the value of the [`explain_json_format_version`](server-system-variables.md) server system variable to `2`, as shown here for the same `EXPLAIN` statement used in the previous example:

```
mysql> SELECT @@explain_json_format_version;
+-------------------------------+
| @@explain_json_format_version |
+-------------------------------+
|                             1 |
+-------------------------------+
1 row in set (0.00 sec)

mysql> SET @@explain_json_format_version = 2;
Query OK, 0 rows affected (0.00 sec)

mysql> SELECT @@explain_json_format_version;
+-------------------------------+
| @@explain_json_format_version |
+-------------------------------+
|                             2 |
+-------------------------------+
1 row in set (0.00 sec)

mysql> EXPLAIN FORMAT=JSON SELECT Name FROM country WHERE Code LIKE 'A%';
+------------------------------------------------------------------------------+
| EXPLAIN                                                                      |
+------------------------------------------------------------------------------+
| {
  "query": "/* select#1 */ select \`world\`.\`country\`.\`Name\` AS \`Name\` from \`world\`.\`country\` where (\`world\`.\`country\`.\`Code\` like 'A%')",
  "inputs": [
    {
      "ranges": [
        "('A' <= Code <= 'A????????')"
      ],
      "covering": false,
      "operation": "Index range scan on country using PRIMARY over ('A' <= Code < 'A????????')",
      "index_name": "PRIMARY",
      "table_name": "country",
      "access_type": "index",
      "estimated_rows": 17.0,
      "index_access_type": "index_range_scan",
      "estimated_total_cost": 3.668778400708174
    }
  ],
  "condition": "(country.\`Code\` like 'A%')",
  "operation": "Filter: (country.\`Code\` like 'A%')",
  "access_type": "filter",
  "estimated_rows": 17.0,
  "estimated_total_cost": 3.668778400708174
}                                                                              |
+------------------------------------------------------------------------------+
```

After using the Version 2 format, you can cause the JSON output from all subsequent `EXPLAIN FORMAT=JSON` statements to revert to the Version 1 format by setting `explain_json_format_version` back to `1` (the default).

The value of `explain_json_format_version` determines the version of the JSON output format employed by all `EXPLAIN` statements which use it, whether the JSON format is used because a given `EXPLAIN` statement includes an explicit `FORMAT=JSON` option, or because the JSON format is used automatically due to the [`explain_format`](server-system-variables.md) system variable being set to `JSON`.

With the help of `EXPLAIN`, you can see where you should add indexes to tables so that the statement executes faster by using indexes to find rows. You can also use `EXPLAIN` to check whether the optimizer joins the tables in an optimal order. To give a hint to the optimizer to use a join order corresponding to the order in which the tables are named in a [`SELECT`](select.md) statement, begin the statement with `SELECT STRAIGHT_JOIN` rather than just [`SELECT`](select.md). (See [Section 15.2.13, “SELECT Statement”](select.md).)

The optimizer trace may sometimes provide information complementary to that of `EXPLAIN`. However, the optimizer trace format and content are subject to change between versions. For details, see [Section 10.15, “Tracing the Optimizer”](optimizer-tracing.md).

If you have a problem with indexes not being used when you believe that they should be, run [`ANALYZE         TABLE`](analyze-table.md) to update table statistics, such as cardinality of keys, that can affect the choices the optimizer makes. See [Section 15.7.3.1, “ANALYZE TABLE Statement”](analyze-table.md).

Note

MySQL Workbench has a Visual Explain capability that provides a visual representation of `EXPLAIN` output. See [Tutorial: Using Explain to Improve Query Performance](https://docs.oracle.com/cd/E17952_01/workbench-en/wb-tutorial-visual-explain-dbt3.html).

#### Obtaining Information with EXPLAIN ANALYZE

`EXPLAIN ANALYZE` runs a statement and produces `EXPLAIN` output along with timing and additional, iterator-based, information about how the optimizer's expectations matched the actual execution. For each iterator, the following information is provided:

- Estimated execution cost
	(Some iterators are not accounted for by the cost model, and so are not included in the estimate.)
- Estimated number of returned rows
- Time to return first row
- Time spent executing this iterator (including child iterators, but not parent iterators), in milliseconds.
	(When there are multiple loops, this figure shows the average time per loop.)
- Number of rows returned by the iterator
- Number of loops

The query execution information is displayed using the `TREE` output format, in which nodes represent iterators. `EXPLAIN ANALYZE` always uses the `TREE` output format. This can optionally be specified explicitly using `FORMAT=TREE`; formats other than `TREE` remain unsupported.

`EXPLAIN ANALYZE` can be used with [`SELECT`](select.md) statements, multi-table [`UPDATE`](update.md) and [`DELETE`](delete.md) statements, and [`TABLE`](table.md) statements.

You can terminate this statement using [`KILL QUERY`](kill.md) or **CTRL-C**.

`EXPLAIN ANALYZE` cannot be used with `FOR CONNECTION`.

Example output:

```
mysql> EXPLAIN ANALYZE SELECT * FROM t1 JOIN t2 ON (t1.c1 = t2.c2)\G
*************************** 1. row ***************************
EXPLAIN: -> Inner hash join (t2.c2 = t1.c1)  (cost=3.5 rows=5) 
(actual time=0.121..0.131 rows=1 loops=1) 
    -> Table scan on t2  (cost=0.07 rows=5) 
(actual time=0.0126..0.0221 rows=5 loops=1) 
    -> Hash
        -> Table scan on t1  (cost=0.75 rows=5) 
(actual time=0.0372..0.0534 rows=5 loops=1)

mysql> EXPLAIN ANALYZE SELECT * FROM t3 WHERE i > 8\G
*************************** 1. row ***************************
EXPLAIN: -> Filter: (t3.i > 8)  (cost=0.75 rows=1.67) 
(actual time=0.0168..0.0182 rows=1 loops=1)
    -> Table scan on t3  (cost=0.75 rows=5) 
(actual time=0.015..0.0167 rows=5 loops=1)

mysql> EXPLAIN ANALYZE FORMAT=TREE SELECT * FROM t3 WHERE pk > 17\G
*************************** 1. row ***************************
EXPLAIN: -> Filter: (t3.pk > 17)  (cost=0.91 rows=2) 
(actual time=0.0334..0.042 rows=2 loops=1)
    -> Index range scan on t3 using PRIMARY over (17 < pk)  
(cost=0.91 rows=2) (actual time=0.0306..0.0384 rows=2 loops=1)
```

The tables used in the example output were created by the statements shown here:

```
CREATE TABLE t1 (
    c1 INTEGER DEFAULT NULL,
    c2 INTEGER DEFAULT NULL
);

CREATE TABLE t2 (
    c1 INTEGER DEFAULT NULL,
    c2 INTEGER DEFAULT NULL
);

CREATE TABLE t3 (
    pk INTEGER NOT NULL PRIMARY KEY,
    i INTEGER DEFAULT NULL
);
```

Values shown for `actual time` in the output of this statement are expressed in milliseconds.

[`explain_format`](server-system-variables.md) has the following effects on `EXPLAIN ANALYZE`:

- If the value of this variable is `TRADITIONAL` or `TREE` (or the synonym `DEFAULT`), `EXPLAIN ANALYZE` uses the `TREE` format. This ensures that this statement continues to use the `TREE` format by default, as it did prior to the introduction of `explain_format`.
- If the value of `explain_format` is `JSON`, `EXPLAIN ANALYZE` returns an error unless `FORMAT=TREE` is specified as part of the statement. This is due to the fact that `EXPLAIN ANALYZE` supports only the `TREE` output format.

We illustrate the behavior described in the second point here, re-using the last `EXPLAIN ANALYZE` statement from the previous example:

```
mysql> SET @@explain_format=JSON;
Query OK, 0 rows affected (0.00 sec)

mysql> SELECT @@explain_format;
+------------------+
| @@explain_format |
+------------------+
| JSON             |
+------------------+
1 row in set (0.00 sec)

mysql> EXPLAIN ANALYZE SELECT * FROM t3 WHERE pk > 17\G
ERROR 1235 (42000): This version of MySQL doesn't yet support 'EXPLAIN ANALYZE with JSON format'

mysql> EXPLAIN ANALYZE FORMAT=TRADITIONAL SELECT * FROM t3 WHERE pk > 17\G
ERROR 1235 (42000): This version of MySQL doesn't yet support 'EXPLAIN ANALYZE with TRADITIONAL format'

mysql> EXPLAIN ANALYZE FORMAT=TREE SELECT * FROM t3 WHERE pk > 17\G
*************************** 1. row ***************************
EXPLAIN: -> Filter: (t3.pk > 17)  (cost=1.26 rows=5)
(actual time=0.013..0.016 rows=5 loops=1)
    -> Index range scan on t3 using PRIMARY  (cost=1.26 rows=5)
(actual time=0.012..0.014 rows=5 loops=1)
```

Using `FORMAT=TRADITIONAL` or `FORMAT=JSON` with `EXPLAIN         ANALYZE` always raises an error, regardless of the value of `explain_format`.

In MySQL 8.4, numbers in the output of `EXPLAIN ANALYZE` and `EXPLAIN         FORMAT=TREE` are formatted according to the following rules:

- Numbers in the range 0.001-999999.5 are printed as decimal numbers.
	Decimal numbers less than 1000 have three significant digits; the remainder have four, five, or six.
- Numbers outside the range 0.001-999999.5 are printed in engineering format. Examples of such values are `1.23e+9` and `934e-6`.
- No trailing zeros are printed. For example, we print `2.3` rather than `2.30`, and `1.2e+6` rather than `1.20e+6`.
- Numbers less than `1e-12` are printed as `0`.