---
title: "Appendix D Backup History Table Update"
book: "MySQL Enterprise Backup User's Guide (Version 9.7.0)"
version: "9.7"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/9.7/en/backup-history-table-update.html"
tags:
  - mysql
  - mysql-9.7
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 9.7.0)

The `mysql.backup_history` table has been updated with the release of MySQL Enterprise Backup 8.0.12 in the following ways:

When MySQL Enterprise Backup 9.7 tries to perform its first full backup on a database server, it automatically checks the format of the `mysql.backup_history` table. If it detects that the table is in the old format (which means the server has been upgraded from 8.0.11 or earlier (or 5.7.22 or earlier) and has been backed up by MySQL Enterprise Backup before), it attempts to perform a format update on the table automatically with the following steps:

1. Create in the new format a table named `mysql.backup_history_new` and copy into it data from the original `mysql.backup_history` table.
2. Rename the original `mysql.backup_history` table to `mysql.backup_history_old`, and the `mysql.backup_history_new` table to `mysql.backup_history`.
3. Drop the `mysql.backup_history_old` table.

For the migration to the new table format to succeed, before performing the first backup task with MySQL Enterprise Backup 9.7 for the first time on a MySQL Server that has been upgraded from 8.0.11 or earlier and has been backed up by MySQL Enterprise Backup before, grant the required privileges to the `mysqlbackup` user on the server by issuing these statements at the **mysql** client::

```
GRANT CREATE, INSERT, DROP ON mysql.backup_history_old TO 'mysqlbackup'@'localhost';
GRANT CREATE, INSERT, DROP, ALTER ON mysql.backup_history_new TO 'mysqlbackup'@'localhost';
```

If these privileges are not granted, the first full backup on the upgraded server will fail with an error message similar to the following:

```
180612 08:40:45 MAIN ERROR: MySQL query 'DROP TABLE IF EXISTS mysql.backup_history_old': 1142, DROP command denied to user 'mysqlbackup'@'localhost' for table 'backup_history_old'
mysqlbackup failed with errors!
```

These privileges are no longer needed after the first full backup has been performed by MySQL Enterprise Backup 9.7, by which point they can be revoked.

Note

If you are working with a multiprimary Group Replication setting, make sure these privileges are granted on all primary nodes; see also [Chapter 9, *Using MySQL Enterprise Backup with Group Replication*](meb-group-replication.md).