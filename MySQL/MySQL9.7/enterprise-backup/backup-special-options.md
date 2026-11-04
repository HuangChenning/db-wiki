---
title: "20.16 Options for Special Backup Types"
book: "MySQL Enterprise Backup User's Guide (Version 9.7.0)"
version: "9.7"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/9.7/en/backup-special-options.html"
tags:
  - mysql
  - mysql-9.7
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 9.7.0)

These options are for backing up database servers that play specific roles in replication, or contain certain kinds of data that require special care in backing up.

- `--replica-info`
	When backing up a replica server, this option captures information needed to set up an identical replica server. It creates a file `meta/ibbackup_replica_info` inside the backup directory, containing a [`CHANGE             REPLICATION SOURCE TO`](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/change-replication-source-to.html) statement with the binary log position and name of the binary log file of the source server. This information is also printed in the **mysqlbackup** output. To set up a new replica for this source, restore the backup data on another server, start a replica server on the backup data, and issue a [`CHANGE REPLICATION SOURCE             TO`](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/change-replication-source-to.html) command with the binary log position saved in the `ibbackup_replica_info` file. See [Section 8.1, “Setting Up a New replica”](advanced.replica.md) for instructions.
	Notes
	- Only use this option when backing up a replica server. Its behavior is undefined when used on a source or non-replication server.
	- This option is not compatible with the [`--no-locking`](backup-capacity-options.md) option; using both options together will make **mysqlbackup** throw an error.
	- This option is not compatible with the [`--only-innodb`](backup-partial-options.md) option.
	- For [TTS](glossary.md) backups for replica servers, use the `--replica-info` option to have the file `backup_gtid_executed.sql` generated and included in the backups.
	The option is an alias of `--slave-info`, which has been decprecated.
- `--slave-info`
	(Deprecated; use `--replica-info` instead) When backing up a replica server, this option captures information needed to set up an identical replica server. It creates a file `meta/ibbackup_slave_info` inside the backup directory, containing a `CHANGE             MASTER` statement with the binary log position and name of the binary log file of the source server. This information is also printed in the **mysqlbackup** output. To set up a new replica for this source, restore the backup data on another server, start a replica server on the backup data, and issue a `CHANGE MASTER` command with the binary log position saved in the `ibbackup_slave_info` file. See [Section 8.1, “Setting Up a New replica”](advanced.replica.md) for instructions.
	Notes
	- Only use this option when backing up a replica server. Its behavior is undefined when used on a source or non-replication server.
	- This option is not compatible with the [`--no-locking`](backup-capacity-options.md) option; using both options together will make **mysqlbackup** throw an error.
	- This option is not compatible with the [`--only-innodb`](backup-partial-options.md) option.
	- For [TTS](glossary.md) backups for replica servers, use the `--slave-info` option to have the file `backup_gtid_executed.sql` generated and included in the backups.
- `--safe-replica-backup-timeout` ``=*`SECONDS`*``
	For a replication setup, the option specifies the time (in seconds) **mysqlbackup** will wait for [`Replica_open_temp_tables`](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/server-status-variables.html#statvar_Replica_open_temp_tables) to become “0” (which happens when no temporary tables are open) to complete the backup for a replica server by asserting a read lock and copies all the non-InnoDB tables. If the duration of the wait exceeds that specified with the option, **mysqlbackup** times out and throws an error. The wait is for preventing **mysqlbackup** from finishing a replica backup when there are temporary tables still open. See descriptions in [Temporary tables on a replica](advanced.replica-backup-restore.md) for details on how **mysqlbackup** deals with temporary tables on a replica server.
	In addition, **mysqlbackup** also runs an initial check at the beginning of a replica backup to see if [`Replica_open_temp_tables=0`](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/server-status-variables.html#statvar_Replica_open_temp_tables) becomes true within the duration set by `--safe-replica-backup-timeout`. If it does not, **mysqlbackup** takes it as an early sign that before the backup is completed, some temporary tables are likely to remain open after the timeout limit is exceeded; **mysqlbackup** then throws an error, instead of continuing with the backup. When that happens, you can either restart the backup with a higher value for `--safe-replica-backup-timeout`, or retry at a time when fewer temporary tables are being used.
	Default: 300
	Warning
	Proper setting of this value depends on the use case, and it can vary a lot according to the situation. Setting the value for this option either too high or too low will affect adversely the performance of the backup operation:
	- *Too high:* If you need to wait for a long time for there to be no more temporary tables, the chance is that the change rate for your database server is quite high, which means the amount of redo log data to be included in the backup will be large and the restore time for the backup will be long. In such a case, it would have been better to have let **mysqlbackup** timeout and then restart the backup operation, so the tables are copied in their final states. It is therefore not helpful to set a high timeout value for the option. As a very general rule of thumb: even for busy databases that use many temporary tables, do not set the value to more than a few hours.
	- *Too low:* Setting the wait time value too low would make the backup process time out very easily and when that happens, the process has to be restarted. With a repeating cycle of restarts, the backup might then take a long time to complete, and resources used on the failed backups will be wasted. As a very general rule of thumb, do not set the timeout to below the default value of 300s.
	Even though the issue described above with temporary tables does not exist for a row-based replication (RBR) setup (for which temporary tables are not replicated onto the replica), any replica backups still wait for temporary tables to be all closed as described above, because the mode of replication could potentially be switched from RBR to statement-based replication (SBR) or mixed-mode replication at any time. Users who are certain that SBR is not occurring for the replica can set `--safe-replica-backup-timeout=0`, with which **mysqlbackup** will not check for any open temporary tables before finishing the backup.
	The option is an alias of `--safe-slave-backup-timeout`, which has been decprecated.
- `--safe-slave-backup-timeout` ``=*`SECONDS`*``
	(Deprecated; use `--safe-replica-backup-timeout` instead) For a replication setup, the option specifies the time (in seconds) **mysqlbackup** will wait for [`Slave_open_temp_tables`](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/server-status-variables.html#statvar_Slave_open_temp_tables) to become “0” (which is true when no temporary tables are open) to complete the backup for a replica server by asserting a read lock and copies all the non-InnoDB tables. If the duration of the wait exceeds that specified with the option, **mysqlbackup** times out and throws an error. The wait is for preventing **mysqlbackup** from finishing a replica backup when there are temporary tables still open. See descriptions in [Temporary tables on a replica](advanced.replica-backup-restore.md) for details on how **mysqlbackup** deals with temporary tables on a replica server.
	In addition, **mysqlbackup** also runs an initial check at the beginning of a replica backup to see if [`Slave_open_temp_tables=0`](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/server-status-variables.html#statvar_Slave_open_temp_tables) becomes true within the duration set by `--safe-slave-backup-timeout`. If it does not, **mysqlbackup** takes it as an early sign that before the backup is completed, some temporary tables are likely to remain open after the timeout limit is exceeded; **mysqlbackup** then throws an error, instead of continuing with the backup. When that happens, you can either restart the backup with a higher value for `--safe-slave-backup-timeout`, or retry at a time when fewer temporary tables are being used.
	Default: 300
	Warning
	Proper setting of this value depends on the use case, and it can vary a lot according to the situation. Setting the value for this option either too high or too low will affect adversely the performance of the backup operation:
	- *Too high:* If you need to wait for a long time for there to be no more temporary tables, the chance is that the change rate for your database server is quite high, which means the amount of redo log data to be included in the backup will be large and the restore time for the backup will be long. In such a case, it would have been better to have let **mysqlbackup** timeout and then restart the backup operation, so the tables are copied in their final states. It is therefore not helpful to set a high timeout value for the option. As a very general rule of thumb: even for busy databases that use many temporary tables, do not set the value to more than a few hours.
	- *Too low:* Setting the wait time value too low would make the backup process time out very easily and when that happens, the process has to be restarted. With a repeating cycle of restarts, the backup might then take a long time to complete, and resources used on the failed backups will be wasted. As a very general rule of thumb, do not set the timeout to below the default value of 300s.
	Even though the issue described above with temporary tables does not exist for a row-based replication (RBR) setup (for which temporary tables are not replicated onto the replica), any replica backups still wait for temporary tables to be all closed as described above, because the mode of replication could potentially be switched from RBR to statement-based replication (SBR) or mixed-mode replication at any time. Users who are certain that SBR is not occurring for the replica can set `--safe-slave-backup-timeout=0`, with which **mysqlbackup** will not check for any open temporary tables before finishing the backup.
- `--suspend-at-end`
	This option pauses the **mysqlbackup** command when the backup procedure is close to ending. It creates a file called `ibbackup_suspended` in the backup log group home directory and waits until you delete that file before proceeding. This option is useful to customize locking behavior and backup of non-InnoDB files through custom scripting.
	All non-InnoDB tables are locked before suspending, putting them into a read-only state, unless you turn off locking with the [`--no-locking`](backup-capacity-options.md). The [`--only-innodb`](backup-partial-options.md) option also prevents the locking step. You can also use a combination of `--only-innodb` and `--suspend-at-end` to back up only certain InnoDB tables.
- `--exec-when-locked` =" *`utility`* *`arg1`* *`arg2`*..."
	| Command-Line Format | `--exec-when-locked="utility arg1 arg2 ..."` |
	| --- | --- |
	| Type | String |
	The specified *`utility`* is executed when all non-InnoDB tables are locked near the end of a backup operation.
	You can use this option to run a script that backs up any information that is not included as part of the usual backup. For example, with `--exec-when-locked`, you can use **mysqldump** to back up tables from the MEMORY storage engine, which are not on disk.
	Set any variable you want to use within your script before you run **mysqlbackup**. In the following example, the `BACKUP_DIR` environment variable is set to point to the current backup directory (quotes are used for the argument of `--exec-when-locked`, to prevent premature expansion of the variable `BACKUP_DIR`):
	On Unix or Linux systems:
	```
	export BACKUP_DIR=path_to_backupdir
	mysqlbackup --exec-when-locked="mysqldump mydb t1 > $BACKUP_DIR/t1.sql" other_options mysqlbackup_command
	```
	Or on Windows systems:
	```
	set BACKUP_DIR=path_to_backupdir
	mysqlbackup --exec-when-locked="mysqldump mydb t1 > %BACKUP_DIR%/t1.sql" other_options mysqlbackup_command
	```
	If the utility cannot be executed or returns a non-zero exit status, the whole backup process is cancelled. If you also use the `--suspend-at-end` option, the utility specified by `--exec-when-locked` is executed after the suspension is lifted.