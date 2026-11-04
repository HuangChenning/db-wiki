---
title: "Performing RMAN Recovery: Advanced Scenarios"
book: "Backup and Recovery User's Guide"
doc_id: E10642-08
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmadvre.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-users-guide
---

## 20 Performing RMAN Recovery: Advanced Scenarios

The preceding chapters in [Part V, "Diagnosing and Responding to Failures"](part_dia.md) cover the most basic recovery scenarios and are intended to be as generic as possible. The scenarios in this chapter are less common or are more complicated than the basic scenarios.

This chapter contains the following topics:

## Recovering a NOARCHIVELOG Database with Incremental Backups

Restoring a database running in `NOARCHIVELOG` mode is similar to restoring a database in `ARCHIVELOG` mode. The main differences are:

- Only consistent backups can be used in restoring a database in `NOARCHIVELOG` mode.
- Media recovery is not possible because no archived redo logs exist.

You can perform limited recovery of changes to a database running in `NOARCHIVELOG` mode by applying incremental backups. The incremental backups must be consistent, like all backups of a database run in `NOARCHIVELOG` mode, so you cannot make backups of the database when it is open.

When you are recovering a `NOARCHIVELOG` database, specify the `NOREDO` option on the `RECOVER` command to indicate that RMAN should not attempt to apply archived redo logs. Otherwise, RMAN returns an error.

To recover a NOARCHIVELOG database with incremental backups:

1. After connecting to the target database and the recovery catalog, place the database in a mounted state:
	```
	STARTUP FORCE MOUNT
	```
2. Restore and recover the database.
	For example, you can perform incomplete recovery with the following commands:
	```
	RESTORE DATABASE 
	  FROM TAG "consistent_whole_backup";
	RECOVER DATABASE NOREDO;
	```
3. Open the database with the `RESETLOGS` option.
	For example, enter the following command:
	```
	ALTER DATABASE OPEN RESETLOGS;
	```

## Restoring the Server Parameter File

If you lose the server parameter file, then RMAN can restore it to its default location or to a location of your choice. Unlike the loss of the control file, the loss of the server parameter file does not cause the instance to immediately stop. The instance may continue operating, although you must shut it down and restart it after restoring the server parameter file.

Note the following considerations when restoring the server parameter file:

- If the instance is already started with the server parameter file, then you cannot overwrite the existing server parameter file.
- When the instance is started with a client-side initialization parameter file, RMAN restores the server parameter file to the default location if the `TO` clause is not used in the restore command. The default location is platform-specific, for example, `?``/dbs/spfile.ora` on Linux.
- A recovery catalog simplifies the recovery procedure because you can avoid recording and remembering the DBID. This procedure assumes that you are not using a recovery catalog.

To restore the server parameter file from autobackup:

1. Start RMAN and do one of the following:
	- If the database instance is started at the time of the loss of the server parameter file, then connect to the target database.
		- If the database instance is not started when the server parameter file is lost, and if you are not using a recovery catalog, then run the `SET DBID` command to set the DBID of the target database. See ["Determining the DBID of the Database"](rcmcomre.md) for details on determining the DBID.
2. Shut down the database instance and restart it without mounting the database.
	When the server parameter file is not available, RMAN starts the instance with a dummy parameter file. For example, enter the following command:
	```
	STARTUP FORCE NOMOUNT;
	```
3. Execute a `RUN` command to restore the server parameter file.
	Depending on the situation, you may need to execute multiple commands in the `RUN` command. Note the following considerations:
	- If restoring from tape, then use `ALLOCATE CHANNEL` to allocate an SBT channel manually. If restoring from disk, then RMAN uses the default disk channel.
		- If the autobackups were not produced with the default format (`%F`), then use the `SET CONTROLFILE AUTOBACKUP FOR DEVICE TYPE` command to specify the format in effect when the autobackup was performed.
		- If the most recent autobackup was not created today, then use `SET UNTIL` to specify the date from which to start the search.
		- If RMAN is not connected to a recovery catalog, then use `SET DBID` to set the DBID for the target database.
		- To restore the server parameter file to a nondefault location, specify the `TO` clause or `TO PFILE` clause on the `RESTORE SPFILE` command.
		- If you know that RMAN never produces more than n autobackups each day, then you can set the `RESTORE SPFILE FROM AUTOBACKUP ... MAXSEQ` parameter to n to reduce the search time. `MAXSEQ` is set to 255 by default, and `RESTORE` counts backward from `MAXSEQ` to find the last backup of the day. To terminate the restore operation if you do not find the autobackup in the current day (or specified day), set `MAXDAYS 1` on the `RESTORE` command.
	The following example illustrates a `RUN` command that restores a server parameter file from an autobackup on tape:
	```
	RUN 
	{
	  ALLOCATE CHANNEL c1 DEVICE TYPE sbt PARMS ...;
	  SET UNTIL TIME 'SYSDATE-7';
	  SET CONTROLFILE AUTOBACKUP FORMAT 
	    FOR DEVICE TYPE sbt TO '/disk1/control_files/autobackup_%F';
	  SET DBID 123456789;
	  RESTORE SPFILE
	    TO '/tmp/spfileTEMP.ora'
	    FROM AUTOBACKUP MAXDAYS 10;
	}
	```
4. Restart the database instance with the restored file.
	If you are restarting RMAN with a server parameter file in a nondefault location, then create an initialization parameter file with the line `SPFILE=` `new_location`, where `new_location` is the path name of the restored server parameter file. Then, restart the instance with the client-side initialization parameter file.
	For example, create a file `/tmp/init.ora` which contains the single line:
	```
	SPFILE=/tmp/spfileTEMP.ora
	```
	You can use the following RMAN command to restart the instance with the restored server parameter file:
	```
	STARTUP FORCE PFILE=/tmp/init.ora;
	```

### Restoring the Server Parameter File from a Control File Autobackup

If you have configured control file autobackups, then the server parameter file is backed up with the control file whenever an autobackup is taken.

To restore the server parameter file from the control file autobackup, you must first set the DBID for your database and then use the `RESTORE SPFILE FROM AUTOBACKUP` command. If the autobackup is in a nondefault format, then first use the `SET CONTROLFILE AUTOBACKUP FORMAT` command to specify the format.

Example 20-1 sets the DBID and restores the server parameter file from a control file autobackup in a nondefault location.

Example 20-1 Restoring the Server Parameter File from a Control File Autobackup

```
SET DBID 320066378;
RUN 
{
  SET CONTROLFILE AUTOBACKUP FORMAT 
    FOR DEVICE TYPE DISK TO 'autobackup_format';
  RESTORE SPFILE FROM AUTOBACKUP;
}
```

RMAN uses the autobackup format and DBID to hunt for control file autobackups. If a control file autobackup is found, then RMAN restores the server parameter file from that backup to its default location.

To learn how to determine the correct value for `autobackup_format`, see the description of `CONFIGURE CONTROLFILE AUTOBACKUP FORMAT` in the entry for the `CONFIGURE` command in [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta010.htm#RCMRF113).

See Also:

["Determining the DBID of the Database"](rcmcomre.md) for details on how to determine the DBID

### Creating an Initialization Parameter File with RMAN

You can also restore the server parameter file as a client-side initialization parameter file with the `TO` `PFILE` `'filename'` clause. The file name that you specify should be on a file system accessible from the host where the RMAN client is running. This file need not be accessible directly from the host running the instance.

The following RMAN command creates an initialization parameter file named `/tmp/initTEMP.ora` on the system running the RMAN client:

```
RESTORE SPFILE TO PFILE '/tmp/initTEMP.ora';
```

To restart the instance with the initialization parameter file, use the following command, again running RMAN on the same client host:

```
STARTUP FORCE PFILE='/tmp/initTEMP.ora';
```

## Performing Recovery with a Backup Control File

This section explains what to do when all current control files are lost and you must restore a backup control file.

### About Recovery with a Backup Control File

If all copies of the current control file are lost or damaged, then you must restore and mount a backup control file. You must then run the `RECOVER` command, even if no data files have been restored, and open the database with the `RESETLOGS` option. If some copies of the current control file are usable, however, then you can follow the procedure in ["Responding to the Loss of a Subset of the Current Control Files"](osadvsce.md) and avoid the recovery and `RESETLOGS` operation.

During recovery, RMAN automatically searches for online and archived logs that are not recorded in the RMAN repository and catalogs any that it finds. RMAN attempts to find a valid archived redo log in any current archiving destination with the current log format. The current format is specified in the initialization parameter file used to start the instance (or all instances in an Oracle RAC configuration). Similarly, RMAN attempts to find the online redo logs by using the file names listed in the control file.

If you changed the archiving destination or format during recovery, or if you added new online log members after the backup of the control file, then RMAN may not be able to automatically catalog a needed online or archived log. Whenever RMAN cannot find online redo logs and you did not specify an `UNTIL` time, RMAN reports errors similar to the following:

```
RMAN-00571: ===========================================================
RMAN-00569: =============== ERROR MESSAGE STACK FOLLOWS ===============
RMAN-00571: ===========================================================
RMAN-03002: failure of recover command at 08/29/2007 14:23:09
RMAN-06054: media recovery requesting unknown log: thread 1 scn 86945
```

In this case, you must use the `CATALOG` command to manually add the required redo logs to the repository so that recovery can proceed.

See Also:

The discussion of `RESTORE CONTROLFILE` in [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2008.htm#RCMRF149) for more details about restrictions on using `RESTORE CONTROLFILE` in different scenarios (such as when using a recovery catalog, or restoring from a specific backup)

#### Control File Locations

When you are restoring the control file, the default destination is all of the locations defined in the `CONTROL_FILES` initialization parameter. If you do not set the `CONTROL_FILES` initialization parameter, then the database uses the same rules to determine the destination for the restored control file that it uses when creating a control file if the `CONTROL_FILES` parameter is not set. These rules are described in [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_5003.htm#SQLRF01203) in the description of the `CREATE CONTROLFILE` statement.

One way to restore the control file to one or more new locations is to change the `CONTROL_FILES` initialization parameter, and then use the `RESTORE CONTROLFILE` command with no arguments to restore the control file to the default locations. For example, if you are restoring your control file after a disk failure made some but not all `CONTROL_FILES` locations unusable, you can change `CONTROL_FILES` to replace references to the failed disk with path names pointing to another disk, and then run `RESTORE CONTROLFILE` with no arguments.

You can also restore the control file to any location that you choose other than the `CONTROL_FILES` locations, by using the form `RESTORE CONTROLFILE TO` 'filename':

```
RESTORE CONTROLFILE TO '/tmp/my_controlfile';
```

You can perform this operation with the database in `NOMOUNT`, `MOUNT`, or `OPEN` states, because you are not overwriting any of the control files currently in use. Any existing file named `'` `filename` `'` is overwritten. After restoring the control file to a new location, you can then update the `CONTROL_FILES` initialization parameter to include the new location.

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2008.htm#RCMRF149) for `RESTORE CONTROLFILE` syntax

#### Recovery With and Without a Recovery Catalog

When RMAN is connected to a recovery catalog, the recovery procedure with a backup control file is identical to recovery with a current control file. The RMAN metadata missing from the backup control file is available from the recovery catalog. The only exception is if the database name is not unique in the catalog, in which case you must use `SET DBID` command before restoring the control file.

If you are not using a recovery catalog, then you must restore your control file from an autobackup. To restore the control file from autobackup, the database must be in a `NOMOUNT` state. As shown in Example 20-2, you must first set the DBID for your database, and then use the `RESTORE CONTROLFILE FROM AUTOBACKUP` command.

Example 20-2 Setting the DBID and Restoring the Control File from Autobackup

```
SET DBID 320066378;
RUN
{
  SET CONTROLFILE AUTOBACKUP FORMAT 
    FOR DEVICE TYPE DISK TO 'autobackup_format';
  RESTORE CONTROLFILE FROM AUTOBACKUP;
}
```

RMAN uses the autobackup format and DBID to determine where to hunt for the control file autobackup. If one is found, RMAN restores the control file to all control file locations listed in the `CONTROL_FILES` initialization parameter.

See Also:

- The description of `CONFIGURE CONTROLFILE AUTOBACKUP FORMAT` in the entry for `CONFIGURE` in [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta010.htm#RCMRF113) to learn how to determine the correct value for the autobackup format.
- See ["Determining the DBID of the Database"](rcmcomre.md) to learn how to determine your DBID.

#### Recovery When Using a Fast Recovery Area

The commands for restoring a control file are the same whether or not the database uses a fast recovery area. If the database uses a recovery area, then RMAN updates a control file restored from backup by crosschecking all disk-based backups and image copies recorded in the control file. RMAN catalogs any backups in the recovery area that are not recorded. As a result, the restored control file has a complete and accurate record of all backups in the recovery area and any other backups known to the control file at the time of the backup.

RMAN does not automatically crosscheck tape backups after restoring a control file. If you are using tape backups, then you can restore and mount the control file, and optionally crosscheck the backups on tape, as shown in the following example:

```
CROSSCHECK BACKUP DEVICE TYPE sbt;
```

### Performing Recovery with a Backup Control File and No Recovery Catalog

This section assumes that you have RMAN backups of the control file, but do not use a recovery catalog. It also assumes that you enabled the control file autobackup feature for the target database and can restore an autobackup of the control file.

Because the autobackup uses a well-known format, RMAN can restore it even though it does not have a repository available that lists the available backups. You can restore the autobackup to the default or a new location. RMAN replicates the control file to all `CONTROL_FILES` locations automatically.

Note:

If you know the backup piece name that contains the control file (for example, from the media manager or because the piece is on disk), then you can specify the piece name using the `RESTORE` `CONTROLFILE` `FROM` `'filename'` command. The database records the location of every autobackup in the alert log.

Because you are not connected to a recovery catalog, the RMAN repository contains only information about available backups at the time of the control file backup. If you know the location of other usable backup sets or image copies, then add them to the control file RMAN repository with the `CATALOG` command.

To recover the database with a control file autobackup in NOCATALOG mode:

1. Start RMAN and connect to a target database.
2. Start the target database instance without mounting the database. For example:
	```
	STARTUP NOMOUNT;
	```
3. Set the database identifier for the target database with the `SET` `DBID` command.
	RMAN displays the DBID whenever you connect to a target database. You can also obtain it by inspecting saved RMAN log files, querying the catalog, or looking at the file names of control file autobackup. For example, run:
	```
	SET DBID 676549873;
	```
4. Write an RMAN command file to restore the autobackup control file and perform recovery.
	The command file should contain the following steps:
	1. Optionally, specify the most recent backup time stamp that RMAN can use when searching for a control file autobackup to restore.
		2. If you know that a different control file autobackup format was in effect when the control file autobackup was created, then specify a nondefault format for the restore of the control file.
		3. If an [SBT](glossary.md) channel created the control file autobackup, then allocate one or more SBT channels. Because no recovery catalog is available, you cannot use preconfigured channels.
		4. Restore the autobackup of the control file, optionally setting the maximum number of days backward that RMAN can search and the initial sequence number that it should use in its search for the first day.
		5. If you know that the control file contained information about configured channels that are useful in the rest of the restore process, then you can exit RMAN to clear manually allocated channels from Step c.
		If you restart the RMAN client and mount the database, then these configured channels are available for your use. If you do not care about using configured channels from your control file, then you can simply mount the database.
		6. This step depends on whether the online redo logs are available. The option `OPEN RESETLOGS` is always required after recovery with a backup control file, regardless of whether logs are available.
		If the online redo logs are usable, then RMAN can find and apply these logs. Perform a complete restore and recovery as described in ["Performing Complete Database Recovery"](rcmcomre.md).
		If the online redo logs are unusable, then perform DBPITR as described in ["Performing Database Point-in-Time Recovery"](rcmflash.md). An `UNTIL` clause is required to specify a target time, SCN, or log sequence number for the recovery before the first SCN of the online redo logs (otherwise, RMAN issues the `RMAN-6054` error).
		When you perform DBPITR with a backup control file, before opening the database with `RESETLOGS`, you can open the database read-only using SQL\*Plus and run queries as needed to verify that the effects of the logical corruption have been reversed. If you are satisfied with the results, then you can open the database with `RESETLOGS`.
		Note:
		When specifying log sequences, if the last created archived redo log has sequence n, then specify `UNTIL` `SEQUENCE` `n` `+1` so that RMAN applies n and then stops.
	In the following example, the online redo log files have been lost, and the most recent archived redo log sequence number is 13243. This example shows how to restore the control file autobackup and recover through the latest log.
	```
	RUN 
	{
	  # Optionally, set upper limit for eligible time stamps of control file 
	  # backups
	  # SET UNTIL TIME '09/10/2007 13:45:00';
	  # Specify a nondefault autobackup format only if required
	  # SET CONTROLFILE AUTOBACKUP FORMAT FOR DEVICE TYPE DISK 
	  #   TO '?/oradata/%F.bck';
	  ALLOCATE CHANNEL c1 DEVICE TYPE sbt PARMS '...'; # allocate manually
	  RESTORE CONTROLFILE FROM AUTOBACKUP
	    MAXSEQ 100           # start at sequence 100 and count down
	    MAXDAYS 180;         # start at UNTIL TIME and search back 6 months
	  ALTER DATABASE MOUNT DATABASE;
	}
	# Now use automatic channels configured in restored control file
	RESTORE DATABASE UNTIL SEQUENCE 13244;
	RECOVER DATABASE UNTIL SEQUENCE 13244;
	```
5. If recovery was successful, then open the database and reset the online logs:
	```
	ALTER DATABASE OPEN RESETLOGS;
	```

## Performing Disaster Recovery

Disaster recovery includes the restoration and recovery of the target database after the loss of the entire target database, the recovery catalog database, all current control files, all online redo log files, and all parameter files.

### Prerequisites of Disaster Recovery

To perform a disaster recovery, you must have the following:

- Backups of all data files
- All archived redo logs generated after the creation time of the oldest backup that you intend to restore
- At least one control file autobackup
- A record of the DBID of the database

### Recovering the Database After a Disaster

The procedure for disaster recovery is similar to the procedure for recovering the database with a backup control file in `NOCATALOG` mode. If you are restoring the database to a new host, then you should also review the considerations described in "Restoring a Database on a New Host".

This scenario assumes that the Linux server on which your database was running has been damaged beyond repair. Fortunately, you backed up the database to Oracle Secure Backup and have the tapes available. The scenario assumes the following:

- Oracle Database is already installed on the new host.
- You are restoring the database to a new Linux host with the same directory structure as the old host.
- You have one tape drive containing backups of all the data files and archived redo logs through log 1124, and autobackups of the control file and server parameter file.
- You do not use a recovery catalog with the database.

To recover the database on the new host:

1. If possible, restore or re-create all relevant network files such as `tnsnames.ora` and `listener.ora` and a password file.
2. Start RMAN and connect to the target database instance.
	At this stage, no initialization parameter file exists. If you have set `ORACLE_SID` and `ORACLE_HOME`, then you can use operating system authentication to connect as `SYSDBA`. For example, start RMAN as follows:
	```
	% rman
	RMAN> CONNECT TARGET /
	```
3. Specify the DBID for the target database with the `SET` `DBID` command, as described in "Restoring the Server Parameter File".
	For example, enter the following command:
	```
	SET DBID 676549873;
	```
4. Run the `STARTUP` `NOMOUNT` command.
	When the server parameter file is not available, RMAN attempts to start the instance with a dummy server parameter file.
5. Allocate a channel to the media manager and then restore the server parameter file from autobackup.
	For example, enter the following command to restore the server parameter file from Oracle Secure Backup:
	```
	RUN
	{
	  ALLOCATE CHANNEL c1 DEVICE TYPE sbt;
	  RESTORE SPFILE FROM AUTOBACKUP;
	}
	```
6. Restart the instance with the restored server parameter file.
	```
	STARTUP FORCE NOMOUNT;
	```
7. Write a command file to perform the restore and recovery operation, and then execute the command file. The command file should do the following:
	1. Allocate a channel to the media manager.
		2. Restore a control file autobackup (see "Performing Recovery with a Backup Control File and No Recovery Catalog").
		3. Mount the restored control file.
		4. Catalog any backups not recorded in the repository with the `CATALOG` command.
		5. Restore the data files to their original locations. If volume names have changed, then run `SET` `NEWNAME` commands before the restore operation and perform a switch after the restore operation to update the control file with the new locations for the data files, as shown in the following example.
		6. Recover the data files. RMAN stops recovery when it reaches the log sequence number specified.
	```
	RMAN> RUN
	{
	  # Manually allocate a channel to the media manager
	  ALLOCATE CHANNEL t1 DEVICE TYPE sbt;
	  # Restore autobackup of the control file. This example assumes that you have 
	  # accepted the default format for the autobackup name.
	  RESTORE CONTROLFILE FROM AUTOBACKUP;
	  #  The set until command is used in case the database
	  #  structure has changed in the most recent backups, and you want to
	  #  recover to that point in time. In this way RMAN restores the database
	  #  to the same structure that the database had at the specified time.
	  ALTER DATABASE MOUNT;
	  SET UNTIL SEQUENCE 1124 THREAD 1;
	  RESTORE DATABASE;
	  RECOVER DATABASE;
	}
	```
	The following example of the `RUN` command shows the same scenario except with new file names for the restored data files:
	```
	RMAN> RUN
	{
	  #  If you must restore the files to new locations,
	  #  use SET NEWNAME commands:
	  SET NEWNAME FOR DATAFILE 1 TO '/dev/vgd_1_0/rlvt5_500M_1';
	  SET NEWNAME FOR DATAFILE 2 TO '/dev/vgd_1_0/rlvt5_500M_2';
	  SET NEWNAME FOR DATAFILE 3 TO '/dev/vgd_1_0/rlvt5_500M_3';
	  ALLOCATE CHANNEL t1 DEVICE TYPE sbt;
	  RESTORE CONTROLFILE FROM AUTOBACKUP;
	  ALTER DATABASE MOUNT;
	  SET UNTIL SEQUENCE 124 THREAD 1;
	  RESTORE DATABASE;
	  SWITCH DATAFILE ALL; # Update control file with new location of data files.
	  RECOVER DATABASE;
	}
	```
8. If recovery was successful, then open the database and reset the online logs:
	```
	ALTER DATABASE OPEN RESETLOGS;
	```

## Restoring a Database on a New Host

If your goal is to perform a test run of your disaster recovery procedures, or to permanently move a database to a new host, then you can use the procedure in this section. This procedure uses the `RESTORE` and `RECOVER` commands.

If you use the procedure in this section, then the DBID for the restored database equals the DBID for the original database. Do not register a test database created in this way in the same recovery catalog as the source database. Because the DBID of the two databases is the same, the metadata for the test database can interfere with RMAN's ability to restore and recover the source database.

If your goal is to create a new copy of your target database for ongoing use on a new host, then use the RMAN `DUPLICATE` command instead of this procedure. The `DUPLICATE` command assigns a new DBID to the database it creates, enabling it to be registered in the same recovery catalog as the original database.

See Also:

["Overview of RMAN Database Duplication"](rcmdupdb.md) to learn how to duplicate a database

### Preparing to Restore a Database on a New Host

To prepare for the restoration of the database to a new host, take the following steps:

- Record the DBID for your source database. If you do not know the DBID for your database, then see ["Determining the DBID of the Database"](rcmcomre.md) to learn how to determine the DBID.
- Make the source database initialization parameter file accessible on the new host. Copy the file from the old host to a new host by using an operating system utility.
- If you perform a test restore operation only, then ensure that RMAN is not connected to the recovery catalog. Otherwise, RMAN records metadata about the restored data files in the recovery catalog. This metadata interferes with future attempts to restore and recover the primary database.
	If you must use a recovery catalog because the control file is not large enough to contain the RMAN repository data on all of the backups that you must restore, then use Oracle Data Pump to export the catalog and import it into a different schema or database. Afterward, use the copied recovery catalog for the test restore. Otherwise, the recovery catalog considers the restored database as the current target database.
- Ensure that backups used for the restore operation are accessible on the restore host. For example, if the backups were made with a media manager, then verify that the tape device is connected to the new host. If you are using disk copies, then use the procedure in the following section.
- If you are performing a trial restore of the production database, then perform either of the following actions before restoring the database in the test environment:
	- If the test database uses a fast recovery area that is physically different from the recovery area used by the production database, then set `DB_RECOVERY_FILE_DEST` in the test database instance to the new location.
		- If the test database uses a fast recovery area that is physically the same as the recovery area used by the production database, then set `DB_UNIQUE_NAME` in the test database instance to a different name from the production database.
	If you do not perform either of the preceding actions, then RMAN assumes that you are restoring the production database and deletes flashback logs from the fast recovery area because they are considered unusable.

#### Restoring Disk Backups to a New Host

To move the database to a new host by using data file copies or backup sets on disk, you must transfer the files manually to the new host. This example assumes that RMAN is using a recovery catalog.

To restore backup files to a new host:

1. Start RMAN and connect to a target database and recovery catalog.
2. Run a `LIST` command to see a listing of backups of the data file and control file autobackups.
	For example, enter the following command to view data file copies:
	```
	LIST COPY;
	```
	For example, enter the following command to view control file backups:
	```
	LIST BACKUP OF CONTROLFILE;
	```
	The piece name of the autobackup must use the `%F` substitution variable, so the autobackup piece name includes the string `c-IIIIIIIIII-YYYYMMDD-QQ`, where `IIIIIIIIII` stands for the DBID, `YYYYMMDD` is a time stamp in the Gregorian calendar of the day the backup is generated, and `QQ` is the sequence in hexadecimal.
3. Copy the backups to the new host with an operating system utility.
	Enter a command such as the following to copy all data file copies to the `?/oradata/trgt` directory on the new host:
	```
	% cp -r /disk1/*dbf /net/new_host/oracle/oradata/trgt
	```
	Enter a command such as the following to copy the autobackup backup piece to the `/tmp` directory on the new host:
	```
	% cp -r /disk1/auto_bkp_loc/c-1618370911-20070208-00 /net/new_host/tmp
	```
	As explained in "Restoring the Server Parameter File from a Control File Autobackup", you must use the `SET CONTROLFILE AUTOBACKUP FORMAT` command when restoring an autobackup from a nondefault location.

### Testing the Restore of a Database on a New Host

This scenario assumes that you want to test whether you can restore your database to a new host. In this scenario, you have two networked Linux hosts, `hosta` and `hostb`. A target database named `trgta` is on `hosta` and is registered in recovery catalog `catdb`. You want to test the restore and recovery of `trgta` on `hostb`, while keeping database `trgta` up and running on `hosta`.

Now, assume that the directory structure of `hostb` is different from `hosta`. The target database is located in `/net/hosta/dev3/oracle/dbs`, but you want to restore the database to `/net/hostb/oracle/oradata/test`. You have tape backups of data files, control files, archived redo logs, and the server parameter file on a media manager accessible by both hosts. The `ORACLE_SID` for the `trgta` database is `trgta` and does not change for the restored database.

Caution:

If you are restoring the database for test purposes, then never connect RMAN to the test database and the recovery catalog.

To restore the database on a new host:

1. Ensure that the backups of the target database are accessible on the new host.
	To test disaster recovery, you must have a recoverable backup of the target database. When preparing your disaster recovery strategy, ensure that the backups of the data files, control files, and server parameter file are restorable on `hostb`. Thus, you must configure the media management software so that `hostb` is a media manager client and can read the backup sets created on `hosta`. Consult the media management vendor for support on this issue.
2. Configure the `ORACLE_SID` on `hostb`.
	This scenario assumes that you want to start the RMAN client on `hostb` and authenticate yourself through the operating system. However, you must be connected to `hostb` either locally or through a net service name.
	After logging in to `hostb` with administrator privileges, edit the `/etc/group` file so that you are included in the DBA group:
	```
	dba:*:614:<your_user_name>
	```
	Set the `ORACLE_SID` environment variable on `hostb` to the same value used on `hosta`:
	```
	% setenv ORACLE_SID trgta
	```
3. Start RMAN on `hostb` and connect to the target database without connecting to the recovery catalog.
	For example, enter the following command:
	```
	% rman NOCATALOG
	RMAN> CONNECT TARGET /
	```
4. Set the DBID and start the database instance without mounting the database.
	For example, run `SET` `DBID` to set the DBID, then run `STARTUP` `NOMOUNT`:
	```
	SET DBID 1340752057;
	STARTUP NOMOUNT
	```
	RMAN fails to find the server parameter file, which has not yet been restored, but starts the instance with a "dummy" file. Sample output follows:
	```
	startup failed: ORA-01078: failure in processing system parameters
	LRM-00109: could not open parameter file '/net/hostb/oracle/dbs/inittrgta.ora'
	trying to start the Oracle instance without parameter files ...
	Oracle instance started
	```
5. Restore and edit the server parameter file.
	Because you enabled the control file autobackup feature when making your backups, the server parameter file is included in the backup. If you are restoring an autobackup that has a nondefault format, then use the `SET CONTROLFILE AUTOBACKUP FORMAT` command to indicate the format.
	Allocate a channel to the media manager, then restore the server parameter file as a client-side parameter file and use the `SET` command to indicate the location of the autobackup (in this example, the autobackup is in `/tmp`):
	```
	RUN
	{
	  ALLOCATE CHANNEL c1 DEVICE TYPE sbt PARMS '...';
	  SET CONTROLFILE AUTOBACKUP FORMAT FOR DEVICE TYPE DISK TO '/tmp/%F';
	  RESTORE SPFILE 
	    TO PFILE '?/oradata/test/inittrgta.ora' 
	    FROM AUTOBACKUP;
	  SHUTDOWN ABORT;
	}
	```
6. Edit the restored initialization parameter file.
	Change any location-specific parameters, for example, those ending in `_DEST`, to reflect the new directory structure. For example, edit the following parameters:
	```
	- IFILE
	- LOG_ARCHIVE_DEST_1
	- CONTROL_FILES
	```
7. Restart the instance with the edited initialization parameter file.
	For example, enter the following command:
	```
	STARTUP FORCE NOMOUNT PFILE='?/oradata/test/inittrgta.ora';
	```
8. Restore the control file from an autobackup and then mount the database.
	For example, enter the following command:
	```
	RUN 
	{
	  ALLOCATE CHANNEL c1 DEVICE TYPE sbt PARMS '...';
	  RESTORE CONTROLFILE FROM AUTOBACKUP;
	  ALTER DATABASE MOUNT;
	}
	```
	RMAN restores the control file to whatever locations you specified in the `CONTROL_FILES` initialization parameter.
9. Catalog the data file copies that you copied in "Restoring Disk Backups to a New Host", using their new file names or `CATALOG START` `WITH` (if you know all the files are in directories with a common prefix easily addressed with a `CATALOG START WITH` command). For example, run:
	```
	CATALOG START WITH '/oracle/oradata/trgt/';
	```
	If you want to specify files individually, then you can execute a `CATALOG` command as follows:
	```
	CATALOG DATAFILECOPY
	  '/oracle/oradata/trgt/system01.dbf', '/oracle/oradata/trgt/undotbs01.dbf', 
	  '/oracle/oradata/trgt/cwmlite01.dbf', '/oracle/oradata/trgt/drsys01.dbf',
	  '/oracle/oradata/trgt/example01.dbf', '/oracle/oradata/trgt/indx01.dbf', 
	  '/oracle/oradata/trgt/tools01.dbf', '/oracle/oradata/trgt/users01.dbf';
	```
10. Start a SQL\*Plus session on the new database and query the database file names recorded in the control file.
	Because the control file is from the `trgta` database, the recorded file names use the original `hosta` file names. You can query `V$` views to obtain this information. Run the following query in SQL\*Plus:
	```
	COLUMN NAME FORMAT a60
	SPOOL  LOG '/tmp/db_filenames.out'
	SELECT FILE# AS "File/Grp#", NAME 
	FROM   V$DATAFILE
	UNION
	SELECT GROUP#,MEMBER 
	FROM   V$LOGFILE;
	SPOOL OFF
	EXIT
	```
11. Write the RMAN restore and recovery script. The script must include the following steps:
	1. For each data file on the destination host that is restored to a different path than it had on the source host, use a `SET` `NEWNAME` command to specify the new path on the destination host. If the file systems on the destination system are set up to have the same paths as the source host, then do not use `SET NEWNAME` for those files restored to the same path as on the source host.
		2. For each online redo log that is to be created at a different location than it had on the source host, use SQL `ALTER` `DATABASE` `RENAME` `FILE` commands to specify the path name on the destination host. If the file systems on the destination system are set up to have the same paths as the source host, then do not use `ALTER DATABASE RENAME FILE` for those files restored to the same path as on the source host.
		3. Perform a `SET UNTIL` operation to limit recovery to the end of the archived redo logs. The recovery stops with an error if no `SET UNTIL` command is specified.
		4. Restore and recover the database.
		5. Run the `SWITCH DATAFILE ALL` command so that the control file recognizes the new path names as the official new names of the data files.
	Example 20-3 shows the RMAN script `reco_test.rman` that can perform the restore and recovery operation.
	Example 20-3 Restoring a Database on a New Host
	```
	RUN
	{
	  # allocate a channel to the tape device
	  ALLOCATE CHANNEL c1 DEVICE TYPE sbt PARMS '...';
	  # rename the data files and online redo logs
	  SET NEWNAME FOR DATAFILE 1 TO '?/oradata/test/system01.dbf';
	  SET NEWNAME FOR DATAFILE 2 TO '?/oradata/test/undotbs01.dbf';
	  SET NEWNAME FOR DATAFILE 3 TO '?/oradata/test/cwmlite01.dbf';
	  SET NEWNAME FOR DATAFILE 4 TO '?/oradata/test/drsys01.dbf';
	  SET NEWNAME FOR DATAFILE 5 TO '?/oradata/test/example01.dbf';
	  SET NEWNAME FOR DATAFILE 6 TO '?/oradata/test/indx01.dbf';
	  SET NEWNAME FOR DATAFILE 7 TO '?/oradata/test/tools01.dbf';
	  SET NEWNAME FOR DATAFILE 8 TO '?/oradata/test/users01.dbf';
	  SQL "ALTER DATABASE RENAME FILE ''/dev3/oracle/dbs/redo01.log''
	      TO ''?/oradata/test/redo01.log'' ";
	  SQL "ALTER DATABASE RENAME FILE ''/dev3/oracle/dbs/redo02.log''
	      TO ''?/oradata/test/redo02.log'' ";
	  # Do a SET UNTIL to prevent recovery of the online logs
	  SET UNTIL SCN 123456;
	  # restore the database and switch the data file names
	  RESTORE DATABASE;
	  SWITCH DATAFILE ALL;
	  # recover the database
	  RECOVER DATABASE;
	}
	EXIT
	```
12. Execute the script created in the previous step.
	For example, start RMAN to connect to the target database and run the `@` command:
	```
	% rman TARGET / NOCATALOG
	RMAN> @reco_test.rman
	```
13. Open the restored database with the `RESETLOGS` option.
	From the RMAN prompt, open the database with the `RESETLOGS` option:
	```
	ALTER DATABASE OPEN RESETLOGS;
	```
	Caution:
	When you re-open your database in the next step, do not connect to the recovery catalog. Otherwise, the new database incarnation created is registered automatically in the recovery catalog, and the file names of the production database are replaced by the new file names specified in the script.
14. Optionally, delete the test database with all of its files.
	Note:
	If you used an ASM disk group, then the `DROP DATABASE` command is the only way to safely remove the files of the test database. If you restored to non-ASM storage then you can also use operating system commands to remove the database.
	Use the `DROP DATABASE` command to delete all files associated with the database automatically. The following example deletes the database files:
	```
	STARTUP FORCE NOMOUNT PFILE='?/oradata/test/inittrgta.ora';
	DROP DATABASE;
	```
	Because you did not perform the restore and recovery operation when connected to the recovery catalog, the recovery catalog contains no records for any of the restored files or the procedures performed during the test. Likewise, the control file of the `trgta` database is completely unaffected by the test.