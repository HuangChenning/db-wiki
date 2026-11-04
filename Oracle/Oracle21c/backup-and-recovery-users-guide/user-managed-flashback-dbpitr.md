---
title: "Backup and Recovery User's Guide"
book: "Database Backup and Recovery User's Guide"
doc_id: F31836-11
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/bradv/user-managed-flashback-dbpitr.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-users-guide
---

A user-managed backup and recovery strategy means a method that does not depend on RMAN. Use the flashback features of Oracle Database in a user-managed backup and recovery strategy.

### 30.1 Performing Flashback Database with SQL\*Plus

You can use SQL\*Plus to perform flashback database operations on multitenant container databases (CDBs) and pluggable databases (PDBs). Oracle Flashback Database returns your entire database or an entire PDB to a previous state without requiring you to restore files from backup.

Flashback Database requires you to create a fast recovery area for your database and enable the collection of flashback logs. The requirements and preparations for flashback database are the same whether you use RMAN or SQL\*Plus.

See Also:

- [Performing Flashback and Database Point-in-Time Recovery](rman-performing-flashback-dbpitr.md) for details about how the Flashback Database feature works, requirements for using Flashback Database, and how to enable the collection of flashback logs required for Flashback Database

#### 30.1.1 Performing Flashback Database of CDBs with SQL\*Plus

Use the SQL\*Plus `FLASHBACK DATABASE` command to return a whole multitenant container database (CDB) to a prior state. This command performs the same function as the RMAN `FLASHBACK DATABASE` command.

Prerequisites:

The prerequisites for performing a flashback database operation are described in " [Prerequisites for Flashback Database and Restore Points](using-flasback-database-restore-points.md) ".

To perform a flashback of the whole CDB using SQL\*Plus:

1. Connect SQL\*Plus to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege.
2. Query the target database to determine the range of possible flashback SCNs. The following SQL\*Plus queries show you the latest and earliest SCN in the flashback window:
	```
	SELECT CURRENT_SCN FROM V$DATABASE;
	SELECT OLDEST_FLASHBACK_SCN, OLDEST_FLASHBACK_TIME 
	FROM   V$FLASHBACK_DATABASE_LOG;
	```
3. Use other flashback features if necessary to identify the SCN or time of the unwanted changes to your database.
4. Ensure that the target database is mounted.
	The following commands start the database in `MOUNT` mode.
	```
	SHUTDOWN IMMEDIATE;
	STARTUP MOUNT;
	```
5. Run the `FLASHBACK DATABASE` command to return the CDB to a prior timestamp, SCN, or restore point.
	The following are some examples of flashback operations on CDBs:
	```
	FLASHBACK DATABASE TO RESTORE POINT cdb_grp;
	FLASHBACK DATABASE TO SCN 34468;
	FLASHBACK DATABASE TO TIMESTAMP '2013-11-05 14:00:00';
	FLASHBACK DATABASE 
	  TO TIMESTAMP to_timestamp('2013-11-11 16:00:00', 'YYYY-MM-DD HH24:MI:SS');
	```
6. When the operation completes, open the database read-only and perform queries to verify that you have recovered the data you need.
	If your chosen target time was not far enough in the past, then use another `FLASHBACK DATABASE` statement. Otherwise, you can use `RECOVER DATABASE` to return the database to the present time and then try another `FLASHBACK DATABASE` statement.
7. When satisfied with the results, open the database with the `RESETLOGS` option.
	If appropriate, you can also use Data Pump Export to save lost data, use `RECOVER DATABASE` to return the database to the present, and reimport the lost object.
8. Since the pluggable databases (PDBs) are not automatically opened when the CDB is opened, open the PDBs.
	The following command, when connected to the root, opens all the PDBs:
	```
	ALTER PLUGGABLE DATABASE ALL OPEN;
	```
	If you want to open only some PDBs, then you can open each PDB separately. The following command, when connected to the root, opens the PDB `my_pdb`.
	```
	ALTER PLUGGABLE DATABASE my_pdb OPEN;
	```

See Also:

[Performing Flashback and Database Point-in-Time Recovery](rman-performing-flashback-dbpitr.md) for details about how the Flashback Database feature works, requirements for using Flashback Database, and how to enable the collection of flashback logs required for Flashback Database

#### 30.1.2 Performing Flashback Database of PDBs with SQL\*Plus

Use the SQL\*Plus `FLASHBACK` `DATABASE` command to return a specific pluggable database (PDB) to a prior state. The remaining PDBs in the multitenant container database (CDB) are not impacted by the flashback operation on a single PDB.

The SQL\*Plus `FLASHBACK DATABASE` command performs the same function as the RMAN `FLASHBACK DATABASE` command.

The prerequistes for performing a flashback database operation are described in [Prerequisites for Flashback Database and Restore Points](using-flasback-database-restore-points.md).

To perform a flashback of a PDB using SQL\*Plus:

1. Connect SQL\*PLus to the root as a common user with the `SYSDBA` privilege.
2. Ensure that the CDB is open.
	The following command, when connected to the root, displays the mode in which the CDB is open.
	```
	SELECT open_mode from V$DATABASE;
	```
3. Determine the desired SCN, restore point, or point in time for the `FLASHBACK DATABASE` command.
	Query the `V$RESTORE_POINT` view to obtain the list of PDB restore points. `V$FLASHBACK_DATABASE_LOG` displays the oldest SCN to which a flashback operation can be performed.
4. Ensure that the PDB for which the Flashback Database operation must be performed is closed. Other PDBs can be open and operational.
	When connected to the root, the following `ALTER PLUGGABLE DATABASE` command closes the PDB `my_pdb`.
	```
	ALTER PLUGGABLE DATABASE my_pdb CLOSE;
	```
5. Perform a Flashback Database operation on the specified PDB to the desired point in time.
	The following are some examples of flashback database operations on PDBs.
	- For a PDB that uses local undo:
		```
		FLASHBACK PLUGGABLE DATABASE my_pdb TO SCN 24368;
		FLASHBACK PLUGGABLE DATABASE my_pdb TO RESTORE POINT guar_rp;
		```
	- For a PDB that uses shared undo, you can only use SQL\*Plus to perform a flashback operation if you are flashing back the PDB to a clean PDB restore point. For example:
		```
		FLASHBACK PLUGGABLE DATABASE my_pdb TO RESTORE POINT before_appl_changes;
		```
6. Open the PDB with `RESETLOGS`.
	The following command opens the PDB named `my_pdb` with `RESETLOGS`:
	```
	ALTER PLUGGABLE DATABASE my_pdb OPEN RESETLOGS;
	```

Note:

Flashback operations on a proxy PDB are not supported.

See Also:

[Performing Flashback and Database Point-in-Time Recovery](rman-performing-flashback-dbpitr.md) for details about how the Flashback Database feature works, requirements for using Flashback Database, and how to enable the collection of flashback logs required for Flashback Database

### 30.2 Overview of User-Managed Media Recovery

This section provides an overview of recovery with SQL\*Plus. This section contains the following topics:

#### 30.2.1 About User-Managed Restore and Recovery

Typically, you restore a file when a media failure or user error has damaged or deleted one or more data files. In a user-managed restore operation, you use an operating system utility to restore a backup of the file.

If a media failure affects data files, then the recovery procedure depends on:

- The archiving mode of the database: `ARCHIVELOG` or `NOARCHIVELOG`
- The type of media failure
- The files affected by the media failure (data files, control files, archived redo logs, and the server parameter file are all candidates for restore operations)

If either a permanent or temporary media failure affects any data files of a database operating in `NOARCHIVELOG` mode, then the database automatically shuts down. If the media failure is temporary, then correct the underlying problem and restart the database. Usually, crash recovery recovers all committed transactions from the online redo log. If the media failure is permanent, then recover the database as described in " Recovering a Database in NOARCHIVELOG Mode ".

Table 30-1 explains the implications for media recovery when you lose files in a database that runs in `ARCHIVELOG` mode.

Table 30-1 User-Managed Restore Operations

| If You Lose... | Then... |
| --- | --- |
| Data files in the `SYSTEM` tablespace or data files with active undo segments | The database automatically shuts down. If the hardware problem is temporary, then fix it and restart the database. Usually, crash recovery recovers lost transactions. If the hardware problem is permanent, then restore the data files from backups and recover the database as described in " Performing Closed Database Recovery ". |
| Data files not in the `SYSTEM` tablespace or data files that do not contain active rollback or undo segments | Affected data files are taken offline, but the database stays open. If the unaffected portions of the database must remain available, then do not shut down the database. Take tablespaces containing problem data files offline using the temporary option, then recover them as described in " Performing Open Database Recovery ". |
| All copies of the current control file | You must restore a backup control file and then open the database with the `RESETLOGS` option.  If you do not have a backup, then you can attempt to re-create the control file. If possible, use the script included in the `ALTER` `DATABASE` `BACKUP` `CONTROLFILE` `TO` `TRACE` output. Additional work may be required to match the control file structure with the current database structure. |
| One copy of a multiplexed control file | Copy an intact multiplexed control file into the location of the damaged or missing control file and open the database. If you cannot copy the control file to its original location, then edit the initialization parameter file to reflect a new location or remove the damaged control file. Then, open the database. |
| One or more archived logs required for media recovery | You must restore backups of these archived logs for recovery to proceed. You can restore either to the default or nondefault location. If you do not have backups, then you must perform incomplete recovery up to an SCN before the first missing redo log and open `RESETLOGS`. |
| The server parameter file (SPFILE) | If you have a backup of the server parameter file, then restore it. Alternatively, if you have a backup of the client-side initialization parameter file, then you can restore a backup of this file, start the instance, and then re-create the server parameter file. |

Note:

Restore and recovery of Oracle Managed Files is no different from restore and recovery of user-named files.

To perform media recovery, Oracle recommends that you use the `RECOVER` statement in SQL\*Plus. You can also use the SQL statement `ALTER` `DATABASE` `RECOVER`, but the `RECOVER` statement is often simpler. To start any type of media recovery, you must adhere to the following restrictions:

- You must have administrator privileges.
- All recovery sessions must be compatible.
- One session cannot start complete media recovery while another performs incomplete media recovery.
- You cannot start media recovery if you are connected to the database through a shared server process.

#### 30.2.2 Automatic Recovery with the RECOVER Command

When using SQL\*Plus to perform media recovery, the easiest strategy is to perform automatic recovery with the SQL\*Plus `RECOVER` command. Automatic recovery initiates recovery without manually prompting SQL\*Plus to apply each individual archived redo log.

When using SQL\*Plus, you have the following options for automating the application of the default file names of archived redo logs needed during recovery:

- Issuing `SET` `AUTORECOVERY` `ON` before issuing the `RECOVER` command. If you perform recovery with `SET` `AUTORECOVERY` `OFF`, which is the default, then you must enter file names manually or accept the suggested file name by pressing Enter.
- Specifying the `AUTOMATIC` keyword as an option of the `RECOVER` command.

In either case, no interaction is required when you issue the `RECOVER` command if the necessary files are in the correct locations with the correct names. When the database successfully applies a redo log file, the following message is returned:

```
Log applied.
```

You are then prompted for the next redo log in the sequence. If the most recently applied log is the last required log, then recovery is terminated.

The file names used for automatic recovery are derived from the concatenated values of `LOG_ARCHIVE_FORMAT` with `LOG_ARCHIVE_DEST_` `n`, where `n` is the highest value among all enabled, local destinations. For example, assume that the following initialization parameter settings are in effect in the database instance:

```
LOG_ARCHIVE_DEST_1 = "LOCATION=/arc_dest/loc1/" 
LOG_ARCHIVE_DEST_2 = "LOCATION=/arc_dest/loc2/"
LOG_ARCHIVE_DEST_STATE_1 = DEFER 
LOG_ARCHIVE_DEST_STATE_2 = ENABLE 
LOG_ARCHIVE_FORMAT = arch_%t_%s_%r.arc
```

In this example, SQL\*Plus automatically suggests the file name `/arc_dest/loc2/arch_%t_%s_%r.arc` (where `%t` is the thread, `%s` is the sequence and `%r` is the resetlogs ID).

See Also:

- Automatic Recovery with SET AUTORECOVERY
- Automatic Recovery with the AUTOMATIC Option of the RECOVER Command

##### 30.2.2.1 Automatic Recovery with SET AUTORECOVERY

After restoring data file backups, you can run the `SET` `AUTORECOVERY` `ON` command to enable automatic recovery. For example, you could enter the following commands in SQL\*Plus to perform automatic recovery and open the database:

```
STARTUP MOUNT
SET AUTORECOVERY ON
RECOVER DATABASE
ALTER DATABASE OPEN;
```

Note:

After issuing the SQL\*Plus `RECOVER` command, you can view all files that have been considered for recovery in the `V$RECOVERY_FILE_STATUS` view. You can access status information for each file in the `V$RECOVERY_STATUS` view. These views are not accessible after you terminate the recovery session.

##### 30.2.2.2 Automatic Recovery with the AUTOMATIC Option of the RECOVER Command

Besides using `SET` `AUTORECOVERY` to turn on automatic recovery, you can also simply specify the `AUTOMATIC` keyword in the `RECOVER` command. For example, you could enter the following commands in SQL\*Plus to perform automatic recovery and open the database:

```
STARTUP MOUNT
RECOVER AUTOMATIC DATABASE
ALTER DATABASE OPEN;
```

If you use an Oracle Real Application Clusters configuration, and if you are performing incomplete recovery or using a backup control file, then the database can only compute the name of the first archived redo log file from the first redo thread. You may have to manually apply the first log file from the other redo threads. After the first log file in a given thread has been supplied, the database can suggest the names of the subsequent logs in this thread.

#### 30.2.3 Recovery When Archived Logs Are in the Default Location

No additional setup is required to perform recovery when the archived redo log files are present in the default location.

During recovery, as a log is needed, the database suggests the file name. If you run nonautomatic media recovery with SQL\*Plus, then the output is displayed in the format shown by this example:

```
ORA-00279: change 53577 generated at 11/26/02 19:20:58 needed for thread 1
ORA-00289: suggestion : /oracle/oradata/trgt/arch/arcr_1_802.arc
ORA-00280: change 53577 for thread 1 is in sequence #802
Specify log: [<RET> for suggested | AUTO | FROM logsource | CANCEL ]
```

Similar messages are returned when you use an `ALTER` `DATABASE` `...` `RECOVER` statement. However, no prompt is displayed.

The database constructs suggested archived log file names by concatenating the current values of the initialization parameters `LOG_ARCHIVE_DEST_` `n` (where `n` is the highest value among all enabled, local destinations) and `LOG_ARCHIVE_FORMAT` and using log history data from the control file. The following are possible settings:

```
LOG_ARCHIVE_DEST_1 = 'LOCATION = /oracle/oradata/trgt/arch/'
LOG_ARCHIVE_FORMAT = arcr_%t_%s.arc

SELECT NAME FROM V$ARCHIVED_LOG;

NAME
----------------------------------------
/oracle/oradata/trgt/arch/arcr_1_467.arc
/oracle/oradata/trgt/arch/arcr_1_468.arc
/oracle/oradata/trgt/arch/arcr_1_469.arc
```

Thus, if all the required archived log files are present at the `LOG_ARCHIVE_DEST_1` destination, and if the value for `LOG_ARCHIVE_FORMAT` is never altered, then the database can suggest and apply log files to complete media recovery automatically.

#### 30.2.4 Recovery When Archived Logs Are in a Nondefault Location

To perform media recovery when archived redo log files are stored in a nondefault location, you must specify the location of archived redo log files.

You have the following mutually exclusive options when performing media recovery when archived logs are not in their default location:

- Edit the `LOG_ARCHIVE_DEST_` `n` parameter that specifies the location of the archived redo logs, then recover as usual.
	This task is described in Resetting the Archived Log Destination.
- Use the `SET` statement in SQL\*Plus to specify the nondefault log location before recovery, or the `LOGFILE ` parameter of the `RECOVER` command.
	This task is described in Overriding the Archived Log Destination.

##### 30.2.4.1 Resetting the Archived Log Destination

You can edit the initialization parameter file or issue `ALTER` `SYSTEM` statements to change the default location of the archived redo logs.

To change the default archived log location before recovery:

1. Use an operating system utility to restore the archived logs to a nondefault location. For example, enter:
	```
	% cp /backup/arch/* /tmp/
	```
2. Change the value for the archive log parameter to the nondefault location. You can issue `ALTER` `SYSTEM` statements while the instance is started, or edit the initialization parameter file and then start the database instance. For example, while the instance is shut down edit the parameter file as follows:
	```
	LOG_ARCHIVE_DEST_1 = 'LOCATION=/tmp/'
	LOG_ARCHIVE_FORMAT = arcr_%t_%s.arc
	```
3. Using SQL\*Plus, start a new instance by specifying the edited initialization parameter file, and then mount the database. For example, enter:
	```
	STARTUP MOUNT
	```
4. Begin media recovery as usual. For example, enter:
	```
	RECOVER DATABASE
	```

##### 30.2.4.2 Overriding the Archived Log Destination

In some cases, you may want to override the current setting for the archiving destination parameter as a source for archived log files.

To recover archived logs in a nondefault location with SET LOGSOURCE:

1. Using an operating system utility, copy the archived redo logs to an alternative location. For example, enter:
	```
	% cp $ORACLE_HOME/oradata/trgt/arch/* /tmp
	```
2. Specify the alternative location within SQL\*Plus for the recovery operation. Use the `LOGSOURCE` parameter of the `SET` statement. For example, start SQL\*Plus and run:
	```
	SET LOGSOURCE "/tmp"
	```
3. Recover the offline tablespace. For example, to recover the offline tablespace `users` do the following:
	```
	RECOVER AUTOMATIC TABLESPACE users
	```
4. Alternatively, you can avoid running `SET` `LOGSOURCE` and simply run:
	```
	RECOVER AUTOMATIC TABLESPACE users FROM "/tmp"
	```

Note:

Overriding the redo log source does not affect the archive redo log destination for online redo log groups being archived.

#### 30.2.5 Recovery Using Storage Snapshot Optimization

Storage Snapshot Optimization enables you to use third-party snapshots of the database, taken when the database is not in backup mode, to recover the database either to the current time or to a specified point in time after the snapshot was created. If the database was not placed in backup mode when the storage snapshot was created, then you can perform recovery using this snapshot only if the snapshot conforms to Oracle requirements. See " [Making Backups with Third-Party Snapshot Technologies](user-managed-database-backups.md) ". If these conditions are met, then you can take the same basic recovery steps as any other backup method, using either RMAN or SQL\*Plus.

If the storage snapshot does not conform to the requirements for using Storage Snapshot Optimization, then you create a snapshot by placing the data files in backup mode. To perform recovery using such snapshots, use the procedure described in Performing Complete Database Recovery Using SQL\*Plus or Performing Incomplete Database Recovery.

Specifying the Time for Snapshot Recovery

If a storage snapshot was created when the database was not in backup mode, you must specify the `SNAPSHOT TIME` option while using this snapshot to recover the database. The `SNAPSHOT TIME` option can be used in both the RMAN or SQL\*Plus `RECOVER` command. The time specified using the `SNAPSHOT TIME` option must be a time that is immediately after the snapshot is complete. If you specify an incorrect time, then the database may be corrupt in a way that is not repairable.

Because the time clocks in the storage array, where the snapshot takes place, and the machine hosting the Oracle Database may not be perfectly synchronized, it is recommended that you add a few seconds to the time that you specify in the `SNAPSHOT TIME` option. This helps you avoid any possibility of leaving the files in an inconsistent state by recovering to a point before the snapshot was taken.

All times specified in the `RECOVER` command, including in the `SNAPSHOT TIME` clause, are assumed to be in the time zone of the Oracle Database host. However, the time clocks in the storage array may be in a different time zone from the Oracle Database host. If the storage array reports its snapshot times in a different time zone, then you must take that difference into account when specifying the time in the `SNAPSHOT TIME` option.

Note:

The recovery point, specified by the `UNTIL` option, cannot be earlier than the specified `SNAPSHOT TIME`.

Examples: Recovery Using Storage Snapshots

The examples in this section use the `RECOVER DATABASE` command to perform recovery using snapshots. You can use the `RECOVER DATABASE` command from RMAN or SQL\*Plus. However, the `UNTIL CANCEL` clause is valid only in SQL\*Plus.

To completely recover a database:

```
RECOVER DATABASE;
```

To recover a database using a particular snapshot:

This example recovers uses a snapshot taken on August 15 at 2:00 P.M. to recover the database. The `UNTIL TIME` clause can specify any time after the snapshot.

```
RECOVER DATABASE UNTIL TIME '10/15/2012 15:00:00' SNAPSHOT TIME '10/15/2012 14:00:00';
```

To perform a partial recovery using archived redo log files:

This example uses the log files from a snapshot taken on August 15 at 2:00 P.M.

```
RECOVER DATABASE UNTIL CANCEL SNAPSHOT TIME '10/15/2012 14:00:00';
```

#### 30.2.6 Recovery Cancellation During User-Managed Recovery

If you start media recovery and must then interrupt it, then either enter `CANCEL` when prompted for a redo log file, or use your operating system's interrupt signal if you must terminate when recovering an individual data file, or when automated recovery is in progress. After recovery is canceled, you can resume it later with the `RECOVER` command. Recovery resumes where it left off when it was canceled.

#### 30.2.7 Parallel Media Recovery

By default, Oracle Database uses **parallel media recovery** to improve performance of the roll forward phase of media recovery. In parallel recovery of media, the database uses a "division of labor" approach to allocate different processes to different data blocks while rolling forward, thereby making the procedure more efficient. The number of processes used is derived from the `CPU_COUNT` initialization parameter, which by default equals the number of CPUs on the system. For example, if parallel recovery is performed on a system where `CPU_COUNT` is `4`, and only one data file is recovered, then four spawned processes read blocks from the archive logs and apply redo.

Typically, media recovery is limited by data block reads and writes. Parallel recovery attempts to use all of the available I/O bandwidth of the system to improve performance. Unless there is a system I/O bottleneck or poor asynchronous I/O support, parallel recovery is likely to improve performance of recovery.

To override the default behavior of performing parallel recovery, use the SQL\*Plus `RECOVER` command with the `NOPARALLEL` option, or `RECOVER` `PARALLEL` `0`. The `RECOVERY_PARALLELISM` initialization parameter controls instance or crash recovery only. Media recovery is not affected by the value used for `RECOVERY_PARALLELISM`.

See Also:

[SQL\*Plus User's Guide and Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=SQPUG053) for more information about the SQL\*Plus `RECOVER` `...` `PARALLEL` and `NOPARALLEL` commands

### 30.3 Performing Complete Database Recovery Using SQL\*Plus

Typically, you perform complete recovery of the database when a media failure has made one or more data files inaccessible. During complete database recovery, you use all available redo to recover the database to the current SCN.

The `V$RECOVER_FILE` view indicates which files need recovery. Depending on the circumstances, you can either recover the whole database or recover individual tablespaces or data files. Because you do not have to open the database with the `RESETLOGS` option after complete recovery, you have the option of recovering some data files at one time and the remaining data files later.

The topics in this section describe the steps necessary to complete media recovery operations.

See Also:

- Performing Closed Database Recovery
- Performing Open Database Recovery
- Performing Crash and Instance Recovery of CDBs

#### 30.3.1 Performing Closed Database Recovery

When performing complete recovery while the database is not open, you can recover either all damaged data files in one operation or perform individual recovery of each damaged data file in separate operations.

This procedure assumes the following:

- The current control file is available.
- You have backups of all needed data files.
- All necessary archived redo logs are available.

To restore and recover damaged or missing data files:

1. If the database is open, query `V$RECOVER_FILE` to determine which data files must be recovered and why they must be recovered.
	If you are planning to perform complete recovery rather than point-in-time recovery, then you can recover only those data files that require recovery, rather than the whole database. For point-in-time recovery, you must restore and recover all data files, unless you perform RMAN TSPITR. You can also use Flashback Database, but this procedure affects all data files and returns the entire database to a past time.
	You can query the `V$RECOVER_FILE` view to list data files requiring recovery by data file number with their status and error information.
	```
	SELECT FILE#, ERROR, ONLINE_STATUS, CHANGE#, TIME 
	FROM V$RECOVER_FILE;
	```
	Note:
	You cannot use `V$RECOVER_FILE` with a control file restored from backup or a control file that was re-created after the time of the media failure affecting the data files. A restored or re-created control file does not contain the information needed to update `V$RECOVER_FILE` accurately.
	You can also perform useful joins by using the data file number and the `V$DATAFILE` and `V$TABLESPACE` views to get the data file and tablespace names.
	The `ERROR` column identifies the problem for each file requiring recovery.
2. Query the `V$ARCHIVED_LOG` and `V$RECOVERY_LOG` views to determine which archived redo log files are needed.
	`V$ARCHIVED_LOG` lists file names for all archived redo logs, whereas `V$RECOVERY_LOG` lists only the archived redo logs that the database needs to perform media recovery. The latter view also includes the probable names of the files based on the naming convention specified by using the `LOG_ARCHIVE_FORMAT` parameter.
	Note:
	`V$RECOVERY_LOG` is only populated when media recovery is required for a data file. Thus, this view is not useful for a planned recovery, such as recovery from a user error.
	If a data file requires recovery, but no backup of the data file exists, then you need all redo generated starting from the time when the data file was added to the database.
3. If all archived logs are available in the default location, then skip to the Step 4.
	If some archived logs must be restored, and if sufficient space is available, then restore the required archived redo log files to the location specified by `LOG_ARCHIVE_DEST_1`. The database locates the correct log automatically when required during media recovery. For example, you might enter a command such as the following on Linux or UNIX:
	```
	% cp /disk2/arch/* $ORACLE_HOME/oradata/trgt/arch
	```
	If sufficient space is not available, then restore some or all of the required archived redo log files to an alternative location.
4. If the database is open, then shut it down. For example:
	```
	SHUTDOWN IMMEDIATE
	```
5. Inspect the media to determine the source of the problem.
	If the hardware problem that caused the media failure was temporary, and if the data was undamaged (for example, a disk or controller power failure occurred), then no media recovery is required: start the database and resume normal operations.
	If you cannot repair the problem, then proceed to the Step 6.
6. If the files are permanently damaged, then identify the most recent backups for the damaged files. Restore only the data files damaged by the media failure: do not restore undamaged data files or any online redo log files.
	For example, if `ORACLE_HOME/` `oradata/trgt/users01.dbf` is the only damaged file, then you may find that `/backup/users01_10_24_02.dbf` is the most recent backup of this file. If you do not have a backup of a specific data file, then you may be able to create an empty replacement file that can be recovered.
7. Use an operating system utility to restore the data files to their default location or to a new location. For example, a Linux or UNIX user restoring `users01.dbf ` to its default location might enter:
	```
	% cp /backup/users01_10_24_06.dbf $ORACLE_HOME/oradata/trgt/users01.dbf
	```
	Use the following guidelines when determining where to restore data file backups:
	- If the hardware problem is repaired and you can restore the data files to their default locations, then restore the data files to their default locations and begin media recovery.
	- If the hardware problem persists and you cannot restore data files to their original locations, then restore the data files to an alternative storage device. Indicate the new location of these files in the control file with the `ALTER DATABASE RENAME FILE` statement. See [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=ADMIN11430).
	- If you are restoring a data file to a raw disk or partition, then the technique is basically the same as when you are restoring to a file on a file system. Be aware of the naming conventions for files on raw devices (which differ depending on the operating system), and use an operating system utility that supports raw devices.
8. Connect to the database with administrator privileges. Then start a new instance and mount, but do not open, the database. For example, enter:
	```
	STARTUP MOUNT
	```
9. If you restored one or more damaged data files to alternative locations, then update the control file of the database to reflect the new data file names. For example, to change the file name of the data file in tablespace `users` you might enter:
	```
	ALTER DATABASE RENAME FILE '?/oradata/trgt/users01.dbf' TO
	                           '/disk2/users01.dbf';
	```
10. Obtain the data file names and statuses of all data files by checking the list of data files that normally accompanies the current control file or by querying the `V$DATAFILE` view. For example, enter:
	```
	SELECT NAME,STATUS FROM V$DATAFILE;
	```
11. Ensure that all data files requiring recovery are online. The only exceptions are data files in an offline tablespace that was taken offline normally or data files in a read-only tablespace. For example, to guarantee that a data file named `/oracle/dbs/tbs_10.f` is online, enter the following:
	```
	ALTER DATABASE DATAFILE '/oracle/dbs/tbs_10.f' ONLINE;
	```
	If a specified data file is already online, then the database ignores the statement. If you prefer, create a script to bring all data files online simultaneously, as in the following example:
	```
	SPOOL onlineall.sql
	SELECT 'ALTER DATABASE DATAFILE '''||name||''' ONLINE;' FROM V$DATAFILE;
	SPOOL OFF
	SQL> @onlineall
	```
12. If you restored archived redo logs to an alternative location, then you can specify the location before media recovery with the `LOGSOURCE` parameter of the `SET` command in SQL\*Plus. For example, if the logs are staged in `/tmp`, you can enter the following command:
	```
	SET LOGSOURCE /tmp
	```
	Alternatively, you can skip Step 12 and use the `FROM` parameter on the `RECOVER` command as in Step 13. For example, if the logs are staged in `/tmp`, you can enter the following command:
	```
	RECOVER AUTOMATIC FROM '/tmp' DATABASE
	```
	Note:
	Overriding the redo log source does not affect the archive redo log destination for online redo log groups being archived.
13. Issue a statement to recover the database, tablespace, or data file. For example, enter one of the following `RECOVER` commands:
	```
	RECOVER AUTOMATIC DATABASE   # whole database
	RECOVER AUTOMATIC TABLESPACE users   # specific tablespace
	RECOVER AUTOMATIC DATAFILE '?/oradata/trgt/users01.dbf'; # specific data file
	```
	If you choose not to automate the application of archived redo logs, then you must accept or reject each prompted log. If you automate recovery, then the database applies the logs automatically. Recovery continues until all required archived and online redo logs have been applied to the restored data files. The database notifies you when media recovery is complete:
	```
	Media recovery complete.
	```
	If no archived redo logs are required for complete media recovery, then the database applies all necessary online redo log files and terminates recovery.
14. After recovery terminates, open the database for use:
	```
	ALTER DATABASE OPEN;
	```
15. After archived logs are applied, and after making sure that a copy of each archived log group still exists in offline storage, delete the restored copy of the archived redo log file to free disk space. For example:
	```
	% rm /tmp/*.arc
	```
	See Also:
	- " [Recovering After the Loss of All Current Control Files](user-managed-recovery-advanced.md) " and " [Re-Creating a Control File](user-managed-recovery-advanced.md) " for information about restoring or re-creating the control file
	- " [Re-Creating Data Files When Backups Are Unavailable](user-managed-recovery-advanced.md) " for information about performing recovery when data file backups are missing
	- " Performing Incomplete Database Recovery " for information about performing database point-in-time recovery when you are missing redo required to completely recover the database
	- " Overview of User-Managed Media Recovery " for an overview of log application during media recovery

#### 30.3.2 Performing Open Database Recovery

You can perform complete recovery of non- `SYSTEM` data files in a database while the database is open.

This procedure assumes the following:

- The current control file is available.
- You have backups of all needed data files.
- All necessary archived redo logs are available.

It is possible for a media failure to occur while the database remains open, leaving the undamaged data files online and available for use. Damaged data files—but not the tablespaces that contain them—are automatically taken offline if the database writer cannot write to them. If the database writer cannot open a data file, an error is still returned. Queries that cannot read damaged files return errors, but the data files are not taken offline because of the failed queries. For example, you may run a SQL query and see output such as:

```
ERROR at line 1:
ORA-01116: error in opening database file 3
ORA-01110: data file 11: '/oracle/oradata/trgt/cwmlite02.dbf'
ORA-27041: unable to open file
SVR4 Error: 2: No such file or directory
Additional information: 3
```

Note:

You cannot use the procedure in this section to perform complete media recovery on the `SYSTEM` tablespace while the database is open. If the media failure damages data files of the `SYSTEM` tablespace, then the database automatically shuts down.

To restore data files in an open database:

1. Follow Step [^1] through Step [^2] in " Performing Closed Database Recovery ".
2. If the database is open, then take all tablespaces containing damaged data files offline. For example, if the tablespaces `USERS` and `TOOLS` contain damaged data files, then execute the following SQL statements:
	```
	ALTER TABLESPACE users OFFLINE TEMPORARY;
	ALTER TABLESPACE tools OFFLINE TEMPORARY;
	```
	If you specify `TEMPORARY`, then Oracle Database creates a [checkpoint](glossary.md) for all online data files in the tablespace. Files that are offline when you issue this statement may require media recovery before you bring the tablespace back online. If you specify `IMMEDIATE`, then you must perform media recovery on the tablespace before bringing it back online.
3. Inspect the media to determine the source of the problem.
	You can use the DBVERIFY utility to run an integrity check on offline data files.
	If the hardware problem that caused the media failure was temporary, and if the data was undamaged, then no media recovery is required. You can bring the offline tablespaces online and resume normal operations. If you cannot repair the problem, or if DBVERIFY reports corrupt blocks, then proceed to the Step 4.
4. If files are permanently damaged, then use operating system commands to restore the most recent backup files of only the data files damaged by the media failure. For example, to restore `users01.dbf` you might use the `cp` command on Linux or UNIX as follows:
	```
	% cp /disk2/backup/users01.dbf $ORACLE_HOME/oradata/trgt/users01.dbf
	```
	If the hardware problem is fixed and the data files can be restored to their original locations, then do so. Otherwise, restore the data files to an alternative storage device. Do not restore undamaged data files, online redo logs, or control files.
	Note:
	In some circumstances, if you do not have a backup of a specific data file, you can use the `ALTER` `DATABASE` `CREATE` `DATAFILE` statement to create an empty replacement file that is recoverable.
5. If you restored one or more damaged data files to alternative locations, then update the control file of the database to reflect the new data file names. For example, to change the file name of the data file in tablespace `users` you might enter:
	```
	ALTER DATABASE RENAME FILE '?/oradata/trgt/users01.dbf' TO
	                           '/disk2/users01.dbf';
	```
6. If you restored archived redo logs to an alternative location, then you can specify the location before media recovery with the `LOGSOURCE` parameter of the `SET` command in SQL\*Plus. For example, if the logs are staged in `/tmp`, you can enter the following command:
	```
	SET LOGSOURCE /tmp
	```
	Alternatively, you can skip Step 6 and use the `FROM` parameter on the `RECOVER` command as in Step 7. For example, if the logs are staged in `/tmp`, you can enter the following command:
	```
	RECOVER AUTOMATIC FROM '/tmp' TABLESPACE users, tools;
	```
	Note:
	Overriding the redo log source does not affect the archive redo log destination for online redo log groups being archived.
7. Connect to the database with administrator privileges, and start offline tablespace recovery of all damaged data files in one or more offline tablespaces using one step. For example, recover `users` and `tools` as follows:
	```
	RECOVER AUTOMATIC TABLESPACE users, tools;
	```
	The database begins the roll forward phase of media recovery by applying the necessary archived and online redo logs to reconstruct the restored data files. Unless the application of files is automated with the `RECOVER` `AUTOMATIC` or `SET` `AUTORECOVERY` `ON` commands, the database prompts for each required redo log file.
	Recovery continues until all required archived logs have been applied to the data files. The online redo logs are then automatically applied to the restored data files to complete media recovery. If no archived redo logs are required for complete media recovery, then the database does not prompt for any. Instead, all necessary online redo logs are applied, and media recovery is complete.
8. When the damaged tablespaces are recovered up to the moment that media failure occurred, bring the offline tablespaces online. For example, to bring tablespaces `USERS` and `TOOLS` online, issue the following statements:
	```
	ALTER TABLESPACE users ONLINE;
	ALTER TABLESPACE tools ONLINE;
	```

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=ADMIN012) to learn about creating data files and [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=SQLRF00802) to learn about `ALTER` `DATABASE` `RENAME` `FILE`
- " [Running the DBVERIFY Utility](user-managed-database-backups.md) "
- " [Recovering After the Loss of All Current Control Files](user-managed-recovery-advanced.md) " and " [Re-Creating a Control File](user-managed-recovery-advanced.md) " for information about restoring or re-creating the control file
- " [Re-Creating Data Files When Backups Are Unavailable](user-managed-recovery-advanced.md) " for information about performing recovery when data file backups are missing
- " Performing Incomplete Database Recovery " for information about performing database point-in-time recovery when you are missing redo required to completely recover the database

#### 30.3.3 Performing Crash and Instance Recovery of CDBs

Oracle Database performs crash and instance recovery for the entire multitenant container database (CDB). You cannot recover individual pluggable databases (PDBs).

This procedure assumes the following:

- The current control file is available.
- You have backups of all needed data files.
- All necessary archived redo logs are available.

To perform crash and instance recovery for a CDB:

1. Open a SQL client such as SQL\*Plus.
2. Connect to the [root](glossary.md) as a common user with the `ALTER PLUGGABLE DATABASE` system privilege.
3. Follow the procedures in " Performing Closed Database Recovery ".
	If you do not want to recover a particular PDB, take its files offline.

See Also:

- " [Recovering After the Loss of All Current Control Files](user-managed-recovery-advanced.md) " and " [Re-Creating a Control File](user-managed-recovery-advanced.md) " for information about restoring or re-creating the control file
- " [Re-Creating Data Files When Backups Are Unavailable](user-managed-recovery-advanced.md) " for information about performing recovery when data file backups are missing
- " Performing Incomplete Database Recovery " for information about performing database point-in-time recovery when you are missing redo required to completely recover the database

### 30.4 Performing Incomplete Database Recovery

Incomplete recovery is also known as database point-in-time recovery.

Typically, you perform [database point-in-time recovery (DBPITR)](glossary.md) in the following situations:

- You want to recover the database to an SCN before a user or administrative error.
- The database contains corrupt blocks.
- Complete database recovery failed because all necessary archived redo logs were not available.
- You are creating a test database or a reporting database from production database backups.

If the database is operating in `ARCHIVELOG` mode, and if the only copy of an archived redo log file is damaged, then the damaged file does not affect the present operation of the database. Table 30-2 describes situations that can arise depending on when the redo log was written and when you backed up the data file.

Table 30-2 Loss of Archived Redo Logs

| If You Backed Up... | Then... |
| --- | --- |
| All data files after the filled online redo log group (which is now archived) was written | The archived version of the filled online redo log group is not required for complete media recovery. |
| A specific data file before the filled online redo log group was written | If the corresponding data file is damaged by a permanent media failure, then use the most recent backup of the damaged data file and perform tablespace point-in-time recovery of the damaged data file, up to the damaged archived redo log file. |

Caution:

If you know that an archived redo log group has been damaged, then immediately back up all data files so that you have a whole database backup that does not require the damaged archived redo log.

The technique for DBPITR is very similar to the technique for performing closed database recovery, except that you terminate DBPITR by specifying a particular time or SCN or entering `CANCEL`. Cancel-based recovery prompts you with the suggested file names of archived redo logs. Recovery stops when you specify `CANCEL` instead of a file name or when all redo has been applied to the data files. Cancel-based recovery is the best technique to control which archived log terminates recovery.

See Also:

- " Performing Cancel-Based Incomplete Recovery "
- " Performing Time-Based or Change-Based Incomplete Recovery "
- " Performing Closed Database Recovery "

#### 30.4.1 Performing Cancel-Based Incomplete Recovery

In cancel-based recovery, recovery proceeds by prompting you with the suggested file names of archived redo log files. Recovery stops when you specify `CANCEL` instead of a file name or when all redo has been applied to the data files.

This procedure assumes the following:

- The current control file is available.
- You have backups of all needed data files.

To perform cancel-based recovery:

1. Follow Step [^1] through Step [^3] in " Performing Closed Database Recovery ".
2. Begin cancel-based recovery by issuing the following command in SQL\*Plus:
	```
	RECOVER DATABASE UNTIL CANCEL
	```
	Note:
	If you fail to specify the `UNTIL` clause on the `RECOVER` command, then the database assumes a complete recovery and does not open until all redo is applied.
	The database applies the necessary redo log files to reconstruct the restored data files. The database supplies the name it expects to find from `LOG_ARCHIVE_DEST_1` and requests you to stop or proceed with applying the log file. If the control file is a backup, then you must supply the names of the online redo logs if you want to apply the changes in these logs.
3. Continue applying redo log files until the last log has been applied to the restored data files, then cancel recovery by executing the following command:
	```
	CANCEL
	```
	The database indicates whether recovery is successful. If you cancel before all the data files have been recovered to a consistent SCN and then try to open the database, then you get an `ORA-1113` error if more recovery is necessary. You can query `V$RECOVER_FILE` to determine whether more recovery is needed, or if a backup of a data file was not restored before starting incomplete recovery.
4. Open the database with the `RESETLOGS` option. You must always reset the logs after incomplete recovery or recovery with a backup control file. For example:
	```
	ALTER DATABASE OPEN RESETLOGS;
	```
	If you attempt to use `OPEN` `RESETLOGS` when you should not, or if you neglect to reset the log when you should, then the database returns an error and does not open the database. Correct the problem and try again.
5. After opening the database with the `RESETLOGS` option, check the alert log.
	Note:
	The easiest way to locate trace files and the alert log is to run the following SQL query: `SELECT NAME, VALUE FROM V$DIAG_INFO`.
	When you open with the `RESETLOGS` option, the database returns different messages depending on whether recovery was complete or incomplete. If the recovery was complete, then the following message appears in the alert log:
	```
	RESETLOGS after complete recovery through change scn
	```
	If the recovery was incomplete, then this message is reported in the alert log, where `scn` refers to the end point of incomplete recovery:
	```
	RESETLOGS after incomplete recovery UNTIL CHANGE scn
	```
	Also check the alert log to determine whether the database detected inconsistencies between the data dictionary and the control file. Table 30-3 describes two possible scenarios.
	Table 30-3 Inconsistencies Between Data Dictionary and Control File
	| Data File Listed in Control File | Data File Listed in the Data Dictionary | Result |
	| --- | --- | --- |
	| Yes | No | References to the unlisted data file are removed from the control file. A message in the alert log indicates what was found. |
	| No | Yes | The database creates a placeholder entry in the control file under `MISSING` `nnnnn` (where `nnnnn` is the file number in decimal). `MISSING` `nnnnn` is flagged in the control file as offline and requiring media recovery. You can make the data file corresponding to `MISSING` `nnnnn` accessible by using `ALTER` `DATABASE` `RENAME` `FILE` for `MISSING` `nnnnn` so that it points to the data file. If you do not have a backup of this data file, then drop the tablespace. |

See Also:

- " About User-Managed Media Recovery Problems " for descriptions of situations that can cause `ALTER` `DATABASE` `OPEN` `RESETLOGS` to fail
- " [Recovering After the Loss of All Current Control Files](user-managed-recovery-advanced.md) " for information about restoring or re-creating the control file
- " [Re-Creating Data Files When Backups Are Unavailable](user-managed-recovery-advanced.md) " for information about performing recovery when data file backups are missing

#### 30.4.2 Performing Time-Based or Change-Based Incomplete Recovery

You can specify an SCN or time for the end point of incomplete recovery.

If your database is affected by seasonal time changes (for example, daylight savings time), then you may experience a problem if a time appears twice in the redo log and you want to recover to the second, or later time. To handle time changes, perform cancel-based or change-based recovery.

This procedure assumes the following:

- The current control file is available.
- You have backups of all needed data files.

To perform change-based or time-based recovery:

1. Follows Step [^1] through Step [^3] in " Performing Closed Database Recovery ".
2. Issue the `RECOVER` `DATABASE` `UNTIL` statement to begin recovery. If recovering to an SCN, then specify as a decimal number without quotation marks. For example, to recover through SCN 10034 issue:
	```
	RECOVER DATABASE UNTIL CHANGE 10034;
	```
	If recovering to a time, then the time is always specified using the following format, delimited by single quotation marks: `'YYYY-MM-DD:HH24:MI:SS'`. The following statement recovers the database up to a specified time:
	```
	RECOVER DATABASE UNTIL TIME '2000-12-31:12:47:30'
	```
3. Apply the necessary redo log files to recover the restored data files. The database automatically terminates the recovery when it reaches the correct time, and returns a message indicating whether recovery is successful.
	Note:
	Unless recovery is automated, the database supplies the name from `LOG_ARCHIVE_DEST_1` and asks you to stop or proceed with after each log. If the control file is a backup, then after the archived logs are applied you must supply the names of the online logs.
4. Follow Steps [^4] and [^5] in " Performing Cancel-Based Incomplete Recovery ".

See Also:

- " [Recovering After the Loss of All Current Control Files](user-managed-recovery-advanced.md) " for information about restoring or re-creating the control file
- " [Re-Creating Data Files When Backups Are Unavailable](user-managed-recovery-advanced.md) " for information about performing recovery when data file backups are missing

### 30.5 Recovering a Database in NOARCHIVELOG Mode

If a media failure damages data files in a `NOARCHIVELOG` database, then the only option for recovery is usually to restore a consistent whole database backup. If you are using logical backups created by Oracle Data Pump Export to supplement regular physical backups, then you can also attempt to restore the database by importing an exported backup of the database into a re-created database or a database restored from an old backup.

To restore and recover the most recent whole database backup:

1. If the database is open, then shut down the database. For example, enter:
	```
	SHUTDOWN IMMEDIATE
	```
2. If possible, correct the media problem so that the backup database files can be restored to their original locations.
3. Restore the most recent whole database backup with operating system commands. Restore all of the data files and control files of the whole database backup, not just the damaged files. If the hardware problem has not been corrected and some or all of the database files must be restored to alternative locations, then restore the whole database backup to a new location. The following example restores a whole database backup to its default location:
	```
	% cp /backup/*.dbf $ORACLE_HOME/oradata/trgt/
	```
4. If necessary, edit the restored initialization parameter file to indicate the new location of the control files. For example:
	```
	CONTROL_FILES = "/new_disk/oradata/trgt/control01.dbf"
	```
5. Start an instance using the restored and edited parameter file and mount, but do not open, the database. For example:
	```
	STARTUP MOUNT
	```
6. If the restored data file names are different (such as when you restore to a different file system or directory, on the same node or a different node), then update the control file to reflect the new data file locations. For example, to rename data file `1` you might enter:
	```
	ALTER DATABASE RENAME FILE '?/oradata/trgt/system01.dbf' TO
	                           '/new_disk/oradata/system01.dbf';
	```
7. If the online redo logs were located on a damaged disk, and the hardware problem is not corrected, then specify a new location for each affected online log. For example, enter:
	```
	ALTER DATABASE RENAME FILE '?/oradata/trgt/redo01.log' TO
	                           '/new_disk/oradata/redo_01.log';
	ALTER DATABASE RENAME FILE '?/oradata/trgt/redo02.log' TO
	                           '/new_disk/oradata/redo_02.log';
	```
8. Because online redo logs are never backed up, you cannot restore them with the data files and control files. To enable the database to reset the online redo logs, you must first mimic incomplete recovery:
	```
	RECOVER DATABASE UNTIL CANCEL
	CANCEL
	```
9. Open the database in `RESETLOGS` mode. This command clears the online redo logs and resets the log sequence to 1:
	```
	ALTER DATABASE OPEN RESETLOGS;
	```
	If you restore a `NOARCHIVELOG` database backup and then reset the log, the action discards all changes to the database made from the time the backup was taken to the time of the failure.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=ADMIN012) for more information about renaming and relocating data files, and [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=SQLRF00802) to learn about `ALTER` `DATABASE` `RENAME` `FILE`

### 30.6 Troubleshooting Media Recovery

This section describes how to troubleshoot user-managed media recovery, that is, media recovery performed without using Recovery Manager (RMAN). This section includes the following topics:

- About User-Managed Media Recovery Problems
- Investigating the Media Recovery Problem: Phase 1
- Trying to Fix the Recovery Problem Without Corrupting Blocks: Phase 2
- Deciding Whether to Allow Recovery to Mark as Corrupt Blocks: Phase 3
- Allowing Recovery to Corrupt Blocks: Phase 4
- Performing Trial Recovery

#### 30.6.1 About User-Managed Media Recovery Problems

Table 30-4 describes potential problems that can occur during media recovery.

Table 30-4 Media Recovery Problems

| Problem | Description |
| --- | --- |
| Missing or misnamed archived log | Recovery stops because the database cannot find the archived log recorded in the control file. |
| When you attempt to open the database, error `ORA-1113` indicates that a data file needs media recovery. | This error commonly occurs because:  - You are performing incomplete recovery but failed to restore all needed data file backups. - Incomplete recovery stopped before data files reached a consistent SCN. - You are recovering data files from an online backup, but not enough redo was applied to make the data files consistent. - You are performing recovery with a backup control file, and did not specify the location of a needed online redo log. - A data file is undergoing media recovery when you attempt to open the database. - Data files needing recovery were not brought online before you execute the `RECOVER` `DATABASE` command, and so were not recovered. |
| Redo record problems | Two possible cases are as follows:  - Recovery stops because of failed consistency checks, a problem called **stuck recovery**. Stuck recovery can occur when an underlying operating system or storage system loses a write issued by the database during normal operation. - The database signals an internal error when applying the redo. This problem can be caused by an Oracle Database bug. If [checksum](glossary.md) verification is not being used, then the errors can also be caused by corruptions to the redo or data blocks. |
| Corrupted archived logs | Logs may be corrupted while they are stored on or copied between storage systems. If `DB_BLOCK_CHECKSUM` is enabled, then the database usually signals a checksum error. If checksum checking is disabled, then log corruption may appear as a problem with redo. |
| Archived logs with incompatible parallel redo format | If you enable the parallel redo feature, then the database generates redo logs in a new format. Prior releases of Oracle are unable to apply parallel redo logs. However, releases before Oracle9i Database Release 2 (9.2) can detect the parallel redo format and indicate the inconsistency with the following error message: `External` `error` `00303,` `00000,` `"cannot` `process` `Parallel` `Redo"`. |
| Corrupted data blocks | A data file backup may have contained a corrupted data block, or the data block may become corrupted either during recovery or when it is copied to the backup. If `DB_BLOCK_CHECKSUM` is enabled, then the database computes a checksum for each block during normal operations and stores it in the block before writing it to disk. When the database reads the block from disk later, it recomputes the checksum and compares it to the stored value. If they do not match, then the database signals a checksum error. If checksum checking is disabled, then the problem may also appear as a redo corruption. |
| Random problems | Memory corruptions and other transient problems can occur during recovery. |

The symptoms of media recovery problems are usually external or internal errors signaled during recovery. For example, an external error indicates that a redo block or a data block has failed checksum verification checks. Internal errors can be caused by either bugs in the database or errors arising from the underlying operating system and hardware.

If media recovery encounters a problem while recovering a database backup, then whether it is a stuck recovery problem or a problem during redo application, the database always stops and leaves the data files undergoing recovery in a consistent state, that is, at a consistent SCN preceding the failure. You can then do one of the following:

- Open the database read-only to investigate the problem.
- Open the database with the `RESETLOGS` option, if the requirements for opening `RESETLOGS` have been met. The `RESETLOGS` restrictions apply to opening the [physical standby database](glossary.md) as well, because a standby database is updated by a form of media recovery.

In general, opening the database read-only or opening with the `RESETLOGS` option requires all online data files to be recovered to the same SCN. If this requirement is not met, then the database may signal `ORA-1113` or other errors when you attempt to open it. Some common causes of `ORA-1113` are described in Table 30-4.

The basic methodology for responding to media recovery problems occurs in the following phases:

1. Try to identify the cause of the problem. Run a trial recovery if needed.
2. If the problem is related to missing redo logs or if you suspect that there is a redo log, memory, or data block corruption, then try to resolve the problem using the methods described in Table 30-5.
3. If you cannot resolve the problem using the methods described in Table 30-5, then do one of the following:
	- Open the database with the `RESETLOGS` option if you are recovering a whole database backup. If you have performed serial media recovery, then the database contains all the changes up to but not including the changes at the SCN where the corruption occurred. No changes from this SCN onward are in the recovered part of the database. If you have restored online backups, then opening `RESETLOGS` succeeds only if you have recovered through all the `ALTER` `...` `END` `BACKUP` operations in the redo stream.
		- Proceed with recovery by allowing media recovery to corrupt data blocks. After media recovery completes, try performing [block media recovery](glossary.md) using RMAN.
		- Call Oracle Support Services as a last resort.
		See Also:
		" [Performing Disaster Recovery](rman-recovery-advanced.md) " to learn about block media recovery

#### 30.6.2 Investigating the Media Recovery Problem: Phase 1

If media recovery encounters a problem, then obtain as much information as possible after recovery halts. You do not want to waste time fixing the wrong problem, which may make matters worse.

The goal of this initial investigation is to determine whether the problem is caused by incorrect setup, corrupted redo logs, corrupted data blocks, memory corruption, or other problems. If you see a [checksum](glossary.md) error on a data block, then the data block is corrupted. If you see a checksum error on a redo log block, then the redo log is corrupted.

Sometimes the cause of a recovery problem can be difficult to determine. Nevertheless, the methods in this section enable you to quickly recover a database even when you do not completely understand the cause of the problem.

To investigate media recovery problems:

1. Examine the `alert.log` to see whether the error messages give general information about the nature of the problem. For example, does the `alert_` `SID``.log` indicate any checksum failures? Does the `alert_` `SID``.log` indicate that media recovery may have to corrupt data blocks to continue?
2. Check the trace file generated by the Oracle Database during recovery. It may contain additional error information.

#### 30.6.3 Trying to Fix the Recovery Problem Without Corrupting Blocks: Phase 2

Depending on the type of media recovery problem you suspect, you have different solutions at your disposal. You can try one or a combination of the techniques described in Table 30-5. These solutions are common repair techniques and fairly safe for resolving most media recovery issues.

Table 30-5 Media Recovery Solutions

| If You Suspect... | Then... |
| --- | --- |
| Missing or misnamed archived redo logs | Determine whether you entered the correct file name. If you did, then check whether the log is missing from the operating system. If it is missing, and if you have a backup, then restore the backup and apply the log. If you do not have a backup, then if possible perform incomplete recovery up to the point of the missing log. |
| `ORA-1113` for `ALTER DATABASE OPEN` | Review the causes of this error in Table 30-4. Ensure that all read/write data files requiring recovery are online.  If you use a backup control file for recovery, then the control file and data files must be at a consistent SCN for the database to be opened. If you do not have the necessary redo, then you must re-create the control file. |
| Corrupt archived logs | The log is corrupted if the checksum verification on the log redo block fails. If `DB_BLOCK_CHECKSUM` was not enabled either during the recovery session or when the database generated the redo, then recovery problems may be caused by corrupted logs. If the log is corrupt and an alternate copy of the corrupt log is available, then try to apply it and see whether this tactic fixes the problem.  The `DB_BLOCK_CHECKSUM` initialization parameter determines whether checksums are computed for redo log and data blocks. |
| Archived logs with incompatible parallel redo format | If you run an Oracle Database release before Oracle9i Database Release 2, and if you attempt to apply redo logs created with the parallel redo format, then you must do the following steps:  1. Upgrade the database to a later release. 2. Perform media recovery. 3. Shut down the database consistently and back up the database. 4. Downgrade the database to the original release. |
| Memory corruption or transient problems | You may be able to fix the problem by shutting down the database and restarting recovery. The database should be left in a consistent state if the second attempt also fails. |
| Corrupt data blocks | Restore and recover the data file again with user-managed methods, or restore and recover individual data blocks with the RMAN `RECOVER ... BLOCK` command. This technique may fix the problem.  A data block is corrupted if the checksum verification on the block fails. If `DB_BLOCK_CHECKING` is disabled, then a corrupted data block problem may appear as a redo problem. If you must proceed with media recovery, then you may want to allow media recovery to mark the block as corrupt for now, continue recovery, and then use RMAN to perform block media recovery later. |

If you cannot fix the problem with the methods described in Table 30-5, then there may be no easy way to fix the problem without losing data. You have these options:

- Open the database with the `RESETLOGS` option (for whole database recovery).
	This solution discards all changes after the point where the redo problem occurred, but guarantees a logically consistent database.
- Allow media recovery to corrupt one or more data blocks and then proceed.
	This option only succeeds if the alert log indicates that recovery can continue if it is allowed to corrupt a data block, which is the case for most recovery problems. This option is best if you must bring up the database quickly and recover all changes. If you are considering this option, then proceed to " Deciding Whether to Allow Recovery to Mark as Corrupt Blocks: Phase 3 ".
	See Also:
	" [Performing Block Media Recovery](rman-block-media-recovery.md) "to learn how to perform block media recovery with the `RECOVER ... BLOCK` command

#### 30.6.4 Deciding Whether to Allow Recovery to Mark as Corrupt Blocks: Phase 3

When media recovery encounters a problem, the alert log may indicate that recovery can continue if it is allowed to mark as corrupt the data block causing the problem. The alert log contains information about the block: its block type, block address, the tablespace it belongs to, and so forth. For blocks containing user data, the alert log may also report the data object number.

In this case, the database can proceed with recovery if it is allowed to mark the problem block as corrupt. Nevertheless, this response is not always advisable. For example, if the block is an important block in the `SYSTEM` tablespace, marking the block as corrupt can eventually prevent you from opening the recovered database. Another consideration is whether the recovery problem is isolated. If this problem is followed immediately by many other problems in the redo stream, then you may want to open the database with the `RESETLOGS` option.

For a block containing user data, you can usually query the database to discover which object or table owns this block. If the database is not open, then you can open the database read-only, even if you are recovering a whole database backup. The following example cancels recovery and opens the database read-only:

```
CANCEL
ALTER DATABASE OPEN READ ONLY;
```

Assume that the data object number reported in the `alert_` `SID``.log` is `8031`. You can determine the owner, object name, and object type by issuing this query:

```
SELECT OWNER, OBJECT_NAME, SUBOBJECT_NAME, OBJECT_TYPE
FROM DBA_OBJECTS
WHERE DATA_OBJECT_ID = 8031;
```

To determine whether a recovery problem is isolated, you can run a diagnostic **trial recovery**, which scans the redo stream for problems but does not actually make any changes to the recovered database. If a trial recovery discovers any recovery problems, then it reports them in the `alert_` `SID``.log`. You can use the `RECOVER` `...` `TEST` statement to invoke trial recovery, as described in " Executing the RECOVER... TEST Statement ".

After you have done these investigations, you can follow the guidelines in Table 30-6 to decide whether to allow recovery to permit corrupt blocks.

Table 30-6 Guidelines for Allowing Recovery to Permit Corrupt Blocks

| If the Problem Is... | and the Block Is... | Then... |
| --- | --- | --- |
| Not isolated |  | You can open the database with the `RESETLOGS` option. This response is important for stuck recovery problems, because stuck recovery can be caused by the operating system or a storage system losing writes. If an operating system or storage system suddenly fails, then it can cause stuck recovery problems on several blocks. |
| Isolated | In the `SYSTEM` tablespace | Do not corrupt the block, because it may eventually prevent you from opening the database. However, sometimes data in the `SYSTEM` tablespace is unimportant. If you must corrupt a `SYSTEM` block and recover all changes, then contact Oracle Support Services. |
| Isolated | Index data | Consider corrupting index blocks because the index can be rebuilt later after the database has been recovered. |
| Isolated | User data | Decide based on the importance of the data. If you continue with data file recovery and corrupt a block, then you lose data in the block. However, you can use RMAN to perform block media recovery later, after data file recovery completes. If you open `RESETLOGS`, then the database is consistent but loses any changes made after the point where recovery was stopped. |
| Isolated | Rollback or undo data | If all of the transactions are committed, then consider corrupting the rollback or undo block. The database is not harmed if the transactions that generated the undo are never rolled back. However, if those transactions are rolled back, then corrupting the undo block can cause problems. If you are unsure, then contact Oracle Support Services. |

See Also:

" Performing Trial Recovery " to learn how to perform trial recovery, and " Allowing Recovery to Corrupt Blocks: Phase 4 " if you decide to allow recovery to permit corrupt blocks

#### 30.6.5 Allowing Recovery to Corrupt Blocks: Phase 4

If you decide to allow recovery to proceed despite block corruptions, then run the `RECOVER` command with the `ALLOW` `n` `CORRUPTION` clause, where `n` is the number of allowable corrupt blocks.

To allow recovery to corrupt blocks:

1. Ensure that all normal recovery preconditions are met. For example, if the database is open, then take tablespaces offline before attempting recovery.
2. Run the `RECOVER` command as in the following example:
	```
	RECOVER DATABASE ALLOW 5 CORRUPTION
	```

#### 30.6.6 Performing Trial Recovery

When problems such as stuck recovery occur, you have a difficult choice. If the block is relatively unimportant, and if the problem is isolated, then it is better to corrupt the block. But if the problem is not isolated, then it may be better to open the database with the `RESETLOGS` option.

Because of this situation, Oracle Database supports [trial recovery](glossary.md). A trial recovery applies redo in a way similar to normal media recovery, but it never writes its changes to disk and it always rolls back its changes. Trial recovery occurs only in memory.

This section contains the following topics:
- How Trial Recovery Works
- Executing the RECOVER... TEST Statement

See Also:

" Allowing Recovery to Corrupt Blocks: Phase 4 "

##### 30.6.6.1 How Trial Recovery Works

By default, if a trial recovery encounters a stuck recovery or similar problem, then it always marks the data block as corrupt in memory when this action can allow recovery to proceed. The database writes errors generated during trial recovery to alert files. These errors are clearly marked as test run errors.

Like normal media recovery, trial recovery can prompt you for archived log file names and ask you to apply them. Trial recovery ends when:

- The database runs out of the maximum number of buffers in memory that trial recovery is permitted to use
- An unrecoverable error is signaled, that is, an error that cannot be resolved by corrupting a data block
- You cancel or interrupt the recovery session
- The next redo record in the redo stream changes the control file
- All requested redo has been applied

When trial recovery ends, the database removes all effects of the test run from the system—except the possible error messages in the alert files. If the instance fails during trial recovery, then the database removes all effects of trial recovery from the system, because trial recovery never writes changes to disk.

Trial recovery lets you foresee what problems might occur if you were to continue with normal recovery. For problems caused by ongoing memory corruption, trial recovery and normal recovery can encounter different errors.

##### 30.6.6.2 Executing the RECOVER... TEST Statement

You can use the `TEST` option for any `RECOVER` command. For example, you can start SQL\*Plus and then issue any of the following commands:

```
RECOVER DATABASE TEST
RECOVER DATABASE USING BACKUP CONTROLFILE UNTIL CANCEL TEST
RECOVER TABLESPACE users TEST
RECOVER DATABASE UNTIL CANCEL TEST
```

By default, trial recovery always attempts to corrupt blocks in memory if this action allows trial recovery to proceed. Trial recovery by default can corrupt an unlimited number of data blocks. You can specify the `ALLOW` `n` `CORRUPTION` clause on the `RECOVER` `...` `TEST` statement to limit the number of data blocks that trial recovery can corrupt in memory.

A trial recovery command is usable in any scenario in which a normal recovery command is usable. Nevertheless, you only need to run trial recovery when recovery runs into problems.

See Also:

How Trial Recovery Works

[^1]: If the database is open, query `V$RECOVER_FILE` to determine which data files must be recovered and why they must be recovered.

If you are planning to perform complete recovery rather than point-in-time recovery, then you can recover only those data files that require recovery, rather than the whole database. For point-in-time recovery, you must restore and recover all data files, unless you perform RMAN TSPITR. You can also use Flashback Database, but this procedure affects all data files and returns the entire database to a past time.

You can query the `V$RECOVER_FILE` view to list data files requiring recovery by data file number with their status and error information.

```
SELECT FILE#, ERROR, ONLINE_STATUS, CHANGE#, TIME 
FROM V$RECOVER_FILE;
```

Note:

You cannot use `V$RECOVER_FILE` with a control file restored from backup or a control file that was re-created after the time of the media failure affecting the data files. A restored or re-created control file does not contain the information needed to update `V$RECOVER_FILE` accurately.   

You can also perform useful joins by using the data file number and the `V$DATAFILE` and `V$TABLESPACE` views to get the data file and tablespace names.

The `ERROR` column identifies the problem for each file requiring recovery.

[^undefined]: Query the `V$ARCHIVED_LOG` and `V$RECOVERY_LOG` views to determine which archived redo log files are needed.

`V$ARCHIVED_LOG` lists file names for all archived redo logs, whereas `V$RECOVERY_LOG` lists only the archived redo logs that the database needs to perform media recovery. The latter view also includes the probable names of the files based on the naming convention specified by using the `LOG_ARCHIVE_FORMAT` parameter.

Note:

`V$RECOVERY_LOG` is only populated when media recovery is required for a data file. Thus, this view is not useful for a planned recovery, such as recovery from a user error.

If a data file requires recovery, but no backup of the data file exists, then you need all redo generated starting from the time when the data file was added to the database.

[^2]: If all archived logs are available in the default location, then skip to the Step 4.

If some archived logs must be restored, and if sufficient space is available, then restore the required archived redo log files to the location specified by `LOG_ARCHIVE_DEST_1`. The database locates the correct log automatically when required during media recovery. For example, you might enter a command such as the following on Linux or UNIX:

```
% cp /disk2/arch/* $ORACLE_HOME/oradata/trgt/arch
```

If sufficient space is not available, then restore some or all of the required archived redo log files to an alternative location.

[^undefined]: If the database is open, then shut it down. For example:

```
SHUTDOWN IMMEDIATE
```

[^undefined]: Inspect the media to determine the source of the problem.

If the hardware problem that caused the media failure was temporary, and if the data was undamaged (for example, a disk or controller power failure occurred), then no media recovery is required: start the database and resume normal operations.

If you cannot repair the problem, then proceed to the Step 6.

[^undefined]: If the files are permanently damaged, then identify the most recent backups for the damaged files. Restore only the data files damaged by the media failure: do not restore undamaged data files or any online redo log files.

For example, if `ORACLE_HOME/` `oradata/trgt/users01.dbf` is the only damaged file, then you may find that `/backup/users01_10_24_02.dbf` is the most recent backup of this file. If you do not have a backup of a specific data file, then you may be able to create an empty replacement file that can be recovered.

[^undefined]: Use an operating system utility to restore the data files to their default location or to a new location. For example, a Linux or UNIX user restoring `users01.dbf ` to its default location might enter:

```
% cp /backup/users01_10_24_06.dbf $ORACLE_HOME/oradata/trgt/users01.dbf
```

Use the following guidelines when determining where to restore data file backups:

- If the hardware problem is repaired and you can restore the data files to their default locations, then restore the data files to their default locations and begin media recovery.
- If the hardware problem persists and you cannot restore data files to their original locations, then restore the data files to an alternative storage device. Indicate the new location of these files in the control file with the `ALTER DATABASE RENAME FILE` statement. See [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=ADMIN11430).
- If you are restoring a data file to a raw disk or partition, then the technique is basically the same as when you are restoring to a file on a file system. Be aware of the naming conventions for files on raw devices (which differ depending on the operating system), and use an operating system utility that supports raw devices.

[^3]: Connect to the database with administrator privileges. Then start a new instance and mount, but do not open, the database. For example, enter:

```
STARTUP MOUNT
```

[^undefined]: If you restored one or more damaged data files to alternative locations, then update the control file of the database to reflect the new data file names. For example, to change the file name of the data file in tablespace `users` you might enter:

```
ALTER DATABASE RENAME FILE '?/oradata/trgt/users01.dbf' TO
                           '/disk2/users01.dbf';
```

[^undefined]: Obtain the data file names and statuses of all data files by checking the list of data files that normally accompanies the current control file or by querying the `V$DATAFILE` view. For example, enter:

```
SELECT NAME,STATUS FROM V$DATAFILE;
```

[^undefined]: Ensure that all data files requiring recovery are online. The only exceptions are data files in an offline tablespace that was taken offline normally or data files in a read-only tablespace. For example, to guarantee that a data file named `/oracle/dbs/tbs_10.f` is online, enter the following:

```
ALTER DATABASE DATAFILE '/oracle/dbs/tbs_10.f' ONLINE;
```

If a specified data file is already online, then the database ignores the statement. If you prefer, create a script to bring all data files online simultaneously, as in the following example: 

```
SPOOL onlineall.sql
SELECT 'ALTER DATABASE DATAFILE '''||name||''' ONLINE;' FROM V$DATAFILE;
SPOOL OFF

SQL> @onlineall
```

[^undefined]: If you restored archived redo logs to an alternative location, then you can specify the location before media recovery with the `LOGSOURCE` parameter of the `SET` command in SQL\*Plus. For example, if the logs are staged in `/tmp`, you can enter the following command:

```
SET LOGSOURCE /tmp
```

Alternatively, you can skip Step 12 and use the `FROM` parameter on the `RECOVER` command as in Step 13. For example, if the logs are staged in `/tmp`, you can enter the following command:

```
RECOVER AUTOMATIC FROM '/tmp' DATABASE
```

Note:

Overriding the redo log source does not affect the archive redo log destination for online redo log groups being archived.

[^undefined]: Issue a statement to recover the database, tablespace, or data file. For example, enter one of the following `RECOVER` commands:

```
RECOVER AUTOMATIC DATABASE   # whole database
RECOVER AUTOMATIC TABLESPACE users   # specific tablespace
RECOVER AUTOMATIC DATAFILE '?/oradata/trgt/users01.dbf'; # specific data file
```

If you choose not to automate the application of archived redo logs, then you must accept or reject each prompted log. If you automate recovery, then the database applies the logs automatically. Recovery continues until all required archived and online redo logs have been applied to the restored data files. The database notifies you when media recovery is complete:

```
Media recovery complete.
```

If no archived redo logs are required for complete media recovery, then the database applies all necessary online redo log files and terminates recovery.

[^undefined]: After recovery terminates, open the database for use:

```
ALTER DATABASE OPEN;
```

[^undefined]: After archived logs are applied, and after making sure that a copy of each archived log group still exists in offline storage, delete the restored copy of the archived redo log file to free disk space. For example:

```
% rm /tmp/*.arc
```

See Also:

- " [Recovering After the Loss of All Current Control Files](user-managed-recovery-advanced.md) " and " [Re-Creating a Control File](user-managed-recovery-advanced.md) " for information about restoring or re-creating the control file
- " [Re-Creating Data Files When Backups Are Unavailable](user-managed-recovery-advanced.md) " for information about performing recovery when data file backups are missing
- " Performing Incomplete Database Recovery " for information about performing database point-in-time recovery when you are missing redo required to completely recover the database
- " Overview of User-Managed Media Recovery " for an overview of log application during media recovery

[^4]: Open the database with the `RESETLOGS` option. You must always reset the logs after incomplete recovery or recovery with a backup control file. For example:

```
ALTER DATABASE OPEN RESETLOGS;
```

If you attempt to use `OPEN` `RESETLOGS` when you should not, or if you neglect to reset the log when you should, then the database returns an error and does not open the database. Correct the problem and try again.

[^5]: After opening the database with the `RESETLOGS` option, check the alert log.

Note:

The easiest way to locate trace files and the alert log is to run the following SQL query: `SELECT NAME, VALUE FROM V$DIAG_INFO`. 

When you open with the `RESETLOGS` option, the database returns different messages depending on whether recovery was complete or incomplete. If the recovery was complete, then the following message appears in the alert log:

```
RESETLOGS after complete recovery through change scn
```

If the recovery was incomplete, then this message is reported in the alert log, where `scn` refers to the end point of incomplete recovery:

```
RESETLOGS after incomplete recovery UNTIL CHANGE scn
```

Also check the alert log to determine whether the database detected inconsistencies between the data dictionary and the control file. Table 30-3 describes two possible scenarios.

Table 30-3 Inconsistencies Between Data Dictionary and Control File

| Data File Listed in Control File | Data File Listed in the Data Dictionary | Result |
| --- | --- | --- |
| Yes | No | References to the unlisted data file are removed from the control file. A message in the alert log indicates what was found. |
| No | Yes | The database creates a placeholder entry in the control file under `MISSING` `nnnnn` (where `nnnnn` is the file number in decimal). `MISSING` `nnnnn` is flagged in the control file as offline and requiring media recovery. You can make the data file corresponding to `MISSING` `nnnnn` accessible by using `ALTER` `DATABASE` `RENAME` `FILE` for `MISSING` `nnnnn` so that it points to the data file. If you do not have a backup of this data file, then drop the tablespace. |