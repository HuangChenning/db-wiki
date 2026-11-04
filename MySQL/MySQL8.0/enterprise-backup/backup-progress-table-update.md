---
title: "Appendix F Backup Progress Table Update"
book: "MySQL Enterprise Backup User's Guide (Version 8.0.46)"
version: "8.0"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/8.0/en/backup-progress-table-update.html"
tags:
  - mysql
  - mysql-8.0
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 8.0.46)

The `mysql.backup_progress` table has been updated with the release of MySQL Enterprise Backup 8.0.19 in the following ways:

- Changed the storage engine from CSV to InnoDB
- Added a new auto-increment primary key column `id`
- Added a composite index on the `backup_id` and `current_timestamp` columns

When MySQL Enterprise Backup 8.0.19 or later tries to perform its first full backup on a database server, it automatically checks the format of the `mysql.backup_progress` table. If it detects that the table is in the old format (which means the server has been upgraded from 8.0.18 or earlier and has been backed up by MySQL Enterprise Backup before), it attempts to perform a format update on the table automatically with the following steps:

1. Create in the new format a table named `mysql.backup_progress_new` and copy into it data from the original `mysql.backup_progress` table.
2. Rename the original `mysql.backup_progress` table to `mysql.backup_progress_old`, and the `mysql.backup_progress_new` table to `mysql.backup_progress`.
3. *For MySQL Enterprise Backup 8.0.21 and later:* Drop the `mysql.backup_progress_old` table.

For the migration to the new table format to succeed, before performing the first backup task with MySQL Enterprise Backup 8.0.19 or later for the first time on a MySQL Server that has been upgraded from 8.0.18 or earlier and has been backed up by MySQL Enterprise Backup before, grant the required privileges to the `mysqlbackup` user on the server by issuing these statements at the **mysql** client::

```
GRANT ALTER ON mysql.backup_progress TO 'mysqlbackup'@'localhost';
GRANT CREATE, INSERT, DROP ON mysql.backup_progress_old TO 'mysqlbackup'@'localhost';
GRANT CREATE, INSERT, DROP, ALTER ON mysql.backup_progress_new TO 'mysqlbackup'@'localhost';
```

If these privileges are not granted, the table upgrade will fail with an error message similar to the following:

```
191219 20:48:43 MAIN   ERROR: MySQL query 'RENAME table mysql.backup_progress TO mysql.backup_progress_old, 
mysql.backup_progress_new TO mysql.backup_progress': 1142, ALTER command denied to user 'mysqlbackup'@'localhost' 
for table 'backup_progress'
```

These privileges are no longer needed after the first full backup has been performed by MySQL Enterprise Backup 8.0.19 or later, by which point they can be revoked.

Note

If you are working with a multiprimary Group Replication setting, make sure these privileges are granted on all primary nodes; see also [Chapter 9, *Using MySQL Enterprise Backup with Group Replication*](meb-group-replication.md).