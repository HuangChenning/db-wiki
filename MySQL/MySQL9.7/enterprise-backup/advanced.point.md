---
title: "5.3 Point-in-Time Recovery"
book: "MySQL Enterprise Backup User's Guide (Version 9.7.0)"
version: "9.7"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/9.7/en/advanced.point.html"
tags:
  - mysql
  - mysql-9.7
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 9.7.0)

You can restore your database server to its state at an arbitrary time using the [binary log](meb-files-backed-up-summary.md) files included in the backups. The process assumes that following conditions are met:

- The backed-up MySQL Server has had its binary logging enabled (which is true by default). To check if this condition has been satisfied, perform this query on the server:
	```
	mysql> SHOW VARIABLES LIKE 'log_bin'; 
	+---------------+-------+
	| Variable_name | Value |
	+---------------+-------+
	| log_bin       | ON    |
	+---------------+-------+
	1 row in set (0.00 sec)
	```
	If the value of [`log_bin`](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/replication-options-binary-log.html#sysvar_log_bin) is `OFF`, binary logging has not been enabled. See [The Binary Log](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/binary-log.html) on how to enable binary logging for the server.
- A series of backups, consisting typically of a full backup followed by a series of incremental backups, has been created for the server. The last backup in the series covers the targeted point in time for recovery. The example below illustrates such a typical case.
- The last backup in the backup series you have taken include in itself the relevant binary log files. (To ensure this requirement is satisfied, do not use any of the following MySQL Enterprise Backup options when creating the backup: [`--skip-binlog`](backup-capacity-options.md), [`--use-tts`](backup-partial-options.md), [`--no-locking`](backup-capacity-options.md), or [`--start-lsn`](backup-incremental-options.md).)

These are the steps for a point-in-time recovery:

1. Restore the series of backups to the server, except for the last incremental backup in the series (which covers the targeted point in time for recovery). When finished, note the binary log position to which you have restored the server. The information is available from the `backup_variables.txt` file in the restored data directory of the server: look for the value of the entry `binlog_position` in the file. For example:
	```
	binlog_position=binlog.000012:426
	```
	This means after the restore of the backup series, the server is now at log position 426 found in the binary log file `binlog.000012`. You will need the information later.
	Note
	While the last binary log position recovered is also displayed by InnoDB after the restore, that is not a reliable means for obtaining the ending log position of your restore, as there could be DDL events and non-InnoDB changes that have taken place after the time reflected by the displayed position.
2. Extract the binary log from the last incremental backup in the backup series (that is, the backup that covers the targeted point in time for recovery). You do this by unpacking the incremental backup image into a backup directory using the [`image-to-backup-dir`](backup-commands-single-file.md) command; for example:
	```
	mysqlbackup --backup-dir=incr-backup-dir2 --backup-image=incremental_image2.bi image-to-backup-dir
	```
	Next, go into the resulting backup directory (`incr-backup-dir2` in this example) and, under the data directory inside, find the binary log file\[s\] (`binlog.000012` in this example):
	```
	incr-backup-dir2$ ls datadir
	binlog.000012       ibbackup_logfile  mysql               pets      undo_002
	...
	```
3. Roll forward the database server to its state at the targeted point in time for recovery, identified as `tR` in this example, using the [binary log](meb-files-backed-up-summary.md) file extracted in the last step. Then, using the [**mysqlbinlog**](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/mysqlbinlog.html) utility, replay to the server the SQL activities recorded in the [binary log](meb-files-backed-up-summary.md) file\[s\], from the log position the server has been restored to in Step 1 above (which is 426 in our example) all the way to time `tR`. Specify the range of binary log events to replay using the `--start-position` option and the `--stop-position` option (which indicates the corresponding binary log position for `tR`), and pipe the output to the **mysql** client:
	```
	mysqlbinlog --start-position="binary-log-position-at-the-end-of-backup-restores" \
	         --stop-position="binary-log-position-corresponding-to-tR" \
	         binary-log-filename  |   mysql -uadmin -p
	```
	Notes
	- Using the `--start-datetime` or `--stop-datetime` option to specify the range of binary log segment to replay is not recommended: there is a higher risk of missing binary log events when using the option. Use `--start-position` and `--stop-position` instead.
	- If you have more than one binary log files in your incremental backup and they are all needed for bringing the server up to its state at `tR`, you need to pipe all of them to the server in a single connection; for example:
		```
		mysqlbinlog --start-position="426" --stop-position="binary-log-position-corresponding-to-tR" \
		  binlog.000012 binlog.000013 binlog.000014 |   mysql -u admin -p
		```
	You can also dump all the **mysqlbinlog** output to a single file first, and then pipe or play the file to the **mysql** client.
	For more explanations on using the binary log for point-in-time recovery, see [Point-in-Time (Incremental) Recovery](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/point-in-time-recovery.html).
4. Check that the server has been restored to the desired point in time.