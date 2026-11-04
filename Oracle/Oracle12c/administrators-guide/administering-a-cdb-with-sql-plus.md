---
title: "Database Administrator’s Guide"
book: "Database Administrator's Guide"
doc_id: E85760-09
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/admin/administering-a-cdb-with-sql-plus.html
tags:
  - oracle
  - 12c
  - administrators-guide
---

Administering a multitenant container database (CDB) with SQL\*Plus includes tasks such as accessing a container in a CDB, modifying a CDB, executing DDL statements in a CDB, and running Oracle-supplied SQL scripts in a CDB.

Note:

You can complete the tasks in this chapter using SQL\*Plus or Oracle SQL Developer.

- About Administering a CDB  
	Administering a CDB is similar to administering a non-CDB, but there are some differences. Most of the differences are because some administrative tasks apply to the entire CDB, while others apply to the CDB root, application containers, application roots, and specific pluggable databases (PDBs) and application PDBs.
- Accessing a Container in a CDB with SQL\*Plus  
	You can access a container in a CDB with SQL\*Plus.
- Executing Code in Containers Using the DBMS\_SQL Package  
	When you are executing PL/SQL code in a container in a CDB, and you want to execute one or more SQL statements in a different container, use the `DBMS_SQL` package to switch containers.
- Modifying a CDB  
	You can modify the entire CDB, the root, or one or more PDBs.
- Using the ALTER SYSTEM SET Statement in a CDB  
	The `ALTER` `SYSTEM` `SET` statement can dynamically set an initialization parameter in one or more containers in a CDB.
- Issuing DML Statements on Containers in a CDB  
	A DML (data manipulation language) statement issued in a CDB root can modify one or more containers in the CDB. In addition, you can specify one or more default container targets for DML statements.
- Executing DDL Statements in a CDB  
	In a CDB, you can execute a data definition language (DDL) statement in the current container or in all containers.
- Managing the CDB Undo Mode  
	When local undo is enabled, each container has its own undo tablespace for every instance in which it is open. When local undo is disabled, there is one undo tablespace for the entire CDB.
- Running Oracle-Supplied SQL Scripts in a CDB  
	You can use the catcon.pl script to run Oracle-supplied SQL scripts in a CDB.
- Shutting Down a CDB Instance  
	You can shut down a CDB instance in the same way that you shut down a non-CDB instance.

**Parent topic:** [Managing a Multitenant Environment](managing-a-multitenant-environment.md)

### 41.1 About Administering a CDB

Administering a CDB is similar to administering a non-CDB, but there are some differences. Most of the differences are because some administrative tasks apply to the entire CDB, while others apply to the CDB root, application containers, application roots, and specific pluggable databases (PDBs) and application PDBs.

- About the Current Container  
	The data dictionary in each container in a CDB is separate, and the current container is the container whose data dictionary is used for name resolution and for privilege authorization. The current container can be the CDB root, an application root, a PDB, or an application PDB. Each session has exactly one current container at any point in time, but it is possible for a session to switch from one container to another.
- About Administrative Tasks in a CDB  
	Common users perform administrative tasks for a CDB.
- About Using Manageability Features in a CDB  
	For each of Oracle Database's manageability features in a CDB, it is important to understand the data location and the data visibility.
- About Managing Database Objects in a CDB  
	In a CDB, different containers can contain different database objects.
- About Flashing Back a PDB  
	You can use the `FLASHBACK PLUGGABLE DATABASE` statement to return a PDB to a past time or system change number (SCN).
- About Restricting PDB Users for Enhanced Security  
	There are several ways to restrict PDB users for enhanced security. A PDB lockdown profile restricts the features and options available to users in a particular PDB. The `PDB_OS_CREDENTIAL` initialization parameter can specify a unique operating system user for a PDB to limit operating system access. Also, when the `PATH_PREFIX` and `CREATE_FILE_DEST` clauses are specified during PDB creation, they limit file system access.

**Parent topic:** Administering a CDB with SQL\*Plus

#### 41.1.1 About the Current Container

The data dictionary in each container in a CDB is separate, and the current container is the container whose data dictionary is used for name resolution and for privilege authorization. The current container can be the CDB root, an application root, a PDB, or an application PDB. Each session has exactly one current container at any point in time, but it is possible for a session to switch from one container to another.

Each container has a unique ID and name in a CDB. You can use the `CON_ID` and `CON_NAME` parameters in the `USERENV` namespace to determine the current container ID and name with the `SYS_CONTEXT` function. For example, the following query returns the current container name:

```
SELECT SYS_CONTEXT ('USERENV', 'CON_NAME') FROM DUAL;
```

You can access a container in various ways in a CDB. For example, you can use the SQL\*Plus `CONNECT` command, and you can use an `ALTER` `SESSION` `SET` `CONTAINER` statement to switch the container of the current session.

The following rules apply to the current container in a CDB:

- The current container can be `CDB$ROOT` (CDB root) only for common users.
- The current container can be a particular PDB for common users and local users.
- The current container can be an application root only for common users or for application common users created in the application root.
- The current container can be a particular application PDB for common users, application common users, and local users.
- The current container must be the CDB root or an application root when a SQL statement includes `CONTAINER = ALL`.
	You can include the `CONTAINER` clause in several SQL statements, such as the `CREATE USER`, `ALTER USER`, `CREATE ROLE`, `GRANT`, `REVOKE`, and `ALTER SYSTEM` statements.
- When a SQL statement includes `CONTAINER = ALL` and the current container is the CDB root, the SQL statement affects all containers in the CDB, including all PDBs, application roots, and application PDBs.
- When a SQL statement includes `CONTAINER = ALL` and the current container is an application root, the SQL statement affects all containers in the application container, including the application root and all of the application PDBs that belong to the application root. The SQL statement does not affect the CDB root or any PDBs or application PDBs that do not belong to the current application root.
- Only a common user or application common user with the commonly granted `SET CONTAINER` privilege can run a SQL statement that includes `CONTAINER = ALL`.

See Also:

- " Accessing a Container in a CDB with SQL\*Plus "
- " Executing Code in Containers Using the DBMS\_SQL Package "
- " [Determining the Current Container ID or Name](viewing-information-about-cdbs-and-pdbs-with-sql-plus.md) "
- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=CNCPT89396)
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQLRF06117)
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=DBSEG754)

**Parent topic:** About Administering a CDB

#### 41.1.2 About Administrative Tasks in a CDB

Common users perform administrative tasks for a CDB.

A common user has a single identity and can log in to the CDB root, any application root, PDB, or application PDB in which it has privileges. Some tasks, such as starting up a CDB instance, can be performed only by a common user.

Other administrative tasks are the same for a CDB and a non-CDB. Table 41-1 describes some of these tasks and provides pointers to the relevant documentation.

Table 41-1 Administrative Tasks Common to CDBs and Non-CDBs

| Task | Description | Additional Information |
| --- | --- | --- |
| Starting up a CDB instance | To start a CDB instance, the current user must be a common user whose current container is the CDB root.  When you open a CDB, the CDB root is opened, but its other containers are mounted. Use the `ALTER` `PLUGGABLE` `DATABASE` statement to modify the open mode of one or more containers. | " [Starting Up a Database](starting-up-and-shutting-down.md) "  " Modifying the Open Mode of PDBs "  " [Modifying a PDB with the ALTER PLUGGABLE DATABASE Statement](administering-pdbs-with-sql-plus.md) "  " About the Current Container " |
| Managing processes | A CDB has one set of background processes shared by the CDB root and all containers. | " [Managing Processes](managing-processes.md) " |
| Managing memory | A CDB has a single system global area (SGA) and a single aggregate program global area (PGA). The memory required by a CDB is the sum of the memory requirements for all of the containers that will be part of the CDB. | " [Managing Memory](managing-memory.md) " |
| Managing security | You can create and drop common users, application common users, and local users in a CDB. You can also grant privileges to and revoke privileges from these users. You can also manage the `CONTAINER_DATA` attributes of common users and application common users.  In addition, grant the following roles to the appropriate users:  - Grant the `CDB_DBA` role to CDB administrators. - Grant the `PDB_DBA` role to application container administrators and PDB administrators. | [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=DBSEG573) |
| Monitoring errors and alerts | A CDB has one alert log for the entire CDB. The name of an application container, PDB, or application PDB is included in records in trace files, when appropriate. | " [Monitoring Errors and Alerts](monitoring-the-database.md) " |
| Managing diagnostic data | In a CDB, you can use the Oracle Database fault diagnosability infrastructure and the Automatic Diagnostic Repository (ADR). | [Managing Diagnostic Data](managing-diagnostic-data.md) |
| Managing control files | A CDB has one control file. | " [Managing Control Files](managing-control-files.md) " |
| Managing the online redo log and the archived redo log files | A CDB has one online redo log and one set of archived redo log files. | " [Managing the Redo Log](managing-the-redo-log.md) "  " [Managing Archived Redo Log Files](managing-archived-redo-log-files.md) " |
| Managing tablespaces | You can create, modify, and drop tablespaces and temporary tablespaces for the CDB root and for individual containers. You can also specify a default tablespace, default tablespace type, and a default temporary tablespace for the CDB root. The CDB root has its own set of Oracle-supplied tablespaces, such as the `SYSTEM` tablespace, and other containers have their own set of Oracle-supplied tablespaces. | " [Managing Tablespaces](managing-tablespaces.md) "  " Modifying a CDB " |
| Managing data files and temp files | The CDB root has its own data files, and other containers have their own data files. In a CDB, you can manage data files and temp files in basically the same way you would manage them for a non-CDB. However, the following exceptions apply to CDBs:  - You can limit the amount of storage used by the data files for a container by using the `STORAGE` clause in a `CREATE` `PLUGGABLE` `DATABASE` or `ALTER` `PLUGGABLE` `DATABASE` statement. - There is a default temporary tablespace for the CDB root and for individual containers. | " [Managing Data Files and Temp Files](managing-data-files-and-temp-files.md) "  " Modifying a CDB "  " [Storage Limits](creating-and-removing-pdbs-with-sql-plus.md) "  " [Modifying a PDB](administering-pdbs-with-sql-plus.md) " |
| Managing undo | A CDB can run in local undo mode or shared undo mode. Local undo mode means that every container in the CDB uses local undo. Shared undo mode means that there is one active undo tablespace for a single-instance CDB, or for an Oracle RAC CDB, there is one active undo tablespace for each instance.  In a CDB, the `UNDO_MANAGEMENT` initialization parameter must be set to `AUTO`, and an undo tablespace is required to manage the undo data. | " Managing the CDB Undo Mode "  " [Managing Undo](managing-undo.md) "  " About the Current Container " |
| Moving data between containers | You can move data between containers using the same methods that you would use to move data between non-CDBs. For example, you can transport the data or use Data Pump export/import to move the data. | " [Transporting Data](transporting-data.md) "  [Oracle Database Utilities](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SUTIL100) |
| Using Oracle Managed Files | Using Oracle Managed files can simplify administration for both a CDB and a non-CDB. | " [Using Oracle Managed Files](using-oracle-managed-files.md) " |
| Using Transparent Data Encryption | Transparent Data Encryption is a feature that enables encryption of individual table columns before storing them in the data file, or enables encryption of entire tablespaces. In a CDB, each container has its own master key for Transparent Data Encryption, and, where applicable, the `ADMINISTER` `KEY` `MANAGEMENT` SQL statement enables key management at the CDB level and for individual containers. | [Oracle Database Advanced Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=ASOAG10352)  " About the Current Container " |
| Using a standby database | Oracle Data Guard can configure a physical standby or a logical standby of a CDB. Data Guard operates on the entire CDB, not on individual containers in a CDB. | [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SBYDB) |
| Using Oracle Database Vault | Oracle Database Vault common realms can be scoped to an application root on common objects. Database Vault common command rules can be scoped to either the CDB or an application root. Local realms and command rules can be locally scoped to individual PDBs or application PDBs. When Oracle Database Vault security objects are in the CDB root or an application root, enforcement of the security objects only applies to the containers that have Oracle Database Vault enabled. | [Oracle Database Vault Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=DVADM71131) |
| Dropping a database | When you drop a CDB, all of the containers in the CDB are dropped along with their data. These containers include the CDB root and CDB seed and all of the application containers, application seeds, PDBs, and application PDBs.  You can also drop individual application containers, application seeds, PDBs, and application PDBs with the `DROP` `PLUGGABLE` `DATABASE` statement. | " [Dropping a Database](creating-and-configuring-an-oracle-database.md) "  " [Dropping a PDB](creating-and-removing-pdbs-with-sql-plus.md) " |

See Also:

[Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=CNCPT89248) for more information about the architecture of a CDB

**Parent topic:** About Administering a CDB

#### 41.1.3 About Using Manageability Features in a CDB

For each of Oracle Database's manageability features in a CDB, it is important to understand the data location and the data visibility.

It is important to understand where the data is stored for Oracle Database's manageability features in a CDB. When the data for a feature is stored in the CDB root only, the data related to a PDB is not included if the PDB is unplugged. However, when the data for a feature is stored in the PDB, the data related to the PDB is included if the PDB is unplugged, and this data remains part of the PDB if it is plugged into the same CDB or a different CDB.

It is also important to understand which data is visible to different users. Generally, in a CDB, a common user can view data for the CDB root and for multiple PDBs when the common user's current container is the CDB root. A common user can view this data by querying container data objects. The specific data that is visible varies for the manageability features. A user whose current container is a PDB can view data for that PDB only.

Table 41-2 describes how the manageability features work in a CDB.

Table 41-2 Manageability Features in a CDB

| Manageability Feature | Data Location | Data Visibility | Additional Information |
| --- | --- | --- | --- |
| Active Session History (ASH)  ASH collects information about active database sessions. You can use this information to analyze and identify performance issues. | Most of the ASH data is stored in memory. A small percentage of the ASH data samples are stored in the CDB root.  ASH data related to a PDB is not included if the PDB is unplugged. | A common user whose current container is the CDB root can view ASH data for the CDB root and for PDBs.  A user whose current container is a PDB can view ASH data for the PDB only. | [Oracle Database 2 Day + Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=TDPPT065)  [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=TGDBA277) |
| Alerts  An alert is a notification of a possible problem. | Threshold settings that pertain to a PDB are stored in the PDB.  Alerts posted when thresholds are violated are enqueued into the alert queue in the CDB root.  Threshold settings that pertain to a PDB are included if the PDB is unplugged. Alerts related to a PDB are not included if the PDB is unplugged. | A common user whose current container is the CDB root can view alerts for the CDB root and for PDBs.  A user whose current container is a PDB can view alert thresholds and alerts for the PDB only. | " [Monitoring Errors and Alerts](monitoring-the-database.md) " |
| Automated Database Maintenance Tasks  Automated database maintenance tasks are tasks that are started automatically at regular intervals to perform maintenance operations on the database. Automated tasks include automatic optimizer statistics collection, Automatic Segment Advisor tasks, and Automatic SQL Tuning Advisor tasks.  The `ENABLE_AUTOMATIC_MAINTENANCE_PDB` initialization parameter can enable or disable the running of automated maintenance tasks for all the PDBs in a CDB or for individual PDBs in a CDB.  The `AUTOTASK_MAX_ACTIVE_PDBS` initialization parameter limits the number of PDBs that can schedule automated maintenance tasks at the same time (during a maintenance window). | A user can schedule maintenance windows and enable or disable maintenance tasks for the current container only. If the current container is the CDB root, then the changes only apply to the CDB root. If the current container is a PDB, then the changes only apply to the PDB.  Data related to a PDB is stored in the PDB for automatic optimizer statistics collection and the Automatic Segment Advisor. This data is included if the PDB is unplugged.  Automatic SQL Tuning Advisor runs only in the CDB root. See the SQL Tuning Advisor row in this table for information about data collected by Automatic SQL Tuning Advisor. | See the appropriate row in this table for data visibility information about the following manageability features: automatic optimizer statistics collection, Optimizer Statistics Advisor, Automatic Segment Advisor, and Automatic SQL Tuning Advisor. | " [Managing Automated Database Maintenance Tasks](managing-automated-database-maintenance-tasks.md) "  [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=REFRN-GUID-3ACE01FA-8342-4F35-94BB-955412B9C76A) for information about the `ENABLE_AUTOMATIC_MAINTENANCE_PDB` initialization parameter  [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=REFRN-GUID-5DC631A2-4CDD-4C1F-B337-184BFD4C29B8) for information about the `AUTOTASK_MAX_ACTIVE_PDBS` initialization parameter |
| Automatic Database Diagnostic Monitor (ADDM)  ADDM can diagnose a database's performance and determine how identified problems can be resolved. | All ADDM runs must be performed in the CDB root. All ADDM results are stored in the CDB root.  ADDM analyzes activity in a PDB within the context of the current analysis target. ADDM does not analyze one PDB at a time. As in previous releases, ADDM runs with a target of either the entire instance or Oracle Real Application Clusters (Oracle RAC) database.  ADDM results related to a PDB are not included if the PDB is unplugged. | ADDM results are visible only to a common user whose current container is the CDB root. The ADDM results can include information about multiple PDBs. The ADDM results cannot be viewed when the current container is a PDB. | [Oracle Database 2 Day DBA](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=ADMQS102)  [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=TGDBA026) |
| Automatic Optimizer Statistics Collection  Automatic optimizer statistics collection gathers optimizer statistics for all schema objects in the database for which there are no statistics or only stale statistics. The statistics gathered by this task are used by the SQL query optimizer to improve the performance of SQL execution. | When an automatic optimizer statistics collection task gathers data for a PDB, it stores this data in the PDB. This data is included if the PDB is unplugged. | A common user whose current container is the CDB root can view optimizer statistics data for PDBs.  A user whose current container is a PDB can view optimizer statistics data for the PDB only. | " [Using Oracle Resource Manager for PDBs with SQL\*Plus](using-oracle-resource-manager-for-pdbs-with-sql-plus.md) "  [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=TGSQL389) |
| Automatic Segment Advisor  The Automatic Segment Advisor identifies segments that have space available for reclamation and makes recommendations on how to defragment those segments. | When Automatic Segment Advisor gathers data for a PDB, it stores this data in the PDB. This data is included if the PDB is unplugged. | A common user whose current container is the CDB root can view Automatic Segment Advisor data for PDBs.  A user whose current container is a PDB can view the Automatic Segment Advisor data for the PDB only. | " [Reclaiming Unused Space](managing-space-for-schema-objects.md) "  " [Using Oracle Resource Manager for PDBs with SQL\*Plus](using-oracle-resource-manager-for-pdbs-with-sql-plus.md) " |
| Automatic Workload Repository (AWR)  The AWR collects, processes, and maintains performance statistics for problem detection and self-tuning purposes. This data is stored in the database. The gathered data can be displayed in both reports and views. | AWR reports can be generated in the CDB root or in any PDB. AWR reports generated in the CDB root pertain to the entire CDB, while AWR reports generated when a PDB is the current container only pertain to that PDB.  AWR data generated in the CDB root is stored in the CDB root. AWR data generated in a PDB is stored in the PDB.  When a PDB is unplugged, AWR data stored in the CDB root is not included.  When a PDB is unplugged, AWR data stored in the PDB is included. | A common user whose current container is the CDB root can view AWR data for the CDB root and for PDBs.  A user whose current container is a PDB can view AWR data for the PDB only. | [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=TGDBA169) |
| Database Replay  Database Replay is a feature of Oracle Real Application Testing. Database Replay captures the workload for a database and replays it exactly on a test database. | Information about database captures and replays are stored in the CDB root. | A common user whose current container is the CDB root can view database capture and replay information. | [Oracle Database Testing Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=RATUG4080) |
| Optimizer Statistics Advisor  Optimizer Statistics Advisor analyzes how statistics are being gathered and suggests changes that can be made to fine tune statistics collection. | Data related to a PDB is stored in the PDB for Optimizer Statistics Advisor. This data is included if the PDB is unplugged. | A common user whose current container is the CDB root can view Optimizer Statistics Advisor data for PDBs.  A user whose current container is a PDB can view the Optimizer Statistics Advisor data for the PDB only. | [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=TGSQL-GUID-054F4B76-DD57-46EE-98EA-0FF04F49D1B3) |
| SQL Management Base (SMB)  SMB stores statement logs, plan histories, SQL plan baselines, and SQL profiles in the data dictionary. | SMB data related to a PDB is stored in the PDB. The SMB data related to a PDB is included if the PDB is unplugged. | A common user whose current container is the CDB root can view SMB data for PDBs.  A user whose current container is a PDB can view the SMB data for the PDB only. | [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=TGSQL631) |
| SQL Performance Analyzer (SPA)  SPA can analyze the SQL performance impact of SQL tuning and other system changes. SPA is often used with Database Replay. | A common user whose current container is the CDB root can run SPA for any PDB. In this case, the SPA results data is stored in the CDB root and is not included if the PDB is unplugged.  A user whose current container is a PDB can run SPA on the PDB. In this case, the SPA results data is stored in the PDB and is included if the PDB is unplugged. | A common user whose current container is the CDB root can view SPA results data for PDBs.  A user whose current container is a PDB can view the SPA results data for the PDB only. | [Oracle Database Testing Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=RATUG239) |
| SQL Tuning Sets (STS)  An STS is a database object that includes one or more SQL statements along with their execution statistics and execution context, and could include a user priority ranking.  You can use an STS to tune a group of SQL statements or test their performance using SPA. | An STS can be stored in the CDB root or in any PDB. If it is stored in the CDB root, then you can load SQL statements from any PDB into it.  When a PDB is unplugged, an STS stored in the CDB root is not included, even if the STS contains SQL statements from the PDB.  When a PDB is unplugged, an STS stored in the PDB is included. | A common user whose current container is the CDB root can view STS data stored in the CDB root only.  A user whose current container is a PDB can view STS data for the PDB only. | [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=TGSQL516) |
| SQL Tuning Advisor  SQL Tuning Advisor optimizes SQL statements that have been identified as high-load SQL statements. | Automatic SQL Tuning Advisor data is stored in the CDB root. It might have results about SQL statements executed in a PDB that were analyzed by the advisor, but these results are not included if the PDB is unplugged.  A common user whose current container is the CDB root can run SQL Tuning Advisor manually for SQL statements from any PDB. When a statement is tuned, it is tuned in any container that runs the statement.  A user whose current container is a PDB can also run SQL Tuning Advisor manually for SQL statements from the PDB. When SQL Tuning Advisor is run manually from a PDB, the results are stored in the PDB from which it is run. In this case, a statement is tuned only for the current PDB, and the results related to a PDB are included if the PDB is unplugged. | When SQL Tuning Advisor is run automatically, the results are visible only to a common user whose current container is the CDB root. These results cannot be viewed when the current container is a PDB.  When SQL Tuning Advisor is run manually by a user whose current container is a PDB, the results are only visible to a user whose current container is that PDB. | [Oracle Database 2 Day + Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=TDPPT160)  [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=TGSQL540) |

To run SPA or SQL Tuning Advisor for SQL statements from a PDB, a common user must have the following privileges:

- Common `SET` `CONTAINER` privilege or local `SET` `CONTAINER` privilege in the PDB
- The privileges required to execute the SQL statements in the PDB

See Also:

- " About the Current Container "
- " [About CDB and PDB Information in Views](viewing-information-about-cdbs-and-pdbs-with-sql-plus.md) " for an overview of container data objects
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=DBSEG803) for detailed information about container data objects

**Parent topic:** About Administering a CDB

#### 41.1.4 About Managing Database Objects in a CDB

In a CDB, different containers can contain different database objects.

An Oracle database stores database objects, such as tables, indexes, and directories. Database objects that are owned by a schema are called schema objects, while database objects that are not owned by a schema are called nonschema objects. The root and PDBs contain schemas, and schemas contain schema objects. The root and PDBs can also contain nonschema objects, such as users, roles, tablespaces, directories, and editions.

In a CDB, the root contains Oracle-supplied schemas and database objects. Oracle-supplied common users, such as `SYS` and `SYSTEM`, own these schemas and common database objects. They can also own local objects, both in the root and in a PDB.

You can create common users in the root to administer containers in the CDB. User-created common users can create database objects in the root. Oracle recommends that, in the root, schemas owned by user-created common users contain only database triggers and the objects used in their definitions. A user-created common user can also own any type of local object in a PDB.

You can create local users in a PDB. A local user in a PDB can create schema objects and nonschema objects in the PDB. You cannot create local users in the root.

Name resolution in a CDB is similar to name resolution in a non-CDB, except that names are resolved in the context of the dictionary of the user's current container.

See Also:

- [Managing Schema Objects](managing-schema-objects.md)
- " About the Current Container "
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQLRF20003) for information about schema objects and nonschema objects
- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=CNCPT89257) for an overview of common users and local users
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=DBSEG573) for information about creating common users and local users

**Parent topic:** About Administering a CDB

#### 41.1.5 About Flashing Back a PDB

You can use the `FLASHBACK PLUGGABLE DATABASE` statement to return a PDB to a past time or system change number (SCN).

You can create restore points for a PDB and flash back the PDB to the restore point without affecting the CDB or other PDBs.

#### 41.1.6 About Restricting PDB Users for Enhanced Security

There are several ways to restrict PDB users for enhanced security. A PDB lockdown profile restricts the features and options available to users in a particular PDB. The `PDB_OS_CREDENTIAL` initialization parameter can specify a unique operating system user for a PDB to limit operating system access. Also, when the `PATH_PREFIX` and `CREATE_FILE_DEST` clauses are specified during PDB creation, they limit file system access.

PDB Lockdown Profiles

When identities are shared between PDBs, elevated privileges might exist. You can use lockdown profiles to prevent this elevation of privileges. Identities can be shared in the following situations:

- At the operating system level, when the database interacts with operating system resources such as files or processes
- At the network level, when the database communicates with other systems
- Inside the database, as PDBs access or create common objects or communicate across container boundaries using features such as database links

To increase security, a CDB administrator might want to use PDB lockdown profiles to restrict users in particular PDBs. A PDB lockdown profile can disable users from running specified SQL statements, such as `ALTER SYSTEM` statements, or disable access to a package that can access the network, such as the `UTL_SMTP` package. A PDB lockdown profile can also restrict access to common users, common objects, and administrative tools, such as Oracle XML DB, administrative features, such as cursor sharing, and database options, such as Oracle Database Advanced Queuing. PDB lockdown profiles can prohibit the use of the XDB protocols (FTP, HTTP, HTTPS) by a PDB with the `XDB_PROTOCOLS` feature.

You create a PDB lockdown profile in a CDB with the `CREATE LOCKDOWN PROFILE` statement. You can add and remove restrictions with the `ALTER LOCKDOWN PROFILE` statement. Only a common user with common `SYSDBA` or common `ALTER SYSTEM` privileges can create or alter a lockdown profile.

You specify a PDB lockdown profile by using the `PDB_LOCKDOWN` initialization parameter. You can set this parameter at the PDB level, in which case the profile applies only to the PDB in which it is set, or at the CDB level, in which case the profile applies to all PDBs. A common user can override a CDB-wide setting for a specific PDB, but only if the user has common `SYSDBA` or common `ALTER SYSTEM` privileges.

See Also:

- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=DBSEG-GUID-AB5E62DB-7E2A-4B5A-BA96-A2BD2DF15275)
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQLRF57092) for more information about the `CREATE LOCKDOWN PROFILE` statement
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=REFRN-GUID-27072E94-1E1D-4BB0-AEAE-D7AFDC02E0A1) for more information about the `PDB_LOCKDOWN` initialization parameter

The PDB\_OS\_CREDENTIAL Initialization Parameter

When the database accesses an external procedure with the `extproc` agent, the `PDB_OS_CREDENTIAL` initialization parameter determines the identity of the operating system user (OS user) employed when interacting with the operating system from a PDB. Using an OS user described by a credential whose name is specified as a value of the `PDB_OS_CREDENTIAL` initialization parameter can ensure that operating system interactions are performed as a less powerful user and provides the ability to protect data belonging to one PDB from being accessed by users connected to another PDB. A credential is an object that is created using the `CREATE_CREDENTIAL` procedure in the `DBMS_CREDENTIAL` package.

The Oracle OS user is usually a highly privileged user, and using that user for operating system interactions is not recommended. Also, using the same OS user for operating system interactions from different PDBs might compromise data belonging to a given PDB.

See Also:

- " [Managing Processes for External Procedures](managing-processes.md) "
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=REFRN-GUID-E563FDDA-6840-42CC-944D-5B0FD60C9003) for more information about the `PDB_OS_CREDENTIAL` initialization parameter
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=ARPLS-GUID-D5791B72-E0F6-4C41-AD3E-DDEDFFCA7D0C)

The PATH\_PREFIX and CREATE\_FILE\_DEST PDB Creation Clauses

The `PATH_PREFIX` clause of the `CREATE PLUGGABLE DATABASE` statement ensures that all directory object paths associated with the PDB are restricted to the specified directory or its subdirectories. It also ensures that the following files associated with the PDB are restricted to specified directory: the Oracle XML repository for the PDB, files created with a `CREATE PFILE` statement, and the export directory for Oracle wallets.

The `CREATE_FILE_DEST` clause of the `CREATE PLUGGABLE DATABASE` statement ensures that all the database files belonging to the PDB are restricted to the specified directory and its subdirectories. The clause enables Oracle Managed Files for the PDB and specifies the default file system directory or Oracle ASM disk group for the PDB's files.

See Also:

- " [Restrictions on PDB File Locations](creating-and-removing-pdbs-with-sql-plus.md) "
- " [CREATE\_FILE\_DEST Clause](creating-and-removing-pdbs-with-sql-plus.md) "

**Parent topic:** About Administering a CDB

### 41.2 Accessing a Container in a CDB with SQL\*Plus

You can access a container in a CDB with SQL\*Plus.

- About Accessing a Container in a CDB with SQL\*Plus  
	You can use SQL\*Plus to access the root or a PDB in a CDB. You can connect to a container by using the SQL\*Plus `CONNECT` command, or you can switch into a container with an `ALTER` `SESSION` `SET` `CONTAINER` SQL statement.
- Connecting to a Container Using the SQL\*Plus CONNECT Command  
	You can use the SQL\*Plus `CONNECT` command to connect to the root or to a PDB.
- Switching to a Container Using the ALTER SESSION Statement  
	When you are connected to a container as a common user, you can switch to a different container and application service using the `ALTER SESSION` statement.

**Parent topic:** Administering a CDB with SQL\*Plus

#### 41.2.1 About Accessing a Container in a CDB with SQL\*Plus

You can use SQL\*Plus to access the root or a PDB in a CDB. You can connect to a container by using the SQL\*Plus `CONNECT` command, or you can switch into a container with an `ALTER` `SESSION` `SET` `CONTAINER` SQL statement.

This section assumes that you understand how to connect to a non-CDB in SQL\*Plus. See " [Submitting Commands and SQL to the Database](getting-started-with-database-administration.md) " for information.

Clients access the root or a PDB through database services. Database services have an optional `PDB` property. When a PDB is created, a new default service for the PDB is created automatically. The service has the same name as the PDB. With the service name, you can access the PDB using the easy connect syntax or the net service name from the tnsnames.ora file. Oracle Net Services must be configured properly for clients to access this service.

When a user connects using a service with a non-null `PDB` property, the user name is resolved in the context of the specified PDB. When a user connects without specifying a service or using a service name with a null `PDB` property, the user name is resolved in the context of the root. You can view the `PDB` property for a service by querying the `CDB_SERVICES` data dictionary view or by running the `config` `service` command in the SRVCTL utility.

The setting for the `SESSIONS` initialization parameter limits the total number of sessions available in a CDB, including the sessions connected to PDBs. If the limit is reached for the CDB, then users cannot connect to PDBs. To ensure that one PDB does not use too many sessions, you can limit the number of sessions available to a PDB by setting the `SESSIONS` initialization parameter in the PDB.

Note:

When two or more CDBs on the same computer system use the same listener and two or more PDBs have the same service name in these CDBs, a connection that specifies this service name connects randomly to one of the PDBs with the service name. To avoid incorrect connections, ensure that all service names for PDBs are unique on the computer system, or configure a separate listener for each CDB on the computer system.

See Also:

- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=CNCPT89270) for more information about database services in a CDB
- [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=NETAG001) for information about configuring Oracle Net Services
- " [Managing Services Associated with PDBs](administering-pdbs-with-sql-plus.md) "
- [Example 45-9](viewing-information-about-cdbs-and-pdbs-with-sql-plus.md)
- " [Listing the Initialization Parameters That Are Modifiable in PDBs](viewing-information-about-cdbs-and-pdbs-with-sql-plus.md) "

**Parent topic:** Accessing a Container in a CDB with SQL\*Plus

#### 41.2.2 Connecting to a Container Using the SQL\*Plus CONNECT Command

You can use the SQL\*Plus `CONNECT` command to connect to the root or to a PDB.

- Connecting to the Root Using the SQL\*Plus CONNECT Command  
	You can connect to the root in the same way that you connect to a non-CDB.
- Connecting to a PDB Using the SQL\*Plus CONNECT Command  
	To connect to a PDB with the SQL\*Plus `CONNECT` command, you can use easy connect or a net service name.

**Parent topic:** Accessing a Container in a CDB with SQL\*Plus

##### 41.2.2.1 Connecting to the Root Using the SQL\*Plus CONNECT Command

You can connect to the root in the same way that you connect to a non-CDB.

Specifically, you can use the following techniques to connect to the root with the SQL\*Plus `CONNECT` command:

- Local connection
- Local connection with operating system authentication
- Database connection using easy connect
- Database connection using a net service name
- Remote database connection using external authentication

The following prerequisites must be met for the user connecting to the root:

- The user must be a common user.
- The user must be granted `CREATE` `SESSION` privilege in the root.

To connect to the root using the SQL\*Plus CONNECT command:

1. Configure your environment so that you can open SQL\*Plus.
	See " [Connecting to the Database with SQL\*Plus](getting-started-with-database-administration.md) ".
2. Start SQL\*Plus with the `/NOLOG` argument:
	```
	sqlplus /nolog
	```
3. Issue a SQL\*Plus `CONNECT` command to connect to the root, as shown in the following examples.

Example 41-1 Connecting to the Root with a Local Connection

This example connects to the root in the local CDB as user `SYSTEM`. SQL\*Plus prompts for the `SYSTEM` user password.

```
connect system
```

Example 41-2 Connecting to the Root with Operating System Authentication

This example connects locally to the root with the `SYSDBA` administrative privilege with operating system authentication.

```
connect / as sysdba
```

Example 41-3 Connecting to the Root with a Net Service Name

Assume that clients are configured to have a net service name for the root in the CDB. For example, the net service name can be part of an entry in a tnsnames.ora file.

This example connects as common user `c##dba` to the database service designated by the net service name `mycdb`. SQL\*Plus prompts for the `c##dba` user password.

```
connect c##dba@mycdb
```

See Also:

" [Submitting Commands and SQL to the Database](getting-started-with-database-administration.md) "

**Parent topic:** Connecting to a Container Using the SQL\*Plus CONNECT Command

##### 41.2.2.2 Connecting to a PDB Using the SQL\*Plus CONNECT Command

To connect to a PDB with the SQL\*Plus `CONNECT` command, you can use easy connect or a net service name.

To connect to a PDB, a user must be one of the following:

- A common user with a `CREATE` `SESSION` privilege granted commonly or granted locally in the PDB
- A local user defined in the PDB with `CREATE` `SESSION` privilege

Only a user with `SYSDBA`, `SYSOPER`, `SYSBACKUP`, or `SYSDG` privilege can connect to a PDB that is in mounted mode. To change the open mode of a PDB, see " Modifying the Open Mode of PDBs ".

To connect to a PDB using the SQL\*Plus CONNECT command:

1. Configure your environment so that you can open SQL\*Plus.
	See " [Connecting to the Database with SQL\*Plus](getting-started-with-database-administration.md) ".
2. Start SQL\*Plus with the `/NOLOG` argument:
	```
	sqlplus /nolog
	```
3. Issue a SQL\*Plus `CONNECT` command using easy connect or a net service name to connect to the PDB.

Example 41-4 Connecting to a PDB

Assume that clients are configured to have a net service name for each PDB that matches each PDB name. For example, the net service name can be part of an entry in a tnsnames.ora file.

The following command connects to the `sh` local user in the `salespdb` PDB:

```
CONNECT sh@salespdb
```

The following command connects to the `SYSTEM` common user in the `salespdb` PDB:

```
CONNECT system@salespdb
```

See " [Step 4: Submit the SQL\*Plus CONNECT Command](getting-started-with-database-administration.md) " for more examples.

**Parent topic:** Connecting to a Container Using the SQL\*Plus CONNECT Command

#### 41.2.3 Switching to a Container Using the ALTER SESSION Statement

When you are connected to a container as a common user, you can switch to a different container and application service using the `ALTER SESSION` statement.

You can use the following statement to switch to a different container and application service:

```
ALTER SESSION SET CONTAINER = container_name [SERVICE = service_name]
```

For container\_name, specify one of the following:

- `CDB$ROOT` to switch to the CDB root
- `PDB$SEED` to switch to the CDB seed
- A PDB name to switch to the PDB
	When the current container is the root, you can view the names of the PDBs in a CDB by querying the `DBA_PDBS` view.

For service\_name, specify a service that is running in the PDB. You can list the services running in the containers of a CDB, excluding the CDB root, by issuing the following query with the CDB root as the current container:

```
COL NAME FORMAT A30
COL CON_NAME FORMAT A20

SELECT NAME,CON_NAME, CON_ID
  FROM V$ACTIVE_SERVICES
  WHERE UPPER(NAME) != CON_NAME
  AND CON_ID !=1
  ORDER BY CON_ID;
```

By default, when you switch to a container, the session uses the default service for the container. However, the default PDB service does not support all of the service attributes and features such as service metrics, Fast Application Notification (FAN), load balancing, Resource Manager, Transaction Guard, Application Continuity, and so on. It is best practice to use a non-default service for the container by specifying `SERVICE = service_name`, where service\_name is the name of the service.

With this new capability, connection pools can switch the service, and, when needed the PDB, on a connection when a connection is borrowed from the pool. Starting with Oracle Database 12c Release 2 (12.2.0.1), connection pools support more than one database service with universal connection pools (UCPs). It can also be used standalone.

When switching to a service, applications are able to consolidate to a CDB, while keeping the database services identified, prioritized, measured, and highly available. Switching to a non-default service provides the following benefits:

- It preserves the service attributes and features.
- It eliminates too many connection pools with too many connections serving these tenants.
- It allows applications to use more database services for workload control without consuming too many connection pools. Customers are able to identify and prioritize workloads using services without over sizing the database connections.

The following are considerations for using the `ALTER` `SESSION` `SET` `CONTAINER` statement:

- After the statement completes successfully, the current schema of the session is set to the schema owned by the common user in the specified container.
- After the statement completes successfully, the security context is reset to that of the schema owned by the common user in the specified container.
- After the statement completes successfully, login triggers for the specified container do not fire.
	If you require a trigger, then you can define a before or after `SET CONTAINER` trigger in a PDB to fire before or after the `ALTER` `SESSION` `SET` `CONTAINER` statement is executed.
- After the statement completes successfully and the `SERVICE` clause specifies a non-default service for the PDB, the session is using a new service with attributes set, including metrics, FAN, TAF, Application Continuity, Transaction Guard, `drain_timeout`, and `stop_option` for the new service.
- Package states are not shared across containers.
- When closing a PDB, sessions that switched into the PDB and sessions that connected directly to the PDB are handled identically.
- A transaction cannot span multiple containers. If you start a transaction and use `ALTER` `SESSION` `SET` `CONTAINER` to switch to a different container, then you cannot issue DML, DDL, `COMMIT`, or `ROLLBACK` statements until you switch back to the container in which you started the transaction.
- If you open a cursor and use `ALTER` `SESSION` `SET` `CONTAINER` to switch to different container, then you cannot fetch data from that cursor until you switch back to the container in which the cursor was opened.
- You can use the `ALTER` `SESSION` `SET` `CONTAINER` statement with the `SERVICE` clause for connection pooling as well as advanced CDB administration.
	For example, you can use this statement for connection pooling with PDBs for a multitenancy application. A multitenancy application uses a single instance of the software on a server to serve multiple customers (tenants). In a non-CDB, multitenancy is typically supported by adding an extra column that identifies the tenant to every table used by the application, and tenants check out connections from a connection pool. In a CDB with PDBs, each tenant can have its own PDB, and you can use the `ALTER` `SESSION` `SET` `CONTAINER` statement in a connection pooling configuration.
- When working with connection pools that serve applications, the applications may be using data sources with different services. Using the `ALTER SESSION SET CONTAINER` statement with the `SERVICE` clause enables the connection pool to use the same connections for many applications, sharing the services.

The following prerequisites must be met to use the `ALTER` `SESSION` `SET` `CONTAINER` statement:

- The current user must be a common user. The initial connection must be made using the SQL\*Plus `CONNECT` command.
- When altering a session to switch to a PDB as a common user that was not supplied with Oracle Database, the current user must be granted the `SET` `CONTAINER` privilege commonly or must be granted this privilege locally in the PDB.

Note:

When an `ALTER` `SESSION` `SET` `CONTAINER` statement is used to switch to the current container, these prerequisites are not enforced, and no error message is returned if they are not met.

Before issuing an `ALTER SESSION SET CONTAINER` statement with the `SERVICE` clause, the following prerequisites must be met:

- The service switched to must be active. You cannot switch to a service that is not running.
- When switching between services, the service attributes of the service being switched from and the service being switched to must match. For example, the services switched from and to must all have TAF, or must all use Application Continuity, or must all have `drain_timeout` set.

To switch to a container using the ALTER SESSION statement:

1. In SQL\*Plus, connect to a container as a common user with the required privileges.
	See " Connecting to a Container Using the SQL\*Plus CONNECT Command ".
2. Check the current open mode of the container to which you are switching.
	To check the current open mode of the root or a PDB, query the `OPEN_MODE` column in the `V$CONTAINERS` view when the current container is the root.
	If the open mode of the root should be changed, then follow the instructions in " [Altering Database Availability](starting-up-and-shutting-down.md) " to change the open mode.
	If the open mode of the PDB should be changed, then follow the instructions in " Modifying the Open Mode of PDBs " to change the open mode.
	The open mode of the root imposes limitations on the open mode of PDBs. For example, the root must be open before any PDBs can be open. Therefore, you might need to change the open mode of the root before changing the open mode of a PDB.
3. If you are switching to a specific service, then ensure that the service is running.
	To check the active status of the service, query the `V$ACTIVE_SERVICES` view when the current container is the CDB root.
	If the service is not running, then use the SRVCTL utility or the `DBMS_SERVICE` package to start the service.
4. Run the `ALTER` `SESSION` `SET` `CONTAINER` statement and specify the container to which you want to switch.
	Include the `SERVICE` clause to switch to a specific application service.

The following examples switch to various containers using `ALTER` `SESSION`.

Example 41-5 Switching to the PDB salespdb and Using the salesrep Service

```
ALTER SESSION SET CONTAINER = salespdb SERVICE = salesrep;
```

Example 41-6 Switching to the PDB salespdb and Using the Default Service

```
ALTER SESSION SET CONTAINER = salespdb;
```

Example 41-7 Switching to the CDB Root

```
ALTER SESSION SET CONTAINER = CDB$ROOT;
```

Example 41-8 Switching to the CDB Seed

```
ALTER SESSION SET CONTAINER = PDB$SEED;
```

Example 41-9 Switching Services Using a Dummy Service in the CDB Root

To design connection pooling that switches the container and the service, one method is to create a dummy service in the CDB root and set all required service attributes on this dummy service (for example, `drain_timeout`, TAF or Application Continuity). The service attributes must match across the CDB root and the PDB. To use this method, complete the following steps:

1. Connect to the dummy service when first creating the connection pool and when creating new connections.
2. As services are added to each PDB, set the same attributes on these real services.
3. When an application requires a connection, complete one of the following actions:
	- Create a new connection to the dummy service, and switch to the PDB and service.
		- Borrow a free connection in the pool and switch to the PDB and service.
		You do not need to return to the CDB root when switching across PDBs.

You do not need to return to the CDB root when switching across PDBs.

See Also:

- " [About Database Resident Connection Pooling](https://docs.oracle.com/en/database/oracle/oracle-database/12.2/admin/managing-processes.html#GUID-BB76E57C-3F16-4C85-AEF6-BA14FC1B4777 "Database Resident Connection Pooling (DRCP) provides a connection pool in the database server for typical Web application usage scenarios where the application acquires a database connection, works on it for a relatively short duration, and then releases it. DRCP pools \"dedicated\" servers. A pooled server is the equivalent of a server foreground process and a database session combined.") "
- [Oracle Universal Connection Pool Developer’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=JJUCP-GUID-82ACD002-4C5F-4BF7-99FF-46A2A97DD35D) for more information about universal connection pools

**Parent topic:** Accessing a Container in a CDB with SQL\*Plus

### 41.3 Executing Code in Containers Using the DBMS\_SQL Package

When you are executing PL/SQL code in a container in a CDB, and you want to execute one or more SQL statements in a different container, use the `DBMS_SQL` package to switch containers.

For example, you can use the `DBMS_SQL` package to switch containers when you need to perform identical actions in more than one container.

The following are considerations for using `DBMS_SQL` to switch containers:

- A transaction cannot span multiple containers.
	If the set of actions you must perform in the target container requires a transaction, then consider using an autonomous transaction and perform a commit or rollback as the last action.
- `SET` `ROLE` statements are not allowed.

Example 41-10 Performing Identical Actions in More Than One Container

This example includes a PL/SQL block that creates the `identact` table in the `hr` schema in two PDBs (`pdb1` and `pdb2`). The example also inserts a row into the `identact` table in both PDBs.

```
DECLARE
  c1 INTEGER;
  rowcount INTEGER;
  taskList VARCHAR2(32767) :=
    'DECLARE
      PRAGMA AUTONOMOUS TRANSACTION;
     BEGIN
       -- Create the hr.identact table.
       EXECUTE IMMEDIATE
         ''CREATE TABLE hr.identact
             (actionno NUMBER(4) NOT NULL,
              action VARCHAR2 (10))'';
       EXECUTE IMMEDIATE
         ''INSERT INTO identact VALUES(1, 'ACTION1')'';
       -- A commit is required if the tasks include DML.
       COMMIT;
       EXCEPTION
         WHEN OTHERS THEN
           -- If there are errors, then drop the table.
           BEGIN
             EXECUTE IMMEDIATE ''DROP TABLE identact'';
           EXCEPTION
            WHEN OTHERS THEN
              NULL;
            END;
        END;';
  TYPE containerListType IS TABLE OF VARCHAR2(128) INDEX BY PLS_INTEGER;
  containerList  containerListType;
BEGIN
  containerList(1) := 'PDB1';
  containerList(2) := 'PDB2';
  c1 := DBMS_SQL.OPEN_CURSOR;
  FOR conIndex IN containerList.first..containerList.last LOOP
    DBMS_OUTPUT.PUT_LINE('Creating in container: ' || containerList(conIndex));
    DBMS_SQL.PARSE(c => c1 ,
                   statement => taskList,
                   language_flag => DBMS_SQL.NATIVE,
                   edition= > NULL,
                   apply_crossedition_trigger => NULL,
                   fire_apply_trigger => NULL,
                   schema => 'HR',
                   container => containerList(conIndex));
     rowcount := DBMS_SQL.EXECUTE(c=>c1);
  END LOOP;
  DBMS_SQL.CLOSE_CURSOR(c=>c1);
END;
/
```

See Also:

- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=ARPLS058) for more information about the `DBMS_SQL` package
- [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=LNPLS00609) for more information about autonomous transactions

**Parent topic:** Administering a CDB with SQL\*Plus

### 41.4 Modifying a CDB

You can modify the entire CDB, the root, or one or more PDBs.

- About Modifying a CDB  
	The `ALTER` `DATABASE` statement modifies a CDB. The `ALTER` `PLUGGABLE` `DATABASE` statement can modify the open mode of one or more PDBs.
- About the Statements That Modify a CDB  
	When connected as a common user whose current container is the root, the `ALTER` `DATABASE` statement works the same in a CDB and a non-CDB.
- Managing Tablespaces in a CDB  
	You can manage tablespaces in a CDB.
- Modifying an Entire CDB  
	You can use the `ALTER` `DATABASE` statement to modify an entire CDB, including the root and all of the PDBs. Most `ALTER` `DATABASE` statements modify the entire CDB.
- Modifying the Root  
	You can use the `ALTER` `DATABASE` statement to modify only the root of a CDB.
- Modifying the Open Mode of PDBs  
	You can modify the open mode of a PDB by using the `ALTER` `PLUGGABLE` `DATABASE` SQL statement or the SQL\*Plus `STARTUP` command.
- Preserving or Discarding the Open Mode of PDBs When the CDB Restarts  
	You can preserve the open mode of one or more PDBs when the CDB restarts by using the `ALTER` `PLUGGABLE` `DATABASE` SQL statement with a pdb\_save\_or\_discard\_state clause.

**Parent topic:** Administering a CDB with SQL\*Plus

#### 41.4.1 About Modifying a CDB

The `ALTER` `DATABASE` statement modifies a CDB. The `ALTER` `PLUGGABLE` `DATABASE` statement can modify the open mode of one or more PDBs.

Table 41-3 lists which containers are modified by clauses in `ALTER` `DATABASE` and `ALTER` `PLUGGABLE` `DATABASE` statements.

Table 41-3 Statements That Modify Containers in a CDB

| Modify Entire CDB | Modify Root Only | Modify One or More PDBs |
| --- | --- | --- |
| When connected as a common user whose current container is the root, `ALTER` `DATABASE` statements with the following clauses modify the entire CDB:  - [startup\_clauses](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQLRF52389) - [recovery\_clauses](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQLRF52390) - [logfile\_clauses](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQLRF52402) - [controlfile\_clauses](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQLRF52410) - [standby\_database\_clauses](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQLRF52412) - [instance\_clauses](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQLRF52423) - [security\_clause](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQLRF52424) - [`RENAME` `GLOBAL_NAME` clause](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQLRF52547) - [`ENABLE` `BLOCK` `CHANGE` `TRACKING` clause](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQLRF52549) - [`DISABLE` `BLOCK` `CHANGE` `TRACKING` clause](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQLRF52550) | When connected as a common user whose current container is the root, `ALTER` `DATABASE` statements with the following clauses modify the root only:  - [database\_file\_clauses](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQLRF52396) - [`DEFAULT` `EDITION` clause](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQLRF52540) - [`DEFAULT` `TABLESPACE` clause](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQLRF52543) - [`DEFAULT` `TEMPORARY` `TABLESPACE` clause](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQLRF52544)  `ALTER` `DATABASE` statements with the following clauses modify the root and set default values for PDBs:  - [flashback\_mode\_clause](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQLRF52421) - [`SET` `DEFAULT` { `BIGFILE` \| `SMALLFILE` } `TABLESPACE` clause](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQLRF52542) - [set\_time\_zone\_clause](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQLRF52421)  You can use these clauses to set non-default values for specific PDBs. | When connected as a common user whose current container is the root, `ALTER` `PLUGGABLE` `DATABASE` statements with the following clause can modify the open mode of one or more PDBs:  - [pdb\_change\_state](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQLRF55686)  When the current container is a PDB, `ALTER` `PLUGGABLE` `DATABASE` statements with this clause can modify the open mode of the current PDB. See " [Modifying a PDB with the ALTER PLUGGABLE DATABASE Statement](administering-pdbs-with-sql-plus.md) ".  When connected as a common user whose current container is the root, `ALTER` `PLUGGABLE` `DATABASE` statements with the following clause can preserve or discard the open mode a PDB when the CDB restarts:  - [pdb\_save\_or\_discard\_state](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQLRF55686) |

This section contains the following topics:

- About the Statements That Modify a CDB
- About Managing Tablespaces in a CDB
- Modifying an Entire CDB
- Modifying the Root
- Modifying the Open Mode of PDBs
- Preserving or Discarding the Open Mode of PDBs When the CDB Restarts

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQLRF00802)
- " About the Current Container "

**Parent topic:** Modifying a CDB

#### 41.4.2 About the Statements That Modify a CDB

When connected as a common user whose current container is the root, the `ALTER` `DATABASE` statement works the same in a CDB and a non-CDB.

Most `ALTER` `DATABASE` statements affect the entire CDB. The exceptions are listed in the "Modify Root Only" column of Table 41-3.

When an `ALTER` `DATABASE` statement with the `RENAME` `GLOBAL_NAME` clause modifies the domain of a CDB, it affects the domain of each PDB with a domain that defaults to that of the CDB.

When connected as a common user whose current container is the root, the `ALTER` `PLUGGABLE` `DATABASE` statement with the pdb\_change\_state clause modifies the open mode of one or more PDBs.

When the current container is a PDB, `ALTER` `DATABASE` and `ALTER` `PLUGGABLE` `DATABASE` statements modify the current PDB only.

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQLRF55667)
- " [Modifying a PDB](administering-pdbs-with-sql-plus.md) "

**Parent topic:** Modifying a CDB

#### 41.4.3 Managing Tablespaces in a CDB

You can manage tablespaces in a CDB.

- About Managing Tablespaces in a CDB  
	A tablespace is a logical storage container for database objects, such as tables and indexes, that consume storage space. At the physical level, a tablespace stores data in one or more data files or temp files. You can use the `ALTER` `DATABASE` statement to manage tablespaces in a CDB.
- About Managing Permanent Tablespaces in a CDB  
	A permanent tablespace can be associated with only one container. Therefore, a permanent tablespace can be associated with the root or with one PDB.
- About Managing Temporary Tablespaces in a CDB  
	Each container in a CDB has its own default temporary tablespace (or tablespace group).

**Parent topic:** Modifying a CDB

##### 41.4.3.1 About Managing Tablespaces in a CDB

A tablespace is a logical storage container for database objects, such as tables and indexes, that consume storage space. At the physical level, a tablespace stores data in one or more data files or temp files. You can use the `ALTER` `DATABASE` statement to manage tablespaces in a CDB.

The following are considerations for tablespaces in a CDB:

- A permanent tablespace can be associated with only one container.
- When you create a tablespace in a container, the tablespace is associated with that container.
- When local undo is disabled for a CDB, the CDB has only one active undo tablespace, or one active undo tablespace for each instance of an Oracle RAC CDB. When local undo is enabled for a CDB, each container in the CDB has its own undo tablespace.
- A local undo tablespace is required for each node in an Oracle Real Application Clusters (Oracle RAC) cluster in which the PDB is open.
- There is one default temporary tablespace each container in the CDB, including the CDB root, each PDB, each application root, and each application PDB.

**Parent topic:** Managing Tablespaces in a CDB

##### 41.4.3.2 About Managing Permanent Tablespaces in a CDB

A permanent tablespace can be associated with only one container. Therefore, a permanent tablespace can be associated with the root or with one PDB.

Each container in a CDB must have its own default permanent tablespace, and default permanent tablespaces cannot be shared between containers. Users connected to the container who are not explicitly assigned a tablespace use the default permanent tablespace for the container.

**Parent topic:** Managing Tablespaces in a CDB

##### 41.4.3.3 About Managing Temporary Tablespaces in a CDB

Each container in a CDB has its own default temporary tablespace (or tablespace group).

You also can create additional temporary tablespaces for individual containers, and you can assign specific users in containers to these temporary tablespaces. When you unplug a PDB, its temporary tablespaces are also unplugged.

When a user is not assigned a temporary tablespace explicitly in a container, the user’s temporary tablespace is the default temporary tablespace for the container.

#### 41.4.4 Modifying an Entire CDB

You can use the `ALTER` `DATABASE` statement to modify an entire CDB, including the root and all of the PDBs. Most `ALTER` `DATABASE` statements modify the entire CDB.

See the "Modify Entire CDB" column of Table 41-3 for a list of these statements.

To modify an entire CDB, the following prerequisites must be met:

- The current user must be a common user with the `ALTER` `DATABASE` privilege.
- To run an `ALTER` `DATABASE` statement with a recovery\_clause, the current user must have the `SYSDBA` administrative privilege commonly granted. In this case, you must exercise this privilege using `AS` `SYSDBA` at connect time.

To modify an entire CDB:

1. In SQL\*Plus, ensure that the current container is the root.
	See " Accessing a Container in a CDB with SQL\*Plus ".
2. Run an `ALTER` `DATABASE` statement with a clause that modifies an entire CDB.

Example 41-11 Backing Up the Control File for a CDB

This `ALTER` `DATABASE` statement uses a recovery\_clause to back up a control file.

```
ALTER DATABASE BACKUP CONTROLFILE TO '+DATA/dbs/backup/control.bkp';
```

Example 41-12 Adding a Redo Log File to a CDB

This `ALTER` `DATABASE` statement uses a logfile\_clause to add redo log files.

```
ALTER DATABASE cdb ADD LOGFILE
  GROUP 4 ('/u01/logs/orcl/redo04a.log','/u02/logs/orcl/redo04b.log')
  SIZE 100M BLOCKSIZE 512 REUSE;
```

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQLRF00802)

**Parent topic:** Modifying a CDB

#### 41.4.5 Modifying the Root

You can use the `ALTER` `DATABASE` statement to modify only the root of a CDB.

When the current container is the root, these `ALTER` `DATABASE` statements modify the root without directly modifying any of the PDBs. See the "Modify Root Only" column of Table 41-3 for a list of these statements.

Some of these statements set the defaults for the PDBs in the CDB. You can overwrite these defaults for a PDB by using the `ALTER` `PLUGGABLE` `DATABASE` statement.

To modify the root, the current user must have the `ALTER` `DATABASE` privilege in the root.

To modify the root:

1. In SQL\*Plus, ensure that the current container is the root.
	See " Accessing a Container in a CDB with SQL\*Plus ".
2. Run an `ALTER` `DATABASE` statement with a clause that modifies the root.

The following examples modify the root.

A user whose current container is the root that is not explicitly assigned a tablespace uses the default permanent tablespace for the root. The tablespace specified in the `ALTER` `DATABASE` statement must exist in the root.

After executing this statement, the default type of subsequently created tablespaces in the root is bigfile. This setting is also the default for PDBs.

The tablespace or tablespace group specified in the `ALTER` `DATABASE` statement must exist in the root.

Example 41-13 Changing the Default Permanent Tablespace for the Root

This `ALTER` `DATABASE` statement uses a `DEFAULT` `TABLESPACE` clause to set the default permanent tablespace to `root_tbs` for the root.

```
ALTER DATABASE DEFAULT TABLESPACE root_tbs;
```

Example 41-14 Bringing a Data File Online for the Root

This `ALTER` `DATABASE` statement uses a database\_file\_clause to bring the /u02/oracle/cdb\_01.dbf data file online.

```
ALTER DATABASE DATAFILE '/u02/oracle/cdb_01.dbf' ONLINE;
```

Example 41-15 Changing the Default Tablespace Type for the Root

This `ALTER` `DATABASE` statement uses a `SET` `DEFAULT` `TABLESPACE` clause to change the default tablespace type to bigfile for the root.

```
ALTER DATABASE SET DEFAULT BIGFILE TABLESPACE;
```

Example 41-16 Changing the Default Temporary Tablespace for the Root

This `ALTER` `DATABASE` statement uses a `DEFAULT` `TEMPORARY` `TABLESPACE` clause to set the default temporary tablespace to `root_temp` for the root.

```
ALTER DATABASE DEFAULT TEMPORARY TABLESPACE root_temp;
```

See Also:

- " [Modifying a PDB](administering-pdbs-with-sql-plus.md) "
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQLRF00802)

**Parent topic:** Modifying a CDB

#### 41.4.6 Modifying the Open Mode of PDBs

You can modify the open mode of a PDB by using the `ALTER` `PLUGGABLE` `DATABASE` SQL statement or the SQL\*Plus `STARTUP` command.

- About the Open Mode of a PDB  
	A PDB can be in various modes.
- About Modifying the Open Mode of PDBs with ALTER PLUGGABLE DATABASE  
	When the current container is the root, an `ALTER` `PLUGGABLE` `DATABASE` statement with a pdb\_change\_state clause modifies the open mode of the specified PDBs.
- About Modifying the Open Mode of PDBs with the SQL\*Plus STARTUP Command  
	When the current container is the root, the `STARTUP` `PLUGGABLE` `DATABASE` command can open a single PDB.
- Modifying the Open Mode of PDBs with ALTER PLUGGABLE DATABASE  
	You can modify the open mode of PDBs with the `ALTER` `PLUGGABLE` `DATABASE` statement with a pdb\_change\_state clause.
- Modifying the Open Mode of PDBs with the SQL\*Plus STARTUP Command  
	You can use the `STARTUP` `PLUGGABLE` `DATABASE` command to open a single PDB.

**Parent topic:** Modifying a CDB

##### 41.4.6.1 About the Open Mode of a PDB

A PDB can be in various modes.

Table 41-4 describes the possible PDB modes.

Table 41-4 PDB Modes

| Mode | Description |
| --- | --- |
| `OPEN` `READ` `WRITE` | A PDB in open read/write mode allows queries and user transactions to proceed and allows users to generate redo logs. |
| `OPEN` `READ` `ONLY` | A PDB in open read-only mode allows queries but does not allow user changes. |
| `OPEN` `MIGRATE` | When a PDB is in open migrate mode, you can run database upgrade scripts on the PDB.  A PDB is in this mode after an `ALTER` `DATABASE` `OPEN` `UPGRADE` is run. |
| `MOUNTED` | When a PDB is in mounted mode, it behaves like a non-CDB in mounted mode. It does not allow changes to any objects, and it is accessible only to database administrators. It cannot read from or write to data files. Information about the PDB is removed from memory caches. Cold backups of the PDB are possible. |

The open read/write, read-only, and migrate modes can be restricted to users with `RESTRICTED` `SESSION` privilege in the PDB.

While a PDB is in mounted or read-only mode, database administrators can create, modify, or drop common users and roles in the CDB. The CDB applies these changes to the PDB when its open mode is changed to open in read/write mode. Before the changes are applied, descriptions of common users and roles in the PDB might be different from the descriptions in the rest of the CDB.

When a PDB is opened, Oracle Database checks the compatibility of the PDB with the CDB. Each compatibility violation is either a warning or an error. If a compatibility violation is a warning, then the warning is recorded in the alert log, but the PDB is opened normally without displaying a warning message. If a compatibility violation is an error, then a message is displayed when the PDB is opened stating that the PDB was altered with errors, and the errors are recorded in the alert log. You must correct the condition that caused each error. When there are errors, the PDB is opened, but access to the PDB is limited to users with `RESTRICTED` `SESSION` privilege so that the compatibility violations can be addressed. You can view descriptions of violations by querying `PDB_PLUG_IN_VIOLATIONS` view.

See Also:

- " Modifying the Open Mode of PDBs " for information about modifying the open mode of one or more PDBs when the current container is the root
- " [Modifying a PDB with the ALTER PLUGGABLE DATABASE Statement](administering-pdbs-with-sql-plus.md) " for information about modifying the open mode of a PDB when the current container is the PDB
- " Shutting Down a CDB Instance "
- " [Modifying a PDB](administering-pdbs-with-sql-plus.md) " for information about modifying other attributes of a PDB

**Parent topic:** Modifying the Open Mode of PDBs

##### 41.4.6.2 About Modifying the Open Mode of PDBs with ALTER PLUGGABLE DATABASE

When the current container is the root, an `ALTER` `PLUGGABLE` `DATABASE` statement with a pdb\_change\_state clause modifies the open mode of the specified PDBs.

The following table describes the clauses of the `ALTER` `PLUGGABLE` `DATABASE` statement that modify the mode of a PDB.

Table 41-5 ALTER PLUGGABLE DATABASE Clauses That Modify the Mode of a PDB

| Clause | Description |
| --- | --- |
| `OPEN` `READ` `WRITE` `[RESTRICTED] [FORCE]` | Opens the PDB in read/write mode.  When `RESTRICTED` is specified, the PDB is accessible only to users with `RESTRICTED` `SESSION` privilege in the PDB. All sessions connected to the PDB that do not have `RESTRICTED` `SESSION` privilege on it are terminated, and their transactions are rolled back.  When `FORCE` is specified, the statement opens a PDB that is currently closed and changes the open mode of a PDB that is in open read-only mode. |
| `OPEN` `READ` `ONLY` `[RESTRICTED] [FORCE]` | Opens the PDB in read-only mode.  When `RESTRICTED` is specified, the PDB is accessible only to users with `RESTRICTED` `SESSION` privilege in the PDB. All sessions connected to the PDB that do not have `RESTRICTED` `SESSION` privilege on it are terminated.  When `FORCE` is specified, the statement opens a PDB that is currently closed and changes the open mode of a PDB that is in open read/write mode. |
| `OPEN` `UPGRADE` `[RESTRICTED]` | Opens the PDB in migrate mode.  When `RESTRICTED` is specified, the PDB is accessible only to users with `RESTRICTED` `SESSION` privilege in the PDB. |
| `CLOSE` `[IMMEDIATE\|ABORT]` | Places the PDB in mounted mode.  The `CLOSE` statement is the PDB equivalent of the SQL\*Plus `SHUTDOWN` command. If you do not specify `IMMEDIATE` or `ABORT`, then the PDB is shut down with the normal mode. See " [Shutting Down with the Normal Mode](starting-up-and-shutting-down.md) ".  When `IMMEDIATE` is specified, this statement is the PDB equivalent of the SQL\*Plus `SHUTDOWN` command with the immediate mode. See " [Shutting Down with the Immediate Mode](starting-up-and-shutting-down.md) ".  When `ABORT` is specified, the PDB is forcefully closed. For a single-instance CDB, PDB media recovery is required when you specify `SHUTDOWN ABORT`. For an Oracle Real Application Clusters (Oracle RAC) CDB, PDB media recovery is required if the `SHUTDOWN ABORT` command closes the last open instance. |

When you issue an `ALTER` `PLUGGABLE` `DATABASE` `OPEN` statement, `READ` `WRITE` is the default unless a PDB being opened belongs to a CDB that is used as a physical standby database, in which case `READ` `ONLY` is the default.

You can specify which PDBs to modify in the following ways:

- List one or more PDBs.
- Specify `ALL` to modify all of the PDBs.
- Specify `ALL` `EXCEPT` to modify all of the PDBs, except for the PDBs listed.

The services Clause

You can use the services clause to specify the services that are started when a single PDB is opened in the following ways:

- List one or more services in the services clause in the following form:
	```
	SERVICES = ('service_name' [,'service_name'] … )
	```
- Specify `ALL` in the services clause to start all of the PDB’s services, as in the following example:
	```
	SERVICES = ALL
	```
- Specify `ALL` `EXCEPT` in the services clause to start all of the PDB’s services, except for the services listed, in the following form:
	```
	SERVICES = ALL EXCEPT('service_name' [,'service_name'] … )
	```
- Specify `NONE` in the services clause to start only the PDB’s default service and none of the other PDB’s services, as in the following example:
	```
	SERVICES = NONE
	```
	`NONE` is the default setting for the services clause. A PDB’s default service is always started, regardless of the setting for the services clause.

The instances Clause

For an Oracle Real Application Clusters (Oracle RAC) CDB, you can use the instances clause to specify the instances on which the PDB is modified in the following ways:

- List one or more instances in the instances clause in the following form:
	```
	INSTANCES = ('instance_name' [,'instance_name'] … )
	```
- Specify `ALL` in the instances clause to modify the PDB in all running instances, as in the following example:
	```
	INSTANCES = ALL
	```
- Specify `ALL` `EXCEPT` in the instances clause to modify the PDB in all of the instances, except for the instances listed, in the following form:
	```
	INSTANCES = ALL EXCEPT('instance_name' [,'instance_name'] … )
	```

Also, when you are closing a PDB in an Oracle RAC CDB, you can use the relocate clause, which includes the following options:

- Specify `NORELOCATE`, the default, to close the PDB in the current instance.
- Specify `RELOCATE` `TO` and specify an instance name to reopen the PDB in the specified instance.
- Specify `RELOCATE` to reopen the PDB on a different instance that is selected by Oracle Database.

Note:

If both the services clause and the instances clause are specified in the same `ALTER PLUGGABLE DATABASE` statement, then the specified services are started on the specified instances.

The relocate Clause

When you are closing a PDB in an Oracle RAC CDB, you can use the relocate clause, which includes the following options:

- Specify `NORELOCATE`, the default, to close the PDB in the current instance.
- Specify `RELOCATE` `TO` and specify an instance name to reopen the PDB in the specified instance.
- Specify `RELOCATE` to reopen the PDB on a different instance that is selected by Oracle Database.

To modify the open mode of PDBs with the `ALTER` `PLUGGABLE` `DATABASE` statement, the following prerequisites must be met:

- The current user must have `SYSDBA`, `SYSOPER`, `SYSBACKUP`, or `SYSDG` administrative privilege, and the privilege must be either commonly granted or locally granted in the PDB. The user must exercise the privilege using `AS` `SYSDBA`, `AS` `SYSOPER`, `AS` `SYSBACKUP`, or `AS` `SYSDG`, respectively, at connect time.
- When `RESTRICTED` `SESSION` is enabled, `RESTRICTED` must be specified when a PDB is opened.
- In an Oracle RAC CDB, if a PDB is open in one or more Oracle RAC instances, then it can be opened in additional instances, but it must be opened in the same mode as in the instances in which it is already open. A PDB can be closed in some instances and opened on others.

Summary of Requirements for the ALTER PLUGGABLE DATABASE Statement

To modify the open mode of PDBs with the `ALTER` `PLUGGABLE` `DATABASE` statement, the following prerequisites must be met:

- The current user must have `SYSDBA`, `SYSOPER`, `SYSBACKUP`, or `SYSDG` administrative privilege, and the privilege must be either commonly granted or locally granted in the PDB. The user must exercise the privilege using `AS` `SYSDBA`, `AS` `SYSOPER`, `AS` `SYSBACKUP`, or `AS` `SYSDG`, respectively, at connect time.
- When `RESTRICTED` `SESSION` is enabled, `RESTRICTED` must be specified when a PDB is opened.
- In an Oracle RAC CDB, if a PDB is open in one or more Oracle RAC instances, then it can be opened in additional instances, but it must be opened in the same mode as in the instances in which it is already open. A PDB can be closed in some instances and opened on others.

To place PDBs in a particular target mode with the `ALTER` `PLUGGAGLE` `DATABASE` statement, you must meet the requirements described in the following table.

Table 41-6 Modifying the Open Mode of PDBs with ALTER PLUGGABLE DATABASE

| Target Mode of PDBs | ALL Keyword Included | FORCE Keyword Included | Required Mode for the Root | Required Mode for Each PDB Being Modified |
| --- | --- | --- | --- | --- |
| Read/write | Yes | Yes | Read/write | Mounted, read-only, or read/write |
| Read/write | Yes | No | Read/write | Mounted or read/write |
| Read/write | No | Yes | Read/write | Mounted, read-only, or read/write |
| Read/write | No | No | Read/write | Mounted |
| Read-only | Yes | Yes | Read-only or read/write | Mounted, read-only, or read/write |
| Read-only | Yes | No | Read-only or read/write | Mounted or read-only |
| Read-only | No | Yes | Read-only or read/write | Mounted, read-only, or read/write |
| Read-only | No | No | Read-only or read/write | Mounted |
| Migrate | Yes | Not applicable | Read-only or read/write | Mounted |
| Migrate | No | Not applicable | Read-only or read/write | Mounted |
| Mounted | Yes | Not applicable | Read-only or read/write | Mounted, read-only, migrate, or read/write |
| Mounted | No | Not applicable | Read-only or read/write | Read-only, migrate, or read/write |

Note:

You can also modify the open mode of a PDB when the current container is the PDB. See " [Modifying a PDB with the ALTER PLUGGABLE DATABASE Statement](administering-pdbs-with-sql-plus.md) ".

##### 41.4.6.3 About Modifying the Open Mode of PDBs with the SQL\*Plus STARTUP Command

When the current container is the root, the `STARTUP` `PLUGGABLE` `DATABASE` command can open a single PDB.

Use the following options of the `STARTUP` `PLUGGABLE` `DATABASE` command to open a PDB:

- `FORCE`
	Closes an open PDB before re-opening it in read/write mode. When this option is specified, no other options are allowed.
- `RESTRICT`
	Enables only users with the `RESTRICTED` `SESSION` system privilege in the PDB to access the PDB.
	If neither `OPEN` `READ` `WRITE` nor `OPEN` `READ` `ONLY` is specified, then the PDB is opened in read-only mode when the CDB to which it belongs is a physical standby database. Otherwise, the PDB is opened in read/write mode.
- `OPEN` open\_pdb\_options
	Opens the PDB in either read/write mode or read-only mode. You can specify `OPEN` `READ` `WRITE` or `OPEN` `READ` `ONLY`. When you specify `OPEN` without any other options, `READ` `WRITE` is the default.

The following prerequisites must be met:

- The current user must have `SYSDBA`, `SYSOPER`, `SYSBACKUP`, or `SYSDG` administrative privilege, and the privilege must be either commonly granted or locally granted in the PDB. The user must exercise the privilege using `AS` `SYSDBA`, `AS` `SYSOPER`, `AS` `SYSBACKUP`, or `AS` `SYSDG`, respectively, at connect time.
- When `RESTRICTED` `SESSION` is enabled, `RESTRICT` must be specified when a PDB is opened.

In addition, to place PDBs in a particular target mode with the `STARTUP` `PLUGGAGLE` `DATABASE` command, you must meet the requirements described in the following table.

Table 41-7 Modifying the Open Mode of a PDB with STARTUP PLUGGABLE DATABASE

| Target Mode of the PDB | FORCE Option Included | Required Mode for the Root | Required Mode of the PDB Being Modified |
| --- | --- | --- | --- |
| Read/write | Yes | Read/write | Mounted, read-only, or read/write |
| Read/write | No | Read/write | Mounted |
| Read-only | No | Read-only or read/write | Mounted |

Note:

You can also use the `STARTUP` command to modify the open mode of a PDB when the current container is the PDB. See " [Using the STARTUP SQL\*Plus Command on a PDB](administering-pdbs-with-sql-plus.md) ".

##### 41.4.6.4 Modifying the Open Mode of PDBs with ALTER PLUGGABLE DATABASE

You can modify the open mode of PDBs with the `ALTER` `PLUGGABLE` `DATABASE` statement with a pdb\_change\_state clause.

1. In SQL\*Plus, ensure that the current container is the root.
	See " Accessing a Container in a CDB with SQL\*Plus ".
2. Run an `ALTER` `PLUGGABLE` `DATABASE` statement with a pdb\_change\_state clause.

Example 41-17 Changing the Open Mode of Listed PDBs

This statement changes the open mode of PDBs `salespdb` and `hrpdb` to open in read/write mode.

```
ALTER PLUGGABLE DATABASE salespdb, hrpdb
   OPEN READ WRITE;
```

This statement changes the open mode of PDB `salespdb` to open in read-only mode. `RESTRICTED` specifies that the PDB is accessible only to users with `RESTRICTED` `SESSION` privilege in the PDB.

```
ALTER PLUGGABLE DATABASE salespdb
   OPEN READ ONLY RESTRICTED;
```

This statement changes the open mode of PDB `salespdb` to open in migrate mode:

```
ALTER PLUGGABLE DATABASE salespdb
   OPEN UPGRADE;
```

Example 41-18 Changing the Open Mode of All PDBs

Run the following query to display the open mode of each PDB associated with a CDB:

```
SELECT NAME, OPEN_MODE FROM V$PDBS WHERE CON_ID > 2;
 
NAME                           OPEN_MODE
------------------------------ ----------
HRPDB                          READ WRITE
SALESPDB                       MOUNTED
DWPDB                          MOUNTED
```

Notice that `hrpdb` is already in read/write mode. To change the open mode of `salespdb` and `dwpdb` to open in read/write mode, use the following statement:

```
ALTER PLUGGABLE DATABASE ALL
   OPEN READ WRITE;
```

The `hrpdb` PDB is not modified because it is already in open read/write mode. The statement does not return an error because two PDBs are in mounted mode and one PDB (`hrpdb`) is in the specified mode (read/write). Similarly, the statement does not return an error if all PDBs are in mounted mode.

However, if any PDB is in read-only mode, then the statement returns an error. To avoid an error and open all PDBs in the CDB in read/write mode, specify the `FORCE` keyword:

```
ALTER PLUGGABLE DATABASE ALL
   OPEN READ WRITE FORCE;
```

With the `FORCE` keyword included, all PDBs are opened in read/write mode, including PDBs in read-only mode.

Example 41-19 Changing the Open Mode of All PDBs Except for Listed Ones

This statement changes the mode of all PDBs except for `salespdb` and `hrpdb` to mounted mode.

```
ALTER PLUGGABLE DATABASE ALL EXCEPT salespdb, hrpdb
   CLOSE IMMEDIATE;
```

Note:

An `ALTER` `PLUGGABLE` `DATABASE` statement modifying the open mode of a PDB is instance-specific. Therefore, if this statement is issued when connected to an Oracle RAC instance, then it affects the open mode of the PDB only in that instance.

See Also:

- " About Modifying the Open Mode of PDBs with ALTER PLUGGABLE DATABASE "
- " [Modifying a PDB](administering-pdbs-with-sql-plus.md) " for information about modifying the other attributes of a PDB
- " [Altering Database Availability](starting-up-and-shutting-down.md) " for information about database modes and their uses
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQLRF55667)
- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=CNCPT89041) for more information about shutdown modes

**Parent topic:** Modifying the Open Mode of PDBs

##### 41.4.6.5 Modifying the Open Mode of PDBs with the SQL\*Plus STARTUP Command

You can use the `STARTUP` `PLUGGABLE` `DATABASE` command to open a single PDB.

To modify a PDB with the `STARTUP` `PLUGGABLE` `DATABASE` command:

1. In SQL\*Plus, ensure that the current container is the root.
	See " Accessing a Container in a CDB with SQL\*Plus ".
2. Run the `STARTUP` `PLUGGABLE` `DATABASE` command.

Note:

When the current container is the root, the SQL\*Plus `SHUTDOWN` command always shuts down the CDB instance. It cannot be used to close individual PDBs.

Example 41-20 Opening a PDB in Read/Write Mode with the STARTUP Command

```
STARTUP PLUGGABLE DATABASE hrpdb OPEN
```

Example 41-21 Opening a PDB in Read/Write Restricted Mode with the STARTUP Command

```
STARTUP PLUGGABLE DATABASE hrpdb RESTRICT
```

Example 41-22 Opening a PDB in Read-Only Restricted Mode with the STARTUP Command

```
STARTUP PLUGGABLE DATABASE hrpdb OPEN READ ONLY RESTRICT
```

Example 41-23 Opening a PDB in Read-Only Mode with the STARTUP Command

```
STARTUP PLUGGABLE DATABASE hrpdb OPEN READ ONLY
```

Example 41-24 Opening a PDB in Read/Write Mode with the STARTUP Command and the FORCE Option

This example assumes that the `hrpdb` PDB is currently open. The `FORCE` option closes the PDB and then opens it in the read/write mode.

```
STARTUP PLUGGABLE DATABASE hrpdb FORCE
```

See Also:

- " About Modifying the Open Mode of PDBs with the SQL\*Plus STARTUP Command "
- " [Modifying a PDB with the SQL\*Plus STARTUP and SHUTDOWN Commands](administering-pdbs-with-sql-plus.md) " for information about using the `STARTUP` or `SHUTDOWN` command when the current container is a PDB
- " [Starting Up a Database](starting-up-and-shutting-down.md) "
- [SQL\*Plus User's Guide and Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQPUG128)

**Parent topic:** Modifying the Open Mode of PDBs

#### 41.4.7 Preserving or Discarding the Open Mode of PDBs When the CDB Restarts

You can preserve the open mode of one or more PDBs when the CDB restarts by using the `ALTER` `PLUGGABLE` `DATABASE` SQL statement with a pdb\_save\_or\_discard\_state clause.

Note:

This feature is available starting with Oracle Database 12c Release 1 (12.1.0.2).

You can do this in the following way:

- Specify `SAVE STATE` to preserve the PDBs' mode when the CDB is restarted.
	For example, if a PDB is in open read/write mode before the CDB is restarted, then the PDB is in open read/write mode after the CDB is restarted; if a PDB is in mounted mode before the CDB is restarted, then the PDB is in mounted mode after the CDB is restarted.
- Specify `DISCARD STATE` to ignore the PDBs' open mode when the CDB is restarted.
	When `DISCARD STATE` is specified for a PDB, the PDB is always mounted after the CDB is restarted.

You can specify which PDBs to modify in the following ways:

- List one or more PDBs.
- Specify `ALL` to modify all of the PDBs.
- Specify `ALL` `EXCEPT` to modify all of the PDBs, except for the PDBs listed.

For an Oracle RAC CDB, you can use the instances clause in the pdb\_save\_or\_discard\_state clause to specify the instances on which a PDB's open mode is preserved in the following ways:

- List one or more instances in the instances clause in the following form:
	```
	INSTANCES = ('instance_name' [,'instance_name'] … )
	```
- Specify `ALL` in the instances clause to modify the PDB in all running instances, as in the following example:
	```
	INSTANCES = ALL
	```
- Specify `ALL` `EXCEPT` in the instances clause to modify the PDB in all of the instances, except for the instances listed, in the following form:
	```
	INSTANCES = ALL EXCEPT('instance_name' [,'instance_name'] … )
	```

For a PDB in an Oracle RAC CDB, `SAVE STATE` and `DISCARD STATE` only affect the mode of the current instance. They do not affect the mode of other instances, even if more than one instance is specified in the instances clause.

To issue an `ALTER` `PLUGGABLE` `DATABASE` SQL statement with a pdb\_save\_or\_discard\_state clause, the current user must have the `ALTER` `DATABASE` privilege in the root.

You can check the saved states for the PDBs in a CDB by querying the `DBA_PDB_SAVED_STATES` view.

To preserve or discard a PDB's open mode when the CDB restarts:

1. In SQL\*Plus, ensure that the current container is the root.
	See " Accessing a Container in a CDB with SQL\*Plus ".
2. Run an `ALTER` `PLUGGABLE` `DATABASE` statement with a pdb\_save\_or\_discard\_state clause.

The following examples either preserve or discard the open mode of one or more PDBs when the CDB restarts.

Example 41-25 Preserving the Open Mode of a PDB When the CDB Restarts

This statement preserves the open mode of the `salespdb` when the CDB restarts.

```
ALTER PLUGGABLE DATABASE salespdb SAVE STATE;
```

Example 41-26 Discarding the Open Mode of a PDB When the CDB Restarts

This statement discards the open mode of the `salespdb` when the CDB restarts.

```
ALTER PLUGGABLE DATABASE salespdb DISCARD STATE;
```

Example 41-27 Preserving the Open Mode of All PDBs When the CDB Restarts

This statement preserves the open mode of all of the PDBs when the CDB restarts.

```
ALTER PLUGGABLE DATABASE ALL SAVE STATE;
```

Example 41-28 Preserving the Open Mode of Listed PDBs When the CDB Restarts

This statement preserves the open mode of the `salespdb` and `hrpdb` when the CDB restarts.

```
ALTER PLUGGABLE DATABASE salespdb, hrpdb SAVE STATE;
```

Example 41-29 Preserving the Open Mode of All PDBs Except for Listed Ones When the CDB Restarts

This statement preserves the open mode of all PDBs except for `salespdb` and `hrpdb`.

```
ALTER PLUGGABLE DATABASE ALL EXCEPT salespdb, hrpdb SAVE STATE;
```

**Parent topic:** Modifying a CDB

### 41.5 Using the ALTER SYSTEM SET Statement in a CDB

The `ALTER` `SYSTEM` `SET` statement can dynamically set an initialization parameter in one or more containers in a CDB.

A CDB uses an inheritance model for initialization parameters in which PDBs inherit initialization parameter values from the root. In this case, inheritance means that the value of a particular parameter in the root applies to a particular PDB.

A PDB can override the root's setting for some parameters, which means that a PDB has an inheritance property for each initialization parameter that is either true or false. The inheritance property is true for a parameter when the PDB inherits the root's value for the parameter. The inheritance property is false for a parameter when the PDB does not inherit the root's value for the parameter.

The inheritance property for some parameters must be true. For other parameters, you can change the inheritance property by running the `ALTER` `SYSTEM` `SET` statement to set the parameter when the current container is the PDB. If `ISPDB_MODIFIABLE` is `TRUE` for an initialization parameter in the `V$SYSTEM_PARAMETER` view, then the inheritance property can be false for the parameter.

When the current container is the root, the `CONTAINER` clause of the `ALTER` `SYSTEM` `SET` statement controls which PDBs inherit the parameter value being set. The `CONTAINER` clause has the following syntax:

```
CONTAINER = { CURRENT | ALL }
```

The following settings are possible:

- `CURRENT`, the default, means that the parameter setting applies only to the current container.
	When the current container is the root, the parameter setting applies to the root and to any PDB with an inheritance property of true for the parameter.
- `ALL` means that the parameter setting applies to all containers in the CDB, including the root and all of the PDBs.
	Specifying `ALL` sets the inheritance property to true for the parameter in all PDBs.

See " About the Current Container " for more information about the `CONTAINER` clause and rules that apply to it.

To use `ALTER` `SYSTEM` `SET` in the root in a CDB:

1. In SQL\*Plus, ensure that the current container is the root.
	The current user must have the commonly granted `ALTER` `SYSTEM` privilege.
	See " Accessing a Container in a CDB with SQL\*Plus ".
2. Run the `ALTER` `SYSTEM` `SET` statement.

Note:

If you want to change the inheritance property for a particular parameter in a particular PDB from false to true, then you can run the `ALTER` `SYSTEM` `RESET` statement to reset the parameter when the current container is the PDB. The following example resets the `OPEN_CURSORS` parameter:

```
ALTER SYSTEM RESET OPEN_CURSORS SCOPE = SPFILE;
```

Example 41-30 Setting an Initialization Parameter for All Containers

This `ALTER` `SYSTEM` `SET` statement sets the `OPEN_CURSORS` initialization parameter to `200` for the all containers and sets the inheritance property to `TRUE` in each PDB.

```
ALTER SYSTEM SET OPEN_CURSORS = 200 CONTAINER = ALL;
```

Example 41-31 Setting an Initialization Parameter for the Root

This `ALTER` `SYSTEM` `SET` statement sets the `OPEN_CURSORS` initialization parameter to `200` for the root and for PDBs with an inheritance property of true for the parameter.

```
ALTER SYSTEM SET OPEN_CURSORS = 200 CONTAINER = CURRENT;
```

See Also:

- " [Using the ALTER SYSTEM Statement to Modify a PDB](administering-pdbs-with-sql-plus.md) "
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQLRF53143) for more information about the `ALTER` `SYSTEM` `SET` statement

**Parent topic:** Administering a CDB with SQL\*Plus

### 41.6 Issuing DML Statements on Containers in a CDB

A DML (data manipulation language) statement issued in a CDB root can modify one or more containers in the CDB. In addition, you can specify one or more default container targets for DML statements.

- About Issuing DML Statements on Containers in a CDB  
	DML statements can affect database objects in more than one container in a CDB.
- Specifying the Default Container for DML Statements in a CDB  
	To specify the default container for DML statements in a CDB, issue the `ALTER DATABASE` statement with the `CONTAINERS DEFAULT TARGET` clause.

**Parent topic:** Administering a CDB with SQL\*Plus

#### 41.6.1 About Issuing DML Statements on Containers in a CDB

DML statements can affect database objects in more than one container in a CDB.

In a CDB root or an application root, a single DML statement that includes the `CONTAINERS` clause can modify a table or view in one or more containers in that CDB or application container. To use the `CONTAINERS` clause, specify the table or view being modified in the `CONTAINERS` clause and the containers affected in the `WHERE` clause. A target container can be specified in an `INSERT VALUES` statement by specifying a value for `CON_ID` in the `VALUES` clause. Also, a target container can be specified in an `UPDATE` or `DELETE` statement by specifying a `CON_ID` predicate in the `WHERE` clause.

For example, the following DML statement updates the `sales.customers` table in the containers with a `CON_ID` of `7` or `8`:
```
UPDATE CONTAINERS(sales.customers) ctab 
   SET ctab.city_name='MIAMI' 
   WHERE ctab.CON_ID IN(7,8) AND
   CUSTOMER_ID=3425;
```

The values specified for the `CON_ID` in the `WHERE` clause must be for containers that are part of the CDB, including PDBs, application roots, and application PDBs.

You can also specify default target containers for DML operations. If a DML statement does not specify values for the `CON_ID` in the `WHERE` clause, then the target containers of the DML operation are those specified in the database property `CONTAINERS_DEFAULT_TARGET` in the CDB root. When issued in a CDB root, the following DML statement modifies the default target containers for the CDB:

```
UPDATE CONTAINERS(sales.customers) ctab 
   SET ctab.city_name='MIAMI' 
   WHERE CUSTOMER_ID=3425;
```

A target container can be specified in an `INSERT VALUES` statement by specifying a value for `CON_ID` in the `VALUES` clause. Also, a target container can be specified in an `UPDATE` or `DELETE` statement by specifying a `CON_ID` predicate in the `WHERE` clause.

By default, the default target containers in a CDB include all of its PDBs, application roots, application seeds, and application PDBs, but not its CDB root or CDB seed. You can determine the default target containers for a CDB by running the following query:
```
SELECT PROPERTY_VALUE FROM DATABASE_PROPERTIES WHERE PROPERTY_NAME='CONTAINERS_DEFAULT_TARGET';
```

The following restrictions apply to the `CONTAINERS` clause:

- `INSERT` as `SELECT` statements where the target of the `INSERT` is in `CONTAINERS()` is not supported.
- A multi-table `INSERT` statement where the target of the `INSERT` is in `CONTAINERS()` is not supported.
- DML statements using the `CONTAINERS` clause require that the database listener is configured using TCP (instead of IPC) and that the `PORT` and `HOST` values are specified for each target PDB using the `PORT` and `HOST` clauses, respectively.

**Parent topic:** Issuing DML Statements on Containers in a CDB

#### 41.6.2 Specifying the Default Container for DML Statements in a CDB

To specify the default container for DML statements in a CDB, issue the `ALTER DATABASE` statement with the `CONTAINERS DEFAULT TARGET` clause.

When a DML statement is issued in a CDB root without specifying containers in the `WHERE` clause, the DML statement affects the default container for the CDB. The default container can be any container in the CDB, including the CDB root, a PDB, an application root, or an application PDB. Only one default container is allowed.

1. In SQL\*Plus, ensure that the current container is the CDB root.
	The current user must have the commonly granted `ALTER DATABASE` privilege.
2. Run the `ALTER DATABASE` statement with the `CONTAINERS DEFAULT TARGET` clause.

Example 41-32 Specifying the Default Container for DML Statements in a CDB

This example specifies that `PDB1` is the default container for DML statements in the CDB.

```
ALTER DATABASE CONTAINERS DEFAULT TARGET = (PDB1);
```

Example 41-33 Clearing the Default Container

This example clears the default container setting. When it is not set, the default container is the CDB root.

```
ALTER DATABASE CONTAINERS DEFAULT TARGET = NONE;
```

**Parent topic:** Issuing DML Statements on Containers in a CDB

### 41.7 Executing DDL Statements in a CDB

In a CDB, you can execute a data definition language (DDL) statement in the current container or in all containers.

- About Executing DDL Statements in a CDB  
	In a CDB, some DDL statements can apply to all containers or to the current container only.
- Executing a DDL Statement in the Current Container  
	Specify `CURRENT` in the `CONTAINER` clause of a DDL statement to execute the statement in the current container.
- Executing a DDL Statement in All Containers in a CDB  
	Specify `ALL` in the `CONTAINER` clause of a DDL statement to execute the statement in all of the containers in a CDB.

**Parent topic:** Administering a CDB with SQL\*Plus

#### 41.7.1 About Executing DDL Statements in a CDB

In a CDB, some DDL statements can apply to all containers or to the current container only.

To specify which containers are affected, use the `CONTAINER` clause:

```
CONTAINER = { CURRENT | ALL }
```

The following settings are possible:

- `CURRENT` means that the statement applies only to the current container.
- `ALL` means that the statement applies to all containers in the CDB, including the root and all of the PDBs.

The following restrictions apply to the `CONTAINER` clause in DDL statements:

- The restrictions described in " About the Current Container ".
- You can use the `CONTAINER` clause only with the DDL statements listed in Table 41-8.

Table 41-8 DDL Statements and the CONTAINER Clause in a CDB

| DDL Statement | CONTAINER = CURRENT | CONTAINER = ALL |
| --- | --- | --- |
| `CREATE` `USER` | Creates a local user in the current PDB. | Creates a common user. |
| `ALTER` `USER` | Alters a local user in the current PDB. | Alters a common user. |
| `CREATE` `ROLE` | Creates a local role in the current PDB. | Creates a common role. |
| `GRANT` | Grants a privilege in the local container to a local user, common user, or local role.  The `SET` `CONTAINER` privilege can be granted to a user-created common user in the current PDB. | Grants a system privilege or object privilege on a common object to a common user or common role. The specified privilege is granted to the user or role across the entire CDB. |
| `REVOKE` | Revokes a privilege in the local container from a local user, common user, or local role.  This statement can revoke only a privilege granted with `CURRENT` specified in the `CONTAINER` clause from the specified user or role in the local container. The statement does not affect privileges granted with `ALL` specified in the `CONTAINER` clause.  The `SET` `CONTAINER` privilege can be revoked from a user-created common user in the current PDB. | Revokes a system privilege or object privilege on a common object from a common user or common role. The specified privilege is revoked from the user or role across the entire CDB.  This statement can revoke only a privilege granted with `ALL` specified in the `CONTAINER` clause from the specified common user or common role. The statement does not affect privileges granted with `CURRENT` specified in the `CONTAINER` clause. However, any privileges granted locally that depend on the privilege granted commonly that is being revoked are also revoked. |

All other DDL statements apply to the current container only.

In addition to the usual rules for user, role, and profile names, the following rules and best practices apply when you create a user, role, or profile in a CDB:

- It is best practice for common user, role, and profile names to start with a prefix to avoid naming conflicts between common users, roles, and profiles and local users, roles, and profiles. You specify this prefix with the `COMMON_USER_PREFIX` initialization parameter in the CDB root. By default, the prefix is `C##` or `c##` in the CDB root.
- In an application container, it is best practice for application common user, role, and profile names to start with a prefix to avoid naming conflicts between application common users, roles, and profiles and local users, roles, and profiles. You specify this prefix with the `COMMON_USER_PREFIX` initialization parameter in the application root. By default, the prefix is `NULL` in an application root.
- When the `COMMON_USER_PREFIX` initialization parameter is set in an application root, the setting applies to the application common user, role, and profile names in the application container. The prefix can be different in the CDB root and in an application root, and the prefix can be different in different application containers.
- Common user, role, and profile names must consist only of ASCII characters. This restriction does not apply to application common user, role, and profile names.
- Local user, role, and profile names cannot start with the prefix specified for common users with the `COMMON_USER_PREFIX` initialization parameter.
- Local user, role, and profile names cannot start with `C##` or `c##`.
- Regardless of the value of `COMMON_USER_PREFIX` in the CDB root, application common user, role, and profile names cannot start with `C##` or `c##`.
- Application common user, role, and profile names cannot start with the prefix specified for common users with the `COMMON_USER_PREFIX` initialization parameter.

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQLRF30041)
- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=CNCPT1732)
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=DBSEG589) for more information about managing users in a CDB
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=REFRN10354) for more information about the `COMMON_USER_PREFIX` initialization parameter
- " Using the ALTER SYSTEM SET Statement in a CDB " for information about using the `ALTER` `SYSTEM` system control statement in a CDB

**Parent topic:** Executing DDL Statements in a CDB

#### 41.7.2 Executing a DDL Statement in the Current Container

Specify `CURRENT` in the `CONTAINER` clause of a DDL statement to execute the statement in the current container.

The supported DDL statements are listed in Table 41-8.

The current user must be granted the required privileges to execute the DDL statement in the current container. For example, to create a user, the current user must be granted the `CREATE` `USER` system privilege in the current container.

To execute a DDL statement in the current container:

1. In SQL\*Plus, access a container.
	See " Accessing a Container in a CDB with SQL\*Plus ".
2. Execute the DDL statement with `CONTAINER` set to `CURRENT`.

A local user's user name cannot start with the prefix specified by the `COMMON_USER_PREFIX` initialization parameter. By default, in the CDB root, the prefix is `C##` or `c##`. An application root can specify its own prefix for an application container. In addition, a common user's name must consist only of ASCII characters. The specified tablespace must exist in the PDB.

Example 41-34 Creating Local User in a PDB

This example creates the local user `testpdb` in the current PDB.

```
CREATE USER testpdb IDENTIFIED BY password 
   DEFAULT TABLESPACE pdb1_tbs
   QUOTA UNLIMITED ON pdb1_tbs
   CONTAINER = CURRENT;
```

**Parent topic:** Executing DDL Statements in a CDB

#### 41.7.3 Executing a DDL Statement in All Containers in a CDB

Specify `ALL` in the `CONTAINER` clause of a DDL statement to execute the statement in all of the containers in a CDB.

The supported DDL statements are listed in Table 41-8.

The following prerequisites must be met:

- The current user must be a common user.
- The current user must be granted the required privileges commonly to execute the DDL statement. For example, to create a user, the current user must be granted the `CREATE` `USER` system privilege commonly.

To execute a DDL statement in all containers in a CDB:

1. In SQL\*Plus, ensure that the current container is the root.
	See " Accessing a Container in a CDB with SQL\*Plus ".
2. Execute the DDL statement with `CONTAINER` set to `ALL`.

A common user's user name must start with the prefix specified by the `COMMON_USER_PREFIX` initialization parameter. By default, in the CDB root, the prefix is `C##` or `c##`. An application root can specify its own prefix for an application container. In addition, a common user's name must consist only of ASCII characters. The specified tablespace must exist in the root and in all PDBs.

Example 41-35 Creating Common User in a CDB

This example creates the common user `c##testcdb`.

```
CREATE USER c##testcdb IDENTIFIED BY password 
   DEFAULT TABLESPACE cdb_tbs
   QUOTA UNLIMITED ON cdb_tbs
   CONTAINER = ALL;
```

**Parent topic:** Executing DDL Statements in a CDB

### 41.8 Managing the CDB Undo Mode

When local undo is enabled, each container has its own undo tablespace for every instance in which it is open. When local undo is disabled, there is one undo tablespace for the entire CDB.

- About the CDB Undo Mode  
	You can configure a CDB to use local undo in every container or to use shared undo for the entire CDB.
- Configuring a CDB to Use Local Undo Mode  
	When a CDB is in shared undo mode, you can change it to use local undo mode by issuing an `ALTER DATABASE LOCAL UNDO ON` statement and restarting the database.
- Configuring a CDB to Use Shared Undo Mode  
	When a CDB is in local undo mode, you can change it to use shared undo mode by issuing an `ALTER DATABASE LOCAL UNDO OFF` statement and restarting the database.

**Parent topic:** Administering a CDB with SQL\*Plus

#### 41.8.1 About the CDB Undo Mode

You can configure a CDB to use local undo in every container or to use shared undo for the entire CDB.

A CDB can run in local undo mode or shared undo mode. You can specify the undo mode of a CDB during CDB creation in the `ENABLE PLUGGABLE DATABASE` clause of the `CREATE DATABASE` statement. You can change the undo mode of a CDB after it is created by issuing an `ALTER DATABASE` statement and restarting the CDB. The undo mode applies to the entire CDB. Therefore, every container either uses shared undo or local undo.

To determine the current CDB undo mode, run the following query in the CDB root:
```
SELECT PROPERTY_NAME, PROPERTY_VALUE 
   FROM   DATABASE_PROPERTIES 
   WHERE  PROPERTY_NAME = 'LOCAL_UNDO_ENABLED';
```

If the query returns `TRUE` for the `PROPERTY_VALUE`, then the CDB is in local undo mode. Otherwise, the CDB is in shared undo mode.

Local Undo Mode

Local undo mode means that each container has its own undo tablespace for every instance in which it is open. In this mode, Oracle Database automatically creates an undo tablespace for every container in the CDB. For an Oracle RAC CDB, there is one active undo tablespace for each instance for each PDB in local undo mode.

Local undo mode provides increased isolation for each container and improves the efficiency of some operations, such as unplugging the container or performing point-in-time recovery on the container. In addition, local undo mode is required for some operations to be supported, such as relocating a PDB or cloning a PDB that is in open read/write mode.

When a CDB is in local undo mode, the following applies:

- Any user who has the appropriate privileges for the current container can create an undo tablespace for the container.
	See [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQLRF01403) for information about the required privileges.
- Undo tablespaces are visible in static data dictionary views and dynamic performance (V$) views in every container in the CDB.

Shared Undo Mode

Shared undo mode means that there is one active undo tablespace for a single-instance CDB. For an Oracle RAC CDB, there is one active undo tablespace for each instance.

When a CDB is in shared undo mode, the following applies:

- Only a common user who has the appropriate privileges and whose current container is the CDB root can create an undo tablespace.
- When the current container is not the CDB root, an attempt to create an undo tablespace fails and returns an error.
- Undo tablespaces are visible in static data dictionary views and dynamic performance (V$) views when the current container is the CDB root. Undo tablespaces are visible only in dynamic performance views when the current container is a PDB, an application root, or an application PDB.

Note:

- When you change the undo mode of a CDB, the new undo mode applies to an individual container the first time the container is opened after the change.
- When you change the undo mode of a CDB, containers in the CDB cannot flash back to a time or SCN that is prior to the change.

#### 41.8.2 Configuring a CDB to Use Local Undo Mode

When a CDB is in shared undo mode, you can change it to use local undo mode by issuing an `ALTER DATABASE LOCAL UNDO ON` statement and restarting the database.

When a CDB is in local undo mode, each container has its own undo tablespace for every instance in which it is open. Oracle Database automatically creates an undo tablespace in any container in the CDB that does not have one. If a PDB without an undo tablespace is cloned, relocated, or plugged into a CDB that is configured to use local undo mode, then Oracle Database automatically creates an undo tablespace for the PDB the first time it is opened.

When a CDB is changed from shared undo mode to local undo mode, Oracle Database creates the required undo tablespaces automatically.

1. Shut down the CDB instance if it is open.
2. Start up the CDB instance in `OPEN UPGRADE` mode. For example:
	`STARTUP UPGRADE`
3. In SQL\*Plus, ensure that the current container is the CDB root. For example, enter the following:
	```
	SHOW CON_NAME
	CON_NAME
	------------------------------
	CDB$ROOT
	```
4. Issue the following SQL statement:
	`ALTER DATABASE LOCAL UNDO ON;`
5. Shut down and restart the CDB instance.
6. **Optional:** Manually create an undo tablespace in the CDB seed.
	While Oracle Database creates an undo tablespace in the CDB seed automatically in local undo mode, you might want to control the size and configuration of the undo tablespace by creating an undo tablespace manually. To ensure the PDBs created from the CDB seed use the manually-created undo tablespace and not the automatically-created undo tablespace, you must set the `UNDO_TABLESPACE` initialization parameter to the manually-created undo tablespace, or drop the automatically-created undo tablespace.
	1. In SQL\*Plus, ensure that the current container is the root.
		2. Place the CDB seed in open read/write mode:
		`ALTER PLUGGABLE DATABASE PDB$SEED OPEN READ WRITE FORCE;`
		3. Switch container to the CDB seed:
		`ALTER SESSION SET CONTAINER=PDB$SEED;`
		4. Create an undo tablespace in the CDB seed. For example:
		```
		CREATE UNDO TABLESPACE seedundots1
		   DATAFILE 'seedundotbs_1a.dbf'
		   SIZE 10M AUTOEXTEND ON
		   RETENTION GUARANTEE;
		```
		5. Switch container to the root:
		`ALTER SESSION SET CONTAINER=CDB$ROOT;`
		6. Place the CDB seed in open read-only mode:
		`ALTER PLUGGABLE DATABASE PDB$SEED OPEN READ ONLY FORCE;`

**Parent topic:** Managing the CDB Undo Mode

#### 41.8.3 Configuring a CDB to Use Shared Undo Mode

When a CDB is in local undo mode, you can change it to use shared undo mode by issuing an `ALTER DATABASE LOCAL UNDO OFF` statement and restarting the database.

1. Shut down the CDB instance if it is open.
2. Start up the CDB instance in `OPEN UPGRADE` mode. For example:
	`STARTUP UPGRADE`
3. In SQL\*Plus, ensure that the current container is the CDB root. For example, enter the following:
	```
	SHOW CON_NAME
	CON_NAME
	------------------------------
	CDB$ROOT
	```
4. Issue the following SQL statement:
	`ALTER DATABASE LOCAL UNDO OFF;`
5. Shut down and restart the CDB instance.

When it is in shared undo mode, the CDB ignores any local undo tablespaces that were created when it was in local undo mode. Oracle recommends that you delete these local undo tablespaces.

**Parent topic:** Managing the CDB Undo Mode

### 41.9 Running Oracle-Supplied SQL Scripts in a CDB

You can use the catcon.pl script to run Oracle-supplied SQL scripts in a CDB.

- About Running Oracle-Supplied SQL Scripts in a CDB  
	In a CDB, the catcon.pl script is the best way to run SQL scripts and SQL statements.
- Syntax and Parameters for catcon.pl  
	The catcon.pl script is a Perl script that must be run at an operating system prompt.
- Running the catcon.pl Script  
	Examples illustrate running the catcon.pl script.

**Parent topic:** Administering a CDB with SQL\*Plus

#### 41.9.1 About Running Oracle-Supplied SQL Scripts in a CDB

In a CDB, the catcon.pl script is the best way to run SQL scripts and SQL statements.

An Oracle Database installation includes several SQL scripts. These scripts perform operations such as creating data dictionary views and installing options.

The catcon.pl script can run scripts in the root and in specified PDBs in the correct order, and it generates log files that you can view to confirm that the SQL script or SQL statement did not generate unexpected errors. It also starts multiple processes and assigns new scripts to them as they finish running scripts previously assigned to them.

Note:

- Unless you exclude the CDB seed when you run catcon.pl, the SQL script or SQL statement is run on the CDB seed.
- You can use the catcon.pl script to run scripts on both CDBs and non-CDBs.

**Parent topic:** Running Oracle-Supplied SQL Scripts in a CDB

#### 41.9.2 Syntax and Parameters for catcon.pl

The catcon.pl script is a Perl script that must be run at an operating system prompt.

The catcon.pl script has the following syntax and parameters:

```
$ORACLE_HOME/perl/bin/perl $ORACLE_HOME/rdbms/admin/catcon.pl  
[--usr username[/password]] [--int_usr username[/password]] [--script_dir directory] 
[--log_dir directory] [{--incl_con|--excl_con} container] [--echo] [--spool] 
[--error_logging { ON | errorlogging-table-other-than-SPERRORLOG } ] [--app_con application_root] 
[--no_set_errlog_ident] [--diag] [-ignore_unavailable_pdbs] [--verbose] [--force_pdb_mode pdb_mode] 
[--recover] --log_file_base log_file_name_base 
-- { SQL_script [arguments] | --x'SQL_statement' }
```

Ensure that `--x` SQL\_statement is preceded by `--` if it follows any single-letter parameter. If `--x` SQL\_statement is preceded by a script name or another `--x` SQL\_statement, then do not precede it with `--`. Also, note that the SQL statement must be inside single quotation marks.

Command line parameters to SQL scripts can be introduced using `--p`. Interactive (or secret) parameters to SQL scripts can be introduced using `--P`.

To view the help for the catcon.pl script, run the following command:

`$ORACLE_HOME/perl/bin/perl $ORACLE_HOME/rdbms/admin/catcon.pl --help`

Table 41-9 describes the catcon.pl parameters. A parameter is optional unless it is indicated that it is required.

The short parameter names in the following table are for backward compatibility. Some parameters do not have short names.

Table 41-9 catcon.pl Parameters

| Parameter | Description |
| --- | --- |
| `--usr`  Short name: `-u` | Specifies the username and password to connect to the root and the specified PDBs. Specify a common user with the required privileges to run the SQL script or the SQL statement. The default is " `/ AS SYSDBA` ". If no password is supplied, then catcon.pl prompts for a password. |
| `--int_usr`  Short name: `-U` | Specifies the username and password to connect to the root and the specified PDBs. Specify a common user with the required privileges to perform internal tasks, such as running queries on the CDB's metadata. The default is " `/ AS SYSDBA` ". If no password is supplied, then catcon.pl prompts for a password. |
| `--script_dir`  Short name: `-d` | Directory that contains the SQL script. The default is the current directory. |
| `--log_dir`  Short name: `-l` | Directory into which catcon.pl writes log files. The default is the current directory. |
| `{--incl_con\|--excl_con}`  Short names: `{-c\|-C}` | The containers in which the SQL script is run or is not run.  The `--incl_con` parameter lists the containers in which the SQL script is run.  The `--excl_con` parameter lists the containers in which the SQL script is not run.  Specify containers in a space-delimited list of PDB names enclosed in single quotation marks.  The `--incl_con` and `--excl_con` parameters are mutually exclusive.  When this parameter is used, the `--app_con` parameter cannot be used. |
| `--echo`  Short name: `-e` | Sets echo `ON` while running the script. The default is echo `OFF`. |
| `--spool`  Short name: `-s` | Spools the output of every script into a file with the following name:  ``` log-file-name-base_script-name-without-extension_[container-name-if-any].default-extension ``` |
| `--error_logging`  Short name: `-E` | When set to `ON`, the default error logging table is used. `ON` is the default setting. When set to `ON`, errors are written to the table `SPERRORLOG` in the current schema in each container in which the SQL script runs. If this table does not exist in a container, then it is created automatically.  When a table other than `SPERRORLOG` is specified, errors are written to the specified table. The table must exist in each container in which the SQL script runs, and the current user must have the necessary privileges to perform DML operations on the table in each of these containers.  See [SQL\*Plus User's Guide and Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQPUG160) for more information about the error logging table. |
| `--app_con`  Short name: `-F` | Specify an application root. The scripts are run in the application root and in the application PDBs that are plugged into the application root.  When this parameter is used, the `--incl_con` and `--excl_con` parameters cannot be used. |
| `--no_set_errlog_ident`  Short name: `-I` | Do not issue a `SET ERRORLOGGING` identifier. This option is intended for cases in which the `SET ERRORLOGGING` identifier is already set and should not be overwritten. |
| `--diag`  Short name: `-g` | Turns on the generation of debugging information. |
| `--verbose`  Short name: `-v` | Turns on verbose output. |
| `--ignore_unavailable_pdbs`  Short name: `-f` | Ignore PDBs that are closed or, if the `--incl_con` or `--excl_con` option is used, do not exist and process only open PDBs that were specified explicitly or implicitly.  When this option is not specified and some specified PDBs do not exist or are not open, an error is returned and none of the containers are processed. |
| `--force_pdb_mode` | The required open mode for all PDBs against which the scripts are run. Specify one of the following values:  - `UNCHANGED` - `READ WRITE` - `READ ONLY` - `UPGRADE` - `DOWNGRADE`  When a value other than `UNCHANGED` is specified, all of the PDBs against which the script is run are changed to the specified open mode. If a PDB is open in a different mode, then the PDB is closed and re-opened in the specified mode. After all of the scripts are run, each PDB is restored to its original open mode.  When `UNCHANGED`, the default, is specified, the open mode of the PDBs is not changed. |
| `--recover`  Short name: `-R` | Causes catcon.pl to attempt to recover if a SQL\*Plus process that it spawned ends unexpectedly. When this parameter is not specified, catcon.pl does not attempt to recover the process and closes. |
| `--log_file_base`  Short name: `-b` | (Required) The base name for log file names. |

**Parent topic:** Running Oracle-Supplied SQL Scripts in a CDB

#### 41.9.3 Running the catcon.pl Script

Examples illustrate running the catcon.pl script.

If a SQL script or SQL statement run by catcon.pl performs data manipulation language (DML) or data definition language (DDL) operations, then the containers being modified must be in read/write mode. See " Modifying the Open Mode of PDBs ".

To run the catcon.pl script:

1. Open a command line prompt.
2. Run the catcon.pl script and specify one or more SQL scripts or SQL statements:
	```
	$ORACLE_HOME/perl/bin/perl $ORACLE_HOME/rdbms/admin/catcon.pl parameters SQL_script
	$ORACLE_HOME/perl/bin/perl $ORACLE_HOME/rdbms/admin/catcon.pl parameters -- --xSQL_statement
	```

Examples That Run the catcon.pl Script

The following examples run the catcon.pl script.

Example 41-36 Running the catblock.sql Script in All Containers in a CDB

This example runs the catblock.sql script in all of the containers of a CDB.

```
$ORACLE_HOME/perl/bin/perl $ORACLE_HOME/rdbms/admin/catcon.pl --usr SYS 
--script_dir $ORACLE_HOME/rdbms/admin --log_file_base catblock_output catblock.sql
```

The following parameters are specified:

- The `--usr` parameter specifies that `SYS` user runs the script in each container.
- The `--script_dir` parameter specifies that the SQL script is in the $ORACLE\_HOME/rdbms/admin directory.
- The `--log_file_base` parameter specifies that the base name for log file names is catblock\_output.

Default parameter values are used for all other parameters. Neither the `--incl_con` nor the `--excl_con` parameter is specified. Therefore, catcon.pl runs the script in all containers by default.

Example 41-37 Running the catblock.sql Script in Specific PDBs

This example runs the catblock.sql script in the `hrpdb` and `salespdb` PDBs in a CDB.

```
$ORACLE_HOME/perl/bin/perl $ORACLE_HOME/rdbms/admin/catcon.pl --usr SYS --int_usr SYS 
--script_dir $ORACLE_HOME/rdbms/admin --log_dir '/disk1/script_output' --incl_con 'HRPDB SALESPDB' 
--log_file_base catblock_output catblock.sql
```

The following parameters are specified:

- The `--usr` parameter specifies that `SYS` user runs the script in each container.
- The `--int_usr` parameter specifies that `SYS` user performs internal tasks.
- The `--script_dir` parameter specifies that the SQL script is in the $ORACLE\_HOME/rdbms/admin directory.
- The `--log_dir` parameter specifies that the output files are placed in the /disk1/script\_output directory.
- The `--incl_con` parameter specifies that the SQL script is run in the `hrpdb` and `salespdb` PDBs. The script is not run in any other containers in the CDB.
- The `--log_file_base` parameter specifies that the base name for log file names is catblock\_output.

Example 41-38 Running the catblock.sql Script in All Containers Except for Specific PDBs

This example runs the catblock.sql script in all of the containers in a CDB except for the `hrpdb` and `salespdb` PDBs.

```
$ORACLE_HOME/perl/bin/perl $ORACLE_HOME/rdbms/admin/catcon.pl --usr SYS 
--script_dir $ORACLE_HOME/rdbms/admin --log_dir '/disk1/script_output' --excl_con 'HRPDB SALESPDB' 
--log_file_base catblock_output catblock.sql
```

The following parameters are specified:

- The `--usr` parameter specifies that `SYS` user runs the script in each container.
- The `--script_dir` parameter specifies that the SQL script is in the $ORACLE\_HOME/rdbms/admin directory.
- The `--log_dir` parameter specifies that the output files are placed in the /disk1/script\_output directory.
- The `--excl_con` parameter specifies that the SQL script is run in all of the containers in the CDB except for the `hrpdb` and `salespdb` PDBs.
- The `--log_file_base` parameter specifies that the base name for log file names is catblock\_output.

Example 41-39 Running a SQL Script with Command Line Parameters

This example runs the custom\_script.sql script in all of the containers of a CDB.

```
$ORACLE_HOME/perl/bin/perl $ORACLE_HOME/rdbms/admin/catcon.pl --usr SYS 
--script_dir /u01/scripts --log_file_base custom_script_output custom_script.sql
'--phr' '--PEnter password for user hr:'
```

The following parameters are specified:

- The `--usr` parameter specifies that `SYS` user runs the script in each container.
- The `--script_dir` parameter specifies that the SQL script is in the /u01/scripts directory.
- The `--log_file_base` parameter specifies that the base name for log file names is custom\_script\_output.
- The `--p` parameter specifies `hr` for a command line parameter
- The `--P` parameter specifies an interactive parameter that prompts for the password of user `hr`.

Default parameter values are used for all other parameters. Neither the `-incl_con` nor the `-excl_con` parameter is specified. Therefore, catcon.pl runs the script in all containers by default.

Example 41-40 Running a SQL Statement in All Containers in a CDB

This example runs a SQL statement in all of the containers of a CDB.

```
$ORACLE_HOME/perl/bin/perl $ORACLE_HOME/rdbms/admin/catcon.pl --usr SYS --echo 
--log_file_base select_output -- --x"SELECT * FROM DUAL"
```

The following parameters are specified:

- The `--usr` parameter specifies that `SYS` user runs the script in each container.
- The `--echo` parameter shows output for the SQL statement.
- The `--log_file_base` parameter specifies that the base name for log file names is select\_output.
- The SQL statement `SELECT * FROM DUAL` is inside quotation marks and is preceded by `--x`. Because `--x` is preceded by a parameter (`--log_file_base`), it must be preceded by `--`.

Default parameter values are used for all other parameters. Neither the `-incl_con` nor the `-excl_con` parameter is specified. Therefore, catcon.pl runs the SQL statement in all containers by default.

See Also:

" [Monitoring Locks](monitoring-the-database.md) " for information about the catblock.sql script

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=REFRN005) for more information about SQL scripts

**Parent topic:** Running Oracle-Supplied SQL Scripts in a CDB

### 41.10 Shutting Down a CDB Instance

You can shut down a CDB instance in the same way that you shut down a non-CDB instance.

The following prerequisites must be met:

- The CDB instance must be mounted or open.
- The current user must be a common user with `SYSDBA`, `SYSOPER`, `SYSBACKUP`, or `SYSDG` administrative privilege. To shut down a CDB, you must exercise this privilege using `AS` `SYSDBA`, `AS` `SYSOPER`, `AS` `SYSBACKUP`, or `AS` `SYSDG`, respectively, at connect time.

To shut down a CDB:

1. In SQL\*Plus, ensure that the current container is the root.
	See " Connecting to a Container Using the SQL\*Plus CONNECT Command ".
2. Shut down the CDB instance.
	" [Shutting Down a Database](starting-up-and-shutting-down.md) "

See Also:

**Parent topic:** Administering a CDB with SQL\*Plus