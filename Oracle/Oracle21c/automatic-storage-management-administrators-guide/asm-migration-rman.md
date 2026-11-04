---
title: "Administrator's Guide"
book: "Automatic Storage Management Administrator's Guide"
doc_id: F30296-05
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/ostmg/asm-migration-rman.html
tags:
  - oracle
  - 21c
  - automatic-storage-management-administrators-guide
---

Recovery Manager (RMAN) provides tools to migrate data to and from Oracle ASM.

This chapter describes how to migrate data into and out of Oracle Automatic Storage Management (Oracle ASM) storage with Recovery Manager (RMAN).

This chapter includes the following topics:

The procedures in this chapter cover an Oracle ASM standalone environment on a Linux platform. File locations and procedures may be different for different Oracle configurations and on other operating system platforms.

See Also:

- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=BRADV-GUID-9997EF87-B293-44D4-92F3-DD938E79170D) for complete information about using RMAN
- Operating system-specific documentation for migrating data in and out of Oracle ASM on specific platforms
- [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=CWADD-GUID-70E524E1-0FAD-4962-9B9F-0691EAEE7A9F) for information about managing and migrating Oracle Cluster Registry and voting files
- [Oracle Real Applications Cluster Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=RACAD-GUID-A02120B2-BE62-4172-B402-BF034566E471) for migrating data in and out of Oracle ASM in an Oracle RAC configuration
- Articles at [My Oracle Support](https://support.oracle.com/) ([`https://support.oracle.com`](https://support.oracle.com/)) for information about gathering and backing up Oracle ASM and Oracle ACFS metadata in a formatted manner, such as HTML format

### Overview of Oracle ASM Data Migration

This section explains the basic concepts and tasks involved in migrating data to and from Oracle ASM.

This section includes the following topics:

- Purpose of Oracle ASM Data Migration
- Basic Concepts of Oracle ASM Data Migration
- Basic Steps of Data Migration to Oracle ASM Using RMAN

#### Purpose of Oracle ASM Data Migration

Alternatives to Oracle ASM storage include file systems, raw disks, and SAN configurations. Oracle ASM includes numerous benefits over these storage alternatives, including performance optimization, redundancy protection, and load balancing. You do not need a third-party Logical Volume Manager because Oracle ASM manages disks for you. Oracle Real Application Clusters (Oracle RAC) databases benefit from Oracle ASM because it provides ready-made shared storage.

If a database currently uses a storage system other than Oracle ASM, then you can migrate all or part of the database into Oracle ASM, thereby simplifying database administration. You can also migrate a fast recovery area to Oracle ASM.

Native operating system commands such as Linux `cp` or Windows `COPY` cannot write or read files in Oracle ASM storage. Because RMAN can read and write Oracle ASM files, you can use RMAN to copy data files into and out of Oracle ASM storage or between Oracle ASM disk groups. This technique is useful if you must store backups on user-managed disks.

#### Basic Concepts of Oracle ASM Data Migration

You can migrate data to Oracle ASM with RMAN even if you are not using RMAN as your primary backup tool. The migration requires one RMAN database backup.

If you have sufficient disk space to hold the entire database both in Oracle ASM and alternative storage systems, then you can move a database directly into Oracle ASM. If you do not have sufficient storage, then you can back the database up to tape, create an Oracle ASM disk group that uses old disk space, and restore the database from tape to Oracle ASM.

After you set the location of the new recovery area, existing backups remain in the old recovery area and count against the total disk quota of the recovery area. The backups are deleted from the old recovery area when space is needed. These backups are usable by RMAN. It is not necessary to move legacy backups to the new Oracle ASM recovery area unless you need disk space. To free space consumed by files in the old recovery area, you can back them up to tape or migrate them to the Oracle ASM recovery area.

Note:

A foreign archived redo log is a log received by a logical standby database for a LogMiner session. Foreign archived redo logs cannot be migrated. Unlike normal archived logs, foreign archived logs have a different internal database identifier (DBID). For this reason, they cannot be backed up or restored on a logical standby database.

Migrating a database from Oracle ASM to an alternative storage system is similar to migration from an alternative storage system to Oracle ASM. The primary change is to modify each step to refer to file locations in the alternative storage system.

#### Basic Steps of Data Migration to Oracle ASM Using RMAN

This section discusses the process of migrating the entire database and fast recovery area from alternative storage to Oracle ASM using RMAN.

The fast recovery area is an optional disk location that you can use to store recovery-related files such as control file and online redo log copies, archived redo log files, flashback logs, and RMAN backups. Oracle Database and RMAN manage the files in the fast recovery area automatically. You can specify the disk quota, which is the user-specified maximum size of the fast recovery area. When the disk quota is reached, Oracle automatically deletes files that are no longer needed.

Flashback logs are Oracle-generated logs used to perform flashback database operations. The database can only write flashback logs to the fast recovery area. Flashback logs are written sequentially and are not archived. They cannot be backed up to disk.

To migrate the entire database and fast recovery area from alternative storage to Oracle ASM, perform the following steps:

1. Back up the database and server parameter file, and disable Oracle Flashback Database.
	The Oracle Flashback Database option returns the entire database to a prior consistent System Change Number (SCN) with the `FLASHBACK` `DATABASE` command in RMAN or SQL. A database flashback is different from traditional media recovery because it does not involve the restore of physical files, instead restoring your current data files to past states using saved images of changed data blocks. This feature uses flashback logs and archived redo logs.
	This step is described in Preparing to Migrate the Database to Oracle ASM Using RMAN.
2. Restore files to Oracle ASM, recover the database, and optionally migrate the fast recovery area to Oracle ASM.
	This step is described in Migrating the Database to Oracle ASM Using RMAN.

To migrate files from Oracle ASM to alternative storage, see Migrating a Database from Oracle ASM to Alternative Storage.

### Preparing to Migrate the Database to Oracle ASM Using RMAN

This section explains how to prepare the database for migration. This section makes the following assumptions:

- You want to migrate the database to two Oracle ASM disk groups: `+DATA` for the database and `+FRA` for the fast recovery area.
- The database to be migrated to Oracle ASM storage is named `mydb`.

To prepare the database for Oracle ASM migration:

1. If the `COMPATIBLE` initialization parameter setting for the database is less than `11.0.0`, then make any read-only transportable tablespaces read/write.
	Read-only transportable tablespaces cannot be migrated because RMAN cannot back them up.
2. If the database is a physical standby database, and if managed recovery is started, then stop managed recovery.
	A physical standby database is a copy of a production database that you can use for disaster protection.
	For example, connect SQL\*Plus to the database with `SYSBACKUP` privileges (rather than `SYSDBA` privileges) to enforce the separation of duty security model, and run the following statement to stop managed recovery:
	```
	SQL> ALTER DATABASE RECOVER MANAGED STANDBY DATABASE CANCEL;
	```
	Keep this terminal window open.
3. Copy the server parameter file or initialization parameter file to a temporary location.
	The following example uses an operating system utility to copy the server parameter file:
	```
	$ cp spfileMYDB.ora orig_spfileMYDB.ora
	```
4. In a new terminal window, start RMAN session and connect as `TARGET` to the database to be migrated. Optionally, connect to a recovery catalog. Connect with `SYSBACKUP` privileges to enforce the separation of duty security model.
5. Back up the data files to the Oracle ASM disk group.
	The following example uses a `RUN` command to make a level 0 incremental backup and allocates four channels to increase the backup speed. A level 0 incremental backup is an RMAN incremental backup that backs up all data blocks in the data files being backed up. An incremental backup at level 0 is identical in content to a full backup, but unlike a full backup the level 0 backup is considered a part of the incremental backup strategy.
	An incremental backup is a RMAN backup in which only modified blocks are backed up. Incremental backups are classified by **level**. A level 0 incremental backup performs the same function as a full backup in that they both back up all blocks that have ever been used. The difference is that a full backup does not affect blocks backed up by subsequent incremental backups, whereas an incremental backup affects blocks backed up by subsequent incremental backups.
	A full backup is a non-incremental RMAN backup. Full does not refer to how much of the database is backed up, but to the fact that the backup is not incremental. Consequently, you can make a full backup of one data file.
	Increase or decrease this number accordingly. The format clause specifies `+DATA`, which is the name of the Oracle ASM disk group to be used for storing the database.
	```
	RUN
	{
	  ALLOCATE CHANNEL dev1 DEVICE TYPE DISK;
	  ALLOCATE CHANNEL dev2 DEVICE TYPE DISK;
	  ALLOCATE CHANNEL dev3 DEVICE TYPE DISK;
	  ALLOCATE CHANNEL dev4 DEVICE TYPE DISK;
	  BACKUP AS COPY
	    INCREMENTAL LEVEL 0
	    DATABASE
	    FORMAT '+DATA'
	    TAG 'ORA_ASM_MIGRATION';
	}
	```
6. If block change tracking is enabled for the database, then optionally make a level 1 incremental backup that you can use later to recover the database copy.
	Block change tracking is a database option that causes Oracle to track data file blocks affected by each database update. The tracking information is stored in a block change tracking file. When block change tracking is enabled, RMAN uses the record of changed blocks from the change tracking file to improve incremental backup performance by only reading those blocks known to have changed, instead of reading data files in their entirety.
	The following example makes an incremental level 1 copy of the level 0 backup created in the previous step:
	```
	RUN
	{
	  ALLOCATE CHANNEL dev1 DEVICE TYPE DISK;
	  ALLOCATE CHANNEL dev2 DEVICE TYPE DISK;
	  ALLOCATE CHANNEL dev3 DEVICE TYPE DISK;
	  ALLOCATE CHANNEL dev4 DEVICE TYPE DISK;
	  BACKUP INCREMENTAL LEVEL 1 
	    FOR RECOVER OF COPY WITH TAG 'ORA_ASM_MIGRATION' 
	    DATABASE;
	}
	```
7. If the database is in `ARCHIVELOG` mode, and if the database is open, then archive the online logs.
	The following example uses the `SQL` command to archive the current redo logs:
	```
	RMAN> SQL "ALTER SYSTEM ARCHIVE LOG CURRENT";
	```
8. If the database instance is currently using a server parameter file, then back it up.
	The following example backs up the server parameter file:
	```
	RMAN> BACKUP AS BACKUPSET SPFILE;
	```
9. If block change tracking is enabled, then disable it.
	The following command disables block change tracking:
	```
	RMAN> SQL "ALTER DATABASE DISABLE BLOCK CHANGE TRACKING";
	```
10. If Flashback Database is enabled, then disable it and drop any guaranteed restore points.
	Note:
	If you are not migrating the fast recovery area, then skip this step.
	Disabling Oracle Flashback Database is necessary because you cannot migrate flashback logs to Oracle ASM. The following command disables Flashback Database:
	```
	RMAN> SQL "ALTER DATABASE FLASHBACK OFF";
	```
	The following command drops the guaranteed restore point named `Q106`:
	```
	RMAN> SQL "DROP RESTORE POINT Q106";
	```
11. Shut down the database consistently.
	The following command shuts down the database:
	```
	RMAN> SHUTDOWN IMMEDIATE;
	```

### Migrating the Database to Oracle ASM Using RMAN

The following procedure is intended to minimize database downtime. The steps differ slightly depending on whether you are migrating a primary or standby database. The procedure makes the same assumptions described in Preparing to Migrate the Database to Oracle ASM Using RMAN. If you are not migrating the recovery area to Oracle ASM, then you must modify some steps, which are noted.

Note:

The following procedure switches between SQL\*Plus and RMAN, so keep a terminal window open for each utility.

To migrate the database to Oracle ASM:

1. Follow the steps in Preparing to Migrate the Database to Oracle ASM Using RMAN.
2. Restore or create a server parameter file in Oracle ASM storage.
	The steps depend on whether the database is using a server parameter file:
	- If the database is using a server parameter file, then restore it to the Oracle ASM disk group with the following commands, where `sid` is the SID of the instance:
		```
		RMAN> STARTUP MOUNT;
		RMAN> RESTORE SPFILE TO '+DATA/spfilesid.ora';
		RMAN> SHUTDOWN IMMEDIATE;
		```
		- If the database is not using a server parameter file, then create one in Oracle ASM. Run the `CREATE SPFILE` command in SQL\*Plus as follows, where `sid` is the SID of the database:
		```
		SQL> CREATE SPFILE='+DATA/spfilesid.ora' FROM PFILE='?/dbs/initsid.ora';
		```
3. Set Oracle Managed Files initialization parameters to Oracle ASM locations.
	Note:
	If you are not migrating the fast recovery area, then do not change the `DB_RECOVERY_FILE_DEST` and `DB_RECOVERY_FILE_DEST_SIZE` initialization parameter settings. However, you must set `DB_CREATE_ONLINE_LOG_DEST_` `n` parameter to an Oracle ASM location for migration of the online redo logs.
	Set the `DB_CREATE_FILE_DEST` and optional `DB_CREATE_ONLINE_LOG_DEST_` `n` initialization parameters to Oracle ASM disk groups. If the database uses a recovery area, then change the recovery area location to the Oracle ASM disk group. Also, change the recovery area size.
	Run commands in SQL\*Plus as shown in the following example. The example assumes that the size of the fast recovery area is 100 GB and specifies the disk group `+FRA` for the fast recovery area.
	```
	SQL> STARTUP FORCE NOMOUNT;
	SQL> ALTER SYSTEM SET DB_CREATE_FILE_DEST='+DATA' SID='*';
	SQL> ALTER SYSTEM SET DB_RECOVERY_FILE_DEST_SIZE=100G SID='*';
	SQL> ALTER SYSTEM SET DB_RECOVERY_FILE_DEST='+FRA' SID='*';
	```
4. Set the `CONTROL_FILES` initialization parameter to Oracle ASM locations.
	If you are migrating the fast recovery area, then enter the following commands in SQL\*Plus to restart the database instance and set the control file locations to disk groups `+DATA` and `+FRA`:
	```
	SQL> STARTUP FORCE NOMOUNT;
	SQL> ALTER SYSTEM SET CONTROL_FILES='+DATA','+FRA' SCOPE=SPFILE SID='*';
	```
	If you are not migrating the fast recovery area, then enter the following commands in SQL\*Plus to restart the database instance and set the control file locations to disk group `+DATA`:
	```
	SQL> STARTUP FORCE NOMOUNT;
	SQL> ALTER SYSTEM SET CONTROL_FILES='+DATA','+DATA' SCOPE=SPFILE SID='*';
	```
5. Migrate the control file to Oracle ASM and mount the control file.
	Switch to the RMAN terminal to restore the control file. In the following example, `original_cf_name` is a control file name in the initialization parameter file before migration:
	```
	RMAN> STARTUP FORCE NOMOUNT;
	RMAN> RESTORE CONTROLFILE FROM 'original_cf_name';
	RMAN> ALTER DATABASE MOUNT;
	```
6. Migrate the data files to Oracle ASM.
	Use RMAN to switch to the database copy that you created in step "Back up the data files to the Oracle ASM disk group" in Preparing to Migrate the Database to Oracle ASM Using RMAN. The switch renames all the data files to files on Oracle ASM disk groups. Afterward, recover the database. If incremental backups were taken, then RMAN applies them during recovery. For example, enter the following commands at the RMAN prompt:
	```
	SWITCH DATABASE TO COPY;
	RUN
	{
	  ALLOCATE CHANNEL dev1 DEVICE TYPE DISK;
	  ALLOCATE CHANNEL dev2 DEVICE TYPE DISK;
	  ALLOCATE CHANNEL dev3 DEVICE TYPE DISK;
	  ALLOCATE CHANNEL dev4 DEVICE TYPE DISK;
	  RECOVER DATABASE;
	}
	```
7. If the database uses block change tracking or Flashback Database, then enable these features.
	Note:
	If you are not migrating the recovery area, then you do not enable Flashback Database unless you had disabled it previously.
	For example, enter the following statements in SQL\*Plus:
	```
	SQL> ALTER DATABASE ENABLE BLOCK CHANGE TRACKING USING FILE '+DATA';
	SQL> ALTER DATABASE FLASHBACK ON;
	```
8. Place the database in its normal operation mode.
	The normal operational mode depends on whether the database is a primary or standby database:
	- If the database is a primary database, then open it as follows:
		```
		SQL> ALTER DATABASE OPEN;
		```
		- If the database is a standby database, then resume managed recovery mode as follows:
		```
		SQL> ALTER DATABASE RECOVER MANAGED STANDBY DATABASE;
		```
9. Drop the tempfiles and re-create them in Oracle ASM.
	Use SQL\*Plus to re-create the tempfiles. In the following example, the name of the tempfile in the original storage is `tempfile_name`. The name of the temporary tablespace is `temp_tbs_name`.
	```
	SQL> ALTER DATABASE TEMPFILE 'tempfile_name' DROP;
	SQL> ALTER TABLESPACE temp_tbs_name ADD TEMPFILE;
	```
10. Migrate the online redo log files.
	If this is a primary database, then add new log group members in Oracle ASM and drop the old members. You can use the following PL/SQL script to migrate the online redo log groups into an Oracle ASM disk group. The PL/SQL script assumes that the Oracle Managed Files initialization parameters specified in step "Set Oracle Managed Files initialization parameters to Oracle ASM locations" in Migrating the Database to Oracle ASM Using RMAN are set.
11. Optionally, migrate backups and copies in the old fast recovery area to Oracle ASM as follows:
	1. If foreign archived logs exists in the recovery area, then you cannot migrate them to Oracle ASM. Run the following command at the RMAN prompt:
		```
		RMAN> DELETE ARCHIVELOG ALL;
		```
		2. Back up archived redo log files, backup sets, and data file copies to Oracle ASM. For example, run the following command at the RMAN prompt:
		```
		RUN
		{
		  ALLOCATE CHANNEL dev1 DEVICE TYPE DISK;
		  ALLOCATE CHANNEL dev2 DEVICE TYPE DISK;
		  ALLOCATE CHANNEL dev3 DEVICE TYPE DISK;
		  ALLOCATE CHANNEL dev4 DEVICE TYPE DISK;
		  BACKUP AS COPY ARCHIVELOG ALL DELETE INPUT;
		  BACKUP BACKUPSET ALL DELETE INPUT;
		  BACKUP AS COPY DATAFILECOPY ALL DELETE INPUT;
		}
		```

Example 8-1 Migrating the online redo logs

```
SET SERVEROUTPUT ON;
DECLARE
   CURSOR rlc IS
      SELECT GROUP# GRP, THREAD# THR, BYTES, 'NO' SRL
      FROM   V$LOG
      UNION
      SELECT GROUP# GRP, THREAD# THR, BYTES, 'YES' SRL
      FROM   V$STANDBY_LOG
      ORDER BY 1;
   stmt     VARCHAR2(2048);
BEGIN
   FOR rlcRec IN rlc LOOP
      IF (rlcRec.srl = 'YES') THEN
         stmt := 'ALTER DATABASE ADD STANDBY LOGFILE THREAD ' ||
                 rlcRec.thr || ' SIZE ' || rlcRec.bytes;
         EXECUTE IMMEDIATE stmt;
         stmt := 'ALTER DATABASE DROP STANDBY LOGFILE GROUP ' || rlcRec.grp;
         EXECUTE IMMEDIATE stmt;
      ELSE
         stmt := 'ALTER DATABASE ADD LOGFILE THREAD ' ||
                 rlcRec.thr || ' SIZE ' ||  rlcRec.bytes;
         EXECUTE IMMEDIATE stmt;
         BEGIN
            stmt := 'ALTER DATABASE DROP LOGFILE GROUP ' || rlcRec.grp;
            DBMS_OUTPUT.PUT_LINE(stmt);
            EXECUTE IMMEDIATE stmt;
         EXCEPTION
            WHEN OTHERS THEN
               EXECUTE IMMEDIATE 'ALTER SYSTEM SWITCH LOGFILE';
               EXECUTE IMMEDIATE 'ALTER SYSTEM CHECKPOINT GLOBAL';
               EXECUTE IMMEDIATE stmt;
         END;
      END IF;
   END LOOP;
END;
/
```

### Migrating a Database from Oracle ASM to Alternative Storage

Migrating a database from Oracle ASM to an alternative storage system is essentially the reverse of the migration to Oracle ASM. Modify the steps in Preparing to Migrate the Database to Oracle ASM Using RMAN and Migrating the Database to Oracle ASM Using RMAN as follows:

- If the procedure specifies Oracle Managed Files locations, then alter the procedure to use locations in alternative storage.
- If the `FORMAT` clause of the `BACKUP` command specifies an Oracle ASM location, then change the backup format to an alternative storage location.
- If a file name used in a SQL statement is an Oracle ASM location, then change it to a file name in the alternative storage location.

### Moving Data Files Between Oracle ASM Disk Groups Using RMAN

You may want to move an active data file in an `ARCHIVELOG` mode database from one Oracle ASM disk group to another. You can use RMAN `BACKUP` `AS` `COPY` to copy the data file to the new disk group and `SET` `NEWNAME` and `SWITCH` commands to rename the data file in the control file.

You can also use the `ALTER` `DATABASE` `MOVE` `DATAFILE`. SQL statement to move data files. For information about moving data files online with `ALTER` `DATABASE` `MOVE` `DATAFILE`, refer to [Moving Data Files Between Disk Groups With ALTER DATABASE](asm-files-directories-templates.md).

For this scenario using RMAN, assume that you are using disk groups `DATA` and `USERDATA` and you want to move the data file `users.261.689589837` to disk group `USERDATA`. Ensure that `ARCHIVELOG` mode is enabled for the database before beginning the procedure to move data files.

To move a data file from one Oracle ASM disk group to another disk group using the RMAN `BACKUP` `AS` `COPY` procedure with the `SET` `NEWNAME` and `SWITCH` commands, perform the following steps.

1. Start RMAN and connect to the target database.
	For example:
	```
	$ rman
	RMAN> CONNECT TARGET SYS@orcl
	target database Password: XXXXXXXXX
	connected to target database: ORCL (DBID=1217369048)
	```
2. Generate a report that shows the names of the data files.
	Run the following `REPORT` command after connecting RMAN to the target database. Note the data file name of the file to be moved.
	For example:
	```
	RMAN> REPORT SCHEMA;
	Report of database schema for database with db_unique_name ORCL
	 
	List of Permanent Datafiles
	===========================
	File Size(MB) Tablespace           RB segs Datafile Name
	---- -------- -------------- ------- ------------------------
	1    740      SYSTEM         ***     +DATA/orcl/datafile/system.258.689589737
	2    570      SYSAUX         ***     +DATA/orcl/datafile/sysaux.259.689589785
	3    55       UNDOTBS1       ***     +DATA/orcl/datafile/undotbs1.260.689589831
	4    5        USERS          ***     +DATA/orcl/datafile/users.261.689589837
	List of Temporary Files
	=======================
	File Size(MB) Tablespace           Maxsize(MB) Tempfile Name
	---- -------- -------------- ----------- --------------------
	1    20       TEMP           32767       +DATA/orcl/tempfile/temp.262.689589851
	```
3. Back up the data file to the new Oracle ASM disk group.
	Run the `BACKUP` `AS` `COPY` command to back up the data file on `DATA` to `USERDATA`.
	For example:
	```
	RMAN> BACKUP AS COPY
	        DATAFILE "+DATA/orcl/datafile/users.261.689589837"
	        FORMAT   "+USERDATA";
	Starting backup at 16-JUN-09
	allocated channel: ORA_DISK_1
	channel ORA_DISK_1: SID=51 device type=DISK
	channel ORA_DISK_1: starting datafile copy
	input datafile file number=00004 name=+DATA/orcl/datafile/users.261.689589837
	output file name=+USERDATA/orcl/datafile/users.256.689682663
	  tag=TAG20090616T103101 RECID=13 STAMP=689682663
	channel ORA_DISK_1: datafile copy complete, elapsed time: 00:00:01
	Finished backup at 16-JUN-09
	```
	You could also specify the data file by the data file number and data file type.
	For example:
	```
	BACKUP AS COPY
	  DATAFILE 4
	  FORMAT   "+USERDATA";
	```
4. Offline the data file that you intend to move to a new disk group.
	Run the following `SQL` command in the RMAN client. Use two single quotation marks around the name of the data file, not double quotation marks.
	For example:
	```
	RMAN> SQL "ALTER DATABASE DATAFILE 
	       ''+DATA/orcl/datafile/users.261.689589837'' OFFLINE";
	sql statement: ALTER DATABASE DATAFILE
	     ''+DATA/orcl/datafile/users.261.689589837''  OFFLINE
	```
5. Point the control file to the newly created copy of the data file.
	Run the `SWITCH...TO COPY` command in the RMAN client. The `TO` `COPY` option of `SWITCH` switches the data file to the most recent copy of the data file.
	For example:
	```
	RMAN> SWITCH DATAFILE "+DATA/orcl/datafile/users.261.689589837" TO COPY;
	datafile 4 switched to datafile copy
	    "+USERDATA/orcl/datafile/users.256.689682663"
	```
	The output of this command displays the new name of the data file.
6. Recover the renamed data file.
	Run the `RECOVER` command in the RMAN client.
	For example:
	```
	RMAN> RECOVER DATAFILE "+USERDATA/orcl/datafile/users.256.689682663";
	Starting recover at 16-JUN-09
	using channel ORA_DISK_1
	starting media recovery
	media recovery complete, elapsed time: 00:00:01
	Finished recover at 16-JUN-09
	```
7. Bring the data file online.
	Run the `SQL` command in the RMAN client. Use two single quotation marks around the name of the data file, not double quotation marks.
	For example:
	```
	RMAN> SQL "ALTER DATABASE DATAFILE
	      ''+USERDATA/orcl/datafile/users.256.689682663'' ONLINE";
	sql statement: ALTER DATABASE DATAFILE
	   ''+USERDATA/orcl/datafile/users.256.689682663'' ONLINE
	```
8. Delete the data file copy from the original Oracle ASM disk group.
	In this scenario, `+DATA/orcl/datafile/users.261.689589837` is the original data file in `DATA`. Because you issued `SET NEWNAME` and `SWITCH` commands for this data file, the original file is now recorded in the RMAN repository as a data file copy. Run a `DELETE` command in the RMAN client to remove this file.
	For example:
	```
	RMAN> DELETE DATAFILECOPY "+DATA/orcl/datafile/users.261.689589837";
	released channel: ORA_DISK_1
	allocated channel: ORA_DISK_1
	channel ORA_DISK_1: SID=51 device type=DISK
	List of Datafile Copies
	=======================
	Key     File S Completion Time Ckp SCN    Ckp Time       
	------- ---- - --------------- ---------- ---------------
	14      4    A 16-JUN-09       864471     16-JUN-09      
	        Name: +DATA/orcl/datafile/users.261.689589837
	        Tag: TAG20090615T084217
	Do you really want to delete the above objects (enter YES or NO)? y
	deleted datafile copy
	datafile copy file name=+DATA/orcl/datafile/users.261.689589837 RECID=14 STAMP=689683255
	Deleted 1 objects
	```