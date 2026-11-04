---
title: "18.5 The ARCHIVE Storage Engine"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/archive-storage-engine.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

The `ARCHIVE` storage engine produces special-purpose tables that store large amounts of unindexed data in a very small footprint.

**Table 18.5 ARCHIVE Storage Engine Features**

| Feature | Support |
| --- | --- |
| **B-tree indexes** | No |
| **Backup/point-in-time recovery** (Implemented in the server, rather than in the storage engine.) | Yes |
| **Cluster database support** | No |
| **Clustered indexes** | No |
| **Compressed data** | Yes |
| **Data caches** | No |
| **Encrypted data** | Yes (Implemented in the server via encryption functions.) |
| **Foreign key support** | No |
| **Full-text search indexes** | No |
| **Geospatial data type support** | Yes |
| **Geospatial indexing support** | No |
| **Hash indexes** | No |
| **Index caches** | No |
| **Locking granularity** | Row |
| **MVCC** | No |
| **Replication support** (Implemented in the server, rather than in the storage engine.) | Yes |
| **Storage limits** | None |
| **T-tree indexes** | No |
| **Transactions** | No |
| **Update statistics for data dictionary** | Yes |

The `ARCHIVE` storage engine is included in MySQL binary distributions. To enable this storage engine if you build MySQL from source, invoke **CMake** with the [`-DWITH_ARCHIVE_STORAGE_ENGINE`](source-configuration-options.md) option.

To examine the source for the `ARCHIVE` engine, look in the `storage/archive` directory of a MySQL source distribution.

You can check whether the `ARCHIVE` storage engine is available with the [`SHOW ENGINES`](show-engines.md) statement.

When you create an `ARCHIVE` table, the storage engine creates files with names that begin with the table name. The data file has an extension of `.ARZ`. An `.ARN` file may appear during optimization operations.

The `ARCHIVE` engine supports [`INSERT`](insert.md), [`REPLACE`](replace.md), and [`SELECT`](select.md), but not [`DELETE`](delete.md) or [`UPDATE`](update.md). It does support `ORDER BY` operations, [`BLOB`](blob.md) columns, and spatial data types (see [Section 13.4.1, “Spatial Data Types”](spatial-type-overview.md)). Geographic spatial reference systems are not supported. The `ARCHIVE` engine uses row-level locking.

The `ARCHIVE` engine supports the `AUTO_INCREMENT` column attribute. The `AUTO_INCREMENT` column can have either a unique or nonunique index. Attempting to create an index on any other column results in an error. The `ARCHIVE` engine also supports the `AUTO_INCREMENT` table option in [`CREATE TABLE`](create-table.md) statements to specify the initial sequence value for a new table or reset the sequence value for an existing table, respectively.

`ARCHIVE` does not support inserting a value into an `AUTO_INCREMENT` column less than the current maximum column value. Attempts to do so result in an [`ER_DUP_KEY`](https://docs.oracle.com/cd/E17952_01/mysql-errors-8.4-en/server-error-reference.html#error_er_dup_key) error.

The `ARCHIVE` engine ignores [`BLOB`](blob.md) columns if they are not requested and scans past them while reading.

The `ARCHIVE` storage engine does not support partitioning.

**Storage:** Rows are compressed as they are inserted. The `ARCHIVE` engine uses `zlib` lossless data compression (see [http://www.zlib.net/](http://www.zlib.net/)). You can use [`OPTIMIZE TABLE`](optimize-table.md) to analyze the table and pack it into a smaller format (for a reason to use [`OPTIMIZE TABLE`](optimize-table.md), see later in this section). The engine also supports [`CHECK     TABLE`](check-table.md). There are several types of insertions that are used:

- An [`INSERT`](insert.md) statement just pushes rows into a compression buffer, and that buffer flushes as necessary. The insertion into the buffer is protected by a lock. A [`SELECT`](select.md) forces a flush to occur.
- A bulk insert is visible only after it completes, unless other inserts occur at the same time, in which case it can be seen partially. A [`SELECT`](select.md) never causes a flush of a bulk insert unless a normal insert occurs while it is loading.

**Retrieval**: On retrieval, rows are uncompressed on demand; there is no row cache. A [`SELECT`](select.md) operation performs a complete table scan: When a [`SELECT`](select.md) occurs, it finds out how many rows are currently available and reads that number of rows. [`SELECT`](select.md) is performed as a consistent read. Note that lots of [`SELECT`](select.md) statements during insertion can deteriorate the compression, unless only bulk inserts are used. To achieve better compression, you can use [`OPTIMIZE TABLE`](optimize-table.md) or [`REPAIR TABLE`](repair-table.md). The number of rows in `ARCHIVE` tables reported by [`SHOW TABLE STATUS`](show-table-status.md) is always accurate. See [Section 15.7.3.4, “OPTIMIZE TABLE Statement”](optimize-table.md), [Section 15.7.3.5, “REPAIR TABLE Statement”](repair-table.md), and [Section 15.7.7.38, “SHOW TABLE STATUS Statement”](show-table-status.md).

### Additional Resources

- A forum dedicated to the `ARCHIVE` storage engine is available at [https://forums.mysql.com/list.php?112](https://forums.mysql.com/list.php?112).