---
title: "Backup and Recovery User's Guide"
book: "Database Backup and Recovery User's Guide"
doc_id: F31836-11
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/bradv/using-flasback-database-restore-points.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-users-guide
---

Use RMAN to configure, monitor, and maintain restore points as part of an overall data protection strategy

This chapter explains Flashback Database and restore points. It discusses configuring, monitoring, and maintaining these features as part of an overall data protection strategy.

Note:

Detailed information on recovery scenarios that use Flashback Database and normal and guaranteed restore points can be found in [Performing Flashback and Database Point-in-Time Recovery](rman-performing-flashback-dbpitr.md).

### 7.1 Overview of Flashback Database, Restore Points and Guaranteed Restore Points

Oracle Flashback Database and restore points are related data protection features that enable you to rewind data back in time to correct any problems caused by logical data corruption or user errors within a designated time window.

These features provide a more efficient alternative to point-in-time recovery and does not require a backup of the database to be restored first. The effects are similar to [database point-in-time recovery (DBPITR)](glossary.md). Flashback Database and restore points are not only effective in traditional database recovery situations but can also be useful during database upgrades, application deployments and testing scenarios when test databases must be quickly created and re-created. Flashback Database also provides an efficient alternative to rebuilding a failed primary database after a Data Guard failover.

Restore points provide capabilities related to Flashback Database and other media recovery operations. In particular, a guaranteed restore point created at a system change number (SCN) ensures that you can use Flashback Database to rewind the database to this SCN. You can use restore points and Flashback Database independently or together.

Flashback Database is accessible through both RMAN and SQL as `FLASHBACK DATABASE`. You can use either language to quickly recover the database from logical data corruption or user errors. The following examples return the database to a specified SCN or restore point:

```
FLASHBACK DATABASE TO RESTORE POINT before_upgrade;
FLASHBACK DATABASE TO SCN 202381;
```

See Also:

[Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=SBYDB4891)

#### 7.1.1 About Flashback Database

Flashback Database is similar to conventional point-in-time recovery in its effects. It enables you to return a database to its state at a time in the recent past. Flashback Database is much faster than point-in-time recovery because it does not require restoring data files from backup and requires applying fewer changes from the archived redo logs.

You can use Flashback Database to reverse most unwanted changes to a database if the data files are intact. You can return a database to its state in a previous [incarnation](glossary.md), and undo the effects of an [`ALTER DATABASE OPEN RESETLOGS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=SQLRF00802) statement. " [Rewinding a Database with Flashback Database](rman-performing-flashback-dbpitr.md) " explains how to use the `FLASHBACK` `DATABASE` command to reverse database changes.

Flashback Database uses its own logging mechanism, creating [flashback logs](glossary.md) and storing them in the [fast recovery area](glossary.md). You can only use Flashback Database if flashback logs are available. To take advantage of this feature, you must set up your database in advance to create flashback logs.

To enable Flashback Database, you configure a fast recovery area and set a [flashback retention target](glossary.md). This retention target specifies how far back you can rewind a database with Flashback Database.

From that time onwards, at regular intervals, the database copies images of each altered block in every data file into the flashback logs. These block images can later be reused to reconstruct the data file contents for any moment at which logs were captured.

When you use Flashback Database to rewind a database to a past target time, the command determines which blocks changed after the target time and restores them from the flashback logs. The database restores the version of each block that is immediately before the target time. The database then uses redo logs to reapply changes that were made after these blocks were written to the flashback logs.

Redo logs on disk or tape must be available for the entire time period spanned by the flashback logs. For example, if the flashback retention target is 1 week, then you must ensure that online and archived redo logs that contain all changes for the past week are accessible. In practice, redo logs are typically needed much longer than the flashback retention target to support point-in-time recovery.

#### 7.1.2 About Flashback Database Window

The range of SCNs for which there is currently enough flashback log data to support the `FLASHBACK DATABASE` command is called the flashback database window. The flashback database window cannot extend further back than the earliest SCN in the available flashback logs.

You cannot back up flashback logs to locations outside the fast recovery area. To increase the likelihood that enough flashback logs are retained to meet the flashback database window, you can increase the space in your fast recovery area (see " [Table 5-3](configuring-rman-client-basic.md) ").

If the fast recovery area is not large enough to hold the flashback logs and files such as archived redo logs and other backups needed for the retention policy, then the database may delete flashback logs from the earliest SCNs forward to make room for other files. Consequently, the flashback database window can be shorter than the flashback retention target, depending on the size of the fast recovery area, other backups that must be retained, and how much flashback logging data is needed. The flashback retention target is a target, not a guarantee that Flashback Database is available.

If you cannot use `FLASHBACK DATABASE` because the flashback database window is not long enough, then usually you can use database point-in-time recovery (DBPITR) to achieve a similar result. Guaranteed restore points are the only way to ensure that you can use Flashback Database to return to a specific point in time or guarantee the size of the flashback window.

Note:

Some database operations, such as dropping a tablespace cannot be reversed with Flashback Database. See " Limitations of Flashback Database " for details.

See Also:

- [Rewinding a Database with Flashback Database](rman-performing-flashback-dbpitr.md) to learn about Flashback Database
- [Performing Database Point-in-Time Recovery](rman-performing-flashback-dbpitr.md) to learn about DBPITR

#### 7.1.3 Limitations of Flashback Database

Because Flashback Database works by undoing changes to the data files that exist at the moment when you run the command, it has certain limitations.

Following are the limitations of Flashback Database:

- Flashback Database can only undo changes to a data file made by Oracle Database. It cannot be used to repair media failures, or to recover from accidental deletion of data files.
- You cannot use Flashback Database alone to retrieve a dropped data file. If you flash back a database to a time when a dropped data file existed in the database, only the data file entry is added to the control file. You can only recover the dropped data file by using RMAN to fully restore and recover the data file.
- If the database control file is restored from backup or re-created, all accumulated flashback log information is discarded. You cannot use `FLASHBACK DATABASE` to return to a point in time before the restore or re-creation of a control file.
- When using Flashback Database with a target time at which a `NOLOGGING` operation was in progress, block corruption is likely in the database objects and data files affected by the `NOLOGGING` operation. For example, if you perform a direct-path `INSERT` operation in `NOLOGGING` mode, and that operation runs from 9:00 to 9:15 on April 3, 2005, and you later use Flashback Database to return to the target time 09:07 on that date, the objects and data files updated by the direct-path `INSERT` may be left with block corruption after the Flashback Database operation completes.
	If possible, avoid using Flashback Database with a target time or SCN that coincides with a `NOLOGGING` operation. Also, perform a full or incremental backup of the affected data files immediately after any `NOLOGGING` operation to ensure recoverability to points in time after the operation. If you expect to use Flashback Database to return to a point in time during an operation such as a direct-path `INSERT`, consider performing the operation in `LOGGING` mode.
	See Also:
	[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=SQLRF30009) for more information about operations that support `NOLOGGING` mode.

#### 7.1.4 About Normal Restore Points

Creating a normal restore point assigns a restore point name to an SCN or specific point in time.

Thus, a restore point functions as a bookmark or alias for this SCN. Before performing any operation that you may have to reverse, you can create a normal restore point. The control file stores the name of the restore point and the SCN.

If you use flashback features or point-in-time recovery, then you can use the name of the restore point instead of a time or SCN. The following commands support this use of restore points:

- The [`RECOVER DATABASE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF140) and `FLASHBACK DATABASE` commands in RMAN
- The [`FLASHBACK TABLE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=SQLRF01802) statement in SQL

Creating a normal restore point eliminates manually recording an SCN in advance or determine the correct SCN after the fact by using features such as Flashback Query.

Normal restore points are lightweight. The control file can maintain a record of thousands of normal restore points with no significant effect on database performance. Normal restore points eventually age out of the control file if not manually deleted, so they require no ongoing maintenance.

See Also:

[Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=ADFNS1008) to learn how to use Flashback Query

#### 7.1.5 About Guaranteed Restore Points

Like a normal restore point, a guaranteed restore point serves as an alias for an SCN in recovery operations. A principal difference is that guaranteed restore points never age out of the control file and must be explicitly dropped.

In general, you can use a guaranteed restore point as an alias for an SCN with any command that works with a normal restore point. Except as noted, the information about where and how to use normal restore points applies to guaranteed restore points as well.

A guaranteed restore point ensures that you can use Flashback Database to rewind a database to its state at the restore point SCN, even if the generation of flashback logs is disabled. If flashback logging is enabled, then a guaranteed restore point enforces the retention of flashback logs required for Flashback Database to any SCN after the earliest guaranteed restore point. Thus, if flashback logging is enabled, you can rewind the database to any SCN in the continuum rather than to a single SCN only.

Note:

If flashback logging is disabled, then you cannot `FLASHBACK DATABASE` directly to SCNs between the guaranteed restore points and the current time. You can, however, flashback to the guaranteed restore point first and then recover to SCN's between the guaranteed restore point and current time.

If the recovery area has enough disk space to store the needed logs, then you can use a guaranteed restore point to rewind a whole database to a known good state days or weeks ago. As with Flashback Database, even the effects of `NOLOGGING` operations like direct load inserts can be reversed with guaranteed restore points.

Note:

Limitations that apply to Flashback Database also apply to guaranteed restore points. For example, dropping a tablespace can prevent flashing back the affected data files to the guaranteed restore point. See " Limitations of Flashback Database " for details. In addition, when there are guaranteed restore points in the database, the database compatibility parameter cannot be set to a higher database version. An attempt to do so results in an error. This restriction exists because flashback database is currently unable to reverse the effects of increasing the database version with the compatibility initialization parameter.

##### 7.1.5.1 Guaranteed Restore Points versus Storage Snapshots

In practice, guaranteed restore points provide a useful alternative to storage snapshots.

Storage snapshots are often used to protect a database before risky operations such as large-scale database updates or application patches or upgrades. Rather than creating a snapshot or [duplicate database](glossary.md) to test the operation, you can create a guaranteed restore point on a primary or [physical standby database](glossary.md). You can then perform the risky operation with the certainty that the required flashback logs are retained.

#### 7.1.6 Overview of Restore Points in a Multitenant Environment

You can create both normal and guaranteed restore points in a multitenant environment.

The basic concepts of restore points for databases are also applicable to restore points in a multitenant environment. You can create the following types of restore points in a multitenant environment:

- CDB restore point
- PDB restore point
- Clean PDB restore point

See Also:

- Overview of Flashback Database, Restore Points and Guaranteed Restore Points

##### 7.1.6.1 About CDB Restore Points

A CDB restore point serves as an alias for an SCN or a point in time in a multitenant container database (CDB). It can be a normal restore point or a guaranteed restore point.

You connect to the root of the target database as a common user with the `SYSDBA` or `SYSBACKUP` privilege to create CDB restore points. You can create CDB restore points starting with Oracle Database 12c Release 1 (12.1). CDB restore points are accessible to every pluggable database within the CDB. However, a CDB restore point does not reflect the PDB sub-incarnation of any of its PDBs.

CDB restore points are useful in the following scenarios:

- The whole CDB needs to be recovered to a particular point in time
- Multiple PDBs in a CDB need to be recovered to a particular point in time

See Also:

- About Restore Points in PDBs

##### 7.1.6.2 About Restore Points in PDBs

You can create normal and guaranteed restore points in a pluggable database (PDB). PDB restore points are accessible only to the PDB in which they are defined.

PDB Restore Points

A PDB restore point is a bookmark to a point in time or an SCN in a particular [pluggable database (PDB)](glossary.md). It pertains only to the PDB for which it is created and is only usable for operations on that PDB. A PDB restore point represents the PDB sub-incarnation of the point in time at which it was created.

PDB restore points can be normal restore points or guaranteed restore points. A guaranteed PDB restore point guarantees that you can perform a flashback operation for the PDB to this restore point.

A PDB restore point can be used to perform Flashback Database operations or point-in-time recovery only for the PDB in which it was created.

Note:

Creating a guaranteed PDB restore point requires careful consideration because such a restore point can prevent required flashback logs in the [multitenant container database (CDB)](glossary.md) from being reused. This can potentially impact CDB functioning because the fast recovery area could run out of space.

Clean PDB Restore Points

A clean PDB restore point is a PDB restore point that is created when the PDB is closed and when there are no outstanding transactions for that PDB. Clean PDB restore points are only applicable to CDBs that use shared undo.

Clean PDB restore points can be normal or guaranteed restore points. Use the `CREATE CLEAN RESTORE POINT` command to explicitly create a clean PDB restore point. For a CDB that uses shared undo, if a PDB is closed and it has no outstanding transactions, any PDB restore point created is marked as a clean PDB restore point.

If you anticipate that you may need to rewind a PDB to a particular point in time, for example, to a state just before an application upgrade, then it is recommended that you create a clean PDB guaranteed restore point.

For CDBs that use shared undo, a Flashback Database operation to a clean PDB restore point is faster than a Flashback Database operation to an SCN or other restore points that are not clean PDB restore points. This is because RMAN does not need to restore any backups while performing a flashback operation to a clean PDB restore point.

##### 7.1.6.3 About the Namespace for PDB Restore Points

Each pluggable database (PDB) has its own namespace for restore points. Therefore, you can define a PDB restore point with the same name in more than one PDB.

In a multitenant environment, when you use a restore point name in a PDB or for a PDB operation, the name is first interpreted as a [PDB restore point](glossary.md) for the concerned PDB. If a PDB restore point with the specified name is not found, then it is interpreted as a [CDB restore point](glossary.md).

See Also:

About Restore Points in PDBs

### 7.2 About Logging for Flashback Database and Guaranteed Restore Points

Logging for Flashback Database and guaranteed restore points involves capturing images of data file blocks before changes are applied. The `FLASHBACK DATABASE` command can use these images to return the data files to their previous state.

The chief differences between normal flashback logging and logging for guaranteed restore points are related to when blocks are logged and whether the logs can be deleted in response to space pressure in the fast recovery area. These differences affect space usage for logs and database performance.

Your recoverability goals partially determine whether to enable logging for flashback database, or use guaranteed restore points, or both. The implications in performance and in space usage for these features, separately and when used together, also factor into your decision.

#### 7.2.1 Guaranteed Restore Points and Fast Recovery Area Space Usage

Certain rules govern the usage of space in the fast recovery area.

When you create a guaranteed restore point, with or without enabling full flashback database logging, you must monitor the space available in your fast recovery area. " [Managing Space for Flashback Logs in the Fast Recovery Area](maintaining-rman-backups.md) " explains how to monitor fast recovery area disk space usage.

The following rules govern creating, retaining, overwriting and deleting of flashback logs in the fast recovery area:

- If the fast recovery area has enough space, then a flashback log is created whenever necessary to satisfy the flashback retention target.
- If a flashback log is old enough that it is no longer needed to satisfy the flashback retention target, then the flashback log may be reused or deleted.
- If the database must create a flashback log and the fast recovery area is full or there is no disk space, then the oldest flashback log is reused instead.
	Note:
	Reusing the oldest flashback log shortens the flashback database window. If enough flashback logs are reused due to a lack of disk space, then the flashback retention target may not be satisfied.
- If the fast recovery area is full, then an archived redo log that is reclaimable according to the fast recovery area rules may be automatically deleted by the fast recovery area to make space for other files. In this case, any flashback logs that require the use of that redo log file for the use of `FLASHBACK DATABASE` are also deleted.
	Note:
	According to fast recovery area rules, a file is reclaimable when one of the following criteria is true:
	- The file is reported as obsolete and not needed by the flashback database. For example, the file is outside the `DB_FLASHBACK_RETENTION_TARGET` parameters.
	- The file is backed up to tape.
- Files in the fast recovery area are not eligible for deletion or reuse if they are required to satisfy a guaranteed restore point. However, archived redo logs required to satisfy a guaranteed restore point may be deleted after they are backed up to disk or tape. When you use the RMAN `FLASHBACK                         DATABASE` command, if the archived redo logs required to satisfy a specified guaranteed restore point are not available in the fast recovery area, they are restored from the backups.
	Retention of flashback logs and other files required to satisfy the guaranteed restore point, in addition to files required to satisfy the backup retention policy, can cause the fast recovery area to fill completely. Consult " [Responding to a Full Fast Recovery Area](maintaining-rman-backups.md) " if your fast recovery area becomes full.

Caution:

If no files are eligible for deletion from the fast recovery area because of the requirements imposed by your retention policy and the guaranteed restore point, then the database performs as if it has encountered a disk full condition. In many circumstances, this causes your database to halt. See " [Responding to a Full Fast Recovery Area](maintaining-rman-backups.md) ".

#### 7.2.2 About Logging for Guaranteed Restore Points with Flashback Logging Disabled

Assume that you create a guaranteed restore point when logging for Flashback Database is disabled. In this case, the first time a data file block is modified after the time of the guaranteed restore point, the database stores an image of the block before the modification in the flashback logs. Thus, the flashback logs preserve the contents of every changed data block when the guaranteed restore point was created. Later modifications to the same block do not cause the contents to be logged again unless another guaranteed restore point was created after the block was last modified or a subsequent flashback database operation has restored the original contents of the block. When you use Flashback Database to restore a database multiple times to the same restore point, it is common practise to drop and recreate the guaranteed restore point each time. This deletes the old flashback logs and also ensures that the space quota for the fast recovery area is not exceeded.

This method of logging has the following important consequences:

- `FLASHBACK DATABASE` can re-create the data file contents at the time of a guaranteed restore point by using the block images.
- For workloads that repeatedly modify the same data, disk space usage can be less than normal flashback logging. Less space is needed because each changed block is only logged once. Applications with low volume inserts may benefit from this disk space saving. This advantage is less likely for applications with high volume inserts or large batch inserts. The performance overhead of logging for a guaranteed restore point without flashback database logging enabled can also be lower.

Assume that your primary goal is the ability to return your database to the time at which the guaranteed restore point was created. In this case, it is usually more efficient to turn off flashback logging and use only guaranteed restore points. For example, suppose that you are performing an application upgrade on a database host over a weekend. You could create a guaranteed restore point at the start of the upgrade. If the upgrade fails, then reverse the changes with the `FLASHBACK DATABASE` command.

#### 7.2.3 About Logging for Flashback Database with Guaranteed Restore Points Defined

If you enable Flashback Database and define one or more guaranteed restore points, then the database performs normal flashback logging.

In this case, the recovery area retains the flashback logs required to flash back to any arbitrary time between the present and the earliest currently defined guaranteed restore point. Flashback logs are not deleted in response to space pressure if they are required to satisfy the guarantee.

Flashback logging causes some performance overhead. Depending upon the pattern of activity on your database, it can also cause significant space pressure in the fast recovery area. Thus, you should monitor space used in the fast recovery area.

### 7.3 Prerequisites for Flashback Database and Restore Points

To ensure successful operation of Flashback Database and guaranteed restore points, you must first set some key database options.

Flashback Database

Configure the following database settings before enabling Flashback Database:

- Your database must be running in `ARCHIVELOG` mode, because archived logs are used in the Flashback Database operation.
- You must have a fast recovery area enabled, because flashback logs can only be stored in the fast recovery area.
- For Oracle Real Application Clusters (Oracle RAC) databases, the fast recovery area must be in a clustered file system or in ASM.
- For creating restore points in CDBs, the `COMPATIBLE` initialization parameter must be set to 12.1.0 or higher.

Guaranteed Restore Points

To use guaranteed restore points, the database must satisfy the following additional prerequisite: the [`COMPATIBLE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=REFRN10019) initialization parameter must be set to 10.2.0 or greater.

Note:

There are no special prerequisites to set before using normal restore points.

Restore Points in PDBs

To create restore points in a [pluggable database (PDB)](glossary.md), the `COMPATIBLE` initialization parameter must be set to 12.2.0 or higher.

### 7.4 Using Normal and Guaranteed Restore Points

You can create, monitor, and drop both normal and guaranteed restore points.

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=SQLRF20001) for reference information about the SQL `CREATE RESTORE POINT` statement

#### 7.4.1 Creating CDB Restore Points

To create or guaranteed restore points in a multitenant container database (CDB), use the `CREATE RESTORE POINT` SQL command. Provide a name for the restore point and specify whether it is to be a guaranteed restore point or a normal one (the default).

To create a CDB restore point:

1. Ensure that the prerequisites described in Prerequisites for Flashback Database and Restore Points are satisfied.
2. Connect SQL\*Plus to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege.
3. Ensure that the CDB is open or mounted. If the CDB is mounted, then it must have been shut down cleanly (unless it is a physical standby database).
4. Run the `CREATE RESTORE POINT` statement to create a CDB restore point.
	The following command creates a normal CDB restore point:
	```
	SQL> CREATE RESTORE POINT cdb_before_upgrade;
	```
	The following command creates a guaranteed CDB restore point:
	```
	SQL> CREATE RESTORE POINT cdb_grp_before_upgrade GUARANTEE FLASHBACK DATABASE;
	```

See Also:

- About CDB Restore Points

#### 7.4.2 Creating PDB Restore Points

You use the `CREATE RESTORE POINT` SQL statement to create normal PDB restore points, guaranteed PDB restore points, or clean PDB restore points in a pluggable database (PDB).

You can create PDB restore points either when connected to the PDB or to the root. When a PDB uses shared undo, you can create a clean restore point only if the PDB does not have any outstanding transactions.

To create a PDB restore point when connected to the PDB:

1. Ensure that the prerequisites described in Prerequisites for Flashback Database and Restore Points are met.
2. Connect SQL\*Plus to the PDB as a common user or local user with the `SYSDBA` or `SYSBACKUP` privilege.
3. If you are creating a clean PDB restore point in a CDB that uses shared undo, then the PDB must be closed.
	The following command displays the state of the PDB:
	```
	SQL> SELECT name, open_mode FROM V$PDBs;
	```
	Use the following command to close the PDB:
	```
	SQL> ALTER PLUGGABLE DATABASE CLOSE;
	```
4. If the multitenant container database (CDB) is in mounted state, then it must have been shut down consistently (unless it is a physical standby database).
5. Set the current container to the PDB.
	The following command sets to current container to the PDB `my_pdb`:
	```
	SQL> ALTER SESSION SET CONTAINER=my_pdb;
	```
6. Create a PDB restore point by using the `CREATE RESTORE POINT` command.
	The following command creates a normal PDB restore point:
	```
	SQL> CREATE RESTORE POINT before_patching;
	```
	The following command creates a guaranteed PDB restore point:
	```
	SQL> CREATE RESTORE POINT before_upgrade GUARENTEE FLASHBACK DATABASE;
	```
	The following command explicitly creates a clean PDB restore point. If a clean restore point cannot be created, then an error is returned.
	```
	SQL> CREATE CLEAN RESTORE POINT before_patching;
	```

To create a PDB restore point when connected to the CDB:

1. Ensure that the prerequisites described in Prerequisites for Flashback Database and Restore Points are met.
2. Connect SQL\*Plus to the root of the target database as a common user with the `SYSDBA` or `SYSBACKUP` privilege.
3. If you are creating a clean PDB restore point in a CDB that uses shared undo, then the PDB must be closed.
	The following command closes the PDB `my_pdb`:
	```
	SQL> ALTER PLUGGABLE DATABASE my_pdb CLOSE;
	```
4. The CDB that contains the PDB can be open or mounted. If the CDB is mounted, then it must have been shut down consistently (unless it is a physical standby database).
	The following commands place the CDB in a mounted state:
	```
	SQL> SHUTDOWN IMMEDIATE;
	SQL> STARTUP MOUNT;
	```
5. Set the current container to the root.
	`SQL> ALTER SESSION SET CONTAINER = CDB$ROOT;`
6. Create a PDB restore point by using the `CREATE RESTORE POINT` command with the `FOR PLUGGABLE DATABASE` clause.
	The following command creates a normal PDB restore point:
	```
	SQL> CREATE RESTORE POINT mypdb_before_patching FOR PLUGGABLE DATABASE my_pdb;
	```
	The following command creates a guaranteed PDB restore point:
	```
	SQL> CREATE RESTORE POINT mypdb_grp_before_upgrade FOR PLUGGABLE DATABASE my_pdb GUARANTEE FLASHBACK DATABASE;
	```
	The following command explicitly creates a clean PDB restore point (when the PDB is closed and has no pending transactions). If the restore point cannot be created, then an error is displayed.
	```
	SQL> CREATE CLEAN RESTORE POINT mypdb_crp_before_patching FOR PLUGGABLE DATABASE my_pdb;
	```

See Also:

- [About Undo and Flashback Database Operations for PDBs](rman-performing-flashback-dbpitr.md)
- About Restore Points in PDBs

#### 7.4.3 Listing Restore Points Using the LIST Command

Use the `LIST` command to list either a specific restore point or all restore points known to the RMAN repository.

The variations of the `LIST` command are as follows:

```
LIST RESTORE POINT restore_point_name;
LIST RESTORE POINT ALL;
```

RMAN indicates the SCN and time of the restore point, the type of restore point, and the name of the restore point. The following example shows sample output:

```
RMAN> LIST RESTORE POINT ALL;
 
using target database control file instead of recovery catalog
SCN              RSP Time  Type       Time      Name
---------------- --------- ---------- --------- ----
341859           28-APR-15            28-APR-15 NORMAL_RS
343690           28-APR-15 GUARANTEED 28-APR-15 GUARANTEED_RS
```

Note:

The `LIST` command does not display details such as the PDB incarnation number and whether a restore point is a PDB restore point. To view additional details about restore points in a multitenant environment, see Listing Restore Points Using the V$RESTORE\_POINT View.

See Also:

" [Rewinding a Database with Flashback Database](rman-performing-flashback-dbpitr.md) "

#### 7.4.4 Listing Restore Points Using the V$RESTORE\_POINT View

You can use the `V$RESTORE_POINT` control file view to obtain information about all currently-defined restore points (normal and guaranteed), including CDB restore points and PDB restore points.

The `V$RESTORE_POINT` view contains additional information about restore points in a multitenant environment that is not displayed by the `LIST RESTORE POINT` command. This includes details such as the incarnation of the [pluggable database (PDB)](glossary.md) in which a [PDB restore point](glossary.md) was created and whether a restore point is a PDB restore point or clean PDB restore point.

The following steps display information about PDB restore points for all PDBs in the CDB:

1. Connect SQL\*Plus to the target database. If the target database is a [multitenant container database (CDB)](glossary.md), then connect to the root.
	- To view restore points for all PDBs, you must connect to the root as a common use with the `SYSDBA` or `SYSBACKUP` privilege.
	- To view the restore points in a particular PDB, you can connect to that PDB as a common user or local user with the `SYSDBA` or `SYSBACKUP` privilege.
2. Query the `V$RESTORE_POINT` view to display information about restore points.

Example 7-1 Displaying Restore Points in a Multitenant Environment

The following query displays details about all restore points in a multitenant environment (query output formatted to fit in the page):

```
SELECT name, guarantee_flashback_database, pdb_restore_point, clean_pdb_restore_point, pdb_incarnation#, storage_sizeFROM v$restore_point;
```
```
NAME                         GUARANTEE_  PDB_RESTORE_POINT  CLEAN_PDB_RESTORE_POINT  STORAGE_SIZE
--------                     ----------  ----------------   -----------------------  ------------
CDB_GRP_BEFORE_PATCH            YES         NO                  NO                     84586
PDB_GRP_BEFORE_UPGRADE_TEMP     YES         YES                 NO                      4562
CDB_RP1                         NO          NO                  NO                         0
PDB1_BEFORE_PATCHING            NO          YES                 NO                         0
MYPDB_CLEAN_GRP_BEFORE_UPGRADE  NO          YES                 YES                        0
```

For normal restore points, `STORAGE_SIZE` is zero. For guaranteed restore points, `STORAGE_SIZE` indicates the approximate number of bytes of disk space in the fast recovery area that is tied up retaining logs required to guarantee `FLASHBACK` `DATABASE` to that restore point.

See Also:

- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=REFRN30390) for information about `V$RESTORE_POINT`
- Listing Restore Points Using the LIST Command
- [Rewinding a Database with Flashback Database](rman-performing-flashback-dbpitr.md)
- [Performing a Flashback Database Operation](rman-performing-flashback-dbpitr.md)
- [Performing a Flashback Database Operation for PDBs](rman-performing-flashback-dbpitr.md)

#### 7.4.5 Dropping Restore Points

When you are satisfied that you do not need an existing restore point, or when you want to create a restore point with the name of an existing restore point, you can drop the restore point, using the `DROP RESTORE POINT` SQL\*Plus statement.

For example:

```
SQL> DROP RESTORE POINT before_app_upgrade;
Restore point dropped.
```

The same statement is used to drop both normal and guaranteed restore points.

Note:

Normal restore points eventually age out of the control file, even if not explicitly dropped. The rules governing retention of restore points in the control file are:

- The most recent 2048 restore points are always kept in the control file, regardless of their age.
- Any restore point more recent than the value of `CONTROL_FILE_RECORD_KEEP_TIME` is retained, regardless of how many restore points are defined.

Normal restore points that do not meet either of these conditions may age out of the control file.

Guaranteed restore points never age out of the control file. They remain until they are explicitly dropped.

See also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=SQLRF20002) for reference information about the SQL `DROP RESTORE POINT` statement

### 7.5 Using Flashback Database

To use flashback logging for a target database, you must enable Flashback Database. Certain guidelines can be followed to ensure optimal performance of Flashback Database.

This section contains the following topics:

- Enabling Flashback Database
- Disabling Flashback Database Logging
- Configuring the Environment for Optimal Flashback Database Performance
- Monitoring the Effect of Flashback Database on Performance
- About Flashback Writer (RVWR) Behavior with I/O Errors

#### 7.5.1 Enabling Flashback Database

Use the `ALTER DATABASE` command to enable Flashback Database

To enable flashback logging:

1. Configure the recovery area as described in " [Enabling the Fast Recovery Area](configuring-rman-client-basic.md) ".
2. Ensure the database instance is open or mounted. If the instance is mounted, then the database must be shut down cleanly unless it is a physical standby database. Other Oracle Real Application Clusters (Oracle RAC) instances can be in any mode.
3. Optionally, set the `DB_FLASHBACK_RETENTION_TARGET` to the length of the desired flashback window in minutes:
	```
	ALTER SYSTEM SET DB_FLASHBACK_RETENTION_TARGET=4320 SCOPE=BOTH; # 3 days
	```
	By default `DB_FLASHBACK_RETENTION_TARGET` is set to 1 day (1440 minutes).
	Note:
	This setting must be persistent across database startup and shutdown.
4. Enable the Flashback Database feature for the whole database:
	```
	ALTER DATABASE FLASHBACK ON;
	```
5. Optionally, disable flashback logging for specific tablespaces.
	By default, flashback logs are generated for all permanent tablespaces. You can reduce overhead by disabling flashback logging for specific tablespaces as in the following example:
	```
	ALTER TABLESPACE tbs_3 FLASHBACK OFF;
	```
	You can re-enable flashback logging for a tablespace later with this command:
	```
	ALTER TABLESPACE tbs_3 FLASHBACK ON;
	```
	If you disable Flashback Database for a tablespace, then you must take its data files offline before running `FLASHBACK` `DATABASE`.

When you enable Flashback Database while the database is open, there is a very small chance the command may not be able to obtain the memory it needs. If the command fails because of that reason, retry the command after a while or retry after a shutdown and restart of the instance.

When you enable Flashback Database on a [physical standby database](glossary.md), you can flash back a standby database. Flashback Database of standby databases has some applications in the Data Guard environment.

See Also:

[Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=SBYDB4891) for details about standby databases

#### 7.5.2 Disabling Flashback Database Logging

Use the `ALTER DATABASE` command to disable Flashback Database.

On a database instance that is either in mount or open state, issue the following command:

```
ALTER DATABASE FLASHBACK OFF;
```

#### 7.5.3 Configuring the Environment for Optimal Flashback Database Performance

Maintaining flashback logs imposes comparatively limited overhead on a database instance. Changed blocks are written from memory to the flashback logs at relatively infrequent, regular intervals, to limit processing and I/O overhead.

To achieve good performance for large production databases with Flashback Database enabled, Oracle recommends the following:

- Use a fast file system for your fast recovery area, preferably without operating system file caching.
	Files that the database creates in the fast recovery area, including flashback logs, are typically large. Operating system file caching is typically not effective for these files, and may actually add CPU overhead for reading from and writing to these files. Thus, it is recommended to use a file system that avoids operating system file caching, such as Automatic Storage Management (ASM).
- Configure enough disk spindles for the file system that holds the fast recovery area.
	For large production databases, multiple disk spindles may be needed to support the required disk throughput for the database to write the flashback logs effectively.
- If the storage system used to hold the fast recovery area does not have nonvolatile RAM, then try to configure the file system on striped storage volumes.
	Use a relatively small stripe size such as 128 KB. This technique enables each write to the flashback logs to be spread across multiple spindles, improving performance.
- For large databases, set the initialization parameter `LOG_BUFFER` to at least 8 MB.

The overhead of logging for Flashback Database depends on the mixture of reads and writes in the database workload. When you have a write-intensive workload, the Flashback Database logging overhead is high since it must log all those database changes. Queries do not change data and thus do not contribute to logging activity for Flashback Database.

#### 7.5.4 Monitoring the Effect of Flashback Database on Performance

Several data analysis methods are available to monitor the Flashback Database workload on your system.

- AWR reports
	The Automatic Workload Repository (AWR) automates database statistics gathering by collecting, processing, and maintaining performance statistics for database problem detection and self-tuning. You can compare AWR reports from before and after the Flashback Database was turned on to monitor performance effects.
- AWR snapshots
	You can review AWR snapshots to pinpoint system usage caused by flashback logging. For example, if `flashback buf free by RVWR` is the top wait event, then you know that Oracle Database cannot write flashback logs very quickly. Therefore, you might want to tune the file system and storage used by the fast recovery area, possibly using a technique described in " Configuring the Environment for Optimal Flashback Database Performance "
- `V$FLASHBACK_DATABASE_STAT` view
	The `V$FLASHBACK_DATABASE_STAT` view shows the bytes of flashback data logged by the database. Each row in the view shows the statistics accumulated (typically over the course of an hour). The `FLASHBACK_DATA` and `REDO_DATA` columns describe bytes of flashback data and redo data written respectively during the time interval, while the `DB_DATA` column describes bytes of data blocks read and written. The columns `FLASHBACK_DATA` and `REDO_DATA` correspond to sequential writes, whereas `DB_DATA` column corresponds to random reads and writes.
- `V$SYSSTAT` view
	Because of the difference between sequential I/O and random I/O, a better indication of I/O overhead is the number of I/O operations issued for flashback logs. The `V$SYSSTAT` statistics shown in Table 7-1 can tell you the number of I/O operations that your instance has issued for various purposes.

Table 7-1 V$SYSSTAT Statistics

| Column Name | Column Meaning |
| --- | --- |
| Physical write I/O request | The number of write operations issued for writing data blocks |
| Physical read I/O request | The number of read operations issued for reading data blocks |
| Redo writes | The number of write operations issued for writing to the redo log |
| Flashback log writes | The number of write operations issued for writing to flashback logs |
| Flashback log write bytes | Total size in bytes of flashback database data written from this instance |

See Also:

- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=REFRN103) for more details on columns in the `V$SYSSTAT` view
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=TGDBA185) to learn about AWR
- [Oracle Database 2 Day + Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=TDPPT091) for more information about AWR reports

#### 7.5.5 About Flashback Writer (RVWR) Behavior with I/O Errors

When flashback is enabled or when there are guaranteed restore points, the background process RVWR writes flashback data to flashback database logs in the fast recovery area.

If RVWR encounters an I/O error, then the following behavior is expected:

- If there are any guaranteed restore points defined, then the instance fails when RVWR encounters I/O errors.
- If no guaranteed restore points are defined, then the instance remains unaffected when RVWR encounters I/O errors. Note the following cases:
	- On a primary database, Oracle Database automatically disables Flashback Database while the database is open. All existing transactions and queries proceed unaffected. This behavior is expected for both single-instance and Oracle RAC databases.
		- On a physical or logical standby, RVWR appears to have stopped responding, retrying the I/O periodically. This may eventually cause the logical standby or the managed recovery of the physical standby to suspend. (Oracle Database does not cause the standby instance to fail because it does not want to cause the primary database to fail in maximum protection mode.) To resolve the issue, you can issue either a `SHUTDOWN ABORT` or an `ALTER DATABASE FLASHBACK OFF` command.