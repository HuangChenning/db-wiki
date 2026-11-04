---
title: "MySQL :: MySQL 26.7 Reference Manual :: 18 Alternative Storage Engines"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/storage-engines.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

## Chapter 18 Alternative Storage Engines

Storage engines are MySQL components that handle the SQL operations for different table types. [`InnoDB`](innodb-storage-engine.md) is the default and most general-purpose storage engine, and Oracle recommends using it for tables except for specialized use cases. (The [`CREATE TABLE`](create-table.md) statement in MySQL 26.7 creates `InnoDB` tables by default.)

MySQL Server uses a pluggable storage engine architecture that enables storage engines to be loaded into and unloaded from a running MySQL server.

To determine which storage engines your server supports, use the [`SHOW ENGINES`](show-engines.md) statement. The value in the `Support` column indicates whether an engine can be used. A value of `YES`, `NO`, or `DEFAULT` indicates that an engine is available, not available, or available and currently set as the default storage engine.

```sql
mysql> SHOW ENGINES\G
*************************** 1. row ***************************
      Engine: PERFORMANCE_SCHEMA
     Support: YES
     Comment: Performance Schema
Transactions: NO
          XA: NO
  Savepoints: NO
*************************** 2. row ***************************
      Engine: InnoDB
     Support: DEFAULT
     Comment: Supports transactions, row-level locking, and foreign keys
Transactions: YES
          XA: YES
  Savepoints: YES
*************************** 3. row ***************************
      Engine: MRG_MYISAM
     Support: YES
     Comment: Collection of identical MyISAM tables
Transactions: NO
          XA: NO
  Savepoints: NO
*************************** 4. row ***************************
      Engine: BLACKHOLE
     Support: YES
     Comment: /dev/null storage engine (anything you write to it disappears)
Transactions: NO
          XA: NO
  Savepoints: NO
*************************** 5. row ***************************
      Engine: MyISAM
     Support: YES
     Comment: MyISAM storage engine
Transactions: NO
          XA: NO
  Savepoints: NO
...
```

This chapter covers use cases for special-purpose MySQL storage engines. It does not cover the default [`InnoDB`](innodb-storage-engine.md) storage engine or the [`NDB`](mysql-cluster.md) storage engine which are covered in [Chapter 17, *The InnoDB Storage Engine*](innodb-storage-engine.md) and [Chapter 25, *MySQL NDB Cluster 26.7*](mysql-cluster.md). For advanced users, it also contains a description of the pluggable storage engine architecture (see [Section 18.11, “Overview of MySQL Storage Engine Architecture”](pluggable-storage-overview.md)).

For information about features offered in commercial MySQL Server binaries, see [*MySQL Editions*](https://www.mysql.com/products/), on the MySQL website. The storage engines available might depend on which edition of MySQL you are using.

For answers to commonly asked questions about MySQL storage engines, see [Section A.2, “MySQL 26.7 FAQ: Storage Engines”](faqs-storage-engines.md).

## MySQL 26.7 Supported Storage Engines

- [`InnoDB`](innodb-storage-engine.md): The default storage engine in MySQL 26.7. `InnoDB` is a transaction-safe (ACID compliant) storage engine for MySQL that has commit, rollback, and crash-recovery capabilities to protect user data. `InnoDB` row-level locking (without escalation to coarser granularity locks) and Oracle-style consistent nonlocking reads increase multi-user concurrency and performance. `InnoDB` stores user data in clustered indexes to reduce I/O for common queries based on primary keys. To maintain data integrity, `InnoDB` also supports `FOREIGN         KEY` referential-integrity constraints. For more information about `InnoDB`, see [Chapter 17, *The InnoDB Storage Engine*](innodb-storage-engine.md).
- [`MyISAM`](myisam-storage-engine.md): These tables have a small footprint. [Table-level locking](glossary.md) limits the performance in read/write workloads, so it is often used in read-only or read-mostly workloads in Web and data warehousing configurations.
- [`Memory`](memory-storage-engine.md): Stores all data in RAM, for fast access in environments that require quick lookups of non-critical data. This engine was formerly known as the `HEAP` engine. Its use cases are decreasing; `InnoDB` with its buffer pool memory area provides a general-purpose and durable way to keep most or all data in memory, and `NDBCLUSTER` provides fast key-value lookups for huge distributed data sets.
- [`CSV`](csv-storage-engine.md): Its tables are really text files with comma-separated values. CSV tables let you import or dump data in CSV format, to exchange data with scripts and applications that read and write that same format. Because CSV tables are not indexed, you typically keep the data in `InnoDB` tables during normal operation, and only use CSV tables during the import or export stage.
- [`Archive`](archive-storage-engine.md): These compact, unindexed tables are intended for storing and retrieving large amounts of seldom-referenced historical, archived, or security audit information.
- [`Blackhole`](blackhole-storage-engine.md): The Blackhole storage engine accepts but does not store data, similar to the Unix `/dev/null` device. Queries always return an empty set. These tables can be used in replication configurations where DML statements are sent to replica servers, but the source server does not keep its own copy of the data.
- [`NDB`](mysql-cluster.md) (also known as [`NDBCLUSTER`](mysql-cluster.md)): This clustered database engine is particularly suited for applications that require the highest possible degree of uptime and availability.
- [`Merge`](merge-storage-engine.md): Enables a MySQL DBA or developer to logically group a series of identical `MyISAM` tables and reference them as one object. Good for VLDB environments such as data warehousing.
- [`Federated`](federated-storage-engine.md): Offers the ability to link separate MySQL servers to create one logical database from many physical servers. Very good for distributed or data mart environments.
- [`Example`](example-storage-engine.md): This engine serves as an example in the MySQL source code that illustrates how to begin writing new storage engines. It is primarily of interest to developers. The storage engine is a “stub” that does nothing. You can create tables with this engine, but no data can be stored in them or retrieved from them.

You are not restricted to using the same storage engine for an entire server or schema. You can specify the storage engine for any table. For example, an application might use mostly `InnoDB` tables, with one `CSV` table for exporting data to a spreadsheet and a few `MEMORY` tables for temporary workspaces.

**Choosing a Storage Engine**

The various storage engines provided with MySQL are designed with different use cases in mind. The following table provides an overview of some storage engines provided with MySQL, with clarifying notes following the table.

**Table 18.1 Storage Engines Feature Summary**

| Feature | MyISAM | Memory | InnoDB | Archive | NDB |
| --- | --- | --- | --- | --- | --- |
| B-tree indexes | Yes | Yes | Yes | No | No |
| Backup/point-in-time recovery (note 1) | Yes | Yes | Yes | Yes | Yes |
| Cluster database support | No | No | No | No | Yes |
| Clustered indexes | No | No | Yes | No | No |
| Compressed data | Yes (note 2) | No | Yes | Yes | No |
| Data caches | No | N/A | Yes | No | Yes |
| Encrypted data | Yes (note 3) | Yes (note 3) | Yes (note 4) | Yes (note 3) | Yes (note 5) |
| Foreign key support | No | No | Yes | No | Yes |
| Full-text search indexes | Yes | No | Yes (note 6) | No | No |
| Geospatial data type support | Yes | No | Yes | Yes | Yes |
| Geospatial indexing support | Yes | No | Yes (note 7) | No | No |
| Hash indexes | No | Yes | No (note 8) | No | Yes |
| Index caches | Yes | N/A | Yes | No | Yes |
| Locking granularity | Table | Table | Row | Row | Row |
| MVCC | No | No | Yes | No | No |
| Replication support (note 1) | Yes | Limited (note 9) | Yes | Yes | Yes |
| Storage limits | 256TB | RAM | 64TB | None | 384EB |
| T-tree indexes | No | No | No | No | Yes |
| Transactions | No | No | Yes | No | Yes |
| Update statistics for data dictionary | Yes | Yes | Yes | Yes | Yes |

**Notes:**

1\. Implemented in the server, rather than in the storage engine.

2\. Compressed MyISAM tables are supported only when using the compressed row format. Tables using the compressed row format with MyISAM are read only.

3\. Implemented in the server via encryption functions.

4\. Implemented in the server via encryption functions; In MySQL 5.7 and later, data-at-rest encryption is supported.

5\. Implemented in the server via encryption functions; encrypted NDB backups as of NDB 8.0.22; transparent NDB file system encryption supported in NDB 8.0.29 and later.

6\. Support for FULLTEXT indexes is available in MySQL 5.6 and later.

7\. Support for geospatial indexing is available in MySQL 5.7 and later.

8\. InnoDB utilizes hash indexes internally for its Adaptive Hash Index feature.

9\. See the discussion later in this section.