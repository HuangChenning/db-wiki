---
title: "19.3 Restore Operations"
book: "MySQL Enterprise Backup User's Guide (Version 9.7.0)"
version: "9.7"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/9.7/en/backup-commands-restore.html"
tags:
  - mysql
  - mysql-9.7
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 9.7.0)

The restore operations restores the data files from a backup to their original locations on the database server, or to other desired locations. Normally, the restoration process requires the database server to be already shut down (or, at least not operating on the directory you are restoring the data to), except for a [partial restore](restore.partial.md). The option [`datadir`](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/server-system-variables.html#sysvar_datadir) must be specified either in the file specified by the [`--defaults-file`](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/option-file-options.html#option_general_defaults-file) option or as a command-line option. For usage examples, see [Chapter 5, *Recovering or Restoring a Database Server*](restoring.md).

```
mysqlbackup [STD-OPTIONS]
            [SERVER-REPOSITORY-OPTIONS]
            [--backup-image=IMAGE]
            [--backup-dir=PATH]
            [--uncompress]
            [MESSAGE-LOGGING-OPTIONS]
            [PARTIAL-BACKUP-RESTORE-OPTIONS]
            [PROGRESS-REPORT-OPTIONS]
            [ENCRYPTION-OPTIONS]
            [CLOUD-STORAGE-OPTIONS]
            [ENCRYPTED-INNODB-OPTIONS]
            copy-back-and-apply-log 
mysqlbackup [STD-OPTIONS]
            [SERVER-REPOSITORY-OPTIONS]
            [--backup-dir=PATH]
            [--uncompress]
            [MESSAGE-LOGGING-OPTIONS]
            [PARTIAL-BACKUP-RESTORE-OPTIONS]
            [PROGRESS-REPORT-OPTIONS]
            [CLOUD-STORAGE-OPTIONS]
            [ENCRYPTED-INNODB-OPTIONS]
            copy-back
```

- `copy-back-and-apply-log`
	In a single step, restores a [single-file backup](glossary.md) specified by the [`--backup-image`](backup-repository-options.md) option or a backup from the directory specified by the [`--backup-dir`](backup-repository-options.md) option to a server's data directory and performs an [`apply-log`](backup-commands-update.md) operation to the restored data to bring them up-to-date. Comparing with a multi-step approach for restoring a [single-file backup](glossary.md) (which typically consists of performing the successive steps of [extract](backup-commands-single-file.md), [uncompress](backup-compression-options.md), [apply-log](backup-commands-update.md), and copy-back for restoring compressed image, or [extract](backup-commands-single-file.md),[apply-log](backup-commands-update.md), and copy-back for uncompressed image), the command makes the restoration process simpler and faster, and also saves the disk space required.
	The following are some special requirements for different kinds of backup restoration using `copy-back-and-apply-log`:
	- To restore a single-file backup, besides specifying the location of the backup image with the [`--backup-image`](backup-repository-options.md) option, also supply with the [`--backup-dir`](backup-repository-options.md) option the location of a folder that will be used for storing temporary files produced during the restoration process.
	- To restore a single-file incremental backup, assuming the full backup (on which the incremental backup was based) has already been restored:
		- Specifies the location of the incremental backup image with the [`--backup-image`](backup-repository-options.md) option.
		- Supplies with the [`--backup-dir`](backup-repository-options.md) option the location of a folder that will be used for storing temporary files produced during the restoration process.
	- *Advanced:* To restore an incremental backup directory, assuming the full backup (on which the incremental backup was based) has already been restored:
		- Use either the [`--backup-dir`](backup-repository-options.md) or [`--incremental-backup-dir`](backup-incremental-options.md) option to specify the incremental backup directory.
	- To restore selected tables:
		- See the general requirements described in [Section 5.1.4, “Table-Level Recovery (TLR)”](restore.partial.md).
		- When restoring a single-file backup created with the option setting [`--use-tts=with-minimum-locking`](backup-partial-options.md), the folder specified with [`--backup-dir`](backup-repository-options.md) is also used for extracting temporarily all the tables in the backup and for performing an [`apply-log`](backup-commands-update.md) operation to make the data up-to-date before restoring them to the server's data directory.
		- *Advanced:* When restoring a backup directory created with the option [`--use-tts=with-minimum-locking`](backup-partial-options.md), an [`apply-log`](backup-commands-update.md) operation will be performed on the backup directory. That means the backup taken will be altered during the process, and users might want to make an extra copy of the backup directory before proceeding with the restoration, in order to prevent the loss of backup data in case something goes wrong.
	Also note that:
	- Backups created with the [`--skip-unused-pages`](backup-capacity-options.md) option cannot be restored using `copy-back-and-apply-log`.
	At the end of the `copy-back-and-apply-log` operation, the file `backup_variables.txt` is being created or updated in the data directory. This file contains metadata about the restored contents and is being used by successive single-step restores of incremental backups; it should not be deleted or modified by users.
	For some sample commands for restoring different kinds of backups with the `copy-back-and-apply-log` command, see [Section 5.1, “Performing a Restore Operation”](restore.md).
- `copy-back`
	Restores files from a directory backup to their original locations within the MySQL server.
	Before restoring a [hot backup](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/glossary.html#glos_hot_backup) using the `copy-back` command, the backup has to be [prepared](glossary.md) and made consistent using the [`apply-log`](backup-commands-update.md) command. See [Section 5.1.7, “Advanced: Preparing and Restoring a Directory Backup”](backup-apply-log.md) for details. You can also perform [`apply-log`](backup-commands-update.md) and `copy-back` together with a single `copy-back-and-apply-log` command.
	Some clean-up efforts on the target directory for restoration might be needed before performing a full restore (for example, when the backup data is used to set up a new MySQL server or to replace all data of an existing MySQL server). See the discussions [here](restore.md) for details.
	There are some special requirements when restoring selected tables from backups; see [Section 5.1.4, “Table-Level Recovery (TLR)”](restore.partial.md) for details.

Warning

When restoring a server for [replication](meb-replication.md) purpose, if the backed-up server has used the [`innodb_undo_directory`](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/innodb-parameters.html#sysvar_innodb_undo_directory) option to put the undo logs outside of the data directory, when using the file `server-my.cnf` or `server-all.cnf` for the [`--defaults-file`](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/option-file-options.html#option_general_defaults-file) option with `copy-back` or `copy-back-and-apply-log`, care should be taken to configure correctly the [`innodb_undo_directory`](server-repository-options.md) option in the file. Otherwise, the data or log files on the original server might be overwritten by accident.