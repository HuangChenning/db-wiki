---
title: "MySQL :: MySQL 26.7 Reference Manual :: 17.8.2 Configuring InnoDB for Read-Only Operation"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/innodb-read-only-instance.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 17.8.2 Configuring InnoDB for Read-Only Operation

You can query `InnoDB` tables where the MySQL data directory is on read-only media by enabling the [`--innodb-read-only`](innodb-parameters.md) configuration option at server startup.

#### How to Enable

To prepare an instance for read-only operation, make sure all the necessary information is [flushed](glossary.md) to the data files before storing it on the read-only medium. Run the server with change buffering disabled ([`innodb_change_buffering=0`](innodb-parameters.md)) and do a [slow shutdown](glossary.md).

To enable read-only mode for an entire MySQL instance, specify the following configuration options at server startup:

- [`--innodb-read-only=1`](innodb-parameters.md)
- If the instance is on read-only media such as a DVD or CD, or the `/var` directory is not writeable by all: [``--pid-file=*`path_on_writeable_media`*``](server-system-variables.md) and [`--event-scheduler=disabled`](server-system-variables.md)
- [`--innodb-temp-data-file-path`](innodb-parameters.md). This option specifies the path, file name, and file size for `InnoDB` temporary tablespace data files. The default setting is `ibtmp1:12M:autoextend`, which creates the `ibtmp1` temporary tablespace data file in the data directory. To prepare an instance for read-only operation, set [`innodb_temp_data_file_path`](innodb-parameters.md) to a location outside of the data directory. The path must be relative to the data directory. For example:
	```svg
	--innodb-temp-data-file-path=../../../tmp/ibtmp1:12M:autoextend
	```

Enabling [`innodb_read_only`](innodb-parameters.md) prevents table creation and drop operations for all storage engines. These operations modify data dictionary tables in the `mysql` system database, but those tables use the `InnoDB` storage engine and cannot be modified when [`innodb_read_only`](innodb-parameters.md) is enabled. The same restriction applies to any operation that modifies data dictionary tables, such as [`ANALYZE       TABLE`](analyze-table.md) and [``ALTER TABLE       *`tbl_name`*       ENGINE=*`engine_name`*``](alter-table.md).

In addition, other tables in the `mysql` system database use the `InnoDB` storage engine in MySQL 26.7. Making those tables read only results in restrictions on operations that modify them. For example, [`CREATE USER`](create-user.md), [`GRANT`](grant.md), [`REVOKE`](revoke.md), and [`INSTALL PLUGIN`](install-plugin.md) operations are not permitted in read-only mode.

#### Usage Scenarios

This mode of operation is appropriate in situations such as:

- Distributing a MySQL application, or a set of MySQL data, on a read-only storage medium such as a DVD or CD.
- Multiple MySQL instances querying the same data directory simultaneously, typically in a data warehousing configuration. You might use this technique to avoid [bottlenecks](glossary.md) that can occur with a heavily loaded MySQL instance, or you might use different configuration options for the various instances to tune each one for particular kinds of queries.
- Querying data that has been put into a read-only state for security or data integrity reasons, such as archived backup data.

Note

This feature is mainly intended for flexibility in distribution and deployment, rather than raw performance based on the read-only aspect. See [Section 10.5.3, “Optimizing InnoDB Read-Only Transactions”](innodb-performance-ro-txn.md) for ways to tune the performance of read-only queries, which do not require making the entire server read-only.

#### How It Works

When the server is run in read-only mode through the [`--innodb-read-only`](innodb-parameters.md) option, certain `InnoDB` features and components are reduced or turned off entirely:

- No [change buffering](glossary.md) is done, in particular no merges from the change buffer. To make sure the change buffer is empty when you prepare the instance for read-only operation, disable change buffering ([`innodb_change_buffering=0`](innodb-parameters.md)) and do a [slow shutdown](glossary.md) first.
- There is no [crash recovery](glossary.md) phase at startup. The instance must have performed a [slow shutdown](glossary.md) before being put into the read-only state.
- Most background threads are turned off. I/O read threads remain, as well as I/O write threads and a page flush coordinator thread for writes to temporary files, which are permitted in read-only mode. A buffer pool resize thread also remains active to enable online resizing of the buffer pool.
- Information about deadlocks, monitor output, and so on is not written to temporary files. As a consequence, [`SHOW ENGINE           INNODB STATUS`](show-engine.md) does not produce any output.
- Changes to configuration option settings that would normally change the behavior of write operations, have no effect when the server is in read-only mode.
- The [MVCC](glossary.md) processing to enforce [isolation levels](glossary.md) is turned off. All queries read the latest version of a record, because update and deletes are not possible.
- The [undo log](glossary.md) is not used. Disable any settings for the [`innodb_undo_directory`](innodb-parameters.md) configuration option.