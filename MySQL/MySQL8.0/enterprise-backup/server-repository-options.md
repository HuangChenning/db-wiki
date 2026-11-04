---
title: "20.3 Server Repository Options"
book: "MySQL Enterprise Backup User's Guide (Version 8.0.46)"
version: "8.0"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/8.0/en/server-repository-options.html"
tags:
  - mysql
  - mysql-8.0
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 8.0.46)

These repository options specify various parameters related to the database server to which a backup is restored.

These options are used only with restore operations, that is, [`copy-back`](backup-commands-restore.md) and [`copy-back-and-apply-log`](backup-commands-restore.md). The descriptions below explain how these options are used with **mysqlbackup**; for information about how these options are used with the MySQL server, click the option names to see the descriptions in the MySQL Reference Manual.

- `datadir` = *`PATH`*
	This is the data directory for the restored MySQL server. It should be supplied with the [`datadir`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/server-system-variables.html#sysvar_datadir) value of the target server for the restore.
	This option must be specified for any restore operations, except for partial restores (see [Section 5.1.4, “Table-Level Recovery (TLR)”](restore.partial.md) for details).
- `log-bin` \[= *`basename`*\]
	Specify the location for the binary log to be restored. By default, during a restore, the binary log is restored to the same location it was found on the backed-up server. Use this option to specify a different target location for the binary log. The option works similarly as the [`--log-bin`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/replication-options-binary-log.html#option_mysqld_log-bin) option of the MySQL server in determining the location and the name of the binary log files—see [description of the server --log-bin option](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/replication-options-binary-log.html#option_mysqld_log-bin) for details. As a summary:
	- Using this option without supplying a ``*`basename`*`` puts the binary log in the target server's data directory with the default basename ``*`host_name`*-bin``.
	- Using this option while supplying a ``*`basename`*`` puts the binary log in the target server's data directory with the specified basename.
	- Using this option while supplying a ``*`basename`*`` containing a full file path (for example, `/home/admin/db/binlogdir/binlog`) puts the binary log on the target server in the specified folder (`/home/admin/db/binlogdir/`) using the supplied basename (`binlog`).
	The option is only for the `copy-back-and-apply-log` and `copy-back` operations. Using it with any other operations makes the command fail.
- `relay-log` \[= *`basename`*\]
	Specify the location for the relay log to be restored on a replica server. By default, during a restore for a replica server, the relay log is restored to the same location it was found on the backed-up replica server. Use this option to specify a different target location for the relay log. The option works similarly as the [`--relay-log`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/replication-options-replica.html#sysvar_relay_log) option of the MySQL server in determining the location and the name of the relay log files—see [description of the server --relay-log option](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/replication-options-replica.html#sysvar_relay_log) for details. As a summary:
	- Using this option without supplying a ``*`basename`*`` puts the relay log in the target server's data directory with the default basename ``*`host_name`*-relay-bin``.
	- Using this option while supplying a ``*`basename`*`` puts the relay log in the target server's data directory with the specified basename.
	- Using this option while supplying a ``*`basename`*`` containing a full file path (for example, `/home/admin/db/relaylogdir/relaylog`) puts the relay log on the target server in the specified folder (`/home/admin/db/relaylogdir/`) using the supplied basename (`relaylog`).
	The option is only for the `copy-back-and-apply-log` and `copy-back` operations. Using it with any other operations makes the command fail.
- `log-bin-index` \[= *`PATH`*\]
	Specify the absolute path (including file name and extension) for restoring the index file that lists all the binary log files, if it is different from the default path given below.
	Default: ``*`data_dir`*/*`host_name`*-bin.index``.
- `relay-log-index` \[= *`PATH`*\]
	Specify the absolute path (including file name and extension) for restoring the index file that lists all the relay log files, if it is different from the default path given below.
	Default: ``*`data_dir`*/*`host_name`*-relay-bin.index``.
- `innodb_data_home_dir` = *`PATH`*
	Specifies the directory where InnoDB data files reside. Usually the same as [`datadir`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/server-system-variables.html#sysvar_datadir), but can be different. This parameter, together with [`innodb_data_file_path`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/innodb-parameters.html#sysvar_innodb_data_file_path) = *`SIZE`*, determines where the InnoDB data files such as `ibdata1`, `ibdata2`, and so on, are situated within the MySQL server.
	For backups:You do not need to specify this option, because its value is retrieved automatically using the database server connection.
	For restores: The directory where InnoDB data files are to be restored. Specify the option only if the InnoDB data files are to be restored outside of the server's data directory. *For release 8.0.16 and later*: the specified directory must be non-existent or empty, or the restore operation will fail.
	- If `innodb_data_home_dir` is not specified, it inherits the value of `datadir`.
	- If `innodb_data_home_dir` is a relative path, the path is located relative to (that is, underneath) the `datadir` value.
	- An `innodb_data_home_dir` of `""` refers to the `/` root directory.
	- If `innodb_data_home_dir` is an absolute path, its value is used as-is.
- `innodb_log_group_home_dir` = *`PATH`*
	Specifies where the InnoDB redo log reside within the server repository. Usually the same as `datadir`, but can be different.
	For backups: You do not need to specify this option, because its value is retrieved automatically using the database server connection.
	For restores: The directory where InnoDB redo log files are to be restored. Specify the option only if the InnoDB redo log files are to be restored outside of the server's data directory. *For release 8.0.16 and later:* the specified directory must be non-existent or empty, or the restore operation will fail.
	- If `innodb_log_group_home_dir` is not specified, it inherits the value of `datadir`.
	- If `innodb_log_group_home_dir` is a relative path, the path is taken to be relative to (that is, underneath) the `datadir` value.
	- If `innodb_log_group_home_dir` is an absolute path, its value is used as-is.
- `innodb_undo_directory` = *`PATH`*
	Specifies where the InnoDB undo log reside within the server repository. Usually the same as [`datadir`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/server-system-variables.html#sysvar_datadir), but can be different.
	For backups: You do not need to specify this option, because its value is retrieved automatically using the database server connection.
	For restores:
	- *For release 8.0.16 and later:* The directory where the default InnoDB undo tablespaces, as well as any non-default undo tablespaces resided in the backed-up server's data directory, are to be restored. (External undo tablespaces are restored by default to the locations they were found on the backed-up server; see the description for [undo log files](meb-files-backed-up-summary.md) for details.) *The specified directory must be non-existent or empty, or the restore operation will fail.*
	- *For release 8.0.15 and earlier:* The directory where the InnoDB undo log files are to be restored. Specify the option only if the undo log files are to be restored outside of the server's data directory.
	Its value is derived as follows:
	- If `innodb_undo_directory` is not specified, it inherits the value of `datadir`.
	- If `innodb_undo_directory` is a relative path, the path is taken to be relative to (that is, underneath) the `datadir` value.
	- If `innodb_undo_directory` is an absolute path, its value is used as-is.
	Warning
	When using this option, make sure the undo log location does not change between successive restores of a full and an incremental backups, or of two incremental backups. Otherwise, the restore is going to fail.