---
title: "Chapter 12 Functions and Operators"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/functions.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

Expressions can be used at several points in [SQL](glossary.md) statements, such as in the `ORDER BY` or `HAVING` clauses of [`SELECT`](select.md) statements, in the `WHERE` clause of a [`SELECT`](select.md), [`DELETE`](delete.md), or [`UPDATE`](update.md) statement, or in [`SET`](set-variable.md) statements. Expressions can be written using values from several sources, such as literal values, column values, `NULL`, variables, built-in functions and operators, loadable functions, and stored functions (a type of stored object).

This chapter describes the built-in functions and operators that are permitted for writing expressions in MySQL. For information about loadable functions and stored functions, see [Section 5.6, “MySQL Server Loadable Functions”](server-loadable-functions.md), and [Section 23.2, “Using Stored Routines”](stored-routines.md). For the rules describing how the server interprets references to different kinds of functions, see [Section 9.2.5, “Function Name Parsing and Resolution”](function-resolution.md).

An expression that contains `NULL` always produces a `NULL` value unless otherwise indicated in the documentation for a particular function or operator.

Note

By default, there must be no whitespace between a function name and the parenthesis following it. This helps the MySQL parser distinguish between function calls and references to tables or columns that happen to have the same name as a function. However, spaces around function arguments are permitted.

To tell the MySQL server to accept spaces after function names by starting it with the [`--sql-mode=IGNORE_SPACE`](server-options.md) option. (See [Section 5.1.10, “Server SQL Modes”](sql-mode.md).) Individual client programs can request this behavior by using the `CLIENT_IGNORE_SPACE` option for [`mysql_real_connect()`](https://docs.oracle.com/cd/E17952_01/c-api-5.7-en/mysql-real-connect.html). In either case, all function names become reserved words.

For the sake of brevity, some examples in this chapter display the output from the [**mysql**](mysql.md) program in abbreviated form. Rather than showing examples in this format:

```
mysql> SELECT MOD(29,9);
+-----------+
| mod(29,9) |
+-----------+
|         2 |
+-----------+
1 rows in set (0.00 sec)
```

This format is used instead:

```
mysql> SELECT MOD(29,9);
        -> 2
```