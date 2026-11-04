---
title: "MySQL :: MySQL 26.7 Reference Manual :: 26.3.4 Maintenance of Partitions"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/partitioning-maintenance.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 26.3.4 Maintenance of Partitions

A number of table and partition maintenance tasks can be carried out on partitioned tables using SQL statements intended for such purposes.

Table maintenance of partitioned tables can be accomplished using the statements [`CHECK TABLE`](check-table.md), [`OPTIMIZE TABLE`](optimize-table.md), [`ANALYZE TABLE`](analyze-table.md), and [`REPAIR TABLE`](repair-table.md), which are supported for partitioned tables.

You can use a number of extensions to [`ALTER         TABLE`](alter-table-partition-operations.md) for performing operations of this type on one or more partitions directly, as described in the following list:

- **Rebuilding partitions.** Rebuilds the partition; this has the same effect as dropping all records stored in the partition, then reinserting them. This can be useful for purposes of defragmentation.
	Example:
	```sql
	ALTER TABLE t1 REBUILD PARTITION p0, p1;
	```
- **Optimizing partitions.** If you have deleted a large number of rows from a partition or if you have made many changes to a partitioned table with variable-length rows (that is, having [`VARCHAR`](char.md), [`BLOB`](blob.md), or [`TEXT`](blob.md) columns), you can use [`ALTER               TABLE ... OPTIMIZE PARTITION`](alter-table-partition-operations.md) to reclaim any unused space and to defragment the partition data file.
	Example:
	```sql
	ALTER TABLE t1 OPTIMIZE PARTITION p0, p1;
	```
	Using `OPTIMIZE PARTITION` on a given partition is equivalent to running `CHECK             PARTITION`, `ANALYZE PARTITION`, and `REPAIR PARTITION` on that partition.
	Some MySQL storage engines, including [`InnoDB`](innodb-storage-engine.md), do not support per-partition optimization; in these cases, [`ALTER             TABLE ... OPTIMIZE PARTITION`](alter-table-partition-operations.md) analyzes and rebuilds the entire table, and causes an appropriate warning to be issued. (Bug #11751825, Bug #42822) Use `ALTER TABLE             ... REBUILD PARTITION` and `ALTER TABLE ...             ANALYZE PARTITION` instead, to avoid this issue.
- **Analyzing partitions.** This reads and stores the key distributions for partitions.
	Example:
	```sql
	ALTER TABLE t1 ANALYZE PARTITION p3;
	```
- **Repairing partitions.** This repairs corrupted partitions.
	Example:
	```sql
	ALTER TABLE t1 REPAIR PARTITION p0,p1;
	```
	Normally, `REPAIR PARTITION` fails when the partition contains duplicate key errors. You can use [`ALTER             IGNORE TABLE`](alter-table-partition-operations.md) with this option, in which case all rows that cannot be moved due to the presence of duplicate keys are removed from the partition (Bug #16900947).
- **Checking partitions.** You can check partitions for errors in much the same way that you can use `CHECK TABLE` with nonpartitioned tables.
	Example:
	```sql
	ALTER TABLE trb3 CHECK PARTITION p1;
	```
	This statement tells you whether the data or indexes in partition `p1` of table `t1` are corrupted. If this is the case, use [`ALTER             TABLE ... REPAIR PARTITION`](alter-table-partition-operations.md) to repair the partition.
	Normally, `CHECK PARTITION` fails when the partition contains duplicate key errors. You can use [`ALTER             IGNORE TABLE`](alter-table-partition-operations.md) with this option, in which case the statement returns the contents of each row in the partition where a duplicate key violation is found. Only the values for the columns in the partitioning expression for the table are reported. (Bug #16900947)

Each of the statements in the list just shown also supports the keyword `ALL` in place of the list of partition names. Using `ALL` causes the statement to act on all partitions in the table.

You can also truncate partitions using [`ALTER TABLE ...         TRUNCATE PARTITION`](alter-table.md). This statement can be used to delete all rows from one or more partitions in much the same way that [`TRUNCATE TABLE`](truncate-table.md) deletes all rows from a table.

[`ALTER TABLE ...         TRUNCATE PARTITION ALL`](alter-table.md) truncates all partitions in the table.