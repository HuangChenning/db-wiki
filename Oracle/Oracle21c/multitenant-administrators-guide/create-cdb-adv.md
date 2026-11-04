---
title: "Administrator’s Guide"
book: "Multitenant Administrator's Guide"
doc_id: F31734-10
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/multi/create-cdb-adv.html
tags:
  - oracle
  - 21c
  - multitenant-administrators-guide
---

- Specifying CREATE DATABASE Statement Clauses  
	When you execute a `CREATE` `DATABASE` statement, Oracle Database performs several operations. The actual operations performed depend on the clauses that you specify in the `CREATE` `DATABASE` statement and the initialization parameters that you have set.
- Specifying Initialization Parameters  
	You can add or edit basic initialization parameters before you create your new database.
- Managing Initialization Parameters Using a Server Parameter File  
	Initialization parameters for the Oracle Database have traditionally been stored in a text initialization parameter file. For better manageability, you can choose to maintain initialization parameters in a binary server parameter file that is persistent across database startup and shutdown.
- Managing Application Workloads with Database Services  
	A database service is a named representation of one or more database instances. Services enable you to group database workloads and route a particular work request to an appropriate instance.
- Managing Standard Edition High Availability for Oracle Databases  
	The Standard Edition High Availability feature provides protection against unplanned outages for Oracle Database Standard Edition 2 single instance databases using Oracle Clusterware.
- Cloning a Database  
	This section describes various methods of cloning an Oracle database.
- Configuring EM Express for a CDB  
	For a CDB, you can configure Oracle Enterprise Manager Database Express (EM Express) for the root and for each PDB by setting a global HTTPS port, or you can set a different port for every container in the CDB.
- Dropping a Database  
	Dropping a CDB involves removing its data files, online redo logs, control files, and initialization parameter files.

**Parent topic:** [Creating CDBs](creating-and-configuring-a-multitenant-environment.md)

### Specifying CREATE DATABASE Statement Clauses

When you execute a `CREATE` `DATABASE` statement, Oracle Database performs several operations. The actual operations performed depend on the clauses that you specify in the `CREATE` `DATABASE` statement and the initialization parameters that you have set.

- About CREATE DATABASE Statement Clauses  
	You can use the `CREATE DATABASE` clauses to simplify the creation and management of your database.
- Protecting Your Database: Specifying Passwords for SYS and SYSTEM Users  
	To protect your database, specify passwords for `SYS` and `SYSTEM` users.
- Creating a Locally Managed SYSTEM Tablespace  
	During database creation, create a locally managed SYSTEM tablespace. A locally managed tablespace uses a bitmap stored in each data file to manage the extents.
- Specify Data File Attributes for the SYSAUX Tablespace  
	The SYSAUX tablespace is created by default, but you can specify its data file attributes during database creation.
- Using Automatic Undo Management: Creating an Undo Tablespace  
	Automatic undo management uses an undo tablespace.
- Creating a Default Permanent Tablespace  
	Oracle strongly recommends that you create a default permanent tablespace. Oracle Database assigns to this tablespace any non- `SYSTEM` users for whom you do not explicitly specify a different permanent tablespace.
- Creating a Default Temporary Tablespace  
	When you create a default temporary tablespace, Oracle Database assigns it as the temporary tablespace for users who are not explicitly assigned a temporary tablespace.
- Specifying Oracle Managed Files at Database Creation  
	You can minimize the number of clauses and parameters that you specify in your `CREATE DATABASE` statement by using the Oracle Managed Files feature.
- Supporting Bigfile Tablespaces During Database Creation  
	Oracle Database simplifies management of tablespaces and enables support for extremely large databases by letting you create **bigfile tablespaces**.
- Specifying the Database Time Zone and Time Zone File  
	Oracle Database datetime and interval data types and time zone support make it possible to store consistent information about the time of events and transactions.
- Specifying FORCE LOGGING Mode  
	Some data definition language statements (such as `CREATE` `TABLE`) allow the `NOLOGGING` clause, which causes some database operations not to generate redo records in the database redo log. The `NOLOGGING` setting can speed up operations that can be easily recovered outside of the database recovery mechanisms, but it can negatively affect media recovery and standby databases.

**Parent topic:** Creating a CDB: Advanced Topics

#### About CREATE DATABASE Statement Clauses

You can use the `CREATE DATABASE` clauses to simplify the creation and management of your database.

When you execute a `CREATE` `DATABASE` statement, Oracle Database performs at least these operations:

- Creates the data files for the database
- Creates the control files for the database
- Creates the online redo logs for the database and establishes the `ARCHIVELOG` mode
- Creates the `SYSTEM` tablespace
- Creates the `SYSAUX` tablespace
- Creates the data dictionary
- Sets the character set that stores data in the database
- Sets the database time zone
- Mounts and opens the database for use

**Parent topic:** Specifying CREATE DATABASE Statement Clauses

#### Protecting Your Database: Specifying Passwords for SYS and SYSTEM Users

To protect your database, specify passwords for `SYS` and `SYSTEM` users.

- In the `CREATE` `DATABASE` statement, include clauses that specify the password for users `SYS` and `SYSTEM`.

The clauses of the `CREATE` `DATABASE` statement used for specifying the passwords for users `SYS` and `SYSTEM` are:

- `USER` `SYS` `IDENTIFIED` `BY` `password`
- `USER` `SYSTEM` `IDENTIFIED` `BY` `password`

When choosing a password, keep in mind that passwords are case-sensitive. Also, there may be password formatting requirements for your database.

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=DBSEG-GUID-451679EB-8676-47E6-82A6-DF025FD65156) for information about the Oracle guidelines for creating secure passwords

**Parent topic:** Specifying CREATE DATABASE Statement Clauses

#### Creating a Locally Managed SYSTEM Tablespace

During database creation, create a locally managed SYSTEM tablespace. A locally managed tablespace uses a bitmap stored in each data file to manage the extents.

- Specify the `EXTENT MANAGEMENT LOCAL` clause in the `CREATE` `DATABASE` statement to create a locally managed `SYSTEM` tablespace.

If you do not specify the `EXTENT MANAGEMENT LOCAL` clause, then by default the database creates a dictionary-managed `SYSTEM` tablespace. Dictionary-managed tablespaces are deprecated.

If you create your database with a locally managed `SYSTEM` tablespace, and if you are not using Oracle Managed Files, then ensure that the following conditions are met:

- You specify the `DEFAULT TEMPORARY TABLESPACE` clause in the `CREATE DATABASE` statement.
- You include the `UNDO TABLESPACE` clause in the `CREATE DATABASE` statement.

See Also:

- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF01204) for more specific information about the use of the `DEFAULT TEMPORARY TABLESPACE` and `UNDO TABLESPACE` clauses when `EXTENT MANAGEMENT LOCAL` is specified for the `SYSTEM` tablespace
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=GUID-6387DF1B-F29C-4EDF-925C-202DEEFE9E1A) to learn about locally managed tablespaces

**Parent topic:** Specifying CREATE DATABASE Statement Clauses

#### Specify Data File Attributes for the SYSAUX Tablespace

The SYSAUX tablespace is created by default, but you can specify its data file attributes during database creation.

To specify data file attributes for the `SYSAUX` tablespace:

- Include the `SYSAUX DATAFILE` clause in the `CREATE` `DATABASE` statement.

If you include a `DATAFILE` clause for the `SYSTEM` tablespace, then you must specify the `SYSAUX DATAFILE` clause as well, or the `CREATE` `DATABASE` statement will fail. This requirement does not exist if the Oracle Managed Files feature is enabled (see " Specifying Oracle Managed Files at Database Creation ").

- About the SYSAUX Tablespace  
	The `SYSAUX` tablespace is always created at database creation.

**Parent topic:** Specifying CREATE DATABASE Statement Clauses

##### About the SYSAUX Tablespace

The `SYSAUX` tablespace is always created at database creation.

The `SYSAUX` tablespace serves as an auxiliary tablespace to the `SYSTEM` tablespace. Because it is the default tablespace for many Oracle Database features and products that previously required their own tablespaces, it reduces the number of tablespaces required by the database. It also reduces the load on the `SYSTEM` tablespace.

You can specify only data file attributes for the `SYSAUX` tablespace, using the `SYSAUX DATAFILE` clause in the `CREATE` `DATABASE` statement. Mandatory attributes of the `SYSAUX` tablespace are set by Oracle Database and include:

- `PERMANENT`
- `READ WRITE`
- `EXTENT MANAGEMENT LOCAL`
- `SEGMENT SPACE MANAGEMENT AUTO`

You cannot alter these attributes with an `ALTER TABLESPACE` statement, and any attempt to do so will result in an error. You cannot drop or rename the `SYSAUX` tablespace.

The size of the `SYSAUX` tablespace is determined by the size of the database components that occupy `SYSAUX`. You can view a list of these components by querying the `V$SYSAUX_OCCUPANTS` view. Based on the initial sizes of these components, the `SYSAUX` tablespace must be at least 400 MB at the time of database creation. The space requirements of the `SYSAUX` tablespace will increase after the database is fully deployed, depending on the nature of its use and workload.

The `SYSAUX` tablespace has the same security attributes as the `SYSTEM` tablespace.

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-30942290-88DD-4D62-816F-F7EDCE661710) to learn how to manage the `SYSAUX` tablespace

**Parent topic:** Specify Data File Attributes for the SYSAUX Tablespace

#### Using Automatic Undo Management: Creating an Undo Tablespace

Automatic undo management uses an undo tablespace.

- To enable automatic undo management, set the `UNDO_MANAGEMENT` initialization parameter to `AUTO` in your initialization parameter file. Alternatively, omit this parameter so that the database defaults to automatic undo management.

In this mode, undo data is stored in an undo tablespace and is managed by Oracle Database. To define and name the undo tablespace yourself, you must include the `UNDO TABLESPACE` clause in the `CREATE DATABASE` statement at database creation time. If you omit this clause, and automatic undo management is enabled, then the database creates a default undo tablespace named `SYS_UNDOTBS`.

Note:

If you decide to define the undo tablespace yourself, then ensure that its block size matches the highest data file block size for the database.

See Also:

- " Specifying the Method of Undo Space Management "
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-2C865CF9-A8B5-4BF1-A451-E8C08D3611F0) for information about the creation and use of undo tablespaces

**Parent topic:** Specifying CREATE DATABASE Statement Clauses

#### Creating a Default Permanent Tablespace

Oracle strongly recommends that you create a default permanent tablespace. Oracle Database assigns to this tablespace any non- `SYSTEM` users for whom you do not explicitly specify a different permanent tablespace.

To specify a default permanent tablespace for the database:

- Include the `DEFAULT` `TABLESPACE` clause in the `CREATE` `DATABASE` statement

If you do not specify the `DEFAULT` `TABLESPACE` clause, then the `SYSTEM` tablespace is the default permanent tablespace for non- `SYSTEM` users.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF01204) for the syntax of the `DEFAULT TABLESPACE` clause of `CREATE DATABASE` and `ALTER DATABASE`

**Parent topic:** Specifying CREATE DATABASE Statement Clauses

#### Creating a Default Temporary Tablespace

When you create a default temporary tablespace, Oracle Database assigns it as the temporary tablespace for users who are not explicitly assigned a temporary tablespace.

To create a default temporary tablespace for the CDB:

- Include the `DEFAULT TEMPORARY TABLESPACE` clause in the `CREATE` `DATABASE` statement.

You can explicitly assign a temporary tablespace or tablespace group to a user in the `CREATE USER` statement. However, if you do not do so, and if no default temporary tablespace has been specified for the database, then by default these users are assigned the `SYSTEM` tablespace as their temporary tablespace. It is not good practice to store temporary data in the `SYSTEM` tablespace, and it is cumbersome to assign every user a temporary tablespace individually. Therefore, Oracle recommends that you use the `DEFAULT TEMPORARY TABLESPACE` clause of `CREATE DATABASE`.

Note:

When you specify a locally managed `SYSTEM` tablespace, the `SYSTEM` tablespace cannot be used as a temporary tablespace. In this case you must create a default temporary tablespace. This behavior is explained in " Creating a Locally Managed SYSTEM Tablespace ".

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF01204) for the syntax of the `DEFAULT TEMPORARY TABLESPACE` clause of `CREATE DATABASE` and `ALTER DATABASE`
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-6B941DE0-D109-4AD5-A13C-753AD37335DC) for information about creating and using temporary tablespaces

**Parent topic:** Specifying CREATE DATABASE Statement Clauses

#### Specifying Oracle Managed Files at Database Creation

You can minimize the number of clauses and parameters that you specify in your `CREATE DATABASE` statement by using the Oracle Managed Files feature.

- Specify either a directory or Oracle Automatic Storage Management (Oracle ASM) disk group in which your files are created and managed by Oracle Database.

By including any of the initialization parameters `DB_CREATE_FILE_DEST,` `DB_CREATE_ONLINE_LOG_DEST_n`, or `DB_RECOVERY_FILE_DEST` in your initialization parameter file, you instruct Oracle Database to create and manage the underlying operating system files of your database. Oracle Database will automatically create and manage the operating system files for the following database structures, depending on which initialization parameters you specify and how you specify clauses in your `CREATE DATABASE` statement:

- Tablespaces and their data files
- Temporary tablespaces and their temp files
- Control files
- Online redo log files
- Archived redo log files
- Flashback logs
- Block change tracking files
- RMAN backups

The following `CREATE DATABASE` statement shows briefly how the Oracle Managed Files feature works, assuming you have specified required initialization parameters:

```
CREATE DATABASE mynewdb
     USER SYS IDENTIFIED BY sys_password
     USER SYSTEM IDENTIFIED BY system_password
     EXTENT MANAGEMENT LOCAL
     UNDO TABLESPACE undotbs1
     DEFAULT TEMPORARY TABLESPACE tempts1
     DEFAULT TABLESPACE users
     ENABLE PLUGGABLE DATABASE
       SEED
       SYSTEM DATAFILES SIZE 125M AUTOEXTEND ON NEXT 10M MAXSIZE UNLIMITED
       SYSAUX DATAFILES SIZE 100M;
```
- The `SYSTEM` tablespace is created as a locally managed tablespace. Without the `EXTENT MANAGEMENT LOCAL` clause, the `SYSTEM` tablespace is created as dictionary managed, which is not recommended.
- No `DATAFILE` clause is specified, so the database creates an Oracle managed data file for the `SYSTEM` tablespace.
- No `LOGFILE` clauses are included, so the database creates two Oracle managed redo log file groups.
- No `SYSAUX DATAFILE` is included, so the database creates an Oracle managed data file for the `SYSAUX` tablespace.
- No `DATAFILE` subclause is specified for the `UNDO TABLESPACE` and `DEFAULT` `TABLESPACE` clauses, so the database creates an Oracle managed data file for each of these tablespaces.
- No `TEMPFILE` subclause is specified for the `DEFAULT TEMPORARY TABLESPACE` clause, so the database creates an Oracle managed temp file.
- If no `CONTROL_FILES` initialization parameter is specified in the initialization parameter file, then the database also creates an Oracle managed control file.
- If you are using a server parameter file, then the database automatically sets the appropriate initialization parameters.
	See Also:
	- " Specifying a Fast Recovery Area " for information about setting initialization parameters that create a Fast Recovery Area
	- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-4A3C4616-0D81-4BBA-8EAD-FCAA8AD5C15A) for information about the Oracle Managed Files feature and how to use it
	- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=OSTMG-GUID-BC612D35-5399-4A35-843E-CF76E3D3CDB5) for information about Automatic Storage Management

**Parent topic:** Specifying CREATE DATABASE Statement Clauses

#### Supporting Bigfile Tablespaces During Database Creation

Oracle Database simplifies management of tablespaces and enables support for extremely large databases by letting you create **bigfile tablespaces**.

Bigfile tablespaces can contain only one file, but that file can have up to 4G blocks. The maximum number of data files in an Oracle Database is limited (usually to 64K files). Therefore, bigfile tablespaces can significantly enhance the storage capacity of an Oracle Database.

This section discusses the clauses of the `CREATE DATABASE` statement that let you include support for bigfile tablespaces.

- Specifying the Default Tablespace Type  
	The `SET DEFAULT...TABLESPACE` clause of the `CREATE DATABASE` statement determines the default type of tablespace for this database in subsequent `CREATE TABLESPACE` statements.
- Overriding the Default Tablespace Type  
	The `SYSTEM` and `SYSAUX` tablespaces are always created with the default tablespace type. However, you optionally can explicitly override the default tablespace type for the `UNDO` and `DEFAULT TEMPORARY` tablespace during the `CREATE DATABASE` operation.

**Parent topic:** Specifying CREATE DATABASE Statement Clauses

##### Specifying the Default Tablespace Type

The `SET DEFAULT...TABLESPACE` clause of the `CREATE DATABASE` statement determines the default type of tablespace for this database in subsequent `CREATE TABLESPACE` statements.

- Specify either `SET DEFAULT BIGFILE TABLESPACE` or `SET DEFAULT SMALLFILE TABLESPACE`.

If you omit this clause, then the default is a **smallfile tablespace**, which is the traditional type of Oracle Database tablespace. A smallfile tablespace can contain up to 1022 files with up to 4M blocks each.

The use of bigfile tablespaces further enhances the Oracle Managed Files feature, because bigfile tablespaces make data files completely transparent for users. SQL syntax for the `ALTER TABLESPACE` statement has been extended to allow you to perform operations on tablespaces, rather than the underlying data files.

The `CREATE DATABASE` statement shown in " Specifying Oracle Managed Files at Database Creation " can be modified as follows to specify that the default type of tablespace is a bigfile tablespace:

```
CREATE DATABASE mynewdb
     USER SYS IDENTIFIED BY sys_password
     USER SYSTEM IDENTIFIED BY system_password
     SET DEFAULT BIGFILE TABLESPACE
     UNDO TABLESPACE undotbs1
     DEFAULT TEMPORARY TABLESPACE tempts1
     ENABLE PLUGGABLE DATABASE
        SEED
        SYSTEM DATAFILES SIZE 125M AUTOEXTEND ON NEXT 10M MAXSIZE UNLIMITED
        SYSAUX DATAFILES SIZE 100M;
```

To dynamically change the default tablespace type after database creation, use the `SET DEFAULT TABLESPACE` clause of the `ALTER DATABASE` statement:

```
ALTER DATABASE SET DEFAULT BIGFILE TABLESPACE;
```

You can determine the current default tablespace type for the database by querying the `DATABASE_PROPERTIES` data dictionary view as follows:

```
SELECT PROPERTY_VALUE FROM DATABASE_PROPERTIES 
   WHERE PROPERTY_NAME = 'DEFAULT_TBS_TYPE';
```

**Parent topic:** Supporting Bigfile Tablespaces During Database Creation

##### Overriding the Default Tablespace Type

The `SYSTEM` and `SYSAUX` tablespaces are always created with the default tablespace type. However, you optionally can explicitly override the default tablespace type for the `UNDO` and `DEFAULT TEMPORARY` tablespace during the `CREATE DATABASE` operation.

- Specify an `UNDO TABLESPACE` clause or a `DEFAULT TEMPORARY TABLESPACE` clause that overrides the default tablespace type.

For example, you can create a bigfile `UNDO` tablespace in a database with the default tablespace type of smallfile as follows:

```
CREATE DATABASE mynewdb
...
     BIGFILE UNDO TABLESPACE undotbs1
        DATAFILE '/u01/oracle/oradata/mynewdb/undotbs01.dbf'
        SIZE 200M REUSE AUTOEXTEND ON MAXSIZE UNLIMITED;
```

You can create a smallfile `DEFAULT` `TEMPORARY` tablespace in a database with the default tablespace type of bigfile as follows:

```
CREATE DATABASE mynewdb
   SET DEFAULT BIGFILE TABLESPACE
...
     SMALLFILE DEFAULT TEMPORARY TABLESPACE tempts1
        TEMPFILE '/u01/oracle/oradata/mynewdb/temp01.dbf' 
        SIZE 20M REUSE
...
```

**Parent topic:** Supporting Bigfile Tablespaces During Database Creation

#### Specifying the Database Time Zone and Time Zone File

Oracle Database datetime and interval data types and time zone support make it possible to store consistent information about the time of events and transactions.

- Setting the Database Time Zone  
	You can set the database time zone with the `SET TIME_ZONE` clause of the `CREATE DATABASE` statement.
- About the Database Time Zone Files  
	Two time zone files are included in a subdirectory of the Oracle home directory. The time zone files contain the valid time zone names.
- Specifying the Database Time Zone File  
	All databases that share information must use the same time zone data file.

**Parent topic:** Specifying CREATE DATABASE Statement Clauses

##### Setting the Database Time Zone

You can set the database time zone with the `SET TIME_ZONE` clause of the `CREATE DATABASE` statement.

- Set the database time zone when the database is created by using the `SET TIME_ZONE` clause of the `CREATE DATABASE` statement.

If you do not set the database time zone, then it defaults to the time zone of the host operating system.

You can change the database time zone for a session by using the `SET TIME_ZONE` clause of the `ALTER SESSION` statement.

See Also:

[Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=NLSPG262) for more information about setting the database time zone

**Parent topic:** Specifying the Database Time Zone and Time Zone File

##### About the Database Time Zone Files

Two time zone files are included in a subdirectory of the Oracle home directory. The time zone files contain the valid time zone names.

The following information is also included for each time zone:

- Offset from Coordinated Universal Time (UTC)
- Transition times for Daylight Saving Time
- Abbreviations for standard time and Daylight Saving Time

The default time zone file is ORACLE\_HOME/oracore/zoneinfo/timezlrg\_11.dat. A smaller time zone file with fewer time zones can be found in ORACLE\_HOME/oracore/zoneinfo/timezone\_11.dat.

To view the time zone names in the file being used by your database, use the following query:

```
SELECT * FROM V$TIMEZONE_NAMES;
```

See Also:

[Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=NLSPG004) for more information about managing and selecting time zone files

**Parent topic:** Specifying the Database Time Zone and Time Zone File

##### Specifying the Database Time Zone File

All databases that share information must use the same time zone data file.

The database server always uses the large time zone file by default.

To use the small time zone file on the client and know that all your data will refer only to regions in the small file:

- Set the `ORA_TZFILE` environment variable on the client to the full path name of the timezone `version`.dat file on the client, where `version` matches the time zone file version that is being used by the database server.

If you are already using the default larger time zone file on the client, then it is not practical to change to the smaller time zone file, because the database may contain data with time zones that are not part of the smaller file.

**Parent topic:** Specifying the Database Time Zone and Time Zone File

#### Specifying FORCE LOGGING Mode

Some data definition language statements (such as `CREATE` `TABLE`) allow the `NOLOGGING` clause, which causes some database operations not to generate redo records in the database redo log. The `NOLOGGING` setting can speed up operations that can be easily recovered outside of the database recovery mechanisms, but it can negatively affect media recovery and standby databases.

Oracle Database lets you force the writing of redo records even when `NOLOGGING` has been specified in DDL statements. The database never generates redo records for temporary tablespaces and temporary segments, so forced logging has no affect for objects.

- Using the FORCE LOGGING Clause  
	You can force the writing of redo records even when `NOLOGGING` is specified in DDL statements.
- Performance Considerations of FORCE LOGGING Mode  
	`FORCE LOGGING` mode results in some performance degradation.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF30009) for information about operations that can be done in `NOLOGGING` mode

**Parent topic:** Specifying CREATE DATABASE Statement Clauses

##### Using the FORCE LOGGING Clause

You can force the writing of redo records even when `NOLOGGING` is specified in DDL statements.

To put the database into `FORCE LOGGING` mode:

- Include the `FORCE LOGGING` clause in the `CREATE DATABASE` statement.

If you do not specify this clause, then the database is not placed into `FORCE LOGGING` mode.

Use the `ALTER DATABASE` statement to place the database into `FORCE LOGGING` mode after database creation. This statement can take a considerable time for completion, because it waits for all unlogged direct writes to complete.

You can cancel `FORCE LOGGING` mode using the following SQL statement:

```
ALTER DATABASE NO FORCE LOGGING;
```

Independent of specifying `FORCE LOGGING` for the database, you can selectively specify `FORCE LOGGING` or `NO FORCE LOGGING` at the tablespace level. However, if `FORCE LOGGING` mode is in effect for the database, it takes precedence over the tablespace setting. If it is not in effect for the database, then the individual tablespace settings are enforced. Oracle recommends that either the entire database is placed into `FORCE LOGGING` mode, or individual tablespaces be placed into `FORCE LOGGING` mode, but not both.

The `FORCE LOGGING` mode is a persistent attribute of the database. That is, if the database is shut down and restarted, it remains in the same logging mode. However, if you re-create the control file, the database is not restarted in the `FORCE LOGGING` mode unless you specify the `FORCE LOGGING` clause in the `CREATE CONTROL FILE` statement.

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-A1939693-60AC-4009-B37C-A1D8D1360D49) for information about using the `FORCE LOGGING` clause for tablespace creation.

**Parent topic:** Specifying FORCE LOGGING Mode

##### Performance Considerations of FORCE LOGGING Mode

`FORCE LOGGING` mode results in some performance degradation.

If the primary reason for specifying `FORCE LOGGING` is to ensure complete media recovery, and there is no standby database active, then consider the following:

- How many media failures are likely to happen?
- How serious is the damage if unlogged direct writes cannot be recovered?
- Is the performance degradation caused by forced logging tolerable?

If the database is running in `NOARCHIVELOG` mode, then generally there is no benefit to placing the database in `FORCE LOGGING` mode. Media recovery is not possible in `NOARCHIVELOG` mode, so if you combine it with `FORCE LOGGING`, the result may be performance degradation with little benefit.

Starting with Oracle Database 18c, the following two new nologging clauses are introduced, which enable non-logged operations to be carried out and have Active Data Guard standby databases receive all the data, thus preventing performance degradation caused by large redo log generation by the `FORCE LOGGING` mode:

- `STANDBY NOLOGGING FOR DATA AVAILABILITY`
- `STANDBY NOLOGGING FOR LOAD PERFORMANCE`

See Also:

[Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SBYDB-GUID-AE2B1237-57A1-4745-A04C-4246A831A963) for more information about these `STANDBY NOLOGGING` clauses

**Parent topic:** Specifying FORCE LOGGING Mode

### Specifying Initialization Parameters

You can add or edit basic initialization parameters before you create your new database.

- About Initialization Parameters and Initialization Parameter Files  
	When an Oracle instance starts, it reads initialization parameters from an initialization parameter file. This file must at a minimum specify the `DB_NAME` parameter. All other parameters have default values.
- Determining the Global Database Name  
	The global database name consists of the user-specified local database name and the location of the database within a network structure.
- Specifying a Fast Recovery Area  
	The Fast Recovery Area is a location in which Oracle Database can store and manage files related to backup and recovery. It is distinct from the database area, which is a location for the current database files (data files, control files, and online redo logs).
- Specifying Control Files  
	Every database has a control file, which contains entries that describe the structure of the database (such as its name, the timestamp of its creation, and the names and locations of its data files and redo files). The `CONTROL_FILES` initialization parameter specifies one or more names of control files, separated by commas.
- Specifying Database Block Sizes  
	The `DB_BLOCK_SIZE` initialization parameter specifies the standard block size for the database.
- Specifying the Maximum Number of Processes  
	The `PROCESSES` initialization parameter determines the maximum number of operating system processes that can be connected to Oracle Database concurrently.
- Specifying the DDL Lock Timeout  
	You can specify the amount of time that blocking DDL statements wait for locks.
- Specifying the Method of Undo Space Management  
	Every Oracle Database must have a method of maintaining information that is used to undo changes to the database. Such information consists of records of the actions of transactions, primarily before they are committed. Collectively these records are called **undo data**.
- Specifying the Database Compatibility Level  
	The `COMPATIBLE` initialization parameter controls the database compatibility level.
- Setting the License Parameter  
	If you use named user licensing, Oracle Database can help you enforce this form of licensing. You can set a limit on the number of users created in the database. Once this limit is reached, you cannot create more users.

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-BEABE53D-8058-4834-B99B-5C80A8AD5B06) for a discussion of the initialization parameters that pertain to memory management
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=REFRN001) for descriptions of all initialization parameters including their default settings

**Parent topic:** Creating a CDB: Advanced Topics

#### About Initialization Parameters and Initialization Parameter Files

When an Oracle instance starts, it reads initialization parameters from an initialization parameter file. This file must at a minimum specify the `DB_NAME` parameter. All other parameters have default values.

The initialization parameter file can be either a read-only text file, a `PFILE`, or a read/write binary file.

The binary file is called a **server parameter file**. A server parameter file enables you to change initialization parameters with `ALTER SYSTEM` commands and to persist the changes across a shutdown and startup. It also provides a basis for self-tuning by Oracle Database. For these reasons, it is recommended that you use a server parameter file. You can create one manually from your edited text initialization file, or automatically by using Database Configuration Assistant (DBCA) to create your database.

Before you manually create a server parameter file, you can start an instance with a text initialization parameter file. Upon startup, the Oracle instance first searches for a server parameter file in a default location, and if it does not find one, searches for a text initialization parameter file. You can also override an existing server parameter file by naming a text initialization parameter file as an argument of the `STARTUP` command.

Default file names and locations for the text initialization parameter file are shown in the following table:

| Platform | Default Name | Default Location |
| --- | --- | --- |
| UNIX and Linux | `init` `ORACLE_SID`.`ora`  For example, the initialization parameter file for the `mynewdb` database is named:  `initmynewdb.ora` | ORACLE\_HOME/ `dbs` |
| Windows | `init` `ORACLE_SID``.ora ` | ORACLE\_HOME\\ `database` |

If you are creating an Oracle database for the first time, Oracle suggests that you minimize the number of parameter values that you alter. As you become more familiar with your database and environment, you can dynamically tune many initialization parameters using the `ALTER SYSTEM` statement. If you are using a text initialization parameter file, then your changes are effective only for the current instance. To make them permanent, you must update them manually in the initialization parameter file, or they will be lost over the next shutdown and startup of the database. If you are using a server parameter file, then initialization parameter file changes made by the `ALTER SYSTEM` statement can persist across shutdown and startup.

See Also:

- " Determining the Global Database Name " for information about the `DB_NAME` parameter
- " Managing Initialization Parameters Using a Server Parameter File "
- " [About Initialization Parameter Files and Startup](administering-a-cdb-with-sql-plus.md) "

**Parent topic:** Specifying Initialization Parameters

##### Sample Initialization Parameter File

Oracle Database provides generally appropriate values in a sample text initialization parameter file. You can edit these Oracle-supplied initialization parameters and add others, depending upon your configuration and options and how you plan to tune the database.

The sample text initialization parameter file is named `init.ora` and is found in the following location on most platforms:

```
ORACLE_HOME/dbs
```

The following is the content of the sample file:

```
##############################################################################
# Example INIT.ORA file
#
# This file is provided by Oracle Corporation to help you start by providing
# a starting point to customize your RDBMS installation for your site. 
# 
# NOTE: The values that are used in this file are only intended to be used
# as a starting point. You may want to adjust/tune those values to your
# specific hardware and needs. You may also consider using Database
# Configuration Assistant tool (DBCA) to create INIT file and to size your
# initial set of tablespaces based on the user input.
###############################################################################
 
# Change '<ORACLE_BASE>' to point to the oracle base (the one you specify at
# install time)
 
db_name='ORCL'
memory_target=1G
processes = 150
db_block_size=8192
db_domain=''
db_recovery_file_dest='<ORACLE_BASE>/flash_recovery_area'
db_recovery_file_dest_size=2G
diagnostic_dest='<ORACLE_BASE>'
dispatchers='(PROTOCOL=TCP) (SERVICE=ORCLXDB)'
open_cursors=300 
remote_login_passwordfile='EXCLUSIVE'
undo_tablespace='UNDOTBS1'
# You may want to ensure that control files are created on separate physical
# devices
control_files = (ora_control1, ora_control2)
compatible ='12.0.0'
enable_pluggable_database=TRUE
```

**Parent topic:** About Initialization Parameters and Initialization Parameter Files

##### Text Initialization Parameter File Format

The text initialization parameter file specifies the values of parameters in name/value pairs.

The text initialization parameter file (PFILE) must contain name/value pairs in one of the following forms:

- For parameters that accept only a single value:
	```
	parameter_name=value
	```
- For parameters that accept one or more values (such as the `CONTROL_FILES` parameter):
	```
	parameter_name=(value[,value] ...)
	```

Parameter values of type string must be enclosed in single quotes ('). Case (upper or lower) in file names is significant only if case is significant on the host operating system.

For parameters that accept multiple values, to enable you to easily copy and paste name/value pairs from the alert log, you can repeat a parameter on multiple lines, where each line contains a different value.

```
control_files='/u01/app/oracle/oradata/orcl/control01.ctl'
control_files='/u01/app/oracle/oradata/orcl/control02.ctl'
control_files='/u01/app/oracle/oradata/orcl/control03.ctl'
```

If you repeat a parameter that does not accept multiple values, then only the last value specified takes effect.

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-39CD6AD3-58D6-44E6-8A6C-0165252674D7) to learn about the alert log
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=REFRN-GUID-6CCB7791-F995-474C-9339-8A3EE2C6777B) for more information about the content and syntax of the text initialization parameter file

**Parent topic:** About Initialization Parameters and Initialization Parameter Files

##### Expressions in Initialization Parameter Settings

Set the value of an initialization parameter to the desired numeric value, text value, or expression.

Starting with Oracle Database Release 21c, you can use expressions when setting the value of initialization parameters. The expressions can contain other initialization parameters and one or more of the following:

- arithmetic operators (+, -, \*, /)
- environment variables
- `MIN` or `MAX` function

Examples:

```
SGA_TARGET = SYSTEM_MEMORY * 0.4
PARALLEL_MAX_SERVERS = MAX(100, PROCESSES * 0.4)
DB_CREATE_FILE_DEST=$ORACLE_HOME/oracle/database_files
```

**Parent topic:** About Initialization Parameters and Initialization Parameter Files

#### Determining the Global Database Name

The global database name consists of the user-specified local database name and the location of the database within a network structure.

- Set the `DB_NAME` and `DB_DOMAIN` initialization parameters.

The `DB_NAME` initialization parameter determines the local name component of the database name, and the `DB_DOMAIN` parameter, which is optional, indicates the domain (logical location) within a network structure. The combination of the settings for these two parameters must form a database name that is unique within a network.

For example, to create a database with a global database name of `test.us.example.com`, edit the parameters of the new parameter file as follows:

```
DB_NAME = test
DB_DOMAIN = us.example.com
```

You can rename the `GLOBAL_NAME` of your database using the `ALTER DATABASE RENAME GLOBAL_NAME` statement. However, you must also shut down and restart the database after first changing the `DB_NAME` and `DB_DOMAIN` initialization parameters and recreating the control files. Recreating the control files is easily accomplished with the command `ALTER` `DATABASE` `BACKUP` `CONTROLFILE` `TO` `TRACE`. See [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=BRADV90011) for more information.

- DB\_NAME Initialization Parameter  
	The `DB_NAME` initialization parameter specifies a database identifier.
- DB\_DOMAIN Initialization Parameter  
	In a distributed database system, the `DB_DOMAIN` initialization parameter specifies the logical location of the database within the network structure.

See Also:

[Oracle Database Utilities](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SUTIL014) for information about using the `DBNEWID` utility, which is another means of changing a database name

**Parent topic:** Specifying Initialization Parameters

##### DB\_NAME Initialization Parameter

The `DB_NAME` initialization parameter specifies a database identifier.

`DB_NAME` must be set to a text string of no more than 8 characters. The database name must start with an alphabetic character. During database creation, the name provided for `DB_NAME` is recorded in the data files, redo log files, and control file of the database. If during database instance startup the value of the `DB_NAME` parameter (in the parameter file) and the database name in the control file are different, then the database does not start.

**Parent topic:** Determining the Global Database Name

##### DB\_DOMAIN Initialization Parameter

In a distributed database system, the `DB_DOMAIN` initialization parameter specifies the logical location of the database within the network structure.

`DB_DOMAIN` is a text string that specifies the network domain where the database is created. If the database you are about to create will ever be part of a distributed database system, then give special attention to this initialization parameter before database creation. This parameter is optional.

**Parent topic:** Determining the Global Database Name

#### Specifying a Fast Recovery Area

The Fast Recovery Area is a location in which Oracle Database can store and manage files related to backup and recovery. It is distinct from the database area, which is a location for the current database files (data files, control files, and online redo logs).

Specify the Fast Recovery Area with the following initialization parameters:

- `DB_RECOVERY_FILE_DEST`: Location of the Fast Recovery Area. This can be a directory, file system, or Automatic Storage Management (Oracle ASM) disk group.
	In an Oracle Real Application Clusters (Oracle RAC) environment, this location must be on a cluster file system, Oracle ASM disk group, or a shared directory configured through NFS.
- `DB_RECOVERY_FILE_DEST_SIZE`: Specifies the maximum total bytes to be used by the Fast Recovery Area. This initialization parameter must be specified before `DB_RECOVERY_FILE_DEST` is enabled.

In an Oracle RAC environment, the settings for these two parameters must be the same on all instances.

You cannot enable these parameters if you have set values for the `LOG_ARCHIVE_DEST` and `LOG_ARCHIVE_DUPLEX_DEST` parameters. You must disable those parameters before setting up the Fast Recovery Area. You can instead set values for the `LOG_ARCHIVE_DEST_` `n` parameters.

Oracle recommends using a Fast Recovery Area, because it can simplify backup and recovery operations for your database.

See Also:

[Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=BRADV8183) to learn how to create and use a Fast Recovery Area

**Parent topic:** Specifying Initialization Parameters

#### Specifying Control Files

Every database has a control file, which contains entries that describe the structure of the database (such as its name, the timestamp of its creation, and the names and locations of its data files and redo files). The `CONTROL_FILES` initialization parameter specifies one or more names of control files, separated by commas.

- Set the `CONTROL_FILES` initialization parameter.

When you execute the `CREATE DATABASE` statement, the control files listed in the `CONTROL_FILES` parameter are created.

If you do not include `CONTROL_FILES` in the initialization parameter file, then Oracle Database creates a control file in the same directory as the initialization parameter file, using a default operating system–dependent file name. If you have enabled Oracle Managed Files, the database creates Oracle managed control files.

If you want the database to create new operating system files when creating database control files, the file names listed in the `CONTROL_FILES` parameter must not match any file names that currently exist on your system. If you want the database to reuse or overwrite existing files when creating database control files, ensure that the file names listed in the `CONTROL_FILES` parameter match the file names that are to be reused, and include a `CONTROLFILE REUSE` clause in the `CREATE DATABASE` statement.

Oracle strongly recommends you use at least two control files stored on separate physical disk drives for each database.

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-5F6F9382-6921-4992-9789-E63B18E99C5F)
- " Specifying Oracle Managed Files at Database Creation "

**Parent topic:** Specifying Initialization Parameters

#### Specifying Database Block Sizes

The `DB_BLOCK_SIZE` initialization parameter specifies the standard block size for the database.

- Set the `DB_BLOCK_SIZE` initialization parameter.

This block size is used for the `SYSTEM` tablespace and by default in other tablespaces. Oracle Database can support up to four additional nonstandard block sizes.

- DB\_BLOCK\_SIZE Initialization Parameter  
	The most commonly used block size should be picked as the standard block size. In many cases, this is the only block size that you must specify.
- Nonstandard Block Sizes  
	You can create tablespaces of nonstandard block sizes.

**Parent topic:** Specifying Initialization Parameters

##### DB\_BLOCK\_SIZE Initialization Parameter

The most commonly used block size should be picked as the standard block size. In many cases, this is the only block size that you must specify.

- Set the `DB_BLOCK_SIZE` initialization parameter.

Typically, `DB_BLOCK_SIZE` is set to either 4K or 8K. If you do not set a value for this parameter, then the default data block size is operating system specific, which is generally adequate.

You cannot change the block size after database creation except by re-creating the database. If the database block size is different from the operating system block size, then ensure that the database block size is a multiple of the operating system block size. For example, if your operating system block size is 2K (2048 bytes), the following setting for the `DB_BLOCK_SIZE` initialization parameter is valid:

```
DB_BLOCK_SIZE=4096
```

A larger data block size provides greater efficiency in disk and memory I/O (access and storage of data). Therefore, consider specifying a block size larger than your operating system block size if the following conditions exist:

- Oracle Database is on a large computer system with a large amount of memory and fast disk drives. For example, databases controlled by mainframe computers with vast hardware resources typically use a data block size of 4K or greater.
- The operating system that runs Oracle Database uses a small operating system block size. For example, if the operating system block size is 1K and the default data block size matches this, the database may be performing an excessive amount of disk I/O during normal operation. For best performance in this case, a database block should consist of multiple operating system blocks.
	See Also:
	Your operating system specific Oracle documentation for details about the default block size.

**Parent topic:** Specifying Database Block Sizes

##### Nonstandard Block Sizes

You can create tablespaces of nonstandard block sizes.

To create tablespaces of nonstandard block sizes:

- Specify the `BLOCKSIZE` clause in a `CREATE TABLESPACE` statement.

These nonstandard block sizes can have any of the following power-of-two values: 2K, 4K, 8K, 16K or 32K. Platform-specific restrictions regarding the maximum block size apply, so some of these sizes may not be allowed on some platforms.

To use nonstandard block sizes, you must configure subcaches within the buffer cache area of the SGA memory for all of the nonstandard block sizes that you intend to use. The initialization parameters used for configuring these subcaches are described in [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-3CEA1AB5-4850-4064-9823-F62C500A579F).

The ability to specify multiple block sizes for your database is especially useful if you are transporting tablespaces between databases. You can, for example, transport a tablespace that uses a 4K block size from an OLTP environment to a data warehouse environment that uses a standard block size of 8K.

Note:

A 32K block size is valid only on 64-bit platforms.

Caution:

Oracle recommends against specifying a 2K block size when 4K sector size disks are in use, because performance degradation can occur. For an explanation, see [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-AC858C69-317E-4193-838D-59F8DDEA1927).

**Parent topic:** Specifying Database Block Sizes

#### Specifying the Maximum Number of Processes

The `PROCESSES` initialization parameter determines the maximum number of operating system processes that can be connected to Oracle Database concurrently.

- Set the `PROCESSES` initialization parameter.

The value of this parameter must be a minimum of one for each background process plus one for each user process. The number of background processes will vary according the database features that you are using. For example, if you are using Advanced Queuing or the file mapping feature, then you will have additional background processes. If you are using Automatic Storage Management, then add three additional processes for the database instance.

If you plan on running 50 user processes, a good estimate would be to set the `PROCESSES` initialization parameter to 70.

**Parent topic:** Specifying Initialization Parameters

#### Specifying the DDL Lock Timeout

You can specify the amount of time that blocking DDL statements wait for locks.

A data definition language (DDL) statement is either nonblocking or blocking, and both types of DDL statements require exclusive locks on internal structures. If these locks are unavailable when a DDL statement runs, then nonblocking and blocking DDL statements behave differently:

- Nonblocking DDL waits until every concurrent DML transaction that references the object affected by the DDL either commits or rolls back.
- Blocking DDL fails, though it might have succeeded if it had been executed subseconds later when the locks become available.

To enable blocking DDL statements to wait for locks, specify a DDL lock timeout—the number of seconds a DDL command waits for its required locks before failing.

- To specify a DDL lock timeout, set the `DDL_LOCK_TIMEOUT` parameter.

The permissible range of values for `DDL_LOCK_TIMEOUT` is 0 to 1,000,000. The default is 0. You can set `DDL_LOCK_TIMEOUT` at the system level, or at the session level with an `ALTER` `SESSION` statement.

Note:

The `DDL_LOCK_TIMEOUT` parameter does not affect nonblocking DDL statements.

#### Specifying the Method of Undo Space Management

Every Oracle Database must have a method of maintaining information that is used to undo changes to the database. Such information consists of records of the actions of transactions, primarily before they are committed. Collectively these records are called **undo data**.

To set up an environment for automatic undo management using an undo tablespace.

- Set the `UNDO_MANAGEMENT` initialization parameter to `AUTO`, which is the default.

- UNDO\_MANAGEMENT Initialization Parameter  
	The `UNDO_MANAGEMENT` initialization parameter determines whether an instance starts in automatic undo management mode, which stores undo in an undo tablespace. Set this parameter to `AUTO` to enable automatic undo management mode. `AUTO` is the default if the parameter is omitted or is null.
- UNDO\_TABLESPACE Initialization Parameter  
	The `UNDO_TABLESPACE` initialization parameter enables you to override that default undo tablespace for an instance.

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-2C865CF9-A8B5-4BF1-A451-E8C08D3611F0)

**Parent topic:** Specifying Initialization Parameters

##### UNDO\_MANAGEMENT Initialization Parameter

The `UNDO_MANAGEMENT` initialization parameter determines whether an instance starts in automatic undo management mode, which stores undo in an undo tablespace. Set this parameter to `AUTO` to enable automatic undo management mode. `AUTO` is the default if the parameter is omitted or is null.

**Parent topic:** Specifying the Method of Undo Space Management

##### UNDO\_TABLESPACE Initialization Parameter

The `UNDO_TABLESPACE` initialization parameter enables you to override that default undo tablespace for an instance.

When an instance starts up in automatic undo management mode, it attempts to select an undo tablespace for storage of undo data. If the database was created in automatic undo management mode, then the default undo tablespace (either the system-created `SYS_UNDOTBS` tablespace or the user-specified undo tablespace) is the undo tablespace used at instance startup. You can override this default for the instance by specifying a value for the `UNDO_TABLESPACE` initialization parameter. This parameter is especially useful for assigning a particular undo tablespace to an instance in an Oracle Real Application Clusters environment.

If no undo tablespace is specified by the `UNDO_TABLESPACE` initialization parameter, then the first available undo tablespace in the database is chosen. If no undo tablespace is available, then the instance starts without an undo tablespace, and undo data is written to the `SYSTEM` tablespace. You should avoid running in this mode.

Note:

When using the `CREATE` `DATABASE` statement to create a database, do not include an `UNDO_TABLESPACE` parameter in the initialization parameter file. Instead, include an `UNDO` `TABLESPACE` clause in the `CREATE` `DATABASE` statement.

**Parent topic:** Specifying the Method of Undo Space Management

#### Specifying the Database Compatibility Level

The `COMPATIBLE` initialization parameter controls the database compatibility level.

- Set the `COMPATIBLE` initialization parameter to a release number.

- About the COMPATIBLE Initialization Parameter  
	The `COMPATIBLE` initialization parameter enables or disables the use of features in the database that affect file format on disk. For example, if you create an Oracle Database 19c database, but specify `COMPATIBLE=12.0.0` in the initialization parameter file, then features that require Oracle Database 19c compatibility generate an error if you try to use them. Such a database is said to be at the 12.0.0 compatibility level.

**Parent topic:** Specifying Initialization Parameters

##### About the COMPATIBLE Initialization Parameter

The `COMPATIBLE` initialization parameter enables or disables the use of features in the database that affect file format on disk. For example, if you create an Oracle Database 19c database, but specify `COMPATIBLE=12.0.0` in the initialization parameter file, then features that require Oracle Database 19c compatibility generate an error if you try to use them. Such a database is said to be at the 12.0.0 compatibility level.

You can advance the compatibility level of your database by changing the `COMPATIBLE` initialization parameter. If you do, then there is no way to start the database using a lower compatibility level setting, except by doing a point-in-time recovery to a time before the compatibility was advanced.

The default value for the `COMPATIBLE` parameter is the release number of the most recent major release.

Note:

- When you set this parameter in a server parameter file (SPFILE) using the `ALTER SYSTEM` statement, you must specify `SCOPE=SPFILE`, and you must restart the database for the change to take effect.
- The `COMPATIBLE` initialization parameter must be specified as at least three decimal numbers separated by a dot, such as `19.0.0`.

See Also:

- [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=UPGRD12473) for a detailed discussion of database compatibility and the `COMPATIBLE` initialization parameter
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=REFRN10019)
- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=BRADV80055) for information about point-in-time recovery of your database

**Parent topic:** Specifying the Database Compatibility Level

#### Setting the License Parameter

If you use named user licensing, Oracle Database can help you enforce this form of licensing. You can set a limit on the number of users created in the database. Once this limit is reached, you cannot create more users.

Note:

This mechanism assumes that each person accessing the database has a unique user name and that no people share a user name. Therefore, so that named user licensing can help you ensure compliance with your Oracle license agreement, do not allow multiple users to log in using the same user name.

To limit the number of users created in a database, set the `LICENSE_MAX_USERS` initialization parameter in the database initialization parameter file.

The following example sets the `LICENSE_MAX_USERS` initialization parameter:

```
LICENSE_MAX_USERS = 200
```

Note:

Oracle no longer offers licensing by the number of concurrent sessions. Therefore the `LICENSE_MAX_SESSIONS` and `LICENSE_SESSIONS_WARNING` initialization parameters are no longer needed and have been deprecated.

**Parent topic:** Specifying Initialization Parameters

### Managing Initialization Parameters Using a Server Parameter File

Initialization parameters for the Oracle Database have traditionally been stored in a text initialization parameter file. For better manageability, you can choose to maintain initialization parameters in a binary server parameter file that is persistent across database startup and shutdown.

- What Is a Server Parameter File?  
	A server parameter file can be thought of as a repository for initialization parameters that is maintained on the system running the Oracle Database server. It is, by design, a server-side initialization parameter file.
- Migrating to a Server Parameter File  
	If you are currently using a text initialization parameter file, then you can migrate to a server parameter file.
- Server Parameter File Default Names and Locations  
	Oracle recommends that you allow the database to give the SPFILE the default name and store it in the default location. This eases administration of your database. For example, the `STARTUP` command assumes this default location to read the SPFILE.
- Creating a Server Parameter File  
	You use the `CREATE SPFILE` statement to create a server parameter file. You must have the `SYSDBA`, `SYSOPER`, or `SYSBACKUP` administrative privilege to execute this statement.
- The SPFILE Initialization Parameter  
	The `SPFILE` initialization parameter contains the name of the current server parameter file.
- Changing Initialization Parameter Values  
	You can change initialization parameter values to affect the operation of a database instance.
- Clearing Initialization Parameter Values  
	You can use the `ALTER SYSTEM RESET` statement to clear an initialization parameter value. When you do so, the initialization parameter value is changed to its default value or its startup value.
- Exporting the Server Parameter File  
	You can use the `CREATE PFILE` statement to export a server parameter file (SPFILE) to a text initialization parameter file.
- Backing Up the Server Parameter File  
	You can create a backup of your server parameter file (SPFILE) by exporting it. If the backup and recovery strategy for your database is implemented using Recovery Manager (RMAN), then you can use RMAN to create a backup of the SPFILE. The SPFILE is backed up automatically by RMAN when you back up your database, but RMAN also enables you to specifically create a backup of the currently active SPFILE.
- Recovering a Lost or Damaged Server Parameter File  
	You can recover the server parameter file (SPFILE). If your server parameter file (SPFILE) becomes lost or corrupted, then the current instance may fail, or the next attempt at starting the database instance may fail.
- Methods for Viewing Parameter Settings  
	You can view parameter settings using several different methods.

**Parent topic:** Creating a CDB: Advanced Topics

#### What Is a Server Parameter File?

A server parameter file can be thought of as a repository for initialization parameters that is maintained on the system running the Oracle Database server. It is, by design, a server-side initialization parameter file.

Initialization parameters stored in a server parameter file are persistent, in that any changes made to the parameters while an instance is running can persist across instance shutdown and startup. This arrangement eliminates the need to manually update initialization parameters to make persistent any changes effected by `ALTER SYSTEM` statements. It also provides a basis for self-tuning by the Oracle Database server.

A server parameter file is initially built from a text initialization parameter file using the `CREATE SPFILE` statement. (It can also be created directly by the Database Configuration Assistant.) The server parameter file is a binary file that cannot be edited using a text editor. Oracle Database provides other interfaces for viewing and modifying parameter settings in a server parameter file.

Note:

Although you can open the binary server parameter file with a text editor and view its text, do not manually edit it. Doing so will corrupt the file. You will not be able to start your instance, and if the instance is running, it could fail.

When you issue a `STARTUP` command with no `PFILE` clause, the Oracle instance searches an operating system–specific default location for a server parameter file from which to read initialization parameter settings. If no server parameter file is found, the instance searches for a text initialization parameter file. If a server parameter file exists but you want to override it with settings in a text initialization parameter file, you must specify the `PFILE` clause when issuing the `STARTUP` command.

See Also:

" [Starting Up a CDB](administering-a-cdb-with-sql-plus.md) "

**Parent topic:** Managing Initialization Parameters Using a Server Parameter File

#### Migrating to a Server Parameter File

If you are currently using a text initialization parameter file, then you can migrate to a server parameter file.

To migrate to a server parameter file:

1. If the initialization parameter file is located on a client system, then transfer the file (for example, FTP) from the client system to the server system.
	Note:
	If you are migrating to a server parameter file in an Oracle Real Application Clusters environment, you must combine all of your instance-specific initialization parameter files into a single initialization parameter file. Instructions for doing this and other actions unique to using a server parameter file for instances that are part of an Oracle Real Application Clusters installation are discussed in [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=RACAD020) and in your platform-specific Oracle Real Application Clusters Installation Guide.
2. Create a server parameter file in the default location using the `CREATE SPFILE FROM PFILE` statement. See " Creating a Server Parameter File " for instructions.
	This statement reads the text initialization parameter file to create a server parameter file. The database does not have to be started to issue a `CREATE SPFILE` statement.
3. Start up or restart the instance.
	The instance finds the new SPFILE in the default location and starts up with it.

**Parent topic:** Managing Initialization Parameters Using a Server Parameter File

#### Server Parameter File Default Names and Locations

Oracle recommends that you allow the database to give the SPFILE the default name and store it in the default location. This eases administration of your database. For example, the `STARTUP` command assumes this default location to read the SPFILE.

The following table shows the default name and location for both the text initialization parameter file (PFILE) and server parameter file (SPFILE) for the UNIX, Linux, and Windows platforms, both with and without the presence of Oracle Automatic Storage Management (Oracle ASM). The table assumes that the SPFILE is a file.

Table 4-1 PFILE and SPFILE Default Names and Locations on UNIX, Linux, and Windows

| Platform | PFILE Default Name | SPFILE Default Name | PFILE Default Location | SPFILE Default Location |
| --- | --- | --- | --- | --- |
| UNIX and Linux | `init` `ORACLE_SID``.ora` | `spfile` `ORACLE_SID``.ora` | Oracle\_Home `/dbs` or the same location as the data files | Without Oracle ASM:  Oracle\_Home `/dbs` or the same location as the data files  When Oracle ASM is present:  In the same disk group as the data files (assuming the database was created with DBCA) |
| Windows | `init` `ORACLE_SID``.ora` | `spfile` `ORACLE_SID``.ora` | Oracle\_Home `\database` | Without Oracle ASM:  OH `\database`  When Oracle ASM is present:  In the same disk group as the data files (assuming the database was created with DBCA) |

Note:

Upon startup, the instance first searches for an SPFILE named `spfile` `ORACLE_SID`.`ora`, and if not found, searches for `spfile.ora`. Using `spfile.ora` enables all Real Application Cluster (Oracle RAC) instances to use the same server parameter file.

If neither SPFILE is found, the instance searches for the text initialization parameter file `init` `ORACLE_SID`.`ora`.

If you create an SPFILE in a location other than the default location, you must create in the default PFILE location a "stub" PFILE that points to the server parameter file. For more information, see " [Starting Up a Database](administering-a-cdb-with-sql-plus.md) ".

When you create the database with DBCA when Oracle ASM is present, DBCA places the SPFILE in an Oracle ASM disk group, and also causes this stub PFILE to be created.

**Parent topic:** Managing Initialization Parameters Using a Server Parameter File

#### Creating a Server Parameter File

You use the `CREATE SPFILE` statement to create a server parameter file. You must have the `SYSDBA`, `SYSOPER`, or `SYSBACKUP` administrative privilege to execute this statement.

To create a server parameter file:

- Run the `CREATE SPFILE` statement.

Note:

When you use the Database Configuration Assistant to create a database, it automatically creates a server parameter file for you.

The `CREATE SPFILE` statement can be executed before or after instance startup. However, if the instance has been started using a server parameter file, an error is raised if you attempt to re-create the same server parameter file that is currently being used by the instance.

You can create a server parameter file (SPFILE) from an existing text initialization parameter file or from memory. Creating the SPFILE from memory means copying the current values of initialization parameters in the running instance to the SPFILE.

The following example creates a server parameter file from text initialization parameter file `/u01/oracle/dbs/init.ora`. In this example no `SPFILE` name is specified, so the file is created with the platform-specific default name and location shown in Table 4-1.

```
CREATE SPFILE FROM PFILE='/u01/oracle/dbs/init.ora';
```

The next example illustrates creating a server parameter file and supplying a name and location.

```
CREATE SPFILE='/u01/oracle/dbs/test_spfile.ora'
       FROM PFILE='/u01/oracle/dbs/test_init.ora';
```

The next example illustrates creating a server parameter file in the default location from the current values of the initialization parameters in memory.

```
CREATE SPFILE FROM MEMORY;
```

Whether you use the default SPFILE name and default location or specify an SPFILE name and location, if an SPFILE of the same name already exists in the location, it is overwritten without a warning message.

When you create an SPFILE from a text initialization parameter file, comments specified on the same lines as a parameter setting in the initialization parameter file are maintained in the SPFILE. All other comments are ignored.

**Parent topic:** Managing Initialization Parameters Using a Server Parameter File

#### The SPFILE Initialization Parameter

The `SPFILE` initialization parameter contains the name of the current server parameter file.

When the default server parameter file is used by the database—that is, you issue a `STARTUP` command and do not specify a `PFILE` parameter—the value of `SPFILE` is internally set by the server. The SQL\*Plus command `SHOW PARAMETERS SPFILE` (or any other method of querying the value of a parameter) displays the name of the server parameter file that is currently in use.

**Parent topic:** Managing Initialization Parameters Using a Server Parameter File

#### Changing Initialization Parameter Values

You can change initialization parameter values to affect the operation of a database instance.

- About Changing Initialization Parameter Values  
	The `ALTER SYSTEM` statement enables you to set, change, or restore to default the values of initialization parameters. If you are using a text initialization parameter file, the `ALTER SYSTEM` statement changes the value of a parameter only for the current instance, because there is no mechanism for automatically updating text initialization parameters on disk. You must update them manually to be passed to a future instance. Using a server parameter file overcomes this limitation.
- Setting or Changing Initialization Parameter Values  
	With a server parameter file, use the `SET` clause of the `ALTER SYSTEM` statement to set or change initialization parameter values.

**Parent topic:** Managing Initialization Parameters Using a Server Parameter File

##### About Changing Initialization Parameter Values

The `ALTER SYSTEM` statement enables you to set, change, or restore to default the values of initialization parameters. If you are using a text initialization parameter file, the `ALTER SYSTEM` statement changes the value of a parameter only for the current instance, because there is no mechanism for automatically updating text initialization parameters on disk. You must update them manually to be passed to a future instance. Using a server parameter file overcomes this limitation.

There are two kinds of initialization parameters:

- Dynamic initialization parameters can be changed for the current Oracle Database instance. The changes take effect immediately.
- Static initialization parameters cannot be changed for the current instance. You must change these parameters in the text initialization file or server parameter file and then restart the database before changes take effect.

**Parent topic:** Changing Initialization Parameter Values

##### Setting or Changing Initialization Parameter Values

With a server parameter file, use the `SET` clause of the `ALTER SYSTEM` statement to set or change initialization parameter values.

- Run an `ALTER SYSTEM SET` statement.

For example, the following statement changes the maximum number of failed login attempts before the connection is dropped. It includes a comment, and explicitly states that the change is to be made only in the server parameter file.

```
ALTER SYSTEM SET SEC_MAX_FAILED_LOGIN_ATTEMPTS=3
                 COMMENT='Reduce from 10 for tighter security.'
                 SCOPE=SPFILE;
```

The next example sets a complex initialization parameter that takes a list of attributes. Specifically, the parameter value being set is the `LOG_ARCHIVE_DEST_n` initialization parameter. This statement could change an existing setting for this parameter or create a new archive destination.

```
ALTER SYSTEM 
     SET LOG_ARCHIVE_DEST_4='LOCATION=/u02/oracle/rbdb1/',MANDATORY,'REOPEN=2'
         COMMENT='Add new destination on Nov 29'
         SCOPE=SPFILE;
```

When a value consists of a list of parameters, you cannot edit individual attributes by the position or ordinal number. You must specify the complete list of values each time the parameter is updated, and the new list completely replaces the old list.

- The SCOPE Clause in ALTER SYSTEM SET Statements  
	The optional `SCOPE` clause in `ALTER SYSTEM SET` statements specifies the scope of an initialization parameter change.

**Parent topic:** Changing Initialization Parameter Values

###### The SCOPE Clause in ALTER SYSTEM SET Statements

The optional `SCOPE` clause in `ALTER SYSTEM SET` statements specifies the scope of an initialization parameter change.

| SCOPE Clause | Description |
| --- | --- |
| `SCOPE = SPFILE ` | The change is applied in the server parameter file only. The effect is as follows:  - No change is made to the current instance. - For both dynamic and static parameters, the change is effective at the next startup and is persistent.  This is the only `SCOPE` specification allowed for static parameters. |
| `SCOPE = MEMORY ` | The change is applied in memory only. The effect is as follows:  - The change is made to the current instance and is effective immediately. - For dynamic parameters, the effect is immediate, but it is not persistent because the server parameter file is not updated.  For static parameters, this specification is not allowed. |
| `SCOPE = BOTH ` | The change is applied in both the server parameter file and memory. The effect is as follows:  - The change is made to the current instance and is effective immediately. - For dynamic parameters, the effect is persistent because the server parameter file is updated.  For static parameters, this specification is not allowed. |

It is an error to specify `SCOPE=SPFILE` or `SCOPE=BOTH` if the instance did not start up with a server parameter file. The default is `SCOPE=BOTH` if a server parameter file was used to start up the instance, and `MEMORY` if a text initialization parameter file was used to start up the instance.

For dynamic parameters, you can also specify the `DEFERRED` keyword. When specified, the change is effective only for future sessions.

When you specify `SCOPE` as `SPFILE` or `BOTH`, an optional `COMMENT` clause lets you associate a text string with the parameter update. The comment is written to the server parameter file.

**Parent topic:** Setting or Changing Initialization Parameter Values

#### Clearing Initialization Parameter Values

You can use the `ALTER SYSTEM RESET` statement to clear an initialization parameter value. When you do so, the initialization parameter value is changed to its default value or its startup value.

The `ALTER SYSTEM RESET` statement includes a `SCOPE` clause. When executed in a non-CDB or a multitenant container database (CDB) root, the `ALTER SYSTEM RESET` statement and `SCOPE` clause behave differently than when the statement is executed in a pluggable database (PDB), an application root, or an application PDB.

The startup value of a parameter is the value of the parameter in memory after the instance's startup or PDB open has completed. This value can be seen in the `VALUE` and `DISPLAY_VALUE` columns in the `V$SYSTEM_PARAMETER` view immediately after startup. The startup value can be different from the value in the spfile or the default value (if the parameter is not set in the spfile), since the value of the parameter can be adjusted internally at startup.

The `SCOPE` values for the `ALTER SYSTEM RESET` statement behave as follows in a non-CDB and in the `CDB$ROOT` of a CDB:

- `SCOPE=SPFILE`: If an instance is using spfile, removes the parameter from the spfile; the default value takes effect upon the next instance startup.
- `SCOPE=MEMORY`: The startup value takes effect immediately. However, the change is not stored in instance's spfile and will be lost upon instance restart.
- `SCOPE=BOTH`: If an instance is using spfile, removes the parameter from the spfile; the default value takes effect immediately and the change is available across instance restart.

Note:

`SCOPE=BOTH` changes the way `SCOPE=MEMORY` behaves. After `SCOPE=BOTH` is issued, `SCOPE=MEMORY` always resets the parameter to the default value.

The `SCOPE` values for the `ALTER SYSTEM RESET` statement behave as follows in a PDB, an application root, or an application PDB:

- `SCOPE=SPFILE`: Removes the parameter from the container's spfile; the container will inherit the parameter value from its root upon the next PDB open.
- `SCOPE=MEMORY`: There are two cases:
	- The parameter is present in container's spfile when the container is opened. The parameter value is updated to the startup value for the parameter. This change is not stored in container’s spfile and will be lost upon the next container open.
		- The parameter is not present in container’s spfile when the container is opened. The container starts inheriting the parameter value from its root.
- `SCOPE=BOTH`: Removes the parameter from the container’s spfile; the container will inherit the parameter value from its root.

Note:

- `SCOPE=BOTH` changes the way `SCOPE=MEMORY` behaves. After `SCOPE=BOTH` is issued, the container always inherits the parameter value from its root when `SCOPE=MEMORY` is issued.
- In a case where a container inherits a parameter value from its root, a PDB inherits the value from `CDB$ROOT`. In an application container, an application PDB inherits the parameter value from its application root, and an application root inherits the parameter value from `CDB$ROOT`.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF00902) for information about the `ALTER SYSTEM` command

**Parent topic:** Managing Initialization Parameters Using a Server Parameter File

#### Exporting the Server Parameter File

You can use the `CREATE PFILE` statement to export a server parameter file (SPFILE) to a text initialization parameter file.

- Run a `CREATE PFILE` statement.

Exporting the server parameter file might be necessary for several reasons:

- For diagnostic purposes, listing all of the parameter values currently used by an instance. This is analogous to the SQL\*Plus `SHOW PARAMETERS` command or selecting from the `V$PARAMETER` or `V$PARAMETER2` views.
- To modify the server parameter file by first exporting it, editing the resulting text file, and then re-creating it using the `CREATE SPFILE` statement

The exported file can also be used to start up an instance using the `PFILE` clause.

You must have the `SYSDBA`, `SYSOPER`, or `SYSBACKUP` administrative privilege to execute the `CREATE PFILE` statement. The exported file is created on the database server system. It contains any comments associated with the parameter in the same line as the parameter setting.

The following example creates a text initialization parameter file from the SPFILE:

```
CREATE PFILE FROM SPFILE;
```

Because no names were specified for the files, the database creates an initialization parameter file with a platform-specific name, and it is created from the platform-specific default server parameter file.

The following example creates a text initialization parameter file from a server parameter file, but in this example the names of the files are specified:

```
CREATE PFILE='/u01/oracle/dbs/test_init.ora'
  FROM SPFILE='/u01/oracle/dbs/test_spfile.ora';
```

Note:

An alternative is to create a PFILE from the current values of the initialization parameters in memory. The following is an example of the required command:

```
CREATE PFILE='/u01/oracle/dbs/test_init.ora' FROM MEMORY;
```

**Parent topic:** Managing Initialization Parameters Using a Server Parameter File

#### Backing Up the Server Parameter File

You can create a backup of your server parameter file (SPFILE) by exporting it. If the backup and recovery strategy for your database is implemented using Recovery Manager (RMAN), then you can use RMAN to create a backup of the SPFILE. The SPFILE is backed up automatically by RMAN when you back up your database, but RMAN also enables you to specifically create a backup of the currently active SPFILE.

- Back up the server parameter file either by exporting it or by using RMAN.

See Also:

- " Exporting the Server Parameter File "
- [Oracle Database Backup and Recovery User’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=BRADV89519)

**Parent topic:** Managing Initialization Parameters Using a Server Parameter File

#### Recovering a Lost or Damaged Server Parameter File

You can recover the server parameter file (SPFILE). If your server parameter file (SPFILE) becomes lost or corrupted, then the current instance may fail, or the next attempt at starting the database instance may fail.

There are several ways to recover the SPFILE:

- If the instance is running, issue the following command to re-create the SPFILE from the current values of initialization parameters in memory:
	```
	CREATE SPFILE FROM MEMORY;
	```
	This command creates the SPFILE with the default name and in the default location. You can also create the SPFILE with a new name or in a specified location. See " Creating a Server Parameter File " for examples.
- If you have a valid text initialization parameter file (PFILE), re-create the SPFILE from the PFILE with the following statement:
	```
	CREATE SPFILE FROM PFILE;
	```
	This command assumes that the PFILE is in the default location and has the default name. See " Creating a Server Parameter File " for the command syntax to use when the PFILE is not in the default location or has a nondefault name.
- Restore the SPFILE from backup.
	See " Backing Up the Server Parameter File " for more information.
- If none of the previous methods are possible in your situation, perform these steps:
	1. Create a text initialization parameter file (PFILE) from the parameter value listings in the alert log.
		When an instance starts up, the initialization parameters used for startup are written to the alert log. You can copy and paste this section from the text version of the alert log (without XML tags) into a new PFILE.
		See [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-D6512D97-FFC3-4BF0-BF50-1F77D150C922) for more information.
		2. Create the SPFILE from the PFILE.
		See " Creating a Server Parameter File " for instructions.

Read/Write Errors During a Parameter Update

If an error occurs while reading or writing the server parameter file during a parameter update, the error is reported in the alert log and all subsequent parameter updates to the server parameter file are ignored. At this point, you can take one of the following actions:

- Shut down the instance, recover the server parameter file and described earlier in this section, and then restart the instance.
- Continue to run the database if you do not care that subsequent parameter updates will not be persistent.

**Parent topic:** Managing Initialization Parameters Using a Server Parameter File

#### Methods for Viewing Parameter Settings

You can view parameter settings using several different methods.

| Method | Description |
| --- | --- |
| `SHOW PARAMETERS ` | This SQL\*Plus command displays the values of initialization parameters in effect for the current session. |
| `SHOW SPPARAMETERS` | This SQL\*Plus command displays the values of initialization parameters in the server parameter file (SPFILE). |
| `CREATE PFILE` | This SQL statement creates a text initialization parameter file (PFILE) from the SPFILE or from the current in-memory settings. You can then view the PFILE with any text editor. |
| `V$PARAMETER` | This view displays the values of initialization parameters in effect for the current session. |
| `V$PARAMETER2` | This view displays the values of initialization parameters in effect for the current session. It is easier to distinguish list parameter values in this view because each list parameter value appears in a separate row. |
| `V$SYSTEM_PARAMETER` | This view displays the values of initialization parameters in effect for the instance. A new session inherits parameter values from the instance-wide values. |
| `V$SYSTEM_PARAMETER2` | This view displays the values of initialization parameters in effect for the instance. A new session inherits parameter values from the instance-wide values. It is easier to distinguish list parameter values in this view because each list parameter value appears in a separate row. |
| `V$SPPARAMETER ` | This view displays the current contents of the SPFILE. The view returns `FALSE` values in the `ISSPECIFIED` column if an SPFILE is not being used by the instance. |

See Also:

[Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=REFRN003) for a complete description of views

**Parent topic:** Managing Initialization Parameters Using a Server Parameter File

### Managing Application Workloads with Database Services

A database service is a named representation of one or more database instances. Services enable you to group database workloads and route a particular work request to an appropriate instance.

- Database Services  
	A database service represents a single database. This database can be a single-instance database or an Oracle Real Application Clusters (Oracle RAC) database with multiple concurrent database instances. A global database service is a service provided by multiple databases synchronized through data replication.
- Global Data Services  
	Starting with Oracle Database 12c, you can use Global Data Services (GDS) for workload management involving multiple Oracle databases.
- Database Service Data Dictionary Views  
	You can query data dictionary views to find information about database services.

**Parent topic:** Creating a CDB: Advanced Topics

#### Database Services

A database service represents a single database. This database can be a single-instance database or an Oracle Real Application Clusters (Oracle RAC) database with multiple concurrent database instances. A global database service is a service provided by multiple databases synchronized through data replication.

- About Database Services  
	Database services divide workloads for a single database into mutually disjoint groupings.
- Database Services and Performance  
	Database services offer an extra dimension in performance tuning.
- Oracle Database Features That Use Database Services  
	Several Oracle Database features support database services.
- Creating Database Services  
	There are a few ways to create database services, depending on your database configuration.

**Parent topic:** Managing Application Workloads with Database Services

##### About Database Services

Database services divide workloads for a single database into mutually disjoint groupings.

Each database service represents a workload with common attributes, service-level thresholds, and priorities. The grouping is based on attributes of work that might include the application function to be used, the priority of execution for the application function, the job class to be managed, or the data range used in the application function or job class. For example, the Oracle E-Business Suite defines a database service for each responsibility, such as general ledger, accounts receivable, order entry, and so on. When you configure database services, you give each service a unique name, associated performance goals, and associated importance. The database services are tightly integrated with Oracle Database and are maintained in the data dictionary.

Connection requests can include a database service name. Thus, middle-tier applications and client/server applications use a service by specifying the database service as part of the connection in TNS connect data. If no database service name is included and the Net Services file listener.ora designates a default database service, then the connection uses the default database service.

Database services enable you to configure a workload for a single database, administer it, enable and disable it, and measure the workload as a single entity. You can do this using standard tools such as the Database Configuration Assistant (DBCA), Oracle Net Configuration Assistant, and Oracle Enterprise Manager Cloud Control (Cloud Control). Cloud Control supports viewing and operating services as a whole, with drill down to the instance-level when needed.

In an Oracle Real Application Clusters (Oracle RAC) environment, a database service can span one or more instances and facilitate workload balancing based on transaction performance. This capability provides end-to-end unattended recovery, rolling changes by workload, and full location transparency. Oracle RAC also enables you to manage several database service features with Cloud Control, the DBCA, and the Server Control utility (`SRVCTL`).

Database services describe applications, application functions, and data ranges as either functional services or data-dependent services. Functional services are the most common mapping of workloads. Sessions using a particular function are grouped together. In contrast, data-dependent routing routes sessions to database services based on data keys. The mapping of work requests to database services occurs in the object relational mapping layer for application servers and TP monitors. For example, in Oracle RAC, these ranges can be completely dynamic and based on demand because the database is shared.

In addition to database services that are used by applications, Oracle Database also supports two internal database services: `SYS$BACKGROUND` is used by the background processes only, and `SYS$USERS` is the default database service for user sessions that are not associated with services.

Using database services requires no changes to your application code. Client-side work can connect to a named database service. Server-side work, such as Oracle Scheduler, parallel execution, and Oracle Database Advanced Queuing, set the database service name as part of the workload definition. Work requests executing under a database service inherit the performance thresholds for the service and are measured as part of the service.

See Also:

- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=CNCPT9855)
- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=RACAD841) for information about using services in an Oracle RAC environment
- [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=NETAG002) for information on connecting to a service
- The Cloud Control online help

**Parent topic:** Database Services

##### Database Services and Performance

Database services offer an extra dimension in performance tuning.

Tuning by "service and SQL" can replace tuning by "session and SQL" in the majority of systems where all sessions are anonymous and shared. With database services, workloads are visible and measurable. Resource consumption and waits are attributable by application. Additionally, resources assigned to database services can be augmented when loads increase or decrease. This dynamic resource allocation enables a cost-effective solution for meeting demands as they occur. For example, database services are measured automatically, and the performance is compared to service-level thresholds. Performance violations are reported to Cloud Control, enabling the execution of automatic or scheduled solutions.

**Parent topic:** Database Services

##### Oracle Database Features That Use Database Services

Several Oracle Database features support database services.

The Automatic Workload Repository (AWR) manages the performance of services. AWR records database service performance, including execution times, wait classes, and resources consumed by services. AWR alerts warn when database service response time thresholds are exceeded. The dynamic views report current service performance metrics with one hour of history. Each database service has quality-of-service thresholds for response time and CPU consumption.

In addition, the Database Resource Manager can map database services to consumer groups. Therefore, you can automatically manage the priority of one database service relative to others. You can use consumer groups to define relative priority in terms of either ratios or resource consumption.

You also can specify an edition attribute for a database service. Editions make it possible to have two or more versions of the same objects in the database. When you specify an edition attribute for a database service, all subsequent connections that specify the database service use this edition as the initial session edition.

Specifying an edition as a database service attribute can make it easier to manage resource usage. For example, database services associated with an edition can be placed on a separate instance in an Oracle RAC environment, and the Database Resource Manager can manage resources used by different editions by associating resource plans with the corresponding database services.

For Oracle Scheduler, you optionally assign a database service when you create a job class. During execution, jobs are assigned to job classes, and job classes can run within database services. Using database services with job classes ensures that the work executed by the job scheduler is identified for workload management and performance tuning.

For parallel query and parallel DML, the query coordinator connects to a database service just like any other client. The parallel query processes inherit the database service for the duration of the execution. At the end of query execution, the parallel execution processes revert to the default database service.

See Also:

Oracle Database Administrator’s Guide to learn about the following topics:

- " [Managing Resources with Oracle Database Resource Manager](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-2BEF5482-CF97-4A85-BD90-9195E41E74EF) "
- " [Specifying Session-to-Consumer Group Mapping Rules](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-5AA9FBC6-3C11-4DA5-B9EE-C98CC2553042) "
- " [Setting the Edition Attribute of a Database Service](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-C11D21A6-718E-4D5D-8E31-D624D16E38DD) "
- " [Scheduling Jobs with Oracle Scheduler](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-D41660D0-D88F-4D9F-8CC8-63D040EDC4E6) "

**Parent topic:** Database Services

##### Creating Database Services

There are a few ways to create database services, depending on your database configuration.

Note:

Starting with Oracle Database 19c, customer use of the `SERVICE_NAMES` parameter is deprecated. It can be desupported in a future release. To manage your services, Oracle recommends that you use the `SRVCTL` or `GDSCTL` command line utilities, or the `DBMS_SERVICE` package.

Note:

This section describes creating services locally.

To create a database service:

- If your single-instance database is being managed by Oracle Restart, use the `SRVCTL` utility to create the database service.
	```
	srvctl add service -db db_unique_name -service service_name
	```
- If your single-instance database is not being managed by Oracle Restart, do one of the following:
	- Append the desired database service name to the `SERVICE_NAMES` parameter.
		- Call the `DBMS_SERVICE.CREATE_SERVICE` package procedure.
- (Optional) Define database service attributes with Cloud Control or with `DBMS_SERVICE.MODIFY_SERVICE`.

Oracle Net Listener (the listener) receives incoming client connection requests and manages the traffic of these requests to the database server. The listener handles connections for registered services, and it supports dynamic service registration.

See Also:

- " Global Data Services "
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-5832E064-85C6-453C-B932-99700B1732A9) for information about Oracle Restart
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ARPLS092) for information about the `DBMS_SERVICE` package
- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=RACAD076) for information about creating a service in an Oracle RAC environment
- [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=NETAG298) for more information about Oracle Net Listener and services

**Parent topic:** Database Services

#### Global Data Services

Starting with Oracle Database 12c, you can use Global Data Services (GDS) for workload management involving multiple Oracle databases.

GDS enables administrators to automatically and transparently manage client workloads across replicated databases that offer common services. These common services are known as global services.

GDS enables you to integrate multiple databases in various locations into private GDS configurations that can be shared by global clients. Benefits include the following:

- Enables central management of global resources
- Provides global scalability, availability, and run-time load balancing
- Allows you to dynamically add databases to the GDS configuration and dynamically migrate global services
- Extends service management, load balancing, and failover capabilities for distributed environments of replicated databases that use features such as Oracle Active Data Guard, Oracle GoldenGate, and so on
- Provides high availability through seamless failover of global services across databases (located both locally or globally)
- Provides workload balancing both within and between data centers through services, connection load balancing, and runtime load balancing
- Allows efficient utilization of the resources of the GDS configuration to service client requests

See Also:

[Oracle Database Global Data Services Concepts and Administration Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=GSMUG-GUID-152F7AB7-F4A8-44B4-BD82-CEDA4A6F41EE) for an overview of Global Data Services

**Parent topic:** Managing Application Workloads with Database Services

#### Database Service Data Dictionary Views

You can query data dictionary views to find information about database services.

You can find information about database services in the following views:

- `DBA_SERVICES`
- `ALL_SERVICES` or `V$SERVICES`
- `V$ACTIVE_SERVICES`
- `V$SERVICE_STATS`
- `V$SERVICE_EVENT`
- `V$SERVICE_WAIT_CLASS`
- `V$SERV_MOD_ACT_STATS`
- `V$SERVICEMETRIC`
- `V$SERVICEMETRIC_HISTORY`

The following additional views also contain some information about database services:

- `V$SESSION`
- `V$ACTIVE_SESSION_HISTORY`
- `DBA_RSRC_GROUP_MAPPINGS`
- `DBA_SCHEDULER_JOB_CLASSES`
- `DBA_THRESHOLDS`

The `ALL_SERVICES` view includes a `GLOBAL_SERVICE` column, and the `V$SERVICES` and `V$ACTIVE_SERVICES` views contain a `GLOBAL` column. These views and columns enable you to determine whether a database service is a global service.

**Parent topic:** Managing Application Workloads with Database Services

### Managing Standard Edition High Availability for Oracle Databases

The Standard Edition High Availability feature provides protection against unplanned outages for Oracle Database Standard Edition 2 single instance databases using Oracle Clusterware.

Note:

Standard Edition High Availability is supported in this release of Oracle Database.

Note:

The `srvctl` commands used with Standard Edition High Availability are different from those used with Oracle Restart. For Standard Edition High Availability, refer to the `srvctl` commands documented in the Oracle Real Application Clusters Administration and Deployment Guide.

- About Standard Edition High Availability  
	In this release, you can install Oracle Database Standard Edition 2 in high availability mode.
- Requirements for Using Standard Edition High Availability With Oracle Databases  
	To use Standard Edition High Availability, deploy Oracle Database Standard Edition 2 in accordance with these configuration requirements.
- Enabling Standard Edition High Availability for Oracle Databases  
	You enable Standard Edition High Availability to provide cluster-based failover for an Oracle Database Standard Edition 2 database.
- Relocating a Standard Edition High Availability Database to Another Node  
	To manage planned outages, you can relocate an Oracle Database Standard Edition 2 database that uses Standard Edition High Availability to another configured node.
- Adding a Node to a Standard Edition High Availability Database  
	Adding new nodes to an existing Standard Edition High Availability configuration provides enhanced failover capabilities to your Standard Edition 2 database.
- Removing a Configured Node from a Standard Edition High Availability Database  
	Use `srvctl` commands to remove a node from the list of nodes configured for a Standard Edition High Availability database.
- Starting and Stopping Standard Edition High Availability Databases  
	Use `srvctl` commands to start or stop an Oracle Database that is configured for Standard Edition High Availability.
- Deactivating Standard Edition High Availability for Oracle Databases  
	When you deactivate Standard Edition High Availability for a single instance Oracle Database, the database is no longer part of a high availability failover configuration.

**Parent topic:** Creating a CDB: Advanced Topics

#### About Standard Edition High Availability

In this release, you can install Oracle Database Standard Edition 2 in high availability mode.

Standard Edition High Availability provides cluster-based failover for single-instance Standard Edition Oracle Databases using Oracle Clusterware.

Oracle Standard Edition High Availability benefits from the cluster capabilities and storage solutions that are already part of Oracle Grid Infrastructure, such as Oracle Clusterware, Oracle Automatic Storage Management (Oracle ASM) and Oracle Advanced Cluster File System (Oracle ACFS).

Using integrated, shared, and concurrently mounted storage, such as Oracle ASM and Oracle ACFS for database files as well as for unstructured data, enables Oracle Grid Infrastructure to restart an Oracle Database on a failover node much faster than any cluster solution that relies on failing over and remounting volumes and file systems.

Standard Edition High Availability is supported on Linux x86-64, Microsoft Windows, and HP-UX Itanium.

Note:

This section is specific to Standard Edition High Availability, which provides cluster-based database failover for Standard Edition Oracle Databases 21c and later. For more information about high availability options for Oracle Database, see [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=CWADD-GUID-C54E2511-24E2-452B-B4C7-0D5A93A751A9).

**Parent topic:** Managing Standard Edition High Availability for Oracle Databases

#### Requirements for Using Standard Edition High Availability With Oracle Databases

To use Standard Edition High Availability, deploy Oracle Database Standard Edition 2 in accordance with these configuration requirements.

- The database is created in a cluster running Oracle Grid Infrastructure for a Standalone Cluster, with its database files placed in Oracle Automatic Storage Management (Oracle ASM) or Oracle Advanced Cluster File System (Oracle ACFS).
- When using the Database Configuration Assistant, do not create a listener when creating an Oracle Database Standard Edition 2 database that you want to configure for Standard Edition High Availability.
- Register the database with Single Client Access Name (SCAN) listeners as remote listeners, and node listeners as the local listener.
- Create a database service. Use this service, instead of the default database service, when you connect applications or database clients to the database.
- Ensure that the server parameter file (`spfile`) and password file are on Oracle ASM or Oracle ACFS. If the `spfile` and password file were placed on a local file system when the database was created or configured, then move these files to Oracle ASM or Oracle ACFS.

Refer to the database installation documentation for additional requirements that must be met.

#### Enabling Standard Edition High Availability for Oracle Databases

You enable Standard Edition High Availability to provide cluster-based failover for an Oracle Database Standard Edition 2 database.

Note:

The steps in this topic must be performed after you install the Oracle Database software binaries to configure Standard Edition High Availability, as described in the Oracle Database Installation Guide for Linux, and create a database. If you have an existing Standard Edition 2 database that runs on one cluster node, and you want to enable Standard Edition High Availability for this database, you need to add a node to the configuration.

Prerequisites

- Ensure that the initialization parameter `local_listener` is not set. This is to enable node listeners to be automatically used and database connections to be made over the node virtual IP address.
	Use the following command to display the current listener configuration:
	```
	SQL> SHOW PARAMETER LOCAL_LISTENER;
	```
	If the output of the above command shows a local listener name, then reset the local listener using the following command:
	```
	SQL> ALTER SYSTEM RESET LOCAL_LISTENER SCOPE = BOTH;
	```
	The database must be restarted for the listener configuration change to take effect. However, if the database is relocated to another node, as part of verifying the Standard Edition High Availability configuration, then the database need not be restarted.
- When the database files are stored in Oracle Advanced Cluster File System (Oracle ACFS), the Oracle ACFS file system must be registered in Oracle Clusterware and the dependency of the database resource on the corresponding Oracle ACFS resources must be configured using `srvctl` commands. For example:
	```
	$ srvctl modify database -db se2cdb2 -acfspath /u01/app/oradata
	```

To enable Standard Edition High Availability for an Oracle Database Standard Edition 2 database:

1. If the database was created using the `CREATE DATABASE` command, then register the database with Oracle Clusterware.
	Databases created using the `CREATE DATABASE` command are not automatically registered with Oracle Clusterware. Use the `srvctl add database` command to register the database.
	For example, the following command registers the single instance database, whose unique name is `se2cdb`, with the nodes `node3` and `node5`:
	```
	$ srvctl add database -db se2cdb -oraclehome $ORACLE_HOME 
	-dbtype SINGLE -spfile +DATA/SE2CDB1/PARAMETERFILE/spfile.276.1030845691 
	-node node3,node5
	```
2. If the database is already registered with Oracle Clusterware, use the `srvctl modify database` command to enable Standard Edition High Availability.
	For example, the following command enables Standard Edition High Availability on a Standard Edition 2 database whose database unique name is `se2cdb`:
	```
	$ srvctl modify database -db se2cdb -node node3,node5
	```
	Note:
	The `-fixed` option to create a fixed single instance database is not supported with Standard Edition High Availability.

After you enable Standard Edition High Availability for a database:

- When there is an unplanned outage of the node which runs the database instance, the instance is restarted on an available node in the configured node list.
- When there is an unplanned termination of the database instance, an attempt is made to restart the instance on the current node. If the restart fails, a failover is initiated to an available node in the configured node list.
- When the node which runs the database instance completely loses connectivity to the public network, the instance is relocated to an available node in the configured node list.

Note:

The order of nodes in the node list determines the node on which the database is started. Oracle Clusterware attempts to start the database on the first node in the node list. If the first node is unavailable, it moves to the next node in the node list.

Oracle Clusterware also uses the order of nodes in the node list to determine the failover target, if the current node fails. Failover targets are considered starting with the first node in the list and until a suitable candidate is found and unless other circumstances in the cluster prevent this order to determine the failover node.

To verify the Standard Edition High Availability configuration, especially its current configured node list, use the `srvctl config                     database` command. For example:

```
$ srvctl config database -db se2cdb 
...
Type: SINGLE
...
Configured nodes:
        node3, node5
```

Notice from the output that the type of database is single, but there are multiple configured nodes. This indicates that Standard Edition High Availability is enabled.

Further verification can be performed by relocating the database to another configured node.

#### Relocating a Standard Edition High Availability Database to Another Node

To manage planned outages, you can relocate an Oracle Database Standard Edition 2 database that uses Standard Edition High Availability to another configured node.

The node to which the database is being relocated must be part of the configured node list for this database.

To relocate an active Oracle Database Standard Edition 2 database from its current node to another configured node:

- Use the `srvctl relocate` command.
	This command performs an offline relocation. It shuts down the database on the existing node and then starts it on the new node.

For example, the following command relocates the Standard Edition 2 database named `se2cdb`, that uses Standard Edition High Availability, to the node `node5`:

```
$ srvctl relocate database -db se2cdb -node node5
```

Note:

The `–abort` and `–revert` options of `srvctl relocate database` command are not supported with Standard Edition High Availability.

**Parent topic:** Managing Standard Edition High Availability for Oracle Databases

#### Adding a Node to a Standard Edition High Availability Database

Adding new nodes to an existing Standard Edition High Availability configuration provides enhanced failover capabilities to your Standard Edition 2 database.

You may need to add nodes in certain scenarios. Assume that you configured two nodes for your Standard Edition High Availability database. Subsequently, a new node is added to the cluster and you want to include this new node in your database configuration. You can do this by adding the node to the Standard Edition High Availability configuration. Another scenario is when you want to enable Standard Edition High Availability for an existing Standard Edition 2 database.

To add a node to a Standard Edition High Availability database:

1. Extend the Oracle Database Oracle home to the new node. The steps depend on the storage used.
	For a local (non-shared) Oracle home:
	1. Log in to the first cluster node (on which you configured Standard Edition High Availability) as the Oracle installation owner user account (`oracle`).
	2. Navigate to the `ORACLE_HOME/addnode` directory and run the `addnode.sh` script on Linux or `addnode.bat` on Windows.
		For example, to extend the Oracle home to `node3` on Linux:
		```
		$ ./addnode.sh -silent "CLUSTER_NEW_NODES={node3}"
		```
	For a shared Oracle home using Oracle ACFS:
	1. Start the Oracle ACFS resource on the new node by running the following command as `root` from the `Grid_home/bin` directory:
		```
		# srvctl start filesystem -device volume_device [-node node_name]
		```
		Note:
		Make sure the Oracle ACFS resources, including Oracle ACFS registry resource and Oracle ACFS file system resource where the Oracle home is located, are online on the newly added node.
	2. Log in to the first cluster node (on which you configured Standard Edition High Availability) as the Oracle installation owner user account (`oracle`).
	3. Attach the Oracle home on the first cluster node to the node that you want to add.
		```
		$ $ORACLE_HOME/addnode/addnode.sh -silent CLUSTER_NEW_NODES=new_node_name
		```
2. On the new node (that must be added), as the `root` user, and run the `ORACLE_HOME/root.sh` script.
	```
	# /u01/app/oracle/product/21.0.0/dbhome_1/root.sh
	```
3. On any configured node, including the node that is being added, as the `oracle` user, add the new node by using the `srvctl                         modify database` command.
	The `-node` argument must list the existing configured nodes and the new node that is being added.
	For example, the following command adds the node `node3` to the database with unique name `se2cdb`. Existing configured nodes are `node1` and `node5`.
	```
	$ srvctl modify database -db se2cdb -node node1,node3,node5
	```

You can optionally verify the new configuration as described in Enabling Standard Edition High Availability for Oracle Databases.

#### Removing a Configured Node from a Standard Edition High Availability Database

Use `srvctl` commands to remove a node from the list of nodes configured for a Standard Edition High Availability database.

Navigate to the Oracle Database home directory. On Linux, log in to the database host computer as the Oracle installation owner user account (`oracle`). On Windows, log in to the database host computer as Administrator.

To remove a configured node from a database that uses Standard Edition High Availability:

1. List the existing configured nodes by using the `srvctl config                         database` command.
2. If the database is currently running on the node that you want to remove, relocate the database to another configured node by using the `srvctl                         relocate database` command.
3. Remove the node by using the `srvctl modify database` command with the `-node` argument.
	The `-node` argument must list all the configured nodes, except the node that must be removed.

Example 4-1 Removing a Configured Node from a Standard Edition High Availability Database

The example assumes that the database with unique name `sec2cdb` uses Standard Edition High Availability and the configured nodes are `node1`, `node2`, and `node3`. The database is currently running on `node3`. To remove `node2` from the list of configured nodes for this database, log in as a user who installed the Oracle Database home and run the following command:

```
$ srvctl modify database -db sec2cdb -node node1,node3
```

#### Starting and Stopping Standard Edition High Availability Databases

Use `srvctl` commands to start or stop an Oracle Database that is configured for Standard Edition High Availability.

Navigate to the Oracle Database home directory. On Linux, log in to the database host computer as the Oracle installation owner user account (`oracle`). On Windows, log in to the database host computer as Administrator.

To start up a Standard Edition High Availability database:

- Use the `srvctl start database` command.
	Optionally, include the `-node` argument to specify the node on which the database must be started.

To stop a Standard Edition High Availability database:

- Use the `srvctl stop database` command

Example 4-2 Starting Up a Standard Edition High Availability Database on a Specified Node

This example starts up a database with the unique name `se2cdb` on the node named `node3`.

```
$ srvctl start database -db sec2cdb -node node3
```

Example 4-3 Stopping a Standard Edition High Availability Database

This example stops a database instance that is configured to use Standard Edition High Availability. The unique name of the database is `sec2cdb`.

```
$ srvctl stop database -db sec2cdb
```

#### Deactivating Standard Edition High Availability for Oracle Databases

When you deactivate Standard Edition High Availability for a single instance Oracle Database, the database is no longer part of a high availability failover configuration.

To deactivate Standard Edition High Availability for an Oracle Database:

- Use the `srvctl modify` command and include only one node in the `-node` argument.

Example 4-4 Deactivating the Use of Standard Edition High Availability for an Oracle Database

This example deactivates the use of Standard Edition High Availability for the database with unique name `se2cdb` and configures only one node, `node1`, for this database:

```
srvctl modify database -db se2cdb -node node1
```

All previously configured nodes are removed and the database is now a single-instance database that is registered with Oracle Clusterware.

**Parent topic:** Managing Standard Edition High Availability for Oracle Databases

### Cloning a Database

This section describes various methods of cloning an Oracle database.

- Cloning a Database in a Multitenant Environment  
	You can clone a database in a multitenant environment.
- Cloning a Database with Oracle Automatic Storage Management (Oracle ASM)  
	Oracle Automatic Storage Management (Oracle ASM) provides support for cloning a pluggable database (PDB) in a multitenant container database (CDB). Oracle ASM does not support cloning a non-CDB.

**Parent topic:** Creating a CDB: Advanced Topics

#### Cloning a Database in a Multitenant Environment

You can clone a database in a multitenant environment.

Refer to [Oracle Multitenant Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=MULTI-GUID-05702CEB-A43C-452C-8081-4CA68DDA8007) for more information about cloning a database in a multitenant environment.

**Parent topic:** Cloning a Database

#### Cloning a Database with Oracle Automatic Storage Management (Oracle ASM)

Oracle Automatic Storage Management (Oracle ASM) provides support for cloning a pluggable database (PDB) in a multitenant container database (CDB). Oracle ASM does not support cloning a non-CDB.

See the following guides for more information:

- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=OSTMG-GUID-F0CA1610-780A-40FB-B8BB-88E0C7688CC2)
- [Oracle Multitenant Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=MULTI-GUID-7ED69A82-B797-4497-A160-FDDAA2AAC999)

**Parent topic:** Cloning a Database

### Configuring EM Express for a CDB

For a CDB, you can configure Oracle Enterprise Manager Database Express (EM Express) for the root and for each PDB by setting a global HTTPS port, or you can set a different port for every container in the CDB.

Note:

EM Express is a web-based database management tool that is built inside the Oracle Database. It supports key performance management and basic database administration functions. Many of EM Express's capabilities are also available in Oracle SQL Developer, which is included in all Oracle Database editions. Oracle recommends that you replace your use of EM Express with Oracle SQL Developer.

To configure EM Express for a CDB:

You can set a global port, which enables you to use EM Express to connect to all PDBs in the CDB using the HTTPS port for the CDB. Alternatively, you can set a different HTTPS port for every container in a CDB.

1. In SQL\*Plus, access a container in a CDB.
	The user must have common `SYSDBA` administrative privilege, and you must exercise this privilege using `AS SYSDBA` at connect time. The container can be the root or a PDB.
	See " [About Container Access in a CDB](administering-a-cdb-with-sql-plus.md) ".
2. Set the port in one of the following ways:
	- To set the global port, connect to the `CDB$ROOT`, and issue the following SQL statement to configure the global port for the CDB:
		```
		EXEC DBMS_XDB_CONFIG.SETGLOBALPORTENABLED(TRUE);
		```
		- To set the HTTPS port for the current container, run the following procedure:
		```
		exec DBMS_XDB_CONFIG.SETHTTPSPORT(https_port_number);
		```
		Replace `https_port_number` with the appropriate HTTPS port number.
3. Access EM Express in one of the following ways:
	- To use the global port, enter the EM Express URL provided by Database Configuration Assistant (DBCA) when it configured the CDB that includes the PDB. When the EM Express login screen appears, specify your administrator credentials, and enter the name of the PDB that you want to connect to in the Container Name field.
		- The URL for the HTTPS port for a container:
		```
		https://database_hostname:https_port_number/em/
		```
		Replace `database_hostname` with the host name of the computer on which the database instance is running, and replace `https_port_number` with the appropriate HTTPS port number.
	When connected to the root, EM Express displays data and enables actions that apply to the entire CDB. When connected to a PDB, EM Express displays data and enables actions that apply to the PDB only.
	Note:
	If the listener is not configured on port 1521, then you must manually configure the port for EM Express.

**Parent topic:** Creating a CDB: Advanced Topics

### Dropping a Database

Dropping a CDB involves removing its data files, online redo logs, control files, and initialization parameter files.

WARNING:

Dropping a CDB deletes all its data.

To drop a database:

- Submit the following statement:
	```
	DROP DATABASE;
	```

The `DROP DATABASE` statement first deletes all control files and all other database files listed in the control file. It then shuts down the database instance.

To use the `DROP DATABASE` statement successfully, the database must be mounted in exclusive and restricted mode.

The `DROP DATABASE` statement has no effect on archived redo log files, nor does it have any effect on copies or backups of the database. It is best to use RMAN to delete such files.

If you used the Database Configuration Assistant to create your database, you can use that tool to delete (drop) your database and remove the files.

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-2042AAE4-DAE5-4CD4-89E9-B9DE3A8A2AA1)

**Parent topic:** Creating a CDB: Advanced Topics