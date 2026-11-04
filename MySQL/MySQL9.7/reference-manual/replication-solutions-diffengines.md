---
title: "19.4.4 Using Replication with Different Source and Replica Storage Engines"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/replication-solutions-diffengines.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 19.4.4 Using Replication with Different Source and Replica Storage Engines

It does not matter for the replication process whether the original table on the source and the replicated table on the replica use different storage engine types. In fact, the [`default_storage_engine`](server-system-variables.md) system variable is not replicated.

This provides a number of benefits in the replication process in that you can take advantage of different engine types for different replication scenarios. For example, in a typical scale-out scenario (see [Section 19.4.5, “Using Replication for Scale-Out”](replication-solutions-scaleout.md)), you want to use `InnoDB` tables on the source to take advantage of the transactional functionality, but use `MyISAM` on the replicas where transaction support is not required because the data is only read. When using replication in a data-logging environment you may want to use the `Archive` storage engine on the replica.

Configuring different engines on the source and replica depends on how you set up the initial replication process:

- If you used [**mysqldump**](mysqldump.md) to create the database snapshot on your source, you could edit the dump file text to change the engine type used on each table.
	Another alternative for [**mysqldump**](mysqldump.md) is to disable engine types that you do not want to use on the replica before using the dump to build the data on the replica. For example, you can add the `--skip-federated` option on your replica to disable the [`FEDERATED`](federated-storage-engine.md) engine. If a specific engine does not exist for a table to be created, MySQL uses the default engine type, usually [`InnoDB`](innodb-storage-engine.md). (This requires that the [`NO_ENGINE_SUBSTITUTION`](sql-mode.md) SQL mode is not enabled.) If you want to disable additional engines in this way, you may want to consider building a special binary to be used on the replica that supports only the engines you want.
- If you use raw data files (a binary backup) to set up the replica, it is not possible to change the initial table format. Instead, use [`ALTER           TABLE`](alter-table.md) to change the table types after the replica has been started.
- For new source/replica replication setups where there are currently no tables on the source, avoid specifying the engine type when creating new tables.

If you are already running a replication solution and want to convert your existing tables to another engine type, follow these steps:

1. Stop the replica from running replication updates:
	```
	mysql> STOP REPLICA;
	```
	This makes it possible to change engine types without interruption.
2. Execute an ``ALTER TABLE ...           ENGINE='*`engine_type`*'`` for each table to be changed.
3. Start the replication process again:
	```
	mysql> START REPLICA;
	```

Although the [`default_storage_engine`](server-system-variables.md) variable is not replicated, be aware that [`CREATE       TABLE`](create-table.md) and [`ALTER TABLE`](alter-table.md) statements that include the engine specification are replicated to the replica correctly. If, in the case of a [`CSV`](csv-storage-engine.md) table, you execute this statement:

```
mysql> ALTER TABLE csvtable ENGINE='MyISAM';
```

This statement is replicated; the table's engine type on the replica is converted to `InnoDB`, even if you have previously changed the table type on the replica to an engine other than `CSV`. If you want to retain engine differences on the source and replica, you should be careful to use the [`default_storage_engine`](server-system-variables.md) variable on the source when creating a new table. For example, instead of:

```
mysql> CREATE TABLE tablea (columna int) Engine=MyISAM;
```

Use this format:

```
mysql> SET default_storage_engine=MyISAM;
mysql> CREATE TABLE tablea (columna int);
```

When replicated, the [`default_storage_engine`](server-system-variables.md) variable is ignored, and the [`CREATE TABLE`](create-table.md) statement executes on the replica using the replica's default engine.