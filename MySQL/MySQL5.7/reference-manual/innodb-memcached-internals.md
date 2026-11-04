---
title: "14.21.7 InnoDB memcached Plugin Internals"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/innodb-memcached-internals.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 14.21.7 InnoDB memcached Plugin Internals

#### InnoDB API for the InnoDB memcached Plugin

The `InnoDB` **memcached** engine accesses `InnoDB` through `InnoDB` APIs, most of which are directly adopted from embedded `InnoDB`. `InnoDB` API functions are passed to the `InnoDB` **memcached** engine as callback functions. `InnoDB` API functions access the `InnoDB` tables directly, and are mostly DML operations with the exception of [`TRUNCATE TABLE`](truncate-table.md).

**memcached** commands are implemented through the `InnoDB` **memcached** API. The following table outlines how **memcached** commands are mapped to DML or DDL operations.

**Table 14.21 memcached Commands and Associated DML or DDL Operations**

| memcached Command | DML or DDL Operations |
| --- | --- |
| `get` | a read/fetch command |
| `set` | a search followed by an `INSERT` or `UPDATE` (depending on whether or not a key exists) |
| `add` | a search followed by an `INSERT` or `UPDATE` |
| `replace` | a search followed by an `UPDATE` |
| `append` | a search followed by an `UPDATE` (appends data to the result before `UPDATE`) |
| `prepend` | a search followed by an `UPDATE` (prepends data to the result before `UPDATE`) |
| `incr` | a search followed by an `UPDATE` |
| `decr` | a search followed by an `UPDATE` |
| `delete` | a search followed by a `DELETE` |
| `flush_all` | `TRUNCATE TABLE` (DDL) |

#### InnoDB memcached Plugin Configuration Tables

This section describes configuration tables used by the `daemon_memcached` plugin. The `cache_policies` table, `config_options` table, and `containers` table are created by the `innodb_memcached_config.sql` configuration script in the `innodb_memcache` database.

```
mysql> USE innodb_memcache;
Database changed
mysql> SHOW TABLES;
+---------------------------+
| Tables_in_innodb_memcache |
+---------------------------+
| cache_policies            |
| config_options            |
| containers                |
+---------------------------+
```

#### cache\_policies Table

The `cache_policies` table defines a cache policy for the `InnoDB` `memcached` installation. You can specify individual policies for `get`, `set`, `delete`, and `flush` operations, within a single cache policy. The default setting for all operations is `innodb_only`.

- `innodb_only`: Use `InnoDB` as the data store.
- `cache_only`: Use the **memcached** engine as the data store.
- `caching`: Use both `InnoDB` and the **memcached** engine as data stores. In this case, if **memcached** cannot find a key in memory, it searches for the value in an `InnoDB` table.
- `disable`: Disable caching.

**Table 14.22 cache\_policies Columns**

| Column | Description |
| --- | --- |
| `policy_name` | Name of the cache policy. The default cache policy name is `cache_policy`. |
| `get_policy` | The cache policy for get operations. Valid values are `innodb_only`, `cache_only`, `caching`, or `disabled`. The default setting is `innodb_only`. |
| `set_policy` | The cache policy for set operations. Valid values are `innodb_only`, `cache_only`, `caching`, or `disabled`. The default setting is `innodb_only`. |
| `delete_policy` | The cache policy for delete operations. Valid values are `innodb_only`, `cache_only`, `caching`, or `disabled`. The default setting is `innodb_only`. |
| `flush_policy` | The cache policy for flush operations. Valid values are `innodb_only`, `cache_only`, `caching`, or `disabled`. The default setting is `innodb_only`. |

#### config\_options Table

The `config_options` table stores **memcached** -related settings that can be changed at runtime using SQL. Supported configuration options are `separator` and `table_map_delimiter`.

**Table 14.23 config\_options Columns**

| Column | Description |
| --- | --- |
| `Name` | Name of the **memcached** -related configuration option. The following configuration options are supported by the `config_options` table:  - `separator`: Used to separate values of a long string into separate values when there are multiple `value_columns` defined. By default, the `separator` is a `\|` character. For example, if you define `col1, col2` as value columns, and you define `\|` as the separator, you can issue the following **memcached** command to insert values into `col1` and `col2`, respectively: 	``` 	set keyx 10 0 19 	valuecolx\|valuecoly 	``` 	`valuecol1x` is stored in `col1` and `valuecoly` is stored in `col2`. - `table_map_delimiter`: The character separating the schema name and the table name when you use the `@@` notation in a key name to access a key in a specific table. For example, `@@t1.some_key` and `@@t2.some_key` have the same key value, but are stored in different tables. |
| `Value` | The value assigned to the **memcached** -related configuration option. |

#### containers Table

The `containers` table is the most important of the three configuration tables. Each `InnoDB` table that is used to store **memcached** values must have an entry in the `containers` table. The entry provides a mapping between `InnoDB` table columns and container table columns, which is required for `memcached` to work with `InnoDB` tables.

The `containers` table contains a default entry for the `test.demo_test` table, which is created by the `innodb_memcached_config.sql` configuration script. To use the `daemon_memcached` plugin with your own `InnoDB` table, you must create an entry in the `containers` table.

**Table 14.24 containers Columns**

| Column | Description |
| --- | --- |
| `name` | The name given to the container. If an `InnoDB` table is not requested by name using `@@` notation, the `daemon_memcached` plugin uses the `InnoDB` table with a `containers.name` value of `default`. If there is no such entry, the first entry in the `containers` table, ordered alphabetically by `name` (ascending), determines the default `InnoDB` table. |
| `db_schema` | The name of the database where the `InnoDB` table resides. This is a required value. |
| `db_table` | The name of the `InnoDB` table that stores **memcached** values. This is a required value. |
| `key_columns` | The column in the `InnoDB` table that contains lookup key values for **memcached** operations. This is a required value. |
| `value_columns` | The `InnoDB` table columns (one or more) that store `memcached` data. Multiple columns can be specified using the separator character specified in the `innodb_memcached.config_options` table. By default, the separator is a pipe character (“\|”). To specify multiple columns, separate them with the defined separator character. For example: `col1\|col2\|col3`. This is a required value. |
| `flags` | The `InnoDB` table columns that are used as flags (a user-defined numeric value that is stored and retrieved along with the main value) for **memcached**. A flag value can be used as a column specifier for some operations (such as `incr`, `prepend`) if a **memcached** value is mapped to multiple columns, so that an operation is performed on a specified column. For example, if you have mapped a `value_columns` to three `InnoDB` table columns, and only want the increment operation performed on one columns, use the `flags` column to specify the column. If you do not use the `flags` column, set a value of `0` to indicate that it is unused. |
| `cas_column` | The `InnoDB` table column that stores compare-and-swap (cas) values. The `cas_column` value is related to the way **memcached** hashes requests to different servers and caches data in memory. Because the `InnoDB` **memcached** plugin is tightly integrated with a single **memcached** daemon, and the in-memory caching mechanism is handled by MySQL and the [InnoDB buffer pool](glossary.md), this column is rarely needed. If you do not use this column, set a value of `0` to indicate that it is unused. |
| `expire_time_column` | The `InnoDB` table column that stores expiration values. The `expire_time_column` value is related to the way **memcached** hashes requests to different servers and caches data in memory. Because the `InnoDB` **memcached** plugin is tightly integrated with a single **memcached** daemon, and the in-memory caching mechanism is handled by MySQL and the [InnoDB buffer pool](glossary.md), this column is rarely needed. If you do not use this column, set a value of `0` to indicate that the column is unused. The maximum expire time is defined as `INT_MAX32` or 2147483647 seconds (approximately 68 years). |
| `unique_idx_name_on_key` | The name of the index on the key column. It must be a unique index. It can be the [primary key](glossary.md) or a [secondary index](glossary.md). Preferably, use the primary key of the `InnoDB` table. Using the primary key avoids a lookup that is performed when using a secondary index. You cannot make a [covering index](glossary.md) for **memcached** lookups; `InnoDB` returns an error if you try to define a composite secondary index over both the key and value columns. |

##### containers Table Column Constraints

- You must supply a value for `db_schema`, `db_name`, `key_columns`, `value_columns` and `unique_idx_name_on_key`. Specify `0` for `flags`, `cas_column`, and `expire_time_column` if they are unused. Failing to do so could cause your setup to fail.
- `key_columns`: The maximum limit for a **memcached** key is 250 characters, which is enforced by **memcached**. The mapped key must be a non-Null [`CHAR`](char.md) or [`VARCHAR`](char.md) type.
- `value_columns`: Must be mapped to a [`CHAR`](char.md), [`VARCHAR`](char.md), or [`BLOB`](blob.md) column. There is no length restriction and the value can be NULL.
- `cas_column`: The `cas` value is a 64 bit integer. It must be mapped to a [`BIGINT`](integer-types.md) of at least 8 bytes. If you do not use this column, set a value of `0` to indicate that it is unused.
- `expiration_time_column`: Must mapped to an [`INTEGER`](integer-types.md) of at least 4 bytes. Expiration time is defined as a 32-bit integer for Unix time (the number of seconds since January 1, 1970, as a 32-bit value), or the number of seconds starting from the current time. For the latter, the number of seconds may not exceed 60\*60\*24\*30 (the number of seconds in 30 days). If the number sent by a client is larger, the server considers it to be a real Unix time value rather than an offset from the current time. If you do not use this column, set a value of `0` to indicate that it is unused.
- `flags`: Must be mapped to an [`INTEGER`](integer-types.md) of at least 32-bits and can be NULL. If you do not use this column, set a value of `0` to indicate that it is unused.

A pre-check is performed at plugin load time to enforce column constraints. If mismatches are found, the plugin is not loaded.

##### Multiple Value Column Mapping

- During plugin initialization, when `InnoDB` **memcached** is configured with information defined in the `containers` table, each mapped column defined in `containers.value_columns` is verified against the mapped `InnoDB` table. If multiple `InnoDB` table columns are mapped, there is a check to ensure that each column exists and is the right type.
- At run-time, for `memcached` insert operations, if there are more delimited values than the number of mapped columns, only the number of mapped values are taken. For example, if there are six mapped columns, and seven delimited values are provided, only the first six delimited values are taken. The seventh delimited value is ignored.
- If there are fewer delimited values than mapped columns, unfilled columns are set to NULL. If an unfilled column cannot be set to NULL, insert operations fail.
- If a table has more columns than mapped values, the extra columns do not affect results.

#### The demo\_test Example Table

The `innodb_memcached_config.sql` configuration script creates a `demo_test` table in the `test` database, which can be used to verify `InnoDB` **memcached** plugin installation immediately after setup.

The `innodb_memcached_config.sql` configuration script also creates an entry for the `demo_test` table in the `innodb_memcache.containers` table.

```
mysql> SELECT * FROM innodb_memcache.containers\G
*************************** 1. row ***************************
                  name: aaa
             db_schema: test
              db_table: demo_test
           key_columns: c1
         value_columns: c2
                 flags: c3
            cas_column: c4
    expire_time_column: c5
unique_idx_name_on_key: PRIMARY

mysql> SELECT * FROM test.demo_test;
+----+------------------+------+------+------+
| c1 | c2               | c3   | c4   | c5   |
+----+------------------+------+------+------+
| AA | HELLO, HELLO     |    8 |    0 |    0 |
+----+------------------+------+------+------+
```