---
title: Data Guard Scenarios
book: Data Guard Concepts and Administration
doc_id: E41134-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41134/scenarios.htm
tags:
  - oracle
  - 11g
  - data-guard-concepts-and-administration
---

## 13 Data Guard Scenarios

This chapter describes scenarios you might encounter while administering your Data Guard configuration. Each scenario can be adapted to your specific environment. Table 13-1 lists the scenarios presented in this chapter.

Table 13-1 Data Guard Scenarios

| Reference | Scenario |
| --- | --- |
| Section 13.1 | Configuring Logical Standby Databases After a Failover |
| Section 13.2 | Converting a Failed Primary Into a Standby Database Using Flashback Database |
| Section 13.3 | Using Flashback Database After Issuing an Open Resetlogs Statement |
| Section 13.4 | Recovering After the NOLOGGING Clause Is Specified |
| Section 13.5 | Creating a Standby Database That Uses OMF or Oracle ASM |
| Section 13.6 | Recovering From Lost-Write Errors on a Primary Database |
| Section 13.7 | Converting a Failed Primary into a Standby Database Using RMAN Backups |
| Section 13.8 | Changing the Character Set of a Primary Without Re-Creating Physical Standbys |

## 13.1 Configuring Logical Standby Databases After a Failover

This section presents the steps required on a logical standby database after the primary database has failed over to another standby database. After a failover has occurred, a logical standby database cannot act as a standby database for the new primary database until it has applied the final redo from the original primary database. This is similar to the way the new primary database applied the final redo during the failover. The steps you must perform depend on whether the new primary database was a physical standby or a logical standby database prior to the failover:

- Section 13.1.1, "When the New Primary Database Was Formerly a Physical Standby Database"
- Section 13.1.2, "When the New Primary Database Was Formerly a Logical Standby Database"

### 13.1.1 When the New Primary Database Was Formerly a Physical Standby Database

This scenario demonstrates how to configure a logical standby database to support a new primary database that was a physical standby database before it assumed the primary role. In this scenario, SAT is the logical standby database and NYC is the primary database.

Step 1 Configure the FAL\_SERVER parameter to enable automatic recovery of log files.

On the SAT database, issue the following statement:

```
SQL> ALTER SYSTEM SET FAL_SERVER='<tns_name_to_new_primary>';
```

Step 2 Verify the logical standby database is capable of serving as a standby database to the new primary database.

Call the `PREPARE_FOR_NEW_PRIMARY` routine to verify and make ready the local logical standby for configuration with the new primary. During this step, local copies of log files that pose a risk for data divergence are deleted from the local database. These log files are then requested for re-archival directly from the new primary database.

On the SAT database, issue the following statement:

```
SQL> EXECUTE DBMS_LOGSTDBY.PREPARE_FOR_NEW_PRIMARY( -
>  former_standby_type => 'PHYSICAL' -
>  dblink => 'nyc_link');
```

Note:

If the `ORA-16109` message is returned and the 'LOGSTDBY: prepare\_for\_new\_primary failure -- applied too far, flashback required.' warning is written in the alert.log, perform the following steps:
1. Flash back the database to the SCN as stated in the warning and then
2. Repeat this step before continuing.

See Section 13.2.3 for an example of how to flash back a logical standby database to an Apply SCN.

Step 3 Start SQL Apply.

On the SAT database, issue the following statement:

```
SQL> START LOGICAL STANDBY APPLY IMMEDIATE;
```

### 13.1.2 When the New Primary Database Was Formerly a Logical Standby Database

This scenario demonstrates how to configure a logical standby database to support a new primary database that was a logical standby database before it assumed the primary role. In this scenario, SAT is the logical standby database and NYC is the primary database.

Step 1 Ensure the new primary database is ready to support logical standby databases.

On the NYC database, ensure the following query returns a value of `READY`. Otherwise the new primary database has not completed the work required to enable support for logical standby databases. For example:

```
SQL> SELECT VALUE FROM SYSTEM.LOGSTDBY$PARAMETERS - 
>   WHERE NAME = 'REINSTATEMENT_STATUS';
```

Note:

If the `VALUE` column contains `NOT POSSIBLE` it means that no logical standby database may be configured with the new primary database, and you must reinstate the database.

Step 2 Configure the FAL\_SERVER parameter to enable automatic recovery of log files.

On the SAT database, issue the following statement:

```
SQL> ALTER SYSTEM SET FAL_SERVER='<tns_name_to_new_primary>';
```

Step 3 Verify the logical standby database is capable of being a standby to the new primary.

Call the `PREPARE_FOR_NEW_PRIMARY` routine to verify and make ready the local logical standby for configuration with the new primary. During this step, local copies of log files which pose a risk for data divergence are deleted from the local database. These log files are then requested for re-archival directly from the new primary database.

On the SAT database, issue the following statement:

```
SQL> EXECUTE DBMS_LOGSTDBY.PREPARE_FOR_NEW_PRIMARY( -
> former_standby_type => 'LOGICAL' -
> dblink => 'nyc_link');
```

Note:

If the `ORA-16109` message is returned and the 'LOGSTDBY: prepare\_for\_new\_primary failure -- applied too far, flashback required.' warning is written in the alert.log file, perform the following steps:
1. Flash back the database to the SCN as stated in the warning and then
2. Repeat this step before continuing.

See Section 13.2.3 for an example of how to flash back a logical standby database to an Apply SCN.

Step 4 Start SQL Apply.

On the SAT database, issue the following statements:

```
SQL> ALTER DATABASE START LOGICAL STANDBY APPLY NEW PRIMARY nyc_link;
```

Note that you must always issue this statement without the real-time apply option enabled. If you want to enable real-time apply on the logical standby database, wait for the above statement to complete successfully, and then issue the following statements:

```
SQL> ALTER DATABASE STOP LOGICAL STANDBY APPLY;
SQL> ALTER DATABASE START LOGICAL STANDBY APPLY IMMEDIATE;
```

## 13.2 Converting a Failed Primary Into a Standby Database Using Flashback Database

After a failover occurs, the original primary database can no longer participate in the Data Guard configuration until it is repaired and established as a standby database in the new configuration. To do this, you can use the Flashback Database feature to recover the failed primary database to a point in time before the failover occurred, and then convert it into a physical or logical standby database in the new configuration. The following sections describe:

- Flashing Back a Failed Primary Database into a Physical Standby Database
- Flashing Back a Failed Primary Database into a Logical Standby Database
	Note:
	You must have already enabled Flashback Database on the original primary database before the failover. See [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/toc.htm) for more information.
- Flashing Back a Logical Standby Database to a Specific Applied SCN
	See Also:
	[Oracle Data Guard Broker](https://docs.oracle.com/cd/E11882_01/server.112/e40771/toc.htm) for automatic reinstatement of the failed primary database as a new standby database (as an alternative to using Flashback Database)

### 13.2.1 Flashing Back a Failed Primary Database into a Physical Standby Database

The following steps assume that a failover has been performed to a physical standby database and that Flashback Database was enabled on the old primary database at the time of the failover. This procedure brings the old primary database back into the Data Guard configuration as a physical standby database.

Step 1 Determine the SCN at which the old standby database became the primary database.

On the new primary database, issue the following query to determine the SCN at which the old standby database became the new primary database:

```
SQL> SELECT TO_CHAR(STANDBY_BECAME_PRIMARY_SCN) FROM V$DATABASE;
```

Step 2 Flash back the failed primary database.

Shut down the old primary database (if necessary), mount it, and flash it back to the value for `STANDBY_BECAME_PRIMARY_SCN` that was determined in Step 1.

```
SQL> SHUTDOWN IMMEDIATE;
SQL> STARTUP MOUNT;
SQL> FLASHBACK DATABASE TO SCN standby_became_primary_scn;
```

Step 3 Convert the database to a physical standby database.

Perform the following steps on the old primary database:

1. Issue the following statement on the old primary database:
	```
	SQL> ALTER DATABASE CONVERT TO PHYSICAL STANDBY;
	```
	This statement will dismount the database after successfully converting the control file to a standby control file.
2. Shut down and restart the database:
	```
	SQL> SHUTDOWN IMMEDIATE;
	SQL> STARTUP MOUNT;
	```

Step 4 Start transporting redo to the new physical standby database.

Perform the following steps on the new primary database:

1. Issue the following query to see the current state of the archive destinations:
	```
	SQL> SELECT DEST_ID, DEST_NAME, STATUS, PROTECTION_MODE, DESTINATION, -
	> ERROR,SRL FROM V$ARCHIVE_DEST_STATUS;
	```
2. If necessary, enable the destination:
	```
	SQL> ALTER SYSTEM SET LOG_ARCHIVE_DEST_STATE_n=ENABLE;
	```
3. Perform a log switch to ensure the standby database begins receiving redo data from the new primary database, and verify it was sent successfully. Issue the following SQL statements on the new primary database:
	```
	SQL> ALTER SYSTEM SWITCH LOGFILE;
	SQL> SELECT DEST_ID, DEST_NAME, STATUS, PROTECTION_MODE, DESTINATION,- 
	> ERROR,SRL FROM V$ARCHIVE_DEST_STATUS;
	```
	On the new standby database, you may also need to change the `LOG_ARCHIVE_DEST_` `n` initialization parameters so that redo transport services do not transmit redo data to other databases.

Step 5 Start Redo Apply on the new physical standby database.

Issue the following SQL statement on the new physical standby database:

```
SQL> ALTER DATABASE RECOVER MANAGED STANDBY DATABASE -
> USING CURRENT LOGFILE DISCONNECT;
```

Redo Apply automatically stops each time it encounters a redo record that is generated as the result of a role transition, so Redo Apply will need to be restarted one or more times until it has applied beyond the SCN at which the new primary database became the primary database. Once the failed primary database is restored and is running in the standby role, you can optionally perform a switchover to transition the databases to their original (pre-failure) roles. See [Section 8.2.1, "Performing a Switchover to a Physical Standby Database"](role_management.md) for more information.

### 13.2.2 Flashing Back a Failed Primary Database into a Logical Standby Database

These steps assume that the Data Guard configuration has already completed a failover involving a logical standby database and that Flashback Database has been enabled on the old primary database. This procedure brings the old primary database back into the Data Guard configuration as a new logical standby database without having to formally instantiate it from the new primary database.

Step 1 Determine the flashback SCN and the recovery SCN.

The flashback SCN is the SCN to which the failed primary database will be flashed back. The recovery SCN is the SCN to which the failed primary database will be recovered. Issue the following query on the new primary to identify these SCNs:

```
SQL> SELECT merge_change# AS FLASHBACK_SCN, processed_change# AS RECOVERY_SCN -
> FROM DBA_LOGSTDBY_HISTORY -
> WHERE stream_sequence# = (SELECT MAX(stream_sequence#)-1 -
> FROM DBA_LOGSTDBY_HISTORY);
```

Step 2 Flash back the failed primary database to the flashback SCN identified in Step 1.

```
SQL> FLASHBACK DATABASE TO SCN flashback_scn;
```

Step 3 Convert the failed primary into a physical standby, and remount the standby database in preparation for recovery.

```
SQL> ALTER DATABASE CONVERT TO PHYSICAL STANDBY;
SQL> SHUTDOWN IMMEDIATE;
SQL> STARTUP MOUNT;
```

Step 4 Configure the FAL\_SERVER parameter to enable automatic recovery of log files.

On the physical standby (failed primary) issue the following statement:

```
SQL> ALTER SYSTEM SET FAL_SERVER='<tns_name_to_new_primary>';
```

Step 5 Remove divergent archive logs from the failed primary database.

Remove any archive logs created at the time of or, after the failover operation, from the failed primary database. If the failed primary database was isolated from the standby, it could have divergent archive logs that are not consistent with the current primary database. To ensure these divergent archive logs are never applied, they must be deleted from backups and the fast recovery area. You can use the following RMAN command to delete the relevant archive logs from the fast recovery area:

```
RMAN> DELETE FORCE ARCHIVELOG FROM SCN ARCHIVE_SCN;
```

Once deleted, these divergent logs and subsequent transactions can never be recovered.

Step 6 Recover until the recovery SCN identified in Step 1.

```
SQL> RECOVER MANAGED STANDBY DATABASE UNTIL CHANGE recovery_scn;
```

Step 7 Enable the database guard.

```
SQL> ALTER DATABASE GUARD ALL;
```

Step 8 Activate the physical standby to become a primary database.

```
SQL> ALTER DATABASE ACTIVATE STANDBY DATABASE;
```

Step 9 Open the database.

```
SQL> ALTER DATABASE OPEN;
```

Step 10 Create a database link to the new primary, and start SQL Apply.

```
SQL> CREATE PUBLIC DATABASE LINK mylink -
> CONNECT TO system IDENTIFIED BY password -
> USING 'service_name_of_new_primary_database';

SQL> ALTER DATABASE START LOGICAL STANDBY APPLY NEW PRIMARY mylink;
```

The role reversal is now complete.

### 13.2.3 Flashing Back a Logical Standby Database to a Specific Applied SCN

One of the benefits of a standby database is that Flashback Database can be performed on the standby database without affecting the primary database service. Flashing back a database to a specific point in time is a straightforward task, however on a logical standby database, you may want to flash back to a time just before a known transaction was committed. Such a need can arise when configuring a logical standby database with a new primary database after a failover.

The following steps describe how to use Flashback Database and SQL Apply to recover to a known applied SCN.

Step 1 Once you have determined the known SCN at the primary (APPLIED\_SCN), issue the following query to determine the corresponding SCN at the logical standby database, to use for the flashback operation:

```
SQL> SELECT DBMS_LOGSTDBY.MAP_PRIMARY_SCN (PRIMARY_SCN => APPLIED_SCN) -
> AS TARGET_SCN FROM DUAL;
```

Step 2 Flash back the logical standby to the TARGET\_SCN returned.

Issue the following SQL statements to flash back the logical standby database to the specified SCN, and open the logical standby database with the RESETLOGS option:

```
SQL> SHUTDOWN;
SQL> STARTUP MOUNT EXCLUSIVE;
SQL> FLASHBACK DATABASE TO SCN <TARGET_SCN>;
SQL> ALTER DATABASE OPEN RESETLOGS;
```

Step 3 Confirm SQL Apply has applied less than or up to the APPLIED\_SCN.

Issue the following query:

```
SQL> SELECT APPLIED_SCN FROM V$LOGSTDBY_PROGRESS;
```

## 13.3 Using Flashback Database After Issuing an Open Resetlogs Statement

Suppose an error has occurred on the primary database in a Data Guard configuration in which the standby database is using real-time apply. In this situation, the same error will be applied on the standby database.

However, if Flashback Database is enabled, you can revert the primary and standby databases back to their pre-error condition by issuing the `FLASHBACK DATABASE` and `OPEN RESETLOGS` statements on the primary database, and then issuing a similar `FLASHBACK STANDBY DATABASE` statement on the standby database before restarting apply services. (If Flashback Database is not enabled, you need to re-create the standby database, as described in [Chapter 3](create_ps.md) and [Chapter 4](create_ls.md), after the point-in-time recovery was performed on the primary database.)

### 13.3.1 Flashing Back a Physical Standby Database to a Specific Point-in-Time

The following steps describe how to avoid re-creating a physical standby database after you issued the `OPEN RESETLOGS` statement on the primary database.

Step 1 Determine the SCN before the RESETLOGS operation occurred.

On the primary database, use the following query to obtain the value of the system change number (SCN) that is 2 SCNs before the `RESETLOGS` operation occurred on the primary database:

```
SQL> SELECT TO_CHAR(RESETLOGS_CHANGE# - 2) FROM V$DATABASE;
```

Step 2 Obtain the current SCN on the standby database.

On the standby database, obtain the current SCN with the following query:

```
SQL> SELECT TO_CHAR(CURRENT_SCN) FROM V$DATABASE;
```

Step 3 Determine if it is necessary to flash back the database.

If the value of `CURRENT_SCN` is larger than the value of resetlogs\_change# - 2, issue the following statement to flash back the standby database.

```
SQL> FLASHBACK STANDBY DATABASE TO SCN resetlogs_change# -2;
```
- If the value of `CURRENT_SCN` is less than the value of the resetlogs\_change# - 2, skip to Step 4.
- If the standby database's SCN is far enough behind the primary database's SCN, and the new branch of redo from the `OPEN RESETLOGS` statement has been registered at the standby, apply services will be able to continue through the `OPEN RESETLOGS` statement without stopping. In this case, flashing back the database is unnecessary because apply services do not stop upon reaching the `OPEN RESETLOGS` statement in the redo data.

Step 4 Restart Redo Apply.

To start Redo Apply on the physical standby database, issue the following statement:

```
SQL> ALTER DATABASE RECOVER MANAGED STANDBY DATABASE -
> USING CURRENT LOGFILE DISCONNECT;
```

The standby database is now ready to receive and apply redo from the primary database.

### 13.3.2 Flashing Back a Logical Standby Database to a Specific Point-in-Time

The following steps describe how to avoid re-creating a logical standby database after you have flashed back the primary database and opened it by issuing an `OPEN RESETLOGS` statement.

Note:

If SQL Apply detects the occurrence of a resetlogs operation at the primary database, it automatically mines the correct branch of redo, if it is possible to do so without having to flashback the logical standby database. Otherwise, SQL Apply stops with an error `ORA-1346: LogMiner processed redo beyond specified reset log scn`. In this section, it is assumed that SQL Apply has already stopped with such an error.

Step 1 Determine the SCN at the primary database.

On the primary database, use the following query to obtain the value of the system change number (SCN) that is 2 SCNs before the `RESETLOGS` operation occurred on the primary database:

```
SQL> SELECT TO_CHAR(RESETLOGS_CHANGE# - 2) AS FLASHBACK_SCN FROM V$DATABASE;
```

Step 2 Determine the target SCN for flashback operation at the logical standby.

In this step, the `FLASHBACK_SCN` value for `PRIMARY_SCN` is from Step 1.

```
SQL> SELECT DBMS_LOGSTDBY.MAP_PRIMARY_SCN (PRIMARY_SCN => FLASHBACK_SCN) -
> AS TARGET_SCN FROM DUAL;
```

Step 3 Flash back the logical standby to the TARGET\_SCN returned.

Issue the following SQL statements to flash back the logical standby database to the specified SCN, and open the logical standby database with the `RESETLOGS` option:

```
SQL> SHUTDOWN;
SQL> STARTUP MOUNT EXCLUSIVE;
SQL> FLASHBACK DATABASE TO SCN <TARGET_SCN>;
SQL> ALTER DATABASE OPEN RESETLOGS;
```

Step 4 Confirm that a log file from the primary's new branch is registered before SQL apply is started.

Issue the following query on the primary database:

```
SQL> SELECT resetlogs_id FROM V$DATABASE_INCARNATION WHERE status = 'CURRENT';
```

Issue the following query on the standby database:

```
SQL> SELECT * FROM DBA_LOGSTDBY_LOG WHERE resetlogs_id = resetlogs_id_at_primary;
```

If one or more rows are returned, it confirms that there are registered logfiles from the primary's new branch.

Step 5 Start SQL Apply.

```
SQL> ALTER DATABASE START LOGICAL STANDBY APPLY IMMEDIATE;
```

## 13.4 Recovering After the NOLOGGING Clause Is Specified

In some SQL statements, the user has the option of specifying the `NOLOGGING` clause, which indicates that the database operation is not logged in the online redo log file. Even though the user specifies the clause, a redo record is still written to the online redo log file. However, there is no data associated with this record. This can result in log application or data access errors at the standby site and manual recovery might be required to resume applying log files.

Note:

To avoid these problems, Oracle recommends that you always specify the `FORCE LOGGING` clause in the `CREATE DATABASE` or `ALTER DATABASE` statements. See the [Oracle Database Administrator's Guide.](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm)

### 13.4.1 Recovery Steps for Logical Standby Databases

For logical standby databases, when SQL Apply encounters a redo record for an operation performed on an interesting table with the `NOLOGGING` clause, it stops with the following error: `ORA-16211 unsupported record found in the archived redo log`.

To recover after the `NOLOGGING` clause is specified, re-create one or more tables from the primary database, as described in [Section 10.5.5](manage_ls.md).

Note:

In general, use of the `NOLOGGING` clause is not recommended. Optionally, if you know in advance that operations using the `NOLOGGING` clause will be performed on certain tables in the primary database, you might want to prevent the application of SQL statements associated with these tables to the logical standby database by using the `DBMS_LOGSTDBY.SKIP` procedure.

### 13.4.2 Recovery Steps for Physical Standby Databases

When the archived redo log file is copied to the standby site and applied to the physical standby database, a portion of the datafile is unusable and is marked as being unrecoverable. When you either fail over to the physical standby database, or open the standby database for read-only access, and attempt to read the range of blocks that are marked as `UNRECOVERABLE`, you will see error messages similar to the following:

```
ORA-01578: ORACLE data block corrupted (file # 1, block # 2521)
ORA-01110: data file 1: '/oracle/dbs/stdby/tbs_1.dbf'
ORA-26040: Data block was loaded using the NOLOGGING option
```

To recover after the `NOLOGGING` clause is specified, you need to copy the datafile that contains the missing redo data from the primary site to the physical standby site. Perform the following steps:

Step 1 Determine which datafiles should be copied.

Follow these steps:

1. Query the primary database:
	```
	SQL> SELECT NAME, UNRECOVERABLE_CHANGE# FROM V$DATAFILE;
	NAME                                                  UNRECOVERABLE
	----------------------------------------------------- -------------
	/oracle/dbs/tbs_1.dbf                                       5216
	/oracle/dbs/tbs_2.dbf                                          0
	/oracle/dbs/tbs_3.dbf                                          0
	/oracle/dbs/tbs_4.dbf                                          0
	4 rows selected.
	```
2. Query the standby database:
	```
	SQL> SELECT NAME, UNRECOVERABLE_CHANGE# FROM V$DATAFILE;
	NAME                                                  UNRECOVERABLE
	----------------------------------------------------- -------------
	/oracle/dbs/stdby/tbs_1.dbf                                 5186
	/oracle/dbs/stdby/tbs_2.dbf                                    0
	/oracle/dbs/stdby/tbs_3.dbf                                    0
	/oracle/dbs/stdby/tbs_4.dbf                                    0
	4 rows selected.
	```
3. Compare the query results of the primary and standby databases.
	Compare the value of the `UNRECOVERABLE_CHANGE#` column in both query results. If the value of the `UNRECOVERABLE_CHANGE#` column in the primary database is greater than the same column in the standby database, then the datafile needs to be copied from the primary site to the standby site.
	In this example, the value of the `UNRECOVERABLE_CHANGE#` in the primary database for the `tbs_1.dbf` datafile is greater, so you need to copy the `tbs_1.dbf` datafile to the standby site.

Step 2 On the primary site, back up the datafile you need to copy to the standby site.

Issue the following SQL statements:

```
SQL> ALTER TABLESPACE system BEGIN BACKUP;
SQL> EXIT;
```

Copy the needed datafile to a local directory.

```
SQL> ALTER TABLESPACE system END BACKUP;
```

Step 3 Copy the datafile to the standby database.

Copy the datafile that contains the missing redo data from the primary site to a location on the physical standby site where files related to recovery are stored.

Step 4 On the standby database, restart Redo Apply.

Issue the following SQL statement:

```
SQL> ALTER DATABASE RECOVER MANAGED STANDBY DATABASE DISCONNECT FROM SESSION;
```

You might get the following error messages (possibly in the alert log) when you try to restart Redo Apply:

```
ORA-00308: cannot open archived log 'standby1'
ORA-27037: unable to obtain file status
SVR4 Error: 2: No such file or directory
Additional information: 3
ORA-01547: warning: RECOVER succeeded but OPEN RESETLOGS would get error below
ORA-01152: file 1 was not restored from a sufficiently old backup
ORA-01110: data file 1: '/oracle/dbs/stdby/tbs_1.dbf'
```

If you get the `ORA-00308` error and Redo Apply does not terminate automatically, you can cancel recovery by issuing the following SQL statement from another terminal window:

```
SQL> ALTER DATABASE RECOVER MANAGED STANDBY DATABASE CANCEL;
```

These error messages are returned when one or more log files in the archive gap have not been successfully applied. If you receive these errors, manually resolve the gaps, and repeat Step 4. See [Section 6.4.3.1](log_transport.md) for information about manually resolving an archive gap.

### 13.4.3 Determining If a Backup Is Required After Unrecoverable Operations

If you performed unrecoverable operations on your primary database, determine if a new backup operation is required by following these steps:

1. Query the `V$DATAFILE` view on the primary database to determine the system change number (SCN) or the time at which the Oracle database generated the most recent invalidated redo data.
2. Issue the following SQL statement on the primary database to determine if you need to perform another backup:
	```
	SQL> SELECT UNRECOVERABLE_CHANGE#,-
	> TO_CHAR(UNRECOVERABLE_TIME, 'mm-dd-yyyy hh:mi:ss') -
	> FROM   V$DATAFILE;
	```
3. If the query in the previous step reports an unrecoverable time for a datafile that is more recent than the time when the datafile was last backed up, then make another backup of the datafile in question.

See [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm) for more information about the `V$DATAFILE` view.

## 13.5 Creating a Standby Database That Uses OMF or Oracle ASM

[Chapter 3](create_ps.md) and [Chapter 4](create_ls.md) described how to create physical and logical standby databases. This section augments the discussions in those chapters with additional steps that must be performed if the primary database uses Oracle Managed Files (OMF) or Oracle Automatic Storage Management (Oracle ASM).

Note:

The discussion in this section is presented at a level of detail that assumes the reader already knows how to create a physical standby database and is an experienced user of the RMAN, OMF, and Oracle ASM features. For more information, see:
- [Chapter 3](create_ps.md), [Chapter 4](create_ls.md), and [Appendix E](rcmbackp.md) for information about creating physical and logical standby databases
- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for information about OMF and Oracle ASM
- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/toc.htm) and [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/toc.htm) for information about RMAN

Perform the following tasks to prepare for standby database creation:

1. Enable forced logging on the primary database.
2. Enable archiving on the primary database.
3. Set all necessary initialization parameters on the primary database.
4. Create an initialization parameter file for the standby database.
5. If the primary database is configured to use OMF, then Oracle recommends that the standby database be configured to use OMF, too. To do this, set the `DB_CREATE_FILE_DEST` and `DB_CREATE_ONLINE_LOG_DEST_` `n` initialization parameters to appropriate values. Maintenance and future role transitions are simplified if the same disk group names are used for both the primary and standby databases.
	Note:
	If OMF parameters are set on the standby, then new files on that standby are always created as OMF, regardless of how they were created on the primary. Therefore, if both the `DB_FILE_NAME_CONVERT` and `DB_CREATE_FILE_DEST` parameters are set on the standby, the `DB_CREATE_FILE_DEST` parameter takes precedence.
6. Set the `STANDBY_FILE_MANAGEMENT` initialization parameter to `AUTO`.
7. Configure Oracle Net, as required, to allow connections to the standby database.
8. Configure redo transport authentication as described in [Section 3.1.2, "Configure Redo Transport Authentication"](create_ps.md).
9. Start the standby database instance without mounting the control file.

Perform the following tasks to create the standby database:

1. If the standby database is going to use Oracle ASM, create an Oracle ASM instance if one does not already exist on the standby database system.
2. Use the RMAN `BACKUP` command to create a backup set that contains a copy of the primary database's datafiles, archived log files, and a standby control file.
3. Use the RMAN `DUPLICATE FOR STANDBY` command to copy the datafiles, archived redo log files and standby control file in the backup set to the standby database's storage area.
	The `DUPLICATE FOR STANDBY` command performs the actual data movement at the standby instance. If the backup set is on tape, the media manager must be configured so that the standby instance can read the backup set. If the backup set is on disk, the backup pieces must be readable by the standby instance, either by making their primary path names available through NFS, or by copying them to the standby system and using RMAN `CATALOG BACKUPPIECE` command to catalog the backup pieces before restoring them.

After you successfully complete these steps, continue with the steps in [Section 3.2.7](create_ps.md), to verify the configuration of the physical standby database.

To create a logical standby database, continue with the standby database creation process described in [Chapter 4](create_ls.md), but with the following modifications:

1. For a logical standby database, setting the `DB_CREATE_FILE_DEST` parameter does not force the creation of OMF filenames. However, if this parameter was set on the primary database, it must also be set on the standby database.
2. After creating a logical standby control file on the primary system, do not use an operating system command to copy this file to the standby system. Instead, use the RMAN `RESTORE CONTROLFILE` command to restore a copy of the logical standby control file to the standby system.
3. If the primary database uses OMF files, use RMAN to update the standby database control file to use the new OMF files created on the standby database. To perform this operation, connect only to the standby database, as shown in the following example:
	```
	> RMAN TARGET sys@lstdby
	target database Password: password
	RMAN> CATALOG START WITH '+stby_diskgroup';
	RMAN> SWITCH DATABASE TO COPY;
	```

After you successfully complete these steps, continue with the steps in [Section 4.2.5](create_ls.md) to start, recover, and verify the logical standby database.

## 13.6 Recovering From Lost-Write Errors on a Primary Database

During media recovery in a Data Guard configuration, a physical standby database can be used to detect lost-write data corruption errors on the primary database. This is done by comparing SCNs of blocks stored in the redo log on the primary database to SCNs of blocks on the physical standby database. If the SCN of the block on the primary database is lower than the SCN on the standby database, then there was a lost-write error on the primary database.

In such a situation, if lost write detection (set with the [`DB_LOST_WRITE_PROTECT`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams063.htm#REFRN10268) initialization parameter) is enabled at both the primary and standby, then a recovery attempt at the standby results in an `ORA-752` error. If lost write detection is not enabled, then a recovery attempt results in an `ORA-600` `[3020]` error. However, not all `ORA-600` `[3020]` errors are due to lost writes at the primary. Therefore, before following the guidelines given in this section, you should work with your Oracle Support representative to determine whether the root cause for the `ORA-600` `[3020]` error was indeed a lost write that occurred on the primary. Also see "Resolving ORA-752 or ORA-600 \[3020\] During Standby Recovery" in the My Oracle Support Note 1265884.1 at `http://support.oracle.com`.

Note:

Because lost-write errors are detected only when a block is read into the cache by a primary and the corresponding redo is later compared to the block on the standby, there may be undetected stale blocks on both the primary and the standby that have not yet been read and verified. These stale blocks do not affect operation of the current database because until those blocks are read, all blocks that have been used up to the SCN of the currently applied redo on the standby to do queries or updates were verified by the standby.

When a primary lost-write error is detected on the standby, one or more block error messages similar to the following for each stale block are printed in the alert file of the standby database:

```
Tue Dec 12 19:09:48 2006
STANDBY REDO APPLICATION HAS DETECTED THAT THE PRIMARY DATABASE
LOST A DISK WRITE OF BLOCK 26, FILE 7
NO REDO AT OR AFTER SCN 389667 CAN BE USED FOR RECOVERY.
.
.
.
```

The alert file then shows that an `ORA-00752` error is raised on the standby database and the managed recovery is cancelled:

```
Slave exiting with ORA-752 exception
Errors in file /oracle/log/diag/rdbms/dgstwrite2/stwrite2/trace/stwrite2_pr00_23532.trc:
ORA-00752: recovery detected a lost write of a data block
ORA-10567: Redo is inconsistent with data block (file# 7, block# 26)
ORA-10564: tablespace TBS_2
ORA-01110: data file 7: '/oracle/dbs/btbs_21.f'
ORA-10561: block type 'TRANSACTION MANAGED DATA BLOCK', data object# 57503
.
.
.
```

The standby database is then recovered to a consistent state, without any corruption to its datafiles caused by this error, at the SCN printed in the alert file:

```
Recovery interrupted!
Recovered data files to a consistent state at change 389569
```

This last message may appear significantly later in the alert file and it may have a lower SCN than the block error messages. Also, the primary database may operate without visible errors even though its datafiles may already be corrupted.

The recommended procedure to recover from such errors is a failover to the physical standby, as described in the following steps.

Steps to Failover to a Physical Standby After Lost-Writes Are Detected on the Primary

1. Shut down the primary database. All data at or after SCN printed in the block error messages will be lost.
2. Issue the following SQL statement on the standby database to convert it to a primary:
	```
	SQL> ALTER DATABASE ACTIVATE STANDBY DATABASE;
	 
	Database altered.
	 
	Tue Dec 12 19:15:23 2006
	alter database activate standby database
	ALTER DATABASE ACTIVATE [PHYSICAL] STANDBY DATABASE (stwrite2)
	RESETLOGS after incomplete recovery UNTIL CHANGE 389569
	Resetting resetlogs activation ID 612657558 (0x24846996)
	Online log /oracle/dbs/bt_log1.f: Thread 1 Group 1 was previously cleared
	Online log /oracle/dbs/bt_log2.f: Thread 1 Group 2 was previously cleared
	Standby became primary SCN: 389567
	Tue Dec 12 19:15:23 2006
	Setting recovery target incarnation to 3
	Converting standby mount to primary mount.
	ACTIVATE STANDBY: Complete - Database mounted as primary (stwrite2)
	Completed: alter database activate standby database
	```
3. Back up the new primary. Performing a backup immediately is a necessary safety measure, because you cannot recover changes made after the failover without a complete backup copy of the database. As a result of the failover, the original primary database can no longer participate in the Data Guard configuration, and all other standby databases will now receive and apply redo data from the new primary database.
4. Open the new primary database.
5. An optional step is to recreate the failed primary as a physical standby. This can be done using the database backup taken at the new primary in step 3. (You cannot use flashback database or the Data Guard broker to reinstantiate the old primary database in this situation.)
	Be aware that a physical standby created using the backup taken from the new primary will have the same datafiles as the old standby. Therefore, any undetected lost writes that the old standby had before it was activated will not be detected by the new standby, since the new standby will be comparing the same blocks. Any new lost writes that happen on either the primary or the standby will be detected.

See Also:

[Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmconfa.htm#BRADV89476) for more information about enabling lost-write detection

## 13.7 Converting a Failed Primary into a Standby Database Using RMAN Backups

To convert a failed primary database, Oracle recommends that you enable the Flashback Database feature on the primary and follow the procedure described in either Section 13.2.1 or Section 13.2.2. The procedures in those sections describe the fastest ways to convert a failed primary into either a physical or logical standby. However, if Flashback Database was not enabled on the failed primary, you can still convert the failed primary into either a physical or logical standby using a local backup of the failed primary, as described in the following sections:

- Converting a Failed Primary into a Physical Standby Using RMAN Backups
- Converting a Failed Primary into a Logical Standby Using RMAN Backups

### 13.7.1 Converting a Failed Primary into a Physical Standby Using RMAN Backups

The steps in this section describe how to convert a failed primary into a physical standby by using RMAN backups. This procedure requires that the `COMPATIBLE` initialization parameter of the old primary be set to at least 11.0.0.

Step 1 Determine the SCN at which the old standby database became the primary database.

On the new primary database, issue the following query to determine the SCN at which the old standby database became the new primary database:

```
SQL> SELECT TO_CHAR(STANDBY_BECAME_PRIMARY_SCN) FROM V$DATABASE;
```

Step 2 Restore and recover the entire database.

Restore the database with a backup taken before the old primary had reached the SCN at which the standby became the new primary (`standby_became_primary_scn)`. Then, perform a point-in-time recovery to recover the old primary to that same point.

Issue the following RMAN commands:

```
RMAN> RUN
    {
      SET UNTIL SCN <standby_became_primary_scn + 1>;
      RESTORE DATABASE;
      RECOVER DATABASE;
     }
```

With user-managed recovery, you can first restore the database manually. Typically, a backup taken a couple of hours before the failover would be old enough. You can then recover the failed primary using the following command:

```
SQL> RECOVER DATABASE USIING BACKUP CONTROLFILE UNTIL CHANGE -
>  <standby_became_primary_scn + 1>;
```

Unlike a reinstantiation that uses Flashback Database, this procedure adds one to `standby_became_primary_scn`. For datafiles, flashing back to an SCN is equivalent to recovering up until that SCN plus one.

Step 3 Convert the database to a physical standby database.

Perform the following steps on the old primary database:

1. Issue the following statement on the old primary database:
	```
	SQL> ALTER DATABASE CONVERT TO PHYSICAL STANDBY;
	```
	This statement will dismount the database after successfully converting the control file to a standby control file.
2. Shut down and restart the database:
	```
	SQL> SHUTDOWN IMMEDIATE;
	SQL> STARTUP MOUNT;
	```

Step 4 Open the database as read-only.

Issue the following command:

```
SQL> ALTER DATABASE OPEN READ ONLY;
```

The goal of this step is to synchronize the control file with the database by using a dictionary check. After this command, check the alert log for any actions suggested by the dictionary check. Typically, no user action is needed if the old primary was not in the middle of adding or dropping datafiles during the failover.

Step 5 (Optional) Mount the standby again, if desired

If you have purchased a license for the Active Data Guard option and would like to operate your physical standby database in active query mode, skip this step. Otherwise, bring your standby database to the mount state.

For example:

```
SQL> SHUTDOWN IMMEDIATE;
SQL> STARTUP MOUNT;
```

Step 6 Restart transporting redo to the new physical standby database.

Before the new standby database was created, the new primary database probably stopped transmitting redo to the remote destination. To restart redo transport services, perform the following steps on the new primary database:

1. Issue the following query to see the current state of the archive destinations:
	```
	SQL> SELECT DEST_ID, DEST_NAME, STATUS, PROTECTION_MODE, DESTINATION, -
	> ERROR,SRL FROM V$ARCHIVE_DEST_STATUS;
	```
2. If necessary, enable the destination:
	```
	SQL> ALTER SYSTEM SET LOG_ARCHIVE_DEST_STATE_n=ENABLE;
	```
3. Perform a log switch to ensure the standby database begins receiving redo data from the new primary database, and verify it was sent successfully.
	Note:
	This is an important step in order for the old primary to become a new standby following the new primary. If this step is not done, the old primary may recover to an incorrect database branch. The only way to correct the problem then is to convert the old primary again.
	At the SQL prompt, enter the following statements:
	```
	SQL> ALTER SYSTEM SWITCH LOGFILE;
	SQL> SELECT DEST_ID, DEST_NAME, STATUS, PROTECTION_MODE, DESTINATION, -
	> ERROR,SRL FROM V$ARCHIVE_DEST_STATUS;
	```
	On the new standby database, you may also need to change the `LOG_ARCHIVE_DEST_` `n` initialization parameters so that redo transport services do not transmit redo data to other databases. This step can be skipped if both the primary and standby database roles were set up with the `VALID_FOR` attribute in one server parameter file (SPFILE). By doing this, the Data Guard configuration operates properly after a role transition.

Step 7 Start Redo Apply.

Start Redo Apply on the new physical standby database, as follows:

```
SQL> ALTER DATABASE RECOVER MANAGED STANDBY DATABASE -
> USING CURRENT LOGFILE DISCONNECT;
```

Once the failed primary database is restored and is running in the standby role, you can optionally perform a switchover to transition the databases to their original (pre-failure) roles. See [Section 8.2.1, "Performing a Switchover to a Physical Standby Database"](role_management.md) for more information.

### 13.7.2 Converting a Failed Primary into a Logical Standby Using RMAN Backups

The steps in this section describe how to convert a failed primary into a logical standby using RMAN backups.

Step 1 Determine the SCN to which to recover the failed primary database.

On the new primary database, issue the following query to determine the SCN to which you want to recover the failed primary database:

```
SQL> SELECT APPLIED_SCN RECOVERY_SCN FROM V$LOGSTDBY_PROGRESS;
```

Also on the new primary database, determine the SCN to use in dealing with archive logs, as follows:

1. Ensure all standby redo logs have been archived. Issue the following query, looking for a value of `READY` to be returned. Depending on the size of the database and the number of logs needing to be archived, it could take some time before a status of `READY` is returned.
	```
	SQL> SELECT VALUE FROM SYSTEM.LOGSTDBY$PARAMETERS - 
	> WHERE NAME='REINSTATEMENT_STATUS';
	```
2. After a status of `READY` has been returned, run the following query to retrieve the SCN for dealing with archive logs as part of this recovery:
	```
	SQL> SELECT VALUE ARCHIVE_SCN FROM SYSTEM.LOGSTDBY$PARAMETERS -
	> WHERE NAME='STANDBY_BECAME_PRIMARY_SCN';
	```

Step 2 Remove divergent archive logs from the failed primary database.

Remove any archive logs created at the time of, or after the failover operation, from the failed primary database. If the failed primary database was isolated from the standby, it could have divergent archive logs that are not consistent with the current primary database. To ensure these divergent archive logs are never applied, they must be deleted from backups and the fast recovery area. You can use the following RMAN command to delete the relevant archive logs from the fast recovery area:

```
RMAN> DELETE ARCHIVELOG FROM SCN ARCHIVE_SCN;
```

Once deleted, these divergent logs and subsequent transactions can never be recovered.

Step 3 Determine the log files to be copied to the failed primary database.

On the new primary database, issue the following query to determine the minimum set of log files that must be copied to the failed primary database before recovering from a backup:

```
SQL> SELECT file_name FROM DBA_LOGSTDBY_LOG WHERE next_change# > ARCHIVE_SCN;
```

Retrieve the required standby logs, copy the backup set to the new standby and restore it to the new standby fast recovery area. Because these logs are coming from standby redo logs, they are not part of the standby's standard archives. The RMAN utility is able to use a partial file name to retrieve the files from the correct location.

The following is a sample use of the RMAN `BACKUP` command:

```
RMAN> BACKUP AS COPY DEVICE TYPE DISK FORMAT '/tmp/test/%U'
> ARCHIVELOG LIKE '<partial file names from above>%';
```

The following is a sample use of the RMAN `RESTORE` command:

```
RMAN> CATALOG START WITH '/tmp/test';
RMAN> RESTORE ARCHIVELOG FROM SEQUENCE 33 UNTIL SEQUENCE 35;
```

Step 4 Restore a backup and recover the database.

Restore a backup of all the original primary's data files and recover to `RECOVERY_SCN + 1`. Oracle recommends that you leverage the current control file.

1. Start up the database in restricted mode to protect it from rogue transactions until the `GUARD ALL` command can be issued after the database has been opened.
2. Use the backup to restore the data files of the failed primary database.
3. Turn off flashback database, if it is enabled (necessary for the `USING BACKUP CONTROLFILE` clause).
4. Perform point-in-time recovery to `RECOVERY_SCN +1` in SQL\*Plus.

Whether you are using a current control file or a backup control file, you must specify the `USING BACKUP CONTROLFILE` clause to allow you to point to the archive logs being restored. Otherwise, the recovery process could attempt to access online redo logs instead of the logs retrieved in Step 3. When prompted for the sequences retrieved in Step 3, ensure you specify the file names of the restored archive log copies, as follows:

```
SQL> RECOVER DATABASE UNTIL CHANGE RECOVERY_SCN + 1 USING BACKUP CONTROLFILE;
```

Step 5 Open the database with the RESETLOGS option.

```
SQL> ALTER DATABASE OPEN RESETLOGS;
```

Step 6 Enable Database Guard

```
SQL> ALTER DATABASE GUARD ALL;
```

Step 7 Create a database link to the new primary database and start SQL Apply.

```
SQL> CREATE PUBLIC DATABASE LINK myLink -
> CONNECT TO SYSTEM IDENTIFIED BY password -
> USING 'service name of new primary database';
```
```
SQL> ALTER DATABASE START LOGICAL STANDBY APPLY NEW PRIMARY myLink;
```

At this point, you can disable restricted session (`ALTER SYSTEM DISABLE RESTRICTED SESSION`) or, if you need to restart the database to re-enable Flashback from Step 4.3, let this restart turn off `RESTRICTED SESSION`.

## 13.8 Changing the Character Set of a Primary Without Re-Creating Physical Standbys

Oracle Data Guard allows you to change both the database character set and the national character set of a primary database without requiring you to recreate any physical standby databases in the configuration. You can continue to use your physical standby database with minimal disruption while performing character set conversion of a primary database.

The process requires the running of several procedures prior to the actual conversion. The conversion itself requires that the primary database be shut down and opened in restricted mode, and that the `CSALTER` script be executed. Both the system data and user data are converted to the new character set.

For a detailed description of the steps involved in this process, see My Oracle Support note 1124165.1 at `http://support.oracle.com`. You will also need to read note 260192.1.

Note:

Similar to the obsolete `ALTER DATABASE CHARACTER SET` SQL statement, the `CSALTER` script should be used only by a system administrator. System administrators must run the Database Character Set Scanner first to confirm that the proper conditions exist for running `CSALTER`. Also, the database must be backed up before running `CSALTER`.

See Also:

[Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/ch11charsetmig.htm#NLSPG469) for more general information about using the `CSALTER` script to migrate character sets