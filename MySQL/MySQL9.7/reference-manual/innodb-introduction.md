---
title: "17.1 Introduction to InnoDB"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/innodb-introduction.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

`InnoDB` is a general-purpose storage engine that balances high reliability and high performance. In MySQL 9.7, `InnoDB` is the default MySQL storage engine. Unless you have configured a different default storage engine, issuing a [`CREATE     TABLE`](create-table.md) statement without an `ENGINE` clause creates an `InnoDB` table.

### Key Advantages of InnoDB

- Its DML operations follow the ACID model, with transactions featuring commit, rollback, and crash-recovery capabilities to protect user data. See [Section 17.2, “InnoDB and the ACID Model”](mysql-acid.md).
- Row-level locking and Oracle-style consistent reads increase multi-user concurrency and performance. See [Section 17.7, “InnoDB Locking and Transaction Model”](innodb-locking-transaction-model.md).
- `InnoDB` tables arrange your data on disk to optimize queries based on primary keys. Each `InnoDB` table has a primary key index called the clustered index that organizes the data to minimize I/O for primary key lookups. See [Section 17.6.2.1, “Clustered and Secondary Indexes”](innodb-index-types.md).
- To maintain data integrity, `InnoDB` supports `FOREIGN KEY` constraints. With foreign keys, inserts, updates, and deletes are checked to ensure they do not result in inconsistencies across related tables. See [Section 15.1.24.5, “FOREIGN KEY Constraints”](create-table-foreign-keys.md).

**Table 17.1 InnoDB Storage Engine Features**

| Feature | Support |
| --- | --- |
| **B-tree indexes** | Yes |
| **Backup/point-in-time recovery** (Implemented in the server, rather than in the storage engine.) | Yes |
| **Cluster database support** | No |
| **Clustered indexes** | Yes |
| **Compressed data** | Yes |
| **Data caches** | Yes |
| **Encrypted data** | Yes (Implemented in the server via encryption functions; In MySQL 5.7 and later, data-at-rest encryption is supported.) |
| **Foreign key support** | Yes |
| **Full-text search indexes** | Yes (Support for FULLTEXT indexes is available in MySQL 5.6 and later.) |
| **Geospatial data type support** | Yes |
| **Geospatial indexing support** | Yes (Support for geospatial indexing is available in MySQL 5.7 and later.) |
| **Hash indexes** | No (InnoDB utilizes hash indexes internally for its Adaptive Hash Index feature.) |
| **Index caches** | Yes |
| **Locking granularity** | Row |
| **MVCC** | Yes |
| **Replication support** (Implemented in the server, rather than in the storage engine.) | Yes |
| **Storage limits** | 64TB |
| **T-tree indexes** | No |
| **Transactions** | Yes |
| **Update statistics for data dictionary** | Yes |

To compare the features of `InnoDB` with other storage engines provided with MySQL, see the *Storage Engine Features* table in [Chapter 18, *Alternative Storage Engines*](storage-engines.md).

### InnoDB Enhancements and New Features

For information about `InnoDB` enhancements and new features, refer to:

- The `InnoDB` enhancements list in [Section 1.4, “What Is New in MySQL 9.7”](mysql-nutshell.md).
- The [Release Notes](https://docs.oracle.com/cd/E17952_01/mysql-9.7-relnotes-en/).

### Additional InnoDB Information and Resources

- For `InnoDB` -related terms and definitions, see the [MySQL Glossary](glossary.md).
- For a forum dedicated to the `InnoDB` storage engine, see [MySQL Forums::InnoDB](http://forums.mysql.com/list.php?22).
- `InnoDB` is published under the same GNU GPL License Version 2 (of June 1991) as MySQL. For more information on MySQL licensing, see [http://www.mysql.com/company/legal/licensing/](http://www.mysql.com/company/legal/licensing/).