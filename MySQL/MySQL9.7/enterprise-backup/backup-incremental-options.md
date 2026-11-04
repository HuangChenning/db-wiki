---
title: "20.7 Incremental Backup Options"
book: "MySQL Enterprise Backup User's Guide (Version 9.7.0)"
version: "9.7"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/9.7/en/backup-incremental-options.html"
tags:
  - mysql
  - mysql-9.7
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 9.7.0)

For an overview of incremental backups and usage examples for these options, see [Section 4.3.3, “Making a Differential or Incremental Backup”](mysqlbackup.incremental.md) and [Section 5.1.3, “Restoring an Incremental Backup”](restore.incremental.md).

To take an incremental backup, specify the `--incremental` or `--incremental-with-redo-log-only`, along with the [`--backup-dir`](backup-repository-options.md) option. Depending on whether `--incremental` or `--incremental-with-redo-log-only` is used, other options are required or recommended. All InnoDB data modified after the [LSN](glossary.md) (specified directly or indirectly by the options you use) is copied into the incremental backup.

- `--incremental` \[={ `page-track|full-scan|optimistic` }\]
	| Command-Line Format | `--incremental` |
	| --- | --- |
	| Type | Enumeration |
	| Default Value | `page-track` |
	| Valid Values | `page-track`  `full-scan`  `optimistic` |
	Possible values for this option and their effects are explained further in the following list:
	- `page-track`: **mysqlbackup** looks for changed pages in `InnoDB` data files that have been modified since the last backup, using the page tracking functionality on the server, and then copies them. This is potentially the fastest way for **mysqlbackup** to create incremental backups.
		If page tracking cannot be used (see [Incremental Backup Using Page Tracking](mysqlbackup.incremental.md)) and `--incremental` is not set explicitly, **mysqlbackup** performs a full-scan backup instead. If this value has been set explicitly but page tracking cannot be used, the backup fails with an error.
	- `full-scan`: **mysqlbackup** scans all `InnoDB` data files in the server data directory to find pages that have been changed since the last backup, and copies them.
	- `optimistic`: **mysqlbackup** scans only for changed pages in the `InnoDB` data files that have been modified since the last backup and then copies them. In general, optimistic incremental backups are faster than full-scan backups when not many tables in the database have been modified. Some restrictions apply when this option is employed; see [Full-scan versus Optimistic Incremental Backup](mysqlbackup.incremental.md).
	`--incremental` also requires the use of either `--incremental-base` or `--start-lsn`. Only `InnoDB` tables are backed up incrementally. By default, *all* files are included in the incremental backup in their entirety. To exclude data that is not specific to *InnoDB* in an incremental backup, use [`--only-innodb`](backup-partial-options.md).
	When [`--copy-back-and-apply-log`](backup-commands-restore.md), [`--copy-back`](backup-commands-restore.md), or [`--apply-log`](backup-commands-update.md) is used, there is no need to use `--incremental`.
- `--incremental-with-redo-log-only`
	Specifies that an [incremental](glossary.md) backup is to be created using only the redo log. This alternate type of incremental backup has different performance characteristics and operational limitations compared to backups created with the `--incremental` option; see [Creating Incremental Backups Using Only the Redo Log](mysqlbackup.incremental.md) for a discussion on their differences, and for how to perform properly a redo-log-only incremental backup.
	To use this option, you also need to specify the `--incremental-base` option or the `--start-lsn`. Just like with the `--incremental` option, only InnoDB tables are backed up incrementally. By default, all non-InnoDB files are included into the incremental backup and in their fullness. To exclude non-InnoDB data in an incremental backup, use the [`--only-innodb`](backup-partial-options.md) option.
	You cannot use the [`--compress`](backup-compression-options.md) option together with the `--incremental-with-redo-log-only` option.
- `--incremental-base` = *`mode`*:*`argument`*
	| Command-Line Format | `--incremental-base=mode:argument` |
	| --- | --- |
	| Type | String |
	With this option, the **mysqlbackup** retrieves the information needed to perform incremental backups from the metadata inside the backup directory rather than from the `--start-lsn` option. It saves you from having to specify an ever-changing, unpredictable [LSN](glossary.md) value when doing a succession of incremental backups. Instead, you specify a way to locate the previous backup directory through the combination of *`mode`*: *`argument`* in the option syntax. The alternatives are:
	- `history:{last_backup | last_full_backup}                 `
		The prefix `history:` followed by one of the two possible values:
		- `last_backup`: This makes **mysqlbackup** query the `end_lsn` value from the last successful [non-TTS backup](glossary.md) as recorded in the `backup_history` table of the server instance that is being backed up.
		- `last_full_backup`: This works similarly as the value `last_backup`, except that it makes **mysqlbackup** look for the last [full backup](glossary.md) that was taken and use it as the base backup, thus creating a differential backup.
		Note
		If the last full or partial backup made was a [TTS](glossary.md) backup, **mysqlbackup** skips it, and keeps searching the backup history until it finds the last [non-TTS backup](glossary.md) and then returns its `end_lsn` value.
	- ``dir:*`directory_path`*``
		*Advanced*: You specify the prefix `dir:` followed by a directory path argument, which points to the previous directory backup. With the first incremental backup, you specify the directory holding the full directory backup; with the second incremental backup, you specify the directory holding the first incremental directory backup, and so on.
- `--start-lsn` = *`LSN`*
	| Command-Line Format | `--start-lsn=LSN` |
	| --- | --- |
	| Type | Numeric |
	In an [incremental backup](glossary.md), specifies the highest [LSN](glossary.md) value included in a previous backup. You can get this value from the output of the previous backup operation, or from the `backup_history` table's `end_lsn` column for the previous backup operation. Always used in combination with the `--incremental` option; not needed when you use the `--incremental-base` option; not recommended when you use the `--incremental-with-redo-log-only` mechanism for incremental backups.
	Note
	No binary log files are copied into the incremental backup if the `--start-lsn` option is used. To include binary log files for the period covered by the incremental backup, instead of `--start-lsn`, use the `--incremental-base` option, which provides the necessary information for **mysqlbackup** to ensure that no gap exists between binary log data included in the previous backup and the current incremental backup.
- `--incremental-backup-dir` = *`PATH`*
	*Advanced:* Specifies the location for data of an incremental directory backup. When creating or restoring an incremental directory backup, the option serves the same function as [`--backup-dir`](backup-repository-options.md) does for backups and restores in general, and the option can in fact be used interchangeably with [`--backup-dir`](backup-repository-options.md) for directory backups. See the description for [`--backup-dir`](backup-repository-options.md) for details.
	For an [`apply-incremental-backup`](backup-commands-update.md) operation, the option specifies the incremental backup directory whose data is used to update a directory backup specified by the [`--backup-dir`](backup-repository-options.md) option.
	Note
	Do not use this option with any operations for image backups, for which the option has no meaning.