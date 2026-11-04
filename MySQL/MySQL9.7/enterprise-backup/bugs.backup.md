---
title: "Appendix B Limitations of MySQL Enterprise Backup"
book: "MySQL Enterprise Backup User's Guide (Version 9.7.0)"
version: "9.7"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/9.7/en/bugs.backup.html"
tags:
  - mysql
  - mysql-9.7
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 9.7.0)

Please refer to the [MySQL Enterprise Backup 9.7 Release Notes](https://docs.oracle.com/cd/E17952_01/mysql-enterprise-backup-9.7-relnotes-en/) for a list of fixed bugs for **mysqlbackup**. Here is a list of limitations of MySQL Enterprise Backup:

- In some cases, backups of non-transactional tables such as [`MyISAM`](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/myisam-storage-engine.html) tables could contain additional uncommitted data. If [autocommit](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/glossary.html#glos_autocommit) is turned off, and both [`InnoDB`](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/innodb-storage-engine.html) tables and non-transactional tables are modified within the same transaction, data can be written to the non-transactional table before the binary log position is updated. The binary log position is updated when the transaction is committed, but the non-transactional data is written immediately. If the backup occurs while such a transaction is open, the backup data contains the updates made to the non-transactional table.
- The `engines` column in the `mysql.backup_history` table does not correctly reflect the storage engines of the backed-up databases.
- Hot backups for large databases with heavy writing workloads (say, in the order of gigabytes per minute) can take a very long time to complete due to the huge redo log files that are generated on the server while the backup is running. However, when it is a relatively small subset of tables in the database that are being modified frequently, the Optimistic Backup feature can be used to improve performance and reduce backup size, as well as backup and recovery times. See [Section 4.3.6, “Making an Optimistic Backup”](meb-backup-optimistic.md) for details.
- While it is possible to backup to or restore from a Network Attached Storage (NAS) device using MySQL Enterprise Backup, due to networking issues that might arise, the consistency of the backups and the performance of the backup or restore operations might be compromised.
- When creating a backup using [transportable tablespace (TTS)](glossary.md) for a server containing tables with a mix of the Antelope and Barracuda file formats, do not apply full locking on the tables (that is, do not specify [`--use-tts=with-full-locking`](backup-partial-options.md)). Instead, just specify [`--use-tts`](backup-partial-options.md) or [`--use-tts=with-minimum-locking`](backup-partial-options.md), both of which will apply minimum locking to the tables.
- Backup of a partitioned table using [transportable tablespace (TTS)](glossary.md) would fail when any (or all) of its partitions were created in a shared tablespace.
- Restoring a partitioned table backed up using [transportable tablespace (TTS)](glossary.md) would fail if any of the partitions was created outside of the backed-up server's data directory.
- If a table containing full-text search (FTS) index is backed up using [transportable tablespace (TTS)](glossary.md), after it is restored, the FTS index will be corrupted. Users will need to recreate the index with the following command:
	```
	mysql> ALTER TABLE mytable ENGINE = INNODB;
	```
	Then, check that there are no more errors with the table:
	```
	mysql> CHECK TABLE mytable;
	```
- Tables created on the MySQL server with the [`ANSI_QUOTES`](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/sql-mode.html#sqlmode_ansi_quotes) SQL mode cannot be backed up using [transportable tablespace (TTS)](glossary.md).
- MySQL Enterprise Backup does not include the `.pem` files from the server into the backup. The files are part of the server instance when SSL connections are enabled.
- During a backup process, if a `CREATE INDEX` statement with `ALGORITHM = INPLACE` is issued when the backup process is going on, because the statement will not go into the redo log of the MySQL server (see [Sorted Index Builds](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/sorted-index-builds.html) for details), it cannot be recorded in the backup, and the index will not be recreated by **mysqlbackup** when the backup is restored.
- When a file of an unrecognized file type exists under a subdirectory in the server's data directory, it will be backed up by **mysqlbackup** unless the [`--only-known-file-types`](backup-partial-options.md) option is used. However, if the name of the file does not have an extension, it will cause **mysqlbackup** to throw an error when it tries to restore the backup to a server.
- Cloud operations by MySQL Enterprise Backup are not supported on macOS or Windows platforms, and also on Linux platforms when generic Linux builds are used for both the server and MySQL Enterprise Backup (i.e., when both the server and MySQL Enterprise Backup have been installed using generic Linux tarballs).
- Using the [`--src-entry`](backup-single-file-options.md) option with the [`extract`](backup-commands-single-file.md) command on cloud backups will cause the command to fail. Cloud backups can only be extracted in full.
- Some limitations apply when **mysqlbackup** works with [encrypted InnoDB tables](meb-encrypted-innodb.md). See [the discussion here](meb-encrypted-innodb.md) for details.
- Backup operations may fail if checksums for redo log pages are disabled (i.e., if [`--innodb_log_checksums`](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/innodb-parameters.html#sysvar_innodb_log_checksums) is `OFF` or `FALSE` or `0`) on the server.
- It is safe to have DDL operations ([CREATE TABLE](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/create-table.html), [RENAME TABLE](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/rename-table.html), [DROP TABLE](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/drop-table.html), [ALTER TABLE](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/alter-table.html), and operations that map to [ALTER TABLE](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/alter-table.html) like [CREATE INDEX](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/create-index.html)) happening on the server in parallel with a backup operation as long as:
	- The tables involved exist in their own tablespaces, instead of being in the system tablespace or some general tablespaces.
	- These server features have not been applied to the tables involved:
		- [Data-at-rest encryption](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/innodb-data-encryption.html)
		- [Page-level compression](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/innodb-page-compression.html)
		- [Full-text indexing](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/innodb-fulltext-index.html)
	- The backup is not taken with the following `mysqlbackup` features:
- A compressed directory backup fails when a general tablespace bears the same basename as the database server's system tablespace (usually `ibdata1`) and exists in the same directory with it (usually the server's data directory). A compressed single-file backup created under the same situation will be corrupted, and cannot be restored. To avoid the problem, the server administrator should not put into the same directory the system tablespace and a general tablespace of the same basename; if that is unavoidable, do not perform a compressed backup for the database server.
- When working with a replication set up whose source server also belongs to a separate Group Replication setup, over time, create backups consistently either from the source or the replica, but not from both. Otherwise, there will be conflicts between the `id` values generated by the source and the replica, causing backups to fail.
- A backup fails if the name of any database is the same as the name of any undo tablespace. For backups to be successful, the database administrator should avoid giving any database and undo tablespace the same name (for example, using the default undo tablespace name `undo_001` to name a database), or the database should be renamed before a backup.