---
title: "Administrator’s Guide"
book: "Multitenant Administrator's Guide"
doc_id: E96136-19
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/multi/administering-a-cdb-with-sql-plus.html
tags:
  - oracle
  - 19c
  - multitenant-administrators-guide
---

## 13 Administering a CDB

Administering a multitenant container database (CDB) includes tasks such as accessing a container, modifying a CDB, executing DDL statements, and running Oracle-supplied SQL scripts.

Note:

You can complete the tasks in this chapter using SQL\*Plus or Oracle SQL Developer.

- About CDB Administration  
	Administering a CDB is similar to administering a non-CDB, with some differences.
- Accessing Containers in a CDB  
	You can connect to a container by using the SQL\*Plus `CONNECT` command. Alternatively, you can switch into a container with an `ALTER SESSION SET CONTAINER` SQL statement.
- Modifying a CDB at the System Level  
	You can set initialization parameters at the CDB level. In some cases, you can override these parameters at the PDB level.
- Modifying Containers When Connected to the CDB Root  
	You can modify the entire CDB or the root with the `ALTER DATABASE` statement.
- Executing SQL in a Different Container  
	To execute SQL in a different container, use the `CONTAINERS` clause for DML or the `CONTAINER` clause for DDL.
- Shutting Down a CDB Instance  
	You can shut down a CDB instance in the same way that you shut down a non-CDB instance.

See Also:

" [Tools for a Multitenant Environment](overview-of-managing-a-multitenant-environment.md) "

**Parent topic:** [Administering a Multitenant Environment](managing-a-multitenant-environment.md)

### About CDB Administration

Administering a CDB is similar to administering a non-CDB, with some differences.

Most differences occur because some administrative tasks apply to the entire CDB, whereas others apply to specific containers.

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
- Overview of Oracle Multitenant with Oracle RAC  
	Oracle Multitenant is an option with Oracle Database 12c that simplifies consolidation, provisioning, upgrades, and more.

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
- " [Determining the Current Container ID or Name](viewing-information-about-cdbs-and-pdbs-with-sql-plus.md) "
- " [Namespaces in a CDB](overview-of-the-multitenant-architecture.md) "
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=SQLRF06117)
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=DBSEG754)

**Parent topic:** About CDB Administration

#### About Administrative Tasks in a CDB

Common users perform administrative tasks for a CDB.

A common user has a single identity and can log in to the CDB root, any application root, PDB, or application PDB in which it has privileges. Some tasks, such as starting up a CDB instance, can be performed only by a common user.

Other administrative tasks are the same for a CDB and a non-CDB. The following table describes some of these tasks and provides pointers to the relevant documentation.

Table 13-1 Administrative Tasks Common to CDBs and Non-CDBs

| Task | Description | Additional Information |
| --- | --- | --- |
| Starting up a CDB instance | To start a CDB instance, the current user must be a common user whose current container is the CDB root.  When you open a CDB, the CDB root is opened, but its other containers are mounted. Use the `ALTER PLUGGABLE DATABASE` statement to modify the open mode of one or more containers. | [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ADMIN-GUID-203404B5-5157-4F29-A241-B8ABC4753819) for information about starting up a database  " [Modifying the Open Mode of PDBs](administering-pdbs-with-sql-plus.md) "  " [Modifying a PDB with the ALTER PLUGGABLE DATABASE Statement](administering-pdbs-with-sql-plus.md) "  " About the Current Container " |
| Managing processes | A CDB has one set of background processes shared by the CDB root and all containers. | [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ADMIN-GUID-9B3A136E-D275-417B-B6F4-59A45D42655F) for information about managing processes |
| Managing memory | A CDB has a single system global area (SGA) and a single aggregate program global area (PGA). The memory required by a CDB is the sum of the memory requirements for all containers that will be part of the CDB. | [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ADMIN-GUID-BEABE53D-8058-4834-B99B-5C80A8AD5B06) for information about managing memory |
| Managing security | You can create and drop common users, application common users, and local users in a CDB. You can also grant privileges to and revoke privileges from these users. You can also manage the `CONTAINER_DATA` attributes of common users and application common users.  In addition, grant the following roles to the appropriate users:  - Grant the `CDB_DBA` role to CDB administrators. - Grant the `PDB_DBA` role to application container administrators and PDB administrators. | [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=DBSEG573) |
| Monitoring errors and alerts | A CDB has one alert log for the entire CDB. The name of an application container, PDB, or application PDB is included in records in trace files, when appropriate. | [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ADMIN-GUID-E5F89E8E-7FBC-47DD-BA5D-96AFD9CE4BC7) for information about monitoring errors and alerts |
| Managing diagnostic data | In a CDB, you can use the Oracle Database fault diagnosability infrastructure and the Automatic Diagnostic Repository (ADR). | [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ADMIN-GUID-8DEB1BE0-8FB9-4FB2-A19A-17CF6F5791C3) for information about managing diagnostic data |
| Managing control files | A CDB has one control file. | [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ADMIN-GUID-5F6F9382-6921-4992-9789-E63B18E99C5F) for information about managing control files |
| Managing the online redo log and the archived redo log files | A CDB has one online redo log and one set of archived redo log files. | [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ADMIN-GUID-BC1F1762-0BB1-4218-B7AF-6160C395AAE4) for information about managing the redo log  [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ADMIN-GUID-5EE4AC49-E1B2-41A2-BEE7-AA951EAAB2F3) for information about managing archived redo log files |
| Managing tablespaces | You can create, modify, and drop tablespaces and temporary tablespaces for the CDB root and for individual containers. You can also specify a default tablespace, default tablespace type, and a default temporary tablespace for the CDB root. The CDB root has its own set of Oracle-supplied tablespaces, such as the `SYSTEM` tablespace, and other containers have their own set of Oracle-supplied tablespaces. | [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ADMIN-GUID-1C162C60-6698-44F2-B2A9-F3E2D2958D88) for information about managing tablespaces  " About Container Modification When Connected to CDB Root " |
| Managing data files and temp files | The CDB root has its own data files, and other containers have their own data files. In a CDB, you can manage data files and temp files in basically the same way you would manage them for a non-CDB. However, the following exceptions apply to CDBs:  - You can limit the amount of storage used by the data files for a container by using the `STORAGE` clause in a `CREATE PLUGGABLE DATABASE` or `ALTER PLUGGABLE DATABASE` statement. - There is a default temporary tablespace for the CDB root and for individual containers. | [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ADMIN-GUID-501A8889-3C18-4F99-B0B7-9095E981B970) for information about managing data files and temp files  " About Container Modification When Connected to CDB Root "  " [Storage Limits](overview-of-pdb-creation.md) "  " [Modifying a PDB at the Database Level](administering-pdbs-with-sql-plus.md) " |
| Managing undo | A CDB can run in local undo mode or shared undo mode. Local undo mode means that every container in the CDB uses local undo. Shared undo mode means that there is one active undo tablespace for a single-instance CDB, or for an Oracle RAC CDB, there is one active undo tablespace for each instance.  In a CDB, the `UNDO_MANAGEMENT` initialization parameter must be set to `AUTO`, and an undo tablespace is required to manage the undo data. | " Setting the Undo Mode in a CDB Using ALTER DATABASE "  [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ADMIN-GUID-2C865CF9-A8B5-4BF1-A451-E8C08D3611F0) for information about managing undo  " About the Current Container " |
| Moving data between containers | You can move data between containers using the same methods that you would use to move data between non-CDBs. For example, you can transport the data or use Data Pump export/import to move the data. | [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ADMIN-GUID-1901E9C3-8FCE-4D4E-AB65-34D703474E52) for information about transporting data  [Oracle Database Utilities](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=SUTIL100) |
| Using Oracle Managed Files | Using Oracle Managed files can simplify administration for both a CDB and a non-CDB. | [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ADMIN-GUID-4A3C4616-0D81-4BBA-8EAD-FCAA8AD5C15A) for information about using Oracle Managed Files |
| Using Transparent Data Encryption | Transparent Data Encryption is a feature that enables encryption of individual table columns before storing them in the data file, or enables encryption of entire tablespaces. In a CDB, each container has its own master key for Transparent Data Encryption, and, where applicable, the `ADMINISTER KEY MANAGEMENT` SQL statement enables key management at the CDB level and for individual containers. | [Oracle Database Advanced Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ASOAG-GUID-0E59AD1E-514A-4F93-9A1F-E5683A535A89)  " About the Current Container " |
| Using a standby database | Oracle Data Guard can configure a physical standby or a logical standby of a CDB. Data Guard operates on the entire CDB, not on individual containers in a CDB. | [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=GUID-5E73667D-4A56-445E-911F-1E99092DD8D7) |
| Using Oracle Database Vault | Oracle Database Vault common realms can be scoped to an application root on common objects. Database Vault common command rules can be scoped to either the CDB or an application root. Local realms and command rules can be locally scoped to individual PDBs or application PDBs. When Oracle Database Vault security objects are in the CDB root or an application root, enforcement of the security objects only applies to the containers that have Oracle Database Vault enabled. | [Oracle Database Vault Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=DVADM71131) |
| Dropping a database | When you drop a CDB, all containers in the CDB are dropped along with their data. These containers include the CDB root and PDB seed and all application containers, application seeds, PDBs, and application PDBs.  You can also drop individual application containers, application seeds, PDBs, and application PDBs with the `DROP PLUGGABLE DATABASE` statement. | [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ADMIN-GUID-92F8F1B3-9E04-46D2-A4E4-3CC788459A38) for information about dropping a database  " [Dropping a PDB](removing-a-pdb.md) " |

See Also:

" [Overview of the Multitenant Architecture](overview-of-the-multitenant-architecture.md) " for more information about the architecture of a CDB

**Parent topic:** About CDB Administration

#### About Using Manageability Features in a CDB

For each of Oracle Database's manageability features in a CDB, it is important to understand the data location and the data visibility.

When feature data resides in the CDB root, the data is not included when a PDB is unplugged. When the data resides in a PDB, however, the data remains both when the PDB is unplugged and when it is plugged in.

Generally, in a CDB, a common user can view data for the CDB root and for multiple PDBs when the common user's current container is the CDB root. A common user can view this data by querying container data objects. The specific data that is visible varies for the manageability features. A user whose current container is a PDB can view data for that PDB only.

The following table describes how the manageability features work in a CDB.

Table 13-2 Manageability Features in a CDB

| Manageability Feature | Data Location | Data Visibility | Additional Information |
| --- | --- | --- | --- |
| Active Session History (ASH)  ASH collects information about active database sessions. You can use this information to analyze and identify performance issues. | Most of the ASH data is stored in memory. A small percentage of the ASH data samples are stored in the CDB root.  ASH data related to a PDB is not included if the PDB is unplugged. | A common user whose current container is the CDB root can view ASH data for the CDB root and for PDBs.  A user whose current container is a PDB can view ASH data for the PDB only. | [Oracle Database 2 Day + Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=TDPPT065)  [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=TGDBA277) |
| Alerts  An alert is a notification of a possible problem. | Threshold settings that pertain to a PDB are stored in the PDB.  Alerts posted when thresholds are violated are enqueued into the alert queue in the CDB root.  Threshold settings that pertain to a PDB are included if the PDB is unplugged. Alerts related to a PDB are not included if the PDB is unplugged. | A common user whose current container is the CDB root can view alerts for the CDB root and for PDBs.  A user whose current container is a PDB can view alert thresholds and alerts for the PDB only. | [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ADMIN-GUID-E5F89E8E-7FBC-47DD-BA5D-96AFD9CE4BC7) for information about monitoring errors and alerts |
| Automated Database Maintenance Tasks  Automated database maintenance tasks are tasks that are started automatically at regular intervals to perform maintenance operations on the database. Automated tasks include automatic optimizer statistics collection, Automatic Segment Advisor tasks, and Automatic SQL Tuning Advisor tasks.  The `ENABLE_AUTOMATIC_MAINTENANCE_PDB` initialization parameter can enable or disable the running of automated maintenance tasks for all the PDBs in a CDB or for individual PDBs in a CDB.  The `AUTOTASK_MAX_ACTIVE_PDBS` initialization parameter limits the number of PDBs that can schedule automated maintenance tasks at the same time (during a maintenance window). | A user can schedule maintenance windows and enable or disable maintenance tasks for the current container only. If the current container is the CDB root, then the changes only apply to the CDB root. If the current container is a PDB, then the changes only apply to the PDB.  Data related to a PDB is stored in the PDB for automatic optimizer statistics collection and the Automatic Segment Advisor. This data is included if the PDB is unplugged.  Automatic SQL Tuning Advisor runs only in the CDB root. See the SQL Tuning Advisor row in this table for information about data collected by Automatic SQL Tuning Advisor. | See the appropriate row in this table for data visibility information about the following manageability features: automatic optimizer statistics collection, Optimizer Statistics Advisor, Automatic Segment Advisor, and Automatic SQL Tuning Advisor. | [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ADMIN-GUID-7F7C805E-BA64-43A5-9A09-FC259FFA9AA8) for information about managing automated database maintenance tasks  [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=REFRN-GUID-3ACE01FA-8342-4F35-94BB-955412B9C76A) for information about the `ENABLE_AUTOMATIC_MAINTENANCE_PDB` initialization parameter  [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=REFRN-GUID-5DC631A2-4CDD-4C1F-B337-184BFD4C29B8) for information about the `AUTOTASK_MAX_ACTIVE_PDBS` initialization parameter |
| Automatic Database Diagnostic Monitor (ADDM)  ADDM can diagnose the performance of a CDB or PDB and determine how identified problems can be resolved. | ADDM executions occur in a PDB or in the CDB root. ADDM analyzes data using one of the following sources:  - AWR data stored inside the PDB through an AWR snapshot taken inside the PDB - AWR data from a non-CDB, CDB root, or PDB that is imported into the AWR storage of a PDB - AWR data stored in the root container through an AWR snapshot taken in root  Before the start of the analysis, ADDM determines the source of the AWR data (PDB or CDB root) and applies the rules applicable to each data type.  Note: Automatic ADDM for a PDB is enabled only when automatic snapshots are enabled for the PDB. | A common user whose current container is the CDB root can review results for the entire CDB. The ADDM results can include information about multiple PDBs. ADDM results related to a PDB are not included if the PDB is unplugged. The ADDM results cannot be viewed when the current container is a PDB.  A user whose current container is a PDB can view ADDM results data for the current PDB only. The results exclude findings that apply to the CDB as a whole, for example, I/O problems relating to the buffer cache size. | [Oracle Database 2 Day DBA](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ADMQS102)  [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=TGDBA026) |
| Automatic Optimizer Statistics Collection  Automatic optimizer statistics collection gathers optimizer statistics for all schema objects in the database for which there are no statistics or only stale statistics. The statistics gathered by this task are used by the SQL query optimizer to improve the performance of SQL execution. | When an automatic optimizer statistics collection task gathers data for a PDB, it stores this data in the PDB. This data is included if the PDB is unplugged. | A common user whose current container is the CDB root can view optimizer statistics data for PDBs.  A user whose current container is a PDB can view optimizer statistics data for the PDB only. | " [Using Oracle Resource Manager for PDBs](using-oracle-resource-manager-for-pdbs-with-sql-plus.md) "  [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=TGSQL389) |
| Automatic Segment Advisor  The Automatic Segment Advisor identifies segments that have space available for reclamation and makes recommendations on how to defragment those segments. | When Automatic Segment Advisor gathers data for a PDB, it stores this data in the PDB. This data is included if the PDB is unplugged. | A common user whose current container is the CDB root can view Automatic Segment Advisor data for PDBs.  A user whose current container is a PDB can view the Automatic Segment Advisor data for the PDB only. | [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ADMIN-GUID-1F297567-4BEC-438E-9E13-683D2BB47F44) for information about reclaiming unused space  " [Using Oracle Resource Manager for PDBs](using-oracle-resource-manager-for-pdbs-with-sql-plus.md) " |
| Automatic Workload Repository (AWR)  The AWR collects, processes, and maintains performance statistics for problem detection and self-tuning purposes. This data is stored in the database. The gathered data can be displayed in both reports and views. | AWR reports can be generated in the CDB root or in any PDB. AWR reports generated in the CDB root pertain to the entire CDB, while AWR reports generated when a PDB is the current container only pertain to that PDB.  AWR data generated in the CDB root is stored in the CDB root. AWR data generated in a PDB is stored in the PDB.  When a PDB is unplugged, AWR data stored in the CDB root is not included.  When a PDB is unplugged, AWR data stored in the PDB is included. | A common user whose current container is the CDB root can view AWR data for the CDB root and for PDBs.  A user whose current container is a PDB can view AWR data for the PDB only. | [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=TGDBA169) |
| Database Replay  Database Replay is a feature of Oracle Real Application Testing. Database Replay captures the workload for a CDB or PDB and replays it exactly on a test database. | Capture files are always stored in operating system files, regardless of whether the capture and replay is at the CDB level or PDB level. | For CDB-level workloads, a common user whose current container is the CDB root can view database capture and replay information. For PDB-level workloads, a local or common PDB administrator with the `SELECT_CATALOG_ROLE` privilege can view this information in `DBA_WORKLOAD_CAPTURES` and `DBA_WORKLOAD_REPLAYS`. | [Oracle Database Testing Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=RATUG4080) |
| Optimizer Statistics Advisor  Optimizer Statistics Advisor analyzes how statistics are being gathered and suggests changes that can be made to fine tune statistics collection. | Data related to a PDB is stored in the PDB for Optimizer Statistics Advisor. This data is included if the PDB is unplugged. | A common user whose current container is the CDB root can view Optimizer Statistics Advisor data for PDBs.  A user whose current container is a PDB can view the Optimizer Statistics Advisor data for the PDB only. | [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=TGSQL-GUID-054F4B76-DD57-46EE-98EA-0FF04F49D1B3) |
| SQL Management Base (SMB)  SMB stores statement logs, plan histories, SQL plan baselines, and SQL profiles in the data dictionary. | SMB data related to a PDB is stored in the PDB. The SMB data related to a PDB is included if the PDB is unplugged. | A common user whose current container is the CDB root can view SMB data for PDBs.  A user whose current container is a PDB can view the SMB data for the PDB only. | [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=TGSQL631) |
| SQL Performance Analyzer (SPA)  SPA can analyze the SQL performance impact of SQL tuning and other system changes. SPA is often used with Database Replay. | A common user whose current container is the CDB root can run SPA for any PDB. In this case, the SPA results data is stored in the CDB root and is not included if the PDB is unplugged.  A user whose current container is a PDB can run SPA on the PDB. In this case, the SPA results data is stored in the PDB and is included if the PDB is unplugged. | A common user whose current container is the CDB root can view SPA results data for PDBs.  A user whose current container is a PDB can view the SPA results data for the PDB only. | [Oracle Database Testing Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=RATUG239) |
| SQL Tuning Sets (STS)  An STS is a database object that includes one or more SQL statements along with their execution statistics and execution context, and could include a user priority ranking.  You can use an STS to tune a group of SQL statements or test their performance using SPA. | An STS can be stored in the CDB root or in any PDB. If it is stored in the CDB root, then you can load SQL statements from any PDB into it.  When a PDB is unplugged, an STS stored in the CDB root is not included, even if the STS contains SQL statements from the PDB.  When a PDB is unplugged, an STS stored in the PDB is included. | A common user whose current container is the CDB root can view STS data stored in the CDB root only.  A user whose current container is a PDB can view STS data for the PDB only. | [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=TGSQL516) |
| SQL Tuning Advisor  SQL Tuning Advisor optimizes SQL statements that have been identified as high-load SQL statements. | Automatic SQL Tuning Advisor data is stored in the CDB root. It might have results about SQL statements executed in a PDB that were analyzed by the advisor, but these results are not included if the PDB is unplugged.  A common user whose current container is the CDB root can run SQL Tuning Advisor manually for SQL statements from any PDB. When a statement is tuned, it is tuned in any container that runs the statement.  A user whose current container is a PDB can also run SQL Tuning Advisor manually for SQL statements from the PDB. When SQL Tuning Advisor is run manually from a PDB, the results are stored in the PDB from which it is run. In this case, a statement is tuned only for the current PDB, and the results related to a PDB are included if the PDB is unplugged. | When SQL Tuning Advisor is run automatically, the results are visible only to a common user whose current container is the CDB root. These results cannot be viewed when the current container is a PDB.  When SQL Tuning Advisor is run manually by a user whose current container is a PDB, the results are only visible to a user whose current container is that PDB. | [Oracle Database 2 Day + Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=TDPPT160)  [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=TGSQL540) |

To run SPA or SQL Tuning Advisor for SQL statements from a PDB, a common user must have the following privileges:

- Common `SET CONTAINER` privilege or local `SET CONTAINER` privilege in the PDB
- The privileges required to execute the SQL statements in the PDB

See Also:

- " About the Current Container "
- " [About CDB and Container Information in Views](viewing-information-about-cdbs-and-pdbs-with-sql-plus.md) " for an overview of container data objects
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=DBSEG803) for detailed information about container data objects

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

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ADMIN-GUID-1C162C60-6698-44F2-B2A9-F3E2D2958D88) for information about managing tablespaces
- " [Unplugging a PDB from a CDB](removing-a-pdb.md) "
- " Modifying an Entire CDB Using ALTER DATABASE "
- " Modifying the CDB Root Using ALTER DATABASE "

**Parent topic:** About Managing Tablespaces in a CDB

#### About Managing Database Objects in a CDB

In a CDB, different containers can contain different database objects.

An Oracle database stores database objects, such as tables, indexes, and directories. Database objects that are owned by a schema are called schema objects, while database objects that are not owned by a schema are called nonschema objects. The root and PDBs contain schemas, and schemas contain schema objects. The root and PDBs can also contain nonschema objects, such as users, roles, tablespaces, directories, and editions.

In a CDB, the root contains Oracle-supplied schemas and database objects. Oracle-supplied common users, such as `SYS` and `SYSTEM`, own these schemas and common database objects. They can also own local objects, both in the root and in a PDB.

You can create common users in the root to administer containers in the CDB. User-created common users can create database objects in the root. Oracle recommends that, in the root, schemas owned by user-created common users contain only database triggers and the objects used in their definitions. A user-created common user can also own any type of local object in a PDB.

You can create local users in a PDB. A local user in a PDB can create schema objects and nonschema objects in the PDB. You cannot create local users in the root.

Name resolution in a CDB is similar to name resolution in a non-CDB, except that names are resolved in the context of the dictionary of the user's current container.

See Also:

- " About the Current Container "
- " [Overview of Common and Local Users in a CDB](overview-of-the-multitenant-architecture.md) "
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ADMIN-GUID-5BEEEA18-8606-48CA-B51A-34FD301BF93B) for information about managing schema objects
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=SQLRF20003) for information about schema objects and nonschema objects
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=DBSEG573) for information about creating common users and local users

**Parent topic:** About CDB Administration

#### About Flashing Back a PDB

You can use the `FLASHBACK PLUGGABLE DATABASE` statement to return a PDB to a past time or system change number (SCN).

You can create restore points for a PDB and flash back the PDB to the restore point without affecting the CDB or other PDBs.

Note:

[Oracle Database Backup and Recovery User’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=BRADV-GUID-A2146E48-16FC-40CC-B25D-902DEB93CB75)

**Parent topic:** About CDB Administration

#### About Restricting PDB Users for Enhanced Security

There are several ways to restrict PDB users for enhanced security.

A PDB lockdown profile restricts the features and options available to users in a PDB. The `PDB_OS_CREDENTIAL` initialization parameter can specify a unique operating system user for a PDB to limit operating system access. Also, when the `PATH_PREFIX` and `CREATE_FILE_DEST` clauses are specified during PDB creation, they limit file system access.

- PDB Lockdown Profiles  
	When identities are shared between PDBs, elevated privileges might exist. You can use lockdown profiles to prevent this elevation of privileges.
- The PDB\_OS\_CREDENTIAL Initialization Parameter  
	When the database accesses an external procedure with the `extproc` agent, the `PDB_OS_CREDENTIAL` initialization parameter determines the identity of the operating system user employed when interacting with the operating system from a PDB.
- The PATH\_PREFIX and CREATE\_FILE\_DEST PDB Creation Clauses  
	The `PATH_PREFIX` clause of `CREATE PLUGGABLE DATABASE` ensures that all directory object paths associated with the PDB are restricted to the specified directory or its subdirectories.

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

- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=DBSEG-GUID-AB5E62DB-7E2A-4B5A-BA96-A2BD2DF15275) for complete information about lockdown profiles
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=GUID-1CDEC3A3-F3F1-4279-9370-36AACF416E0A) for more information about the `CREATE LOCKDOWN PROFILE` statement
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=REFRN-GUID-27072E94-1E1D-4BB0-AEAE-D7AFDC02E0A1) for more information about the `PDB_LOCKDOWN` initialization parameter

**Parent topic:** About Restricting PDB Users for Enhanced Security

##### The PDB\_OS\_CREDENTIAL Initialization Parameter

When the database accesses an external procedure with the `extproc` agent, the `PDB_OS_CREDENTIAL` initialization parameter determines the identity of the operating system user employed when interacting with the operating system from a PDB.

Using an OS user described by a credential whose name is specified as a value of the `PDB_OS_CREDENTIAL` initialization parameter can ensure that operating system interactions are performed as a less powerful user. In this way, the feature protects data belonging to one PDB from being accessed by users connected to another PDB. A credential is an object that is created using the `CREATE_CREDENTIAL` procedure in the `DBMS_CREDENTIAL` package.

The Oracle OS user is usually a highly privileged user. Using this account for operating system interactions is not recommended. Also, using the same OS user for operating system interactions from different PDBs might compromise data belonging to a given PDB.

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ADMIN-GUID-C34E01D5-97AC-4FC3-974D-268C0A2F4EC7) for information about managing processes for external procedures
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=REFRN-GUID-E563FDDA-6840-42CC-944D-5B0FD60C9003) for more information about the `PDB_OS_CREDENTIAL` initialization parameter
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ARPLS-GUID-D5791B72-E0F6-4C41-AD3E-DDEDFFCA7D0C)

**Parent topic:** About Restricting PDB Users for Enhanced Security

##### The PATH\_PREFIX and CREATE\_FILE\_DEST PDB Creation Clauses

The `PATH_PREFIX` clause of `CREATE PLUGGABLE DATABASE` ensures that all directory object paths associated with the PDB are restricted to the specified directory or its subdirectories.

`PATH_PREFIX` also ensures that the following files associated with the PDB are restricted to specified directory:

- The Oracle XML repository for the PDB
- Files created with a `CREATE PFILE` statement
- The export directory for Oracle wallets
- Library object created with a `CREATE LIBRARY` statement

Note:

The library must use a directory object. If a PDB uses a predefined `PATH_PREFIX`, attempts to use a library object that does not use a directory object result in an `ORA-65394` error. The library object is not invalidated, but to make it usable you must recreate it using a directory object.

The `CREATE_FILE_DEST` clause of the `CREATE PLUGGABLE DATABASE` statement ensures that all the database files belonging to the PDB are restricted to the specified directory and its subdirectories. The clause enables Oracle Managed Files for the PDB and specifies the default file system directory or Oracle ASM disk group for the PDB files.

See Also:

- " [Restrictions on PDB File Locations](overview-of-pdb-creation.md) "
- " [CREATE\_FILE\_DEST Clause](overview-of-pdb-creation.md) "

**Parent topic:** About Restricting PDB Users for Enhanced Security

#### Overview of Oracle Multitenant with Oracle RAC

Oracle Multitenant is an option with Oracle Database 12c that simplifies consolidation, provisioning, upgrades, and more.

It is based on an architecture that allows a multitenant container database (CDB) to hold several pluggable databases (PDBs). You can adopt an existing database as a PDB without having to change the application tier. In this architecture, Oracle RAC provides the local high availability that is required when consolidating various business-critical applications on one system.

When using PDBs with Oracle RAC, the multitenant CDB is based on Oracle RAC. You can make each PDB available on either every instance of the Oracle RAC CDB or a subset of instances. In either case, access to and management of the PDBs are regulated using dynamic database services, which will also be used by applications to connect to the respective PDB, as they would in a single instance Oracle database using Oracle Net Services for connectivity.

You can isolate PDBs to prevent certain operations from being performed on or within a particular PDB that may interfere with other PDBs sharing the same Oracle RAC database or database instance. PDB isolation allows for a higher degree of consolidation using Oracle Multitenant.

If you create an Oracle RAC database as a CDB and plug one or more PDBs into the CDB, then, by default, a PDB is not started automatically on any instance of the Oracle RAC CDB. With the first dynamic database service assigned to the PDB (other than the default database service which has the same name as the database name), the PDB is made available on those instances on which the service runs.

Whether a PDB is available on more than one instance of an Oracle RAC CDB, the CDB is typically managed by the services running on the PDB. You can manually enable PDB access on each instance of an Oracle RAC CDB by starting the PDB manually on that instance.

### Accessing Containers in a CDB

You can connect to a container by using the SQL\*Plus `CONNECT` command. Alternatively, you can switch into a container with an `ALTER SESSION SET CONTAINER` SQL statement.

- About Container Access in a CDB  
	You can use SQL\*Plus to access the root or a PDB in a CDB.
- Accessing a Container in a CDB  
	Access a container in a CDB with SQL\*Plus by issuing a `CONNECT` or `ALTER SESSION` command.

**Parent topic:** Administering a CDB

#### About Container Access in a CDB

You can use SQL\*Plus to access the root or a PDB in a CDB.

Note:

This section assumes that you understand how to connect to a non-CDB in SQL\*Plus.

- Services in a CDB  
	Clients access the root or a PDB through database services.
- Session Limits in a CDB  
	The setting for the `SESSIONS` initialization parameter limits the total number of sessions available in a CDB, including the sessions connected to PDBs.
- User Names in a Multitenant Environment  
	Within each PDB, a user name must be unique with respect to other user names and roles in that PDB.
- How the Multitenant Option Affects Password Files for Administrative Users  
	In a multitenant environment, the password information for the local and common administrative users is stored in different locations.

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ADMIN-GUID-58A40F41-B611-4C0F-A6E3-D45A81515BF2) for information about submitting commands and SQL to the database
- [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=NETAG001) for information about configuring Oracle Net Services

**Parent topic:** Accessing Containers in a CDB

##### Services in a CDB

Clients access the root or a PDB through database services.

Database services have an optional `PDB` property. When a PDB is created, a new default service for the PDB is created automatically. The service has the same name as the PDB. With the service name, you can access the PDB using the easy connect syntax or the net service name from the `tnsnames.ora` file. Oracle Net Services must be configured properly for clients to access this service.

When a user connects using a service with a non-null `PDB` property, the user name is resolved in the context of the specified PDB. When a user connects without specifying a service or using a service name with a null `PDB` property, the user name is resolved in the context of the root. You can view the `PDB` property for a service by querying the `CDB_SERVICES` data dictionary view or by running the `config service` command in the SRVCTL utility.

Note:

When two or more CDBs on the same computer system use the same listener and two or more PDBs have the same service name in these CDBs, a connection that specifies this service name connects randomly to one of the PDBs with the service name. To avoid incorrect connections, ensure that all service names for PDBs are unique on the computer system, or configure a separate listener for each CDB on the computer system.

##### Session Limits in a CDB

The setting for the `SESSIONS` initialization parameter limits the total number of sessions available in a CDB, including the sessions connected to PDBs.

If the limit is reached for the CDB, then users cannot connect to PDBs. To ensure that one PDB does not use too many sessions, you can limit the number of sessions available to a PDB by setting the `SESSIONS` initialization parameter in the PDB.

See Also:

" [Listing the Modifiable Initialization Parameters in PDBs](viewing-information-about-cdbs-and-pdbs-with-sql-plus.md) "

**Parent topic:** About Container Access in a CDB

##### User Names in a Multitenant Environment

Within each PDB, a user name must be unique with respect to other user names and roles in that PDB.

Note the following restrictions:

- For common user names, names for user-created common users must begin with a common user prefix. By default, for CDB common users, this prefix is `C##`. For application common users, this prefix is an empty string. This means that there are no restrictions on the name that can be assigned to an application common user other than that it cannot start with the prefix reserved for CDB common users. For example, you could name a CDB common user `c##hr_admin` and an application common user `hr_admin`.
	The `COMMON_USER_PREFIX` parameter in `CDB$ROOT` defines the common user prefix. You can change this setting, but do so only with great care.
- For local user names, the name cannot start with `C##` (or `c##`).
- A user and a role cannot have the same name.

##### How the Multitenant Option Affects Password Files for Administrative Users

In a multitenant environment, the password information for the local and common administrative users is stored in different locations.

- For CDB administrative users: The password information (hashes of the password) for the CDB common administrative users to whom administrative privileges were granted in the CDB root is stored in the password file.
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

- Connecting to the Root Using the SQL\*Plus CONNECT Command  
	You can connect to the root in the same way that you connect to a non-CDB.
- Connecting to a PDB Using the SQL\*Plus CONNECT Command  
	To connect to a PDB with the SQL\*Plus `CONNECT` command, you can use easy connect or a net service name.

**Parent topic:** Accessing a Container in a CDB

###### Connecting to the Root Using the SQL\*Plus CONNECT Command

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
2. Start SQL\*Plus with the `/NOLOG` argument:
	```
	sqlplus /nolog
	```
3. Issue a SQL\*Plus `CONNECT` command to connect to the root, as shown in the following examples.

Example 13-1 Connecting to the Root with a Local Connection

This example connects to the root in the local CDB as user `SYSTEM`. SQL\*Plus prompts for the `SYSTEM` user password.

```
connect system
```

Example 13-2 Connecting to the Root with Operating System Authentication

This example connects locally to the root with the `SYSDBA` administrative privilege with operating system authentication.

```
connect / as sysdba
```

Example 13-3 Connecting to the Root with a Net Service Name

Assume that clients are configured to have a net service name for the root in the CDB. For example, the net service name can be part of an entry in a `tnsnames.ora` file.

This example connects as common user `c##dba` to the database service designated by the net service name `mycdb`. SQL\*Plus prompts for the `c##dba` user password.

```
connect c##dba@mycdb
```

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ADMIN-GUID-58A40F41-B611-4C0F-A6E3-D45A81515BF2) for information about submitting commands and SQL to the database

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

Example 13-4 Connecting to a PDB

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

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ADMIN-GUID-991445B9-EA9E-481E-A33D-E737F2DD9CFB) for information about submitting the SQL\*Plus `CONNECT` command

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
	For example, you can use this statement for connection pooling with PDBs for a multitenant application. A multitenant application uses a single instance of the software on a server to serve multiple customers (tenants). In a non-CDB, multitenant is typically supported by adding an extra column that identifies the tenant to every table used by the application, and tenants check out connections from a connection pool. In a CDB with PDBs, each tenant can have its own PDB, and you can use the `ALTER SESSION SET CONTAINER` statement in a connection pooling configuration.
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
	If the open mode of the root should be changed, then follow the instructions in [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ADMIN-GUID-2042AAE4-DAE5-4CD4-89E9-B9DE3A8A2AA1) about altering database availability to change the open mode.
	If the open mode of the PDB should be changed, then follow the instructions in " [Modifying the Open Mode of PDBs](administering-pdbs-with-sql-plus.md) " to change the open mode.
	The open mode of the root imposes limitations on the open mode of PDBs. For example, the root must be open before any PDBs can be open. Therefore, you might need to change the open mode of the root before changing the open mode of a PDB.
3. If you are switching to a specific service, then ensure that the service is running.
	To check the active status of the service, query the `V$ACTIVE_SERVICES` view when the current container is the CDB root.
	If the service is not running, then use the SRVCTL utility or the `DBMS_SERVICE` package to start the service.
4. Run the `ALTER SESSION SET CONTAINER` statement and specify the container to which you want to switch.
	Include the `SERVICE` clause to switch to a specific application service.

The following examples switch to various containers using `ALTER` `SESSION`.

Example 13-5 Switching to the PDB salespdb and Using the salesrep Service

```
ALTER SESSION SET CONTAINER = salespdb SERVICE = salesrep;
```

Example 13-6 Switching to the PDB salespdb and Using the Default Service

```
ALTER SESSION SET CONTAINER = salespdb;
```

Example 13-7 Switching to the CDB Root

```
ALTER SESSION SET CONTAINER = CDB$ROOT;
```

Example 13-8 Switching to the PDB Seed

```
ALTER SESSION SET CONTAINER = PDB$SEED;
```

Example 13-9 Switching Services Using a Dummy Service in the CDB Root

To design connection pooling that switches the container and the service, one method is to create a dummy service in the CDB root and set all required service attributes on this dummy service (for example, `drain_timeout`, TAF or Application Continuity). The service attributes must match across the CDB root and the PDB. To use this method, complete the following steps:

1. Connect to the dummy service when first creating the connection pool and when creating new connections.
2. As services are added to each PDB, set the same attributes on these real services.
3. When an application requires a connection, complete one of the following actions:
	- Create a new connection to the dummy service, and switch to the PDB and service.
		- Borrow a free connection in the pool and switch to the PDB and service.
		You do not need to return to the CDB root when switching across PDBs.

You do not need to return to the CDB root when switching across PDBs.

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ADMIN-GUID-BB76E57C-3F16-4C85-AEF6-BA14FC1B4777) for information about database resident connection pooling

**Parent topic:** Accessing a Container in a CDB

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

Example 13-10 Setting an Initialization Parameter for All Containers

This `ALTER SYSTEM SET` statement sets the `OPEN_CURSORS` initialization parameter to `200` for the all containers and sets the inheritance property to `TRUE` in each PDB.

```
ALTER SYSTEM SET OPEN_CURSORS = 200 CONTAINER = ALL;
```

Example 13-11 Setting an Initialization Parameter for the Root

This `ALTER SYSTEM SET` statement sets the `OPEN_CURSORS` initialization parameter to `200` for the root and for PDBs with an inheritance property of true for the parameter.

```
ALTER SYSTEM SET OPEN_CURSORS = 200 CONTAINER = CURRENT;
```

See Also:

- " [Modifying a PDB at the System Level](administering-pdbs-with-sql-plus.md) "
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=SQLRF53143) for more information about the `ALTER SYSTEM SET` statement

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
	In this case, the `ALTER DATABASE` statement works the same as in a non-CDB. When an `ALTER DATABASE` statement with the `RENAME GLOBAL_NAME` clause modifies the domain of a CDB, it affects the domain of each PDB with a domain that defaults to that of the CDB. The `ALTER PLUGGABLE DATABASE` statement with the pdb\_change\_state clause modifies the open mode of one or more PDBs.
- Connected to a PDB
	In this case, the `ALTER DATABASE` and `ALTER PLUGGABLE DATABASE` statements modify the current PDB only.

The following table lists which containers are modified by clauses in `ALTER DATABASE` and `ALTER PLUGGABLE DATABASE` statements.

Table 13-3 Statements That Modify Containers in a CDB

| Modify Entire CDB | Modify Root Only | Modify One or More PDBs |
| --- | --- | --- |
| When connected as a common user whose current container is the root, `ALTER DATABASE` statements with the following clauses modify the entire CDB:  - [startup\_clauses](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=SQLRF52389) - [recovery\_clauses](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=SQLRF52390) - [logfile\_clauses](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=SQLRF52402) - [controlfile\_clauses](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=SQLRF52410) - [standby\_database\_clauses](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=SQLRF52412) - [instance\_clauses](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=SQLRF52423) - [security\_clause](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=SQLRF52424) - [`RENAME GLOBAL_NAME`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=SQLRF52547) clause - [`ENABLE BLOCK CHANGE TRACKING`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=SQLRF52549) clause - [`DISABLE BLOCK CHANGE TRACKING`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=SQLRF52550) clause | When connected as a common user whose current container is the root, `ALTER DATABASE` statements with the following clauses modify the root only:  - [database\_file\_clauses](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=SQLRF52396) - [`DEFAULT EDITION`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=SQLRF52540) clause - [`DEFAULT TABLESPACE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=SQLRF52543) clause - [`DEFAULT TEMPORARY TABLESPACE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=SQLRF52544) clause  `ALTER DATABASE` statements with the following clauses modify the root and set default values for PDBs:  - [flashback\_mode\_clause](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=SQLRF52421) - [`SET DEFAULT {BIGFILE\|SMALLFILE} TABLESPACE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=SQLRF52542) clause - [set\_time\_zone\_clause](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=SQLRF52421)  You can use these clauses to set nondefault values for specific PDBs. | When connected as a common user whose current container is the root, `ALTER PLUGGABLE DATABASE` statements with the following clause can modify the open mode of one or more PDBs:  - [pdb\_change\_state](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=SQLRF55686)  When the current container is a PDB, `ALTER PLUGGABLE DATABASE` statements with this clause can modify the open mode of the current PDB.  When connected as a common user whose current container is the root, `ALTER PLUGGABLE DATABASE` statements with the following clause can preserve or discard the open mode a PDB when the CDB restarts:  - [pdb\_save\_or\_discard\_state](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=SQLRF55686) |

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

Example 13-12 Backing Up the Control File for a CDB

The following `ALTER DATABASE` statement uses a recovery\_clause to back up a control file.

```
ALTER DATABASE BACKUP CONTROLFILE TO '+DATA/dbs/backup/control.bkp';
```

Example 13-13 Adding a Redo Log File to a CDB

The following `ALTER DATABASE` statement uses a logfile\_clause to add redo log files.

```
ALTER DATABASE cdb ADD LOGFILE
  GROUP 4 ('/u01/logs/orcl/redo04a.log','/u02/logs/orcl/redo04b.log')
  SIZE 100M BLOCKSIZE 512 REUSE;
```

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=SQLRF00802)

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

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=SQLRF01403) for information about the required privileges

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

When the current container is the root, some `ALTER DATABASE` statements modify the root without directly modifying any of the PDBs. See the "Modify Root Only" column of Table 13-3 for a list of these statements.

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

Example 13-14 Changing the Default Permanent Tablespace for the Root

This `ALTER DATABASE` statement uses a `DEFAULT TABLESPACE` clause to set the default permanent tablespace to `root_tbs` for the root.

```
ALTER DATABASE DEFAULT TABLESPACE root_tbs;
```

Example 13-15 Bringing a Data File Online for the Root

This `ALTER DATABASE` statement uses a database\_file\_clause to bring the /u02/oracle/cdb\_01.dbf data file online.

```
ALTER DATABASE DATAFILE '/u02/oracle/cdb_01.dbf' ONLINE;
```

Example 13-16 Changing the Default Tablespace Type for the Root

This `ALTER DATABASE` statement uses a `SET DEFAULT TABLESPACE` clause to change the default tablespace type to bigfile for the root.

```
ALTER DATABASE SET DEFAULT BIGFILE TABLESPACE;
```

Example 13-17 Changing the Default Temporary Tablespace for the Root

This `ALTER DATABASE` statement uses a `DEFAULT TEMPORARY TABLESPACE` clause to set the default temporary tablespace to `root_temp` for the root.

```
ALTER DATABASE DEFAULT TEMPORARY TABLESPACE root_temp;
```

See Also:

- " [Modifying a PDB at the Database Level](administering-pdbs-with-sql-plus.md) "
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=SQLRF00802)

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

Example 13-18 Specifying the Default Container for DML Statements in a CDB

This example specifies that `PDB1` is the default container for DML statements in the CDB.

```
ALTER DATABASE CONTAINERS DEFAULT TARGET = (PDB1);
```

Example 13-19 Clearing the Default Container

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
- You can use the `CONTAINER` clause only with the DDL statements listed in Table 13-4.

Table 13-4 DDL Statements and the CONTAINER Clause in a CDB

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
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=SQLRF30041)
- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=CNCPT1732)
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=DBSEG589) for more information about managing users in a CDB
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=REFRN10354) for more information about the `COMMON_USER_PREFIX` initialization parameter

**Parent topic:** Executing DDL Statements in a CDB

##### Executing a DDL Statement in the Current Container

Specify `CURRENT` in the `CONTAINER` clause of a DDL statement to execute the statement in the current container.

The supported DDL statements are listed in Table 13-4.

The current user must be granted the required privileges to execute the DDL statement in the current container. For example, to create a user, the current user must be granted the `CREATE USER` system privilege in the current container.

To execute a DDL statement in the current container:

1. In SQL\*Plus, access a container.
	See " Accessing a Container in a CDB with SQL\*Plus ".
2. Execute the DDL statement with `CONTAINER` set to `CURRENT`.

A local user's user name cannot start with the prefix specified by the `COMMON_USER_PREFIX` initialization parameter. By default, in the CDB root, the prefix is `C##` or `c##`. An application root can specify its own prefix for an application container. In addition, a common user's name must consist only of ASCII characters. The specified tablespace must exist in the PDB.

Example 13-20 Creating Local User in a PDB

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

The supported DDL statements are listed in Table 13-4.

The following prerequisites must be met:

- The current user must be a common user.
- The current user must be granted the required privileges commonly to execute the DDL statement. For example, to create a user, the current user must be granted the `CREATE USER` system privilege commonly.

To execute a DDL statement in all containers in a CDB:

1. In SQL\*Plus, ensure that the current container is the root.
	See " About Container Access in a CDB ".
2. Execute the DDL statement with `CONTAINER` set to `ALL`.

A common user's user name must start with the prefix specified by the `COMMON_USER_PREFIX` initialization parameter. By default, in the CDB root, the prefix is `C##` or `c##`. An application root can specify its own prefix for an application container. In addition, a common user's name must consist only of ASCII characters. The specified tablespace must exist in the root and in all PDBs.

Example 13-21 Creating Common User in a CDB

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

- Unless you exclude the PDB seed when you run `catcon.pl`, the SQL script or SQL statement is run on the PDB seed.
- You can use the `catcon.pl` script to run scripts on both CDBs and non-CDBs.

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

Table 13-5 catcon.pl Parameters

| Parameter | Short Name | Description |
| --- | --- | --- |
| `--usr` | `-u` | Specifies the user name and password to connect to the root and the specified PDBs. Specify a common user with the required privileges to run the SQL script or the SQL statement. The default is " `/ AS SYSDBA` ". If no password is supplied, then `catcon.pl` prompts for a password. |
| `--int_usr` | `-U` | Specifies the user name and password to connect to the root and the specified PDBs. Specify a common user with the required privileges to perform internal tasks, such as querying CDB metadata. The default is `/ AS SYSDBA`. If no password is supplied, then `catcon.pl` prompts for a password. |
| `--script_dir` | `-d` | Directory that contains the SQL script. The default is the current directory. |
| `--log_dir` | `-l` | Directory into which `catcon.pl` writes log files. The default is the current directory. |
| `{--incl_con\|--excl_con}` | `{-c\|-C}` | The containers in which the SQL script is run or is not run.  The `--incl_con` parameter lists the containers in which the SQL script is run.  The `--excl_con` parameter lists the containers in which the SQL script is not run.  Specify containers in a space-delimited list of PDB names enclosed in single quotation marks.  The `--incl_con` and `--excl_con` parameters are mutually exclusive.  When this parameter is used, the `--app_con` parameter cannot be used. |
| `--echo` | `-e` | Sets echo `ON` while running the script. The default is echo `OFF`. |
| `--spool` | `-s` | Spools the output of every script into a file with the following name:  ``` log-file-name-base_script-name-without-extension_[container-name-if-any].default-extension ``` |
| `--error_logging` | `-E` | When set to `ON`, the default error logging table is used. `ON` is the default setting. When set to `ON`, errors are written to the table `SPERRORLOG` in the current schema in each container in which the SQL script runs. If this table does not exist in a container, then it is created automatically.  When a table other than `SPERRORLOG` is specified, errors are written to the specified table. The table must exist in each container in which the SQL script runs, and the current user must have the necessary privileges to perform DML operations on the table in each of these containers.  See [SQL\*Plus User's Guide and Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=SQPUG160) for more information about the error logging table. |
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

Example 13-22 Running the catblock.sql Script in All Containers in a CDB

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

Example 13-23 Running the catblock.sql Script in Specific PDBs

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

Example 13-24 Running the catblock.sql Script in All Containers Except for Specific PDBs

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

Example 13-25 Running a SQL Script with Command Line Parameters

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

Example 13-26 Running a SQL Statement in All Containers in a CDB

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
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ADMIN-GUID-D6146406-ADA2-443A-A843-137FA427ABED) for information about the `catblock.sql` script
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=REFRN005) for more information about SQL scripts

**Parent topic:** Running Oracle-Supplied SQL Scripts in a CDB

#### Executing Code in Containers Using the DBMS\_SQL Package

When you are executing PL/SQL code in a container in a CDB, and you want to execute one or more SQL statements in a different container, use the `DBMS_SQL` package to switch containers.

For example, you can use the `DBMS_SQL` package to switch containers when you need to perform identical actions in more than one container.

The following are considerations for using `DBMS_SQL` to switch containers:

- A transaction cannot span multiple containers.
	If the set of actions you must perform in the target container requires a transaction, then consider using an autonomous transaction and perform a commit or rollback as the last action.
- `SET` `ROLE` statements are not allowed.

Example 13-27 Performing Identical Actions in More Than One Container

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

- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ARPLS058) for more information about the `DBMS_SQL` package
- [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=LNPLS00609) for more information about autonomous transactions

**Parent topic:** Executing SQL in a Different Container

### Shutting Down a CDB Instance

You can shut down a CDB instance in the same way that you shut down a non-CDB instance.

Prerequisites

The following prerequisites must be met:

- The CDB instance must be mounted or open.
- The current user must be a common user with `SYSDBA`, `SYSOPER`, `SYSBACKUP`, or `SYSDG` administrative privilege. To shut down a CDB, you must exercise this privilege using `AS` `SYSDBA`, `AS` `SYSOPER`, `AS` `SYSBACKUP`, or `AS` `SYSDG`, respectively, at connect time.

To shut down a CDB:

1. In SQL\*Plus, ensure that the current container is the root.
	See " Connecting to a Container Using the SQL\*Plus CONNECT Command ".
2. Shut down the CDB instance.