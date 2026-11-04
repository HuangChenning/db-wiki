---
title: "20.5 Metadata Options"
book: "MySQL Enterprise Backup User's Guide (Version 8.0.46)"
version: "8.0"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/8.0/en/backup-metadata-options.html"
tags:
  - mysql
  - mysql-8.0
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 8.0.46)

These options control the generation of metadata about backups. Some metadata is stored in the backup directory, other metadata is stored in tables within the `mysql` database of the backed-up instance.

- `--no-history-logging`
	Turns off the recording of backup progress and history in logging tables inside the backed-up database server. See [Section 17.3, “Using the MySQL Enterprise Backup Logs”](trouble.logging.md) for details about these tables.
	Default: history logging is enabled.
- `--comments` = *`STRING`*
	| Command-Line Format | `--comments=STRING` |
	| --- | --- |
	| Type | String |
	Specifies a comment string that describes or identifies the backup. Surround multi-word comments with appropriate quotation marks. The string is saved in a file `meta/comments.txt` in the backup. For example: `--comments="Backup of HR data on             2010/12/10"`.
- `--comments-file` = *`PATH`*
	| Command-Line Format | `--comments-file=PATH` |
	| --- | --- |
	| Type | File name |
	Specifies path to a file containing comments describing the backup. This file is saved as `meta/comments.txt` in the backup. For example: `--comments-file=/path/to/comments.txt`.
	This option overrides the `--comments` option if both are specified.