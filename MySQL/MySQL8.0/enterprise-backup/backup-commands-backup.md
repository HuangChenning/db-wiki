---
title: "19.1 Backup Operations"
book: "MySQL Enterprise Backup User's Guide (Version 8.0.46)"
version: "8.0"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/8.0/en/backup-commands-backup.html"
tags:
  - mysql
  - mysql-8.0
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 8.0.46)

The backup operations are the most frequently performed tasks by MySQL Enterprise Backup. Various kinds of backups can be performed by adding different options, like using [`--compress`](backup-compression-options.md) or [`--incremental`](backup-incremental-options.md) for compressed or incremental backups. Here is the syntax for the **mysqlbackup** commands for performing a backup operation:

```
mysqlbackup [STD-OPTIONS]
            [CONNECTION-OPTIONS]
            [SERVER-REPOSITORY-OPTIONS]
            [BACKUP-REPOSITORY-OPTIONS]
            [METADATA-OPTIONS]
            [COMPRESSION-OPTIONS]
            [SPECIAL-BACKUP-TYPES-OPTIONS]
            [INCREMENTAL-BACKUP-OPTIONS]
            [PARTIAL-BACKUP-RESTORE-OPTIONS]
            [SINGLE-FILE-BACKUP-OPTIONS]
            [PERFORMANCE-SCALABILITY-CAPACITY-OPTIONS]            
            [MESSAGE-LOGGING-OPTIONS]
            [PROGRESS-REPORT-OPTIONS]
            [ENCRYPTION-OPTIONS]
            [CLOUD-STORAGE-OPTIONS]
            [ENCRYPTED-INNODB-OPTIONS]
            backup-to-image

mysqlbackup [STD-OPTIONS]
            [CONNECTION-OPTIONS]
            [SERVER-REPOSITORY-OPTIONS]
            [BACKUP-REPOSITORY-OPTIONS]
            [METADATA-OPTIONS]
            [COMPRESSION-OPTIONS]
            [SPECIAL-BACKUP-TYPES-OPTIONS]
            [INCREMENTAL-BACKUP-OPTIONS]
            [PARTIAL-BACKUP-RESTORE-OPTIONS]
            [PERFORMANCE-SCALABILITY-CAPACITY-OPTIONS]            
            [MESSAGE-LOGGING-OPTIONS]
            [PROGRESS-REPORT-OPTIONS]
            [ENCRYPTED-INNODB-OPTIONS]
            backup | backup-and-apply-log
```

- `backup-to-image`
	Produces a single-file backup holding the backup data. In most cases, single-file backups are preferred over directory backups, which are created using the `backup` command.
	The command requires the [`--backup-image`](backup-repository-options.md) option to specify the destination file. Can be used to stream the backup to a storage device or another system without ever storing the data on the database server. You can specify [`--backup-image=-`](backup-repository-options.md), representing standard output, allowing the output to be piped to another command. To avoid mixing normal informational messages with backup output, the `--help` message, errors, alerts, and normal informational messages are always printed to standard error stream.
	The command also requires the use of the [`--backup-dir`](backup-repository-options.md) option to supply a temporary folder to save the backup metadata (including the **mysqlbackup** message log, the start and end [LSN](glossary.md), and so on) and some temporary output.
- `backup`
	Backs up data to a directory. In most cases, single-file backups, which are created using the `backup-to-image` command, are preferred over directory backups.
	The command only performs the initial phase of a complete backup process. The second phase is performed later by running **mysqlbackup** again with the [`apply-log`](backup-commands-update.md) command, which makes the backup consistent.
- `backup-and-apply-log`
	A combination of `backup` and [`apply-log`](backup-commands-update.md). It cannot be used for an incremental backup.