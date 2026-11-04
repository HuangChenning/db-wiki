---
title: "Backup and Recovery User's Guide"
book: "Database Backup and Recovery User's Guide"
doc_id: F31836-11
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/bradv/rman-recovery-advanced.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-users-guide
---

Learn how to perform recovery scenarios that are less common or more complicated than the basic scenarios.

### 20.1 Recovering a NOARCHIVELOG Database with Incremental Backups

You can perform limited recovery of changes to a database running in `NOARCHIVELOG` mode by applying incremental backups. The incremental backups must be consistent, like all backups of a database run in `NOARCHIVELOG` mode, so you cannot make backups of the database when it is open.

Restoring a database running in `NOARCHIVELOG` mode is similar to restoring a database in `ARCHIVELOG` mode. The main differences are:

- Only consistent backups can be used in restoring a database in `NOARCHIVELOG` mode.
- Media recovery is not possible because no archived redo logs exist.

When you are recovering a `NOARCHIVELOG` database, specify the `NOREDO` option on the `RECOVER` command to indicate that RMAN does not attempt to apply archived redo logs. Otherwise, RMAN returns an error.

To recover a NOARCHIVELOG database with incremental backups:

1. After connecting to the target database and the recovery catalog, place the database in a mounted state:
	```
	STARTUP FORCE MOUNT
	```
2. For example, you can perform incomplete recovery with the following commands:
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

### 20.2 Restoring the Server Parameter File

RMAN can restore a lost server parameter file to its default location or to a location of your choice. Unlike the loss of the control file, the loss of the server parameter file does not cause the instance to immediately stop. The instance may continue operating, although you must shut it down and restart it after restoring the server parameter file.

Note the following considerations when restoring the server parameter file:

- If the instance is already started with the server parameter file, then you cannot overwrite the existing server parameter file.
- When the instance is started with a client-side initialization parameter file, RMAN restores the server parameter file to the default location if the `TO` clause is not used in the restore command. The default location is platform-specific, for example, `?``/dbs/spfile.ora` on Linux.
- A recovery catalog simplifies the recovery procedure because you can avoid recording and remembering the DBID. This procedure assumes that you are not using a recovery catalog.

To restore the server parameter file from autobackup:

1. Start RMAN and do one of the following:
	- If the database instance is started at the time of the loss of the server parameter file, then connect to the target database.
	- If the database instance is not started when the server parameter file is lost, and if you are not using a recovery catalog, then run the `SET DBID` command to set the DBID of the target database.
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

See Also:

" [Determining the DBID of the Database](rman-complete-database-recovery.md) " for details on determining the DBID

#### 20.2.1 Restoring the Server Parameter File from a Control File Autobackup

If you have configured control file autobackups, then the server parameter file is backed up with the control file whenever an autobackup is taken.

To restore the server parameter file from the control file autobackup:

1. Set the DBID for your database.
2. Use the `RESTORE SPFILE FROM AUTOBACKUP` command.
	If the autobackup is in a nondefault format, then first use the `SET CONTROLFILE AUTOBACKUP FORMAT` command to specify the format.

Example 20-1 Restoring the Server Parameter File from a Control File Autobackup

This example sets the DBID and restores the server parameter file from a control file autobackup in a nondefault location. RMAN uses the autobackup format and DBID to search for control file autobackups. If a control file autobackup is found, then RMAN restores the server parameter file from that backup to its default location.

```
SET DBID 320066378;
RUN 
{
  SET CONTROLFILE AUTOBACKUP FORMAT 
    FOR DEVICE TYPE DISK TO 'autobackup_format';
  RESTORE SPFILE FROM AUTOBACKUP;
}
```

See Also:

- Description of `CONFIGURE CONTROLFILE AUTOBACKUP FORMAT` in the entry for the `CONFIGURE` command in [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF113) to learn how to determine the correct value for `autobackup_format`
- " [Determining the DBID of the Database](rman-complete-database-recovery.md) " for details on how to determine the DBID

#### 20.2.2 Creating an Initialization Parameter File with RMAN

You can also restore the server parameter file as a client-side initialization parameter file with the `TO PFILE 'filename'` clause.

The file name that you specify must be on a file system accessible from the host where the RMAN client is running. This file need not be accessible directly from the host running the instance.

The following RMAN command creates an initialization parameter file named `/tmp/initTEMP.ora` on the system running the RMAN client:

```
RESTORE SPFILE TO PFILE '/tmp/initTEMP.ora';
```

To restart the instance with the initialization parameter file, use the following command, again running RMAN on the same client host:

```
STARTUP FORCE PFILE='/tmp/initTEMP.ora';
```

### 20.3 Performing Recovery with a Backup Control File

When all current control files are lost, you must restore a backup control file.

This section contains the following topics:

- About Recovery with a Backup Control File
- Performing Recovery with a Backup Control File and No Recovery Catalog

#### 20.3.1 About Recovery with a Backup Control File

If all copies of the current control file are lost or damaged, then you must restore and mount a backup control file. You must then run the `RECOVER` command, even if no data files have been restored, and open the database with the `RESETLOGS` option.

During recovery, RMAN automatically searches for online and archived logs that are not recorded in the RMAN repository and catalogs any that it finds. RMAN attempts to find a valid archived redo log in any current archiving destination with the current log format. The current format is specified in the initialization parameter file used to start the instance (or all instances in an Oracle RAC configuration). Similarly, RMAN attempts to find the online redo logs by using the file names listed in the control file.

If you changed the archiving destination or format during recovery, or if you added new online log members after the backup of the control file, then RMAN may not be able to automatically catalog a needed online or archived log. Whenever RMAN cannot find online redo logs and you did not specify an `UNTIL` time, RMAN reports errors similar to the following:

```
RMAN-00571: ===========================================================
RMAN-00569: =============== ERROR MESSAGE STACK FOLLOWS ===============
RMAN-00571: ===========================================================
RMAN-03002: failure of recover command at 08/29/2013 14:23:09
RMAN-06054: media recovery requesting unknown log: thread 1 scn 86945
```

In this case, you must use the `CATALOG` command to manually add the required redo logs to the repository so that recovery can proceed.

Note:

If some copies of the current control file are usable, however, then you can follow the procedure in " [Responding to the Loss of a Subset of the Current Control Files](user-managed-recovery-advanced.md) " and avoid the recovery and `RESETLOGS` operation.

See Also:

The discussion of `RESTORE CONTROLFILE` in [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF149) for more details about restrictions on using `RESTORE CONTROLFILE` in different scenarios (such as when using a recovery catalog, or restoring from a specific backup)

##### 20.3.1.1 About Control File Locations During RMAN Restore

When restoring the control file, the default destination is all of the locations defined in the `CONTROL_FILES` initialization parameter. If the `CONTROL_FILES` initialization parameter is not set, then the database uses the same rules to determine the destination for the restored control file that it uses when creating a control file if the `CONTROL_FILES` parameter is not set.

One way to restore the control file to one or more new locations is to change the `CONTROL_FILES` initialization parameter, and then use the `RESTORE CONTROLFILE` command with no arguments to restore the control file to the default locations. For example, if you are restoring your control file after a disk failure made some but not all `CONTROL_FILES` locations unusable, you can change `CONTROL_FILES` to replace references to the failed disk with path names pointing to another disk, and then run `RESTORE CONTROLFILE` with no arguments.

You can also restore the control file to any location that you choose other than the `CONTROL_FILES` locations, by using the form `RESTORE CONTROLFILE TO ' filename'`:

```
RESTORE CONTROLFILE TO '/tmp/my_controlfile';
```

You can perform this operation with the database in `NOMOUNT`, `MOUNT`, or `OPEN` states, because you are not overwriting any of the control files currently in use. Any existing file named `'filename'` is overwritten. After restoring the control file to a new location, you can then update the `CONTROL_FILES` initialization parameter to include the new location.

See Also:

- The description of the `CREATE CONTROLFILE` statement in [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=SQLRF01203) for the rules that determine the destination of restored control files
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF149) for `RESTORE CONTROLFILE` syntax

##### 20.3.1.2 About RMAN Recovery With and Without a Recovery Catalog

The process of recovering a control file depends on whether a recovery catalog is used.

When RMAN is connected to a recovery catalog, the recovery procedure with a backup control file is identical to recovery with a current control file. The RMAN metadata missing from the backup control file is available from the recovery catalog. The only exception is if the database name is not unique in the catalog, in which case you must use `SET DBID` command before restoring the control file.

If you are not using a recovery catalog, then you must restore your control file from an autobackup. To restore the control file from autobackup, the database must be in a `NOMOUNT` state. You must first set the DBID for your database, and then use the `RESTORE CONTROLFILE FROM AUTOBACKUP` command.

Example 20-2 Setting the DBID and Restoring the Control File from Autobackup

In this example, RMAN uses the autobackup format and DBID to determine where to hunt for the control file autobackup. If one is found, RMAN restores the control file to all control file locations listed in the `CONTROL_FILES` initialization parameter.

```
SET DBID 320066378;
RUN
{
  SET CONTROLFILE AUTOBACKUP FORMAT 
    FOR DEVICE TYPE DISK TO 'autobackup_format';
  RESTORE CONTROLFILE FROM AUTOBACKUP;
}
```

See Also:

- " [Determining the DBID of the Database](rman-complete-database-recovery.md) " to learn how to determine your DBID
- The description of `CONFIGURE CONTROLFILE AUTOBACKUP FORMAT` in the entry for `CONFIGURE` in [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF113) to learn how to determine the correct value for the autobackup format

##### 20.3.1.3 About RMAN Recovery When Using a Fast Recovery Area

The commands for restoring a control file are the same whether or not the database uses a fast recovery area.

If the database uses a fast recovery area, then RMAN updates a control file restored from backup by crosschecking all disk-based backups and image copies recorded in the control file. RMAN catalogs any backups in the recovery area that are not recorded. As a result, the restored control file has a complete and accurate record of all backups in the recovery area and any other backups known to the control file at the time of the backup.

RMAN does not automatically crosscheck tape backups after restoring a control file. If you are using tape backups, then you can restore and mount the control file, and optionally crosscheck the backups on tape, as shown in the following example:

```
CROSSCHECK BACKUP DEVICE TYPE sbt;
```

#### 20.3.2 Performing Recovery with a Backup Control File and No Recovery Catalog

Recovering a database with a backup control file and when no recovery catalog is used requires you to restore the control file from an autobackup.

This section assumes that you have RMAN backups of the control file, but do not use a recovery catalog. It also assumes that you enabled the control file autobackup feature for the target database and can restore an autobackup of the control file.

Because the autobackup uses a well-known format, RMAN can restore it even though it does not have a repository available that lists the available backups. You can restore the autobackup to the default or a new location. RMAN replicates the control file to all `CONTROL_FILES` locations automatically.

Note:

If you know the backup piece name that contains the control file (for example, from the media manager or because the piece is on disk), then you can specify the piece name using the `RESTORE CONTROLFILE FROM 'filename'` command. The database records the location of every autobackup in the alert log.

Because you are not connected to a recovery catalog, the RMAN repository contains only information about available backups at the time of the control file backup. If you know the location of other usable backup sets or image copies, then add them to the control file RMAN repository with the `CATALOG` command.

To recover the database with a control file autobackup in `NOCATALOG` mode:

1. Start RMAN and connect to a target database, as described in " [Making Database Connections with RMAN](starting-interacting-with-rman-client.md) ".
2. Start the target database instance without mounting the database. For example:
	```
	STARTUP NOMOUNT;
	```
3. Set the database identifier for the target database with the `SET DBID` command.
	RMAN displays the DBID whenever you connect to a target database. You can also obtain it by inspecting saved RMAN log files, querying the catalog, or looking at the file names of control file autobackup. For example, run:
	```
	SET DBID 676549873;
	```
4. Write an RMAN command file to restore the autobackup control file and perform recovery.
	The command file contains the following steps:
	1. Optionally, specify the most recent backup time stamp that RMAN can use when searching for a control file autobackup to restore.
		2. If you know that a different control file autobackup format was in effect when the control file autobackup was created, then specify a nondefault format for the restore of the control file.
		3. If an SBT channel created the control file autobackup, then allocate one or more SBT channels. Because no recovery catalog is available, you cannot use preconfigured channels.
		4. Restore the autobackup of the control file, optionally setting the maximum number of days backward that RMAN can search and the initial sequence number that it uses in its search for the first day.
		5. If you know that the control file contains information about configured channels that is useful to you in the rest of the restore process, then you can exit RMAN to clear manually allocated channels from Step 4.c.
		If you restart the RMAN client and mount the database, then these configured channels are available for your use. If you do not care about using configured channels from your control file, then you can simply mount the database.
		6. This step depends on whether the online redo logs are available. The option `OPEN RESETLOGS` is always required after recovery with a backup control file, regardless of whether logs are available.
		If the online redo logs are usable, then RMAN can find and apply these logs. Perform a complete restore and recovery as described in " [Performing Complete Database Recovery](rman-complete-database-recovery.md) ".
		If the online redo logs are unusable, then perform DBPITR as described in " [Performing Database Point-in-Time Recovery](rman-performing-flashback-dbpitr.md) ". An `UNTIL` clause is required to specify a target time, SCN, or log sequence number for the recovery before the first SCN of the online redo logs (otherwise, RMAN issues the `RMAN-6054` error).
		When you perform DBPITR with a backup control file, before opening the database with `RESETLOGS`, you can open the database read-only using SQL\*Plus and run queries as needed to verify that the effects of the logical corruption have been reversed. If you are satisfied with the results, then you can open the database with `RESETLOGS`.
		Note:
		When specifying log sequences, if the last created archived redo log has sequence n, then specify `UNTIL SEQUENCE n+1` so that RMAN applies n and then stops.
	In the following example, the online redo log files have been lost, and the most recent archived redo log sequence number is 13243. This example shows how to restore the control file autobackup and recover through the latest log.
	```
	RUN 
	{
	  # Optionally, set upper limit for eligible time stamps of control file 
	  # backups
	  # SET UNTIL TIME '09/10/2017 13:45:00';
	  # Specify a nondefault autobackup format only if required
	  # SET CONTROLFILE AUTOBACKUP FORMAT FOR DEVICE TYPE DISK 
	  #   TO '?/oradata/%F.bck';
	  ALLOCATE CHANNEL c1 DEVICE TYPE sbt PARMS '...'; # allocate manually
	  RESTORE CONTROLFILE FROM AUTOBACKUP
	    MAXSEQ 100           # start at sequence 100 and count down
	    MAXDAYS 180;         # start at UNTIL TIME and search back 6 months
	  ALTER DATABASE MOUNT;
	}
	# Now use automatic channels configured in restored control file
	RESTORE DATABASE UNTIL SEQUENCE 13244;
	RECOVER DATABASE UNTIL SEQUENCE 13244;
	```
5. If recovery was successful, then open the database and reset the online logs:
	```
	ALTER DATABASE OPEN RESETLOGS;
	```

### 20.4 Performing Disaster Recovery

Disaster recovery includes the restoration and recovery of the target database after the loss of the entire target database, the recovery catalog database, all current control files, all online redo log files, and all parameter files.

This section contains the following topics:

- Prerequisites of Disaster Recovery
- Recovering the Database After a Disaster

#### 20.4.1 Prerequisites of Disaster Recovery

Certain prerequisites must be met before you perform disaster recovery using RMAN.

You must have the following:

- Backups of all data files
- All archived redo logs generated after the creation time of the oldest backup that you intend to restore
- At least one control file autobackup
- A record of the DBID of the database

#### 20.4.2 Recovering the Database After a Disaster

Assume that the Linux server on which your database was running has been damaged beyond repair. Fortunately, you backed up the database to Oracle Secure Backup and have the tapes available. You can recover the database by using these backups.

The procedure for disaster recovery is similar to the procedure for recovering the database with a backup control file in `NOCATALOG` mode. If you are restoring the database to a new host, then review the considerations described in " Restoring a Database on a New Host ".

. The scenario assumes the following:

- Oracle Database is installed on the new host.
- You are restoring the database to a new Linux host with the same directory structure as the old host.
- You have one tape drive containing backups of all the data files and archived redo logs through log 1124, and autobackups of the control file and server parameter file.
- You do not use a recovery catalog with the database.

To recover the database on the new host:

1. Ensure that the prerequisites described in " Prerequisites of Disaster Recovery " are met.
2. If possible, restore or re-create all relevant network files such as `tnsnames.ora` and `listener.ora` and a password file.
3. Start RMAN and connect to the target database instance, as described in " [Making Database Connections with RMAN](starting-interacting-with-rman-client.md) ".
	At this stage, no initialization parameter file exists. If you have set `ORACLE_SID` and `ORACLE_HOME`, then you can use operating system authentication to connect as `SYSDBA` or `SYSBACKUP`.
4. Specify the DBID for the target database with the `SET` `DBID` command, as described in " Restoring the Server Parameter File ".
	For example, enter the following command:
	```
	SET DBID 676549873;
	```
5. Run the `STARTUP NOMOUNT` command.
	When the server parameter file is not available, RMAN attempts to start the instance with a dummy server parameter file.
6. Allocate a channel to the media manager and then restore the server parameter file from autobackup.
	For example, enter the following command to restore the server parameter file from Oracle Secure Backup:
	```
	RUN
	{
	  ALLOCATE CHANNEL c1 DEVICE TYPE sbt;
	  RESTORE SPFILE FROM AUTOBACKUP;
	}
	```
7. Restart the instance with the restored server parameter file.
	```
	STARTUP FORCE NOMOUNT;
	```
8. Write a command file to perform the restore and recovery operation, and then execute the command file. The command file must do the following:
	1. Allocate a channel to the media manager.
		2. Restore a control file autobackup (see " Performing Recovery with a Backup Control File and No Recovery Catalog ").
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
9. If recovery was successful, then open the database and reset the online logs:
	```
	ALTER DATABASE OPEN RESETLOGS;
	```

### 20.5 Restoring a Database on a New Host

Use the `RESTORE` and `RECOVER` commands to restore a database on a new host. Restoring a database on a new host is useful when you want to perform a test run of your disaster recovery procedures or to permanently move a database to a new host.

If you use the procedure in this section, then the DBID for the restored database is the same as the DBID for the original database. Do not register a test database created in this way in the same recovery catalog as the source database. Because the DBID of the two databases is the same, the metadata for the test database can interfere with RMAN's ability to restore and recover the source database.

If your goal is to create a copy of your target database for ongoing use on a new host, then use the RMAN `DUPLICATE` command instead of this procedure. The `DUPLICATE` command assigns a new DBID to the database it creates, enabling it to be registered in the same recovery catalog as the original database.

To restore a database on a new host:

1. Complete the steps that must be performed before you restore the database, as described in " Preparing to Restore a Database on a New Host ".
2. Transfer the target database backups to the new host and restore the backups, as described in " Restoring Disk Backups to a New Host ".

See Also:

Testing the Restore of a Database on a New Host

#### 20.5.1 Preparing to Restore a Database on a New Host

Certain steps must be preformed to prepare for the restoration of the database on a new host.

The steps include the following:

- Record the DBID for your source database.
- Make the source database initialization parameter file accessible on the new host. Copy the file from the old host to a new host by using an operating system utility.
- If you perform a test restore operation only, then ensure that RMAN is not connected to the recovery catalog. Otherwise, RMAN records metadata about the restored data files in the recovery catalog. This metadata interferes with future attempts to restore and recover the primary database.
	If you must use a recovery catalog because the control file is not large enough to contain the RMAN repository data on all of the backups that you must restore, then use Oracle Data Pump to export the catalog and import it into a different schema or database. Afterward, use the copied recovery catalog for the test restore. Otherwise, the recovery catalog considers the restored database as the current target database.
- Ensure that backups used for the restore operation are accessible on the restore host. For example, if the backups were made with a media manager, then verify that the tape device is connected to the new host. If you are using disk copies, then use the procedure in the following section.
- If you are performing a trial restore of the production database, then perform either of the following actions before restoring the database in the test environment:
	- If the test database will use a fast recovery area that is physically different from the recovery area used by the production database, then set `DB_RECOVERY_FILE_DEST` in the test database instance to the new location.
		- If the test database will use a fast recovery area that is physically the same as the recovery area used by the production database, then set `DB_UNIQUE_NAME` in the test database instance to a different name from the production database.
	If you do not perform either of the preceding actions, then RMAN assumes that you are restoring the production database and deletes flashback logs from the fast recovery area because they are considered unusable.

See Also:

" [Determining the DBID of the Database](rman-complete-database-recovery.md) " to learn how to determine the DBID fo your database

#### 20.5.2 Restoring Disk Backups to a New Host

To move the database to a new host by using data file copies or backup sets on disk, you must transfer the files manually to the new host. This procedure assumes that RMAN is using a recovery catalog.

To restore backup files to a new host:

1. Start RMAN and connect to a target database and recovery catalog, as described in " [Making Database Connections with RMAN](starting-interacting-with-rman-client.md) ".
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
	% cp -r /disk1/auto_bkp_loc/c-1618370911-20130208-00 /net/new_host/tmp
	```
	You must use the `SET CONTROLFILE AUTOBACKUP FORMAT` command when restoring an autobackup from a nondefault location.

See Also:

" Restoring the Server Parameter File from a Control File Autobackup "

#### 20.5.3 Testing the Restore of a Database on a New Host

It is recommended that you test whether you can restore your database to a new host.

In this scenario, you have two networked Linux hosts, `hosta` and `hostb`. A target database named `trgta` is on `hosta` and is registered in recovery catalog `catdb`. You want to test the restore and recovery of `trgta` on `hostb`, while keeping database `trgta` up and running on `hosta`.

Now, assume that the directory structure of `hostb` is different from `hosta`. The target database is located in `/net/hosta/dev3/oracle/dbs`, but you want to restore the database to `/net/hostb/oracle/oradata/test`. You have tape backups of data files, control files, archived redo logs, and the server parameter file on a media manager accessible by both hosts. The `ORACLE_SID` for the `TRGTA` database is `TRGTA` and does not change for the restored database.

Caution:

If you are restoring the database for test purposes, then never connect RMAN to the test database and the production recovery catalog.

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
9. Catalog the data file copies that you copied in " Restoring Disk Backups to a New Host ", using their new file names or `CATALOG START` `WITH` (if you know all the files are in directories with a common prefix easily addressed with a `CATALOG START WITH` command). For example, run:
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
	The following code shows the RMAN script `reco_test.rman` that can perform the restore and recovery operation.
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
	  ALTER DATABASE RENAME FILE '/dev3/oracle/dbs/redo01.log'
	      TO '?/oradata/test/redo01.log';
	  ALTER DATABASE RENAME FILE '/dev3/oracle/dbs/redo02.log'
	      TO '?/oradata/test/redo02.log';
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
	When you re-open your database in the next step, do not connect to the production recovery catalog. Otherwise, the new database incarnation created is registered automatically in the recovery catalog, and the file names of the production database are replaced by the new file names specified in the script.
14. Optionally, delete the test database with all of its files.
	Note:
	If you used an ASM disk group, then the `DROP DATABASE` command is the only way to safely remove the files of the test database. If you restored to non-ASM storage then you can also use operating system commands to remove the database.
	Use the `DROP DATABASE` command to delete all files associated with the database automatically. The following example deletes the database files:
	```
	STARTUP FORCE NOMOUNT PFILE='?/oradata/test/inittrgta.ora';
	DROP DATABASE;
	```
	Because you did not perform the restore and recovery operation when connected to the recovery catalog, the recovery catalog contains no records for any of the restored files or the procedures performed during the test. Likewise, the control file of the `trgta` database is completely unaffected by the test.

See Also:

" [Making Database Connections with RMAN](starting-interacting-with-rman-client.md) "

### 20.6 Restoring Backups Created Using Older Versions of RMAN

You can restore backups that were created using older versions of RMAN, up to Oracle Database 9i Release 2 (9.2.0.8).

There must be a supported upgrade path between the Oracle Database version on which the backups were created and the Oracle software version on which you want to run the restored database.

In this example, the source database is an Oracle Database 11g Release 2 database and it is configured to use a server parameter file (spfile). The database runs in `ARCHIVELOG` mode and uses a fast recovery area. Control file autobackups are also configured. You then create RMAN backups of the source database, including the archived redo logs.

The destination host on which these backups are restored has Oracle Database 12c Release 1 installed.

To restore RMAN backups that were created using an RMAN version that is older than the current target database version:

1. Verify that there is a supported upgrade path from the database version on which the backups were created to the Oracle server version on which you plan to restore the database.
	For example, if your RMAN backups were created on Oracle Database 11g Release 2 (11.2.0.3) and you want to run the restored database on Oracle Database 12c Release 1 (12.1), then you must verify that there is a supported upgrade path from release 11.2.0.3 to release 12.1.
	See Also:
	[Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=UPGRD12358) for information about the database upgrade paths
2. Ensure that the source database backups are available at the destination host on which they must be restored.
	You can either use an operating system utility to copy the backups to the destination host or store the backups in a shared location that is accessible to the destination host.
3. Shut down the destination database.
4. On the destination host, set the `ORACLE_SID` to the same value that was used on the source database.
	```
	%  setenv ORACLE_SID db112
	```
5. Start RMAN on the destination host and connect to the target database using operating system authentication and without a recovery catalog.
	```
	% rman target / NOCATALOG
	```
6. Set the DBID to the same value as the source database.
	The following command sets the DBID to 699892390, which is the DBID of the source database whose backups are being restored.
	```
	RMAN> set DBID 699892390;
	```
7. Start the target database in nomount mode.
	```
	RMAN> startup nomount;
	```
	RMAN fails to find the server parameter file, which has not yet been restored. However, the instance is started with a “dummy” file and the following output is displayed:
	```
	startup failed: ORA-01078: failure in processing system parameters
	LRM-00109: could not open parameter file '/oracle/dbs/inittrgta.ora'
	trying to start the Oracle instance without parameter files ...
	Oracle instance started
	```
8. Restore the server parameter file from the source database autobackup.
	Because controlfile autobackups were enabled in the source database, the server parameter file is included in the backup. To restore an autobackup that has a nondefault format, use the `SET CONTROLFILE AUTOBACKUP FORMAT` command to indicate the format.
	The following example sets the autobackup format, restores the spfile in the source database to the pfile `/dev3/oracle/network/init_db112.ora`, and then shuts down the target database.
	```
	run
	{
	    set controlfile autobackup format for device type disk to '/scratch/fra/cf/%F.bck';
	    restore spfile to pfile '/dev3/oracle/network/init_db112.ora' from autobackup recovery area '/scratch /fra/cf' db_name 'DB112';
	    shutdown abort;
	}
	```
9. Edit the restored initialization parameter file and modify the required initialization parameters.
	This includes the `COMPATIBLE` parameter, if the compatibility requirement for the target database is different from that set in the source database, and parameters that are deprecated in the target database release. Also update any location-specific parameters such as those ending with `_DEST` to reflect the new directory structure.
	In this example, you must edit the pfile located at `/dev3/oracle/network/init_db112.ora`.
10. Restart the instance with the edited initialization parameter file.
	The following command starts the database instance in nomount mode using the edited parameter file.
	```
	RMAN> startup force nomount pfile='/dev3/oracle/network/init_db112.ora';
	```
11. Restore the control file from an autobackup and then mount the database.
	The following example sets the format for the control file autobackups, restores the control file from an autobackup, and then mounts the database.
	```
	run
	{
	    set controlfile autobackup format for device type disk to '/scratch/fra/cf/%F.bck';
	    restore controlfile from autobackup recovery area '/scratch/fra/cf' db_name 'DB112'; 
	    alter database mount;
	}
	```
	The control file is restored to the location specified in the `CONTROL_FILES` initialization parameter in the edited initialization parameter file.
12. Catalog data file copies of the source database that were made available to the destination host.
	If all the files are in directories with a common prefix, then use the `CATALOG START WITH` command. If you want to specify the file names individually, then use the `CATALOG DATAFILECOPY` command.
	In the following example, all the data file copies are stored in a single folder `/scratch/fra/DB112/backupset` and so we use the `CATALOG START WITH` command.
	```
	RMAN> catalog start with '/scratch/fra/DB112/backupset';
	```
13. Restore and recover the source database.
	If the data files are restored to a different path than those on the source database, you must specify a new path on the destination host by using the `SET NEWNAME` command. If the online redo logs are to be created in a different location than those on the source database, then use the `ALTER DATABASE RENAME FILE` command to specify the location of each redo log file on the destination database.
	In this example, the `SET NEWNAME FOR DATABASE` command is used to specify the new location for all restored data files. The new location for each online redo log file is specified using an `ALTER DATABASE RENAME FILE` command. Recovery is performed until the SCN specified in the command.
	```
	run
	{
	    set newname for database to '/ade/b/1885631999/oracle/dbs/%U.f';
	    alter database rename file '/dev1/oracle/dbs/redo01.log' to '/dev3/oracle/dbs/redo1.log';
	    alter database rename file '/dev1/oracle/dbs/redo02.log' to '/dev3/oracle/dbs/redo2.log';
	    set until scn 1092435;
	    restore database;
	    switch datafile all;
	    recover database;
	}
	```
14. Open the restored database with the `RESETLOGS` and `UPGRADE` options.
	```
	RMAN> alter database open resetlogs upgrade;
	Statement processed
	RMAN-06900: WARNING: unable to generate V$RMAN_STATUS or V$RMAN_OUTPUT row
	RMAN-06901: WARNING: disabling update of the V$RMAN_STATUS and V$RMAN_OUTPUT rows
	ORACLE error from target database: 
	ORA-04023: Object SYS.STANDARD could not be validated or authorized
	```
	The error is caused by database packages that need to be revalidated as part of the upgrade process.
15. Exit RMAN.
16. Upgrade the target database to the desired Oracle release by performing the steps required to upgrade a database.
	See Also:
	[Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=UPGRD12358) for information about upgrading the database

### 20.7 Restoring and Recovering Files Over the Network

RMAN enables you to restore or recover files by connecting, over the network, to a physical standby database that contains the required files. You can restore an entire database, data files, control files, server parameter file, or tablespaces. Restoring files over the network is very useful in scenarios where you need to synchronize the primary and standby databases.

Backup sets are used to restore or recover files over the network. Therefore, you can use multisection backups, encryption, and compression to improve backup and restore performance.

Restoring and recovering files over the network is supported starting with Oracle Database 12c Release 1 (12.1).

This section includes:

- About Restoring Files Over the Network
- About Recovering Files Over the Network
- Scenarios for Restoring and Recovering Files Over the Network
- Restoring Data Files Over the Network
- Rolling Forward a Physical Standby Database Using the RECOVER Command

#### 20.7.1 About Restoring Files Over the Network

RMAN restores database files, over the network, from a physical standby database by using the `FROM SERVICE` clause of the `RESTORE` command.

The `FROM SERVICE` clause provides the service name of the physical standby database from which the files must be restored. During the restore operation, RMAN creates backup sets, on the physical standby database, of the files that need to be restored and then transfers these backup sets to the target database over the network.

Use the `SECTION SIZE` clause of the `RESTORE` command to perform a multisection restore operation. To encrypt the backup sets created on the physical standby database, use the `SET ENCRYPTION` command before the `RESTORE` command to specify the encryption algorithm used.

To transfer files from the physical standby database as compressed backup sets, use the `USING COMPRESSED BACKUPSET` clause in the `RESTORE` command. By default, RMAN compresses backup sets using the algorithm that is set in the RMAN configuration. You can override the default and set a different algorithm by using the `SET COMPRESSION ALGORITHM` command before the `RESTORE` statement.

#### 20.7.2 About Recovering Files Over the Network

You can perform recovery by fetching an incremental backup, over the network, from a primary database and then applying this incremental backup to the physical standby database.

RMAN is connected as `TARGET` to the physical standby database. The recovery process is optimized by restoring only the used data blocks in a data file. Use the `FROM SERVICE` clause to specify the service name of the primary database from which the incremental backup must be fetched.

To use multisection backup sets during the recovery process, specify the `SECTION SIZE` clause in the `RECOVER` command. To transfer the required files from the primary database as encrypted backup sets, use the `SET ENCRYPTION` command before the `RESTORE` command to specify the encryption algorithm used to create the backup sets.

To compress backup sets that are used to recover files over the network, use the `USING COMPRESSED BACKUPSET`. RMAN compresses backup sets when it creates them on the primary database and then transfers these backup sets to the target database.

#### 20.7.3 Scenarios for Restoring and Recovering Files Over the Network

Recovering files by connecting, over the network, to a physical standby database is useful in certain scenarios.

These scenarios include the following:

- You need to roll-forward a physical standby database to make it in-sync with the primary database.
	After creating an incremental backup of the latest changes on the primary database, you can restore the physical standby database using the incremental backup.
- You want to restore lost data files, control files, or tablespaces on a primary database using the corresponding files on the physical standby database. You can also restore files on a physical standby database by using the primary database.

#### 20.7.4 Restoring Data Files Over the Network

Use the `RESTORE` command to restore lost or damaged data files by connecting over the network to a primary database or physical standby database.

In this example, the `DB_UNIQUE_NAME` of the primary database is `MAIN` and the `DB_UNIQUE_NAME` of the physical standby database is `STANDBY`. The data file `sales.dbf` on the primary database was lost. You want to restore this data file from the physical standby database. The service name of the physical standby database is `standby_tns`. The `RESTORE` command with the `FROM SERVICE` clause enables you to restore the lost data file in the primary database by using the data file in the physical standby database. The password file in the primary database and the physical standby database are the same.

Use the following steps to restore the data file `sales.dbf` in the primary database by using the data file in the physical standby database:

1. Connect to the primary database as a user with the `SYSBACKUP` privilege.
	```
	%RMAN
	RMAN> CONNECT TARGET "sbu@main AS SYSBACKUP";
	```
	Enter the password for the `sbu` user when prompted.
2. Specify that the backup sets must be encrypted using the AES128 encryption algorithm
	```
	RMAN> SET ENCRYPTION ALGORITHM 'AES128';
	```
3. Ensure that the `tnsnames.ora` file in the physical standby database contains an entry corresponding to the primary database. Also ensure that the password files on the primary and physical standby database are the same.
4. Restore the data file on the primary database by using the data file on the physical standby database. The following command creates multisection backup sets to perform the restore operation.
	```
	RESTORE DATAFILE '/oradata/datafiles/sales.dbf'
	FROM SERVICE standby_tns
	SECTION SIZE 120M;
	```

#### 20.7.5 Rolling Forward a Physical Standby Database Using the RECOVER Command

RMAN rolls forward a physical standby database by creating an incremental backup that contains the changes to the primary database, transferring the incremental backup over the network to the physical standby database, and then applying the incremental backup to the physical standby database. All changes to data files on the primary database, beginning with the SCN in the standby data file header, are included in the incremental backup.

You can use the `RECOVER ... FROM SERVICE` command to synchronize the data files on the physical standby database with those on the primary database. This command refreshes the standby data files and rolls them forward to the same point-in-time as the primary. However, the standby control file still contains old SCN values which are lower than the SCN values in the standby data files. Therefore, to complete the synchronization of the physical standby database, you must refresh the standby control file and then update the data file names, online redo log file names, and the standby redo log file names in the refreshed standby control file.

If network resources are a constraint, then you can use the `BACKUP INCREMENTAL` command to create incremental backups on the primary database, and then use the incremental backups to roll forward the physical standby database.

" Steps to Refresh a Physical Standby Database with Changes Made to the Primary Database " describes the steps to refresh a physical standby using the `FROM SERVICE` clause.

See Also:

[Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=SBYDB-GUID-B140C38B-DE01-4252-8422-7154018DDFEC) for information about using the `BACKUP INCREMENTAL` command to roll forward a physical standby database

##### 20.7.5.1 Steps to Refresh a Physical Standby Database with Changes Made to the Primary Database

Use the `RECOVER STANDBY DATABASE` command with the `FROM SERVICE` clause to refresh a physical standby database with changes that were made to the primary database.

Consider a primary database whose `DB_UNIQUE_NAME` is `MAIN` and net service name is `primary_db`. The `DB_UNIQUE_NAME` of the physical standby database is `STANDBY` and its net service name is `standby_db`.

To refresh the physical standby database with changes made to the primary database:

1. Ensure that the following prerequisites are met:
	- Oracle Net connectivity is established between the physical standby database and the primary database.
		You can establish connectivity by adding an entry corresponding to the primary database in the `tnsnames.ora` file of the physical standby database.
		- The password files on the primary database and the physical standby database are the same.
		- The `COMPATIBLE` initialization parameter, for the primary database and physical standby database, is set to 12.0 or later.
2. Start RMAN, and connect as target to the physical standby database. It is recommended that you also connect to a recovery catalog.
	The following commands connect as `TARGET` to the physical standby database, and as `CATALOG` to the recovery catalog. The connection to the physical standby is established using the `sbu` user, who has been granted `SYSBACKUP` privilege. The net service name of the physical standby database is `standby_db` and that of the recovery catalog is `catdb`.
	```
	CONNECT TARGET "sbu@standby_db AS SYSBACKUP";
	CONNECT CATALOG rman@catdb;
	```
3. Roll forward the physical standby database using the `RECOVER STANDBY DATABASE` command with the `FROM                             SERVICE` clause.
	The `FROM SERVICE` clause specifies the service name of the primary database. The physical standby is rolled forward by applying changes that were made to the primary database. The physical standby database is restarted after the roll forward operation.
	The following example rolls forward the physical standby database and applies changes that were made to the primary database with service name is `primary_db`.
	```
	RECOVER STANDBY DATABASE FROM SERVICE primary_db;
	```
4. (For Active Data Guard only) Perform the following steps to recover redo data and open the physical standby database in read-only mode:
	```
	ALTER DATABASE RECOVER MANAGED STANDBY DATABASE UNTIL CONSISTENT;
	ALTER DATABASE OPEN READ ONLY;
	```
5. Start the managed recovery processes on the physical standby database.
	The following command starts the managed recovery process:
	```
	ALTER DATABASE RECOVER MANAGED STANDBY DATABASE DISCONNECT FROM SESSION;
	```
	When using Data Guard Broker, use the following command to start the managed recovery process:
	```
	DGMGRL> edit database standby_db set state='APPLY-ON';
	```