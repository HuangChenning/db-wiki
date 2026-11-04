---
title: "Backup and Recovery User's Guide"
book: "Database Backup and Recovery User's Guide"
doc_id: F31836-11
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/bradv/reporting-rman-operations.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-users-guide
---

Run reports on RMAN operations to determine files that need back up, monitor space usage, and query backup metadata.

### 11.1 Overview of RMAN Reporting

This section explains the purpose and basic concepts of RMAN reporting.

#### 11.1.1 Purpose of RMAN Reporting

As part of your backup and recovery strategy, you should periodically run reports that indicate what you have backed up. You can determine which data files need backups or which files were not backed up recently. You can also preview which backups RMAN must restore if a problem occurs.

Another important aspect of backup and recovery is monitoring space usage. If you back up to disk, then it is possible for the disk to fill, which can create performance problems or even cause the database to halt. You can use RMAN to determine whether a backup is an obsolete backup and can therefore be deleted.

You may also need to obtain historical information about RMAN jobs. For example, you may want to know how many backup jobs have been issued, the status of each backup job (for example, whether it failed or completed), when a job started and finished, and what type of backup was performed.

#### 11.1.2 Basic Concepts of RMAN Reporting

RMAN stores metadata of every database on which it performs operations.

RMAN always stores its RMAN repository of metadata in the control file of the target database. For example, suppose that you use RMAN to back up the `prod1` and `prod2` databases. RMAN stores the metadata for backups of `prod1` in the control file of `prod1`, and the metadata for backups of `prod2` in the control file of `prod2`.

Optionally, you can use RMAN with a recovery catalog. In this case, RMAN maintains an additional repository of metadata in a set of tables in a separate recovery catalog database. For example, you could create a recovery catalog in `prod3`. You can register multiple target databases in this recovery catalog. For example, if you register `prod1` and `prod2` in the recovery catalog stored in `prod3`, then RMAN stores metadata about its backups of `prod1` and `prod2` in the recovery catalog schema.

The following table lists the techniques used to access metadata from the RMAN repository.

Table 11-1 Techniques for Accessing Data from the RMAN Repository

| Technique | Description | Additional Information |
| --- | --- | --- |
| RMAN `LIST` and `REPORT` commands | The RMAN `LIST` and `REPORT` commands provide extensive information about available backups and how they can be used to restore and recover your database. | - Listing Backups and Recovery-Related Objects - Reporting on Backups and Database Schema - `LIST`, `REPORT`, and `RESTORE` commands in Oracle Database Backup and Recovery Reference |
| `V$` views | When the database is open, several `V$` views provide direct access to RMAN repository records in the control file of each target database.  Some `V$` views such as `V$DATAFILE_HEADER`, `V$PROCESS`, and `V$SESSION` contain information not found in the recovery catalog views. | Oracle Database Reference |
| `RC_` views | If your database is registered in a recovery catalog, then `RC_` views provide direct access to the RMAN repository data stored in the recovery catalog.  The `RC_` views mostly correspond to the `V$` views. | Recovery Catalog Views in Oracle Database Backup and Recovery Reference |
| `RESTORE ... PREVIEW ` and `RESTORE ... VALIDATE HEADER` commands | These commands list the backups that RMAN can restore to the specified time.  `RESTORE ... PREVIEW` queries the metadata but does not read the backup files. The `RESTORE ... VALIDATE HEADER` command performs the same work, but in addition to listing the files needed for restore and recovery operations, the command validates the backup file headers to determine whether the files on disk or in the media management catalog correspond to the metadata in the RMAN repository. | Previewing Backups Used in Restore Operations |

The RMAN repository can sometimes fail to reflect the reality on disk and tape. For example, a user may delete a backup with an operating system utility, so that the RMAN repository incorrectly reports the backup as available. You can use commands such as `CHANGE`, `CROSSCHECK`, and `DELETE` to update the RMAN repository to reflect the actual state of available backups. Otherwise, the output of the commands and views may be misleading, which means that RMAN may not be able to find the backups to restore and recover your database.

#### 11.1.3 Reporting in a Data Guard Environment

In a Data Guard environment, you can use the `LIST`, `REPORT`, and `SHOW` commands just as you can when not using Data Guard. You can run these commands with the `FOR DB_UNIQUE_NAME` clause to show the backups associated with a specified database.

Every backup is associated with the primary or standby database that created it. For example, if you backed up the database with the `DB_UNIQUE_NAME` of `standby1`, then the `standby1` database is associated with this backup.

For example, the following command lists archived redo logs associated only with `sfstandby`:

```
LIST ARCHIVELOG ALL FOR DB_UNIQUE_NAME sfstandby;
```

If you use the `LIST`, `REPORT`, and `SHOW` commands in a Data Guard environment without specifying the `FOR DB_UNIQUE_NAME` clause, then RMAN shows the files that are accessible to the target database.

In a Data Guard environment, you must use RMAN with a recovery catalog. RMAN stores the metadata for all backup and recovery files in the Data Guard environment in the recovery catalog. When running the RMAN reporting commands, you can either connect RMAN as `TARGET` to a mounted or open database, or identify the database with the `SET DBID` command.

### 11.2 Listing Backups and Recovery-Related Objects

The `LIST` command uses the information in the RMAN repository to provide lists of backups and other objects relating to backup and recovery.

To list backups and other objects in the CDB, connect to the root as a common user with the `SYSBACKUP` or `SYSDBA` privilege.

To list backups and other objects in a PDB, connect to the PDB as a common user or local user with the `SYSBACKUP` or `SYSDBA` privilege. Or, you can connect to the root as a common user or local user with the `SYSBACKUP` or `SYSDBA` privilege and use the `LIST` command with the `PLUGGABLE DATABASE` clause.

#### 11.2.1 About the LIST Command

The primary purpose of the `LIST` command is to list backup and copies.

For example, you can list:

- Backups and proxy copies of a database, tablespace, data file, archived redo log, or control file
- Backups that have expired
- Backups restricted by time, path name, device type, tag, or recoverability
- Archived redo log files and disk copies

Besides backups and copies, RMAN can list other types of data. The following table summarizes several useful objects that you can list.

Table 11-2 LIST Objects

| Contents of List | Command | Description |
| --- | --- | --- |
| Backup sets and proxy copies | `LIST BACKUP` | You can list all backup sets, copies, and proxy copies of a database, tablespace, data file, archived redo log, control file, or server parameter file. |
| Image copies | `LIST COPY` | You can list data file copies and archived redo log files. By default, `LIST COPY` displays copies of all database files and archived redo logs. Both usable and unusable image copies are included in the output, even those that cannot be restored or are expired or unavailable. |
| Archived redo log files | `LIST ARCHIVELOG` | You can list archive redo log files. You can list all archive log redo log files or specify individual archive log files through SCN, time, or sequence number ranges. If you specify a range you can further restrict the list returned by specifying an incarnation number. |
| Preplugin backups | `LIST ... PREPLUGIN` | You can list all preplugin backups and preplugin archived redo log files. |
| Database incarnations | `LIST INCARNATION` | You can list all incarnations of a database. A new database incarnation is created when you open with the `RESETLOGS` option. |
| Databases in a Data Guard environment | `LIST DB_UNIQUE_NAME` | A database in a Data Guard environment is distinguished by its `DB_UNIQUE_NAME` initialization parameter setting. You can list all databases that have the same DBID. |
| Backups and copies for a primary or standby database in a Data Guard environment | `LIST ... FOR DB_UNIQUE_NAME` | You can list all backups and copies for a specified database in a Data Guard environment or for all databases in the environment.  RMAN restricts the output to files or objects associated exclusively with the database with the specified `DB_UNIQUE_NAME`. For example, you can use `LIST` with `FOR DB_UNIQUE_NAME` to display the list of archived redo log files associated with a particular standby or primary database. Objects that are not owned by any database (`SITE_KEY` column in the recovery catalog view is null) are not listed. |
| Restore points | `LIST RESTORE POINT` | You can list restore points known to the RMAN repository. |
| Names of stored scripts | `LIST SCRIPT NAMES` | You can list the names of recovery catalog scripts created with the `CREATE SCRIPT` or `REPLACE SCRIPT` command. A recovery catalog is required. |
| Failures for use with Data Recovery Advisor | `LIST FAILURE` | A failure is a persistent data corruption mapped to a repair option. Use `LIST                                     FAILURE` with the `ADVISE` and `REPAIR` commands.  Starting in Oracle Database 19c, the Data Recovery Advisor (DRA) feature is deprecated.  The deprecation of DRA includes deprecation of the following Oracle Recovery Manager (RMAN) commands: `LIST FAILURE`, `ADVISE FAILURE`, `REPAIR                     FAILURE`, and `CHANGE FAILURE`. Database administrators will no longer have access to these commands. There is no replacement feature for DRA. |

The `LIST` command supports options that control how output is displayed. Table 11-3 summarizes the most common `LIST` options.

Table 11-3 Most Common LIST Options

| LIST Option | Description |
| --- | --- |
| `LIST EXPIRED` | Lists backups or copies that are recorded in the RMAN repository but that were not present at the expected location on disk or tape during the most recent crosscheck. Such backups may have been deleted outside of RMAN. |
| `LIST ... BY FILE` | Lists backups of each data file, archived redo log file, control file, and server parameter file. Each row describes a backup of a file. |
| `LIST ... SUMMARY` | Provides a one-line summary of each backup. |

The `LIST` objects and options are not exhausted by the contents of the preceding tables. For example, you can list backups restricted by time, path name, device type, tag, or recoverability.

#### 11.2.2 Listing All Backups and Copies

Specify the desired objects with the `listObjList` or `recordSpec` clause. If you do not specify an object, then RMAN displays copies of all database files and archived redo log files.

By default, RMAN serially lists each backup or proxy copy and then identifies the files included in the backup. You can also list backups by file. By default, RMAN lists in verbose mode, which means that it provides extensive, multiline information. You can also list backups in a summary mode if the verbose mode generates too much output.

To view a summary report of all backups and copies, run the `LIST` command with the `SUMMARY` option.

- To list objects in the entire CDB, connect to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege.
- To list objects in a PDB, use one of the following techniques:
	- Connect to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege. Use the `LIST...PLUGGABLE DATABASE` command. For example:
		```
		LIST BACKUP OF PLUGGABLE DATABASE hr_pdb, sales_pdb;
		```
		- Connect to the PDB as a common user or local user with the `SYSDBA` or `SYSBACKUP` privilege. Use the `LIST` command.

Example 11-1 Summary Listing of All Backups

This example shows a summary of all RMAN backups.

```
RMAN> list backup summary;

List of Backups
===============
Key     TY LV S Device Type Completion Time #Pieces #Copies Compressed Tag
------- -- -- - ----------- --------------- ------- ------- ---------- ---
1       B  A  A SBT_TAPE    21-OCT-13       1       1       NO         TAG20131021T094505
2       B  F  A SBT_TAPE    21-OCT-13       1       1       NO         TAG20131021T094513
3       B  A  A SBT_TAPE    21-OCT-13       1       1       NO         TAG20131021T094624
4       B  F  A SBT_TAPE    21-OCT-13       1       1       NO         TAG20131021T094639
5       B  F  A DISK        04-NOV-13       1       1       YES        TAG20131104T195949
```

To view verbose output for backups and copies, run the `LIST` command without the `SUMMARY` option.

Example 11-2 Verbose Listings of Backups and Copies

This example lists RMAN backups and copies with the default verbose output.

```
RMAN> list backup;

List of Backup Sets
===================

BS Key  Size       Device Type Elapsed Time Completion Time
------- ---------- ----------- ------------ ---------------
7       136M       DISK        00:00:20     04-NOV-13      
        BP Key: 7   Status: AVAILABLE  Compressed: NO  Tag: TAG20071104T200759
        Piece Name: /d2/RDBMS/backupset/2013_11_04/o1_mf_annnn_TAG20071104T200759_ztjxx3k8_.bkp

  List of Archived Logs in backup set 7
  Thrd Seq     Low SCN    Low Time  Next SCN   Next Time
  ---- ------- ---------- --------- ---------- ---------
  1    1       173832     21-OCT-13 174750     21-OCT-13
  1    2       174750     21-OCT-13 174755     21-OCT-13
  1    3       174755     21-OCT-13 174758     21-OCT-13

BS Key  Type LV Size       Device Type Elapsed Time Completion Time
------- ---- -- ---------- ----------- ------------ ---------------
8       Full    2M         DISK        00:00:01     04-NOV-13      
        BP Key: 8   Status: AVAILABLE  Compressed: NO  Tag: TAG20071104T200829
        Piece Name: /disk1/oracle/dbs/c-774627068-20131104-01
  Controlfile Included: Ckp SCN: 631510       Ckp time: 04-NOV-13
  SPFILE Included: Modification time: 21-OCT-13
```
```
RMAN> list copy;

List of Datafile Copies
=======================
 
Key     File S Completion Time Ckp SCN    Ckp Time
------- ---- - --------------- ---------- ---------------
1       7    A 11-OCT-13       360072     11-OCT-13
        Name: /work/orcva/RDBMS/datafile/o1_mf_tbs_2_2lv7bf82_.dbf
        Tag: DF7COPY
 
2       8    A 11-OCT-13       360244     11-OCT-13
        Name: /work/orcva/RDBMS/datafile/o1_mf_tbs_2_2lv7qmcj_.dbf
        Tag: TAG20131011T184835
 
List of Control File Copies
===========================
 
Key     S Completion Time Ckp SCN    Ckp Time
------- - --------------- ---------- ---------------
3       A 11-OCT-13       360380     11-OCT-13
        Name: /d2/RDBMS/controlfile/o1_mf_TAG20131011T185335_2lv80zqd_.ctl
        Tag: TAG20131011T185335
 
List of Archived Log Copies for database with db_unique_name RDBMS
=====================================================================
 
Key     Thrd Seq     S Low Time
------- ---- ------- - ---------
1       1    1       A 11-OCT-13
        Name: /work/arc_dest/arcr_1_1_603561743.arc
 
2       1    2       A 11-OCT-13
        Name: /work/arc_dest/arcr_1_2_603561743.arc
 
3       1    3       A 11-OCT-13
        Name: /work/arc_dest/arcr_1_3_603561743.arc
```

Example 11-3 Listing Backups By File

This example illustrates how to list backups by file using `LIST` with the `BY FILE` option.

```
RMAN> list backup by file;

List of Datafile Backups
========================

File Key     TY LV S Ckp SCN    Ckp Time  #Pieces #Copies Compressed Tag
---- ------- -  -- - ---------- --------- ------- ------- ---------- ---
1    5       B  F  A 631092     04-NOV-13 1       1       YES        TAG20131104T195949
     2       B  F  A 175337     21-OCT-13 1       1       NO         TAG20131021T094513
2    5       B  F  A 631092     04-NOV-13 1       1       YES        TAG20131104T195949
     2       B  F  A 175337     21-OCT-13 1       1       NO         TAG20131021T094513

... some rows omitted

List of Archived Log Backups
============================

Thrd Seq     Low SCN    Low Time  BS Key  S #Pieces #Copies Compressed Tag
---- ------- ---------- --------- ------- - ------- ------- ---------- ---
1    1       173832     21-OCT-13 7       A 1       1       NO         TAG20131104T200759
                                  1       A 1       1       NO         TAG20131021T094505
1    2       174750     21-OCT-13 7       A 1       1       NO         TAG20131104T200759
                                  1       A 1       1       NO         TAG20131021T094505
... some rows omitted
1    38      575472     03-NOV-13 7       A 1       1       NO         TAG20131104T200759
1    39      617944     04-NOV-13 7       A 1       1       NO         TAG20131104T200759

List of Controlfile Backups
===========================
CF Ckp SCN Ckp Time  BS Key  S #Pieces #Copies Compressed Tag
---------- --------- ------- - ------- ------- ---------- ---
631510     04-NOV-13 8       A 1       1       NO         TAG20131104T200829
631205     04-NOV-13 6       A 1       1       NO         TAG20131104T200432

List of SPFILE Backups
======================
Modification Time BS Key  S #Pieces #Copies Compressed Tag
----------------- ------- - ------- ------- ---------- ---
21-OCT-13         8       A 1       1       NO         TAG20131104T200829
21-OCT-13         6       A 1       1       NO         TAG20131104T200432
```

#### 11.2.3 Listing Selected Backups and Copies

You can specify several different conditions to narrow your `LIST` output.

To list selected backups and copies:

1. Start RMAN and connect to a target database and recovery catalog (if used).
	- To list selected objects in the entire CDB, connect to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege.
	- To list selected objects in a PDB, use one of the following:
		- Connect to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege. Use the `LIST...PLUGGABLE DATABASE` command.
			- Connect to the PDB as a common user or local user with the `SYSDBA` or `SYSBACKUP` privilege. Use the `LIST` command.
2. Run `LIST COPY` or `LIST BACKUP` with the `listObjList` or `recordSpec` clause. For example, enter any of the following commands:
	```
	# lists backups of all files in database
	LIST BACKUP OF DATABASE; 
	# lists copy of specified datafile    
	LIST COPY OF DATAFILE 'ora_home/oradata/trgt/system01.dbf'; 
	# lists specified backup set
	LIST BACKUPSET 213; 
	# lists datafile copy
	LIST DATAFILECOPY '/tmp/tools01.dbf';
	```
	You can also restrict the search by specifying the `maintQualifier` or `RECOVERABLE` clause. For example, enter any of the following commands:
	```
	# specify a backup set by tag
	LIST BACKUPSET TAG 'weekly_full_db_backup';
	# specify a backup or copy by device type
	LIST COPY OF DATAFILE 'ora_home/oradata/trgt/system01.dbf' DEVICE TYPE sbt;
	# specify a backup by directory or path
	LIST COPY LIKE '/tmp/%';
	# specify a backup or copy by a range of completion dates
	LIST COPY OF DATAFILE 2 COMPLETED BETWEEN '10-DEC-2012' AND '17-DEC-2012';
	# specify logs backed up at least twice to tape
	LIST ARCHIVELOG ALL BACKED UP 2 TIMES TO DEVICE TYPE sbt;
	# specify backup sets backed up at least once to disk
	LIST BACKUPSET BACKED UP 1 TIMES TO DISK;
	# specify backups of PDB backed up at least twice to sbt
	LIST BACKUP OF PLUGGABLE DATABASE my_pdb BACKED UP 2 TIMES TO SBT;
	```
3. The output depends upon the options that you pass to the `LIST` command. For example, the following lists copies of data file `1` contained in backup sets.
	```
	RMAN> LIST BACKUP OF DATAFILE 1;
	List of Backup Sets
	===================
	BS Key  Type LV Size       Device Type Elapsed Time Completion Time
	------- ---- -- ---------- ----------- ------------ ---------------
	2       Full    230M       SBT_TAPE    00:00:49     21-OCT-13
	        BP Key: 2   Status: AVAILABLE  Compressed: NO  Tag: TAG20131021T094513
	        Handle: 02f4eatc_1_1   Media: /smrdir
	  List of Datafiles in backup set 2
	  File LV Type Ckp SCN    Ckp Time  Name
	  ---- -- ---- ---------- --------- ----
	  1       Full 175337     21-OCT-13 /oracle/dbs/tbs_01.f
	BS Key  Type LV Size       Device Type Elapsed Time Completion Time
	------- ---- -- ---------- ----------- ------------ ---------------
	5       Full    233M       DISK        00:04:30     04-NOV-13
	        BP Key: 5   Status: AVAILABLE  Compressed: NO  Tag: TAG20131104T195949
	        Piece Name: /disk1/2013_11_04/o1_mf_nnndf_TAG20131104T195949_ztjxfvgz_.bkp
	  List of Datafiles in backup set 5
	  File LV Type Ckp SCN    Ckp Time  Name
	  ---- -- ---- ---------- --------- ----
	  1       Full 631092     04-NOV-13 /oracle/dbs/tbs_01.f
	```

#### 11.2.4 Listing Backups of Dropped PDBs

Use the `LIST` command with the `GUID` option to list backups of pluggable databases (PDBs) that have been dropped from a multitenant container database (CDB).

After a PDB is dropped, you cannot perform operations or query data dictionary views by using the PDB name. However, you can obtain information about dropped PDBs by querying using GUID of a PDB.

To list backups of dropped PDBs:

1. Connect to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege.
2. Query the `DBA_PDB_HISTORY` view to determine the GUID of the PDB that was dropped.
	The following example displays the PDBs that were dropped from the CDB `test_db`:
	```
	SELECT pdb_name, pdb_guid FROM dba_pdb_history
	WHERE db_name = 'test_db';
	```
3. Use the `LIST` command with the `GUID` option to display backups of a dropped PDB.
	The following commands display backup sets and image copies of a dropped PDB with the specified GUID:
	```
	LIST BACKUP GUID 'CDFFD672330A7527D0147204CD0E08D4';
	LIST COPY GUID 'CDFFD672330A7527D0147204CD0E08D4';
	```

#### 11.2.5 Listing Preplugin Backups

Use the `LIST` command to list preplugin backups and preplugin archived redo log files.

The `COMPATIBLE` parameter for the target CDB must be set to 18.0.0 or higher.

1. Start RMAN and connect to the root of the target database as a common user with the `SYSDBA` or `SYSBACKUP` privilege. Connect to a recovery catalog, if used.
2. Ensure that the target CDB is in read-write or read-only mode.
3. Set the current container to the PDB whose backup objects you want to display by using the `SET` command.
	The following command sets the current container to `my_pdb`.
	```
	SET PREPLUGIN CONTAINER = my_pdb;
	```
4. Run the `LIST PREPLUGIN` command with the `listObjList` or `recordSpec` clause to display preplugin backups.
	To list preplugin backups of a PDB, use the following command:
	```
	LIST PREPLUGIN BACKUP OF PLUGGABLE DATABASE pdb1;
	```
	To list all preplugin archived redo log files in the target CDB, use the following command:
	```
	LIST PREPLUGIN ARCHVELOG ALL;
	```

#### 11.2.6 Listing Database Incarnations

Each time an `OPEN RESETLOGS` operation is performed on a database, this operation creates a new incarnation of the database.

When performing incremental backups, RMAN can use a backup from a previous incarnation or the current incarnation as a basis for subsequent incremental backups. When performing restore and recovery operations, RMAN can use backups from a previous incarnation just as it can use backups from the current incarnation, if all archived logs are available.

To list database incarnations:

1. Start RMAN and connect to a target database and recovery catalog (if used).
2. Run the `LIST` `INCARNATION` command, as shown in the following example:
	```
	LIST INCARNATION;
	```
	If you are using a recovery catalog, and if you register multiple target databases in the same catalog, then you can distinguish them by using the `OF                             DATABASE` option:
	```
	LIST INCARNATION OF DATABASE prod3;
	```
	Following is a sample output of listing the incarnation of a particular database:
	```
	RMAN> LIST INCARNATION OF DATABASE rdbms;
	List of Database Incarnations
	DB Key  Inc Key DB Name  DB ID            STATUS  Reset SCN  Reset Time
	------- ------- -------- ---------------- ------  ---------- ----------
	1       1       RDBMS    774627068        PARENT  1          21-OCT-13
	2       2       RDBMS    774627068        CURRENT 173832     21-OCT-13
	```
	The preceding output indicates that a `RESETLOGS` operation was performed on database `rdbms` at SCN 173832, resulting in a new incarnation. The incarnation is distinguished by incarnation key (represented in the `Inc Key` column).

### 11.3 Reporting on Backups and Database Schema

The RMAN `REPORT` command analyzes the available backups and your database. You can view reports on the metadata related to a multitenant container database (CDB), the root only, or one or more pluggable databases (PDBs).

#### 11.3.1 About Reports of RMAN Backups

The `REPORT` command provides various reports of RMAN backups.

Use the `REPORT` command to answer important questions, such as:

- Which files need a backup?
- Which files have had unrecoverable operations performed on them?
- Which backups are obsolete and can be deleted?
- What was the physical schema of the target database or a database in the Data Guard environment at some previous time?
- Which files have not been backed up recently?

Reports enable you to confirm that your backup and recovery strategy is in fact meeting your requirements for database recoverability. The two major forms of `REPORT` used to determine whether your database is recoverable are:

- `REPORT NEED BACKUP`
	Reports which database files must be backed up to meet a configured or specified retention policy
- `REPORT UNRECOVERABLE`
	Reports which database files require backup because they have been affected by some `NOLOGGING` operation such as a direct-path `INSERT`

The RMAN repository contains other information that you can access with the `REPORT` command. The following table summarizes the `REPORT` options.

Table 11-4 REPORT Options

| Contents of Report | Command | Description |
| --- | --- | --- |
| Obsolete backups | `REPORT OBSOLETE` | Full backups, data file copies, and archived redo logs recorded in the RMAN repository that can be deleted because they are no longer needed |
| Database schema | `REPORT SCHEMA` | The names of all data files (permanent and temporary) and tablespaces for the target database at the specified point in time. If you use RMAN in a Data Guard environment, then you can report the schema for a specified `DB_UNIQUE_NAME`. |

#### 11.3.2 Reporting on Files Needing a Backup Under a Retention Policy

Use the `REPORT NEED BACKUP` command to determine which database files need backup under a specific retention policy. With no arguments, this command reports which objects need backup under the currently configured retention policy.

- To report on objects in the whole CDB, connect to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege. Use the `REPORT NEED BACKUP` command.
- To report on objects in a PDB, use one of the following:
	- Connect to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege. Use the `REPORT NEED BACKUP PLUGGABLE DATABASE` command.
		- Connect to the PDB as a common user or local user with the `SYSDBA` or `SYSBACKUP` privilege. Use the `REPORT NEED BACKUP` command.

The output for a configured retention policy of `REDUNDANCY                     1` is similar to this example:

```
RMAN> REPORT NEED BACKUP;

RMAN retention policy will be applied to the command
RMAN retention policy is set to redundancy 1
Report of files with less than 1 redundant backups
File #bkps Name
---- ----- -----------------------------------------------------
2    0     /oracle/oradata/trgt/undotbs01.dbf
```

Note:

If you disable the retention policy using `CONFIGURE RETENTION POLICY TO NONE`, then `REPORT NEED BACKUP` returns an error message, because without a retention policy, RMAN cannot determine which files must be backed up.

##### 11.3.2.1 Using RMAN REPORT NEED BACKUP with Different Retention Policies

You can use options of the `REPORT NEED BACKUP` command to specify different retention policies.

Use one of the following forms to specify different criteria for `REPORT NEED BACKUP`:

- `REPORT NEED BACKUP RECOVERY WINDOW OF ` `n` `DAYS`
	Displays objects requiring backup to satisfy a recovery window-based retention policy
- `REPORT NEED BACKUP REDUNDANCY ` `n`
	Displays objects requiring backup to satisfy a redundancy-based retention policy
- `REPORT NEED BACKUP DAYS ` `n`
	Displays files that require more than `n` days' worth of archived redo log files for recovery
- `REPORT NEED BACKUP INCREMENTAL ` `n`
	Displays files that require application of more than `n` incremental backups for recovery

##### 11.3.2.2 Using RMAN REPORT NEED BACKUP with Tablespaces and Data Files

The `REPORT NEED BACKUP` command can check the entire database, skip specified tablespaces, or check only specific tablespaces or data files against different retention policies.

The following are examples:

```
REPORT NEED BACKUP RECOVERY WINDOW OF 2 DAYS DATABASE SKIP TABLESPACE TBS_2;
REPORT NEED BACKUP REDUNDANCY 2 DATAFILE 1;
REPORT NEED BACKUP TABLESPACE TBS_3; # uses configured retention policy
REPORT NEED BACKUP INCREMENTAL 2; # checks entire database
```

##### 11.3.2.3 Using REPORT NEED BACKUP with Backups on Tape or Disk Only

You can limit the backups tested by the `REPORT NEED BACKUP` command to disk-based or tape-based backups only.

Following are some examples:

```
REPORT NEED BACKUP RECOVERY WINDOW OF 2 DAYS DATABASE DEVICE TYPE sbt;
REPORT NEED BACKUP DEVICE TYPE DISK;
REPORT NEED BACKUP TABLESPACE TBS_3 DEVICE TYPE sbt;
```

#### 11.3.3 Reporting on Data Files Affected by Unrecoverable Operations

When a data file has been changed by an unrecoverable operation, such as a direct load insert, normal media recovery cannot be used to recover the file, because an unrecoverable operation does not generate redo. You must perform either a full or incremental backup of affected data files after such operations, to ensure that data blocks affected by the unrecoverable operation can be recovered using RMAN.

To identify data files affected by an unrecoverable operation:

1. Start RMAN and connect to a target database and recovery catalog (if used).
	- To report on objects in the database, connect to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege. Use the `REPORT                                     UNRECOVERABLE` command.
	- To report on objects in a PDB, use one of the following:
		- Connect to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege. Use the `REPORT UNRECOVERABLE PLUGGABLE                                             DATABASE` command.
			- Connect to the PDB as a common user or local user with the `SYSDBA` or `SYSBACKUP` privilege. Use the `REPORT UNRECOVERABLE` command.
2. Run the `REPORT UNRECOVERABLE` command with the required clauses.
	The following example includes sample output when connected to the root:
	```
	RMAN> REPORT UNRECOVERABLE;
	Report of files that need backup due to unrecoverable operations
	File Type of Backup Required Name
	---- ----------------------- -----------------------------------
	1    full                    /oracle/oradata/trgt/system01.dbf
	```

#### 11.3.4 Reporting on Obsolete Backups

You can report backup sets, backup pieces, and data file copies that are obsolete that is, not needed to meet a specified retention policy by specifying the `OBSOLETE` keyword.

To report obsolete backups:

1. Start RMAN and connect to the target database and recovery catalog (if used).
	- To report on objects in the database, connect to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege. Use the `REPORT                                     OBSOLETE` command.
	- To report on objects in a PDB, connect to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege. Use the `REPORT                                     OBSOLETE OF PLUGGABLE DATABASE` command.
	You cannot view reporting information about obsolete backups or delete obsolete backups when connected to a PDB.
2. Execute the `CROSSCHECK` command to update the status of backups in the repository compared to their status on disk.
	In the simplest case, you could crosscheck all backups on disk, tape or both, using any one of the following commands:
	```
	CROSSCHECK BACKUP DEVICE TYPE DISK;
	CROSSCHECK BACKUP DEVICE TYPE sbt;
	CROSSCHECK BACKUP; # crosschecks all backups on all devices 
	CROSSCHECK BACKUP OF PLUGGABLE DATABASE my_pdb;    #when connected to the root
	```
3. Run `REPORT OBSOLETE` to identify which backups are obsolete because they are no longer needed for recovery.
	To display the obsolete backups for a particular PDB when connected to the root, use the `PLUGGABLE DATABASE` clause with the `REPORT` command. For example:
	```
	RMAN> REPORT OBSOLETE OF PLUGGABLE DATABASE my_pdb;
	```
	If you do not specify any other options, then `REPORT OBSOLETE` displays the backups that are obsolete according to the current retention policy, as shown in the following example:
	```
	RMAN> REPORT OBSOLETE;
	RMAN retention policy will be applied to the command
	RMAN retention policy is set to redundancy 1
	Report of obsolete backups and copies
	Type                 Key    Completion Time    Filename/Handle
	-------------------- ------ ------------------ --------------------
	Datafile Copy        44     08-FEB-13          /backup/ora_df549738566_s70_s1
	Datafile Copy        45     08-FEB-13          /backup/ora_df549738567_s71_s1
	Datafile Copy        46     08-FEB-13          /backup/ora_df549738568_s72_s1
	Backup Set           26     08-FEB-13
	  Backup Piece       26     08-FEB-13          /backup/ora_df549738682_s76_s1
	.
	.
	.
	```
	You can also check which backups are obsolete under different recovery window-based or redundancy-based retention policies, by using `REPORT OBSOLETE` with `RECOVERY WINDOW` and `REDUNDANCY` options, as shown in these examples:
	```
	REPORT OBSOLETE RECOVERY WINDOW OF 3 DAYS;
	REPORT OBSOLETE REDUNDANCY 1;
	```

#### 11.3.5 Reporting on the Database Schema

The `REPORT SCHEMA` command lists and displays information about the database files, tablespaces, and so on.

If you do not specify `FOR DB_UNIQUE_NAME` with `REPORT SCHEMA`, then a recovery catalog connection is optional, but a target database connection is required. In a Data Guard environment, you can specify `REPORT SCHEMA FOR DB_UNIQUE_NAME` to report the schema for a database in the environment. In this case, an RMAN connection to a target database is not required. You can connect RMAN to the recovery catalog and set the DBID instead.

To report on the database schema:

1. Start RMAN and connect to the desired databases.
2. If you did not connect RMAN to a target database in the previous step, and you intend to specify the `FOR DB_UNIQUE_NAME` clause on `REPORT SCHEMA`, then set the database DBID. For example, enter the following command:
	```
	RMAN> SET DBID 28014364;
	```
3. Run the `REPORT` `SCHEMA` command as shown in the following example:
	```
	RMAN> REPORT SCHEMA;
	 
	Report of database schema for database with db_unique_name DGRDBMS
	 
	List of Permanent Datafiles
	===========================
	File Size(MB) Tablespace           RB segs Datafile Name
	---- -------- -------------------- ------- ------------------------
	1    450      SYSTEM               YES     /disk1/oracle/dbs/t_db1.f
	2    141      SYSAUX               NO      /disk1/oracle/dbs/t_ax1.f
	3    50       UD1                  YES     /disk1/oracle/dbs/t_undo1.f
	4    50       TBS_11               NO      /disk1/oracle/dbs/tbs_111.f
	5    50       TBS_11               NO      /disk1/oracle/dbs/tbs_112.f
	 
	List of Temporary Files
	=======================
	File Size(MB) Tablespace           Maxsize(MB) Tempfile Name
	---- -------- -------------------- ----------- --------------------
	1    40       TEMP                 32767       /disk1/oracle/dbs/t_tmp1.f
	```
	If you use a recovery catalog, then you can use the `atClause` to specify a past time, SCN, or log sequence number, as shown in these examples of the command:
	```
	RMAN> REPORT SCHEMA AT TIME 'SYSDATE-14';     # schema 14 days ago
	RMAN> REPORT SCHEMA AT SCN 1000;              # schema at scn 1000
	RMAN> REPORT SCHEMA AT SEQUENCE 100 THREAD 1; # schema at sequence 100
	RMAN> REPORT SCHEMA FOR DB_UNIQUE_NAME standby1; # schema for database standby1
	```

### 11.4 Using V$ Views to Query Backup Metadata

In some cases, V$ views supply information that is not available through use of the `LIST` and `REPORT` commands.

This section describes cases in which V$ views are particularly useful.

#### 11.4.1 Querying Details of Past and Current RMAN Jobs

An RMAN job is the set of commands executed within an RMAN session. Thus, one RMAN job can contain multiple commands.

For example, you may execute two separate `BACKUP` commands and a `RECOVER COPY` command in a single session. An RMAN backup job is the set of `BACKUP` commands executed in one RMAN job. For example, a `BACKUP      DATABASE` and `BACKUP ARCHIVELOG ALL` command executed in the same RMAN job constitute a single RMAN backup job.

The views `V$RMAN_BACKUP_JOB_DETAILS` and `V$RMAN_BACKUP_SUBJOB_DETAILS` and their corresponding recovery catalog versions provide details of RMAN backup jobs. For example, the views show how long a backup took, how many backup jobs have been issued, the status of each backup job (for example, whether it failed or completed), when a job started and finished, and what type of backup was performed. The `SESSION_KEY` column is the unique key for the RMAN session in which the backup job occurred.

RMAN backups often write less than they read. Because of RMAN compression, the `OUTPUT_BYTES_PER_SEC` column cannot be used as the measurement of backup speed. The appropriate column to measure backup speed is `INPUT_BYTES_PER_SEC`. The ratio between read and written data is described in the `COMPRESSION_RATIO` column.

To query details about past and current RMAN jobs:

1. Connect SQL\*Plus to the database whose backup history you intend to query.
2. Query the `V$RMAN_BACKUP_JOB_DETAILS` view for information about the backup type, status, and start and end time.
	The following query shows the backup job history ordered by session key, which is the primary key for the RMAN session:
	```
	COL STATUS FORMAT a9
	COL hrs    FORMAT 999.99
	SELECT SESSION_KEY, INPUT_TYPE, STATUS,
	       TO_CHAR(START_TIME,'mm/dd/yy hh24:mi') start_time,
	       TO_CHAR(END_TIME,'mm/dd/yy hh24:mi')   end_time,
	       ELAPSED_SECONDS/3600                   hrs
	FROM V$RMAN_BACKUP_JOB_DETAILS
	ORDER BY SESSION_KEY;
	```
	The following sample output shows the backup job history:
	```
	SESSION_KEY INPUT_TYPE    STATUS    START_TIME     END_TIME           HRS
	----------- ------------- --------- -------------- -------------- -------
	          9 DATAFILE FULL COMPLETED 04/18/07 18:14 04/18/07 18:15     .02
	         16 DB FULL       COMPLETED 04/18/07 18:20 04/18/07 18:22     .03
	        113 ARCHIVELOG    COMPLETED 04/23/07 16:04 04/23/07 16:05     .01
	```
3. Query the `V$RMAN_BACKUP_JOB_DETAILS` view for the rate of backup jobs in an RMAN session.
	The following query shows the backup job speed ordered by session key, which is the primary key for the RMAN session. The columns `in_sec` and `out_sec` display the data input and output per second.
	```
	COL in_sec FORMAT a10
	COL out_sec FORMAT a10
	COL TIME_TAKEN_DISPLAY FORMAT a10
	SELECT SESSION_KEY, 
	       OPTIMIZED, 
	       COMPRESSION_RATIO, 
	       INPUT_BYTES_PER_SEC_DISPLAY in_sec,
	       OUTPUT_BYTES_PER_SEC_DISPLAY out_sec, 
	       TIME_TAKEN_DISPLAY
	FROM   V$RMAN_BACKUP_JOB_DETAILS
	ORDER BY SESSION_KEY;
	```
	The following sample output shows the speed of the backup jobs:
	```
	SESSION_KEY OPT COMPRESSION_RATIO IN_SEC     OUT_SEC    TIME_TAKEN
	----------- --- ----------------- ---------- ---------- ----------
	          9 NO                  1     8.24M      8.24M  00:01:14
	         16 NO         1.32732239     6.77M      5.10M  00:01:45
	        113 NO                  1     2.99M      2.99M  00:00:44
	```
4. Query the `V$RMAN_BACKUP_JOB_DETAILS` view for the size of the backups in an RMAN session.
	If you run `BACKUP DATABASE`, then `V$RMAN_BACKUP_JOB_DETAILS.OUTPUT_BYTES` shows the total size of backup sets written by the backup job for the database that you are backing up. To view backup set sizes for all registered databases, query `V$RMAN_BACKUP_JOB_DETAILS`.
	The following query shows the backup job size and throughput ordered by session key, which is the primary key for the RMAN session. The columns `in_size` and `out_size` display the data input and output per second.
	```
	COL in_size  FORMAT a10
	COL out_size FORMAT a10
	SELECT SESSION_KEY, 
	       INPUT_TYPE,
	       COMPRESSION_RATIO, 
	       INPUT_BYTES_DISPLAY in_size,
	       OUTPUT_BYTES_DISPLAY out_size
	FROM   V$RMAN_BACKUP_JOB_DETAILS
	ORDER BY SESSION_KEY;
	```
	The following sample output shows the size of the backup jobs:
	```
	SESSION_KEY INPUT_TYPE    COMPRESSION_RATIO IN_SIZE    OUT_SIZE
	----------- ------------- ----------------- ---------- ----------
	         10 DATAFILE FULL                 1   602.50M    602.58M
	         17 DB FULL              1.13736669   634.80M    558.13M
	```

#### 11.4.2 Determining the Encryption Status of Backup Pieces

The `ENCRYPTED` column of the `V$BACKUP_PIECE` and `V$RMAN_BACKUP_PIECE` views indicates whether a backup piece is encrypted (`YES`) or unencrypted (`NO`).

For example, you can run the following query in SQL\*Plus to determine which backup pieces are encrypted:

```
COL BS_REC    FORMAT 99999
COL BP_REC    FORMAT 99999
COL MB        FORMAT 9999999
COL ENCRYPTED FORMAT A7
COL TAG       FORMAT A25

SELECT S.RECID AS "BS_REC", P.RECID AS "BP_REC", P.ENCRYPTED, 
       P.TAG, P.HANDLE AS "MEDIA_HANDLE"
FROM   V$BACKUP_PIECE P, V$BACKUP_SET S
WHERE  P.SET_STAMP = S.SET_STAMP
AND    P.SET_COUNT = S.SET_COUNT;
```

The following sample output shows that the backups are encrypted:

```
BS_REC BP_REC ENCRYPT TAG
------ ------ ------- -------------------------
MEDIA_HANDLE
--------------------------------------------------------------------------------
     1      1 YES     TAG20070711T140124
/disk1/c-39525561-20070711-00
 
     2      2 YES     TAG20070711T140128
/disk1/c-39525561-20070711-01
 
     3      3 YES     TAG20070711T140130
/disk1/c-39525561-20070711-02
```

### 11.5 Querying Recovery Catalog Views

The `LIST`, `REPORT`, and `SHOW` commands provide the easiest means of accessing the data in the control file and the recovery catalog.

Nevertheless, you can sometimes also obtain useful information from the recovery catalog views, which reside in the recovery catalog schema and use the `RC_` prefix.

#### 11.5.1 About Recovery Catalog Views

RMAN obtains backup and recovery metadata from a target database control file and stores it in the tables of the recovery catalog. The recovery catalog views are derived from these tables. The recovery catalog views are not normalized or optimized for user queries.

In general, the recovery catalog views are not as user-friendly as the RMAN reporting commands. For example, when you start RMAN and connect to a target database, you obtain the information for this target database only when you issue `LIST`, `REPORT`, and `SHOW` commands. If you have 10 different target databases registered in the same recovery catalog, then any query of the catalog views shows the metadata for all incarnations of all 10 databases. You often must perform complex selects and joins among the views to extract usable information about a database [incarnation](glossary.md).

Most of the catalog views have a corresponding `V$` view in the database. For example, `RC_BACKUP_PIECE` corresponds to `V$BACKUP_PIECE`. The primary difference between the recovery catalog view and corresponding `V$` view is that each recovery catalog view contains metadata about all the target databases registered in the recovery catalog. The `V$` view contains information only about itself.

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF003) for a description of recovery catalog views

##### 11.5.1.1 About Unique Identifiers for Registered Databases

Most recovery catalog views contain the columns `DB_KEY` and `DBINC_KEY`. Each database registered in the recovery catalog can be uniquely identified by either the primary key, which is the `DB_KEY` column value, or the `DBID`, which is the 32-bit unique database identifier. Each incarnation of a database is uniquely identified by the `DBINC_KEY` column.

You can use `DB_KEY` and `DBINC_KEY` to retrieve the records of a specific incarnation of a target database. Then, you can perform joins with most of the other catalog views to isolate records belonging to this incarnation.

An important difference between catalog and `V$` views is that a different system of unique identifiers is used for backup and recovery files. For example, many `V$` views such as `V$ARCHIVED_LOG` use the `RECID` and `STAMP` columns to form a concatenated primary key. The corresponding recovery catalog view uses a derived value as its primary keys and stores this value in a single column. For example, the primary key in `RC_ARCHIVED_LOG` is the `AL_KEY` column. The `AL_KEY` column value is the primary key that RMAN displays in the `LIST` command output.

##### 11.5.1.2 About Unique Identifiers in a Data Guard Environment

Special considerations apply when querying the recovery catalog in a Data Guard environment.

In a Data Guard environment, multiple databases share the same DBID. Several views contain a `DB_UNIQUE_NAME` column, which indicates the `DB_UNIQUE_NAME` of the database incarnation to which the record belongs. All databases in a Data Guard environment share the same DBID but have different `DB_UNIQUE_NAME` values.

The value of `DB_UNIQUE_NAME` is `null` when the database name is not known to the catalog, as for Oracle9i databases that are registered in a recovery catalog. Also, the column value is `null` when a database is upgraded to Oracle Database 11g or later but the recovery catalog schema has not reconciled the database names for all files.

In the recovery catalog views, the primary database and its associated standby databases share the same `DB_KEY`. However, every database in a Data Guard environment has a unique `RC_SITE.SITE_KEY` value. For example, a primary database `prod` and its standby database `standby1` might both have the `DB_KEY` value of 1, whereas the `SITE_KEY` of `prod` is 3 and the `SITE_KEY` of `standby1` is 30.

Some recovery catalog views do not have a `DB_UNIQUE_NAME` column, but include a `SITE_KEY` column. You can use the `SITE_KEY` column to join with `RC_SITE.SITE_KEY` to determine the `DB_UNIQUE_NAME` of the database associated with a file. As explained in " [About RMAN File Management in a Data Guard Environment](rman-architecture.md) ", every file in a Data Guard environment is associated with the primary or standby database that created it.

See Also:

[Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=SBYDB04700) to learn how to report on and manage files in a Data Guard environment

#### 11.5.2 Querying Catalog Views for the Target DB\_KEY or DBID Values

The `DB_KEY` value, which is the primary key for a registered database, is used only in the recovery catalog. The easiest way is to obtain the `DB_KEY` is to use the DBID of the target database, which is displayed whenever you connect RMAN to a database as `TARGET`.

The DBID distinguishes databases registered in the RMAN recovery catalog.

Assume that you want to obtain information about a database registered in the recovery catalog.

To query the catalog for information about the current incarnation of a database:

1. Determine the DBID for the database whose records you want to view.
	You can obtain the DBID by looking at the output displayed when RMAN connects to the database, querying `V$RMAN_OUTPUT`, or querying a `V$DATABASE` view. The following example connects SQL\*Plus to the desired database and queries the DBID:
	```
	SQL> CONNECT / AS SYSBACKUP
	SQL> SELECT DBID 
	  2  FROM   V$DATABASE;
	     DBID
	---------
	598368217
	```
2. Start SQL\*Plus and connect to the recovery catalog database as the owner of the recovery catalog.
3. Obtain the database key for the database whose DBID you obtained in Step 1.
	To obtain the `DB_KEY` for a database run the following query, where `dbid_of_target` is the DBID obtained in Step 1:
	```
	SELECT DB_KEY 
	FROM   RC_DATABASE 
	WHERE  DBID = dbid_of_target;
	```
4. Query the records for the current incarnation of the database whose DBID you obtained in Step 1.
	To obtain information about the current incarnation of a target database, specify the target database `DB_KEY` value and perform a join with the `RC_DATABASE_INCARNATION` view. Use a `WHERE` condition to specify that the `CURRENT_INCARNATION` column value is set to `YES`. For example, to obtain information about backup sets in the current incarnation of a target database with the `DB_KEY` value of `1`, query as follows:
	```
	SELECT BS_KEY, BACKUP_TYPE, COMPLETION_TIME
	FROM   RC_DATABASE_INCARNATION i, RC_BACKUP_SET b
	WHERE  i.DB_KEY = 1
	AND    i.DB_KEY = b.DB_KEY
	AND    i.CURRENT_INCARNATION = 'YES';
	```

See Also:

- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF174) for details about the `RC_DATABASE_INCARNATION` view
- [About Database Incarnations](rman-data-repair-concepts.md)

#### 11.5.3 Querying RC\_BACKUP\_FILES

You can query the view `RC_BACKUP_FILES` for information about all backups of any database registered in the recovery catalog. Before querying `RC_BACKUP_FILES`, however, you must call the `DBMS_RCVMAN.SETDATABASE` procedure.

Specify the DBID of a database registered in the recovery catalog, as shown in the following example:

```
SQL> CALL DBMS_RCVMAN.SETDATABASE(null,null,null,2283997583);
```

The fourth parameter must be the DBID of a database registered in the recovery catalog. The other parameters must all be `NULL`.

See Also:

- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF1670) for details about the `RC_BACKUP_FILES` view
- [Determining the DBID of the Database](rman-complete-database-recovery.md) for techniques for determining the DBID of a database