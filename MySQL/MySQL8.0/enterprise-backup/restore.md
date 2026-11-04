---
title: "5.1 Performing a Restore Operation"
book: "MySQL Enterprise Backup User's Guide (Version 8.0.46)"
version: "8.0"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/8.0/en/restore.html"
tags:
  - mysql
  - mysql-8.0
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 8.0.46)

The **mysqlbackup** commands to perform a restore operation are [`copy-back-and-apply-log`](backup-commands-restore.md) and [`copy-back`](backup-commands-restore.md) (for directory backup only; see [Section 5.1.7, “Advanced: Preparing and Restoring a Directory Backup”](backup-apply-log.md)). Normally, the restoration process requires the database server to be already shut down (or, at least not operating on the directory you are restoring the data to), except for a [partial restore](restore.partial.md). The process copies the data files, logs, and other backed-up files from the backup directory back to their original locations, and performs any required post-processing on them.

**Example 5.1 Restoring a Database Server**

```
mysqlbackup --defaults-file=<my.cnf> -uroot --backup-image=<image_name> \
  --backup-dir=<backupTmpDir> --datadir=<restoreDir> copy-back-and-apply-log
```

The [`copy-back-and-apply-log`](backup-commands-restore.md) command achieves two things:

- Extracts the backup from the image file and copies it to the data directory on the server to be restored.
- Performs an [apply log operation](backup-commands-update.md) to the restored data to bring them up-to-date.

See [Section 4.2.4, “Restoring a Database”](mysqlbackup.restore.md) for an explanation of the important options used in a restore operation like [`--defaults-file`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/option-file-options.html#option_general_defaults-file), [`--datadir`](server-repository-options.md), [`--backup-image`](backup-repository-options.md), and [`--backup-dir`](backup-repository-options.md).

The restored data includes the `backup_history` table, where MySQL Enterprise Backup records details of each backup. The table allows you to perform future incremental backups using the [`` --incremental-base=`history:{last_backup       | last_full_backup}` ``](backup-incremental-options.md) option.

Important

- When performing a restore, make sure the target directories for restore data are all clean, containing no old or unwanted data files (this might require manual removal of files at the locations specified by the [`--datadir`](server-repository-options.md), [`--innodb_data_home_dir`](server-repository-options.md), [`--innodb_log_group_home_dir`](server-repository-options.md), and [`--innodb_undo_directory`](server-repository-options.md) options). The same cleanup is not required for partial restores, for which other requirements described in [Section 5.1.4, “Table-Level Recovery (TLR)”](restore.partial.md) apply.
- After a full restore, depending on how you are going to start the restored server, you might need to adjust the ownership of the restored data directory. For example, if the server is going to be started by the user `mysql`, use the following command to change the owner attribute of the data directory and the files under it to the `mysql` user, and the group attribute to the `mysql` group.
	```
	$ chown -R mysql:mysql /path/to/datadir
	```

The following subsections describe a number of different scenarios for restoring a backup.