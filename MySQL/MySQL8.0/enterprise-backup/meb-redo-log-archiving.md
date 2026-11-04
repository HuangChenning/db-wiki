---
title: "Chapter 7 Backing up Using Redo Log Archiving"
book: "MySQL Enterprise Backup User's Guide (Version 8.0.46)"
version: "8.0"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/8.0/en/meb-redo-log-archiving.html"
tags:
  - mysql
  - mysql-8.0
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 8.0.46)

*For MySQL Enterprise Backup 8.0.17 and later:* **mysqlbackup** may sometimes fail to keep pace with redo log generation on the backed up server while a backup operation is in progress, resulting in lost redo log records due to those records being overwritten. This issue most often occurs when there is significant server activity during the backup operation, and the redo log file storage media operates at a faster speed than the backup storage media. The [redo log archiving](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/innodb-redo-log.html#innodb-redo-log-archiving) feature, introduced in MySQL 8.0.17, addresses this issue by sequentially writing redo log records to an archive file in addition to the redo log files. **mysqlbackup** can then copy redo log records from the archive file as necessary, thereby avoiding the potential loss of data.

When [redo log archiving](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/innodb-redo-log.html#innodb-redo-log-archiving) has been enabled on the server to be backed up, **mysqlbackup** utilizes the feature by default for backups, as long as the following are true:

- The OS user that runs **mysqlbackup** has read and write access to the folder on the server that stores the redo log archive file; the folder is the first labeled directory defined by the system variable `innodb_redo_log_archive_dirs` on the server.
- The MySQL user **mysqlbackup** uses to connect to the server must be granted the `INNODB_REDO_LOG_ARCHIVE` privilege, for activating [redo log archiving](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/innodb-redo-log.html#innodb-redo-log-archiving) on the server.

Redo log archiving can be skipped using the **mysqlbackup** option [`--no-redo-log-archive`](backup-capacity-options.md).

If [redo log archiving](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/innodb-redo-log.html#innodb-redo-log-archiving) is skipped by **mysqlbackup**, disabled on the server, or is simply not working for some reasons, **mysqlbackup** then reverts to copying the redo log data from the redo log files, as it used to do before the feature was introduced.