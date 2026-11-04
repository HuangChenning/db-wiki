---
title: "16.7 Data Dictionary Usage Differences"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/data-dictionary-usage-differences.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

Use of a data dictionary-enabled MySQL server entails some operational differences compared to a server that does not have a data dictionary:

- Previously, enabling the [`innodb_read_only`](innodb-parameters.md) system variable prevented creating and dropping tables only for the `InnoDB` storage engine. As of MySQL 8.4, enabling [`innodb_read_only`](innodb-parameters.md) prevents these operations for all storage engines. Table creation and drop operations for any storage engine modify data dictionary tables in the `mysql` system database, but those tables use the `InnoDB` storage engine and cannot be modified when [`innodb_read_only`](innodb-parameters.md) is enabled. The same principle applies to other table operations that require modifying data dictionary tables. Examples:
	- [`ANALYZE TABLE`](analyze-table.md) fails because it updates table statistics, which are stored in the data dictionary.
	- [``ALTER TABLE               *`tbl_name`*               ENGINE=*`engine_name`*``](alter-table.md) fails because it updates the storage engine designation, which is stored in the data dictionary.
	Note
	Enabling [`innodb_read_only`](innodb-parameters.md) also has important implications for non-data dictionary tables in the `mysql` system database. For details, see the description of [`innodb_read_only`](innodb-parameters.md) in [Section 17.14, “InnoDB Startup Options and System Variables”](innodb-parameters.md)
- Previously, tables in the `mysql` system database were visible to DML and DDL statements. As of MySQL 8.4, data dictionary tables are invisible and cannot be modified or queried directly. However, in most cases there are corresponding `INFORMATION_SCHEMA` tables that can be queried instead. This enables the underlying data dictionary tables to be changed as server development proceeds, while maintaining a stable `INFORMATION_SCHEMA` interface for application use.
- `INFORMATION_SCHEMA` tables in MySQL 8.4 are closely tied to the data dictionary, resulting in several usage differences:
	- Previously, `INFORMATION_SCHEMA` queries for table statistics in the [`STATISTICS`](information-schema-statistics-table.md) and [`TABLES`](information-schema-tables-table.md) tables retrieved statistics directly from storage engines. As of MySQL 8.4, cached table statistics are used by default. The [`information_schema_stats_expiry`](server-system-variables.md) system variable defines the period of time before cached table statistics expire. The default is 86400 seconds (24 hours). (To update the cached values at any time for a given table, use [`ANALYZE               TABLE`](analyze-table.md).) If there are no cached statistics or statistics have expired, statistics are retrieved from storage engines when querying table statistics columns. To always retrieve the latest statistics directly from storage engines, set [`information_schema_stats_expiry`](server-system-variables.md) to `0`. For more information, see [Section 10.2.3, “Optimizing INFORMATION\_SCHEMA Queries”](information-schema-optimization.md).
	- Several `INFORMATION_SCHEMA` tables are views on data dictionary tables, which enables the optimizer to use indexes on those underlying tables. Consequently, depending on optimizer choices, the row order of results for `INFORMATION_SCHEMA` queries might differ from previous results. If a query result must have specific row ordering characteristics, include an `ORDER BY` clause.
	- Queries on `INFORMATION_SCHEMA` tables may return column names in a different lettercase than in earlier MySQL series. Applications should test result set column names in case-insensitive fashion. If that is not feasible, a workaround is to use column aliases in the select list that return column names in the required lettercase. For example:
		```
		SELECT TABLE_SCHEMA AS table_schema, TABLE_NAME AS table_name
		FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'users';
		```
	- [**mysqldump**](mysqldump.md) no longer dumps the `INFORMATION_SCHEMA` database, even if explicitly named on the command line.
	- [``CREATE               TABLE *`dst_tbl`* LIKE               *`src_tbl`*``](create-table-like.md) requires that *`src_tbl`* be a base table and fails if it is an `INFORMATION_SCHEMA` table that is a view on data dictionary tables.
	- Previously, result set headers of columns selected from `INFORMATION_SCHEMA` tables used the capitalization specified in the query. This query produces a result set with a header of `table_name`:
		```
		SELECT table_name FROM INFORMATION_SCHEMA.TABLES;
		```
		As of MySQL 8.4, these headers are capitalized; the preceding query produces a result set with a header of `TABLE_NAME`. If necessary, a column alias can be used to achieve a different lettercase. For example:
		```
		SELECT table_name AS 'table_name' FROM INFORMATION_SCHEMA.TABLES;
		```
- The data directory affects how [**mysqldump**](mysqldump.md) dumps information from the `mysql` system database:
	- [**mysqldump**](mysqldump.md) only dumps non-data dictionary tables in that database, when previously it was possible to dump all tables in the `mysql` system database.
	- Previously, the [`--routines`](mysqldump.md) and [`--events`](mysqldump.md) options were not required to include stored routines and events when using the [`--all-databases`](mysqldump.md) option: The dump included the `mysql` system database, and therefore also the `proc` and `event` tables containing stored routine and event definitions. As of MySQL 8.4, the `event` and `proc` tables are not used. Definitions for the corresponding objects are stored in data dictionary tables, but those tables are not dumped. To include stored routines and events in a dump made using [`--all-databases`](mysqldump.md), use the [`--routines`](mysqldump.md) and [`--events`](mysqldump.md) options explicitly.
	- Previously, the [`--routines`](mysqldump.md) option required the [`SELECT`](privileges-provided.md) privilege for the `proc` table. As of MySQL 8.4, that table is not used; [`--routines`](mysqldump.md) requires the global [`SELECT`](privileges-provided.md) privilege instead.
	- Previously, it was possible to dump stored routine and event definitions together with their creation and modification timestamps, by dumping the `proc` and `event` tables. As of MySQL 8.4, those tables are not used, so it is not possible to dump timestamps.
- Previously, creating a stored routine that contains illegal characters produced a warning. As of MySQL 8.4, this is an error.