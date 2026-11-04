---
title: "20.4 Backup Repository Options"
book: "MySQL Enterprise Backup User's Guide (Version 8.0.46)"
version: "8.0"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/8.0/en/backup-repository-options.html"
tags:
  - mysql
  - mysql-8.0
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 8.0.46)

These options specify various parameters related to the backup image or directory, or to how the backup will be restored. Typically, `--backup-image` and `--backup-dir` are the only options from the group that you need to specify when using **mysqlbackup**.

The backup repository options are used with the following operations:

The backup repository options are divided into two groups: the first one determines the structure of the backup, and the second one provides information on the original structure of the data on the backed-up server for future operations on the backup.

The following options determine the structure of the backup:

- `--backup-image` = *`IMAGE`*
	| Command-Line Format | `--backup-image=IMAGE` |
	| --- | --- |
	| Type | File name |
	Specify the path name of the file used for a single-file backup, restore, or another [single-file operation](backup-commands-single-file.md).
	By default, the single-file backup is streamed to standard output, so that you can pipe it directly to other commands such as a tape backup or an **ssh** -related network command. This default behavior occurs when the `--backup-image` option is omitted from the command, or when the command has `--backup-image=-`.
	Except when `--backup-image=-`, if the `--backup-image` option is used but its value is not a full file path, this is how **mysqlbackup** interprets the value of the option:
	- *For release 8.0.18 and earlier:* **mysqlbackup** takes the value of `--backup-image` as a path relative to the location specified by `--backup-dir`. For [`backup-to-image`](backup-commands-backup.md) operations, if the `--with-timestamp` option is also used, the backup image is then saved in a subdirectory that bears the timestamp in its name under the [backup directory](glossary.md).
	- *For release 8.0.19 and 8.0.20:* **mysqlbackup** takes the value of `--backup-image` as a path relative to the current working directory in which the **mysqlbackup** command is run. For [`backup-to-image`](backup-commands-backup.md) operations, if the `--with-timestamp` option is also used, it is ignored.
	- *For release 8.0.21 and later:*
		- For [`backup-to-image`](backup-commands-backup.md) operations, **mysqlbackup** takes the value of `--backup-image` as a path relative to the location specified by `--backup-dir`. If the `--with-timestamp` option is also used, the backup image is then saved in a subdirectory that bears the timestamp in its name under the [backup directory](glossary.md).
		- For [`copy-back-and-apply-log`](backup-commands-restore.md) and [single-file operations](backup-commands-single-file.md) other than [`backup-to-image`](backup-commands-backup.md), **mysqlbackup** takes the value of `--backup-image` as a path relative to the current working directory in which the **mysqlbackup** command is run.
	You can optionally prefix the image name with `file:` to signify a file I/O (the default). For tape backups, prefix the image name with `sbt:`. See [Section 4.3.1.2, “Backing Up to Tape”](meb-backup-tape.md) for details about tape backups.
- `` `--backup_dir`=*`PATH`* ``
	Same as `--backup-dir`. The [backup directory](glossary.md) under which the backup data and metadata are stored, permanently or temporarily. It is a crucial parameter required for most kinds of backup and restore operations.
	The option is used differently for different operations and under different situations:
	- *For backup to a single file (including incremental, compressed, encrypted, and cloud backups):* Use `--backup-dir` to supply a temporary folder to save the backup metadata (including the **mysqlbackup** message log, the start and end [LSN](glossary.md), and so on) and some temporary output. The backup data, together with a copy of the metadata, will be stored in a singe file whose name is specified with the `--backup-image` option.
		However, if `--backup-image` does not give a full path name, **mysqlbackup** will actually take the value of `--backup-image` as a path relative to the directory specified by `--backup-dir`, and thus store the single-file backup under `--backup-dir` (or, if the `--with-timestamp` option is used, under a subdirectory created under `--backup-dir`, which bears the timestamp in its name).
		Note
		*For release 8.0.19 and 8.0.20 only:* A relative path specified for `--backup-image` is taken to be relative to the directory in which the [`backup-to-image`](backup-commands-backup.md) command is run.
	- *For backup to a directory:* Use `--backup-dir` to specify the directory to store the backup data and metadata (including the **mysqlbackup** message log, the start and end [LSN](glossary.md), and so on). The directory specified by `--backup-dir` cannot be a subdirectory of the directory specified by [`--datadir`](server-repository-options.md).
		When the `--with-timestamp` option is also specified, an additional level of subdirectory, with the timestamp in its name, is created under `--backup-dir` (see description for the `--with-timestamp` option for details). Unless the `--with-timestamp` option is used, the directory specified by `--backup-dir` must be empty, or the backup operation will fail with an error.
	- *For restoring a single-file backup (including incremental, compressed, encrypted, and cloud backups):* When using [`copy-back-and-apply-log`](backup-commands-restore.md) to restore a single-file backup, use `--backup-dir` to supply a temporary folder to store the temporary data of the restore operation. The directory specified by `--backup-dir` should be empty—if a non-empty directory is used, the restore operation will still be carried out, but the restore data might be corrupted.
		When restoring a single-file backup created with the option setting [`use-tts`](backup-partial-options.md) = `with-minimum-locking`, the folder specified with `--backup-dir` is also used for extracting temporarily all the tables in the backup and for performing an [`apply-log`](backup-commands-update.md) operation to make the data up-to-date before restoring them to the server's data directory.
	- *For restoring a backup directory:* Use `--backup-dir` to specify the location of the backup directory, from which data will be restored to the server.
- `backup_innodb_data_home_dir` = *`PATH`*
	The directory under which the backup's InnoDB data files are to be stored. Specify the option if you want to put the data files at somewhere other than the default location (which is ``*`backup-dir`*/datadir``). If the value of the parameter is different from ``*`backup-dir`*/datadir``, it is stored into the `backup-my.cnf` file as [`innodb_data_home_dir`](server-repository-options.md) for information, so that **mysqlbackup** can understand the structure of the backup when it performs various operations on the backup. Together with the `backup_innodb_data_file_path` option, it determines the actual file paths of the InnoDB data files inside the backup.
	*For release 8.0.17 and later,* the value for the parameter is derived as follows:
	- If `backup_innodb_data_home_dir` is not specified, its value will be ``*`backup-dir`*/datadir``.
	- If `backup_innodb_data_home_dir` is an absolute path, its value is used as-is, unless it points to a location that is under *`backup-dir`* but is not equal to ``*`backup-dir`*/datadir``, in which case **mysqlbackup** will throw an error and abort the operation.
	- If `backup_innodb_data_home_dir` is a relative path, the path is taken to be relative to (that is, underneath) *`backup-dir`*, and it should point to ``*`backup-dir`*/datadir``, or **mysqlbackup** will throw an error and abort the operation.
	- An empty string (“”) for `backup_innodb_data_home_dir` means the value of `backup_innodb_data_file_path` is to be taken as an absolute path.
	*For release 8.0.16 and before,* the value for the parameter is derived as follows:
	- If `backup_innodb_data_home_dir` is not specified, its value will be ``*`backup-dir`*/datadir``.
	- If `backup_innodb_data_home_dir` is an absolute path, its value is used as-is.
	- If `backup_innodb_data_home_dir` is a relative path, the path is taken to be relative to (that is, underneath) *`backup-dir`*.
	- An empty string (“”) for `backup_innodb_data_home_dir` means the value of `backup_innodb_data_file_path` is to be taken as an absolute path.
	This parameter is applicable only for backup operations; during a restore, the InnoDB data files are restored under the data directory specified by [`--datadir`](server-repository-options.md), unless another location is specified using the [`--innodb_data_home_dir`](server-repository-options.md) option during restore.
- `backup_innodb_data_file_path` = *`VALUE`*
	The InnoDB data file names and sizes. Examples:
	```
	ibdata1:32M;ibdata2:32M:autoextend
	/abs/path/ibdata1:32M:autoextend
	innodb-dir/ibdata1:32M:autoextend
	```
	This parameter, together with `backup_innodb_data_home_dir`, determines where the InnoDB data files are stored within the backup repository. Any file path specified with this option is taken to be relative to the value of the `backup_innodb_data_home_dir` option (that is true even if the file path is specified in the form of an absolute path, like `/abs/path/ibdata1:32M:autoextend`). To specify truly absolute paths for InnoDB data files in the backup with this option, you must set the `backup_innodb_data_home_dir` option to `""` \[empty string\], in addition to using an absolute path for this option.
	When the parameter is not specified, it inherits the value from the value of the [`innodb_data_file_path`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/innodb-parameters.html#sysvar_innodb_data_file_path) option on the backed-up server. If both the source and destination of the backup attempt to use the same absolute paths that resolves to the same files, the backup is cancelled.
	The value of the parameter is stored into the `backup-my.cnf` file as `innodb_data_file_path` for information, so that **mysqlbackup** can understand the structure of the backup when it performs various operations on the backup.
- `backup_innodb_log_group_home_dir` = *`PATH`*
	The directory under which the backup's InnoDB logs will be stored. Specify this option only if you want to put the logs at somewhere other than the default location (which is ``*`backup-dir`*/datadir``). If the value of the parameter is different from ``*`backup-dir`*/datadir``, it is stored in the `backup-my.cnf` file as `innodb_log_group_home_dir` for information, so that **mysqlbackup** can understand the structure of the backup when it performs various operations on the backup. Note that while you can specify a directory for saving the logs, the names of the log files are fixed and not reconfigurable by this option.
	*For release 8.0.17 and later,* the value for the parameter is derived as follows:
	- If `backup_innodb_log_group_home_dir` is not specified, its value will be ``*`backup-dir`*/datadir``.
	- If `backup_innodb_log_group_home_dir` is an absolute path, its value is used as-is, unless it points to a location that is under *`backup-dir`* but is not equal to ``*`backup-dir`*/datadir``, in which case **mysqlbackup** will throw an error and abort the operation.
	- If `backup_innodb_log_group_home_dir` is a relative path, the path is taken to be relative to (that is, underneath) *`backup-dir`*, and it should point to ``*`backup-dir`*/datadir``, or **mysqlbackup** will throw an error and abort the operation.
	- An empty string (“”) for the option produces an error.
	*For release 8.0.16 and before,* the value of the parameter is derived as follows:
	- If `backup_innodb_log_group_home_dir` is not specified, its value will be ``*`backup-dir`*/datadir``.
	- If `backup_innodb_log_group_home_dir` is an absolute path, its value is used as-is.
	- If `backup_innodb_log_group_home_dir` is a relative path, the path is taken to be relative to (that is, underneath) *`backup-dir`*.
	- An empty string (“”) for the option produces an error.
	This parameter is applicable only for backup operations; during a restore, the InnoDB log files are restored under the data directory specified by [`--datadir`](server-repository-options.md), unless another location is specified using the [`--innodb_log_group_home_dir`](server-repository-options.md) option during restore.
- `backup_innodb_undo_directory` = *`PATH`*
	The relative or absolute directory path where separate tablespaces are created for the InnoDB undo logs during the backup. Specify the option if you want to put the undo logs at somewhere other than the default location (which is `backup_innodb_log_group_home_dir`). If the value of the parameter is different from ``*`backup-dir`*/datadir``, it is stored in the `backup-my.cnf` file as `innodb_undo_directory` for information, so that **mysqlbackup** can understand the structure of the backup when it performs various operations on the backup.
	The value for the parameter is derived as follows:
	- If `backup_innodb_undo_directory` is not specified, the option takes up the same value as `backup_innodb_log_group_home_dir`.
	- If `backup_innodb_undo_directory` is an absolute path, its value is used as-is, unless it points to a location that is under *`backup-dir`* but is not equal to ``*`backup-dir`*/datadir``, in which case **mysqlbackup** will throw an error and abort the operation.
	- If `backup_innodb_undo_directory` is a relative path, the path is taken to be relative to (that is, underneath) *`backup-dir`* and it should point to ``*`backup-dir`*/datadir``, or **mysqlbackup** will throw an error and abort the operation.
	- An empty string (“”) for the option produces an error.
	This parameter is applicable only for backup operations; see the description for [undo log files](meb-files-backed-up-summary.md) on where undo logs are restored.
- `--with-timestamp`
	Creates a subdirectory underneath the backup directory, with a name formed with the timestamp of the backup operation. It is useful for maintaining a single backup directory containing many backup snapshots put under different subdirectories.
	Default: no timestamped subdirectory is created. To reuse the same backup directory for a new backup without using this option, remove the previous backup image or backup files manually.