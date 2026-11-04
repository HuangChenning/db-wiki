---
title: "5.1.3 Restoring an Incremental Backup"
book: "MySQL Enterprise Backup User's Guide (Version 8.0.46)"
version: "8.0"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/8.0/en/restore.incremental.html"
tags:
  - mysql
  - mysql-8.0
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 8.0.46)

### 5.1.3 Restoring an Incremental Backup

Note

For MySQL Enterprise Backup 8.0.21 and later: The [`--incremental`](backup-incremental-options.md) option is no longer needed when restoring an incremental backup.

There are different ways to use incremental backups to restore a database server under different scenarios. The preferred method is to first restore the full backup and make it up-to-date to the time at which the full backup was performed using the [`copy-back-and-apply-log`](backup-commands-restore.md) command (see [Example 5.1, “Restoring a Database Server”](restore.md) on how to do it), then use [`copy-back-and-apply-log`](backup-commands-restore.md) again to restore the incremental backup image on top of the full backup that was just restored:

**Example 5.6 Restoring an Incremental Backup Image**

```
mysqlbackup --defaults-file=<my.cnf> -uroot --backup-image=<inc_image_name> \
  --backup-dir=<incBackupTmpDir> --datadir=<restoreDir> --incremental \
  copy-back-and-apply-log
```

In this example, the incremental backup image named *`<inc_image_name>`* is restored to *`<restoreDir>`* on the server (where the full backup that the incremental backup image was based on has already been restored). The [`--backup-dir`](backup-repository-options.md) option is used to specify the temporary directory into which temporary output, status files, and backup metadata are saved. Repeat the step with other incremental backup images that you have, until the data has been restored to a desired point in time.

#### Advanced: Restoring an Incremental Backup Directory

Incremental directory backups can be restored in a series of [`copy-back-and-apply-log`](backup-commands-restore.md) command, as illustrated above for single-file backups. Alternatively, at anytime after an incremental backup is taken and before the data is restored, you can bring your full backup up-to-date with your incremental backup. First, apply to the full backup any changes that occurred while the backup was running:

```
$ mysqlbackup --backup-dir=/full-backup/2010-12-08_17-14-11 apply-log
..many lines of output...
101208 17:15:10  mysqlbackup: Full backup prepared for recovery successfully!

101208 17:15:10 mysqlbackup: mysqlbackup completed OK!
```

Then, we apply the changes from the incremental backup using the [`apply-incremental-backup`](backup-commands-update.md) command:

```
$ mysqlbackup --incremental-backup-dir=/incr-backup/2010-12-08_17-14-48 \
  --backup-dir=/full-backup/2010-12-08_17-14-11 apply-incremental-backup
...many lines of output...
101208 17:15:12 mysqlbackup: mysqlbackup completed OK!
```

Now, the data files in the full backup directory are fully up-to-date, as of the time of the last incremental backup. You can keep updating it with more incremental backups, so it is ready to be restored anytime.

#### Binary Log and Relay Log Restore

When an incremental backup is being restored using either the [`copy-back-and-apply-log`](backup-commands-restore.md) or [`apply-incremental-backup`](backup-commands-update.md) command, the binary log (and also the relay log, in the case of a replica server), if included in the incremental backup, is also restored to the target server by default. This default behavior is overridden when either (1) the [`--skip-binlog`](backup-capacity-options.md) option (or the [`--skip-relaylog`](backup-capacity-options.md) option for the relay log) is used with the restore command, or (2) if the full backup the incremental backup was based on or any prior incremental backup that came in between the full backup and this incremental backup has the binary log (or relay log) missing (in both case, *for MySQL Enterprise Backup 8.0.19 and later*, **mysqlbackup** renamed any binary log (but not relay log) files and their index files that have already been restored onto the server by adding the `.old` extension to their file names).

Location of the binary log (or relay log) after an incremental backup is restored is, by default, the same as the log's location on the backed-up server when the incremental backup was taken, or as specified by the [`--log-bin`](server-repository-options.md) (or [`--relay-log`](server-repository-options.md)) option during the restore of the incremental backup.

See [Section 4.3.3, “Making a Differential or Incremental Backup”](mysqlbackup.incremental.md), and [Section 20.7, “Incremental Backup Options”](backup-incremental-options.md), for more details on incremental backups.