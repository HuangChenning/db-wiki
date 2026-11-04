---
title: "Administrator’s Guide"
book: "Multitenant Administrator's Guide"
doc_id: F31734-10
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/multi/administering-a-cdb-with-sql-plus.html
tags:
  - oracle
  - 21c
  - multitenant-administrators-guide
---

Administering a multitenant container database (CDB) includes tasks such as accessing a container, modifying a CDB, executing DDL statements, and running Oracle-supplied SQL scripts.

Note:

You can complete the tasks in this chapter using SQL\*Plus or Oracle SQL Developer.

- About CDB Administration  
	Some administrative tasks apply to the entire CDB, whereas others apply to specific containers.
- Accessing Containers in a CDB  
	You can connect to a container by using the SQL\*Plus `CONNECT` command. Alternatively, you can switch into a container with an `ALTER SESSION SET CONTAINER` SQL statement.
- Starting Up and Shutting Down a CDB  
	When you start up a CDB, you create an instance and then determine the state of the CDB. Shutting down a currently running Oracle Database instance can optionally close and dismount a CDB.
- Modifying a CDB at the System Level  
	You can set initialization parameters at the CDB level. In some cases, you can override these parameters at the PDB level.
- Modifying Containers When Connected to the CDB Root  
	You can modify the entire CDB or the root with the `ALTER DATABASE` statement.
- Executing SQL in a Different Container  
	To execute SQL in a different container, use the `CONTAINERS` clause for DML or the `CONTAINER` clause for DDL.
- Monitoring Containers in a CDB  
	You can view metadata about CDBs, PDBs, and application containers using SQL\*Plus or SQL Developer.

See Also:

" [Tools for a Multitenant Environment](introduction-to-the-multitenant-architecture.md) "

**Parent topic:** [Administering a Multitenant Environment](managing-a-multitenant-environment.md)

### About CDB Administration

Some administrative tasks apply to the entire CDB, whereas others apply to specific containers.

- About the Current Container  
	The data dictionary in each container in a CDB is separate, and the current container is the container whose data dictionary is used for name resolution and for privilege authorization.
- About Administrative Tasks in a CDB  
	Common users perform administrative tasks for a CDB.
- About Using Manageability Features in a CDB  
	For each of Oracle Database's manageability features in a CDB, it is important to understand the data location and the data visibility.
- About Managing Tablespaces in a CDB  
	A tablespace is a logical storage container for database objects, such as tables and indexes, that consume storage space.
- About Managing Database Objects in a CDB  
	In a CDB, different containers can contain different database objects.
- About Flashing Back a PDB  
	You can use the `FLASHBACK PLUGGABLE DATABASE` statement to return a PDB to a past time or system change number (SCN).
- About Restricting PDB Users for Enhanced Security  
	There are several ways to restrict PDB users for enhanced security.

**Parent topic:** Administering a CDB

#### About the Current Container

The data dictionary in each container in a CDB is separate, and the current container is the container whose data dictionary is used for name resolution and for privilege authorization.

The current container can be the CDB root, an application root, a PDB, or an application PDB. Each session has exactly one current container at any point in time. However, a session can switch from one container to another.

Each container has a unique ID and name in a CDB. You can use the `CON_ID` and `CON_NAME` parameters in the `USERENV` namespace to determine the current container ID and name with the `SYS_CONTEXT` function. For example, the following query returns the current container name:

```
SELECT SYS_CONTEXT ('USERENV', 'CON_NAME') FROM DUAL;
```

You can access a container in various ways. For example, you can use the SQL\*Plus `CONNECT` command, and you can use an `ALTER SESSION SET CONTAINER` statement to switch the container of the current session.

The following rules apply to the current container in a CDB:

- The current container can be `CDB$ROOT` (CDB root) only for common users.
- The current container can be a specific PDB for common users and local users.
- The current container can be an application root only for common users or for application common users created in the application root.
- The current container can be a specific application PDB for common users, application common users, and local users.
- The current container must be the CDB root or an application root when a SQL statement includes `CONTAINER = ALL`.
	You can include the `CONTAINER` clause in several SQL statements, such as the `CREATE USER`, `ALTER USER`, `CREATE ROLE`, `GRANT`, `REVOKE`, and `ALTER SYSTEM` statements. Note the following rules about `CONTAINER = ALL`:
	- When a SQL statement includes `CONTAINER = ALL` and the current container is the CDB root, the SQL statement affects all containers in the CDB, including all PDBs, application roots, and application PDBs.
		- When a SQL statement includes `CONTAINER = ALL` and the current container is an application root, the SQL statement affects all containers in the application container, including the application root and all the application PDBs that belong to the application root. The SQL statement does not affect the CDB root or any PDBs or application PDBs that do not belong to the current application root.
		- Only a common user or application common user with the commonly granted `SET CONTAINER` privilege can run a SQL statement that includes `CONTAINER = ALL`.

See Also:

- " About Container Access in a CDB "
- " Executing Code in Containers Using the DBMS\_SQL Package "
- " Determining the Current Container ID or Name "
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF06117)
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=DBSEG754)

**Parent topic:** About CDB Administration

#### About Administrative Tasks in a CDB

Common users perform administrative tasks for a CDB.

A common user has a single identity and can log in to the CDB root, any application root, PDB, or application PDB in which it has privileges. Some tasks, such as starting up a CDB instance, can be performed only by a common user.

Note:

A multitenant container database is the only supported architecture in Oracle Database 21c. While the documentation is being revised, legacy terminology may persist. In most cases, "database" and "non-CDB" refer to a CDB or PDB, depending on context. In some contexts, such as upgrades, "non-CDB" refers to a non-CDB from a previous release.

The following table describes some CDB administrative tasks and provides pointers to the relevant documentation.

Table 15-1 Administrative Tasks for CDBs

| Task | Description | Additional Information |
| --- | --- | --- |
| Starting up a CDB instance | To start a CDB instance, the current user must be a common user whose current container is the CDB root.  When you open a CDB, the CDB root is opened, but its other containers are mounted. Use the `ALTER PLUGGABLE DATABASE` statement to modify the open mode of one or more containers. | " Starting Up and Shutting Down a CDB " for information about starting up a database  " [Modifying the Open Mode of PDBs](administering-pdbs-with-sql-plus.md) "  " [Modifying a PDB with the ALTER PLUGGABLE DATABASE Statement](administering-pdbs-with-sql-plus.md) "  " About the Current Container " |
| Managing processes | A CDB has one set of background processes shared by the CDB root and all containers. | [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-9B3A136E-D275-417B-B6F4-59A45D42655F) for information about managing processes |
| Managing memory | A CDB has a single system global area (SGA) and a single aggregate program global area (PGA). The memory required by a CDB is the sum of the memory requirements for all containers that will be part of the CDB. | [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-BEABE53D-8058-4834-B99B-5C80A8AD5B06) for information about managing memory |
| Managing security | You can create and drop common users, application common users, and local users in a CDB. You can also grant privileges to and revoke privileges from these users. You can also manage the `CONTAINER_DATA` attributes of common users and application common users.  In addition, grant the following roles to the appropriate users:  - Grant the `CDB_DBA` role to CDB administrators. - Grant the `PDB_DBA` role to application container administrators and PDB administrators. | [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=DBSEG573) |
| Monitoring errors and alerts | A CDB has one alert log for the entire CDB. The name of an application container, PDB, or application PDB is included in records in trace files, when appropriate. | [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-E5F89E8E-7FBC-47DD-BA5D-96AFD9CE4BC7) for information about monitoring errors and alerts |
| Managing diagnostic data | In a CDB, you can use the Oracle Database fault diagnosability infrastructure and the Automatic Diagnostic Repository (ADR). | [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-8DEB1BE0-8FB9-4FB2-A19A-17CF6F5791C3) for information about managing diagnostic data |
| Managing control files | A CDB has one control file. | [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-5F6F9382-6921-4992-9789-E63B18E99C5F) for information about managing control files |
| Managing the online redo log and the archived redo log files | A CDB has one online redo log and one set of archived redo log files. | [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-BC1F1762-0BB1-4218-B7AF-6160C395AAE4) for information about managing the redo log  [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-5EE4AC49-E1B2-41A2-BEE7-AA951EAAB2F3) for information about managing archived redo log files |
| Managing tablespaces | You can create, modify, and drop tablespaces and temporary tablespaces for the CDB root and for individual containers. You can also specify a default tablespace, default tablespace type, and a default temporary tablespace for the CDB root. The CDB root has its own set of Oracle-supplied tablespaces, such as the `SYSTEM` tablespace, and other containers have their own set of Oracle-supplied tablespaces. | [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-1C162C60-6698-44F2-B2A9-F3E2D2958D88) for information about managing tablespaces  " About Container Modification When Connected to CDB Root " |
| Managing data files and temp files | The CDB root has its own data files, and other containers have their own data files. Note the following:  - You can limit the amount of storage used by the data files for a container by using the `STORAGE` clause in a `CREATE PLUGGABLE DATABASE` or `ALTER PLUGGABLE DATABASE` statement. - There is a default temporary tablespace for the CDB root and for individual containers. | [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-501A8889-3C18-4F99-B0B7-9095E981B970) for information about managing data files and temp files  " About Container Modification When Connected to CDB Root "  " [Storage Limits](overview-of-pdb-creation.md) "  " [Modifying a PDB at the Database Level](administering-pdbs-with-sql-plus.md) " |
| Managing undo | A CDB can run in local undo mode or shared undo mode. Local undo mode means that every container in the CDB uses local undo. Shared undo mode means that there is one active undo tablespace for a single-instance CDB, or for an Oracle RAC CDB, there is one active undo tablespace for each instance.  In a CDB, the `UNDO_MANAGEMENT` initialization parameter must be set to `AUTO`, and an undo tablespace is required to manage the undo data. | " Setting the Undo Mode in a CDB Using ALTER DATABASE "  [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-2C865CF9-A8B5-4BF1-A451-E8C08D3611F0) for information about managing undo  " About the Current Container " |
| Moving data between containers | You can move data between containers within a CDB using the same methods that you would use to move data between CDBs. For example, you can transport the data or use Data Pump export/import to move the data. | [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-1901E9C3-8FCE-4D4E-AB65-34D703474E52) for information about transporting data  [Oracle Database Utilities](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SUTIL100) |
| Using Oracle Managed Files | Using Oracle Managed files can simplify administration for a CDB. | [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-4A3C4616-0D81-4BBA-8EAD-FCAA8AD5C15A) for information about using Oracle Managed Files |
| Using Transparent Data Encryption | Transparent Data Encryption is a feature that enables encryption of individual table columns before storing them in the data file, or enables encryption of entire tablespaces. In a CDB, each container has its own master key for Transparent Data Encryption, and, where applicable, the `ADMINISTER KEY MANAGEMENT` SQL statement enables key management at the CDB level and for individual containers. | [Oracle Database Advanced Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ASOAG-GUID-0E59AD1E-514A-4F93-9A1F-E5683A535A89)  " About the Current Container " |
| Using a standby database | Oracle Data Guard can configure a physical standby or a logical standby of a CDB. Data Guard operates on the entire CDB, not on individual containers in a CDB. | [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=GUID-5E73667D-4A56-445E-911F-1E99092DD8D7) |
| Using Oracle Database Vault | Oracle Database Vault common realms can be scoped to an application root on common objects. Database Vault common command rules can be scoped to either the CDB or an application root. Local realms and command rules can be locally scoped to individual PDBs or application PDBs. When Oracle Database Vault security objects are in the CDB root or an application root, enforcement of the security objects only applies to the containers that have Oracle Database Vault enabled. | [Oracle Database Vault Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=DVADM71131) |
| Dropping a database | When you drop a CDB, all containers in the CDB are dropped along with their data. These containers include the CDB root and PDB seed and all application containers, application seeds, PDBs, and application PDBs.  You can also drop individual application containers, application seeds, PDBs, and application PDBs with the `DROP PLUGGABLE DATABASE` statement. | [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-92F8F1B3-9E04-46D2-A4E4-3CC788459A38) for information about dropping a database  " [Dropping a PDB](removing-a-pdb.md) " |

See Also:

[Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=CNCPT-GUID-BBAD3448-8A5A-4397-BD3A-F05D945DB7F8) for more information about the architecture of a CDB

**Parent topic:** About CDB Administration

#### About Using Manageability Features in a CDB

For each of Oracle Database's manageability features in a CDB, it is important to understand the data location and the data visibility.

When feature data resides in the CDB root, the data is not included when a PDB is unplugged. When the data resides in a PDB, however, the data remains both when the PDB is unplugged and when it is plugged in.

Generally, in a CDB, a common user can view data for the CDB root and for multiple PDBs when the common user's current container is the CDB root. A common user can view this data by querying container data objects. The specific data that is visible varies for the manageability features. A user whose current container is a PDB can view data for that PDB only.

The following table describes how the manageability features work in a CDB.

Table 15-2 Manageability Features in a CDB

| Manageability Feature | Data Location | Data Visibility | Additional Information |
| --- | --- | --- | --- |
| Active Session History (ASH)  ASH collects information about active database sessions. You can use this information to analyze and identify performance issues. | Most of the ASH data is stored in memory. A small percentage of the ASH data samples are stored in the CDB root.  ASH data related to a PDB is not included if the PDB is unplugged. | A common user whose current container is the CDB root can view ASH data for the CDB root and for PDBs.  A user whose current container is a PDB can view ASH data for the PDB only. | [Oracle Database 2 Day + Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=TDPPT065)  [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=TGDBA277) |
| Alerts  An alert is a notification of a possible problem. | Threshold settings that pertain to a PDB are stored in the PDB.  Alerts posted when thresholds are violated are enqueued into the alert queue in the CDB root.  Threshold settings that pertain to a PDB are included if the PDB is unplugged. Alerts related to a PDB are not included if the PDB is unplugged. | A common user whose current container is the CDB root can view alerts for the CDB root and for PDBs.  A user whose current container is a PDB can view alert thresholds and alerts for the PDB only. | [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-E5F89E8E-7FBC-47DD-BA5D-96AFD9CE4BC7) for information about monitoring errors and alerts |
| Automated Database Maintenance Tasks  Automated database maintenance tasks are tasks that are started automatically at regular intervals to perform maintenance operations on the database. Automated tasks include automatic optimizer statistics collection, Automatic Segment Advisor tasks, and Automatic SQL Tuning Advisor tasks.  The `ENABLE_AUTOMATIC_MAINTENANCE_PDB` initialization parameter can enable or disable the running of automated maintenance tasks for all the PDBs in a CDB or for individual PDBs in a CDB.  The `AUTOTASK_MAX_ACTIVE_PDBS` initialization parameter limits the number of PDBs that can schedule automated maintenance tasks at the same time (during a maintenance window). | A user can schedule maintenance windows and enable or disable maintenance tasks for the current container only. If the current container is the CDB root, then the changes only apply to the CDB root. If the current container is a PDB, then the changes only apply to the PDB.  Data related to a PDB is stored in the PDB for automatic optimizer statistics collection and the Automatic Segment Advisor. This data is included if the PDB is unplugged.  Automatic SQL Tuning Advisor runs only in the CDB root. See the SQL Tuning Advisor row in this table for information about data collected by Automatic SQL Tuning Advisor. | See the appropriate row in this table for data visibility information about the following manageability features: automatic optimizer statistics collection, Optimizer Statistics Advisor, Automatic Segment Advisor, and Automatic SQL Tuning Advisor. | [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-7F7C805E-BA64-43A5-9A09-FC259FFA9AA8) for information about managing automated database maintenance tasks  [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=REFRN-GUID-3ACE01FA-8342-4F35-94BB-955412B9C76A) for information about the `ENABLE_AUTOMATIC_MAINTENANCE_PDB` initialization parameter  [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=REFRN-GUID-5DC631A2-4CDD-4C1F-B337-184BFD4C29B8) for information about the `AUTOTASK_MAX_ACTIVE_PDBS` initialization parameter |
| Automatic Database Diagnostic Monitor (ADDM)  ADDM can diagnose the performance of a CDB or PDB and determine how identified problems can be resolved. | ADDM executions occur in a PDB or in the CDB root. ADDM analyzes data using one of the following sources:  - AWR data stored inside the PDB through an AWR snapshot taken inside the PDB - AWR data from a CDB root or PDB that is imported into the AWR storage of a PDB - AWR data stored in the root container through an AWR snapshot taken in root  Before the start of the analysis, ADDM determines the source of the AWR data (PDB or CDB root) and applies the rules applicable to each data type.  Note: Automatic ADDM for a PDB is enabled only when automatic snapshots are enabled for the PDB. | A common user whose current container is the CDB root can review results for the entire CDB. The ADDM results can include information about multiple PDBs. ADDM results related to a PDB are not included if the PDB is unplugged. The ADDM results cannot be viewed when the current container is a PDB.  A user whose current container is a PDB can view ADDM results data for the current PDB only. The results exclude findings that apply to the CDB as a whole, for example, I/O problems relating to the buffer cache size. | [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=TGDBA026) |
| Automatic Optimizer Statistics Collection  Automatic optimizer statistics collection gathers optimizer statistics for all schema objects in the database for which there are no statistics or only stale statistics. The statistics gathered by this task are used by the SQL query optimizer to improve the performance of SQL execution. | When an automatic optimizer statistics collection task gathers data for a PDB, it stores this data in the PDB. This data is included if the PDB is unplugged. | A common user whose current container is the CDB root can view optimizer statistics data for PDBs.  A user whose current container is a PDB can view optimizer statistics data for the PDB only. | [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=TGSQL389) |
| Automatic Segment Advisor  The Automatic Segment Advisor identifies segments that have space available for reclamation and makes recommendations on how to defragment those segments. | When Automatic Segment Advisor gathers data for a PDB, it stores this data in the PDB. This data is included if the PDB is unplugged. | A common user whose current container is the CDB root can view Automatic Segment Advisor data for PDBs.  A user whose current container is a PDB can view the Automatic Segment Advisor data for the PDB only. | [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-1F297567-4BEC-438E-9E13-683D2BB47F44) for information about reclaiming unused space |
| Automatic Workload Repository (AWR)  The AWR collects, processes, and maintains performance statistics for problem detection and self-tuning purposes. This data is stored in the database. The gathered data can be displayed in both reports and views. | AWR reports can be generated in the CDB root or in any PDB. AWR reports generated in the CDB root pertain to the entire CDB, while AWR reports generated when a PDB is the current container only pertain to that PDB.  AWR data generated in the CDB root is stored in the CDB root. AWR data generated in a PDB is stored in the PDB.  When a PDB is unplugged, AWR data stored in the CDB root is not included.  When a PDB is unplugged, AWR data stored in the PDB is included. | A common user whose current container is the CDB root can view AWR data for the CDB root and for PDBs.  A user whose current container is a PDB can view AWR data for the PDB only. | [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=TGDBA169) |
| Database Replay  Database Replay is a feature of Oracle Real Application Testing. Database Replay captures the workload for a CDB or PDB and replays it exactly on a test database. | Capture files are always stored in operating system files, regardless of whether the capture and replay is at the CDB level or PDB level. | For CDB-level workloads, a common user whose current container is the CDB root can view database capture and replay information. For PDB-level workloads, a local or common PDB administrator with the `SELECT_CATALOG_ROLE` privilege can view this information in `DBA_WORKLOAD_CAPTURES` and `DBA_WORKLOAD_REPLAYS`. | [Oracle Database Testing Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=RATUG4080) |
| Optimizer Statistics Advisor  Optimizer Statistics Advisor analyzes how statistics are being gathered and suggests changes that can be made to fine tune statistics collection. | Data related to a PDB is stored in the PDB for Optimizer Statistics Advisor. This data is included if the PDB is unplugged. | A common user whose current container is the CDB root can view Optimizer Statistics Advisor data for PDBs.  A user whose current container is a PDB can view the Optimizer Statistics Advisor data for the PDB only. | [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=TGSQL-GUID-054F4B76-DD57-46EE-98EA-0FF04F49D1B3) |
| SQL Management Base (SMB)  SMB stores statement logs, plan histories, SQL plan baselines, and SQL profiles in the data dictionary. | SMB data related to a PDB is stored in the PDB. The SMB data related to a PDB is included if the PDB is unplugged. | A common user whose current container is the CDB root can view SMB data for PDBs.  A user whose current container is a PDB can view the SMB data for the PDB only. | [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=TGSQL631) |
| SQL Performance Analyzer (SPA)  SPA can analyze the SQL performance impact of SQL tuning and other system changes. SPA is often used with Database Replay. | A common user whose current container is the CDB root can run SPA for any PDB. In this case, the SPA results data is stored in the CDB root and is not included if the PDB is unplugged.  A user whose current container is a PDB can run SPA on the PDB. In this case, the SPA results data is stored in the PDB and is included if the PDB is unplugged. | A common user whose current container is the CDB root can view SPA results data for PDBs.  A user whose current container is a PDB can view the SPA results data for the PDB only. | [Oracle Database Testing Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=RATUG239) |
| SQL Tuning Sets (STS)  An STS is a database object that includes one or more SQL statements along with their execution statistics and execution context, and could include a user priority ranking.  You can use an STS to tune a group of SQL statements or test their performance using SPA. | An STS can be stored in the CDB root or in any PDB. If it is stored in the CDB root, then you can load SQL statements from any PDB into it.  When a PDB is unplugged, an STS stored in the CDB root is not included, even if the STS contains SQL statements from the PDB.  When a PDB is unplugged, an STS stored in the PDB is included. | A common user whose current container is the CDB root can view STS data stored in the CDB root only.  A user whose current container is a PDB can view STS data for the PDB only. | [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=TGSQL516) |
| SQL Tuning Advisor  SQL Tuning Advisor optimizes SQL statements that have been identified as high-load SQL statements. | Automatic SQL Tuning Advisor data is stored in the CDB root. It might have results about SQL statements executed in a PDB that were analyzed by the advisor, but these results are not included if the PDB is unplugged.  A common user whose current container is the CDB root can run SQL Tuning Advisor manually for SQL statements from any PDB. When a statement is tuned, it is tuned in any container that runs the statement.  A user whose current container is a PDB can also run SQL Tuning Advisor manually for SQL statements from the PDB. When SQL Tuning Advisor is run manually from a PDB, the results are stored in the PDB from which it is run. In this case, a statement is tuned only for the current PDB, and the results related to a PDB are included if the PDB is unplugged. | When SQL Tuning Advisor is run automatically, the results are visible only to a common user whose current container is the CDB root. These results cannot be viewed when the current container is a PDB.  When SQL Tuning Advisor is run manually by a user whose current container is a PDB, the results are only visible to a user whose current container is that PDB. | [Oracle Database 2 Day + Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=TDPPT160)  [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=TGSQL540) |

To run SPA or SQL Tuning Advisor for SQL statements from a PDB, a common user must have the following privileges:

- Common `SET CONTAINER` privilege or local `SET CONTAINER` privilege in the PDB
- The privileges required to execute the SQL statements in the PDB

See Also:

- " About the Current Container "
- " About CDB and Container Information in Views " for an overview of container data objects
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=DBSEG803) for detailed information about container data objects

**Parent topic:** About CDB Administration

#### About Managing Tablespaces in a CDB

A tablespace is a logical storage container for database objects, such as tables and indexes, that consume storage space.

At the physical level, a tablespace stores data in one or more data files or temp files. You can use the `ALTER DATABASE` statement to manage tablespaces in a CDB.

The following are considerations for tablespaces in a CDB:

- A permanent tablespace can be associated with exactly one container.
- When you create a tablespace in a container, the tablespace is associated with that container.
- When local undo is disabled for a CDB, the CDB has only one active undo tablespace, or one active undo tablespace for each instance of an Oracle RAC CDB. When local undo is enabled for a CDB, each container in the CDB has its own undo tablespace.
- A local undo tablespace is required for each node in an Oracle Real Application Clusters (Oracle RAC) cluster in which the PDB is open.
- There is one default temporary tablespace each container in the CDB, including the CDB root, each PDB, each application root, and each application PDB.

- About Managing Permanent Tablespaces in a CDB  
	A permanent tablespace can be associated with only one container. Therefore, a permanent tablespace can be associated with the root or with one PDB.
- About Managing Temporary Tablespaces in a CDB  
	Each container in a CDB has its own default temporary tablespace (or tablespace group).

**Parent topic:** About CDB Administration

##### About Managing Permanent Tablespaces in a CDB

A permanent tablespace can be associated with only one container. Therefore, a permanent tablespace can be associated with the root or with one PDB.

Each container in a CDB must have its own default permanent tablespace, and default permanent tablespaces cannot be shared between containers. Users connected to the container who are not explicitly assigned a tablespace use the default permanent tablespace for the container.

**Parent topic:** About Managing Tablespaces in a CDB

##### About Managing Temporary Tablespaces in a CDB

Each container in a CDB has its own default temporary tablespace (or tablespace group).

You also can create additional temporary tablespaces for individual containers, and you can assign specific users in containers to these temporary tablespaces. When you unplug a PDB, its temporary tablespaces are also unplugged.

When a user is not assigned a temporary tablespace explicitly in a container, the user’s temporary tablespace is the default temporary tablespace for the container.

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-1C162C60-6698-44F2-B2A9-F3E2D2958D88) for information about managing tablespaces
- " [Unplugging a PDB from a CDB](removing-a-pdb.md) "
- " Modifying an Entire CDB Using ALTER DATABASE "
- " Modifying the CDB Root Using ALTER DATABASE "

**Parent topic:** About Managing Tablespaces in a CDB

#### About Managing Database Objects in a CDB

In a CDB, different containers can contain different database objects.

An Oracle database stores database objects, such as tables, indexes, and directories. Database objects that are owned by a schema are called schema objects, while database objects that are not owned by a schema are called nonschema objects. The CDB root and PDBs contain schemas, and schemas contain schema objects. The CDB root and PDBs can also contain nonschema objects, such as users, roles, tablespaces, directories, and editions.

The CDB root contains Oracle-supplied schemas and database objects. Oracle-supplied common users, such as `SYS` and `SYSTEM`, own these schemas and common database objects. They can also own local objects, both in the CDB root and in a PDB.

You can create common user accounts in the CDB root to administer PDBs and application containers. User-created common user accounts can create database objects in the CDB root. Oracle recommends that, in the CDB root, schemas owned by user-created common user accounts contain only database triggers and the objects used in their definitions. A user-created common user account can also own any type of local object in a PDB.

You can create local user accounts in a PDB. A local user in a PDB can create schema objects and nonschema objects in the PDB. You cannot create local user accounts in the CDB root.

In a CDB, names are resolved in the context of the dictionary of the user's current container.

See Also:

- " About the Current Container "
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-5BEEEA18-8606-48CA-B51A-34FD301BF93B) for information about managing schema objects
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF20003) for information about schema objects and nonschema objects
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=DBSEG573) for information about creating common users and local users

**Parent topic:** About CDB Administration

#### About Flashing Back a PDB

You can use the `FLASHBACK PLUGGABLE DATABASE` statement to return a PDB to a past time or system change number (SCN).

You can create restore points for a PDB and flash back the PDB to the restore point without affecting the CDB or other PDBs.

Note:

[Oracle Database Backup and Recovery User’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=BRADV-GUID-A2146E48-16FC-40CC-B25D-902DEB93CB75)

**Parent topic:** About CDB Administration

#### About Restricting PDB Users for Enhanced Security

There are several ways to restrict PDB users for enhanced security.

A PDB lockdown profile restricts the features and options available to users in a PDB. The `PDB_OS_CREDENTIAL` initialization parameter can specify a unique operating system user for a PDB to limit operating system access. Also, when the `PATH_PREFIX` and `CREATE_FILE_DEST` clauses are specified during PDB creation, they limit file system access.

- PDB Lockdown Profiles  
	When identities are shared between PDBs, elevated privileges might exist. You can use lockdown profiles to prevent this elevation of privileges.
- PDB\_OS\_CREDENTIAL Initialization Parameter  
	When the database accesses an external procedure with the `extproc` agent, the `PDB_OS_CREDENTIAL` initialization parameter determines the identity of the operating system user employed when interacting with the operating system from a PDB.

**Parent topic:** About CDB Administration

##### PDB Lockdown Profiles

When identities are shared between PDBs, elevated privileges might exist. You can use lockdown profiles to prevent this elevation of privileges.

Identities can be shared in the following situations:

- At the operating system level, when the database interacts with operating system resources such as files or processes
- At the network level, when the database communicates with other systems
- Inside the database, as PDBs access or create common objects or communicate across container boundaries using features such as database links

To increase security, a CDB administrator can use PDB lockdown profiles to restrict users in particular PDBs. A PDB lockdown profile can disable users from running specified SQL statements, such as `ALTER SYSTEM` statements, or disable access to a package that can access the network, such as `UTL_SMTP`. A PDB lockdown profile can also restrict access to common users, common objects, administrative tools such as Oracle XML DB, administrative features such as cursor sharing, and database options such as Oracle Database Advanced Queuing. PDB lockdown profiles can prohibit the use of the XDB protocols (FTP, HTTP, HTTPS) by a PDB with the `XDB_PROTOCOLS` feature.

When logged in to the CDB root or application root, create a lockdown profile by issuing the `CREATE LOCKDOWN PROFILE` statement, which supports the following optional clauses:

- `FROM static_base_profile` creates a new lockdown profile by using the values from an existing profile. Any subsequent changes to the existing profile will not affect the new profile.
- `INCLUDING dynamic_base_profile` creates a new lockdown profile by using the values from an existing profile, except that this new lockdown profile inherits the `DISABLE STATEMENT` rules that comprise the base profile, and any subsequent changes to the base profile.

The user issuing the statement must have the `CREATE LOCKDOWN PROFILE` system privilege in the current container. You can add and remove restrictions with the `ALTER LOCKDOWN PROFILE` statement. The user must issue the `ALTER` statement in the CDB root or application root and must have the have `ALTER LOCKDOWN PROFILE` system privilege in the current container.

Specify a lockdown profile by using the `PDB_LOCKDOWN` initialization parameter. This parameter determines whether the PDB lockdown profile applies to a given PDB. You can set this parameter at the following levels:

- PDB
	The profile applies only to the PDB in which it is set.
- Application container
	The profile applies to all application PDBs in the application container. The value can be modified only by an application common user who has application common `SYSDBA` or common `ALTER SYSTEM` privileges or a CDB common user who has common `SYSDBA` or common `ALTER SYSTEM` privileges.
- CDB
	The profile applies to all PDBs. A common user who has common `SYSDBA` or common `ALTER SYSTEM` privileges can override a CDB-wide setting for a specific PDB.

If the `PDB_LOCKDOWN` parameter in a PDB is set to the name of a lockdown profile different from the container for this PDB (CDB or application container), then a set of rules govern the interaction between restrictions.

See Also:

- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=DBSEG-GUID-AB5E62DB-7E2A-4B5A-BA96-A2BD2DF15275) for complete information about lockdown profiles
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=GUID-1CDEC3A3-F3F1-4279-9370-36AACF416E0A) for more information about the `CREATE LOCKDOWN PROFILE` statement
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=REFRN-GUID-27072E94-1E1D-4BB0-AEAE-D7AFDC02E0A1) for more information about the `PDB_LOCKDOWN` initialization parameter

**Parent topic:** About Restricting PDB Users for Enhanced Security

##### PDB\_OS\_CREDENTIAL Initialization Parameter

When the database accesses an external procedure with the `extproc` agent, the `PDB_OS_CREDENTIAL` initialization parameter determines the identity of the operating system user employed when interacting with the operating system from a PDB.

Using an operating system user described by a credential whose name is specified as a value of the `PDB_OS_CREDENTIAL` initialization parameter can ensure that operating system interactions are performed as a less powerful user. In this way, the feature protects data belonging to one PDB from being accessed by users connected to another PDB. A credential is an object that is created using the `CREATE_CREDENTIAL` procedure in the `DBMS_CREDENTIAL` package.

The Oracle operating system user is usually a highly privileged user. Using this account for operating system interactions is not recommended. Also, using the same OS user for operating system interactions from different PDBs might compromise data belonging to a given PDB.

**Parent topic:** About Restricting PDB Users for Enhanced Security

### Accessing Containers in a CDB

You can connect to a container by using the SQL\*Plus `CONNECT` command. Alternatively, you can switch into a container with an `ALTER SESSION SET CONTAINER` SQL statement.

- About Container Access in a CDB  
	You can use SQL\*Plus to access the root or a PDB in a CDB.
- Accessing a Container in a CDB  
	Access a container in a CDB with SQL\*Plus by issuing a `CONNECT` or `ALTER SESSION` command.

**Parent topic:** Administering a CDB

#### About Container Access in a CDB

You can use SQL\*Plus to access the root or a PDB in a CDB.

- Services in a CDB  
	Clients access the root or a PDB through database services.
- Session Limits in a CDB  
	The setting for the `SESSIONS` initialization parameter limits the total number of sessions available in a CDB, including the sessions connected to PDBs.
- User Names in a Multitenant Environment  
	Within each PDB, a user name must be unique with respect to other user names and roles in that PDB.
- How the Multitenant Option Affects Password Files for Administrative Users  
	The password information for the local and common administrative users is stored in different locations.

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-58A40F41-B611-4C0F-A6E3-D45A81515BF2) for information about submitting commands and SQL to the database
- [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=NETAG001) for information about configuring Oracle Net Services

**Parent topic:** Accessing Containers in a CDB

##### Services in a CDB

Clients access the root or a PDB through database services.

Database services have an optional `PDB` property. When a PDB is created, a new default service for the PDB is created automatically. The service has the same name as the PDB. With the service name, you can access the PDB using the easy connect syntax or the net service name from the `tnsnames.ora` file. Oracle Net Services must be configured properly for clients to access this service.

When a user connects using a service with a non-null `PDB` property, the user name is resolved in the context of the specified PDB. When a user connects without specifying a service or using a service name with a null `PDB` property, the user name is resolved in the context of the root. You can view the `PDB` property for a service by querying the `CDB_SERVICES` data dictionary view or by running the `config service` command in the SRVCTL utility.

Note:

When two or more CDBs on the same computer system use the same listener and two or more PDBs have the same service name in these CDBs, a connection that specifies this service name connects randomly to one of the PDBs with the service name. To avoid incorrect connections, ensure that all service names for PDBs are unique on the computer system, or configure a separate listener for each CDB on the computer system.

See Also:

- " [Managing Services for PDBs](administering-pdbs-with-sql-plus.md) "
- " Example 15-36 "

**Parent topic:** About Container Access in a CDB

##### Session Limits in a CDB

The setting for the `SESSIONS` initialization parameter limits the total number of sessions available in a CDB, including the sessions connected to PDBs.

If the limit is reached for the CDB, then users cannot connect to PDBs. To ensure that one PDB does not use too many sessions, you can limit the number of sessions available to a PDB by setting the `SESSIONS` initialization parameter in the PDB.

See Also:

" Listing the Modifiable Initialization Parameters in PDBs "

**Parent topic:** About Container Access in a CDB

##### User Names in a Multitenant Environment

Within each PDB, a user name must be unique with respect to other user names and roles in that PDB.

Note the following restrictions:

- For common user names, names for user-created common users must begin with a common user prefix. By default, for CDB common users, this prefix is `C##`. For application common users, this prefix is an empty string. This means that there are no restrictions on the name that can be assigned to an application common user other than that it cannot start with the prefix reserved for CDB common users. For example, you could name a CDB common user `c##hr_admin` and an application common user `hr_admin`.
	The `COMMON_USER_PREFIX` parameter in `CDB$ROOT` defines the common user prefix. You can change this setting, but do so only with great care.
- For local user names, the name cannot start with `C##` (or `c##`).
- A user and a role cannot have the same name.

##### How the Multitenant Option Affects Password Files for Administrative Users

The password information for the local and common administrative users is stored in different locations.

- For CDB common administrative users: The password information (hashes of the password) for the CDB common administrative users to whom administrative privileges were granted in the CDB root is stored in the password file.
- For all users in a CDB to whom administrative privileges were granted outside the CDB root: To view information about the password hash information of these users, query the `$PWFILE_USERS` dynamic view.

#### Accessing a Container in a CDB

Access a container in a CDB with SQL\*Plus by issuing a `CONNECT` or `ALTER SESSION` command.

- Connecting to a Container Using the SQL\*Plus CONNECT Command  
	You can use the SQL\*Plus `CONNECT` command to connect to the root or to a PDB.
- Switching to a Container Using the ALTER SESSION Statement  
	When you are connected to a container as a common user, you can switch to a different container and application service using the `ALTER SESSION` statement.

**Parent topic:** Accessing Containers in a CDB

##### Connecting to a Container Using the SQL\*Plus CONNECT Command

You can use the SQL\*Plus `CONNECT` command to connect to the root or to a PDB.

- Connecting to the CDB Root Using the SQL\*Plus CONNECT Command  
	You can connect to the CDB root in several ways.
- Connecting to a PDB Using the SQL\*Plus CONNECT Command  
	To connect to a PDB with the SQL\*Plus `CONNECT` command, you can use easy connect or a net service name.

**Parent topic:** Accessing a Container in a CDB

###### Connecting to the CDB Root Using the SQL\*Plus CONNECT Command

You can connect to the CDB root in several ways.

Specifically, you can use the following techniques to connect to the root with the SQL\*Plus `CONNECT` command:

- Local connection
- Local connection with operating system authentication
- Database connection using easy connect
- Database connection using a net service name
- Remote database connection using external authentication

The following prerequisites must be met for the user connecting to the CDB root:

- The user must be a common user.
- The user must be granted `CREATE SESSION` privilege in the CDB root.

To connect to the root using the SQL\*Plus CONNECT command:

1. Configure your environment so that you can open SQL\*Plus.
2. Start SQL\*Plus with the `/NOLOG` argument:
	```
	sqlplus /nolog
	```
3. Issue a SQL\*Plus `CONNECT` command to connect to the root, as shown in the following examples.

Example 15-1 Connecting to the Root with a Local Connection

This example connects to the root in the local CDB as user `SYSTEM`. SQL\*Plus prompts for the `SYSTEM` user password.

```
connect system
```

Example 15-2 Connecting to the Root with Operating System Authentication

This example connects locally to the root with the `SYSDBA` administrative privilege with operating system authentication.

```
connect / as sysdba
```

Example 15-3 Connecting to the Root with a Net Service Name

Assume that clients are configured to have a net service name for the root in the CDB. For example, the net service name can be part of an entry in a `tnsnames.ora` file.

This example connects as common user `c##dba` to the database service designated by the net service name `mycdb`. SQL\*Plus prompts for the `c##dba` user password.

```
connect c##dba@mycdb
```

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-58A40F41-B611-4C0F-A6E3-D45A81515BF2) for information about submitting commands and SQL to the database

**Parent topic:** Connecting to a Container Using the SQL\*Plus CONNECT Command

###### Connecting to a PDB Using the SQL\*Plus CONNECT Command

To connect to a PDB with the SQL\*Plus `CONNECT` command, you can use easy connect or a net service name.

To connect to a PDB, a user must be one of the following:

- A common user with a `CREATE` `SESSION` privilege granted commonly or granted locally in the PDB
- A local user defined in the PDB with `CREATE` `SESSION` privilege

Only a user with `SYSDBA`, `SYSOPER`, `SYSBACKUP`, or `SYSDG` privilege can connect to a PDB that is in mounted mode. To change the open mode of a PDB, see " [Modifying the Open Mode of PDBs](administering-pdbs-with-sql-plus.md) ".

To connect to a PDB using the SQL\*Plus CONNECT command:

1. Configure your environment so that you can open SQL\*Plus.
2. Start SQL\*Plus with the `/NOLOG` argument:
	```
	sqlplus /nolog
	```
3. Issue a SQL\*Plus `CONNECT` command using easy connect or a net service name to connect to the PDB.

Example 15-4 Connecting to a PDB

Assume that clients are configured to have a net service name for each PDB that matches each PDB name. For example, the net service name can be part of an entry in a `tnsnames.ora` file.

The following command connects to the `sh` local user in the `salespdb` PDB:

```
CONNECT sh@salespdb
```

The following command connects to the `SYSTEM` common user in the `salespdb` PDB:

```
CONNECT system@salespdb
```

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-991445B9-EA9E-481E-A33D-E737F2DD9CFB) for information about submitting the SQL\*Plus `CONNECT` command

**Parent topic:** Connecting to a Container Using the SQL\*Plus CONNECT Command

##### Switching to a Container Using the ALTER SESSION Statement

When you are connected to a container as a common user, you can switch to a different container and application service using the `ALTER SESSION` statement.

You can use the following statement to switch to a different container and application service:

```
ALTER SESSION SET CONTAINER = container_name [SERVICE = service_name]
```

For container\_name, specify one of the following:

- `CDB$ROOT` to switch to the CDB root
- `PDB$SEED` to switch to the PDB seed
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

By default, when you switch to a container, the session uses the default service for the container. However, the default PDB service does not support all service attributes and features such as service metrics, Fast Application Notification (FAN), load balancing, Resource Manager, Transaction Guard, Application Continuity, and so on. It is best practice to use a nondefault service for the container by specifying `SERVICE = service_name`, where service\_name is the name of the service.

With this new capability, connection pools can switch the service, and, when needed the PDB, on a connection when a connection is borrowed from the pool. Starting with Oracle Database 12c Release 2 (12.2.0.1), connection pools support more than one database service with universal connection pools (UCPs). It can also be used standalone.

When switching to a service, applications can consolidate to a CDB, while keeping the database services identified, prioritized, measured, and highly available. Switching to a nondefault service provides the following benefits:

- It preserves the service attributes and features.
- It eliminates too many connection pools with too many connections serving these tenants.
- It allows applications to use more database services for workload control without consuming too many connection pools. Customers can identify and prioritize workloads using services without over sizing the database connections.

The following are considerations for using the `ALTER SESSION SET CONTAINER` statement:

- After the statement completes successfully, the current schema of the session is set to the schema owned by the common user in the specified container.
- After the statement completes successfully, the security context is reset to that of the schema owned by the common user in the specified container.
- After the statement completes successfully, login triggers for the specified container do not fire.
	If you require a trigger, then you can define a before or after `SET CONTAINER` trigger in a PDB to fire before or after the `ALTER SESSION SET CONTAINER` statement is executed.
- After the statement completes successfully and the `SERVICE` clause specifies a nondefault service for the PDB, the session is using a new service with attributes set, including metrics, FAN, TAF, Application Continuity, Transaction Guard, `drain_timeout`, and `stop_option` for the new service.
- Package states are not shared across containers.
- When closing a PDB, sessions that switched into the PDB and sessions that connected directly to the PDB are handled identically.
- A transaction cannot span multiple containers. If you start a transaction and use `ALTER` `SESSION` `SET` `CONTAINER` to switch to a different container, then you cannot issue DML, DDL, `COMMIT`, or `ROLLBACK` statements until you switch back to the container in which you started the transaction.
- If you open a cursor and use `ALTER SESSION SET CONTAINER` to switch to different container, then you cannot fetch data from that cursor until you switch back to the container in which the cursor was opened.
- You can use the `ALTER SESSION SET CONTAINER` statement with the `SERVICE` clause for connection pooling as well as advanced CDB administration.
	For example, you can use this statement for connection pooling with PDBs for a multitenant application. A multitenant application uses a single instance of the software on a server to serve multiple customers (tenants). In a CDB, each tenant can have its own PDB. You can use the `ALTER SESSION SET CONTAINER` statement in a connection pooling configuration.
- When working with connection pools that serve applications, the applications may be using data sources with different services. Using the `ALTER SESSION SET CONTAINER` statement with the `SERVICE` clause enables the connection pool to use the same connections for many applications, sharing the services.

The following prerequisites must be met to use the `ALTER SESSION SET CONTAINER` statement:

- The current user must be a common user. The initial connection must be made using the SQL\*Plus `CONNECT` command.
- When altering a session to switch to a PDB as a common user that was not supplied with Oracle Database, the current user must be granted the `SET` `CONTAINER` privilege commonly or must be granted this privilege locally in the PDB.

Note:

When an `ALTER SESSION SET CONTAINER` statement is used to switch to the current container, these prerequisites are not enforced, and no error message is returned if they are not met.

Before issuing an `ALTER SESSION SET CONTAINER` statement with the `SERVICE` clause, the following prerequisites must be met:

- The service switched to must be active. You cannot switch to a service that is not running.
- When switching between services, the service attributes of the service being switched from and the service being switched to must match. For example, the services switched from and to must all have TAF, or must all use Application Continuity, or must all have `drain_timeout` set.

To switch to a container using the ALTER SESSION statement:

1. In SQL\*Plus, connect to a container as a common user with the required privileges.
2. Check the current open mode of the container to which you are switching.
	To check the current open mode of the root or a PDB, query the `OPEN_MODE` column in the `V$CONTAINERS` view when the current container is the root.
	If the open mode of the root should be changed, then follow the instructions in [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-2042AAE4-DAE5-4CD4-89E9-B9DE3A8A2AA1) about altering database availability to change the open mode.
	If the open mode of the PDB should be changed, then follow the instructions in " [Modifying the Open Mode of PDBs](administering-pdbs-with-sql-plus.md) " to change the open mode.
	The open mode of the root imposes limitations on the open mode of PDBs. For example, the root must be open before any PDBs can be open. Therefore, you might need to change the open mode of the root before changing the open mode of a PDB.
3. If you are switching to a specific service, then ensure that the service is running.
	To check the active status of the service, query the `V$ACTIVE_SERVICES` view when the current container is the CDB root.
	If the service is not running, then use the SRVCTL utility or the `DBMS_SERVICE` package to start the service.
4. Run the `ALTER SESSION SET CONTAINER` statement and specify the container to which you want to switch.
	Include the `SERVICE` clause to switch to a specific application service.

The following examples switch to various containers using `ALTER` `SESSION`.

Example 15-5 Switching to the PDB salespdb and Using the salesrep Service

```
ALTER SESSION SET CONTAINER = salespdb SERVICE = salesrep;
```

Example 15-6 Switching to the PDB salespdb and Using the Default Service

```
ALTER SESSION SET CONTAINER = salespdb;
```

Example 15-7 Switching to the CDB Root

```
ALTER SESSION SET CONTAINER = CDB$ROOT;
```

Example 15-8 Switching to the PDB Seed

```
ALTER SESSION SET CONTAINER = PDB$SEED;
```

Example 15-9 Switching Services Using a Dummy Service in the CDB Root

To design connection pooling that switches the container and the service, one method is to create a dummy service in the CDB root and set all required service attributes on this dummy service (for example, `drain_timeout`, TAF or Application Continuity). The service attributes must match across the CDB root and the PDB. To use this method, complete the following steps:

1. Connect to the dummy service when first creating the connection pool and when creating new connections.
2. As services are added to each PDB, set the same attributes on these real services.
3. When an application requires a connection, complete one of the following actions:
	- Create a new connection to the dummy service, and switch to the PDB and service.
		- Borrow a free connection in the pool and switch to the PDB and service.
		You do not need to return to the CDB root when switching across PDBs.

You do not need to return to the CDB root when switching across PDBs.

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-BB76E57C-3F16-4C85-AEF6-BA14FC1B4777) for information about database resident connection pooling

**Parent topic:** Accessing a Container in a CDB

### Starting Up and Shutting Down a CDB

When you start up a CDB, you create an instance and then determine the state of the CDB. Shutting down a currently running Oracle Database instance can optionally close and dismount a CDB.

- Starting Up a CDB  
	When you start up a CDB, you create an instance of that database and you determine the state of the database.
- Altering Database Availability  
	You can alter the availability of a database. You may want to do this in order to restrict access for maintenance reasons or to make the database read only.
- Shutting Down a CDB  
	You can shut down a CDB with SQL\*Plus or Oracle Restart.
- Quiescing a CDB  
	A quiesced CDB allows only DBA transactions, queries, fetches, or PL/SQL statements.
- Suspending and Resuming a Database  
	The `ALTER SYSTEM SUSPEND` statement halts all input and output (I/O) to data files (file header and file data) and control files. The suspended state lets you back up a database without I/O interference. When the database is suspended all preexisting I/O operations are allowed to complete and any new database accesses are placed in a queued state. Use the `ALTER SYSTEM RESUME` statement to resume normal database operations.
- Delaying Instance Abort  
	The `INSTANCE_ABORT_DELAY_TIME` initialization parameter specifies the amount of time, in seconds, to delay shutting down a database when an error causes the instance to abort.

See Also:

[Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=RACAD801) for additional information specific to an Oracle Real Application Clusters environment

**Parent topic:** Administering a CDB

#### Starting Up a CDB

When you start up a CDB, you create an instance of that database and you determine the state of the database.

Normally, you start up an instance by mounting and opening the CDB. This operation makes the CDB available for any valid user to connect to and perform typical data access operations.

- About Database Startup Options  
	When Oracle Restart is not in use, you can start up a database instance with SQL\*Plus, Recovery Manager, or Oracle Enterprise Manager Cloud Control (Cloud Control). If your database is being managed by Oracle Restart, then Oracle recommends starting the database with SRVCTL.
- Specifying Initialization Parameters at Startup  
	To start a database instance, the CDB must read instance configuration parameters (the initialization parameters) from either a server parameter file (`SPFILE`) or a text initialization parameter file (PFILE).
- About Automatic Startup of Database Services  
	When your database is managed by Oracle Restart, you can configure startup options for each individual database service (service).
- Preparing to Start Up an Instance  
	You must perform some preliminary steps before attempting to start an instance of your CDB using SQL\*Plus.
- Starting Up an Instance  
	You can start up an instance using SQL\*Plus or Oracle Restart.

**Parent topic:** Starting Up and Shutting Down a CDB

##### About Database Startup Options

When Oracle Restart is not in use, you can start up a database instance with SQL\*Plus, Recovery Manager, or Oracle Enterprise Manager Cloud Control (Cloud Control). If your database is being managed by Oracle Restart, then Oracle recommends starting the database with SRVCTL.

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-5832E064-85C6-453C-B932-99700B1732A9) for information about Oracle Restart

- Starting Up a Database Using SQL\*Plus  
	You can start a SQL\*Plus session, connect to Oracle Database with administrator privileges, and then issue the `STARTUP` command. Using SQL\*Plus in this way is the only method described in detail in this book.
- Starting Up a Database Using Recovery Manager  
	You can also use Recovery Manager (RMAN) to execute `STARTUP` and `SHUTDOWN` commands. You may prefer to do this if your are within the RMAN environment and do not want to invoke SQL\*Plus.
- Starting Up a Database Using Cloud Control  
	You can use Cloud Control to administer your database, including starting it up and shutting it down. Cloud Control combines a GUI console, agents, common services, and tools to provide an integrated and comprehensive systems management platform for managing Oracle products. Cloud Control enables you to perform the functions discussed in this book using a GUI interface, rather than command line operations.
- Starting Up a Database Using SRVCTL  
	When Oracle Restart is installed and configured for your database, Oracle recommends that you use SRVCTL to start the database.

**Parent topic:** Starting Up a CDB

###### Starting Up a Database Using SQL\*Plus

You can start a SQL\*Plus session, connect to Oracle Database with administrator privileges, and then issue the `STARTUP` command. Using SQL\*Plus in this way is the only method described in detail in this book.

- Run the SQL\*Plus `STARTUP` command.

###### Starting Up a Database Using Recovery Manager

You can also use Recovery Manager (RMAN) to execute `STARTUP` and `SHUTDOWN` commands. You may prefer to do this if your are within the RMAN environment and do not want to invoke SQL\*Plus.

- Run an RMAN `STARTUP` command.

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=RCMRF158) for information about the RMAN `STARTUP` command

**Parent topic:** About Database Startup Options

###### Starting Up a Database Using Cloud Control

You can use Cloud Control to administer your database, including starting it up and shutting it down. Cloud Control combines a GUI console, agents, common services, and tools to provide an integrated and comprehensive systems management platform for managing Oracle products. Cloud Control enables you to perform the functions discussed in this book using a GUI interface, rather than command line operations.

- In Cloud Control, start the database instance.

See Also:

The Cloud Control online help

**Parent topic:** About Database Startup Options

###### Starting Up a Database Using SRVCTL

When Oracle Restart is installed and configured for your database, Oracle recommends that you use SRVCTL to start the database.

Starting the database instance with SRVCTL ensures that:

- Any components on which the database depends (such as Oracle Automatic Storage Management and the Oracle Net listener) are automatically started first, and in the proper order.
- The database is started according to the settings in its Oracle Restart configuration. An example of such a setting is the server parameter file location.
- Environment variables stored in the Oracle Restart configuration for the database are set before starting the instance.

To start a database instance with SRVCTL:

- Run the `srvctl start database` command.

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-08ABD19E-3DBA-4467-BAF2-42C008ABB2B3) to learn more about `srvctl start database`

**Parent topic:** About Database Startup Options

##### Specifying Initialization Parameters at Startup

To start a database instance, the CDB must read instance configuration parameters (the initialization parameters) from either a server parameter file (`SPFILE`) or a text initialization parameter file (PFILE).

The CDB looks for these files in a default location. You can specify nondefault locations for these files, and the method for doing so depends on whether you start the database with SQL\*Plus (when Oracle Restart is not in use) or with SRVCTL (when the database is being managed with Oracle Restart).

- About Initialization Parameter Files and Startup  
	When you start the database instance, it attempts to read the initialization parameters from an `SPFILE` in a platform-specific default location. If it finds no `SPFILE`, then it searches for a text initialization parameter file.
- Starting Up with SQL\*Plus with a Nondefault Server Parameter File  
	With SQL\*Plus, you can use the `PFILE` clause to start an instance with a nondefault server parameter file.
- Starting Up with SRVCTL with a Nondefault Server Parameter File  
	If your database is being managed by Oracle Restart, then you can specify the location of a nondefault SPFILE by setting or modifying the SPFILE location option in the Oracle Restart configuration for the database.

See Also:

" [Creating a CDB: Basic Steps](creating-and-configuring-an-oracle-database.md) " for more information about initialization parameters, initialization parameter files, and server parameter files

**Parent topic:** Starting Up a CDB

###### About Initialization Parameter Files and Startup

When you start the database instance, it attempts to read the initialization parameters from an `SPFILE` in a platform-specific default location. If it finds no `SPFILE`, then it searches for a text initialization parameter file.

In the platform-specific default location, Oracle Database locates your initialization parameter file by examining file names in the following order:

1. The location specified by the `-spfile` option in the SRVCTL commands `srvctl add database` or `srvctl modify database`
	You can check the current setting with the `srvctl config database` command.
2. `spfile` `ORACLE_SID`.`ora`
3. `spfile.ora`
4. `init` `ORACLE_SID`.`ora`

The first three files are `SPFILE` s and the fourth is a text initialization parameter file. If DBCA created the SPFILE in an Oracle Automatic Storage Management disk group, then the database searches for the SPFILE in the disk group.

When `AS COPY` is not specified in a `CREATE SPFILE` statement and the database is defined as a resource in Oracle Clusterware, if you specify both the `spfile_name` and the `FROM PFILE` clause, then this statement automatically updates the SPFILE name and location in the database resource. When `AS COPY` is specified in a `CREATE SPFILE` statement, the SPFILE is copied, and the database resource is not updated.

Note:

The `spfile.ora` file is included in this search path because in an Oracle Real Application Clusters environment one server parameter file is used to store the initialization parameter settings for all instances. There is no instance-specific location for storing a server parameter file.

If you (or the Database Configuration Assistant) created a server parameter file, but you want to override it with a text initialization parameter file, then you can do so with SQL\*Plus, specifying the `PFILE` clause of the `STARTUP` command to identify the initialization parameter file:

```
STARTUP PFILE = /u01/oracle/dbs/init.ora
```

Nondefault Server Parameter Files

A nondefault server parameter file (`SPFILE`) is an `SPFILE` that is in a location other than the default location. It is not usually necessary to start an instance with a nondefault `SPFILE`. However, should such a need arise, both SRVCTL (with Oracle Restart) and SQL\*Plus provide ways to do so. These are described later in this section.

Initialization Files and Oracle Automatic Storage Management

A database that uses Oracle Automatic Storage Management (Oracle ASM) usually has a nondefault `SPFILE`. If you use the Database Configuration Assistant (DBCA) to configure a database to use Oracle ASM, DBCA creates an `SPFILE` for the database instance in an Oracle ASM disk group, and then causes a text initialization parameter file (PFILE) to be created in the default location in the local file system to point to the `SPFILE`, as explained in the next section.

See Also:

- " [Table 4-1](create-cdb-adv.md) " lists PFILE and SPFILE default names and locations.
- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=RACAD020) for more information about the server parameter file for an Oracle Real Application Clusters environment
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-B2D64FD5-0DE7-4201-AB0F-3941955CADB8) for the SRVCTL Command Reference for Oracle Restart

**Parent topic:** Specifying Initialization Parameters at Startup

###### Starting Up with SQL\*Plus with a Nondefault Server Parameter File

With SQL\*Plus, you can use the `PFILE` clause to start an instance with a nondefault server parameter file.

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

**Parent topic:** Specifying Initialization Parameters at Startup

###### Starting Up with SRVCTL with a Nondefault Server Parameter File

If your database is being managed by Oracle Restart, then you can specify the location of a nondefault SPFILE by setting or modifying the SPFILE location option in the Oracle Restart configuration for the database.

To start up with SRVCTL with a nondefault server parameter file:

1. Prepare to run SRVCTL as described in [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-BAA85F03-7A2B-40F7-BC4C-774D47EF7605).
2. ```
	srvctl modify database -db db_unique_name -spfile spfile_path
	```
	where `db_unique_name` must match the `DB_UNIQUE_NAME` initialization parameter setting for the database.
3. ```
	srvctl start database -db db_unique_name [options]
	```

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-B2D64FD5-0DE7-4201-AB0F-3941955CADB8) for the SRVCTL Command Reference for Oracle Restart

**Parent topic:** Specifying Initialization Parameters at Startup

##### About Automatic Startup of Database Services

When your database is managed by Oracle Restart, you can configure startup options for each individual database service (service).

If you set the management policy for a service to `AUTOMATIC` (the default), the service starts automatically when you start the database with SRVCTL. If you set the management policy to `MANUAL`, the service does not automatically start, and you must manually start it with SRVCTL. A `MANUAL` setting does not prevent Oracle Restart from monitoring the service when it is running and restarting it if a failure occurs.

In an Oracle Data Guard (Data Guard) environment in which databases are managed by Oracle Restart, you can additionally control automatic startup of services by assigning Data Guard roles to the services in their Oracle Restart configurations. A service automatically starts upon manual database startup only if the management policy of the service is `AUTOMATIC` and if one of its assigned roles matches the current role of the database.

Note:

When using Oracle Restart, Oracle strongly recommends that you use SRVCTL to create database services.

See Also:

[srvctl add service](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-802E24A9-F823-4942-804E-0ABBD97943D1) and [srvctl modify service](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-45A7239E-B588-404E-A831-E62541092AE9) in Oracle Database Administrator’s Guide for the syntax for setting the management policy of and Data Guard roles for a service

**Parent topic:** Starting Up a CDB

##### Preparing to Start Up an Instance

You must perform some preliminary steps before attempting to start an instance of your CDB using SQL\*Plus.

Note:

The following instructions are for installations where Oracle Restart is not in use.

To prepare for starting an instance:

1. Ensure that any Oracle components on which the database depends are started.
	For example, if the CDB stores data in Oracle Automatic Storage Management (Oracle ASM) disk groups, ensure that the Oracle ASM instance is running and the required disk groups are mounted. Also, it is preferable to start the Oracle Net listener before starting the CDB.
2. If you intend to use operating system authentication, log in to the database host computer as a member of the OSDBA group.
3. Ensure that environment variables are set so that you connect to the desired Oracle instance.
4. Start SQL\*Plus without connecting to the CDB root:
	```
	SQLPLUS /NOLOG
	```
5. Connect to the CDB root as `SYSOPER`, `SYSDBA`, `SYSBACKUP`, or `SYSDG`. For example:
	```
	CONNECT username AS SYSDBA
	—or—
	CONNECT / AS SYSDBA
	```

Now you are connected to the CDB root and ready to start up an instance of your database.

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-BB22E256-CC25-405F-A887-E3FA92CC37D4) to learn about operating system authentication
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-58A40F41-B611-4C0F-A6E3-D45A81515BF2) for information about setting environment variables to connect to an Oracle instance
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-EA0104A2-B256-4866-9C8A-9B69F8D0F24E) if your database is being managed by Oracle Restart
- [SQL\*Plus User's Guide and Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQPUG-GUID-71DD7D4A-70C1-4E39-9AF8-20AC54928540) for descriptions and syntax for the `CONNECT`, `STARTUP`, and `SHUTDOWN` commands

**Parent topic:** Starting Up a CDB

##### Starting Up an Instance

You can start up an instance using SQL\*Plus or Oracle Restart.

- About Starting Up an Instance  
	When Oracle Restart is not in use, you use the SQL\*Plus `STARTUP` command to start up an Oracle Database instance. If your database is being managed by Oracle Restart, Oracle recommends that you use the `srvctl start database` command.
- Starting an Instance, and Mounting and Opening a Database  
	Normal database operation means that an instance is started and the database is mounted and open. This mode allows any valid user to connect to the database and perform data access operations.
- Starting an Instance Without Mounting a Database  
	You can start an instance without mounting a database. Typically, you do so only during database creation.
- Starting an Instance and Mounting a Database  
	You can start an instance and mount a CDB without opening it, allowing you to perform specific maintenance operations.
- Restricting Access to an Instance at Startup  
	You can start an instance, and optionally mount and open a database, in restricted mode so that the instance is available only to administrative personnel (not general database users).
- Forcing an Instance to Start  
	In unusual circumstances, you might experience problems when attempting to start a database instance, and you can force a database instance to start.
- Starting an Instance, Mounting a Database, and Starting Complete Media Recovery  
	If you know that media recovery is required, then you can start an instance, mount a database to the instance, and have the recovery process automatically start.
- Automatic Database Startup at Operating System Start  
	Many sites use procedures to enable automatic startup of one or more Oracle Database instances and databases immediately following a system start.
- Starting Remote Instances  
	If your local Oracle Database server is part of a distributed database, then you might want to start a remote instance and database.

**Parent topic:** Starting Up a CDB

###### About Starting Up an Instance

When Oracle Restart is not in use, you use the SQL\*Plus `STARTUP` command to start up an Oracle Database instance. If your database is being managed by Oracle Restart, Oracle recommends that you use the `srvctl start database` command.

With SQL\*Plus and Oracle Restart, you can start a database instance in various modes:

- `NOMOUNT` —Start the instance without mounting a CDB. This does not allow access to the database and usually would be done only for database creation or the re-creation of control files.
- `MOUNT` —Start the instance and mount the CDB, but leave it closed. This state allows for certain DBA activities, but does not allow general access to the database.
- `OPEN` —Start the instance, and mount and open the CDB. This can be done in unrestricted mode, allowing access to all users, or in restricted mode, allowing access for database administrators only.
- `FORCE` —Force the instance to start after a startup or shutdown problem.
- `OPEN RECOVER` —Start the instance and have complete media recovery begin immediately.

Note:

You cannot start a database instance if you are connected to the database through a shared server process.

The following scenarios describe and illustrate the various states in which you can start up an instance. Some restrictions apply when combining clauses of the `STARTUP` command or combining startup options for the `srvctl start database` command.

Note:

It is possible to encounter problems starting up an instance if control files, database files, or online redo logs are not available. If one or more of the files specified by the `CONTROL_FILES` initialization parameter does not exist or cannot be opened when you attempt to mount a database, Oracle Database returns a warning message and does not mount the database. If one or more of the data files or online redo logs is not available or cannot be opened when attempting to open a database, the database returns a warning message and does not open the database.

See Also:

- [SQL\*Plus User's Guide and Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQPUG127) for details on the `STARTUP` command syntax
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-EA0104A2-B256-4866-9C8A-9B69F8D0F24E) for instructions for starting a database that is managed by Oracle Restart

**Parent topic:** Starting Up an Instance

###### Starting an Instance, and Mounting and Opening a Database

Normal database operation means that an instance is started and the database is mounted and open. This mode allows any valid user to connect to the database and perform data access operations.

The following command starts an instance, reads the initialization parameters from the default location, and then mounts and opens the database.

| SQL\*Plus | SRVCTL (When Oracle Restart Is In Use) |
| --- | --- |
| ``` STARTUP ``` | ``` srvctl start database -db db_unique_name ``` |

where `db_unique_name` matches the `DB_UNIQUE_NAME` initialization parameter.

**Parent topic:** Starting Up an Instance

###### Starting an Instance Without Mounting a Database

You can start an instance without mounting a database. Typically, you do so only during database creation.

Use one of the following commands:

| SQL\*Plus | SRVCTL (When Oracle Restart Is In Use) |
| --- | --- |
| ``` STARTUP NOMOUNT ``` | ``` srvctl start database -db db_unique_name -startoption nomount ``` |

**Parent topic:** Starting Up an Instance

###### Starting an Instance and Mounting a Database

You can start an instance and mount a CDB without opening it, allowing you to perform specific maintenance operations.

For example, the CDB must be mounted but not open during the following tasks:

- Starting with Oracle Database 12c Release 1 (12.1.0.2), putting a database instance in force full database caching mode. For more information, see [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-CEBDCC3D-4B69-43C1-A7BE-F635F9F69D5F).
- Enabling and disabling redo log archiving options. For more information, see [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-5EE4AC49-E1B2-41A2-BEE7-AA951EAAB2F3).
- Performing full database recovery. For more information, see [Oracle Database Backup and Recovery User’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=BRADV8005).

The following command starts an instance and mounts the database, but leaves the database closed:

| SQL\*Plus | SRVCTL (When Oracle Restart Is In Use) |
| --- | --- |
| ``` STARTUP MOUNT ``` | ``` srvctl start database -db db_unique_name -startoption mount ``` |

**Parent topic:** Starting Up an Instance

###### Restricting Access to an Instance at Startup

You can start an instance, and optionally mount and open a database, in restricted mode so that the instance is available only to administrative personnel (not general database users).

Use this mode of instance startup when you must accomplish one of the following tasks:

- Perform an export or import of data
- Perform a data load (with SQL\*Loader)
- Temporarily prevent typical users from using data
- Perform certain migration or upgrade operations

Typically, all users with the `CREATE SESSION` system privilege can connect to an open database. Opening a database in restricted mode allows database access only to users with both the `CREATE SESSION` and `RESTRICTED SESSION` system privilege. Only database administrators should have the `RESTRICTED SESSION` system privilege. Further, when the instance is in restricted mode, a database administrator cannot access the instance remotely through an Oracle Net listener, but can only access the instance locally from the system that the instance is running on.

The following command starts an instance (and mounts and opens the database) in restricted mode:

| SQL\*Plus | SRVCTL (When Oracle Restart Is In Use) |
| --- | --- |
| ``` STARTUP RESTRICT ``` | ``` srvctl start database -db db_unique_name -startoption restrict ``` |

You can use the restrict mode in combination with the mount, nomount, and open modes.

Later, use the `ALTER SYSTEM` statement to disable the `RESTRICTED SESSION` feature:

```
ALTER SYSTEM DISABLE RESTRICTED SESSION;
```

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-989D380B-A4BE-43D2-B687-C68EDA7F69A5) to learn how to use the `ALTER SYSTEM` statement to restrict access after you open the database in nonrestricted mode
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF53082) for more information on the `ALTER SYSTEM` statement

**Parent topic:** Starting Up an Instance

###### Forcing an Instance to Start

In unusual circumstances, you might experience problems when attempting to start a database instance, and you can force a database instance to start.

You should not force a database to start unless you are faced with the following:

- You cannot shut down the current instance with the `SHUTDOWN NORMAL`, `SHUTDOWN IMMEDIATE`, or `SHUTDOWN TRANSACTIONAL` commands.
- You experience problems when starting an instance.

If one of these situations arises, you can usually solve the problem by starting a new instance (and optionally mounting and opening the database) using one of these commands:

| SQL\*Plus | SRVCTL (When Oracle Restart Is In Use) |
| --- | --- |
| ``` STARTUP FORCE ``` | ``` srvctl start database -db db_unique_name -startoption force ``` |

If an instance is running, the force mode shuts it down with mode `ABORT` before restarting it. In this case, the alert log shows the message " `Shutting down instance (abort)` " followed by " `Starting ORACLE instance (normal)`."

See Also:

" Shutting Down with the Abort Mode " to understand the side effects of aborting the current instance

**Parent topic:** Starting Up an Instance

###### Starting an Instance, Mounting a Database, and Starting Complete Media Recovery

If you know that media recovery is required, then you can start an instance, mount a database to the instance, and have the recovery process automatically start.

To do so, use one of these commands:

| SQL\*Plus | SRVCTL (When Oracle Restart Is In Use) |
| --- | --- |
| ``` STARTUP OPEN RECOVER ``` | ``` srvctl start database -db db_unique_name -startoption "open,recover" ``` |

If you attempt to perform recovery when no recovery is required, Oracle Database issues an error message.

**Parent topic:** Starting Up an Instance

###### Automatic Database Startup at Operating System Start

Many sites use procedures to enable automatic startup of one or more Oracle Database instances and databases immediately following a system start.

The procedures for performing this task are specific to each operating system. For information about automatic startup, see your operating system specific Oracle documentation.

The preferred (and platform-independent) method of configuring automatic startup of a database is Oracle Restart.

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-5832E064-85C6-453C-B932-99700B1732A9) to learn about Oracle Restart

**Parent topic:** Starting Up an Instance

###### Starting Remote Instances

If your local Oracle Database server is part of a distributed database, then you might want to start a remote instance and database.

Procedures for starting and stopping remote instances vary widely depending on communication protocol and operating system.

**Parent topic:** Starting Up an Instance

#### Altering Database Availability

You can alter the availability of a database. You may want to do this in order to restrict access for maintenance reasons or to make the database read only.

- Mounting a Database to an Instance  
	When you perform specific administrative operations, the database must be started and mounted to an instance, but closed. You can achieve this scenario by starting the instance and mounting the database.
- Opening a Closed Database  
	When a database is mounted but closed, you can make it available for general use by opening it.
- Opening a Database in Read-Only Mode  
	Opening a database in read-only mode enables you to query an open database while eliminating any potential for online data content changes.
- Restricting Access to an Open Database  
	When a database is in restricted mode, only users with the `RESTRICTED SESSION` privilege can initiate new connections. Users connecting as `SYSDBA` or connecting with the `DBA` role have this privilege.

**Parent topic:** Starting Up and Shutting Down a CDB

##### Mounting a Database to an Instance

When you perform specific administrative operations, the database must be started and mounted to an instance, but closed. You can achieve this scenario by starting the instance and mounting the database.

- To mount a database to a previously started, but not opened instance, use the SQL statement `ALTER DATABASE` with the `MOUNT` clause as follows:
	```
	ALTER DATABASE MOUNT;
	```

See Also:

" Starting an Instance and Mounting a Database " for a list of operations that require the database to be mounted and closed (and procedures to start an instance and mount a database in one step)

**Parent topic:** Altering Database Availability

##### Opening a Closed Database

When a database is mounted but closed, you can make it available for general use by opening it.

- To open a mounted database, use the `ALTER DATABASE` SQL statement with the `OPEN` clause:
	```
	ALTER DATABASE OPEN;
	```

After executing this statement, any valid Oracle Database user with the `CREATE SESSION` system privilege can connect to the database.

**Parent topic:** Altering Database Availability

##### Opening a Database in Read-Only Mode

Opening a database in read-only mode enables you to query an open database while eliminating any potential for online data content changes.

While opening a database in read-only mode guarantees that data files and redo log files are not written to, it does not restrict database recovery or operations that change the state of the database without generating redo. For example, you can take data files offline or bring them online since these operations do not affect data content.

If a query against a database in read-only mode uses temporary tablespace, for example to do disk sorts, then the issuer of the query must have a locally managed tablespace assigned as the default temporary tablespace. Otherwise, the query will fail.

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
- You cannot invoke a remote procedure (even a read-only remote procedure) from a read-only database if the remote procedure has never been called on the database. This limitation applies to remote procedure calls in anonymous PL/SQL blocks and in SQL statements. You can either put the remote procedure call in a stored procedure, or you can invoke the remote procedure in the database before it becomes read only.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF008) for more information about the `ALTER DATABASE` statement

**Parent topic:** Altering Database Availability

##### Restricting Access to an Open Database

When a database is in restricted mode, only users with the `RESTRICTED SESSION` privilege can initiate new connections. Users connecting as `SYSDBA` or connecting with the `DBA` role have this privilege.

To place an already running instance in restricted mode:

- Run the SQL statement `ALTER SYSTEM` with the `ENABLE RESTRICTED SESSION` clause.

When you place a running instance in restricted mode, no user sessions are terminated or otherwise affected. Therefore, after placing an instance in restricted mode, consider killing (terminating) all current user sessions before performing administrative tasks.

To lift an instance from restricted mode, use `ALTER SYSTEM` with the `DISABLE RESTRICTED SESSION` clause.

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-260EE1DC-D306-4B4E-B848-A94DA2F46615) for directions for killing user sessions
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-7A570C5F-BCBB-49A4-9586-270ED9DE2079) to learn some reasons for placing an instance in restricted mode

**Parent topic:** Altering Database Availability

#### Shutting Down a CDB

You can shut down a CDB with SQL\*Plus or Oracle Restart.

- About Shutting Down the Database  
	When Oracle Restart is not in use, you can shut down a database instance with SQL\*Plus by connecting as `SYSOPER`, `SYSDBA`, `SYSBACKUP`, or `SYSDG` and issuing the `SHUTDOWN` command. If your database is being managed by Oracle Restart, the recommended way to shut down the database is with the `srvctl stop database` command.
- Shutting Down with the Normal Mode  
	When you shut down a database with the normal mode, the database waits for all connected users to disconnect before shutting down. Normal mode is the default mode of shutdown.
- Shutting Down with the Immediate Mode  
	When you shut down a database with the immediate mode, Oracle Database terminates any executing SQL statements and disconnects users. Active transactions are terminated and uncommitted changes are rolled back.
- Shutting Down with the Transactional Mode  
	When you shut down a database with transactional mode, the database prevents users from starting new transactions, but waits for all current transactions to complete before shutting down. This mode can take a significant amount of time depending on the nature of the current transactions.
- Shutting Down with the Abort Mode  
	You can shut down a database instantaneously by aborting the database instance.
- Shutdown Timeout  
	Shutdown modes that wait for users to disconnect or for transactions to complete have a limit on the amount of time that they wait.

**Parent topic:** Starting Up and Shutting Down a CDB

##### About Shutting Down the Database

When Oracle Restart is not in use, you can shut down a database instance with SQL\*Plus by connecting as `SYSOPER`, `SYSDBA`, `SYSBACKUP`, or `SYSDG` and issuing the `SHUTDOWN` command. If your database is being managed by Oracle Restart, the recommended way to shut down the database is with the `srvctl stop database` command.

Control is not returned to the session that initiates a database shutdown until shutdown is complete. Users who attempt connections while a shutdown is in progress receive a message like the following:

```
ORA-01090: shutdown in progress - connection is not permitted
```

Note:

You cannot shut down a database if you are connected to the database through a shared server process.

There are several modes for shutting down a database: normal, immediate, transactional, and abort. Some shutdown modes wait for certain events to occur (such as transactions completing or users disconnecting) before actually bringing down the database. There is a one-hour timeout period for these events.

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-5832E064-85C6-453C-B932-99700B1732A9) for information about Oracle Restart

**Parent topic:** Shutting Down a CDB

##### Shutting Down with the Normal Mode

When you shut down a database with the normal mode, the database waits for all connected users to disconnect before shutting down. Normal mode is the default mode of shutdown.

To shut down a database in normal situations, use one of these commands:

| SQL\*Plus | SRVCTL (When Oracle Restart Is In Use) |
| --- | --- |
| ``` SHUTDOWN [NORMAL] ``` | ``` srvctl stop database -db db_unique_name -stopoption normal ``` |

The `NORMAL` clause of the SQL\*Plus `SHUTDOWN` command is optional because this is the default shutdown method. For SRVCTL, if the `-stopoption` option is omitted, the shutdown operation proceeds according to the stop options stored in the Oracle Restart configuration for the database. The default stop option is `immediate`.

Normal database shutdown proceeds with the following conditions:

- No new connections are allowed after the statement is issued.
- Before the database is shut down, the database waits for all currently connected users to disconnect from the database.

The next startup of the database will not require any instance recovery procedures.

**Parent topic:** Shutting Down a CDB

##### Shutting Down with the Immediate Mode

When you shut down a database with the immediate mode, Oracle Database terminates any executing SQL statements and disconnects users. Active transactions are terminated and uncommitted changes are rolled back.

Use immediate database shutdown only in the following situations:

- To initiate an automated and unattended backup
- When a power shutdown is going to occur soon
- When the database or one of its applications is functioning irregularly and you cannot contact users to ask them to log off or they are unable to log off

To shut down a database immediately, use one of the following commands:

| SQL\*Plus | SRVCTL (When Oracle Restart Is In Use) |
| --- | --- |
| ``` SHUTDOWN IMMEDIATE ``` | ``` srvctl stop database -db db_unique_name -stopoption immediate ``` |

Immediate database shutdown proceeds with the following conditions:

- No new connections are allowed, nor are new transactions allowed to be started, after the statement is issued.
- Any uncommitted transactions are rolled back. (If long uncommitted transactions exist, this method of shutdown might not complete quickly, despite its name.)
- Oracle Database does not wait for users currently connected to the database to disconnect. The database implicitly rolls back active transactions and disconnects all connected users.

The next startup of the database will not require any instance recovery procedures.

**Parent topic:** Shutting Down a CDB

##### Shutting Down with the Transactional Mode

When you shut down a database with transactional mode, the database prevents users from starting new transactions, but waits for all current transactions to complete before shutting down. This mode can take a significant amount of time depending on the nature of the current transactions.

When you want to perform a planned shutdown of an instance while allowing active transactions to complete first, use one of the following commands:

| SQL\*Plus | SRVCTL (When Oracle Restart Is In Use) |
| --- | --- |
| ``` SHUTDOWN TRANSACTIONAL ``` | ``` srvctl stop database -db db_unique_name -stopoption transactional ``` |

Transactional database shutdown proceeds with the following conditions:

- No new connections are allowed, nor are new transactions allowed to be started, after the statement is issued.
- After all transactions have completed, any client still connected to the instance is disconnected.
- At this point, the instance shuts down just as it would when a `SHUTDOWN IMMEDIATE` statement is submitted.

The next startup of the database will not require any instance recovery procedures.

A transactional shutdown prevents clients from losing work, and at the same time, does not require all users to log off.

**Parent topic:** Shutting Down a CDB

##### Shutting Down with the Abort Mode

You can shut down a database instantaneously by aborting the database instance.

If possible, perform this type of shutdown only in the following situations:

- The database or one of its applications is functioning irregularly and none of the other types of shutdown works.
- You must shut down the database instantaneously (for example, if you know a power shutdown is going to occur in one minute).
- You experience problems when starting a database instance.

When you must do a database shutdown by aborting transactions and user connections, use one of the following commands:

| SQL\*Plus | SRVCTL (When Oracle Restart Is In Use) |
| --- | --- |
| ``` SHUTDOWN ABORT ``` | ``` srvctl stop database -db db_unique_name -stopoption abort ``` |

An aborted database shutdown proceeds with the following conditions:

- No new connections are allowed, nor are new transactions allowed to be started, after the statement is issued.
- Current client SQL statements being processed by Oracle Database are immediately terminated.
- Uncommitted transactions are not rolled back.
- Oracle Database does not wait for users currently connected to the database to disconnect. The database implicitly disconnects all connected users.

The next startup of the database will require automatic instance recovery procedures.

**Parent topic:** Shutting Down a CDB

##### Shutdown Timeout

Shutdown modes that wait for users to disconnect or for transactions to complete have a limit on the amount of time that they wait.

If all events blocking the shutdown do not occur within one hour, the shutdown operation aborts with the following message: `ORA-01013: user requested cancel of current operation`. This message is also displayed if you interrupt the shutdown process, for example by pressing `CTRL-C`. Oracle recommends that you do not attempt to interrupt an instance shutdown. Instead, allow the shutdown process to complete, and then restart the instance.

After `ORA-01013` occurs, you must consider the instance to be in an unpredictable state. You must therefore continue the shutdown process by resubmitting a `SHUTDOWN` command. If subsequent `SHUTDOWN` commands continue to fail, you must submit a `SHUTDOWN` `ABORT` command to bring down the instance. You can then restart the instance.

**Parent topic:** Shutting Down a CDB

#### Quiescing a CDB

A quiesced CDB allows only DBA transactions, queries, fetches, or PL/SQL statements.

- About Quiescing a Database  
	Occasionally you might want to put a database in a state that allows only DBA transactions, queries, fetches, or PL/SQL statements. Such a state is referred to as a **quiesced state**, in the sense that no ongoing non-DBA transactions, queries, fetches, or PL/SQL statements are running in the system.
- Placing a Database into a Quiesced State  
	When you place a database in quiesced state, non-DBA active sessions will continue until they become inactive. An active session is one that is currently inside of a transaction, a query, a fetch, or a PL/SQL statement; or a session that is currently holding any shared resources (for example, enqueues). No inactive sessions are allowed to become active.
- Restoring the System to Normal Operation  
	When you restore the system to normal operation, all non-DBA activity is allowed to proceed.
- Viewing the Quiesce State of an Instance  
	You can view the quiesce state of an instance by querying the `V$INSTANCE` view.

**Parent topic:** Starting Up and Shutting Down a CDB

##### About Quiescing a Database

Occasionally you might want to put a database in a state that allows only DBA transactions, queries, fetches, or PL/SQL statements. Such a state is referred to as a **quiesced state**, in the sense that no ongoing non-DBA transactions, queries, fetches, or PL/SQL statements are running in the system.

Note:

In this discussion of quiesce database, a DBA is defined as user `SYS` or `SYSTEM`. Other users, including those with the `DBA` role, are not allowed to issue the `ALTER SYSTEM QUIESCE DATABASE` statement or proceed after the database is quiesced.

The quiesced state lets administrators perform actions that cannot safely be done otherwise. These actions include:

- Actions that fail if concurrent user transactions access the same object, for example, changing the schema of a database table or adding a column to an existing table where a no-wait lock is required.
- Actions whose undesirable intermediate effect can be seen by concurrent user transactions, for example, a multistep procedure for reorganizing a table when the table is first exported, then dropped, and finally imported. A concurrent user who attempts to access the table after it was dropped, but before import, would not have an accurate view of the situation.

Without the ability to quiesce the database, you would need to shut down the database and reopen it in restricted mode. This is a serious restriction, especially for systems requiring 24 x 7 availability. Quiescing a database is much a smaller restriction, because it eliminates the disruption to users and the downtime associated with shutting down and restarting the database.

When the database is in the quiesced state, it is through the facilities of the Database Resource Manager that non-DBA sessions are prevented from becoming active. Therefore, while this statement is in effect, any attempt to change the current resource plan will be queued until after the system is unquiesced.

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-2BEF5482-CF97-4A85-BD90-9195E41E74EF) for more information about the Database Resource Manager

**Parent topic:** Quiescing a CDB

##### Placing a Database into a Quiesced State

When you place a database in quiesced state, non-DBA active sessions will continue until they become inactive. An active session is one that is currently inside of a transaction, a query, a fetch, or a PL/SQL statement; or a session that is currently holding any shared resources (for example, enqueues). No inactive sessions are allowed to become active.

For example, If a user issues a SQL query in an attempt to force an inactive session to become active, the query will appear to be hung. When the database is later unquiesced, the session is resumed, and the blocked action is processed.

- To place a database into a quiesced state, issue the following SQL statement:
	```
	ALTER SYSTEM QUIESCE RESTRICTED;
	```

Once all non-DBA sessions become inactive, the `ALTER SYSTEM QUIESCE RESTRICTED` statement completes, and the database is in a quiesced state. In an Oracle Real Application Clusters environment, this statement affects all instances, not just the one that issues the statement.

The `ALTER SYSTEM QUIESCE RESTRICTED` statement may wait a long time for active sessions to become inactive. You can determine the sessions that are blocking the quiesce operation by querying the `V$BLOCKING_QUIESCE` view. This view returns only a single column: `SID` (Session ID). You can join it with `V$SESSION` to get more information about the session, as shown in the following example:

```
select bl.sid, user, osuser, type, program
from v$blocking_quiesce bl, v$session se
where bl.sid = se.sid;
```

If you interrupt the request to quiesce the database, or if your session terminates abnormally before all active sessions are quiesced, then Oracle Database automatically reverses any partial effects of the statement.

For queries that are carried out by successive multiple Oracle Call Interface (OCI) fetches, the `ALTER SYSTEM QUIESCE RESTRICTED` statement does not wait for all fetches to finish. It only waits for the current fetch to finish.

For both dedicated and shared server connections, all non-DBA logins after this statement is issued are queued by the Database Resource Manager, and are not allowed to proceed. To the user, it appears as if the login is hung. The login will resume when the database is unquiesced.

The database remains in the quiesced state even if the session that issued the statement exits. A DBA must log in to the database to issue the statement that specifically unquiesces the database.

Note:

You cannot perform a cold backup when the database is in the quiesced state, because Oracle Database background processes may still perform updates for internal purposes even while the database is quiesced. In addition, the file headers of online data files continue to appear to be accessible. They do not look the same as if a clean shutdown had been performed. However, you can still take online backups while the database is in a quiesced state.

See Also:

- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=REFRN30399) for more information about the `V$BLOCKING_QUIESCE` view
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=REFRN30223) for more information about the `V$SESSION` view

**Parent topic:** Quiescing a CDB

##### Restoring the System to Normal Operation

When you restore the system to normal operation, all non-DBA activity is allowed to proceed.

- To restore the database to normal operation, issue the following SQL statement:
	```
	ALTER SYSTEM UNQUIESCE;
	```

In an Oracle Real Application Clusters environment, this statement is not required to be issued from the same session, or even the same instance, as that which quiesced the database. If the session issuing the `ALTER SYSTEM UNQUIESCE` statement terminates abnormally, then the Oracle Database server ensures that the unquiesce operation completes.

**Parent topic:** Quiescing a CDB

##### Viewing the Quiesce State of an Instance

You can view the quiesce state of an instance by querying the `V$INSTANCE` view.

To view the quiesce state of an instance:

- Query the `ACTIVE_STATE` column of the `V$INSTANCE` view.

The column has one of these values:

- `NORMAL`: Normal unquiesced state.
- `QUIESCING`: Being quiesced, but some non-DBA sessions are still active.
- `QUIESCED`: Quiesced; no non-DBA sessions are active or allowed.

**Parent topic:** Quiescing a CDB

#### Suspending and Resuming a Database

The `ALTER SYSTEM SUSPEND` statement halts all input and output (I/O) to data files (file header and file data) and control files. The suspended state lets you back up a database without I/O interference. When the database is suspended all preexisting I/O operations are allowed to complete and any new database accesses are placed in a queued state. Use the `ALTER SYSTEM RESUME` statement to resume normal database operations.

To suspend database operations:

- Run the `ALTER SYSTEM SUSPEND` statement.

To resume database operations:

- Run the `ALTER SYSTEM RESUME` statement.

The suspend command is not specific to an instance. In an Oracle Real Application Clusters environment, when you issue the suspend command on one system, internal locking mechanisms propagate the halt request across instances, thereby quiescing all active instances in a given cluster. However, if a new instance is started while another instance is being suspended, then the new instance is not suspended.

The `SUSPEND` and `RESUME` commands can be issued from different instances. For example, if instances 1, 2, and 3 are running, and you issue an `ALTER SYSTEM SUSPEND` statement from instance 1, then you can issue a `RESUME` statement from instance 1, 2, or 3 with the same effect.

The suspend/resume feature is useful in systems that allow you to mirror a disk or file and then split the mirror, providing an alternative backup and restore solution. If you use a system that cannot split a mirrored disk from an existing database while writes are occurring, then you can use the suspend/resume feature to facilitate the split.

The suspend/resume feature is not a suitable substitute for normal shutdown operations, because copies of a suspended database can contain uncommitted updates.

Note:

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

[Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=BRADV204) for details about backing up a database using the database suspend/resume feature

**Parent topic:** Starting Up and Shutting Down a CDB

#### Delaying Instance Abort

The `INSTANCE_ABORT_DELAY_TIME` initialization parameter specifies the amount of time, in seconds, to delay shutting down a database when an error causes the instance to abort.

Some errors cause the Oracle database instance to abort. You can use the `INSTANCE_ABORT_DELAY_TIME` initialization parameter to specify the amount of time to delay shutting down the instance. A database administrator can use the delay time to get information about the error and minimize problems that can result when an instance aborts. For example, a database administrator might use the delay time to get diagnostics, redirect connections using Transparent Application Failover (TAF), and flush the buffer cache. A message is written to the alert log when a delayed abort is initiated.

Caution:

Do not set the `INSTANCE_ABORT_DELAY_TIME` value too high. Since the instance is closing because of an error, some processes or resources might be corrupted or unavailable, which can make complex actions impossible.

To delay instance abort:

- Set the `INSTANCE_ABORT_DELAY_TIME` initialization parameter to the number of seconds to delay shutting down an instance when an error causes it to abort.
	This parameter is set to `0` by default.

Example 15-10 Setting the INSTANCE\_ABORT\_DELAY\_TIME Initialization Parameter

```
ALTER SYSTEM SET INSTANCE_ABORT_DELAY_TIME=60;
```

**Parent topic:** Starting Up and Shutting Down a CDB

### Modifying a CDB at the System Level

You can set initialization parameters at the CDB level. In some cases, you can override these parameters at the PDB level.

- About System-Level Modifications of a CDB  
	The `ALTER SYSTEM SET` statement dynamically sets an initialization parameter in one or more containers.
- Modifying a CDB with ALTER SYSTEM  
	To modify a CDB at the system level, use the `ALTER SYSTEM` statement.

**Parent topic:** Administering a CDB

#### About System-Level Modifications of a CDB

The `ALTER SYSTEM SET` statement dynamically sets an initialization parameter in one or more containers.

A CDB uses an inheritance model for initialization parameters in which PDBs inherit initialization parameter values from the root. In this case, inheritance means that the value of a specific parameter in the root applies to a specific PDB.

A PDB can override the root setting for some parameters. In such cases, a PDB has an inheritance property for each initialization parameter that is either true or false. The inheritance property is true for a parameter when the PDB inherits the root's value for the parameter; otherwise, the property is false.

The inheritance property for some parameters must be true. For other parameters, when the current container is the PDB, you can change the inheritance property by running the `ALTER SYSTEM SET` statement. If `V$SYSTEM_PARAMETER.ISPDB_MODIFIABLE` is `TRUE` for an initialization parameter, then the inheritance property can be false for the parameter.

When the current container is the root, the `CONTAINER` clause of the `ALTER SYSTEM SET` statement controls which PDBs inherit the parameter value being set. The `CONTAINER` clause has the following syntax:

```
CONTAINER = { CURRENT | ALL }
```

The following settings are possible:

- `CURRENT`
	The parameter setting applies only to the current container. This is the default setting for `CONTAINER`. When the current container is the root, the parameter setting applies to the root and to any PDB with an inheritance property of true for the parameter.
- `ALL`
	The parameter setting applies to all containers in the CDB, including the root and all PDBs. Specifying `ALL` sets the inheritance property to true for the parameter in all PDBs.

See Also:

" About the Current Container " for more information about the `CONTAINER` clause and rules that apply to it

**Parent topic:** Modifying a CDB at the System Level

#### Modifying a CDB with ALTER SYSTEM

To modify a CDB at the system level, use the `ALTER SYSTEM` statement.

Prerequisites

The current user must have the commonly granted `ALTER SYSTEM` privilege.

To use ALTER SYSTEM SET in the root in a CDB:

1. In SQL\*Plus, ensure that the current container is the root.
2. Run the `ALTER SYSTEM SET` statement.

Note:

To change the inheritance property for a parameter in a PDB from false to true, run the `ALTER SYSTEM RESET` statement to reset the parameter when the current container is the PDB. The following sample statement resets the `OPEN_CURSORS` parameter:

```
ALTER SYSTEM RESET OPEN_CURSORS SCOPE = SPFILE;
```

Example 15-11 Setting an Initialization Parameter for All Containers

This `ALTER SYSTEM SET` statement sets the `OPEN_CURSORS` initialization parameter to `200` for the all containers and sets the inheritance property to `TRUE` in each PDB.

```
ALTER SYSTEM SET OPEN_CURSORS = 200 CONTAINER = ALL;
```

Example 15-12 Setting an Initialization Parameter for the Root

This `ALTER SYSTEM SET` statement sets the `OPEN_CURSORS` initialization parameter to `200` for the root and for PDBs with an inheritance property of true for the parameter.

```
ALTER SYSTEM SET OPEN_CURSORS = 200 CONTAINER = CURRENT;
```

See Also:

- " [Modifying a PDB at the System Level](administering-pdbs-with-sql-plus.md) "
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF53143) for more information about the `ALTER SYSTEM SET` statement

**Parent topic:** Modifying a CDB at the System Level

### Modifying Containers When Connected to the CDB Root

You can modify the entire CDB or the root with the `ALTER DATABASE` statement.

- About Container Modification When Connected to CDB Root  
	The `ALTER DATABASE` statement modifies a CDB. When you are connected to the CDB root, the `ALTER PLUGGABLE DATABASE` statement can modify the open mode of one or more PDBs.
- Modifying an Entire CDB Using ALTER DATABASE  
	You can use the `ALTER DATABASE` statement to modify an entire CDB, including the root and all PDBs. Most `ALTER DATABASE` statements modify the entire CDB.
- Setting the Undo Mode in a CDB Using ALTER DATABASE  
	When local undo is enabled, each container has its own undo tablespace for every instance in which it is open. When local undo is disabled, there is one undo tablespace for the entire CDB.
- Modifying the CDB Root Using ALTER DATABASE  
	To modify only the root of a CDB, use the `ALTER DATABASE` statement.

**Parent topic:** Administering a CDB

#### About Container Modification When Connected to CDB Root

The `ALTER DATABASE` statement modifies a CDB. When you are connected to the CDB root, the `ALTER PLUGGABLE DATABASE` statement can modify the open mode of one or more PDBs.

The behavior of `ALTER DATABASE` and `ALTER PLUGGABLE DATABASE` depends on which container you are connected to when you use the statement:

- Connected as a common user to CDB root
	When an `ALTER DATABASE` statement with the `RENAME GLOBAL_NAME` clause modifies the domain of a CDB, it affects the domain of each PDB with a domain that defaults to that of the CDB. The `ALTER PLUGGABLE DATABASE` statement with the pdb\_change\_state clause modifies the open mode of one or more PDBs.
- Connected to a PDB
	In this case, the `ALTER DATABASE` and `ALTER PLUGGABLE DATABASE` statements modify the current PDB only.

The following table lists which containers are modified by clauses in `ALTER DATABASE` and `ALTER PLUGGABLE DATABASE` statements.

Table 15-3 Statements That Modify Containers in a CDB

| Modify Entire CDB | Modify Root Only | Modify One or More PDBs |
| --- | --- | --- |
| When connected as a common user whose current container is the root, `ALTER DATABASE` statements with the following clauses modify the entire CDB:  - [startup\_clauses](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF52389) - [recovery\_clauses](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF52390) - [logfile\_clauses](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF52402) - [controlfile\_clauses](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF52410) - [standby\_database\_clauses](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF52412) - [instance\_clauses](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF52423) - [security\_clause](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF52424) - [`RENAME GLOBAL_NAME`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF52547) clause - [`ENABLE BLOCK CHANGE TRACKING`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF52549) clause - [`DISABLE BLOCK CHANGE TRACKING`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF52550) clause | When connected as a common user whose current container is the root, `ALTER DATABASE` statements with the following clauses modify the root only:  - [database\_file\_clauses](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF52396) - [`DEFAULT EDITION`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF52540) clause - [`DEFAULT TABLESPACE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF52543) clause - [`DEFAULT TEMPORARY TABLESPACE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF52544) clause  `ALTER DATABASE` statements with the following clauses modify the root and set default values for PDBs:  - [flashback\_mode\_clause](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF52421) - [`SET DEFAULT {BIGFILE\|SMALLFILE} TABLESPACE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF52542) clause - [set\_time\_zone\_clause](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF52421)  You can use these clauses to set nondefault values for specific PDBs. | When connected as a common user whose current container is the root, `ALTER PLUGGABLE DATABASE` statements with the following clause can modify the open mode of one or more PDBs:  - [pdb\_change\_state](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF55686)  When the current container is a PDB, `ALTER PLUGGABLE DATABASE` statements with this clause can modify the open mode of the current PDB.  When connected as a common user whose current container is the root, `ALTER PLUGGABLE DATABASE` statements with the following clause can preserve or discard the open mode a PDB when the CDB restarts:  - [pdb\_save\_or\_discard\_state](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF55686) |

#### Modifying an Entire CDB Using ALTER DATABASE

You can use the `ALTER DATABASE` statement to modify an entire CDB, including the root and all PDBs. Most `ALTER DATABASE` statements modify the entire CDB.

For a list of statements that modify the entire CDB rather than the root or individual PDBs, see the "Modify Entire CDB" column of " About Container Modification When Connected to CDB Root ".

Prerequisites

To modify an entire CDB, the following prerequisites must be met:

- The current user must be a common user with the `ALTER DATABASE` privilege.
- To use an `ALTER DATABASE` statement with a recovery\_clause, the current user must have the `SYSDBA` administrative privilege commonly granted. In this case, you must exercise this privilege using `AS SYSDBA` at connect time.

To modify an entire CDB:

1. In SQL\*Plus, ensure that the current container is the root.
2. Use an `ALTER DATABASE` statement with a clause that modifies an entire CDB.

Example 15-13 Backing Up the Control File for a CDB

The following `ALTER DATABASE` statement uses a recovery\_clause to back up a control file.

```
ALTER DATABASE BACKUP CONTROLFILE TO '+DATA/dbs/backup/control.bkp';
```

Example 15-14 Adding a Redo Log File to a CDB

The following `ALTER DATABASE` statement uses a logfile\_clause to add redo log files.

```
ALTER DATABASE cdb ADD LOGFILE
  GROUP 4 ('/u01/logs/orcl/redo04a.log','/u02/logs/orcl/redo04b.log')
  SIZE 100M BLOCKSIZE 512 REUSE;
```

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF00802)

**Parent topic:** Modifying Containers When Connected to the CDB Root

#### Setting the Undo Mode in a CDB Using ALTER DATABASE

When local undo is enabled, each container has its own undo tablespace for every instance in which it is open. When local undo is disabled, there is one undo tablespace for the entire CDB.

- About the CDB Undo Mode  
	You can configure a CDB to use local undo in every container or to use shared undo (default) for the entire CDB.
- Configuring a CDB to Use Local Undo Mode  
	You can change a CDB to local undo mode by issuing an `ALTER DATABASE LOCAL UNDO ON` statement and restarting the database.
- Configuring a CDB to Use Shared Undo Mode  
	To change a CDB to use shared undo mode, use an `ALTER DATABASE LOCAL UNDO OFF` statement.

**Parent topic:** Modifying Containers When Connected to the CDB Root

##### About the CDB Undo Mode

You can configure a CDB to use local undo in every container or to use shared undo (default) for the entire CDB.

A CDB runs either in local or shared undo mode. The undo mode applies to the entire CDB. Therefore, every container either uses shared undo or local undo.

You can specify the undo mode of a CDB during CDB creation in the `ENABLE PLUGGABLE DATABASE` clause of the `CREATE DATABASE` statement. If you do not specify the `UNDO` clause, then shared undo mode is the default. You can change the undo mode of a CDB after it is created by issuing an `ALTER DATABASE` statement and restarting the CDB.

To determine the current CDB undo mode, run the following query in the CDB root:
```
SELECT PROPERTY_NAME, PROPERTY_VALUE
FROM   DATABASE_PROPERTIES
WHERE  PROPERTY_NAME = 'LOCAL_UNDO_ENABLED';
```

If the query returns `TRUE` for the `PROPERTY_VALUE`, then the CDB is in local undo mode. Otherwise, the CDB is in shared undo mode.

- About Local Undo Mode  
	Local undo mode means that each container has its own undo tablespace for every instance in which it is open.
- About Shared Undo Mode  
	Shared undo mode means that only one active undo tablespace exists for a single-instance CDB. For an Oracle RAC CDB, there is one active undo tablespace for each instance.

**Parent topic:** Setting the Undo Mode in a CDB Using ALTER DATABASE

###### About Local Undo Mode

Local undo mode means that each container has its own undo tablespace for every instance in which it is open.

In this mode, Oracle Database automatically creates an undo tablespace for every container in the CDB. For an Oracle RAC CDB, there is one active undo tablespace for each instance for each PDB in local undo mode.

Local undo mode provides increased isolation for each container and improves the efficiency of some operations, such as unplugging the container or performing point-in-time recovery on the container. In addition, local undo mode is required for some operations to be supported, such as relocating a PDB or cloning a PDB that is in open read/write mode.

When a CDB is in local undo mode, the following applies:

- Any user who has the appropriate privileges for the current container can create an undo tablespace for the container.
- Undo tablespaces are visible in static data dictionary views and dynamic performance (V$) views in every container in the CDB.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF01403) for information about the required privileges

**Parent topic:** About the CDB Undo Mode

###### About Shared Undo Mode

Shared undo mode means that only one active undo tablespace exists for a single-instance CDB. For an Oracle RAC CDB, there is one active undo tablespace for each instance.

When a CDB is in shared undo mode, the following applies:

- Only a common user who has the appropriate privileges and whose current container is the CDB root can create an undo tablespace.
- When the current container is not the CDB root, an attempt to create an undo tablespace fails and returns an error.
- Undo tablespaces are visible in static data dictionary views and dynamic performance (V$) views when the current container is the CDB root. Undo tablespaces are visible only in dynamic performance views when the current container is a PDB, an application root, or an application PDB.

Note:

- When you change the undo mode of a CDB, the new undo mode applies to an individual container the first time the container is opened after the change.
- When you change the undo mode of a CDB, containers in the CDB cannot flash back to a time or SCN that is prior to the change.

**Parent topic:** About the CDB Undo Mode

##### Configuring a CDB to Use Local Undo Mode

You can change a CDB to local undo mode by issuing an `ALTER DATABASE LOCAL UNDO ON` statement and restarting the database.

When a CDB is in local undo mode, each container has its own undo tablespace for every instance in which it is open. Oracle Database automatically creates an undo tablespace in any container in the CDB that does not have one. If a PDB without an undo tablespace is cloned, relocated, or plugged into a CDB that is configured to use local undo mode, then Oracle Database automatically creates an undo tablespace for the PDB the first time it is opened.

When a CDB is changed from shared undo mode to local undo mode, Oracle Database creates the required undo tablespaces automatically.

1. If the CDB instance is open, then shut it down.
2. Start up the CDB instance in `OPEN UPGRADE` mode. For example:
	`STARTUP UPGRADE`
3. In SQL\*Plus, ensure that the current container is the CDB root. For example, enter the following:
	```
	SHOW CON_NAME
	CON_NAME
	------------------------------
	CDB$ROOT
	```
4. Query the current undo mode of the CDB:
	```
	SELECT PROPERTY_NAME, PROPERTY_VALUE 
	FROM   DATABASE_PROPERTIES 
	WHERE  PROPERTY_NAME = 'LOCAL_UNDO_ENABLED';
	```
5. To enable local undo, issue the following SQL statement:
	`ALTER DATABASE LOCAL UNDO ON;`
6. Shut down and restart the CDB instance.
7. **Optional:** Manually create an undo tablespace in the PDB seed.
	While Oracle Database creates an undo tablespace in the PDB seed automatically in local undo mode, you might want to control the size and configuration of the undo tablespace by creating an undo tablespace manually. To ensure the PDBs created from the PDB seed use the manually-created undo tablespace and not the automatically-created undo tablespace, you must set the `UNDO_TABLESPACE` initialization parameter to the manually-created undo tablespace, or drop the automatically-created undo tablespace.
	1. In SQL\*Plus, ensure that the current container is the root.
		2. Place the PDB seed in open read/write mode:
		`ALTER PLUGGABLE DATABASE PDB$SEED OPEN READ WRITE FORCE;`
		3. Switch container to the PDB seed:
		`ALTER SESSION SET CONTAINER=PDB$SEED;`
		4. Create an undo tablespace in the PDB seed. For example:
		```
		CREATE UNDO TABLESPACE seedundots1
		   DATAFILE 'seedundotbs_1a.dbf'
		   SIZE 10M AUTOEXTEND ON
		   RETENTION GUARANTEE;
		```
		5. Switch container to the root:
		`ALTER SESSION SET CONTAINER=CDB$ROOT;`
		6. Place the PDB seed in open read-only mode:
		`ALTER PLUGGABLE DATABASE PDB$SEED OPEN READ ONLY FORCE;`

**Parent topic:** Setting the Undo Mode in a CDB Using ALTER DATABASE

##### Configuring a CDB to Use Shared Undo Mode

To change a CDB to use shared undo mode, use an `ALTER DATABASE LOCAL UNDO OFF` statement.

1. If the CDB instance is open, then shut it down.
2. Start up the CDB instance in `OPEN UPGRADE` mode. For example:
	`STARTUP UPGRADE`
3. In SQL\*Plus, ensure that the current container is the CDB root. For example, enter the following:
	```
	SHOW CON_NAME
	CON_NAME
	------------------------------
	CDB$ROOT
	```
4. Optionally, query the current undo mode of the CDB:
	```
	SELECT PROPERTY_NAME, PROPERTY_VALUE 
	FROM   DATABASE_PROPERTIES 
	WHERE  PROPERTY_NAME = 'LOCAL_UNDO_ENABLED';
	```
5. To turn off local undo, issue the following SQL statement:
	`ALTER DATABASE LOCAL UNDO OFF;`
6. Shut down and restart the CDB instance.

When in shared undo mode, the CDB ignores any local undo tablespaces that were created when it was in local undo mode. Oracle recommends that you delete the unused local undo tablespaces.

**Parent topic:** Setting the Undo Mode in a CDB Using ALTER DATABASE

#### Modifying the CDB Root Using ALTER DATABASE

To modify only the root of a CDB, use the `ALTER DATABASE` statement.

When the current container is the root, some `ALTER DATABASE` statements modify the root without directly modifying any of the PDBs. See the "Modify Root Only" column of Table 15-3 for a list of these statements.

Some statements set the defaults for the PDBs in the CDB. You can overwrite these defaults for a PDB by using the `ALTER PLUGGABLE DATABASE` statement.

Prerequisites

To modify the root, the current user must have the `ALTER DATABASE` privilege in the root.

To modify the root:

1. In SQL\*Plus, ensure that the current container is the root.
2. Run an `ALTER DATABASE` statement with a clause that modifies the root.

The following examples modify the root.

A user whose current container is the root that is not explicitly assigned a tablespace uses the default permanent tablespace for the root. The tablespace specified in the `ALTER DATABASE` statement must exist in the root.

After executing this statement, the default type of subsequently created tablespaces in the root is bigfile. This setting is also the default for PDBs.

The tablespace or tablespace group specified in the `ALTER DATABASE` statement must exist in the root.

Example 15-15 Changing the Default Permanent Tablespace for the Root

This `ALTER DATABASE` statement uses a `DEFAULT TABLESPACE` clause to set the default permanent tablespace to `root_tbs` for the root.

```
ALTER DATABASE DEFAULT TABLESPACE root_tbs;
```

Example 15-16 Bringing a Data File Online for the Root

This `ALTER DATABASE` statement uses a database\_file\_clause to bring the /u02/oracle/cdb\_01.dbf data file online.

```
ALTER DATABASE DATAFILE '/u02/oracle/cdb_01.dbf' ONLINE;
```

Example 15-17 Changing the Default Tablespace Type for the Root

This `ALTER DATABASE` statement uses a `SET DEFAULT TABLESPACE` clause to change the default tablespace type to bigfile for the root.

```
ALTER DATABASE SET DEFAULT BIGFILE TABLESPACE;
```

Example 15-18 Changing the Default Temporary Tablespace for the Root

This `ALTER DATABASE` statement uses a `DEFAULT TEMPORARY TABLESPACE` clause to set the default temporary tablespace to `root_temp` for the root.

```
ALTER DATABASE DEFAULT TEMPORARY TABLESPACE root_temp;
```

See Also:

- " [Modifying a PDB at the Database Level](administering-pdbs-with-sql-plus.md) "
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF00802)

**Parent topic:** Modifying Containers When Connected to the CDB Root

### Executing SQL in a Different Container

To execute SQL in a different container, use the `CONTAINERS` clause for DML or the `CONTAINER` clause for DDL.

- Issuing DML Statements on a Container in a CDB  
	A DML (data manipulation language) statement issued in a CDB or application root can modify a different container in the CDB. In addition, you can specify a default container target for DML statements.
- Executing DDL Statements in a CDB  
	In a CDB, you can execute a data definition language (DDL) statement in the current container or in all containers.
- Running Oracle-Supplied SQL Scripts in a CDB  
	You can use the `catcon.pl` script to run Oracle-supplied SQL or SQL scripts within a CDB. You can run the script against any specified containers.
- Executing Code in Containers Using the DBMS\_SQL Package  
	When you are executing PL/SQL code in a container in a CDB, and you want to execute one or more SQL statements in a different container, use the `DBMS_SQL` package to switch containers.

**Parent topic:** Administering a CDB

#### Issuing DML Statements on a Container in a CDB

A DML (data manipulation language) statement issued in a CDB or application root can modify a different container in the CDB. In addition, you can specify a default container target for DML statements.

- About Issuing DML Statements on a Container in a CDB  
	DML statements can affect database objects in a specified container in a CDB.
- Specifying the Default Container for DML Statements in a CDB  
	To specify the default container for DML statements in a CDB, issue the `ALTER DATABASE` statement with the `CONTAINERS DEFAULT TARGET` clause.

**Parent topic:** Executing SQL in a Different Container

##### About Issuing DML Statements on a Container in a CDB

DML statements can affect database objects in a specified container in a CDB.

The container is specified by container ID. Because the container ID can appear in more than one location, the database uses the following order of precedence:

1. The `CON_ID` specified in the `WHERE` clause of a DML statement
2. The `CONTAINERS_DEFAULT_TARGET` database property
3. The current container, which is either the CDB root or application root

In a CDB root or an application root, a DML statement that includes the `CONTAINERS` clause can modify a table or view in a single container in the CDB or application container. To use the `CONTAINERS` clause, specify the table or view being modified in the `CONTAINERS` clause and the container ID affected in the `WHERE` clause.

You can specify a target container in an `INSERT VALUES` statement by specifying a value for `CON_ID` in the `VALUES` clause. Also, you can specify a target container in an `UPDATE` or `DELETE` statement by specifying a `CON_ID` predicate in the `WHERE` clause. For example, the following DML statement updates the `sales.customers` table in the container with a `CON_ID` of `7`:
```
UPDATE CONTAINERS(sales.customers) ctab 
   SET ctab.city_name='MIAMI' 
   WHERE ctab.CON_ID=7 
   AND CUSTOMER_ID=3425;
```

The following restrictions apply to the `CONTAINERS` clause:

- The specified schema must exist both in the container specified by `CON_ID` and in the CDB or application root where the statement is executed.
- The value specified for the `CON_ID` in the `WHERE` clause must refer to a PDB, application root, or application PDB within the CDB.
- `INSERT` as `SELECT` statements where the target of the `INSERT` is in `CONTAINERS()` is not supported.
- A multitable `INSERT` statement where the target of the `INSERT` is in `CONTAINERS()` is not supported.
- DML statements using the `CONTAINERS` clause require that the database listener is configured using TCP (instead of IPC) and that the `PORT` and `HOST` values are specified for each target PDB using the `PORT` and `HOST` clauses, respectively.

**Parent topic:** Issuing DML Statements on a Container in a CDB

##### Specifying the Default Container for DML Statements in a CDB

To specify the default container for DML statements in a CDB, issue the `ALTER DATABASE` statement with the `CONTAINERS DEFAULT TARGET` clause.

When a DML statement is issued in a CDB root without specifying containers in the `WHERE` clause, the DML statement affects the default container for the CDB. The default container can be any container in the CDB, including the CDB root, a PDB, an application root, or an application PDB. Only one default container is allowed.

The `CONTAINERS_DEFAULT_TARGET` database property sets the default container. By default, this property is not set. You can determine the default target containers for a CDB by running the following query:
```
SELECT PROPERTY_VALUE 
FROM   DATABASE_PROPERTIES 
WHERE  PROPERTY_NAME='CONTAINERS_DEFAULT_TARGET';
```

1. In SQL\*Plus, ensure that the current container is the CDB root or application root.
	The current user must have the commonly granted `ALTER DATABASE` privilege.
2. Run the `ALTER DATABASE` statement with the `CONTAINERS DEFAULT TARGET` clause.

Example 15-19 Specifying the Default Container for DML Statements in a CDB

This example specifies that `PDB1` is the default container for DML statements in the CDB.

```
ALTER DATABASE CONTAINERS DEFAULT TARGET = (PDB1);
```

Example 15-20 Clearing the Default Container

This example clears the default container setting. When it is not set, the default container is the CDB root.

```
ALTER DATABASE CONTAINERS DEFAULT TARGET = NONE;
```

**Parent topic:** Issuing DML Statements on a Container in a CDB

#### Executing DDL Statements in a CDB

In a CDB, you can execute a data definition language (DDL) statement in the current container or in all containers.

- About Executing DDL Statements in a CDB  
	In a CDB, some DDL statements can apply to all containers or to the current container only.
- Executing a DDL Statement in the Current Container  
	Specify `CURRENT` in the `CONTAINER` clause of a DDL statement to execute the statement in the current container.
- Executing a DDL Statement in All Containers in a CDB  
	Specify `ALL` in the `CONTAINER` clause of a DDL statement to execute the statement in all containers in a CDB.

**Parent topic:** Executing SQL in a Different Container

##### About Executing DDL Statements in a CDB

In a CDB, some DDL statements can apply to all containers or to the current container only.

To specify which containers are affected, use the `CONTAINER` clause:

```
CONTAINER = { CURRENT | ALL }
```

The following settings are possible:

- `CURRENT` means that the statement applies only to the current container.
- `ALL` means that the statement applies to all containers in the CDB, including the root and all PDBs.

The following restrictions apply to the `CONTAINER` clause in DDL statements:

- The restrictions described in " About the Current Container ".
- You can use the `CONTAINER` clause only with the DDL statements listed in Table 15-4.

Table 15-4 DDL Statements and the CONTAINER Clause in a CDB

| DDL Statement | CONTAINER = CURRENT | CONTAINER = ALL |
| --- | --- | --- |
| `CREATE USER` | Creates a local user in the current PDB. | Creates a common user. |
| `ALTER USER` | Alters a local user in the current PDB. | Alters a common user. |
| `CREATE ROLE` | Creates a local role in the current PDB. | Creates a common role. |
| `GRANT` | Grants a privilege in the local container to a local user, common user, or local role.  The `SET CONTAINER` privilege can be granted to a user-created common user in the current PDB. | Grants a system privilege or object privilege on a common object to a common user or common role. The specified privilege is granted to the user or role across the entire CDB. |
| `REVOKE` | Revokes a privilege in the local container from a local user, common user, or local role.  This statement can revoke only a privilege granted with `CURRENT` specified in the `CONTAINER` clause from the specified user or role in the local container. The statement does not affect privileges granted with `ALL` specified in the `CONTAINER` clause.  The `SET CONTAINER` privilege can be revoked from a user-created common user in the current PDB. | Revokes a system privilege or object privilege on a common object from a common user or common role. The specified privilege is revoked from the user or role across the entire CDB.  This statement can revoke only a privilege granted with `ALL` specified in the `CONTAINER` clause from the specified common user or common role. The statement does not affect privileges granted with `CURRENT` specified in the `CONTAINER` clause. However, any privileges granted locally that depend on the privilege granted commonly that is being revoked are also revoked. |

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

- " Modifying a CDB with ALTER SYSTEM " for information about using the `ALTER SYSTEM` statement in a CDB
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF30041)
- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=CNCPT1732)
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=DBSEG589) for more information about managing users in a CDB
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=REFRN10354) for more information about the `COMMON_USER_PREFIX` initialization parameter

**Parent topic:** Executing DDL Statements in a CDB

##### Executing a DDL Statement in the Current Container

Specify `CURRENT` in the `CONTAINER` clause of a DDL statement to execute the statement in the current container.

The supported DDL statements are listed in Table 15-4.

The current user must be granted the required privileges to execute the DDL statement in the current container. For example, to create a user, the current user must be granted the `CREATE USER` system privilege in the current container.

To execute a DDL statement in the current container:

1. In SQL\*Plus, access a container.
	See " Accessing a Container in a CDB with SQL\*Plus ".
2. Execute the DDL statement with `CONTAINER` set to `CURRENT`.

A local user's user name cannot start with the prefix specified by the `COMMON_USER_PREFIX` initialization parameter. By default, in the CDB root, the prefix is `C##` or `c##`. An application root can specify its own prefix for an application container. In addition, a common user's name must consist only of ASCII characters. The specified tablespace must exist in the PDB.

Example 15-21 Creating Local User in a PDB

This example creates the local user `testpdb` in the current PDB.

```
CREATE USER testpdb IDENTIFIED BY password 
   DEFAULT TABLESPACE pdb1_tbs
   QUOTA UNLIMITED ON pdb1_tbs
   CONTAINER = CURRENT;
```

**Parent topic:** Executing DDL Statements in a CDB

##### Executing a DDL Statement in All Containers in a CDB

Specify `ALL` in the `CONTAINER` clause of a DDL statement to execute the statement in all containers in a CDB.

The supported DDL statements are listed in Table 15-4.

The following prerequisites must be met:

- The current user must be a common user.
- The current user must be granted the required privileges commonly to execute the DDL statement. For example, to create a user, the current user must be granted the `CREATE USER` system privilege commonly.

To execute a DDL statement in all containers in a CDB:

1. In SQL\*Plus, ensure that the current container is the root.
	See " About Container Access in a CDB ".
2. Execute the DDL statement with `CONTAINER` set to `ALL`.

A common user's user name must start with the prefix specified by the `COMMON_USER_PREFIX` initialization parameter. By default, in the CDB root, the prefix is `C##` or `c##`. An application root can specify its own prefix for an application container. In addition, a common user's name must consist only of ASCII characters. The specified tablespace must exist in the root and in all PDBs.

Example 15-22 Creating Common User in a CDB

This example creates the common user `c##testcdb`.

```
CREATE USER c##testcdb IDENTIFIED BY password 
   DEFAULT TABLESPACE cdb_tbs
   QUOTA UNLIMITED ON cdb_tbs
   CONTAINER = ALL;
```

**Parent topic:** Executing DDL Statements in a CDB

#### Running Oracle-Supplied SQL Scripts in a CDB

You can use the `catcon.pl` script to run Oracle-supplied SQL or SQL scripts within a CDB. You can run the script against any specified containers.

- About Running Oracle-Supplied SQL Scripts in a CDB  
	In a CDB, the `catcon.pl` script is the best way to run SQL scripts and SQL statements.
- Syntax and Parameters for catcon.pl  
	The `catcon.pl` script is a Perl script that must be run at an operating system prompt.
- Running the catcon.pl Script  
	Examples illustrate running the `catcon.pl` script.

**Parent topic:** Executing SQL in a Different Container

##### About Running Oracle-Supplied SQL Scripts in a CDB

In a CDB, the `catcon.pl` script is the best way to run SQL scripts and SQL statements.

An Oracle Database installation includes several SQL scripts. These scripts perform operations such as creating data dictionary views and installing options.

The `catcon.pl` script can run scripts in the root and in specified PDBs in the correct order, and it generates log files that you can view to confirm that the SQL script or SQL statement did not generate unexpected errors. It also starts multiple processes and assigns new scripts to them as they finish running scripts previously assigned to them.

Note:

Unless you exclude the PDB seed when you run `catcon.pl`, the SQL script or SQL statement is run on the PDB seed.

**Parent topic:** Running Oracle-Supplied SQL Scripts in a CDB

##### Syntax and Parameters for catcon.pl

The `catcon.pl` script is a Perl script that must be run at an operating system prompt.

The `catcon.pl` script has the following syntax and parameters:

```
$ORACLE_HOME/perl/bin/perl $ORACLE_HOME/rdbms/admin/catcon.pl  
[--usr username[/password]] 
[--int_usr username[/password]] 
[--script_dir directory] 
[--log_dir directory] 
[{--incl_con|--excl_con} container] 
[--echo] 
[--spool] 
[--error_logging { ON | errorlogging-table-other-than-SPERRORLOG } ] 
[--app_con application_root] 
[--no_set_errlog_ident] 
[--diag] 
[-ignore_unavailable_pdbs] 
[--verbose] 
[--force_pdb_mode pdb_mode] 
[--num_procs number]
[--user_scripts]
[--recover] 
--log_file_base log_file_name_base 
-- { SQL_script [arguments] | --x'SQL_statement' }
```

Ensure that `--x SQL_statement` is preceded by `--` if it follows any single-letter parameter. If `--x SQL_statement` is preceded by a script name or another `--x SQL_statement`, then do not precede it with `--`. Also, note that the SQL statement must be inside single quotation marks.

Command line parameters to SQL scripts can be introduced using `--p`. Interactive (or secret) parameters to SQL scripts can be introduced using `--P`.

To view the help for the `catcon.pl` script, change directories to `$ORACLE_HOME/perl/bin/`, and then run the following command:

```
perl $ORACLE_HOME/rdbms/admin/catcon.pl --help
```

The following table describes the `catcon.pl` parameters. A parameter is optional unless it is indicated that it is required.

The short parameter names in the following table are for backward compatibility. Some parameters do not have short names.

Table 15-5 catcon.pl Parameters

| Parameter | Short Name | Description |
| --- | --- | --- |
| `--usr` | `-u` | Specifies the user name and password to connect to the root and the specified PDBs. Specify a common user with the required privileges to run the SQL script or the SQL statement. The default is " `/ AS SYSDBA` ". If no password is supplied, then `catcon.pl` prompts for a password. |
| `--int_usr` | `-U` | Specifies the user name and password to connect to the root and the specified PDBs. Specify a common user with the required privileges to perform internal tasks, such as querying CDB metadata. The default is `/ AS SYSDBA`. If no password is supplied, then `catcon.pl` prompts for a password. |
| `--script_dir` | `-d` | Directory that contains the SQL script. The default is the current directory. |
| `--log_dir` | `-l` | Directory into which `catcon.pl` writes log files. The default is the current directory. |
| `{--incl_con\|--excl_con}` | `{-c\|-C}` | The containers in which the SQL script is run or is not run.  The `--incl_con` parameter lists the containers in which the SQL script is run.  The `--excl_con` parameter lists the containers in which the SQL script is not run.  Specify containers in a space-delimited list of PDB names enclosed in single quotation marks.  The `--incl_con` and `--excl_con` parameters are mutually exclusive.  When this parameter is used, the `--app_con` parameter cannot be used. |
| `--echo` | `-e` | Sets echo `ON` while running the script. The default is echo `OFF`. |
| `--spool` | `-s` | Spools the output of every script into a file with the following name:  ``` log-file-name-base_script-name-without-extension_[container-name-if-any].default-extension ``` |
| `--error_logging` | `-E` | When set to `ON`, the default error logging table is used. `ON` is the default setting. When set to `ON`, errors are written to the table `SPERRORLOG` in the current schema in each container in which the SQL script runs. If this table does not exist in a container, then it is created automatically.  When a table other than `SPERRORLOG` is specified, errors are written to the specified table. The table must exist in each container in which the SQL script runs, and the current user must have the necessary privileges to perform DML operations on the table in each of these containers.  See [SQL\*Plus User's Guide and Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQPUG160) for more information about the error logging table. |
| `--app_con` | `-F` | Specify an application root. The scripts are run in the application root and in the application PDBs that are plugged into the application root.  When this parameter is used, the `--incl_con` and `--excl_con` parameters cannot be used. |
| `--no_set_errlog_ident` | `-I` | Do not issue a `SET ERRORLOGGING` identifier. This option is intended for cases in which the `SET ERRORLOGGING` identifier is already set and should not be overwritten. |
| `--diag` | `-g` | Turns on the generation of debugging information. |
| `--verbose` | `-v` | Turns on verbose output. |
| `--ignore_unavailable_pdbs` | `-f` | Ignore PDBs that are closed or, if the `--incl_con` or `--excl_con` option is used, do not exist and process only open PDBs that were specified explicitly or implicitly.  When this option is not specified and some specified PDBs do not exist or are not open, an error is returned and none of the containers are processed. |
| `--force_pdb_mode` | n/a | The required open mode for all PDBs against which the scripts are run. Specify one of the following values:  - `UNCHANGED` - `READ WRITE` - `READ ONLY` - `UPGRADE` - `DOWNGRADE`  When a value other than `UNCHANGED` is specified, all of the PDBs against which the script is run are changed to the specified open mode. If a PDB is open in a different mode, then the PDB is closed and re-opened in the specified mode. After all of the scripts are run, each PDB is restored to its original open mode.  When `UNCHANGED`, the default, is specified, the open mode of the PDBs is not changed. |
| `--num_procs` | `-n` | Specifies how many SQL\*Plus processes `catcon.pl` will spawn to execute statements and/or scripts supplied by the caller. This overrides the number that would be spawned by `catcon.pl` based on number of PDBs in a CDB and the value of the `CPU_COUNT` initialization parameter. |
| `--user_scripts` | `-S` | Specifies that all scripts and/or statements supplied by the caller will not run in `CDB$ROOT`, `PDB$SEED`, or App Root Clones. All objects, such as tables and views, created by the scripts and/or statements will not be marked as Oracle-maintained. |
| `--recover` | `-R` | Causes `catcon.pl` to attempt to recover if a SQL\*Plus process that it spawned ends unexpectedly. When this parameter is not specified, `catcon.pl` does not attempt to recover the process and closes. |
| `--log_file_base` | `-b` | (Required) The base name for log file names. |

**Parent topic:** Running Oracle-Supplied SQL Scripts in a CDB

##### Running the catcon.pl Script

Examples illustrate running the `catcon.pl` script.

If a SQL script or SQL statement run by `catcon.pl` performs data manipulation language (DML) or data definition language (DDL) operations, then the containers being modified must be in read/write mode.

To run the catcon.pl script:

1. Open a command line prompt.
2. Run the `catcon.pl` script and specify one or more SQL scripts or SQL statements:
	```
	cd $ORACLE_HOME/perl/bin/
	perl $ORACLE_HOME/rdbms/admin/catcon.pl parameters SQL_script
	perl $ORACLE_HOME/rdbms/admin/catcon.pl parameters -- --xSQL_statement
	```

Example 15-23 Running the catblock.sql Script in All Containers in a CDB

The following example runs the `catblock.sql` script in all of the containers of a CDB (the backslash indicates line continuation):

```
$ORACLE_HOME/perl/bin/perl $ORACLE_HOME/rdbms/admin/catcon.pl \
--usr SYS --script_dir $ORACLE_HOME/rdbms/admin \
--log_file_base catblock_output catblock.sql
```

The following parameters are specified:

- The `--usr` parameter specifies that `SYS` user runs the script in each container.
- The `--script_dir` parameter specifies that the SQL script is in the `$ORACLE_HOME/rdbms/admin` directory.
- The `--log_file_base` parameter specifies that the base name for log file names is `catblock_output`.

Default parameter values are used for all other parameters. Neither the `--incl_con` nor the `--excl_con` parameter is specified. Therefore, catcon.pl runs the script in all containers by default.

Example 15-24 Running the catblock.sql Script in Specific PDBs

The following example runs the `catblock.sql` script in the `hrpdb` and `salespdb` PDBs in a CDB.

```
$ORACLE_HOME/perl/bin/perl $ORACLE_HOME/rdbms/admin/catcon.pl \
--usr SYS --int_usr SYS --script_dir $ORACLE_HOME/rdbms/admin \
--log_dir '/disk1/script_output' --incl_con 'HRPDB SALESPDB' \
--log_file_base catblock_output catblock.sql
```

The following parameters are specified:

- The `--usr` parameter specifies that `SYS` user runs the script in each container.
- The `--int_usr` parameter specifies that `SYS` user performs internal tasks.
- The `--script_dir` parameter specifies that the SQL script is in the `$ORACLE_HOME/rdbms/admin` directory.
- The `--log_dir` parameter specifies that the output files are placed in the `/disk1/script_output` directory.
- The `--incl_con` parameter specifies that the SQL script is run in the `hrpdb` and `salespdb` PDBs. The script is not run in any other containers in the CDB.
- The `--log_file_base` parameter specifies that the base name for log file names is `catblock_output`.

Example 15-25 Running the catblock.sql Script in All Containers Except for Specific PDBs

The following example runs the `catblock.sql` script in all of the containers in a CDB except for the `hrpdb` and `salespdb` PDBs.

```
$ORACLE_HOME/perl/bin/perl $ORACLE_HOME/rdbms/admin/catcon.pl \
--usr SYS --script_dir $ORACLE_HOME/rdbms/admin \
--log_dir '/disk1/script_output' --excl_con 'HRPDB SALESPDB' \ 
--log_file_base catblock_output catblock.sql
```

The following parameters are specified:

- The `--usr` parameter specifies that `SYS` user runs the script in each container.
- The `--script_dir` parameter specifies that the SQL script is in the `$ORACLE_HOME/rdbms/admin` directory.
- The `--log_dir` parameter specifies that the output files are placed in the `/disk1/script_output` directory.
- The `--excl_con` parameter specifies that the SQL script is run in all of the containers in the CDB except for the `hrpdb` and `salespdb` PDBs.
- The `--log_file_base` parameter specifies that the base name for log file names is `catblock_output`.

Example 15-26 Running a SQL Script with Command Line Parameters

The following example runs the `custom_script.sql` script in all of the containers of a CDB.

```
cd $ORACLE_HOME/perl/bin/
perl $ORACLE_HOME/rdbms/admin/catcon.pl --usr SYS --script_dir /u01/scripts \
--log_file_base custom_script_output custom_script.sql '--phr' \
'--PEnter password for user hr:'
```

The following parameters are specified:

- The `--usr` parameter specifies that `SYS` user runs the script in each container.
- The `--script_dir` parameter specifies that the SQL script is in the /u01/scripts directory.
- The `--log_file_base` parameter specifies that the base name for log file names is `custom_script_output`.
- The `--p` parameter specifies `hr` for a command line parameter
- The `--P` parameter specifies an interactive parameter that prompts for the password of user `hr`.

Default parameter values are used for all other parameters. Neither the `-incl_con` nor the `-excl_con` parameter is specified. Therefore, catcon.pl runs the script in all containers by default.

Example 15-27 Running a SQL Statement in All Containers in a CDB

The following example runs a SQL statement in all of the containers of a CDB.

```
cd $ORACLE_HOME/perl/bin/
perl $ORACLE_HOME/rdbms/admin/catcon.pl --usr SYS --echo \
--log_file_base select_output -- --x"SELECT * FROM DUAL"
```

The following parameters are specified:

- The `--usr` parameter specifies that `SYS` user runs the script in each container.
- The `--echo` parameter shows output for the SQL statement.
- The `--log_file_base` parameter specifies that the base name for log file names is `select_output`.
- The SQL statement `SELECT * FROM DUAL` is inside quotation marks and is preceded by `--x`. Because `--x` is preceded by a parameter (`--log_file_base`), it must be preceded by `--`.

Default parameter values are used for all other parameters. Neither the `-incl_con` nor the `-excl_con` parameter is specified. Therefore, catcon.pl runs the SQL statement in all containers by default.

See Also:

- " [Modifying the Open Mode of PDBs](administering-pdbs-with-sql-plus.md) "
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-D6146406-ADA2-443A-A843-137FA427ABED) for information about the `catblock.sql` script
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=REFRN005) for more information about SQL scripts

**Parent topic:** Running Oracle-Supplied SQL Scripts in a CDB

#### Executing Code in Containers Using the DBMS\_SQL Package

When you are executing PL/SQL code in a container in a CDB, and you want to execute one or more SQL statements in a different container, use the `DBMS_SQL` package to switch containers.

For example, you can use the `DBMS_SQL` package to switch containers when you need to perform identical actions in more than one container.

The following are considerations for using `DBMS_SQL` to switch containers:

- A transaction cannot span multiple containers.
	If the set of actions you must perform in the target container requires a transaction, then consider using an autonomous transaction and perform a commit or rollback as the last action.
- `SET` `ROLE` statements are not allowed.

Example 15-28 Performing Identical Actions in More Than One Container

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
    DBMS_SQL.PARSE(
      c => c1 ,
      statement                  => taskList,
      language_flag              => DBMS_SQL.NATIVE,
      edition                    => NULL,
      apply_crossedition_trigger => NULL,
      fire_apply_trigger         => NULL,
      schema                     => 'HR',
      container                  => containerList(conIndex));
     rowcount := DBMS_SQL.EXECUTE(c=>c1);
  END LOOP;
  DBMS_SQL.CLOSE_CURSOR(c=>c1);
END;
/
```

See Also:

- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ARPLS058) for more information about the `DBMS_SQL` package
- [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=LNPLS00609) for more information about autonomous transactions

**Parent topic:** Executing SQL in a Different Container

### Monitoring Containers in a CDB

You can view metadata about CDBs, PDBs, and application containers using SQL\*Plus or SQL Developer.

- About CDB and Container Information in Views  
	In a CDB, the metadata for data dictionary tables and view definitions is stored only in the root.
- Viewing Information About the Containers in a CDB  
	The `V$CONTAINERS` view provides information about all containers in a CDB, including the root and all PDBs.
- Viewing Information About PDBs  
	The `CDB_PDBS` view and `DBA_PDBS` view provide information about the PDBs associated with a CDB, including the status of each PDB.
- Viewing the Open Mode of Each PDB  
	The `V$PDBS` view provides information about the PDBs associated with the current database instance.
- Querying Container Data Objects  
	In the root, container data objects can show information about database objects (such as tables and users) contained in the root and in PDBs. Access to PDB information is controlled by the common user's `CONTAINER_DATA` attribute.
- Querying Across Containers with the CONTAINERS Clause  
	The `CONTAINERS` clause enables you to query tables and views across all containers in a CDB. It also enables you to query application common objects across all containers in an application container.
- Determining the Current Container ID or Name  
	You can determine your current container ID or container name in a CDB.
- Listing the Modifiable Initialization Parameters in PDBs  
	In a CDB, some initialization parameters apply to the root and to all PDBs. When such an initialization parameter is changed, it affects the entire CDB. You can set other initialization parameters to different values in each container.

**Parent topic:** Administering a CDB

#### About CDB and Container Information in Views

In a CDB, the metadata for data dictionary tables and view definitions is stored only in the root.

Each container, including each PDB, application root, and application PDB, has its own set of data dictionary tables and views for the objects contained in the container. Because each container can contain different data and schema objects, containers can display different metadata in data dictionary views, even when querying the same view in each container. For example, metadata about tables displayed in the `DBA_TABLES` view can be different in two different containers because the containers can contain different tables. An internal mechanism called a [metadata link](glossary.md) enables a container to access the metadata for these views in the root.

If a dictionary table stores information that pertains to the whole CDB, instead of for each container, then the metadata and the data displayed in a data dictionary view are stored in the root. For example, Automatic Workload Repository (AWR) data can be stored in the root, and this data is displayed in some data dictionary views, such as the `DBA_HIST_ACTIVE_SESS_HISTORY` view. An internal mechanism called a [data link](glossary.md) enables a container to access both the metadata and the data for these types of views in the root.

- About Viewing Information When the Current Container Is Not the CDB Root  
	When the current container is a PDB, an application root, or an application PDB, the data dictionary views show metadata for the current container only.
- About Viewing Information When the Current Container Is the CDB Root  
	When the current container is the CDB root, a common user can view data dictionary information for the CDB root and for PDBs, application roots, and application PDBs by querying container data objects.
- Views for a CDB  
	You can query a set of views for information about a CDB and its PDBs.

See Also:

[Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=CNCPT-GUID-23E972DA-EDBB-4212-A5FD-25BF7A9FD7CA) for more information about dictionary access in containers, metadata links, and data links

**Parent topic:** Monitoring Containers in a CDB

##### About Viewing Information When the Current Container Is Not the CDB Root

When the current container is a PDB, an application root, or an application PDB, the data dictionary views show metadata for the current container only.

Also, in a container that is not the CDB root, `CDB_` views only show information about database objects visible through the corresponding `DBA_` view.

**Parent topic:** About CDB and Container Information in Views

##### About Viewing Information When the Current Container Is the CDB Root

When the current container is the CDB root, a common user can view data dictionary information for the CDB root and for PDBs, application roots, and application PDBs by querying container data objects.

A container data object is a table or view that can contain data pertaining to the following:

- One or more containers
- The CDB as a whole
- One or more containers and the CDB as a whole

Container data objects include `V$`, `GV$`, `CDB_`, and some Automatic Workload Repository `DBA_HIST*` views. A common user's `CONTAINER_DATA` attribute determines which containers are visible in container data objects.

In a CDB, for every `DBA_` view, there is a corresponding `CDB_` view. All `CDB_` views are container data objects, but most `DBA_` views are not.

Each container data object contains a `CON_ID` column that identifies the container for each row returned. Table 15-6 describes the meanings of the values in the `CON_ID` column.

Table 15-6 CON\_ID Column in Container Data Objects

| Value in CON\_ID Column | Description |
| --- | --- |
| 0 | The data pertains to the entire CDB |
| 1 | The data pertains to the CDB root |
| 2 | The data pertains to the PDB seed |
| 3 - 4,098 | The data pertains to a PDB, an application root, or an application PDB  Each container has its own container ID. |

The following views behave differently from other `[G]V$` views:

- `[G]V$SYSSTAT`
- `[G]V$SYS_TIME_MODEL`
- `[G]V$SYSTEM_EVENT`
- `[G]V$SYSTEM_WAIT_CLASS`

When queried from the CDB root, these views return instance-wide data, with `0` in the `CON_ID` column for each row returned. However, you can query equivalent views that behave the same as other container data objects. The following views can return specific data for each container in a CDB: `[G]V$CON_SYSSTAT`, `[G]V$CON_SYS_TIME_MODEL`, `[G]V$CON_SYSTEM_EVENT`, and `[G]V$CON_SYSTEM_WAIT_CLASS`.

Note:

- When querying a container data object, the data returned depends on whether containers are open and on the privileges granted to the user running the query.
- In an Oracle Real Application Clusters (Oracle RAC) environment, the data returned by container data objects might vary based on the instance to which a session is connected.
- When a container is opened in restricted mode, it is ignored in queries on `CDB_` views.

See Also:

- " About the Current Container "
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=DBSEG803) for detailed information about container data objects

**Parent topic:** About CDB and Container Information in Views

##### Views for a CDB

You can query a set of views for information about a CDB and its PDBs.

Table 15-7 describes data dictionary views that are useful for monitoring a CDB and its PDBs.

Table 15-7 Views for a CDB

| View | Description | More Information |
| --- | --- | --- |
| Container data objects, including:  - `V$` views - `GV$` views - `CDB_` views - `DBA_HIST*` views | Container data objects can display information about multiple PDBs. Each container data object includes a `CON_ID` column to identify containers.  There is a `CDB_` view for each corresponding `DBA_` view. | " Querying Container Data Objects "  [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=DBSEG803) |
| `{CDB\|DBA}_PDBS` | Displays information about the PDBs associated with the CDB, including the status of each PDB. | " Viewing Information About PDBs "  [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=REFRN23794) |
| `CDB_PROPERTIES` | Displays the permanent properties of each container in a CDB. | [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=REFRN29012) |
| `{CDB\|DBA}_PDB_HISTORY` | Displays the history of each PDB. | [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=REFRN23865) |
| `{CDB\|DBA}_CONTAINER_DATA` | Displays information about the user-level and object-level `CONTAINER_DATA` attributes specified in the CDB. | [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=REFRN23866) |
| `{CDB\|DBA}_HIST_PDB_INSTANCE` | Displays the PDBs and instances in the Workload Repository. | [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=REFRN23862) |
| `{CDB\|DBA}_PDB_SAVED_STATES` | Displays information about the current saved PDB states in the CDB. | [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=REFRN23959)  " [Preserving or Discarding the Open Mode of PDBs When the CDB Restarts](administering-pdbs-with-sql-plus.md) " |
| `{CDB\|DBA}_APPLICATIONS` | Describes all applications in an application container. | " [Viewing Information About Applications](administering-application-containers-with-sql-plus.md) " |
| `{CDB\|DBA}_APP_STATEMENTS` | Describes all statements from application installation, upgrade, and patch operations in an application container. | " [Viewing Information About Application Statements](administering-application-containers-with-sql-plus.md) " |
| `{CDB\|DBA}_APP_PATCHES` | Describes all application patches in an application container. | " [Viewing Information About Application Patches](administering-application-containers-with-sql-plus.md) " |
| `{CDB\|DBA}_APP_ERRORS` | Describes all application error messages generated in an application container. | " [Viewing Information About Application Errors](administering-application-containers-with-sql-plus.md) " |
| `{CDB\|DBA}_CDB_RSRC_PLANS` | Displays information about all the CDB resource plans. | [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=REFRN23809) |
| `{CDB\|DBA}_CDB_RSRC_PLAN_DIRECTIVES` | Displays information about all the CDB resource plan directives. | [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=REFRN23808) |
| `PDB_ALERTS` | Contains descriptions of reasons for PDB alerts. | [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=REFRN29165) |
| `PDB_PLUG_IN_VIOLATIONS` | Displays information about incompatibilities between a PDB and the CDB to which it belongs. This view is also used to display information generated by executing `DBMS_PDB.CHECK_PLUG_COMPATIBILITY`. | [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=REFRN29161)  " [Plugging In an Unplugged PDB](plugging-in-a-pdb.md) " |
| `{USER\|ALL\|DBA\|CDB}_OBJECTS` | Displays information about database objects, and the `SHARING` column shows whether a database object is a metadata-linked object, a data-linked object, an extended data-linked object, or a standalone object that is not linked to another object. | [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=REFRN20146) |
| `{ALL\|DBA\|CDB}_SERVICES` | Displays information about database services, and the `PDB` column shows the name of the PDB associated with each service. | [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=REFRN20465) |
| `{USER\|ALL\|DBA\|CDB}_VIEWS`  `{USER\|ALL\|DBA\|CDB}_TABLES` | The `CONTAINER_DATA` column shows whether the view or table is a container data object. | [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=REFRN-GUID-0FE29B36-0882-47AE-A54E-A01FC9C4100A) |
| `{USER\|ALL\|DBA\|CDB}_USERS` | The `COMMON` column shows whether a user is a common user or a local user. | [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=REFRN20302) |
| `{USER\|ALL\|DBA\|CDB}_ROLES`  `{USER\|ALL\|DBA\|CDB}_COL_PRIVS`  `{USER\|ALL}_COL_PRIVS_MADE`  `{USER\|ALL}_COL_PRIVS_RECD`  `{USER\|ALL}_TAB_PRIVS_MADE`  `{USER\|ALL}_TAB_PRIVS_RECD`  `{USER\|DBA\|CDB}_SYS_PRIVS`  `{USER\|DBA\|CDB}_ROLE_PRIVS`  `ROLE_TAB_PRIVS`  `ROLE_SYS_PRIVS` | The `COMMON` column shows whether a role or privilege is commonly granted or locally granted. | [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=REFRN-GUID-C8E5500E-A013-45D3-AEFB-2C9C0AC87EC7) |
| `{USER\|ALL\|DBA\|CDB}_ARGUMENTS`  `{USER\|ALL\|DBA\|CDB}_CLUSTERS`  `{USER\|ALL\|DBA\|CDB}_CONSTRAINTS`  `{ALL\|DBA\|CDB}_DIRECTORIES`  `{USER\|ALL\|DBA\|CDB}_IDENTIFIERS`  `{USER\|ALL\|DBA\|CDB}_LIBRARIES`  `{USER\|ALL\|DBA\|CDB}_PROCEDURES`  `{USER\|ALL\|DBA\|CDB}_SOURCE`  `{USER\|ALL\|DBA\|CDB}_SYNONYMS`  `{USER\|ALL\|DBA\|CDB}_VIEWS` | The `ORIGIN_CON_ID` column shows the ID of the container from which the row originates. | [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=REFRN-GUID-1F535054-CABC-4321-AA2F-151DA726A2D7) |
| `[G]V$DATABASE` | Displays information about the database from the control file. If the database is a CDB, then CDB-related information is included. | [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=REFRN30047) |
| `[G]V$CONTAINERS` | Displays information about the containers associated with the current CDB, including the root and all PDBs. | " Viewing Information About the Containers in a CDB "  [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=REFRN30708) |
| `[G]V$PDBS` | Displays information about the PDBs associated with the current CDB, including the open mode of each PDB. | " Viewing the Open Mode of Each PDB "  [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=REFRN30652) |
| `[G]V$PDB_INCARNATION` | Displays information about all PDB incarnations. Oracle creates a new PDB incarnation whenever a PDB is opened with the `RESETLOGS` option. | [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=REFRN30709) |
| `[G]V$SYSTEM_PARAMETER`  `[G]V$PARAMETER` | Displays information about initialization parameters, and the `ISPDB_MODIFIABLE` column shows whether a parameter can be modified for a PDB. | " Listing the Modifiable Initialization Parameters in PDBs "  [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=REFRN30275) |
| `V$DIAG_ALERT_EXT`  `[G]V$DIAG_APP_TRACE_FILE`  `[G]V$DIAG_OPT_TRACE_RECORDS`  `V$DIAG_SESS_OPT_TRACE_RECORDS`  `V$DIAG_SESS_SQL_TRACE_RECORDS`  `[G]V$DIAG_SQL_TRACE_RECORDS`  `[G]V$DIAG_TRACE_FILE`  `[G]V$DIAG_TRACE_FILE_CONTENTS` | Displays trace file and alert file data for the current container in a CDB. | [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=TGSQL-GUID-93ACB9CC-9937-479E-8995-FEABD854C900) |
| `V$DIAG_INCIDENT`  `V$DIAG_PROBLEM` | Displays information about problems and incidents for the current container in a CDB. | [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=REFRN-GUID-081E633E-D430-475F-98C1-4066EA9623C7) |

**Parent topic:** About CDB and Container Information in Views

#### Viewing Information About the Containers in a CDB

The `V$CONTAINERS` view provides information about all containers in a CDB, including the root and all PDBs.

To view this information, the query must be run by a common user whose current container is the root. When the current container is a PDB, this view only shows information about the current PDB.

To view information about the containers in a CDB:

1. In SQL\*Plus, ensure that the current container is the root.
	See " About Container Access in a CDB ".
2. Query the `V$CONTAINERS` view.

Example 15-29 Viewing Identifying Information About Each Container in a CDB

```
COLUMN NAME FORMAT A8

SELECT NAME, CON_ID, DBID, CON_UID, GUID FROM V$CONTAINERS ORDER BY CON_ID;
```

Sample output:

```
NAME         CON_ID       DBID    CON_UID GUID
-------- ---------- ---------- ---------- --------------------------------
CDB$ROOT          1  659189539          1 C091A6F89C7572A1E0436797E40AC78D
PDB$SEED          2 4026479912 4026479912 C091AE9C00377591E0436797E40AC138
HRPDB             3 3718888687 3718888687 C091B6B3B53E7834E0436797E40A9040
SALESPDB          4 2228741407 2228741407 C091FA64EF8F0577E0436797E40ABE9F
```

**Parent topic:** Monitoring Containers in a CDB

#### Viewing Information About PDBs

The `CDB_PDBS` view and `DBA_PDBS` view provide information about the PDBs associated with a CDB, including the status of each PDB.

To view this information, the query must be run by a common user whose current container is the root. When the current container is a PDB, all queries on these views return no results.

To view information about PDBs:

1. In SQL\*Plus, ensure that the current container is the root.
	See " Accessing a Container in a CDB with SQL\*Plus ".
2. Query the `CDB_PDBS` or `DBA_PDBS` view.

Example 15-30 Viewing Container ID, Name, and Status of Each PDB

```
COLUMN PDB_NAME FORMAT A15
 
SELECT PDB_ID, PDB_NAME, STATUS FROM DBA_PDBS ORDER BY PDB_ID;
```

Sample output:

```
PDB_ID PDB_NAME        STATUS
---------- --------------- -------------
         2 PDB$SEED        NORMAL
         3 HRPDB           NORMAL
         4 SALESPDB        NORMAL
```

See Also:

" About the Current Container "

**Parent topic:** Monitoring Containers in a CDB

#### Viewing the Open Mode of Each PDB

The `V$PDBS` view provides information about the PDBs associated with the current database instance.

You can query this view to determine the open mode of each PDB. For each PDB that is open, this view can also show when the PDB was last opened. A common user can query this view when the current container is the root or a PDB. When the current container is a PDB, this view only shows information about the current PDB.

To view the open status of each PDB:

1. In SQL\*Plus, access a container.
	See " Accessing a Container in a CDB with SQL\*Plus ".
2. Query the `V$PDBS` view.

Example 15-31 Viewing the Name and Open Mode of Each PDB

```
COLUMN NAME FORMAT A15
COLUMN RESTRICTED FORMAT A10
COLUMN OPEN_TIME FORMAT A30
 
SELECT NAME, OPEN_MODE, RESTRICTED, OPEN_TIME FROM V$PDBS;
```

Sample output:

```
NAME            OPEN_MODE  RESTRICTED OPEN_TIME
--------------- ---------- ---------- ------------------------------
PDB$SEED        READ ONLY  NO         21-MAY-12 12.19.54.465 PM
HRPDB           READ WRITE NO         21-MAY-12 12.34.05.078 PM
SALESPDB        MOUNTED    NO         22-MAY-12 10.37.20.534 AM
```

See Also:

- " [Modifying the Open Mode of PDBs with ALTER PLUGGABLE DATABASE](administering-pdbs-with-sql-plus.md) "
- " [Modifying the Open Mode of PDBs](administering-pdbs-with-sql-plus.md) "
- " [Modifying a PDB with the ALTER PLUGGABLE DATABASE Statement](administering-pdbs-with-sql-plus.md) "
- " About the Current Container "

**Parent topic:** Monitoring Containers in a CDB

#### Querying Container Data Objects

In the root, container data objects can show information about database objects (such as tables and users) contained in the root and in PDBs. Access to PDB information is controlled by the common user's `CONTAINER_DATA` attribute.

For example, `CDB_` views are container data objects. See " About Viewing Information When the Current Container Is the CDB Root " and [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=DBSEG803) for more information about container data objects.

Each container data object contains a `CON_ID` column that shows the container ID of each PDB in the query results. You can view the PDB name for a container ID by querying the `DBA_PDBS` view.

To use container data objects to show information about multiple PDBs:

1. In SQL\*Plus, ensure that the current container is the root.
	See " About Container Access in a CDB ".
2. Query the container data object to show the desired information.

Note:

When a query contains a join of a container data object and a non-container data object, and the current container is the root, the query returns data for the entire CDB only (`CON_ID` = `0`).

Example 15-32 Showing the Tables Owned by Specific Schemas in Multiple PDBs

This example queries the `DBA_PDBS` view and the `CDB_TABLES` view from the root to show the tables owned by `hr` user and `oe` user in the PDBs associated with the CDB. This query returns only rows where the PDB has an ID greater than 2 (`p.PDB_ID > 2`) to avoid showing the users in the CDB root and PDB seed.

```
COLUMN PDB_NAME FORMAT A15
COLUMN OWNER FORMAT A15
COLUMN TABLE_NAME FORMAT A30
 
SELECT p.PDB_ID, p.PDB_NAME, t.OWNER, t.TABLE_NAME 
  FROM DBA_PDBS p, CDB_TABLES t 
  WHERE p.PDB_ID > 2 AND
        t.OWNER IN('HR','OE') AND
        p.PDB_ID = t.CON_ID
   ORDER BY p.PDB_ID;
```

Sample output:

```
PDB_ID PDB_NAME        OWNER           TABLE_NAME
---------- --------------- --------------- ------------------------------
         3 HRPDB           HR              COUNTRIES
         3 HRPDB           HR              JOB_HISTORY
         3 HRPDB           HR              EMPLOYEES
         3 HRPDB           HR              JOBS
         3 HRPDB           HR              DEPARTMENTS
         3 HRPDB           HR              LOCATIONS
         3 HRPDB           HR              REGIONS
         4 SALESPDB        OE              PRODUCT_INFORMATION
         4 SALESPDB        OE              INVENTORIES
         4 SALESPDB        OE              ORDERS
         4 SALESPDB        OE              ORDER_ITEMS
         4 SALESPDB        OE              WAREHOUSES
         4 SALESPDB        OE              CUSTOMERS
         4 SALESPDB        OE              SUBCATEGORY_REF_LIST_NESTEDTAB
         4 SALESPDB        OE              PRODUCT_REF_LIST_NESTEDTAB
         4 SALESPDB        OE              PROMOTIONS
         4 SALESPDB        OE              PRODUCT_DESCRIPTIONS
```

This sample output shows the PDB `hrpdb` has tables in the `hr` schema and the PDB `salespdb` has tables in the `oe` schema.

Example 15-33 Showing the Users in Multiple PDBs

This example queries the `DBA_PDBS` view and the `CDB_USERS` view from the root to show the users in each PDB. The query uses `p.PDB_ID > 2` to avoid showing the users in the CDB root and the PDB seed.

```
COLUMN PDB_NAME FORMAT A15
COLUMN USERNAME FORMAT A30
 
SELECT p.PDB_ID, p.PDB_NAME, u.USERNAME 
  FROM DBA_PDBS p, CDB_USERS u
  WHERE p.PDB_ID > 2 AND
        p.PDB_ID = u.CON_ID
  ORDER BY p.PDB_ID;
```

Sample output:

```
PDB_ID PDB_NAME        USERNAME
---------- --------------- ------------------------------
         .
         .
         .
         3 HRPDB           HR
         3 HRPDB           OLAPSYS
         3 HRPDB           MDSYS
         3 HRPDB           ORDSYS
         .
         .
         .
         4 SALESPDB        OE
         4 SALESPDB        CTXSYS
         4 SALESPDB        MDSYS
         4 SALESPDB        EXFSYS
         4 SALESPDB        OLAPSYS
         .
         .
         .
```

Example 15-34 Showing the Data Files for Each PDB in a CDB

This example queries the `DBA_PDBS` and `CDB_DATA_FILES` views to show the name and location of each data file for all of the PDBs in a CDB, including the PDB seed.

```
COLUMN PID FORMAT 999
COLUMN PDB_NAME FORMAT A8
COLUMN FILE_ID FORMAT 9999
COLUMN TABLESPACE_NAME FORMAT A10
COLUMN FILE_NAME FORMAT A45

SELECT p.PDB_ID AS PID, p.PDB_NAME, d.FILE_ID, d.TABLESPACE_NAME, d.FILE_NAME
  FROM DBA_PDBS p, CDB_DATA_FILES d
  WHERE p.PDB_ID = d.CON_ID
  ORDER BY p.PDB_ID;
```

Sample output:

```
PID PDB_NAME FILE_ID TABLESPACE FILE_NAME
--- -------- ------- ---------- ----------------------------------------
  2 PDB$SEED       6 SYSAUX     /disk1/oracle/dbs/pdbseed/cdb1_ax.f
  2 PDB$SEED       5 SYSTEM     /disk1/oracle/dbs/pdbseed/cdb1_db.f
  3 HRPDB          9 SYSAUX     /disk1/oracle/dbs/hrpdb/hrpdb_ax.f
  3 HRPDB          8 SYSTEM     /disk1/oracle/dbs/hrpdb/hrpdb_db.f
  3 HRPDB         13 USER       /disk1/oracle/dbs/hrpdb/hrpdb_usr.dbf
  4 SALESPDB      15 SYSTEM     /disk1/oracle/dbs/salespdb/salespdb_db.f
  4 SALESPDB      16 SYSAUX     /disk1/oracle/dbs/salespdb/salespdb_ax.f
  4 SALESPDB      18 USER       /disk1/oracle/dbs/salespdb/salespdb_usr.dbf
```

Example 15-35 Showing the Temp Files in a CDB

This example queries the `CDB_TEMP_FILES` view to show the name and location of each temp file in a CDB, as well as the tablespace that uses the temp file.

```
COLUMN CON_ID FORMAT 999
COLUMN FILE_ID FORMAT 9999
COLUMN TABLESPACE_NAME FORMAT A15
COLUMN FILE_NAME FORMAT A45

SELECT CON_ID, FILE_ID, TABLESPACE_NAME, FILE_NAME
  FROM CDB_TEMP_FILES
  ORDER BY CON_ID;
```

Sample output:

```
CON_ID FILE_ID TABLESPACE_NAM FILE_NAME
------ ------- -------------- ---------------------------------------------
     1       1 TEMP           /disk1/oracle/dbs/t_tmp1.f
     2       2 TEMP           /disk1/oracle/dbs/pdbseed/t_tmp1.f
     3       3 TEMP           /disk1/oracle/dbs/hrpdb/t_hrpdb_tmp1.f
     4       4 TEMP           /disk1/oracle/dbs/salespdb/t_salespdb_tmp1.f
```

Example 15-36 Showing the Services Associated with PDBs

This example queries the `CDB_SERVICES` view to show the PDB name, network name, and container ID of each service associated with a PDB.

```
COLUMN NETWORK_NAME FORMAT A30
COLUMN PDB FORMAT A15
COLUMN CON_ID FORMAT 999

SELECT PDB, NETWORK_NAME, CON_ID FROM CDB_SERVICES
  WHERE PDB IS NOT NULL AND
        CON_ID > 2
  ORDER BY PDB;
```

Sample output:

```
PDB             NETWORK_NAME                   CON_ID
--------------- ------------------------------ ------
HRPDB           hrpdb.example.com                   3
SALESPDB        salespdb.example.com                4
```

#### Querying Across Containers with the CONTAINERS Clause

The `CONTAINERS` clause enables you to query tables and views across all containers in a CDB. It also enables you to query application common objects across all containers in an application container.

- About Querying Across Containers with the CONTAINERS Clause  
	The `CONTAINERS` clause enables you to query across containers in a CDB.
- Querying User-Created Tables and Views Across All Containers  
	The `CONTAINERS` clause enables you to query user-created tables and views across all containers. This clause enables queries from the CDB root to display data in tables or views that exist in all open PDBs in a CDB.
- Querying Application Common Objects Across Application PDBs  
	The `CONTAINERS` clause enables you to query application common objects across all PDBs in an application container. Queries from the application root display data in objects that exist in all open PDBs in the container.

**Parent topic:** Monitoring Containers in a CDB

##### About Querying Across Containers with the CONTAINERS Clause

The `CONTAINERS` clause enables you to query across containers in a CDB.

The `CONTAINERS` clause enables you to query user-created tables and views across all containers in a CDB. This clause enables queries from the CDB root to display data in tables or views that exist in all open containers in a CDB.

The `CONTAINERS` clause also enables you to query application common objects, such as tables and views, across all application PDBs in an application container. This clause enables queries from the application root to display data in tables or views that exist in all open application PDBs in the application container.

The `CONTAINERS` clause exposes three implicitly generated columns:
- `CON_ID`: The ID of the container from which the row is retrieved.
- `CON$NAME`: The name of the container from which the row is retrieved. This is a hidden column.
- `CDB$NAME`: The name of the CDB from which the row is retrieved. In the absence of a proxy PDB or a CDB fleet, all rows will have the same value for `CDB$NAME`. This is a hidden column.

When the `CONTAINERS` clause is evaluated, each container is treated as a partition; therefore, the plan output for a query using the `CONTAINERS` clause includes a partition iterator. Partition pruning can be used to restrict the set of containers that is accessed during query execution. The pruning predicate may be specified either on the `CON_ID` column or the `CON$NAME` column, both of which are implicitly generated for a `CONTAINERS` clause.

Evaluation of the `CONTAINERS` clause makes use of parallel execution processes. Each container is assigned to a parallel execution process (P00\*) and the process switches into the container to execute a recursive SQL statement on the base table or view. The base table or view is the object whose name is passed as an argument to the `CONTAINERS` clause.

The `CONTAINERS_PARALLEL_DEGREE` initialization parameter can control the degree of parallelism of a query involving the `CONTAINERS` clause. If the value of `CONTAINERS_PARALLEL_DEGREE` is lower than `65535` (the default), then the specified value is used.

When the `CONTAINERS_PARALLEL_DEGREE` initialization parameter is set to the default value (`65535`), queries that use the `CONTAINERS` clause are parallel by default. The default degree of parallelism is calculated with the following formula:
```
max(min(cpu_count,number_of_open_containers),#instances)
```

In addition, you can pass a `DEFAULT_PDB_HINT` hint in the `CONTAINERS` clause. The hint is passed in the query that is run in each container.

The columns accessed by the recursive SQL statement are determined by the columns of the `CONTAINERS` clause accessed in the query. Predicates in the query using the `CONTAINERS` clause may be pushed down to the recursive SQL and evaluated within each container, significantly reducing the number of rows that need to be processed as a post filter on the `CONTAINERS` clause.

You can force the recursive SQL that results from a query that includes the `CONTAINERS` clause to be parallel by using the `DEFAULT_PDB_HINT` clause of a `CONTAINERS` hint or by using automatic degree of parallelism. However, parallel statement queuing is not possible for recursive SQL that results from a query that includes the `CONTAINERS` clause.

Columns of the following types are removed if they exist in a table specified in a `CONTAINERS` clause:

- The following user-defined types: object types, varrays, REFs, and nested tables
- The following Oracle-supplied types: `ANYTYPE`, `ANYDATASET`, URI types, `SDO_TOPO_GEOMETRY`, `SDO_GEORASTER`, and `Expression`

Note:

- When a container is opened in restricted mode, it is ignored by the `CONTAINERS` clause.
- When the `CONTAINERS` clause is used and an error is returned by a container, the query does not return results from the container that raised the error, and the error is not returned. For example, you cannot select a `BFILE` column from a remote table into a local variable. If a query that does this uses the `CONTAINERS` clause and includes local and remote containers, then the query returns results for the local containers, but not the remote containers, and no error is returned.

See Also:

- " About the Current Container "
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF56898) for more information about the `CONTAINERS` clause and the `CONTAINERS` hint
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=DBSEG803) for detailed information about container data objects
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=REFRN-GUID-17F470E8-4C0D-43C8-AD2F-376B1503BCF6) for more information about the `CONTAINERS_PARALLEL_DEGREE` initialization parameter
- [Oracle Database Data Warehousing Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=DWHSG9066) for more information about automatic degree of parallelism and parallel statement queuing

**Parent topic:** Querying Across Containers with the CONTAINERS Clause

##### Querying User-Created Tables and Views Across All Containers

The `CONTAINERS` clause enables you to query user-created tables and views across all containers. This clause enables queries from the CDB root to display data in tables or views that exist in all open PDBs in a CDB.

Prerequisites

The tables and views, or synonyms of them, specified in the `CONTAINERS` clause must exist in the CDB root and in all other containers.

To use the `CONTAINERS` clause to query tables and views across all containers:

1. In SQL\*Plus, access a container.
	To view data in multiple containers, ensure that the current container is the CDB root.
	See " About Container Access in a CDB ".
2. Run a query that includes the `CONTAINERS` clause.

Example 15-37 Querying a Table Owned by a Common User Across All Containers

This example makes the following assumptions:

- An organization has several PDBs, and each PDB is for a different department in the organization.
- Each PDB has an `employees` table that tracks the employees in the department, but the table in each PDB contains different employees.
- The CDB root also has an empty `employees` table.
- The `employees` table in each container is owned by the same common user.

With the CDB root as the current container and the common user that owns the table as the current user, run the following query with the `CONTAINERS` clause to return all employees in the `employees` table in all PDBs:

```
SELECT * FROM CONTAINERS(employees);
```

Example 15-38 Querying a Table Owned by Local Users Across All Containers

This example makes the following assumptions:

- An organization has several PDBs, and each PDB is for a different department in the organization.
- Each PDB has an `hr.employees` table that tracks the employees in the department, but the table in each PDB contains different employees.
- The CDB root also has an empty `employees` table owned by a common user.

To run a query that returns all employees in all PDBs, first connect to each PDB as a common user, and create a view with the following statement:

```
CREATE OR REPLACE VIEW employees AS SELECT * FROM hr.employees;
```

The common user that owns the view must be the same common user that owns the `employees` table in the CDB root. After you run this statement in each PDB, the common user has a view named `employees` in each PDB.

With the CDB root as the current container and the common user as the current user, run the following query with the `CONTAINERS` clause to return all employees in the `hr.employees` table in all PDBs:

```
SELECT * FROM CONTAINERS(employees);
```

You can also query the view in specific containers. For example, the following SQL statement queries the view in the containers with a `CON_ID` of `3` and `4`:

```
SELECT * FROM CONTAINERS(employees) WHERE CON_ID IN(3,4);
```

Note:

You can also use the `CONTAINERS` clause to query Oracle-supplied tables and views. When running the query, ensure that the current user is the owner of the table or view, or create a view using the `CONTAINERS` clause and grant `SELECT` privilege on the view to the appropriate users.

See Also:

- " About the Current Container "
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF56898) for more information about the `CONTAINERS` clause
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=DBSEG803) for detailed information about container data objects

**Parent topic:** Querying Across Containers with the CONTAINERS Clause

##### Querying Application Common Objects Across Application PDBs

The `CONTAINERS` clause enables you to query application common objects across all PDBs in an application container. Queries from the application root display data in objects that exist in all open PDBs in the container.

The `CONTAINERS` clause is most useful for metadata-linked application common objects. With metadata-linked application common objects, the structure is the same in all containers in an application container, but the data is different. You can use the `CONTAINERS` clause to view the data in a metadata-linked application common object in multiple application PDBs. The benefits are similar for extended data-linked objects. The `CONTAINERS` clause uses parallel execution to execute the query across the distinct application PDBs hosted in the application root.

To use the `CONTAINERS` clause to query tables and views across all application PDBs:

1. In SQL\*Plus, access the application root.
	See " About Container Access in a CDB ".
2. Run a query that includes the `CONTAINERS` clause.

Note:

You can enable the `CONTAINERS_DEFAULT` attribute for a table or view in an application root. When this attribute is enabled, the `CONTAINERS` clause is used for queries and DML statements on the database object by default, and the `CONTAINERS` clause is not required in the SQL statements. To enable the `CONTAINERS_DEFAULT` attribute for a table or view in an application root, run the `ALTER TABLE` or `CREATE OR REPLACE VIEW` statement with the `ENABLE CONTAINERS_DEFAULT` clause.

Example 15-39 Querying an Application Common Object Across All Application PDBs

This example makes the following assumptions:

- An organization has several application PDBs, and each application PDB is for a different department in the organization.
- Each application PDB has an `employees` table that tracks the employees in the department, but the table in each application PDB contains different employees.
- The application root also has an empty `employees` table.
- The employees table in each container is owned by the same common user.
- A company has multiple tenants that use an application in an application container, and each tenant has its own application PDB.
- The company uses metadata-linked application common objects to keep the structure of the data the same in all application PDBs, but the data is different in each application PDB.
- Each application PDB has a metadata-linked `sales.customers` table that stores information about each tenant’s customers.

With the application root as the current container and the application common user that owns the table as the current user, run the following query with the `CONTAINERS` clause to return all customers in the `sales.customers` table in all application PDBs:

```
SELECT * FROM CONTAINERS(sales.customers);
```

See Also:

- " [About Application Common Objects](administering-application-containers-with-sql-plus.md) "
- " About the Current Container "
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF56898) for more information about the `CONTAINERS` clause
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=DBSEG803) for detailed information about container data objects

**Parent topic:** Querying Across Containers with the CONTAINERS Clause

#### Determining the Current Container ID or Name

You can determine your current container ID or container name in a CDB.

To determine the current container ID:

- Run the following SQL\*Plus command:
	```
	SHOW CON_ID
	```

To determine the current container name:

- Run the following SQL\*Plus command:
	```
	SHOW CON_NAME
	```

In addition, you can use the functions listed in Table 15-8 to determine the container ID, container name, DBID, GUID, and UID of a container.

Table 15-8 Functions That Return Container Information

| Function | Description |
| --- | --- |
| `CON_NAME_TO_ID` ('container\_name') | Returns the container ID based on the container's name. |
| `CON_DBID_TO_ID` (container\_dbid) | Returns the container ID based on the container's DBID. |
| `CON_UID_TO_ID` (container\_uid) | Returns the container ID based on the container's unique identifier (UID). |
| `CON_GUID_TO_ID` (container\_guid) | Returns the container ID based on the container's globally unique identifier (GUID). |
| `CON_ID_TO_CON_NAME` (container\_id) | Returns the container name based on the container ID. |
| `CON_ID_TO_DBID` (container\_id) | Returns the container's DBID based on the container ID. |
| `CON_ID_TO_GUID` (container\_id) | Returns the container's globally unique identifier (GUID) based on the container ID. |
| `CON_ID_TO_UID` (container\_id) | Returns the container’s unique identifier (UID) based on the container ID. |

The `V$CONTAINERS` view shows the name, DBID, UID, and GUID for each container in a CDB.

Example 15-40 Returning the Container ID Based on the Container Name

```
SELECT CON_NAME_TO_ID('HRPDB') FROM DUAL;
```

Example 15-41 Returning the Container ID Based on the Container DBID

```
SELECT CON_DBID_TO_ID(2226957846) FROM DUAL;
```

Example 15-42 Returning the Container Name Based on the Container ID

```
SELECT CON_ID_TO_CON_NAME(4) FROM DUAL;
```

**Parent topic:** Monitoring Containers in a CDB

#### Listing the Modifiable Initialization Parameters in PDBs

In a CDB, some initialization parameters apply to the root and to all PDBs. When such an initialization parameter is changed, it affects the entire CDB. You can set other initialization parameters to different values in each container.

For example, you might have a parameter set to one value in the root, set to another value in one PDB, and set to yet another value in a second PDB.

The query in this section lists the initialization parameters that you can set independently in each PDB.

To list the initialization parameters that are modifiable in each container:

1. In SQL\*Plus, access a container.
	See " About Container Access in a CDB ".
2. Run the following query:
	```
	SELECT NAME FROM V$SYSTEM_PARAMETER
	  WHERE ISPDB_MODIFIABLE = 'TRUE'
	  ORDER BY NAME;
	```

If an initialization parameter listed by this query is not set independently for a PDB, then the PDB inherits the parameter value of the root.

- Viewing the History of PDBs  
	The `CDB_PDB_HISTORY` view shows the history of the PDBs in a CDB. It provides information about when and how each PDB was created and other information about each PDB's history.

See Also:

- " Modifying a CDB with ALTER SYSTEM "
- " [Modifying a PDB at the System Level](administering-pdbs-with-sql-plus.md) "

**Parent topic:** Monitoring Containers in a CDB

##### Viewing the History of PDBs

The `CDB_PDB_HISTORY` view shows the history of the PDBs in a CDB. It provides information about when and how each PDB was created and other information about each PDB's history.

To view the history of each PDB:

1. In SQL\*Plus, ensure that the current container is the root.
	See " Accessing a Container in a CDB with SQL\*Plus ".
2. Query `CDB_PDB_HISTORY` view.

Example 15-43 Viewing the History of PDBs

This example shows the following information about each PDB's history:

- The `DB_NAME` field shows the CDB that contained the PDB.
- The `CON_ID` field shows the container ID of the PDB.
- The `PDB_NAME` field shows the name of the PDB in one of its incarnations.
- The `OPERATION` field shows the operation performed in the PDB's history.
- The `OP_TIMESTAMP` field shows the date on which the operation was performed.
- If the PDB was cloned in an operation, then the `CLONED_FROM_PDB` field shows the PDB from which the PDB was cloned.
```
COLUMN DB_NAME FORMAT A10
COLUMN CON_ID FORMAT 999
COLUMN PDB_NAME FORMAT A15
COLUMN OPERATION FORMAT A16
COLUMN OP_TIMESTAMP FORMAT A10
COLUMN CLONED_FROM_PDB_NAME FORMAT A15
 
SELECT DB_NAME, CON_ID, PDB_NAME, OPERATION, OP_TIMESTAMP, CLONED_FROM_PDB_NAME
  FROM CDB_PDB_HISTORY
  WHERE CON_ID > 2
  ORDER BY CON_ID;
```

Sample output:

```
DB_NAME    CON_ID PDB_NAME        OPERATION        OP_TIMESTA CLONED_FROM_PDB
---------- ------ --------------- ---------------- ---------- ---------------
NEWCDB          3 HRPDB           CREATE           10-APR-12  PDB$SEED
NEWCDB          4 SALESPDB        CREATE           17-APR-12  PDB$SEED
NEWCDB          5 TESTPDB         CLONE            30-APR-12  SALESPDB
```

Note:

When the current container is a PDB, the `CDB_PDB_HISTORY` view shows the history of the current PDB only. A local user whose current container is a PDB can query the `DBA_PDB_HISTORY` view and exclude the `CON_ID` column from the query to view the history of the current PDB.

See Also:

" About the Current Container "