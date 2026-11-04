---
title: "Backup and Recovery User's Guide"
book: "Database Backup and Recovery User's Guide"
doc_id: F31836-11
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/bradv/rman-performing-flashback-dbpitr.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-users-guide
---

RMAN enables you to investigate unwanted database changes, and select and perform an appropriate recovery strategy, based upon Oracle Flashback Technology and database backups.

### 18.1 Overview of Oracle Flashback Technology and Database Point-in-Time Recovery

This overview describes the purpose and basic concepts of Oracle Flashback Technology and database point-in-time recovery.

#### 18.1.1 Purpose of Flashback and Database Point-in-Time Recovery

Certain situations are suited for using point-in-time recovery or flashback features to return the database or database object to its state at a previous point in time.

Some typical situations include the following:

- A user error or corruption removes needed data or introduces corrupted data. For example, a user or DBA might erroneously delete or update the contents of one or more tables, drop database objects that are still needed during an update to an application, or run a large batch update that fails midway.
- A database upgrade fails or an upgrade script goes awry.
- A complete database recovery after a media failure cannot succeed because you do not have all of the needed redo logs or incremental backups.

#### 18.1.2 About Point-in-Time Recovery and Flashback Features

Database point-in-time recovery (DBPITR) and Flashback features enable you to recover your database to a prior point in time.

DBPITR is the most basic solution to unwanted database changes. It is sometimes called incomplete recovery because it does not use all of the available redo or completely recover all changes to your database. In this case, you restore a whole database backup and then apply redo logs or incremental backups to re-create all changes up to a point in time before the unwanted change.

If unwanted database changes are extensive but confined to specific tablespaces, then you can use tablespace point-in-time recovery (TSPITR) to return these tablespaces to an earlier system change number while the unaffected tablespaces remain available.

If unwanted database changes are limited to specific tables or table partitions, then you can use a previously created RMAN backup to return only these objects to a point in time before the unwanted changes occurred.

Oracle Database also provides a set of features collectively known as Flashback Technology that supports viewing past states of data, and winding and rewinding data back and forth in time, without requiring the restore of the database from backup. Depending on the changes to your database, Flashback Technology can often reverse the unwanted changes more quickly and with less impact on database availability.

See Also:

- [Performing RMAN Tablespace Point-in-Time Recovery (TSPITR)](performing-rman-tspitr.md)
- [Recovering Tables and Table Partitions](rman-recovering-tables-partitions.md)

##### 18.1.2.1 About Flashback Database and PITR for PDBs

Certain dependencies may exist between database point-in-time recovery (DBPITR) and flashback operations.

For pluggable databases (PDBs) that use local undo, DBPITR and flashback operations are independent of each other.

For PDBs that use shared undo, DBPITR and flashback operations are independent with the following caveat:

If you perform a flashback operation for a PDB or recover a PDB to a particular point in time, Oracle Database may apply undo data during the PDB `RESETLOGS` operation to back out transactions that are not committed at that point in time. If you subsequently recover the entire multitenant container database (CDB) to a point in time that is in the middle of the PDB `RESETLOGS` operation, then you will receive a warning that some PDBs may not be opened. For such PDBs, you must perform one of the following mutually exclusive actions:

- Recover the entire CDB or perform a flashback operation for the entire CDB to a different SCN
- Recover all the affected PDBs or perform a flashback database operation for all the affected PDBs to a different SCN

Starting with Oracle Database 21c, you can perform a PDB flashback or point-in-time recovery operation to an orphan PDB incarnation within the same database incarnation or an orphan PDB incarnation within an ancestor database incarnation. Within a CDB, you can simultaneously perform flashback or PITR multiple PDBs to different database and PDB incarnations with the current database ancestor incarnation. For example, consider two PDBs named `pdb1` and `pdb2` in a CDB. you can flash back `pdb1` to point on PDB incarnation (5,3) and perform PITR on `pdb2` to a point on PDB incarnation (6,9) provided both incarnation 5 and incarnation 6 are on the current database ancestor path.

Note:

You cannot perform PDB flashback or PITR operation to a PDB incarnation within an orphan database incarnation.

#### 18.1.3 Basic Concepts of Database Point-in-Time Recovery

DBPITR works at the physical level to return the data files to their state at a target time in the past.

In an RMAN DBPITR operation, you specify a target SCN, log sequence, restore point, or time. RMAN restores the database from backups created before the target time, and then applies incremental backups and logs to recreate all changes between the time of the data file backups and the end point of recovery. When the end point is specified as an SCN, the database applies the redo logs and stops after each redo thread or the specified SCN, whichever occurs first. When the end point is specified as a time, the database internally determines a suitable SCN for the specified time and then recovers to this SCN.

If your backup strategy is properly designed and your database is running in `ARCHIVELOG` mode, then DBPITR is an option in nearly all circumstances. Given a target SCN, data files are restored from backup and recovered efficiently with no intervention from the user. Nevertheless, RMAN DBPITR has the following disadvantages:

- You cannot return selected objects to their earlier state, only the entire database.
- Your entire database is unavailable during the DBPITR.
- DBPITR can be time-consuming because RMAN must restore all data files. Also, RMAN may need to restore redo logs and incremental backups to recover the data files. If backups are on tape, then this process can take even longer.

Note:

RMAN simplifies DBPITR in comparison to the user-managed DBPITR described in " [Performing Incomplete Database Recovery](user-managed-flashback-dbpitr.md) ".

##### 18.1.3.1 Basic Concepts of Point-in-Time Recovery for PDBs

You can perform point-in-time recovery (PITR) of one or more PDBs. Backups created before the PITR operation remain valid and they can be used if a media failure occurs.

During a PDB PITR operation, all the data files for the PDBs are recovered in place. If the CDB uses shared undo, the `UNDO` tablespace cannot be recovered in place because it is shared by all PDBs in the CDB. Therefore, RMAN restores the `UNDO`, `SYSTEM`, and `SYSAUX` tablespaces to an auxiliary destination and then uses the undo information to recover the PDB to the target time.

When a fast recovery area is configured, RMAN uses it as the auxiliary destination during PDB PITR. If no fast recovery area is configured, use the `AUXILIARY DESTINATION` clause to specify the location used to store auxiliary database files. If the fast recovery area does not have sufficient space to restore the root tablespaces and the undo tablespace, use the `AUXILIARY DESTINATION` clause to specify an alternate location.

In a Data Guard environment, for the standby database to follow a primary database in which a PDB was restored to a particular point in time, you may need to either flash back the entire standby database, restore the PDB, or flash back the PDB.

See Also:

Performing Database Point-in-Time Recovery

#### 18.1.4 Basic Concepts of Flashback Technology

The flashback features of the Oracle Database are more efficient than media recovery in most circumstances in which they are available. You can use them to investigate past states of the database.

##### 18.1.4.1 About Physical Flashback Features Useful in Backup and Recovery

Oracle Flashback Database is the most efficient alternative to DBPITR.

Unlike the other flashback features, it operates at a physical level and reverts the current data files to their contents at a past time. The result is like the result of a DBPITR, including the `OPEN RESETLOGS`, but Flashback Database is typically faster because it does not require you to restore data files and requires only limited application of redo compared to media recovery.

A [fast recovery area](glossary.md) is required for Flashback Database. To enable logging for Flashback Database, you must set the [`DB_FLASHBACK_RETENTION_TARGET`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=REFRN10233) initialization parameter and issue the `ALTER DATABASE FLASHBACK ON` statement.

During normal operation, the database periodically writes old images of data file blocks to the [flashback logs](glossary.md). Flashback logs are written sequentially and often in bulk. In some respects, flashback logging is like a continuous backup. The database automatically creates, deletes, and resizes flashback logs in the recovery area. Flashback logs are not archived. You need only be aware of flashback logs for monitoring performance and determining disk space allocation for the recovery area.

When you perform a Flashback Database operation, the database uses flashback logs to access past versions of data blocks and also uses some data in the archived redo logs. Consequently, you cannot enable Flashback Database after a failure is discovered and then use Flashback Database to rewind through this failure. You can use the related capability of guaranteed restore points to protect the contents of your database at a fixed point in time, such as immediately before a risky database change.

If any unrecoverable operations are encountered during the small amount of redo apply required, then logically corrupt data blocks will result. This can lead to Oracle errors when such blocks are accessed.

See Also:

- Rewinding a Database with Flashback Database
- [Configuring the Fast Recovery Area](configuring-rman-client-basic.md)
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=ADMIN-GUID-21282FF3-1E98-478E-8111-0A7CAFCFCD97)

###### 18.1.4.1.1 About Flashback Database Operations with PDBs

You can perform a Flashback Database operation for a whole multitenant container database (CDB) or for a particular pluggable database (PDB).

Note:

You cannot perform a flashback operation only on the root. You must perform a flashback operation on the whole CDB.

Flashback Database on a whole CDB enables you to rewind the entire CDB, including all its PDBs, to a previous point in time. The target time can be specified by system change number (SCN), log sequence number, restore point, or time.

Flashback Database on a PDB enables you to reverse unwanted changes caused by logical data corruption or user errors in that PDB. Other PDBs can remain open and operational while performing Flashback Database on a particular PDB.

The desired target point in time is specified by a PDB restore point, a CDB restore point, an SCN, or a time expression. A flashback operation on a PDB to a CDB restore point is equivalent to a flashback operation on the PDB to the restore point SCN on the CDB incarnation. In general, for PDBs, a flashback operation to a PDB restore point is more accurate than a flashback operation to a CDB restore point. This is because a PDB restore point represents the PDB sub-incarnation of the point in time at which it was created.

Multiple flashback operations can be performed on a single PDB. However, you can only perform a flashback operation on a PDB to one of its ancestor incarnations. A PDB must always stay in a past incarnation that is compatible with the overall database incarnation.

PDB backups remain valid even after a Flashback Database operation is performed on the PDB. In case of a media failure, you can perform recovery by using these backups. This type of PDB recovery can recover through database resetlogs and PDB resetlogs.

You can also perform a Flashback Database operation for a PDB on a physical standby database after performing the same operation on the primary database.

Note:

To perform a flashback operation for an application container, you must perform flashback operations for the application root and all the individual application PDBs that are part of the application container. Performing a flashback operation on the application root reverts only the application root to the specified point in time.

See Also:

- Rewinding a Database with Flashback Database
- [Performing Flashback Database with SQL\*Plus](user-managed-flashback-dbpitr.md)

##### 18.1.4.2 About Logical Flashback Features Useful in Backup and Recovery

Logical flashback features are used to recover tables and their contents to a past time.

The logical features are as follows:

- Flashback Table
	You can recover a table or set of tables to a specified earlier point in time without taking any part of the database offline. In many cases, Flashback Table eliminates the need to perform more complicated point-in-time recovery operations. Flashback Table restores tables while automatically maintaining associated attributes such as current indexes, triggers, and constraints, and not requiring you to find and restore application-specific properties.
- Flashback Drop
	You can reverse the effects of a `DROP TABLE` statement.

All logical flashback features except Flashback Drop rely on **undo data**. Used primarily for providing read consistency for SQL queries and rolling back transactions, undo records contain the information required to reconstruct data as it existed at a past time and examine the record of changes since that past time.

Flashback Drop relies on a mechanism called the [recycle bin](glossary.md), which the database uses to manage dropped database objects until the space they occupied is needed for new data. There is no fixed amount of space allocated to the recycle bin, and no guarantee regarding how long dropped objects remain in the recycle bin. Depending on system activity, a dropped object may remain in the recycle bin for seconds or for months.

See Also:

- Rewinding a Table with Flashback Table
- Rewinding a DROP TABLE Operation with Flashback Drop
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=ADMIN013) for more information about undo data and automatic undo management

##### 18.1.4.3 About Undo and Flashback Database Operations for PDBs

A multitenant container database (CDB) can use shared undo or local undo. The technique used by RMAN to perform flashback database operations depends on the type of undo configuration for the CDB.

When a CDB uses local undo, performing a flashback database operation on a pluggable database (PDB) is straight-forward because only data files related to that PDB need to be modified.

In a CDB that uses shared undo, one set of tablespaces is shared by all PDBs. Undo data for multiple PDBs may be mixed within the undo tablespaces and even within individual data blocks. Therefore, to perform a flashback database operation for a PDB, RMAN automatically uses an auxiliary instance to restore shared undo tablespaces and certain tablespaces in the root and then recovers data to the required point in time. This process may involve restoring backups for a relatively small amount of data. When you perform a flashback database operation on a PDB to a clean PDB restore point, no auxiliary instance or restoring of backups is required.

By default, the auxiliary instance is created in the fast recovery area. You can use the `AUXILIARY DESTINATION` clause in the `FLASHBACK DATABASE` command to specify an alternate location for the auxiliary instance.

See Also:

- About Flashback Database Operations with PDBs
- Rewinding a Database with Flashback Database

#### 18.1.5 About Managing Redo Corruption in CDBs

RMAN provides methods to manage redo corruption to data blocks in a PDB.

In very rare circumstances, the redo logs in a [multitenant container database (CDB)](glossary.md) may be corrupted. In such a scenario, if the affected data blocks reside only in one pluggable database (PDB), then you can do one of the following:

- perform a flashback operation on the PDB to a point in time before the corruption and then open the PDB with `RESETLOGS`
- perform a point-in-time recovery of the PDB to a point in time before the corruption and then open the PDB with `RESETLOGS`

After you perform one of these steps on the primary database, any standby database of this primary database can also skip the corrupted redo provided you perform the steps required to enable a standby to follow a primary after a PITR or Flashback on the PDB.

See Also:

- About Flashback Database Operations with PDBs
- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=SBYDB-GUID-8D948A24-A3B7-4E4F-917A-00B047CF3CAF) for steps to enable a standby to follow a primary

### 18.2 Rewinding a Table with Flashback Table

Flashback Table uses information in the undo tablespace rather than restored backups to retrieve the table. When a Flashback Table operation occurs, new rows are deleted and old rows are reinserted. The rest of your database remains available while the flashback of the table is being performed.

To rewind a table to a previous point in time:

1. Ensure that the prerequisites described in " Prerequisites for Flashback Table " are met.
2. Perform a Flashback Table operation on the table, as described in " Performing a Flashback Table Operation ".

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=ADMIN013) for more information about automatic undo management

#### 18.2.1 Prerequisites for Flashback Table

To perform a Flashback Table operation, the table must be eligible to be flashed back and the user performing the operation must have the required privileges.

You must have the following privileges to use the Flashback Table feature:

- You must have been granted the `FLASHBACK ANY TABLE` system privilege or you must have the `FLASHBACK` object privilege on the table.
- You must have `READ` or `SELECT`, `INSERT`, `DELETE`, and `ALTER` privileges on the table.
- To flash back a table to a restore point, you must have the `SELECT ANY DICTIONARY` or `FLASHBACK ANY TABLE` system privilege or the `SELECT_CATALOG_ROLE` role.

For an object to be eligible to be flashed back, the following prerequisites must be met:

- The object must not be included the following categories: tables that are part of a cluster, materialized views, Advanced Queuing (AQ) tables, static data dictionary tables, system tables, remote tables, object tables, nested tables, or individual table partitions or subpartitions.
- The structure of the table must not have been changed between the current time and the target flashback time.
	The following Data Definition Language (DDL) operations change the structure of a table: upgrading, moving, or truncating a table; adding a constraint to a table, adding a table to a cluster; modifying or dropping a column; adding, dropping, merging, splitting, coalescing, or truncating a partition or subpartition (except adding a range partition).
- Row movement must be enabled on the table, which indicates that rowids change after the flashback occurs.
	This restriction exists because if rowids before the flashback were stored by the application, then there is no guarantee that the rowids correspond to the same rows after the flashback. If your application depends on rowids, then you cannot use Flashback Table.
- The undo data in the [undo tablespace](glossary.md) must extend far enough back in time to satisfy the flashback target time or SCN.
	The point to which you can perform Flashback Table is determined by the [undo retention period](glossary.md), which is the minimal time for which undo data is kept before being recycled, and tablespace characteristics. The undo data contains information about data blocks before they were changed. The flashback operation uses undo to re-create the original data.
	To ensure that the undo information is retained for Flashback Table operations, Oracle suggests setting the `UNDO_RETENTION` parameter to 86400 seconds (24 hours) or greater for the undo tablespace.

Note:

`FLASHBACK` `TABLE ``...` `TO` `BEFORE` `DROP` is a use of the Flashback Drop feature, not Flashback Table, and therefore is not subject to these prerequisites. See " Rewinding a DROP TABLE Operation with Flashback Drop " for more information.

#### 18.2.2 Performing a Flashback Table Operation

To use the Flashback Table feature on one or more tables, use the `FLASHBACK TABLE` SQL statement with a target time or SCN.

Assume that you want to perform a flashback of the `hr.temp_employees` table after a user made some incorrect updates. Use the following steps:

1. Ensure that the prerequisites that are described in " Prerequisites for Flashback Table " are met.
2. (Optional) To keep database triggers enabled during the flashback table operation, see " Keeping Triggers Enabled During Flashback Table ".
3. Connect SQL\*Plus to the PDB that contains the table, as a common user or local user with the `SYSDBA` or `SYSBACKUP` privilege. Identify the current database (CDB) SCN.
	You cannot roll back a `FLASHBACK TABLE` statement, but you can issue another `FLASHBACK TABLE` statement and specify a time just before the current time. Therefore, it is advisable to record the current SCN.
4. Identify the time, SCN, or restore point to which you want to return the table.
	If you have created restore points, then you can list available restore points by executing the following query:
	```
	SELECT NAME, SCN, TIME FROM V$RESTORE_POINT;
	```
5. Ensure that enough undo data exists to rewind the table to the specified target.
	If the `UNDO_RETENTION` initialization parameter is set, and the undo retention guarantee is on, then you can use the following query to determine how long undo data is being retained:
	```
	SELECT NAME, VALUE/60 MINUTES_RETAINED
	FROM   V$PARAMETER
	WHERE  NAME = 'undo_retention';
	```
6. Ensure that row movement is enabled for all objects that you are rewinding with Flashback Table.
	You can enable row movement for a table with the following SQL statement:
	```
	ALTER TABLE hr.temp_employees ENABLE ROW MOVEMENT;
	```
7. Determine whether the table that you intend to flash back has dependencies on other tables. If dependencies exist, then decide whether to flash back these tables as well.
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
8. Execute a `FLASHBACK TABLE` statement for the objects to flash back.
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
	  TO TIMESTAMP TO_TIMESTAMP('2013-10-17 09:30:00', 'YYYY-MM-DD HH:MI:SS');
	```
	Note:
	The mapping of time stamps to SCNs is not always exact. When you use time stamps with the `FLASHBACK TABLE` statement, the time to which the table is flashed back can vary by up to approximately 3 seconds of the time specified for `TO_TIMESTAMP`. If an exact point in time is required, then use an SCN rather than a time.
9. Optionally, query the table to check the data.

See Also:

Keeping Triggers Enabled During Flashback Table

##### 18.2.2.1 Keeping Triggers Enabled During Flashback Table

By default, the database disables triggers on the affected table before performing a `FLASHBACK TABLE` operation. After the operation, the database returns the triggers to the state they were in before the operation (enabled or disabled).

To keep triggers enabled during the flashback of the table, add an `ENABLE TRIGGERS` clause to the `FLASHBACK TABLE` statement.

For example, assume that at 17:00 an HR administrator discovers that an employee is missing from the `hr.temp_employees` table. This employee was included in the table at 14:00, the last time the report was run. Therefore, someone accidentally deleted the record for this employee between 14:00 and 17:00. The HR administrator uses Flashback Table to return the table to its state at 14:00, respecting any triggers set on the `hr.temp_employees` table, by using the SQL statement in the following example:

```
FLASHBACK TABLE hr.temp_employees
  TO TIMESTAMP TO_TIMESTAMP('2013-03-03 14:00:00' , 'YYYY-MM-DD HH:MI:SS') 
  ENABLE TRIGGERS;
```

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=ADMIN01512) to learn how to recover tables with the Flashback Table feature
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=SQLRF01802) for a simple Flashback Table scenario

### 18.3 Rewinding a DROP TABLE Operation with Flashback Drop

You can retrieve objects from the recycle bin with the `FLASHBACK TABLE ... TO BEFORE DROP` statement.

This section contains the following topics:

#### 18.3.1 About Flashback Drop

Flashback Drop reverses the effects of a `DROP TABLE` operation. Flashback Drop is faster than other recovery mechanisms that can be used in this situation, such as point-in-time recovery, and does not lead to downtime or loss of recent transactions.

When you drop a table, the database does not immediately remove the space associated with the table. Instead, the table is renamed and, along with any associated objects, placed in the recycle bin. System-generated recycle bin object names are unique. You can query objects in the recycle bin, just as you can query other objects.

A flashback operation retrieves the table from the recycle bin. When retrieving dropped tables, you can specify either the original user-specified name of the table or the system-generated name.

When you drop a table, the table and all of its dependent objects go into the recycle bin together. Likewise, when you perform Flashback Drop, the objects are generally all retrieved together. When you restore a table from the recycle bin, dependent objects such as indexes do not get their original names back; they retain their system-generated recycle bin names. Oracle Database retrieves all indexes defined on the table except for bitmap join indexes, and all triggers and constraints defined on the table except for referential integrity constraints that reference other tables.

Some dependent objects such as indexes may possibly have been reclaimed because of space pressure. In such cases, the reclaimed dependent objects are not retrievable from the recycle bin.

#### 18.3.2 Prerequisites of Flashback Drop

Prerequisites must be met before you perform a Flashback Drop operation.

The user privileges required for the operations related to Flashback Drop and the recycle bin are as follows:

- `DROP`
	Any user with `DROP` privileges over an object can drop the object, placing it in the recycle bin.
- `FLASHBACK TABLE ... TO BEFORE DROP`
	Privileges for this statement are tied to the privileges for `DROP`. That is, any user who can drop an object can perform Flashback Drop to retrieve the dropped object from the recycle bin.
- `PURGE`
	Privileges for a purge of the recycle bin are tied to the `DROP` privileges. Any user having `DROP` `TABLE`, `DROP` `ANY` `TABLE`, or `PURGE` `DBA_RECYCLE_BIN` privileges can purge the objects from the recycle bin.
- `READ` or `SELECT` and `FLASHBACK` for objects in the Recycle Bin
	Users must have the `READ` or `SELECT` and `FLASHBACK` privileges over an object in the recycle bin to query the object in the recycle bin. Any users who had the `READ` or `SELECT` privilege over an object before it was dropped continue to have the `READ` or `SELECT` privilege over the object in the recycle bin. Users must have `FLASHBACK` privilege to query any object in the recycle bin, because these are objects from a past state of the database.

Objects must meet the following prerequisites to be eligible for retrieval from the recycle bin:

- The recycle bin is only available for non-system, locally managed tablespaces. If a table is in a non-system, locally managed tablespace, but one or more of its dependent segments (objects) is in a dictionary-managed tablespace, then these objects are protected by the recycle bin.
- Tables that have fine-grained auditing (FGA) and Virtual Private Database (VPD) policies defined over them are not protected by the recycle bin.
- Partitioned index-organized tables are not protected by the recycle bin.
- The table must not have been purged, either by a user or by Oracle Database during a space reclamation operation.

#### 18.3.3 Performing a Flashback Drop Operation

Use the `FLASHBACK TABLE ... TO BEFORE DROP` statement to recover objects from the recycle bin. You can specify either the name of the table in the recycle bin or the original table name.

This section assumes a scenario in which you drop the wrong table. Many times you have been asked to drop tables in the test databases, but in this case you accidentally connect to the production database instead and drop `hr.employee_demo` in a PDB. You decide to use `FLASHBACK TABLE` to retrieve the dropped object.

To retrieve a dropped table:

1. Ensure that the prerequisites described in " Prerequisites of Flashback Drop " are met.
2. Connect SQL\*Plus to the PDB as a common user or local user with `SYSDBA` or `SYSBACKUP` privilege and obtain the name of the dropped table in the recycle bin.
	You can use the SQL\*Plus command `SHOW RECYCLEBIN` as follows:
	```
	SHOW RECYCLEBIN;
	ORIGINAL NAME    RECYCLEBIN NAME                   TYPE         DROP TIME
	---------------- --------------------------------- ------------ -------------
	EMPLOYEE_DEMO    BIN$gk3lsj/3akk5hg3j2lkl5j3d==$0  TABLE    2019-04-11:17:08:54
	```
	The `ORIGINAL NAME` column shows the original name of the object, whereas the `RECYCLEBIN NAME` column shows the name of the object as it exists in the bin.
	Alternatively, you can query `USER_RECYCLEBIN` or `DBA_RECYCLEBIN` to obtain the table name. The following example queries the `RECYCLEBIN` view to determine the original names of dropped objects:
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
3. Optionally, query the table in the recycle bin.
	You must use the recycle bin name of the object in your query rather than the object's original name. The following example queries the table with the recycle bin name of `BIN$gk3lsj/3akk5hg3j2lkl5j3d==$0`:
	```
	SELECT * FROM  "BIN$gk3lsj/3akk5hg3j2lkl5j3d==$0";
	```
	Quotation marks are required because of the special characters in the recycle bin name.
	Note:
	If you have the necessary privileges, then you can also use Flashback Query on tables in the recycle bin, but only by using the recycle bin name rather than the original table name. You cannot use Data Manipulation Language (DML) or DDL statements on objects in the recycle bin.
4. Retrieve the dropped table.
	Use the `FLASHBACK TABLE ... TO BEFORE DROP` statement. The following example restores the `BIN$gk3lsj/3akk5hg3j2lkl5j3d==$0` table, changes its name back to `hr.employee_demo`, and purges its entry from the recycle bin:
	```
	FLASHBACK TABLE "BIN$gk3lsj/3akk5hg3j2lkl5j3d==$0" TO BEFORE DROP;
	```
	The table name is enclosed in quotation marks because of the possibility of special characters appearing in the recycle bin object names.
	Alternatively, you can use the original name of the table:
	```
	FLASHBACK TABLE HR.EMPLOYEE_DEMO TO BEFORE DROP;
	```
	You can also assign a new name to the restored table by specifying the `RENAME TO` clause. For example:
	```
	FLASHBACK TABLE "BIN$gk3lsj/3akk5hg3j2lkl5j3d==$0" TO BEFORE DROP 
	  RENAME TO hr.emp_demo;
	```
5. Optionally, verify that all dependent objects retained their system-generated recycle bin names.
	The following query determines the names of the indexes of the retrieved `hr.employee_demo` table:
	```
	SELECT INDEX_NAME 
	FROM   USER_INDEXES 
	WHERE  TABLE_NAME = 'EMPLOYEE_DEMO';
	INDEX_NAME
	------------------------------
	BIN$JKS983293M1dsab4gsz/I249==$0
	```
6. Optionally, rename the retrieved indexes to their original names.
	The following statement renames the index to its original name of `i_emp_demo`:
	```
	ALTER INDEX "BIN$JKS983293M1dsab4gsz/I249==$0" RENAME TO I_EMP_DEMO;
	```
7. If the retrieved table had referential constraints before it was placed in the recycle bin, then re-create them.
	This step must be performed manually because the recycle bin does not preserve referential constraints on a table.

##### 18.3.3.1 Retrieving Objects Using Flashback Drop When Multiple Objects Share the Same Original Name

You can create, and then drop, several objects with the same original name. All dropped objects are stored in the recycle bin.

For example, consider the SQL statements in the following example:

Example 18-1 Dropping Multiple Objects with the Same Name

```
CREATE TABLE temp_employees ( ...columns ); # temp_employees version 1
DROP TABLE temp_employees;

CREATE TABLE temp_employees ( ...columns ); # temp_employees version 2
DROP TABLE temp_employees;

CREATE TABLE temp_employees ( ...columns ); # temp_employees version 3
DROP TABLE temp_employees;
```

Each table `temp_employees` is assigned a unique name in the recycle bin when it is dropped. You can use a `FLASHBACK TABLE ... TO BEFORE DROP` statement with the original name of the table, as shown in this example:

```
FLASHBACK TABLE temp_employees TO BEFORE DROP;
```

The most recently dropped table with this original name is retrieved from the recycle bin, with its original name.

The following example shows the retrieval from the recycle bin of all three dropped `temp_employees` tables from the previous example, with each assigned a new name.

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
BIN$yrMKlZaLMhfgNAgAIMenRA==$0 TEMP_EMPLOYEES  2013-02-05:21:05:52
BIN$yrMKlZaVMhfgNAgAIMenRA==$0 TEMP_EMPLOYEES  2013-02-05:21:25:13
BIN$yrMKlZaQMhfgNAgAIMenRA==$0 TEMP_EMPLOYEES  2013-02-05:22:05:53
```

You can use the following command to retrieve the middle table:

```
FLASHBACK TABLE BIN$yrMKlZaVMhfgNAgAIMenRA==$0 TO BEFORE DROP;
```

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=ADMIN01511) to learn how to use Flashback Drop and manage the recycle bin
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=SQLRF01802) for information about the `FLASHBACK TABLE` statement

### 18.4 Rewinding a Database with Flashback Database

Flashback Database reverses unwanted changes by returning your database to its state at a previous point in time.

#### 18.4.1 Prerequisites of Flashback Database

Flashback Database works by undoing changes to the data files that exist at the moment that you run the command. Prerequisites must be met to perform a Flashback Database operation.

To use the `FLASHBACK DATABASE` command to return your database contents to points in time within the flashback window, your database must have been previously configured for flashback logging. To return the database to a guaranteed restore point, you must have previously defined a guaranteed restore point.

Note the following important prerequisites:

- No current data files are lost or damaged. You can only use `FLASHBACK DATABASE` to rewind changes to a data file made by an Oracle database, not to repair media failures.
- You are not trying to recover from accidental deletion of data files or undo a change to the database name.
- You are not trying to use `FLASHBACK DATABASE` to return to a point in time before the restore or re-creation of a control file. If the database control file is restored from backup or re-created, then all accumulated flashback log information is discarded.
- You are not trying to use `FLASHBACK DATABASE` to undo a compatibility change.

See Also:

- " [Overview of Flashback Database, Restore Points and Guaranteed Restore Points](using-flasback-database-restore-points.md) "
- " [Using Normal and Guaranteed Restore Points](using-flasback-database-restore-points.md) "
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF194) for a complete list of command prerequisites and usage notes for `FLASHBACK DATABASE`

#### 18.4.2 Performing a Flashback Database Operation

You can rewind a whole multitenant container database (CDB) to a past point in time by using the `FLASHBACK DATABASE` command.

This topic presents a basic technique for performing a flashback of the database, specifying the desired target point in time with a time expression, the name of a normal or guaranteed restore point, or an SCN. It makes the following assumptions:

- You are rewinding the database to a point in time within the current database incarnation.
- The SCN used in the `FLASHBACK                                                  DATABASE` command refers to an SCN in the direct ancestral path of the database incarnations. An incarnation is in this path if it was not abandoned after the database was previously opened with the `RESETLOGS` option.

To perform a flashback database operation for a whole CDB:

1. Ensure that the prerequisites described in " Prerequisites of Flashback Database " are met.
2. Connect SQL\*Plus to the target CDB and determine the desired SCN, restore point, or point in time for the `FLASHBACK DATABASE` command.
	Obtain the earliest SCN in the flashback database window as follows:
	```
	SELECT OLDEST_FLASHBACK_SCN, OLDEST_FLASHBACK_TIME
	FROM V$FLASHBACK_DATABASE_LOG;
	```
	The most recent SCN that can be reached with Flashback Database is the current SCN of the database. The following query returns the current SCN:
	```
	SELECT CURRENT_SCN FROM V$DATABASE;
	```
	You can query available guaranteed restore points as follows (sample output included):
	```
	SELECT NAME, SCN, TIME, DATABASE_INCARNATION#,
	       GUARANTEE_FLASHBACK_DATABASE
	FROM   V$RESTORE_POINT
	WHERE  GUARANTEE_FLASHBACK_DATABASE='YES';
	 
	NAME                   SCN TIME                  DATABASE_INCARNATION# GUA
	--------------- ---------- --------------------- --------------------- ---
	BEFORE_CHANGES     5753126 04-MAR-12 12.39.45 AM                     2 YES
	```
	Note:
	If the flashback window does not extend far enough back into the past to reach the desired target time, and if you do not have a guaranteed restore point at the desired time, then you can achieve similar results by using database point-in-time recovery, as described in " Performing Point-in-Time Recovery of a Database ".
3. Shut down the database consistently, ensure that it is not opened by any instance, and then mount it:
	```
	SHUTDOWN IMMEDIATE;
	STARTUP MOUNT;
	```
4. Repeat the query in Step 2 of this procedure.
	Some flashback logging data is generated when the database is shut down. If flashback logs were deleted due to space pressure in the fast recovery area, then your target SCN may not be reachable.
	Note:
	If you run `FLASHBACK DATABASE` when your target SCN is outside the flashback window, then `FLASHBACK DATABASE` fails with an `ORA-38729` error. In this case, your database does not change.
5. Connect to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege, as described in " [Making Database Connections with RMAN](starting-interacting-with-rman-client.md) ".
6. To see which channels are preconfigured, run the `SHOW` command.
	During the flashback operation, RMAN may need to restore archived redo logs from backup. To see whether channels are configured, enter the following command (sample output is included):
	```
	SHOW ALL;
	```
	If the necessary devices and channels are configured, then no action is necessary. Otherwise, use the `CONFIGURE` command to configure automatic channels, or include `ALLOCATE CHANNEL` commands within a `RUN` block.
7. Run the `FLASHBACK DATABASE` command to perform a flashback operation for the whole CDB to a specified point in time.
	You can specify the target time by using an SCN, a time expression, or a CDB restore point.
	The following examples perform a flashback database operation for the whole CDB:
	```
	FLASHBACK DATABASE TO SCN 345588;
	FLASHBACK DATABASE TO RESTORE POINT cdb_before_upgrade;
	```
	When the `FLASHBACK DATABASE` command completes, the database is left mounted and recovered to the specified target time.
8. Open the CDB read-only in SQL\*Plus and run some queries to verify the database contents.
	Open the CDB read-only as follows:
	```
	ALTER DATABASE OPEN READ ONLY;
	```
	If you are satisfied with the state of the database, then end the procedure with Step 9. If you are not satisfied with the state of the database, skip to Step 10.
9. If you are satisfied with the results, then perform either of the following mutually exclusive actions:
	- Make the database available for updates by opening the database with the `RESETLOGS` option. If the database is open read-only, then execute the following commands in SQL\*Plus:
		```
		SHUTDOWN IMMEDIATE
		STARTUP MOUNT
		ALTER DATABASE OPEN RESETLOGS;
		```
		Note:
		After you perform this `OPEN RESETLOGS` operation, all changes to the database after the target SCN for `FLASHBACK DATABASE` are abandoned. Nevertheless, you can use the technique in " Rewinding the Database to an SCN in an Abandoned Incarnation Branch " to return the database to that range of SCNs while they remain in the flashback window.
	- Make a logical backup of the objects whose state was corrupted by using Oracle Data Pump Export. Afterward, use RMAN to recover the database to the present time:
		```
		RECOVER DATABASE;
		```
		This step undoes the effect of the Flashback Database by reapplying all changes in the redo logs to the database, returning it to the most recent SCN.
		After reopening the database read/write, you can import the exported objects with the Data Pump Import utility. See [Oracle Database Utilities](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=SUTIL100) to learn how to use Data Pump.
10. If you find that you used the wrong restore point, time, or SCN for the flashback, then mount the database and perform one of the following mutually exclusive options:
	- If your chosen target time was not far enough in the past, then use another `FLASHBACK DATABASE` command to rewind the database further back in time:
		```
		FLASHBACK DATABASE TO SCN 42963;  #earlier than current SCN
		```
	- If you chose a target SCN that is too far in the past, then use `RECOVER DATABASE UNTIL` to wind the database forward in time to the desired SCN:
		```
		RECOVER DATABASE UNTIL SCN 56963; #later than current SCN
		```
	- If you want to completely undo the effect of the `FLASHBACK DATABASE` command, then you can perform complete recovery of the database by using the `RECOVER DATABASE` command without an `UNTIL` clause or `SET UNTIL` command:
		```
		RECOVER DATABASE;
		```
		The `RECOVER DATABASE` command reapplies all changes to the database, returning it to the most recent SCN.
11. Since the [PDB](glossary.md) s are not automatically opened when the CDB is opened, open the PDBs.
	The following command, when connected to the root, opens all the PDBs:
	```
	ALTER PLUGGABLE DATABASE ALL OPEN;
	```
	If you want to open only some PDBs, then you can open each PDB separately. The following command, when connected to the root, opens the PDB `my_pdb`.
	```
	ALTER PLUGGABLE DATABASE my_pdb OPEN;
	```

Note:

When the `COMPATIBLE` initialization parameter is set to 12.1.0, in rare cases, performing a flashback database operation on a CDB across PDB (pluggable database) point-in-time recovery (PITR) or PDB flashback may result in the following error:

`ORA-39866: Data files for Pluggable Database                                           <PDB_name> must be offline to flashback across                                           special 12.1 PDB resetlogs`

To resolve this error and perform a flashback operation on a CDB across PDB PITR or PDB flashback, use the steps described in “Performing Flashback Database Operations on a CDB When a PDB Was Recovered Using DBPITR” in the Oracle Database Backup and Recovery User’s Guide 12c Release 1 (12.1).

#### 18.4.3 Performing a Flashback Database Operation for PDBs

You can perform a flashback database operation for a single pluggable database (PDB) using the `FLASHBACK DATABASE` command. Only data files related to that PDB are modified. The remaining PDBs in the CDB are not impacted and are available for use.

This topic presents a basic technique for performing a flashback of the PDB, specifying the desired target point in time with a time expression, the name of a normal or guaranteed restore point, or an SCN. It makes the following assumptions:

- You are rewinding the PDB to a point in time within the current database incarnation.
- The SCN used in the `FLASHBACK DATABASE` command refers to an SCN in the direct ancestral path of the PDB incarnations.

To perform a Flashback Database operation for a PDB:

1. Connect to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege, as described in [Making Database Connections with RMAN](starting-interacting-with-rman-client.md).
2. Ensure that the CDB is open.
	The following command, when connected to the root, displays the mode in which the CDB is open.
	```
	SELECT open_mode from V$DATABASE;
	```
3. Determine the desired SCN, restore point, or point in time for the Flashback Database command.
	When using restore points, you can perform a flashback database operation either to a CDB restore point, PDB restore point, PDB clean restore point, or PDB guaranteed restore point.
	Query the `V$RESTORE_POINT` view to obtain the list of PDB restore points. `V$FLASHBACK_DATABASE_LOG` displays the oldest SCN to which a flashback operation can be performed.
4. Ensure that the PDB for which the Flashback Database operation must be performed is closed. Other PDBs can be open and operational.
	When connected to the root, the following `ALTER PLUGGABLE DATABASE` command closes the PDB `my_pdb`.
	```
	ALTER PLUGGABLE DATABASE my_pdb CLOSE;
	```
5. Perform a Flashback Database operation for the specified PDB to the desired point in time.
	The following are some examples of flashback database operations for PDBs.
	- For a PDB that uses local undo:
		```
		FLASHBACK PLUGGABLE DATABASE my_pdb TO SCN 24368;
		FLASHBACK PLUGGABLE DATABASE my_pdb TO RESTORE POINT guar_rp;
		FLASHBACK PLUGGABLE DATABASE my_pdb TO CLEAN RESTORE POINT clean_rp;
		```
	- For a PDB that uses shared undo, you can optionally include the `AUXILIARY DESTINATION` clause to specify a location for the auxiliary instance that stores data files restored as part of the Flashback Database operation. If you omit this clause, then the auxiliary instance is created in the fast recovery area.
		```
		FLASHBACK PLUGGABLE DATABASE my_pdb TO SCN 24368 AUXILIARY DESTINATION '+data';
		FLASHBACK PLUGGABLE DATABASE my_pdb TO RESTORE POINT before_appl_changes AUXILIARY DESTINATION '/temp/aux_dest';
		FLASHBACK PLUGGABLE DATABASE my_pdb TO TIME "TO_DATE('03/20/15','MM/DD/YY')";
		```
6. Open the PDB with `RESETLOGS`.
	The following command opens the PDB named `my_pdb` with `RESETLOGS`:
	```
	ALTER PLUGGABLE DATABASE my_pdb OPEN RESETLOGS;
	```

Note:

Flashback operations are not supported for proxy PDBs.

Note:

- [About Restore Points in PDBs](using-flasback-database-restore-points.md)
- About Flashback Database Operations with PDBs

#### 18.4.4 Performing a Flashback Operation on a PDB to an Ancestor or Orphan Incarnation

You can flash back a PDB to an orphan PDB incarnation that is either within the same CDB incarnation or in an ancestor CDB incarnation.

Note:

- Flashback of a PDB to an orphan incarnation is supported only when the database uses local undo.
- Flashback of a PDB to an orphan CDB incarnation is not supported.

For example, assume today is Friday. You perform a flashback operation on a PDB, `pdb1`, to 4 pm on Wednesday and then open the PDB with `RESETLOGS`. All SCNs between 4pm on Wednesday and the current time are now on an orphan PDB incarnation. Starting with Oracle Database Release 21c, you can perform a flashback operation on `pdb1` to any time on Thursday because this time is within the current CDB incarnation.

Performing a flashback operation on a particular PDB modifies the data files for that PDB only. The remaining PDBs in the CDB are not impacted. The point in time to which the PDB must be flashed back is specified using a specific time, SCN, CDB restore point, PDB restore point, PDB clean restore point, or PDB guaranteed restore point.

Flashback data, until the point-in-time specified for the flashback, must be available.

1. Connect to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege. See "Making Database Connections with RMAN".
2. Ensure that the CDB is open.
	The following command, when connected to the root, displays the current mode of the CDB.
	```
	SELECT open_mode from V$DATABASE;
	```
3. If the CDB uses an Oracle keystore to encrypt backup data, ensure that the keystore is open.
	The following command opens the keystore:
	```
	ADMINISTER KEY MANAGEMENT SET KEYSTORE OPEN IDENTIFIED BY "my_password";
	```
4. Determine the desired SCN, restore point, or point in time for the Flashback Database command. This point must be within the current CDB incarnation or an ancestor CDB incarnation.
5. Ensure that the PDB that must be flashed back is closed. Other PDBs can be open and operational.
	When connected to the root, the following command closes the PDB `my_pdb`.
	```
	ALTER PLUGGABLE DATABASE my_pdb CLOSE;
	```
6. Set the orphan PDB incarnation to which the flashback PDB operation must be performed.
	This step is required only if the flashback operation is to an SCN or a CDB restore point in an orphan PDB incarnation. You need not set the orphan PDB incarnation, if the flashback operation is to a specified time or PDB restore point.
	The following command, when connected to the root, sets the recovery target PDB incarnation for the PDB named `my_pdb` to 5:
	```
	RESET PLUGGABLE DATABASE my_pdb INCARNATION TO 5;
	```
7. Perform a Flashback Database operation for the specified PDB to the desired point in time.
	The following are examples of flashback database operations on a PDB that uses local undo:
	```
	FLASHBACK PLUGGABLE DATABASE my_pdb TO SCN 153478;
	```
	```
	FLASHBACK PLUGGABLE DATABASE my_pdb TO RESTORE POINT clean_rp;
	```
8. Open the PDB with `RESETLOGS`.
	The following command opens the PDB named `my_pdb` with `RESETLOGS`:
	```
	ALTER PLUGGABLE DATABASE my_pdb OPEN RESETLOGS;
	```

#### 18.4.5 Monitoring Flashback Database

Data dictionary views contain information that is used to monitor flashback database.

When you use Flashback Database to rewind a database to a past target time, Flashback Database determines which blocks changed after the target time and restores them from the flashback logs. This is called the restore phase. After this phase completes, Flashback Database then uses redo logs to reapply changes that were made after these blocks were written to the flashback logs. This is called the recovery phase.

The progress of Flashback Database during the restore phase can be monitored by querying the `V$SESSION_LONGOPS` view. The `opname` is `Flashback Database`. Under the column `TOTALWORK` is the number of megabytes of flashback logs that must be read. The column `SOFAR` in the following example lists the number of megabytes that have been currently read.

Example 18-3 Tracking Flashback Database Progress - Restore Phase

```
SQL> SELECT sofar, totalwork, units FROM v$session_longops WHERE opname = 'Flashback Database';
 
SOFAR  TOTALWORK  UNITS
-----  ---------- --------------------------------
   17          60 Megabytes
```

The progress of Flashback Database during the recovery phase can be monitored by querying the view `V$RECOVERY_PROGRESS`.

See Also:

The [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=REFRN30199) for information about the view `V$RECOVERY_PROGRESS`

### 18.5 Performing Database Point-in-Time Recovery

Use the `RECOVER` command to perform point-in-time recovery (PITR) of container databases (CDBs) and pluggable databases (PDBs). PITR of PDBs can only be performed using RMAN.

RMAN DBPITR restores the database from backups before the target time for recovery, then uses incremental backups and redo to roll the database forward to the target time. You can recover to an SCN, time, log sequence number, or restore point. Oracle recommends that you create restore points at important times to make point-in-time recovery more manageable if it ever becomes necessary.

Oracle recommends that you perform Flashback Database rather than database point-in-time recovery if possible. Media recovery with backups are the last option when flashback technologies cannot be used to undo the most recent changes.

#### 18.5.1 Prerequisites of Database Point-in-Time Recovery

Certain prerequisites must be met to perform database point-in-time recovery (DBPITR).

This includes the following:

- Your database must be running in `ARCHIVELOG` mode.
- You must have backups of all data files from before the target SCN for DBPITR and archived logs for the period between the SCN of the backups and the target SCN.
- If the backups were created using transparent encryption, and if a password-protected software keystore was used, then the keystore password must be provided before the restore operation is performed. Use the `SET` command with the `DECRYPTION WALLET OPEN                         IDENTIFIED BY` option to specify the password that must be used to open the password-based keystore.
	If a user with the `SYSBACKUP` privilege is performing the recovery, and a password-protected software keystore is used, grant the `SYSKM` privilege to this user.
- If the backups were created using password-mode encryption, then you must provide the password used to decrypt backups before you run the `RESTORE` and `RECOVER` commands. Use the `SET DECRYPTION IDENTIFIED BY` command to specify the password used to decrypt the backups.

See Also:

- `SET` command in [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF153) for the syntax and usage of this command
- `RECOVER` command in [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF140) for a complete account of command prerequisites and usage notes

#### 18.5.2 Performing Point-in-Time Recovery of a Database

Use the `RESTORE` and `RECOVER` commands to perform point-in-time recovery for a whole CDB.

When performing DBPITR, you can avoid errors by using the `SET UNTIL` command to set the target time at the beginning of the procedure, rather than specifying the `UNTIL` clause on the `RESTORE` and `RECOVER` commands individually. This ensures that the data files restored from backup have time stamps early enough to be used in the subsequent `RECOVER` operation.

This section makes the following assumptions:

- You are performing DBPITR within the current database incarnation. If your target time is not in the current incarnation, then see " Recovering the Database to an Ancestor Incarnation " for more information about DBPITR to ancestor incarnations.
- The control file is current. If you must restore a backup control file, then see " [Performing Recovery with a Backup Control File](rman-recovery-advanced.md) ".
- Your database is using the current server parameter file. If you must restore a backup server parameter file, then see " [Restoring the Server Parameter File](rman-recovery-advanced.md) ".

To perform point-in-time recovery of a whole CDB:

1. Ensure that the prerequisites described in " Prerequisites of Database Point-in-Time Recovery " are met.
2. Determine the time, SCN, restore point, or log sequence that ends recovery.
	You can use the Flashback Query features to help you identify when the logical corruption occurred. If you have a flashback data archive enabled for a table, then you can query data that existed far in the past.
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
	         1  344890611          1          1      20037 24-SEP-13      20043
	         2  344890615          1          2      20043 24-SEP-13      20045
	         3  344890618          1          3      20045 24-SEP-13      20046
	```
	For example, if you discover that a user accidentally dropped a tablespace at 9:02 a.m., then you can recover to 9 a.m., just before the drop occurred. You lose all changes to the database made after this time.
3. If you are using a target time expression instead of a target SCN, then ensure that the time format environment variables are appropriate before invoking RMAN.
	The following are sample Globalization Support settings:
	```
	NLS_LANG = american_america.us7ascii
	NLS_DATE_FORMAT="Mon DD YYYY HH24:MI:SS"
	```
4. Connect RMAN to the root as a common user with the `SYSBACKUP` or `SYSDBA` privilege, as described in " [Connecting as Target to the Root](starting-interacting-with-rman-client.md) ". If applicable, connect to a recovery catalog.
5. Bring the CDB to a mounted state.
	```
	SHUTDOWN IMMEDIATE;
	STARTUP MOUNT;
	```
6. Perform the following operations within a `RUN` block:
	1. For DBPITR, use `SET` `UNTIL` to specify the target time, SCN, or log sequence number, or use `SET` `TO` to specify a restore point. If specifying a time, then use the date format specified in the `NLS_LANG` and `NLS_DATE_FORMAT` environment variables.
		2. If automatic channels are not configured, then manually allocate disk and tape channels as needed.
		3. Restore and recover the CDB.
	The following example performs DBPITR on the target CDB until SCN 1000:
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
	SET UNTIL TIME 'Nov 15 2013 09:00:00';
	SET UNTIL SEQUENCE 9923;  
	SET TO RESTORE POINT before_update;
	```
	If the operation completes without errors, then DBPITR has succeeded.
7. Perform either of the following mutually exclusive actions:
	- Open your CDB for read/write, abandoning all changes after the target SCN. In this case, you must shut down the CDB, mount it, and then execute the following command:
		```
		ALTER DATABASE OPEN RESETLOGS;
		```
		The `OPEN RESETLOGS` operation fails if a data file is offline unless the data file went offline normally or is read-only. You can bring files in read-only or offline normal tablespaces online after the `RESETLOGS` because they do not need any redo.
	- Export one or more objects from your CDB with Data Pump Export. You can then recover the CDB to the current point in time and reimport the exported objects, thus returning these objects to their state before the unwanted change without abandoning all other changes.
8. PDBs are not opened when the CDB is opened. The following command, when connected to the [root](glossary.md), opens all the PDBs.
	```
	ALTER PLUGGABLE DATABASE ALL OPEN;
	```
	You can open each PDB separately.

#### 18.5.3 Performing Point-in-Time Recovery of PDBs

When you recover one or more PDBs to a specified point-in-time, the remaining PDBs in the CDB are not affected and they can be open and operational.

Note:

If you are not using a recovery catalog, it is recommended that you turn on control file auto backups. Otherwise, PITR for PDBs may not work effectively when RMAN needs to undo data file additions or deletions.

When performing DBPITR on one or more PDBs in a CDB that uses shared undo, backups of the root and the CDB seed (`PDB$SEED`) of the CDB that contains the PDBs are required.

Starting with Oracle Database 12c Release 2 (12.2), if the `COMPATIBLE` initialization parameter is set to 12.2.0 or higher, you can perform flashback database for a CDB across a PDB flashback operation or PDB PITR.

To perform DBPITR on a PDB:

1. Ensure that the prerequisites described in " Prerequisites of Database Point-in-Time Recovery " are met.
2. Determine the time, SCN, restore point, or log sequence that ends recovery.
	Use Flashback Query or the alert log to determine when the logical corruption occurred. Or, use a SQL query to determine the log sequence number that contains the target SCN and then recover through this log.
3. If you are using a target time expression instead of a target SCN, then ensure that the time format environment variables are appropriate before invoking RMAN.
	The following are sample Globalization Support settings:
	```
	NLS_LANG = american_america.us7ascii
	NLS_DATE_FORMAT="Mon DD YYYY HH24:MI:SS"
	```
4. Connect RMAN to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege, as described in " [Making Database Connections with RMAN](starting-interacting-with-rman-client.md) ". If applicable, connect to a recovery catalog.
5. Close the PDB that is being recovered. The other PDBs and the CDB can remain open.
	```
	ALTER PLUGGABLE DATABASE pdb1 CLOSE;
	```
6. Perform the following operations within a `RUN` block:
	1. For DBPITR, use `SET UNTIL` to specify the target time, SCN, or log sequence number, or use `SET TO` to specify a restore point. If specifying a time, then use the date format specified in the `NLS_LANG` and `NLS_DATE_FORMAT` environment variables.
		2. If automatic channels are not configured, then manually allocate disk and tape channels as needed.
		3. Restore and recover the CDB.
	The following example performs DBPITR on the PDB `my_pdb` until SCN 1000:
	```
	RUN
	{ 
	  SET UNTIL SCN 1000;    
	  RESTORE PLUGGABLE DATABASE my_pdb;
	  RECOVER PLUGGABLE DATABASE my_pdb;
	}
	```
	If the operation completes without errors, then DBPITR has succeeded.
7. Open the PDB abandoning all changes after the target SCN.
	The following example opens the PDB named `my_pdb`.
	```
	ALTER PLUGGABLE DATABASE my_pdb OPEN RESETLOGS;
	```

Example 18-4 Recovering a PDB to a Specified Point-in-time

This example recovers a PDB named `PDB5` up to the SCN 1066 and then opens it for read/write access. Connect to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege and enter the following commands:

```
ALTER PLUGGABLE DATABASE pdb5 CLOSE;
run 
{
   SET UNTIL SCN 1066;
   RESTORE PLUGGABLE DATABASE pdb5;
   RECOVER PLUGGABLE DATABASE pdb5;
}
ALTER PLUGGABLE DATABASE pdb5 OPEN RESETLOGS;
```

This example assumes that a fast recovery area is being used. If you do not use a fast recovery area, then you must specify the temporary location of the auxiliary set files by using the `AUXILIARY DESTINATION` clause.

Opening the PDB with `RESETLOGS` creates a new PDB incarnation. You can query the `V$PDB_INCARNATION` view for the incarnation number.

See Also:

" Basic Concepts of Point-in-Time Recovery for PDBs " for information about the fast recovery area usage during point-in-time recovery of PDBs

#### 18.5.4 Performing Point-in-Time Recovery of PDBs to an Ancestor or Orphan Incarnation

You can perform point-in-time recovery (PITR) of a PDB to an orphan PDB incarnation that is either within the same CDB incarnation or in an ancestor CDB incarnation.

Performing PITR on a particular PDB modifies the data files for that PDB only. The remaining PDBs in the CDB are not impacted. The point in time to which the PDB must be recovered is specified as a specific time, SCN, CDB restore point, PDB restore point, PDB clean restore point, or PDB guaranteed restore point.

Note:

- Point-in-time recovery of a PDB to an orphan incarnation is supported only when the database uses local undo.
- Point-in-time recovery of a PDB to an orphan CDB incarnation is not supported.

Backups of all files, until the point specified for PITR, must be available.

1. Connect to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege. See "Making Database Connections with RMAN".
2. Ensure that the CDB is open.
	The following command, when connected to the root, displays the current mode of the CDB.
	```
	SELECT open_mode from V$DATABASE;
	```
3. If the CDB uses an Oracle keystore to encrypt backup data, ensure that the keystore is open.
	The following command opens the keystore:
	```
	ADMINISTER KEY MANAGEMENT SET KEYSTORE OPEN IDENTIFIED BY "my_password";
	```
4. Determine the desired SCN, restore point, or point in time for the PDB PITR operation. This point must be within the current CDB incarnation or in an ancestor CDB incarnation.
5. Ensure that the PDB that must be recovered is closed. Other PDBs can be open and operational.
	When connected to the root, the following command closes the PDB `my_pdb`.
	```
	ALTER PLUGGABLE DATABASE my_pdb CLOSE;
	```
6. Set the orphan PDB incarnation to which PDB PITR must be performed.
	This step is required only if the PITR is to an SCN or a CDB restore point in an orphan PDB incarnation. You need not set the orphan PDB incarnation, if the PITR is to a specified time or PDB restore point.
	The following command, when connected to the root, sets the recovery target PDB incarnation for the PDB named `my_pdb` to 5:
	```
	RESET PLUGGABLE DATABASE INCARNATION TO 5;
	```
7. Perform point-in-time recovery of the specified PDB to the desired point in time.
	The following are some examples of point-in-time recovery operations for a PDB that uses local undo.
	```
	RESTORE PLUGGABLE DATABASE my_pdb TO RESTORE POINT clean_rp;
	RECOVER PLUGGABLE DATABASE my_pdb TO RESTORE POINT clean_rp;
	```
8. Open the PDB with `RESETLOGS`.
	The following command opens the PDB named `my_pdb` with `RESETLOGS`:
	```
	ALTER PLUGGABLE DATABASE my_pdb OPEN RESETLOGS;
	```

#### 18.5.5 Recovering a Dropped PDB

Use the `RECOVER PLUGGABLE DATABASE` command to recover a PDB that was dropped.

Ensure that the backups required to recover the PDB are available. You need a backup of the control file, root, and the PDB that was dropped.

To recover a dropped PDB:

1. Ensure that the prerequisites described in " Prerequisites of Database Point-in-Time Recovery " are met.
	If the PDB was configured with isolated mode setting, then open the PDB keystore.
2. Determine the time, SCN, or log sequence to which the PDB must be recovered.
	Use Flashback Query or the alert log to determine when the logical corruption occurred. Or, use a SQL query to determine the log sequence number that contains the target SCN and then recover through this log.
3. If you are using a target time expression instead of a target SCN, then ensure that the time format environment variables are appropriate before invoking RMAN.
4. Connect RMAN to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege, as described in " [Making Database Connections with RMAN](starting-interacting-with-rman-client.md) ". If applicable, connect to a recovery catalog.
5. Perform the following operations within a `RUN` block:
	1. Use `SET UNTIL` to specify the target time, SCN, or log sequence number, or use `SET TO` to specify a restore point. If specifying a time, then use the date format specified in the `NLS_LANG` and `NLS_DATE_FORMAT` environment variables.
		2. If automatic channels are not configured, then manually allocate disk and tape channels as needed.
		3. The following example recovers the PDB `mypdb` that was previously dropped.
		```
		run
		{
		    SET UNTIL SCN 146898;
		    RECOVER PLUGGABLE DATABASE mypdb;
		}
		```
		If a fast recovery area is not used, include the `AUXILIARY DESTINATION` clause in the `RECOVER` command.
6. Open the PDB abandoning all changes after the target SCN.
	The following example opens the PDB named `mypdb`:
	`ALTER PLUGGABLE DATABASE mypdb OPEN                         RESETLOGS;`

### 18.6 Performing Point-in-Time Recovery of Application PDBs

Use the `RESTORE` and `RECOVER` commands to perform point-in-time recovery of an application PDB.

The `COMPATIBLE` parameter for the CDB must be set to 12.2 or higher.

To perform point-in-time recovery of an application PDB:

1. Ensure that the prerequisites for point-in-time recovery are met. Ensure that the prerequisites for point-in-time recovery are met, as described in " Prerequisites of Database Point-in-Time Recovery ".
2. Start RMAN and connect to the application rooot as an application common user with the `SYSDBA` or `SYSBACKUP` privilege.
	The application root has its own service name and you can connect to the application root in the same way that you connect to a PDB.
3. Determine the time, SCN, restore point, or log sequence that ends recovery.
4. Close the application PDB that must be recovered.
	The following command closes the application PDB called `hr_appcont_pdb1`.
	```
	ALTER PLUGGABLE DATABASE hr_appcont_pdb1 CLOSE;
	```
5. Perform the following operations within a `RUN` block:
	1. Use `SET UNTIL` to specify the target time, SCN, or log sequence number, or use `SET TO` to specify a restore point. If specifying a time, then use the date format specified in the `NLS_LANG` and `NLS_DATE_FORMAT` environment variables.
		2. If automatic channels are not configured, then manually allocate disk and tape channels as needed.
		3. Restore and recover the application container.
	```
	RUN
	{
	SET UNTIL SCN 34506;
	RESTORE PLUGGABLE DATABASE hr_appcont_pdb1;
	RECOVER PLUGGABLE DATABASE hr_appcont_pdb1;
	}
	```
6. Open the application PDB with `RESETLOGS`. This results in all changes after the target SCN being abandoned.
	```
	ALTER PLUGGABLE DATABASE hr_appcont_pdb1 OPEN RESETLOGS;
	```

See Also:

[Making Database Connections with RMAN](starting-interacting-with-rman-client.md)

### 18.7 Performing Point-in-Time Recovery of Sparse Databases

Performing point-in-time recovery of sparse databases is similar to performing point-in-time recovery of normal databases.

Ensure that the `COMPATIBLE` initialization parameter of the database being recovered is set to 12.2 or higher.

Note:

The base (read-only) data files in a sparse database are not encrypted. Ensure that the base data files are stored in a protected storage and accessed using secured communications.

To perform point-in-time recovery of a sparse database:

1. Ensure that the prerequisites described in " Prerequisites of Database Point-in-Time Recovery " are met.
2. Determine the time, SCN, restore point, or log sequence that ends recovery.
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
	         1  344890611          1          1      20037 24-SEP-13      20043
	         2  344890615          1          2      20043 24-SEP-13      20045
	         3  344890618          1          3      20045 24-SEP-13      20046
	```
	For example, if you discover that a user accidentally dropped a tablespace at 9:02 a.m., then you can recover to 9 a.m., just before the drop occurred. You lose all changes to the database made after this time.
3. If you are using a target time expression instead of a target SCN, then ensure that the time format environment variables are appropriate before invoking RMAN.
	The following are sample Globalization Support settings:
	```
	NLS_LANG = american_america.us7ascii
	NLS_DATE_FORMAT="Mon DD YYYY HH24:MI:SS"
	```
4. Connect RMAN to the target database and, if applicable, the recovery catalog database, as described in " [Making Database Connections with RMAN](starting-interacting-with-rman-client.md) ".
5. Bring the database to a mounted state.
	```
	SHUTDOWN IMMEDIATE;
	STARTUP MOUNT;
	```
	If the operation completes without errors, then DBPITR has succeeded.
6. Perform the following operations within a `RUN` block:
	1. For DBPITR, use `SET` `UNTIL` to specify the target time, SCN, or log sequence number, or use `SET` `TO` to specify a restore point. If specifying a time, then use the date format specified in the `NLS_LANG` and `NLS_DATE_FORMAT` environment variables.
	2. If automatic channels are not configured, then manually allocate disk and tape channels as needed.
	3. Restore and recover the sparse database with the `FROM SPARSE` option.
		The following example performs point-in-time recovery for a sparse database till the SCN `2775080`:
		```
		RUN 
		{
		SET UNTIL SCN 2775080; 
		RESTORE FROM SPARSE DATABASE; 
		RECOVER DATABASE; 
		}
		```
7. Perform either of the following mutually exclusive actions:
	- Open your database for read/write, abandoning all changes after the target SCN. In this case, you must shut down the database, mount it, and then execute the following command:
		```
		ALTER DATABASE OPEN RESETLOGS;
		```
		The `OPEN RESETLOGS` operation fails if a data file is offline unless the data file went offline normally or is read-only. You can bring files in read-only or offline normal tablespaces online after the `RESETLOGS` because they do not need any redo.
	- Export one or more objects from your database with Data Pump Export. You can then recover the database to the current point in time and reimport the exported objects, thus returning these objects to their state before the unwanted change without abandoning all other changes.

### 18.8 Flashback and Database Point-in-Time Recovery Scenarios

This section describes variations of the basic Flashback Database and DBPITR scenarios.

This section contains the following topics:

- Rewinding an OPEN RESETLOGS Operation with Flashback Database
- Rewinding the Database to an SCN in an Abandoned Incarnation Branch
- Recovering the Database to an Ancestor Incarnation

#### 18.8.1 Rewinding an OPEN RESETLOGS Operation with Flashback Database

Flashback Database can be used to undo an `OPEN RESETLOGS` operation.

The procedure for using Flashback Database to reverse an unwanted `ALTER                     DATABASE OPEN RESETLOGS` statement is similar to the general case described in " Performing a Flashback Database Operation ". Rather than specifying a particular SCN or point in time for the `FLASHBACK DATABASE` command, however, you use `FLASHBACK                     DATABASE TO BEFORE RESETLOGS`.

To undo an `OPEN RESETLOGS` operation:

1. Connect SQL\*Plus to the target database and verify that the beginning of the flashback window is earlier than the time of the most recent `OPEN RESETLOGS`.
	Run the following queries:
	```
	SELECT RESETLOGS_CHANGE# FROM V$DATABASE;
	SELECT OLDEST_FLASHBACK_SCN FROM V$FLASHBACK_DATABASE_LOG;
	```
	If `V$DATABASE.RESETLOGS_CHANGE#` is greater than `V$FLASHBACK_DATABASE_LOG.OLDEST_FLASHBACK_SCN`, then you can use Flashback Database to reverse the `OPEN RESETLOGS` operation.
2. Shut down the database, mount it, and recheck the flashback window. If the resetlogs SCN is still within the flashback window, then proceed to the next step.
3. Connect RMAN to the target database, as described in " [Making Database Connections with RMAN](starting-interacting-with-rman-client.md) ".
4. Perform a flashback to the SCN immediately before the `RESETLOGS`.
	Use the following form of the `FLASHBACK DATABASE` command:
	```
	FLASHBACK DATABASE TO BEFORE RESETLOGS;
	```
	As with other uses of `FLASHBACK DATABASE`, if the target SCN is before the beginning of the flashback database window, an error is returned and the database is not modified. If the command completes successfully, then the database is left mounted and recovered to the most recent SCN before the `OPEN RESETLOGS` operation in the previous incarnation.
5. Open the database read-only in SQL\*Plus and perform queries as needed to ensure that the effects of the logical corruption have been reversed.
	Open the database read-only as follows:
	```
	ALTER DATABASE OPEN READ ONLY;
	```
6. To make the database available for updates again, shut down the database, mount it, and then execute the following command:
	```
	ALTER DATABASE OPEN RESETLOGS;
	```

##### 18.8.1.1 About Undoing an OPEN RESETLOGS on Standby Databases with Flashback Database

Flashback Database across `OPEN RESETLOGS` may be used to perform multiple functions in a Data Guard environment.

This includes the following:

- Flashback to undo logical standby switchovers
	In this case, the database reverts to its role (primary or standby) at the target time for the Flashback Database operation.
- Undo of a physical standby activation
	You can temporarily activate a physical standby database, use it for testing or reporting purposes, and then use Flashback Database to return it to its role as a physical standby.
- Ongoing use of a standby database for testing
	The use of Flashback Database means that you do not require the use of storage snapshots.

See Also:

[Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=SBYDB00717) for details on these advanced applications of Flashback Database with Data Guard

#### 18.8.2 Rewinding the Database to an SCN in an Abandoned Incarnation Branch

You can use Flashback Database to rewind a database to an abandoned database incarnation.

The effect of Flashback Database or DBPITR followed by an `OPEN RESETLOGS` operation is to return the database to a previous SCN, and to abandon changes after this point. Therefore, some SCNs after that point can refer either to changes that were abandoned or changes in the current history of the database. In this way, a target SCN specified in `FLASHBACK DATABASE` can be ambiguous.

Unlike SCNs, time expressions and restore points are not ambiguous. A time expression is always associated with the incarnation that was current at that time. A restore point is always associated with the current incarnation when it was created. This is true even for times and restore points that correspond to abandoned database incarnations. The database incarnation is automatically reset to the incarnation that was current at the specified time or when the restore point was created.

You may want to use Flashback Database to rewind the database to an SCN in the parent incarnation that is later than the SCN of the `OPEN RESETLOGS` operation at which the current incarnation path branched from the old incarnation. [Figure 14-1](rman-data-repair-concepts.md) shows how SCNs can be generated in an incarnation branch even after an `OPEN RESETLOGS` operation creates a new incarnation. As shown in the diagram, the database could be at SCN 3000 in incarnation 3 when you must return to the abandoned SCN 1500 in incarnation 1.

If the SCN to which you are rewinding is in the [direct ancestral path](glossary.md), or if you are rewinding the database to a [restore point](glossary.md), then an explicit `RESET DATABASE` command is not necessary for Flashback Database. However, an explicit `RESET DATABASE TO INCARNATION` command is required when you use `FLASHBACK DATABASE` to rewind the database to an SCN in an abandoned database incarnation.

To rewind the database to an SCN in an abandoned incarnation branch:

1. Use SQL\*Plus to connect to the target database and verify that the flashback logs contain enough information to flash back to the SCN.
	For example, execute the following query:
	```
	SELECT OLDEST_FLASHBACK_SCN FROM V$FLASHBACK_DATABASE_LOG;
	```
2. Determine the target incarnation number for the Flashback Database operation, that is, the incarnation key for the parent incarnation.
	For example, execute the following query:
	```
	SELECT PRIOR_INCARNATION# 
	FROM   V$DATABASE_INCARNATION 
	WHERE  STATUS = 'CURRENT';
	```
3. Start RMAN and connect to the target database, as described in " [Making Database Connections with RMAN](starting-interacting-with-rman-client.md) ".
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
6. Run the `FLASHBACK DATABASE` command, specifying the target SCN.
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

- " [About Database Incarnations](rman-data-repair-concepts.md) " for useful background information about database incarnations, abandoned changes, and the effects of `ALTER DATABASE OPEN RESETLOGS`
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF148) for details about the `RESET DATABASE` command

#### 18.8.3 Recovering the Database to an Ancestor Incarnation

To perform DPITR to an noncurrent database incarnation, you must explicitly execute the `RESET DATABASE` to reset the database to the incarnation that was current at the target SCN. You must also restore a control file from the database incarnation containing the target SCN.

When RMAN is connected to a recovery catalog, a `RESTORE CONTROLFILE` command only searches the current database incarnation for the closest time specified in the `UNTIL` clause. To restore a control file from a noncurrent incarnation, you must execute `LIST INCARNATION` to identify the target database incarnation and specify this incarnation in the `RESET DATABASE TO INCARNATION` command.

When RMAN is not connected to a recovery catalog, you cannot execute the `RESET DATABASE TO INCARNATION` command before the database is mounted. Thus, you must execute `SET UNTIL`, restore the control file from autobackup, and then mount it.

Assume the following situation:

- RMAN is connected to a recovery catalog.
- You have a backup of target database `trgt` from October 2, 2013.
- DBPITR was performed on this database on October 10, 2013 to correct an earlier error. The `OPEN` `RESETLOGS` operation after that DBPITR started a new incarnation.

On October 25, you discover that you need crucial data that was dropped from the database at 8:00 a.m. on October 8, 2013. This time is before the beginning of the current incarnation.

To perform DBPITR to a noncurrent incarnation:

1. Ensure that the prerequisites described in " Prerequisites of Database Point-in-Time Recovery " are met.
2. Start RMAN and connect to a target database and recovery catalog, if required, as described in " [Making Database Connections with RMAN](starting-interacting-with-rman-client.md) ".
3. Determine which database incarnation was current at the time of the backup.
	Use `LIST INCARNATION` to find the primary key of the incarnation that was current at the target time:
	```
	LIST INCARNATION OF DATABASE trgt;
	List of Database Incarnations
	DB Key  Inc Key   DB Name   DB ID       STATUS     Reset SCN    Reset Time
	------- -------   -------   ------      -------    ----------   ----------
	1       2         TRGT      1224038686  PARENT     1            02-OCT-13
	1       582       TRGT      1224038686  CURRENT    59727        10-OCT-13
	```
	Look at the `Reset SCN` and `Reset Time` columns to identify the correct incarnation, and note the incarnation key in the `Inc` `Key` column. In this example, the backup was made 2 October 2013. In this case, the incarnation key value is 2.
4. Ensure that the database is started but not mounted.
	```
	STARTUP FORCE NOMOUNT;
	```
5. Reset the target database to the incarnation obtained in Step 2.
	In this example, specify the incarnation current at the time of the backup of 2 October. Use the value from the `Inc Key` column to identify the incarnation.
	```
	RESET DATABASE TO INCARNATION 2;
	```
6. Restore and recover the database, performing the following actions in the `RUN` command:
	- Set the end time for recovery to the time just before the loss of the data.
	- Allocate any channels required that are not configured.
	- Restore the control file from the October 2 backup and mount it.
	- Restore the data files and recover the database. Use the `RECOVER DATABASE ... UNTIL` command to perform DBPITR, bringing the database to the target time of 7:55 a.m. on October 8, just before the data was lost.
	The following example shows all of the steps required in this case:
	```
	RUN
	{
	  SET UNTIL TIME 'Oct 8 2013 07:55:00'; 
	  RESTORE CONTROLFILE;
	  # without recovery catalog, use RESTORE CONTROLFILE FROM AUTOBACKUP
	  ALTER DATABASE MOUNT; 
	  RESTORE DATABASE;
	  RECOVER DATABASE;
	}
	ALTER DATABASE OPEN RESETLOGS;
	```
	See Also:
	[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF148) for details about the `RESET DATABASE` command