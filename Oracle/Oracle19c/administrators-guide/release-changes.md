---
title: "Database Administrator’s Guide"
book: "Database Administrator's Guide"
doc_id: E96348-21
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/admin/release-changes.html
tags:
  - oracle
  - 19c
  - administrators-guide
---

## Changes in This Release for Oracle Database Administrator's Guide

There are changes in this document for recent releases of Oracle Database.

### Changes in Oracle Database Release 19c, Version 19.7

The following are changes in Oracle Database Administrator's Guide for Oracle Database release 19c, version 19.7.

New Features

- Standard Edition High Availability
	The Standard Edition High Availability feature provides cluster-based failover for Standard Edition 2 databases that use Oracle Clusterware.
	See " [Managing Standard Edition High Availability for Oracle Databases](creating-and-configuring-an-oracle-database.md) ".

**Parent topic:** Changes in This Release for Oracle Database Administrator's Guide

### Changes in Oracle Database Release 19c, Version 19.1

The following are changes in Oracle Database Administrator's Guide for Oracle Database release 19c, version 19.1.

- New Features
- Desupported Features

**Parent topic:** Changes in This Release for Oracle Database Administrator's Guide

#### New Features

The following features are new in this release:

- Oracle Database supplied user accounts are now schema only accounts
	Most of the Oracle Database supplied user accounts, except `SYS` and sample schemas are now schema only accounts, that is, these accounts are created without passwords. This prevents malicious users from logging into these accounts. You can assign passwords to these accounts whenever you want them to be authenticated. To find the status of an account, query the `ACCOUNT_STATUS` column of the `DBA_USERS` data dictionary view. If the account is schema only, then the status is `NONE`.
	See " [Predefined User Accounts](managing-users-and-securing-the-database.md) ".
- Automatic indexing
	The automatic indexing feature automates index management tasks, such as creating, rebuilding, and dropping indexes in an Oracle database based on changes in the application workload. This feature improves database performance by managing indexes automatically in an Oracle database.
	See " [Managing Automatic Indexes](managing-indexes.md) ".
- Quarantine for execution plans for SQL statements consuming excessive system resources
	You can now configure quarantine for execution plans for SQL statements that are terminated by the Resource Manager due to their excessive consumption of system resources, such as CPU and I/O. The quarantined execution plans for SQL statements are not allowed to run again, thus protecting the database from performance degradation.
	See " [Quarantine for Execution Plans for SQL Statements Consuming Excessive System Resources](diagnosing-and-resolving-problems.md) ".
- Memoptimized Rowstore – Fast Ingest
	The fast ingest feature of the Memoptimized Rowstore optimizes the processing of high-frequency, single-row data inserts from applications, such as Internet of Things (IoT) applications.
	See " [Enabling High Performance Data Streaming with the Memoptimized Rowstore](managing-memory.md) ".
- Hybrid partitioned tables
	Oracle Database now supports hybrid partitioned tables. A hybrid partitioned table is a partitioned table in which some partitions reside in the database and some partitions reside outside the database in external files, such as operating system files or Hadoop Distributed File System (HDFS) files.
	See [Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=VLDBG-GUID-C2B04585-BCFC-40D6-AFAB-47DF99A31C76).
	See also " [Specify the Type of Table to Create](managing-tables.md) ".
- New features in DBCA in the silent mode
	The following are the new features in DBCA in the silent mode:
	- Ability to create a PDB by cloning a remote PDB
		You can use the `createFromRemotePDB` parameter of the DBCA command `createPluggableDatabase` to create a PDB by cloning a remote PDB.
		See " [createPluggableDatabase](creating-and-configuring-an-oracle-database.md) ".
		- Ability to relocate a PDB to another CDB
		You can use the DBCA command `relocatePDB` to relocate a PDB to another CDB.
		See " [relocatePDB](creating-and-configuring-an-oracle-database.md) ".
		- Ability to create a duplicate of an Oracle database
		You can use the DBCA command `createDuplicateDB` to create a duplicate of an Oracle database.
		See " [createDuplicateDB](creating-and-configuring-an-oracle-database.md) ".
- New features related to SQL statements diagnosability
	The SQL diagnostics and repair tools, such as SQL Test Case Builder and SQL Repair Advisor have been enhanced to provide better diagnosis and repair capabilities for managing problematic SQL statements.
	- New SQL Repair Advisor function `DBMS_SQLDIAG.SQL_DIAGNOSE_AND_REPAIR`
		The new SQL Repair Advisor function `DBMS_SQLDIAG.SQL_DIAGNOSE_AND_REPAIR` creates a diagnostic task, executes it, and accepts SQL patch recommendation for a SQL statement that is generating a critical error.
		See [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=ARPLS-GUID-5B000758-3E3F-4F8B-83B6-DBCBE4815B2C).
		See also " [Running the SQL Repair Advisor Using the DBMS\_SQLDIAG Package Subprograms](diagnosing-and-resolving-problems.md) ".
		- New options to control SQL Test Case Builder output
		You can now specify these new options in the `DBMS_SQLDIAG.EXPORT_SQL_TESTCASE` procedure to control the output of SQL Test Case Builder: `compress`, `diag_event`, and `problem_type`.
		See " [Output of SQL Test Case Builder](diagnosing-and-resolving-problems.md) ".
		- New view `V$SQL_TESTCASES`
		You can view the information about all the test cases generated by SQL Test Case Builder by querying the `V$SQL_TESTCASES` view.
		See [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=REFRN-GUID-BFF605B2-49FA-44B1-880D-8928F5395184).
		See also " [Output of SQL Test Case Builder](diagnosing-and-resolving-problems.md) ".
- New SQL script `catpcat.sql` for building the data dictionary
	After creating a database using `CREATE DATABASE` statement, you can run `catctl.pl` with the new script `catpcat.sql` in place of running the scripts `catalog.sql` and `catproc.sql` for building the data dictionary. The script `catpcat.sql` runs the scripts ` catalog.sql` and `catproc.sql` with parallel processes, thus improving the performance of building the data dictionary manually.
	See " [Step 11: Run Scripts to Build Data Dictionary Views](creating-and-configuring-an-oracle-database.md) ".
- New `ALTER SYSTEM` statement clause `FLUSH PASSWORDFILE_METADATA_CACHE`
	If the database password file name or location has changed, then you must run the `ALTER SYSTEM` statement with the `FLUSH PASSWORDFILE_METADATA_CACHE` clause for the changes to take effect.
	See " [Creating a Database Password File with ORAPWD](getting-started-with-database-administration.md) ".
	See also [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=SQLRF-GUID-2C638517-D73A-41CA-9D8E-A62D1A0B7ADB).
- Oracle Database Resource Manager automatically enabled for Oracle Database In-Memory
	The Resource Manager is automatically enabled when Oracle Database In-Memory is enabled by setting the `INMEMORY_SIZE` initialization parameter to a value greater than 0.
	See " [Enabling Oracle Database Resource Manager and Switching Plans](managing-resources-with-oracle-database-resource-manager.md) ".
- New view `DBA_REGISTRY_BACKPORTS`
	The new view `DBA_REGISTRY_BACKPORTS` shows the bugs that have been fixed by the patches applied to the database. Only the bug fixes that have modified the data dictionary are displayed in this view.
	See [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=REFRN-GUID-23AC3A42-AE7E-4809-BE97-A586A89B611E).

**Parent topic:** Changes in Oracle Database Release 19c, Version 19.1

#### Desupported Features

The following features are desupported in this release.

- Oracle Multimedia
	Starting in Oracle Database 19c, Oracle Multimedia is desupported. Oracle recommends that you store multimedia content in SecureFiles LOBs, and use third party products for image processing and conversion.
- Oracle Streams
	Starting in Oracle Database 19c, the Oracle Streams feature is desupported. Use Oracle GoldenGate to replace all replication features of Oracle Streams.

**Parent topic:** Changes in Oracle Database Release 19c, Version 19.1

### Changes in Oracle Database Release 18c, Version 18.1

The following are changes in Oracle Database Administrator's Guide for Oracle Database release 18c, version 18.1.

- New Features
- Other Changes

**Parent topic:** Changes in This Release for Oracle Database Administrator's Guide

#### New Features

The following features are new in this release:

- Shadow lost write protection
	Shadow lost write protection provides fast detection and immediate response to a lost write. Using shadow lost write protection can minimize data loss and the time required to repair a database. You can enable shadow lost write protection for a database, a tablespace, or a data file without requiring an Oracle Data Guard standby database.
	See " [Managing Lost Write Protection with Shadow Tablespaces](managing-tablespaces.md) ".
- New default location for Oracle Database password file
	The default location for Oracle Database password file is `ORACLE_BASE` directory instead of `ORACLE_HOME` directory. This change supports read-only Oracle homes.
	See " [ORAPWD Syntax and Command Line Argument Descriptions](getting-started-with-database-administration.md) ".
	See " [About Configuring an Oracle Home in Read-Only Mode](creating-and-configuring-an-oracle-database.md) ".
- Private temporary tables
	Private temporary tables are stored in memory and each one is visible only to the session that created it.
	See " [Creating a Temporary Table](managing-tables.md) ".
- Inline external tables
	Inline external tables enable the runtime definition of an external table as part of a SQL statement, without creating the external table as persistent object in the data dictionary.
	See " [Using Inline External Tables](managing-tables.md) ".
- Parallel queue timeout
	You can specify the action to be taken on a timed out parallel SQL statement by setting the `PQ_TIMEOUT_ACTION` resource manager directive.
	See " [Parallel Queue Timeout](managing-resources-with-oracle-database-resource-manager.md) ".
- Cancelling a SQL statement in a session
	You can cancel a SQL statement in a session using the `ALTER SYSTEM CANCEL SQL` statement.
	See " [Cancelling a SQL Statement in a Session](managing-processes.md) ".
- Scalable sequence
	A scalable sequence can be used to improve the performance of data load operation in Oracle RAC databases.
	See " [Making a Sequence Scalable](managing-views-sequences-and-synonyms.md) ".
- Resetting a sequence
	The new `RESTART` clause can be used in an `ALTER                         SEQUENCE` statement to reset the sequence numbering.
	See " [Altering Sequences](managing-views-sequences-and-synonyms.md) ".
- The Memoptimized Rowstore
	The Memoptimized Rowstore enables fast lookup of data for the tables that are mainly queried based on primary key columns. This feature is particularly useful for the applications such as Internet of Things (IoT).
	See " [Enabling High Performance Data Streaming with the Memoptimized Rowstore](managing-memory.md) ".
- Read-only Oracle home
	An Oracle home can be configured in a read-only mode, thus preventing creation or modification of files inside the Oracle home directory `ORACLE_HOME`. A read-only Oracle home can be used as a software image that can be shared across multiple database servers. This simplifies patching and mass rollout as only one Oracle home image needs to be updated to distribute a patch to multiple database servers.
	See " [About Configuring an Oracle Home in Read-Only Mode](creating-and-configuring-an-oracle-database.md) ".
- Cloning a multitenant pluggable database (PDB) with Oracle Automatic Storage Management (Oracle ASM)
	Oracle ASM can be used to create a clone of a PDB.
	See [Oracle Multitenant Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=MULTI-GUID-7ED69A82-B797-4497-A160-FDDAA2AAC999).
- Proxy resident connection pooling
	Proxy resident connection pooling provides improved high availability, security, and performance for database clients. Proxy resident connection pooling uses the Proxy Resident Connection Pool that can be configured using Oracle Connection Manager in Traffic Director Mode.
	See " [About Proxy Resident Connection Pooling](managing-processes.md) ".
- Integration of Microsoft Active Directory Services with Oracle Database
	The Oracle Database can connect directly to Microsoft Active Directory and authenticate and authorize users. This provides a simpler, less complex option than the full featured integration with Oracle Enterprise User Security (EUS) and an Oracle Directory Service.
	See " [About Centralized User and Privilege Management](distributed-database-concepts.md) ".
- New nologging clauses for Active Data Guard
	Database nologging has been extended to provide better support for use in an Active Data Guard environment without significantly increasing the amount of redo log generation. The following two new nologging modes are introduced as alternatives to the existing nologging mode `NOLOGGING`:
	```
	STANDBY NOLOGGING FOR DATA AVAILABILITY
	STANDBY NOLOGGING FOR LOAD PERFORMANCE
	```
	See " [Performance Considerations of FORCE LOGGING Mode](creating-and-configuring-an-oracle-database.md) ".
- New features in DBCA silent mode
	- Creating a copy of a multitenant container database (CDB)
		A copy of a CDB can be created using the `-createDuplicateDB` command.
		See " [createDuplicateDB](creating-and-configuring-an-oracle-database.md) ".
		- Creating a copy of an Oracle RAC database
		A copy of an Oracle RAC database can be created using the `-createDuplicateDB` command option `-databaseConfigType` with the value of `RAC` or `RACONENODE`.
		See " [createDuplicateDB](creating-and-configuring-an-oracle-database.md) ".
		- Creating a standby database from an existing database
		A standby database can be created from an existing database using the `-createDuplicateDB` command option `-createAsStandby`.
		See " [createDuplicateDB](creating-and-configuring-an-oracle-database.md) ".
		- Verifying hardware and software prerequisites before creating a database
		Hardware and software prerequisites for creating a database can be verified by executing the `-executePrereqs` command on the system where the database needs to be created.
		See " [executePrereqs](creating-and-configuring-an-oracle-database.md) ".
		- Creating a copy of a database template
		A copy of a database template can be created using the `-createTemplateFromTemplate` command.
		See " [createTemplateFromTemplate](creating-and-configuring-an-oracle-database.md) ".
- Creating a copy of a pluggable database (PDB)
	A copy of a PDB can be created using the `-createPluggableDatabase` command option `-createPDBFrom` with the value of `PDB`.
	See " [createPluggableDatabase](creating-and-configuring-an-oracle-database.md) ".

**Parent topic:** Changes in Oracle Database Release 18c, Version 18.1

#### Other Changes

The following are additional changes in the release:

- New Oracle Multitenant book
	All the Oracle Multitenant topics have been moved from Oracle Database Administrator's Guide to a new book [Oracle Multitenant Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=MULTI-GUID-267F7D12-D33F-4AC9-AA45-E9CD671B6F22).
- New Oracle Sharding book
	All the Oracle Sharding topics have been moved from Oracle Database Administrator's Guide to a new book [Oracle Database Using Oracle Sharding](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=SHARD-GUID-0F39B1FB-DCF9-4C8A-A2EA-88705B90C5BF).

**Parent topic:** Changes in Oracle Database Release 18c, Version 18.1

### Changes in Oracle Database 12c Release 2 (12.2)

The following are changes in Oracle Database Administrator's Guide for Oracle Database 12c Release 2 (12.2).

- New Features

**Parent topic:** Changes in This Release for Oracle Database Administrator's Guide

#### New Features

The following features are new in this release:

- Improvements to online redefinition of tables:
	- In past releases, tables with `BFILE` columns could not be redefined online. In Oracle Database 12c Release 2 (12.2), tables with `BFILE` columns can be redefined online.
		- For online table redefinition that did not change the shape of the table, you can enable rollback of a table to return the table to its original definition and preserve DML changes made to the table.
		See " [Rolling Back Online Table Redefinition](managing-tables.md) ".
		- You can refresh dependent fast refreshable materialized views during online table redefinition by setting the `refresh_dep_mviews` parameter to `Y` in the `REDEF_TABLE` procedure or the `START_REDEF_TABLE` procedure.
		See " [Refreshing Dependent Materialized Views During Online Table Redefinition](managing-tables.md) ".
		- Optimize the performance of bulk updates to a table with the `EXECUTE_UPDATE` procedure in the `DBMS_REDEFINITION` package. Performance is optimized because the updates are not logged in the redo log.
		See " [Optimizing the Performance of Bulk Updates](managing-tables.md) ".
		- You can query the `V$ONLINE_REDEF` view to monitor the progress of an online table redefinition operation.
		See " [Monitoring Online Table Redefinition Progress](managing-tables.md) ".
		- When online table redefinition fails, often you can correct the problem that caused the failure and restart the online redefinition process where it last stopped.
		See " [Restarting Online Table Redefinition After a Failure](managing-tables.md) ".
- Limit PGA usage with Resource Manager
	Resource Manager can limit the amount of PGA memory that can be allocated to each session in a particular consumer group.
	See " [Program Global Area (PGA)](managing-resources-with-oracle-database-resource-manager.md) ".
- Improvements in index compression
	You can specify a high level of advanced index compression in addition to the low level available in past releases. The high level of advanced index compression saves more space than the low level.
	See " [Creating an Index Using Advanced Index Compression](managing-indexes.md) ".
- Hybrid Columnar Compression can be enabled for array inserts
	Rows inserted with an array insert can be compressed using Hybrid Columnar Compression. In past releases, only rows inserted with a direct-path `INSERT` could be compressed using Hybrid Columnar Compression.
	See " [About Table Compression](managing-tables.md) ".
- Improvements in table move operations
	When the `ONLINE` keyword is included in an `ALTER TABLE MOVE` statement, data manipulation language (DML) operations are supported during the move operation. Also, indexes are usable during the move operation when the `ONLINE` keyword is included and the `UPDATE INDEXES` clause is included.
	See " [About Moving a Table to a New Segment or Tablespace](managing-tables.md) ".
- New `SYSRAC` administrative privileges for separation of duties
	Oracle Database now provides an new administrative privilege for tasks related to Oracle Real Application Clusters (Oracle RAC) operations.
	See " [Administrative Privileges](getting-started-with-database-administration.md) ".
- New database resident connection pooling parameter for long running transactions
	To prevent long running transactions from being rolled back because of the limit specified in the `MAX_THINK_TIME` parameter, the new parameter `MAX_TXN_THINK_TIME` for subprograms in the `DBMS_CONNECTION_POOL` package specifies the maximum amount of time, in seconds, for any sessions with a transaction in progress.
	See " [Configuration Parameters for Database Resident Connection Pooling](managing-processes.md) ".
- Additional information available about the state of each connection in the database resident connection pool
	New columns added to the `V$CPOOL_CONN_INFO` view provide more information about the current state of each connection in the connection pool.
	See " [Determining the States of Connections in the Connection Pool](managing-processes.md) ".
- Improved monitoring for database links
	New views and supplied PL/SQL functions enable you to determine the host name of an outgoing database link, view detailed information about information about incoming database links, and determine the source of high system change number (SCN) activity for incoming database links.
	See " [Determining the Host of Outgoing Database Links](managing-a-distributed-database.md) ", " [Determining Information About Incoming Database Links](managing-a-distributed-database.md) ", and " [Determining the Source of High SCN Activity for Incoming Database Links](managing-a-distributed-database.md) ".
- Object quarantine
	Object quarantine isolates an object that has raised an error and monitors the object for impacts on the system.
	See " [Monitoring Quarantined Objects](monitoring-the-database.md) ".
- Delay of instance abort
	The `INSTANCE_ABORT_DELAY_TIME` initialization parameter specifies a delay time when an error causes an instance to abort.
	See " [Delaying Instance Abort](starting-up-and-shutting-down.md) ".
- Prespawned processes
	Oracle Database can prespawn processes for better client connection performance.
	See " [Managing Prespawned Processes](managing-processes.md) ".
- Partitioned external tables
	For large amounts of data, partitioning for external tables provides fast query performance and enhanced data maintenance.
	See " [Partitioning External Tables](managing-tables.md) ".

**Parent topic:** Changes in Oracle Database 12c Release 2 (12.2)

### Changes in Oracle Database 12c Release 1 (12.1.0.2)

The following are changes in Oracle Database Administrator's Guide for Oracle Database 12c Release 1 (12.1.0.2).

- New Features

**Parent topic:** Changes in This Release for Oracle Database Administrator's Guide

#### New Features

The following features are new in this release:

- In-Memory Column Store
	The In-Memory Column Store (IM column store) in an optional area in the SGA that stores whole tables, table partitions, individual columns, and materialized views in a compressed columnar format. The database uses special techniques to scan columnar data extremely rapidly. The IM column store is a supplement to rather than a replacement for the database buffer cache.
	See " [Improving Query Performance with Oracle Database In-Memory](managing-memory.md) ".
- Data Pump Support for the In-Memory Column Store
	Data Pump can keep, override, or drop the In-Memory clause for database objects being imported.
	See [Oracle Database In-Memory Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=INMEM-GUID-D7307BB7-2C8D-4A2C-98F6-B3F6000EFC20).
- Force full database caching mode
	To improve performance, you can force an instance to store the database in the buffer cache.
	See " [Using Force Full Database Caching Mode](managing-memory.md) ".
- Big Table Cache
	The Automatic Big Table Caching feature enables parallel queries to use the buffer cache.
	See " [Memory Architecture Overview](managing-memory.md) ".
- Attribute-clustered tables
	Attribute clustering specifies a directive for heap-organized tables to store data in close proximity on disk, providing performance and data storage benefits. This directive is only applicable for direct path operations, such was a bulk insert or a move operation.
	See " [Consider Using Attribute-Clustered Tables](managing-tables.md) ".
- Zone maps
	A zone is a set of contiguous data blocks on disk. A zone map tracks the minimum and maximum of specified columns for all individual zones. The primary benefit of zone maps is I/O reduction for table scans.
	See " [Consider Using Zone Maps](managing-tables.md) ".
- Advanced index compression
	Advanced index compression results in excellent compression ratios while still providing efficient access to the indexes. Advanced index compression works at the block level to provide the best compression for each block, which means that users do not require knowledge of data characteristics. Advanced index compression automatically chooses the right compression for each block.
	See " [Creating an Index Using Advanced Index Compression](managing-indexes.md) ".
- Oracle Clusterware support for the Diagnosability Framework
	Oracle Clusterware uses the Diagnosability Framework and ADR for recording diagnostic trace data and the Clusterware alert log.
	See " [ADR in an Oracle Clusterware Environment](diagnosing-and-resolving-problems.md) ".
- `READ` object privilege and `READ` `ANY` `TABLE` system privilege
	`READ` privilege on an object enables a user to select from an object without providing the user with any other privileges.
	See " [System and Object Privileges for External Tables](managing-tables.md) " and [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=DBSEG992) for more information.

**Parent topic:** Changes in Oracle Database 12c Release 1 (12.1.0.2)

### Changes in Oracle Database 12c Release 1 (12.1.0.1)

The following are changes in Oracle Database Administrator's Guide for Oracle Database 12c Release 1 (12.1.0.1).

- New Features
- Deprecated Features

**Parent topic:** Changes in This Release for Oracle Database Administrator's Guide

#### New Features

The following features are new in this release:

- Full transportable export/import
	Full transportable export/import enables you to move a database from one database instance to another. Transporting a database is much faster than other methods that move a database, such as full database export/import. In addition, you can use full transportable export/import to move a non-CDB (or an Oracle Database 11g Release 2 (11.2.0.3) database) into a PDB that is part of a CDB.
	See [Transporting Data](transporting-data.md).
- New administrative privileges for separation of duties
	Oracle Database now provides administrative privileges for tasks related to Oracle Recovery Manager (Oracle RMAN), Oracle Data Guard, and Transparent Data Encryption. Each new administrative privilege grants the minimum required privileges to complete tasks in each area of administration. The new administrative privileges enable you to avoid granting `SYSDBA` administrative privilege for many common tasks.
	See " [Administrative Privileges](getting-started-with-database-administration.md) "
- Database Smart Flash Cache support for multiple flash devices
	A database instance can access and combine multiple flash devices for Database Smart Flash Cache without requiring a volume manager.
	See " [Database Smart Flash Cache Initialization Parameters](managing-memory.md) ".
- Temporary undo
	Undo for temporary objects is stored in a temporary tablespace, not in the undo tablespace. Using temporary undo reduces the amount of undo stored in the undo tablespace and the size of the redo log. It also enables data manipulation language (DML) operations on temporary tables in a physical standby database with the Oracle Active Data Guard option.
	See " [Managing Temporary Undo](managing-undo.md) ". Also, see [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=SBYDB5163) for information about the benefits of temporary undo in an Oracle Data Guard environment.
- Move a data file online
	You can move a data file when the data file is online and being accessed. This capability simplifies maintenance operations, such as moving data to a different storage device.
	See " [Renaming and Relocating Online Data Files](managing-data-files-and-temp-files.md) ".
- Multiple indexes on the same set of columns
	You can create multiple indexes on the same set of columns to perform application migrations without dropping an existing index and recreating it with different attributes.
	See " [Understand When to Create Multiple Indexes on the Same Set of Columns](managing-indexes.md) ".
- Move a partition or subpartition online
	DML operations can continue to run uninterrupted on a partition or subpartition that is being moved without using online table redefinition.
	See " [Moving a Table to a New Segment or Tablespace](managing-tables.md) ".
- Online redefinition of a table in one step
	You can use the `REDEF_TABLE` procedure in the `DBMS_REDEFINITION` package to perform online redefinition of a table's storage properties in a single call to the procedure.
	See " [Performing Online Redefinition with the REDEF\_TABLE Procedure](managing-tables.md) ".
- Online redefinition of tables with multiple partitions
	To minimize downtime when redefining multiple partitions in a table, you can redefine these partitions online in a single session.
	See " [Online Redefinition of One or More Partitions](managing-tables.md) ".
- Online redefinition of tables with Virtual Private Database (VPD) policies
	To minimize downtime, tables with VPD policies can be redefined online.
	See " [Handling Virtual Private Database (VPD) Policies During Online Redefinition](managing-tables.md) ".
- New time limit parameter in the `FINISH_REDEF_TABLE` procedure
	The `dml_lock_timeout` parameter in the `FINISH_REDEF_TABLE` procedure in the `DBMS_REDEFINITION` package can specify how long the procedure waits for pending DML to commit.
	See step [8](managing-tables.md) in " [Performing Online Redefinition with Multiple Procedures in DBMS\_REDEFINITION](managing-tables.md) ".
- Invisible columns
	You can make individual table columns invisible. Any generic access of a table does not show the invisible columns in the table.
	See " [Understand Invisible Columns](managing-tables.md) ".
- Optimized `ALTER` `TABLE``...``ADD` `COLUMN` with default value for nullable columns
	A nullable column is a column created without using the `NOT` `NULL` constraint. For certain types of tables, when adding a nullable column that has a default value, the database can optimize the resource usage and storage requirements for the operation. It does so by storing the default value for the new column as table metadata, avoiding the need to store the value in all existing records.
	See " [Adding Table Columns](managing-tables.md) ".
- Copy-on-write cloning of a database with CloneDB
	When cloning a database with CloneDB, Oracle Database can create the files in a CloneDB database based on copy-on-write technology, so that only the blocks that are modified in the CloneDB database require additional storage on disk.
	See " [Cloning a Database with CloneDB](creating-and-configuring-an-oracle-database.md) ".
- DDL log
	When the logging of DDL statements is enabled, DDL statements are recorded in a separate DDL log instead of the alert log.
	See " [DDL Log](diagnosing-and-resolving-problems.md) ".
- Debug log
	Some information that can be used to debug a problem is recorded in a separate debug log instead of the alert log.
	See " [Debug Log](diagnosing-and-resolving-problems.md) ".
- Full-word options for the Server Control (SRVCTL) utility
	For improved usability, each SRVCTL utility option is a full word instead of single letter.
	See " [SRVCTL Command Reference for Oracle Restart](configuring-automatic-restart-of-an-oracle-database.md) ".
- Transaction Guard and Application Continuity
	Transaction Guard ensures at-most-once execution of transactions to protect applications from duplicate transaction submissions and associated logical errors. Transaction Guard enables Application Continuity, which is the ability to replay transactions and continue processing after recoverable communication errors.
	See " [Transaction Guard and Application Continuity](creating-and-configuring-an-oracle-database.md) ".
- Enhanced statement queuing
	Critical statements can bypass the parallel statement queue. You can set the resource plan directive `PARALLEL_STMT_CRITICAL` to `BYPASS_QUEUE` for a high-priority consumer group so that parallel statements from the consumer group bypass the parallel statement queue.
	See " [Creating Resource Plan Directives](managing-resources-with-oracle-database-resource-manager.md) ".
- New Job Types
	Several new script jobs have been added that permit running custom user scripts using SQL\*Plus, the RMAN interpreter, or a command shell for the computer platform.
	See " [Script Jobs](oracle-scheduler-concepts.md) ".

**Parent topic:** Changes in Oracle Database 12c Release 1 (12.1.0.1)

#### Deprecated Features

The following features are deprecated in this release and may be desupported in a future release:

- The `IGNORECASE` argument of ORAPWD
	To support strong authentication, Oracle recommends that you set `IGNORECASE` to `n` or omit `IGNORECASE` entirely. The default value of this optional ORAPWD argument is `n`.
	See " [Creating a Database Password File with ORAPWD](getting-started-with-database-administration.md) " for further information.
- Single-character options with Server Control (SRVCTL) utility commands
	All SRVCTL commands have been enhanced to accept full-word options instead of the single-letter options. All new SRVCTL command options added in this release support full-word options only and do not have single-letter equivalents. The use of single-character options with SRVCTL commands might be desupported in a future release.
	See " [SRVCTL Command Reference for Oracle Restart](configuring-automatic-restart-of-an-oracle-database.md) " for further information.
- The `FILE_MAPPING` initialization parameter
	The `FILE_MAPPING` initialization parameter is deprecated. It is still supported for backward compatibility.
	See [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=REFRN10060) for information about the `FILE_MAPPING` initialization parameter.
- `*_SCHEDULER_CREDENTIALS`
	This view continues to be available for backward compatibility.
	See " [Specifying Scheduler Job Credentials](scheduling-jobs-with-oracle-scheduler.md) " for further information.

See Also:

[Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=UPGRD60000)

**Parent topic:** Changes in Oracle Database 12c Release 1 (12.1.0.1)