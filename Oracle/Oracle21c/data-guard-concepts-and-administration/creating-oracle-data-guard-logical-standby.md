---
title: Concepts and Administration
book: Data Guard Concepts and Administration
doc_id: F31838-07
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sbydb/creating-oracle-data-guard-logical-standby.html
tags:
  - oracle
  - 21c
  - data-guard-concepts-and-administration
---

There are a number of steps involved in creating a logical standby database, including prerequisites and post-creation tasks.

Note:

A multitenant container database is the only supported architecture in Oracle Database 20c. While the documentation is being revised, legacy terminology may persist. In most cases, "database" and "non-CDB" refer to a CDB or PDB, depending on context. In some contexts, such as upgrades, "non-CDB" refers to a non-CDB from a previous release.

See the following topics for information about creating a logical standby database.

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sbydb&id=ADMIN11117) for information about creating and using server parameter files
- Oracle Enterprise Manager Cloud Control online help system for information about using the Oracle Data Guard broker graphical user interface (GUI) to automatically create a logical standby database.

### About Creating a Logical Standby in a Multitenant Environment

Learn about how logical standby databases work in a multitenant environment.

Be aware of the following when you create and use a multitenant container database CDB) as a logical standby:

- The database role is defined at the CDB level, not at the pluggable database (PDB) container level.
- You must have the `CDB_DBA` role.
- If you execute a switchover or failover operation, then the entire CDB undergoes the role change.
- Any DDL related to role changes must be executed while connected to the root container of the CDB.
- A logical standby of a CDB operates a single pool of processes that mine the redo stream once, but the responsibility is shared for updating all of the PDBs and the root container of the CDB.
- You are not required to have the same set of PDBs at the primary and standby. However, only tables that exist in the same container at both the primary and standby are replicated.
- In general, logical standby PL/SQL interfaces which modify global configuration attributes, such as `DBMS_LOGSTDBY.APPLY_SET`, are executed in the root container. However, `DBMS_LOGSTDBY.INSTANTIATE_TABLE` must be called inside the container where the table of interest resides, and the `DBMS_LOGSTDBY.SKIP` procedure must be called inside the container of interest.
- Logical standby views are enhanced to provide container names where appropriate. Many DBA views have analogous CDB views whose names begin with CDB. For example, the view `CDB_LOGSTDBY_NOT_UNIQUE` contains the same data as shown in `DBA_LOGSTDBY_NOT_UNIQUE` view, but it has an additional column indicating the PDB name. When the `CDB_LOGSTDBY_NOT_UNIQUE` view is queried in the root it shows data for all databases in the CDB.
- The `ALTER DATABASE RECOVER TO LOGICAL STANDBY` command functions only in the CDB; it is not allowed in a PDB.
- A role is associated with an entire CDB; individual PDBs do not have their own roles. Therefore, the following role change DDL associated with logical standbys affect the entire CDB:
	`ALTER DATABASE [PREPARE|COMMIT] TO SWITCHOVER`
	`ALTER DATABASE ACTIVATE LOGICAL STANDBY`
- The `ALTER DATABASE [START|STOP] LOGICAL STANDBY                         APPLY` command functions only in the root container and affects the entire CDB. This statement is not allowed on a PDB.
- The `ALTER DATABASE GUARD` command functions only in the root container and affects the entire CDB. For example, if an `ALTER                         DATABASE GUARD ALL` statement is issued, then user activity in the root and in all PDBs is restricted.

See Also:

- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sbydb&id=ARPLS66850) for more information about using the `DBMS_LOGSTDBY.SKIP` procedure in containers

### Prerequisite Conditions for Creating a Logical Standby Database

Before you create a logical standby database, you must first ensure the primary database is properly configured.

Perform the following tasks on the primary database to prepare for logical standby database creation:

- Determine Support for Data Types and Storage Attributes for Tables
- Ensure Table Rows in the Primary Database Can Be Uniquely Identified

A logical standby database uses standby redo logs (SRLs) for redo received from the primary database, and also writes to online redo logs (ORLs) as it applies changes to the standby database. Thus, logical standby databases often require additional `ARC` n processes to simultaneously archive SRLs and ORLs. Additionally, because archiving of ORLs takes precedence over archiving of SRLs, a greater number of SRLs may be needed on a logical standby during periods of very high workload.

Note:

Logical standby databases must be run in `ARCHIVELOG` mode for standby redo log archival to be performed.

See [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sbydb&id=ADMIN008) for information about archiving.

#### Determine Support for Data Types and Storage Attributes for Tables

Before setting up a logical standby database, ensure the logical standby database can maintain the data types and tables in your primary database.

See [Unsupported Tables](data-type-ddl-support-on-logical-standby-databases.md) for information about specific SQL queries you can use to determine if there are any unsupported data types or storage attributes.

#### Ensure Table Rows in the Primary Database Can Be Uniquely Identified

The ROWIDs contained in the redo records generated by the primary database cannot be used to identify the corresponding row in the logical standby database.

This is because the physical organization in a logical standby database is different from that of the primary database, even though the logical standby database is created from a backup copy of the primary database.

Oracle uses primary-key or unique-constraint/index supplemental logging to logically identify a modified row in the logical standby database. When database-wide primary-key and unique-constraint/index supplemental logging is enabled, each `UPDATE` statement also writes the column values necessary in the redo log to uniquely identify the modified row in the logical standby database.

- If a table has a primary key defined, then the primary key is logged along with the modified columns as part of the `UPDATE` statement to identify the modified row.
- In the absence of a primary key, the shortest nonnull unique-constraint/index is logged along with the modified columns as part of the `UPDATE` statement to identify the modified row.
- If there is no primary key and no nonnull unique constraint/index, then all columns with a declared maximum length of 4000 bytes are logged as part of the `UPDATE` statement to help identify the modified row. There are some requirements and restrictions with respect to supported data types. See the following sections for more information:
	- [Supported Table Storage Types](data-type-ddl-support-on-logical-standby-databases.md)
		- [Unsupported Table Storage Types](data-type-ddl-support-on-logical-standby-databases.md)
- A function-based index, even though it is declared as unique, cannot be used to uniquely identify a modified row. However, logical standby databases support replication of tables that have function-based indexes defined, as long as modified rows can be uniquely identified.

Oracle recommends that you add a primary key or a nonnull unique index to tables in the primary database, whenever possible, to ensure that SQL Apply can efficiently apply redo data updates to the logical standby database.

Perform the following steps to ensure SQL Apply can uniquely identify rows of each table being replicated in the logical standby database.

1. Query the `DBA_LOGSTDBY_NOT_UNIQUE` view to display a list of tables that SQL Apply may not be able to uniquely identify. For example:
	```
	SQL> SELECT OWNER, TABLE_NAME FROM DBA_LOGSTDBY_NOT_UNIQUE
	  2> WHERE (OWNER, TABLE_NAME) NOT IN 
	  3> (SELECT DISTINCT OWNER, TABLE_NAME FROM DBA_LOGSTDBY_UNSUPPORTED) 
	  4> AND BAD_COLUMN = 'Y';
	```
	This query may take a few minutes to run.
2. If your application ensures the rows in a table are unique, then you can create a disabled primary key `RELY` constraint on the table. This avoids the overhead of maintaining a primary key on the primary database.

To create a disabled `RELY` constraint on a primary database table, use the `ALTER TABLE` statement with a `RELY DISABLE` clause. The following example creates a disabled `RELY` constraint on a table named `mytab`, for which rows can be uniquely identified using the `id` and `name` columns:

```
SQL> ALTER TABLE mytab ADD PRIMARY KEY (id, name) RELY DISABLE;
```

When you specify the `RELY` constraint, the system assumes that rows are unique. Because you are telling the system to rely on the information, but are not validating it on every modification done to the table, you must be careful to select columns for the disabled `RELY` constraint that uniquely identify each row in the table. If such uniqueness is not present, then SQL Apply does not correctly maintain the table.

To improve the performance of SQL Apply, add a unique-constraint/index to the columns to identify the row on the logical standby database. Failure to do so results in full table scans during `UPDATE` or `DELETE` statements carried out on the table by SQL Apply.

See Also:

- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sbydb&id=REFRN23123) for information about the `DBA_LOGSTDBY_NOT_UNIQUE` view
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sbydb&id=SQLRF01001) for information about the `ALTER TABLE` statement syntax
- [Create a Primary Key RELY Constraint](managing-oracle-data-guard-logical-standby-databases.md) for information about `RELY` constraints and actions you can take to increase performance on a logical standby database

### Step-by-Step Instructions for Creating a Logical Standby Database

These are the tasks you perform to create a logical standby database.

Note:

New data types added after Oracle Database 12c Release 1 (12.1) are not supported with Oracle Data Guard logical standby. For example, Oracle Data Guard logical standby does not support long identifiers, complex Abstract Data Types (ADTs), and spatial data types. Note that this limitation does not exist with an Oracle Data Guard physical standby database, `DBMS_ROLLING`, or Oracle GoldenGate. To obtain the benefits of a standby database with more recent data types, Oracle recommends that you consider using either a physical standby database, a snapshot standby database, or that you use the logical replication features of Oracle GoldenGate.

Table 4-1 Creating a Logical Standby Database

| Task | Database |
| --- | --- |
| Create a Physical Standby Database | Primary |
| Stop Redo Apply on the Physical Standby Database | Standby |
| Prepare the Primary Database to Support a Logical Standby Database | Primary |
| Transition to a Logical Standby Database | Standby |
| Open the Logical Standby Database | Standby |
| Verify the Logical Standby Database Is Performing Properly | Standby |

#### Creating a Logical Standby Task 1: Create a Physical Standby Database

You create a logical standby database by first creating a physical standby database and then transitioning it to a logical standby database.

Follow the instructions in [Creating a Physical Standby Database](creating-oracle-data-guard-physical-standby.md) to create a physical standby database.

#### Creating a Logical Standby Task 2: Stop Redo Apply on the Physical Standby Database

You can run Redo Apply on the new physical standby database for any length of time before converting it to a logical standby database.

However, before converting to a logical standby database, stop Redo Apply on the physical standby database. Stopping Redo Apply is necessary to avoid applying changes past the redo that contains the LogMiner dictionary (described in Build a Dictionary in the Redo Data).

To stop Redo Apply, issue the following statement on the physical standby database:

```
SQL> ALTER DATABASE RECOVER MANAGED STANDBY DATABASE CANCEL;
```

#### Creating a Logical Standby Task 3: Prepare the Primary Database to Support a Logical Standby Database

As part of creating a logical standby database, you must prepare the primary database to support a logical standby.

See the following topics:

- Prepare the Primary Database for Role Transitions
- Build a Dictionary in the Redo Data

##### Prepare the Primary Database for Role Transitions

You may have to modify certain parameters when you prepare to switch the role of a primary database.

In [Set Primary Database Initialization Parameters](creating-oracle-data-guard-physical-standby.md), you set up several standby role initialization parameters to take effect when the primary database is transitioned to the physical standby role.

Note:

This step is necessary only if you plan to perform switchovers.

If you plan to transition the primary database to the logical standby role, then you must also modify the parameters shown in bold typeface in Example 4-1, so that no parameters need to change after a role transition:

- Change the `VALID_FOR` attribute in the original `LOG_ARCHIVE_DEST_1` destination to archive redo data only from the online redo log and not from the standby redo log.
- Include the `LOG_ARCHIVE_DEST_3` destination on the primary database. This parameter only takes effect when the primary database is transitioned to the logical standby role.

The following table describes the archival processing defined by the changed initialization parameters shown in Example 4-1.

| LOG\_ARCHIVE\_DEST\_n | When the Chicago Database Is Running in the Primary Role | When the Chicago Database Is Running in the Logical Standby Role |
| --- | --- | --- |
| `LOG_ARCHIVE_DEST_1` | Directs archiving of redo data generated by the primary database from the local online redo log files to the local archived redo log files in `/arch1/chicago/`. | Directs archiving of redo data generated by the logical standby database from the local online redo log files to the local archived redo log files in `/arch1/chicago/`. |
| `LOG_ARCHIVE_DEST_3` | Is ignored; `LOG_ARCHIVE_DEST_3` is valid only when `chicago` is running in the standby role. | Directs archiving of redo data from the standby redo log files to the local archived redo log files in `/arch2/chicago/`. |

Example 4-1 Primary Database: Logical Standby Role Initialization Parameters

```
LOG_ARCHIVE_DEST_1=
 'LOCATION=/arch1/chicago/ 
  VALID_FOR=(ONLINE_LOGFILES,ALL_ROLES)
  DB_UNIQUE_NAME=chicago'
LOG_ARCHIVE_DEST_3=
 'LOCATION=/arch2/chicago/
  VALID_FOR=(STANDBY_LOGFILES,STANDBY_ROLE) 
  DB_UNIQUE_NAME=chicago'
LOG_ARCHIVE_DEST_STATE_3=ENABLE
```

To dynamically set these initialization parameters, use the SQL `ALTER SYSTEM SET` statement and include the `SCOPE=BOTH` clause so that the changes take effect immediately and persist after the database is shut down and started up again.

##### Build a Dictionary in the Redo Data

A LogMiner dictionary must be built into the redo data so that the LogMiner component of SQL Apply can properly interpret changes it sees in the redo.

As part of building the LogMiner dictionary, supplemental logging is automatically set up to log primary key and unique-constraint/index columns. The supplemental logging information ensures each update contains enough information to logically identify each row that is modified by the statement.

To build the LogMiner dictionary, issue the following statement:

```
SQL> EXECUTE DBMS_LOGSTDBY.BUILD;
```

The `DBMS_LOGSTDBY.BUILD` procedure waits for all existing transactions to complete. Long-running transactions executed on the primary database affect the timeliness of this command.

Note:

In databases created using Oracle Database 11g Release 2 (11.2) or later, supplemental logging information is automatically propagated to any existing physical standby databases. However, for databases in earlier releases, or if the database was created using an earlier release and then upgraded to 11.2, you must check whether supplemental logging is enabled at the physical standby(s) if it is also enabled at the primary database. If it is not enabled at the physical standby(s), then before performing a switchover or failover, you must enable supplemental logging on all existing physical standby databases. To do so, issue the following SQL statement on each physical standby:

```
SQL>  ALTER DATABASE ADD SUPPLEMENTAL LOG DATA (PRIMARY KEY, UNIQUE INDEX) COLUMNS;
```

If you do not do this, then any logical standby that is also in the same Oracle Data Guard configuration is unusable if a switchover or failover is performed to one of the physical standby databases. If a switchover or failover has already occurred and supplemental logging was not enabled, then you must recreate all logical standby databases.

See Also:

- The `DBMS_LOGSTDBY.BUILD` PL/SQL package in [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sbydb&id=ARPLS66834)
- The `UNDO_RETENTION` initialization parameter in [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sbydb&id=REFRN10225)

#### Creating a Logical Standby Task 4: Transition to a Logical Standby Database

There are some necessary tasks you must perform to prepare the physical standby database to transition to a logical standby database.

The following topics describe these tasks:

- Convert to a Logical Standby Database
- Adjust Initialization Parameters for the Logical Standby Database

##### Convert to a Logical Standby Database

The redo logs contain the information necessary to convert your physical standby database to a logical standby database.

Note:

If you have an Oracle RAC physical standby database, then shut down all but one instance, set `CLUSTER_DATABASE` to `FALSE`, and start the standby database as a single instance in `MOUNT EXCLUSIVE` mode, as follows:

```
SQL> ALTER SYSTEM SET CLUSTER_DATABASE=FALSE SCOPE=SPFILE;
SQL> SHUTDOWN ABORT;
SQL> STARTUP MOUNT EXCLUSIVE;
```

To continue applying redo data to the physical standby database until it is ready to convert to a logical standby database, issue the following SQL statement:

```
SQL> ALTER DATABASE RECOVER TO LOGICAL STANDBY db_name;
```

For db\_name, specify a database name that is different from the primary database to identify the new logical standby database. If you are using a server parameter file (spfile) at the time you issue this statement, then the database updates the file with appropriate information about the new logical standby database. If you are not using an spfile, then the database issues a message reminding you to set the name of the `DB_NAME` parameter after shutting down the database.

Note:

If you are creating a logical standby database in the context of performing a rolling upgrade of Oracle software with a physical standby database, then issue the following command instead:

```
SQL> ALTER DATABASE RECOVER TO LOGICAL STANDBY KEEP IDENTITY;
```

A logical standby database created with the `KEEP IDENTITY` clause retains the same `DB_NAME` and `DBID` as that of its primary database. Such a logical standby database can only participate in one switchover operation, and thus should only be created in the context of a rolling upgrade with a physical standby database.

The `KEEP IDENTITY` clause is available only if the database being upgraded is running Oracle Database release 11.1 or later.

The statement waits, applying redo data until the LogMiner dictionary is found in the log files. This may take several minutes, depending on how long it takes redo generated in Build a Dictionary in the Redo Data to be transmitted to the standby database, and how much redo data needs to be applied. If a dictionary build is not successfully performed on the primary database, then this command never completes. You can cancel the SQL statement by issuing the `ALTER DATABASE RECOVER                     MANAGED STANDBY DATABASE CANCEL` statement from another SQL session.

Caution:

In releases prior to Oracle Database 11g, you needed to create a new password file before you opened the logical standby database. This is no longer needed. Creating a new password file at the logical standby database causes redo transport services to not work properly.

##### Adjust Initialization Parameters for the Logical Standby Database

Note:

If you started with an Oracle RAC physical standby database, then set `CLUSTER_DATABASE` back to `TRUE`, as follows:

```
SQL> ALTER SYSTEM SET CLUSTER_DATABASE=TRUE SCOPE=SPFILE;
```

On the logical standby database, shutdown the instance and issue the `STARTUP MOUNT` statement to start and mount the database. Do not open the database; it should remain closed to user access until later in the creation process. For example:

```
SQL> SHUTDOWN;
SQL> STARTUP MOUNT;
```

You need to modify the `LOG_ARCHIVE_DEST_` `n` parameters because, unlike physical standby databases, logical standby databases are open databases that generate redo data and have multiple log files (online redo log files, archived redo log files, and standby redo log files). It is good practice to specify separate local destinations for:

- Archived redo log files that store redo data generated by the logical standby database. In Example 4-2, this is configured as the `LOG_ARCHIVE_DEST_1=LOCATION=/arch1/boston` destination.
- Archived redo log files that store redo data received from the primary database. In Example 4-2, this is configured as the `LOG_ARCHIVE_DEST_3=LOCATION=/arch2/boston` destination.

Example 4-2 shows the initialization parameters that were modified for the logical standby database. The parameters shown are valid for the Boston logical standby database when it is running in either the primary or standby database role.

Note:

If database compatibility is set to 11.1 or later, you can use the fast recovery area to store remote archived logs. To do this, you need to set only the following parameters (assuming you have already set the `DB_RECOVERY_FILE_DEST` and `DB_RECOVERY_FILE_DEST_SIZE` parameters):

```
LOG_ARCHIVE_DEST_1=
  'LOCATION=USE_DB_RECOVERY_FILE_DEST
   DB_UNIQUE_NAME=boston'
```

Because you are using the fast recovery area, it is not necessary to specify the `VALID_FOR` parameter. Its default value is (`ALL_LOGFILES,ALL_ROLES`) and that is the desired behavior in this case. `LOG_ARCHIVE_DEST_1` is used for all log files, both online (primary) and standby.

The following table describes the archival processing defined by the initialization parameters shown in Example 4-2.

| LOG\_ARCHIVE\_DEST\_n | When the Boston Database Is Running in the Primary Role | When the Boston Database Is Running in the Logical Standby Role |
| --- | --- | --- |
| `LOG_ARCHIVE_DEST_1` | Directs archival of redo data generated by the primary database from the local online redo log files to the local archived redo log files in `/arch1/boston/`. | Directs archival of redo data generated by the logical standby database from the local online redo log files to the local archived redo log files in `/arch1/boston/`. |
| `LOG_ARCHIVE_DEST_2` | Directs transmission of redo data to the remote logical standby database `chicago`. | Is ignored; `LOG_ARCHIVE_DEST_2` is valid only when `boston` is running in the primary role. |
| `LOG_ARCHIVE_DEST_3` | Is ignored; `LOG_ARCHIVE_DEST_3` is valid only when `boston` is running in the standby role. | Directs archival of redo data received from the primary database to the local archived redo log files in `/arch2/boston/`. |

Note:

The `DB_FILE_NAME_CONVERT` initialization parameter is not honored once a physical standby database is converted to a logical standby database. If necessary, register a skip handler and provide SQL Apply with a replacement DDL string to execute by converting the path names of the primary database data files to the standby data file path names. See the [`DBMS_LOGSTDBY`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sbydb&id=ARPLS363) package for information about the `SKIP` procedure.

Example 4-2 Modifying Initialization Parameters for a Logical Standby Database

```
LOG_ARCHIVE_DEST_1=
  'LOCATION=/arch1/boston/
   VALID_FOR=(ONLINE_LOGFILES,ALL_ROLES)
   DB_UNIQUE_NAME=boston'
LOG_ARCHIVE_DEST_2=
  'SERVICE=chicago ASYNC
   VALID_FOR=(ONLINE_LOGFILES,PRIMARY_ROLE)
   DB_UNIQUE_NAME=chicago'
LOG_ARCHIVE_DEST_3=
  'LOCATION=/arch2/boston/
   VALID_FOR=(STANDBY_LOGFILES,STANDBY_ROLE)
   DB_UNIQUE_NAME=boston'
LOG_ARCHIVE_DEST_STATE_1=ENABLE
LOG_ARCHIVE_DEST_STATE_2=ENABLE
LOG_ARCHIVE_DEST_STATE_3=ENABLE
```

#### Creating a Logical Standby Task 5: Open the Logical Standby Database

Use an `ALTER DATABASE` SQL statement to open the newly created logical standby.

For example, issue the following statement (do not supply the `RESETLOGS` option if the logical standby was created using the `KEEP` `IDENTITY` option):

```
SQL> ALTER DATABASE OPEN RESETLOGS;
```

Note:

If you started with an Oracle RAC physical standby database, then you can start up all other standby instances at this point.

Caution:

If you are co-locating the logical standby database on the same computer system as the primary database, then you must issue the following SQL statement before starting SQL Apply for the first time, so that SQL Apply skips the file operations performed at the primary database. The reason this is necessary is that SQL Apply has access to the same directory structure as the primary database, and data files that belong to the primary database could possibly be damaged if SQL Apply attempted to re-execute certain file-specific operations.

```
SQL> EXECUTE DBMS_LOGSTDBY.SKIP('ALTER TABLESPACE');
```

The `DB_FILENAME_CONVERT` parameter that you set up while co-locating the physical standby database on the same system as the primary database, is ignored by SQL Apply. See [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sbydb&id=ARPLS363) for information about `DBMS_LOGSTDBY.SKIP` and equivalent behavior in the context of a logical standby database.

Because this is the first time the database is being opened, the database's global name is adjusted automatically to match the new `DB_NAME` initialization parameter. (This is not true if the logical standby was created using the `KEEP` `IDENTITY` option.)

Note:

If you are creating the logical standby database to perform a rolling upgrade of the Oracle Database software, and you are concerned about updates to objects that may not be supported by SQL Apply, then Oracle recommends that you use the `DBMS_LOGSTDBY` PL/SQL procedure. At the logical standby database, run the following procedures to capture and record the information as events in the `DBA_LOGSTDBY_EVENTS` table:

```
EXEC DBMS_LOGSTDBY.APPLY_SET('MAX_EVENTS_RECORDED',
DBMS_LOGSTDBY.MAX_EVENTS);

EXEC DBMS_LOGSTDBY.APPLY_SET('RECORD_UNSUPPORTED_OPERATIONS', 'TRUE');
```

This captures information about any transactions running on the primary that are not supported by logical standby. When the upgrade is complete and before you switch production to the new version, check this table. If nothing is recorded, then you know everything was replicated. If something is recorded, then you can choose to either take corrective action or abandon the upgrade.

See Also:

- [Customizing Logging of Events in the DBA\_LOGSTDBY\_EVENTS View](managing-oracle-data-guard-logical-standby-databases.md) for more information about the `DBA_LOGSTDBY_EVENTS` view
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sbydb&id=ARPLS363) for complete information about the `DBMS_LOGSTDBY` package

Issue the following statement to begin applying redo data to the logical standby database:

```
SQL>  ALTER DATABASE START LOGICAL STANDBY APPLY IMMEDIATE;
```

#### Creating a Logical Standby Task 6: Verify the Logical Standby Database Is Performing Properly

After you create a logical standby database, it is important to verify that it is performing properly.

See the following topics:

- [Redo Transport Services](oracle-data-guard-redo-transport-services.md)
- [Managing a Logical Standby Database](managing-oracle-data-guard-logical-standby-databases.md)

### Creating a Logical Standby: Post-Creation Steps

Note:

The conversion of the physical standby database to a logical standby database happens in two phases:

1. As part of the `ALTER DATABASE RECOVER TO LOGICAL STANDBY` statement (unless you have specified the `KEEP IDENTITY` clause), the DBID of the database is changed.
2. As part of the first successful invocation of `ALTER DATABASE START LOGICAL STANDBY APPLY ` statement, the control file is updated to make it consistent with that of the newly created logical standby database.
	After you have successfully invoked the `ALTER DATABASE START LOGICAL STANDBY APPLY` statement, take a full backup of the logical standby database, because the backups taken from the primary database cannot be used to restore the logical standby database.

At this point, the logical standby database is running and can provide the maximum performance level of data protection. The following list describes additional preparations you can take on the logical standby database:

- Upgrade the data protection mode
	The Oracle Data Guard configuration is initially set up in the maximum performance mode (the default).
- Enable Flashback Database
	Flashback Database removes the need to re-create the primary database after a failover. Flashback Database enables you to return a database to its state at a time in the recent past much faster than traditional point-in-time recovery, because it does not require restoring data files from backup nor the extensive application of redo data. You can enable Flashback Database on the primary database, the standby database, or both.

See Also:

- [Converting a Failed Primary Into a Standby Database Using Flashback Database](examples-of-using-oracle-data-guard.md) and [Using Flashback Database After Issuing an Open Resetlogs Statement](examples-of-using-oracle-data-guard.md) for scenarios showing how to use Flashback Database in an Oracle Data Guard environment.
- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sbydb&id=BRADV71000) for more information about Flashback Database