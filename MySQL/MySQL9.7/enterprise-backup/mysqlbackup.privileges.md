---
title: "4.1.2 Grant MySQL Privileges to Backup Administrator"
book: "MySQL Enterprise Backup User's Guide (Version 9.7.0)"
version: "9.7"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/9.7/en/mysqlbackup.privileges.html"
tags:
  - mysql
  - mysql-9.7
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 9.7.0)

### 4.1.2 Grant MySQL Privileges to Backup Administrator

The **mysqlbackup** command connects to the MySQL server using the credentials supplied with the `--user` and `--password` options. The specified [`user`](connection-options.md) needs certain privileges. You can either create a new user with a limited set of privileges, or use an administrative account such as root. Here are the privileges required by **mysqlbackup**:

- The minimum privileges for the MySQL user with which **mysqlbackup** connects to the server include:
	- `SELECT` on all databases and tables, for table locks that protect the backups against inconsistency caused by parallel DDL operations.
	- `BACKUP_ADMIN` on all databases and tables. This also optimizes locking in order to minimize disruption to database processing.
	- `RELOAD` on all databases and tables.
	- `SYSTEM_VARIABLES_ADMIN`, to enable and disable logging.
	- `REPLICATION CLIENT`, to retrieve the [binary log](glossary.md) position, which is stored with the backup.
	- `PROCESS`, to process DDL statements with the `ALGORITHM = INPLACE` clause.
	- `CREATE`, `INSERT`, `DROP`, and `UPDATE` on the tables `mysql.backup_progress` and `mysql.backup_history`, and also `SELECT` and `ALTER` on `mysql.backup_history`.
	To create a MySQL user (`mysqlbackup` in this example) and set the above-mentioned privileges for the user to connect from localhost, issue statements like the following from the `mysql` client program:
	```
	CREATE USER 'mysqlbackup'@'localhost' IDENTIFIED BY 'password';
	GRANT SELECT, BACKUP_ADMIN, RELOAD, PROCESS, SYSTEM_VARIABLES_ADMIN, REPLICATION CLIENT ON *.* 
	    TO \`mysqlbackup\`@\`localhost\`;
	GRANT CREATE, INSERT, DROP, UPDATE ON mysql.backup_progress TO 'mysqlbackup'@'localhost'; 
	GRANT CREATE, INSERT, DROP, UPDATE, SELECT, ALTER ON mysql.backup_history 
	    TO 'mysqlbackup'@'localhost';
	```
- The following additional privileges are required for using specific features of MySQL Enterprise Backup:
	- For using [transportable tablespaces (TTS)](glossary.md) to back up and restore InnoDB tables:
		- `LOCK TABLES` for backing up tables. `CREATE` for restoring tables.
		- `DROP` for dropping tables if the restore fails for some reasons.
		- `FILE` for restoring tables in external tablespaces outside of the server's data directory.
	- For [creating tape backups using the System Backup to Tape (SBT) API](meb-backup-osb.md) :
		- `CREATE`, `INSERT`, `DROP`, and `UPDATE` on the `mysql.backup_sbt_history` table
	- For [working with encrypted InnoDB tables](meb-encrypted-innodb.md):
		- [`ENCRYPTION_KEY_ADMIN`](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/privileges-provided.html#priv_encryption-key-admin) to enable InnoDB encryption key rotation.
	- For backing up and restoring user-created non-InnoDB tables:
		- `LOCK TABLES` on all schemas containing user-created non-InnoDB tables
	- For using [redo log archiving](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/innodb-redo-log.html#innodb-redo-log-archiving) for backups:
		- `` `INNODB_REDO_LOG_ARCHIVE` `` to invoke the `` `innodb_redo_log_archive_start()` `` function.
	- For [Section 5.1.4, “Table-Level Recovery (TLR)”](restore.partial.md) of [non-TTS backups](glossary.md):
		- `INSERT` and `ALTER` to update tables
	Set those additional privileges if you are using the features that require them. To set all of them, issue statements like the following from the `mysql` client program:
	```
	GRANT LOCK TABLES, CREATE, DROP, FILE, INSERT, ALTER ON *.* TO 'mysqlbackup'@'localhost';
	GRANT CREATE, DROP, UPDATE ON mysql.backup_sbt_history TO 'mysqlbackup'@'localhost';
	GRANT ENCRYPTION_KEY_ADMIN ON *.* TO 'mysqlbackup'@'localhost';
	GRANT INNODB_REDO_LOG_ARCHIVE ON *.* TO 'mysqlbackup'@'localhost';
	```
- For privileges required for using MySQL Enterprise Backup with a Group Replication setting, see [Chapter 9, *Using MySQL Enterprise Backup with Group Replication*](meb-group-replication.md).
- The following additional privileges might also be required after a server upgrade:
	- **When using MySQL Enterprise Backup 9.7 for the first time **on a MySQL Server that has been upgraded from 8.0.18 or earlier and has been backed up by MySQL Enterprise Backup before****:
		- `ALTER` on `mysql.backup_progress`.
		- `CREATE`, `INSERT`, and `DROP` on `mysql.backup_progress_old`.
		- `CREATE`, `INSERT`, `DROP`, and `ALTER` on `mysql.backup_progress_new`.
		Grant these privileges by issuing these sample statements at the **mysql** client:
		```
		GRANT ALTER ON mysql.backup_progress TO 'mysqlbackup'@'localhost';
		GRANT CREATE, INSERT, DROP ON mysql.backup_progress_old TO 'mysqlbackup'@'localhost';
		GRANT CREATE, INSERT, DROP, ALTER ON mysql.backup_progress_new TO 'mysqlbackup'@'localhost';
		```
		Note
		If you are working with a multiprimary Group Replication setting, make sure these privileges are granted on all primary nodes; see also [Chapter 9, *Using MySQL Enterprise Backup with Group Replication*](meb-group-replication.md).
		These privileges are for the attempt to migrate the `mysql.backup_progress` table to a newer format (see [Appendix F, *Backup Progress Table Update*](backup-progress-table-update.md) for details), and they are no longer needed after the first backup operation by MySQL Enterprise Backup 9.7 has taken place on the server, by which point they can be revoked.
	- **When using MySQL Enterprise Backup 9.7 for the first time **on a MySQL Server that has been upgraded from 8.0.11 or earlier and has been backed up by MySQL Enterprise Backup before****:
		- `CREATE`, `INSERT`, and `DROP` on `mysql.backup_history_old`.
		- `CREATE`, `INSERT`, `DROP`, and `ALTER` on `mysql.backup_history_new`.
		Grant these privileges by issuing these sample statements at the **mysql** client:
		```
		GRANT CREATE, INSERT, DROP ON mysql.backup_history_old TO 'mysqlbackup'@'localhost';
		GRANT CREATE, INSERT, DROP, ALTER ON mysql.backup_history_new TO 'mysqlbackup'@'localhost';
		```
		Note
		If you are working with a multiprimary Group Replication setting, make sure these privileges are granted on all primary nodes; see also [Chapter 9, *Using MySQL Enterprise Backup with Group Replication*](meb-group-replication.md).
		These privileges are for the attempt to migrate the `mysql.backup_history` table to a newer format (see [Appendix D, *Backup History Table Update*](backup-history-table-update.md) for details), and they are no longer needed after the first backup operation by MySQL Enterprise Backup 9.7 has taken place on the server, by which point they can be revoked.
	- **When performing for the first time a backup [using the SBT API](meb-backup-osb.md) with MySQL Enterprise Backup 9.7 **on a MySQL Server that has been upgraded from 8.0.20 or earlier and has been backed up by MySQL Enterprise Backup before [using the SBT API](meb-backup-osb.md)****:
		- `ALTER` on `mysql.backup_sbt_history`.
		- `CREATE`, `INSERT`, and `DROP` on `mysql.backup_sbt_history_old`.
		- `CREATE`, `INSERT`, `DROP`, and `ALTER` on `mysql.backup_sbt_history_new`.
		Grant these privileges by issuing these sample statements at the **mysql** client:
		```
		GRANT ALTER ON mysql.backup_sbt_history TO 'mysqlbackup'@'localhost';
		GRANT CREATE, INSERT, DROP ON mysql.backup_sbt_history_old TO 'mysqlbackup'@'localhost';
		GRANT CREATE, INSERT, DROP, ALTER ON mysql.backup_sbt_history_new TO 'mysqlbackup'@'localhost';
		```
		Note
		If you are working with a multiprimary Group Replication setting, make sure these privileges are granted on all primary nodes; see also [Chapter 9, *Using MySQL Enterprise Backup with Group Replication*](meb-group-replication.md).
		These privileges are for the attempt to migrate the `mysql.backup_sbt_history` table to a newer format (see [Appendix E, *SBT Backup History Table Update*](backup-sbt-history-table-update.md) for details), and they are no longer needed after the first backup operation by MySQL Enterprise Backup 9.7 using the SBT API has taken place on the server, by which point they can be revoked.

Note

Make sure that the limit `MAX_QUERIES_PER_HOUR` is not set for the user **mysqlbackup** uses to access the server, or backup operations might fail unexpectedly.