---
title: "10.4.4 Internal Temporary Table Use in MySQL"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/internal-temporary-tables.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 10.4.4 Internal Temporary Table Use in MySQL

In some cases, the server creates internal temporary tables while processing statements. Users have no direct control over when this occurs.

The server creates temporary tables under conditions such as these:

- Evaluation of [`UNION`](union.md) statements, with some exceptions described later.
- Evaluation of some views, such those that use the `TEMPTABLE` algorithm, [`UNION`](union.md), or aggregation.
- Evaluation of derived tables (see [Section 15.2.15.8, “Derived Tables”](derived-tables.md)).
- Evaluation of common table expressions (see [Section 15.2.20, “WITH (Common Table Expressions)”](with.md)).
- Tables created for subquery or semijoin materialization (see [Section 10.2.2, “Optimizing Subqueries, Derived Tables, View References, and Common Table Expressions”](subquery-optimization.md)).
- Evaluation of statements that contain an `ORDER             BY` clause and a different `GROUP             BY` clause, or for which the `ORDER             BY` or `GROUP BY` contains columns from tables other than the first table in the join queue.
- Evaluation of `DISTINCT` combined with `ORDER BY` may require a temporary table.
- For queries that use the `SQL_SMALL_RESULT` modifier, MySQL uses an in-memory temporary table, unless the query also contains elements (described later) that require on-disk storage.
- To evaluate [`INSERT ...             SELECT`](insert-select.md) statements that select from and insert into the same table, MySQL creates an internal temporary table to hold the rows from the [`SELECT`](select.md), then inserts those rows into the target table. See [Section 15.2.7.1, “INSERT... SELECT Statement”](insert-select.md).
- Evaluation of multiple-table [`UPDATE`](update.md) statements.
- Evaluation of [`GROUP_CONCAT()`](aggregate-functions.md) or [`COUNT(DISTINCT)`](aggregate-functions.md) expressions.
- Evaluation of window functions (see [Section 14.20, “Window Functions”](window-functions.md)) uses temporary tables as necessary.

To determine whether a statement requires a temporary table, use [`EXPLAIN`](explain.md) and check the `Extra` column to see whether it says `Using temporary` (see [Section 10.8.1, “Optimizing Queries with EXPLAIN”](using-explain.md)). `EXPLAIN` does not necessarily say `Using temporary` for derived or materialized temporary tables. For statements that use window functions, [`EXPLAIN`](explain.md) with `FORMAT=JSON` always provides information about the windowing steps. If the windowing functions use temporary tables, it is indicated for each step.

Some query conditions prevent the use of an in-memory temporary table, in which case the server uses an on-disk table instead:

- Presence of a [`BLOB`](blob.md) or [`TEXT`](blob.md) column in the table. However, the `TempTable` storage engine, which is the default storage engine for in-memory internal temporary tables in MySQL 8.0, supports binary large object types as of MySQL 8.0.13. See Internal Temporary Table Storage Engine.
- Presence of any string column with a maximum length larger than 512 (bytes for binary strings, characters for nonbinary strings) in the [`SELECT`](select.md) list, if [`UNION`](union.md) or [`UNION ALL`](union.md) is used.
- The [`SHOW COLUMNS`](show-columns.md) and [`DESCRIBE`](describe.md) statements use `BLOB` as the type for some columns, thus the temporary table used for the results is an on-disk table.

The server does not use a temporary table for [`UNION`](union.md) statements that meet certain qualifications. Instead, it retains from temporary table creation only the data structures necessary to perform result column typecasting. The table is not fully instantiated and no rows are written to or read from it; rows are sent directly to the client. The result is reduced memory and disk requirements, and smaller delay before the first row is sent to the client because the server need not wait until the last query block is executed. [`EXPLAIN`](explain.md) and optimizer trace output reflects this execution strategy: The `UNION RESULT` query block is not present because that block corresponds to the part that reads from the temporary table.

These conditions qualify a `UNION` for evaluation without a temporary table:

- The union is `UNION ALL`, not `UNION` or `UNION             DISTINCT`.
- There is no global `ORDER BY` clause.
- The union is not the top-level query block of an `{INSERT | REPLACE} ... SELECT ...` statement.

#### Internal Temporary Table Storage Engine

An internal temporary table can be held in memory and processed by the `TempTable` or `MEMORY` storage engine, or stored on disk by the `InnoDB` storage engine.

##### Storage Engine for In-Memory Internal Temporary Tables

The [`internal_tmp_mem_storage_engine`](server-system-variables.md) variable defines the storage engine used for in-memory internal temporary tables. Permitted values are `TempTable` (the default) and `MEMORY`.

Note

As of MySQL 8.0.27, configuring a session setting for [`internal_tmp_mem_storage_engine`](server-system-variables.md) requires the [`SESSION_VARIABLES_ADMIN`](privileges-provided.md) or [`SYSTEM_VARIABLES_ADMIN`](privileges-provided.md) privilege.

The `TempTable` storage engine provides efficient storage for [`VARCHAR`](char.md) and [`VARBINARY`](binary-varbinary.md) columns, and other binary large object types as of MySQL 8.0.13.

The following variables control TempTable storage engine limits and behavior:

- [`tmp_table_size`](server-system-variables.md): From MySQL 8.0.28, [`tmp_table_size`](server-system-variables.md) defines the maximum size of any individual in-memory internal temporary table created by the TempTable storage engine. When the [`tmp_table_size`](server-system-variables.md) limit is reached, MySQL automatically converts the in-memory internal temporary table to an `InnoDB` on-disk internal temporary table. The default [`tmp_table_size`](server-system-variables.md) setting is 16777216 bytes (16 MiB).
	The [`tmp_table_size`](server-system-variables.md) limit is intended to prevent individual queries from consuming an inordinate amount global TempTable resources, which can affect the performance of concurrent queries that require TempTable resources. Global TempTable resources are controlled by the [`temptable_max_ram`](server-system-variables.md) and [`temptable_max_mmap`](server-system-variables.md) settings.
	If the [`tmp_table_size`](server-system-variables.md) limit is less than the [`temptable_max_ram`](server-system-variables.md) limit, it is not possible for an in-memory temporary table to contain more data than permitted by the [`tmp_table_size`](server-system-variables.md) limit. If the [`tmp_table_size`](server-system-variables.md) limit is greater than the sum of the [`temptable_max_ram`](server-system-variables.md) and [`temptable_max_mmap`](server-system-variables.md) limits, it is not possible for an in-memory temporary table to contain more than the sum of the [`temptable_max_ram`](server-system-variables.md) and [`temptable_max_mmap`](server-system-variables.md) limits.
- [`temptable_max_ram`](server-system-variables.md): Defines the maximum amount of RAM that can be used by the `TempTable` storage engine before it starts allocating space from memory-mapped files or before MySQL starts using `InnoDB` on-disk internal temporary tables, depending on your configuration. The default [`temptable_max_ram`](server-system-variables.md) setting is 1073741824 bytes (1GiB).
	Note
	The [`temptable_max_ram`](server-system-variables.md) setting does not account for the thread-local memory block allocated to each thread that uses the `TempTable` storage engine. The size of the thread-local memory block depends on the size of the thread's first memory allocation request. If the request is less than 1MB, which it is in most cases, the thread-local memory block size is 1MB. If the request is greater than 1MB, the thread-local memory block is approximately the same size as the initial memory request. The thread-local memory block is held in thread-local storage until thread exit.
- [`temptable_use_mmap`](server-system-variables.md): Controls whether the `TempTable` storage engine allocates space from memory-mapped files or MySQL uses `InnoDB` on-disk internal temporary tables when the [`temptable_max_ram`](server-system-variables.md) limit is exceeded. The default setting is [`temptable_use_mmap=ON`](server-system-variables.md).
	Note
	The [`temptable_use_mmap`](server-system-variables.md) variable was introduced in MySQL 8.0.16 and deprecated in MySQL 8.0.26; expect support for it to be removed in a future version of MySQL. Setting [`temptable_max_mmap=0`](server-system-variables.md) is equivalent to setting [`temptable_use_mmap=OFF`](server-system-variables.md).
- [`temptable_max_mmap`](server-system-variables.md): Introduced in MySQL 8.0.23. Defines the maximum amount of memory the TempTable storage engine is permitted to allocate from memory-mapped files before MySQL starts using `InnoDB` on-disk internal temporary tables. The default setting is 1073741824 bytes (1GiB). The limit is intended to address the risk of memory mapped files using too much space in the temporary directory ([`tmpdir`](server-system-variables.md)). A [`temptable_max_mmap=0`](server-system-variables.md) setting disables allocation from memory-mapped files, effectively disabling their use, regardless of the [`temptable_use_mmap`](server-system-variables.md) setting.

Use of memory-mapped files by the `TempTable` storage engine is governed by these rules:

- Temporary files are created in the directory defined by the [`tmpdir`](server-system-variables.md) variable.
- Temporary files are deleted immediately after they are created and opened, and therefore do not remain visible in the [`tmpdir`](server-system-variables.md) directory. The space occupied by temporary files is held by the operating system while temporary files are open. The space is reclaimed when temporary files are closed by the `TempTable` storage engine, or when the `mysqld` process is shut down.
- Data is never moved between RAM and temporary files, within RAM, or between temporary files.
- New data is stored in RAM if space becomes available within the limit defined by [`temptable_max_ram`](server-system-variables.md). Otherwise, new data is stored in temporary files.
- If space becomes available in RAM after some of the data for a table is written to temporary files, it is possible for the remaining table data to be stored in RAM.

When using the `MEMORY` storage engine for in-memory temporary tables ([`internal_tmp_mem_storage_engine=MEMORY`](server-system-variables.md)), MySQL automatically converts an in-memory temporary table to an on-disk table if it becomes too large. The maximum size of an in-memory temporary table is defined by the [`tmp_table_size`](server-system-variables.md) or [`max_heap_table_size`](server-system-variables.md) value, whichever is smaller. This differs from `MEMORY` tables explicitly created with [`CREATE TABLE`](create-table.md). For such tables, only the [`max_heap_table_size`](server-system-variables.md) variable determines how large a table can grow, and there is no conversion to on-disk format.

##### Storage Engine for On-Disk Internal Temporary Tables

In MySQL 8.0.15 and earlier, the [`internal_tmp_disk_storage_engine`](server-system-variables.md) variable defined the storage engine used for on-disk internal temporary tables. Supported storage engines were `InnoDB` and `MyISAM`.

From MySQL 8.0.16, MySQL uses only the `InnoDB` storage engine for on-disk internal temporary tables. The `MYISAM` storage engine is no longer supported for this purpose.

`InnoDB` on-disk internal temporary tables are created in session temporary tablespaces that reside in the data directory by default. For more information, see [Section 17.6.3.5, “Temporary Tablespaces”](innodb-temporary-tablespace.md).

In MySQL 8.0.15 and earlier:

- For common table expressions (CTEs), the storage engine used for on-disk internal temporary tables cannot be `MyISAM`. If [`internal_tmp_disk_storage_engine=MYISAM`](server-system-variables.md), an error occurs for any attempt to materialize a CTE using an on-disk temporary table.
- When using [`internal_tmp_disk_storage_engine=INNODB`](server-system-variables.md), queries that generate on-disk internal temporary tables that exceed `InnoDB` row or column limits return Row size too large or Too many columns errors. The workaround is to set [`internal_tmp_disk_storage_engine`](server-system-variables.md) to `MYISAM`.

#### Internal Temporary Table Storage Format

When in-memory internal temporary tables are managed by the `TempTable` storage engine, rows that include `VARCHAR` columns, `VARBINARY` columns, and other binary large object type columns (supported as of MySQL 8.0.13) are represented in memory by an array of cells, with each cell containing a NULL flag, the data length, and a data pointer. Column values are placed in consecutive order after the array, in a single region of memory, without padding. Each cell in the array uses 16 bytes of storage. The same storage format applies when the `TempTable` storage engine allocates space from memory-mapped files.

When in-memory internal temporary tables are managed by the `MEMORY` storage engine, fixed-length row format is used. `VARCHAR` and `VARBINARY` column values are padded to the maximum column length, in effect storing them as `CHAR` and `BINARY` columns.

Prior to MySQL 8.0.16, on-disk internal temporary tables were managed by the `InnoDB` or `MyISAM` storage engine (depending on the [`internal_tmp_disk_storage_engine`](server-system-variables.md) setting). Both engines store internal temporary tables using dynamic-width row format. Columns take only as much storage as needed, which reduces disk I/O, space requirements, and processing time compared to on-disk tables that use fixed-length rows. Beginning with MySQL 8.0.16, [`internal_tmp_disk_storage_engine`](server-system-variables.md) is not supported, and internal temporary tables on disk are always managed by `InnoDB`.

When using the `MEMORY` storage engine, statements can initially create an in-memory internal temporary table and then convert it to an on-disk table if the table becomes too large. In such cases, better performance might be achieved by skipping the conversion and creating the internal temporary table on disk to begin with. The [`big_tables`](server-system-variables.md) variable can be used to force disk storage of internal temporary tables.

#### Monitoring Internal Temporary Table Creation

When an internal temporary table is created in memory or on disk, the server increments the [`Created_tmp_tables`](server-status-variables.md) value. When an internal temporary table is created on disk, the server increments the [`Created_tmp_disk_tables`](server-status-variables.md) value. If too many internal temporary tables are created on disk, consider adjusting the engine-specific limits described in Internal Temporary Table Storage Engine.

Note

Due to a known limitation, [`Created_tmp_disk_tables`](server-status-variables.md) does not count on-disk temporary tables created in memory-mapped files. By default, the TempTable storage engine overflow mechanism creates internal temporary tables in memory-mapped files. See Internal Temporary Table Storage Engine.

The `memory/temptable/physical_ram` and `memory/temptable/physical_disk` Performance Schema instruments can be used to monitor `TempTable` space allocation from memory and disk. `memory/temptable/physical_ram` reports the amount of allocated RAM. `memory/temptable/physical_disk` reports the amount of space allocated from disk when memory-mapped files are used as the TempTable overflow mechanism. If the `physical_disk` instrument reports a value other than 0 and memory-mapped files are used as the TempTable overflow mechanism, a TempTable memory limit was reached at some point. Data can be queried in Performance Schema memory summary tables such as [`memory_summary_global_by_event_name`](performance-schema-memory-summary-tables.md). See [Section 29.12.20.10, “Memory Summary Tables”](performance-schema-memory-summary-tables.md).