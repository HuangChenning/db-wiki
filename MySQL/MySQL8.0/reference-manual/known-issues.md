---
title: "B.3.7 Known Issues in MySQL"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/known-issues.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### B.3.7 Known Issues in MySQL

This section lists known issues in recent versions of MySQL.

For information about platform-specific issues, see the installation and debugging instructions in [Section 2.1, “General Installation Guidance”](general-installation-issues.md), and [Section 7.9, “Debugging MySQL”](debugging-mysql.md).

The following problems are known:

- Subquery optimization for `IN` is not as effective as for `=`.
- Even if you use `lower_case_table_names=2` (which enables MySQL to remember the case used for databases and table names), MySQL does not remember the case used for database names for the function [`DATABASE()`](information-functions.md) or within the various logs (on case-insensitive systems).
- Dropping a `FOREIGN KEY` constraint does not work in replication because the constraint may have another name on the replica.
- [`REPLACE`](replace.md) (and [`LOAD DATA`](load-data.md) with the [`REPLACE`](replace.md) option) does not trigger `ON DELETE CASCADE`.
- `DISTINCT` with `ORDER BY` does not work inside [`GROUP_CONCAT()`](aggregate-functions.md) if you do not use all and only those columns that are in the `DISTINCT` list.
- When inserting a big integer value (between 2 <sup>63</sup> and 2 <sup>64</sup> −1) into a decimal or string column, it is inserted as a negative value because the number is evaluated in signed integer context.
- With statement-based binary logging, the source server writes the executed queries to the binary log. This is a very fast, compact, and efficient logging method that works perfectly in most cases. However, it is possible for the data on the source and replica to become different if a query is designed in such a way that the data modification is nondeterministic (generally not a recommended practice, even outside of replication).
	For example:
	- [`CREATE                 TABLE ... SELECT`](create-table-select.md) or [`INSERT                 ... SELECT`](insert-select.md) statements that insert zero or `NULL` values into an `AUTO_INCREMENT` column.
	- [`DELETE`](delete.md) if you are deleting rows from a table that has foreign keys with `ON DELETE CASCADE` properties.
	- [`REPLACE ...                 SELECT`](replace.md), `INSERT IGNORE ...                 SELECT` if you have duplicate key values in the inserted data.
	**If and only if the preceding queries have no `ORDER BY` clause guaranteeing a deterministic order**.
	For example, for [`INSERT ...             SELECT`](insert-select.md) with no `ORDER BY`, the [`SELECT`](select.md) may return rows in a different order (which results in a row having different ranks, hence getting a different number in the `AUTO_INCREMENT` column), depending on the choices made by the optimizers on the source and replica.
	A query is optimized differently on the source and replica only if:
	- The table is stored using a different storage engine on the source than on the replica. (It is possible to use different storage engines on the source and replica. For example, you can use `InnoDB` on the source, but `MyISAM` on the replica if the replica has less available disk space.)
	- MySQL buffer sizes ([`key_buffer_size`](server-system-variables.md), and so on) are different on the source and replica.
	- The source and replica run different MySQL versions, and the optimizer code differs between these versions.
	This problem may also affect database restoration using **mysqlbinlog|mysql**.
	The easiest way to avoid this problem is to add an `ORDER BY` clause to the aforementioned nondeterministic queries to ensure that the rows are always stored or modified in the same order. Using row-based or mixed logging format also avoids the problem.
- Log file names are based on the server host name if you do not specify a file name with the startup option. To retain the same log file names if you change your host name to something else, you must explicitly use options such as [``--log-bin=*`old_host_name`*-bin``](replication-options-binary-log.md). See [Section 7.1.7, “Server Command Options”](server-options.md). Alternatively, rename the old files to reflect your host name change. If these are binary logs, you must edit the binary log index file and fix the binary log file names there as well. (The same is true for the relay logs on a replica.)
- [**mysqlbinlog**](mysqlbinlog.md) does not delete temporary files left after a [`LOAD DATA`](load-data.md) statement. See [Section 6.6.9, “mysqlbinlog — Utility for Processing Binary Log Files”](mysqlbinlog.md).
- `RENAME` does not work with `TEMPORARY` tables or tables used in a `MERGE` table.
- When using `SET CHARACTER SET`, you cannot use translated characters in database, table, and column names.
- Prior to MySQL 8.0.17, you cannot use `_` or `%` with `ESCAPE` in [`LIKE ...             ESCAPE`](string-comparison-functions.md).
- The server uses only the first [`max_sort_length`](server-system-variables.md) bytes when comparing data values. This means that values cannot reliably be used in `GROUP BY`, `ORDER BY`, or `DISTINCT` if they differ only after the first [`max_sort_length`](server-system-variables.md) bytes. To work around this, increase the variable value. The default value of [`max_sort_length`](server-system-variables.md) is 1024 and can be changed at server startup time or at runtime.
- Numeric calculations are done with [`BIGINT`](integer-types.md) or [`DOUBLE`](floating-point-types.md) (both are normally 64 bits long). Which precision you get depends on the function. The general rule is that bit functions are performed with [`BIGINT`](integer-types.md) precision, [`IF()`](flow-control-functions.md) and [`ELT()`](string-functions.md) with [`BIGINT`](integer-types.md) or [`DOUBLE`](floating-point-types.md) precision, and the rest with [`DOUBLE`](floating-point-types.md) precision. You should try to avoid using unsigned long long values if they resolve to be larger than 63 bits (9223372036854775807) for anything other than bit fields.
- You can have up to 255 [`ENUM`](enum.md) and [`SET`](set.md) columns in one table.
- In [`MIN()`](aggregate-functions.md), [`MAX()`](aggregate-functions.md), and other aggregate functions, MySQL currently compares [`ENUM`](enum.md) and [`SET`](set.md) columns by their string value rather than by the string's relative position in the set.
- In an [`UPDATE`](update.md) statement, columns are updated from left to right. If you refer to an updated column, you get the updated value instead of the original value. For example, the following statement increments `KEY` by `2`, **not** `1`:
	```
	mysql> UPDATE tbl_name SET KEY=KEY+1,KEY=KEY+1;
	```
- You can refer to multiple temporary tables in the same query, but you cannot refer to any given temporary table more than once. For example, the following does not work:
	```
	mysql> SELECT * FROM temp_table, temp_table AS t2;
	ERROR 1137: Can't reopen table: 'temp_table'
	```
- The optimizer may handle `DISTINCT` differently when you are using “hidden” columns in a join than when you are not. In a join, hidden columns are counted as part of the result (even if they are not shown), whereas in normal queries, hidden columns do not participate in the `DISTINCT` comparison.
	An example of this is:
	```
	SELECT DISTINCT mp3id FROM band_downloads
	       WHERE userid = 9 ORDER BY id DESC;
	```
	and
	```
	SELECT DISTINCT band_downloads.mp3id
	       FROM band_downloads,band_mp3
	       WHERE band_downloads.userid = 9
	       AND band_mp3.id = band_downloads.mp3id
	       ORDER BY band_downloads.id DESC;
	```
	In the second case, you may get two identical rows in the result set (because the values in the hidden `id` column may differ).
	Note that this happens only for queries that do not have the `ORDER BY` columns in the result.
- If you execute a `PROCEDURE` on a query that returns an empty set, in some cases the `PROCEDURE` does not transform the columns.
- Creation of a table of type `MERGE` does not check whether the underlying tables are compatible types.
- If you use [`ALTER TABLE`](alter-table.md) to add a `UNIQUE` index to a table used in a `MERGE` table and then add a normal index on the `MERGE` table, the key order is different for the tables if there was an old, non- `UNIQUE` key in the table. This is because [`ALTER TABLE`](alter-table.md) puts `UNIQUE` indexes before normal indexes to be able to detect duplicate keys as early as possible.
- An [`UPDATE`](update.md) statement involving a temporary table with a join on a non-temporary table having a trigger defined on it can result in an error, even though the update statement reads only the non-temporary table, in the following cases:
	- With read-only mode enabled (by using `SET                 GLOBAL                 ` [`read_only`](server-system-variables.md) `                 = 1`).
	- With the transaction level set to `READ_ONLY` (that is, using [`SET                 GLOBAL TRANSACTION READ ONLY`](set-transaction.md) or `SET                 SESSION TRANSACTION READ ONLY`).