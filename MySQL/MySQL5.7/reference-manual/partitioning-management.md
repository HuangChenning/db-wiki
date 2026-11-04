---
title: "22.3 Partition Management"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/partitioning-management.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

MySQL 5.7 provides a number of ways to modify partitioned tables. It is possible to add, drop, redefine, merge, or split existing partitions. All of these actions can be carried out using the partitioning extensions to the [`ALTER       TABLE`](alter-table-partition-operations.md) statement. There are also ways to obtain information about partitioned tables and partitions. We discuss these topics in the sections that follow.

- For information about partition management in tables partitioned by `RANGE` or `LIST`, see [Section 22.3.1, “Management of RANGE and LIST Partitions”](partitioning-management-range-list.md).
- For a discussion of managing `HASH` and `KEY` partitions, see [Section 22.3.2, “Management of HASH and KEY Partitions”](partitioning-management-hash-key.md).
- See [Section 22.3.5, “Obtaining Information About Partitions”](partitioning-info.md), for a discussion of mechanisms provided in MySQL 5.7 for obtaining information about partitioned tables and partitions.
- For a discussion of performing maintenance operations on partitions, see [Section 22.3.4, “Maintenance of Partitions”](partitioning-maintenance.md).

Note

In MySQL 5.7, all partitions of a partitioned table must have the same number of subpartitions, and it is not possible to change the subpartitioning once the table has been created.

To change a table's partitioning scheme, it is necessary only to use the [`ALTER       TABLE`](alter-table-partition-operations.md) statement with a *`partition_options`* clause. This clause has the same syntax as that as used with [`CREATE TABLE`](create-table.md) for creating a partitioned table, and always begins with the keywords `PARTITION BY`. Suppose that you have a table partitioned by range using the following [`CREATE TABLE`](create-table.md) statement:

```
CREATE TABLE trb3 (id INT, name VARCHAR(50), purchased DATE)
    PARTITION BY RANGE( YEAR(purchased) ) (
        PARTITION p0 VALUES LESS THAN (1990),
        PARTITION p1 VALUES LESS THAN (1995),
        PARTITION p2 VALUES LESS THAN (2000),
        PARTITION p3 VALUES LESS THAN (2005)
    );
```

To repartition this table so that it is partitioned by key into two partitions using the `id` column value as the basis for the key, you can use this statement:

```
ALTER TABLE trb3 PARTITION BY KEY(id) PARTITIONS 2;
```

This has the same effect on the structure of the table as dropping the table and re-creating it using `CREATE TABLE trb3       PARTITION BY KEY(id) PARTITIONS 2;`.

`ALTER TABLE ... ENGINE = ...` changes only the storage engine used by the table, and leaves the table's partitioning scheme intact. Use `ALTER TABLE ... REMOVE       PARTITIONING` to remove a table's partitioning. See [Section 13.1.8, “ALTER TABLE Statement”](alter-table.md).

Important

Only a single `PARTITION BY`, `ADD         PARTITION`, `DROP PARTITION`, `REORGANIZE PARTITION`, or `COALESCE         PARTITION` clause can be used in a given [`ALTER         TABLE`](alter-table-partition-operations.md) statement. If you (for example) wish to drop a partition and reorganize a table's remaining partitions, you must do so in two separate [`ALTER         TABLE`](alter-table-partition-operations.md) statements (one using `DROP         PARTITION` and then a second one using `REORGANIZE PARTITION`).

In MySQL 5.7, it is possible to delete all rows from one or more selected partitions using [`ALTER TABLE ...       TRUNCATE PARTITION`](alter-table.md).