---
title: "19.2 Update Operations"
book: "MySQL Enterprise Backup User's Guide (Version 8.0.46)"
version: "8.0"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/8.0/en/backup-commands-update.html"
tags:
  - mysql
  - mysql-8.0
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 8.0.46)

There are two types of operations to bring your backup data up-to-date:

### Apply-log Operation

After a backup job was first completed, the backup data might not be in a consistent state, because data could have been inserted, updated, or deleted while the backup was running. This initial backup file is known as the [raw backup](glossary.md). During a backup, **mysqlbackup** also copies the accumulated InnoDB log to a file called `ibbackup_logfile`. In an apply-log operation, the `ibbackup_logfile` file is used to “roll forward” the raw data files, so that every page in the data files corresponds to the same log sequence number of the InnoDB log. This is similar to the operation that takes place during a [crash recovery](glossary.md).

For single-file backups, the apply-log operation is usually performed as part of the [`copy-back-and-apply-log`](backup-commands-restore.md) command. For directory backups, the [`copy-back-and-apply-log`](backup-commands-restore.md) command can also be used, but you also have the two alternatives of

- Performing the apply-log operation together with the back up using the [`backup-and-apply-log`](backup-commands-backup.md) command (not applicable for incremental or compressed directory backups)
- Performing the apply-log operation separately with the `apply-log` command on the raw backup, before running the [`copy-back`](backup-commands-restore.md) command.

```
mysqlbackup [STD-OPTIONS]
            [--limit-memory=MB] [--uncompress] [--backup-dir=PATH]
            [MESSAGE-LOGGING-OPTIONS]
            [PROGRESS-REPORT-OPTIONS]
            [ENCRYPTED-INNODB-OPTIONS]
            apply-log
```

`apply-log`

*Advanced:* Brings the InnoDB tables in the directory backup up-to-date, including any changes made to the data while the backup was running.

**Example 19.1 Apply Log to Full Backup**

```
mysqlbackup --backup-dir=/path/to/backup apply-log
```

It reads the `backup-my.cnf` file inside *`backup-dir`* to understand the backup. The `my.cnf` defaults files have no effect other than supplying the ``limit-memory=*`MB`*`` value, which limits usage of memory while doing the `apply-log` operation.

### Apply-incremental-backup Operation

*Advanced:* Use the `apply-incremental-backup` to update a backup directory with data in an incremental backup directory:

```
mysqlbackup [STD-OPTIONS]
            [--incremental-backup-dir=PATH] [--backup-dir=PATH]
            [--limit-memory=MB] [--uncompress]
            [MESSAGE-LOGGING-OPTIONS]
            [PROGRESS-REPORT-OPTIONS]
            [ENCRYPTED-INNODB-OPTIONS]
            apply-incremental-backup
```

`apply-incremental-backup`

*Advanced:* Brings up-to-date a directory backup specified with the [`--backup-dir`](backup-repository-options.md) option, using the data from an incremental backup directory specified with the [`--incremental-backup-dir`](backup-incremental-options.md) option. See [Section 5.1.3, “Restoring an Incremental Backup”](restore.incremental.md) for instructions on restoring incremental backups.

For a single-file incremental backup, you typically use the [`copy-back-and-apply-log`](backup-commands-restore.md) command (with the [`--incremental`](backup-incremental-options.md) option for MySQL Enterprise Backup 8.0.20 and earlier) to apply the data in the incremental image backup to the full backup that has already been restored to the data directory of the target server.