---
title: "A.2 MySQL 8.0 FAQ: Storage Engines"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/faqs-storage-engines.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

A.2.1. Where can I obtain complete documentation for MySQL storage engines?

A.2.2. Are there any new storage engines in MySQL 8.0?

A.2.3. Have any storage engines been removed in MySQL 8.0?

A.2.4. Can I prevent the use of a particular storage engine?

A.2.5. Is there an advantage to using the InnoDB storage engine exclusively, as opposed to a combination of InnoDB and non-InnoDB storage engines?

A.2.6. What are the unique benefits of the ARCHIVE storage engine?

| **A.2.1.** | Where can I obtain complete documentation for MySQL storage engines? |
| --- | --- |
|  | See [Chapter 18, *Alternative Storage Engines*](storage-engines.md). That chapter contains information about all MySQL storage engines except for the [`InnoDB`](innodb-storage-engine.md) storage engine and the [`NDB`](mysql-cluster.md) storage engine (used for MySQL Cluster). [`InnoDB`](innodb-storage-engine.md) is covered in [Chapter 17, *The InnoDB Storage Engine*](innodb-storage-engine.md). [`NDB`](mysql-cluster.md) is covered in [Chapter 25, *MySQL NDB Cluster 8.0*](mysql-cluster.md). |
| **A.2.2.** | Are there any new storage engines in MySQL 8.0? |
|  | No. `InnoDB` is the default storage engine for new tables. See [Section 17.1, “Introduction to InnoDB”](innodb-introduction.md) for details. |
| **A.2.3.** | Have any storage engines been removed in MySQL 8.0? |
|  | The `PARTITION` storage engine plugin which provided partitioning support is replaced by a native partitioning handler. As part of this change, the server can no longer be built using `-DWITH_PARTITION_STORAGE_ENGINE`. `partition` is also no longer displayed in the output of [`SHOW PLUGINS`](show-plugins.md), or shown in the [`INFORMATION_SCHEMA.PLUGINS`](information-schema-plugins-table.md) table.  In order to support partitioning of a given table, the storage engine used for the table must now provide its own (“native”) partitioning handler. [`InnoDB`](innodb-storage-engine.md) is the only storage engine supported in MySQL 8.0 that includes a native partitioning handler. An attempt to create partitioned tables in MySQL 8.0 using any other storage engine fails. (The [`NDB`](mysql-cluster.md) storage engine used by MySQL Cluster also provides its own partitioning handler, but is currently not supported by MySQL 8.0.) |
| **A.2.4.** | Can I prevent the use of a particular storage engine? |
|  | Yes. The [`disabled_storage_engines`](server-system-variables.md) configuration option defines which storage engines cannot be used to create tables or tablespaces. By default, [`disabled_storage_engines`](server-system-variables.md) is empty (no engines disabled), but it can be set to a comma-separated list of one or more engines. |
| **A.2.5.** | Is there an advantage to using the `InnoDB` storage engine exclusively, as opposed to a combination of `InnoDB` and non- `InnoDB` storage engines? |
|  | Yes. Using `InnoDB` tables exclusively can simplify backup and recovery operations. MySQL Enterprise Backup does a [hot backup](glossary.md) of all tables that use the `InnoDB` storage engine. For tables using `MyISAM` or other non- `InnoDB` storage engines, it does a “warm” backup, where the database continues to run, but those tables cannot be modified while being backed up. See [Section 32.1, “MySQL Enterprise Backup Overview”](mysql-enterprise-backup.md). |
| **A.2.6.** | What are the unique benefits of the `ARCHIVE` storage engine? |
|  | The `ARCHIVE` storage engine stores large amounts of data without indexes; it has a small footprint, and performs selects using table scans. See [Section 18.5, “The ARCHIVE Storage Engine”](archive-storage-engine.md), for details. |