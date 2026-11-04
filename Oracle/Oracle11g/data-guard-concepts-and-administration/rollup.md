---
title: Using SQL Apply to Upgrade the Oracle Database
book: Data Guard Concepts and Administration
doc_id: E41134-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41134/rollup.htm
tags:
  - oracle
  - 11g
  - data-guard-concepts-and-administration
---

## 12 Using SQL Apply to Upgrade the Oracle Database

Starting with Oracle Database 10g release 1 (10.1.0.3), you can use a logical standby database to perform a rolling upgrade of Oracle Database 10g software. During a rolling upgrade, you can run different releases of an Oracle database on the primary and logical standby databases while you upgrade them, one at a time, incurring minimal downtime on the primary database.

Note:

This chapter describes an alternative to the usual upgrade procedure involving longer downtime, as described in [Appendix B, "Upgrading and Downgrading Databases in a Data Guard Configuration"](upgrades.md). Do not attempt to combine steps from the method described in this chapter with steps from Appendix B.

The instructions in this chapter describe how to minimize downtime while upgrading an Oracle database. This chapter provides the following topics:

## 12.1 Benefits of a Rolling Upgrade Using SQL Apply

Performing a rolling upgrade with SQL Apply has the following advantages:

- Your database will incur very little downtime. The overall downtime can be as little as the time it takes to perform a switchover.
- You eliminate application downtime due to PL/SQL recompilation.
- You can validate the upgraded database release without affecting the primary database.

## 12.2 Requirements to Perform a Rolling Upgrade Using SQL Apply

The rolling upgrade procedure requires the following:

- A primary database that is running Oracle Database release x and a logical standby database that is running Oracle Database release y.
- The databases must not be part of a Data Guard Broker configuration. See [Oracle Data Guard Broker](https://docs.oracle.com/cd/E11882_01/server.112/e40771/toc.htm) for information about removing databases from a broker configuration.
- The Data Guard protection mode must be set to either maximum availability or maximum performance. Query the `PROTECTION_LEVEL` column in the `V$DATABASE` view to find out the current protection mode setting.
- To ensure the primary database can proceed while the logical standby database is being upgraded, the `LOG_ARCHIVE_DEST_` `n` initialization parameter for the logical standby database destination must not be set to `MANDATORY`.
- The `COMPATIBLE` initialization parameter must match the software release prior to the upgrade. That is, a rolling upgrade from release x to release y requires that the `COMPATIBLE` initialization parameter be set to release x on both the primary and standby databases.

## 12.3 Figures and Conventions Used in the Upgrade Instructions

Figure 12-1 shows a Data Guard configuration before the upgrade begins, with the primary and logical standby databases both running the same Oracle Database software release.

Figure 12-1 Data Guard Configuration Before Upgrade

![Figure 12-1 Data Guard Configuration Before Upgrade](img/sbydb023.gif)

> The illustration shows a Data Guard configuration before the upgrade begins, with the primary and logical standby databases both running the same Oracle Database software release. In the figure, the primary and standby databases are both running at version "x" and SQL Apply is actively transporting redo from the primary to logical standby database.
  

During the upgrade process, the Data Guard configuration operates with mixed database releases at several points in this process. Data protection is not available across releases. During these steps, consider having a second standby database in the Data Guard configuration to provide data protection.

The steps and figures describing the upgrade procedure refer to the databases as Database A and Database B rather than as the primary database and standby database. This is because the databases switch roles during the upgrade procedure. Initially, Database A is the primary database and Database B is the logical standby database, as shown in Figure 12-1.

The following sections describe scenarios in which you can use the SQL Apply rolling upgrade procedure:

- Section 12.4, "Performing a Rolling Upgrade By Creating a New Logical Standby Database"
- Section 12.5, "Performing a Rolling Upgrade With an Existing Logical Standby Database"
- Section 12.6, "Performing a Rolling Upgrade With an Existing Physical Standby Database"

## 12.4 Performing a Rolling Upgrade By Creating a New Logical Standby Database

This scenario assumes that you do not have an existing Data Guard configuration, but you are going to create a logical standby database solely for the purpose of performing a rolling upgrade of the Oracle Database.

Table 12-1 lists the steps to prepare the primary and standby databases for upgrading.

Table 12-1 Steps to Perform a Rolling Upgrade by Creating a New Logical Standby

| Step | Description |
| --- | --- |
| Step 1 | Identify unsupported data types and storage attributes |
| Step 2 | Create a logical standby database |
| Step 3 | Perform a rolling upgrade |

Step 1 Identify unsupported data types and storage attributes

To identify unsupported database objects on the primary database and decide how to handle them, follow these steps:

1. Identify unsupported data types and storage attributes for tables:
	- Review the list of supported data types and storage attributes provided in [Appendix C, "Data Type and DDL Support on a Logical Standby Database"](data_support.md).
		- Query the `DBA_LOGSTDBY_UNSUPPORTED` and `DBA_LOGSTDBY_SKIP` views on the primary database. Changes that are made to the listed tables and schemas on the primary database will not be applied on the logical standby database. Use the following query to see a list of unsupported tables:
		```
		SQL> SELECT DISTINCT OWNER, TABLE_NAME FROM DBA_LOGSTDBY_UNSUPPORTED;
		```
		Use the following query to see a list of unsupported internal schemas:
		```
		SQL> SELECT OWNER FROM DBA_LOGSTDBY_SKIP -
		>  WHERE STATEMENT_OPT = 'INTERNAL SCHEMA';
		```
2. Decide how to handle unsupported tables.
	If unsupported objects are being modified on your primary database, it might be possible to perform the upgrade anyway by temporarily suspending changes to the unsupported tables for the period of time it takes to perform the upgrade procedure.
	If you can prevent changes to unsupported data, then using SQL Apply might still be a viable way to perform the upgrade procedure. This method requires that you prevent users from modifying any unsupported tables from the time you create the logical standby control file to the time you complete the upgrade. For example, assume that the Payroll department updates an object table, but that department updates the database only Monday through Friday. However, the Customer Service department requires database access 24 hours a day, 7 days a week, but uses only supported data types and tables. In this scenario, you could perform the upgrade over a weekend. You can monitor transaction activity in the `DBA_LOGSTDBY_EVENTS` view and discontinue the upgrade (if necessary) up to the time you perform the first switchover.
	If you cannot prevent changes to unsupported tables during the upgrade, any unsupported transactions that occur are recorded in the `DBA_LOGSTDBY_EVENTS` table on the logical standby database. After the upgrade is completed, you might be able to use the Oracle Data Pump Export/Import utility to import the changed tables to the upgraded databases.
	See Also:
	- [Section 10.6.4, "Using Triggers to Replicate Unsupported Tables"](manage_ls.md)
	The size of the changed tables will determine how long database operations will be unavailable, so you must decide if a table is too large to export and import its data into the standby database. For example, a 4-terabyte table is not a good candidate for the export/import process.

Note:

If you cannot use a logical standby database because the data types in your application are unsupported, then perform the upgrade as documented in [Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/toc.htm).

Step 2 Create a logical standby database

To create a logical standby database, follow the instructions in [Chapter 4](create_ls.md).

Note:

Before you start SQL Apply for the first time, make sure you capture information about transactions running on the primary database that will not be supported by a logical standby database. Run the following procedures to capture and record the information as events in the `DBA_LOGSTDBY_EVENTS` view:
```
EXECUTE DBMS_LOGSTDBY.APPLY_SET('MAX_EVENTS_RECORDED',
 DBMS_LOGSTDBY.MAX_EVENTS);

EXECUTE DBMS_LOGSTDBY.APPLY_SET('RECORD_UNSUPPORTED_OPERATIONS',
 'TRUE');
```

Oracle recommends configuring a standby redo log on the logical standby database to minimize downtime.

Step 3 Perform a rolling upgrade

Now that you have created a logical standby database, you can follow the procedure described in Section 12.5, "Performing a Rolling Upgrade With an Existing Logical Standby Database", which assumes that you have a logical standby running the same Oracle software.

## 12.5 Performing a Rolling Upgrade With an Existing Logical Standby Database

This section provides a step-by-step procedure for upgrading the logical standby database and the primary database. Table 12-2 lists the steps.

Table 12-2 Steps to Perform a Rolling Upgrade WIth an Existing Logical Standby

| Step | Description |
| --- | --- |
| Step 1 | Prepare for rolling upgrade |
| Step 2 | Upgrade the logical standby database |
| Step 3 | Restart SQL Apply on the upgraded logical standby database |
| Step 4 | Monitor events on the upgraded standby database |
| Step 5 | Begin a switchover |
| Step 6 | Import any tables that were modified during the upgrade |
| Step 7 | Complete the switchover and activate user applications |
| Step 8 | Upgrade the old primary database |
| Step 9 | Start SQL Apply on the old primary database |
| Step 10 | Optionally, raise the compatibility level on both databases |
| Step 11 | Monitor events on the new logical standby database |
| Step 12 | Optionally, perform another switchover |

Step 1 Prepare for rolling upgrade

Follow these steps to prepare to perform a rolling upgrade of Oracle Software:

1. Stop SQL Apply by issuing the following statement on the logical standby database (Database B):
	```
	SQL> ALTER DATABASE STOP LOGICAL STANDBY APPLY;
	```
2. Set compatibility, if needed, to the highest value.
	Ensure the `COMPATIBLE` initialization parameter specifies the release number for the Oracle Database software running on the primary database prior to the upgrade.
	For example, if the primary database is running release 10.1, then set the `COMPATIBLE` initialization parameter to 10.1 on both databases. Be sure to set the `COMPATIBLE` initialization parameter on the standby database first before you set it on the primary database.

Step 2 Upgrade the logical standby database

Upgrade Oracle database software on the logical standby database (Database B) to release y. While the logical standby database is being upgraded, it will not accept redo data from the primary database.

To upgrade Oracle Database software, refer to the Oracle Database Upgrade Guide for the applicable Oracle Database release.

Figure 12-2 shows Database A running release x, and Database B running release y. During the upgrade, redo data accumulates on the primary system.

Figure 12-2 Upgrade the Logical Standby Database Release

![Figure 12-2 Upgrade the Logical Standby Database Release](img/sbydb026.gif)

> The illustration shows Database A running release x, and Database B running release y. During the upgrade, redo transport services are not transmitting data from the primary database to the standby database, so redo data is accumulating on the primary system.
>
> Copyright © 1999, 2014, Oracle and/or its affiliates. All rights reserved.  
> [Legal Notices](https://docs.oracle.com/cd/E11882_01/dcommon/html/cpyr.htm)
  

Step 3 Restart SQL Apply on the upgraded logical standby database

Restart SQL Apply and operate with release x on Database A and release y on Database B. To start SQL Apply, issue the following statement on Database B:

```
SQL> ALTER DATABASE START LOGICAL STANDBY APPLY IMMEDIATE;
```

The redo data that was accumulating on the primary system is automatically transmitted and applied on the newly upgraded logical standby database. The Data Guard configuration can run the mixed releases shown in Figure 12-3 for an arbitrary period while you verify that the upgraded Oracle Database software release is running properly in the production environment.

Figure 12-3 Running Mixed Releases

![Figure 12-3 Running Mixed Releases](img/sbydb024.gif)

> The illustration shows a configuration that is running mixed releases. In this configuration, redo transport services are started and the redo data that was accumulating on the primary system is being transmitted and applied on the newly upgraded logical standby database. The Data Guard configuration is running in a mixed release environment, such that the primary database is running release x and the standby database is running release y.
  

To monitor how quickly Database B is catching up to Database A, query the `V$LOGSTDBY_PROGRESS` view on Database B. For example:

```
SQL> ALTER SESSION SET NLS_DATE_FORMAT = 'DD-MON-YY HH24:MI:SS';
Session altered.

SQL> SELECT SYSDATE, APPLIED_TIME FROM V$LOGSTDBY_PROGRESS;

SYSDATE            APPLIED_TIME
------------------ ------------------
27-JUN-05 17:07:06 27-JUN-05 17:06:50
```

Step 4 Monitor events on the upgraded standby database

You should frequently query the `DBA_LOGSTDBY_EVENTS` view to learn if there are any DDL and DML statements that have not been applied on Database B. Example 12-1 demonstrates how monitoring events can alert you to potential differences in the two databases.

Example 12-1 Monitoring Events with DBA\_LOGSTDBY\_EVENTS

```
SQL> SET LONG 1000
SQL> SET PAGESIZE 180
SQL> SET LINESIZE 79
SQL> SELECT EVENT_TIMESTAMP, EVENT, STATUS FROM DBA_LOGSTDBY_EVENTS -
> ORDER BY EVENT_TIMESTAMP;

EVENT_TIMESTAMP
---------------------------------------------------------------------------
EVENT
--------------------------------------------------------------------------------
STATUS
--------------------------------------------------------------------------------
…
24-MAY-05 05.18.29.318912 PM
CREATE TABLE SYSTEM.TST (one number)
ORA-16226: DDL skipped due to lack of support
 
24-MAY-05 05.18.29.379990 PM
"SYSTEM"."TST"
ORA-16129: unsupported dml encountered
```

In the preceding example:

- The `ORA-16226` error shows a DDL statement that could not be supported. In this case, it could not be supported because it belongs to an internal schema.
- The `ORA-16129` error shows that a DML statement was not applied.

These types of errors indicate that not all of the changes that occurred on Database A have been applied to Database B. At this point, you must decide whether or not to continue with the upgrade procedure. If you are certain that this difference between the logical standby database and the primary database is acceptable, then continue with the upgrade procedure. If not, discontinue and reinstantiate Database B and perform the upgrade procedure at another time.

Step 5 Begin a switchover

When you are satisfied that the upgraded database software is operating properly, perform a switchover to reverse the database roles by issuing the following statement on Database A:

```
SQL> ALTER DATABASE COMMIT TO SWITCHOVER TO LOGICAL STANDBY;
```

This statement must wait for existing transactions to complete. To minimize the time it takes to complete the switchover, users still connected to Database A should log off immediately and reconnect to Database B.

Note:

The usual two-phased prepared switchover described in [Section 8.3.1](role_management.md) cannot be used because it requires both primary and standby databases to be running the same version of the Oracle software and at this point, the primary database is running a lower version of the Oracle software. Instead, the single-phased unprepared switchover procedure documented above is used. The unprepared switchover should only be used in the context of a rolling upgrade using a logical standby database.

Note:

If you suspended activity to unsupported tables or packages on Database A when it was the primary database, you must continue to suspend the same activities on Database B while it is the primary database if you eventually plan to switch back to Database A.

Step 6 Import any tables that were modified during the upgrade

Step 4 "Monitor events on the upgraded standby database" described how to list unsupported tables that are being modified. If unsupported DML statements were issued on the primary database (as described in Example 12-1), import the latest version of those tables using an import utility such as Oracle Data Pump.

For example, the following import command truncates the `scott.emp` table and populates it with data matching the former primary database (A):

```
IMPDP SYSTEM NETWORK_LINK=DATABASEA TABLES=SCOTT.EMP TABLE_EXIST_ACTION=TRUNCATE
```

Note that this command will prompt you for the `impdp` password before executing.

Step 7 Complete the switchover and activate user applications

When you are satisfied that the upgraded database software is operating properly, complete the switchover to reverse the database roles:

1. On Database B, query the `SWITCHOVER_STATUS` column of the `V$DATABASE` view, as follows:
	```
	SQL> SELECT SWITCHOVER_STATUS FROM V$DATABASE;
	SWITCHOVER_STATUS
	--------------------
	TO PRIMARY
	```
2. When the `SWITCHOVER_STATUS` column displays `TO PRIMARY`, complete the switchover by issuing the following statement on Database B:
	```
	SQL> ALTER DATABASE COMMIT TO SWITCHOVER TO PRIMARY;
	```
	Note:
	The usual two-phased prepared switchover described in [Section 8.3.1](role_management.md) cannot be used because it requires both primary and standby databases to be running the same version of the Oracle software and at this point, the primary database is running a lower version of the Oracle software. Instead, the single-phased unprepared switchover procedure documented above is used. The unprepared switchover should only be used in the context of a rolling upgrade using a logical standby database.
3. Activate the user applications and services on Database B, which is now running in the primary database role.

After the switchover, you cannot send redo data from the new primary database (B) that is running the new database software release to the new standby database (A) that is running an older software release. This means the following:

- Redo data is accumulating on the new primary database.
- The new primary database is unprotected at this time.

Figure 12-4 shows Database B, the former standby database (running release y), is now the primary database, and Database A, the former primary database (running release x), is now the standby database. The users are connected to Database B.

If Database B can adequately serve as the primary database and your business does not require a logical standby database to support the primary database, then you have completed the rolling upgrade process. Allow users to log in to Database B and begin working there, and discard Database A when it is convenient. Otherwise, continue with step 8.

Figure 12-4 After a Switchover

![Figure 12-4 After a Switchover](img/sbydb027.gif)

> The illustration shows the Data Guard configuration running in mixed-version mode after a switchover has occurred. In the figure, the standby database is running release x and the primary database is running release y. SQL Apply is not running because Database A, which is still running release x, cannot apply redo data from Database B until Database is upgraded and SQL Apply is started.
  

Step 8 Upgrade the old primary database

Database A is still running release x and cannot apply redo data from Database B until you upgrade it and start SQL Apply.

For more information about upgrading Oracle Database software, see the [Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/toc.htm) for the applicable Oracle Database release.

Figure 12-5 shows the system after both databases have been upgraded.

Figure 12-5 Both Databases Upgraded

![Figure 12-5 Both Databases Upgraded](img/sbydb025.gif)

> The illustration shows the Data Guard configuration after both databases have been upgraded to release y. SQL Apply has been started so that redo that was accumulating on the primary database (B) is now being sent to the logical standby database (A).
>
> Copyright © 1999, 2014, Oracle and/or its affiliates. All rights reserved.  
> [Legal Notices](https://docs.oracle.com/cd/E11882_01/dcommon/html/cpyr.htm)
  

Step 9 Start SQL Apply on the old primary database

Issue the following statement to start SQL Apply on Database A and, if necessary, create a database link to Database B:

```
SQL> ALTER DATABASE START LOGICAL STANDBY APPLY IMMEDIATE NEW PRIMARY db_link_to_b;
```

Note:

You will need to create a database link (if one has not already been set up) and to use the `NEW PRIMARY` clause, because in Step 4 the single-phased unprepared switchover was used to turn Database A into a standby database.

You will need to connect as user `SYSTEM` or with an account with a similar level of privileges.

When you start SQL Apply on Database A, the redo data that is accumulating on the primary database (B) is sent to the logical standby database (A). The primary database is protected against data loss once all the redo data is available on the standby database.

Step 10 Optionally, raise the compatibility level on both databases

Raise the compatibility level of both databases by setting the `COMPATIBLE` initialization parameter. You must raise the compatibility level at the logical standby database before you raise it at the primary database. Set the `COMPATIBLE` parameter on the standby database before you set it on the primary database. See [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams035.htm#REFRN10019) for more information about the `COMPATIBLE` initialization parameter.

Step 11 Monitor events on the new logical standby database

To ensure that all changes performed on Database B are properly applied to the logical standby database (A), you should frequently query the `DBA_LOGSTDBY_EVENTS` view, as you did for Database A in step 4. (See Example 12-1.)

If changes were made that invalidate Database A as a copy of your existing primary database, you can discard Database A and create a new logical standby database in its place. See [Chapter 4, "Creating a Logical Standby Database"](create_ls.md) for complete information.

Step 12 Optionally, perform another switchover

Optionally, perform another switchover of the databases so Database A is once again running in the primary database role (as shown in Figure 12-1).

Note:

You will use the two-phased prepared switchover described in [Section 8.3.1](role_management.md) since at this time, both Database A and Database B are running the same version of the Oracle software.

## 12.6 Performing a Rolling Upgrade With an Existing Physical Standby Database

The steps in this section show you how to perform a rolling upgrade of Oracle software and then get back to your original configuration in which A is the primary database and B is the physical standby database, and both of them are running the upgraded Oracle software.

Note:

The steps in this section assume that you have a primary database (A) and a physical standby database (B) already set up and using Oracle Database release 11.1 or later.

Table 12-3 summarizes the steps involved.

Table 12-3 Steps to Perform a Rolling Upgrade With an Existing Physical Standby

| Step | Description |
| --- | --- |
| Step 1 | Prepare the primary database for a rolling upgrade (perform these steps on Database A) |
| Step 2 | Convert the physical standby database into a logical standby database (perform these steps on Database B) |
| Step 3 | Upgrade the logical standby database and catch up with the primary database (perform these steps on Database B) |
| Step 4 | Flashback Database A to the guaranteed restore point (perform these steps on Database A) |
| Step 5 | Mount Database A using the new version of Oracle software |
| Step 6 | Convert Database A to a physical standby |
| Step 7 | Start managed recovery on Database A |
| Step 8 | Perform a switchover to make Database A the primary database |
| Step 9 | Clean up the guaranteed restore point created in Database A |

Step 1 Prepare the primary database for a rolling upgrade (perform these steps on Database A)

1. Enable Flashback Database, if it is not already enabled:
	```
	SQL> SHUTDOWN IMMEDIATE;
	SQL> STARTUP MOUNT;
	SQL> ALTER DATABASE FLASHBACK ON;
	SQL> ALTER DATABASE OPEN;
	```
2. Create a guaranteed restore point:
	```
	SQL> CREATE RESTORE POINT pre_upgrade GUARANTEE FLASHBACK DATABASE;
	```

Step 2 Convert the physical standby database into a logical standby database (perform these steps on Database B)

1. Follow the steps outlined in [Chapter 4, "Creating a Logical Standby Database"](create_ls.md) except for the following difference. In [Section 4.2.4.1, "Convert to a Logical Standby Database"](create_ls.md) you must use a different command to convert the logical standby database. Instead of `ALTER DATABASE RECOVER TO LOGICAL STANDBY db_name`, issue the following command:
	```
	SQL> ALTER DATABASE RECOVER TO LOGICAL STANDBY KEEP IDENTITY;
	SQL> ALTER DATABASE OPEN;
	```
2. You must take the following actions before you start SQL Apply for the first time:
	1. Disable automatic deletion of foreign archived logs at the logical standby, as follows:
		```
		SQL> EXECUTE DBMS_LOGSTDBY.APPLY_SET('LOG_AUTO_DELETE', 'FALSE');
		```
		Note:
		You should not delete any remote archived logs processed by the logical standby database (Database B). These remote archived logs are required later during the rolling upgrade process. If you are using the recovery area to store the remote archived logs, you must ensure that it has enough space to accommodate these logs without interfering with the normal operation of the logical standby database.
		2. Make sure you capture information about transactions running on the primary database that will not be supported by a logical standby database. Run the following procedures to capture and record the information as events in the `DBA_LOGSTDBY_EVENTS` table:
		```
		SQL> EXECUTE DBMS_LOGSTDBY.APPLY_SET('MAX_EVENTS_RECORDED', -
		> DBMS_LOGSTDBY.MAX_EVENTS);
		 
		SQL> EXECUTE DBMS_LOGSTDBY.APPLY_SET('RECORD_UNSUPPORTED_OPERATIONS', 'TRUE');
		```
		3. Start SQL Apply for the first time, as follows:
		```
		SQL> ALTER DATABASE START LOGICAL STANDBY APPLY IMMEDIATE;
		```
	See Also:
	- [Section 10.5.1, "Customizing Logging of Events in the DBA\_LOGSTDBY\_EVENTS View"](manage_ls.md) for more information about the `DBA_LOGSTDBY_EVENTS` view
	- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_lsbydb.htm#ARPLS363) for complete information about the `DBMS_LOGSTDBY` package

Step 3 Upgrade the logical standby database and catch up with the primary database (perform these steps on Database B)

You can now follow Steps 1 through 8 as described in Section 12.5, "Performing a Rolling Upgrade With an Existing Logical Standby Database". At the end of these steps, Database B will be your primary database running the upgraded version of the Oracle software, and Database A has become your logical standby database.

Move on to the next step to turn Database A into the physical standby for Database B.

Step 4 Flashback Database A to the guaranteed restore point (perform these steps on Database A)

```
SQL> SHUTDOWN IMMEDIATE;
SQL> STARTUP MOUNT;
SQL> FLASHBACK DATABASE TO RESTORE POINT pre_upgrade;
SQL> SHUTDOWN IMMEDIATE;
```

Step 5 Mount Database A using the new version of Oracle software

At this point, you should switch the Oracle binary at Database A to use the higher version of the Oracle software. You will not run the upgrade scripts, since Database A will be turned into a physical standby, and will be upgraded automatically as it applies the redo data generated by Database B.

Mount Database A, as follows:

```
SQL> STARTUP MOUNT;
```

Step 6 Convert Database A to a physical standby

```
SQL> ALTER DATABASE CONVERT TO PHYSICAL STANDBY;
SQL> SHUTDOWN IMMEDIATE;
```

Step 7 Start managed recovery on Database A

Database A will be upgraded automatically as it applies the redo data generated by Database B. Managed recovery will wait until the new incarnation branch from the primary is registered before it starts applying redo.

```
SQL> STARTUP MOUNT;
SQL> ALTER DATABASE RECOVER MANAGED STANDBY DATABASE USING CURRENT LOGFILE - 
>  DISCONNECT FROM SESSION;
```

Note:

When Redo Apply restarts, it waits for a new incarnation from the current primary database (Database B) to be registered.

Step 8 Perform a switchover to make Database A the primary database

At this point, Database B is your primary database and Database A is your physical standby, both running the higher version of the Oracle software. To make Database A the primary database, follow the steps described in [Section 8.2.1, "Performing a Switchover to a Physical Standby Database"](role_management.md).

Step 9 Clean up the guaranteed restore point created in Database A

To preserve disk space, drop the existing guaranteed restore point:

```
SQL> DROP RESTORE POINT PRE_UPGRADE;
```

See Also:

The "Database Rolling Upgrade Using Transient Logical Standby: Oracle Data Guard 11g" best practices white paper available on the Oracle Maximum Availability Architecture (MAA) home page at:

`http://www.oracle.com/goto/maa`