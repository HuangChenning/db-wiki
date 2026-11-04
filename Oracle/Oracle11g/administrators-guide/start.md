---
title: Starting Up and Shutting Down
book: "Administrator's Guide"
doc_id: E25494-07
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e25494/start.htm
tags:
  - oracle
  - 11g
  - administrators-guide
---

## 3 Starting Up and Shutting Down

In this chapter:

## Starting Up a Database

When you start up a database, you create an instance of that database and you determine the state of the database. Normally, you start up an instance by mounting and opening the database. Doing so makes the database available for any valid user to connect to and perform typical data access operations. Other options exist, and these are also discussed in this section.

This section contains the following topics relating to starting up an instance of a database:

- About Database Startup Options
- About Initialization Parameter Files and Startup
- About Automatic Startup of Database Services
- Preparing to Start Up an Instance
- Starting Up an Instance

### About Database Startup Options

When Oracle Restart is not in use, you can start up a database instance with SQL\*Plus, Recovery Manager, or Enterprise Manager. If your database is being managed by Oracle Restart, the recommended way to start the database is with SRVCTL.

See [Chapter 4, "Configuring Automatic Restart of an Oracle Database"](restart.md) for information about Oracle Restart.

#### Starting Up a Database Using SQL\*Plus

You can start a SQL\*Plus session, connect to Oracle Database with administrator privileges, and then issue the `STARTUP` command. Using SQL\*Plus in this way is the only method described in detail in this book.

#### Starting Up a Database Using Recovery Manager

You can also use Recovery Manager (RMAN) to execute `STARTUP` and `SHUTDOWN` commands. You may prefer to do this if your are within the RMAN environment and do not want to invoke SQL\*Plus.

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2019.htm#RCMRF158) for information about the RMAN `STARTUP` command

#### Starting Up a Database Using Oracle Enterprise Manager

You can use Oracle Enterprise Manager to administer your database, including starting it up and shutting it down. Enterprise Manager combines a GUI console, agents, common services, and tools to provide an integrated and comprehensive systems management platform for managing Oracle products. Enterprise Manager Database Control, which is the portion of Enterprise Manager that is dedicated to administering an Oracle database, enables you to perform the functions discussed in this book using a GUI interface, rather than command line operations.

See Also:

- [Oracle Enterprise Manager Concepts](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=OEMCN)
- [Oracle Database 2 Day DBA](https://docs.oracle.com/cd/E11882_01/server.112/e10897/instance.htm#ADMQS052)

The remainder of this section describes using SQL\*Plus to start up a database instance.

#### Starting Up a Database Using SRVCTL

When Oracle Restart is installed and configured for your database, Oracle recommends that you use SRVCTL to start the database. This ensures that:

- Any components on which the database depends (such as Oracle Automatic Storage Management and the Oracle Net listener) are automatically started first, and in the proper order.
- The database is started according to the settings in its Oracle Restart configuration. An example of such a setting is the server parameter file location.
- Environment variables stored in the Oracle Restart configuration for the database are set before starting the instance.

See ["srvctl start database"](restart.md) and ["Starting and Stopping Components Managed by Oracle Restart"](restart.md) for details.

### Specifying Initialization Parameters at Startup

To start an instance, the database must read instance configuration parameters (the initialization parameters) from either a server parameter file (`SPFILE`) or a text initialization parameter file (PFILE).

The database looks for these files in a default location. You can specify nondefault locations for these files, and the method for doing so depends on whether you start the database with SQL\*Plus (when Oracle Restart is not in use) or with SRVCTL (when the database is being managed with Oracle Restart).

The following sections provide details:

- About Initialization Parameter Files and Startup
- Starting Up with SQL\*Plus with a Nondefault Server Parameter File
- Starting Up with SRVCTL with a Nondefault Server Parameter File

See Also:

[Chapter 2, "Creating and Configuring an Oracle Database"](create.md), for more information about initialization parameters, initialization parameter files, and server parameter files

#### About Initialization Parameter Files and Startup

When you start the database instance, it attempts to read the initialization parameters from an `SPFILE` in a platform-specific default location. If it finds no `SPFILE`, it searches for a text initialization parameter file.

[Table 2-3](create.md) lists PFILE and SPFILE default names and locations.

In the platform-specific default location, Oracle Database locates your initialization parameter file by examining file names in the following order:

1. `spfile` `ORACLE_SID`.`ora`
2. `spfile.ora`
3. `init` `ORACLE_SID`.`ora`

The first two files are `SPFILE` s and the third is a text initialization parameter file. If DBCA created the SPFILE in an Oracle Automatic Storage Management disk group, the database searches for the SPFILE in the disk group.

Note:

The `spfile.ora` file is included in this search path because in an Oracle Real Application Clusters environment one server parameter file is used to store the initialization parameter settings for all instances. There is no instance-specific location for storing a server parameter file.

For more information about the server parameter file for an Oracle Real Application Clusters environment, see [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/admin.htm#RACAD020).

If you (or the Database Configuration Assistant) created a server parameter file, but you want to override it with a text initialization parameter file, you can do so with SQL\*Plus, specifying the `PFILE` clause of the `STARTUP` command to identify the initialization parameter file:

```
STARTUP PFILE = /u01/oracle/dbs/init.ora
```

Nondefault Server Parameter Files A nondefault server parameter file (`SPFILE`) is an `SPFILE` that is in a location other than the default location. It is not usually necessary to start an instance with a nondefault `SPFILE`. However, should such a need arise, both SRVCTL (with Oracle Restart) and SQL\*Plus provide ways to do so. These are described later in this section.

Initialization Files and Oracle Automatic Storage Management A database that uses Oracle Automatic Storage Management (Oracle ASM) usually has a nondefault `SPFILE`. If you use the Database Configuration Assistant (DBCA) to configure a database to use Oracle ASM, DBCA creates an `SPFILE` for the database instance in an Oracle ASM disk group, and then causes a text initialization parameter file (PFILE) to be created in the default location in the local file system to point to the `SPFILE`, as explained in the next section.

#### Starting Up with SQL\*Plus with a Nondefault Server Parameter File

With SQL\*Plus you can use the `PFILE` clause to start an instance with a nondefault server parameter file.

To start up with SQL\*Plus with a nondefault server parameter file:

1. Create a one-line text initialization parameter file that contains only the `SPFILE` parameter. The value of the parameter is the nondefault server parameter file location.
	For example, create a text initialization parameter file `/u01/oracle/dbs/spf_init.ora` that contains only the following parameter:
	```
	SPFILE = /u01/oracle/dbs/test_spfile.ora
	```
	Note:
	You cannot use the `IFILE` initialization parameter within a text initialization parameter file to point to a server parameter file. In this context, you must use the `SPFILE` initialization parameter.
2. Start up the instance pointing to this initialization parameter file.
	```
	STARTUP PFILE = /u01/oracle/dbs/spf_init.ora
	```

The `SPFILE` must reside on the database host computer. Therefore, the preceding method also provides a means for a client system to start a database that uses an `SPFILE`. It also eliminates the need for a client system to maintain a client-side initialization parameter file. When the client system reads the initialization parameter file containing the `SPFILE` parameter, it passes the value to the server where the specified `SPFILE` is read.

#### Starting Up with SRVCTL with a Nondefault Server Parameter File

If your database is being managed by Oracle Restart, you can specify the location of a nondefault SPFILE by setting or modifying the SPFILE location option in the Oracle Restart configuration for the database.

To start up with SRVCTL with a nondefault server parameter file:

1. Prepare to run SRVCTL as described in ["Preparing to Run SRVCTL"](restart.md).
2. Enter the following command:
	```
	srvctl modify database -d db_unique_name -p spfile_path
	```
	where `db_unique_name` must match the `DB_UNIQUE_NAME` initialization parameter setting for the database.
3. Enter the following command:
	```
	srvctl start database -d db_unique_name [options]
	```

See ["SRVCTL Command Reference for Oracle Restart"](restart.md) for more information.

### About Automatic Startup of Database Services

When your database is managed by Oracle Restart, you can configure startup options for each individual database service (service). If you set the management policy for a service to `AUTOMATIC` (the default), the service starts automatically when you start the database with SRVCTL. If you set the management policy to `MANUAL`, the service does not automatically start, and you must manually start it with SRVCTL. A `MANUAL` setting does not prevent Oracle Restart from monitoring the service when it is running and restarting it if a failure occurs.

In an Oracle Data Guard (Data Guard) environment in which databases are managed by Oracle Restart, you can additionally control automatic startup of services by assigning Data Guard roles to the services in their Oracle Restart configurations. A service automatically starts upon manual database startup only if the management policy of the service is `AUTOMATIC` and if one of its assigned roles matches the current role of the database.

See ["srvctl add service"](restart.md) and ["srvctl modify service"](restart.md) for the syntax for setting the management policy of and Data Guard roles for a service.

Note:

When using Oracle Restart, Oracle strongly recommends that you use SRVCTL to create database services.

### Preparing to Start Up an Instance

Note:

The following instructions are for installations where Oracle Restart is not in use. If your database is being managed by Oracle Restart, follow the instructions in ["Starting and Stopping Components Managed by Oracle Restart"](restart.md).

You must perform some preliminary steps before attempting to start an instance of your database using SQL\*Plus.

1. Ensure that any Oracle components on which the database depends are started.
	For example, if the database stores data in Oracle Automatic Storage Management (Oracle ASM) disk groups, ensure that the Oracle ASM instance is running and the required disk groups are mounted. Also, it is preferable to start the Oracle Net listener before starting the database.
2. If you intend to use operating system authentication, log in to the database host computer as a member of the OSDBA group.
	See ["Using Operating System Authentication"](dba.md) for more information.
3. Ensure that environment variables are set so that you connect to the desired Oracle instance. For details, see ["Submitting Commands and SQL to the Database"](dba.md).
4. Start SQL\*Plus without connecting to the database:
	```
	SQLPLUS /NOLOG
	```
5. Connect to Oracle Database as `SYSDBA`:
	```
	CONNECT username AS SYSDBA
	—or—
	CONNECT / AS SYSDBA
	```

Now you are connected to the database and ready to start up an instance of your database.

See Also:

[SQL\*Plus User's Guide and Reference](https://docs.oracle.com/cd/E11882_01/server.112/e16604/toc.htm) for descriptions and syntax for the `CONNECT`, `STARTUP`, and `SHUTDOWN` commands.

### Starting Up an Instance

When Oracle Restart is not in use, you use the SQL\*Plus `STARTUP` command to start up an Oracle Database instance. If your database is being managed by Oracle Restart, Oracle recommends that you use the [srvctl start database](restart.md) command.

In either case, you can start an instance in various modes:

- `NOMOUNT` —Start the instance without mounting a database. This does not allow access to the database and usually would be done only for database creation or the re-creation of control files.
- `MOUNT` —Start the instance and mount the database, but leave it closed. This state allows for certain DBA activities, but does not allow general access to the database.
- `OPEN` —Start the instance, and mount and open the database. This can be done in unrestricted mode, allowing access to all users, or in restricted mode, allowing access for database administrators only.
- `FORCE` —Force the instance to start after a startup or shutdown problem.
- `OPEN` `RECOVER` —Start the instance and have complete media recovery begin immediately.

Note:

You cannot start a database instance if you are connected to the database through a shared server process.

The following scenarios describe and illustrate the various states in which you can start up an instance. Some restrictions apply when combining clauses of the `STARTUP` command or combining startup options for the [srvctl start database](restart.md) command.

Note:

It is possible to encounter problems starting up an instance if control files, database files, or redo log files are not available. If one or more of the files specified by the `CONTROL_FILES` initialization parameter does not exist or cannot be opened when you attempt to mount a database, Oracle Database returns a warning message and does not mount the database. If one or more of the data files or redo log files is not available or cannot be opened when attempting to open a database, the database returns a warning message and does not open the database.

See Also:

- [SQL\*Plus User's Guide and Reference](https://docs.oracle.com/cd/E11882_01/server.112/e16604/ch_twelve044.htm#SQPUG127) for details on the `STARTUP` command syntax
- ["Starting and Stopping Components Managed by Oracle Restart"](restart.md) for instructions for starting a database that is managed by Oracle Restart.

#### Starting an Instance, and Mounting and Opening a Database

Normal database operation means that an instance is started and the database is mounted and open. This mode allows any valid user to connect to the database and perform data access operations.

The following command starts an instance, reads the initialization parameters from the default location, and then mounts and opens the database.

| SQL\*Plus | SRVCTL (When Oracle Restart Is In Use) |
| --- | --- |
| ``` STARTUP ``` | ``` srvctl start database -d db_unique_name ``` |

where `db_unique_name` matches the `DB_UNIQUE_NAME` initialization parameter.

#### Starting an Instance Without Mounting a Database

You can start an instance without mounting a database. Typically, you do so only during database creation. Use one of the following commands:

| SQL\*Plus | SRVCTL (When Oracle Restart Is In Use) |
| --- | --- |
| ``` STARTUP NOMOUNT ``` | ``` srvctl start database -d db_unique_name -o nomount ``` |

#### Starting an Instance and Mounting a Database

You can start an instance and mount a database without opening it, allowing you to perform specific maintenance operations. For example, the database must be mounted but not open during the following tasks:

- Enabling and disabling redo log archiving options. For more information, see [Chapter 13, "Managing Archived Redo Logs"](archredo.md).
- Performing full database recovery. For more information, see [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/toc.htm)

The following command starts an instance and mounts the database, but leaves the database closed:

| SQL\*Plus | SRVCTL (When Oracle Restart Is In Use) |
| --- | --- |
| ``` STARTUP MOUNT ``` | ``` srvctl start database -d db_unique_name -o mount ``` |

#### Restricting Access to an Instance at Startup

You can start an instance, and optionally mount and open a database, in restricted mode so that the instance is available only to administrative personnel (not general database users). Use this mode of instance startup when you must accomplish one of the following tasks:

- Perform an export or import of data
- Perform a data load (with SQL\*Loader)
- Temporarily prevent typical users from using data
- Perform certain migration or upgrade operations

Typically, all users with the `CREATE SESSION` system privilege can connect to an open database. Opening a database in restricted mode allows database access only to users with both the `CREATE SESSION` and `RESTRICTED SESSION` system privilege. Only database administrators should have the `RESTRICTED SESSION` system privilege. Further, when the instance is in restricted mode, a database administrator cannot access the instance remotely through an Oracle Net listener, but can only access the instance locally from the system that the instance is running on.

The following command starts an instance (and mounts and opens the database) in restricted mode:

| SQL\*Plus | SRVCTL (When Oracle Restart Is In Use) |
| --- | --- |
| ``` STARTUP RESTRICT ``` | ``` srvctl start database -d db_unique_name -o restrict ``` |

You can use the restrict mode in combination with the mount, nomount, and open modes.

Later, use the `ALTER SYSTEM` statement to disable the `RESTRICTED SESSION` feature:

```
ALTER SYSTEM DISABLE RESTRICTED SESSION;
```

If you open the database in nonrestricted mode and later find that you must restrict access, you can use the `ALTER SYSTEM` statement to do so, as described in "Restricting Access to an Open Database".

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_2014.htm#SQLRF53082) for more information on the `ALTER SYSTEM` statement

#### Forcing an Instance to Start

In unusual circumstances, you might experience problems when attempting to start a database instance. You should not force a database to start unless you are faced with the following:

- You cannot shut down the current instance with the `SHUTDOWN NORMAL`, `SHUTDOWN IMMEDIATE`, or `SHUTDOWN TRANSACTIONAL` commands.
- You experience problems when starting an instance.

If one of these situations arises, you can usually solve the problem by starting a new instance (and optionally mounting and opening the database) using one of these commands:

| SQL\*Plus | SRVCTL (When Oracle Restart Is In Use) |
| --- | --- |
| ``` STARTUP FORCE ``` | ``` srvctl start database -d db_unique_name -o force ``` |

If an instance is running, the force mode shuts it down with mode `ABORT` before restarting it. In this case, the alert log shows the message " `Shutting down instance (abort)` " followed by " `Starting ORACLE instance (normal)`."

See Also:

"Shutting Down with the Abort Mode" to understand the side effects of aborting the current instance

#### Starting an Instance, Mounting a Database, and Starting Complete Media Recovery

If you know that media recovery is required, you can start an instance, mount a database to the instance, and have the recovery process automatically start by using one of these commands:

| SQL\*Plus | SRVCTL (When Oracle Restart Is In Use) |
| --- | --- |
| ``` STARTUP OPEN RECOVER ``` | ``` srvctl start database -d db_unique_name -o "open,recover" ``` |

If you attempt to perform recovery when no recovery is required, Oracle Database issues an error message.

#### Automatic Database Startup at Operating System Start

Many sites use procedures to enable automatic startup of one or more Oracle Database instances and databases immediately following a system start. The procedures for performing this task are specific to each operating system. For information about automatic startup, see your operating system specific Oracle documentation.

Beginning with Oracle Database 11g Release 2, the preferred (and platform-independent) method of configuring automatic startup of a database is Oracle Restart. See [Chapter 4, "Configuring Automatic Restart of an Oracle Database"](restart.md) for details.

#### Starting Remote Instances

If your local Oracle Database server is part of a distributed database, you might want to start a remote instance and database. Procedures for starting and stopping remote instances vary widely depending on communication protocol and operating system.

## Altering Database Availability

You can alter the availability of a database. You may want to do this in order to restrict access for maintenance reasons or to make the database read only. The following sections explain how to alter the availability of a database:

- Mounting a Database to an Instance
- Opening a Closed Database
- Opening a Database in Read-Only Mode
- Restricting Access to an Open Database

### Mounting a Database to an Instance

When you perform specific administrative operations, the database must be started and mounted to an instance, but closed. You can achieve this scenario by starting the instance and mounting the database.

To mount a database to a previously started, but not opened instance, use the SQL statement `ALTER DATABASE` with the `MOUNT` clause as follows:

```
ALTER DATABASE MOUNT;
```

See Also:

"Starting an Instance and Mounting a Database" for a list of operations that require the database to be mounted and closed (and procedures to start an instance and mount a database in one step)

### Opening a Closed Database

You can make a mounted but closed database available for general use by opening the database. To open a mounted database, use the `ALTER DATABASE` SQL statement with the `OPEN` clause:

```
ALTER DATABASE OPEN;
```

After executing this statement, any valid Oracle Database user with the `CREATE SESSION` system privilege can connect to the database.

### Opening a Database in Read-Only Mode

Opening a database in read-only mode enables you to query an open database while eliminating any potential for online data content changes. While opening a database in read-only mode guarantees that data file and redo log files are not written to, it does not restrict database recovery or operations that change the state of the database without generating redo. For example, you can take data files offline or bring them online since these operations do not affect data content.

If a query against a database in read-only mode uses temporary tablespace, for example to do disk sorts, then the issuer of the query must have a locally managed tablespace assigned as the default temporary tablespace. Otherwise, the query will fail. This is explained in ["Creating a Locally Managed Temporary Tablespace"](tspaces.md).

The following statement opens a database in read-only mode:

```
ALTER DATABASE OPEN READ ONLY;
```

You can also open a database in read/write mode as follows:

```
ALTER DATABASE OPEN READ WRITE;
```

However, read/write is the default mode.

Note:

You cannot use the `RESETLOGS` clause with a `READ ONLY` clause.

Limitations of a Read-only Database

- An application must not write database objects while executing against a read-only database. For example, an application writes database objects when it inserts, deletes, updates, or merges rows in a database table, including a global temporary table. An application writes database objects when it manipulates a database sequence. An application writes database objects when it locks rows, when it runs `EXPLAIN PLAN`, or when it executes DDL. Many of the functions and procedures in Oracle-supplied PL/SQL packages, such as `DBMS_SCHEDULER`, write database objects. If your application calls any of these functions and procedures, or if it performs any of the preceding operations, your application writes database objects and hence is not read-only.
- When executing on a read-only database, you must commit or roll back any in-progress transaction that involves one database link before you use another database link. This is true even if you execute a generic `SELECT` statement on the first database link and the transaction is currently read-only.
- You cannot compile or recompile PL/SQL stored procedures on a read-only database. To minimize PL/SQL invalidation because of remote procedure calls, use `REMOTE_DEPENDENCIES_MODE=SIGNATURE` in any session that does remote procedure calls on a read-only database.
- You cannot invoke a remote procedure (even a read-only remote procedure) from a read-only database if the remote procedure has never been called on the database. This limitation applies to remote procedure calls in anonymous PL/SQL blocks and in SQL statements. You can either put the remote procedure call in a stored procedure, or you can invoke the remote procedure in the database prior to it becoming read only.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_1.htm#SQLRF008) for more information about the `ALTER DATABASE` statement

### Restricting Access to an Open Database

To place an already running instance in restricted mode, use the SQL statement `ALTER SYSTEM` with the `ENABLE RESTRICTED SESSION` clause. After this statement successfully completes, only users with the `RESTRICTED` `SESSION` privilege can initiate new connections. Users connecting as `SYSDBA` or connecting with the `DBA` role have this privilege.

When you place a running instance in restricted mode, no user sessions are terminated or otherwise affected. Therefore, after placing an instance in restricted mode, consider killing (terminating) all current user sessions before performing administrative tasks.

To lift an instance from restricted mode, use `ALTER SYSTEM` with the `DISABLE RESTRICTED SESSION` clause.

See Also:

- ["Terminating Sessions"](manproc.md) for directions for killing user sessions
- "Restricting Access to an Instance at Startup" to learn some reasons for placing an instance in restricted mode

## Shutting Down a Database

When Oracle Restart is not in use, you can shut down a database instance with SQL\*Plus by connecting as `SYSOPER` or `SYSDBA` and issuing the `SHUTDOWN` command. If your database is being managed by Oracle Restart, the recommended way to shut down the database is with the [srvctl stop database](restart.md) command.

Control is not returned to the session that initiates a database shutdown until shutdown is complete. Users who attempt connections while a shutdown is in progress receive a message like the following:

```
ORA-01090: shutdown in progress - connection is not permitted
```

Note:

You cannot shut down a database if you are connected to the database through a shared server process.

There are several modes for shutting down a database: normal, immediate, transactional, and abort. Some shutdown modes wait for certain events to occur (such as transactions completing or users disconnecting) before actually bringing down the database. There is a one-hour timeout period for these events.

Details are provided in the following sections:

- Shutting Down with the Normal Mode
- Shutting Down with the Immediate Mode
- Shutting Down with the Transactional Mode
- Shutting Down with the Abort Mode
- Shutdown Timeout

See Also:

[Chapter 4, "Configuring Automatic Restart of an Oracle Database"](restart.md) for information about Oracle Restart.

### Shutting Down with the Normal Mode

To shut down a database in normal situations, use one of these commands:

| SQL\*Plus | SRVCTL (When Oracle Restart Is In Use) |
| --- | --- |
| ``` SHUTDOWN [NORMAL] ``` | ``` srvctl stop database -d db_unique_name -o normal ``` |

The `NORMAL` clause of the SQL\*Plus `SHUTDOWN` command is optional because this is the default shutdown method. For SRVCTL, if the -o option is omitted, the shutdown operation proceeds according to the stop options stored in the Oracle Restart configuration for the database. The default stop option is `immediate`.

Normal database shutdown proceeds with the following conditions:

- No new connections are allowed after the statement is issued.
- Before the database is shut down, the database waits for all currently connected users to disconnect from the database.

The next startup of the database will not require any instance recovery procedures.

### Shutting Down with the Immediate Mode

Use immediate database shutdown only in the following situations:

- To initiate an automated and unattended backup
- When a power shutdown is going to occur soon
- When the database or one of its applications is functioning irregularly and you cannot contact users to ask them to log off or they are unable to log off

To shut down a database immediately, use one of the following commands:

| SQL\*Plus | SRVCTL (When Oracle Restart Is In Use) |
| --- | --- |
| ``` SHUTDOWN IMMEDIATE ``` | ``` srvctl stop database -d db_unique_name -o immediate ``` |

Immediate database shutdown proceeds with the following conditions:

- No new connections are allowed, nor are new transactions allowed to be started, after the statement is issued.
- Any uncommitted transactions are rolled back. (If long uncommitted transactions exist, this method of shutdown might not complete quickly, despite its name.)
- Oracle Database does not wait for users currently connected to the database to disconnect. The database implicitly rolls back active transactions and disconnects all connected users.

The next startup of the database will not require any instance recovery procedures.

### Shutting Down with the Transactional Mode

When you want to perform a planned shutdown of an instance while allowing active transactions to complete first, use one of the following commands:

| SQL\*Plus | SRVCTL (When Oracle Restart Is In Use) |
| --- | --- |
| ``` SHUTDOWN TRANSACTIONAL ``` | ``` srvctl stop database -d db_unique_name -o transactional ``` |

Transactional database shutdown proceeds with the following conditions:

- No new connections are allowed, nor are new transactions allowed to be started, after the statement is issued.
- After all transactions have completed, any client still connected to the instance is disconnected.
- At this point, the instance shuts down just as it would when a `SHUTDOWN IMMEDIATE` statement is submitted.

The next startup of the database will not require any instance recovery procedures.

A transactional shutdown prevents clients from losing work, and at the same time, does not require all users to log off.

### Shutting Down with the Abort Mode

You can shut down a database instantaneously by aborting the database instance. If possible, perform this type of shutdown only in the following situations:

The database or one of its applications is functioning irregularly and none of the other types of shutdown works.

- You must shut down the database instantaneously (for example, if you know a power shutdown is going to occur in one minute).
- You experience problems when starting a database instance.

When you must do a database shutdown by aborting transactions and user connections, use one of the following commands:

| SQL\*Plus | SRVCTL (When Oracle Restart Is In Use) |
| --- | --- |
| ``` SHUTDOWN ABORT ``` | ``` srvctl stop database -d db_unique_name -o abort ``` |

An aborted database shutdown proceeds with the following conditions:

- No new connections are allowed, nor are new transactions allowed to be started, after the statement is issued.
- Current client SQL statements being processed by Oracle Database are immediately terminated.
- Uncommitted transactions are not rolled back.
- Oracle Database does not wait for users currently connected to the database to disconnect. The database implicitly disconnects all connected users.

The next startup of the database will require automatic instance recovery procedures.

### Shutdown Timeout

Shutdown modes that wait for users to disconnect or for transactions to complete have a limit on the amount of time that they wait. If all events blocking the shutdown do not occur within one hour, the shutdown operation aborts with the following message: `ORA-01013: user requested cancel of current operation`. This message is also displayed if you interrupt the shutdown process, for example by pressing `CTRL-C`. Oracle recommends that you do not attempt to interrupt an instance shutdown. Instead, allow the shutdown process to complete, and then restart the instance.

After `ORA-01013` occurs, you must consider the instance to be in an unpredictable state. You must therefore continue the shutdown process by resubmitting a `SHUTDOWN` command. If subsequent `SHUTDOWN` commands continue to fail, you must submit a `SHUTDOWN` `ABORT` command to bring down the instance. You can then restart the instance.

## Quiescing a Database

Occasionally you might want to put a database in a state that allows only DBA transactions, queries, fetches, or PL/SQL statements. Such a state is referred to as a quiesced state, in the sense that no ongoing non-DBA transactions, queries, fetches, or PL/SQL statements are running in the system.

Note:

In this discussion of quiesce database, a DBA is defined as user `SYS` or `SYSTEM`. Other users, including those with the `DBA` role, are not allowed to issue the `ALTER SYSTEM QUIESCE DATABASE` statement or proceed after the database is quiesced.

The quiesced state lets administrators perform actions that cannot safely be done otherwise. These actions include:

- Actions that fail if concurrent user transactions access the same object--for example, changing the schema of a database table or adding a column to an existing table where a no-wait lock is required.
- Actions whose undesirable intermediate effect can be seen by concurrent user transactions--for example, a multistep procedure for reorganizing a table when the table is first exported, then dropped, and finally imported. A concurrent user who attempts to access the table after it was dropped, but before import, would not have an accurate view of the situation.

Without the ability to quiesce the database, you would need to shut down the database and reopen it in restricted mode. This is a serious restriction, especially for systems requiring 24 x 7 availability. Quiescing a database is much a smaller restriction, because it eliminates the disruption to users and the downtime associated with shutting down and restarting the database.

When the database is in the quiesced state, it is through the facilities of the Database Resource Manager that non-DBA sessions are prevented from becoming active. Therefore, while this statement is in effect, any attempt to change the current resource plan will be queued until after the system is unquiesced. See [Chapter 27, "Managing Resources with Oracle Database Resource Manager"](dbrm.md) for more information about the Database Resource Manager.

### Placing a Database into a Quiesced State

To place a database into a quiesced state, issue the following SQL statement:

```
ALTER SYSTEM QUIESCE RESTRICTED;
```

Non-DBA active sessions will continue until they become inactive. An active session is one that is currently inside of a transaction, a query, a fetch, or a PL/SQL statement; or a session that is currently holding any shared resources (for example, enqueues). No inactive sessions are allowed to become active. For example, If a user issues a SQL query in an attempt to force an inactive session to become active, the query will appear to be hung. When the database is later unquiesced, the session is resumed, and the blocked action is processed.

Once all non-DBA sessions become inactive, the `ALTER SYSTEM QUIESCE RESTRICTED` statement completes, and the database is in a quiesced state. In an Oracle Real Application Clusters environment, this statement affects all instances, not just the one that issues the statement.

The `ALTER SYSTEM QUIESCE RESTRICTED` statement may wait a long time for active sessions to become inactive. You can determine the sessions that are blocking the quiesce operation by querying the `V$BLOCKING_QUIESCE` view. This view returns only a single column: `SID` (Session ID). You can join it with `V$SESSION` to get more information about the session, as shown in the following example:

```
select bl.sid, user, osuser, type, program
from v$blocking_quiesce bl, v$session se
where bl.sid = se.sid;
```

See [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm) for details on these view.

If you interrupt the request to quiesce the database, or if your session terminates abnormally before all active sessions are quiesced, then Oracle Database automatically reverses any partial effects of the statement.

For queries that are carried out by successive multiple Oracle Call Interface (OCI) fetches, the `ALTER SYSTEM QUIESCE RESTRICTED` statement does not wait for all fetches to finish. It only waits for the current fetch to finish.

For both dedicated and shared server connections, all non-DBA logins after this statement is issued are queued by the Database Resource Manager, and are not allowed to proceed. To the user, it appears as if the login is hung. The login will resume when the database is unquiesced.

The database remains in the quiesced state even if the session that issued the statement exits. A DBA must log in to the database to issue the statement that specifically unquiesces the database.

Note:

You cannot perform a cold backup when the database is in the quiesced state, because Oracle Database background processes may still perform updates for internal purposes even while the database is quiesced. In addition, the file headers of online data files continue to appear to be accessible. They do not look the same as if a clean shutdown had been performed. However, you can still take online backups while the database is in a quiesced state.

### Restoring the System to Normal Operation

The following statement restores the database to normal operation:

```
ALTER SYSTEM UNQUIESCE;
```

All non-DBA activity is allowed to proceed. In an Oracle Real Application Clusters environment, this statement is not required to be issued from the same session, or even the same instance, as that which quiesced the database. If the session issuing the `ALTER SYSTEM UNQUIESCE` statement terminates abnormally, then the Oracle Database server ensures that the unquiesce operation completes.

### Viewing the Quiesce State of an Instance

You can query the `ACTIVE_STATE` column of the `V$INSTANCE` view to see the current state of an instance. The column values has one of these values:

- `NORMAL`: Normal unquiesced state.
- `QUIESCING`: Being quiesced, but some non-DBA sessions are still active.
- `QUIESCED`: Quiesced; no non-DBA sessions are active or allowed.

## Suspending and Resuming a Database

The `ALTER SYSTEM SUSPEND` statement halts all input and output (I/O) to data files (file header and file data) and control files. The suspended state lets you back up a database without I/O interference. When the database is suspended all preexisting I/O operations are allowed to complete and any new database accesses are placed in a queued state.

The suspend command is not specific to an instance. In an Oracle Real Application Clusters environment, when you issue the suspend command on one system, internal locking mechanisms propagate the halt request across instances, thereby quiescing all active instances in a given cluster. However, if a new instance is started while another instance is being suspended, then the new instance is not suspended.

Use the `ALTER SYSTEM RESUME` statement to resume normal database operations. The `SUSPEND` and `RESUME` commands can be issued from different instances. For example, if instances 1, 2, and 3 are running, and you issue an `ALTER SYSTEM SUSPEND` statement from instance 1, then you can issue a `RESUME` statement from instance 1, 2, or 3 with the same effect.

The suspend/resume feature is useful in systems that allow you to mirror a disk or file and then split the mirror, providing an alternative backup and restore solution. If you use a system that cannot split a mirrored disk from an existing database while writes are occurring, then you can use the suspend/resume feature to facilitate the split.

The suspend/resume feature is not a suitable substitute for normal shutdown operations, because copies of a suspended database can contain uncommitted updates.

Caution:

Do not use the `ALTER SYSTEM SUSPEND` statement as a substitute for placing a tablespace in hot backup mode. Precede any database suspend operation by an `ALTER TABLESPACE BEGIN BACKUP` statement.

The following statements illustrate `ALTER SYSTEM SUSPEND/RESUME` usage. The `V$INSTANCE` view is queried to confirm database status.

```
SQL> ALTER SYSTEM SUSPEND;
System altered
SQL> SELECT DATABASE_STATUS FROM V$INSTANCE;
DATABASE_STATUS
---------
SUSPENDED

SQL> ALTER SYSTEM RESUME;
System altered
SQL> SELECT DATABASE_STATUS FROM V$INSTANCE;
DATABASE_STATUS
---------
ACTIVE
```

See Also:

[Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/osbackup.htm#BRADV204) for details about backing up a database using the database suspend/resume feature