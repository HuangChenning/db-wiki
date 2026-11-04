---
title: "Backup and Recovery User's Guide"
book: "Database Backup and Recovery User's Guide"
doc_id: F31836-11
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/bradv/user-managed-recovery-advanced.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-users-guide
---

You can recover from several common media failure scenarios when using a user-managed backup and recovery strategy, that is, a strategy that does not depend on Recovery Manager.

This chapter describes several common media failure scenarios. It shows how to recover from each failure when using a user-managed backup and recovery strategy, that is, a strategy that does not depend on Recovery Manager.

Note:

A multitenant container database is the only supported architecture in Oracle Database 21c. While the documentation is being revised, legacy terminology may persist. In most cases, "database" and "non-CDB" refer to a CDB or PDB, depending on context. In some contexts, such as upgrades, "non-CDB" refers to a non-CDB from a previous release.

### 31.1 Responding to the Loss of a Subset of the Current Control Files

Use the following procedures to recover a database if a permanent media failure has damaged one or more control files of a database and at least one current control file has not been damaged by the media failure.

This section contains the following topics:

- Copying a Multiplexed Control File to a Default Location
- Copying a Multiplexed Control File to a Nondefault Location

#### 31.1.1 Copying a Multiplexed Control File to a Default Location

If the disk and file system containing the lost control file are intact, then you can simply copy an intact control file to the location of the missing control file. In this case, you do not have to edit the `CONTROL_FILES` initialization parameter.

To replace a damaged control file by copying a multiplexed control file:

1. If the instance is still running, then shut it down:
	```
	SQL> SHUTDOWN ABORT
	```
2. Correct the hardware problem that caused the media failure. If you cannot repair the hardware problem quickly, then proceed with database recovery by restoring damaged control files to an alternative storage device, as described in " Copying a Multiplexed Control File to a Nondefault Location ".
3. Use an intact multiplexed copy of the database's current control file to copy over the damaged control files. For example, to replace `bad_cf.f ` with `good_cf.f`, you might enter:
	```
	% cp /oracle/good_cf.f /oracle/dbs/bad_cf.f
	```
4. Start a new instance and mount and open the database. For example, enter:
	```
	SQL> STARTUP
	```

#### 31.1.2 Copying a Multiplexed Control File to a Nondefault Location

If the disk and file system containing the lost control file are not intact, then you cannot copy a good control file to the location of the missing control file. In this case, you must alter the `CONTROL_FILES` initialization parameter to indicate a new location for the missing control file.

To restore a control file to a nondefault location:

1. If the instance is still running, then shut it down:
	```
	SQL> SHUTDOWN ABORT
	```
2. If you cannot correct the hardware problem that caused the media failure, then copy the intact control file to alternative location.
	For example, to copy a good version of `control01.dbf` to a new disk location you might issue the following commands:
	```
	% cp /disk1/oradata/trgt/control01.dbf /new_disk/control01.dbf
	```
3. Edit the parameter file of the database so that the `CONTROL_FILES` parameter reflects the current locations of all control files and excludes all control files that were not restored.
	Assume that the initialization parameter file contains the following setting:
	```
	CONTROL_FILES='/disk1/oradata/trgt/control01.dbf','/bad_disk/control02.dbf'
	```
	You can edit the `CONTROL_FILES` initialization parameter as follows:
	```
	CONTROL_FILES='/disk1/oradata/trgt/control01.dbf','/new_disk/control02.dbf'
	```
4. Start a new instance and mount and open the database. For example:
	```
	SQL> STARTUP
	```

### 31.2 Recovering After the Loss of All Current Control Files

Use the following procedures to restore a backup control file if a permanent media failure has damaged all control files of a database and you have a backup of the control file. When a control file is inaccessible, you can start the instance, but not mount the database. If you attempt to mount the database when the control file is unavailable, then you receive the following error message:

```
ORA-00205: error in identifying control file, check alert log for more info
```

Note:

The easiest way to locate trace files and the alert log is to run the following SQL query: `SELECT NAME, VALUE FROM V$DIAG_INFO`.

You cannot mount and open the database until the control file is accessible again. If you restore a backup control file, then you must open the database with the ` RESETLOGS` option.

As indicated in Table 31-1, the procedure for restoring the control file depends on whether the online redo logs are available.

Table 31-1 Scenarios When Control Files Are Lost

| Status of Online Logs | Status of Data Files | Restore Procedure |
| --- | --- | --- |
| Available | Current | If the online logs contain redo necessary for recovery, then restore a backup control file and apply the logs during recovery. You must specify the file name of the online logs containing the changes to open the database. After recovery, open the database with the `RESETLOGS` option.  Note: If you re-create a control file, then it is not necessary to use the `OPEN` `RESETLOGS` option after recovery when the online redo logs are accessible. |
| Unavailable | Current | If the online logs contain redo necessary for recovery, then re-create the control file. Because the online redo logs are inaccessible, open `RESETLOGS`. |
| Available | Backup | Restore a backup control file, perform complete recovery, and then open the database with the `RESETLOGS` option. |
| Unavailable | Backup | Restore a backup control file, perform incomplete recovery, and then open `RESETLOGS`. |

This section contains the following topics:

#### 31.2.1 Recovering with a Backup Control File in the Default Location

If possible, restore the control file to its original location. In this way, you avoid having to specify new control file locations in the initialization parameter file.

To restore a backup control file to its default location:

1. If the instance is still running, shut it down:
	```
	SQL> SHUTDOWN ABORT
	```
2. Correct the hardware problem that caused the media failure.
3. Restore the backup control file to all locations specified in the `CONTROL_FILES` parameter in the server parameter file or initialization parameter file. For example, if `/disk1/oradata/trgt/control01.dbf` and `/disk2/oradata/trgt/control02.dbf` are the control file locations listed in the server parameter file, then use an operating system utility to restore the backup control file to these locations:
	```
	% cp /backup/control01.dbf /disk1/oradata/trgt/control01.dbf
	% cp /backup/control02.dbf /disk2/oradata/trgt/control02.dbf
	```
4. Start a new instance and mount the database. For example, enter:
	```
	SQL> STARTUP MOUNT
	```
5. Begin recovery by executing the `RECOVER` command with the `USING` `BACKUP` `CONTROLFILE` clause. Specify `UNTIL` `CANCEL` if you are performing incomplete recovery. For example, enter:
	```
	SQL> RECOVER DATABASE USING BACKUP CONTROLFILE UNTIL CANCEL
	```
6. Apply the prompted archived logs. If you then receive another message saying that the required archived log is missing, then it probably means that a necessary redo record is located in the online redo logs. This situation can occur when unarchived changes were located in the online logs when the instance failed.
	For example, assume that you see the following:
	```
	ORA-00279: change 55636 generated at 11/08/2002 16:59:47 needed for thread 1
	ORA-00289: suggestion : /oracle/work/arc_dest/arcr_1_111.arc
	ORA-00280: change 55636 for thread 1 is in sequence #111
	Specify log: {<RET>=suggested | filename | AUTO | CANCEL}
	```
	You can specify the name of an online redo log and press Enter (you may have to try this a few times until you find the correct log):
	```
	ORACLE_HOME/oradata/redo01.dbf
	Log applied.
	Media recovery complete.
	```
	If the online logs are inaccessible, then you can cancel recovery without applying them. If all data files are current, and if redo in the online logs is required for recovery, then you cannot open the database without applying the online logs. If the online logs are inaccessible, then you must re-create the control file, using the procedure described in " Re-Creating a Control File ".
7. Open the database with the `RESETLOGS` option after finishing recovery:
	```
	SQL> ALTER DATABASE OPEN RESETLOGS;
	```

#### 31.2.2 Recovering with a Backup Control File in a Nondefault Location

If you cannot restore the control file to its original place because the media damage is too severe, then you must specify new control file locations in the server parameter file. A valid control file must be available in all locations specified by the `CONTROL_FILES` initialization parameter. If not, then the database prevents you from the mounting the database.

To restore a control file to a nondefault location:

1. If the instance is still running, shut it down:
	```
	SQL> SHUTDOWN ABORT
	```
2. Correct the hardware problem that caused the media failure.
3. Edit all locations specified in the `CONTROL_FILES` initialization parameter to reflect the new control file locations. Assume that the control file locations listed in the server parameter file are as follows, and both disks are inaccessible:
	```
	CONTROL_FILES='/disk1/oradata/trgt/control01.dbf',
	              '/disk2/oradata/trgt/control02.dbf'
	```
	You can edit the initialization parameter file and specify accessible locations, as shown in the following example:
	```
	CONTROL_FILES='/disk3/cf/control01.dbf','/disk4/cf/control02.dbf'
	```
4. Restore the backup control file to all locations specified in the `CONTROL_FILES` parameter in the server parameter file or initialization parameter file. For example, if `/disk1/oradata/trgt/control01.dbf` and `/disk2/oradata/trgt/control02.dbf` are the control file locations listed in the server parameter file, then use an operating system utility to restore the backup control file to these locations:
	```
	% cp /backup/control01.dbf /disk1/oradata/trgt/control01.dbf
	% cp /backup/control02.dbf /disk2/oradata/trgt/control02.dbf
	```
5. Start a new instance and mount the database. For example, enter:
	```
	SQL> STARTUP MOUNT
	```
6. Begin recovery by executing the `RECOVER` command with the `USING` `BACKUP` `CONTROLFILE` clause. Specify `UNTIL` `CANCEL` if you are performing incomplete recovery. For example, enter:
	```
	SQL> RECOVER DATABASE USING BACKUP CONTROLFILE UNTIL CANCEL
	```
7. Apply the prompted archived logs. If you then receive another message saying that the required archived log is missing, then it probably means that a necessary redo record is located in the online redo logs. This situation can occur when unarchived changes were located in the online logs when the instance failed.
	For example, assume that you see the following:
	```
	ORA-00279: change 55636 generated at 11/08/2002 16:59:47 needed for thread 1
	ORA-00289: suggestion : /oracle/work/arc_dest/arcr_1_111.arc
	ORA-00280: change 55636 for thread 1 is in sequence #111
	Specify log: {<RET>=suggested | filename | AUTO | CANCEL}
	```
	You can specify the name of an online redo log and press Enter (you may have to try this a few times until you find the correct log):
	```
	ORACLE_HOME/oradata/redo01.dbf
	Log applied.
	Media recovery complete.
	```
	If the online logs are inaccessible, then you can cancel recovery without applying them. If all data files are current, and if redo in the online logs is required for recovery, then you cannot open the database without applying the online logs. If the online logs are inaccessible, then you must re-create the control file, using the procedure described in " Re-Creating a Control File ".
8. Open the database with the `RESETLOGS` option after finishing recovery:
	```
	SQL> ALTER DATABASE OPEN RESETLOGS;
	```

#### 31.2.3 Recovering Through an Added Data File with a Backup Control File

If database recovery with a backup control file rolls forward through a `CREATE` `TABLESPACE` or an `ALTER` `TABLESPACE` `ADD` `DATAFILE` operation, then the database stops recovery when applying the redo record for the added files and lets you confirm the file names.

For example, suppose that the following sequence of events occurs:

1. You back up the database.
2. You create a tablespace containing the following data files: `/disk1/oradata/trgt/test01.dbf` and `/disk1/oradata/trgt/test02.dbf`.
3. You restore a backup control file and perform media recovery through the `CREATE` `TABLESPACE` operation.

You may see the following error when applying the `CREATE` `TABLESPACE` redo data:

```
ORA-00283: recovery session canceled due to errors 
ORA-01244: unnamed datafile(s) added to control file by media recovery
ORA-01110: data file 11: '/disk1/oradata/trgt/test02.dbf'
ORA-01110: data file 10: '/disk1/oradata/trgt/test01.dbf'
```

To recover through an ADD DATAFILE operation:

1. View the files added by querying `V$DATAFILE`., as in the following example:
	```
	SELECT FILE#,NAME 
	FROM V$DATAFILE;
	FILE#           NAME
	--------------- ----------------------
	1               /disk1/oradata/trgt/system01.dbf
	.
	.
	.
	10               /disk1/oradata/trgt/UNNAMED00001
	11               /disk1/oradata/trgt/UNNAMED00002
	```
2. If multiple unnamed files exist, then determine which unnamed file corresponds to which data file by using one of these methods:
	- Open the `alert_` `SID``.log`, which contains messages about the original file location for each unnamed file.
	- Derive the original file location of each unnamed file from the error message and `V$DATAFILE`: each unnamed file corresponds to the file in the error message with the same file number.
3. Issue the `ALTER` `DATABASE` `RENAME` `FILE` statement to rename the data files. For example, enter:
	```
	ALTER DATABASE RENAME FILE '/db/UNNAMED00001' TO
	                           '/disk1/oradata/trgt/test01.dbf';
	ALTER DATABASE RENAME FILE '/db/UNNAMED00002' TO
	                           '/disk1/oradata/trgt/test02.dbf';
	```
4. Continue recovery by issuing the recovery statement. For example:
	```
	RECOVER AUTOMATIC DATABASE USING BACKUP CONTROLFILE UNTIL CANCEL
	```

#### 31.2.4 Recovering Read-Only Tablespaces with a Backup Control File

If you have a read-only tablespace on read-only or slow media, then you may encounter errors or poor performance when recovering with the `USING` `BACKUP` `CONTROLFILE` option. This situation occurs when the backup control file indicates that a tablespace was read/write when the control file was backed up. In this case, media recovery may attempt to write to the files. For read-only media, the database issues an error saying that it cannot write to the files. For slow media, such as a hierarchical storage system backed up by tapes, performance may suffer.

To avoid these problems, use current control files rather than backups to recover the database. If you must use a backup control file, then you can also avoid this problem if the read-only tablespace has not suffered a media failure. You have the following alternatives for recovering read-only and slow media when using a backup control file:

- Take data files from read-only tablespaces offline before doing recovery with a backup control file, and then bring the files online after media recovery.
- Use the correct version of the control file for the recovery. If the tablespace is read-only when recovery completes, then the control file backup must be from a time when the tablespace was read-only. Similarly, if the tablespace is read/write after recovery, then the control file must be from a time when the tablespace was read/write.

### 31.3 Re-Creating a Control File

If all control files have been lost in a permanent media failure, but all online redo log members remain intact, then you can recover the database after creating a new control file. You are not required to open the database with the `RESETLOGS` option after the recovery.

Depending on the existence and currency of a control file backup, you have the options listed in Table 31-2 for generating the text of the `CREATE` `CONTROLFILE` statement. The changes to the database are recorded in the alert\_SID.log, so check this log when you are deciding which option to choose.

Table 31-2 Options for Creating the Control File

| If you... | Then... |
| --- | --- |
| Executed `ALTER` `DATABASE` `BACKUP` `CONTROLFILE` `TO` `TRACE` `NORESETLOGS` after you made the last structural change to the database, and if you have saved the SQL command trace output | Use the `CREATE` `CONTROLFILE` statement from the trace output as-is. |
| Performed your most recent execution of `ALTER` `DATABASE` `BACKUP` `CONTROLFILE` `TO` `TRACE` before you made a structural change to the database | Edit the output of `ALTER` `DATABASE` `BACKUP` `CONTROLFILE` `TO` `TRACE` to reflect the change. For example, if you recently added a data file to the database, then add this data file to the `DATAFILE` clause of the `CREATE` `CONTROLFILE` statement. |
| Backed up the control file with the `ALTER` `DATABASE` `BACKUP` `CONTROLFILE` `TO` `filename` statement (not the `TO` `TRACE` option) | Use the control file copy to obtain SQL output. Create a temporary database instance, mount the backup control file, and then run `ALTER` `DATABASE` `BACKUP` `CONTROLFILE` `TO` `TRACE` `NORESETLOGS`. If the control file copy predated a recent structural change, then edit the trace option to reflect the change. |
| Do not have a control file backup in either `TO` `TRACE` format or `TO` `filename` format | Execute the `CREATE` `CONTROLFILE` statement manually (See [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=SQLRF01203)). |

Note:

If your character set is not the default US7ASCII, then you must specify the character set as an argument to the `CREATE` `CONTROLFILE` statement. The database character set is written to the alert log at startup. The character set information is also recorded in the `BACKUP` `CONTROLFILE` `TO` `TRACE` output.

To create a control file and recover the database:

1. Start the database in `NOMOUNT` mode. For example, enter:
	```
	STARTUP NOMOUNT
	```
2. Create the control file with the `CREATE` `CONTROLFILE` statement, specifying the `NORESETLOGS` option (See to Table 31-2 for options). The following example assumes that the character set is the default US7ASCII:
	```
	CREATE CONTROLFILE REUSE DATABASE SALES NORESETLOGS ARCHIVELOG
	     MAXLOGFILES 32
	     MAXLOGMEMBERS 2
	     MAXDATAFILES 32
	     MAXINSTANCES 16
	     MAXLOGHISTORY 1600
	LOGFILE
	     GROUP 1 (
	       '/diska/prod/sales/db/log1t1.dbf',
	       '/diskb/prod/sales/db/log1t2.dbf'
	     )  SIZE 100K,
	     GROUP 2 (
	       '/diska/prod/sales/db/log2t1.dbf',
	       '/diskb/prod/sales/db/log2t2.dbf'
	     )  SIZE 100K
	DATAFILE
	     '/diska/prod/sales/db/database1.dbf',
	     '/diskb/prod/sales/db/filea.dbf';
	```
	After creating the control file, the instance mounts the database.
3. Recover the database as usual (without specifying the `USING` `BACKUP` `CONTROLFILE` clause):
	```
	RECOVER DATABASE
	```
4. Open the database after recovery completes (the `RESETLOGS` option is not required):
	```
	ALTER DATABASE OPEN;
	```
5. Immediately back up the control file. The following SQL statement backs up a database's control file to `/backup/control01.dbf`:
	```
	ALTER DATABASE BACKUP CONTROLFILE TO '/backup/control01.dbf' REUSE;
	```

To create a control file for a multitenant container database:

1. Ensure that the [multitenant container database (CDB)](glossary.md) is not mounted in any instance.
2. Open SQL\*Plus.
3. Connect to the [root](glossary.md) as a user with the `SYSDBA` privilege.
4. Follow the previous procedure for creating a control file and recovering the database.

See Also:

" [Backing Up the Control File to a Trace File](user-managed-database-backups.md) ", and " Re-Creating Data Files When Backups Are Unavailable "

#### 31.3.1 Recovering Through a RESETLOGS with a Created Control File

You can recover backups through an `OPEN` `RESETLOGS` operation so long as:

- You have a current, backup, or created control file that detects prior incarnations
- You have all available archived redo logs

If you must re-create the control file, then the trace file generated by `ALTER` `DATABASE` `BACKUP` `CONTROLFILE` `TO` `TRACE` contains the necessary commands to reconstruct the complete incarnation history. The `V$DATABASE_INCARNATION` view displays the `RESETLOGS` history of the control file, and the `V$LOG_HISTORY` view displays the archived log history.

It is possible for the incarnation history to be incomplete in the in re-created control file. For example, archived logs necessary for recovery may be missing. In this case, it is possible to create incarnation records explicitly with the `ALTER` `DATABASE` `REGISTER` `LOGFILE` statement.

In the following example, you register four logs that are necessary for recovery but are not recorded in the re-created control file, and then recover the database:

```
ALTER DATABASE REGISTER LOGFILE '/disk1/oradata/trgt/arch/arcr_1_1_42343523.arc';
ALTER DATABASE REGISTER LOGFILE '/disk1/oradata/trgt/arch/arcr_1_1_34546466.arc';
ALTER DATABASE REGISTER LOGFILE '/disk1/oradata/trgt/arch/arcr_1_1_23435466.arc';
ALTER DATABASE REGISTER LOGFILE '/disk1/oradata/trgt/arch/arcr_1_1_12343533.arc';
RECOVER AUTOMATIC DATABASE;
```

#### 31.3.2 Recovery of Read-Only Files with a Re-Created Control File

If a current or backup control file is unavailable for recovery, then you can execute a `CREATE` `CONTROLFILE` statement. Do not list read-only files in the `CREATE` `CONTROLFILE` statement so recovery can skip them. No recovery is required for read-only data files unless you restored backups of these files when the data files were read/write.

After you create a control file and attempt to mount and open the database, the database performs a data dictionary check against the files listed in the control file. For each file that is not listed in the `CREATE` `CONTROLFILE` statement but is present in the data dictionary, an entry is created for them in the control file. These files are named as `MISSING` `nnnnn`, where `nnnnn` is a 5-digit number starting with `0`.

After the database is open, rename the read-only files to their correct file names by executing the `ALTER` `DATABASE` `RENAME` `FILE` statement for all the files whose names are prefixed with `MISSING`.

To prepare for a scenario in which you might have to re-create the control file:

Run the following statement when the database is mounted or open to obtain the `CREATE` `CONTROLFILE` syntax:

```
ALTER DATABASE BACKUP CONTROLFILE TO TRACE;
```

The preceding SQL statement produces a trace file that you can edit and use as a script to re-create the control file. You can specify either the `RESETLOGS` or `NORESETLOGS` (default) keywords to generate `CREATE` `CONTROLFILE` `...` `RESETLOGS` or `CREATE` `CONTROLFILE` `...` `NORESETLOGS` versions of the script.

All the restrictions related to read-only files in `CREATE` `CONTROLFILE` statements also apply to offline normal tablespaces, except that you must to bring the tablespace online after the database is open. Omit temp files from the `CREATE` `CONTROLFILE` statement and add them after opening the database.

See Also:

" [Backing Up the Control File to a Trace File](user-managed-database-backups.md) " to learn how to make trace backups of the control file

### 31.4 Re-Creating Data Files When Backups Are Unavailable

If a data file is damaged and no backup of the file is available, then you can still recover the data file if:

- All archived log files written after the creation of the original data file are available
- The control file contains the name of the damaged file (that is, the control file is current, or is a backup taken after the damaged data file was added to the database)
	Note:
	You cannot re-create any of the data files for the `SYSTEM` tablespace by using the `CREATE` `DATAFILE` clause of the `ALTER` `DATABASE` statement because the necessary redo is not available.

To re-create a data file for recovery:

1. Create an empty data file to replace a damaged data file that has no corresponding backup. For example, assume that data file `/disk1/oradata/trgt/users01.dbf` is damaged, and no backup is available. The following statement re-creates the original data file (same size) on `disk2`:
	```
	ALTER DATABASE CREATE DATAFILE '/disk1/oradata/trgt/users01.dbf' AS
	                               '/disk2/users01.dbf';
	```
	This statement creates an empty file that is the same size as the lost file. The database looks at information in the control file and the data dictionary to obtain size information. The old data file is renamed as the new data file.
2. Perform media recovery on the empty data file. For example, enter:
	```
	RECOVER DATAFILE '/disk2/users01.dbf'
	```
3. All archived logs written after the original data file was created must be applied to the new, empty version of the lost data file during recovery.

### 31.5 Recovering NOLOGGING Tables and Indexes

You can create tables and indexes with the `CREATE` `TABLE` `AS` `SELECT` statement. You can also specify that the database create them with the `NOLOGGING` option. When you create a table or index as `NOLOGGING`, the database does not generate redo log records for the operation. Thus, you cannot recover objects created with `NOLOGGING`, even if you run in `ARCHIVELOG` mode.

Note:

If you cannot afford to lose tables or indexes created with `NOLOGGING`, then make a backup after the unrecoverable table or index is created.

Be aware that when you perform media recovery, and some tables or indexes are created normally whereas others are created with the `NOLOGGING` option, the `NOLOGGING` objects are marked logically corrupt by the `RECOVER` operation. Any attempt to access the unrecoverable objects returns an `ORA-01578` error message. Drop the `NOLOGGING` objects and re-create them if needed.

Because it is possible to create a table with the `NOLOGGING` option and then create an index with the `LOGGING` option on that table, the index is not marked as logically corrupt after you perform media recovery. The table was unrecoverable (and thus marked as corrupt after recovery), however, so the index points to corrupt blocks. The index must be dropped, and the table and index must be re-created if necessary.

See Also:

[Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=SBYDB00920) for information about the effect of `NOLOGGING` on a database

### 31.6 Recovering Transportable Tablespaces

The [transportable tablespace](glossary.md) feature of Oracle Database enables a user to transport a set of tablespaces from one database to another. Transporting a tablespace into a database is like creating a tablespace with loaded data. Using this feature is often an advantage for the following reasons:

- It is faster than using the Data Pump Export or SQL\*Loader utilities because it involves only copying data files and integrating metadata
- You can use it to move index data, hence avoiding the necessity of rebuilding indexes

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=ADMIN011) for detailed information about using the transportable tablespace feature

Like normal tablespaces, transportable tablespaces are recoverable. However, even though you can recover normal tablespaces without a backup, you must have a consistent version of the transported data files to recover a transported tablespace.

To recover a transportable tablespace, use the following procedure:

1. If the database is open, then take the transported tablespace offline. For example, if you want to recover the `users` tablespace, then issue the following statement:
	```
	ALTER TABLESPACE users OFFLINE IMMEDIATE;
	```
2. Restore a backup of the transported data files with an operating system utility. The backup can be the initial version of the transported data files or any backup taken after the tablespace is transported. For example, enter:
	```
	% cp /backup/users.dbf $ORACLE_HOME/oradata/trgt/users01.dbf
	```
3. Recover the tablespace as usual. For example, enter:
	```
	RECOVER TABLESPACE users
	```

You may see the error `ORA-01244` when recovering through a transportable tablespace operation just as when recovering through a `CREATE` `TABLESPACE` operation. In this case, rename the unnamed files to the correct locations using the procedure in " Recovering Through an Added Data File with a Backup Control File ".

### 31.7 Recovering After the Loss of Online Redo Log Files

If a media failure has affected the online redo logs of a database, then the appropriate recovery procedure depends oncertain considerations.

The considerations include the following:

- The configuration of the online redo log: mirrored or non-mirrored
- The type of media failure: temporary or permanent
- The types of online redo log files affected by the media failure: current, active, unarchived, or inactive

The following table displays `V$LOG` status information that can be crucial in a recovery situation involving online redo logs.

Table 31-3 STATUS Column of V$LOG

| Status | Description |
| --- | --- |
| `UNUSED` | The online redo log has never been written to. |
| `CURRENT` | The online redo log is active, that is, needed for instance recovery, and it is the log to which the database is currently writing. The redo log can be open or closed. |
| `ACTIVE` | The online redo log is active, that is, needed for instance recovery, but is not the log to which the database is currently writing. It may be in use for block recovery, and may or may not be archived. |
| `CLEARING` | The log is being re-created as an empty log after an `ALTER DATABASE CLEAR                                     LOGFILE` statement. After the log is cleared, then the status changes to `UNUSED`. |
| `CLEARING_CURRENT` | The current log is being cleared of a closed thread. The log can stay in this status if there is some failure in the switch such as an I/O error writing the new log header. |
| `INACTIVE` | The log is no longer needed for instance recovery. It may be in use for media recovery, and may or may not be archived. |

#### 31.7.1 Recovering After Losing a Member of a Multiplexed Online Redo Log Group

You can recover after losing a member of a multiplexed online redo log group. The database continues to function as usual during the following conditions:

If the online redo log of a database is multiplexed, and if at least one member of each online redo log group is not affected by the media failure, then the database continues functioning as usual, but error messages are written to the log writer trace file and the `alert_` `SID``.log` of the database.

You can resolve the problem of a missing member of a multiplexed online redo log group by taking one of the following actions:

- If the hardware problem is temporary, then correct it. The log writer process accesses the previously unavailable online redo log files as if the problem never existed.
- If the hardware problem is permanent, then drop the damaged member and add a new member by using the following procedure.
	Note:
	The newly added member provides no redundancy until the log group is reused.

1. Locate the file name of the damaged member in `V$LOGFILE`. The status is `INVALID` if the file is inaccessible:
	```
	SELECT GROUP#, STATUS, MEMBER 
	FROM V$LOGFILE
	WHERE STATUS='INVALID';
	GROUP#    STATUS       MEMBER
	-------   -----------  ---------------------
	0002      INVALID      /disk1/oradata/trgt/redo02.log
	```
2. Drop the damaged member. For example, to drop member `redo02.log` from group `2`, issue the following statement:
	```
	ALTER DATABASE DROP LOGFILE MEMBER '/disk1/oradata/trgt/redo02.log';
	```
3. Add a new member to the group. For example, to add `redo02.log` to group `2`, issue the following statement:
	```
	ALTER DATABASE ADD LOGFILE MEMBER '/disk1/oradata/trgt/redo02b.log' 
	  TO GROUP 2;
	```
	If the file to add already exists, then it must be the same size as the other group members, and you must specify the `REUSE` option. For example:
	```
	ALTER DATABASE ADD LOGFILE MEMBER '/disk1/oradata/trgt/redo02b.log'
	  REUSE TO GROUP 2;
	```

#### 31.7.2 Recovering After Losing All Members of an Online Redo Log Group

If a media failure damages all members of an online redo log group, then different scenarios can occur depending on the type of online redo log group affected by the failure and the archiving mode of the database.

If the damaged online redo log group is current and active, then it is needed for crash recovery; otherwise, it is not. Table 31-4 outlines the various recovery scenarios.

Table 31-4 Recovering After the Loss of an Online Redo Log Group

| If the Group Is... | Then... | And You Can... |
| --- | --- | --- |
| Inactive | It is not needed for crash recovery | Clear the archived or unarchived group. |
| Active | It is needed for crash recovery | Attempt to issue a checkpoint and clear the log; if impossible, then you must either use Flashback Database or restore a backup and perform incomplete recovery up to the most recent available redo log. |
| Current | It is the redo log that the database is currently writing to | Attempt to clear the log; if impossible, then you must either use Flashback Database or restore a backup and perform incomplete recovery up to the most recent available redo log. |

To determine whether the damaged group is active or inactive.

1. Locate the file name of the lost redo log in `V$LOGFILE` and then look for the group number corresponding to it. For example, enter:
	```
	SELECT GROUP#, STATUS, MEMBER FROM V$LOGFILE;
	GROUP#    STATUS       MEMBER
	-------   -----------  ---------------------
	0001                    /oracle/dbs/log1a.f
	0001                    /oracle/dbs/log1b.f
	0002      INVALID       /oracle/dbs/log2a.f
	0002      INVALID       /oracle/dbs/log2b.f
	0003                    /oracle/dbs/log3a.f
	0003                    /oracle/dbs/log3b.f
	```
2. For example, execute the following SQL query (sample output included):
	```
	SELECT GROUP#, MEMBERS, STATUS, ARCHIVED 
	FROM V$LOG;
	GROUP#  MEMBERS           STATUS     ARCHIVED
	------  -------           ---------  -----------
	 0001   2                 INACTIVE   YES
	 0002   2                 ACTIVE     NO
	 0003   2                 CURRENT    NO
	```
3. Perform one of the following actions:
	- If the affected group is inactive, then follow the procedure in " Losing an Inactive Online Redo Log Group ".
	- If the affected group is active (as in the preceding example), then follow the procedure in " Losing an Active Online Redo Log Group ".

##### 31.7.2.1 Losing an Inactive Online Redo Log Group

If all members of an online redo log group with `INACTIVE` status are damaged, then the procedure depends on whether you can fix the media problem that damaged the inactive redo log group. If the failure is temporary, then fix the problem. The log writer can reuse the redo log group when required. If the failure is permanent, then the damaged inactive online redo log group eventually halts normal database operation. Reinitialize the damaged group manually by issuing the `ALTER DATABASE CLEAR LOGFILE` statement as described in this section.

###### 31.7.2.1.1 Clearing Inactive, Archived Redo

You can clear an inactive redo log group when the database is open or closed. The procedure depends on whether the damaged group has been archived.

To clear an inactive, online redo log group that has been archived:

1. If the database is shut down, then start a new instance and mount the database:
	```
	STARTUP MOUNT
	```
2. Reinitialize the damaged log group. For example, to clear redo log group `2`, issue the following statement:
	```
	ALTER DATABASE CLEAR LOGFILE GROUP 2;
	```

###### 31.7.2.1.2 Clearing Inactive, Unarchived Redo

Clearing a not-yet-archived redo log allows it to be reused without archiving it. This action makes backups unusable if they were started before the last change in the log, unless the file was taken offline before the first change in the log. Hence, if you need the cleared log file for recovery of a backup, then you cannot recover that backup. Clearing a not-yet-archived-redo-log, prevents complete recovery from backups due to the missing log.

To clear an inactive, online redo log group that has not been archived:

1. If the database is shut down, then start a new instance and mount the database:
	```
	SQL> STARTUP MOUNT
	```
2. Clear the log using the `UNARCHIVED` keyword.
	For example, to clear log group `2`, issue the following SQL statement:
	```
	SQL> ALTER DATABASE CLEAR UNARCHIVED LOGFILE GROUP 2;
	```
	If there is an offline data file that requires the cleared log to bring it online, then the keywords `UNRECOVERABLE` `DATAFILE` are required. The data file must be dropped because the redo logs necessary to bring the data file online are being cleared, and there is no copy of it. For example, enter:
	```
	SQL> ALTER DATABASE CLEAR UNARCHIVED LOGFILE GROUP 2 UNRECOVERABLE DATAFILE;
	```
3. Immediately back up all data files in the database with an operating system utility, so that you have a backup you can use for complete recovery without relying on the cleared log group. For example, enter:
	```
	% cp /disk1/oracle/dbs/*.dbf /disk2/backup
	```
4. Back up the database's control file with the `ALTER` `DATABASE` statement. For example, enter:
	```
	SQL> ALTER DATABASE BACKUP CONTROLFILE TO '/oracle/dbs/cf_backup.f';
	```

###### 31.7.2.1.3 Failure of CLEAR LOGFILE Operation

The `ALTER` `DATABASE` `CLEAR` `LOGFILE` statement can fail with an I/O error due to media failure when it is not possible to:

- Relocate the redo log file onto alternative media by re-creating it under the currently configured redo log file name
- Reuse the currently configured log file name to re-create the redo log file because the name itself is invalid or unusable (for example, due to media failure)

In these cases, the `ALTER` `DATABASE` `CLEAR` `LOGFILE` statement (before receiving the I/O error) successfully informs the control file that the log is being cleared and does not require archiving. The I/O error occurs at the step in which the `CLEAR` `LOGFILE` statement attempts to create the new redo log file and write zeros to it. This fact is reflected in `V$LOG.CLEARING_CURRENT`.

##### 31.7.2.2 Losing an Active Online Redo Log Group

If the database is still running and the lost active redo log is not the current log, then issue the `ALTER` `SYSTEM` `CHECKPOINT` statement. If the operation is successful, then the active redo log becomes inactive, and you can follow the procedure in " Losing an Inactive Online Redo Log Group ". If the operation is unsuccessful, or if your database has halted, then perform one of procedures in this section, depending on the archiving mode.

The current log is the one `LGWR` is currently writing to. If a `LGWR` I/O operation fails, then LGWR terminates and the instance fails. In this case, you must restore a backup, perform incomplete recovery, and open the database with the `RESETLOGS` option.

###### 31.7.2.2.1 Recovering from the Loss of Active Logs in NOARCHIVELOG Mode

In this scenario, the database archiving mode is `NOARCHIVELOG`.

To recover from the loss of an active online log group in NOARCHIVELOG mode:

1. If the media failure is temporary, then correct the problem so that the database can reuse the group when required.
2. Restore the database from a consistent, whole database backup (data files and control files). For example, enter:
	```
	% cp /disk2/backup/*.dbf $ORACLE_HOME/oradata/trgt/
	```
3. ```
	STARTUP MOUNT
	```
4. Because online redo logs are not backed up, you cannot restore them with the data files and control files. To allow the database to reset the online redo logs, you must first mimic incomplete recovery:
	```
	RECOVER DATABASE UNTIL CANCEL
	CANCEL
	```
5. Open the database using the `RESETLOGS` option:
	```
	ALTER DATABASE OPEN RESETLOGS;
	```
6. Shut down the database consistently. For example, enter:
	```
	SHUTDOWN IMMEDIATE
	```
7. Make a whole database backup.

If the media failure is temporary, then correct the problem so that the database can reuse the group when required. If the media failure is not temporary, then use the following procedure.

###### 31.7.2.2.2 Recovering from Loss of Active Logs in ARCHIVELOG Mode

In this scenario, the database archiving mode is `ARCHIVELOG`.

To recover from loss of an active online redo log group in ARCHIVELOG mode:

1. Begin incomplete media recovery, recovering up through the log before the damaged log.
2. Ensure that the current name of the lost redo log can be used for a newly created file. If not, then rename the members of the damaged online redo log group to a new location. For example, enter:
	```
	ALTER DATABASE RENAME FILE "/disk1/oradata/trgt/redo01.log" TO "/tmp/redo01.log";
	ALTER DATABASE RENAME FILE "/disk1/oradata/trgt/redo02.log" TO "/tmp/redo02.log";
	```
3. Open the database using the `RESETLOGS` option:
	```
	ALTER DATABASE OPEN RESETLOGS;
	```
	Note:
	All updates executed from the end point of the incomplete recovery to the present must be reexecuted.

##### 31.7.2.3 Loss of Multiple Redo Log Groups

If you have lost multiple groups of the online redo log, then use the recovery method for the most difficult log to recover. The order of difficulty, from most difficult to least difficult, is as follows:

1. The current online redo log
2. An active online redo log
3. An unarchived online redo log
4. An inactive online redo log

### 31.8 Recovering from a Dropped Table Without Using Flashback Features

One common error is the accidental dropping of a table from your database. In general, the fastest and simplest solution is to use the Flashback Drop feature to reverse the dropping of the table. If you cannot use Flashback Table (for example, because Flashback Drop is disabled or the table was dropped with the `PURGE` option), then you can perform the procedure in this section.

In this scenario, assume that you do not have the Flashback Database functionality enabled, so the `FLASHBACK` `DATABASE` command is not an option. However, you do have physical backups of the database. If possible, keep the database that experienced the user error online and available for use.

Note:

Grant powerful privileges only to appropriate users to minimize user errors that require recovery.

To recover a table that has been accidentally dropped:

1. Back up all data files of the existing database in case an error is made during the remaining steps of this procedure.
2. Restore a partial backup of the database to an alternative location. At minimum, restore the following:
	- `SYSTEM` and `SYSAUX` tablespaces
	- Tablespaces containing undo or rollback segments
	- Self-contained tablespaces that contain the data to be retrieved
3. Perform incomplete recovery of this backup using a restored backup control file, to the point just before the table was dropped.
4. Export the lost data from the temporary, restored version of the database using Data Pump Export. In this case, export the accidentally dropped table.
	Note:
	System audit options are exported.
5. Use the Data Pump Import utility to import the data back into the production database.
6. Delete the files of the temporary copy of the database to conserve space.

See Also:

[Oracle Database Utilities](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=SUTIL100) for more information about Oracle Data Pump

### 31.9 Dropping a Database with SQL\*Plus

You may need to remove a database, that is, the database files that form the database, from the operating system. For example, this scenario can occur when you create a test database and then no longer have a use for it. The SQL statement `DROP` `DATABASE` can perform this function.

See Also:

" [Dropping a Database](maintaining-rman-backups.md) " to learn how to use the equivalent RMAN command `DROP` `DATABASE`

To drop a database with SQL\*Plus:

1. After connecting to the database with administrator privileges, ensure that the database is either mounted or open in restricted mode with no users connected.
	For example, enter the following command:
	```
	SQL> STARTUP RESTRICT FORCE MOUNT
	```
2. Remove the data files and control files from the operating system.
	For example, enter the following command:
	```
	SQL> DROP DATABASE; # deletes all database files, both ASM and non-ASM
	```
	If the database is on raw disk, then the command does not delete the actual raw disk special files.
3. Use an operating system utility to delete all backups and archived logs associated with the database.
	For example, on Linux and UNIX enter the following command:
	```
	% rm /backup/* /disk1/oradata/trgt/arch/*
	```