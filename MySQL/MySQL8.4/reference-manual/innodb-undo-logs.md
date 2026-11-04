---
title: "17.6.6 Undo Logs"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/innodb-undo-logs.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 17.6.6 Undo Logs

An undo log is a collection of undo log records associated with a single read-write transaction. An undo log record contains information about how to undo the latest change by a transaction to a [clustered index](glossary.md) record. If another transaction needs to see the original data as part of a consistent read operation, the unmodified data is retrieved from undo log records. Undo logs exist within [undo log segments](glossary.md), which are contained within [rollback segments](glossary.md). Rollback segments reside in [undo tablespaces](glossary.md) and in the [global temporary tablespace](glossary.md).

Undo logs that reside in the global temporary tablespace are used for transactions that modify data in user-defined temporary tables. These undo logs are not redo-logged, as they are not required for crash recovery. They are used only for rollback while the server is running. This type of undo log benefits performance by avoiding redo logging I/O.

For information about data-at-rest encryption for undo logs, see [Undo Log Encryption](innodb-data-encryption.md).

Each undo tablespace and the global temporary tablespace individually support a maximum of 128 rollback segments. The [`innodb_rollback_segments`](innodb-parameters.md) variable defines the number of rollback segments.

The number of transactions that a rollback segment supports depends on the number of undo slots in the rollback segment and the number of undo logs required by each transaction. The number of undo slots in a rollback segment differs according to `InnoDB` page size.

| InnoDB Page Size | Number of Undo Slots in a Rollback Segment (InnoDB Page Size / 16) |
| --- | --- |
| `4096 (4KB)` | `256` |
| `8192 (8KB)` | `512` |
| `16384 (16KB)` | `1024` |
| `32768 (32KB)` | `2048` |
| `65536 (64KB)` | `4096` |

A transaction is assigned up to four undo logs, one for each of the following operation types:

Undo logs are assigned as needed. For example, a transaction that performs [`INSERT`](insert.md), [`UPDATE`](update.md), and [`DELETE`](delete.md) operations on regular and temporary tables requires a full assignment of four undo logs. A transaction that performs only [`INSERT`](insert.md) operations on regular tables requires a single undo log.

A transaction that performs operations on regular tables is assigned undo logs from an assigned undo tablespace rollback segment. A transaction that performs operations on temporary tables is assigned undo logs from an assigned global temporary tablespace rollback segment.

An undo log assigned to a transaction remains attached to the transaction for its duration. For example, an undo log assigned to a transaction for an [`INSERT`](insert.md) operation on a regular table is used for all [`INSERT`](insert.md) operations on regular tables performed by that transaction.

Given the factors described above, the following formulas can be used to estimate the number of concurrent read-write transactions that `InnoDB` is capable of supporting.

Note

It is possible to encounter a concurrent transaction limit error before reaching the number of concurrent read-write transactions that `InnoDB` is capable of supporting. This occurs when a rollback segment assigned to a transaction runs out of undo slots. In such cases, try rerunning the transaction.

When transactions perform operations on temporary tables, the number of concurrent read-write transactions that `InnoDB` is capable of supporting is constrained by the number of rollback segments allocated to the global temporary tablespace, which is 128 by default.

- If each transaction performs either an [`INSERT`](insert.md) **or** an [`UPDATE`](update.md) or [`DELETE`](delete.md) operation, the number of concurrent read-write transactions that `InnoDB` is capable of supporting is:
	```
	(innodb_page_size / 16) * innodb_rollback_segments * number of undo tablespaces
	```
- If each transaction performs an [`INSERT`](insert.md) **and** an [`UPDATE`](update.md) or [`DELETE`](delete.md) operation, the number of concurrent read-write transactions that `InnoDB` is capable of supporting is:
	```
	(innodb_page_size / 16 / 2) * innodb_rollback_segments * number of undo tablespaces
	```
- If each transaction performs an [`INSERT`](insert.md) operation on a temporary table, the number of concurrent read-write transactions that `InnoDB` is capable of supporting is:
	```
	(innodb_page_size / 16) * innodb_rollback_segments
	```
- If each transaction performs an [`INSERT`](insert.md) **and** an [`UPDATE`](update.md) or [`DELETE`](delete.md) operation on a temporary table, the number of concurrent read-write transactions that `InnoDB` is capable of supporting is:
	```
	(innodb_page_size / 16 / 2) * innodb_rollback_segments
	```