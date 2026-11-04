---
title: Creating a Physical Standby Database
book: Data Guard Concepts and Administration
doc_id: E41134-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41134/create_ps.htm
tags:
  - oracle
  - 11g
  - data-guard-concepts-and-administration
---

## 3 Creating a Physical Standby Database

This chapter steps you through the process of creating a physical standby database. It includes the following main topics:

The steps described in this chapter configure the standby database for maximum performance mode, which is the default data protection mode. [Chapter 5](protection.md) provides information about configuring the different data protection modes.

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for information about creating and using server parameter files
- [Oracle Data Guard Broker](https://docs.oracle.com/cd/E11882_01/server.112/e40771/toc.htm) and the Enterprise Manager online help system for information about using the graphical user interface to automatically create a physical standby database
- [Appendix E](rcmbackp.md) for information about creating a standby database with Recovery Manager (RMAN)

## 3.1 Preparing the Primary Database for Standby Database Creation

Before you create a standby database you must first ensure the primary database is properly configured.

Table 3-1 provides a checklist of the tasks that you perform on the primary database to prepare for physical standby database creation. There is also a reference to the section that describes the task in more detail.

Table 3-1 Preparing the Primary Database for Physical Standby Database Creation

| Reference | Task |
| --- | --- |
| Section 3.1.1 | Enable Forced Logging |
| Section 3.1.2 | Configure Redo Transport Authentication |
| Section 3.1.3 | Configure the Primary Database to Receive Redo Data |
| Section 3.1.4 | Set Primary Database Initialization Parameters |
| Section 3.1.5 | Enable Archiving |

Note:

Perform these preparatory tasks only once. After you complete these steps, the database is prepared to serve as the primary database for one or more standby databases.

### 3.1.1 Enable Forced Logging

Place the primary database in `FORCE LOGGING` mode. You can do this after database creation using the following SQL statement:

```
SQL> ALTER DATABASE FORCE LOGGING;
```

When you issue this statement, the primary database must at least be mounted (and it can also be open). This statement can take a considerable amount of time to complete, because it waits for all unlogged direct write I/O to finish.

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/create.htm#ADMIN11096) for more information about the ramifications of specifying `FORCE` `LOGGING` mode

### 3.1.2 Configure Redo Transport Authentication

Data Guard uses Oracle Net sessions to transport redo data and control messages between the members of a Data Guard configuration. These redo transport sessions are authenticated using either the Secure Sockets Layer (SSL) protocol or a remote login password file.

SSL is used to authenticate redo transport sessions between two databases if:

- The databases are members of the same Oracle Internet Directory (OID) enterprise domain and it allows the use of current user database links
- The `LOG_ARCHIVE_DEST_` `n`, and `FAL_SERVER` database initialization parameters that correspond to the databases use Oracle Net connect descriptors configured for SSL
- Each database has an Oracle wallet or supported hardware security module that contains a user certificate with a distinguished name (DN) that matches the DN in the OID entry for the database

If the SSL authentication requirements are not met, each member of a Data Guard configuration must be configured to use a remote login password file and every physical standby database in the configuration must have an up-to-date copy of the password file from the primary database.

Note:

Whenever you grant or revoke the `SYSDBA` or `SYSOPER` privileges or change the login password of a user who has these privileges, you must replace the password file at each physical or snapshot standby database in the configuration with a fresh copy of the password file from the primary database.

### 3.1.3 Configure the Primary Database to Receive Redo Data

Although this task is optional, Oracle recommends that a primary database be configured to receive redo data when a Data Guard configuration is created. By following this best practice, your primary database will be ready to quickly transition to the standby role and begin receiving redo data.

See [Section 6.2.3](log_transport.md) for a complete discussion of how to configure a database to receive redo data.

### 3.1.4 Set Primary Database Initialization Parameters

On the primary database, you define initialization parameters that control redo transport services while the database is in the primary role. There are additional parameters you need to add that control the receipt of the redo data and apply services when the primary database is transitioned to the standby role.

Example 3-1 shows the primary role initialization parameters that you maintain on the primary database. This example represents a Data Guard configuration with a primary database located in Chicago and one physical standby database located in Boston. The parameters shown in Example 3-1 are valid for the Chicago database when it is running in either the primary or the standby database role. The configuration examples use the names shown in the following table:

| Database | DB\_UNIQUE\_NAME | Oracle Net Service Name |
| --- | --- | --- |
| Primary | chicago | chicago |
| Physical standby | boston | boston |

Example 3-1 Primary Database: Primary Role Initialization Parameters

```
DB_NAME=chicago
DB_UNIQUE_NAME=chicago
LOG_ARCHIVE_CONFIG='DG_CONFIG=(chicago,boston)'
CONTROL_FILES='/arch1/chicago/control1.ctl', '/arch2/chicago/control2.ctl'
LOG_ARCHIVE_DEST_1=
 'LOCATION=/arch1/chicago/ 
  VALID_FOR=(ALL_LOGFILES,ALL_ROLES)
  DB_UNIQUE_NAME=chicago'
LOG_ARCHIVE_DEST_2=
 'SERVICE=boston ASYNC
  VALID_FOR=(ONLINE_LOGFILES,PRIMARY_ROLE) 
  DB_UNIQUE_NAME=boston'
LOG_ARCHIVE_DEST_STATE_1=ENABLE
LOG_ARCHIVE_DEST_STATE_2=ENABLE
REMOTE_LOGIN_PASSWORDFILE=EXCLUSIVE
LOG_ARCHIVE_FORMAT=%t_%s_%r.arc
```

These parameters control how redo transport services transmit redo data to the standby system and the archiving of redo data on the local file system. Note that the example specifies asynchronous (`ASYNC`) network transmission to transmit redo data on the `LOG_ARCHIVE_DEST_2` initialization parameter. These are the recommended settings and require standby redo log files (see Section 3.1.3, "Configure the Primary Database to Receive Redo Data").

Example 3-2 shows the additional standby role initialization parameters on the primary database. These parameters take effect when the primary database is transitioned to the standby role.

Example 3-2 Primary Database: Standby Role Initialization Parameters

```
FAL_SERVER=boston
DB_FILE_NAME_CONVERT='boston','chicago'
LOG_FILE_NAME_CONVERT=
 '/arch1/boston/','/arch1/chicago/','/arch2/boston/','/arch2/chicago/' 
STANDBY_FILE_MANAGEMENT=AUTO
```

Specifying the initialization parameters shown in Example 3-2 sets up the primary database to resolve gaps, converts new datafile and log file path names from a new primary database, and archives the incoming redo data when this database is in the standby role. With the initialization parameters for both the primary and standby roles set as described, none of the parameters need to change after a role transition.

The following table provides a brief explanation about each parameter setting shown in Example 3-1 and Example 3-2.

| Parameter | Recommended Setting |
| --- | --- |
| [`DB_NAME`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams064.htm#REFRN10041) | On a primary database, specify the name used when the database was created. On a physical standby database, use the `DB_NAME` of the primary database. |
| [`DB_UNIQUE_NAME`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams070.htm#REFRN10242) | Specify a unique name for each database. This name stays with the database and does not change, even if the primary and standby databases reverse roles. |
| [`LOG_ARCHIVE_CONFIG`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams123.htm#REFRN10237) | The `DG_CONFIG` attribute of this parameter must be explicitly set on each database in a Data Guard configuration to enable full Data Guard functionality. Set `DG_CONFIG` to a text string that contains the `DB_UNIQUE_NAME` of each database in the configuration, with each name in this list separated by a comma. |
| [`CONTROL_FILES`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams037.htm#REFRN10021) | Specify the path name for the control files on the primary database. Example 3-1 shows how to do this for two control files. It is recommended that a second copy of the control file is available so an instance can be easily restarted after copying the good control file to the location of the bad control file. |
| [`LOG_ARCHIVE_DEST_n`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams126.htm#REFRN10087) | Specify where the redo data is to be archived on the primary and standby systems. In Example 3-1: - `LOG_ARCHIVE_DEST_1` archives redo data generated by the primary database from the local online redo log files to the local archived redo log files in /arch1/chicago/. - `LOG_ARCHIVE_DEST_2` is valid only for the primary role. This destination transmits redo data to the remote physical standby destination `boston`.  Note: If a fast recovery area was configured (with the `DB_RECOVERY_FILE_DEST` initialization parameter) and you have not explicitly configured a local archiving destination with the `LOCATION` attribute, Data Guard automatically uses the `LOG_ARCHIVE_DEST_1` initialization parameter (if it has not already been set) as the default destination for local archiving. Also, see [Chapter 15](log_arch_dest_param.md) for complete `LOG_ARCHIVE_DEST_` `n` information. |
| [`LOG_ARCHIVE_DEST_STATE_n`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams126.htm#REFRN10087) | Specify `ENABLE` to allow redo transport services to transmit redo data to the specified destination. |
| [`REMOTE_LOGIN_PASSWORDFILE`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams212.htm#REFRN10184) | This parameter must be set to `EXCLUSIVE` or `SHARED` if a remote login password file is used to authenticate administrative users or redo transport sessions. |
| [`LOG_ARCHIVE_FORMAT`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams128.htm#REFRN10089) | Specify the format for the archived redo log files using a thread (%t), sequence number (%s), and resetlogs ID (%r). |
| [`FAL_SERVER`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams089.htm#REFRN10056) | Specify the Oracle Net service name of the FAL server (typically this is the database running in the primary role). When the Chicago database is running in the standby role, it uses the Boston database as the FAL server from which to fetch (request) missing archived redo log files if Boston is unable to automatically send the missing log files. |
| [`DB_FILE_NAME_CONVERT`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams057.htm#REFRN10038) | Specify the path name and filename location of the standby database datafiles followed by the primary location. This parameter converts the path names of the primary database datafiles to the standby datafile path names. If the standby database is on the same system as the primary database or if the directory structure where the datafiles are located on the standby site is different from the primary site, then this parameter is required. Note that this parameter is used only to convert path names for physical standby databases. Multiple pairs of paths may be specified by this parameter. |
| [`LOG_FILE_NAME_CONVERT`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams137.htm#REFRN10098) | Specify the location of the standby database online redo log files followed by the primary location. This parameter converts the path names of the primary database log files to the path names on the standby database. If the standby database is on the same system as the primary database or if the directory structure where the log files are located on the standby system is different from the primary system, then this parameter is required. Multiple pairs of paths may be specified by this parameter. |
| [`STANDBY_FILE_MANAGEMENT`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams252.htm#REFRN10212) | Set to `AUTO` so when datafiles are added to or dropped from the primary database, corresponding changes are made automatically to the standby database. |

Caution:

Review the initialization parameter file for additional parameters that may need to be modified. For example, you may need to modify the dump destination parameters if the directory location on the standby database is different from those specified on the primary database.

### 3.1.5 Enable Archiving

If archiving is not enabled, issue the following statements to put the primary database in `ARCHIVELOG` mode and enable automatic archiving:

```
SQL> SHUTDOWN IMMEDIATE;
SQL> STARTUP MOUNT;
SQL> ALTER DATABASE ARCHIVELOG;
SQL> ALTER DATABASE OPEN;
```

See [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for information about archiving.

## 3.2 Step-by-Step Instructions for Creating a Physical Standby Database

This section describes the tasks you perform to create a physical standby database. It is written at a level of detail that requires you to already have a thorough understanding of the following topics, which are described in the [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm), [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/toc.htm), and [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm):

- Database administrator authentication
- Database initialization parameters
- Managing redo logs, data files, and control files
- Managing archived redo logs
- Fast recovery areas
- Oracle Net Configuration

Table 3-2 provides a checklist of the tasks that you perform to create a physical standby database and the database or databases on which you perform each task. There is also a reference to the section that describes the task in more detail.

Table 3-2 Creating a Physical Standby Database

| Reference | Task | Database |
| --- | --- | --- |
| Section 3.2.1 | Create a Backup Copy of the Primary Database Datafiles | Primary |
| Section 3.2.2 | Create a Control File for the Standby Database | Primary |
| Section 3.2.3 | Create a Parameter File for the Standby Database | Primary |
| Section 3.2.4 | Copy Files from the Primary System to the Standby System | Primary |
| Section 3.2.5 | Set Up the Environment to Support the Standby Database | Standby |
| Section 3.2.6 | Start the Physical Standby Database | Standby |
| Section 3.2.7 | Verify the Physical Standby Database Is Performing Properly | Standby |

### 3.2.1 Create a Backup Copy of the Primary Database Datafiles

You can use any backup copy of the primary database to create the physical standby database, as long as you have the necessary archived redo log files to completely recover the database. Oracle recommends that you use the Recovery Manager utility (RMAN).

See [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/toc.htm) for information about how to perform a database backup operation.

### 3.2.2 Create a Control File for the Standby Database

If the backup procedure required you to shut down the primary database, issue the following SQL\*Plus statement to start the primary database:

```
SQL> STARTUP MOUNT;
```

Then, create the control file for the standby database, and open the primary database to user access, as shown in the following example:

```
SQL> ALTER DATABASE CREATE STANDBY CONTROLFILE AS '/tmp/boston.ctl';
SQL> ALTER DATABASE OPEN;
```

Note:

You cannot use a single control file for both the primary and standby databases.

### 3.2.3 Create a Parameter File for the Standby Database

Perform the following steps to create a parameter file for the standby database.

Step 1 Create a parameter file (PFILE) from the server parameter file (SPFILE) used by the primary database.

For example:

```
SQL> CREATE PFILE='/tmp/initboston.ora' FROM SPFILE;
```

In Section 3.2.5, you will create a server parameter file from this parameter file, after it has been modified to contain parameter values appropriate for use at the physical standby database.

Step 2 Modify the parameter values in the parameter file created in the previous step.

Although most of the initialization parameter settings in the parameter file are also appropriate for the physical standby database, some modifications must be made.

Example 3-3 shows, in bold typeface, the parameters from Example 3-1 and Example 3-2 that must be changed.

Example 3-3 Modifying Initialization Parameters for a Physical Standby Database

```
.
.
.
DB_NAME=chicago
DB_UNIQUE_NAME=boston
LOG_ARCHIVE_CONFIG='DG_CONFIG=(chicago,boston)'
CONTROL_FILES='/arch1/boston/control1.ctl', '/arch2/boston/control2.ctl'
DB_FILE_NAME_CONVERT='chicago','boston'
LOG_FILE_NAME_CONVERT=
 '/arch1/chicago/','/arch1/boston/','/arch2/chicago/','/arch2/boston/'
LOG_ARCHIVE_FORMAT=log%t_%s_%r.arc
LOG_ARCHIVE_DEST_1=
 'LOCATION=/arch1/boston/
  VALID_FOR=(ALL_LOGFILES,ALL_ROLES) 
  DB_UNIQUE_NAME=boston'
LOG_ARCHIVE_DEST_2=
 'SERVICE=chicago ASYNC
  VALID_FOR=(ONLINE_LOGFILES,PRIMARY_ROLE) 
  DB_UNIQUE_NAME=chicago'
LOG_ARCHIVE_DEST_STATE_1=ENABLE
LOG_ARCHIVE_DEST_STATE_2=ENABLE
REMOTE_LOGIN_PASSWORDFILE=EXCLUSIVE
STANDBY_FILE_MANAGEMENT=AUTO
FAL_SERVER=chicago
.
.
.
```

Ensure the `COMPATIBLE` initialization parameter is set to the same value on both the primary and standby databases. If the values differ, redo transport services may be unable to transmit redo data from the primary database to the standby databases.

It is always a good practice to use the `SHOW PARAMETERS` command to verify no other parameters need to be changed.

The following table provides a brief explanation about the parameter settings shown in Example 3-3 that have different settings from the primary database.

| Parameter | Recommended Setting |
| --- | --- |
| [`DB_UNIQUE_NAME`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams070.htm#REFRN10242) | Specify a unique name for this database. This name stays with the database and does not change even if the primary and standby databases reverse roles. |
| [`CONTROL_FILES`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams037.htm#REFRN10021) | Specify the path name for the control files on the standby database. Example 3-3 shows how to do this for two control files. It is recommended that a second copy of the control file is available so an instance can be easily restarted after copying the good control file to the location of the bad control file. |
| [`DB_FILE_NAME_CONVERT`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams057.htm#REFRN10038) | Specify the path name and filename location of the primary database datafiles followed by the standby location. This parameter converts the path names of the primary database datafiles to the standby datafile path names. If the standby database is on the same system as the primary database or if the directory structure where the datafiles are located on the standby site is different from the primary site, then this parameter is required. |
| [`LOG_FILE_NAME_CONVERT`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams137.htm#REFRN10098) | Specify the location of the primary database online redo log files followed by the standby location. This parameter converts the path names of the primary database log files to the path names on the standby database. If the standby database is on the same system as the primary database or if the directory structure where the log files are located on the standby system is different from the primary system, then this parameter is required. |
| [`LOG_ARCHIVE_DEST_` `n`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams125.htm#REFRN10086) | Specify where the redo data is to be archived. In Example 3-3: - `LOG_ARCHIVE_DEST_1` archives redo data received from the primary database to archived redo log files in /arch1/boston/. - `LOG_ARCHIVE_DEST_2` is currently ignored because this destination is valid only for the primary role. If a switchover occurs and this instance becomes the primary database, then it will transmit redo data to the remote Chicago destination.  Note: If a fast recovery area was configured (with the `DB_RECOVERY_FILE_DEST` initialization parameter) and you have not explicitly configured a local archiving destination with the `LOCATION` attribute, Data Guard automatically uses the `LOG_ARCHIVE_DEST_1` initialization parameter (if it has not already been set) as the default destination for local archiving. Also, see [Chapter 15](log_arch_dest_param.md) for complete information about `LOG_ARCHIVE_DEST_` `n`. |
| [`FAL_SERVER`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams089.htm#REFRN10056) | Specify the Oracle Net service name of the FAL server (typically this is the database running in the primary role). When the Boston database is running in the standby role, it uses the Chicago database as the FAL server from which to fetch (request) missing archived redo log files if Chicago is unable to automatically send the missing log files. |

Caution:

Review the initialization parameter file for additional parameters that may need to be modified. For example, you may need to modify the dump destination parameters if the directory location on the standby database is different from those specified on the primary database.

### 3.2.4 Copy Files from the Primary System to the Standby System

Use an operating system copy utility to copy the following binary files from the primary system to the standby system:

- Backup datafiles created in Section 3.2.1
- Standby control file created in Section 3.2.2
- Initialization parameter file created in Section 3.2.3

### 3.2.5 Set Up the Environment to Support the Standby Database

Perform the following steps to create a Windows-based service, create a password file, set up the Oracle Net environment, and create a SPFILE.

Step 1 Create a Windows-based service.

If the standby database will be hosted on a Windows system, use the ORADIM utility to create a Windows service. For example:

```
WINNT> oradim –NEW –SID boston –STARTMODE manual
```

See [Oracle Database Platform Guide for Microsoft Windows](https://docs.oracle.com/cd/E11882_01/win.112/e10845/toc.htm) for more information about using the ORADIM utility.

Step 2 Copy the remote login password file from the primary database system to the standby database system

If the primary database has a remote login password file, copy it to the appropriate directory on the physical standby database system. Note that the password file must be re-copied each time the `SYSDBA` or `SYSOPER` privilege is granted or revoked and whenever the login password of a user with these privileges is changed.

This step is optional if operating system authentication is used for administrative users and if SSL is used for redo transport authentication

Step 3 Configure listeners for the primary and standby databases.

On both the primary and standby sites, use Oracle Net Manager to configure a listener for the respective databases.

To restart the listeners (to pick up the new definitions), enter the following LSNRCTL utility commands on both the primary and standby systems:

```
% lsnrctl stop
% lsnrctl start
```

See [Oracle Database Net Services Administrator's Guide.](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm)

Step 4 Create Oracle Net service names.

On both the primary and standby systems, use Oracle Net Manager to create a network service name for the primary and standby databases that will be used by redo transport services.

The Oracle Net service name must resolve to a connect descriptor that uses the same protocol, host address, port, and service that you specified when you configured the listeners for the primary and standby databases. The connect descriptor must also specify that a dedicated server be used.

See the [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm) and the [Oracle Database Administrator's Guide.](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm)

Step 5 Create a server parameter file for the standby database.

On an idle standby database, use the SQL `CREATE` statement to create a server parameter file for the standby database from the text initialization parameter file that was edited in Step 2. For example:

```
SQL> CREATE SPFILE FROM PFILE='initboston.ora';
```

Step 6 Copy the primary database encryption wallet to the standby database system

If the primary database has a database encryption wallet, copy it to the standby database system and configure the standby database to use this wallet.

Note:

The database encryption wallet must be copied from the primary database system to each standby database system whenever the master encryption key is updated.

Encrypted data in a standby database cannot be accessed unless the standby database is configured to point to a database encryption wallet or hardware security module that contains the current master encryption key from the primary database.

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/asotrans.htm#ASOAG600) for more information about transparent database encryption

### 3.2.6 Start the Physical Standby Database

Perform the following steps to start the physical standby database and Redo Apply.

Step 1 Start the physical standby database.

On the standby database, issue the following SQL statement to start and mount the database:

```
SQL> STARTUP MOUNT;
```

Step 2 Prepare the Standby Database to Receive Redo Data

Prepare the standby database to receive and archive redo data from the primary database, by performing the steps described in [Section 6.2.3](log_transport.md).

Step 3 Create an Online Redo Log on the Standby Database

Although this step is optional, Oracle recommends that an online redo log be created when a standby database is created. By following this best practice, a standby database will be ready to quickly transition to the primary database role.

The size and number of redo log groups in the online redo log of a standby database should be chosen so that the standby database performs well if it transitions to the primary role.

Step 4 Start Redo Apply.

On the standby database, issue the following command to start Redo Apply:

```
SQL> ALTER DATABASE RECOVER MANAGED STANDBY DATABASE USING CURRENT LOGFILE - 
> DISCONNECT FROM SESSION;
```

The statement includes the `DISCONNECT FROM SESSION` option so that Redo Apply runs in a background session. See [Section 7.3, "Applying Redo Data to Physical Standby Databases"](log_apply.md) for more information.

The statement also includes the `USING CURRENT LOGFILE` clause so that redo can be applied as soon as it has been received. See [Section 7.3.1, "Starting Redo Apply"](log_apply.md) for more information.

### 3.2.7 Verify the Physical Standby Database Is Performing Properly

Once you create the physical standby database and set up redo transport services, you may want to verify database modifications are being successfully transmitted from the primary database to the standby database.

To see that redo data is being received on the standby database, you should first identify the existing archived redo log files on the standby database, force a log switch and archive a few online redo log files on the primary database, and then check the standby database again. The following steps show how to perform these tasks.

Step 1 Identify the existing archived redo log files.

On the standby database, query the `V$ARCHIVED_LOG` view to identify existing files in the archived redo log. For example:

```
SQL> SELECT SEQUENCE#, FIRST_TIME, NEXT_TIME -
>  FROM V$ARCHIVED_LOG ORDER BY SEQUENCE#;

 SEQUENCE# FIRST_TIME         NEXT_TIME
---------- ------------------ ------------------
         8 11-JUL-07 17:50:45 11-JUL-07 17:50:53
         9 11-JUL-07 17:50:53 11-JUL-07 17:50:58
        10 11-JUL-07 17:50:58 11-JUL-07 17:51:03

3 rows selected.
```

Step 2 Force a log switch to archive the current online redo log file.

On the primary database, issue the `ALTER SYSTEM SWITCH LOGFILE` statement to force a log switch and archive the current online redo log file group:

```
SQL> ALTER SYSTEM SWITCH LOGFILE;
```

Step 3 Verify the new redo data was archived on the standby database.

On the standby database, query the `V$ARCHIVED_LOG` view to verify the redo data was received and archived on the standby database:

```
SQL> SELECT SEQUENCE#, FIRST_TIME, NEXT_TIME -
> FROM V$ARCHIVED_LOG ORDER BY SEQUENCE#;

 SEQUENCE# FIRST_TIME         NEXT_TIME
---------- ------------------ ------------------
         8 11-JUL-07 17:50:45 11-JUL-07 17:50:53
         9 11-JUL-07 17:50:53 11-JUL-07 17:50:58
        10 11-JUL-07 17:50:58 11-JUL-07 17:51:03
        11 11-JUL-07 17:51:03 11-JUL-07 18:34:11
4 rows selected.
```

The archived redo log files are now available to be applied to the physical standby database.

Step 4 Verify that received redo has been applied.

On the standby database, query the `V$ARCHIVED_LOG` view to verify that received redo has been applied:

```
SQL> SELECT SEQUENCE#,APPLIED FROM V$ARCHIVED_LOG -
> ORDER BY SEQUENCE#;

SEQUENCE# APP
--------- ---
        8 YES
        9 YES
       10 YES
       11 IN-MEMORY
```

4 rows selected.

Note:

The value of the `APPLIED` column for the most recently received log file will be either `IN-MEMORY` or `YES` if that log file has been applied.

## 3.3 Post-Creation Steps

At this point, the physical standby database is running and can provide the maximum performance level of data protection. The following list describes additional actions you can take on the physical standby database:

- Upgrade the data protection mode
	The Data Guard configuration is initially set up in the maximum performance mode (the default).
- Enable Flashback Database
	Flashback Database removes the need to re-create the primary database after a failover. Flashback Database enables you to return a database to its state at a time in the recent past much faster than traditional point-in-time recovery, because it does not require restoring datafiles from backup nor the extensive application of redo data. You can enable Flashback Database on the primary database, the standby database, or both. See [Section 13.2](scenarios.md) and [Section 13.3](scenarios.md) for scenarios showing how to use Flashback Database in a Data Guard environment. Also, see [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/toc.htm) for more information about Flashback Database.