---
title: "1.6.1 MySQL Extensions to Standard SQL"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/extensions-to-ansi.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 1.6.1 MySQL Extensions to Standard SQL

MySQL Server supports some extensions that you are not likely to find in other SQL DBMSs. Be warned that if you use them, your code is most likely not portable to other SQL servers. In some cases, you can write code that includes MySQL extensions, but is still portable, by using comments of the following form:

```
/*! MySQL-specific code */
```

In this case, MySQL Server parses and executes the code within the comment as it would any other SQL statement, but other SQL servers should ignore the extensions. For example, MySQL Server recognizes the `STRAIGHT_JOIN` keyword in the following statement, but other servers should not:

```
SELECT /*! STRAIGHT_JOIN */ col1 FROM table1,table2 WHERE ...
```

If you add a version number after the `!` character, the syntax within the comment is executed only if the MySQL version is greater than or equal to the specified version number. The `KEY_BLOCK_SIZE` clause in the following comment is executed only by servers from MySQL 5.1.10 or higher:

```
CREATE TABLE t1(a INT, KEY (a)) /*!50110 KEY_BLOCK_SIZE=1024 */;
```

The following descriptions list MySQL extensions, organized by category.

- Organization of data on disk
	MySQL Server maps each database to a directory under the MySQL data directory, and maps tables within a database to file names in the database directory. Consequently, database and table names are case-sensitive in MySQL Server on operating systems that have case-sensitive file names (such as most Unix systems). See [Section 11.2.3, “Identifier Case Sensitivity”](identifier-case-sensitivity.md).
- General language syntax
	- By default, strings can be enclosed by `"` as well as `'`. If the [`ANSI_QUOTES`](sql-mode.md) SQL mode is enabled, strings can be enclosed only by `'` and the server interprets strings enclosed by `"` as identifiers.
	- `\` is the escape character in strings.
	- In SQL statements, you can access tables from different databases with the *`db_name.tbl_name`* syntax. Some SQL servers provide the same functionality but call this `User space`. MySQL Server doesn't support tablespaces such as used in statements like this: `CREATE TABLE ralph.my_table ... IN                 my_tablespace`.
- SQL statement syntax
	- The [`ANALYZE TABLE`](analyze-table.md), [`CHECK TABLE`](check-table.md), [`OPTIMIZE TABLE`](optimize-table.md), and [`REPAIR TABLE`](repair-table.md) statements.
	- The [`CREATE DATABASE`](create-database.md), [`DROP DATABASE`](drop-database.md), and [`ALTER DATABASE`](alter-database.md) statements. See [Section 15.1.12, “CREATE DATABASE Statement”](create-database.md), [Section 15.1.24, “DROP DATABASE Statement”](drop-database.md), and [Section 15.1.2, “ALTER DATABASE Statement”](alter-database.md).
	- The [`DO`](do.md) statement.
	- [`EXPLAIN                 SELECT`](explain.md) to obtain a description of how tables are processed by the query optimizer.
	- The [`FLUSH`](flush.md) and [`RESET`](reset.md) statements.
	- The [`SET`](set-variable.md) statement. See [Section 15.7.6.1, “SET Syntax for Variable Assignment”](set-variable.md).
	- The [`SHOW`](show.md) statement. See [Section 15.7.7, “SHOW Statements”](show.md). The information produced by many of the MySQL-specific [`SHOW`](show.md) statements can be obtained in more standard fashion by using [`SELECT`](select.md) to query `INFORMATION_SCHEMA`. See [Chapter 28, *INFORMATION\_SCHEMA Tables*](information-schema.md).
	- Use of [`LOAD DATA`](load-data.md). In many cases, this syntax is compatible with Oracle [`LOAD DATA`](load-data.md). See [Section 15.2.9, “LOAD DATA Statement”](load-data.md).
	- Use of [`RENAME TABLE`](rename-table.md). See [Section 15.1.36, “RENAME TABLE Statement”](rename-table.md).
	- Use of [`REPLACE`](replace.md) instead of [`DELETE`](delete.md) plus [`INSERT`](insert.md). See [Section 15.2.12, “REPLACE Statement”](replace.md).
	- Use of ``CHANGE                 *`col_name`*``, ``DROP                 *`col_name`*``, or [`DROP INDEX`](drop-index.md), `IGNORE` or `RENAME` in [`ALTER TABLE`](alter-table.md) statements. Use of multiple `ADD`, `ALTER`, `DROP`, or `CHANGE` clauses in an [`ALTER TABLE`](alter-table.md) statement. See [Section 15.1.9, “ALTER TABLE Statement”](alter-table.md).
	- Use of index names, indexes on a prefix of a column, and use of `INDEX` or `KEY` in [`CREATE                 TABLE`](create-table.md) statements. See [Section 15.1.20, “CREATE TABLE Statement”](create-table.md).
	- Use of `TEMPORARY` or `IF NOT                 EXISTS` with [`CREATE                 TABLE`](create-table.md).
	- Use of `IF EXISTS` with [`DROP TABLE`](drop-table.md) and [`DROP DATABASE`](drop-database.md).
	- The capability of dropping multiple tables with a single [`DROP TABLE`](drop-table.md) statement.
	- The `ORDER BY` and `LIMIT` clauses of the [`UPDATE`](update.md) and [`DELETE`](delete.md) statements.
	- ``INSERT INTO *`tbl_name`*                 SET *`col_name`* = ...`` syntax.
	- The `DELAYED` clause of the [`INSERT`](insert.md) and [`REPLACE`](replace.md) statements.
	- The `LOW_PRIORITY` clause of the [`INSERT`](insert.md), [`REPLACE`](replace.md), [`DELETE`](delete.md), and [`UPDATE`](update.md) statements.
	- Use of `INTO OUTFILE` or `INTO                 DUMPFILE` in [`SELECT`](select.md) statements. See [Section 15.2.13, “SELECT Statement”](select.md).
	- Options such as `STRAIGHT_JOIN` or `SQL_SMALL_RESULT` in [`SELECT`](select.md) statements.
	- You don't need to name all selected columns in the `GROUP BY` clause. This gives better performance for some very specific, but quite normal queries. See [Section 14.19, “Aggregate Functions”](aggregate-functions-and-modifiers.md).
	- You can specify `ASC` and `DESC` with `GROUP                 BY`, not just with `ORDER BY`.
	- The ability to set variables in a statement with the `:=` assignment operator. See [Section 11.4, “User-Defined Variables”](user-variables.md).
- Data types
- Functions and operators
	- To make it easier for users who migrate from other SQL environments, MySQL Server supports aliases for many functions. For example, all string functions support both standard SQL syntax and ODBC syntax.
	- MySQL Server understands the [`||`](logical-operators.md) and [`&&`](logical-operators.md) operators to mean logical OR and AND, as in the C programming language. In MySQL Server, [`||`](logical-operators.md) and [`OR`](logical-operators.md) are synonyms, as are [`&&`](logical-operators.md) and [`AND`](logical-operators.md). Because of this nice syntax, MySQL Server doesn't support the standard SQL [`||`](logical-operators.md) operator for string concatenation; use [`CONCAT()`](string-functions.md) instead. Because [`CONCAT()`](string-functions.md) takes any number of arguments, it is easy to convert use of the [`||`](logical-operators.md) operator to MySQL Server.
	- Use of [``COUNT(DISTINCT                 *`value_list`*)``](aggregate-functions.md) where *`value_list`* has more than one element.
	- String comparisons are case-insensitive by default, with sort ordering determined by the collation of the current character set, which is `utf8mb4` by default. To perform case-sensitive comparisons instead, you should declare your columns with the `BINARY` attribute or use the `BINARY` cast, which causes comparisons to be done using the underlying character code values rather than a lexical ordering.
	- The [`%`](mathematical-functions.md) operator is a synonym for [`MOD()`](mathematical-functions.md). That is, ``*`N`* %                 *`M`*`` is equivalent to [``MOD(*`N`*,*`M`*)``](mathematical-functions.md). [`%`](mathematical-functions.md) is supported for C programmers and for compatibility with PostgreSQL.
	- The [`=`](comparison-operators.md), [`<>`](comparison-operators.md), [`<=`](comparison-operators.md), [`<`](comparison-operators.md), [`>=`](comparison-operators.md), [`>`](comparison-operators.md), [`<<`](bit-functions.md), [`>>`](bit-functions.md), [`<=>`](comparison-operators.md), [`AND`](logical-operators.md), [`OR`](logical-operators.md), or [`LIKE`](string-comparison-functions.md) operators may be used in expressions in the output column list (to the left of the `FROM`) in [`SELECT`](select.md) statements. For example:
		```
		mysql> SELECT col1=1 AND col2=2 FROM my_table;
		```
	- The [`LAST_INSERT_ID()`](information-functions.md) function returns the most recent `AUTO_INCREMENT` value. See [Section 14.15, “Information Functions”](information-functions.md).
	- [`LIKE`](string-comparison-functions.md) is permitted on numeric values.
	- The [`REGEXP`](regexp.md) and [`NOT REGEXP`](regexp.md) extended regular expression operators.
	- [`CONCAT()`](string-functions.md) or [`CHAR()`](string-functions.md) with one argument or more than two arguments. (In MySQL Server, these functions can take a variable number of arguments.)
	- The [`BIT_COUNT()`](bit-functions.md), [`CASE`](flow-control-functions.md), [`ELT()`](string-functions.md), [`FROM_DAYS()`](date-and-time-functions.md), [`FORMAT()`](string-functions.md), [`IF()`](flow-control-functions.md), [`MD5()`](encryption-functions.md), [`PERIOD_ADD()`](date-and-time-functions.md), [`PERIOD_DIFF()`](date-and-time-functions.md), [`TO_DAYS()`](date-and-time-functions.md), and [`WEEKDAY()`](date-and-time-functions.md) functions.
	- Use of [`TRIM()`](string-functions.md) to trim substrings. Standard SQL supports removal of single characters only.
	- The `GROUP BY` functions [`STD()`](aggregate-functions.md), [`BIT_OR()`](aggregate-functions.md), [`BIT_AND()`](aggregate-functions.md), [`BIT_XOR()`](aggregate-functions.md), and [`GROUP_CONCAT()`](aggregate-functions.md). See [Section 14.19, “Aggregate Functions”](aggregate-functions-and-modifiers.md).