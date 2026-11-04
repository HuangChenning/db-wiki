---
title: "Backup and Recovery User's Guide"
book: "Database Backup and Recovery User's Guide"
doc_id: F31836-11
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/bradv/user-managed-database-backups.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-users-guide
---

You can back up an Oracle database in a user-managed backup and recovery strategy, that is, a strategy that does not depend on using Recovery Manager (RMAN).

Note:

A multitenant container database is the only supported architecture in Oracle Database 21c. While the documentation is being revised, legacy terminology may persist. In most cases, "database" and "non-CDB" refer to a CDB or PDB, depending on context. In some contexts, such as upgrades, "non-CDB" refers to a non-CDB from a previous release.

### 29.1 Querying V$ Views to Obtain Backup Information

Before making a backup, you must identify all the files in your database and decide what to back up. You can use V$ views to obtain this information.

This section contains the following topics:

- Listing Database Files Before a Backup
- Determining Data File Status for Online Tablespace Backups

#### 29.1.1 Listing Database Files Before a Backup

Use the `V$DATAFILE` and `V$CONTROLFILE` views to identify the data files and control files for your database. This same procedure works whether you named these files manually or allowed Oracle Managed Files to name them.

Caution:

Never back up online redo log files.

To list data files and control files:

1. Start SQL\*Plus and query `V$DATAFILE` to obtain a list of data files. For example, enter:
	```
	SELECT NAME FROM V$DATAFILE;
	```
	You can also join the `V$TABLESPACE` and `V$DATAFILE` views to obtain a listing of data files along with their associated tablespaces:
	```
	SELECT   t.NAME "Tablespace", f.NAME "Data File"
	FROM     V$TABLESPACE t, V$DATAFILE f
	WHERE    t.TS# = f.TS#
	ORDER BY t.NAME;
	```
2. Obtain the file names of the current control files by querying the `V$CONTROLFILE` view. For example, issue the following query:
	```
	SELECT NAME FROM V$CONTROLFILE;
	```
	You only need to back up one copy of a multiplexed control file.
3. If you plan to perform control file backup with the `ALTER` `DATABASE` `BACKUP` `CONTROLFILE` `TO` `'` `filename` `'` statement, then save a list of all data files and online redo log files with the control file backup. Because the current database structure may not match the database structure at the time a given control file backup was created, saving a list of files recorded in the backup control file can aid the recovery procedure.

#### 29.1.2 Determining Data File Status for Online Tablespace Backups

To check whether a data file is part of a current online tablespace backup, query the `V$BACKUP` view.

This view is useful only for user-managed online tablespace backups, because neither RMAN backups nor offline tablespace backups require the data files of a tablespace to be in [backup mode](glossary.md). Some user-managed backup procedures require you to place the tablespace in backup mode to protect against the possibility of a fractured block. However, updates to the database create more than the usual amount of redo in backup mode.

The `V$BACKUP` view is most useful when the database is open. It is also useful immediately after an instance failure because it shows the backup status of the files at the time of the failure. Use this information to determine whether you have left any tablespaces in backup mode.

`V$BACKUP` is not useful if the control file currently in use is a restored backup or a new control file created after the media failure occurred. A restored or re-created control file does not contain the information that the database needs to populate `V$BACKUP` accurately. Also, if you have restored a backup of a file, this file's `STATUS` in `V$BACKUP` reflects the backup status of the older version of the file, not the most current version. Thus, this view can contain misleading data about restored files.

For example, the following query displays which data files are currently included in a tablespace that has been placed in backup mode:

```
SELECT t.name AS "TB_NAME", d.file# as "DF#", d.name AS "DF_NAME", b.status
FROM   V$DATAFILE d, V$TABLESPACE t, V$BACKUP b
WHERE  d.TS#=t.TS#
AND    b.FILE#=d.FILE#
AND    b.STATUS='ACTIVE';
```

The following sample output shows that the `tools` and `users` tablespaces currently have `ACTIVE` status:

```
TB_NAME                 DF#        DF_NAME                           STATUS
----------------------  ---------- --------------------------------  ------
TOOLS                   7          /oracle/oradata/trgt/tools01.dbf  ACTIVE
USERS                   8          /oracle/oradata/trgt/users01.dbf  ACTIVE
```

In the `STATUS` column, `NOT` `ACTIVE` indicates that the file is not currently in backup mode (that is, you have not executed the `ALTER` `TABLESPACE` `...` `BEGIN` `BACKUP ` or `ALTER DATABASE BEGIN BACKUP` statement), whereas `ACTIVE` indicates that the file is currently in backup mode.

### 29.2 Making User-Managed Backups of Databases

You can create user-manged backups of CDBs and PDBs.

You can make a consistent whole database backup of all files in a database after the database has been shut down with the `NORMAL`, `IMMEDIATE`, or `TRANSACTIONAL` options. A whole database backup taken while the database is open or after an instance failure or `SHUTDOWN ABORT` command is inconsistent. In such cases, the files are inconsistent with the database checkpoint SCN.

You can make a whole database backup if a database is operating in either `ARCHIVELOG` or `NOARCHIVELOG` mode. If you run the database in `NOARCHIVELOG` mode, however, then the backup must be consistent; that is, you must shut down the database cleanly before the backup.

The set of backup files that results from a consistent whole database backup is consistent because all files are checkpointed to the same SCN. You can restore the consistent database backup without further recovery. After restoring the backup files, you can perform additional recovery steps to recover the database to a more current time if the database is operated in `ARCHIVELOG` mode. Also, you can take inconsistent whole database backups if your database is in `ARCHIVELOG` mode.

Control files play a crucial role in database restore and recovery. For databases running in `ARCHIVELOG` mode, Oracle recommends that you back up control files with the `` ALTER DATABASE BACKUP CONTROLFILE TO '`filename` `` `'` statement.

See Also:

" Making User-Managed Backups of the Control File " for more information about backing up control files

To make a consistent whole database backup for a CDB:

1. Open SQL\*Plus.
2. Connect to the root as a common user with the `SYSDBA` or `SYSBACKUP` system privilege, as described in " [Connecting as Target to the Root](starting-interacting-with-rman-client.md) ".
3. If the database is open, then use SQL\*Plus to shut down the database with the `NORMAL`, `IMMEDIATE`, or `TRANSACTIONAL` options.
4. Use an operating system utility to make backups of all data files and all control files specified by the `CONTROL_FILES` parameter of the initialization parameter file. Also, back up the initialization parameter file and other Oracle product initialization files. To find these files, do a search for `*.ora` starting in your Oracle home directory and recursively search all of its subdirectories.
	For example, you can back up the data files, control files, and archived logs to `/disk3/backup` as follows:
	```
	% cp $ORACLE_HOME/oradata/cdb1/*.dbf /disk3/backup
	% cp $ORACLE_HOME/oradata/cdb1/arch/* /disk3/backup/arch
	```
5. Restart the database with the `STARTUP` command in SQL\*Plus.

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=SQLRF00802) for more information about using `ALTER DATABASE` command for CDBs
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=MULTI-GUID-045DE684-6680-4099-A49E-2F5B5FA59670) for more information about starting up and shutting down a database

To make a consistent backup of a PDB:

1. Open SQL\*Plus.
2. Connect to the PDB as a common user or local user with the `SYSDBA` or `SYSBACKUP` system privilege, as described in " [Connecting as Target to a PDB](starting-interacting-with-rman-client.md) ".
3. Begin the backup with the SQL `ALTER DATABASE` command.
	```
	ALTER DATABASE BEGIN BACKUP;
	```
4. Use an operating system utility to copy the data files belonging to the PDB to a backup device.
5. End the backup with the SQL `ALTER DATABASE` command.
	```
	ALTER DATABASE END BACKUP;
	```

### 29.3 Making User-Managed Backups of Tablespaces and Data Files

The technique for making user-managed backups of tablespaces and data files depends on whether the files are offline or online.

This section contains the following topics:

- Making User-Managed Backups of Offline Tablespaces and Data Files
- Making User-Managed Backups of Online Tablespaces and Data Files

#### 29.3.1 Making User-Managed Backups of Offline Tablespaces and Data Files

Identify the data files associated with a tablespace before creating a user-managed backup of the tablespace.

Note the following guidelines when backing up offline tablespaces:

- You cannot take offline the `SYSTEM` tablespace or a tablespace with active undo segments. The following technique cannot be used for such tablespaces.
- Assume that a table is in tablespace `Primary` and its index is in tablespace `Index`. Taking tablespace `Index` offline while leaving tablespace `Primary` online can cause errors when data manipulation language (DML) is issued against the indexed tables located in `Primary`. The problem appears only when the access method chosen by the optimizer must access the indexes in the `Index` tablespace.

To back up offline tablespaces:

1. Open SQL\*Plus.
2. Perform one of the following operations:
	- To back up offline tablespaces in the root, connect to the root as a common user with the `SYSDBA` or `SYSBACKUP` system privilege.
	- To back up offline tablespaces in a PDB, connect to the PDB as a common user or local user with `SYSDBA` or `SYSBACKUP` system privilege.
3. Before beginning a backup of a tablespace, identify the tablespace's data files by querying the `DBA_DATA_FILES` view. For example, assume that you want to back up the `users` tablespace. Enter the following statement in SQL\*Plus:
	```
	SELECT TABLESPACE_NAME, FILE_NAME
	  FROM SYS.DBA_DATA_FILES
	  WHERE TABLESPACE_NAME = 'USERS';
	 
	TABLESPACE_NAME                   FILE_NAME
	-------------------------------   --------------------------------
	USERS                             /oracle/oradata/trgt/users01.dbf
	```
	In this example, `/oracle/oradata/trgt/users01.dbf ` is a fully specified file name corresponding to the data file in the `users` tablespace.
4. Take the tablespace offline using normal priority if possible, because it guarantees that you can subsequently bring the tablespace online without having to recover it. For example:
	```
	SQL> ALTER TABLESPACE users OFFLINE NORMAL;
	```
5. Back up the offline data files. For example:
	```
	% cp /oracle/oradata/trgt/users01.dbf /d2/users01_'date "+%m_%d_%y"'.dbf
	```
6. Bring the tablespace online. For example:
	```
	ALTER TABLESPACE users ONLINE;
	```
	Note:
	If you took the tablespace offline using temporary or immediate priority, then you cannot bring the tablespace online unless you perform tablespace recovery.
7. Archive the unarchived redo logs so that the redo required to recover the tablespace backup is archived. For example, enter:
	```
	ALTER SYSTEM ARCHIVE LOG CURRENT;
	```

#### 29.3.2 Making User-Managed Backups of Online Tablespaces and Data Files

You can back up all or only specific data files of an online tablespace while the database is open. The procedure differs depending on whether the online tablespace is read/write or read-only.

Note:

Do not back up temporary tablespaces.

##### 29.3.2.1 Making User-Managed Backups of Online Read/Write Tablespaces

You must put a read/write tablespace in backup mode to make user-managed data file backups when the tablespace is online and the database is open.

The `ALTER TABLESPACE...BEGIN BACKUP` statement places a tablespace in backup mode. In backup mode, the database copies whole changed data blocks into the redo stream. After you take the tablespace out of backup mode with the `ALTER TABLESPACE...END BACKUP` or `ALTER DATABASE...END                     BACKUP` statement, the database advances the data file checkpoint SCN to the current database checkpoint SCN.

When restoring a data file backed up in this way, the database asks for the appropriate set of redo log files to apply if recovery is needed. The redo logs contain all changes required to recover the data files and make them consistent.

To back up online read/write tablespaces in an open database:

1. Before beginning a backup of a tablespace, use the `DBA_DATA_FILES` data dictionary view to identify all of the data files in the tablespace. For example, assume that you want to back up the `users` tablespace. Enter the following:
	```
	SELECT TABLESPACE_NAME, FILE_NAME
	FROM   SYS.DBA_DATA_FILES
	WHERE  TABLESPACE_NAME = 'USERS';
	 
	TABLESPACE_NAME                   FILE_NAME
	-------------------------------   --------------------
	USERS                             /oracle/oradata/trgt/users01.dbf
	USERS                             /oracle/oradata/trgt/users02.dbf
	```
2. Mark the beginning of the online tablespace backup. For example, the following statement marks the start of an online backup for the tablespace `users`:
	```
	SQL> ALTER TABLESPACE users BEGIN BACKUP;
	```
	Caution:
	If you do not use `BEGIN BACKUP` to mark the beginning of an online tablespace backup and wait for this statement to complete before starting your copies of online tablespaces, then the data file copies produced are not usable for subsequent recovery operations. Attempting to recover such a backup is risky and can return errors that result in inconsistent data. For example, the attempted recovery operation can issue a fuzzy file warning, and can lead to an inconsistent database that you cannot open.
3. Back up the online data files of the online tablespace with operating system commands. For example, Linux and UNIX users might enter:
	```
	% cp /oracle/oradata/trgt/users01.dbf /d2/users01_'date "+%m_%d_%y"'.dbf
	% cp /oracle/oradata/trgt/users02.dbf /d2/users02_'date "+%m_%d_%y"'.dbf
	```
4. After backing up the data files of the online tablespace, run the SQL statement `ALTER TABLESPACE` with the `END BACKUP` option. For example, the following statement ends the online backup of the tablespace `users`:
	```
	SQL> ALTER TABLESPACE users END BACKUP;
	```
5. Archive the unarchived redo logs so that the redo required to recover the tablespace backup is archived. For example, enter:
	```
	SQL> ALTER SYSTEM ARCHIVE LOG CURRENT;
	```
	Caution:
	If you fail to take the tablespace out of backup mode, then Oracle Database continues to write copies of data blocks in this tablespace to the online redo logs, causing performance problems. Also, you receive an `ORA-01149` error if you try to shut down the database with the tablespaces still in backup mode.

##### 29.3.2.2 Making Multiple User-Managed Backups of Online Read/Write Tablespaces

When backing up several online tablespaces, depending on your needs, you can back them up either serially or in parallel.

###### 29.3.2.2.1 Backing Up Online Tablespaces in Parallel

You can simultaneously create data file copies of multiple tablespaces requiring backups in backup mode.

Note, however, that by putting all tablespaces in online mode together, you can generate large redo logs if there is heavy update activity on the affected tablespaces, because the redo must contain a copy of each changed data block in each changed data file. Be sure to consider the size of the likely redo before using the procedure outlined here.

To back up online tablespaces in parallel:

1. Prepare the online tablespaces for backup by issuing all necessary `ALTER TABLESPACE` statements together. For example, put tablespaces `users`, `tools`, and `indx` in backup mode as follows:
	```
	SQL> ALTER TABLESPACE users BEGIN BACKUP;
	SQL> ALTER TABLESPACE tools BEGIN BACKUP;
	SQL> ALTER TABLESPACE indx BEGIN BACKUP;
	```
	If you are backing up all tablespaces, you can use this command:
	```
	SQL> ALTER DATABASE BEGIN BACKUP;
	```
2. Back up all files of the online tablespaces. For example, a Linux or UNIX user might back up data files with the `*.dbf` suffix as follows:
	```
	% cp $ORACLE_HOME/oradata/trgt/*.dbf /disk2/backup/
	```
3. Take the tablespaces out of backup mode as in the following example:
	```
	SQL> ALTER TABLESPACE users END BACKUP;
	SQL> ALTER TABLESPACE tools END BACKUP;
	SQL> ALTER TABLESPACE indx END BACKUP;
	```
	Again, if you are handling all data files together, you can use the `ALTER DATABASE` command instead of `ALTER TABLESPACE`:
	```
	SQL> ALTER DATABASE END BACKUP;
	```
4. Archive the online redo logs so that the redo required to recover the tablespace backups is available for later media recovery. For example, enter:
	```
	SQL> ALTER SYSTEM ARCHIVE LOG CURRENT;
	```

###### 29.3.2.2.2 Backing Up Online Tablespaces Serially

You can place all tablespaces requiring online backups in backup mode one at a time.

Oracle recommends the serial backup option because it minimizes the time between `ALTER TABLESPACE...BEGIN/END BACKUP` statements. During online backups, more redo information is generated for the tablespace because whole data blocks are copied into the redo log.

To back up online tablespaces serially:

1. Prepare a tablespace for online backup. For example, to put tablespace `users` in backup mode enter the following:
	```
	SQL> ALTER TABLESPACE users BEGIN BACKUP;
	```
	In this case you probably do not want to use `ALTER                             DATABASE BEGIN BACKUP` to put all tablespaces in backup mode simultaneously, because of the unnecessary volume of redo log information generated for tablespaces in online mode.
2. Back up the data files in the tablespace. For example, enter:
	```
	% cp /oracle/oradata/trgt/users01.dbf /d2/users01_'date "+%m_%d_%y"'.dbf
	```
3. Take the tablespace out of backup mode. For example, enter:
	```
	SQL> ALTER TABLESPACE users END BACKUP;
	```
4. Repeat this procedure for each remaining tablespace.
5. Archive the unarchived redo logs so that the redo required to recover the tablespace backups is archived. For example, enter:
	```
	SQL> ALTER SYSTEM ARCHIVE LOG CURRENT;
	```

##### 29.3.2.3 Ending a Backup After an Instance Failure or SHUTDOWN ABORT

Multiple reasons can cause a tablespace backup to fail and thereby require failure recovery.

The following situations can cause a tablespace backup to fail and be incomplete:

- The backup completed, but you did not run the `ALTER TABLESPACE...END                             BACKUP` statement.
- An instance failure or `SHUTDOWN ABORT` interrupted the backup.

Whenever recovery from a failure is required, if a data file is in backup mode when an attempt is made to open it, then the database does not open the data file until either a recovery command is issued, or the data file is taken out of backup mode.

For example, the database may display a message such as the following at startup:

```
ORA-01113: file 12 needs media recovery
ORA-01110: data file 12: '/oracle/dbs/tbs_41.f'
```

If the database indicates that the data files for multiple tablespaces require media recovery because you forgot to end the online backups for these tablespaces, then so long as the database is mounted, running the `ALTER DATABASE END                     BACKUP` statement takes all the data files out of backup mode simultaneously.

In high availability situations, and in situations when no database administrator (DBA) is monitoring the database, the requirement for user intervention is intolerable. Hence, you can write a failure recovery script that does the following:

1. Mounts the database
2. Runs the `ALTER DATABASE END BACKUP` statement
3. Runs the `ALTER DATABASE OPEN` statement, enabling the system to start automatically

An automated crash recovery script containing `ALTER DATABASE END                     BACKUP` is especially useful in the following situations:

- All nodes in an Oracle Real Application Clusters (Oracle RAC) configuration fail.
- One node fails in a (that is, a cluster that is not an Oracle RAC configuration in which the secondary node must mount and recover the database when the first node fails).

Alternatively, you can take the following manual measures after the system fails with tablespaces in backup mode:

- Recover the database and avoid issuing `END BACKUP` statements altogether.
- Mount the database, then run the `ALTER TABLESPACE...END BACKUP` statement for each tablespace still in backup mode.

###### 29.3.2.3.1 Ending Backup Mode with the ALTER DATABASE END BACKUP Statement

You can run the `ALTER DATABASE END BACKUP` statement when you have multiple tablespaces still in backup mode. The primary purpose of this command is to allow a crash recovery script to restart a failed system without DBA intervention.

You can also perform the following procedure manually.

To take tablespaces out of backup mode simultaneously:

1. Mount but do not open the database. For example, enter:
	```
	SQL> STARTUP MOUNT
	```
2. If you are performing this procedure manually (that is, not as part of a failure recovery script), query the `V$BACKUP` view to list the data files of the tablespaces that were being backed up before the database was restarted:
	```
	SQL>  SELECT * FROM V$BACKUP WHERE STATUS = 'ACTIVE';
	FILE#      STATUS             CHANGE#    TIME       CON_ID
	---------- ------------------ ---------- ---------  -------
	        12 ACTIVE                  20863 25-NOV-02        0
	        13 ACTIVE                  20863 25-NOV-02        0
	        20 ACTIVE                  20863 25-NOV-02        0
	 3 rows selected.
	```
3. Issue the `ALTER DATABASE END BACKUP` statement to take all data files currently in backup mode out of backup mode. For example, enter:
	```
	SQL> ALTER DATABASE END BACKUP;
	```
	You can use this statement only when the database is mounted but not open. If the database is open, then use `ALTER TABLESPACE...END                                                   BACKUP` or `ALTER DATABASE                                                   DATAFILE...END BACKUP` for each affected tablespace or data file.
	Caution:
	Do not use `ALTER DATABASE END                                                   BACKUP` if you have restored any of the affected files from a backup.

###### 29.3.2.3.2 Ending Backup Mode with the SQL\*Plus RECOVER Command

Using the SQL\*Plus `RECOVER` command to respond to a failed online user-managed backup is useful when you are not sure whether someone has restored a backup.

Because, if someone has indeed restored a backup, then the `RECOVER` command brings the backup up-to-date. Only run the `ALTER DATABASE END                     BACKUP` or `ALTER TABLESPACE...END BACKUP` statement if you are sure that the files are current.

Note:

The `RECOVER` command method is slow because the database must scan redo generated from the beginning of the online backup.

To take tablespaces out of backup mode with the RECOVER command:

1. Mount the database. For example, enter:
	```
	SQL> STARTUP MOUNT
	```
2. Recover the database as usual. For example, enter:
	```
	SQL> RECOVER DATABASE
	```
3. Use the `V$BACKUP` view to confirm that there are no active data files:
	```
	SQL>  SELECT * FROM V$BACKUP WHERE STATUS = 'ACTIVE';
	no rows selected.
	```

See Also:

[Performing User-Managed Database Flashback and Recovery](user-managed-flashback-dbpitr.md) for information about recovering a database

##### 29.3.2.4 Making User-Managed Backups of Read-Only Tablespaces

When backing up an online read-only tablespace, you can simply back up the online data files. You do not have to place the tablespace in backup mode because the database is not permitting changes to the data files.

If the set of read-only tablespaces is self-contained, then in addition to backing up the tablespaces with operating system commands, you can also export the tablespace metadata with the transportable tablespace functionality. If a media error or a user error occurs (such as accidentally dropping a table in the read-only tablespace), you can transport the tablespace back into the database.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=ADMIN11394) to learn how to transport tablespaces

To back up online read-only tablespaces in an open database:

1. Open SQL\*Plus.
2. Perform one of the following operations:
	- To back up offline tablespaces in the root, connect to the root as a common user with the `SYSDBA` or `SYSBACKUP` system privilege.
	- To back up offline tablespaces in a PDB, connect to the PDB as a common user or local user with `SYSDBA` or `SYSBACKUP` system privilege.
3. Query the `DBA_TABLESPACES` view to determine which tablespaces are read-only. For example, run this query:
	```
	SELECT TABLESPACE_NAME, STATUS 
	FROM DBA_TABLESPACES
	WHERE STATUS = 'READ ONLY';
	```
4. Before beginning a backup of a read-only tablespace, identify all of the tablespace's data files by querying the `DBA_DATA_FILES` data dictionary view. For example, assume that you want to back up the `history` tablespace:
	```
	SELECT TABLESPACE_NAME, FILE_NAME
	FROM SYS.DBA_DATA_FILES
	WHERE TABLESPACE_NAME = 'HISTORY';
	 
	TABLESPACE_NAME                   FILE_NAME
	-------------------------------   --------------------
	HISTORY                           /oracle/oradata/trgt/history01.dbf
	HISTORY                           /oracle/oradata/trgt/history02.dbf
	```
5. Back up the online data files of the read-only tablespace with operating system commands. You do not have to take the tablespace offline or put the tablespace in backup mode because users are automatically prevented from making changes to the read-only tablespace. For example:
	```
	% cp $ORACLE_HOME/oradata/trgt/history*.dbf  /disk2/backup/
	```
	Note:
	When restoring a backup of a read-only tablespace, take the tablespace offline, restore the data files, then bring the tablespace online. A backup of a read-only tablespace is still usable if the read-only tablespace is made read/write after the backup, but the restored backup requires recovery.
6. Optionally, export the metadata in the read-only tablespace. By using the transportable tablespace feature, you can quickly restore the data files and import the metadata in case of media failure or user error. For example, export the metadata for tablespace `history` as follows:
	```
	% expdp DIRECTORY=dpump_dir1 DUMPFILE=hs.dmp TRANSPORT_TABLESPACES=history 
	  LOGFILE=tts.log
	```
	See Also:
	[Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=REFRN002) for more information about the `DBA_DATA_FILES` and `DBA_TABLESPACES` views

### 29.4 Making User-Managed Backups of the Control File

Back up the control file of a database after making a structural modification to a database operating in `ARCHIVELOG` mode. To back up a database's control file, you must have the `ALTER` `DATABASE` system privilege.

This section contains the following topics:

- Backing Up the Control File to a Binary File
- Backing Up the Control File to a Trace File

#### 29.4.1 Backing Up the Control File to a Binary File

The primary method for backing up the control file is to use a SQL statement to generate a binary file. A binary backup is preferable to a trace file backup because it contains additional information such as the archived log history, offline range for read-only and offline tablespaces, and backup sets and copies (if you use RMAN). If `COMPATIBLE` is 10.2 or higher, binary control file backups include temp file entries.

To back up the control file after a structural change:

1. Make the desired change to the database. For example, you may create a tablespace:
	```
	CREATE TABLESPACE tbs_1 DATAFILE 'file_1.f' SIZE 10M;
	```
2. Back up the database's control file, specifying a file name for the output binary file. The following example backs up a control file to `/disk1/backup/cf.bak`:
	```
	ALTER DATABASE BACKUP CONTROLFILE TO '/disk1/backup/cf.bak' REUSE;
	```
	Specify `REUSE` to make the new control file overwrite one that currently exists.

#### 29.4.2 Backing Up the Control File to a Trace File

You can back up the control file to a text file that contains a `CREATE CONTROLFILE` statement. You can edit the trace file to create a script that creates a new control file based on the control file that was current when you created the trace file.

If you specify neither the `RESETLOGS` nor `NORESETLOGS` option in the SQL statement, then the resulting trace file contains versions of the control file for both `RESETLOGS` and `NORESETLOGS` options. Temp file entries are included in the output using `ALTER TABLESPACE ... ADD TEMPFILE` statements.

To avoid recovering offline normal or read-only tablespaces, edit them out of the `CREATE` `CONTROLFILE` statement. When you open the database with the re-created control file, the database marks these omitted files as `MISSING`. You can run an `ALTER` `DATABASE` `RENAME` `FILE` statement to rename them to their original file names.

The trace file containing the `CREATE CONTROLFILE` statement is stored in a subdirectory determined by the `DIAGNOSTIC_DEST` initialization parameter. You can look in the database alert log for the name and location of the trace file to which the `CREATE CONTROLFILE` statement was written. See [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=ADMIN11267) to learn how to locate the alert log.

To back up the control file to a trace file:

1. Mount or open the database.
2. ```
	ALTER DATABASE BACKUP CONTROLFILE TO TRACE;
	```

See Also:

" [Recovery of Read-Only Files with a Re-Created Control File](user-managed-recovery-advanced.md) " for special issues relating to read-only, offline normal, and temporary files included in `CREATE` `CONTROLFILE` statements

### 29.5 Making User-Managed Backups of Archived Redo Logs

To save disk space in your primary archiving location, you may want to back up archived logs to tape or to an alternative disk location. If you archive to multiple locations, then only back up one copy of each log sequence number.

To back up archived redo logs:

1. To determine which archived redo log files the database has generated, query `V$ARCHIVED_LOG`. For example, run the following query:
	```
	SELECT THREAD#,SEQUENCE#,NAME 
	FROM V$ARCHIVED_LOG;
	```
2. Back up one copy of each log sequence number by using an operating system utility. This example backs up all logs in the primary archiving location to a disk devoted to log backups:
	```
	% cp $ORACLE_HOME/oracle/trgt/arch/* /disk2/backup/arch
	```
	See Also:
	[Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=REFRN002) for more information about the data dictionary views

### 29.6 Making User-Managed Backups in SUSPEND Mode

This section contains the following topics:

- About the Suspend/Resume Feature
- Making Backups in a Suspended Database

#### 29.6.1 About the Suspend/Resume Feature

Some third-party tools allow you to mirror a set of disks or logical devices, that is, maintain an exact duplicate of the primary data in another location, and then split the mirror. Splitting the mirror involves separating the copies so that you can use them independently.

With the `SUSPEND` / `RESUME` functionality, you can suspend I/O to the database, then split the mirror and make a backup of the split mirror. By using this feature, which complements the backup mode functionality, you can suspend database I/Os so that no new I/O can be performed. You can then access the suspended database to make backups without I/O interference.

Usually, you do not need to use `SUSPEND` / `RESUME` to make split mirror backups, although it is necessary if your system requires the database cache to be free of dirty buffers before a volume can be split. Some RAID devices benefit from suspending writes while the split operation is occurring; your RAID vendor can advise you on whether your system would benefit from this feature.

The `ALTER` `SYSTEM` `SUSPEND` statement suspends the database by halting I/Os to data file headers, data files, and control files. When the database is suspended, all preexisting I/O operations can complete; however, any new database I/O access attempts are queued.

The `ALTER` `SYSTEM` `SUSPEND` and `ALTER` `SYSTEM` `RESUME` statements operate on the database and not just the instance. If the `ALTER` `SYSTEM` `SUSPEND` statement is entered on one system in an Oracle RAC configuration, then the internal locking mechanisms propagate the halt request across instances, thereby suspending I/O operations for all active instances in a given cluster.

#### 29.6.2 Making Backups in a Suspended Database

After a successful database suspension, you can back up the database to disk or break the mirrors. Because suspending a database does not guarantee immediate termination of I/O, Oracle recommends that you precede the `ALTER SYSTEM SUSPEND` statement with a `BEGIN BACKUP` statement so that the tablespaces are placed in backup mode.

You must use conventional user-managed backup methods to back up split mirrors. RMAN cannot make database backups or copies because these operations require reading the data file headers. After the database backup is finished or the mirrors are resilvered, then you can resume normal database operations using the `ALTER SYSTEM RESUME` statement.

Backing up a suspended database without splitting mirrors can cause an extended database outage because the database is inaccessible during this time. If backups are taken by splitting mirrors, however, then the outage is nominal. The outage time depends on the size of cache to flush, the number of data files, and the time required to break the mirror.

Note the following restrictions for the `SUSPEND/RESUME` feature:

- In an Oracle RAC configuration, do not start a new instance while the original nodes are suspended.
- No checkpoint is initiated by the `ALTER SYSTEM SUSPEND` or `ALTER SYSTEM RESUME` statements.
- You cannot issue `SHUTDOWN` with `IMMEDIATE`, `NORMAL`, or `TRANSACTIONAL` options while the database is suspended.
- Issuing `SHUTDOWN ABORT` on a database that is suspended reactivates the database. This prevents media recovery or failure recovery from getting into a unresponsive state.

To make a split mirror backup in SUSPEND mode:

1. Place the database tablespaces in backup mode. For example, to place tablespace `users` in backup mode, enter:
	```
	ALTER TABLESPACE users BEGIN BACKUP;
	```
	If you are backing up all of the tablespaces for your database, you can instead use:
	```
	ALTER DATABASE BEGIN BACKUP;
	```
	Caution:
	Do not use the `ALTER SYSTEM SUSPEND` statement as a substitute for placing a tablespace in backup mode.
2. If your mirror system has problems with splitting a mirror while disk writes are occurring, then suspend the database. For example, issue the following statement:
	```
	ALTER SYSTEM SUSPEND;
	```
3. Verify that the database is suspended by querying the `V$INSTANCE` view. Run only this query in a separate SQL session.
	For example:
	```
	SELECT DATABASE_STATUS FROM V$INSTANCE;
	DATABASE_STATUS 
	----------------- 
	SUSPENDED
	```
4. Split the mirrors at the operating system or hardware level.
5. End the database suspension. For example, issue the following statement:
	```
	ALTER SYSTEM RESUME;
	```
6. Establish that the database is active by querying the `V$INSTANCE` view. For example, enter:
	```
	SELECT DATABASE_STATUS FROM V$INSTANCE;
	DATABASE_STATUS 
	----------------- 
	ACTIVE
	```
7. Take the specified tablespaces out of backup mode. For example, enter the following statement to take tablespace `users` out of backup mode:
	```
	ALTER TABLESPACE users END BACKUP;
	```
8. Copy the control file and archive the online redo logs as usual for a backup.

### 29.7 Making User-Managed Backups to Raw Devices

A [raw device](glossary.md) is a disk or partition that does not have a file system. A raw device can contain only a single file. Backing up files on raw devices poses operating system specific issues. The following sections discuss some of these issues on UNIX, Linux, and Windows.

This section contains the following topics:

- Backing Up to Raw Devices on Linux and UNIX
- Backing Up to Raw Devices on Windows

#### 29.7.1 Backing Up to Raw Devices on Linux and UNIX

The `dd` command on Linux and UNIX is the most common backup utility for backing up to or from raw devices. See your operating system-specific documentation for complete details about this utility.

Using `dd` effectively requires that you specify the correct options, based on your database. Table 29-1 lists details about your database that affect the options you use for `dd`.

Table 29-1 Aspects of the Database Important for dd Usage

| Data | Explanation |
| --- | --- |
| Block size | You can specify the size of the buffer that `dd` uses to copy data. For example, you can specify that `dd` copies data in units of 8 KB or 64 KB. The block size for `dd` need not correspond to either the Oracle block size or the operating system block size: it is merely the size of the buffer used by `dd` when making the copy. |
| Raw offset | On some systems, the beginning of the file on the raw device is reserved for use by the operating system. This storage space is called the **raw offset**. Oracle Database does not back up or restore these bytes. |
| Size of Oracle Database block `0` | At the beginning of every Oracle database file, the operating system-specific code places an Oracle block called **block 0**. The generic Oracle code does not recognize this block, but the block is included in the size of the file on the operating system. Typically, this block is the same size as the other Oracle blocks in the file. |

The information in Table 29-1 enables you to set the `dd` options specified in Table 29-2.

Table 29-2 Options for dd Command

| This Option... | Specifies... |
| --- | --- |
| `if` | The name of the input file, that is, the file that you are reading |
| `of` | The name of the output file, that is, the file to which you are writing |
| `bs` | The buffer size used by `dd` to copy data |
| `skip` | The number of `dd` buffers to skip on the input raw device if a raw offset exists. For example, if you are backing up a file on a raw device with a 64 KB raw offset, and the `dd` buffer size is 8 KB, then you can specify `skip=8` so that the copy starts at offset 64 KB. |
| `seek` | The number of `dd` buffers to skip on the output raw device if a raw offset exists. For example, if you are backing up a file onto a raw device with a 64 KB raw offset, and the `dd` buffer size is 8 KB, then you can specify `skip=8` so that the copy starts at offset 64 KB. |
| `count` | The number of blocks on the input raw device for `dd` to copy. It is best to specify the exact number of blocks to copy when copying from a raw device to a file system; otherwise extra space at the end of the raw volume that is not used by the Oracle data file is copied to the file system.  Remember to include block `0` in the total size of the input file. For example, if the `dd` block size is 8 KB, and you are backing up a 30720 KB data file, then you can set `count=3841`. This value for `count` actually backs up 30728 KB: the extra 8 KB are for Oracle block `0`. |

Because a raw device can be the input or output device for a backup, you have four possible scenarios for the backup. The possible options for `dd` depend on which scenario you choose, as illustrated in Table 29-3.

Table 29-3 Scenarios Involving dd Backups

| Backing Up from... | Backing Up to... | Options Specified for dd Command |
| --- | --- | --- |
| Raw device | Raw device | `if,` `of,` `bs,` `skip`, `seek`, `count` |
| Raw device | File system | `if,` `of,` `bs,` `skip`, `count` |
| File system | Raw device | `if,` `of,` `bs,` `seek` |
| File system | File system | `if,` `of,` `bs` |

##### 29.7.1.1 Backing Up with the dd Utility on Linux and UNIX: Examples

For these examples of `dd` utility usage, assume the following:

- You are backing up a 30720 KB data file.
- The beginning of the data file has a block 0 of 8 KB.
- The raw offset is 64 KB.
- You set the `dd` block size to 8 KB when a raw device is involved in the copy.

In the following example, you back up from one raw device to another raw device:

```
% dd if=/dev/rsd1b of=/dev/rsd2b bs=8k skip=8 seek=8 count=3841
```

In the following example, you back up from a raw device to a file system:

```
% dd if=/dev/rsd1b of=/backup/df1.dbf bs=8k skip=8 count=3841
```

In the following example, you back up from a file system to a raw device:

```
% dd if=/backup/df1.dbf of=/dev/rsd2b bs=8k seek=8
```

In the following example, you back up from a file system to a file system, and set the block size to a high value to boost I/O performance:

```
% dd if=/oracle/dbs/df1.dbf of=/backup/df1.dbf bs=1024k
```

#### 29.7.2 Backing Up to Raw Devices on Windows

Like Linux and UNIX, Windows supports raw disk partitions in which the database can store data files, online logs, and control files. Each raw partition is assigned either a drive letter or physical drive number and does not contain a file system. As in Linux and UNIX, each raw partition on Windows is mapped to a single file.

Windows differs from Linux and UNIX in the naming convention for Oracle files. On Windows, raw data file names are formatted as follows:

```
\\.\drive_letter:
\\.\PHYSICALDRIVEdrive_number
```

For example, the following are possible raw file names:

```
\\.\G:
\\.\PHYSICALDRIVE3
```

The procedure for making user-managed backups of raw data files is basically the same as for copying files on a Windows file system, except that you use the Oracle `OCOPY` utility rather than the Windows-supplied `copy.exe` or `ntbackup.exe` utilities. `OCOPY` supports 64-bit file I/O, physical raw drives, and raw files. The `OCOPY` utility cannot back up directly to tape.

To display online documentation for `OCOPY`, enter `OCOPY` by itself at the Windows prompt. Sample output follows:

```
Usage of OCOPY:
     ocopy from_file [to_file [a | size_1 [size_n]]]
     ocopy -b from_file to_drive
     ocopy -r from_drive to_dir
```

Note the important `OCOPY` options described in Table 29-4.

Table 29-4 OCOPY Options

| Option | Action |
| --- | --- |
| `b` | Splits the input file into multiple output files. This option is useful for backing up to devices that are smaller than the input file. |
| `r` | Combines multiple input files and writes to a single output file. This option is useful for restoring backups created with the `-b` option. |

##### 29.7.2.1 Backing Up with OCOPY: Example

In this example, assume the following:

- Data file `12` is mounted on the `\\.\G:` raw partition.
- The `C:` drive mounts a file system.
- The database is open.

To back up the data file on the raw partition \\\\.\\ `G:` to a local file system, you can run the following command at the prompt after placing data file `12` in backup mode:

```
OCOPY "\\.G:" C:\backup\datafile12.bak
```

##### 29.7.2.2 Specifying the -b and -r Options for OCOPY: Example

In this example, assume the following:

- `\\.\G:` is a raw partition containing data file `7`
- The `E:` drive is a removable disk drive.
- The database is open.

To back up the data file onto drive `E:`, you can execute the following command at the Windows prompt after placing data file `7` in backup mode:

```
# first argument is file name, second argument is drive
OCOPY -b "\\.\G:" E:\
```

When drive `E:` fills up, you can use another disk. In this way, you can divide the backup of data file `7` into multiple files.

Similarly, to restore the backup, take the tablespace containing data file `7` offline and run this command:

```
# first argument is drive, second argument is directory
OCOPY -r E:\ "\\.\G:"
```

### 29.8 Making Backups with Third-Party Snapshot Technologies

You can use Storage Snapshot Optimization to take third-party snapshots of the database, without placing the database in backup mode. The snapshots must conform to the requirements described in this section.

Storage Snapshot Optimization provides the following benefits:

- Eliminates the complexity and overhead associated with placing the database in backup mode.
- Performs the recovery in a single step by using the `RECOVER ... SNAPSHOT TIME` command. You can recover either to the current time or to a point in time after the snapshot was taken.

To use Snapshot Storage Optimization, the third-party snapshot technology must conform to the following requirements:

- The database is crash consistent during the snapshot.
- The snapshot preserves write order for each file.
- The snapshot technology stores the time at which the snapshot is completed.

If the vendor cannot guarantee compliance with these requirements, then you must place your data files into [backup mode](glossary.md) by using the [`ALTER DATABASE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=SQLRF00802) or [`ALTER TABLESPACE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=SQLRF01002) statement with the `BEGIN BACKUP` clause. Place your data files in backup mode just before you create the snapshot. When a tablespace is in backup mode, the database writes the before image for an entire block to the redo stream before modifying a block. The database also records changes to the block in the online redo log. Backup mode also freezes the [data file checkpoint](glossary.md) until the file is removed from backup mode. Oracle Database performs this safeguard because it cannot guarantee that a third-party backup tool copies the file header before copying the data blocks. Immediately after the snapshot is created, use the `ALTER DATABASE` or `ALTER TABLESPACE` command with the `END BACKUP` clause to take the data files out of backup mode. You need not wait until the snapshot is actually copied to the backup media to end backup mode.

Note:

RMAN does not support storage-based replication technologies when the database being backed-up resides on Oracle Automatic Storage Management (Oracle ASM).

See Also:

" [Recovery Using Storage Snapshot Optimization](user-managed-flashback-dbpitr.md) "

[Volume Shadow Copy Service (VSS)](glossary.md) is a set of Windows APIs that enable applications to create consistent snapshots called **shadow copies**. The [Oracle VSS writer](glossary.md) runs as a service on Windows systems and is integrated with VSS-enabled applications. You can use these applications to create snapshots of database files managed by the Oracle instance. For example, you can make shadow copies of an Oracle database while it is open read/write.

See Also:

[Oracle Database Platform Guide for Microsoft Windows](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=NTQRF280) to learn how to back up and recover the database with VSS-enabled applications

### 29.9 Verifying User-Managed Data File Backups

You must periodically verify your backups to ensure that they are usable for recovery.

This section contains the following topics:

- Testing the Restoration of Data File Backups
- Running the DBVERIFY Utility

#### 29.9.1 Testing the Restoration of Data File Backups

The best way to test the usability of data file backups is to restore them to a separate host and attempt to open the database, performing media recovery if necessary. This option requires that you have a separate host available for the restore procedure.

See Also:

" [Performing Complete Database Recovery](user-managed-flashback-dbpitr.md) " to learn how to recover files with SQL\*Plus

#### 29.9.2 Running the DBVERIFY Utility

The `DBVERIFY` program is an external command-line utility that performs a physical data structure integrity check on an offline data file. Use `DBVERIFY` to ensure that a user-managed backup of a data file is valid before it is restored or as a diagnostic aid when you have encountered data corruption problems.

The name and location of `DBVERIFY` is dependent on your operating system. For example, to perform an integrity check on data file `users01.dbf` on Linux or UNIX, run the `dbv` command as follows:

```
% dbv file=users01.dbf
```

Sample `dbv` output follows:

```
DBVERIFY - Verification starting : FILE = users01.dbf

DBVERIFY - Verification complete

Total Pages Examined         : 250
Total Pages Processed (Data) : 1
Total Pages Failing   (Data) : 0
Total Pages Processed (Index): 0
Total Pages Failing   (Index): 0
Total Pages Processed (Other): 2
Total Pages Processed (Seg)  : 0
Total Pages Failing   (Seg)  : 0
Total Pages Empty            : 247
Total Pages Marked Corrupt   : 0
Total Pages Influx           : 0
```

See Also:

[Oracle Database Utilities](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=SUTIL013) to learn about `DBVERIFY`