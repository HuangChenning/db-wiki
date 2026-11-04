---
title: "Appendix E SBT Backup History Table Update"
book: "MySQL Enterprise Backup User's Guide (Version 9.7.0)"
version: "9.7"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/9.7/en/backup-sbt-history-table-update.html"
tags:
  - mysql
  - mysql-9.7
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 9.7.0)

The `mysql.backup_sbt_history` table has been updated with the release of MySQL Enterprise Backup 8.0.21 in the following ways:

When MySQL Enterprise Backup 9.7 tries to perform its first full backup on a database using the SBT API (see [Section 11.1, “Backing Up to Tape with Oracle Secure Backup”](meb-backup-osb.md) for details), it automatically checks the format of the `mysql.backup_sbt_history` table. If it detects that the table is in the old format (which means the server has been upgraded from 8.0.20 or earlier and has been backed up by MySQL Enterprise Backup before using the SBT API), it attempts to perform an update on the table automatically with the following steps:

1. Create in the new format a table named `mysql.backup_sbt_history_new` and copy into it data from the original `mysql.backup_sbt_history` table.
2. Rename the original `mysql.backup_sbt_history` table to `mysql.backup_sbt_history_old`, and the `mysql.backup_sbt_history_new` table to `mysql.backup_sbt_history`.
3. Drop the `mysql.backup_history_old` table.

For the migration to the new table format to succeed, before performing the first backup task using the SBT API with MySQL Enterprise Backup 9.7 on a MySQL Server that has been upgraded from 8.0.20 or earlier and has been backed up by MySQL Enterprise Backup before with the SBT API, grant the required privileges to the `mysqlbackup` user on the server by issuing these statements at the **mysql** client::

```
GRANT ALTER ON mysql.backup_sbt_history TO 'mysqlbackup'@'localhost';
GRANT CREATE, INSERT, DROP ON mysql.backup_sbt_history_old TO 'mysqlbackup'@'localhost';
GRANT CREATE, INSERT, DROP, ALTER ON mysql.backup_sbt_history_new TO 'mysqlbackup'@'localhost';
```

If these privileges are not granted, the first full backup on the upgraded server using the SBT API will fail with an error message similar to the following:

```
200612 08:40:45 MAIN ERROR: MySQL query 'DROP TABLE IF EXISTS mysql.backup_sbt_history_old': 1142, DROP command denied to user 'mysqlbackup'@'localhost' for table 'backup_sbt_history_old'
mysqlbackup failed with errors!
```

These privileges are no longer needed after the first full backup with SBT API has been performed by MySQL Enterprise Backup 9.7, by which point they can be revoked.

Note

If you are working with a multiprimary Group Replication setting, make sure these privileges are granted on all primary nodes; see also [Chapter 9, *Using MySQL Enterprise Backup with Group Replication*](meb-group-replication.md).