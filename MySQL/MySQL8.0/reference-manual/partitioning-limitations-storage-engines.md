---
title: "26.6.2 Partitioning Limitations Relating to Storage Engines"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/partitioning-limitations-storage-engines.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 26.6.2 Partitioning Limitations Relating to Storage Engines

In MySQL 8.0, partitioning support is not actually provided by the MySQL Server, but rather by a table storage engine's own or native partitioning handler. In MySQL 8.0, only the [`InnoDB`](innodb-storage-engine.md) and [`NDB`](mysql-cluster.md) storage engines provide native partitioning handlers. This means that partitioned tables cannot be created using any other storage engine than these. (You must be using MySQL NDB Cluster with the `NDB` storage engine to create `NDB` tables.)

**InnoDB storage engine.** [`InnoDB`](innodb-storage-engine.md) foreign keys and MySQL partitioning are not compatible. Partitioned `InnoDB` tables cannot have foreign key references, nor can they have columns referenced by foreign keys. `InnoDB` tables which have or which are referenced by foreign keys cannot be partitioned.

[`ALTER         TABLE ... OPTIMIZE PARTITION`](alter-table-partition-operations.md) does not work correctly with partitioned tables that use `InnoDB`. Use `ALTER TABLE ... REBUILD PARTITION` and `ALTER TABLE ... ANALYZE PARTITION`, instead, for such tables. For more information, see [Section 15.1.9.1, “ALTER TABLE Partition Operations”](alter-table-partition-operations.md).

**User-defined partitioning and the NDB storage engine (NDB Cluster).** Partitioning by `KEY` (including `LINEAR KEY`) is the only type of partitioning supported for the [`NDB`](mysql-cluster.md) storage engine. It is not possible under normal circumstances in NDB Cluster to create an NDB Cluster table using any partitioning type other than \[`LINEAR`\] `KEY`, and attempting to do so fails with an error.

*Exception (not for production)*: It is possible to override this restriction by setting the [`new`](server-system-variables.md) system variable on NDB Cluster SQL nodes to `ON`. If you choose to do this, you should be aware that tables using partitioning types other than `[LINEAR] KEY` are not supported in production. *In such cases, you can create and use tables with partitioning types other than `KEY` or `LINEAR KEY`, but you do this entirely at your own risk*. You should also be aware that this functionality is now deprecated and subject to removal without further notice in a future release of NDB Cluster.

The maximum number of partitions that can be defined for an [`NDB`](mysql-cluster.md) table depends on the number of data nodes and node groups in the cluster, the version of the NDB Cluster software in use, and other factors. See [NDB and user-defined partitioning](mysql-cluster-nodes-groups.md), for more information.

The maximum amount of fixed-size data that can be stored per partition in an `NDB` table is 128 TB. Previously, this was 16 GB.

[`CREATE TABLE`](create-table.md) and [`ALTER         TABLE`](alter-table-partition-operations.md) statements that would cause a user-partitioned [`NDB`](mysql-cluster.md) table not to meet either or both of the following two requirements are not permitted, and fail with an error:

1. The table must have an explicit primary key.
2. All columns listed in the table's partitioning expression must be part of the primary key.

**Exception.** If a user-partitioned [`NDB`](mysql-cluster.md) table is created using an empty column-list (that is, using `PARTITION BY KEY()` or `PARTITION BY           LINEAR KEY()`), then no explicit primary key is required.

**Partition selection.** Partition selection is not supported for [`NDB`](mysql-cluster.md) tables. See [Section 26.5, “Partition Selection”](partitioning-selection.md), for more information.

**Upgrading partitioned tables.** When performing an upgrade, tables which are partitioned by `KEY` must be dumped and reloaded. Partitioned tables using storage engines other than `InnoDB` cannot be upgraded from MySQL 5.7 or earlier to MySQL 8.0 or later; you must either drop the partitioning from such tables with `ALTER TABLE ...           REMOVE PARTITIONING` or convert them to `InnoDB` using `ALTER TABLE ...           ENGINE=INNODB` prior to the upgrade.

For information about converting `MyISAM` tables to `InnoDB`, see [Section 17.6.1.5, “Converting Tables from MyISAM to InnoDB”](converting-tables-to-innodb.md).