---
title: "Backup and Recovery User's Guide"
book: "Database Backup and Recovery User's Guide"
doc_id: F31836-11
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/bradv/rman-recovering-tables-partitions.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-users-guide
---

Use the `RECOVER` command to recover tables and table partitions to a specified point-in-time.

### 22.1 Overview of Recovering Tables and Table Partitions

The RMAN `RECOVER` command enables you to recover tables and table partitions from RMAN backups.

Note:

There are other methods of recovering tables to a specified point in time such as Oracle Flashback and TSPITR. For more information about the scenarios in which these methods are useful and how to recover tables using these methods, see:

- [Performing Flashback and Database Point-in-Time Recovery](rman-performing-flashback-dbpitr.md)
- [Performing RMAN Tablespace Point-in-Time Recovery (TSPITR)](performing-rman-tspitr.md)

#### 22.1.1 Purpose of Recovering Tables and Table Partitions from RMAN Backups

RMAN enables you to recover one or more tables or table partitions to a specified point in time without affecting the remaining database objects. You can use previously-created RMAN backups to recover tables and table partitions to a specified point in time.

Recovering tables and table partitions from RMAN backups is useful in the following scenarios:

- You need to recover a very small number of tables to a particular point in time. In this situation, TSPITR is not the most effective solution because it moves all the objects in the tablespace to a specified point in time.
- You need to recover tables that have been logically corrupted or have been dropped and purged.
- Flashback Table is not possible because the desired point-in-time is older than available undo.
- You want to recover data that is lost after a DDL operation modified the structure of tables. Using Flashback Table is not possible because a DDL was run on the tables between the desired point in time and the current time. Flashback Table cannot rewind tables through structural changes such as a truncate table operation.

#### 22.1.2 Basic Concepts of Recovering Tables and Table Partitions from RMAN Backups

RMAN uses the `RECOVER` command to recover tables or table partitions to a specified point in time.

To recover tables and table partitions from an RMAN backup, you need to provide the following information:

- Names of tables or table partitions that must be recovered
- Point in time to which the tables or table partitions must be recovered
- Whether the recovered tables or table partitions must be imported into the target database

RMAN uses this information to automate the process of recovering the specified tables or table partitions. As part of the recovery process, RMAN creates an auxiliary database that is used to recover tables or table partitions to the specified point in time.

If the recovered tables or table partitions need to be renamed, mapped to a new tablespace, or mapped to a new schema, then you must specify the new names for the tables, tablespaces, or schemas.

##### 22.1.2.1 RMAN Backups Required to Recover Tables and Table Partitions

To recover tables or table partitions, you need a full backup of undo, `SYSTEM`, `SYSAUX`, and the tablespace that contains the tables or table partitions.

To recover a table, all partitions that contain the dependent objects of the table must be included in the recovery set. If the indexes or partitions for a table in tablespace `tbs1` are contained in tablespace `tbs2`, then you can recover the table only if tablepsace `tbs2` is also included in the recovery set.

To recover tables in a PDB, you need backups of the following:

- `SYSTEM`, `SYSAUX`, and undo tablespace of the root, CDB seed, and the PDB containing the tables
- Tablespace containing the tables or partitions

See Also:

Prerequisites for Recovering Tables and Table Partitions from RMAN Backups

##### 22.1.2.2 Steps Performed By RMAN to Recover Tables and Table Partitions

RMAN performs a series of steps while automating the process of recovering tables or table partitions from an RMAN backup.

The steps include the following:

1. Determines which backup contains the tables or table partitions that need to be recovered, based on the point in time specified for the recovery.
2. Determines if there is sufficient space on the target host to create the auxiliary instance that will be used during the table or partition recovery process.
	If the required space is not available, then RMAN displays an error and exits the recovery operation.
3. Creates an auxiliary database on the target host and recovers the specified tables or table partitions, until the specified point in time, into this auxiliary database.
	You can specify the location on the target host to which the recovered data files are stored in the auxiliary database.
4. Creates a Data Pump [export dump file](glossary.md) that contains the recovered tables or table partitions.
	You can specify the name and the location of the Data Pump export dump file used to store the metadata of the recovered tables or table partitions.
5. (Optional) Imports the Data Pump export dump file into the target instance.
	You can choose not to import the export dump file that contains the recovered tables or table partitions into the target database. If you do not import the export dump file as part of the recovery process, you must manually import it later using the Data Pump Import utility.
6. (Optional) Renames the recovered tables or table partitions in the target database.
	You can also import recovered objects into a tablespace or schema that is different from the one in which they originally existed.

#### 22.1.3 Guidelines for Recovering Tables and Table Partitions

You can follow guidelines for recovering tables and tables partitions from RMAN backups.

##### 22.1.3.1 Specify the Location of Auxiliary Database Files Created During Table Recovery

RMAN creates an auxiliary database that it uses during the process of recovering the specified tables or table partitions. Multiple techniques are available to specify the location of auxiliary database files.

On the target host that is used to store data files for the auxiliary database, use one of the following methods:

- `SET NEWNAME` command
	Use a `RUN` block that contains the `RECOVER` command and the required `SET                         NEWNAME` commands that rename data files.
- `AUXILIARY DESTINATION` clause in the `RECOVER` command
	This is the recommended method. When you use the `SET                         NEWNAME` command, if you omit the name of even one data file that is required during recovery process, the tables or table partitions cannot be recovered.

See Also:

- `RECOVER` command syntax in [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF140)
- `SET` command syntax in [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF153)

##### 22.1.3.2 Specify the Name and Location of the Data Pump Export Dump File

After recovering tables or table partitions to the specified point in time, RMAN creates a Data Pump export dump file that contains the recovered objects. You can either specify a name and location for this dump file or allow RMAN to use a default name and location.

- Use the `DATAPUMP DESTINATION` clause of the `RECOVER` command to specify the operating system directory in which the Data Pump export dump file is created.
	If you omit this clause, the dump file is stored in the location specified by the `AUXILIARY DESTINATION` parameter. If you do not specify an auxiliary destination, the dump file is stored in a default operating system-specific location. On Linux, this default location is `$ORACLE_HOME/dbs`. On Windows, the default location is `%ORACLE_HOME\database`.
- Use the `DUMP FILE` clause of the `RECOVER` command to specify the name of the Data Pump export dump file.
	If you omit this clause, RMAN uses a default operating system-specific name for the dump file. On Linux and Windows, the default dump file name is `tspitr_` `SID-of-clone_n``.dmp`, where `SID-of-clone` is the Oracle SID of the auxiliary database created by RMAN to perform the recovery and `n` is any randomly-generated number. If a file with the name specified by `DUMP FILE` exists in the location in which the dump file must be created, then the recover operation fails.

##### 22.1.3.3 Decide Whether to Import Recovered Tables and Table Partitions into the Target Database

You can choose not to import the recovered tables or table partitions.

By default, RMAN recovers the tables or table partitions to the specified point in time, creates an export dump file that contains these recovered objects, and imports them into the target database. To skip importing recovered objects into the target database, include the `NOTABLEIMPORT` clause in the `RESTORE` command. When you need the recovered objects, you must manually import the export dump file into your target database by using the Data Pump Import utility.

If an error occurs during the import operation, RMAN does not delete the export dump file at the end of the table recovery. This enables you to manually import the dump file.

##### 22.1.3.4 Rename the Recovered Tables and Table Partitions

Use the `REMAP TABLE` clause to rename recovered tables or table partitions in the target database.

If the target database contains a table with the same name as that of the recovered table, RMAN displays an error message indicating that you must rename the recovered table by using the `REMAP TABLE` clause.

When you recover table partitions, each table partition is recovered into a separate table. Use the `REMAP TABLE` clause to specify the table names into which each recovered partition must be imported. If you do not explicitly specify table names, RMAN generates table names by concatenating the recovered table name and partition name. The generated names are in the format `tablename_partitionname`. If a table with this name exists in the target database, then RMAN appends \_1 to the name. If this name too exists, then RMAN appends \_2 to the name and so on.

To import the recovered tables or table partitions into a tablespace that is different from the one in which these objects originally existed, use the `REMAP TABLESPACE` clause of the `RECOVER` command. Only the tables or table partitions that are being recovered are remapped, the existing objects are not changed.

Note:

When you use the `REMAP TABLE` clause, named constraints and indexes cannot be imported.

##### 22.1.3.5 Recover Tables and Partitions Into a New Schema

Recovering tables or table partitions into a different schema enables you to avoid name conflicts that may be caused by constraint, index, or trigger names that already existing in the source schema.

Starting with Oracle Database 12c Release 2 (12.2), you can recover tables or table partitions into a schema that is different from the source schema (the schema in which they originally existed). While recovering objects into a different schema, you can either retain their original names or rename them. You can rename tables and remap the schema in a single recovery operation. For example, you can recover the `HR.EMPLOYEES` table either into the `NEW_HR.EMPLOYEES` table, the `HR.NEW_EMPLOYEES` table, or the `NEW_HR.NEW_EMPLOYEES` table. The `REMAP TABLE` clause enables you to rename objects and recover them into a different schema.

During table recovery, use the `REMAP TABLE` clause of the `RECOVER TABLE` command to map the source schema to a new schema. The new schema must exist in the target database before you perform the recovery.

Note:

Table recovery is not supported on physical standby databases. For logical standby databases, objects that are recovered on the primary database are propagated to the logical standby.

See Also:

Example: Recovering a Table into a New Schema

#### 22.1.4 Limitations of Recovering Tables and Table Partitions from RMAN Backups

Recovering tables and table partitions from RMAN backups by using the `RECOVER` command is subject to certain limitations.

The limitations include the following:

- Tables and table partitions belonging to `SYS` schema cannot be recovered.
- Tables and table partitions from `SYSTEM` and `SYSAUX` tablespaces cannot be recovered.
- Tables and table partitions on standby databases cannot be recovered.
- Tables with named `NOT NULL` constraints cannot be recovered with the `REMAP` option.

### 22.2 Preparing to Recover Tables and Table Partitions

You must perform some preliminary tasks before you prepare to recover tables or table partitions.

The preparation for recovering tables or table partitions from RMAN backups includes the following steps:

- Review the limitations described in " Limitations of Recovering Tables and Table Partitions from RMAN Backups ".
- Verifying that the prerequisites required to recover tables or table partitions are met. See Prerequisites for Recovering Tables and Table Partitions from RMAN Backups.
- Determining the point in time to which the tables or table partitions must be recovered
- Deciding if the recovered tables or table partitions must be imported into the target database
	By default, RMAN imports the recovered tables or table partitions into the target database. However, you can specify that RMAN must not import the recovered objects.
- Deciding if the recovered tables or table partitions must be renamed, mapped to a new tablespace, or mapped to a new schema.

#### 22.2.1 Prerequisites for Recovering Tables and Table Partitions from RMAN Backups

Certain prerequisites must be met before you recover tables or table partitions from RMAN backups.

They include the following:

- The target database must be in read-write mode.
- The target database must be in `ARCHIVELOG` mode.
- You must have RMAN backups of the tables or table partitions as they existed at the point in time to which you want recover these objects.
- To recover single table partitions, the `COMPATIBLE` initialization parameter for target database must be set to 11.1.0 or higher.

See Also:

RMAN Backups Required to Recover Tables and Table Partitions

#### 22.2.2 Determining the Point-in-time to Which Tables and Table Partitions Must be Recovered

It is important to determine the exact point in time to which you want to recover the tables or table partitions. There are multiple ways to specify the point in time to which objects must be recovered.

Use one of the following methods:

- SCN
	Recovers tables or table partitions to the state that they were at the time specified by the SCN.
- Time
	Recovers tables or table partitions to the state they were in at the specified time. Use the date format specified in the `NLS_LANG` and `NLS_DATE_FORMAT` environment variables. You can also use data constants such as `SYSDATE` to specify the time, for example `SYSDATE-30`.
- Sequence number
	Recovers tables or table partitions to the state they were at the time specified by the log sequence number and thread number.

### 22.3 Recovering Tables and Table Partitions

Use the `RESTORE` and `RECOVER` commands to recover tables or table partitions.

To recover tables or table partitions in a non-CDB to a specified point in time:

1. Perform the planning tasks described in " Preparing to Recover Tables and Table Partitions ".
2. Start RMAN and connect as `TARGET` to the target database. You must connect as a user with the `SYSBACKUP` or `SYSDBA` privilege, as described in " [Making Database Connections with RMAN](starting-interacting-with-rman-client.md) ".
3. Recover the selected tables or table partitions to the specified point in time by using the `RECOVER TABLE` command. You must use the `AUXILIARY DESTINATION` clause and one of the following clauses to specify the point in time for recovery: `UNTIL TIME`, `UNTIL SCN`, or `UNTIL SEQUENCE`.
	You can use the following additional clauses in the `RECOVER` command:
	- `DUMP FILE` and `DATAPUMP DESTINATION`
		Specifies the name of the [export dump file](glossary.md) containing recovered tables or table partitions and the location in which it must be stored.
		See " Specify the Name and Location of the Data Pump Export Dump File " for information.
	- `NOTABLEIMPORT`
		Indicates that the recovered tables or table partitions must not be imported into the target database.
		See " Decide Whether to Import Recovered Tables and Table Partitions into the Target Database "
	- `REMAP TABLE`
		Renames the recovered tables or table partitions in the target database. This clause is also used to recover tables or table partitions into a schema that is different from the source schema.
		See " Rename the Recovered Tables and Table Partitions and Recover Tables and Partitions Into a New Schema "
	- `REMAP TABLESPACE`
		Recovers the tables or table partitions into a tablespace that is different from the one in which these objects originally existed.
		See " Rename the Recovered Tables and Table Partitions "

Note:

Recovering tables is only supported when connected locally to the target database.

See Also:

Examples: Recovering Tables and Table Partitions From RMAN Backups

### 22.4 Recovering Tables and Table Partitions in PDBs

Use the `RECOVER` command to recover one or more tables or table partitions in a pluggable database (PDB) to a specified point-in-time, without impacting other objects in the PDB.

To recover tables or table partitions in a PDB:

1. Perform the planning tasks described in " Preparing to Recover Tables and Table Partitions ".
2. Start RMAN and connect to the root as a user with the `SYSDBA` or `SYSBACKUP` privilege, as described in " [Making Database Connections with RMAN](starting-interacting-with-rman-client.md) ".
3. Recover the tables or table partitions to the specified point in time by using the `RECOVER TABLE ... OF PLUGGABLE DATABASE` command.
	You must use the `AUXILIARY DESTINATION` clause and one of the following clauses: `UNITL TIME`, `UNTIL SCN`, or `UNTIL SEQUENCE`.
	Depending on your requirements, you may also need to use the one or more of the following clauses: `DUMP FILE`, `DATAPUMP DESTINATION`, `NOTABLEIMPORT`, `REMAP TABLE`, or `REMAP TABLESPACE`.
	The following command recovers the table `PDB_EMP` in the PDB `HR_PDB` to the state that it was in 4 days before the current date. `HR` is the name of the schema that contains the table. The recovered table is renamed to `EMP_RECVR`.
	```
	RECOVER TABLE HR.PDB_EMP OF PLUGGABLE DATABASE HR_PDB
	UNTIL TIME 'SYSDATE-4'
	AUXILIARY DESTINATION '/tmp/backups'
	REMAP TABLE 'HR'.'PDB_EMP':'EMP_RECVR';
	```

Note:

Recovering tables is only supported when connected locally to the target database.

See Also:

- Guidelines for Recovering Tables and Table Partitions
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF140) for information about the `RECOVER` command

### 22.5 Examples: Recovering Tables and Table Partitions From RMAN Backups

This section contains examples that cover multiple scenarios for recovering tables and table partitions.

- Example: Recovering Tables to a Specified Point in Time
- Example: Recovering Table Partitions to a Specified Log Sequence Number
- Example: Recovering a Table into a New Schema

#### 22.5.1 Example: Recovering Tables to a Specified Point in Time

This example recovers multiple tables to a specified point in time that is represented using `SYSDATE`.

Assume that you want to recover two tables `EMP` and `DEPT` to the state they were in two days ago, before some logical corruption occurred. However, you do not want RMAN to import these tables into the target database. RMAN must only create the [export dump file](glossary.md), called `emp_dept_exp_dump.dat`, in the location `/tmp/recover/dumpfiles`. Using `NOTABLEIMPORT` indicates that these tables must not be imported into the target database. You can import these tables, when required, by using the Data Pump import utility. The auxiliary destination used during the recovery process is `/tmp/oracle/recover`.

To recover tables `EMP` and `DEPT` without importing them into the target database:

1. Perform the planning tasks described in " Preparing to Recover Tables and Table Partitions ".
	In this example, you need to recover tables to a point in time specified by an expression that uses `SYSDATE`. However, the recovered tables must not be imported in to the target database.
2. Start an RMAN session and connect as `TARGET` to the target database as described in " [Making Database Connections with RMAN](starting-interacting-with-rman-client.md) ".
3. Recover the tables `EMP` and `DEPT` using the following clauses in the `RECOVER` command: `DATAPUMP DESTINATION`, `DUMP FILE`, `REMAP TABLE`, and `NOTABLEIMPORT`.
	The following `RECOVER` command recovers the `EMP` and `DEPT` tables.
	```
	RECOVER TABLE SCOTT.EMP, SCOTT.DEPT
	    UNTIL TIME 'SYSDATE-1'
	    AUXILIARY DESTINATION '/tmp/oracle/recover'
	    DATAPUMP DESTINATION '/tmp/recover/dumpfiles'
	    DUMP FILE 'emp_dept_exp_dump.dat'
	    NOTABLEIMPORT;
	```

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF140) for additional examples about recovering tables to a specified point in time

#### 22.5.2 Example: Recovering Table Partitions to a Specified Log Sequence Number

This example uses RMAN backups to recover multiple table partitions.

In this example, the table `sales`, in the schema `sh`, contains the following partitions: `sales_1998`, `sales_1999`, `sales_2000`, and `sales_2001`. This table is stored in the `sales_ts` tablespace. You need to recover two partitions, `sales_1998` and `sales_1999`, to a point in time that is specified by a redo log sequence number. The recovered tables must be automatically imported into the target database and mapped to the tablespace `SALES_PRE_2000_TS`.

To recover the partitions `sales_1998` and `sales_1999` to a specified log sequence number:

1. Perform the planning tasks described in " Preparing to Recover Tables and Table Partitions ".
	In this example, you need to recover two table partitions to a specified log sequence number and then import these partitions into the target database.
2. Start an RMAN session and connect as `TARGET` to the target database as described in " [Making Database Connections with RMAN](starting-interacting-with-rman-client.md) ".
3. Recover partitions using the following `RECOVER` command with the `REMAP TABLE` and `REMAP TABLESPACE` clauses.
	```
	RECOVER TABLE SH.SALES:SALES_1998, SH.SALES:SALES_1999
	    UNTIL SEQUENCE 354
	    AUXILIARY DESTINATION '/tmp/oracle/recover'
	    REMAP TABLE 'SH'.'SALES':'SALES_1998':'HISTORIC_SALES_1998',
	              'SH'.'SALES':'SALES_1999':'HISTORIC_SALES_1999' 
	    REMAP TABLESPACE 'SALES_TS':'SALES_PRE_2000_TS';
	```
	In this case, the specified table partitions are imported as separate tables, called `historic_sales_1998` and `historic_sales_1999`, into the `sales_pre_2000_ts` tablespace of the target database. The `REMAP TABLE` clause specifies the names used for the imported tables. The auxiliary destination used during the recovery process is `/tmp/oracle/recover`.
	If you omit the `REMAP TABLE` clause, RMAN uses default names for the imported tables. The name is a combination of the original table name and the partition name.

#### 22.5.3 Example: Recovering a Table into a New Schema

This example recovers multiple tables into a new schema that is different from the source schema.

In this example, the `HR.DEPARTMENTS` and `SH.CHANNELS` tables need to be recovered to the state that they were in one day ago, before a logical corruption occurred. The recovered tables must be renamed as `NEW_DEPARTMENTS` and `NEW_CHANNELS` and imported into the `EXAMPLE` schema. The schema `EXAMPLE` exists at the time this example is run.

The `REMAP TABLE` clause is used to indicate how the source schema is mapped to a new target schema. The auxiliary destination used during the recovery process is `/tmp/auxdest`.

1. Perform the planning tasks required to recover tables from RMAN backups. In this example, you need to recover tables to a point in time specified by an expression that uses `SYSDATE`.
	See Preparing to Recover Tables and Table Partitions.
2. Start an RMAN session and connect to the target database as described in " [Making Database Connections with RMAN](starting-interacting-with-rman-client.md) ".
3. Recover the `HR.DEPARTMENTS` and `SH.CHANNELS` tables, rename them to `NEW_DEPARTMENTS` and `NEW_CHANNELS` respectively, and then import them into the `EXAMPLE` schema.
	The following `RECOVER` command performs the required table recovery:
	```
	RECOVER TABLE HR.DEPARTMENTS, SH.CHANNELS
	UNTIL TIME 'SYSDATE – 1' 
	AUXILIARY DESTINATION '/tmp/auxdest'
	REMAP TABLE hr.departments:example.new_departments, sh.channels:example.new_channels;
	```