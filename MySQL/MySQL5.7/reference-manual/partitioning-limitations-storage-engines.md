---
title: "22.6.2 Partitioning Limitations Relating to Storage Engines"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/partitioning-limitations-storage-engines.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 22.6.2 Partitioning Limitations Relating to Storage Engines

The following limitations apply to the use of storage engines with user-defined partitioning of tables.

**MERGE storage engine.** User-defined partitioning and the `MERGE` storage engine are not compatible. Tables using the `MERGE` storage engine cannot be partitioned. Partitioned tables cannot be merged.

**FEDERATED storage engine.** Partitioning of `FEDERATED` tables is not supported; it is not possible to create partitioned `FEDERATED` tables.

**CSV storage engine.** Partitioned tables using the `CSV` storage engine are not supported; it is not possible to create partitioned `CSV` tables.

**InnoDB storage engine.** [`InnoDB`](innodb-storage-engine.md) foreign keys and MySQL partitioning are not compatible. Partitioned `InnoDB` tables cannot have foreign key references, nor can they have columns referenced by foreign keys. `InnoDB` tables which have or which are referenced by foreign keys cannot be partitioned.

`InnoDB` does not support the use of multiple disks for subpartitions. (This is currently supported only by `MyISAM`.)

In addition, [`ALTER         TABLE ... OPTIMIZE PARTITION`](alter-table-partition-operations.md) does not work correctly with partitioned tables that use the `InnoDB` storage engine. Use `ALTER TABLE ... REBUILD         PARTITION` and `ALTER TABLE ... ANALYZE         PARTITION`, instead, for such tables. For more information, see [Section 13.1.8.1, “ALTER TABLE Partition Operations”](alter-table-partition-operations.md).

**User-defined partitioning and the NDB storage engine (NDB Cluster).** Partitioning by `KEY` (including `LINEAR KEY`) is the only type of partitioning supported for the [`NDB`](mysql-cluster.md) storage engine. It is not possible under normal circumstances in NDB Cluster to create an NDB Cluster table using any partitioning type other than \[`LINEAR`\] `KEY`, and attempting to do so fails with an error.

*Exception (not for production)*: It is possible to override this restriction by setting the [`new`](server-system-variables.md) system variable on NDB Cluster SQL nodes to `ON`. If you choose to do this, you should be aware that tables using partitioning types other than `[LINEAR] KEY` are not supported in production. *In such cases, you can create and use tables with partitioning types other than `KEY` or `LINEAR KEY`, but you do this entirely at your own risk*. You should also be aware that this functionality is now deprecated and subject to removal without further notice in a future release of NDB Cluster.

The maximum number of partitions that can be defined for an [`NDB`](mysql-cluster.md) table depends on the number of data nodes and node groups in the cluster, the version of the NDB Cluster software in use, and other factors. See [NDB and user-defined partitioning](mysql-cluster-nodes-groups.md), for more information.

As of MySQL NDB Cluster 7.5.2, the maximum amount of fixed-size data that can be stored per partition in an `NDB` table is 128 TB. Previously, this was 16 GB.

[`CREATE TABLE`](create-table.md) and [`ALTER         TABLE`](alter-table-partition-operations.md) statements that would cause a user-partitioned [`NDB`](mysql-cluster.md) table not to meet either or both of the following two requirements are not permitted, and fail with an error:

1. The table must have an explicit primary key.
2. All columns listed in the table's partitioning expression must be part of the primary key.

**Exception.** If a user-partitioned [`NDB`](mysql-cluster.md) table is created using an empty column-list (that is, using `PARTITION BY KEY()` or `PARTITION BY           LINEAR KEY()`), then no explicit primary key is required.

**Partition selection.** Partition selection is not supported for [`NDB`](mysql-cluster.md) tables. See [Section 22.5, “Partition Selection”](partitioning-selection.md), for more information.

**Upgrading partitioned tables.** When performing an upgrade, tables which are partitioned by `KEY` and which use any storage engine other than [`NDB`](mysql-cluster.md) must be dumped and reloaded.

**Same storage engine for all partitions.** All partitions of a partitioned table must use the same storage engine and it must be the same storage engine used by the table as a whole. In addition, if one does not specify an engine on the table level, then one must do either of the following when creating or altering a partitioned table:

- Do *not* specify any engine for *any* partition or subpartition
- Specify the engine for *all* partitions or subpartitions