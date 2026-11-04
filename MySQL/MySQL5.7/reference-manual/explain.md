---
title: "13.8.2 EXPLAIN Statement"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/explain.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 13.8.2 EXPLAIN Statement

```
{EXPLAIN | DESCRIBE | DESC}
    tbl_name [col_name | wild]

{EXPLAIN | DESCRIBE | DESC}
    [explain_type]
    {explainable_stmt | FOR CONNECTION connection_id}

explain_type: {
    EXTENDED
  | PARTITIONS
  | FORMAT = format_name
}

format_name: {
    TRADITIONAL
  | JSON
}

explainable_stmt: {
    SELECT statement
  | DELETE statement
  | INSERT statement
  | REPLACE statement
  | UPDATE statement
}
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

[`DESCRIBE`](describe.md) is a shortcut for [`SHOW COLUMNS`](show-columns.md). These statements also display information for views. The description for [`SHOW COLUMNS`](show-columns.md) provides more information about the output columns. See [Section 13.7.5.5, “SHOW COLUMNS Statement”](show-columns.md).

By default, [`DESCRIBE`](describe.md) displays information about all columns in the table. *`col_name`*, if given, is the name of a column in the table. In this case, the statement displays information only for the named column. *`wild`*, if given, is a pattern string. It can contain the SQL `%` and `_` wildcard characters. In this case, the statement displays output only for the columns with names matching the string. There is no need to enclose the string within quotation marks unless it contains spaces or other special characters.

The [`DESCRIBE`](describe.md) statement is provided for compatibility with Oracle.

The [`SHOW CREATE TABLE`](show-create-table.md), [`SHOW TABLE STATUS`](show-table-status.md), and [`SHOW INDEX`](show-index.md) statements also provide information about tables. See [Section 13.7.5, “SHOW Statements”](show.md).

#### Obtaining Execution Plan Information

The `EXPLAIN` statement provides information about how MySQL executes statements:

- `EXPLAIN` works with [`SELECT`](select.md), [`DELETE`](delete.md), [`INSERT`](insert.md), [`REPLACE`](replace.md), and [`UPDATE`](update.md) statements.
- When `EXPLAIN` is used with an explainable statement, MySQL displays information from the optimizer about the statement execution plan. That is, MySQL explains how it would process the statement, including information about how tables are joined and in which order. For information about using `EXPLAIN` to obtain execution plan information, see [Section 8.8.2, “EXPLAIN Output Format”](explain-output.md).
- When `EXPLAIN` is used with ``FOR CONNECTION             *`connection_id`*`` rather than an explainable statement, it displays the execution plan for the statement executing in the named connection. See [Section 8.8.4, “Obtaining Execution Plan Information for a Named Connection”](explain-for-connection.md).
- For [`SELECT`](select.md) statements, `EXPLAIN` produces additional execution plan information that can be displayed using [`SHOW WARNINGS`](show-warnings.md). See [Section 8.8.3, “Extended EXPLAIN Output Format”](explain-extended.md).
	Note
	In older MySQL releases, extended information was produced using `EXPLAIN               EXTENDED`. That syntax is still recognized for backward compatibility but extended output is now enabled by default, so the `EXTENDED` keyword is superfluous and deprecated. Its use results in a warning, and it is removed from `EXPLAIN` syntax in MySQL 8.0.
- `EXPLAIN` is useful for examining queries involving partitioned tables. See [Section 22.3.5, “Obtaining Information About Partitions”](partitioning-info.md).
	Note
	In older MySQL releases, partition information was produced using `EXPLAIN               PARTITIONS`. That syntax is still recognized for backward compatibility but partition output is now enabled by default, so the `PARTITIONS` keyword is superfluous and deprecated. Its use results in a warning, and it is removed from `EXPLAIN` syntax in MySQL 8.0.
- The `FORMAT` option can be used to select the output format. `TRADITIONAL` presents the output in tabular format. This is the default if no `FORMAT` option is present. `JSON` format displays the information in JSON format.
	For complex statements, the JSON output can be quite large; in particular, it can be difficult when reading it to pair the closing bracket and opening brackets; to cause the JSON structure's key, if it has one, to be repeated near the closing bracket, set [`end_markers_in_json=ON`](server-system-variables.md). You should be aware that while this makes the output easier to read, it also renders the JSON invalid, causing JSON functions to raise an error.

`EXPLAIN` requires the same privileges required to execute the explained statement. Additionally, `EXPLAIN` also requires the [`SHOW VIEW`](privileges-provided.md) privilege for any explained view.

With the help of `EXPLAIN`, you can see where you should add indexes to tables so that the statement executes faster by using indexes to find rows. You can also use `EXPLAIN` to check whether the optimizer joins the tables in an optimal order. To give a hint to the optimizer to use a join order corresponding to the order in which the tables are named in a [`SELECT`](select.md) statement, begin the statement with `SELECT STRAIGHT_JOIN` rather than just [`SELECT`](select.md). (See [Section 13.2.9, “SELECT Statement”](select.md).)

The optimizer trace may sometimes provide information complementary to that of `EXPLAIN`. However, the optimizer trace format and content are subject to change between versions. For details, see [Section 8.15, “Tracing the Optimizer”](optimizer-tracing.md).

If you have a problem with indexes not being used when you believe that they should be, run [`ANALYZE         TABLE`](analyze-table.md) to update table statistics, such as cardinality of keys, that can affect the choices the optimizer makes. See [Section 13.7.2.1, “ANALYZE TABLE Statement”](analyze-table.md).

Note

MySQL Workbench has a Visual Explain capability that provides a visual representation of `EXPLAIN` output. See [Tutorial: Using Explain to Improve Query Performance](https://docs.oracle.com/cd/E17952_01/workbench-en/wb-tutorial-visual-explain-dbt3.html).