---
title: "20.11 Message Logging Options"
book: "MySQL Enterprise Backup User's Guide (Version 9.7.0)"
version: "9.7"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/9.7/en/backup-message-logging-options.html"
tags:
  - mysql
  - mysql-9.7
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 9.7.0)

**mysqlbackup** writes important progress and error information to the `stderr` stream. The information is often very valuable for tracking down problems that occur during an operation. Starting from MySQL Enterprise Backup 3.9, the output to the `stderr` stream is also saved to a log file by default (for most **mysqlbackup** operations), so that the error information can be easily accessed in any debug process.

The message logging works like a **tee** process on a Unix-like system, in which the output of a program is split to be both displayed and saved to a file. The log file thus produced is named in the following format: ``MEB_*`timestamp`*_*`operation`*.log``, where *`operation`* is the **mysqlbackup** operation that was run (e.g., [`backup`](backup-commands-backup.md), [`apply-log`](backup-commands-update.md), etc.), and *`timestamp`* is the date and time at which the operation was run. Here are some examples of names for the log files:

```
MEB_2013-06-24.16-32-43_backup.log
MEB_2013-06-28.11-07-18_apply_log.log
MEB_2013-06-29.10-08-06_list_image.log
```

The following options control the message logging function:

- `--skip-messages-logdir`
	Skip message logging. Logging is turned on by default (except for the [`list-image`](backup-commands-single-file.md) and [`validate`](backup-commands-validate.md) operations; see the description for the `--messages-logdir` option for details), and it is turned off by this option.
- ``             --messages-logdir=*`path`*``
	| Command-Line Format | `--messages-logdir=PATH` |
	| --- | --- |
	| Type | Directory name |
	| Default Value | `backup_dir/meta` |
	Specifies the path name of an existing directory for storing the message log. If the specified directory does not exist, message logging fails and returns an error message. When this option is omitted, the default directory of ``*`backup_dir`*/meta`` is used, where *`backup_dir`* is the directory specified with the [`--backup-dir`](backup-repository-options.md) option.
	Note
	Use this option to turn on message logging for the [`list-image`](backup-commands-single-file.md) and [`validate`](backup-commands-validate.md) operations. Message logging is turned off by default for the two operations, because they do not modify any files and a message log is usually not required for debugging them. And because the default path name of `backup_dir/meta` is not meaningful for the two operations, this option is required for both turning on message logging and for supplying the path name of a directory in which to save the log file. However, if the `--skip-messages-logdir` option is also specified, it takes precedence and message logging is skipped.

The following are some examples showing how the message logging is controlled.

This creates a log file for the [`backup`](backup-commands-backup.md) operation in the directory `/home/backup_dir/meta` due to the default settings:

```
mysqlbackup -uroot --port=3306 --backup-dir=/home/backup_dir backup
```

This skips message logging for the [`backup`](backup-commands-backup.md) operation:

```
mysqlbackup -uroot --port=3306 --backup-dir=/home/backup_dir \
      --skip-messages-logdir backup
```

This creates a log file for the [`apply-log`](backup-commands-update.md) operation in an existing directory named `/home/teelog_dir`, rather than the default location:

```
mysqlbackup -uroot --port=3306 --backup-dir=/home/backup_dir \
      --messages-logdir=/home/teelog_dir apply-log
```

This creates a log file for the [`list-image`](backup-commands-single-file.md) operation in an existing directory named `/home/teelog_dir`:

```
mysqlbackup -uroot --port=3306 --backup-image=/backup/my.mbi \
      --messages-logdir=/home/teelog_dir list-image
```