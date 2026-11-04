---
title: "8.1 Setting Up a New replica"
book: "MySQL Enterprise Backup User's Guide (Version 9.7.0)"
version: "9.7"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/9.7/en/advanced.replica.html"
tags:
  - mysql
  - mysql-9.7
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 9.7.0)

MySQL Enterprise Backup allows you to set up a replica server (referred to as the “replica” below) by backing up the source server (referred to as the “source” below) and restoring the backup on a new replica, without having to stop the source.

*For servers NOT using GTID*:

1. Take a full backup of the source and then use, for example, the [`copy-back-and-apply-log`](backup-commands-restore.md) command, to restore the backup and the log files to the right directories on the new replica and prepare the data.
	Note
	Do not use the [`--no-locking`](backup-capacity-options.md) option when backing up the server, or you will be unable to get a proper binary log position in Step 4 below for initializing the replica.
2. Edit the `my.cnf` file of the new replica and put [`skip-replica-start`](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/replication-options-replica.html#option_mysqld_skip-replica-start) and `event_scheduler=off` (if the source uses the [Event Scheduler](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/event-scheduler.html)) under the `[mysqld]` section.
3. Start the new replica **mysqld**. You see the following in the server's output:
	```
	…
	InnoDB: Last MySQL binlog file position 0 128760007, file name ./hundin-bin.000006
	…
	```
	While a `Last MySQL binlog file position` has been displayed, it is NOT necessarily the latest binary log position on the backed up server, as InnoDB does not store binary log position information for any DDL operations or any changes to non-InnoDB tables. *Do not use this binary log position to initialize the replica*. The next step explains how to find the correct binary log position to use.
4. Look for the file ``*`datadir`*/meta/backup_variables.txt`` where ``*`datadir`*`` is the data directory of the new replica. Look into the file to retrieve the latest binary log position and the corresponding log file number stored inside:
	```
	binlog_position=hundin-bin.000006:128760128
	```
5. Use the `CHANGE REPLICATION SOURCE TO` SQL statement and the information you have retrieved in the last step to initialize the replica properly:
	```
	CHANGE REPLICATION SOURCE TO
	SOURCE_LOG_FILE='hundin-bin.000006',
	SOURCE_LOG_POS=128760128;
	```
6. Set the status of any events that were copied from the source to `DISABLE ON REPLICA`. For example:
	```
	mysql> ALTER EVENT mysql.event DISABLE ON REPLICA;
	```
7. Remove the line `skip-replica-start` and `event_scheduler=off` entries you added to the `my.cnf` file of the replica in step 2. (You can also leave the `skip-replica-start` entry in, but then you will always need to use the [`START REPLICA`](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/start-replica.html) statement to start replication whenever you restart the replica server.)
8. Restart the replica server. Replication starts.

*For servers using GTIDs (see [Setting Up Replication Using GTIDs](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/replication-gtids-howto.html) on how to enable servers to use GTIDs)*:

1. Take a full backup of the source and then use, for example, the [`copy-back-and-apply-log`](backup-commands-restore.md) command, to restore the backup and the log files to the right directories on a new GTID-enabled replica and prepare the data.
2. Edit the `my.cnf` file of the new replica and put `skip-replica-start` and `event_scheduler=off` (if the source uses the [Event Scheduler](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/event-scheduler.html)) under the `[mysqld]` section.
3. Start the new replica server.
4. Connect to the replica server with the **mysql** client. Then, execute the following statement to reset the binary log:
	```
	mysql> RESET MASTER;
	```
	And execute the following statement to stop the binary logging:
	```
	mysql> SET sql_log_bin=0;
	```
5. When a server using the GTID feature is backed up, **mysqlbackup** produces a file named `backup_gtid_executed.sql`, which can be found in the restored data directory of the new replica server. The file contains a SQL statement that sets the `GTID_PURGED` configuration option on the replica:
	```
	# On a new replica, issue the following command if GTIDs are enabled:
	SET @@GLOBAL.GTID_PURGED='f65db8e2-0e1a-11e5-a980-080027755380:1-3';
	```
	It also contains a commented-out [`CHANGE           REPLICATION SOURCE TO`](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/change-replication-source-to.html) statement for initializing the replica:
	```
	# Use the following command if you want to use the GTID handshake protocol:
	# CHANGE REPLICATION SOURCE TO SOURCE_AUTO_POSITION = 1;
	```
	Uncomment the command and add any needed connection and authentication parameters to it (for example, `SOURCE_HOST`, `SOURCE_USER`, `SOURCE_PASSWORD`, and `SOURCE_PORT`):
	```
	# Use the following command if you want to use the GTID handshake protocol:
	CHANGE REPLICATION SOURCE TO SOURCE_HOST='127.0.0.1', SOURCE_USER='muser', SOURCE_PASSWORD='mpass', SOURCE_PORT=18675, SOURCE_AUTO_POSITION = 1;
	```
	Execute the file with the **mysql** client
	```
	mysql> source /path-to-backup_gtid_executed.sql/backup_gtid_executed.sql
	```
6. Set the status of any events that were copied from the source to `DISABLE ON REPLICA`. For example:
	```
	mysql> ALTER EVENT mysql.event DISABLE ON REPLICA;
	```
7. Remove the `skip-replica-start` and `event_scheduler=off` entries you added to the `my.cnf` file of the replica in step 2. (You can also leave the `skip-replica-start` entry in, but then you will always need to use the [`START REPLICA`](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/start-replica.html) statement to start replication whenever you restart the replica server.)
8. Restart the replica server. Replication starts.

For more information on the GTIDs, see [GTID feature](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/replication-gtids.html).