---
title: Concepts and Administration
book: Data Guard Concepts and Administration
doc_id: E85767-01
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/sbydb/creating-oracle-data-guard-physical-standby.html
tags:
  - oracle
  - 12c
  - data-guard-concepts-and-administration
---

You can manually create a physical standby database in maximum performance mode using asynchronous redo transport and real-time apply, the default Oracle Data Guard configuration.

See the following main topics:

See Also:

- [Oracle Database Administrator's Guide](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sbydb&id=ADMIN11117) for information about creating and using server parameter files
- Enterprise Manager online help system for information about using the Oracle Data Guard broker graphical user interface (GUI) to automatically create a physical standby database
- [Creating a Standby Database with Recovery Manager](creating-data-guard-standby-database-using-RMAN.md) for information about alternative methods of creating a physical standby database that automate much of the process by using Oracle Recovery Manager (RMAN) and either backup based duplication or active duplication over a network
- [Oracle Data Guard Broker](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sbydb&id=DGBKR090) for information about configuring a database so that it can be managed by Oracle Data Guard broker

Note:

If you are working in a multitenant container database (CDB) environment, then see Creating a Physical Standby of a CDB for information about behavioral differences from non-CDB environments. For instance, in a CDB environment, many DBA views have analogous CDB views that you should use instead.

### 3.1 Preparing the Primary Database for Standby Database Creation

Before you create a standby database you must first ensure the primary database is properly configured.

Perform the following tasks on the primary database to prepare for physical standby database creation:

- Enable Forced Logging
- Configure Redo Transport Authentication
- Configure the Primary Database to Receive Redo Data
- Set Primary Database Initialization Parameters
- Enable Archiving

Note:

Perform these preparatory tasks only once. After you complete these steps, the database is prepared to serve as the primary database for one or more standby databases.

#### 3.1.1 Enable Forced Logging

As part of preparing the primary database for standby database creation, you place the primary database in `FORCE LOGGING` mode.

You can do this after database creation using the following SQL statement:

```
SQL> ALTER DATABASE FORCE LOGGING;
```

When you issue this statement, the primary database must at least be mounted (and it can also be open). This statement can take a considerable amount of time to complete, because it waits for all unlogged direct write I/O to finish.

See Also:

- [Oracle Database Administrator's Guide](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sbydb&id=ADMIN11096) for more information about the ramifications of specifying `FORCE` `LOGGING` mode

#### 3.1.2 Configure Redo Transport Authentication

Oracle Data Guard uses Oracle Net sessions to transport redo data and control messages between the members of an Oracle Data Guard configuration.

These redo transport sessions are authenticated using either the Secure Sockets Layer (SSL) protocol or a remote login password file.

SSL is used to authenticate redo transport sessions between two databases if:

- The databases are members of the same Oracle Internet Directory (OID) enterprise domain and it allows the use of current user database links
- The `LOG_ARCHIVE_DEST_` `n`, and `FAL_SERVER` database initialization parameters that correspond to the databases use Oracle Net connect descriptors configured for SSL
- Each database has an Oracle wallet or supported hardware security module that contains a user certificate with a distinguished name (DN) that matches the DN in the OID entry for the database

If the SSL authentication requirements are not met, then each member of an Oracle Data Guard configuration must be configured to use a remote login password file and every physical standby database in the configuration must have an up-to-date copy of the password file from the primary database.

Note:

As of Oracle Database 12c Release 2 (12.2.0.1) password file changes done on a primary database are automatically propagated to standby databases. The only exception to this is far sync instances. Updated password files must still be manually copied to far sync instances because far sync instances receive redo, but do not apply it. Once the password file is up-to-date at the far sync instance, the redo is automatically propagated to any standby databases that are set up to receive redo logs from that far sync instance. The password file is updated on the standby when the redo is applied.

See Also:

- [Oracle Database Administrator's Guide](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sbydb&id=ADMIN11060) and [Oracle Database Reference](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sbydb&id=REFRN10184) for more information about remote login password files
- [Oracle Database Security Guide](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sbydb&id=DBSEG070) for more information about SSL
- [Oracle Database Net Services Administrator's Guide](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sbydb&id=NETAG001) for more information about Oracle Net Services

#### 3.1.3 Configure the Primary Database to Receive Redo Data

It is a best practice to configure the primary database to receive redo if this is the first time a standby database is added to the configuration.

The primary database can then quickly transition to the standby role and begin receiving redo data, if necessary.

To create a standby redo log, use the SQL `ALTER` `DATABASE` `ADD` `STANDBY` `LOGFILE` statement. For example:

```
SQL> ALTER DATABASE ADD STANDBY LOGFILE ('/oracle/dbs/slog1.rdo') SIZE 500M;
 
SQL> ALTER DATABASE ADD STANDBY LOGFILE ('/oracle/dbs/slog2.rdo') SIZE 500M;
```

See [Configuring an Oracle Database to Receive Redo Data](oracle-data-guard-redo-transport-services.md) for a discussion of how to determine the size of each log file and the number of log groups, as well as other background information about managing standby redo logs.

#### 3.1.4 Set Primary Database Initialization Parameters

On the primary database, you define initialization parameters that control redo transport services while the database is in the primary role.

There are additional parameters you need to add that control the receipt of the redo data and apply services when the primary database is transitioned to the standby role.

The following example shows the primary role initialization parameters that you maintain on the primary database. This example represents an Oracle Data Guard configuration with a primary database located in Chicago and one physical standby database located in Boston. The parameters shown in this example are valid for the Chicago database when it is running in either the primary or the standby database role. The configuration examples use the names shown in the following table:

| Database | DB\_UNIQUE\_NAME | Oracle Net Service Name |
| --- | --- | --- |
| Primary | chicago | chicago |
| Physical standby | boston | boston |

```
DB_NAME=chicago
DB_UNIQUE_NAME=chicago
LOG_ARCHIVE_CONFIG='DG_CONFIG=(chicago,boston)'
CONTROL_FILES='/arch1/chicago/control1.ctl', '/arch2/chicago/control2.ctl'
LOG_ARCHIVE_DEST_1=
 'LOCATION=USE_DB_RECOVERY_FILE_DEST 
  VALID_FOR=(ALL_LOGFILES,ALL_ROLES)
  DB_UNIQUE_NAME=chicago'
LOG_ARCHIVE_DEST_2=
 'SERVICE=boston ASYNC
  VALID_FOR=(ONLINE_LOGFILES,PRIMARY_ROLE) 
  DB_UNIQUE_NAME=boston'
REMOTE_LOGIN_PASSWORDFILE=EXCLUSIVE
LOG_ARCHIVE_FORMAT=%t_%s_%r.arc
```

These parameters control how redo transport services transmit redo data to the standby system and the archiving of redo data on the local file system. Note that the example specifies asynchronous (`ASYNC`) network transmission to transmit redo data on the `LOG_ARCHIVE_DEST_2` initialization parameter. These are the recommended settings and require standby redo log files (see Configure the Primary Database to Receive Redo Data).

The following shows the additional standby role initialization parameters on the primary database. These parameters take effect when the primary database is transitioned to the standby role.

```
FAL_SERVER=boston
DB_FILE_NAME_CONVERT='/boston/','/chicago/'
LOG_FILE_NAME_CONVERT='/boston/','/chicago/' 
STANDBY_FILE_MANAGEMENT=AUTO
```

Specifying the initialization parameters shown above sets up the primary database to resolve gaps, converts new data file and log file path names from a new primary database, and archives the incoming redo data when this database is in the standby role. With the initialization parameters for both the primary and standby roles set as described, none of the parameters need to change after a role transition.

The following table provides a brief explanation about each parameter setting shown in the previous two examples.

| Parameter | Recommended Setting |
| --- | --- |
| [`DB_NAME`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sbydb&id=REFRN10041) | On a primary database, specify the name used when the database was created. On a physical standby database, use the `DB_NAME` of the primary database. |
| [`DB_UNIQUE_NAME`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sbydb&id=REFRN10242) | Specify a unique name for each database. This name stays with the database and does not change, even if the primary and standby databases reverse roles. |
| [`LOG_ARCHIVE_CONFIG`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sbydb&id=REFRN10237) | The `DG_CONFIG` attribute of this parameter must be explicitly set on each database in an Oracle Data Guard configuration to enable full Oracle Data Guard functionality. Set `DG_CONFIG` to a text string that contains the `DB_UNIQUE_NAME` of each database in the configuration, with each name in this list separated by a comma. |
| [`CONTROL_FILES`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sbydb&id=REFRN10021) | Specify the path name for the control files on the primary database. It is recommended that a second copy of the control file is available so an instance can be easily restarted after copying the good control file to the location of the bad control file. |
| [`LOG_ARCHIVE_DEST_n`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sbydb&id=REFRN10086) | Specify where the redo data is to be archived on the primary and standby systems.  - `LOG_ARCHIVE_DEST_1` archives redo data generated by the primary database from the local online redo log files to the local archived redo log files in /arch1/chicago/. - `LOG_ARCHIVE_DEST_2` is valid only for the primary role. This destination transmits redo data to the remote physical standby destination `boston`.  Note: If a fast recovery area was configured (with the `DB_RECOVERY_FILE_DEST` initialization parameter) and you have not explicitly configured a local archiving destination with the `LOCATION` attribute, Oracle Data Guard automatically uses the `LOG_ARCHIVE_DEST_1` initialization parameter (if it has not already been set) as the default destination for local archiving. Also, see [LOG\_ARCHIVE\_DEST\_n Parameter Attributes](LOG_ARCHIVE_DEST_n-parameter-attributes.md) for complete `LOG_ARCHIVE_DEST_` `n` information. |
| [`REMOTE_LOGIN_PASSWORDFILE`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sbydb&id=REFRN10184) | This parameter must be set to `EXCLUSIVE` or `SHARED` if a remote login password file is used to authenticate administrative users or redo transport sessions. |
| [`LOG_ARCHIVE_FORMAT`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sbydb&id=REFRN10089) | Specify the format for the archived redo log files using a thread (%t), sequence number (%s), and resetlogs ID (%r). |
| [`FAL_SERVER`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sbydb&id=REFRN10056) | Specify the Oracle Net service name of the FAL server (typically this is the database running in the primary role). When the Chicago database is running in the standby role, it uses the Boston database as the FAL server from which to fetch (request) missing archived redo log files if Boston is unable to automatically send the missing log files. |
| [`DB_FILE_NAME_CONVERT`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sbydb&id=REFRN10038) | Specify the path name and filename location of the standby database data files followed by the primary location. This parameter converts the path names of the primary database data files to the standby data file path names. This parameter is used only to convert path names for physical standby databases. Multiple pairs of paths may be specified by this parameter. |
| [`LOG_FILE_NAME_CONVERT`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sbydb&id=REFRN10098) | Specify the location of the standby database online redo log files followed by the primary location. This parameter converts the path names of the primary database log files to the path names on the standby database. Multiple pairs of paths may be specified by this parameter. |
| [`STANDBY_FILE_MANAGEMENT`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sbydb&id=REFRN10212) | Set to `AUTO` so when data files are added to or dropped from the primary database, corresponding changes are made automatically to the standby database. |

Note:

Review the initialization parameter file for additional parameters that may need to be modified. For example, you may need to modify the dump destination parameters if the directory location on the standby database is different from those specified on the primary database.

#### 3.1.5 Enable Archiving

If archiving is not enabled, then you must put the primary database in `ARCHIVELOG` mode and enable automatic archiving.

Issue the following SQL statements:

```
SQL> SHUTDOWN IMMEDIATE;
SQL> STARTUP MOUNT;
SQL> ALTER DATABASE ARCHIVELOG;
SQL> ALTER DATABASE OPEN;
```

See [Oracle Database Administrator's Guide](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sbydb&id=ADMIN008) for information about archiving.

### 3.2 Step-by-Step Instructions for Creating a Physical Standby Database

These are the tasks you perform to create a physical standby database.

The information in this topic is written at a level of detail that requires you to already have a thorough understanding of the following topics:

- Database administrator authentication
- Database initialization parameters
- Managing redo logs, data files, and control files
- Managing archived redo logs
- Fast recovery areas
- Oracle Net configuration

Table 3-1 provides a checklist of the tasks that you perform to create a physical standby database and the database or databases on which you perform each task.

Table 3-1 Creating a Physical Standby Database

| Task | Database |
| --- | --- |
| Create a Backup Copy of the Primary Database Data Files | Primary |
| Create a Control File for the Standby Database | Primary |
| Create a Parameter File for the Standby Database | Primary |
| Copy Files from the Primary System to the Standby System | Primary |
| Set Up the Environment to Support the Standby Database | Standby |
| Start the Physical Standby Database | Standby |
| Verify the Physical Standby Database Is Performing Properly | Standby |

#### 3.2.1 Creating a Physical Standby Task 1: Create a Backup Copy of the Primary Database Data Files

You can use any backup copy of the primary database to create the physical standby database, as long as you have the necessary archived redo log files to completely recover the database.

You can use any backup copy of the primary database to create the physical standby database, as long as you have the necessary archived redo log files to completely recover the database. Oracle recommends that you use the Recovery Manager utility (RMAN).

See [Oracle Database High Availability Architecture and Best Practices](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sbydb&id=HAOVW132) for backup recommendations and [Oracle Database Backup and Recovery User's Guide](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sbydb&id=BRADV191) to perform a database backup operation.

#### 3.2.2 Creating a Physical Standby Task 2: Create a Control File for the Standby Database

Create the control file for the standby database (the primary database does not have to be open, but it must at least be mounted).

The following is an example of creating the control file for the standby database:

```
SQL> ALTER DATABASE CREATE STANDBY CONTROLFILE AS '/tmp/boston.ctl';
```

The `ALTER DATABASE` command designates the database that is to operate in the standby role; in this case, a database named `boston`.

You cannot use a single control file for both the primary and standby databases. They must each have their own file.

Note:

If a control file backup is taken on the primary and restored on a standby (or vice versa), then the location of the snapshot control file on the restored system is configured to be the default. (The default value for the snapshot control file name is platform-specific and dependent on Oracle home.) Manually reconfigure it to the correct value using the RMAN `CONFIGURE SNAPSHOT CONTROLFILE` command.

#### 3.2.3 Creating a Physical Standby Task 3: Create a Parameter File for the Standby Database

Create a parameter file (PFILE) from the server parameter file (SPFILE) used by the primary database.

Perform the following steps:

1. Issue a SQL statement such as the following:
	```
	SQL> CREATE PFILE='/tmp/initboston.ora' FROM SPFILE;
	```
	In Set Up the Environment to Support the Standby Database, you then create a server parameter file from this parameter file, after it has been modified to contain parameter values appropriate for use at the physical standby database.
2. Modify the parameter values in the parameter file created in the previous step.
	Although most of the initialization parameter settings in the parameter file are also appropriate for the physical standby database, some modifications must be made.
	Example 3-1 shows, in bold typeface, the parameters created earlier on the primary that must be changed.

Example 3-1 Modifying Initialization Parameters for a Physical Standby Database

```
.
.
.
DB_NAME=chicago
DB_UNIQUE_NAME=boston
LOG_ARCHIVE_CONFIG='DG_CONFIG=(chicago,boston)'
CONTROL_FILES='/arch1/boston/control1.ctl', '/arch2/boston/control2.ctl'
DB_FILE_NAME_CONVERT='/chicago/','/boston/'
LOG_FILE_NAME_CONVERT='/chicago/','/boston/'
LOG_ARCHIVE_FORMAT=log%t_%s_%r.arc
LOG_ARCHIVE_DEST_1=
 'LOCATION=USE_DB_RECOVERY_FILE_DEST
  VALID_FOR=(ALL_LOGFILES,ALL_ROLES) 
  DB_UNIQUE_NAME=boston'
LOG_ARCHIVE_DEST_2=
 'SERVICE=chicago ASYNC
  VALID_FOR=(ONLINE_LOGFILES,PRIMARY_ROLE) 
  DB_UNIQUE_NAME=chicago'
REMOTE_LOGIN_PASSWORDFILE=EXCLUSIVE
STANDBY_FILE_MANAGEMENT=AUTO
FAL_SERVER=chicago
.
.
.
```

Ensure the `COMPATIBLE` initialization parameter is set to the same value on both the primary and standby databases. If the values differ, then redo transport services may be unable to transmit redo data from the primary database to the standby databases.

It is always a good practice to use the `SHOW PARAMETERS` command to verify no other parameters need to be changed.

The following table provides a brief explanation about the parameter settings shown in Example 3-1 that have different settings from the primary database.

| Parameter | Recommended Setting |
| --- | --- |
| [`DB_UNIQUE_NAME`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sbydb&id=REFRN10242) | Specify a unique name for this database. This name stays with the database and does not change even if the primary and standby databases reverse roles. |
| [`CONTROL_FILES`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sbydb&id=REFRN10021) | Specify the path name for the control files on the standby database. Example 3-1 shows how to do this for two control files. It is recommended that a second copy of the control file is available so an instance can be easily restarted after copying the good control file to the location of the bad control file. |
| [`DB_FILE_NAME_CONVERT`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sbydb&id=REFRN10038) | Specify the path name and filename location of the primary database data files followed by the standby location. This parameter converts the path names of the primary database data files to the standby data file path names. |
| [`LOG_FILE_NAME_CONVERT`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sbydb&id=REFRN10098) | Specify the location of the primary database online redo log files followed by the standby location. This parameter converts the path names of the primary database log files to the path names on the standby database. |
| [`LOG_ARCHIVE_DEST_` `n`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sbydb&id=REFRN10086) | Specify where the redo data is to be archived. In Example 3-1:  - `LOG_ARCHIVE_DEST_1` archives redo data received from the primary database to archived redo log files in /arch1/boston/. - `LOG_ARCHIVE_DEST_2` is currently ignored because this destination is valid only for the primary role. If a switchover occurs and this instance becomes the primary database, then it transmits redo data to the remote Chicago destination.  Note: If a fast recovery area was configured (with the `DB_RECOVERY_FILE_DEST` initialization parameter) and you have not explicitly configured a local archiving destination with the `LOCATION` attribute, then Oracle Data Guard automatically uses the `LOG_ARCHIVE_DEST_1` initialization parameter (if it has not already been set) as the default destination for local archiving. Also, see [LOG\_ARCHIVE\_DEST\_n Parameter Attributes](LOG_ARCHIVE_DEST_n-parameter-attributes.md) for complete information about `LOG_ARCHIVE_DEST_` `n`. |
| [`FAL_SERVER`](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sbydb&id=REFRN10056) | Specify the Oracle Net service name of the FAL server (typically this is the database running in the primary role). When the Boston database is running in the standby role, it uses the Chicago database as the FAL server from which to fetch (request) missing archived redo log files if Chicago is unable to automatically send the missing log files. |

Note:

Review the initialization parameter file for additional parameters that may need to be modified. For example, you may need to modify the dump destination parameters if the directory location on the standby database is different from those specified on the primary database.

#### 3.2.4 Creating a Physical Standby Task 4: Copy Files from the Primary System to the Standby System

Ensure that all required directories are created. Use an operating system copy utility to copy binary files from the primary system to their correct locations on the standby system.

The binary files to copy are as follows:

- Database backup created in Create a Backup Copy of the Primary Database Data Files
- Standby control file created in Create a Control File for the Standby Database
- Initialization parameter file created in Create a Parameter File for the Standby Database

#### 3.2.5 Creating a Physical Standby Task 5: Set Up the Environment to Support the Standby Database

Set up the environment by creating a Windows-based service, a password file and an SPFILE, and setting up the Oracle Net environment.

Perform the following steps:

1. If the standby database is going to be hosted on a Windows system, then use the ORADIM utility to create a Windows service. For example:
	```
	oradim –NEW –SID boston –STARTMODE manual
	```
	The ORADIM utility automatically determines the username for which this service should be created and prompts for a password for that username (if that username needs a password). See [Oracle Database Platform Guide for Microsoft Windows](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sbydb&id=NTQRF05011) for more information about using the ORADIM utility.
2. Copy the remote login password file from the primary database system to the standby database system.
	This step is optional if operating system authentication is used for administrative users and if SSL is used for redo transport authentication. If not, then copy the remote login password file from the primary database to the appropriate directory on the physical standby database system.
	Any subsequent changes to the password file on the primary are automatically propagated to the standby. Changes to a password file can include when administrative privileges (`SYSDG`, `SYSOPER`, `SYSDBA`, and so on) are granted or revoked, and when passwords of any user with administrative privileges is changed. Updated password files must still be manually copied to far sync instances because far sync instances receive redo, but do not apply it. Once the password file is up-to-date at the far sync instance, the redo containing the password update at the primary is automatically propagated to any standby databases that are set up to receive redo from that far sync instance. The password file is updated on the standby when the redo is applied.
3. Configure and start a listener on the standby system if one is not already configured.
	See [Oracle Database Net Services Administrator's Guide.](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sbydb&id=NETAG010)
4. Create Oracle Net service names.
	On both the primary and standby systems, use Oracle Net Manager to create a network service name for the primary and standby databases that are to be used by redo transport services. The Net service names in this example are `chicago` and `boston`.
	The Oracle Net service name must resolve to a connect descriptor that uses the same protocol, host address, port, and service that you specified when you configured the listeners for the primary and standby databases. The connect descriptor must also specify that a dedicated server be used.
	See the [Oracle Database Net Services Administrator's Guide](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sbydb&id=NETAG175) for more information about service names.
5. On an idle standby database, use the SQL `CREATE` statement to create a server parameter file for the standby database from the text initialization parameter file that was edited in Task 3. For example:
	```
	SQL> CREATE SPFILE FROM PFILE='initboston.ora';
	```
6. If the primary database has a database encryption wallet, then copy it to the standby database system and configure the standby database to use this wallet.
	Note:
	The database encryption wallet must be copied from the primary database system to each standby database system whenever the master encryption key is updated.
	Encrypted data in a standby database cannot be accessed unless the standby database is configured to point to a database encryption wallet or hardware security module that contains the current master encryption key from the primary database.

#### 3.2.6 Creating a Physical Standby Task 6: Start the Physical Standby Database

These are the steps to start the physical standby database and Redo Apply.

1. On the standby database, issue the following SQL statement to start and mount the database:
	```
	SQL> STARTUP MOUNT;
	```
2. Restore the backup of the data files taken in Create a Backup Copy of the Primary Database Data Files and copied in Copy Files from the Primary System to the Standby System on the standby system.
3. On the standby database, issue the following command to start Redo Apply:
	```
	SQL> ALTER DATABASE RECOVER MANAGED STANDBY DATABASE - 
	> DISCONNECT FROM SESSION;
	```
	The statement includes the `DISCONNECT FROM SESSION` option so that Redo Apply runs in a background session.

#### 3.2.7 Creating a Physical Standby Task 7: Verify the Physical Standby Database Is Performing Properly

After you create the physical standby database and set up redo transport services, you may want to verify database modifications are being successfully transmitted from the primary database to the standby database.

On the standby database, query the `V$MANAGED_STANDBY` view to verify that redo is being transmitted from the primary database and applied to the standby database.

The following is an example of querying the `V$MANAGED_STANDBY` view:

```
SQL> SELECT CLIENT_PROCESS, PROCESS, THREAD#, SEQUENCE#, STATUS FROM 
V$MANAGED_STANDBY WHERE CLIENT_PROCESS='LGWR' OR PROCESS='MRP0';
 
CLIENT_PROCESS PROCESS   THREAD#    SEQUENCE#  STATUS
-------------- --------- ---------- ---------- ------------
N/A            MRP0      1          80         APPLYING_LOG
LGWR           RFS       1          80         IDLE
```

The query output should show one line for the primary database with a `CLIENT_PROCESS` of `LGWR`. This indicates that redo transport is functioning correctly and the primary redo thread is being sent to the standby.

Note:

If the Primary database is an Oracle RAC database, then the output contains one line with a `CLIENT_PROCESS` of `LGWR` for each primary instance that is currently active.

The query output should also show one line for the MRP. If the MRP status shows `APPLYING_LOG` and the `SEQUENCE#` is equal to the sequence number currently being sent by the primary database, then the standby has resolved all gaps and is currently in real-time apply mode.

Note:

The MRP may show a `SEQUENCE#` older than the sequence number currently being sent from the primary. This indicates that it is applying archive log files that were sent as a gap and it has not yet caught up. Once all gaps are resolved, the same query shows that the MRP is applying the current `SEQUENCE#`.

### 3.3 Creating a Physical Standby: Post-Creation Steps

After the physical standby database is running, you can upgrade the data protection mode, and you can enable Flashback Database.

- Upgrade the data protection mode
	[Oracle Data Guard Protection Modes](oracle-data-guard-protection-modes.md) provides information about configuring the different data protection modes.
- Enable Flashback Database
	Flashback Database removes the need to re-create the primary database after a failover. Flashback Database enables you to return a database to its state at a time in the recent past much faster than traditional point-in-time recovery, because it does not require restoring data files from backup nor the extensive application of redo data. You can enable Flashback Database on the primary database, the standby database, or both.

See Also:

- [Converting a Failed Primary Into a Standby Database Using Flashback Database](examples-of-using-oracle-data-guard.md) and [Using Flashback Database After Issuing an Open Resetlogs Statement](examples-of-using-oracle-data-guard.md) for scenarios showing how to use Flashback Database in an Oracle Data Guard environment
- [Oracle Database Backup and Recovery User's Guide](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sbydb&id=BRADV71000) for more information about Flashback Database

### 3.4 Using DBCA to Create a Data Guard Standby

The Database Configuration Assistant (DBCA) can also be used as a simple command-line method to create an Oracle Data Guard physical standby database.

The DBCA command qualifier used to create the physical standby database is `createDuplicateDB`.

DBCA can only be used to create standby databases for non-multitenant primary databases. In addition, this capability creates only single instance standby databases, not Oracle Real Application Clusters (Oracle RAC) databases. If required, the standby can then be converted to an Oracle RAC standby database, either manually or using Oracle Enterprise Manager Cloud Control.

The basic `createDuplicateDB` command has the following syntax:

```
dbca -createDuplicateDB 
    -gdbName global_database_name 
    -primaryDBConnectionString easy_connect_string_to_primary
    -sid database_system_identifier
    [-createAsStandby 
        [-dbUniqueName db_unique_name_for_standby]]
    [-customScripts scripts_list]
```

For more information about `createDuplicateDB` options, including the use of custom scripts, see [Oracle Database Administrator’s Guide](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sbydb&id=ADMIN-GUID-7F4B1A64-5B08-425A-A62E-854542B3FD4E).

In the following two examples the primary database is `chicago` and it resides on the primary system `myprimary.domain`. Each example creates a physical standby on the system on which the command is executed, `boston`. The `initParams` parameter is used in the examples to show how other DBCA parameters can be used in the standby creation command. In these examples, `initParams` is used to explicitly set the `INSTANCE_NAME` of the standby to match the `DB_UNIQUE_NAME`, `boston`.

This first example creates the standby database without any custom scripts being executed afterward.

```
dbca –silent -createDuplicateDB -primaryDBConnectionString  myprimary.domain:1523/chicago.domain 
-gdbName chicago.domain -sid boston -initParams instance_name=boston –createAsStandby
```
```
Enter SYS user password:
Listener config step
33% complete
Auxiliary instance creation
66% complete
RMAN duplicate
100% complete
Look at the log file " /u01/app/oracle/product/12.2.0/dbhome_1/cfgtoollogs/dbca/chicago/chicago.log" for further details.
```

The following example is exactly the same as the previous example, except that it runs a SQL script named `/tmp/test.sql` which can be used to perform post-creation operations.

```
dbca -silent -createDuplicateDB -primaryDBConnectionString  myprimary.domain:1523/chicago.domain
-gdbName chicago.domain -sid boston -initParams instance_name=boston -createAsStandby  -customScripts /tmp/test.sql
```
```
Enter SYS user password:

Listener config step
25% complete
Auxiliary instance creation
50% complete
RMAN duplicate
75% complete
Running Custom Scripts
100% complete
Look at the log file " /u01/app/oracle/product/12.2.0/dbhome_1/cfgtoollogs/dbca/chicago/chicago.log" for further details.
```

Note:

Even though it is required to have a listener running on the physical standby system, it is not necessary to configure the Oracle Net service names for the databases on either system to execute these commands. In these examples, the Easy Connect naming method was used to create a connection to the primary database, `Chicago`, to complete creation of the standby, `Boston`. Before adding the new standby to the Data Guard configuration you would first configure Oracle Net service name descriptors on both systems, as described in Step 4 in Creating a Physical Standby Task 5: Set Up the Environment to Support the Standby Database.

When these commands complete without any errors, the physical standby `Boston` is ready to be added to your Data Guard configuration. As part of adding it, you would need to define the Data Guard parameters in `Chicago` and `Boston` as shown in Creating a Physical Standby Task 3: Create a Parameter File for the Standby Database. Optionally, if you have an Oracle Data Guard broker configuration, you could use the broker `ADD DATABASE` command to add the new standby to your configuration (see [Oracle Data Guard Broker](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sbydb&id=DGBKR-GUID-EA723918-2509-4BBC-871B-163885DE3C73)).

### 3.5 Creating a Physical Standby of a CDB

You can create a physical standby of a multitenant container database (CDB) just as you can create a physical standby of a regular primary database.

The following are some of the behavioral differences to be aware of when you create and use a physical standby of a CDB:

- If you execute a switchover or failover operation, the entire CDB undergoes the role change. If you used the `ENABLED_PDBS_ON_STANDBY` intialization parameter, then be aware of the possibility that not every PDB is present in both the primary and the standby databases.
- The database role is defined at the CDB level, not at the individual container level.
- Any DDL related to role changes must be executed in the root container because a role is associated with an entire CDB. Individual pluggable databases (PDBs) do not have their own roles.
- In a physical standby of a CDB, the syntax of SQL statements is generally the same as for noncontainer databases. However, the effect of some statements, including the following, may be different:
	- `ALTER DATABASE RECOVER MANAGED STANDBY` functions only in the root container; it is not allowed in a PDB.
		- A role is associated with an entire CDB; individual PDBs do not have their own roles. Therefore, the following role change DDL associated with physical standbys affect the entire CDB:
		`ALTER DATABASE SWITCHOVER TO target_db_name`
		`ALTER DATABASE ACTIVATE PHYSICAL STANDBY`
- The `ALTER PLUGGABLE DATABASE [OPEN|CLOSE]` SQL statement is supported on the standby, provided you have already opened the root container.
- The `ALTER PLUGGABLE DATABASE RECOVER` statement is not supported on the standby. (Standby recovery is always at the CDB level.)
- To administer a multitenant environment, you must have the `CDB_DBA` role.
- Oracle recommends that the standby database have its own keystore.
- In a multitenant environment, the redo must be shipped to the root container of the standby database.
	The following is an example of how to determine whether redo is being shipped to the root container. Suppose your primary database has the following settings:
	```
	LOG_ARCHIVE_DEST_2='SERVICE=boston ASYNC VALID_FOR=(ONLINE_LOGFILES,
	PRIMARY_ROLE) DB_UNIQUE_NAME=boston'
	```
	Redo is being shipped to `boston`. The container ID (`CON_ID`) for the root container is always 1, so you must make sure that the `CON_ID` is 1 for the service `boston`. To do this, check the service name in the `tnsnames.ora` file. For example:
	```
	boston = (DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)(HOST=boston-server)(PORT=1521))
	(CONNECT_DATA=(SERVICE_NAME=boston.us.example.com))
	```
	The service name for `boston` is `boston.us.example.com`.
	On the standby database, query the `CDB_SERVICES` view to determine the `CON_ID`. For example:
	```
	SQL> SELECT NAME, CON_ID FROM CDB_SERVICES;
	NAME                                 CON_ID
	---------------------------------------------
	boston.us.example.com                 1
	```
	The query result shows that the `CON_ID` for `boston` is 1.

See Also:

- [Oracle Database Concepts](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sbydb&id=CNCPT89249) for more information about CDBs
- [Oracle Database Advanced Security Guide](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sbydb&id=ASOAG10284) for more information about creating keystores

### 3.6 Creating a PDB in a Primary Database

In an Oracle Data Guard configuration, a PDB on a primary database is created in the same way that a PDB on a regular database is created.

The steps to create a PDB on a regular database are documented in the [Oracle Database Administrator's Guide](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sbydb&id=ADMIN13549). Before following those steps, note the following:

- In Oracle Database 12c Release 1 (12.1), you could only specify whether a PDB was created and recovered in all (`ALL`) standbys or in no (`NONE`) standbys when adding a PDB to the primary database. As of Oracle Database 12c Release 2 (12.2.0.1), you can specify a subset of PDBs to be replicated on a physical standby of a multitenant container database (CDB), instead of having to choose either all PDBs or none. To do so, use the `ENABLED_PDBS_ON_STANDBY` initialization parameter to specify a list of PDBs or use the enhanced `STANDBYS` qualifier on the `CREATE PLUGGABLE DATABASE` statement, or both. PDBs that are not enabled on a standby CDB can remain disabled (true SUBSET Standby) or they can be enabled at a later date when all the required files are available at the standby CDB.
- The `ENABLED_PDBS_ON_STANDBY` parameter is valid only on a physical standby; it is ignored by primary databases. (It can be set on a primary database to be used if that database ever becomes a standby database.) It can be used to specify which PDBs should or should not be enabled on a physical standby database. If the parameter is not specified, then all PDBs in the CDB are created on the standby unless the `STANDBYS` clause is used. See [ENABLED\_PDBS\_ON\_STANDBY](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sbydb&id=REFRN-GUID-A2EC2381-D9C0-4612-87C9-A225C7BCE8C4) for more information about this parameter.
- To specify in which standby CDBs the new PDB being created is to be included, you can also use the `STANDBYS` clause of the SQL `CREATE PLUGGABLE DATABASE` statement. The syntax is as follows:
	```
	create pluggable database … STANDBYS={('cdb_name', 'cdb_name', ...) | NONE | ALL [EXCEPT ('cdb_name', 'cdb_name', ...)]}
	```
	- `cdb_name` is the `DB_UNIQUE_NAME` for the physical standbys in which the PDB is to be included
		- `NONE` excludes the PDB being created from all standby CDBs. When a PDB is excluded from all standby CDBs, the PDB's data files are offline and marked as unnamed on all of the standby CDBs. Any new standby CDBs that are instantiated after the PDB has been created must disable the PDB for recovery explicitly to exclude it from the standby CDB. It is possible to enable a PDB on a standby CDB after it was excluded on that standby CDB.
		- `ALL` (the default) includes the PDB being created in all standby CDBs.
		- `EXCEPT cdb_name` includes the PDB being created in all standby CDBs except for those CDBs listed in this clause by their `DB_UNIQUE_NAME`.
	Parentheses are required around the list of CDB names and each name must be enclosed within single quotation marks. The value of `DB_UNIQUE_NAME` can be up to 30 characters and is case insensitive. The following characters are valid in a database name: alphanumeric characters, underscore (\_), number sign (#), and dollar sign ($).
	Note:
	The `EXCEPT` clause is available starting with Oracle Database 12c Release 2 (12.2.0.1).
- To create a PDB as a local clone from a different PDB or from the seed PDB within the same primary CDB, copy the data files that belong to the source PDB over to the standby database. (This step is not necessary in an Oracle Active Data Guard environment because the data files are copied automatically at the standby when the PDB is created on the standby database.)
	To perform a remote clone of a PDB from another CDB into the primary CDB, you must use the `STANDBY=NONE` clause and then copy the files and enable recovery by following the steps in the My Oracle Support note 2049127.1 at [`http://support.oracle.com`](http://support.oracle.com/).
- To create a PDB from an XML file, copy the data files specified in the XML file to the standby database.
	If your standby database has the Oracle Active Data Guard option enabled (open read-only), then copy to it the same set of PDB data files that are to be plugged into the primary database. To minimize disruptions to managed standby recovery or database sessions running on systems that have Oracle Active Data Guard enabled, you must copy these files to the standby database before plugging in the PDB at the primary database. Ensure that the files are copied to an appropriate location where they can be found by managed standby recovery:
	- If data files reside in standard operating system file systems, then the location of the files at the standby database are based on the value of the `DB_FILE_NAME_CONVERT` parameter. For more details about setting primary database initialization parameters, see Set Primary Database Initialization Parameters
		- If data files reside in ASM, then use the ASMCMD utility to copy the files to the following location at the standby database:
		```
		<db_create_file_dest>/<db_unique_name>/<GUID>/datafile
		```
		The `GUID` parameter is the global unique identifier assigned to the PDB; once assigned, it does not change. To find the value of the `GUID` parameter, query the `V$CONTAINERS` view before unplugging the PDB from its original source container. The following example shows how to find the value of the `GUID` parameter for the PDB whose PDB container ID in the source container is `3`:
		```
		SELECT guid
		  FROM V$CONTAINERS
		 WHERE con_id=3;
		 
		GUID
		 
		D98C12257A951FC4E043B623F00A7AF5
		```
		In this example, if the value of the `DB_CREATE_FILE_DEST` parameter is `+DATAFILE` and the value of the `DB_UNIQUE_NAME` parameter is `BOSTON`, then the data files are copied to:
		```
		+DATAFILE/BOSTON/D98C12257A951FC4E043B623F00A7AF5/datafile
		```

The path name of the data files on the standby database must be the same as the resultant path name when you create the PDB on the primary, unless the `DB_FILE_NAME_CONVERT` database initialization parameter has been configured on the standby. In that case, the path name of the data files on the standby database is the path name on the primary with `DB_FILE_NAME_CONVERT` applied.

See Also:

- [Oracle Database SQL Language Reference](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sbydb&id=SQLRF55686) for more information about the SQL statement `CREATE` `PLUGGABLE` `DATABASE`