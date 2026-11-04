---
title: "22.6.4 Partitioning and Locking"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/partitioning-limitations-locking.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 22.6.4 Partitioning and Locking

For storage engines such as [`MyISAM`](myisam-storage-engine.md) that actually execute table-level locks when executing DML or DDL statements, such a statement in older versions of MySQL (5.6.5 and earlier) that affected a partitioned table imposed a lock on the table as a whole; that is, all partitions were locked until the statement was finished. In MySQL 5.7, partition lock pruning eliminates unneeded locks in many cases, and most statements reading from or updating a partitioned `MyISAM` table cause only the effected partitions to be locked. For example, a [`SELECT`](select.md) from a partitioned `MyISAM` table locks only those partitions actually containing rows that satisfy the `SELECT` statement's `WHERE` condition are locked.

For statements affecting partitioned tables using storage engines such as [`InnoDB`](innodb-storage-engine.md), that employ row-level locking and do not actually perform (or need to perform) the locks prior to partition pruning, this is not an issue.

The next few paragraphs discuss the effects of partition lock pruning for various MySQL statements on tables using storage engines that employ table-level locks.

#### Effects on DML statements

[`SELECT`](select.md) statements (including those containing unions or joins) lock only those partitions that actually need to be read. This also applies to `SELECT ... PARTITION`.

An [`UPDATE`](update.md) prunes locks only for tables on which no partitioning columns are updated.

[`REPLACE`](replace.md) and [`INSERT`](insert.md) lock only those partitions having rows to be inserted or replaced. However, if an `AUTO_INCREMENT` value is generated for any partitioning column then all partitions are locked.

[`INSERT ...         ON DUPLICATE KEY UPDATE`](insert-on-duplicate.md) is pruned as long as no partitioning column is updated.

[`INSERT ...         SELECT`](insert-select.md) locks only those partitions in the source table that need to be read, although all partitions in the target table are locked.

Locks imposed by [`LOAD DATA`](load-data.md) statements on partitioned tables cannot be pruned.

The presence of `BEFORE INSERT` or `BEFORE UPDATE` triggers using any partitioning column of a partitioned table means that locks on `INSERT` and `UPDATE` statements updating this table cannot be pruned, since the trigger can alter its values: A `BEFORE INSERT` trigger on any of the table's partitioning columns means that locks set by `INSERT` or `REPLACE` cannot be pruned, since the `BEFORE INSERT` trigger may change a row's partitioning columns before the row is inserted, forcing the row into a different partition than it would be otherwise. A `BEFORE UPDATE` trigger on a partitioning column means that locks imposed by `UPDATE` or `INSERT ... ON DUPLICATE KEY UPDATE` cannot be pruned.

#### Affected DDL statements

[`CREATE VIEW`](create-view.md) does not cause any locks.

[`ALTER         TABLE ... EXCHANGE PARTITION`](alter-table-partition-operations.md) prunes locks; only the exchanged table and the exchanged partition are locked.

[`ALTER         TABLE ... TRUNCATE PARTITION`](alter-table-partition-operations.md) prunes locks; only the partitions to be emptied are locked.

In addition, [`ALTER TABLE`](alter-table.md) statements take metadata locks on the table level.

#### Other statements

[`LOCK TABLES`](lock-tables.md) cannot prune partition locks.

[``CALL         stored_procedure(*`expr`*)``](call.md) supports lock pruning, but evaluating *`expr`* does not.

[`DO`](do.md) and [`SET`](set-variable.md) statements do not support partitioning lock pruning.