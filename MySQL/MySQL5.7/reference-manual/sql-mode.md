---
title: "5.1.10 Server SQL Modes"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/sql-mode.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 5.1.10 Server SQL Modes

The MySQL server can operate in different SQL modes, and can apply these modes differently for different clients, depending on the value of the [`sql_mode`](server-system-variables.md) system variable. DBAs can set the global SQL mode to match site server operating requirements, and each application can set its session SQL mode to its own requirements.

Modes affect the SQL syntax MySQL supports and the data validation checks it performs. This makes it easier to use MySQL in different environments and to use MySQL together with other database servers.

For answers to questions often asked about server SQL modes in MySQL, see [Section A.3, “MySQL 5.7 FAQ: Server SQL Mode”](faqs-sql-modes.md).

When working with `InnoDB` tables, consider also the [`innodb_strict_mode`](innodb-parameters.md) system variable. It enables additional error checks for `InnoDB` tables.

#### Setting the SQL Mode

The default SQL mode in MySQL 5.7 includes these modes: `ONLY_FULL_GROUP_BY`, `STRICT_TRANS_TABLES`, `NO_ZERO_IN_DATE`, `NO_ZERO_DATE`, `ERROR_FOR_DIVISION_BY_ZERO`, `NO_AUTO_CREATE_USER`, and `NO_ENGINE_SUBSTITUTION`.

These modes were added to the default SQL mode in MySQL 5.7: The `ONLY_FULL_GROUP_BY` and `STRICT_TRANS_TABLES` modes were added in MySQL 5.7.5. The `NO_AUTO_CREATE_USER` mode was added in MySQL 5.7.7. The `ERROR_FOR_DIVISION_BY_ZERO`, `NO_ZERO_DATE`, and `NO_ZERO_IN_DATE` modes were added in MySQL 5.7.8. For additional discussion regarding these changes to the default SQL mode value, see SQL Mode Changes in MySQL 5.7.

To set the SQL mode at server startup, use the [``--sql-mode="*`modes`*"``](server-options.md) option on the command line, or [``sql-mode="*`modes`*"``](server-options.md) in an option file such as `my.cnf` (Unix operating systems) or `my.ini` (Windows). *`modes`* is a list of different modes separated by commas. To clear the SQL mode explicitly, set it to an empty string using [`--sql-mode=""`](server-options.md) on the command line, or [`sql-mode=""`](server-options.md) in an option file.

Note

MySQL installation programs may configure the SQL mode during the installation process. If the SQL mode differs from the default or from what you expect, check for a setting in an option file that the server reads at startup.

To change the SQL mode at runtime, set the global or session [`sql_mode`](server-system-variables.md) system variable using a [`SET`](set-variable.md) statement:

```
SET GLOBAL sql_mode = 'modes';
SET SESSION sql_mode = 'modes';
```

Setting the `GLOBAL` variable requires the [`SUPER`](privileges-provided.md) privilege and affects the operation of all clients that connect from that time on. Setting the `SESSION` variable affects only the current client. Each client can change its session [`sql_mode`](server-system-variables.md) value at any time.

To determine the current global or session [`sql_mode`](server-system-variables.md) setting, select its value:

```
SELECT @@GLOBAL.sql_mode;
SELECT @@SESSION.sql_mode;
```

Important

**SQL mode and user-defined partitioning.** Changing the server SQL mode after creating and inserting data into partitioned tables can cause major changes in the behavior of such tables, and could lead to loss or corruption of data. It is strongly recommended that you never change the SQL mode once you have created tables employing user-defined partitioning.

When replicating partitioned tables, differing SQL modes on the source and replica can also lead to problems. For best results, you should always use the same server SQL mode on the source and replica.

For more information, see [Section 22.6, “Restrictions and Limitations on Partitioning”](partitioning-limitations.md).

#### The Most Important SQL Modes

The most important [`sql_mode`](server-system-variables.md) values are probably these:

- `ANSI`
	This mode changes syntax and behavior to conform more closely to standard SQL. It is one of the special combination modes listed at the end of this section.
- `STRICT_TRANS_TABLES`
	If a value could not be inserted as given into a transactional table, abort the statement. For a nontransactional table, abort the statement if the value occurs in a single-row statement or the first row of a multiple-row statement. More details are given later in this section.
	As of MySQL 5.7.5, the default SQL mode includes `STRICT_TRANS_TABLES`.
- `TRADITIONAL`
	Make MySQL behave like a “traditional” SQL database system. A simple description of this mode is “give an error instead of a warning” when inserting an incorrect value into a column. It is one of the special combination modes listed at the end of this section.
	Note
	With `TRADITIONAL` mode enabled, an [`INSERT`](insert.md) or [`UPDATE`](update.md) aborts as soon as an error occurs. If you are using a nontransactional storage engine, this may not be what you want because data changes made prior to the error may not be rolled back, resulting in a “partially done” update.

When this manual refers to “strict mode,” it means a mode with either or both `STRICT_TRANS_TABLES` or `STRICT_ALL_TABLES` enabled.

#### Full List of SQL Modes

The following list describes all supported SQL modes:

- `ALLOW_INVALID_DATES`
	Do not perform full checking of dates. Check only that the month is in the range from 1 to 12 and the day is in the range from 1 to 31. This may be useful for Web applications that obtain year, month, and day in three different fields and store exactly what the user inserted, without date validation. This mode applies to [`DATE`](datetime.md) and [`DATETIME`](datetime.md) columns. It does not apply to [`TIMESTAMP`](datetime.md) columns, which always require a valid date.
	With `ALLOW_INVALID_DATES` disabled, the server requires that month and day values be legal, and not merely in the range 1 to 12 and 1 to 31, respectively. With strict mode disabled, invalid dates such as `'2004-04-31'` are converted to `'0000-00-00'` and a warning is generated. With strict mode enabled, invalid dates generate an error. To permit such dates, enable `ALLOW_INVALID_DATES`.
- `ANSI_QUOTES`
	Treat `"` as an identifier quote character (like the `` ` `` quote character) and not as a string quote character. You can still use `` ` `` to quote identifiers with this mode enabled. With `ANSI_QUOTES` enabled, you cannot use double quotation marks to quote literal strings because they are interpreted as identifiers.
- `ERROR_FOR_DIVISION_BY_ZERO`
	The `ERROR_FOR_DIVISION_BY_ZERO` mode affects handling of division by zero, which includes [``MOD(*`N`*,0)``](mathematical-functions.md). For data-change operations ([`INSERT`](insert.md), [`UPDATE`](update.md)), its effect also depends on whether strict SQL mode is enabled.
	- If this mode is not enabled, division by zero inserts `NULL` and produces no warning.
	- If this mode is enabled, division by zero inserts `NULL` and produces a warning.
	- If this mode and strict mode are enabled, division by zero produces an error, unless `IGNORE` is given as well. For `INSERT IGNORE` and `UPDATE IGNORE`, division by zero inserts `NULL` and produces a warning.
	For [`SELECT`](select.md), division by zero returns `NULL`. Enabling `ERROR_FOR_DIVISION_BY_ZERO` causes a warning to be produced as well, regardless of whether strict mode is enabled.
	`ERROR_FOR_DIVISION_BY_ZERO` is deprecated. `ERROR_FOR_DIVISION_BY_ZERO` is not part of strict mode, but should be used in conjunction with strict mode and is enabled by default. A warning occurs if `ERROR_FOR_DIVISION_BY_ZERO` is enabled without also enabling strict mode or vice versa. For additional discussion, see SQL Mode Changes in MySQL 5.7.
	Because `ERROR_FOR_DIVISION_BY_ZERO` is deprecated; expect it to be removed in a future release of MySQL as a separate mode name and its effect included in the effects of strict SQL mode.
- `HIGH_NOT_PRECEDENCE`
	The precedence of the [`NOT`](logical-operators.md) operator is such that expressions such as `NOT a             BETWEEN b AND c` are parsed as `NOT (a             BETWEEN b AND c)`. In some older versions of MySQL, the expression was parsed as `(NOT a) BETWEEN b AND             c`. The old higher-precedence behavior can be obtained by enabling the `HIGH_NOT_PRECEDENCE` SQL mode.
	```
	mysql> SET sql_mode = '';
	mysql> SELECT NOT 1 BETWEEN -5 AND 5;
	        -> 0
	mysql> SET sql_mode = 'HIGH_NOT_PRECEDENCE';
	mysql> SELECT NOT 1 BETWEEN -5 AND 5;
	        -> 1
	```
- `IGNORE_SPACE`
	Permit spaces between a function name and the `(` character. This causes built-in function names to be treated as reserved words. As a result, identifiers that are the same as function names must be quoted as described in [Section 9.2, “Schema Object Names”](identifiers.md). For example, because there is a [`COUNT()`](aggregate-functions.md) function, the use of `count` as a table name in the following statement causes an error:
	```
	mysql> CREATE TABLE count (i INT);
	ERROR 1064 (42000): You have an error in your SQL syntax
	```
	The table name should be quoted:
	```
	mysql> CREATE TABLE \`count\` (i INT);
	Query OK, 0 rows affected (0.00 sec)
	```
	The `IGNORE_SPACE` SQL mode applies to built-in functions, not to loadable functions or stored functions. It is always permissible to have spaces after a loadable function or stored function name, regardless of whether `IGNORE_SPACE` is enabled.
	For further discussion of `IGNORE_SPACE`, see [Section 9.2.5, “Function Name Parsing and Resolution”](function-resolution.md).
- `NO_AUTO_CREATE_USER`
	Prevent the [`GRANT`](grant.md) statement from automatically creating new user accounts if it would otherwise do so, unless authentication information is specified. The statement must specify a nonempty password using `IDENTIFIED BY` or an authentication plugin using `IDENTIFIED WITH`.
	It is preferable to create MySQL accounts with [`CREATE USER`](create-user.md) rather than [`GRANT`](grant.md). `NO_AUTO_CREATE_USER` is deprecated and the default SQL mode includes `NO_AUTO_CREATE_USER`. Assignments to [`sql_mode`](server-system-variables.md) that change the `NO_AUTO_CREATE_USER` mode state produce a warning, except assignments that set [`sql_mode`](server-system-variables.md) to `DEFAULT`. Expect `NO_AUTO_CREATE_USER` to be be removed in a future release of MySQL, and its effect to be enabled at all times (and for [`GRANT`](grant.md) not to create accounts any longer).
	Previously, before `NO_AUTO_CREATE_USER` was deprecated, one reason not to enable it was that it was not replication safe. Now it can be enabled and replication-safe user management performed with `CREATE USER IF NOT             EXISTS`, `DROP USER IF EXISTS`, and `ALTER USER IF EXISTS` rather than `GRANT`. These statements enable safe replication when replicas may have different grants than those on the source. See [Section 13.7.1.2, “CREATE USER Statement”](create-user.md), [Section 13.7.1.3, “DROP USER Statement”](drop-user.md), and [Section 13.7.1.1, “ALTER USER Statement”](alter-user.md).
- `NO_AUTO_VALUE_ON_ZERO`
	`NO_AUTO_VALUE_ON_ZERO` affects handling of `AUTO_INCREMENT` columns. Normally, you generate the next sequence number for the column by inserting either `NULL` or `0` into it. `NO_AUTO_VALUE_ON_ZERO` suppresses this behavior for `0` so that only `NULL` generates the next sequence number.
	This mode can be useful if `0` has been stored in a table's `AUTO_INCREMENT` column. (Storing `0` is not a recommended practice, by the way.) For example, if you dump the table with [**mysqldump**](mysqldump.md) and then reload it, MySQL normally generates new sequence numbers when it encounters the `0` values, resulting in a table with contents different from the one that was dumped. Enabling `NO_AUTO_VALUE_ON_ZERO` before reloading the dump file solves this problem. For this reason, [**mysqldump**](mysqldump.md) automatically includes in its output a statement that enables `NO_AUTO_VALUE_ON_ZERO`.
- `NO_BACKSLASH_ESCAPES`
	Enabling this mode disables the use of the backslash character (`\`) as an escape character within strings and identifiers. With this mode enabled, backslash becomes an ordinary character like any other, and the default escape sequence for [`LIKE`](string-comparison-functions.md) expressions is changed so that no escape character is used.
- `NO_DIR_IN_CREATE`
	When creating a table, ignore all `INDEX             DIRECTORY` and `DATA DIRECTORY` directives. This option is useful on replica replication servers.
- `NO_ENGINE_SUBSTITUTION`
	Control automatic substitution of the default storage engine when a statement such as [`CREATE             TABLE`](create-table.md) or [`ALTER             TABLE`](alter-table.md) specifies a storage engine that is disabled or not compiled in.
	By default, `NO_ENGINE_SUBSTITUTION` is enabled.
	Because storage engines can be pluggable at runtime, unavailable engines are treated the same way:
	With `NO_ENGINE_SUBSTITUTION` disabled, for [`CREATE TABLE`](create-table.md) the default engine is used and a warning occurs if the desired engine is unavailable. For [`ALTER TABLE`](alter-table.md), a warning occurs and the table is not altered.
	With `NO_ENGINE_SUBSTITUTION` enabled, an error occurs and the table is not created or altered if the desired engine is unavailable.
- `NO_FIELD_OPTIONS`
	Do not print MySQL-specific column options in the output of [`SHOW CREATE TABLE`](show-create-table.md). This mode is used by [**mysqldump**](mysqldump.md) in portability mode.
	Note
	As of MySQL 5.7.22, `NO_FIELD_OPTIONS` is deprecated. It is removed in MySQL 8.0.
- `NO_KEY_OPTIONS`
	Do not print MySQL-specific index options in the output of [`SHOW CREATE TABLE`](show-create-table.md). This mode is used by [**mysqldump**](mysqldump.md) in portability mode.
	Note
	As of MySQL 5.7.22, `NO_KEY_OPTIONS` is deprecated. It is removed in MySQL 8.0.
- `NO_TABLE_OPTIONS`
	Do not print MySQL-specific table options (such as `ENGINE`) in the output of [`SHOW CREATE TABLE`](show-create-table.md). This mode is used by [**mysqldump**](mysqldump.md) in portability mode.
	Note
	As of MySQL 5.7.22, `NO_TABLE_OPTIONS` is deprecated. It is removed in MySQL 8.0.
- `NO_UNSIGNED_SUBTRACTION`
	Subtraction between integer values, where one is of type `UNSIGNED`, produces an unsigned result by default. If the result would otherwise have been negative, an error results:
	```
	mysql> SET sql_mode = '';
	Query OK, 0 rows affected (0.00 sec)
	mysql> SELECT CAST(0 AS UNSIGNED) - 1;
	ERROR 1690 (22003): BIGINT UNSIGNED value is out of range in '(cast(0 as unsigned) - 1)'
	```
	If the `NO_UNSIGNED_SUBTRACTION` SQL mode is enabled, the result is negative:
	```
	mysql> SET sql_mode = 'NO_UNSIGNED_SUBTRACTION';
	mysql> SELECT CAST(0 AS UNSIGNED) - 1;
	+-------------------------+
	| CAST(0 AS UNSIGNED) - 1 |
	+-------------------------+
	|                      -1 |
	+-------------------------+
	```
	If the result of such an operation is used to update an `UNSIGNED` integer column, the result is clipped to the maximum value for the column type, or clipped to 0 if `NO_UNSIGNED_SUBTRACTION` is enabled. With strict SQL mode enabled, an error occurs and the column remains unchanged.
	When `NO_UNSIGNED_SUBTRACTION` is enabled, the subtraction result is signed, *even if any operand is unsigned*. For example, compare the type of column `c2` in table `t1` with that of column `c2` in table `t2`:
	```
	mysql> SET sql_mode='';
	mysql> CREATE TABLE test (c1 BIGINT UNSIGNED NOT NULL);
	mysql> CREATE TABLE t1 SELECT c1 - 1 AS c2 FROM test;
	mysql> DESCRIBE t1;
	+-------+---------------------+------+-----+---------+-------+
	| Field | Type                | Null | Key | Default | Extra |
	+-------+---------------------+------+-----+---------+-------+
	| c2    | bigint(21) unsigned | NO   |     | 0       |       |
	+-------+---------------------+------+-----+---------+-------+
	mysql> SET sql_mode='NO_UNSIGNED_SUBTRACTION';
	mysql> CREATE TABLE t2 SELECT c1 - 1 AS c2 FROM test;
	mysql> DESCRIBE t2;
	+-------+------------+------+-----+---------+-------+
	| Field | Type       | Null | Key | Default | Extra |
	+-------+------------+------+-----+---------+-------+
	| c2    | bigint(21) | NO   |     | 0       |       |
	+-------+------------+------+-----+---------+-------+
	```
	This means that `BIGINT UNSIGNED` is not 100% usable in all contexts. See [Section 12.10, “Cast Functions and Operators”](cast-functions.md).
- `NO_ZERO_DATE`
	The `NO_ZERO_DATE` mode affects whether the server permits `'0000-00-00'` as a valid date. Its effect also depends on whether strict SQL mode is enabled.
	- If this mode is not enabled, `'0000-00-00'` is permitted and inserts produce no warning.
	- If this mode is enabled, `'0000-00-00'` is permitted and inserts produce a warning.
	- If this mode and strict mode are enabled, `'0000-00-00'` is not permitted and inserts produce an error, unless `IGNORE` is given as well. For `INSERT IGNORE` and `UPDATE                 IGNORE`, `'0000-00-00'` is permitted and inserts produce a warning.
	`NO_ZERO_DATE` is deprecated. `NO_ZERO_DATE` is not part of strict mode, but should be used in conjunction with strict mode and is enabled by default. A warning occurs if `NO_ZERO_DATE` is enabled without also enabling strict mode or vice versa. For additional discussion, see SQL Mode Changes in MySQL 5.7.
	Because `NO_ZERO_DATE` is deprecated; expect it to be removed in a future release of MySQL as a separate mode name and its effect included in the effects of strict SQL mode.
- `NO_ZERO_IN_DATE`
	The `NO_ZERO_IN_DATE` mode affects whether the server permits dates in which the year part is nonzero but the month or day part is 0. (This mode affects dates such as `'2010-00-01'` or `'2010-01-00'`, but not `'0000-00-00'`. To control whether the server permits `'0000-00-00'`, use the `NO_ZERO_DATE` mode.) The effect of `NO_ZERO_IN_DATE` also depends on whether strict SQL mode is enabled.
	- If this mode is not enabled, dates with zero parts are permitted and inserts produce no warning.
	- If this mode is enabled, dates with zero parts are inserted as `'0000-00-00'` and produce a warning.
	- If this mode and strict mode are enabled, dates with zero parts are not permitted and inserts produce an error, unless `IGNORE` is given as well. For `INSERT IGNORE` and `UPDATE IGNORE`, dates with zero parts are inserted as `'0000-00-00'` and produce a warning.
	`NO_ZERO_IN_DATE` is deprecated. `NO_ZERO_IN_DATE` is not part of strict mode, but should be used in conjunction with strict mode and is enabled by default. A warning occurs if `NO_ZERO_IN_DATE` is enabled without also enabling strict mode or vice versa. For additional discussion, see SQL Mode Changes in MySQL 5.7.
	Because `NO_ZERO_IN_DATE` is deprecated; expect it to be removed in a future release of MySQL as a separate mode name and its effect included in the effects of strict SQL mode.
- `ONLY_FULL_GROUP_BY`
	Reject queries for which the select list, `HAVING` condition, or `ORDER             BY` list refer to nonaggregated columns that are neither named in the `GROUP BY` clause nor are functionally dependent on (uniquely determined by) `GROUP BY` columns.
	As of MySQL 5.7.5, the default SQL mode includes `ONLY_FULL_GROUP_BY`. (Before 5.7.5, MySQL does not detect functional dependency and `ONLY_FULL_GROUP_BY` is not enabled by default.)
	A MySQL extension to standard SQL permits references in the `HAVING` clause to aliased expressions in the select list. Before MySQL 5.7.5, enabling `ONLY_FULL_GROUP_BY` disables this extension, thus requiring the `HAVING` clause to be written using unaliased expressions. As of MySQL 5.7.5, this restriction is lifted so that the `HAVING` clause can refer to aliases regardless of whether `ONLY_FULL_GROUP_BY` is enabled.
	For additional discussion and examples, see [Section 12.19.3, “MySQL Handling of GROUP BY”](group-by-handling.md).
- `PAD_CHAR_TO_FULL_LENGTH`
	By default, trailing spaces are trimmed from [`CHAR`](char.md) column values on retrieval. If `PAD_CHAR_TO_FULL_LENGTH` is enabled, trimming does not occur and retrieved [`CHAR`](char.md) values are padded to their full length. This mode does not apply to [`VARCHAR`](char.md) columns, for which trailing spaces are retained on retrieval.
	```
	mysql> CREATE TABLE t1 (c1 CHAR(10));
	Query OK, 0 rows affected (0.37 sec)
	mysql> INSERT INTO t1 (c1) VALUES('xy');
	Query OK, 1 row affected (0.01 sec)
	mysql> SET sql_mode = '';
	Query OK, 0 rows affected (0.00 sec)
	mysql> SELECT c1, CHAR_LENGTH(c1) FROM t1;
	+------+-----------------+
	| c1   | CHAR_LENGTH(c1) |
	+------+-----------------+
	| xy   |               2 |
	+------+-----------------+
	1 row in set (0.00 sec)
	mysql> SET sql_mode = 'PAD_CHAR_TO_FULL_LENGTH';
	Query OK, 0 rows affected (0.00 sec)
	mysql> SELECT c1, CHAR_LENGTH(c1) FROM t1;
	+------------+-----------------+
	| c1         | CHAR_LENGTH(c1) |
	+------------+-----------------+
	| xy         |              10 |
	+------------+-----------------+
	1 row in set (0.00 sec)
	```
- `PIPES_AS_CONCAT`
	Treat [`||`](logical-operators.md) as a string concatenation operator (same as [`CONCAT()`](string-functions.md)) rather than as a synonym for [`OR`](logical-operators.md).
- `REAL_AS_FLOAT`
	Treat [`REAL`](floating-point-types.md) as a synonym for [`FLOAT`](floating-point-types.md). By default, MySQL treats [`REAL`](floating-point-types.md) as a synonym for [`DOUBLE`](floating-point-types.md).
- `STRICT_ALL_TABLES`
	Enable strict SQL mode for all storage engines. Invalid data values are rejected. For details, see Strict SQL Mode.
	From MySQL 5.7.4 through 5.7.7, `STRICT_ALL_TABLES` includes the effect of the `ERROR_FOR_DIVISION_BY_ZERO`, `NO_ZERO_DATE`, and `NO_ZERO_IN_DATE` modes. For additional discussion, see SQL Mode Changes in MySQL 5.7.
- `STRICT_TRANS_TABLES`
	Enable strict SQL mode for transactional storage engines, and when possible for nontransactional storage engines. For details, see Strict SQL Mode.
	From MySQL 5.7.4 through 5.7.7, `STRICT_TRANS_TABLES` includes the effect of the `ERROR_FOR_DIVISION_BY_ZERO`, `NO_ZERO_DATE`, and `NO_ZERO_IN_DATE` modes. For additional discussion, see SQL Mode Changes in MySQL 5.7.

#### Combination SQL Modes

The following special modes are provided as shorthand for combinations of mode values from the preceding list.

- `ANSI`
	Equivalent to `REAL_AS_FLOAT`, `PIPES_AS_CONCAT`, `ANSI_QUOTES`, `IGNORE_SPACE`, and (as of MySQL 5.7.5) `ONLY_FULL_GROUP_BY`.
	`ANSI` mode also causes the server to return an error for queries where a set function *`S`* with an outer reference ``*`S`*(*`outer_ref`*)`` cannot be aggregated in the outer query against which the outer reference has been resolved. This is such a query:
	```
	SELECT * FROM t1 WHERE t1.a IN (SELECT MAX(t1.b) FROM t2 WHERE ...);
	```
	Here, [`MAX(t1.b)`](aggregate-functions.md) cannot aggregated in the outer query because it appears in the `WHERE` clause of that query. Standard SQL requires an error in this situation. If `ANSI` mode is not enabled, the server treats ``*`S`*(*`outer_ref`*)`` in such queries the same way that it would interpret ``*`S`*(*`const`*)``.
	See [Section 1.6, “MySQL Standards Compliance”](compatibility.md).
- `DB2`
	Equivalent to `PIPES_AS_CONCAT`, `ANSI_QUOTES`, `IGNORE_SPACE`, `NO_KEY_OPTIONS`, `NO_TABLE_OPTIONS`, `NO_FIELD_OPTIONS`.
	Note
	As of MySQL 5.7.22, `DB2` is deprecated. It is removed in MySQL 8.0.
- `MAXDB`
	Equivalent to `PIPES_AS_CONCAT`, `ANSI_QUOTES`, `IGNORE_SPACE`, `NO_KEY_OPTIONS`, `NO_TABLE_OPTIONS`, `NO_FIELD_OPTIONS`, `NO_AUTO_CREATE_USER`.
	Note
	As of MySQL 5.7.22, `MAXDB` is deprecated. It is removed in MySQL 8.0.
- `MSSQL`
	Equivalent to `PIPES_AS_CONCAT`, `ANSI_QUOTES`, `IGNORE_SPACE`, `NO_KEY_OPTIONS`, `NO_TABLE_OPTIONS`, `NO_FIELD_OPTIONS`.
	Note
	As of MySQL 5.7.22, `MSSQL` is deprecated. It is removed in MySQL 8.0.
- `MYSQL323`
	Equivalent to `MYSQL323`, `HIGH_NOT_PRECEDENCE`. This means `HIGH_NOT_PRECEDENCE` plus some [`SHOW CREATE TABLE`](show-create-table.md) behaviors specific to `MYSQL323`:
	- [`TIMESTAMP`](datetime.md) column display does not include `DEFAULT` or `ON UPDATE` attributes.
	- String column display does not include character set and collation attributes. For [`CHAR`](char.md) and [`VARCHAR`](char.md) columns, if the collation is binary, `BINARY` is appended to the column type.
	- The ``ENGINE=*`engine_name`*`` table option displays as ``TYPE=*`engine_name`*``.
	- For [`MEMORY`](memory-storage-engine.md) tables, the storage engine is displayed as `HEAP`.
	Note
	As of MySQL 5.7.22, `MYSQL323` is deprecated. It is removed in MySQL 8.0.
- `MYSQL40`
	Equivalent to `MYSQL40`, `HIGH_NOT_PRECEDENCE`. This means `HIGH_NOT_PRECEDENCE` plus some behaviors specific to `MYSQL40`. These are the same as for `MYSQL323`, except that [`SHOW CREATE TABLE`](show-create-table.md) does not display `HEAP` as the storage engine for [`MEMORY`](memory-storage-engine.md) tables.
	Note
	As of MySQL 5.7.22, `MYSQL40` is deprecated. It is removed in MySQL 8.0.
- `ORACLE`
	Equivalent to `PIPES_AS_CONCAT`, `ANSI_QUOTES`, `IGNORE_SPACE`, `NO_KEY_OPTIONS`, `NO_TABLE_OPTIONS`, `NO_FIELD_OPTIONS`, `NO_AUTO_CREATE_USER`.
	Note
	As of MySQL 5.7.22, `ORACLE` is deprecated. It is removed in MySQL 8.0.
- `POSTGRESQL`
	Equivalent to `PIPES_AS_CONCAT`, `ANSI_QUOTES`, `IGNORE_SPACE`, `NO_KEY_OPTIONS`, `NO_TABLE_OPTIONS`, `NO_FIELD_OPTIONS`.
	Note
	As of MySQL 5.7.22, `POSTGRESQL` is deprecated. It is removed in MySQL 8.0.
- `TRADITIONAL`
	Before MySQL 5.7.4, and in MySQL 5.7.8 and later, `TRADITIONAL` is equivalent to `STRICT_TRANS_TABLES`, `STRICT_ALL_TABLES`, `NO_ZERO_IN_DATE`, `NO_ZERO_DATE`, `ERROR_FOR_DIVISION_BY_ZERO`, `NO_AUTO_CREATE_USER`, and `NO_ENGINE_SUBSTITUTION`.
	From MySQL 5.7.4 though 5.7.7, `TRADITIONAL` is equivalent to `STRICT_TRANS_TABLES`, `STRICT_ALL_TABLES`, `NO_AUTO_CREATE_USER`, and `NO_ENGINE_SUBSTITUTION`. The `NO_ZERO_IN_DATE`, `NO_ZERO_DATE`, and `ERROR_FOR_DIVISION_BY_ZERO` modes are not named because in those versions their effects are included in the effects of strict SQL mode (`STRICT_ALL_TABLES` or `STRICT_TRANS_TABLES`). Thus, the effects of `TRADITIONAL` are the same in all MySQL 5.7 versions (and the same as in MySQL 5.6). For additional discussion, see SQL Mode Changes in MySQL 5.7.

#### Strict SQL Mode

Strict mode controls how MySQL handles invalid or missing values in data-change statements such as [`INSERT`](insert.md) or [`UPDATE`](update.md). A value can be invalid for several reasons. For example, it might have the wrong data type for the column, or it might be out of range. A value is missing when a new row to be inserted does not contain a value for a non- `NULL` column that has no explicit `DEFAULT` clause in its definition. (For a `NULL` column, `NULL` is inserted if the value is missing.) Strict mode also affects DDL statements such as [`CREATE TABLE`](create-table.md).

If strict mode is not in effect, MySQL inserts adjusted values for invalid or missing values and produces warnings (see [Section 13.7.5.40, “SHOW WARNINGS Statement”](show-warnings.md)). In strict mode, you can produce this behavior by using [`INSERT IGNORE`](insert.md) or [`UPDATE         IGNORE`](update.md).

For statements such as [`SELECT`](select.md) that do not change data, invalid values generate a warning in strict mode, not an error.

Strict mode produces an error for attempts to create a key that exceeds the maximum key length. When strict mode is not enabled, this results in a warning and truncation of the key to the maximum key length.

Strict mode does not affect whether foreign key constraints are checked. [`foreign_key_checks`](server-system-variables.md) can be used for that. (See [Section 5.1.7, “Server System Variables”](server-system-variables.md).)

Strict SQL mode is in effect if either `STRICT_ALL_TABLES` or `STRICT_TRANS_TABLES` is enabled, although the effects of these modes differ somewhat:

- For transactional tables, an error occurs for invalid or missing values in a data-change statement when either `STRICT_ALL_TABLES` or `STRICT_TRANS_TABLES` is enabled. The statement is aborted and rolled back.
- For nontransactional tables, the behavior is the same for either mode if the bad value occurs in the first row to be inserted or updated: The statement is aborted and the table remains unchanged. If the statement inserts or modifies multiple rows and the bad value occurs in the second or later row, the result depends on which strict mode is enabled:
	- For `STRICT_ALL_TABLES`, MySQL returns an error and ignores the rest of the rows. However, because the earlier rows have been inserted or updated, the result is a partial update. To avoid this, use single-row statements, which can be aborted without changing the table.
	- For `STRICT_TRANS_TABLES`, MySQL converts an invalid value to the closest valid value for the column and inserts the adjusted value. If a value is missing, MySQL inserts the implicit default value for the column data type. In either case, MySQL generates a warning rather than an error and continues processing the statement. Implicit defaults are described in [Section 11.6, “Data Type Default Values”](data-type-defaults.md).

Strict mode affects handling of division by zero, zero dates, and zeros in dates as follows:

- Strict mode affects handling of division by zero, which includes [``MOD(*`N`*,0)``](mathematical-functions.md):
	For data-change operations ([`INSERT`](insert.md), [`UPDATE`](update.md)):
	- If strict mode is not enabled, division by zero inserts `NULL` and produces no warning.
	- If strict mode is enabled, division by zero produces an error, unless `IGNORE` is given as well. For `INSERT IGNORE` and `UPDATE IGNORE`, division by zero inserts `NULL` and produces a warning.
	For [`SELECT`](select.md), division by zero returns `NULL`. Enabling strict mode causes a warning to be produced as well.
- Strict mode affects whether the server permits `'0000-00-00'` as a valid date:
	- If strict mode is not enabled, `'0000-00-00'` is permitted and inserts produce no warning.
	- If strict mode is enabled, `'0000-00-00'` is not permitted and inserts produce an error, unless `IGNORE` is given as well. For `INSERT IGNORE` and `UPDATE                 IGNORE`, `'0000-00-00'` is permitted and inserts produce a warning.
- Strict mode affects whether the server permits dates in which the year part is nonzero but the month or day part is 0 (dates such as `'2010-00-01'` or `'2010-01-00'`):
	- If strict mode is not enabled, dates with zero parts are permitted and inserts produce no warning.
	- If strict mode is enabled, dates with zero parts are not permitted and inserts produce an error, unless `IGNORE` is given as well. For `INSERT IGNORE` and `UPDATE                 IGNORE`, dates with zero parts are inserted as `'0000-00-00'` (which is considered valid with `IGNORE`) and produce a warning.

For more information about strict mode with respect to `IGNORE`, see Comparison of the IGNORE Keyword and Strict SQL Mode.

Before MySQL 5.7.4, and in MySQL 5.7.8 and later, strict mode affects handling of division by zero, zero dates, and zeros in dates in conjunction with the `ERROR_FOR_DIVISION_BY_ZERO`, `NO_ZERO_DATE`, and `NO_ZERO_IN_DATE` modes. From MySQL 5.7.4 though 5.7.7, the `ERROR_FOR_DIVISION_BY_ZERO`, `NO_ZERO_DATE`, and `NO_ZERO_IN_DATE` modes do nothing when named explicitly and their effects are included in the effects of strict mode. For additional discussion, see SQL Mode Changes in MySQL 5.7.

#### Comparison of the IGNORE Keyword and Strict SQL Mode

This section compares the effect on statement execution of the `IGNORE` keyword (which downgrades errors to warnings) and strict SQL mode (which upgrades warnings to errors). It describes which statements they affect, and which errors they apply to.

The following table presents a summary comparison of statement behavior when the default is to produce an error versus a warning. An example of when the default is to produce an error is inserting a `NULL` into a `NOT         NULL` column. An example of when the default is to produce a warning is inserting a value of the wrong data type into a column (such as inserting the string `'abc'` into an integer column).

| Operational Mode | When Statement Default is Error | When Statement Default is Warning |
| --- | --- | --- |
| Without `IGNORE` or strict SQL mode | Error | Warning |
| With `IGNORE` | Warning | Warning (same as without `IGNORE` or strict SQL mode) |
| With strict SQL mode | Error (same as without `IGNORE` or strict SQL mode) | Error |
| With `IGNORE` and strict SQL mode | Warning | Warning |

One conclusion to draw from the table is that when the `IGNORE` keyword and strict SQL mode are both in effect, `IGNORE` takes precedence. This means that, although `IGNORE` and strict SQL mode can be considered to have opposite effects on error handling, they do not cancel when used together.

##### The Effect of IGNORE on Statement Execution

Several statements in MySQL support an optional `IGNORE` keyword. This keyword causes the server to downgrade certain types of errors and generate warnings instead. For a multiple-row statement, downgrading an error to a warning may enable a row to be processed. Otherwise, `IGNORE` causes the statement to skip to the next row instead of aborting. (For nonignorable errors, an error occurs regardless of the `IGNORE` keyword.)

Example: If the table `t` has a primary key column `i` containing unique values, attempting to insert the same value of `i` into multiple rows normally produces a duplicate-key error:

```
mysql> CREATE TABLE t (i INT NOT NULL PRIMARY KEY);
mysql> INSERT INTO t (i) VALUES(1),(1);
ERROR 1062 (23000): Duplicate entry '1' for key 'PRIMARY'
```

With `IGNORE`, the row containing the duplicate key still is not inserted, but a warning occurs instead of an error:

```
mysql> INSERT IGNORE INTO t (i) VALUES(1),(1);
Query OK, 1 row affected, 1 warning (0.01 sec)
Records: 2  Duplicates: 1  Warnings: 1

mysql> SHOW WARNINGS;
+---------+------+---------------------------------------+
| Level   | Code | Message                               |
+---------+------+---------------------------------------+
| Warning | 1062 | Duplicate entry '1' for key 'PRIMARY' |
+---------+------+---------------------------------------+
1 row in set (0.00 sec)
```

Example: If the table `t2` has a `NOT         NULL` column `id`, attempting to insert `NULL` produces an error in strict SQL mode:

```
mysql> CREATE TABLE t2 (id INT NOT NULL);
mysql> INSERT INTO t2 (id) VALUES(1),(NULL),(3);
ERROR 1048 (23000): Column 'id' cannot be null
mysql> SELECT * FROM t2;
Empty set (0.00 sec)
```

If the SQL mode is not strict, `IGNORE` causes the `NULL` to be inserted as the column implicit default (0 in this case), which enables the row to be handled without skipping it:

```
mysql> INSERT INTO t2 (id) VALUES(1),(NULL),(3);
mysql> SELECT * FROM t2;
+----+
| id |
+----+
|  1 |
|  0 |
|  3 |
+----+
```

These statements support the `IGNORE` keyword:

- [`CREATE TABLE             ... SELECT`](create-table.md): `IGNORE` does not apply to the [`CREATE TABLE`](create-table.md) or [`SELECT`](select.md) parts of the statement but to inserts into the table of rows produced by the [`SELECT`](select.md). Rows that duplicate an existing row on a unique key value are discarded.
- [`DELETE`](delete.md): `IGNORE` causes MySQL to ignore errors during the process of deleting rows.
- [`INSERT`](insert.md): With `IGNORE`, rows that duplicate an existing row on a unique key value are discarded. Rows set to values that would cause data conversion errors are set to the closest valid values instead.
	For partitioned tables where no partition matching a given value is found, `IGNORE` causes the insert operation to fail silently for rows containing the unmatched value.
- [`LOAD DATA`](load-data.md), [`LOAD XML`](load-xml.md): With `IGNORE`, rows that duplicate an existing row on a unique key value are discarded.
- [`UPDATE`](update.md): With `IGNORE`, rows for which duplicate-key conflicts occur on a unique key value are not updated. Rows updated to values that would cause data conversion errors are updated to the closest valid values instead.

The `IGNORE` keyword applies to the following ignorable errors:

##### The Effect of Strict SQL Mode on Statement Execution

The MySQL server can operate in different SQL modes, and can apply these modes differently for different clients, depending on the value of the [`sql_mode`](server-system-variables.md) system variable. In “strict” SQL mode, the server upgrades certain warnings to errors.

For example, in non-strict SQL mode, inserting the string `'abc'` into an integer column results in conversion of the value to 0 and a warning:

```
mysql> SET sql_mode = '';
Query OK, 0 rows affected (0.00 sec)

mysql> INSERT INTO t (i) VALUES('abc');
Query OK, 1 row affected, 1 warning (0.01 sec)

mysql> SHOW WARNINGS;
+---------+------+--------------------------------------------------------+
| Level   | Code | Message                                                |
+---------+------+--------------------------------------------------------+
| Warning | 1366 | Incorrect integer value: 'abc' for column 'i' at row 1 |
+---------+------+--------------------------------------------------------+
1 row in set (0.00 sec)
```

In strict SQL mode, the invalid value is rejected with an error:

```
mysql> SET sql_mode = 'STRICT_ALL_TABLES';
Query OK, 0 rows affected (0.00 sec)

mysql> INSERT INTO t (i) VALUES('abc');
ERROR 1366 (HY000): Incorrect integer value: 'abc' for column 'i' at row 1
```

For more information about possible settings of the [`sql_mode`](server-system-variables.md) system variable, see Section 5.1.10, “Server SQL Modes”.

Strict SQL mode applies to the following statements under conditions for which some value might be out of range or an invalid row is inserted into or deleted from a table:

Within stored programs, individual statements of the types just listed execute in strict SQL mode if the program was defined while strict mode was in effect.

Strict SQL mode applies to the following errors, which represent a class of errors in which an input value is either invalid or missing. A value is invalid if it has the wrong data type for the column or might be out of range. A value is missing if a new row to be inserted does not contain a value for a `NOT         NULL` column that has no explicit `DEFAULT` clause in its definition.

```
ER_BAD_NULL_ERROR
ER_CUT_VALUE_GROUP_CONCAT
ER_DATA_TOO_LONG
ER_DATETIME_FUNCTION_OVERFLOW
ER_DIVISION_BY_ZERO
ER_INVALID_ARGUMENT_FOR_LOGARITHM
ER_NO_DEFAULT_FOR_FIELD
ER_NO_DEFAULT_FOR_VIEW_FIELD
ER_TOO_LONG_KEY
ER_TRUNCATED_WRONG_VALUE
ER_TRUNCATED_WRONG_VALUE_FOR_FIELD
ER_WARN_DATA_OUT_OF_RANGE
ER_WARN_NULL_TO_NOTNULL
ER_WARN_TOO_FEW_RECORDS
ER_WRONG_ARGUMENTS
ER_WRONG_VALUE_FOR_TYPE
WARN_DATA_TRUNCATED
```

Note

Because continued MySQL development defines new errors, there may be errors not in the preceding list to which strict SQL mode applies.

#### SQL Mode Changes in MySQL 5.7

In MySQL 5.7.22, these SQL modes are deprecated and are removed in MySQL 8.0: `DB2`, `MAXDB`, `MSSQL`, `MYSQL323`, `MYSQL40`, `ORACLE`, `POSTGRESQL`, `NO_FIELD_OPTIONS`, `NO_KEY_OPTIONS`, `NO_TABLE_OPTIONS`.

In MySQL 5.7, the `ONLY_FULL_GROUP_BY` SQL mode is enabled by default because `GROUP BY` processing has become more sophisticated to include detection of functional dependencies. However, if you find that having `ONLY_FULL_GROUP_BY` enabled causes queries for existing applications to be rejected, either of these actions should restore operation:

- If it is possible to modify an offending query, do so, either so that nonaggregated columns are functionally dependent on `GROUP BY` columns, or by referring to nonaggregated columns using [`ANY_VALUE()`](miscellaneous-functions.md).
- If it is not possible to modify an offending query (for example, if it is generated by a third-party application), set the `sql_mode` system variable at server startup to not enable `ONLY_FULL_GROUP_BY`.

In MySQL 5.7, the `ERROR_FOR_DIVISION_BY_ZERO`, `NO_ZERO_DATE`, and `NO_ZERO_IN_DATE` SQL modes are deprecated. The long term plan is to have the three modes be included in strict SQL mode and to remove them as explicit modes in a future release of MySQL. For compatibility in MySQL 5.7 with MySQL 5.6 strict mode and to provide additional time for affected applications to be modified, the following behaviors apply:

- `ERROR_FOR_DIVISION_BY_ZERO`, `NO_ZERO_DATE`, and `NO_ZERO_IN_DATE` are not part of strict SQL mode, but it is intended that they be used together with strict mode. As a reminder, a warning occurs if they are enabled without also enabling strict mode or vice versa.
- `ERROR_FOR_DIVISION_BY_ZERO`, `NO_ZERO_DATE`, and `NO_ZERO_IN_DATE` are enabled by default.

With the preceding changes, stricter data checking is still enabled by default, but the individual modes can be disabled in environments where it is currently desirable or necessary to do so.