---
title: "20.8 Partial Backup and Restore Options"
book: "MySQL Enterprise Backup User's Guide (Version 9.7.0)"
version: "9.7"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/9.7/en/backup-partial-options.html"
tags:
  - mysql
  - mysql-9.7
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 9.7.0)

To select specific data to be backed up or restored, use the partial backup and restore options described in this section.

For an overview of partial backup and restore, as well as usage examples on the following options, see [Section 4.3.5, “Making a Partial Backup”](partial.md) and [Section 5.1.4, “Table-Level Recovery (TLR)”](restore.partial.md).

- `--include-tables` = *`REGEXP`*
	| Command-Line Format | `--include-tables=REGEXP` |
	| --- | --- |
	| Type | String |
	Include for backup or restoration only those tables (both Innodb and non-Innodb) whose fully qualified names (in the form of ``*`db_name`*.*`table_name`*``) match the regular expression *`REGEXP`*. The regular expression syntax used is the extended form specified in the POSIX 1003.2 standard. For example, `--include-tables=^mydb\.t[12]$` matches the tables `t1` and `t2` in the database `mydb`. On Unix-like systems, quote the regular expression appropriately to prevent interpretation of shell meta-characters. **mysqlbackup** throws an error when the option is used without a regular expression being supplied with it.
	While **mysqlbackup** understands the MySQL convention of quoting the database or the table name (or both) by backticks (see [Schema Object Names](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/identifiers.html)), there is no need to include the backticks in the regular expression for `--include-tables`.
	The option can also be used with the [`backup-dir-to-image`](backup-commands-single-file.md) and [`image-to-backup-dir`](backup-commands-single-file.md) commands to select tables when creating or unpacking a backup image.
	**mysqlbackup** throws an error when no table matches the regular expression specified with `--include-tables`.
	When used together with the `--exclude-tables` option, `--include-tables` is applied first, meaning **mysqlbackup** first selects all tables specified by `--include-tables` and then excludes from the set those tables specified by `--exclude-tables`.
	The option cannot be used together with the legacy `--include` option.
- `--exclude-tables` = *`REGEXP`*
	| Command-Line Format | `--exclude-tables=REGEXP` |
	| --- | --- |
	| Type | String |
	Exclude for backup or restoration all tables (both Innodb and non-Innodb) whose fully qualified names (in the form of ``*`db_name`*.*`table_name`*``) match the regular expression *`REGEXP`*. The regular expression syntax is the extended form specified in the POSIX 1003.2 standard. For example, `--exclude-tables=^mydb\.t[12]$` matches the tables `t1` and `t2` in the database `mydb`. On Unix-like systems, quote the regular expression appropriately to prevent interpretation of shell meta-characters. **mysqlbackup** throws an error when the option is used without a regular expression being supplied with it.
	While **mysqlbackup** understands the MySQL convention of quoting the database or the table name (or both) by backticks (see [Schema Object Names](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/identifiers.html)), there is no need to include the backticks in the regular expression for `--exclude-tables`.
	The option can also be used with the [`backup-dir-to-image`](backup-commands-single-file.md) and [`image-to-backup-dir`](backup-commands-single-file.md) commands to select tables when creating or unpacking a backup image.
	The option cannot be used together with the legacy `--include` option.
	When used together with the `--include-tables` option, `--include-tables` is applied first, meaning **mysqlbackup** first select all tables specified by `--include-tables`, and then exclude from the set those tables specified by `--exclude-tables`.
- `--only-known-file-types`
	For back up only. By default, all files in the database subdirectories under the data directory of the server are included in the backup (see [Table 1.1, “Types of Files in a Backup”](meb-files-backed-up-summary.md) for details). If the `--only-known-file-types` option is specified, **mysqlbackup** only backs up those types of files that are data files for MySQL or its built-in storage engines, which, besides the `ibdata*` files, have the following extensions:
	- `.ARM`: ARCHIVE table metadata
	- `.ARZ`: ARCHIVE table data
	- `.CSM`: CSV table metadata
	- `.CSV`: CSV table data
	- `.ibd`: InnoDB tablespace created using the file-per-table mode
	- `.MRG`: Merge storage engine references to other tables
	- `.MYD`: MyISAM data
	- `.MYI`: MyISAM indexes
- `--only-innodb`
	For back up only. Back up only InnoDB data and log files. All files created by other storage engines are excluded. Typically used when there is no need to copy MyISAM files.
	The option is not compatible with the [`--replica-info`](backup-special-options.md) option.
	Default: backups include files from all storage engines.
- `--use-tts` \[={ `with-minimum-locking|with-full-locking` }\]
	| Command-Line Format | `--use-tts[={with-minimum-locking\|with-full-locking}]` |
	| --- | --- |
	| Type | Enumeration |
	| Default Value | `with-minimum-locking` |
	| Valid Values | `with-minimum-locking`  `with-full-locking` |
	Enable selective backup of InnoDB tables using [transportable tablespaces (TTS)](glossary.md). This is to be used in conjunction with the `--include-tables` and `--exclude-tables` options for selecting the InnoDB tables to be backed up by regular expressions. Using [TTS](glossary.md) for backups offers the following advantages:
	- Backups can be restored to a different server
	- The [system tablespace](glossary.md) is not backed up, saving disk space and I/O resources
	- Data consistency of the tables is managed by MySQL Enterprise Backup
	However, the option has the following limitations:
	- Individual partitions cannot be selectively backed up or restored. Tables selected by the `--include-tables` and `--exclude-tables` options are always backed up or restored in full.
	- Can only backup tables that are stored in their own individual tablespaces (i.e., tables created with the [innodb\_file\_per\_table](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/glossary.html#glos_file_per_table) option enabled)
	- Non-InnoDB tables are not backed up
	- Cannot be used for incremental backups
	- Does not include the binary log or the relay log in the backup
	See also [Appendix B, *Limitations of MySQL Enterprise Backup*](bugs.backup.md) for some more minor limitations.
	There are two possible values for the option:
	- `with-minimum-locking`: Hot copies of the selected tables are backed up, and the tables are then locked in read-only mode while the [redo log](glossary.md) (with only the portion containing the relevant changes made after the hot backup) is being included in the backup. Any tables created during the locking phase are ignored.
	- `with-full-locking`: The selected tables are locked in read-only mode while they are being backed up. The [redo log](glossary.md) is not included in the backup. Any tables created during the locking phase are ignored.
		Note
		Due to a known issue, when creating a backup using TTS for a server containing tables with a mix of the Antelope and Barracuda file formats, do NOT apply full locking on the tables.
	Default: `with-minimum-locking`
	To use the `--use-tts` option, extra privileges are required of the user through which **mysqlbackup** connects to the server; see [Section 4.1.2, “Grant MySQL Privileges to Backup Administrator”](mysqlbackup.privileges.md) for details.
	There are some special requirements for restoring backups created with the `--use-tts` option; see [Section 5.1.5, “Restoring Backups Created with the `--use-tts` Option”](restore-use-tts.md) for details.
- `--rename` =“ *`old_table_name`* to *`new_table_name`* ”
	Rename a single table when it is selected by the `--include-tables` or `--exclude-tables` option (or both together) to be restored to a database server from a backup created using the `--use-tts` option. The table named *`old_table_name`* is renamed to *`new_table_name`*. Note that when using the option:
	- The `--include-tables` or `--exclude-tables` option (or both together) must be used in the restore command for the `--rename` option to work, unless there is only one table in the backup. Also, the `--include-tables` or `--exclude-tables` option (or both together) should specify one and only one table for restore when `--rename` is used, or the restore will fail.
	- *`old_table_name`* and *`new_table_name`* can be fully qualified (containing the database names, in the form of *`old_db_name`*.*`old_tb_name`* and *`new_db_name`*.*`new_tb_name`*) or not. By using fully-qualified table names, a table can be restored into a database different from its original one. If the database specified with *`new_db_name`* does not exist on the target server, it will be created during the restore process. Regular expressions are not accepted in the argument of the option.
	- The restore fails if *`old_table_name`* does not match with the table specified using the `--include-tables` or `--exclude-tables` option (or both together), or if *`new_table_name`* already exists in the target database.
	- The requirements listed in [Section 5.1.5, “Restoring Backups Created with the `--use-tts` Option”](restore-use-tts.md) apply.
	See [Section 5.1.5, “Restoring Backups Created with the `--use-tts` Option”](restore-use-tts.md), for more information on selective restores, and for an example of table renaming.

### Legacy Partial Backup Options

Important

Information in this subsection is only for using the legacy option of `--include`, which has been **deprecated**. For creating partial backups, use the `--include-tables` and `--exclude-tables` options instead.

Besides `--include`, some other options are also discussed below, but the information is only for using the options together with `--include`.

For an overview of partial backups and usage examples for these legacy options, see [Making a Partial Backup with the Legacy Options (Deprecated)](partial.md).

- `--include` = *`REGEXP`*
	This option is for filtering InnoDB tables for backup. The InnoDB tables' fully qualified names are checked against the regular expression specified by the option. If the REGEXP matches ``*`db_name`*.*`table_name`*``, the table is included. The regular expression syntax used is the extended form specified in the POSIX 1003.2 standard. For example, `--include=mydb\.t[12]` matches the tables `t1` and `t2` in the database `mydb`. **mysqlbackup** throws an error when the option is used without a regular expression being supplied with it.
	This option only applies to InnoDB tables created with the MySQL option [`innodb_file_per_table`](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/innodb-parameters.html#sysvar_innodb_file_per_table) enabled (which is the default setting for MySQL 5.6 and after), in which case the tables are in separate files that can be included or excluded from the backup. All tables in the InnoDB system tablespace are always backed up.
	When no InnoDB table names match the specified regular expression, an error is thrown with a message indicating there are no matches.
	Default: Backs up all InnoDB tables.
	Note
	This option does not filter non-InnoDB tables.
- `--use-tts` \[={ `with-minimum-locking|with-full-locking` }\]
	Enable selective backup of InnoDB tables using [transportable tablespaces (TTS)](glossary.md). This is to be used in conjunction with the `--include` option, which selects the InnoDB tables to be backed up by a regular expression. Using [TTS](glossary.md) for backups offers the following advantages:
	- Backups can be restored to a different server
	- The [system tablespace](glossary.md) is not backed up, saving disk space and I/O resources
	- Data consistency of the tables is managed by MySQL Enterprise Backup
	See important discussions here on the limitations with using the `--use-tts` option.
	There are two possible values for the option:
	- `with-minimum-locking`: Hot copies of the selected tables are backed up, and the tables are then locked in read-only mode while the [redo log](glossary.md) (with only the portion containing the relevant changes made after the hot backup) is being included in the backup. Any tables created during the locking phase are ignored.
	- `with-full-locking`: The selected tables are locked in read-only mode while they are being backed up. The [redo log](glossary.md) is not included in the backup. Any tables created during the locking phase are ignored.
	Default: back up with minimum locking
	There are some special requirements for restoring backups created with the `--use-tts` option; see the [explanations](restore-use-tts.md) in [Section 5.1, “Performing a Restore Operation”](restore.md) for details.