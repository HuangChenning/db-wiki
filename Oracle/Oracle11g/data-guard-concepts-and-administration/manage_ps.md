---
title: Managing Physical and Snapshot Standby Databases
book: Data Guard Concepts and Administration
doc_id: E41134-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41134/manage_ps.htm
tags:
  - oracle
  - 11g
  - data-guard-concepts-and-administration
---

## 9 Managing Physical and Snapshot Standby Databases

This chapter describes how to manage physical and snapshot standby databases. The following topics are discussed:

See [Oracle Data Guard Broker](https://docs.oracle.com/cd/E11882_01/server.112/e40771/toc.htm) to learn how the Data Guard broker simplifies the management of physical and snapshot standby databases.

## 9.1 Starting Up and Shutting Down a Physical Standby Database

This section describes how to start up and shut down a physical standby database.

### 9.1.1 Starting Up a Physical Standby Database

Use the SQL\*Plus `STARTUP` command to start a physical standby database. The SQL\*Plus STARTUP command starts, mounts, and opens a physical standby database in read-only mode when it is invoked without any arguments.

Once mounted or opened, a physical standby database can receive redo data from the primary database.

See [Section 7.3](log_apply.md) for information about Redo Apply and Section 9.2 for information about opening a physical standby database in read-only mode.

Note:

When Redo Apply is started on a physical standby database that has not yet received redo data from the primary database, an `ORA-01112` message may be returned. This indicates that Redo Apply is unable to determine the starting sequence number for media recovery. If this occurs, manually retrieve an archived redo log file from the primary database and register it on the standby database, or wait for redo transport to begin before starting Redo Apply.

### 9.1.2 Shutting Down a Physical Standby Database

Use the SQL\*Plus `SHUTDOWN` command to stop Redo Apply and shut down a physical standby database. Control is not returned to the session that initiates a database shutdown until shutdown is complete.

If the primary database is up and running, defer the standby destination on the primary database and perform a log switch before shutting down the physical standby database.

## 9.2 Opening a Physical Standby Database

A physical standby database can be opened for read-only access and used to offload queries from a primary database.

Note:

A physical standby database that is opened in read-only mode is subject to the same restrictions as any other Oracle database opened in read-only mode. For more information, see [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/start.htm#ADMIN11154).

If a license for the Oracle Active Data Guard option has been purchased, Redo Apply can be active while the physical standby database is open, thus allowing queries to return results that are identical to what would be returned from the primary database. This capability is known as the real-time query feature. See Section 9.2.1 for more details.

If a license for the Oracle Active Data Guard option has not been purchased, a physical standby database cannot be open while Redo Apply is active, so the following rules must be observed when opening a physical standby database instance or starting Redo Apply:

- Redo Apply must be stopped before any physical standby database instance is opened.
- If one or more physical standby instances are open, those instances must be stopped or restarted in a mounted state before starting Redo Apply.

See Also:

- [Oracle Database Licensing Information](https://docs.oracle.com/cd/E11882_01/license.112/e47877/options.htm#DBLIC141) for more information about Oracle Active Data Guard

### 9.2.1 Real-time query

The `COMPATIBLE` database initialization parameter must be set to 11.0 or higher to use the real-time query feature of the Oracle Active Data Guard option.

A physical standby database instance cannot be opened if Redo Apply is active on a mounted instance of that database. Use the following SQL statements to stop Redo Apply, open a standby instance read-only, and restart Redo Apply:

```
SQL> ALTER DATABASE RECOVER MANAGED STANDBY DATABASE CANCEL;
SQL> ALTER DATABASE OPEN;
SQL> ALTER DATABASE RECOVER MANAGED STANDBY DATABASE USING CURRENT LOGFILE -
> DISCONNECT;
```

Note:

If Redo Apply is active on an open instance, additional instances can be opened without having to stop Redo Apply.

Redo Apply cannot be started on a mounted physical standby instance if any instance of that database is open. The instance must be opened before starting Redo Apply on it.

Example: Querying V$DATABASE to Check the Standby's Open Mode

This example shows how the value of the `V$DATABASE.OPEN_MODE` column changes when a physical standby is open in real-time query mode.

1. Start up and open a physical standby instance, and perform the following SQL query to show that the database is open in read-only mode:
	```
	SQL> SELECT open_mode FROM V$DATABASE;
	 
	OPEN_MODE
	--------------------
	READ ONLY
	```
2. Issue the following SQL statement to start Redo Apply:
	```
	SQL> ALTER DATABASE RECOVER MANAGED STANDBY DATABASE USING CURRENT LOGFILE -
	> DISCONNECT;
	 
	Database altered.
	```
3. Now that the standby is in real-time query mode (that is, the standby is open in read-only mode and Redo Apply is active), the `V$DATABASE.OPEN_MODE` column changes to indicate the following:
	```
	SQL> SELECT open_mode FROM V$DATABASE;
	 
	OPEN_MODE
	--------------------
	READ ONLY WITH APPLY
	```

#### 9.2.1.1 Monitoring Apply Lag in a Real-time Query Environment

If you are using real-time query to offload queries from a primary database to a physical standby database, you may want to monitor the apply lag to ensure that it is within acceptable limits.

The current apply lag is the difference, in elapsed time, between when the last applied change became visible on the standby and when that same change was first visible on the primary. This metric is computed to the nearest second.

To obtain the apply lag, query the `V$DATAGUARD_STATS` view. For example:

```
SQL> SELECT name, value, datum_time, time_computed FROM V$DATAGUARD_STATS -
> WHERE name like 'apply lag';
     
    NAME         VALUE            DATUM_TIME              TIME_COMPUTED
    ---------    -------------    -------------------     -------------------
    apply lag    +00 00:00:00     05/27/2009 08:54:16     05/27/2009 08:54:17
```

The `apply` `lag` metric is computed using data that is periodically received from the primary database. The `DATUM_TIME` column contains a timestamp of when this data was last received by the standby database. The `TIME_COMPUTED` column contains a timestamp taken when the `apply` `lag` metric was calculated. The difference between the values in these columns should be less than 30 seconds. If the difference is larger than this, the `apply` `lag` metric may not be accurate.

To obtain a histogram that shows the history of apply lag values since the standby instance was last started, query the `V$STANDBY_EVENT_HISTOGRAM` view. For example:

```
SQL> SELECT * FROM V$STANDBY_EVENT_HISTOGRAM WHERE NAME = 'apply lag' - 
> AND COUNT > 0;

NAME             TIME       UNIT         COUNT        LAST_TIME_UPDATED
---------     ---------   --------    -----------    ------------------------
apply lag         0        seconds        79681          06/18/2009 10:05:00
apply lag         1        seconds         1006          06/18/2009 10:03:56
apply lag         2        seconds           96          06/18/2009 09:51:06
apply lag         3        seconds            4          06/18/2009 04:12:32
apply lag         4        seconds            1          06/17/2009 11:43:51
apply lag         5        seconds            1          06/17/2009 11:43:52

6 rows selected
```

To evaluate the apply lag over a time period, take a snapshot of `V$STANDBY_EVENT_HISTOGRAM` at the beginning of the time period and compare that snapshot with one taken at the end of the time period.

#### 9.2.1.2 Configuring Apply Lag Tolerance in a Real-time Query Environment

The `STANDBY_MAX_DATA_DELAY` session parameter can be used to specify a session-specific apply lag tolerance, measured in seconds, for queries issued by non-administrative users to a physical standby database that is in real-time query mode. This capability allows queries to be safely offloaded from the primary database to a physical standby database, because it is possible to detect if the standby database has become unacceptably stale.

If `STANDBY_MAX_DATA_DELAY` is set to the default value of `NONE`, queries issued to a physical standby database will be executed regardless of the apply lag on that database.

If `STANDBY_MAX_DATA_DELAY` is set to a non-zero value, a query issued to a physical standby database will be executed only if the apply lag is less than or equal to `STANDBY_MAX_DATA_DELAY`. Otherwise, an `ORA-3172` error is returned to alert the client that the apply lag is too large.

If `STANDBY_MAX_DATA_DELAY` is set to 0, a query issued to a physical standby database is guaranteed to return the exact same result as if the query were issued on the primary database, unless the standby database is lagging behind the primary database, in which case an `ORA-3172` error is returned.

Use the `ALTER SESSION` SQL statement to set `STANDBY_MAX_DATA_DELAY`. For example:

```
SQL> ALTER SESSION SET STANDBY_MAX_DATA_DELAY=2
```

#### 9.2.1.3 Forcing Redo Apply Synchronization in a Real-time Query Environment

Issue the following SQL statement on a physical standby database to ensure that all redo data received from the primary database has been applied to a physical standby database:

```
SQL> ALTER SESSION SYNC WITH PRIMARY;
```

This statement will block until all redo data received by the standby database at the time that this command is issued has been applied to the physical standby database. An `ORA-3173` error is returned immediately, and synchronization will not occur, if the redo transport status at the standby database is not SYNCHRONIZED or if Redo Apply is not active.

You can ensure that Redo Apply synchronization occurs in specific cases by using the `SYS_CONTEXT('USERENV','DATABASE_ROLE')` function to create a standby-only trigger (that is, a trigger that is enabled on the primary but that only takes certain actions if it is running on a standby). For example, you could create the following trigger that would execute the `ALTER SESSION SYNC WITH PRIMARY` statement for a specific user connection at logon:

```
CREATE TRIGGER adg_logon_sync_trigger
 AFTER LOGON ON user.schema
  begin
    if (SYS_CONTEXT('USERENV', 'DATABASE_ROLE')  IN ('PHYSICAL STANDBY')) then
      execute immediate 'alter session sync with primary';
    end if;
  end;
```

#### 9.2.1.4 Real-time Query Restrictions

The apply lag control and Redo Apply synchronization mechanisms described above require that the client be connected and issuing queries to a physical standby database that is in real-time query mode.

The following additional restrictions apply if `STANDBY_MAX_DATA_DELAY` is set to 0 or if the `ALTER SESSION SYNC WITH PRIMARY` SQL statement is used:

- The standby database must receive redo data via the SYNC transport.
- The redo transport status at the standby database must be SYNCHRONIZED and the primary database must be running in either maximum protection mode or maximum availability mode.
- Real-time apply must be enabled.
- Active Data Guard achieves high performance of real-time queries in an Oracle RAC environment through the use of cache fusion. This allows the Data Guard apply instance and queries to work out of cache and not be slowed down by disk I/O limitations. A consequence of this is that an unexpected failure of the apply instance leaves buffers in inconsistent states across all the open Oracle RAC instances. To ensure data consistency and integrity, Data Guard closes all the other open instances in the Oracle RAC configuration, and brings them to a mounted state. You must manually reopen the instances - at which time the data is automatically made consistent, followed by restarting redo apply on one of the instances. Note that in a Data Guard broker configuration, the instances are automatically reopened and redo apply is automatically restarted on one of the instances.
	See Also:
	- [Oracle Data Guard Broker](https://docs.oracle.com/cd/E11882_01/server.112/e40771/dbresource.htm#DGBKR260) for more information about how the broker handles apply instance failures
	- The My Oracle Support note 1357597.1 at `http://support.oracle.com` for additional information about apply instance failures in an Active Data Guard Oracle RAC standby

#### 9.2.1.5 Automatic Repair of Corrupt Data Blocks

If a corrupt data block is encountered when a primary database is accessed, it is automatically replaced with an uncorrupted copy of that block from a physical standby database. This requires the following conditions:

- The physical standby database must be operating in real-time query mode, which requires an Active Data Guard license.
- The physical standby database must be running real-time apply.

Also keep the following in mind:

- Automatic repair is supported with any Data Guard protection mode. However, the effectiveness of repairing a corrupt block at the primary using the noncorrupt version of the block from the standby depends on how closely the standby apply is synchronized with the redo generated by the primary.
- When an automatic block repair has been performed, a message is written to the database alert log.
- If automatic block repair is not possible, an `ORA-1578` error is returned.

If a corrupt data block is discovered on a physical standby database, the server attempts to automatically repair the corruption by obtaining a copy of the block from the primary database if the following database initialization parameters are configured on the standby database:

- The `LOG_ARCHIVE_CONFIG` parameter is configured with a `DG_CONFIG` list and a `LOG_ARCHIVE_DEST_` `n` parameter is configured for the primary database.
	or
- The `FAL_SERVER` parameter is configured and its value contains an Oracle Net service name for the primary database.

#### 9.2.1.6 Manual Repair of Corrupt Data Blocks

The RMAN `RECOVER BLOCK` command is used to manually repair a corrupted data block. This command searches several locations for an uncorrupted copy of the data block. By default, one of the locations is any available physical standby database operating in real-time query mode. The `EXCLUDE STANDBY` option of the RMAN `RECOVER BLOCK` command can be used to exclude physical standby databases as a source for replacement blocks.

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2001.htm#RCMRF140) for more information about the RMAN `RECOVER BLOCK` command

#### 9.2.1.7 Tuning Queries on a Physical Standby Database

Appendix D of the Active Data Guard 11g Best Practices white paper describes how to tune queries for optimal performance on a physical standby database. This paper is available on the Oracle Maximum Availability Architecture (MAA) home page at:

`http://www.oracle.com/goto/maa`

#### 9.2.1.8 Adding Temp Files to a Physical Standby Database

If you are using a standby to offload queries from the primary database, and the nature of the workload requires more temp table space than is automatically created when the standby is first created, then you may need to manually add additional space.

To add temporary files to the physical standby database, perform the following tasks:

1. Identify the tablespaces that should contain temporary files. Do this by entering the following command on the standby database:
	```
	SQL> SELECT TABLESPACE_NAME FROM DBA_TABLESPACES
	2> WHERE CONTENTS = 'TEMPORARY';
	 
	TABLESPACE_NAME
	--------------------------------
	TEMP1
	TEMP2
	```
2. For each tablespace identified in the previous query, add a new temporary file to the standby database. The following example adds a new temporary file called `TEMP1` with size and reuse characteristics that match the primary database temporary files:
	```
	SQL> ALTER TABLESPACE TEMP1 ADD TEMPFILE
	2> '/arch1/boston/temp01.dbf'
	3> SIZE 40M REUSE;
	```

## 9.3 Primary Database Changes That Require Manual Intervention at a Physical Standby

Most structural changes made to a primary database are automatically propagated through redo data to a physical standby database. Table 9-1 lists primary database structural and configuration changes which require manual intervention at a physical standby database.

Table 9-1 Primary Database Changes That Require Manual Intervention at a Physical Standby

| Reference | Primary Database Change | Action Required on Physical Standby Database |
| --- | --- | --- |
| Section 9.3.1 | Add a datafile or create a tablespace | No action is required if the `STANDBY_FILE_MANAGEMENT` database initialization parameter is set to `AUTO`. If this parameter is set to `MANUAL`, the new datafile must be copied to the physical standby database. |
| Section 9.3.2 | Drop or delete a tablespace or datafile | Delete datafile from primary and physical standby database after the redo data containing the `DROP` or `DELETE` command is applied to the physical standby. |
| Section 9.3.3 | Use transportable tablespaces | Move tablespace between the primary and the physical standby database. |
| Section 9.3.4 | Rename a datafile | Rename the datafile on the physical standby database. |
| Section 9.3.5 | Add or drop a redo log file group | Evaluate the configuration of the redo log and standby redo log on the physical standby database and adjust as necessary. |
| Section 9.3.6 | Perform a DML or DDL operation using the `NOLOGGING` or `UNRECOVERABLE` clause | Copy the datafile containing the unlogged changes to the physical standby database. |
| Section 9.3.7 | Grant or revoke administrative privileges or change the password of a user who has administrative privileges | If the `REMOTE_LOGIN_PASSWORDFILE` initialization parameter is set to `SHARED` or `EXCLUSIVE`, replace the password file on the physical standby database with a fresh copy of the password file from the primary database. |
| Section 9.3.8 | Reset the TDE master encryption key | Replace the database encryption wallet on the physical standby database with a fresh copy of the database encryption wallet from the primary database. |
| [Chapter 14](init_params.md) | Change initialization parameters | Evaluate whether a corresponding change must be made to the initialization parameters on the physical standby database. |

### 9.3.1 Adding a Datafile or Creating a Tablespace

The `STANDBY_FILE_MANAGEMENT` database initialization parameter controls whether the addition of a datafile to the primary database is automatically propagated to a physical standby databases.

- If the `STANDBY_FILE_MANAGEMENT` parameter on the physical standby database is set to `AUTO`, any new datafiles created on the primary database are automatically created on the physical standby database.
- If the `STANDBY_FILE_MANAGEMENT` database parameter on the physical standby database is set to `MANUAL`, a new datafile must be manually copied from the primary database to the physical standby databases after it is added to the primary database.

Note that if an existing datafile from another database is copied to a primary database, that it must also be copied to the standby database and that the standby control file must be re-created, regardless of the setting of `STANDBY_FILE_MANAGEMENT` parameter.

#### 9.3.1.1 Using the STANDBY\_FILE\_MANAGEMENT Parameter with Raw Devices

Note:

Do not use the following procedure with databases that use Oracle Managed Files. Also, if the raw device path names are not the same on the primary and standby servers, use the `DB_FILE_NAME_CONVERT` database initialization parameter to convert the path names.

By setting the `STANDBY_FILE_MANAGEMENT` parameter to `AUTO` whenever new datafiles are added or dropped on the primary database, corresponding changes are made in the standby database without manual intervention. This is true as long as the standby database is using a file system. If the standby database is using raw devices for datafiles, then the STANDBY\_FILE\_MANAGEMENT parameter will continue to work, but manual intervention is needed. This manual intervention involves ensuring the raw devices exist before Redo Apply applies the redo data that will create the new datafile.On the primary database, create a new tablespace where the datafiles reside in a raw device. At the same time, create the same raw device on the standby database. For example:

```
SQL> CREATE TABLESPACE MTS2 DATAFILE '/dev/raw/raw100' size 1m;
Tablespace created.
 
SQL> ALTER SYSTEM SWITCH LOGFILE; 
System altered.
```

The standby database automatically adds the datafile because the raw devices exist. The standby alert log shows the following:

```
Fri Apr  8 09:49:31 2005
Media Recovery Log /u01/MILLER/flash_recovery_area/MTS_STBY/archivelog/2005_04_08/o1_mf_1_7_15ffgt0z_.arc
Recovery created file /dev/raw/raw100
Successfully added datafile 6 to media recovery
Datafile #6: '/dev/raw/raw100'
Media Recovery Waiting for thread 1 sequence 8 (in transit)
```

However, if the raw device was created on the primary system but not on the standby, then Redo Apply will stop due to file-creation errors. For example, issue the following statements on the primary database:

```
SQL> CREATE TABLESPACE MTS3 DATAFILE '/dev/raw/raw101' size 1m;
Tablespace created.
 
SQL> ALTER SYSTEM SWITCH LOGFILE;
System altered.
```

The standby system does not have the `/dev/raw/raw101` raw device created. The standby alert log shows the following messages when recovering the archive:

```
Fri Apr  8 10:00:22 2005
Media Recovery Log /u01/MILLER/flash_recovery_area/MTS_STBY/archivelog/2005_04_08/o1_mf_1_8_15ffjrov_.arc
File #7 added to control file as 'UNNAMED00007'.
Originally created as:
'/dev/raw/raw101'
Recovery was unable to create the file as:
'/dev/raw/raw101'
MRP0: Background Media Recovery terminated with error 1274
Fri Apr  8 10:00:22 2005
Errors in file /u01/MILLER/MTS/dump/mts_mrp0_21851.trc:
ORA-01274: cannot add datafile '/dev/raw/raw101' - file could not be created
ORA-01119: error in creating database file '/dev/raw/raw101'
ORA-27041: unable to open file
Linux Error: 13: Permission denied
Additional information: 1
Some recovered datafiles maybe left media fuzzy
Media recovery may continue but open resetlogs may fail
Fri Apr  8 10:00:22 2005
Errors in file /u01/MILLER/MTS/dump/mts_mrp0_21851.trc:
ORA-01274: cannot add datafile '/dev/raw/raw101' - file could not be created
ORA-01119: error in creating database file '/dev/raw/raw101'
ORA-27041: unable to open file
Linux Error: 13: Permission denied
Additional information: 1
Fri Apr  8 10:00:22 2005
MTS; MRP0: Background Media Recovery process shutdown
ARCH: Connecting to console port...
```

#### 9.3.1.2 Recovering from Errors

To correct the problems described in Section 9.3.1.1, perform the following steps:

1. Create the raw device on the standby database and assign permissions to the Oracle user.
2. Query the `V$DATAFILE` view. For example:
	```
	SQL> SELECT NAME FROM V$DATAFILE;
	NAME -------------------------------------------------------------------------------
	/u01/MILLER/MTS/system01.dbf
	/u01/MILLER/MTS/undotbs01.dbf
	/u01/MILLER/MTS/sysaux01.dbf
	/u01/MILLER/MTS/users01.dbf
	/u01/MILLER/MTS/mts.dbf
	/dev/raw/raw100
	/u01/app/oracle/product/10.1.0/dbs/UNNAMED00007
	SQL> ALTER SYSTEM SET STANDBY_FILE_MANAGEMENT=MANUAL;
	SQL> ALTER DATABASE CREATE DATAFILE -
	> '/u01/app/oracle/product/10.1.0/dbs/UNNAMED00007' -
	>  AS -
	> '/dev/raw/raw101';
	```
3. In the standby alert log you should see information similar to the following:
	```
	Fri Apr  8 10:09:30 2005
	alter database create datafile
	'/dev/raw/raw101' as '/dev/raw/raw101'
	Fri Apr  8 10:09:30 2005
	Completed: alter database create datafile
	'/dev/raw/raw101' a
	```
4. On the standby database, set `STANDBY_FILE_MANAGEMENT` to `AUTO` and restart Redo Apply:
	```
	SQL> ALTER SYSTEM SET STANDBY_FILE_MANAGEMENT=AUTO;
	SQL> ALTER DATABASE RECOVER MANAGED STANDBY DATABASE DISCONNECT;
	```

At this point Redo Apply uses the new raw device datafile and recovery continues.

### 9.3.2 Dropping Tablespaces and Deleting Datafiles

When a tablespace is dropped or a datafile is deleted from a primary database, the corresponding datafile(s) must be deleted from the physical standby database. The following example shows how to drop a tablespace:

```
SQL> DROP TABLESPACE tbs_4;
SQL> ALTER SYSTEM SWITCH LOGFILE;
```

To verify that deleted datafiles are no longer part of the database, query the `V$DATAFILE` view.

Delete the corresponding datafile on the standby system after the redo data that contains the previous changes is applied to the standby database. For example:

```
% rm /disk1/oracle/oradata/payroll/s2tbs_4.dbf
```

On the primary database, after ensuring the standby database applied the redo information for the dropped tablespace, you can remove the datafile for the tablespace. For example:

```
% rm /disk1/oracle/oradata/payroll/tbs_4.dbf
```

#### 9.3.2.1 Using DROP TABLESPACE INCLUDING CONTENTS AND DATAFILES

You can issue the SQL `DROP TABLESPACE INCLUDING CONTENTS AND DATAFILES` statement on the primary database to delete the datafiles on both the primary and standby databases. To use this statement, the `STANDBY_FILE_MANAGEMENT` initialization parameter must be set to `AUTO`. For example, to drop the tablespace at the primary site:

```
SQL> DROP TABLESPACE INCLUDING CONTENTS AND DATAFILES tbs_4;
SQL> ALTER SYSTEM SWITCH LOGFILE;
```

### 9.3.3 Using Transportable Tablespaces with a Physical Standby Database

You can use the Oracle transportable tablespaces feature to move a subset of an Oracle database and plug it in to another Oracle database, essentially moving tablespaces between the databases.

To move or copy a set of tablespaces into a primary database when a physical standby is being used, perform the following steps:

1. Generate a transportable tablespace set that consists of datafiles for the set of tablespaces being transported and an export file containing structural information for the set of tablespaces.
2. Transport the tablespace set:
	1. Copy the datafiles and the export file to the primary database.
		2. Copy the datafiles to the standby database.
	The data files must have the same path name on the primary and standby databases unless the `DB_FILE_NAME_CONVERT` database initialization parameter has been configured. If `DB_FILE_NAME_CONVERT` has not been configured and the path names of the data files are not the same on the primary and standby databases, issue the `ALTER DATABASE RENAME FILE` statement to rename the data files. Do this after Redo Apply has failed to apply the redo generated by plugging the tablespace into the primary database. The `STANDBY_FILE_MANAGEMENT` initialization parameter must be set to `MANUAL` before renaming the data files, and should be reset to the previous value after renaming the data files.
3. Plug in the tablespace.
	Invoke the Data Pump utility to plug the set of tablespaces into the primary database. Redo data will be generated and applied at the standby site to plug the tablespace into the standby database.

For more information about transportable tablespaces, see [Oracle Database Administrator's Guide.](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm)

### 9.3.4 Renaming a Datafile in the Primary Database

When you rename one or more datafiles in the primary database, the change is not propagated to the standby database. Therefore, if you want to rename the same datafiles on the standby database, you must manually make the equivalent modifications on the standby database because the modifications are not performed automatically, even if the `STANDBY_FILE_MANAGEMENT` initialization parameter is set to `AUTO`.

The following steps describe how to rename a datafile in the primary database and manually propagate the changes to the standby database.

1. To rename the datafile in the primary database, take the tablespace offline:
	```
	SQL> ALTER TABLESPACE tbs_4 OFFLINE;
	```
2. Exit from the SQL prompt and issue an operating system command, such as the following UNIX `mv` command, to rename the datafile on the primary system:
	```
	% mv /disk1/oracle/oradata/payroll/tbs_4.dbf 
	/disk1/oracle/oradata/payroll/tbs_x.dbf
	```
3. Rename the datafile in the primary database and bring the tablespace back online:
	```
	SQL> ALTER TABLESPACE tbs_4 RENAME DATAFILE -
	> '/disk1/oracle/oradata/payroll/tbs_4.dbf' -
	>  TO '/disk1/oracle/oradata/payroll/tbs_x.dbf';
	SQL> ALTER TABLESPACE tbs_4 ONLINE;
	```
4. Connect to the standby database and stop Redo Apply:
	```
	SQL> ALTER DATABASE RECOVER MANAGED STANDBY DATABASE CANCEL;
	```
5. Shut down the standby database:
	```
	SQL> SHUTDOWN;
	```
6. Rename the datafile at the standby site using an operating system command, such as the UNIX `mv` command:
	```
	% mv /disk1/oracle/oradata/payroll/tbs_4.dbf /disk1/oracle/oradata/payroll/tbs_x.dbf
	```
7. Start and mount the standby database:
	```
	SQL> STARTUP MOUNT;
	```
8. Rename the datafile in the standby control file. Note that the `STANDBY_FILE_MANAGEMENT` database initialization parameter must be set to `MANUAL` in order to rename a datafile. This parameter can be reset to its previous value after renaming a datafile.
	```
	SQL> ALTER DATABASE RENAME FILE '/disk1/oracle/oradata/payroll/tbs_4.dbf' -
	> TO '/disk1/oracle/oradata/payroll/tbs_x.dbf';
	```
9. On the standby database, restart Redo Apply:
	```
	SQL> ALTER DATABASE RECOVER MANAGED STANDBY DATABASE USING CURRENT LOGFILE -
	> DISCONNECT FROM SESSION;
	```

If you do not rename the corresponding datafile at the standby system, and then try to refresh the standby database control file, the standby database will attempt to use the renamed datafile, but it will not find it. Consequently, you will see error messages similar to the following in the alert log:

```
ORA-00283: recovery session canceled due to errors
ORA-01157: cannot identify/lock datafile 4 - see DBWR trace file
ORA-01110: datafile 4: '/Disk1/oracle/oradata/payroll/tbs_x.dbf'
```

### 9.3.5 Add or Drop a Redo Log File Group

The configuration of the redo log and standby redo log on a physical standby database should be reevaluated and adjusted as necessary after adding or dropping a log file group on the primary database.

Take the following steps to add or drop a log file group or standby log file group on a physical standby database:

1. Stop Redo Apply.
2. If the `STANDBY_FILE_MANAGEMENT` initialization parameter is set to `AUTO`, change the value to `MANUAL`.
3. Add or drop a log file group.
	Note:
	An online logfile group must always be manually cleared before it can be dropped from a physical standby database. For example:
	```
	ALTER DATABASE CLEAR LOGFILE GROUP 3;
	```
	An online logfile group that has a status of `CURRENT` or `CLEARING_CURRENT` cannot be dropped from a physical standby database. An online logfile group that has this status can be dropped after a role transition.
4. Restore the `STANDBY_FILE_MANAGEMENT` initialization parameter and the Redo Apply options to their original states.
5. Restart Redo Apply.

### 9.3.6 NOLOGGING or Unrecoverable Operations

When you perform a DML or DDL operation using the `NOLOGGING` or `UNRECOVERABLE` clause, the standby database is invalidated and may require substantial DBA administrative activities to repair. You can specify the `SQL ALTER DATABASE` or `SQL ALTER TABLESPACE` statement with the `FORCE` `LOGGING` clause to override the `NOLOGGING` setting. However, this statement will not repair an already invalidated database.

See [Section 13.4](scenarios.md) for information about recovering after the `NOLOGGING` clause is used.

### 9.3.7 Refresh the Password File

If the `REMOTE_LOGIN_PASSWORDFILE` database initialization parameter is set to `SHARED` or `EXCLUSIVE`, the password file on a physical standby database must be replaced with a fresh copy from the primary database after granting or revoking administrative privileges or changing the password of a user with administrative privileges.

Failure to refresh the password file on the physical standby database may cause authentication of redo transport sessions or connections as SYSDBA or SYSOPER to the physical standby database to fail.

### 9.3.8 Reset the TDE Master Encryption Key

The database encryption wallet on a physical standby database must be replaced with a fresh copy of the database encryption wallet from the primary database whenever the TDE master encryption key is reset on the primary database.

Failure to refresh the database encryption wallet on the physical standby database will prevent access to encrypted columns on the physical standby database that are modified after the master encryption key is reset on the primary database.

## 9.4 Recovering Through the OPEN RESETLOGS Statement

Data Guard allows recovery on a physical standby database to continue after the primary database has been opened with the `RESETLOGS` option. When an `ALTER DATABASE OPEN RESETLOGS` statement is issued on the primary database, the incarnation of the database changes, creating a new branch of redo data.

When a physical standby database receives a new branch of redo data, Redo Apply automatically takes the new branch of redo data. For physical standby databases, no manual intervention is required if the standby database did not apply redo data past the new resetlogs SCN (past the start of the new branch of redo data). The following table describes how to resynchronize the standby database with the primary database branch.

| If the standby database... | Then... | Perform these steps... |
| --- | --- | --- |
| Has not applied redo data past the new resetlogs SCN (past the start of the new branch of redo data) and the new redo branch from `OPEN RESETLOGS` has been registered at the standby | Redo Apply automatically takes the new branch of redo. | No manual intervention is necessary. The MRP automatically resynchronizes the standby database with the new branch of redo data.  Note: To check whether the new redo branch has been registered at the standby, perform the following query at the primary and standby and verify that the results match:  ``` SELECT resetlogs_id, resetlogs_change# FROM V$DATABASE_INCARNATION WHERE status='CURRENT' ``` |
| Has applied redo data past the new resetlogs SCN (past the start of the new branch of redo data) and Flashback Database is enabled on the standby database | The standby database is recovered in the future of the new branch of redo data. | 1. Follow the procedure in [Section 13.3.1](scenarios.md) to flash back a physical standby database. 2. Restart Redo Apply to continue application of redo data onto new reset logs branch.  The MRP automatically resynchronizes the standby database with the new branch. |
| Has applied redo data past the new resetlogs SCN (past the start of the new branch of redo data) and Flashback Database is not enabled on the standby database | The primary database has diverged from the standby on the indicated primary database branch. | Re-create the physical standby database following the procedures in [Chapter 3](create_ps.md). |
| Is missing intervening archived redo log files from the new branch of redo data | The MRP cannot continue until the missing log files are retrieved. | Locate and register missing archived redo log files from each branch. |
| Is missing archived redo log files from the end of the previous branch of redo data. | The MRP cannot continue until the missing log files are retrieved. | Locate and register missing archived redo log files from the previous branch. |

See [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/toc.htm) for more information about database incarnations, recovering through an `OPEN RESETLOGS` operation, and Flashback Database.

## 9.5 Monitoring Primary, Physical Standby, and Snapshot Standby Databases

This section describes where to find useful information for monitoring primary and standby databases.

Table 9-2 summarizes common primary database management actions and where to find information related to these actions.

Table 9-2 Sources of Information About Common Primary Database Management Actions

| Primary Database Action | Primary Site Information | Standby Site Information |
| --- | --- | --- |
| Enable or disable a redo thread | - Alert log - `V$THREAD` | Alert log |
| Display database role, protection mode, protection level, switchover status, fast-start failover information, and so forth | `V$DATABASE` | `V$DATABASE` |
| Add or drop a redo log file group | - Alert log - `V$LOG` - `STATUS` column of `V$LOGFILE` | Alert log |
| `CREATE CONTROLFILE` | Alert log | Alert log |
| Monitor Redo Apply | - Alert log - `V$ARCHIVE_DEST_STATUS` | - Alert log - `V$ARCHIVED_LOG` - `V$LOG_HISTORY` - `V$MANAGED_STANDBY` |
| Change tablespace status | - `V$RECOVER_FILE` - `DBA_TABLESPACES` - Alert log | - `V$RECOVER_FILE` - `DBA_TABLESPACES` |
| Add or drop a datafile or tablespace | - `DBA_DATA_FILES` - Alert log | - `V$DATAFILE` - Alert log |
| Rename a datafile | - `V$DATAFILE` - Alert log | - `V$DATAFILE` - Alert log |
| Unlogged or unrecoverable operations | - `V$DATAFILE` - `V$DATABASE` | Alert log |
| Monitor redo transport | - `V$ARCHIVE_DEST_STATUS` - `V$ARCHIVED_LOG` - `V$ARCHIVE_DEST` - Alert log | - `V$ARCHIVED_LOG` - Alert log |
| Issue `OPEN RESETLOGS` or `CLEAR UNARCHIVED LOGFILES` statements | Alert log | Alert log |
| Change initialization parameter | Alert log | Alert log |

### 9.5.1 Using Views to Monitor Primary, Physical, and Snapshot Standby Databases

This section shows how to use dynamic performance views to monitor primary, physical standby, and snapshot standby databases.

The following dynamic performance views are discussed:

- V$DATABASE
- V$MANAGED\_STANDBY
- V$ARCHIVED\_LOG
- V$LOG\_HISTORY
- V$DATAGUARD\_STATUS
- V$ARCHIVE\_DEST

See Also:

[Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm) for complete reference information about views

#### 9.5.1.1 V$DATABASE

The following query displays the data protection mode, data protection level, database role, and switchover status for a primary, physical standby or snapshot standby database:

```
SQL> SELECT PROTECTION_MODE, PROTECTION_LEVEL, –
> DATABASE_ROLE ROLE, SWITCHOVER_STATUS –
> FROM V$DATABASE;
```

The following query displays fast-start failover status:

```
SQL> SELECT FS_FAILOVER_STATUS "FSFO STATUS", -
> FS_FAILOVER_CURRENT_TARGET TARGET, -
> FS_FAILOVER_THRESHOLD THRESHOLD, -
> FS_FAILOVER_OBSERVER_PRESENT "OBSERVER PRESENT" –
> FROM V$DATABASE;
```

#### 9.5.1.2 V$MANAGED\_STANDBY

The following query displays Redo Apply and redo transport status on a physical standby database:

```
SQL> SELECT PROCESS, STATUS, THREAD#, SEQUENCE#,-
> BLOCK#, BLOCKS FROM V$MANAGED_STANDBY;
 
PROCESS STATUS       THREAD#    SEQUENCE#  BLOCK#     BLOCKS
------- ------------ ---------- ---------- ---------- ----------
RFS     ATTACHED     1          947        72         72
MRP0    APPLYING_LOG 1          946        10         72
```

The sample output shows that a RFS process completed archiving a redo log file with a sequence number of 947 and that Redo Apply is actively applying an archived redo log file with a sequence number of 946. Redo Apply is currently recovering block number 10 of the 72-block archived redo log file.

#### 9.5.1.3 V$ARCHIVED\_LOG

The following query displays information about archived redo log files that have been received by a physical or snapshot standby database from a primary database:

```
SQL> SELECT THREAD#, SEQUENCE#, FIRST_CHANGE#, -
> NEXT_CHANGE# FROM V$ARCHIVED_LOG;
 
THREAD#    SEQUENCE#  FIRST_CHANGE# NEXT_CHANGE#
---------- ---------- ------------- ------------
1          945        74651         74739
1          946        74739         74772
1          947        74772         74795
```

The sample output shows that three archived redo log files have been received from the primary database.

#### 9.5.1.4 V$LOG\_HISTORY

The following query displays archived log history information:

```
SQL> SELECT THREAD#, SEQUENCE#, FIRST_CHANGE#, -
> NEXT_CHANGE# FROM V$LOG_HISTORY;
```

#### 9.5.1.5 V$DATAGUARD\_STATUS

The following query displays messages generated by Data Guard events that caused a message to be written to the alert log or to a server process trace file:

```
SQL> SELECT MESSAGE FROM V$DATAGUARD_STATUS;
```

#### 9.5.1.6 V$ARCHIVE\_DEST

The following query shows the status of each redo transport destination, and for redo transport destinations that are standby databases, the SCN of the last primary database redo applied at that standby database:

```
SQL> SELECT DEST_ID, APPLIED_SCN FROM V$ARCHIVE_DEST WHERE TARGET='STANDBY';
   
DEST_ID    STATUS    APPLIED_SCN
---------- --------- -----------
2          VALID     439054
3          VALID     439054
```

## 9.6 Tuning Redo Apply

The Active Data Guard 11g Best Practices (includes best practices for Redo Apply) white paper describes how to optimize Redo Apply and media recovery performance. This paper is available on the Oracle Maximum Availability Architecture (MAA) home page at:

`http://www.oracle.com/goto/maa`

See Also:

My Oracle Support note 454848.1 at `http://support.oracle.com` for information about the installation and use of the Standby Statspack, which can be used to collect Redo Apply performance data from a physical standby database

## 9.7 Managing a Snapshot Standby Database

A snapshot standby database is a fully updatable standby database. A snapshot standby database receives and archives, but does not apply, redo data from a primary database. Redo data received from the primary database is applied when a snapshot standby database is converted back into a physical standby database, after discarding all local updates to the snapshot standby database.

A snapshot standby database typically diverges from its primary database over time because redo data from the primary database is not applied as it is received. Local updates to the snapshot standby database will cause additional divergence. The data in the primary database is fully protected however, because a snapshot standby can be converted back into a physical standby database at any time, and the redo data received from the primary will then be applied.

A snapshot standby database provides disaster recovery and data protection benefits that are similar to those of a physical standby database. Snapshot standby databases are best used in scenarios where the benefit of having a temporary, updatable snapshot of the primary database justifies increased time to recover from primary database failures.

### 9.7.1 Converting a Physical Standby Database into a Snapshot Standby Database

Perform the following steps to convert a physical standby database into a snapshot standby database:

1. Stop Redo Apply, if it is active.
2. Ensure that the database is mounted, but not open.
3. Ensure that a fast recovery area has been configured. It is not necessary for flashback database to be enabled.
4. Issue the following SQL statement to perform the conversion:
	```
	SQL> ALTER DATABASE CONVERT TO SNAPSHOT STANDBY;
	```

Note:

A physical standby database that is managed by the Data Guard broker can be converted into a snapshot standby database using either DGMGRL or Oracle Enterprise Manager. See [Oracle Data Guard Broker](https://docs.oracle.com/cd/E11882_01/server.112/e40771/toc.htm) for more details.

### 9.7.2 Using a Snapshot Standby Database

A snapshot standby database can be opened in read-write mode and is fully updatable.

A snapshot standby database has the following characteristics:

- A snapshot standby database cannot be the target of a switchover or failover. A snapshot standby database must first be converted back into a physical standby database before performing a role transition to it.
- A snapshot standby database cannot be the only standby database in a Maximum Protection Data Guard configuration.

Note:

Flashback Database is used to convert a snapshot standby database back into a physical standby database. Any operation that cannot be reversed using Flashback Database technology will prevent a snapshot standby from being converted back to a physical standby.

For information about some of the limitations of Flashback Database, see [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/flashdb.htm#BRADV543).

### 9.7.3 Converting a Snapshot Standby Database into a Physical Standby Database

Perform the following steps to convert a snapshot standby database into a physical standby database:

1. On an Oracle Real Applications Cluster (Oracle RAC) database, shut down all but one instance.
2. Ensure that the database is mounted, but not open.
3. Issue the following SQL statement to perform the conversion:
	```
	SQL> ALTER DATABASE CONVERT TO PHYSICAL STANDBY;
	```

The database is dismounted after conversion and must be restarted.

Redo data received while the database was a snapshot standby database will be automatically applied when Redo Apply is started.

Note:

A snapshot standby database must be opened at least once in read-write mode before it can be converted into a physical standby database.