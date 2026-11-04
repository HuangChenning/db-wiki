---
title: "5.1.7 Advanced: Preparing and Restoring a Directory Backup"
book: "MySQL Enterprise Backup User's Guide (Version 9.7.0)"
version: "9.7"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/9.7/en/backup-apply-log.html"
tags:
  - mysql
  - mysql-9.7
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 9.7.0)

### 5.1.7 Advanced: Preparing and Restoring a Directory Backup

A directory backup, just like a single-file backup, can be [prepared](glossary.md) and restored using the [`copy-back-and-apply-log`](backup-commands-restore.md) command as explained at the beginning of [Section 5.1, “Performing a Restore Operation”](restore.md).

**Example 5.10 Restoring a Backup Directory using copy-back-and-apply-log**

```
mysqlbackup --defaults-file=/usr/local/mysql/my.cnf \
  --backup-dir=/export/backups/full \
    copy-back-and-apply-log
```

However, two alternatives exist for directory backups:

- Perform the [apply log operation](backup-commands-update.md) on the [raw backup](glossary.md) right after the backup, or anytime before restore, using the [`apply-log`](backup-commands-update.md) command. You can run this step on the same database server where you did the backup, or transfer the raw backup files to a different system first, to limit the CPU and storage overhead on the database server. Here are some examples of doing that, on different kinds of directory backups:
	**Example 5.11 Applying the Log to a Backup**
	This example runs **mysqlbackup** to roll forward the data files so that the data is ready to be restored:
	```
	mysqlbackup --backup-dir=/export/backups/2011-06-21__8-36-58 apply-log
	```
	That command creates InnoDB log files (`ib_logfile*`) within the backup directory and applies log records to the InnoDB data files (`ibdata*` and `*.ibd`). For a compressed backup, there is no need to add the `--uncompress` option.
- For backups that are non-incremental, you can combine the initial backup and the [`apply-log`](backup-commands-update.md) steps using the [`backup-and-apply-log`](backup-commands-backup.md) command.

After the backup has been prepared, you can now restore it using the [`copy-back`](backup-commands-restore.md) command:

```
mysqlbackup --defaults-file=/usr/local/mysql/my.cnf \
  --backup-dir=/export/backups/full \
    copy-back
```