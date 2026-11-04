---
title: Performing Flashback and Database Point-in-Time Recovery
book: "Backup and Recovery User's Guide"
doc_id: E10642-08
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmflash.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-users-guide
---

## 18 Performing Flashback and Database Point-in-Time Recovery

This chapter explains how to investigate unwanted database changes, and select and perform an appropriate recovery strategy based upon Oracle Flashback Technology and database backups. It includes the following topics:

## Overview of Oracle Flashback Technology and Database Point-in-Time Recovery

This section explains the purpose and basic concepts of Flashback Technology and database point-in-time recovery.

### Purpose of Flashback and Database Point-in-Time-Recovery

Typically, the following situations call for flashback features or point-in-time recovery:

- A user error or corruption removes needed data or introduces corrupted data. For example, a user or DBA might erroneously delete or update the contents of one or more tables, drop database objects that are still needed during an update to an application, or run a large batch update that fails midway.
- A database upgrade fails or an upgrade script goes awry.
- A complete database recovery after a media failure cannot succeed because you do not have all of the needed redo logs or incremental backups.

In either situation, you can use point-in-time recovery or flashback features to return the database or database object to its state at a previous point in time.

### Basic Concepts of Point-in-Time Recovery and Flashback Features

The most basic solution to unwanted database changes is RMAN [database point-in-time recovery (DBPITR)](glossary.md). DBPITR is sometimes called [incomplete recovery](glossary.md) because it does not use all of the available redo or completely recover all changes to your database. In this case, you restore a whole database backup and then apply redo logs or incremental backups to re-create all changes up to a point in time before the unwanted change.

If unwanted database changes are extensive but confined to specific tablespaces, then you can use [tablespace point-in-time recovery (TSPITR)](glossary.md) to return these tablespaces to an earlier SCN while the unaffected tablespaces remain available. RMAN TSPITR is an advanced technique described in [Chapter 21, "Performing RMAN Tablespace Point-in-Time Recovery (TSPITR)"](rcmtspit.md).

Oracle Database also provides a set of features collectively known as Flashback Technology that supports viewing past states of data, and winding and rewinding data back and forth in time, without requiring the restore of the database from backup. Depending on the changes to your database, Flashback Technology can often reverse the unwanted changes more quickly and with less impact on database availability.

#### Basic Concepts of Database Point-in-Time Recovery

DBPITR works at the physical level to return the data files to their state at a target time in the past. In an RMAN DBPITR operation, you specify a target SCN, log sequence, restore point, or time. RMAN restores the database from backups created before the target time, and then applies incremental backups and logs to re-create all changes between the time of the data file backups and the end point of recovery. When the end point is specified as an SCN, the database applies the redo logs and stops at the end of each redo thread or the specified SCN, whichever occurs first. When the end point is specified as a time, the database internally determines a suitable SCN for the specified time and then recovers to this SCN.

If your backup strategy is properly designed and your database is running in `ARCHIVELOG` mode, then DBPITR is an option in nearly all circumstances. RMAN simplifies DBPITR in comparison to the user-managed DBPITR described in ["Performing Incomplete Database Recovery"](osrecvry.md). Given a target SCN, data files are restored from backup and recovered efficiently with no intervention from the user. Nevertheless, RMAN DBPITR has the following disadvantages:

- You cannot return selected objects to their earlier state, only the entire database.
- Your entire database is unavailable during the DBPITR.
- DBPITR can be time-consuming because RMAN must restore all data files. Also, RMAN may need to restore redo logs and incremental backups to recover the data files. If backups are on tape, then this process can take even longer.

#### Basic Concepts of Flashback Technology

The flashback features of Oracle are more efficient than media recovery in most circumstances in which they are available. You can use them to investigate past states of the database.

##### Physical Flashback Features Useful in Backup and Recovery

[Oracle Flashback Database](glossary.md), which is explained in "Rewinding a Database with Flashback Database", is the most efficient alternative to DBPITR. Unlike the other flashback features, it operates at a physical level and reverts the current data files to their contents at a past time. The result is like the result of a DBPITR, including the `OPEN RESETLOGS`, but Flashback Database is typically faster because it does not require you to restore data files and requires only limited application of redo compared to media recovery.

As explained in ["Configuring the Fast Recovery Area"](rcmconfb.md), a [fast recovery area](glossary.md) is required for Flashback Database. To enable logging for Flashback Database, you must set the [`DB_FLASHBACK_RETENTION_TARGET`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams061.htm#REFRN10233) initialization parameter and issue the `ALTER` `DATABASE` `FLASHBACK` `ON` statement.

During normal operation, the database periodically writes old images of data file blocks to the [flashback logs](glossary.md). Flashback logs are written sequentially and often in bulk. In some respects, flashback logging is like a continuous backup. The database automatically creates, deletes, and resizes flashback logs in the recovery area. Flashback logs are not archived. You need only be aware of flashback logs for monitoring performance and determining disk space allocation for the recovery area.

When you perform a Flashback Database operation, the database uses flashback logs to access past versions of data blocks and also uses some data in the archived redo logs. Consequently, you cannot enable Flashback Database after a failure is discovered and then use Flashback Database to rewind through this failure. You can use the related capability of guaranteed restore points to protect the contents of your database at a fixed point in time, such as immediately before a risky database change.

##### Logical Flashback Features Useful in Backup and Recovery

The remaining flashback features operate at the logical level. The logical features documented in this chapter are as follows:

- Flashback Table
	You can recover a table or set of tables to a specified point in time in the past without taking any part of the database offline. In many cases, Flashback Table eliminates the need to perform more complicated point-in-time recovery operations. Flashback Table restores tables while automatically maintaining associated attributes such as current indexes, triggers and constraints, and not requiring you to find and restore application-specific properties.
	"Rewinding a Table with Flashback Table" explains how to use this feature.
- Flashback Drop
	You can reverse the effects of a `DROP` `TABLE` statement.
	"Rewinding a DROP TABLE Operation with Flashback Drop" explains how to use this feature.

Note:

Because the logical flashback features have uses not specific to backup and recovery, some documentation for them is located elsewhere in the documentation set.

All logical flashback features except Flashback Drop rely on undo data. Used primarily for providing read consistency for SQL queries and rolling back transactions, undo records contain the information required to reconstruct data as it existed at a past time and examine the record of changes since that past time.

Flashback Drop relies on a mechanism called the [recycle bin](glossary.md), which the database uses to manage dropped database objects until the space they occupied is needed for new data. There is no fixed amount of space allocated to the recycle bin, and no guarantee about how long dropped objects remain in the recycle bin. Depending on system activity, a dropped object may remain in the recycle bin for seconds or for months.

See Also:

- [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/logical.htm#CNCPT305) and [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/undo.htm#ADMIN013) for more information about undo data and automatic undo management
- [Oracle Database Advanced Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/adfns_flashback.htm#ADFNS1008) to learn how to use the logical flashback features
- ["Understanding Flashback Database, Restore Points and Guaranteed Restore Points"](flashdb.md) for more information on setting up your database to use Flashback Database, and on the related restore points feature

## Rewinding a Table with Flashback Table

Flashback Table uses information in the undo tablespace rather than restored backups to retrieve the table. When a Flashback Table operation occurs, new rows are deleted and old rows are reinserted. The rest of your database remains available while the flashback of the table is being performed.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/undo.htm#ADMIN013) for more information on Automatic Undo Management

### Prerequisites of Flashback Table

To use the Flashback Table feature on one or more tables, use the `FLASHBACK` `TABLE` SQL statement with a target time or SCN.

You must have the following privileges to use the Flashback Table feature:

- You must have been granted the `FLASHBACK ANY TABLE` system privilege or you must have the `FLASHBACK` object privilege on the table.
- You must have `SELECT`, `INSERT`, `DELETE`, and `ALTER` privileges on the table.
- To flash back a table to a restore point, you must have the `SELECT ANY DICTIONARY` or `FLASHBACK ANY TABLE` system privilege or the `SELECT_CATALOG_ROLE` role.

For an object to be eligible to be flashed back, the following prerequisites must be met:

- The object must not be included the following categories: tables that are part of a cluster, materialized views, Advanced Queuing (AQ) tables, static data dictionary tables, system tables, remote tables, object tables, nested tables, or individual table partitions or subpartitions.
- The structure of the table must not have been changed between the current time and the target flash back time.
	The following DDL operations change the structure of a table: upgrading, moving, or truncating a table; adding a constraint to a table, adding a table to a cluster; modifying or dropping a column; adding, dropping, merging, splitting, coalescing, or truncating a partition or subpartition (except adding a range partition).
- Row movement must be enabled on the table, which indicates that rowids will change after the flashback occurs.
	This restriction exists because if rowids before the flashback were stored by the application, then there is no guarantee that the rowids correspond to the same rows after the flashback. If your application depends on rowids, then you cannot use Flashback Table.
- The undo data in the [undo tablespace](glossary.md) must extend far enough back in time to satisfy the flashback target time or SCN.
	The point to which you can perform Flashback Table is determined by the [undo retention period](glossary.md), which is the minimal time for which undo data is kept before being recycled, and tablespace characteristics. The undo data contains information about data blocks before they were changed. The flashback operation uses undo to re-create the original data.
	To ensure that the undo information is retained for Flashback Table operations, Oracle suggests setting the `UNDO_RETENTION` parameter to 86400 seconds (24 hours) or greater for the undo tablespace.

Note:

`FLASHBACK` `TABLE` `...` `TO` `BEFORE` `DROP` is a use of the Flashback Drop feature, not Flashback Table, and therefore is not subject to these prerequisites. See "Rewinding a DROP TABLE Operation with Flashback Drop" for more information.

### Performing a Flashback Table Operation

In this scenario, assume that you want to perform a flashback of the `hr.temp_employees` table after a user made some incorrect updates.

The perform a flashback of `temp_employees`:

1. Connect SQL\*Plus to the target database and identify the current SCN.
	You cannot roll back a `FLASHBACK TABLE` statement, but you can issue another `FLASHBACK TABLE` statement and specify a time just before the current time. Therefore, it is advisable to record the current SCN. You can obtain it by querying `V$DATABASE` as follows:
	```
	SELECT CURRENT_SCN
	FROM   V$DATABASE;
	```
2. Identify the time, SCN, or restore point to which you want to return the table.
	If you have created restore points, then you can list available restore points by executing the following query:
	```
	SELECT NAME, SCN, TIME 
	FROM   V$RESTORE_POINT;
	```
3. Ensure that enough undo data exists to rewind the table to the specified target.
	If the `UNDO_RETENTION` intialization parameter is set, and the undo retention guarantee is on, then you can use the following query to determine how long undo data is being retained:
	```
	SELECT NAME, VALUE/60 MINUTES_RETAINED
	FROM   V$PARAMETER
	WHERE  NAME = 'undo_retention';
	```
4. Ensure that row movement is enabled for all objects that you are rewinding with Flashback Table.
	You can enable row movement for a table with the following SQL statement, where table is the name of the table that you are rewinding:
	```
	ALTER TABLE table ENABLE ROW MOVEMENT;
	```
5. Determine whether the table that you intend to flash back has dependencies on other tables. If dependencies exist, then decide whether to flash back these tables as well.
	You can issue the following SQL query to determine the dependencies, where schema\_name is the schema for the table to be flashed back and table\_name is the name of the table:
	```
	SELECT other.owner, other.table_name
	FROM   sys.all_constraints this, sys.all_constraints other
	WHERE  this.owner = schema_name
	AND    this.table_name = table_name
	AND    this.r_owner = other.owner
	AND    this.r_constraint_name = other.constraint_name
	AND    this.constraint_type='R';
	```
6. Execute a `FLASHBACK TABLE` statement for the objects that you want to flash back.
	The following SQL statement returns the `hr.temp_employees` table to the restore point named `temp_employees_update`:
	```
	FLASHBACK TABLE hr.temp_employees
	  TO RESTORE POINT temp_employees_update;
	```
	The following SQL statement rewinds the `hr.temp_employees` table to its state when the database was at the time specified by the SCN:
	```
	FLASHBACK TABLE hr.temp_employees
	  TO SCN 123456;
	```
	As shown in the following example, you can also specify the target point in time with `TO_TIMESTAMP`:
	```
	FLASHBACK TABLE hr.temp_employees
	  TO TIMESTAMP TO_TIMESTAMP('2007-10-17 09:30:00', 'YYYY-MM-DD HH:MI:SS');
	```
	Note:
	The mapping of timestamps to SCNs is not always exact. When using timestamps with the `FLASHBACK` `TABLE` statement, the time to which the table is flashed back can vary by up to approximately three seconds of the time specified for `TO_TIMESTAMP`. If an exact point in time is required, then use an SCN rather than a time.
7. Optionally, query the table to check the data.

#### Keeping Triggers Enabled During Flashback Table

By default, the database disables triggers on the affected table before performing a `FLASHBACK TABLE` operation. After the operation, the database returns the triggers to the state they were in before the operation (enabled or disabled). To keep triggers enabled during the flashback of the table, add an `ENABLE TRIGGERS` clause to the `FLASHBACK TABLE` statement in Step [^1].

For example, assume that at 17:00 an HR administrator discovers that an employee is missing from the `hr.temp_employees` table. This employee was included in the table at 14:00, the last time the report was run. Therefore, someone accidentally deleted the record for this employee between 14:00 and 17:00. She uses Flashback Table to return the table to its state at 14:00, respecting any triggers set on the `hr.temp_employees` table, by using the SQL statement in the following example:

```
FLASHBACK TABLE temp_employees
  TO TIMESTAMP TO_TIMESTAMP('2005-03-03 14:00:00' , 'YYYY-MM-DD HH:MI:SS') 
  ENABLE TRIGGERS;
```

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/tables.htm#ADMIN01512) to learn how to recover tables with the Flashback Table feature
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_9012.htm#SQLRF01802) for a simple Flashback Table scenario

## Rewinding a DROP TABLE Operation with Flashback Drop

This section explains how to retrieve objects from the recycle bin with the `FLASHBACK TABLE ... TO BEFORE DROP` statement.

### About Flashback Drop

Flashback Drop reverses the effects of a `DROP TABLE` operation. Flashback Drop is faster than other recovery mechanisms that can be used in this situation, such as point-in-time recovery, and does not lead to downtime or loss of recent transactions.

When you drop a table, the database does not immediately remove the space associated with the table. Instead, the table is renamed and, along with any associated objects, placed in the recycle bin. System-generated recycle bin object names are unique. You can query objects in the recycle bin, just as you can query other objects.

A flashback operation retrieves the table from the recycle bin. When retrieving dropped tables, you can specify either the original user-specified name of the table or the system-generated name.

When you drop a table, the table and all of its dependent objects go into the recycle bin together. Likewise, when you perform Flashback Drop, the objects are generally all retrieved together. When you restore a table from the recycle bin, dependent objects such as indexes do not get their original names back; they retain their system-generated recycle bin names. Oracle Database retrieves all indexes defined on the table except for bitmap join indexes, and all triggers and constraints defined on the table except for referential integrity constraints that reference other tables.

Some dependent objects such as indexes may have been reclaimed because of space pressure. In such cases, the reclaimed dependent objects are not retrievable from the recycle bin.

### Prerequisites of Flashback Drop

The following list summarizes the user privileges required for the operations related to Flashback Drop and the recycle bin:

- `DROP`
	Any user with drop privileges over an object can drop the object, placing it in the recycle bin.
- `FLASHBACK TABLE ... TO BEFORE DROP`
	Privileges for this statement are tied to the privileges for `DROP`. That is, any user who can drop an object can perform Flashback Drop to retrieve the dropped object from the recycle bin.
- `PURGE`
	Privileges for a purge of the recycle bin are tied to the `DROP` privileges. Any user having `DROP` `TABLE` or `DROP` `ANY` `TABLE` privileges can purge the objects from the recycle bin.
- `SELECT` for objects in the Recycle Bin
	Users must have `SELECT` and `FLASHBACK` privileges over an object in the recycle bin to query the object in the recycle bin. Any users who had the `SELECT` privilege over an object before it was dropped continue to have the `SELECT` privilege over the object in the recycle bin. Users must have `FLASHBACK` privilege to query any object in the recycle bin because these are objects from a past state of the database.

Objects must meet the following prerequisites to be eligible for retrieval from the recycle bin:

- The recycle bin is only available for non-system, locally managed tablespaces. If a table is in a non-system, locally managed tablespace, but one or more of its dependent segments (objects) is in a dictionary-managed tablespace, then these objects are protected by the recycle bin.
- Tables that have Fine-Grained Auditing (FGA) and Virtual Private Database (VPD) policies defined over them are not protected by the recycle bin.
- Partitioned index-organized tables are not protected by the recycle bin.
- The table must not have been purged, either by a user or by Oracle Database because of a space reclamation operation.

### Performing a Flashback Drop Operation

Use the `FLASHBACK` `TABLE` `...` `TO` `BEFORE` `DROP` statement to recover objects from the recycle bin. You can specify either the name of the table in the recycle bin or the original table name.

This section assumes a scenario in which you drop the wrong table. Many times you have been asked to drop tables in the test databases, but in this case you accidentally connect to the production database instead and drop `hr.employee_demo`. You decide to use `FLASHBACK TABLE` to retrieve the dropped object.

To retrieve a dropped table:

1. Connect SQL\*Plus to the target database and obtain the name of the dropped table in the recycle bin.
	You can use the SQL\*Plus command `SHOW RECYCLEBIN` as follows:
	```
	SHOW RECYCLEBIN;
	ORIGINAL NAME    RECYCLEBIN NAME                   TYPE         DROP TIME
	---------------- --------------------------------- ------------ -------------
	EMPLOYEE_DEMO    BIN$gk3lsj/3akk5hg3j2lkl5j3d==$0  TABLE    2005-04-11:17:08:54
	```
	The `ORIGINAL NAME` column shows the original name of the object, while the `RECYCLEBIN NAME` column shows the name of the object as it exists in the bin.
	Alternatively, you can query `USER_RECYCLEBIN` or `DBA_RECYCLEBIN` to obtain the table name. The following example queries the views to determine the original names of dropped objects:
	```
	SELECT object_name AS recycle_name, original_name, type 
	FROM   recyclebin;
	RECYCLE_NAME                      ORIGINAL_NAME          TYPE
	--------------------------------  ---------------------  ----------
	BIN$gk3lsj/3akk5hg3j2lkl5j3d==$0  EMPLOYEE_DEMO          TABLE
	BIN$JKS983293M1dsab4gsz/I249==$0  I_EMP_DEMO             INDEX
	```
	If you plan to manually restore original names for dependent objects, then ensure that you make note of each dependent object's system-generated recycle bin name before you restore the table.
	Note:
	Object views such as `DBA_TABLES` do not display the recycle bin objects.
2. Optionally, query the table in the recycle bin.
	You must use the recycle bin name of the object in your query rather than the object's original name. The following example queries the table with the recycle bin name of `BIN$KSD8DB9L345KLA==$0`:
	```
	SELECT * 
	FROM   "BIN$gk3lsj/3akk5hg3j2lkl5j3d==$0";
	```
	Quotes are required because of the special characters in the recycle bin name.
	Note:
	If you have the necessary privileges, then you can also use Flashback Query on tables in the recycle bin, but only by using the recycle bin name rather than the original table name. You cannot use DML or DDL statements on objects in the recycle bin.
3. Retrieve the dropped table.
	Use the `FLASHBACK TABLE ... TO BEFORE DROP` statement. The following example restores the `BIN$gk3lsj/3akk5hg3j2lkl5j3d==$0` table, changes its name back to `hr.employee_demo`, and purges its entry from the recycle bin:
	```
	FLASHBACK TABLE "BIN$gk3lsj/3akk5hg3j2lkl5j3d==$0" TO BEFORE DROP;
	```
	The table name is enclosed in quotes because of the possibility of special characters appearing in the recycle bin object names.
	Alternatively, you can use the original name of the table:
	```
	FLASHBACK TABLE HR.EMPLOYEE_DEMO TO BEFORE DROP;
	```
	You can also assign a new name to the restored table by specifying the `RENAME TO` clause. For example:
	```
	FLASHBACK TABLE "BIN$KSD8DB9L345KLA==$0" TO BEFORE DROP 
	  RENAME TO hr.emp_demo;
	```
4. Optionally, verify that all dependent objects retained their system-generated recycle bin names.
	The following query determines the names of the indexes of the retrieved `hr.employee_demo` table:
	```
	SELECT INDEX_NAME 
	FROM   USER_INDEXES 
	WHERE  TABLE_NAME = 'EMPLOYEE_DEMO';
	INDEX_NAME
	------------------------------
	BIN$JKS983293M1dsab4gsz/I249==$0
	```
5. Optionally, rename the retrieved indexes to their original names.
	The following statement renames the index to its original name of `i_emp_demo`:
	```
	ALTER INDEX "BIN$JKS983293M1dsab4gsz/I249==$0" RENAME TO I_EMP_DEMO;
	```
6. If the retrieved table had referential constraints before it was placed in the recycle bin, then re-create them.
	This step must be performed manually because the recycle bin does not preserve referential constraints on a table.

#### Retrieving Objects When Multiple Objects Share the Same Original Name

You can create, and then drop, several objects with the same original name. All the dropped objects are stored in the recycle bin. For example, consider the SQL statements in the following example.

Example 18-1 Dropping Multiple Objects with the Same Name

```
CREATE TABLE temp_employees ( ...columns ); # temp_employees version 1
DROP TABLE temp_employees;

CREATE TABLE temp_employees ( ...columns ); # temp_employees version 2
DROP TABLE temp_employees;

CREATE TABLE temp_employees ( ...columns ); # temp_employees version 3
DROP TABLE temp_employees;
```

In Example 18-1, each table `temp_employees` is assigned a unique name in the recycle bin when it is dropped. You can use a `FLASHBACK TABLE ... TO BEFORE DROP` statement with the original name of the table, as shown in this example:

```
FLASHBACK TABLE temp_employees TO BEFORE DROP;
```

The most recently dropped table with this original name is retrieved from the recycle bin, with its original name. Example 18-2 shows the retrieval from the recycle bin of all three dropped `temp_employees` tables from the previous example, with each assigned a new name.

Example 18-2 Renaming Dropped Tables

```
FLASHBACK TABLE temp_employees TO BEFORE DROP 
  RENAME TO temp_employees_VERSION_3;
FLASHBACK TABLE temp_employees TO BEFORE DROP 
  RENAME TO temp_employees_VERSION_2;
FLASHBACK TABLE temp_employees TO BEFORE DROP 
  RENAME TO temp_employees_VERSION_1;
```

Because the original name in `FLASHBACK` `TABLE` refers to the most recently dropped table with this name, the last table dropped is the first retrieved.

You can also retrieve any table from the recycle bin, regardless of any collisions among original names, by using the unique recycle bin name of the table. For example, assume that you query the recycle bin as follows (sample output included):

```
SELECT object_name, original_name, createtime 
FROM   recyclebin;    

OBJECT_NAME                    ORIGINAL_NAME   CREATETIME
------------------------------ --------------- -------------------
BIN$yrMKlZaLMhfgNAgAIMenRA==$0 TEMP_EMPLOYEES  2007-02-05:21:05:52
BIN$yrMKlZaVMhfgNAgAIMenRA==$0 TEMP_EMPLOYEES  2007-02-05:21:25:13
BIN$yrMKlZaQMhfgNAgAIMenRA==$0 TEMP_EMPLOYEES  2007-02-05:22:05:53
```

You can use the following command to retrieve the middle table:

```
FLASHBACK TABLE BIN$yrMKlZaVMhfgNAgAIMenRA==$0 TO BEFORE DROP;
```

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/tables.htm#ADMIN01511) to learn how to use Flashback Drop and manage the recycle bin
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_9012.htm#SQLRF01802) for information about the `FLASHBACK TABLE` statement

## Rewinding a Database with Flashback Database

This section explains the most common scenario for using Flashback Database to reverse unwanted changes to your database.

### Prerequisites of Flashback Database

To use the `FLASHBACK` `DATABASE` command to return your database contents to points in time within the flashback window, your database must be configured for flashback logging as described in ["Understanding Flashback Database, Restore Points and Guaranteed Restore Points"](flashdb.md). To return the database to a guaranteed restore point, you must have defined a guaranteed restore point as described in ["Using Normal and Guaranteed Restore Points"](flashdb.md).

Flashback Database works by undoing changes to the data files that exist at the moment that you run the command. Note the following important prerequisites:

- No current data files are lost or damaged. You can only use `FLASHBACK DATABASE` to rewind changes to a data file made by an Oracle database, not to repair media failures.
- You are not trying to recover from accidental deletion of data files, undo a shrink data file operation, or undo a change to the database name.
- You are not trying to use `FLASHBACK` `DATABASE` to return to a point in time before the restore or re-creation of a control file. If the database control file is restored from backup or re-created, then all accumulated flashback log information is discarded.
- You are not trying to use `FLASHBACK` `DATABASE` to undo a compatibility change.

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta023.htm#RCMRF194) for a complete list of command prerequisites and usage notes for `FLASHBACK DATABASE`

### Performing a Flashback Database Operation

This section presents a basic technique for performing a flashback of the database, specifying the desired target point in time with a time expression, the name of a normal or guaranteed restore point, or an SCN.

This scenario assumes that you are rewinding the database to a point in time within the current database [incarnation](glossary.md). To return the database to the point in time immediately before the most recent `OPEN` `RESETLOGS`, see "Rewinding an OPEN RESETLOGS Operation with Flashback Database".

By default, an SCN used in a `FLASHBACK DATABASE` command refers to an SCN in the [direct ancestral path](glossary.md) of the database incarnations. As explained in ["Database Incarnations"](rcmrvcon.md), an incarnation is in this path if it was not abandoned after the database was previously opened with the `RESETLOGS` option. To retrieve changes in abandoned incarnations, see "Rewinding the Database to an SCN in an Abandoned Incarnation Branch".

To perform a Flashback Database operation:

1. Connect SQL\*Plus to the target database and determine the desired SCN, restore point, or point in time for the `FLASHBACK` `DATABASE` command.
	Obtain the earliest SCN in the flashback database window as follows:
	```
	SELECT OLDEST_FLASHBACK_SCN, OLDEST_FLASHBACK_TIME
	FROM   V$FLASHBACK_DATABASE_LOG;
	```
	The most recent SCN that can be reached with Flashback Database is the current SCN of the database. The following query returns the current SCN:
	```
	SELECT CURRENT_SCN
	FROM   V$DATABASE;
	```
	You can query available guaranteed restore points as follows (sample output included):
	```
	SELECT NAME, SCN, TIME, DATABASE_INCARNATION#,
	       GUARANTEE_FLASHBACK_DATABASE
	FROM   V$RESTORE_POINT
	WHERE  GUARANTEE_FLASHBACK_DATABASE='YES';
	 
	NAME                   SCN TIME                  DATABASE_INCARNATION# GUA
	--------------- ---------- --------------------- --------------------- ---
	BEFORE_CHANGES     5753126 04-MAR-05 12.39.45 AM                     2 YES
	```
	Note:
	If the flashback window does not extend far enough back into the past to reach the desired target time, and if you do not have a guaranteed restore point at the desired time, then you can achieve similar results by using database point-in-time recovery, as described in "Performing Database Point-in-Time Recovery".
2. Shut down the database consistently, ensure that it is not opened by any instance, and then mount it:
	```
	SHUTDOWN IMMEDIATE;
	STARTUP MOUNT;
	```
3. Repeat the query in Step 1 of this procedure.
	Some flashback logging data is generated when the database is shut down. If flashback logs were deleted due to space pressure in the fast recovery area, then your target SCN may not be reachable.
	Note:
	If you run `FLASHBACK` `DATABASE` when your target SCN is outside the flashback window, then `FLASHBACK` `DATABASE` fails with an `ORA-38729` error. In this case your database does not change.
4. Start RMAN and connect to the target database.
5. Run the `SHOW` command to see which channels are preconfigured.
	During the flashback operation, RMAN may need to restore archived redo logs from backup. Enter the following command to see whether channels are configured (sample output is included):
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
	If the necessary devices and channels are already configured, then no action is necessary. Otherwise, use the `CONFIGURE` command to configure automatic channels, or include `ALLOCATE CHANNEL` commands within a `RUN` block.
6. Run the RMAN `FLASHBACK DATABASE` command.
	You can specify the target time by using one of the forms of the command shown in the following examples:
	```
	FLASHBACK DATABASE TO SCN 46963;
	FLASHBACK DATABASE 
	  TO RESTORE POINT BEFORE_CHANGES;
	FLASHBACK DATABASE TO TIME   
	  "TO_DATE('09/20/05','MM/DD/YY')";
	```
	When the `FLASHBACK` `DATABASE` command completes, the database is left mounted and recovered to the specified target time.
7. Open the database read-only in SQL\*Plus and run some queries to verify the database contents.
	Open the database read-only as follows:
	```
	ALTER DATABASE OPEN READ ONLY;
	```
	If you are satisfied with the state of the database, then end the procedure with Step [^2]. If you are not satisfied with the state of the database, skip to Step [^3].
8. If satisfied with the results, then perform either of the following mutually exclusive actions:
	- Make the database available for updates by opening the database with the `RESETLOGS` option. If the database is currently open read-only, then execute the following commands in SQL\*Plus:
		```
		SHUTDOWN IMMEDIATE
		STARTUP MOUNT
		ALTER DATABASE OPEN RESETLOGS;
		```
		Note:
		After you perform this `OPEN` `RESETLOGS` operation, all changes to the database after the target SCN for `FLASHBACK` `DATABASE` are abandoned. Nevertheless, you can use the technique in "Rewinding the Database to an SCN in an Abandoned Incarnation Branch" to return the database to that range of SCNs while they remain in the flashback window.
		- Use Oracle Data Pump Export to make a logical backup of the objects whose state was corrupted. Afterward, use RMAN to recover the database to the present time:
		```
		RECOVER DATABASE;
		```
		This step undoes the effect of the Flashback Database by re-applying all changes in the redo logs to the database, returning it to the most recent SCN.
		After re-opening the database read/write, you can import the exported objects with the Data Pump Import utility. See [Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/dp_overview.htm#SUTIL100) to learn how to use Data Pump.
9. If you find that you used the wrong restore point, time, or SCN for the flashback, then mount the database and perform one of the following mutually exclusive options:
	- If your chosen target time was not far enough in the past, then use another `FLASHBACK` `DATABASE` command to rewind the database further back in time:
		```
		FLASHBACK DATABASE TO SCN 42963;  #earlier than current SCN
		```
	- If you chose a target SCN that is too far in the past, then use `RECOVER` `DATABASE` `UNTIL` to wind the database forward in time to the desired SCN:
		```
		RECOVER DATABASE UNTIL SCN 56963; #later than current SCN
		```
	- If you want to completely undo the effect of the `FLASHBACK` `DATABASE` command, then you can perform complete recovery of the database by using the `RECOVER` `DATABASE` command without an `UNTIL` clause or `SET UNTIL` command:
		```
		RECOVER DATABASE;
		```
		The `RECOVER DATABASE` command reapplies all changes to the database, returning it to the most recent SCN.

### Monitoring Flashback Database

When you use Flashback Database to rewind a database to a past target time, Flashback Database determines which blocks changed after the target time and restores them from the flashback logs. This is called the restore phase. After this phase completes, Flashback Database then uses redo logs to reapply changes that were made after these blocks were written to the flashback logs. This is called the recovery phase.

The progress of Flashback Database during the restore phase can be monitored by querying the `V$SESSION_LONGOPS` view. The `opname` is `Flashback Database`. Under the column `TOTALWORK` is the number of megabytes of flashback logs that must be read. The column `SOFAR` in Example 18-3 lists the number of megabytes that have been currently read.

Example 18-3 Tracking Flashback Database Progress - Restore Phase

```
SQL> select sofar, totalwork, units from v$session_longops where opname = 'Flashback Database';
 
SOFAR  TOTALWORK  UNITS
-----  ---------- --------------------------------
   17          60 Megabytes
```

The progress of Flashback Database during the recovery phase can be monitored by querying the view `V$RECOVERY_PROGRESS`.

See Also:

The [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2128.htm#REFRN30199) for information on the view `V$RECOVERY_PROGRESS`.

## Performing Database Point-in-Time Recovery

RMAN DBPITR restores the database from backups before the target time for recovery, then uses incremental backups and redo to roll the database forward to the target time. You can recover to an SCN, time, log sequence number, or restore point. Oracle recommends that you create restore points at important times to make point-in-time recovery more manageable if it ever becomes necessary.

Oracle recommends that you perform Flashback Database rather than database point-in-time recovery if possible. Media recovery with backups should be the last option when flashback technologies cannot be used to undo the most recent changes.

### Prerequisites of Database Point-in-Time Recovery

The prerequisites for database point-in-time recovery are as follows:

- Your database must be running in `ARCHIVELOG` mode.
- You must have backups of all data files from before the target SCN for DBPITR and archived logs for the period between the SCN of the backups and the target SCN.

For a complete account of command prerequisites and usage notes, refer to the `RECOVER` entry in [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2001.htm#RCMRF140).

### Performing Database Point-in-Time Recovery

This section explains the basic steps of DBPITR. The procedure makes the following assumptions:

- You are performing DBPITR within the current database [incarnation](glossary.md). If your target time is not in the current incarnation, then see "Recovering the Database to an Ancestor Incarnation" for more information on DBPITR to ancestor incarnations.
- The control file is current. If you need to restore a backup control file, then see ["Performing Recovery with a Backup Control File"](rcmadvre.md).
- Your database is using the current server parameter file. If you must restore a backup server parameter file, then see ["Restoring the Server Parameter File"](rcmadvre.md).

When performing DBPITR, you can avoid errors by using the `SET` `UNTIL` command to set the target time at the beginning of the procedure, rather than specifying the `UNTIL` clause on the `RESTORE` and `RECOVER` commands individually. This ensures that the data files restored from backup have timestamps early enough to be used in the subsequent `RECOVER` operation.

To perform DBPITR:

1. Determine the time, SCN, restore point, or log sequence that should end recovery.
	You can use the Flashback Query features to help you identify when the logical corruption occurred. If you have a [flashback data archive](glossary.md) enabled for a table, then you can query data that existed far in the past.
	You can also use the alert log to try to determine the time of the event from which you must recover.
	Alternatively, you can use a SQL query to determine the log sequence number that contains the target SCN and then recover through this log. For example, run the following query to list the logs in the current database incarnation (sample output included):
	```
	SELECT RECID, STAMP, THREAD#, SEQUENCE#, FIRST_CHANGE#
	       FIRST_TIME, NEXT_CHANGE#
	FROM   V$ARCHIVED_LOG
	WHERE  RESETLOGS_CHANGE# =
	       ( SELECT RESETLOGS_CHANGE#
	         FROM   V$DATABASE_INCARNATION
	         WHERE  STATUS = 'CURRENT');
	RECID      STAMP      THREAD#    SEQUENCE#  FIRST_CHAN FIRST_TIM NEXT_CHANG
	---------- ---------- ---------- ---------- ---------- --------- ----------
	         1  344890611          1          1      20037 24-SEP-05      20043
	         2  344890615          1          2      20043 24-SEP-05      20045
	         3  344890618          1          3      20045 24-SEP-05      20046
	```
	For example, if you discover that a user accidentally dropped a tablespace at 9:02 a.m., then you can recover to 9 a.m., just before the drop occurred. You lose all changes to the database made after this time.
2. If you are using a target time expression instead of a target SCN, then make sure the time format environment variables are appropriate before invoking RMAN.
	The following are sample Globalization Support settings:
	```
	NLS_LANG = american_america.us7ascii
	NLS_DATE_FORMAT="Mon DD YYYY HH24:MI:SS"
	```
3. Connect RMAN to the target database and, if applicable, the recovery catalog database. Bring the database to a mounted state:
	```
	SHUTDOWN IMMEDIATE;
	STARTUP MOUNT;
	```
4. Perform the following operations within a `RUN` block:
	1. Use `SET` `UNTIL` to specify the target time, restore point, SCN, or log sequence number for DBPITR. If specifying a time, then use the date format specified in the `NLS_LANG` and `NLS_DATE_FORMAT` environment variables.
		2. If automatic channels are not configured, then manually allocate disk and tape channels as needed.
		3. Restore and recover the database.
	The following example performs DBPITR on the target database until SCN 1000:
	```
	RUN
	{ 
	  SET UNTIL SCN 1000;    
	  RESTORE DATABASE;
	  RECOVER DATABASE;
	}
	```
	As shown in the following examples, you can also use time expressions, restore points, or log sequence numbers to specify the `SET` `UNTIL` time:
	```
	SET UNTIL TIME 'Nov 15 2004 09:00:00';
	SET UNTIL SEQUENCE 9923;  
	SET UNTIL RESTORE POINT before_update;
	```
	If the operation completes without errors, then DBPITR has succeeded.
5. Perform either of the following mutually exclusive actions:
	- Open your database for read/write, abandoning all changes after the target SCN. In this case, you must shut down the database, mount it, and then execute the following command:
		```
		ALTER DATABASE OPEN RESETLOGS;
		```
		The `OPEN RESETLOGS` operation fails if a data file is offline unless the data file went offline normally or is read-only. You can bring files in read-only or offline normal tablespaces online after the `RESETLOGS` because they do not need any redo.
		- Export one or more objects from your database with Data Pump Export. You can then recover the database to the current point in time and re-import the exported objects, thus returning these objects to their state before the unwanted change without abandoning all other changes.

## Flashback and Database Point-in-Time Recovery Scenarios

This section describes variations on the basic scenarios described in "Rewinding a Database with Flashback Database" and "Performing Database Point-in-Time Recovery".

### Rewinding an OPEN RESETLOGS Operation with Flashback Database

The procedure for using Flashback Database to reverse an unwanted `ALTER DATABASE OPEN RESETLOGS` statement is similar to the general case described in "Performing a Flashback Database Operation". Rather than specifying a particular SCN or point in time for the `FLASHBACK` `DATABASE` command, however, you use `FLASHBACK` `DATABASE` `TO` `BEFORE` `RESETLOGS`.

To undo an `OPEN` `RESETLOGS` operation:

1. Connect SQL\*Plus to the target database and verify that the beginning of the flashback window is earlier than the time of the most recent `OPEN` `RESETLOGS`.
	Run the following queries:
	```
	SELECT RESETLOGS_CHANGE# 
	FROM   V$DATABASE;
	SELECT OLDEST_FLASHBACK_SCN 
	FROM   V$FLASHBACK_DATABASE_LOG;
	```
	If `V$DATABASE.RESETLOGS_CHANGE#` is greater than `V$FLASHBACK_DATABASE_LOG.OLDEST_FLASHBACK_SCN`, then you can use Flashback Database to reverse the `OPEN` `RESETLOGS`.
2. Shut down the database, mount it, and recheck the flashback window. If the resetlogs SCN is still within the flashback window, then proceed to the next step.
3. Connect RMAN to the target database and perform a flashback to the SCN immediately before the `RESETLOGS`.
	Use the following form of the `FLASHBACK` `DATABASE` command:
	```
	FLASHBACK DATABASE TO BEFORE RESETLOGS;
	```
	As with other uses of `FLASHBACK` `DATABASE`, if the target SCN is before the beginning of the flashback database window, an error is returned and the database is not modified. If the command completes successfully, then the database is left mounted and recovered to the most recent SCN before the `OPEN RESETLOGS` in the previous incarnation.
4. Open the database read-only in SQL\*Plus and perform queries as needed to ensure that the effects of the logical corruption have been reversed.
	Open the database read-only as follows:
	```
	ALTER DATABASE OPEN READ ONLY;
	```
5. To make the database available for updates again, shut down the database, mount it, and then execute the following command:
	```
	ALTER DATABASE OPEN RESETLOGS;
	```

#### Undoing an OPEN RESETLOGS on Standby Databases with Flashback Database

Flashback Database across `OPEN RESETLOGS` may be used to perform the following functions in a Data Guard environment:

- Flashback to undo logical standby switchovers
	In this case, the database reverts to its role (primary or standby) at the target time for the Flashback Database operation.
- Undo of a physical standby activation
	You can temporarily activate a physical standby database, use it for testing or reporting purposes, and then use Flashback Database to return it to its role as a physical standby.
- Ongoing use of a standby database for testing
	The use of Flashback Database means that you do are not require the use of storage snapshots.

See Also:

[Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/role_management.htm#SBYDB00717) for details on these advanced applications of Flashback Database with Data Guard

### Rewinding the Database to an SCN in an Abandoned Incarnation Branch

The effect of Flashback Database or DBPITR followed by an `OPEN` `RESETLOGS` is to return the database to a previous SCN, and to abandon changes after this point. Therefore, some SCNs after that point can refer either to changes that were abandoned or changes in the current history of the database. In this way, a target SCN specified in `FLASHBACK DATABASE` can be ambiguous.

Unlike SCNs, time expressions and restore points are not ambiguous. A time expression is always associated with the incarnation that was current at that time. A restore point is always associated with the current incarnation when it was created. This is true even for times and restore points that correspond to abandoned database incarnations. The database incarnation is automatically reset to the incarnation that was current at the specified time or when the restore point was created.

You may want to use Flashback Database to rewind the database to an SCN in the parent incarnation that is later than the SCN of the `OPEN RESETLOGS` at which the current incarnation path branched from the old incarnation. [Figure 14-1, "Database Incarnation History"](rcmrvcon.md) shows how SCNs can be generated in an incarnation branch even after an `OPEN RESETLOGS` creates a new incarnation. As shown in the diagram, the database could be at SCN 3000 in incarnation 3 when you must return to the abandoned SCN 1500 in incarnation 1.

If the SCN to which you are rewinding is in the [direct ancestral path](glossary.md), or if you are rewinding the database to a [restore point](glossary.md), then an explicit `RESET DATABASE` is not necessary for Flashback Database. However, an explicit `RESET` `DATABASE` `TO` `INCARNATION` command is required when using `FLASHBACK DATABASE` to rewind the database to an SCN in an abandoned database incarnation.

To rewind the database to an SCN in an abandoned incarnation branch:

1. Use SQL\*Plus to connect to the target database and verify that the flashback logs contain enough information to flash back to the SCN.
	For example, execute the following query:
	```
	SELECT OLDEST_FLASHBACK_SCN
	FROM   V$FLASHBACK_DATABASE_LOG;
	```
2. Determine the target incarnation number for the Flashback Database operation, that is, the incarnation key for the parent incarnation.
	For example, execute the following query:
	```
	SELECT PRIOR_INCARNATION# 
	FROM   V$DATABASE_INCARNATION 
	WHERE  STATUS = 'CURRENT';
	```
3. Start RMAN and connect to the target database.
4. Shut down the database, and then mount it as follows:
	```
	SHUTDOWN IMMEDIATE;
	STARTUP MOUNT;
	```
5. Set the database incarnation to the parent incarnation.
	For example, use the following command to return to incarnation 1:
	```
	RESET DATABASE TO INCARNATION 1;
	```
6. Run the `FLASHBACK` `DATABASE` command, specifying the target SCN.
	For example, use the following command to rewind the database to SCN 1500:
	```
	FLASHBACK DATABASE TO SCN 1500;
	```
7. Open the database read-only in SQL\*Plus and perform queries as needed to ensure that the effects of the logical corruption have been reversed.
	Open the database read-only as follows:
	```
	ALTER DATABASE OPEN READ ONLY;
	```
8. To make the database available for updates again, shut down the database, mount it, and then execute the following command:
	```
	ALTER DATABASE OPEN RESETLOGS;
	```

See Also:

- ["Database Incarnations"](rcmrvcon.md) for useful background information about database incarnations, abandoned changes, and the effects of `ALTER DATABASE OPEN` `RESETLOGS`
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2007.htm#RCMRF148) for details about the `RESET` `DATABASE` command

### Recovering the Database to an Ancestor Incarnation

The procedure for DBPITR within the current incarnation is different from DBPITR to an SCN in a noncurrent incarnation. In the latter case, you must explicitly execute the `RESET DATABASE` to reset the database to the incarnation that was current at the target SCN. Also, you must restore a control file from the database incarnation containing the target SCN.

When RMAN is connected to a recovery catalog, a `RESTORE CONTROLFILE` command only searches the current database incarnation for the closest time specified in the `UNTIL` clause. To restore a control file from a noncurrent incarnation, you must execute `LIST INCARNATION` to identify the target database incarnation and specify this incarnation in the `RESET DATABASE TO INCARNATION` command.

When RMAN is connected to a recovery catalog, you cannot execute the `RESET DATABASE TO INCARNATION` command before the database is mounted. Thus, you must execute `SET UNTIL`, restore the control file from autobackup, and then mount it.

Assume the following situation:

- RMAN is connected to a recovery catalog.
- You have a backup of target database `trgt` from October 2, 2007.
- DBPITR was performed on this database on October 10, 2007 to correct an earlier error. The `OPEN` `RESETLOGS` operation at the end of that DBPITR started a new incarnation.

On October 25, you discover that you need crucial data that was dropped from the database at 8:00 a.m. on October 8, 2007. This time is before the beginning of the current incarnation.

To perform DBPITR to a noncurrent incarnation:

1. Start RMAN and connect to a target database and recovery catalog.
2. Determine which database incarnation was current at the time of the backup.
	Use `LIST` `INCARNATION` to find the primary key of the incarnation that was current at the target time:
	```
	LIST INCARNATION OF DATABASE trgt;
	List of Database Incarnations
	DB Key  Inc Key   DB Name   DB ID       STATUS     Reset SCN    Reset Time
	------- -------   -------   ------      -------    ----------   ----------
	1       2         TRGT      1224038686  PARENT     1            02-OCT-06
	1       582       TRGT      1224038686  CURRENT    59727        10-OCT-06
	```
	Look at the `Reset SCN` and `Reset Time` columns to identify the correct incarnation, and note the incarnation key in the `Inc` `Key` column. In this example, the backup was made 2 October 2007. In this case, the incarnation key value is 2.
3. Make sure the database is started but not mounted.
	```
	STARTUP FORCE NOMOUNT
	```
4. Reset the target database to the incarnation obtained in Step 2.
	In this example, specify the incarnation current at the time of the backup of 2 October. Use the value from the `Inc Key` column to identify the incarnation.
	```
	RESET DATABASE TO INCARNATION 2;
	```
5. Restore and recover the database, performing the following actions in the `RUN` command:
	- Set the end time for recovery to the time just before the loss of the data.
		- Allocate any channels required that are not already configured.
		- Restore the control file from the October 2 backup and mount it.
		- Restore the data files and recover the database. Use the `RECOVER DATABASE` `...` `UNTIL` command to perform DBPITR, bringing the database to the target time of 7:55 a.m. on October 8, just before the data was lost.
	The following example shows all of the steps required in this case:
	```
	RUN
	{
	  SET UNTIL TIME 'Oct 8 2007 07:55:00'; 
	  RESTORE CONTROLFILE;
	  # without recovery catalog, use RESTORE CONTROLFILE FROM AUTOBACKUP
	  ALTER DATABASE MOUNT; 
	  RESTORE DATABASE;
	  RECOVER DATABASE;
	}
	ALTER DATABASE OPEN RESETLOGS;
	```
	See Also:
	[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2007.htm#RCMRF148) for details about the `RESET` `DATABASE` command

[^1]: Execute a `FLASHBACK TABLE` statement for the objects that you want to flash back.

The following SQL statement returns the `hr.temp_employees` table to the restore point named `temp_employees_update`:

```
FLASHBACK TABLE hr.temp_employees
  TO RESTORE POINT temp_employees_update;
```

The following SQL statement rewinds the `hr.temp_employees` table to its state when the database was at the time specified by the SCN:

```
FLASHBACK TABLE hr.temp_employees
  TO SCN 123456;
```

As shown in the following example, you can also specify the target point in time with `TO_TIMESTAMP`:

```
FLASHBACK TABLE hr.temp_employees
  TO TIMESTAMP TO_TIMESTAMP('2007-10-17 09:30:00', 'YYYY-MM-DD HH:MI:SS');
```

Note:

The mapping of timestamps to SCNs is not always exact. When using timestamps with the `FLASHBACK` `TABLE` statement, the time to which the table is flashed back can vary by up to approximately three seconds of the time specified for `TO_TIMESTAMP`. If an exact point in time is required, then use an SCN rather than a time.

[^undefined]: Optionally, query the table to check the data.

[^2]: If satisfied with the results, then perform either of the following mutually exclusive actions:

- Make the database available for updates by opening the database with the `RESETLOGS` option. If the database is currently open read-only, then execute the following commands in SQL\*Plus:
	```
	SHUTDOWN IMMEDIATE
	STARTUP MOUNT
	ALTER DATABASE OPEN RESETLOGS;
	```
	Note:
	After you perform this `OPEN` `RESETLOGS` operation, all changes to the database after the target SCN for `FLASHBACK` `DATABASE` are abandoned. Nevertheless, you can use the technique in "Rewinding the Database to an SCN in an Abandoned Incarnation Branch" to return the database to that range of SCNs while they remain in the flashback window.
- Use Oracle Data Pump Export to make a logical backup of the objects whose state was corrupted. Afterward, use RMAN to recover the database to the present time:
	```
	RECOVER DATABASE;
	```
	This step undoes the effect of the Flashback Database by re-applying all changes in the redo logs to the database, returning it to the most recent SCN.
	After re-opening the database read/write, you can import the exported objects with the Data Pump Import utility. See [Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/dp_overview.htm#SUTIL100) to learn how to use Data Pump.

[^3]: If you find that you used the wrong restore point, time, or SCN for the flashback, then mount the database and perform one of the following mutually exclusive options:

- If your chosen target time was not far enough in the past, then use another `FLASHBACK` `DATABASE` command to rewind the database further back in time:
	```
	FLASHBACK DATABASE TO SCN 42963;  #earlier than current SCN
	```
- If you chose a target SCN that is too far in the past, then use `RECOVER` `DATABASE` `UNTIL` to wind the database forward in time to the desired SCN:
	```
	RECOVER DATABASE UNTIL SCN 56963; #later than current SCN
	```
- If you want to completely undo the effect of the `FLASHBACK` `DATABASE` command, then you can perform complete recovery of the database by using the `RECOVER` `DATABASE` command without an `UNTIL` clause or `SET UNTIL` command:
	```
	RECOVER DATABASE;
	```
	The `RECOVER DATABASE` command reapplies all changes to the database, returning it to the most recent SCN.