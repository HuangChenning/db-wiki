---
title: Performing Complete Database Recovery
book: "Backup and Recovery User's Guide"
doc_id: E10642-08
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmcomre.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-users-guide
---

## 17 Performing Complete Database Recovery

This chapter explains how to use RMAN to return your database to normal operation after the loss of one or more data files. This chapter contains the following topics:

## Overview of Complete Database Recovery

This section explains the purpose of complete restore and recovery of the database and specifies the scope of the chapter.

### Purpose of Complete Database Recovery

This chapter assumes that some or all of your data files are lost or damaged. Typically, this situation is caused by a media failure or accidental deletion. Your goal is to return the database to normal operation by restoring the damaged files from RMAN backups and recovering all database changes.

### Scope of This Chapter

This chapter explains how to use complete recovery to fix the most common database problems. This chapter makes the following assumptions:

- You have lost some or all data files and your goal is to recover all changes, but you have not lost all current control files or an entire online redo log group.
	[Chapter 18, "Performing Flashback and Database Point-in-Time Recovery"](rcmflash.md) explains how to recover some but not all database changes. [Chapter 30, "Performing User-Managed Recovery: Advanced Scenarios"](osadvsce.md) explains how to respond when some but not all current control files or members of an online redo log group are lost. ["Performing Recovery with a Backup Control File"](rcmadvre.md) explains how to recover the database when all control files are lost.
- Your database is using the current server parameter file.
	To restore a backup server parameter file, see ["Restoring the Server Parameter File"](rcmadvre.md).
- You have the complete set of archived redo logs and incremental backups needed for recovery of your data file backups. Every data file either has a backup, or a complete set of online and archived redo logs goes back to the creation of a data file with no backup.
	RMAN can handle lost data files without user intervention during restore and recovery. When a data file is lost, the possible cases can be classified as follows:
	- The control file knows about the data file, that is, you backed up the control file after data file creation, but the data file itself is not backed up. If the data file record is in the control file, then `RESTORE` creates the data file in the original location or in a user-specified location. The `RECOVER` command can then apply the necessary logs to the data file.
		- The control file does not have the data file record, that is, you did not back up the control file after data file creation. During recovery, the database detects the missing data file and reports it to RMAN, which creates a new data file and continues recovery by applying the remaining logs. If the data file was created in a parent incarnation, then it is created during the restore or recovery phase as appropriate.
- You are not restoring and recovering an encrypted tablespace.
	If you perform media recovery on an encrypted tablespace, then the Oracle wallet must be open when performing media recovery of this tablespace. See [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/tspaces.htm#ADMIN12327) to learn about encrypted tablespaces.
- Your database runs in a single-instance configuration.
	While RMAN can restore and recover databases in Oracle RAC and Data Guard configurations, these scenarios are beyond the scope of this manual.
- You are using the RMAN client rather than Oracle Enterprise Manager.
	Enterprise Manager provides access to RMAN through a set of wizards. These wizards lead you through a variety of recovery procedures based on an analysis of your database, your available backups, and your data recovery objectives.
	By using Enterprise Manager, you can perform the simpler restore and recovery scenarios outlined in this chapter. You can also use more sophisticated restore and recovery techniques such as point-in-time recovery and database flashback, which allow for efficient repair of media failures and user errors. Typically, using Enterprise Manager is simpler than using the RMAN command-line client directly.

See Also:

- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/backup.htm#RACAD059) for more information about using RMAN with Oracle RAC
- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/rman.htm#SBYDB04700) for more information about using RMAN with Data Guard
- [Oracle Database 2 Day DBA](https://docs.oracle.com/cd/E11882_01/server.112/e10897/backrest.htm#ADMQS009) for more details on the restore and recovery features of Enterprise Manager

## Preparing for Complete Database Recovery

While RMAN simplifies most database restore and recovery tasks, you must still plan your database restore and recovery strategy based on which database files have been lost and your recovery goal. This section contains the following topics:

- Identifying the Database Files to Restore or Recover
- Determining the DBID of the Database
- Previewing Backups Used in Restore Operations
- Validating Backups Before Restoring Them
- Restoring Archived Redo Logs Needed for Recovery

### Identifying the Database Files to Restore or Recover

The techniques for determining which files require restore or recovery depend upon the type of file that is lost.

#### Identifying a Lost Control File

It is usually obvious when the control file of your database is lost. The database shuts down immediately when any of the multiplexed control files becomes inaccessible. Also, the database reports an error if you try to start it without a valid control file at each location specified in the `CONTROL_FILES` initialization parameter.

Loss of some but not all copies of your control file does not require you to restore a control file from backup. If at least one control file remains intact, then you can either copy an intact copy of the control file over the damaged or missing control file, or update the initialization parameter file so that it does not refer to the damaged or missing control file. After the `CONTROL_FILES` parameter references only present, intact copies of the control file, you can restart your database.

If you restore the control file from backup, then you must perform media recovery of the whole database and then open it with the `OPEN RESETLOGS` option, even if no data files must be restored. This technique is described in ["Performing Recovery with a Backup Control File"](rcmadvre.md).

#### Identifying Datafiles Requiring Media Recovery

When and how to recover depends on the state of the database and the location of its data files.

##### Identifying Datafiles with RMAN

An easy technique for determining which data files are missing is to run a `VALIDATE DATABASE` command, which attempts to read all specified data files. For example, start the RMAN client and run the following commands to validate the database (sample output included).

Example 17-1 BACKUP VALIDATE DATABASE

```
RMAN> VALIDATE DATABASE;

Starting validate at 20-OCT-06
allocated channel: ORA_DISK_1
channel ORA_DISK_1: SID=90 device type=DISK
could not read file header for datafile 7 error reason 4
RMAN-00571: ===========================================================
RMAN-00569: =============== ERROR MESSAGE STACK FOLLOWS ===============
RMAN-00571: ===========================================================
RMAN-03002: failure of backup command at 10/20/2007 13:05:43
RMAN-06056: could not access datafile 7
```

The output in Example 17-1 indicates that data file 7 is inaccessible. You can then run the `REPORT SCHEMA` command to obtain the tablespace name and file name for data file 7 as follows (sample output included):

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

##### Identifying Datafiles with SQL

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
	If `ERROR` is not `NULL`, then the data file header cannot be read and validated. Check for a temporary hardware or operating system problem causing the error. If there is no such problem, you must restore the file or switch to a copy.
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
	To find data file and tablespace names, you can also perform useful joins using the data file number and the `V$DATAFILE` and `V$TABLESPACE` views. For example:
	```
	SELECT r.FILE# AS df#, d.NAME AS df_name, t.NAME AS tbsp_name, 
	       d.STATUS, r.ERROR, r.CHANGE#, r.TIME
	FROM V$RECOVER_FILE r, V$DATAFILE d, V$TABLESPACE t
	WHERE t.TS# = d.TS#
	AND d.FILE# = r.FILE#;
	```
	The `ERROR` column identifies the problem for each file requiring recovery.

See Also:

[Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm) for information about the `V$` views

### Determining the DBID of the Database

In situations requiring the recovery of your server parameter file or control file from autobackup, you must know the DBID. You should record the DBID along with other basic information about your database.

If you do not have a record of the DBID of your database, then you can find it in the following places without opening your database:

- The DBID is used in forming the file name for the control file autobackup. Locate this file, and then refer to ["Configuring the Control File Autobackup Format"](rcmconfb.md) to determine where the DBID appears in the file name.
- If you have any text files that preserve the output from an RMAN session, then the DBID is displayed by the RMAN client when it starts up and connects to your database. Typical output follows:
	```
	% rman TARGET /
	Recovery Manager: Release 11.1.0.6.0 - Production on Wed Jul 11 17:51:30 2007
	 
	Copyright (c) 1982, 2007, Oracle.  All rights reserved.
	 
	connected to target database: PROD (DBID=36508508)
	```

### Previewing Backups Used in Restore Operations

You can apply `RESTORE` `...` `PREVIEW` to any `RESTORE` operation to create a detailed list of every backup to be used in the requested `RESTORE` operation, and the necessary target SCN for recovery after the `RESTORE` operation is complete. This command accesses the RMAN repository to query the backup metadata, but does not actually read the backup files to ensure that they can be restored.

As an alternative to `RESTORE ... PREVIEW`, you can use the `RESTORE ... VALIDATE HEADER` command. In addition to listing the files needed for restore and recovery, the `RESTORE ... VALIDATE HEADER` command validates the backup file headers to determine whether the files on disk or in the media management catalog correspond to the metadata in the RMAN repository.

When planning your restore and recovery operation, use `RESTORE ...` `PREVIEW` or `RESTORE ... VALIDATE HEADER` to ensure that all required backups are available or to identify situations in which you may want to direct RMAN to use or avoid specific backups.

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
	If satisfied with the output, then stop here. If the output indicates that RMAN will request a backup from a tape that you know is temporarily unavailable, then continue with this procedure. If the output indicates that a backup is stored offsite, then skip to "Recalling Offsite Backups".
2. If needed, use the `CHANGE` command to set the backup status of any temporarily unavailable backups to `UNAVAILABLE`.
	["Updating a Backup to Status AVAILABLE or UNAVAILABLE"](rcmmaint.md) explains how to perform this task.
3. Optionally, run `RESTORE` `...` `PREVIEW` again to confirm that the restore does not attempt to use unavailable backups.

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta027.htm#RCMRF132) for details on interpreting `RESTORE` `...` `PREVIEW` output, which is in the same format as the output of the `LIST` command

#### Recalling Offsite Backups

Some media managers provide status information to RMAN about which backups are offsite. An [offsite backup](glossary.md) is stored in a remote location, such as a secure storage facility, and cannot be restored unless the media manager retrieves the media.

Offsite backups are marked as `AVAILABLE` in the RMAN repository even though the media must be retrieved from storage before the backup can be restored. If RMAN attempts to restore a offsite backup, then the restore job fails.

You can use `RESTORE ... PREVIEW` to identify offsite backups. The command output indicates whether backups are stored offsite, as shown by the text at the end of the sample output in Example 17-2.

Example 17-2 RESTORE... PREVIEW Output

```
List of Backup Sets
===================

BS Key  Size       Device Type Elapsed Time Completion Time
------- ---------- ----------- ------------ ---------------
9       2.25M      SBT_TAPE    00:00:00     21-MAY-07
        BP Key: 9   Status: AVAILABLE  Compressed: NO  Tag: TAG20070521T144258
        Handle: 0aii9k7i_1_1   Media: 0aii9k7i_1_1
 
  List of Archived Logs in backup set 9
  Thrd Seq     Low SCN    Low Time  Next SCN   Next Time
  ---- ------- ---------- --------- ---------- ---------
  1    1       392314     21-MAY-07 392541     21-MAY-07
  1    2       392541     21-MAY-07 392545     21-MAY-07
  1    3       392545     21-MAY-07 392548     21-MAY-07
  1    4       392548     21-MAY-07 395066     21-MAY-07
  1    5       395066     21-MAY-07 395095     21-MAY-07
  1    6       395095     21-MAY-07 395355     21-MAY-07
 
List of remote backup files
============================
        Handle: aii9k7i_1_1   Media: 0aii9k7i_1_1
validation succeeded for backup piece
Finished restore at 21-MAY-07
released channel: dev1
```

You can use `RESTORE` `...` `PREVIEW` `RECALL` to instruct the media manager to make offsite backups available.

To recall offsite backups:

1. If backups are stored offsite, then execute a `RESTORE ... PREVIEW` command with the `RECALL` option.
	The following example initiates recall for the offsite archived log backups shown in Example 17-2 (sample output included):
	```
	RESTORE ARCHIVELOG ALL PREVIEW RECALL;
	```
	The following sample output indicates that RMAN initiated a recall:
	```
	List of Backup Sets
	===================
	 
	 
	BS Key  Size       Device Type Elapsed Time Completion Time
	------- ---------- ----------- ------------ ---------------
	9       2.25M      SBT_TAPE    00:00:00     21-MAY-07
	        BP Key: 9   Status: AVAILABLE  Compressed: NO  Tag: TAG20070521T144258
	        Handle: VAULT0aii9k7i_1_1   Media: /tmp,VAULT0aii9k7i_1_1
	 
	  List of Archived Logs in backup set 9
	  Thrd Seq     Low SCN    Low Time  Next SCN   Next Time
	  ---- ------- ---------- --------- ---------- ---------
	  1    1       392314     21-MAY-07 392541     21-MAY-07
	  1    2       392541     21-MAY-07 392545     21-MAY-07
	  1    3       392545     21-MAY-07 392548     21-MAY-07
	  1    4       392548     21-MAY-07 395066     21-MAY-07
	  1    5       395066     21-MAY-07 395095     21-MAY-07
	  1    6       395095     21-MAY-07 395355     21-MAY-07
	 
	Initiated recall for the following list of remote backup files
	==========================================================
	        Handle: VAULT0aii9k7i_1_1   Media: /tmp,VAULT0aii9k7i_1_1
	validation succeeded for backup piece
	Finished restore at 21-MAY-07
	released channel: dev1
	```
2. Run the `RESTORE` `..``.` `PREVIEW` command. If necessary, return to the previous step until no backups needed for the restore are reported as offsite.

### Validating Backups Before Restoring Them

While the procedures in "Previewing Backups Used in Restore Operations" indicate which backups will be restored, they do not verify that the backups are actually usable. You can run RMAN commands to test the availability of usable backups for any `RESTORE` operation, or test the contents of a specific backup for use in `RESTORE` operations. The contents of the backups are actually read and checked for corruption. You have the following validation options:

- `RESTORE` `...` `VALIDATE` tests whether RMAN can restore a specific object from a backup. RMAN chooses which backups to use.
- `VALIDATE BACKUPSET` tests the validity of a backup set that you specify.
	See Also:
	[Chapter 16, "Validating Database Files and Backups"](rcmvalid.md)

### Restoring Archived Redo Logs Needed for Recovery

RMAN restores archived redo log files from backup automatically as needed to perform recovery. You can also restore archived redo logs manually to save the time needed to restore these files later during the `RECOVER` command, or if you want to store the restored archived redo log files in some new location. RMAN also gives you the flexibility of restoring all archive redo log files, the current ones or archive redo log files from a specified previous incarnation of the database.

By default, RMAN restores archived redo logs with names constructed using the `LOG_ARCHIVE_FORMAT` and the highest `LOG_ARCHIVE_DEST_` `n` parameters of the target database. These parameters are combined in a platform-specific fashion to form the name of the restored archived log.

#### Restoring Archived Redo Logs to a New Location

You can override the default location for restored archived redo logs with the `SET` `ARCHIVELOG` `DESTINATION` command. This command manually stages archived logs to different locations while a database restore is occurring. During recovery, RMAN knows where to find the newly restored archived logs; it does not require them to be in the location specified in the initialization parameter file.

To restore archived redo logs to a new location:

1. Start RMAN and connect to a target database.
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
	  # restore and recover datafiles as needed
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

#### Restoring Archived Redo Logs to Multiple Locations

You can specify restore destinations for archived logs multiple times in one [RUN block](glossary.md), to distribute restored logs among several destinations. (You cannot, however specify multiple destinations simultaneously to produce multiple copies of the same log during the restore operation.) You can use this feature to manage disk space used to contain the restored logs.

This example restores 300 archived redo logs from backup, distributing them across the directories `/fs1/tmp`, `/fs2/tmp`, and `/fs3/tmp`:

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
  # restore and recover datafiles as needed
  .
  .
  .
}
```

When you issue a `RECOVER` command, RMAN finds the needed restored archived logs automatically across the destinations to which they were restored, and applies them to the data files.

## Performing Complete Database Recovery

This section assumes that you have already performed the tasks in "Preparing for Complete Database Recovery". This section describes the basic outline of complete database recovery, which is intended to encompass a wide range of different scenarios.

### About Complete Database Recovery

You use the `RESTORE` and `RECOVER` commands to restore and recover the database. During the recovery, RMAN automatically restores backups of any needed archived redo logs. If backups are stored on a media manager, then channels must be configured in advance or a `RUN` block with `ALLOCATE` `CHANNEL` commands must be used to enable access to backups stored there.

If RMAN restores archived redo logs to the fast recovery area during a recovery, then it automatically deletes the restored logs after applying them to the data files. Otherwise, you can use the `DELETE ARCHIVELOG` command to delete restored archived redo logs from disk when they are no longer needed for recovery. For example, you can enter the following command:

```
RECOVER DATABASE DELETE ARCHIVELOG;
```

#### Restoring Datafiles to a Nondefault Location

If you cannot restore data files to their default locations, then you must update the control file to reflect the new locations of the data files. Use the RMAN `SET NEWNAME` command within a `RUN` command to specify the new file name. Afterward, use a `SWITCH` command, which is equivalent to using the SQL statement `ALTER DATABASE RENAME FILE`, to update the names of the data files in the control file. `SWITCH` `DATAFILE` `ALL` updates the control file to reflect the new names for all data files for which a `SET` `NEWNAME` has been issued in a `RUN` command.

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2020.htm#RCMRF159) for `SWITCH` syntax

#### Decryption of Backups

If RMAN is restoring encrypted backups, then RMAN automatically decrypts backup sets when their contents are restored. Transparently encrypted backups require no intervention to restore, as long as the Oracle wallet is open and available.

Password-encrypted backups require the correct password to be entered before they can be restored. You must enter the encryption password with the `SET` `DECRYPTION` command. If restoring from a group of backups that were created with different passwords, then specify all of the required passwords on the `SET` `DECRYPTION` command. RMAN automatically uses the correct password with each backup set.

See Also:

- ["Configuring Backup Encryption"](rcmconfa.md) to learn how to configure transparent backup encryption
- ["Encrypting RMAN Backups"](rcmbckad.md) to learn how to create encrypted backups

### Performing Complete Recovery of the Whole Database

This scenario assumes that database `trgt` has lost most or all of its data files. It also assumes that the database uses a fast recovery area.

After restore and recovery of a whole database, when the database is open, missing temporary tablespaces that were recorded in the control file are re-created with their previous creation size, `AUTOEXTEND`, and `MAXSIZE` attributes. Only temporary tablespaces that are missing are re-created. If a temp file exists at the location recorded in the RMAN repository but has an invalid header, then RMAN does not re-create the temp file.

If the temp files were created as Oracle managed files, then they are re-created in the current `DB_CREATE_FILE_DEST` location. Otherwise, they are re-created at their previous locations. If RMAN cannot re-create the file due to an I/O error or some other cause, then the error is reported in the alert log and the database open operation continues.

To restore and recover the whole database:

1. Start RMAN and connect to a target database.
	For example, enter the following command:
	```
	% rman
	RMAN> CONNECT TARGET /
	```
	RMAN displays the database status when it connects: `not started`, `not mounted`, `not open` (when the database is mounted but not open), or none (when the database is open).
2. If the database is not mounted, then mount but do not open the database.
	For example, enter the following command:
	```
	STARTUP MOUNT;
	```
3. Use the `SHOW` command to see which channels are preconfigured.
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
	CONFIGURE CHANNEL DEVICE TYPE 'SBT_TAPE' PARMS "SBT_LIBRARY=/usr/local/oracle/backup/lib/libobk.so";
	```
	If the necessary devices and channels are already configured, then no action is necessary. Otherwise, you can use the `CONFIGURE` command to configure automatic channels, or include `ALLOCATE CHANNEL` commands within a `RUN` block.
4. If restoring password-protected encrypted backups, then specify the password.
	Use the `SET DECRYPTION IDENTIFIED BY` command to specify a password for password-protected backups, as shown in the following example (where password represents the actual password that you enter):
	```
	SET DECRYPTION IDENTIFIED BY password;
	```
	If you created backups with different passwords, then you can run the `SET DECRYPTION IDENTIFIED BY` `password` command multiple times, specifying all of the possible passwords that might be required to restore the backups.
5. Restore and recover the database. Do one of the following:
	- If you are restoring all data files to their original locations, then execute `RESTORE DATABASE` and `RECOVER DATABASE` sequentially at the RMAN prompt.
		For example, enter the following commands if automatic channels are configured (sample output included):
		```
		RMAN> RESTORE DATABASE;
		Starting restore at 20-JUN-06
		allocated channel: ORA_DISK_1
		channel ORA_DISK_1: SID=35 device type=DISK
		allocated channel: ORA_SBT_TAPE_1
		channel ORA_SBT_TAPE_1: SID=34 device type=SBT_TAPE
		channel ORA_SBT_TAPE_1: Oracle Secure Backup
		 
		channel ORA_DISK_1: starting datafile backup set restore
		channel ORA_DISK_1: specifying datafile(s) to restore from backup set
		channel ORA_DISK_1: restoring datafile 00001 to /disk1/oracle/dbs/tbs_01.f
		channel ORA_DISK_1: restoring datafile 00002 to /disk1/oracle/dbs/tbs_ax1.f
		.
		.
		.
		Finished restore at 20-JUN-06
		```
		```
		RMAN> RECOVER DATABASE;
		Starting recover at 20-JUN-06
		using channel ORA_DISK_1
		allocated channel: ORA_SBT_TAPE_1
		channel ORA_SBT_TAPE_1: SID=34 device type=SBT_TAPE
		channel ORA_SBT_TAPE_1: Oracle Secure Backup
		 
		starting media recovery
		 
		channel ORA_DISK_1: starting archived log restore to default destination
		channel ORA_DISK_1: restoring archived log
		archived log thread=1 sequence=5
		channel ORA_DISK_1: restoring archived log
		archived log thread=1 sequence=6
		.
		.
		.
		channel ORA_DISK_1: reading from backup piece /disk1/oracle/work/orcva/TKRM/backupset/2007_06_20/o1_mf_annnn_TAG20070620T113128_29jhr197_.bkp
		channel ORA_DISK_1: piece handle=/disk1/oracle/work/orcva/TKRM/backupset/2007_06_20/o1_mf_annnn_TAG20070620T113128_29jhr197_.bkp tag=TAG20070620T113128
		channel ORA_DISK_1: restored backup piece 1
		channel ORA_DISK_1: restore complete, elapsed time: 00:00:02
		archived log file name=/disk1/oracle/work/orcva/TKRM/archivelog/2007_06_20/o1_mf_1_5_29jhv47k_.arc thread=1 sequence=5
		channel default: deleting archived log(s)
		.
		.
		.
		media recovery complete, elapsed time: 00:00:15
		Finished recover at 20-JUN-06
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
		- If you are restoring some data files to new locations, then execute `RESTORE DATABASE` and `RECOVER DATABASE` sequentially in a `RUN` command. Use the `SET NEWNAME` to rename data files, as described in "Restoring Datafiles to a Nondefault Location".
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

### Performing Complete Recovery of a Tablespace

In the basic scenario, the database is open, and some but not all of the data files are damaged. You want to restore and recover the damaged tablespace while leaving the database open so that the rest of the database remains available. This scenario assumes that database `trgt` has lost tablespace `users`.

To restore and recover a tablespace:

1. Start RMAN and connect to a target database.
2. If the database is open, then take the data file requiring recovery offline.
	For example, enter the following command to take `users` offline:
	```
	SQL "ALTER TABLESPACE users OFFLINE IMMEDIATE";
	```
3. Use the `SHOW` command to see which channels are preconfigured.
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
	CONFIGURE CHANNEL DEVICE TYPE 'SBT_TAPE' PARMS  "SBT_LIBRARY=/usr/local/oracle/backup/lib/libobk.so";
	```
	If the necessary devices and channels are already configured, then no action is necessary. Otherwise, you can use the `CONFIGURE` command to configure automatic channels, or include `ALLOCATE CHANNEL` commands within a `RUN` block.
4. If restoring password-protected encrypted backups, then specify the password.
	Use the `SET DECRYPTION IDENTIFIED BY` command to specify a password for password-protected backups, as shown in the following example (where password represents the actual password that you enter):
	```
	SET DECRYPTION IDENTIFIED BY password;
	```
5. Restore and recover the tablespace. Do one of the following:
	- If you are restoring data files to their original locations, then run the `RESTORE TABLESPACE` and `RECOVER TABLESPACE` commands at the RMAN prompt.
		For example, enter the following command if automatic channels are configured (sample output included):
		```
		RMAN> RESTORE TABLESPACE users;
		 
		Starting restore at 20-JUN-06
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
		channel ORA_DISK_1: reading from backup piece /disk1/oracle/work/orcva/TKRM/backupset/2007_06_20/o1_mf_nnndf_TAG20070620T105435_29jflwor_.bkp
		channel ORA_DISK_1: piece handle=/disk1/oracle/work/orcva/TKRM/backupset/2007_06_20/o1_mf_nnndf_TAG20070620T105435_29jflwor_.bkp tag=TAG20070620T105435
		channel ORA_DISK_1: restored backup piece 1
		channel ORA_DISK_1: restore complete, elapsed time: 00:00:01
		Finished restore at 20-JUN-06
		```
		```
		RMAN> RECOVER TABLESPACE users;
		 
		Starting recover at 20-JUN-06
		using channel ORA_DISK_1
		using channel ORA_SBT_TAPE_1
		 
		starting media recovery
		 
		archived log for thread 1 with sequence 27 is already on disk as file /disk1/oracle/work/orcva/TKRM/archivelog/2007_06_20/o1_mf_1_27_29jjmtc9_.arc
		archived log for thread 1 with sequence 28 is already on disk as file /disk1/oracle/work/orcva/TKRM/archivelog/2007_06_20/o1_mf_1_28_29jjnc5x_.arc
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
		channel ORA_DISK_1: reading from backup piece /disk1/oracle/work/orcva/TKRM/backupset/2007_06_20/o1_mf_annnn_TAG20070620T113128_29jhr197_.bkp
		channel ORA_DISK_1: piece handle=/disk1/oracle/work/orcva/TKRM/backupset/2007_06_20/o1_mf_annnn_TAG20070620T113128_29jhr197_.bkp tag=TAG20070620T113128
		channel ORA_DISK_1: restored backup piece 1
		channel ORA_DISK_1: restore complete, elapsed time: 00:00:02
		archived log file name=/disk1/oracle/work/orcva/TKRM/archivelog/2007_06_20/o1_mf_1_5_29jkdvjq_.arc thread=1 sequence=5
		channel default: deleting archived log(s)
		archived log file name=/disk1/oracle/work/orcva/TKRM/archivelog/2007_06_20/o1_mf_1_5_29jkdvjq_.arc RECID=91 STAMP=593611179
		archived log file name=/disk1/oracle/work/orcva/TKRM/archivelog/2007_06_20/o1_mf_1_6_29jkdvbz_.arc thread=1 sequence=6
		channel default: deleting archived log(s)
		.
		.
		.
		media recovery complete, elapsed time: 00:00:01
		Finished recover at 20-JUN-06
		```
		- If you are restoring some data files to new locations, then execute `RESTORE TABLESPACE` and `RECOVER TABLESPACE` in a `RUN` command. Use the `SET NEWNAME` to rename data files, as described in "Restoring Datafiles to a Nondefault Location".
		The following example restores the data files in tablespaces `users` to a new location, then performs recovery. Assume that the old data files were stored in the `/disk1` path and the new ones are stored in the `/disk2` path.
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
	SQL "ALTER TABLESPACE users ONLINE";
	```

### Performing Complete Recovery After Switching to a Copy

If you have image copies of the inaccessible data files in the fast recovery area, then you can use the `SWITCH DATAFILE ... TO COPY` command to point the control file at the data file copy and then use `RECOVER` to recover lost changes. You can also use the SWITCH DATABASE TO COPY command to point the control file at a copy of the whole database. Because you do not need to restore backups, this recovery technique takes less time than traditional restore and recovery.

Note:

A `SWITCH TABLESPACE ... TO COPY` command is also supported for cases when all data files in a tablespace are lost and copies of all data files exist. The same restriction exists for `SWITCH DATABASE TO COPY`.

#### Switching to a Data File Copy

In the basic scenario, the database is open, and some but not all of the data files are damaged. During the course of the day, a data file goes missing due to storage failure. You must repair this file, but cannot afford the time to do a restore and recovery from a backup. You decide to use a recent image copy backup as the new file, thus eliminating restore time. This scenario assumes that database `trgt` has lost data file `4`.

To switch to a data file copy and perform recovery:

1. Start RMAN and connect to a target database.
2. If the database is open, then take the tablespace requiring recovery offline.
	Enter the following command to take data file `4` offline:
	```
	SQL "ALTER DATABASE DATAFILE 4 OFFLINE";
	```
3. Switch the offline data file to the latest copy.
	Enter the following command to point the control file to the latest image copy of data file `4`:
	```
	SWITCH DATAFILE 4 TO COPY;
	```
4. Recover the data file with the `RECOVER DATAFILE` command.
	Enter the following command:
	```
	RECOVER DATAFILE 4;
	```
	RMAN automatically restores archived redo logs and incremental backups. Because the database uses a fast recovery area, RMAN automatically deletes them after they have been applied.
5. Examine the output to see if recovery was successful. If so, bring the recovered data file back online.
	Enter the following command to bring data file `4` online:
	```
	SQL "ALTER DATABASE DATAFILE 4 ONLINE";
	```

#### Switching to a Database Copy

In this scenario, the database is shut down, and all of the data files are damaged. You have image copies of all the damaged data files. You decide to use the existing image copies as the new data files, thus eliminating restore time.

To switch to a database copy and perform recovery:

1. Start RMAN and connect to a target database.
2. Mount the database.
3. Switch the database to the latest copy.
	Enter the following command to point the control file to the latest image copy of the database:
	```
	SWITCH DATABASE TO COPY;
	```
4. Recover the database with the `RECOVER DATABASE` command.
	Enter the following command:
	```
	RECOVER DATABASE;
	```
	RMAN automatically restores archived redo logs and incremental backups. Because the database uses a fast recovery area, RMAN automatically deletes them after they have been applied.
5. Examine the output to see if recovery was successful. If so, open the database.
	Enter the following command to open the database:
	```
	ALTER DATABASE OPEN;
	```