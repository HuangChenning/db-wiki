---
title: "MySQL :: MySQL 26.7 Reference Manual :: 15.1.1 Atomic Data Definition Statement Support"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/atomic-ddl.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 15.1.1 Atomic Data Definition Statement Support

MySQL 26.7 supports atomic Data Definition Language (DDL) statements. This feature is referred to as *atomic DDL*. An atomic DDL statement combines the data dictionary updates, storage engine operations, and binary log writes associated with a DDL operation into a single, atomic operation. The operation is either committed, with applicable changes persisted to the data dictionary, storage engine, and binary log, or is rolled back, even if the server halts during the operation.

Note

*Atomic DDL* is not *transactional DDL*. DDL statements, atomic or otherwise, implicitly end any transaction that is active in the current session, as if you had done a [`COMMIT`](commit.md) before executing the statement. This means that DDL statements cannot be performed within another transaction, within transaction control statements such as [`START TRANSACTION ...         COMMIT`](commit.md), or combined with other statements within the same transaction.

Atomic DDL is made possible by the MySQL data dictionary, which provides centralized, transactional metadata storage.

The atomic DDL feature is described under the following topics in this section:

#### Supported DDL Statements

The atomic DDL feature supports both table and non-table DDL statements. Table-related DDL operations require storage engine support, whereas non-table DDL operations do not. Currently, only the `InnoDB` storage engine supports atomic DDL.

- Supported table DDL statements include `CREATE`, `ALTER`, and `DROP` statements for databases, tablespaces, tables, and indexes, and the [`TRUNCATE TABLE`](truncate-table.md) statement.
- Supported non-table DDL statements include:
	- `CREATE` and `DROP` statements, and, if applicable, `ALTER` statements for stored programs, triggers, views, and loadable functions.
	- Account management statements: `CREATE`, `ALTER`, `DROP`, and, if applicable, `RENAME` statements for users and roles, as well as [`GRANT`](grant.md) and [`REVOKE`](revoke.md) statements.

The following statements are not supported by the atomic DDL feature:

- Table-related DDL statements that involve a storage engine other than `InnoDB`.
- [`INSTALL PLUGIN`](install-plugin.md) and [`UNINSTALL PLUGIN`](uninstall-plugin.md) statements.
- [`INSTALL COMPONENT`](install-component.md) and [`UNINSTALL COMPONENT`](uninstall-component.md) statements.
- [`CREATE SERVER`](create-server.md), [`ALTER SERVER`](alter-server.md), and [`DROP SERVER`](drop-server.md) statements.

#### Atomic DDL Characteristics

The characteristics of atomic DDL statements include the following:

- Metadata updates, binary log writes, and storage engine operations, where applicable, are combined into a single atomic operation.
- There are no intermediate commits at the SQL layer during the DDL operation.
- Where applicable:
	- The state of data dictionary, routine, event, and loadable function caches is consistent with the status of the DDL operation, meaning that caches are updated to reflect whether or not the DDL operation was completed successfully or rolled back.
	- The storage engine methods involved in a DDL operation do not perform intermediate commits, and the storage engine registers itself as part of the DDL operation.
	- The storage engine supports redo and rollback of DDL operations, which is performed in the *Post-DDL* phase of the DDL operation.
- The visible behaviour of DDL operations is atomic.

#### DDL Statement Behavior

This section describes some important aspects of DDL statement behavior when using a storage engine that support atomic DDL, such as [`InnoDB`](innodb-storage-engine.md).

- [`DROP TABLE`](drop-table.md) operations are fully atomic if all named tables use a storage engine which supports atomic DDL. The statement either drops all tables successfully or is rolled back.
	[`DROP TABLE`](drop-table.md) fails with an error if a named table does not exist, and no changes are made, regardless of the storage engine.
- [`CREATE DATABASE`](create-database.md) and [`DROP DATABASE`](drop-database.md) are fully atomic and crash-safe, provided that all tables in the named database use a storage engine which supports atomic DDL, in which case the statement either adds or drops all objects successfully, or is rolled back.
- For tables that do not use a storage engine which supports atomic DDL, table deletion occurs outside of the atomic [`DROP TABLE`](drop-table.md) or [`DROP DATABASE`](drop-database.md) transaction. Such table deletions are written to the binary log individually, which limits the discrepancy between the storage engine, data dictionary, and binary log to one table at most in the case of an interrupted [`DROP TABLE`](drop-table.md) or [`DROP DATABASE`](drop-database.md) operation. For operations that drop multiple tables, any tables that do not use a storage engine which supports atomic DDL are dropped before tables that do so.
- [`CREATE TABLE`](create-table.md), [`ALTER TABLE`](alter-table.md), [`RENAME TABLE`](rename-table.md), [`TRUNCATE TABLE`](truncate-table.md), [`CREATE TABLESPACE`](create-tablespace.md), and [`DROP TABLESPACE`](drop-tablespace.md) operations for tables that use a storage engine which supports atomic DDL are either fully committed or rolled back if the server halts during their operation. [`RENAME             TABLE`](rename-table.md) operations are atomic only if all named tables use a storage engine which supports atomic DDL.
- For storage engines that support atomic DDL, the [`CREATE             TABLE ... SELECT`](create-table-select.md) statement is logged as one transaction in the binary log when row-based replication is in use.
	On storage engines that support both atomic DDL and foreign key constraints, creation of foreign keys is not permitted in [`CREATE             TABLE ... SELECT`](create-table-select.md) statements when row-based replication is in use. Foreign key constraints can be added later using [`ALTER TABLE`](alter-table.md).
	When [`CREATE             TABLE ... SELECT`](create-table-select.md) is applied as an atomic operation, a metadata lock is held on the table while data is inserted, which prevents concurrent access to the table for the duration of the operation.
- [`DROP VIEW`](drop-view.md) fails if a named view does not exist, and no changes are made.
- Account management statements either succeed for all named users or roll back and have no effect if an error occurs.

#### Storage Engine Support

Currently, only the `InnoDB` storage engine supports atomic DDL. Storage engines that do not support atomic DDL are exempted from DDL atomicity. DDL operations involving exempted storage engines remain capable of introducing inconsistencies that can occur when operations are interrupted or only partially completed.

To support redo and rollback of DDL operations, `InnoDB` writes DDL logs to the `mysql.innodb_ddl_log` table, which is a hidden data dictionary table that resides in the `mysql.ibd` data dictionary tablespace.

To view DDL logs that are written to the `mysql.innodb_ddl_log` table during a DDL operation, enable the [`innodb_print_ddl_logs`](innodb-parameters.md) configuration option. For more information, see Viewing DDL Logs.

Note

The redo logs for changes to the `mysql.innodb_ddl_log` table are flushed to disk immediately regardless of the [`innodb_flush_log_at_trx_commit`](innodb-parameters.md) setting. Flushing the redo logs immediately avoids situations where data files are modified by DDL operations but the redo logs for changes to the `mysql.innodb_ddl_log` table resulting from those operations are not persisted to disk. Such a situation could cause errors during rollback or recovery.

The `InnoDB` storage engine executes DDL operations in phases. DDL operations such as [`ALTER TABLE`](alter-table.md) may perform the *Prepare* and *Perform* phases multiple times prior to the *Commit* phase.

1. *Prepare*: Create the required objects and write the DDL logs to the `mysql.innodb_ddl_log` table. The DDL logs define how to roll forward and roll back the DDL operation.
2. *Perform*: Perform the DDL operation. For example, perform a create routine for a `CREATE             TABLE` operation.
3. *Commit*: Update the data dictionary and commit the data dictionary transaction.
4. *Post-DDL*: Replay and remove DDL logs from the `mysql.innodb_ddl_log` table. To ensure that rollback can be performed safely without introducing inconsistencies, file operations such as renaming or removing data files are performed in this final phase. This phase also removes dynamic metadata from the `mysql.innodb_dynamic_metadata` data dictionary table for [`DROP             TABLE`](drop-table.md), [`TRUNCATE             TABLE`](truncate-table.md), and other DDL operations that rebuild the table.

DDL logs are replayed and removed from the `mysql.innodb_ddl_log` table during the *Post-DDL* phase, regardless of whether the DDL operation is committed or rolled back. DDL logs should only remain in the `mysql.innodb_ddl_log` table if the server is halted during a DDL operation. In this case, the DDL logs are replayed and removed after recovery.

In a recovery situation, a DDL operation may be committed or rolled back when the server is restarted. If the data dictionary transaction that was performed during the *Commit* phase of a DDL operation is present in the redo log and binary log, the operation is considered successful and is rolled forward. Otherwise, the incomplete data dictionary transaction is rolled back when `InnoDB` replays data dictionary redo logs, and the DDL operation is rolled back.

#### Viewing DDL Logs

To view DDL logs that are written to the `mysql.innodb_ddl_log` data dictionary table during atomic DDL operations that involve the `InnoDB` storage engine, enable [`innodb_print_ddl_logs`](innodb-parameters.md) to have MySQL write the DDL logs to `stderr`. Depending on the host operating system and MySQL configuration, `stderr` may be the error log, terminal, or console window. See [Section 7.4.2.2, “Default Error Log Destination Configuration”](error-log-destination-configuration.md).

`InnoDB` writes DDL logs to the `mysql.innodb_ddl_log` table to support redo and rollback of DDL operations. The `mysql.innodb_ddl_log` table is a hidden data dictionary table that resides in the `mysql.ibd` data dictionary tablespace. Like other hidden data dictionary tables, the `mysql.innodb_ddl_log` table cannot be accessed directly in non-debug versions of MySQL. (See [Section 16.1, “Data Dictionary Schema”](data-dictionary-schema.md).) The structure of the `mysql.innodb_ddl_log` table corresponds to this definition:

```sql
CREATE TABLE mysql.innodb_ddl_log (
  id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  thread_id BIGINT UNSIGNED NOT NULL,
  type INT UNSIGNED NOT NULL,
  space_id INT UNSIGNED,
  page_no INT UNSIGNED,
  index_id BIGINT UNSIGNED,
  table_id BIGINT UNSIGNED,
  old_file_path VARCHAR(512) COLLATE utf8mb4_bin,
  new_file_path VARCHAR(512) COLLATE utf8mb4_bin,
  KEY(thread_id)
);
```

- `id`: A unique identifier for a DDL log record.
- `thread_id`: Each DDL log record is assigned a `thread_id`, which is used to replay and remove DDL logs that belong to a particular DDL operation. DDL operations that involve multiple data file operations generate multiple DDL log records.
- `type`: The DDL operation type. Types include `FREE` (drop an index tree), `DELETE` (delete a file), `RENAME` (rename a file), or `DROP` (drop metadata from the `mysql.innodb_dynamic_metadata` data dictionary table).
- `space_id`: The tablespace ID.
- `page_no`: A page that contains allocation information; an index tree root page, for example.
- `index_id`: The index ID.
- `table_id`: The table ID.
- `old_file_path`: The old tablespace file path. Used by DDL operations that create or drop tablespace files; also used by DDL operations that rename a tablespace.
- `new_file_path`: The new tablespace file path. Used by DDL operations that rename tablespace files.

This example demonstrates enabling [`innodb_print_ddl_logs`](innodb-parameters.md) to view DDL logs written to `strderr` for a `CREATE TABLE` operation.

```sql
mysql> SET GLOBAL innodb_print_ddl_logs=1;
mysql> CREATE TABLE t1 (c1 INT) ENGINE = InnoDB;
```
```svg
[Note] [000000] InnoDB: DDL log insert : [DDL record: DELETE SPACE, id=18, thread_id=7,
space_id=5, old_file_path=./test/t1.ibd]
[Note] [000000] InnoDB: DDL log delete : by id 18
[Note] [000000] InnoDB: DDL log insert : [DDL record: REMOVE CACHE, id=19, thread_id=7,
table_id=1058, new_file_path=test/t1]
[Note] [000000] InnoDB: DDL log delete : by id 19
[Note] [000000] InnoDB: DDL log insert : [DDL record: FREE, id=20, thread_id=7,
space_id=5, index_id=132, page_no=4]
[Note] [000000] InnoDB: DDL log delete : by id 20
[Note] [000000] InnoDB: DDL log post ddl : begin for thread id : 7
[Note] [000000] InnoDB: DDL log post ddl : end for thread id : 7
```