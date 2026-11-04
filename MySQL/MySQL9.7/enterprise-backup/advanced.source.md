---
title: "8.3 Restoring a Source Database"
book: "MySQL Enterprise Backup User's Guide (Version 9.7.0)"
version: "9.7"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/9.7/en/advanced.source.html"
tags:
  - mysql
  - mysql-9.7
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 9.7.0)

To fix a corruption problem in a replication source database, you can restore the backup, taking care not to propagate unnecessary SQL operations to the replica servers:

1. Shut down the source database and then use, for example, the [`copy-back-and-apply-log`](backup-commands-restore.md) command, to restore a backup of it and prepare the data.
2. Edit the source's `my.cnf` file and comment out `log-bin`, so that the replicas do not receive twice the binary log needed to recover the source.
3. Replication in the replicas must be stopped temporarily while you pipe the binary log to the source. In the replicas, do:
	```
	mysql> STOP REPLICA;
	```
4. Start the source **mysqld** on the restored backup:
	```
	$ mysqld
	…
	InnoDB: Doing recovery: scanned up to log sequence number 0 64300044
	InnoDB: Last MySQL binlog file position 0 5585832, file name
	./omnibook-bin.000002
	…
	```
	InnoDB prints the binary log file (`./omnibook-bin.000002` in this case) and the position (`5585832` in this case) it was able to recover to.
5. Pipe the remaining of the binary log files to the restored server. The number of remaining binary log files varies depending on the length of the timespan between the last backup and the time to which you want to bring the database up to date. The longer the timespan, the more remaining binary log files there may be. All the binary log files, containing all the continuous binary log positions in that timespan, are required for a successful restore.
	You also need to supply the starting position in the binary log by which the piping of the events should start. Deduce that information from the `meta/backup_variables.txt` file in the backup you just restored in step 1 above (access `backup_variables.txt` by, for example, going to the temporary backup directory you specified with [`--backup-dir`](backup-repository-options.md) during the restore, and find the file under the `meta` folder): look for the entry ``binlog_position=**`value`**`` in `meta/backup_variables.txt`, and supply **`value`** to **mysqlbinlog** with the [`--start-position`](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/mysqlbinlog.html#option_mysqlbinlog_start-position) option.
	Note
	While the last binary log position recovered is also displayed by InnoDB after the restore (see step 4 above), that is not a reliable number for deducing the start position for **mysqlbinlog** to use, as there could be DDL events and non-InnoDB changes that have taken place after the time reflected by the displayed position.
	For example, if there are two more binary log files, `omnibook-bin.000003` and `omnibook-bin.000004` that come after `omnibook-bin.000002` and the recovery in step 4 above has ended by `5585834` *according to the `backup_variables.txt` file*, pipe the binary log with a single connection to the server with this command:
	```
	$ mysqlbinlog --start-position=5585834 /mysqldatadir/omnibook-bin.000002 \
	  /mysqldatadir/omnibook-bin.000003 /mysqldatadir/omnibook-bin.000004 | mysql
	```
	See [Point-in-Time (Incremental) Recovery](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/point-in-time-recovery.html) for more instructions on using **mysqlbinlog**.
6. The source database is now recovered. Shut down the source and edit `my.cnf` to uncomment `log-bin`.
7. Start the source again.
8. Start replication in the replicas again:
	```
	mysql> START REPLICA;
	```