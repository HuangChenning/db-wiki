---
title: "Database Administrator’s Guide"
book: "Database Administrator's Guide"
doc_id: E85760-09
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/admin/administering-pdbs-with-sql-plus.html
tags:
  - oracle
  - 12c
  - administrators-guide
---

Administering PDBs with SQL\*Plus includes tasks such as connecting to a PDB, modifying a PDB, and managing services associated with PDBs.

Note:

You can complete the tasks in this chapter using SQL\*Plus or Oracle SQL Developer.

- About Administering PDBs  
	Administering a pluggable database (PDB) involves a subset of the tasks required to administer a non-CDB.
- Connecting to a PDB with SQL\*Plus  
	You can use several techniques to connect to a PDB with the SQL\*Plus `CONNECT` command.
- Modifying a PDB  
	You can modify a PDB using the `ALTER PLUGGABLE DATABASE` statement and with the SQL\*Plus `STARTUP` and `SHUTDOWN` commands.
- Using the ALTER SYSTEM Statement to Modify a PDB  
	You can use the `ALTER SYSTEM` statement to modify a PDB.
- Managing Services Associated with PDBs  
	You can create, modify, or remove services for a PDB.
- Refreshing a PDB  
	You can refresh a PDB that was created as a refreshable clone.
- Modifying the Listener Settings of a Referenced PDB  
	A PDB that is referenced by a proxy PDB is called a referenced PDB. When the port or host name changes for the listener of the referenced PDB, you must modify the listener settings of the referenced PDB so that its proxy PDBs continue to function properly.

**Parent topic:** [Managing a Multitenant Environment](managing-a-multitenant-environment.md)

### 43.1 About Administering PDBs

Administering a pluggable database (PDB) involves a subset of the tasks required to administer a non-CDB.

In this subset of tasks, most are the same for a PDB and a non-CDB, but there are some differences. For example, there are differences when you modify the open mode of a PDB. Also, a PDB administrator is limited to managing a single PDB and cannot affect other PDBs in the multitenant container database (CDB).

Other administrative tasks are the same for a PDB and a non-CDB. Table 43-1 describes some of these tasks.

Table 43-1 Administrative Tasks Common to PDBs and Non-CDBs

| Task | Description | Additional Information |
| --- | --- | --- |
| Managing tablespaces | You can create, modify, and drop tablespaces for a PDB. You can specify a default tablespace and default tablespace type for each PDB. Also, there is a default temporary tablespace for each PDB. You optionally can create additional temporary tablespaces for use by individual PDBs. | " [Managing Tablespaces](managing-tablespaces.md) "  " Modifying a PDB " |
| Managing data files and temp files | Each PDB has its own data files. You can manage data files and temp files in the same way that you would manage them for a non-CDB. You can also limit the amount of storage used by the data files for a PDB by using the `STORAGE` clause in a `CREATE` `PLUGGABLE` `DATABASE` or `ALTER` `PLUGGABLE` `DATABASE` statement. | " [Managing Data Files and Temp Files](managing-data-files-and-temp-files.md) "  " [Storage Limits](creating-and-removing-pdbs-with-sql-plus.md) "  " Modifying a PDB " |
| Managing schema objects | You can create, modify, and drop schema objects in a PDB in the same way that you would in a non-CDB. You can also create triggers that fire for a specific PDB.  When you manage database links in a CDB, the root has a unique global database name, and so does each PDB. The global name of the root is defined by the `DB_NAME` and `DB_DOMAIN` initialization parameters. The global database name of a PDB is defined by the PDB name and the `DB_DOMAIN` initialization parameter. The global database name of each PDB must be unique within the domain. | " [Schema Objects](schema-objects.md) "  [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=LNPLS01374) for information about creating triggers in a CDB  " [Creating Database Links](managing-a-distributed-database.md) " |

When you are administering a PDB, you can modify the PDB with an `ALTER` `DATABASE`, `ALTER` `PLUGGABLE` `DATABASE`, or `ALTER` `SYSTEM` statement. You can also execute DDL statements on the PDB.

It is also important to understand which administrative tasks cannot be performed when the current container is a PDB. The following are some administrative tasks that are performed by a common user for the entire CDB or for the root when the current container is the root:

- Starting up and shutting down a CDB instance
- Modifying the CDB or the root with an `ALTER` `DATABASE` statement
- Modifying the CDB or the root with an `ALTER` `SYSTEM` statement
- Executing data definition language (DDL) statements on a CDB or the root
- Managing the following components:
	- Processes
		- Memory
		- Errors and alerts
		- Diagnostic data
		- Control files
		- The online redo log and the archived redo log files
		- Undo
- Creating, plugging in, unplugging, and dropping PDBs

A common user whose current container is the root can also change the open mode of one or more PDBs. See [Administering a CDB with SQL\*Plus](administering-a-cdb-with-sql-plus.md) for more information about this task and other tasks related to administering a CDB or the root.

A common user or local user whose current container is a PDB can change the open mode of the current PDB. See " Modifying a PDB " for more information about this task.

See Also:

" [About the Current Container](administering-a-cdb-with-sql-plus.md) "

**Parent topic:** Administering PDBs with SQL\*Plus

### 43.2 Connecting to a PDB with SQL\*Plus

You can use several techniques to connect to a PDB with the SQL\*Plus `CONNECT` command.

This section assumes that you understand how to connect to a non-CDB in SQL\*Plus. See " [Connecting to the Database with SQL\*Plus](getting-started-with-database-administration.md) " for information.

You can use the following techniques to connect to a PDB with the SQL\*Plus `CONNECT` command:

- Local connection with operating system authentication
- Database connection using easy connect
- Database connection using a net service name

The following prerequisites must be met:

- The user connecting to the PDB must be granted the `CREATE` `SESSION` privilege in the PDB.
- To connect to a PDB as a user that does not have `SYSDBA`, `SYSOPER`, `SYSBACKUP`, or `SYSDG` administrative privilege, the PDB must be open. See " [Modifying the Open Mode of PDBs](administering-a-cdb-with-sql-plus.md) " and " Modifying a PDB " for information about changing the open mode of a PDB.

Note:

This section assumes that the user connecting to the PDB is a local user. You can also connect to the PDB as a common user, and you can connect to the root as a common user and switch to the PDB.

To connect to a PDB using the SQL\*Plus CONNECT command:

1. Configure your environment so that you can open SQL\*Plus.
	See " [Connecting to the Database with SQL\*Plus](getting-started-with-database-administration.md) ".
2. Start SQL\*Plus with the `/NOLOG` argument:
	```
	sqlplus /nolog
	```
3. Issue a `CONNECT` command using easy connect or a net service name to connect to the PDB.
	To connect to a PDB, connect to a service with a `PDB` property.

Example 43-1 Connecting to a PDB in SQL\*Plus Using the PDB's Net Service Name

The following command connects to the `hr` user using the `hrapp` service. The `hrapp` service has a `PDB` property for the `hrpdb` PDB. This example assumes that the client is configured to have a net service name for the `hrapp` service.

```
CONNECT hr@hrapp
```

See " [Step 4: Submit the SQL\*Plus CONNECT Command](getting-started-with-database-administration.md) " for more examples.

See Also:

- " [Accessing a Container in a CDB with SQL\*Plus](administering-a-cdb-with-sql-plus.md) " for information about connecting to a PDB as a common user
- " Managing Services Associated with PDBs "

**Parent topic:** Administering PDBs with SQL\*Plus

### 43.3 Modifying a PDB

You can modify a PDB using the `ALTER PLUGGABLE DATABASE` statement and with the SQL\*Plus `STARTUP` and `SHUTDOWN` commands.

- Modifying a PDB with the ALTER PLUGGABLE DATABASE Statement  
	You can modify a PDB with the `ALTER` `PLUGGABLE` `DATABASE` SQL statement.
- Modifying a PDB with the SQL\*Plus STARTUP and SHUTDOWN Commands  
	When the current container is a PDB, you can use the SQL\*Plus `STARTUP` command to open the PDB and the SQL\*Plus `SHUTDOWN` command to close the PDB.

**Parent topic:** Administering PDBs with SQL\*Plus

#### 43.3.1 Modifying a PDB with the ALTER PLUGGABLE DATABASE Statement

You can modify a PDB with the `ALTER` `PLUGGABLE` `DATABASE` SQL statement.

- About Modifying a PDB with the ALTER PLUGGABLE DATABASE Statement  
	An `ALTER` `PLUGGABLE` `DATABASE` statement can modify a PDB.
- Modifying a PDB with the ALTER PLUGGABLE DATABASE Statement  
	You can use the `ALTER` `PLUGGABLE` `DATABASE` statement to modify the attributes of a single PDB.
- Changing the Global Database Name of a PDB  
	You can change the global database name of a PDB with the `ALTER` `PLUGGABLE` `DATABASE` `RENAME` `GLOBAL_NAME` `TO` statement.

**Parent topic:** Modifying a PDB

##### 43.3.1.1 About Modifying a PDB with the ALTER PLUGGABLE DATABASE Statement

An `ALTER` `PLUGGABLE` `DATABASE` statement can modify a PDB.

When the current container is a PDB, an `ALTER` `PLUGGABLE` `DATABASE` statement with any of the following clauses modifies the PDB:

- database\_file\_clauses
	These clauses work the same as they would in an `ALTER` `DATABASE` statement, but the statement applies to the current PDB.
- set\_time\_zone\_clause
	This clause works the same as it would in an `ALTER` `DATABASE` statement, but it applies to the current PDB.
- `DEFAULT TABLESPACE` clause
	For users created while the current container is a PDB, this clause specifies the default tablespace for the user if the default tablespace is not specified in the `CREATE` `USER` statement.
- `DEFAULT TEMPORARY TABLESPACE` clause
	For users created while the current container is a PDB, this clause specifies the default temporary tablespace for the user if the default temporary tablespace is not specified in the `CREATE` `USER` statement.
- `RENAME GLOBAL_NAME` clause
	This clause changes the unique global database name for the PDB. The new global database name must be different from that of any container in the CDB. When you change the global database name of a PDB, the PDB name is changed to the name before the first period in the global database name.
	You must change the `PDB` property of database services used to connect to the PDB when you change the global database name. See " Managing Services Associated with PDBs ".
- `SET DEFAULT { BIGFILE | SMALLFILE } TABLESPACE` clause
	This clause changes the default type of subsequently created tablespaces in the PDB to either bigfile or smallfile. This clause works the same as it would in an `ALTER` `DATABASE` statement, but it applies to the current PDB.
- `DEFAULT EDITION` clause
	This clause works the same as it would in an `ALTER` `DATABASE` statement, but it applies to the current PDB. Each PDB can use edition-based redefinition, and editions in one PDB do not affect editions in other PDBs. In a multitenant environment in which each PDB has its own application, you can use edition-based redefinition independently for each distinct application.
- pdb\_storage\_clause
	This clause sets a limit on the amount of storage used by all tablespaces that belong to a PDB. This limit applies to the total size of all data files and temp files comprising tablespaces that belong to the PDB.
	This clause can also set a limit on the amount of storage that can be used by unified audit OS spillover (.bin format) files in the PDB. If the limit is reached, then no additional storage is available for these files.
	This clause can also set a limit on the amount of storage in a shared temporary tablespace that can be used by sessions connected to the PDB. If the limit is reached, then no additional storage in the shared temporary tablespace is available to sessions connected to the PDB.
- pdb\_change\_state\_clause
	This clause changes the open mode of the current PDB.
	If you specify the optional `RESTRICTED` keyword, then the PDB is accessible only to users with the `RESTRICTED` `SESSION` privilege in the PDB.
	Specifying `FORCE` in this clause changes semantics of the `ALTER` `PLUGGABLE` `DATABASE` statement so that, in addition to opening a PDB that is currently closed, it can be used to change the open mode of a PDB that is already open.
	See " [Modifying the Open Mode of PDBs with ALTER PLUGGABLE DATABASE](administering-a-cdb-with-sql-plus.md) ".
- logging\_clause
	Note:
	This clause is available starting with Oracle Database 12c Release 1 (12.1.0.2).
	This clause specifies the logging attribute of the PDB. The logging attribute controls whether certain DML operations are logged in the redo log file (`LOGGING`) or not (`NOLOGGING`).
	You can use this clause to specify one of the following attributes:
	- `LOGGING` indicates that any future tablespaces created within the PDB will be created with the `LOGGING` attribute by default. You can override this default logging attribute by specifying `NOLOGGING` at the schema object level, in a `CREATE TABLE` statement for example.
		- `NOLOGGING` indicates that any future tablespaces created within the PDB will be created with the `NOLOGGING` attribute by default. You can override this default logging attribute by specifying `LOGGING` at the schema object level, in a `CREATE TABLE` statement for example.
	The specified attribute is used to establish the logging attribute of tablespaces created within the PDB if the logging\_clause is not specified in the `CREATE TABLESPACE` statement.
	The `DBA_PDBS` view shows the current logging attribute for a PDB.
	Note:
	The PDB must be open in restricted mode to use this clause.
	See Also:
	- " [Controlling the Writing of Redo Records](managing-tablespaces.md) "
	- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQLRF30009) for more information about the logging attribute
- pdb\_force\_logging\_clause
	Note:
	This clause is available starting with Oracle Database 12c Release 1 (12.1.0.2).
	This clause places a PDB into force logging or force nologging mode or takes a PDB out of force logging or force nologging mode.
	You can use this clause to specify one of the following attributes:
	- `ENABLE FORCE LOGGING` places the PDB in force logging mode, which causes all changes in the PDB, except changes in temporary tablespaces and temporary segments, to be logged. Force logging mode cannot be overridden at the schema object level.
		PDB-level force logging mode takes precedence over and is independent of any `NOLOGGING` or `FORCE LOGGING` settings you specify for individual tablespaces in the PDB and any `NOLOGGING` settings you specify for individual database objects in the PDB.
		`ENABLE FORCE LOGGING` cannot be specified if a PDB is in force nologging mode. `DISABLE FORCE NOLOGGING` must be specified first.
		- `DISABLE FORCE LOGGING` takes a PDB which is currently in force logging mode out of that mode. If the PDB is not in force logging mode currently, then specifying `DISABLE FORCE LOGGING` results in an error.
		- `ENABLE FORCE NOLOGGING` places the PDB in force nologging mode, which causes no changes in the PDB to be logged. Force nologging mode cannot be overridden at the schema object level.
		CDB-wide force logging mode supersedes PDB-level force nologging mode. PDB-level force nologging mode takes precedence over and is independent of any `LOGGING` or `FORCE LOGGING` settings you specify for individual tablespaces in the PDB and any `LOGGING` settings you specify for individual database objects in the PDB.
		`ENABLE FORCE NOLOGGING` cannot be specified if a PDB is in force logging mode. `DISABLE FORCE LOGGING` must be specified first.
		- `DISABLE FORCE NOLOGGING` takes a PDB that is currently in force nologging mode out of that mode. If the PDB is not in force nologging mode currently, then specifying `DISABLE FORCE NOLOGGING` results in an error.
	The `DBA_PDBS` view shows whether a PDB is in force logging or force nologging mode.
	Note:
	The PDB must be open in restricted mode to use this clause.
	See Also:
	- " [Controlling the Writing of Redo Records](managing-tablespaces.md) "
	- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQLRF30009) for more information about force logging mode and force nologging mode
- pdb\_recovery\_clause
	Note:
	This clause is available starting with Oracle Database 12c Release 1 (12.1.0.2).
	`ALTER PLUGGABLE DATABASE DISABLE RECOVERY` takes the data files that belong to the PDB offline and disables recovery of the PDB. The PDB's data files are not part of any recovery session until it is enabled again. Any new data files created while recovery is disabled are created as unnamed files for the PDB.
	`ALTER PLUGGABLE DATABASE ENABLE RECOVERY` brings the data files that belong to the PDB online and marks the PDB for active recovery. Recovery sessions include these files.
	You can check the recovery status of a PDB by querying the `RECOVERY_STATUS` column in the `V$PDBS` view.
	See [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SBYDB5261) for more information about the pdb\_recovery­\_clause.

An `ALTER` `DATABASE` statement issued when the current container is a PDB that includes clauses that are supported for an `ALTER` `PLUGGABLE` `DATABASE` statement have the same effect as the corresponding `ALTER` `PLUGGABLE` `DATABASE` statement. However, these statements cannot include clauses that are specific to PDBs, such as the pdb\_storage\_clause, the pdb\_change\_state\_clause, the logging\_clause, and the pdb\_recovery\_clause.

See Also:

" [About the Current Container](administering-a-cdb-with-sql-plus.md) "

**Parent topic:** Modifying a PDB with the ALTER PLUGGABLE DATABASE Statement

##### 43.3.1.2 Modifying a PDB with the ALTER PLUGGABLE DATABASE Statement

You can use the `ALTER` `PLUGGABLE` `DATABASE` statement to modify the attributes of a single PDB.

See " About Modifying a PDB with the ALTER PLUGGABLE DATABASE Statement " for information about the clauses that modify the attributes of a single PDB. When the current container is a PDB, an `ALTER` `PLUGGABLE` `DATABASE` statement with one of these clauses modifies the PDB. The modifications overwrite the defaults set for the root in the PDB. The modifications do not affect the root or other PDBs.

The following prerequisites must be met:

- To change the open mode of the PDB from mounted to opened or from opened to mounted, the current user must have `SYSDBA`, `SYSOPER`, `SYSBACKUP`, or `SYSDG` administrative privilege, and the privilege must be either commonly granted or locally granted in the PDB. The user must exercise the privilege using `AS` `SYSDBA`, `AS` `SYSOPER`, `AS` `SYSBACKUP`, or `AS` `SYSDG`, respectively, at connect time.
- For all other operations performed using the `ALTER` `PLUGGABLE` `DATABASE` statement, the current user must have the `ALTER` `DATABASE` system privilege, and the privilege must be either commonly granted or locally granted in the PDB.
- To close a PDB, the PDB must be open.

Note:

This section does not cover changing the global database name of a PDB using the `ALTER` `PLUGGABLE` `DATABASE` statement. To do so, see " Changing the Global Database Name of a PDB ".

To modify a PDB with the `ALTER` `PLUGGABLE` `DATABASE` statement:

1. In SQL\*Plus, ensure that the current container is a PDB.
	See " Connecting to a PDB with SQL\*Plus ".
2. Run an `ALTER` `PLUGGABLE` `DATABASE` statement.

The following examples modify a single PDB.

Example 43-2 Changing the Open Mode of a PDB

This `ALTER` `PLUGGABLE` `DATABASE` statement changes the open mode of the current PDB to mounted.

```
ALTER PLUGGABLE DATABASE CLOSE IMMEDIATE;
```

The following statement changes the open mode of the current PDB to open read-only.

```
ALTER PLUGGABLE DATABASE OPEN READ ONLY;
```

A PDB must be in mounted mode to change its open mode to read-only or read/write unless you specify the `FORCE` keyword.

The following statement changes the open mode of the current PDB from mounted or open read-only to open read-write.

```
ALTER PLUGGABLE DATABASE OPEN FORCE;
```

The following statement changes the open mode of the current PDB from mounted to migrate.

```
ALTER PLUGGABLE DATABASE OPEN UPGRADE;
```

Example 43-3 Bringing a Data File Online for a PDB

This `ALTER` `PLUGGABLE` `DATABASE` statement uses a database\_file\_clause to bring the /u03/oracle/pdb1\_01.dbf data file online.

```
ALTER PLUGGABLE DATABASE DATAFILE '/u03/oracle/pdb1_01.dbf' ONLINE;
```

Example 43-4 Changing the Default Tablespaces for a PDB

This `ALTER` `PLUGGABLE` `DATABASE` statement uses a `DEFAULT` `TABLESPACE` clause to set the default permanent tablespace to `pdb1_tbs` for the PDB.

```
ALTER PLUGGABLE DATABASE DEFAULT TABLESPACE pdb1_tbs;
```

This `ALTER` `PLUGGABLE` `DATABASE` statement uses a `DEFAULT` `TEMPORARY` `TABLESPACE` clause to set the default temporary tablespace to `pdb1_temp` for the PDB.

```
ALTER PLUGGABLE DATABASE DEFAULT TEMPORARY TABLESPACE pdb1_temp;
```

The tablespace or tablespace group specified in the `ALTER` `PLUGGABLE` `DATABASE` statement must exist in the PDB. Users whose current container is a PDB that are not explicitly assigned a default tablespace or default temporary tablespace use the default tablespace or default temporary tablespace for the PDB.

Example 43-5 Changing the Default Tablespace Type for a PDB

This `ALTER` `DATABASE` statement uses a `SET` `DEFAULT` `TABLESPACE` clause to change the default tablespace type to bigfile for the PDB.

```
ALTER PLUGGABLE DATABASE SET DEFAULT BIGFILE TABLESPACE;
```

Example 43-6 Setting Storage Limits for a PDB

This statement sets the storage limit for all tablespaces that belong to a PDB to two gigabytes.

```
ALTER PLUGGABLE DATABASE STORAGE(MAXSIZE 2G);
```

This statement specifies that there is no storage limit for the tablespaces that belong to the PDB.

```
ALTER PLUGGABLE DATABASE STORAGE(MAXSIZE UNLIMITED);
```

This statement specifies that there is no storage limit for the tablespaces that belong to the PDB and that there is no storage limit for the shared temporary tablespace that can be used by sessions connected to the PDB.

```
ALTER PLUGGABLE DATABASE STORAGE UNLIMITED;
```

Example 43-7 Setting the Logging Attribute of a PDB

With the PDB open in restricted mode, this statement specifies the `NOLOGGING` attribute for the PDB:

```
ALTER PLUGGABLE DATABASE NOLOGGING;
```

Note:

This example requires Oracle Database 12c Release 1 (12.1.0.2) or later.

Example 43-8 Setting the Force Logging Mode of a PDB

This statement enables force logging mode for the PDB:

```
ALTER PLUGGABLE DATABASE ENABLE FORCE LOGGING;
```

Note:

This example requires Oracle Database 12c Release 1 (12.1.0.2) or later.

Example 43-9 Setting the Default Edition for a PDB

This example sets the default edition for the current PDB to `PDB1E3`.

```
ALTER PLUGGABLE DATABASE DEFAULT EDITION = PDB1E3;
```

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQLRF55667) for more information about the `ALTER` `PLUGGABLE` `DATABASE` statement
- [Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=ADFNS020) for a complete discussion of edition-based redefinition

**Parent topic:** Modifying a PDB with the ALTER PLUGGABLE DATABASE Statement

##### 43.3.1.3 Changing the Global Database Name of a PDB

You can change the global database name of a PDB with the `ALTER` `PLUGGABLE` `DATABASE` `RENAME` `GLOBAL_NAME` `TO` statement.

When you change the global database name of a PDB, the new global database name must be different from that of any container in the CDB.

The following prerequisites must be met:

- The current user must have the `ALTER` `DATABASE` system privilege, and the privilege must be either commonly granted or locally granted in the PDB.
- For an Oracle Real Application Clusters (Oracle RAC) database, the PDB must be open on the current instance only. The PDB must be closed on all other instances.
- The PDB being modified must be opened on the current instance in read/write mode with `RESTRICTED` specified so that it is accessible only to users with `RESTRICTED` `SESSION` privilege in the PDB.

To change the global database name of a PDB:

When you change the global database name of a PDB, the PDB name is changed to the first part of the new global name, which is the part before the first period. Also, Oracle Database changes the name of the default database service for the PDB automatically. Oracle Database also changes the `PDB` property of all database services in the PDB to the new global name of the PDB. You must close the PDB and open it in read/write mode for Oracle Database to complete the integration of the new PDB service name into the CDB, as shown in steps [^1] and [^2].

Oracle Net Services must be configured properly for clients to access database services. You might need to alter your Oracle Net Services configuration as a result of the PDB name change.

See Also:

- " Modifying a PDB " for more information about modifying the open mode of a PDB
- " Managing Services Associated with PDBs " for information about PDBs and database services
- " Connecting to a PDB with SQL\*Plus "

**Parent topic:** Modifying a PDB with the ALTER PLUGGABLE DATABASE Statement

#### 43.3.2 Modifying a PDB with the SQL\*Plus STARTUP and SHUTDOWN Commands

When the current container is a PDB, you can use the SQL\*Plus `STARTUP` command to open the PDB and the SQL\*Plus `SHUTDOWN` command to close the PDB.

- Using the STARTUP SQL\*Plus Command on a PDB  
	When the current container is a PDB, the SQL\*Plus `STARTUP` command opens the PDB.
- Using the SQL\*Plus SHUTDOWN Command on a PDB  
	When the current container is a PDB, the SQL\*Plus `SHUTDOWN` command closes the PDB.

**Parent topic:** Modifying a PDB

##### 43.3.2.1 Using the STARTUP SQL\*Plus Command on a PDB

When the current container is a PDB, the SQL\*Plus `STARTUP` command opens the PDB.

Use the following options of the `STARTUP` command to open a PDB:

- `FORCE`
	Closes an open PDB before re-opening it in read/write mode. When this option is specified, no other options are allowed.
- `RESTRICT`
	Enables only users with the `RESTRICTED` `SESSION` system privilege in the PDB to access the PDB.
	If neither `OPEN` `READ` `WRITE` nor `OPEN` `READ` `ONLY` is specified and `RESTRICT` is specified, then the PDB is opened in read-only mode when the CDB to which it belongs is a physical standby database. Otherwise, the PDB is opened in read/write mode.
- `OPEN` open\_pdb\_options
	Opens the PDB in either read/write mode or read-only mode. Specify `OPEN` `READ` `WRITE` or `OPEN` `READ` `ONLY`. When `RESTRICT` is not specified, `READ` `WRITE` is always the default.

To issue the `STARTUP` command when the current container is a PDB, the following prerequisites must be met:

- The current user must have `SYSDBA`, `SYSOPER`, `SYSBACKUP`, or `SYSDG` administrative privilege, and the privilege must be either commonly granted or locally granted in the PDB. The user must exercise the privilege using `AS` `SYSDBA`, `AS` `SYSOPER`, `AS` `SYSBACKUP`, or `AS` `SYSDG`, respectively, at connect time.
- Excluding the use of the `FORCE` option, the PDB must be in mounted mode to open it.
- To place a PDB in mounted mode, the PDB must be in open read-only or open read/write mode.

To modify a PDB with the `STARTUP` command:

1. In SQL\*Plus, ensure that the current container is a PDB.
	See " Connecting to a PDB with SQL\*Plus ".
2. Run the `STARTUP` command.

See Also:

- " [Starting Up a Database](starting-up-and-shutting-down.md) "
- " [About the Current Container](administering-a-cdb-with-sql-plus.md) "
- [SQL\*Plus User's Guide and Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQPUG128)

Example 43-10 Opening a PDB in Read/Write Mode with the STARTUP Command

```
STARTUP OPEN
```

Example 43-11 Opening a PDB in Read-Only Mode with the STARTUP Command

```
STARTUP OPEN READ ONLY
```

Example 43-12 Opening a PDB in Read-Only Restricted Mode with the STARTUP Command

```
STARTUP RESTRICT OPEN READ ONLY
```

Example 43-13 Opening a PDB in Read/Write Mode with the STARTUP Command and the FORCE Option

This example assumes that the PDB is currently open. The `FORCE` option closes the PDB and then opens it in the read/write mode.

```
STARTUP FORCE
```

**Parent topic:** Modifying a PDB with the SQL\*Plus STARTUP and SHUTDOWN Commands

##### 43.3.2.2 Using the SQL\*Plus SHUTDOWN Command on a PDB

When the current container is a PDB, the SQL\*Plus `SHUTDOWN` command closes the PDB.

After the `SHUTDOWN` command is issued on a PDB successfully, it is in mounted mode.

The following `SHUTDOWN` modes are possible:

- When you specify `SHUTDOWN` only, then the PDB is shut down with the normal mode.
- When you specify `SHUTDOWN IMMEDIATE`, the PDB is shut down with the immediate mode.
- When you specify `SHUTDOWN ABORT`, the PDB is forcefully closed.
	For a single-instance CDB, PDB media recovery is required when you specify `SHUTDOWN ABORT`. For an Oracle Real Application Clusters (Oracle RAC) CDB, PDB media recovery is required if the `SHUTDOWN ABORT` command closes the last open instance.

To issue the `SHUTDOWN` command when the current container is a PDB, the following prerequisites must be met:

- The current user must have `SYSDBA`, `SYSOPER`, `SYSBACKUP`, or `SYSDG` administrative privilege, and the privilege must be either commonly granted or locally granted in the PDB. The user must exercise the privilege using `AS` `SYSDBA`, `AS` `SYSOPER`, `AS` `SYSBACKUP`, or `AS` `SYSDG`, respectively, at connect time.
- To close a PDB, the PDB must be open.

To modify a PDB with the `SHUTDOWN` command:

1. In SQL\*Plus, ensure that the current container is a PDB.
	See " Connecting to a PDB with SQL\*Plus ".
2. Run the `SHUTDOWN` command.

Note:

- When the current container is a PDB, the `SHUTDOWN` command only closes the PDB, not the CDB instance.
- There is no `SHUTDOWN` command for a PDB that is equivalent to `SHUTDOWN` `TRANSACTIONAL` for a non-CDB.

See Also:

- " [Modifying the Open Mode of PDBs with ALTER PLUGGABLE DATABASE](administering-a-cdb-with-sql-plus.md) "
- " [Shutting Down a Database](starting-up-and-shutting-down.md) " for more information about shutdown modes
- " [About the Current Container](administering-a-cdb-with-sql-plus.md) "
- [SQL\*Plus User's Guide and Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQPUG125)

Example 43-14 Closing a PDB with the SHUTDOWN IMMEDIATE Command

```
SHUTDOWN IMMEDIATE
```

**Parent topic:** Modifying a PDB with the SQL\*Plus STARTUP and SHUTDOWN Commands

### 43.4 Using the ALTER SYSTEM Statement to Modify a PDB

You can use the `ALTER SYSTEM` statement to modify a PDB.

- About Using the ALTER SYSTEM Statement on a PDB  
	The `ALTER` `SYSTEM` statement can dynamically alter a PDB. You can issue an `ALTER` `SYSTEM` statement when you want to change the way a PDB operates.
- Using the ALTER SYSTEM Statement on a PDB  
	You can use the `ALTER SYSTEM` statement to modify a PDB.

**Parent topic:** Administering PDBs with SQL\*Plus

#### 43.4.1 About Using the ALTER SYSTEM Statement on a PDB

The `ALTER` `SYSTEM` statement can dynamically alter a PDB. You can issue an `ALTER` `SYSTEM` statement when you want to change the way a PDB operates.

When the current container is a PDB, you can run the following `ALTER` `SYSTEM` statements:

- `ALTER SYSTEM FLUSH SHARED_POOL`
- `ALTER SYSTEM FLUSH BUFFER_CACHE`
- `ALTER SYSTEM FLUSH FLASH_CACHE`
- `ALTER SYSTEM ENABLE RESTRICTED SESSION`
- `ALTER SYSTEM DISABLE RESTRICTED SESSION`
- `ALTER SYSTEM SET USE_STORED_OUTLINES`
- `ALTER SYSTEM SUSPEND`
- `ALTER SYSTEM RESUME`
- `ALTER SYSTEM CHECKPOINT`
- `ALTER SYSTEM CHECK DATAFILES`
- `ALTER SYSTEM REGISTER`
- `ALTER SYSTEM KILL SESSION`
- `ALTER SYSTEM DISCONNECT SESSION`
- `ALTER SYSTEM SET` initialization\_parameter (for a subset of initialization parameters)

All other `ALTER` `SYSTEM` statements affect the entire CDB and must be run by a common user in the root.

The `ALTER` `SYSTEM` `SET` initialization\_parameter statement can modify only some initialization parameters for PDBs. All initialization parameters can be set for the root. For any initialization parameter that is not set explicitly for a PDB, the PDB inherits the root's parameter value.

You can modify an initialization parameter for a PDB when the `ISPDB_MODIFIABLE` column is `TRUE` for the parameter in the `V$SYSTEM_PARAMETER` view. The following query lists all of the initialization parameters that are modifiable for a PDB:

```
SELECT NAME FROM V$SYSTEM_PARAMETER WHERE ISPDB_MODIFIABLE='TRUE' ORDER BY NAME;
```

When the current container is a PDB, run the `ALTER` `SYSTEM` `SET` initialization\_parameter statement to modify the PDB. The statement does not affect the root or other PDBs. The following table describes the behavior of the `SCOPE` clause when you use a server parameter file (SPFILE) and run the `ALTER` `SYSTEM` `SET` statement on a PDB.

| SCOPE Setting | Behavior |
| --- | --- |
| `MEMORY` | The initialization parameter setting is changed in memory and takes effect immediately in the PDB. The new setting affects only the PDB.  The setting reverts to the value set in the root in the any of the following cases:  - An `ALTER` `SYSTEM` `SET` statement sets the value of the parameter in the root with `SCOPE` equal to `BOTH` or `MEMORY`, and the PDB is closed and re-opened. The parameter value in the PDB is not changed if `SCOPE` is equal to `SPFILE`, and the PDB is closed and re-opened. - The PDB is closed and re-opened. - The CDB is shut down and re-opened. |
| `SPFILE` | The initialization parameter setting is changed for the PDB and stored persistently. The new setting takes effect in any of the following cases:  - The PDB is closed and re-opened. - The CDB is shut down and re-opened.  In these cases, the new setting affects only the PDB. |
| `BOTH` | The initialization parameter setting is changed in memory, and it is changed for the PDB and stored persistently. The new setting takes effect immediately in the PDB and persists after the PDB is closed and re-opened or the CDB is shut down and re-opened. The new setting affects only the PDB. |

When a PDB is unplugged from a CDB, the values of the initialization parameters that were specified for the PDB with `SCOPE=BOTH` or `SCOPE=SPFILE` are added to the PDB's XML metadata file. These values are restored for the PDB when it is plugged in to a CDB.

Note:

A text initialization parameter file (PFILE) cannot contain PDB-specific parameter values.

**Parent topic:** Using the ALTER SYSTEM Statement to Modify a PDB

#### 43.4.2 Using the ALTER SYSTEM Statement on a PDB

You can use the `ALTER SYSTEM` statement to modify a PDB.

The current user must be granted the following privileges, and the privileges must be either commonly granted or locally granted in the PDB:

- `CREATE` `SESSION`
- `ALTER` `SYSTEM`

To use `ALTER` `SYSTEM` to modify a PDB:

1. In SQL\*Plus, ensure that the current container is a PDB.
	See " Connecting to a PDB with SQL\*Plus ".
2. Run the `ALTER` `SYSTEM` statement.

Example 43-15 Enable Restricted Sessions in a PDB

To restrict sessions in a PDB, issue the following statement:

```
ALTER SYSTEM ENABLE RESTRICTED SESSION;
```

Example 43-16 Changing the Statistics Gathering Level for the PDB

This `ALTER` `SYSTEM` statement sets the `STATISTICS_LEVEL` initialization parameter to `ALL` for the current PDB:

```
ALTER SYSTEM SET STATISTICS_LEVEL = ALL SCOPE = MEMORY;
```

See Also:

- " [Using the ALTER SYSTEM SET Statement in a CDB](administering-a-cdb-with-sql-plus.md) "
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQLRF00902)

**Parent topic:** Using the ALTER SYSTEM Statement to Modify a PDB

### 43.5 Managing Services Associated with PDBs

You can create, modify, or remove services for a PDB.

- About Services Associated with PDBs  
	Database services have an optional `PDB` property. You can set a `PDB` property when you create a service, and you can modify the `PDB` property of a service.
- Creating, Modifying, or Removing a Service for a PDB  
	You can create, modify, or remove a service with a `PDB` property.

See Also:

" [Managing Application Workloads with Database Services](creating-and-configuring-an-oracle-database.md) "

**Parent topic:** Administering PDBs with SQL\*Plus

#### 43.5.1 About Services Associated with PDBs

Database services have an optional `PDB` property. You can set a `PDB` property when you create a service, and you can modify the `PDB` property of a service.

The `PDB` property associates the service with the PDB. When a client connects to a service with a `PDB` property, the current container for the connection is the PDB. You can view the `PDB` property for a service by querying the `ALL_SERVICES` data dictionary view or, when using the SRVCTL utility, by using the `srvctl` `config` `service` command.

The `PDB` property is required only when you are creating a service or modifying the `PDB` property of a service. For example, you do not specify a `PDB` property when you start, stop, or remove a service, and you do not need to specify a `PDB` property when you modify a service without modifying its `PDB` property.

When a PDB is created, a new default service for the PDB is created automatically, and this service has the same name as the PDB. You cannot manage this service, and it should only be used for administrative tasks. Do not use this default PDB service for applications. Always use user-defined services for applications because you can customize user-defined services to fit the requirements of your applications.

Note:

- Each database service name must be unique in a CDB, and each database service name must be unique within the scope of all the CDBs whose instances are reached through a specific listener.
- In an Oracle Clusterware environment, an Oracle Clusterware resource must be created for each service that is created for the PDB.
- When your database is being managed by Oracle Restart or Oracle Clusterware, and you use the SRVCTL utility to start a service with a PDB property for a PDB that is closed, the PDB is opened in read/write mode on the nodes where the service is started. However, stopping a PDB service does not change the open mode of the PDB. See " Modifying a PDB with the ALTER PLUGGABLE DATABASE Statement " for information about changing the open mode of a PDB.
- When you unplug or drop a PDB, the services of the unplugged or dropped PDB are not removed automatically. You can remove these services manually.
- Do not associate a service with a proxy PDB.

See Also:

" [About the Current Container](administering-a-cdb-with-sql-plus.md) "

" [Creating a PDB as a Proxy PDB](creating-and-removing-pdbs-with-sql-plus.md) "

**Parent topic:** Managing Services Associated with PDBs

#### 43.5.2 Creating, Modifying, or Removing a Service for a PDB

You can create, modify, or remove a service with a `PDB` property.

You can do so in the following ways:

- If your single-instance database is being managed by Oracle Restart or your Oracle RAC database is being managed by Oracle Clusterware, then use the Server Control (SRVCTL) utility to create, modify, or remove the service.
	To create a service for a PDB using the SRVCTL utility, use the `add` `service` command and specify the PDB in the `-pdb` parameter. If you do not specify a PDB in the `-pdb` parameter when you create a service, then the service is associated with the root.
	To modify the `PDB` property of a service using the SRVCTL utility, use the `modify` `service` command and specify the PDB in the `-pdb` parameter. To remove a service for a PDB using the SRVCTL utility, use the `remove` `service` command.
	You can use other SRVCTL commands to manage the service, such as the `start` `service` and `stop` `service` commands, even if they do not include the `-pdb` parameter.
	The PDB name is not validated when you create or modify a service with the SRVCTL utility. However, an attempt to start a service with invalid PDB name results in an error.
- If your database is not being managed by Oracle Restart or Oracle Clusterware, then use the `DBMS_SERVICE` package to create or remove a database service.
	When you create a service with the `DBMS_SERVICE` package, the `PDB` property of the service is set to the current container. Therefore, to create a service with a `PDB` property set to a specific PDB using the `DBMS_SERVICE` package, run the `CREATE_SERVICE` procedure when the current container is that PDB. If you create a service using the `CREATE_SERVICE` procedure when the current container is the root, then the service is associated with the root.
	You cannot modify the `PDB` property of a service with the `DBMS_SERVICE` package. However, you can remove a service in one PDB and create a similar service in a different PDB. In this case, the new service has the `PDB` property of the PDB in which it was created.
	You can also use other `DBMS_SERVICE` subprograms to manage the service, such as the `START_SERVICE` and `STOP_SERVICE` procedures. Use the `DELETE_SERVICE` procedure to remove a service.

Oracle recommends using the SRVCTL utility to create and modify services. However, if you do not use the SRVCTL utility, then you can use the `DBMS_SERVICE` package.

To create, modify, or remove a service with a PDB property using the SRVCTL utility:

1. Log in to the host computer with the correct user account, and ensure that you run SRVCTL from the correct Oracle home.
2. To create or modify a service, run the `add` `service` command, and specify the PDB in the `-pdb` parameter. To modify the `PDB` property of a service, run the `modify` `service` command, and specify the PDB in the `-pdb` parameter. To remove a service, run the `remove` `service` command.

To create or remove a service for a PDB using the DBMS\_SERVICE package:

1. In SQL\*Plus, ensure that the current container is a PDB.
	See " Connecting to a PDB with SQL\*Plus ".
2. Run the appropriate subprogram in the `DBMS_SERVICE` package.

Note:

If your database is being managed by Oracle Restart or Oracle Clusterware, then use the SRVCTL utility to manage services. Do not use the `DBMS_SERVICE` package.

Example 43-17 Creating a Service for a PDB Using the SRVCTL Utility

This example adds the `salesrep` service for the PDB `salespdb` in the CDB with `DB_UNIQUE_NAME` `mycdb`:

```
srvctl add service -db mycdb -service salesrep -pdb salespdb
```

Example 43-18 Modifying the PDB Property of a Service Using the SRVCTL Utility

This example modifies the `salesrep` service in the CDB with `DB_UNIQUE_NAME` `mycdb` to associate the service with the `hrpdb` PDB:

```
srvctl modify service -db mycdb -service salesrep -pdb hrpdb
```

Example 43-19 Removing a Service Using the SRVCTL Utility

This example removes the `salesrep` service in the CDB with `DB_UNIQUE_NAME` `mycdb`:

```
srvctl remove service -db mycdb -service salesrep
```

Example 43-20 Creating a Service for a PDB Using the DBMS\_SERVICE Package

This example creates the `salesrep` service for the current PDB:

```
BEGIN
  DBMS_SERVICE.CREATE_SERVICE(
    service_name => 'salesrep',
    network_name => 'salesrep.example.com');
END;
/
```

The `PDB` property of the service is set to the current container. For example, if the current container is the `salespdb` PDB, then the PDB property of the service is `salespdb`.

Example 43-21 Removing a Service Using the DBMS\_SERVICE Package

This example removes the `salesrep` service in the current PDB.

```
BEGIN
  DBMS_SERVICE.DELETE_SERVICE(
    service_name => 'salesrep');
END;
/
```

See Also:

- [Configuring Automatic Restart of an Oracle Database](configuring-automatic-restart-of-an-oracle-database.md)
- [Example 45-9](viewing-information-about-cdbs-and-pdbs-with-sql-plus.md)
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=ARPLS092) for information about the `DBMS_SERVICE` package
- [Oracle Database 2 Day + Real Application Clusters Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=TDPRC289) and [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=RACAD076) for information about creating services in an Oracle Real Application Clusters (Oracle RAC) environment

**Parent topic:** Managing Services Associated with PDBs

### 43.6 Refreshing a PDB

You can refresh a PDB that was created as a refreshable clone.

When you refresh a PDB manually, changes made to the source PDB since the last refresh are propagated to the PDB being refreshed. You can manually refresh a PDB that is configured for automatic refresh.

To refresh a PDB, the PDB must have been created as a clone with the `REFRESH MODE MANUAL` or `REFRESH MODE EVERY minutes` clause included.

1. In SQL\*Plus, ensure that the current container is the PDB you want to refresh.
2. If the PDB is not closed, then close the PDB. For example, issue the following SQL statement:
	`ALTER PLUGGABLE DATABASE CLOSE IMMEDIATE;`
3. Issue the following SQL statement:
	`ALTER PLUGGABLE DATABASE REFRESH;`

### 43.7 Modifying the Listener Settings of a Referenced PDB

A PDB that is referenced by a proxy PDB is called a referenced PDB. When the port or host name changes for the listener of the referenced PDB, you must modify the listener settings of the referenced PDB so that its proxy PDBs continue to function properly.

- Altering the Listener Host Name of a Referenced PDB  
	When the host name of the listener for a referenced PDB changes, you must run an `ALTER PLUGGABLE DATABASE CONTAINERS HOST` statement to reset the host name of the referenced PDB so that its proxy PDBs continue to function properly.
- Altering the Listener Port Number of a Referenced PDB  
	When the port number of the listener for a referenced PDB changes, you must run an `ALTER PLUGGABLE DATABASE CONTAINERS PORT` statement to reset the port number of the referenced PDB so that its proxy PDBs continue to function properly.

**Parent topic:** Administering PDBs with SQL\*Plus

#### 43.7.1 Altering the Listener Host Name of a Referenced PDB

When the host name of the listener for a referenced PDB changes, you must run an `ALTER PLUGGABLE DATABASE CONTAINERS HOST` statement to reset the host name of the referenced PDB so that its proxy PDBs continue to function properly.

A proxy PDB uses a database link to establish communication with its referenced PDB during PDB creation. After communication is established, the proxy PDB communicates directly with the referenced PDB without using a database link, and the database link can be dropped. When the listener host name changes for the referenced PDB, each proxy PDB must re-establish communication with its referenced PDB.

The listener host name of a referenced PDB is a database property. When it is set, you can view the current setting by querying the `DATABASE_PROPERTIES` data dictionary view.

The current user must have the `ALTER` `DATABASE` system privilege, and the privilege must be either commonly granted or locally granted in the PDB.

1. In SQL\*Plus, ensure that the current container is the referenced PDB.
	See " Connecting to a PDB with SQL\*Plus ".
2. Run an `ALTER PLUGGABLE DATABASE CONTAINERS HOST` statement and specify the new host name, or include the `RESET` keyword to return the host name to its default setting, which is the host name of the referenced PDB.
3. Drop and re-create the proxy PDBs that reference the referenced PDB to re-establish communication for each proxy PDB and its referenced PDB.

Example 43-22 Altering the Listener Host Name of a Referenced PDB

This example changes the host name for the referenced PDB to `myhost.example.com`.

```
ALTER PLUGGABLE DATABASE CONTAINERS HOST='myhost.example.com';
```

Example 43-23 Resetting the Listener Host Name to the Default Value

This example resets the host name for the referenced PDB to its default value. The default value is the host name of the referenced PDB.

```
ALTER PLUGGABLE DATABASE CONTAINERS HOST RESET;
```

#### 43.7.2 Altering the Listener Port Number of a Referenced PDB

When the port number of the listener for a referenced PDB changes, you must run an `ALTER PLUGGABLE DATABASE CONTAINERS PORT` statement to reset the port number of the referenced PDB so that its proxy PDBs continue to function properly.

A proxy PDB uses a database link to establish communication with its referenced PDB during PDB creation. After communication is established, the proxy PDB communicates directly with the referenced PDB without using a database link, and the database link can be dropped. When the listener port number changes for the referenced PDB, each proxy PDB must re-establish communication with its referenced PDB.

The listener port number of a referenced PDB is a database property. When it is set, you can view the current setting by querying the `DATABASE_PROPERTIES` data dictionary view.

The current user must have the `ALTER` `DATABASE` system privilege, and the privilege must be either commonly granted or locally granted in the PDB.

1. In SQL\*Plus, ensure that the current container is the referenced PDB.
	See " Connecting to a PDB with SQL\*Plus ".
2. Run an `ALTER PLUGGABLE DATABASE CONTAINERS PORT` statement and specify the new port number, or include the `RESET` keyword to return the port number to its default setting, which is 1521.
3. Drop and re-create the proxy PDBs that reference the referenced PDB to re-establish communication for each proxy PDB and its referenced PDB.

Example 43-24 Altering the Listener Port Number of a Referenced PDB

This example changes the port number for the referenced PDB to `1543`.

```
ALTER PLUGGABLE DATABASE CONTAINERS PORT=1543;
```

Example 43-25 Resetting the Listener Port Number to the Default Value

This example resets the port number for the referenced PDB to its default value. The default value for the port number is 1521.

```
ALTER PLUGGABLE DATABASE CONTAINERS PORT RESET;
```

[^1]: Close the PDB.

[^2]: Open the PDB in read/write mode.