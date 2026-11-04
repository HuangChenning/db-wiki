---
title: "Backup and Recovery User's Guide"
book: "Database Backup and Recovery User's Guide"
doc_id: F31836-11
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/bradv/rman-complete-database-recovery.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-users-guide
---

Use RMAN to return your database to normal operation after the loss of one or more data files.

### 17.1 Overview of Complete Database Recovery

Complete recovery returns your database to normal operation after the loss of one or more database files.

This section contains the following topics:

#### 17.1.1 Purpose of Complete Database Recovery

Complete recovery is recovering a database to the most recent point in time, without the loss of any committed transactions.

This chapter assumes that some or all of your data files are lost or damaged. Typically, this situation is caused by a media failure or accidental deletion. Your goal is to return the database to normal operation by restoring the damaged files from RMAN backups and recovering all database changes.

#### 17.1.2 Scope of This Chapter

The complete recovery operations described in this chapter are subject to certain conditions.

This chapter makes the following assumptions:

- You have lost some or all data files and your goal is to recover all changes, but you have not lost all current control files or an entire online redo log group.
- Your database is using the current server parameter file.
- You have the complete set of archived redo logs and incremental backups needed for recovery of your data file backups. Every data file either has a backup, or a complete set of online and archived redo logs goes back to the creation of a data file with no backup.
	RMAN can handle lost data files without user intervention during restore and recovery. When a data file is lost, the possible cases can be classified as follows:
	- The control file knows about the data file, that is, you backed up the control file after data file creation, but the data file itself is not backed up. If the data file record is in the control file, then `RESTORE` creates the data file in the original location or in a user-specified location. The `RECOVER` command can then apply the necessary logs to the data file.
		- The control file does not have the data file record, that is, you did not back up the control file after data file creation. During recovery, the database detects the missing data file and reports it to RMAN, which creates a data file and continues recovery by applying the remaining logs. If the data file was created in a parent incarnation, then it is created during the restore or recovery phase as appropriate.
- You are not restoring and recovering an encrypted tablespace.
	If you perform media recovery on an encrypted tablespace, then the Oracle keystore must be open when performing media recovery of this tablespace.
- Your database runs in a single-instance configuration.
	Although RMAN can restore and recover databases in Oracle RAC and Data Guard configurations, these scenarios are beyond the scope of this manual.
- You are using the RMAN client rather than Oracle Enterprise Manager.

See Also:

- " [Performing Flashback and Database Point-in-Time Recovery](rman-performing-flashback-dbpitr.md) " for information about recovering some but not all database changes
- " [Performing Recovery with a Backup Control File](rman-recovery-advanced.md) " for information about recovering the database when all control files are lost
- " [Restoring the Server Parameter File](rman-recovery-advanced.md) " for information about restoring a backup server parameter file

#### 17.1.3 About Real-time Redo Transport for Recovery Appliance

Zero Data Loss Recovery Appliance (Recovery Appliance) substantially reduces the window of potential data loss that exists between successive archived redo log backups. You to recover target databases to within a few subseconds of a database failure.

When real-time redo transport is configured for a target database, redo data from the current redo log groups is written asynchronously to Recovery Appliance as it is generated. As the redo stream is received, it is stored as a complete RMAN archived redo log. If the target database crashes, the redo data received from the current redo log group, until the time of the crash, is used during restore and recovery operations.

You must perform certain configuration steps to enable real-time redo transport for the target database.

Note:

Real-time redo transport can be used only with Recovery Appliance.

See Also:

[Zero Data Loss Recovery Appliance Protected Databases Configuration Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=AMPDB732) for the steps to configure real-time redo transport

### 17.2 Preparing for Complete Database Recovery

You must plan your database restore and recovery strategy based on your recovery goal and which database files have been lost.

This section contains the following topics:

- Identifying the Database Files to Restore or Recover
- Determining the DBID of the Database
- Previewing Backups Used in Restore Operations
- Validating Backups Before Restoring Them
- Restoring Archived Redo Logs Needed for Recovery
- Providing the Password Required to Decrypt Encrypted Backups

#### 17.2.1 Identifying the Database Files to Restore or Recover

The techniques for determining which files require restore or recovery depend upon the type of file that is lost.

This section contains the following topics:

- Identifying a Lost Control File
- Identifying Data Files Requiring Media Recovery

##### 17.2.1.1 Identifying a Lost Control File

The database shuts down immediately when any of the multiplexed control files become inaccessible.

If you try to start the database without a valid control file at each location specified in the `CONTROL_FILES` initialization parameter, then the database reports an error.

Loss of some but not all copies of your control file does not require you to restore a control file from backup. If at least one control file remains intact, then you can either copy an intact copy of the control file over the damaged or missing control file, or update the initialization parameter file so that it does not refer to the damaged or missing control file. After the `CONTROL_FILES` parameter references only present, intact copies of the control file, you can restart your database.

If you restore the control file from backup, then you must perform media recovery of the whole database and then open it with the `OPEN RESETLOGS` option, even if no data files must be restored. This technique is described in " [Performing Recovery with a Backup Control File](rman-recovery-advanced.md) ".

##### 17.2.1.2 Identifying Data Files Requiring Media Recovery

The decision about when and how to recover depends on the state of the database and the location of its data files.

Use RMAN or SQL\*Plus to identify data files that require media recovery.

See Also:

- Identifying Data Files with RMAN
- Identifying Data Files with SQL

###### 17.2.1.2.1 Identifying Data Files with RMAN

An easy technique for determining which data files are missing is to run a `VALIDATE DATABASE` command.

Example 17-1 VALIDATE DATABASE

This example validates the database and tries to read all specified data files (sample output included).

```
RMAN> VALIDATE DATABASE;

Starting validate at 20-OCT-13
allocated channel: ORA_DISK_1
channel ORA_DISK_1: SID=90 device type=DISK
could not read file header for datafile 7 error reason 4
RMAN-00571: ===========================================================
RMAN-00569: =============== ERROR MESSAGE STACK FOLLOWS ===============
RMAN-00571: ===========================================================
RMAN-03002: failure of backup command at 10/20/2013 13:05:43
RMAN-06056: could not access datafile 7
```

The output of `VALIDATE DATABASE` command indicates that data file 7 is inaccessible. You can then run the `REPORT SCHEMA` command to obtain the tablespace name and file name for data file 7 as follows (sample output included):
```
RMAN> REPORT SCHEMA;
 
Report of database schema for database with db_unique_name RDBMS
 
List of Permanent Datafiles
===========================
File Size(MB) Tablespace           RB segs Datafile Name
---- -------- -------------------- ------- ------------------------
1    450      SYSTEM               ***     +DATAFILE/tbs_01.f
2    86       SYSAUX               ***     +DATAFILE/tbs_ax1.f
3    15       UD1                  ***     +DATAFILE/tbs_undo1.f
4    2        SYSTEM               ***     +DATAFILE/tbs_02.f
5    2        TBS_1                ***     +DATAFILE/tbs_11.f
6    2        TBS_1                ***     +DATAFILE/tbs_12.f
7    2        TBS_2                ***     +DATAFILE/tbs_21.f
 
List of Temporary Files
=======================
File Size(MB) Tablespace           Maxsize(MB) Tempfile Name
---- -------- -------------------- ----------- --------------------
1    40       TEMP                 32767       +DATAFILE/tbs_tmp1.f
```

###### 17.2.1.2.2 Identifying Data Files with SQL

Although `VALIDATE DATABASE` is a good technique for determining whether files are inaccessible, you may want to use SQL queries to obtain more detailed information.

To determine whether data files require media recovery:

1. Start SQL\*Plus and connect to the target database instance with administrator privileges.
2. Determine the status of the database by executing the following SQL query:
	```
	SELECT STATUS FROM V$INSTANCE;
	```
	If the status is `OPEN`, then the database is open. Nevertheless, some data files may require media recovery.
3. Query `V$DATAFILE_HEADER` to determine the status of your data files. Run the following SQL statements to check the data file headers:
	```
	SELECT FILE#, STATUS, ERROR, RECOVER, TABLESPACE_NAME, NAME 
	FROM   V$DATAFILE_HEADER 
	WHERE  RECOVER = 'YES' 
	OR     (RECOVER IS NULL AND ERROR IS NOT NULL);
	```
	Each row returned represents a data file that either requires media recovery or has an error requiring a restore. Check the `RECOVER` and `ERROR` columns. `RECOVER` indicates whether a file needs media recovery, and `ERROR` indicates whether there was an error reading and validating the data file header.
	If `ERROR` is not `NULL`, then the data file header cannot be read and validated. Check for a temporary hardware or operating system problem causing the error. If there is no such problem, then you must restore the file or switch to a copy.
	If the `ERROR` column is `NULL` and the `RECOVER` column is `YES`, then the file requires media recovery (and may also require a restore from backup).
	Note:
	Because `V$DATAFILE_HEADER` only reads the header block of each data file, it does not detect all problems that require the data file to be restored. For example, this view cannot tell whether a data file contains corrupt data blocks.
4. Optionally, query `V$RECOVER_FILE` to list data files requiring recovery by data file number with their status and error information. For example, execute the following query:
	```
	SELECT FILE#, ERROR, ONLINE_STATUS, CHANGE#, TIME 
	FROM   V$RECOVER_FILE;
	```
	Note:
	You cannot use `V$RECOVER_FILE` with a control file restored from backup or a control file that was re-created after the time of the media failure affecting the data files. A restored or re-created control file does not contain the information needed to update `V$RECOVER_FILE` accurately.
	To find data file and tablespace names, you can also perform joins using the data file number and the `V$DATAFILE` and `V$TABLESPACE` views, as shown in the following example.
	```
	SELECT r.FILE# AS df#, d.NAME AS df_name, t.NAME AS tbsp_name, 
	       d.STATUS, r.ERROR, r.CHANGE#, r.TIME
	FROM V$RECOVER_FILE r, V$DATAFILE d, V$TABLESPACE t
	WHERE t.TS# = d.TS#
	AND d.FILE# = r.FILE#;
	```
	The `ERROR` column identifies the problem for each file requiring recovery.

#### 17.2.2 Determining the DBID of the Database

It is recommended that you record the DBID of your database.

In situations requiring the recovery of your server parameter file or control file from autobackup, you must know the DBID. Be sure to record the DBID along with other basic information about your database.

If you do not have a record of the DBID of your database, then you can find it in the following places without opening your database:

- The DBID is used in forming the file name for the control file autobackup. Locate this file, and then refer to " [Configuring the Control File Autobackup Format](configuring-rman-client-basic.md) " to determine where the DBID appears in the file name.
- If you have any text files that preserve the output from an RMAN session, then the DBID is displayed by the RMAN client when it starts up and connects to your database. Typical output follows:
	```
	% rman TARGET /
	Recovery Manager: Release 12.1.0.1.0 - Production on Wed Jan 16 17:51:30 2013
	 
	Copyright (c) 1982, 2013, Oracle and/or its affiliates.  All rights reserved.
	 
	connected to target database: PROD (DBID=36508508)
	```

#### 17.2.3 Previewing Backups Used in Restore Operations

Previewing backups helps you to ensure that all backups required for a restore and recovery operation are available.

You can apply `RESTORE` `...` `PREVIEW` to any `RESTORE` operation to create a detailed list of every backup to be used in the requested `RESTORE` operation, and the necessary target SCN for recovery after the `RESTORE` operation is complete. This command accesses the RMAN repository to query the backup metadata, but does not actually read the backup files to ensure that they can be restored.

As an alternative to `RESTORE ... PREVIEW`, you can use the `RESTORE ... VALIDATE HEADER` command. In addition to listing the files needed for restore and recovery, the `RESTORE ... VALIDATE HEADER` command validates the backup file headers to determine whether the files on disk or in the media management catalog correspond to the metadata in the RMAN repository.

When planning your restore and recovery operation, use `RESTORE ... ``PREVIEW` or `RESTORE ... VALIDATE HEADER` to ensure that all required backups are available or to identify situations in which you may want to direct RMAN to use or avoid specific backups.

To preview backups to be used in a restore operation:

1. Run a `RESTORE` command with the `PREVIEW` option.
	For example, run one of the following commands:
	```
	RESTORE DATABASE PREVIEW;
	RESTORE ARCHIVELOG FROM TIME 'SYSDATE-7' PREVIEW;
	```
	If the report produced by `RESTORE` `...` `PREVIEW` provides too much information, then specify the `SUMMARY` option as shown in the following example:
	```
	RESTORE DATABASE PREVIEW SUMMARY;
	```
	If you are satisfied with the output, then stop here. If the output indicates that RMAN will request a backup from a tape that you know is temporarily unavailable, then continue with this procedure. If the output indicates that a backup is stored off-site, then skip to " Recalling Off-site Backups ".
2. If needed, use the `CHANGE` command to set the backup status of any temporarily unavailable backups to `UNAVAILABLE`.
	" [Updating a Backup to Status AVAILABLE or UNAVAILABLE](maintaining-rman-backups.md) " explains how to perform this task.
3. Optionally, run `RESTORE ``...` `PREVIEW` again to confirm that the restore operation does not attempt to use unavailable backups.

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF132) for details on interpreting `RESTORE` `...` `PREVIEW` output, which is in the same format as the output of the `LIST` command

##### 17.2.3.1 Recalling Off-site Backups

An offsite backup is stored in a remote location, such as a secure storage facility, and cannot be restored unless the media manager retrieves the media.

Some media managers provide status information to RMAN about which backups are off-site. Off-site backups are marked as `AVAILABLE` in the RMAN repository even though the media must be retrieved from storage before the backup can be restored. If RMAN attempts to restore an off-site backup, then the restore job fails.

To recall offsite backups:

1. (Optional) Identify the off-site backups using the `RESTORE ... PREVIEW` command. The command output indicates whether backups are stored off-site, as shown by the text after the sample output in the following example.
	```
	List of Backup Sets
	===================
	BS Key  Size       Device Type Elapsed Time Completion Time
	------- ---------- ----------- ------------ ---------------
	9       2.25M      SBT_TAPE    00:00:00     21-MAY-13
	        BP Key: 9   Status: AVAILABLE  Compressed: NO  Tag: TAG20130521T144258
	        Handle: 0aii9k7i_1_1   Media: 0aii9k7i_1_1
	 
	  List of Archived Logs in backup set 9
	  Thrd Seq     Low SCN    Low Time  Next SCN   Next Time
	  ---- ------- ---------- --------- ---------- ---------
	  1    1       392314     21-MAY-13 392541     21-MAY-13
	  1    2       392541     21-MAY-13 392545     21-MAY-13
	  1    3       392545     21-MAY-13 392548     21-MAY-13
	  1    4       392548     21-MAY-13 395066     21-MAY-13
	  1    5       395066     21-MAY-13 395095     21-MAY-13
	  1    6       395095     21-MAY-13 395355     21-MAY-13
	 
	List of remote backup files
	============================
	        Handle: aii9k7i_1_1   Media: 0aii9k7i_1_1
	validation succeeded for backup piece
	Finished restore at 21-MAY-13
	released channel: dev1
	```
	You can use `RESTORE` `...` `PREVIEW` `RECALL` to instruct the media manager to make off-site backups available.
2. If backups are stored offsite, then execute a `RESTORE ... PREVIEW` command with the `RECALL` option.
	The following example initiates recall for the off-site archived log backups shown in the previous step (sample output included):
	```
	RESTORE ARCHIVELOG ALL PREVIEW RECALL;
	```
	The following sample output indicates that RMAN initiated a recall:
	```
	List of Backup Sets
	===================
	 
	 
	BS Key  Size       Device Type Elapsed Time Completion Time
	------- ---------- ----------- ------------ ---------------
	9       2.25M      SBT_TAPE    00:00:00     21-MAY-13
	        BP Key: 9   Status: AVAILABLE  Compressed: NO  Tag: TAG20130521T144258
	        Handle: VAULT0aii9k7i_1_1   Media: /tmp,VAULT0aii9k7i_1_1
	 
	  List of Archived Logs in backup set 9
	  Thrd Seq     Low SCN    Low Time  Next SCN   Next Time
	  ---- ------- ---------- --------- ---------- ---------
	  1    1       392314     21-MAY-13 392541     21-MAY-13
	  1    2       392541     21-MAY-13 392545     21-MAY-13
	  1    3       392545     21-MAY-13 392548     21-MAY-13
	  1    4       392548     21-MAY-13 395066     21-MAY-13
	  1    5       395066     21-MAY-13 395095     21-MAY-13
	  1    6       395095     21-MAY-13 395355     21-MAY-13
	 
	Initiated recall for the following list of remote backup files
	==========================================================
	        Handle: VAULT0aii9k7i_1_1   Media: /tmp,VAULT0aii9k7i_1_1
	validation succeeded for backup piece
	Finished restore at 21-MAY-13
	released channel: dev1
	```
3. Run the `RESTORE` ` ...` `PREVIEW` command. If necessary, return to the previous step until no backups needed for the restore operation are reported as off-site.

#### 17.2.4 Validating Backups Before Restoring Them

Validating backups determines if the backups are usable.

Although the output of a restore preview operation indicates which backups will be restored, the usability of the backups is not actually verified. You can run RMAN commands to test the availability of usable backups for any `RESTORE` operation, or test the contents of a specific backup for use in `RESTORE` operations. The contents of the backups are actually read and checked for corruption.

Use one of the following validation options:

- `RESTORE` `...` `VALIDATE` to test whether RMAN can restore a specific object from a backup. RMAN chooses which backups to use.
- `VALIDATE BACKUPSET` to test the validity of a backup set that you specify.
	See Also:
	[Validating Database Files and Backups](validating-database-files-backups.md)

#### 17.2.5 Restoring Archived Redo Logs Needed for Recovery

RMAN restores archived redo log files from backup automatically as needed to perform recovery.

You can also restore archived redo logs manually to save the time needed to restore these files later during the `RECOVER` command, or if you want to store the restored archived redo log files in some new location. RMAN also gives you the flexibility of restoring all archive redo log files, the current ones, or archive redo log files from a specified previous incarnation of the database.

In case of missing archived redo logs during disaster recovery, RMAN enables you to automate the database recovery till the last available archived redo log, using the `UNTIL AVAILABLE REDO` option. You can use this option only when performing recovery for a whole database. Using this option for a data file, tablespace, or pluggable database is not supported. To perform point-in-time recovery for a pluggable database, you must provide the SCN number as the point of recovery.

By default, RMAN restores archived redo logs with names constructed using the `LOG_ARCHIVE_FORMAT` and the highest `LOG_ARCHIVE_DEST_` `n` parameters of the target database. These parameters are combined in a platform-specific fashion to form the name of the restored archived log.

This section contains the following topics:

- " Restoring Archived Redo Logs to a New Location "
- " Restoring Archived Redo Logs to Multiple Locations "

##### 17.2.5.1 Restoring Archived Redo Logs to a New Location

RMAN enables you to override the default location for restored archived redo log files.

The `SET ARCHIVELOG DESTINATION` command manually stages archived logs to different locations while a database restore operation is occurring. During recovery, RMAN knows where to find the newly restored archived logs; it does not require them to be in the location specified in the initialization parameter file.

To restore archived redo logs to a new location:

1. Start RMAN and connect to a target database, as described in " [Making Database Connections with RMAN](starting-interacting-with-rman-client.md) ".
2. Ensure that the database is mounted or open.
3. Perform the following operations within a `RUN` command:
	1. Specify the new location for the restored archived redo logs using `SET` `ARCHIVELOG` `DESTINATION`.
		2. Either explicitly restore the archived redo logs or execute commands that automatically restore the logs.
	The following sample `RUN` command explicitly restores all backup archived logs to a new location:
	```
	RUN
	{ 
	  SET ARCHIVELOG DESTINATION TO '/oracle/temp_restore';
	  RESTORE ARCHIVELOG ALL;
	  # restore and recover data files as needed
	  .
	  .
	  .
	}
	```
	The following example sets the archived log destination and then uses `RECOVER DATABASE` to restore archived logs from this destination automatically:
	```
	RUN
	{ 
	  SET ARCHIVELOG DESTINATION TO '/oracle/temp_restore';
	  RESTORE DATABASE;
	  RECOVER DATABASE; # restores and recovers logs automatically
	}
	```

##### 17.2.5.2 Restoring Archived Redo Logs to Multiple Locations

To manage disk space that is used to contain the restored logs, you can specify restore destinations for archived logs multiple times in one `RUN` block, to distribute restored logs among several destinations.

Note that you cannot specify multiple destinations simultaneously to produce multiple copies of the same log during the restore operation.

The following example restores 300 archived redo logs from backup, distributing them across the directories ` /fs1/tmp`, `/fs2/tmp`, and `/fs3/tmp`:

```
RUN 
{ 
  # Set a new location for logs 1 through 100.
  SET ARCHIVELOG DESTINATION TO '/fs1/tmp';
  RESTORE ARCHIVELOG FROM SEQUENCE 1 UNTIL SEQUENCE 100;
  # Set a new location for logs 101 through 200.
  SET ARCHIVELOG DESTINATION TO '/fs2/tmp';
  RESTORE ARCHIVELOG FROM SEQUENCE 101 UNTIL SEQUENCE 200;
  # Set a new location for logs 201 through 300.
  SET ARCHIVELOG DESTINATION TO '/fs3/tmp';
  RESTORE ARCHIVELOG FROM SEQUENCE 201 UNTIL SEQUENCE 300;
  # restore and recover data files as needed
  .
  .
  .
}
```

When you issue a `RECOVER` command, RMAN finds the needed restored archived logs automatically across the destinations to which they were restored, and applies them to the data files.

#### 17.2.6 Providing the Password Required to Decrypt Encrypted Backups

For backups encrypted using certain techniques, you must provide the password that will be used to decrypt these backups.

- Backups that were encrypted using transparent encryption with an auto-login keystore require no intervention to restore, if the keystore is available. RMAN decrypts these backups while restoring their contents.
- For backups that were encrypted using transparent encryption with a password-protected software keystore, the keystore must be available and the keystore password must be provided before the restore operation is performed. Use the `SET` command with the `DECRYPTION                             WALLET OPEN IDENTIFIED BY` option to specify the password that must be used to open the password-based software keystore.
	The following command sets the keystore password for a password-based software keystore (where `password` is a placeholder for the actual password that you enter):
	```
	SET DECRYPTION WALLET OPEN IDENTIFIED BY password;
	```
	If a user with the `SYSBACKUP` privilege is performing the recovery, and a password-protected keystore is used, grant the `SYSKM` privilege to this user.
- Backups created using password-mode encryption require the correct password to be entered before they can be restored. Use the `SET DECRYPTION` command to specify the password used to decrypt the backups. If you are restoring from a group of backups that were created with different passwords, then specify all of the required passwords on the `SET DECRYPTION` command. RMAN automatically uses the correct password with each backup set. The `SET` command must be used before executing the `RESTORE` and `RECOVER` commands.
	The following command sets the password used to decrypt backups (where `password` is a placeholder for the actual password that you enter):
	```
	SET DECRYPTION IDENTIFIED BY password;
	```

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF149) for additional information about performing restore operations using encrypted backups

### 17.3 Performing Complete Database Recovery

RMAN and Oracle Enterprise Manager Cloud Control (Cloud Control) provide full support for backup and recovery of whole multitenant container database (CDB), only the root, or one or more pluggable databases (PDBs).

During complete recovery RMAN restores one or more data files and then applies all the redo generated after the restored backup.

#### 17.3.1 About Complete Database Recovery

You use the `RESTORE` and `RECOVER` commands to restore and recover the database.

During the recovery, RMAN automatically restores backups of any needed archived redo logs. If backups are stored on a media manager, then channels must be configured in advance or a `RUN` block with `ALLOCATE CHANNEL` commands must be used to enable access to backups stored there.

If RMAN restores archived redo logs to the fast recovery area during a recovery, then it automatically deletes the restored logs after applying them to the data files. Otherwise, you can use the `DELETE ARCHIVELOG` command to delete restored archived redo logs from disk when they are no longer needed for recovery. For example, you can enter the following command:

```
RECOVER DATABASE DELETE ARCHIVELOG;
```

##### 17.3.1.1 About Restoring Data Files to a Nondefault Location

If you cannot restore data files to their default locations, then you must update the control file to reflect the new locations of the data files.

Use the RMAN `SET NEWNAME` command within a `RUN` command to specify the new file name. Afterward, use a `SWITCH` command to update the names of the data files in the control file. `SWITCH DATAFILE                 ALL` updates the control file to reflect the new names for all data files for which a `SET NEWNAME` has been issued in a `RUN` command.

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF159) for `SWITCH` syntax

#### 17.3.2 Performing Complete Recovery of a Whole CDB

When you recover a whole CDB, you recover the root and all PDBs in a single operation.

After restore and recovery of a whole database, when the database is open, missing temporary tablespaces that were recorded in the control file are re-created with their previous creation size, `AUTOEXTEND`, and `MAXSIZE` attributes. Only temporary tablespaces that are missing are re-created. If a temp file exists at the location recorded in the RMAN repository but has an invalid header, then RMAN does not re-create the temp file.

If the temp files were created as Oracle-managed files, then they are re-created in the current `DB_CREATE_FILE_DEST` location. Otherwise, they are re-created at their previous locations. If RMAN cannot re-create the file due to an I/O error or some other cause, then the error is reported in the alert log and the database open operation continues.

See Also:

" Scope of This Chapter " for some of the assumptions used in the recovery procedures

To recover a whole CDB:

1. Complete the preparation steps that are required for your scenario, as described in " Preparing for Complete Database Recovery ".
2. Start RMAN and connect to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege, as described in " [Connecting as Target to the Root](starting-interacting-with-rman-client.md) ". Connect to a recovery catalog (if used).
	RMAN displays the database status when it connects: `not started`, `not mounted`, `not open` (when the database is mounted but not open), or `none` (when the database is open).
3. If the database is not mounted, then mount but do not open the database. Use the following command:
	```
	STARTUP MOUNT;
	```
4. Use the `SHOW` command to see which channels are preconfigured.
	If the necessary devices and channels are configured, then no action is necessary. Otherwise, you can use the `CONFIGURE` command to configure automatic channels, or include `ALLOCATE CHANNEL` commands within a `RUN` block.
5. Restore and recover the database. This procedure assumes that a fast recovery area is being used.
	Do one of the following:
	- If you are restoring all data files to their original locations, then execute `RESTORE DATABASE` and `RECOVER DATABASE` sequentially at the RMAN prompt.
		For example, enter the following commands if automatic channels are configured:
		```
		RESTORE DATABASE;
		RECOVER DATABASE;
		```
		If you manually allocate channels, then you must issue the `RESTORE` and `RECOVER` commands together within a `RUN` block as shown in the following example:
		```
		RUN
		{
		  ALLOCATE CHANNEL c1 DEVICE TYPE sbt;
		  RESTORE DATABASE;
		  RECOVER DATABASE;
		}
		```
		- If you are restoring some data files to new locations, then execute `RESTORE DATABASE` and `RECOVER DATABASE` sequentially in a `RUN` command. Use the `SET NEWNAME` command to rename data files.
		The following example restores the database, specifying new names for three of the data files, and then recovers the database:
		```
		RUN
		{  
		  SET NEWNAME FOR DATAFILE 2 TO '/disk2/df2.dbf';
		  SET NEWNAME FOR DATAFILE 3 TO '/disk2/df3.dbf';
		  SET NEWNAME FOR DATAFILE 4 TO '/disk2/df4.dbf';
		  RESTORE DATABASE;
		  SWITCH DATAFILE ALL;
		  RECOVER DATABASE;
		}
		```
6. Examine the output to see if media recovery was successful. If so, open the database.
	For example, enter the following command:
	```
	ALTER DATABASE OPEN;
	```

See Also:

About Restoring Data Files to a Nondefault Location

#### 17.3.3 Performing Complete Recovery of the Root

You might consider recovering only the root if a data corruption or user error occurs that affects only the root.

However, Oracle strongly recommends that you recover all PDBs after recovering the root to prevent metadata inconsistencies among the root and the PDBs. In this case, it might be preferable to perform a complete recovery of the whole CDB.

See Also:

" Scope of This Chapter " for some of the assumptions used in the recovery procedures

To recover the root:

1. Complete the preparation steps that are required for your recovery scenario, as described in " Preparing for Complete Database Recovery ".
2. Start RMAN and connect to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege, as described in " [Connecting as Target to the Root](starting-interacting-with-rman-client.md) ".
3. Place the CDB in mounted mode.
	```
	SHUTDOWN IMMEDIATE;
	STARTUP MOUNT;
	```
4. (Optional) Use the `CONFIGURE` command to configure the default device type and automatic channels.
5. Restore and recover the root with the following commands:
	```
	RESTORE DATABASE ROOT;
	RECOVER DATABASE ROOT;
	```
6. Examine the output to see if media recovery was successful. If so, proceed to the next step.
7. (Strongly recommended) Recover all PDBs, including the CDB seed.
	1. Issue the `RESTORE PLUGGABLE DATABASE` and `RECOVER PLUGGABLE DATABASE` commands.
		The following example recovers the PDBs `sales` and `hr`:
		```
		RESTORE PLUGGABLE DATABASE 'PDB$SEED', sales, hr;
		RECOVER PLUGGABLE DATABASE 'PDB$SEED', sales, hr;
		```
		2. Examine the output to see if media recovery was successful. If so, proceed to the next step.
8. Open the CDB and all PDBs.
	```
	ALTER DATABASE OPEN;
	ALTER PLUGGABLE DATABASE ALL OPEN;
	```

See Also:

Performing Complete Recovery of a Whole CDB

#### 17.3.4 Performing Complete Recovery of a Tablespace in a CDB

Use the `RESTORE` and `RECOVER` commands with the `TABLESPACE` option to perform complete recovery of a tablespace in the CDB root.

Scope of This Chapter for some of the assumptions used in the recovery procedures

In the basic scenario, the database is open, and some but not all of the data files are damaged. You want to restore and recover the damaged tablespace while leaving the database open so that the rest of the database remains available. This scenario assumes that database `TRGT` has lost tablespace `USERS`.

To restore and recover a tablespace in the root:

1. Complete the preparation steps that are required for your recovery scenario as described in " Preparing for Complete Database Recovery ".
2. Start RMAN and connect to the root of the target database as a common user with the `SYSDBA` or `SYSBACKUP` privilege, as described in " [Making Database Connections with RMAN](starting-interacting-with-rman-client.md) ". Connect to a recovery catalog (if used).
3. If the database is open, then take the tablespace requiring recovery offline.
	For example, enter the following command to take `USERS` offline:
	```
	ALTER TABLESPACE users OFFLINE IMMEDIATE;
	```
4. Use the `SHOW` command to see which channels are preconfigured.
	For example, enter the following command (sample output is included):
	```
	SHOW ALL;
	RMAN configuration parameters for database with db_unique_name PROD1 are:
	.
	.
	.
	CONFIGURE DEFAULT DEVICE TYPE TO DISK; # default
	CONFIGURE DEVICE TYPE DISK PARALLELISM 1 BACKUP TYPE TO BACKUPSET; # default
	CONFIGURE DEVICE TYPE SBT_TAPE PARALLELISM 1 BACKUP TYPE TO BACKUPSET; # default
	CONFIGURE CHANNEL DEVICE TYPE 'SBT_TAPE' PARMS  "SBT_
	LIBRARY=/usr/local/oracle/backup/lib/libobk.so";
	```
	If the necessary devices and channels are configured, then no action is necessary. Otherwise, you can use the `CONFIGURE` command to configure automatic channels, or include `ALLOCATE CHANNEL` commands within a `RUN` block.
5. Restore and recover the tablespace. Do one of the following:
	- If you are restoring data files to their original locations, then run the `RESTORE TABLESPACE` and `RECOVER TABLESPACE` commands at the RMAN prompt.
		For example, enter the following command if automatic channels are configured (sample output included):
		```
		RMAN> RESTORE TABLESPACE users;
		 
		Starting restore at 20-JUN-13
		allocated channel: ORA_DISK_1
		channel ORA_DISK_1: SID=37 device type=DISK
		allocated channel: ORA_SBT_TAPE_1
		channel ORA_SBT_TAPE_1: SID=38 device type=SBT_TAPE
		channel ORA_SBT_TAPE_1: Oracle Secure Backup
		 
		channel ORA_DISK_1: starting datafile backup set restore
		channel ORA_DISK_1: specifying datafile(s) to restore from backup set
		channel ORA_DISK_1: restoring datafile 00012 to /disk1/oracle/dbs/users01.f
		channel ORA_DISK_1: restoring datafile 00013 to /disk1/oracle/dbs/users02.f
		channel ORA_DISK_1: restoring datafile 00021 to /disk1/oracle/dbs/users03.f
		channel ORA_DISK_1: reading from backup piece
		 /disk1/oracle/work/orcva/TKRM/backupset/2013_06_20/o1_mf_nnndf_
		TAG20130620T105435_29jflwor_.bkp
		channel ORA_DISK_1: piece
		 handle=/disk1/oracle/work/orcva/TKRM/backupset/2013_06_20/o1_mf_nnndf_
		TAG20130620T105435_29jflwor_.bkp tag=TAG20130620T105435
		channel ORA_DISK_1: restored backup piece 1
		channel ORA_DISK_1: restore complete, elapsed time: 00:00:01
		Finished restore at 20-JUN-13
		```
		```
		RMAN> RECOVER TABLESPACE users;
		 
		Starting recover at 20-JUN-13
		using channel ORA_DISK_1
		using channel ORA_SBT_TAPE_1
		 
		starting media recovery
		 
		archived log for thread 1 with sequence 27 is on disk as file
		 /disk1/oracle/work/orcva/TKRM/archivelog/2013_06_20/o1_mf_1_27_29jjmtc9_.arc
		archived log for thread 1 with sequence 28 is on disk as file
		 /disk1/oracle/work/orcva/TKRM/archivelog/2013_06_20/o1_mf_1_28_29jjnc5x_.arc
		.
		.
		.
		channel ORA_DISK_1: starting archived log restore to default destination
		channel ORA_DISK_1: restoring archived log
		archived log thread=1 sequence=5
		channel ORA_DISK_1: restoring archived log
		archived log thread=1 sequence=6
		channel ORA_DISK_1: restoring archived log
		archived log thread=1 sequence=7
		.
		.
		.
		channel ORA_DISK_1: reading from backup piece
		 /disk1/oracle/work/orcva/TKRM/backupset/2013_06_20/o1_mf_annnn_
		TAG20130620T113128_29jhr197_.bkp
		channel ORA_DISK_1: piece
		 handle=/disk1/oracle/work/orcva/TKRM/backupset/2013_06_20/o1_mf_annnn_
		TAG20130620T113128_29jhr197_.bkp tag=TAG20130620T113128
		channel ORA_DISK_1: restored backup piece 1
		channel ORA_DISK_1: restore complete, elapsed time: 00:00:02
		archived log file name=/disk1/oracle/work/orcva/TKRM/archivelog/2013_06_
		20/o1_mf_1_5_29jkdvjq_.arc thread=1 sequence=5
		channel default: deleting archived log(s)
		archived log file name=/disk1/oracle/work/orcva/TKRM/archivelog/2013_06_
		20/o1_mf_1_5_29jkdvjq_.arc RECID=91 STAMP=593611179
		archived log file name=/disk1/oracle/work/orcva/TKRM/archivelog/2013_06_
		20/o1_mf_1_6_29jkdvbz_.arc thread=1 sequence=6
		channel default: deleting archived log(s)
		.
		.
		.
		media recovery complete, elapsed time: 00:00:01
		Finished recover at 20-JUN-13
		```
	- If you are restoring some data files to new locations, then execute `RESTORE TABLESPACE` and `RECOVER TABLESPACE` in a `RUN` command. Use the `SET NEWNAME` command to rename data files, as described in " About Restoring Data Files to a Nondefault Location ".
		The following example restores the data files in tablespace `users` to a new location, and then performs recovery. Assume that the old data files were stored in the `/disk1` path and the new ones will be stored in the `/disk2` path.
		```
		RUN
		{
		  # specify the new location for each datafile
		  SET NEWNAME FOR DATAFILE '/disk1/oracle/dbs/users01.f' TO 
		                           '/disk2/users01.f';
		  SET NEWNAME FOR DATAFILE '/disk1/oracle/dbs/users02.f' TO 
		                           '/disk2/users02.f';
		  SET NEWNAME FOR DATAFILE '/disk1/oracle/dbs/users03.f' TO 
		                           '/disk2/users03.f';
		  RESTORE TABLESPACE users;
		  SWITCH DATAFILE ALL;   # update control file with new file names
		  RECOVER TABLESPACE users;
		}
		```
6. Examine the output to see if recovery was successful. If so, bring the recovered tablespace back online.
	For example, enter the following command:
	```
	ALTER TABLESPACE users ONLINE;
	```

#### 17.3.5 Performing Complete Recovery of PDBs with RMAN

You can perform complete recovery of one or more PDBs without affecting operations of other open PDBs.

See Also:

" Scope of This Chapter " for some of the assumptions used in the recovery procedures

There are two approaches to recovering a PDB with RMAN:

- Connect to the root and then use the `RESTORE PLUGGABLE DATABASE` and `RECOVER PLUGGABLE DATABASE` commands. This approach enables you to recover multiple PDBs with a single command.
- Connect to the PDB and use the `RESTORE DATABASE` and `RECOVER                             DATABASE` commands. This approach recovers only a single PDB and enables you to use the same commands used for recovering databases.

To recover one or more PDBs while connected to the root:

1. Complete the preparation steps that are required for your recovery scenario, as described in " Preparing for Complete Database Recovery ".
2. Start RMAN. Connect to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege and to a recovery catalog (if used), as described in " [Connecting as Target to the Root](starting-interacting-with-rman-client.md) ".
3. Close the PDBs that you want to recover.
	```
	ALTER PLUGGABLE DATABASE sales, hr CLOSE;
	```
	If any data files are missing, an error occurs and you cannot close a PDB. You must then connect to the PDB to which the missing data file belongs, take the missing data file offline, and then close the PDB.
	The following command takes the data file 12 offline:
	```
	ALTER PLUGGABLE DATABASE DATAFILE 12 OFFLINE;
	```
	Note:
	If the data files that store the `SYSTEM` tablespace of a PDB are missing, then follow the recovery steps that are described in " Performing Complete Recovery of Tablespaces or Data Files in a PDB with RMAN ".
4. (Optional) Use the `CONFIGURE` command to configure the default device type and automatic channels.
5. Issue the `RESTORE PLUGGABLE DATABASE` and `RECOVER PLUGGABLE DATABASE` commands.
	The following example recovers the CDB seed, `PDB$SEED`, and the PDBs `sales` and `hr`:
	```
	RESTORE PLUGGABLE DATABASE 'pdb$seed', sales, hr;
	RECOVER PLUGGABLE DATABASE 'pdb$seed', sales, hr;
	```
6. If any data files were taken offline in Step 2, make these data files online.
	Connect to the PDB to which the missing data file belongs and then make the data file online. The following command makes the data file 12 online:
	```
	ALTER DATABASE DATAFILE 12 ONLINE;
	```
7. Examine the output to see if media recovery was successful. If so, open the PDBs.
	```
	ALTER PLUGGABLE DATABASE sales, hr OPEN;
	```

To connect to and recover one PDB:

1. Complete the preparation steps that are required for your recovery scenario, as described in " Preparing for Complete Database Recovery ".
2. Start RMAN. Connect to the PDB as a [local user](glossary.md) with the `SYSDBA` system privilege and to a recovery catalog (if used), as described in " [Connecting as Target to a PDB](starting-interacting-with-rman-client.md) ".
3. ```
	ALTER PLUGGABLE DATABASE CLOSE;
	```
	If any data files are missing, an error occurs and you cannot close the PDB. You must take the missing data file offline and then close the PDB.
	The following command takes the data file 12 offline:
	```
	ALTER DATABASE DATAFILE 12 OFFLINE;
	```
	Note:
	If the data files that store the `SYSTEM` tablespace of a PDB are missing, then follow the recovery steps described in " Performing Complete Recovery of Tablespaces or Data Files in a PDB with RMAN ".
4. (Optional) Use the `CONFIGURE` command to configure the default device type and automatic channels.
5. Issue the `RESTORE DATABASE` and `RECOVER DATABASE` commands.
	```
	RESTORE DATABASE;
	RECOVER DATABASE;
	```
6. If any data files were taken offline in Step 2, make these data files online.
	The following command makes the data file 12 online:
	```
	ALTER DATABASE DATAFILE 12 ONLINE;
	```
7. ```
	ALTER PLUGGABLE DATABASE OPEN;
	```

#### 17.3.6 Performing Complete Recovery of PDBs with Cloud Control

Enterprise Manager Cloud Control (Cloud Control) provides an interface to recover PDBs.

To recover one or more PDBs with Cloud Control:

1. From the Database Home page, select Backup & Recovery from the Availability menu, and then select Perform Recovery.
2. If you have not logged in to the database previously, the Database Login page is displayed. Log in to the database using Named or New credentials and then click Login.
	Cloud Control displays the Perform Recovery page.
3. From the User Directed Recovery section, select Pluggable Databases from the Recovery Scope drop-down list, and then click Recover.
	The Perform Pluggable Database Recovery Wizard appears and displays the Pluggable Databases page.
4. Select the PDBs that you want to recover by following these steps:
	1. Click Add to display the Available Pluggable Databases page.
		2. From the list of PDBs shown, click in the Select column to designate the PDBs that you want to recover. Optionally, you can click Select All to turn on the Select option for all available PDBs. Click Select None to deselect all PDBs.
		3. Click the Select button to return to the Pluggable Databases page.
		4. Optionally, you can remove PDBs from the table by clicking in the Select column for each PDB that you want to remove and then clicking Remove.
5. Complete the wizard by navigating through the remainder of the pages to recover the PDBs. For more information about each page of the wizard, click Help.

See Also:

" [Accessing the Database Home Page Using Cloud Control](introduction-backup-recovery.md) "

#### 17.3.7 Performing Complete Recovery of Tablespaces or Data Files in a PDB with RMAN

Because tablespaces in different PDBs can have the same name, to eliminate ambiguity, you must connect directly to a PDB to recover one or more of its tablespaces. In contrast, because data file numbers and paths are unique across the CDB, you can connect either to the root or to a PDB when recovering PDB data files.

If you connect to the root, you can recover data files from multiple PDBs with a single command. If you connect to a PDB, you can recover only data files in that PDB.

To restore and recover a non-SYSTEM tablespace in a PDB:

1. Complete the preparation steps that are required for your recovery scenario, as described in " Preparing for Complete Database Recovery ".
2. Start RMAN. Connect to a target database and to a recovery catalog (if used), as described in " [Making Database Connections with RMAN](starting-interacting-with-rman-client.md)."
3. If the database is open, then take the tablespace requiring recovery offline.
	For example, enter the following command to take the `USERS` tablespace offline:
	```
	ALTER TABLESPACE users OFFLINE IMMEDIATE;
	```
4. Use the `SHOW` command to see which channels are preconfigured.
	If the necessary devices and channels are configured, then no action is necessary. Otherwise, you can use the `CONFIGURE` command to configure automatic channels, or include `ALLOCATE CHANNEL` commands within a `RUN` block.
5. Restore and recover the tablespace. Do one of the following:
	- If you are restoring data files to their original locations, then run the `RESTORE TABLESPACE` and `RECOVER TABLESPACE` commands at the RMAN prompt.
		For example, enter the following commands if automatic channels are configured:
		```
		RMAN> RESTORE TABLESPACE users;
		RMAN> RECOVER TABLESPACE users;
		```
		- If you are restoring some data files to new locations, then execute `RESTORE TABLESPACE` and `RECOVER TABLESPACE` in a `RUN` command. Use the `SET NEWNAME` command to rename data files.
6. Examine the output to see if recovery was successful. If so, bring the recovered tablespace back online.
	For example, enter the following command:
	```
	ALTER TABLESPACE users ONLINE;
	```

To restore and recover the SYSTEM tablespace in a PDB:

1. Complete the preparation steps that are required for your recovery scenario, as described in " Preparing for Complete Database Recovery ".
2. Start RMAN. Connect to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege and to a recovery catalog (if used), as described in " [Connecting as Target to the Root](starting-interacting-with-rman-client.md) ".
3. Shut down the CDB and restart it in mount mode.
	```
	SHUTDOWN IMMEDIATE;
	STARTUP MOUNT;
	```
4. Restore and recover the data files that store the `SYSTEM` tablespace of the affected PDB.
	```
	RESTORE DATAFILE 2,3;
	RECOVER DATAFILE 2,3;
	```
5. Open all the PDBs in the CDB.
	```
	ALTER PLUGGABLE DATABASE ALL OPEN READ WRITE;
	```

To recover non-SYSTEM data files in a PDB:

1. Complete the preparation steps that are required for your recovery scenario, as described in " Preparing for Complete Database Recovery ".
2. Do one of the following:
	- Start RMAN. Connect to the root as a [common user](glossary.md) with the `SYSDBA` or `SYSBACKUP` privilege and to a recovery catalog (if used), as described in " [Connecting as Target to the Root](starting-interacting-with-rman-client.md) ".
	- Start RMAN. Connect to the PDB as a local user with the `SYSDBA` privilege and to a recovery catalog (if used), as described in " [Connecting as Target to a PDB](starting-interacting-with-rman-client.md) ".
3. Issue the `RESTORE DATAFILE` and `RECOVER DATAFILE` commands.
	```
	RESTORE DATAFILE 10, 13;
	RECOVER DATAFILE 10, 13;
	```

See Also:

" About Restoring Data Files to a Nondefault Location "

#### 17.3.8 Performing Complete Recovery of Tablespaces in a PDB with Cloud Control

Oracle Enterprise Manager Cloud Control (Cloud Control) provides an interface to recover tablespaces within a PDB.

To perform complete recovery of tablespaces in a PDB with Cloud Control:

1. From the Database Home page, select Backup & Recovery from the Availability menu, and then select Perform Recovery.
2. If you have not logged in to the database previously, the Database Login page is displayed. Log in to the database using Named or New credentials and then click Login.
	Cloud Control displays the Perform Recovery page.
3. From the User Directed Recovery section, select Tablespaces from the Recovery Scope drop-down list, and then click Recover.
4. On the Perform Object Level Recovery:Point-in-time page, ensure that Recover to the current time is selected, and click Next.
5. On the Perform Object Level Recovery: Tablespaces page, select the tablespaces that you want to recover by completing these steps:
	1. Click Add to display the Available Tablespaces page.
		The Search Results table shows all available tablespaces and includes the name of the PDB to which each tablespace belongs.
		2. Click Select to designate the tablespaces that you want to recover. Optionally, you can click Select All to turn on the Select option for all available tablespaces. Click Select None to deselect all tablespaces.
		3. Click the Select button to return to the Perform Object Level Recovery: Tablespaces page.
		4. Optionally, you can remove tablespaces from the table by turning on the Select option for each tablespace that you want to remove and then clicking Remove.
6. Click Next to move to the next step in the wizard.
7. Complete the wizard by navigating through the remainder of the pages to recover the PDB tablespace. For more information about each page of the wizard, click Help.

See Also:

" [Accessing the Database Home Page Using Cloud Control](introduction-backup-recovery.md) "

#### 17.3.9 Performing Complete Recovery After Switching to a Copy

You can recover a database by switching to image copies of inaccessible data files. This technique takes less time than traditional restore and recovery because no backups need to be restored.

If you have image copies of the inaccessible data files in the fast recovery area, then you can use the `SWITCH DATAFILE ... TO COPY` command to point the control file at the data file copy and then use `RECOVER` to recover lost changes. You can also use the `SWITCH DATABASE TO COPY` command to point the control file at a copy of the whole database.

Note:

A `SWITCH TABLESPACE ... TO COPY` command is also supported for cases when all data files in a tablespace are lost and copies of all data files exist. The same restriction exists for `SWITCH DATABASE ... TO COPY`.

##### 17.3.9.1 Performing Recovery After Switching to a Data File Copy

When one or more data files are damaged, you can perform recovery by switching to existing image copies of the damaged data files.

" Scope of This Chapter " for some of the assumptions used in the recovery procedures

In the basic scenario, the database is open, and some but not all of the data files are damaged. During the course of the day, a data file goes missing due to storage failure. You must repair this file, but cannot afford the time to do a restore and recovery from a backup. You decide to use a recent image copy backup as the new file, thus eliminating restore time. This scenario assumes that database `trgt` has lost data file 4.

To switch to a data file copy and perform recovery:

1. Complete the preparation steps required for your scenario, as described in " Preparing for Complete Database Recovery ".
2. Start RMAN and connect to a target database, as described in " [Making Database Connections with RMAN](starting-interacting-with-rman-client.md) ".
	- To switch to a data file in a CDB, connect to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege.
	- To switch to a data file in a PDB, you can either connect to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege or to the PDB as a common user or local user with the `SYSDBA` or `SYSBACKUP` privilege.
3. If the database is open, then take the tablespace requiring recovery offline.
	Enter the following command to take data file 4 offline:
	```
	ALTER DATABASE DATAFILE 4 OFFLINE;
	```
4. Switch the offline data file to the latest copy.
	Enter the following command to point the control file to the latest image copy of data file 4:
	```
	SWITCH DATAFILE 4 TO COPY;
	```
5. Recover the data file with the `RECOVER DATAFILE` command.
	Enter the following command:
	```
	RECOVER DATAFILE 4;
	```
	RMAN automatically restores archived redo logs and incremental backups. Because the database uses a fast recovery area, RMAN automatically deletes them after they have been applied.
6. Examine the output to see if recovery was successful. If so, bring the recovered data file back online.
	Enter the following command to bring data file 4 online:
	```
	ALTER DATABASE DATAFILE 4 ONLINE;
	```

##### 17.3.9.2 Performing Complete Recovery After Switching to a Database Copy

You can perform complete database recovery by switching to image copies of the damaged data files instead of restoring these data files.

" Scope of This Chapter " for some of the assumptions used in the recovery procedures

In this scenario, the database is shut down, and all of the data files are damaged. You have image copies of all the damaged data files and decide to use the existing image copies as the new data files, thus eliminating restore time.

To switch to a database copy and perform recovery:

1. Complete the preparation steps required for your scenario, as described in " Preparing for Complete Database Recovery ".
2. Start RMAN and connect to the root of a target database, as described in " [Making Database Connections with RMAN](starting-interacting-with-rman-client.md) ".
	- To switch to a CDB, connect to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege.
	- To switch to a PDB, you can either connect to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege or to the PDB as a common user or local user with the `SYSDBA` or `SYSBACKUP` privilege.
3. Mount the database.
4. Switch the database to the latest copy.
	To point the control file to the latest image copy of the CDB, enter the following command:
	```
	SWITCH DATABASE TO COPY;
	```
	To switch a PDB to the latest copy, the command used depends on how the RMAN connection was established. If you connected to the root, use the `SWITCH PLUGGABLE DATABASE TO        COPY` command. If you connected to the PDB, use the `SWITCH DATABASE TO        COPY` command.
5. Recover the database.
	- Enter the following command to recover a CDB:
		```
		RECOVER DATABASE;
		```
		RMAN automatically restores archived redo logs and incremental backups. Because the database uses a fast recovery area, RMAN automatically deletes them after they have been applied.
	- To recover a PDB when connected to the root, use the `RECOVER PLUGGABLE         DATABASE` command, To recover a PDB when connected to the PDB, use the `RECOVER DATABASE` command.
6. Examine the output to see if recovery was successful. If so, open the database.
	Enter the following command to open the CDB:
	```
	ALTER DATABASE OPEN;
	```
	Enter the following command, when connected to the root, to open a PDB:
	```
	ALTER PLUGGABLE DATABASE OPEN;
	```

### 17.4 Performing Complete Recovery Using Preplugin Backups

Use the `RECOVER` command to perform complete recovery using preplugin backups.

This section contains the following topics:

- About Complete Recovery of PDBs Using PrePlugin Backups
- Performing Complete Recovery of PDBs Using Preplugin Backups
- Example: Performing Complete Recovery of PDBs Using Preplugin Backups

#### 17.4.1 About Complete Recovery of PDBs Using PrePlugin Backups

Preplugin backups are used to restore and recover a PDB to its state at a time in the past that was before the PDB was plugged in to the current CDB.

To perform complete recovery using preplugin backups, use the `FROM PREPLUGIN` clause of the `RESTORE` and `RECOVER` commands. RMAN restores data files using preplugin backups and then uses the preplugin incremental backups and archived redo logs to recover data files to a point in time that is before the PDB was plugged in to the destination CDB.

The metadata for the preplugin backups is migrated to the destination CDB when you unplug the PDB or use the `DBMS_PDB.EXPORTRMANBACKUP()` procedure with non-CDBs. Preplugin backups are not automatically migrated to the destination CDB. You must ensure that the destination CDB has access to the backups created on the source database.

The location to which RMAN restores preplugin archived redo logs depends on whether a fast recovery area is configured in the destination CDB. If a fast recovery area is not the default destination for archived redo log files in the CDB, then RMAN restores preplugin archived redo logs to the fast recovery area. If the fast recovery area is the default destination for archived redo log files in the CDB, then you must use the `SET ARCHIVELOG DESTINATION` command to specify a location for the preplugin archived redo log files.

See Also:

- [About Preplugin Backups](rman-backup-concepts.md)
- Performing Complete Recovery of PDBs Using Preplugin Backups
- Example: Performing Complete Recovery of PDBs Using Preplugin Backups

#### 17.4.2 Performing Complete Recovery of PDBs Using Preplugin Backups

RMAN performs complete recovery of a PDB using preplugin backups. These preplugin backups were created on a source non-CDB or a source CDB before the PDB was migrated to the current target CDB.

Preplugin backups must include all archived redo logs that are required to recover the PDB.

To perform complete recovery using preplugin backups of a non-CDB, the non-CDB backups must be created using the procedure described in " [Creating a Preplugin Backup of the Whole Database](backing-up-database.md) ".

Note:

You cannot recover a PDB using preplugin backups if the preplugin backup was created before the PDB was opened with the `RESETLOGS` option.

To perform complete recovery of a PDB using preplugin backups:

1. Ensure that the prerequisites for performing recovery using preplugin backups described in [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF-GUID-73642FF2-43C5-48B2-9969-99001C52EB50) are met.
2. Ensure that the shared location containing preplugin backups of the PDB is accessible to the destination host.
	Note:
	Using shared disk is the only method that is supported to share prelugin backups with the destination host. Manually copying the required backups to the destination is not supported.
3. Connect to the target CDB using one of the following techniques:
	- Connect to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege
	- Connect to the PDB that needs to be recovered as a user with the `SYSDBA` or `SYSBACKUP` privilege.
	See " [Making Database Connections with RMAN](starting-interacting-with-rman-client.md) ".
4. Close the PDB that is being recovered. For example:
	```
	ALTER PLUGGABLE DATABASE pdb1 CLOSE IMMEDIATE;
	```
5. Set the current container to the PDB that is being recovered. For example:
	```
	SET PREPLUGIN CONTAINER=pdb1;
	```
6. (Optional) To view the preplugin backups, use the `LIST` command.
	```
	LIST PREPLUGIN BACKUP OF PLUGGABLE DATABASE pdb1;
	LIST PREPLUGIN ARCHIVELOG ALL;
	```
7. (Optional) To catalog any backups that were not stored in the source database control file before migration, use the `CATALOG...PREPLUGIN` command.
	The `ROOT` must be open in read-write mode for cataloging backups. The following command catalogs the specified archived redo log:
	```
	CATALOG PREPLUGIN ARCHIVELOG '/disk1/o1_mf_annnn_dmy2r45h_.bkp';
	```
8. Restore the PDB using preplugin backups.
	```
	RESTORE PLUGGABLE DATABASE pdb1 FROM PREPLUGIN;
	```
9. Recover the PDB using preplugin backups.
	The `RECOVER ... FROM PREPLUGIN` command performs preplugin recovery. If the destination CDB uses the fast recovery area as the archivelog destination, then use `SET ARCHIVELOG DESTINATION` to specify the destination to which preplugin backups must be recovered.
	```
	RUN
	{
	   SET ARCHIVELOG DESTINATION TO '/disk1/alog_dest';
	   RECOVER PLUGGABLE DATABASE pdb1 FROM PREPLUGIN;
	}
	```
10. Restore any new data files that were added after `pdb1` was plugged in to the destination CDB and then perform normal recovery of `pdb1`.
	```
	RESTORE PLUGGABLE DATABASE pdb1 SKIP PREPLUGIN;
	RECOVER PLUGGABLE DATABASE pdb1;
	```
11. The following command opens the PDB called `pdb1`.
	```
	ALTER PLUGGABLE DATABASE pdb1 OPEN;
	```

See Also:

- Example: Performing Complete Recovery of PDBs Using Preplugin Backups
- About Complete Recovery of PDBs Using PrePlugin Backups

#### 17.4.3 Example: Performing Complete Recovery of PDBs Using Preplugin Backups

This example performs complete recovery of a PDB `my_pdb` in the destination CDB `prod_cdb` using preplugin backups.

The PDB `my_pdb` was unplugged from the CDB `test_cdb` and then plugged in to the CDB `prod_cdb`. When this PDB was unplugged from `test_cdb`, its metadata was stored in the file `mypdb.xml`. This metadata was used to plug `my_pdb` into `prod_cdb`. The backups of `my_pdb` that were created in the source CDB `test_cdb` are stored in the shared location `/oracle/database/backups`. The CDB `prod_cdb` uses the fast recovery area to store archived redo log files.

1. Ensure that the prerequisites for performing recovery using preplugin backups described in [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF-GUID-4491C03F-C5F8-43E5-B4C4-FE26C70F2E9B) are met.
2. Set up a shared disk to share the preplugin backups created on the source with the destination host.
3. Start RMAN and connect to the root of `prod_cdb` as a common user with the `SYSBABKUP` privilege.
	The following command uses password file authentication to connect to the root as a common user with the `SYSBACKUP` privilege.
	```
	CONNECT TARGET sbu@prod_cdb as SYSBACKUP;
	```
4. Close the PDB `my_pdb`.
	```
	ALTER PLUGGABLE DATABASE my_pdb CLOSE IMMEDIATE;
	```
5. Set the preplugin container to the PDB that is being recovered.
	```
	SET PREPLUGIN CONTAINER=my_pdb;
	```
6. Restore `my_pdb` using the preplugin backups that were created on the source CDB `test_cdb` before `my_pdb` was plugged in to `prod_cdb`.
	```
	RESTORE PLUGGABLE DATABASE my_pdb FROM PREPLUGIN;
	```
7. Recover `my_pdb` using preplugin backups. Because the fast recovery area is configured to store archived redo log files for the destination CDB, you must specify an alternate destination for the restored preplugin archived redo log files.
	```
	RUN
	{
	   SET ARCHIVELOG DESTINATION TO '/disk1/arc_dest/';
	   RECOVER PLUGGABLE DATABASE my_pdb FROM PREPLUGIN;
	}
	```
8. If any data files were added to `my_pdb` after it was plugged in to `prod_cdb`, then restore these data files and then recover the PDB `my_pdb`.
	```
	RESTORE PLUGGABLE DATABASE my_pdb SKIP PREPLUGIN;
	RECOVER PLUGGABLE DATABASE my_pdb;
	```
9. Open the PDB `my_pdb`.
	```
	ALTER PLUGGABLE DATABASE my_pdb OPEN;
	```

### 17.5 Performing Complete Recovery of Application Containers

RMAN enables you to use the `RESTORE` and `RECOVER` commands to perform complete recovery of the application containers without impacting the other containers in the CDB.

See Also:

- Performing Complete Recovery of the Application Root
- Performing Complete Recovery of the Application Root and Application PDBs
- Performing Complete Recovery of Application PDBs

#### 17.5.1 Performing Complete Recovery of the Application Root

Use the `RESTORE` and `RECOVER` commands to perform complete recovery of the application root.

The `COMPATIBLE` parameter for the CDB must be set to 19.0 or higher.

To recover the application root when connected to the root in a CDB

1. Perform one of the following steps:
	- Start RMAN and connect to the application root as an application common user with the `SYSDBA` or `SYSBACKUP` privilege.
		The application root has its own service name and you can connect to the application root in the same way that you connect to a PDB.
	- Start RMAN and connect to the CDB root as a common user with the `SYSDBA` or `SYSBACKUP` privilege.
2. Close the application container whose application root needs to be recovered.
	When connected to the application root or CDB, use the following command to close the application container whose application root is called `hr_appcont`:
	```
	ALTER PLUGGABLE DATABASE hr_appcont CLOSE;
	```
3. (Optional) Use the `CONFIGURE` command to configure the default device type and automatic channels.
4. Restore and recover the application root.
	The following commands restore and recover an application root named hr\_appcont:
	```
	RESTORE APPLICATION ROOT DATABASE hr_appcont;
	RECOVER APPLICATION ROOT DATABASE hr_appcont;
	```
5. Examine the output to see if media recovery was successful. If so, proceed to the next step.
6. When connected to the application root, use the following command:
	```
	ALTER DATABASE OPEN;
	```
	When connected to the CDB, use the following command:
	```
	ALTER PLUGGABLE DATABASE hr_appcont OPEN;
	```

See Also:

[Making Database Connections with RMAN](starting-interacting-with-rman-client.md)

#### 17.5.2 Performing Complete Recovery of the Application Root and Application PDBs

You can perform complete recovery of an application container, which includes the application root and all its application PDBs without impacting the other PDBs within the CDB.

The `COMPATIBLE` parameter for the CDB must be set to 12.2 or higher.

To perform complete recovery of the application root and all its application PDBs:

1. Start RMAN and connect to the application root as an application common user with the `SYSDBA` or `SYSBACKUP` privilege.
	The application root has its own service name and you can connect to the application root in the same way that you connect to a PDB.
2. The following command closes the application container whose application root is called `hr_appcont`:
	```
	ALTER PLUGGABLE DATABASE hr_appcont CLOSE;
	```
3. (Optional) Use the `CONFIGURE` command to configure the default device type and automatic channels.
4. Restore and recover the application container (application root and all application PDBs) using the following commands.
	```
	RESTORE DATABASE;
	RECOVER DATABASE;
	```
5. Examine the output to see if media recovery was successful. If so, proceed to the next step.
6. Open the application root and all the application PDBs.
	```
	ALTER DATABASE OPEN;
	ALTER PLUGGABLE DATABASE ALL OPEN;
	```

See Also:

[Making Database Connections with RMAN](starting-interacting-with-rman-client.md)

#### 17.5.3 Performing Complete Recovery of Application PDBs

Use the `RESTORE` and `RECOVER` commands to perform complete recovery of one or more application PDBs.

The `COMPATIBLE` parameter for the CDB must be set to 12.2 or higher.

To perform complete recovery of an application PDB:

1. Start RMAN and establish one of the following types of connections:
	- Connect to the application root as an application common user with the `SYSDBA` or `SYSBACKUP` privilege.
		The application root has its own service name and you can connect to the application root in the same way that you connect to a PDB.
	- Connect to the CDB root as a common user with the `SYSDBA` or `SYSBACKUP` privilege.
2. Close the application PDB for which complete recovery is required.
	The following command closes the application PDB called `hr_appcont_pdb1`:
	```
	ALTER PLUGGABLE DATABASE hr_appcont_pdb1 CLOSE;
	```
3. (Optional) Use the `CONFIGURE` command to configure the default device type and automatic channels.
4. Restore and recover the application PDB.
	The following commands perform complete recovery of an application PDB called `hr_appcont_pdb1`
	```
	RESTORE PLUGGABLE DATABASE hr_appcont_pdb1;
	RECOVER PLUGGABLE DATABASE hr_appcont_pdb1;
	```
5. Examine the output to see if media recovery was successful. If so, proceed to the next step.
6. The following commands opens the application PDB called `hr_appcont_pdb1`:
	```
	ALTER PLUGGABLE DATABASE hr_appcont_pdb1 OPEN;
	```

See Also:

[Making Database Connections with RMAN](starting-interacting-with-rman-client.md)

### 17.6 Performing Complete Recovery of Sparse Databases with RMAN

You can recover sparse databases to the most recent point in time using the `RESTORE` and `RECOVER` commands.

Note:

The base (read-only) data files in a sparse database are not encrypted. Ensure that the base data files are stored in a protected storage and accessed using secured communications.

#### 17.6.1 Performing Complete Recovery of a Sparse CDB

Performing complete recovery of a CDB containing is very similar to performing the complete recovery of a database.

RMAN first restores the logical data that was backed up from the delta storage space of the database and then recovers the database by reading from the redo log and applying the logical data file blocks. You can perform either complete recovery or point-in-time recovery of a sparse database, tablespace, or data file.

To recover a sparse CDB:

1. Complete the preparation steps required for your scenario, as described in " Preparing for Complete Database Recovery ".
2. Start RMAN and connect to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege, as described in " [Making Database Connections with RMAN](starting-interacting-with-rman-client.md) ".
3. If the CDB is not mounted, then mount but do not open the CDB.
	For example, enter the following command:
	```
	STARTUP MOUNT;
	```
4. Use the `SHOW` command to see which channels are preconfigured.
	If the necessary devices and channels are configured, then no action is necessary. Otherwise, you can use the `CONFIGURE` command to configure automatic channels, or include `ALLOCATE CHANNEL` commands within a `RUN` block.
5. Restore and recover the sparse CDB. The following commands perform complete recovery of a sparse CDB:
	```
	RESTORE FROM SPARSE DATABASE;
	RECOVER DATABASE;
	```
6. To recover a specific tablespace containing sparse data files, use the `RESTORE` and `RECOVER` commands for the tablespace.
	The following example restores and recovers the tablespace `MY_TBS`
	```
	RESTORE FROM SPARSE TABLESPACE MY_TBS;
	RECOVER TABLESPACE MY_TBS;
	```

#### 17.6.2 Performing Recovery of a Sparse PDB with RMAN

You can recover a sparse PDB while you are connected at the root level or at the CDB level.

To recover one or more sparse PDBs while connected to the root:

1. Complete the preparation steps required for your recovery scenario, as described in " Preparing for Complete Database Recovery ".
2. Start RMAN and connect to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege, as described in " [Making Database Connections with RMAN](starting-interacting-with-rman-client.md) ".
3. Close the PDBs that you want to recover.
	```
	ALTER PLUGGABLE DATABASE sales, hr CLOSE;
	```
	If any data files are missing, an error occurs and you cannot close a PDB. You must then connect to the PDB to which the missing data file belongs, take the missing data file offline, and then close the PDB.
	The following command takes the data file 12 offline:
	```
	ALTER PLUGGABLE DATABASE DATAFILE 12 OFFLINE;
	```
	Note:
	If the data files that store the `SYSTEM` tablespace of a PDB are missing, then follow the recovery steps described in " Performing Complete Recovery of Tablespaces or Data Files in a PDB with RMAN ".
4. (Optional) Use the `CONFIGURE` command to configure the default device type and automatic channels.
5. Run the `RESTORE` and `RECOVER` commands for the pluggable database.
	The following example performs complete recovery of the PDB `HR_PDB` when connected to the root:
	```
	RESTORE FROM SPARSE PLUGGABLE DATABASE HR_PDB;
	RECOVER PLUGGABLE DATABASE HR_PDB;
	```

To connect to and recover one sparse PDB:

1. Complete the preparation steps required for your recovery scenario, as described in " Preparing for Complete Database Recovery ".
2. Start RMAN and connect to the PDB as a [local user](glossary.md) with the `SYSDBA` or `SYSBACKUP` system privilege, as described in " [Making Database Connections with RMAN](starting-interacting-with-rman-client.md) ".
3. ```
	ALTER PLUGGABLE DATABASE CLOSE;
	```
	If any data files are missing, an error occurs and you cannot close the PDB. You must take the missing data file offline and then close the PDB.
	The following command takes the data file 12 offline:
	```
	ALTER DATABASE DATAFILE 12 OFFLINE;
	```
	Note:
	If the data files that store the `SYSTEM` tablespace of a PDB are missing, then follow the recovery steps described in " Performing Complete Recovery of Tablespaces or Data Files in a PDB with RMAN ".
4. (Optional) Use the `CONFIGURE` command to configure the default device type and automatic channels.
5. Issue the `RESTORE` and `RECOVER` commands.
	The following example restores and recovers the PDB `USERS_PDB`
	```
	RESTORE FROM SPARSE DATABASE FROM USERS_PDB;
	RECOVER DATABASE USERS_PDB;
	```
	.