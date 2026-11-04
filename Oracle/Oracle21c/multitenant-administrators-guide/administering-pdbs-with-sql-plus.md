---
title: "Administrator’s Guide"
book: "Multitenant Administrator's Guide"
doc_id: F31734-10
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/multi/administering-pdbs-with-sql-plus.html
tags:
  - oracle
  - 21c
  - multitenant-administrators-guide
---

Administering PDBs includes tasks such as connecting to a PDB, modifying a PDB, and managing services associated with PDBs.

- About PDB Administration  
	Administering a pluggable database (PDB) involves a subset of the tasks required to administer a CDB.
- Managing Connections to a PDB  
	You manage connections for a PDB in the same way as for a CDB, with some special considerations.
- Modifying a PDB at the System Level  
	You can use the `ALTER SYSTEM` statement to modify a PDB.
- Modifying a PDB at the Database Level  
	You can modify a PDB using the `ALTER PLUGGABLE DATABASE` statement.
- Modifying the Open Mode of PDBs  
	You can modify the open mode of a PDB by using the `ALTER PLUGGABLE DATABASE` SQL statement or the SQL\*Plus `STARTUP` command.

**Parent topic:** [Administering a Multitenant Environment](managing-a-multitenant-environment.md)

### About PDB Administration

Administering a pluggable database (PDB) involves a subset of the tasks required to administer a CDB.

In this subset of tasks, most are the same for a PDB and a CDB, but differences exist. For example, there are differences when you modify the open mode of a PDB. Also, a PDB administrator is limited to managing a single PDB and cannot manage other PDBs in the multitenant container database (CDB).

- Tasks Common to PDBs and CDBs  
	Most administrative tasks are the same for a PDB and a CDB.
- Tasks Specific to CDBs  
	Some administrative tasks cannot be performed when the current container is a PDB.

See Also:

" Modifying a PDB at the Database Level " for more information about changing the open mode of the current PDB

**Parent topic:** Administering PDBs

#### Tasks Common to PDBs and CDBs

Most administrative tasks are the same for a PDB and a CDB.

When you are administering a PDB, you can modify the PDB with an `ALTER DATABASE`, `ALTER PLUGGABLE DATABASE`, or `ALTER SYSTEM` statement. You can also execute DDL statements on the PDB. The following table describes some of these tasks common to a PDB and CDB.

Table 16-1 Administrative Tasks Common to PDBs and CDBs

| Task | Description | Additional Information |
| --- | --- | --- |
| Managing tablespaces | You can create, modify, and drop tablespaces for a PDB. You can specify a default tablespace and default tablespace type for each PDB. Also, there is a default temporary tablespace for each PDB. You optionally can create additional temporary tablespaces for use by individual PDBs. | " Modifying a PDB at the Database Level "  [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-1C162C60-6698-44F2-B2A9-F3E2D2958D88) for information about managing tablespaces |
| Managing data files and temp files | Each PDB has its own data files. You can manage data files and temp files in the same way that you would manage them for a CDB. You can also limit the amount of storage used by the data files for a PDB by using the `STORAGE` clause in a `CREATE PLUGGABLE DATABASE` or `ALTER PLUGGABLE DATABASE` statement. | " Modifying a PDB at the Database Level "  [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-501A8889-3C18-4F99-B0B7-9095E981B970) for information about managing data files and temp files |
| Managing schema objects | You can create, modify, and drop schema objects in a PDB in the same way that you would in a CDB. You can also create triggers that fire for a specific PDB.  When you manage database links in a CDB, the root has a unique global database name, and so does each PDB. The global name of the root is defined by the `DB_NAME` and `DB_DOMAIN` initialization parameters. The global database name of a PDB is defined by the PDB name and the `DB_DOMAIN` initialization parameter. The global database name of each PDB must be unique within the domain. | [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-2DA8C61C-58B0-4892-8E5D-E7A9120BC120) for more information about schema objects  [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-B5950167-35F8-4C88-B063-382E0290CB53)  [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=LNPLS01374) for information about creating triggers in a CDB |

**Parent topic:** About PDB Administration

#### Tasks Specific to CDBs

Some administrative tasks cannot be performed when the current container is a PDB.

The following tasks are performed by a common user for the entire CDB or for the CDB root when the current container is the root:

- Starting up and shutting down a CDB instance
- Modifying the CDB or the root with an `ALTER DATABASE` statement
- Modifying the CDB or the root with an `ALTER SYSTEM` statement
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

A common user whose current container is the root can also change the open mode of one or more PDBs. Similarly, a common user or local user whose current container is a PDB can change the open mode of the current PDB.

**Parent topic:** About PDB Administration

### Managing Connections to a PDB

You manage connections for a PDB in the same way as for a CDB, with some special considerations.

- Connecting to a PDB  
	You can use several techniques to connect to a PDB with the SQL\*Plus `CONNECT` command.
- Managing Services for PDBs  
	You can create, modify, or remove services for a PDB.
- Modifying the Listener Settings of a Referenced PDB  
	A PDB that is referenced by a proxy PDB is called a referenced PDB.

**Parent topic:** Administering PDBs

#### Connecting to a PDB

You can use several techniques to connect to a PDB with the SQL\*Plus `CONNECT` command.

This section assumes that you understand how to connect to a CDB in SQL\*Plus.

You can use the following techniques to connect to a PDB with the SQL\*Plus `CONNECT` command:

- Local connection with operating system authentication
- Database connection using easy connect
- Database connection using a net service name

Prerequisites

The following prerequisites must be met:

- The user connecting to the PDB must be granted the `CREATE SESSION` privilege in the PDB.
- To connect to a PDB as a user that does not have `SYSDBA`, `SYSOPER`, `SYSBACKUP`, or `SYSDG` administrative privilege, the PDB must be open.

Note:

This section assumes that the user connecting to the PDB using a local user account. You can also connect to the PDB as a common user, and you can connect to the root as a common user and switch to the PDB.

To connect to a PDB using the SQL\*Plus CONNECT command:

1. Configure your environment so that you can open SQL\*Plus.
2. Start SQL\*Plus with the `/NOLOG` argument:
	```
	sqlplus /nolog
	```
3. Issue a `CONNECT` command using easy connect or a net service name to connect to the PDB.
	To connect to a PDB, connect to a service with a `PDB` property.

Example 16-1 Connecting to a PDB in SQL\*Plus Using the PDB's Net Service Name

The following command connects to the `hr` user using the `hrapp` service. The `hrapp` service has a `PDB` property for the `hrpdb` PDB. This example assumes that the client is configured to have a net service name for the `hrapp` service.

```
CONNECT hr@hrapp
```

See Also:

- " Modifying the Open Mode of PDBs " and " Modifying a PDB at the Database Level " for information about changing the open mode of a PDB.
- " [About Container Access in a CDB](administering-a-cdb-with-sql-plus.md) " for information about connecting to a PDB as a common user
- " Managing Services for PDBs "
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-895EC72B-C620-4D93-9F23-3F6DC1706764) for information about connecting to the database with SQL\*Plus

**Parent topic:** Managing Connections to a PDB

#### Managing Services for PDBs

You can create, modify, or remove services for a PDB.

- About Services for PDBs  
	Each PDB has a default service, but you can create your own using SRVCTL or `DBMS_SERVICE`.
- Managing Services for a PDB Using SRVCTL and DBMS\_SERVICE  
	You can create, modify, or remove a service with a `PDB` property.

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-1739D947-9967-4A40-8CE6-6EA7F46D4D9F)

**Parent topic:** Managing Connections to a PDB

##### About Services for PDBs

Each PDB has a default service, but you can create your own using SRVCTL or `DBMS_SERVICE`.

- The PDB Property  
	The `PDB` property associates a service with a PDB. When a client connects to a service with a `PDB` property, the current container for the connection is the PDB.
- Default and User-Defined Services  
	Creating a PDB creates a new default service for the PDB automatically.
- Tools for Managing Services  
	Oracle recommends using the SRVCTL utility to create and modify services. Alternatively, you can use the `DBMS_SERVICE` package.

**Parent topic:** Managing Services for PDBs

###### The PDB Property

The `PDB` property associates a service with a PDB. When a client connects to a service with a `PDB` property, the current container for the connection is the PDB.

The `PDB` property is required only when you do either of the following:

- Create a service
- Modify the `PDB` property of a service

You do not specify a `PDB` property when you start, stop, or remove a service. Also, you do not need to specify a `PDB` property when you modify a service without modifying its `PDB` property.

You can view the `PDB` property for a service by querying the `ALL_SERVICES` data dictionary view. Alternatively, when using the SRVCTL utility, you can use the `srvctl config service` command.

See Also:

" [About the Current Container](administering-a-cdb-with-sql-plus.md) "

**Parent topic:** About Services for PDBs

###### Default and User-Defined Services

Creating a PDB creates a new default service for the PDB automatically.

Each database service name must be unique in a CDB, and each database service name must be unique within the scope of all the CDBs whose instances are reached through a specific listener. The default service has the same name as the PDB. You cannot manage this service, which you should only use for administrative tasks.

Always use user-defined services for applications. The reason is that you can customize user-defined services to fit the requirements of your applications. Oracle recommends that you not use the default PDB service for applications.

Note:

Do not associate a service with a proxy PDB.

In an Oracle Clusterware environment, you must create an Oracle Clusterware resource for each service that is created for the PDB. When your database is being managed by Oracle Restart or Oracle Clusterware, and when you use the SRVCTL utility to start a service with a PDB property for a PDB that is closed, the PDB is opened in read/write mode on the nodes where the service is started. However, stopping a PDB service does not change the open mode of the PDB.

When you unplug or drop a PDB, the services of the unplugged or dropped PDB are not removed automatically. You can remove these services manually.

See Also:

- " Modifying a PDB with the ALTER PLUGGABLE DATABASE Statement " for information about changing the open mode of a PDB
- " [Creating a Proxy PDB That References an Application Root Replica](administering-application-containers-with-sql-plus.md) "

**Parent topic:** About Services for PDBs

###### Tools for Managing Services

Oracle recommends using the SRVCTL utility to create and modify services. Alternatively, you can use the `DBMS_SERVICE` package.

SRVCTL

If your single-instance database is being managed by Oracle Restart or your Oracle RAC database is being managed by Oracle Clusterware, then use the Server Control (SRVCTL) utility to create, modify, or remove the service.

To create a service for a PDB using the SRVCTL utility, use the `add` `service` command and specify the PDB in the `-pdb` parameter. If you do not specify `-pdb`, then the service is associated with the root.

To modify the `PDB` property of a service using the SRVCTL utility, use the `modify` `service` command and specify the PDB in the `-pdb` parameter. To remove a service for a PDB using the SRVCTL utility, use the `remove` `service` command.

You can use other SRVCTL commands to manage the service, such as the `start service`, `stop service`, and `relocate service` commands, even if they do not include the `-pdb` parameter.

The PDB name is not validated when you create or modify a service with the SRVCTL utility. However, an attempt to start a service with invalid PDB name results in an error.

DBMS\_SERVICE

If your database is not being managed by Oracle Restart or Oracle Clusterware, then use the `DBMS_SERVICE` package to create or remove a database service.

`DBMS_SERVICE` exists at the root level and in each PDB. It is owned and executed by `SYS` at each level. A PDB administrator cannot stop, relocate, or test the connection for a service that is owned by another PDB.

When you create a service with the `DBMS_SERVICE` package, the `PDB` property of the service is set to the current container. Therefore, to create a service with a `PDB` property set to a specific PDB using the `DBMS_SERVICE` package, run the `CREATE_SERVICE` procedure when the PDB is the current container. If you create a service using the `CREATE_SERVICE` procedure when the current container is the root, then the service is associated with the root.

You cannot modify the `PDB` property of a service with the `DBMS_SERVICE` package. However, you can remove a service in one PDB and create a similar service in a different PDB. In this case, the new service has the `PDB` property of the PDB in which it was created.

You can also use other `DBMS_SERVICE` subprograms to manage the service, such as the `START_SERVICE` and `STOP_SERVICE` procedures. You can use `DBMS_SERVICE.*_CONNECTION_TEST` procedures to check the health of a database connection during planned maintenance. Use the `DELETE_SERVICE` procedure to remove a service.

See Also:

- " [Example 15-36](administering-a-cdb-with-sql-plus.md) "
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-5832E064-85C6-453C-B932-99700B1732A9) for information about configuring automatic restart of an Oracle database
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ARPLS092) for information about the `DBMS_SERVICE` package
- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=RACAD076) for information about creating services in an Oracle Real Application Clusters (Oracle RAC) environment

**Parent topic:** About Services for PDBs

##### Managing Services for a PDB Using SRVCTL and DBMS\_SERVICE

You can create, modify, or remove a service with a `PDB` property.

To manage a service with a PDB property using the SRVCTL utility:

1. Log in to the host computer with the correct user account.
2. Ensure that you run SRVCTL from the correct Oracle home.
3. Perform one of the following operations:
	- To create or modify a service, run the `add service` command, and specify the PDB in the `-pdb` parameter.
		- To modify the `PDB` property of a service, run the `modify service` command, and specify the PDB in the `-pdb` parameter.
		- To remove a service, run the `remove service` command.

To create or remove a service for a PDB using the DBMS\_SERVICE package:

1. In SQL\*Plus, ensure that the current container is a PDB.
	See " Connecting to a PDB ".
2. Run the appropriate subprogram in the `DBMS_SERVICE` package.

Note:

If your database is being managed by Oracle Restart or Oracle Clusterware, then use the SRVCTL utility to manage services. Do not use the `DBMS_SERVICE` package.

Example 16-2 Creating a Service for a PDB Using the SRVCTL Utility

This example adds the `salesrep` service for the PDB `salespdb` in the CDB with `DB_UNIQUE_NAME mycdb`:

```
srvctl add service -db mycdb -service salesrep -pdb salespdb
```

Example 16-3 Modifying the PDB Property of a Service Using the SRVCTL Utility

This example modifies the `salesrep` service in the CDB with `DB_UNIQUE_NAME mycdb` to associate the service with the `hrpdb` PDB:

```
srvctl modify service 
  -db mycdb 
  -service salesrep 
  -pdb hrpdb
```

Example 16-4 Relocating a Service in Oracle RAC Using the SRVCTL Utility

You can use the `relocate service` command to relocate a service from one Oracle RAC instance, where the service is currently running, to another instance, where it can run. This technique applies both to services for administrator-managed databases as well as singleton services for policy-managed databases.

The following command relocates service `svc1` from Oracle RAC instance `cdb_inst1`, where it is currently running, to instance `cdb_inst2`, where it is currently not running:

```
srvctl relocate service 
  ­db cdb 
  ­service svc1 
  ­oldinst cdb_inst1 
  ­newinst cdb_inst2 
  –drain_timeout NNN 
  –stopoption immediate
```

The following command performs the same operation for a policy-managed database:

```
srvctl relocate service 
  ­db cdb 
  ­service svc1 
  ­currentnode cdb_inst1 
  ­targetnode cdb_inst2 
  –drain_timeout NNN 
  –stopoption immediate
```

Example 16-5 Removing a Service Using the SRVCTL Utility

This example removes the `salesrep` service in the CDB with `DB_UNIQUE_NAME` `mycdb`:

```
srvctl remove service 
  -db mycdb 
  -service salesrep
```

Example 16-6 Creating a Service for a PDB Using the DBMS\_SERVICE Package

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

Example 16-7 Removing a Service Using the DBMS\_SERVICE Package

This example removes the `salesrep` service in the current PDB.

```
BEGIN
  DBMS_SERVICE.DELETE_SERVICE(
    service_name => 'salesrep');
END;
/
```

See Also:

- " [Example 15-36](administering-a-cdb-with-sql-plus.md) "
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ARPLS092) for information about the `DBMS_SERVICE` package
- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=RACAD076) for information about managing services in an Oracle Real Application Clusters (Oracle RAC) environment

**Parent topic:** Managing Services for PDBs

#### Modifying the Listener Settings of a Referenced PDB

A PDB that is referenced by a proxy PDB is called a referenced PDB.

When the port or host name changes for the listener of the referenced PDB, you must modify the listener settings of the referenced PDB so that its proxy PDBs continue to function properly.

- Altering the Listener Host Name of a Referenced PDB  
	When the host name of the listener for a referenced PDB changes, you must run an `ALTER PLUGGABLE DATABASE CONTAINERS HOST` statement to reset the host name of the referenced PDB so that its proxy PDBs continue to function properly.
- Altering the Listener Port Number of a Referenced PDB  
	When the port number of the listener for a referenced PDB changes, you must run an `ALTER PLUGGABLE DATABASE CONTAINERS PORT` statement to reset the port number of the referenced PDB so that its proxy PDBs continue to function properly.

**Parent topic:** Managing Connections to a PDB

##### Altering the Listener Host Name of a Referenced PDB

When the host name of the listener for a referenced PDB changes, you must run an `ALTER PLUGGABLE DATABASE CONTAINERS HOST` statement to reset the host name of the referenced PDB so that its proxy PDBs continue to function properly.

A proxy PDB uses a database link to establish communication with its referenced PDB during PDB creation. After communication is established, the proxy PDB communicates directly with the referenced PDB without using the database link used during PDB creation, and the database link can be dropped. When the listener host name changes for the referenced PDB, each proxy PDB must reestablish communication with its referenced PDB.

Beginning with Oracle Database 19c, version 19.10, you can execute the `ALTER PLUGGABLE                     DATABASE CONTAINERS HOST` command in the CDB root, an application root, or a PDB by including the PDB name.

The current user must have the `ALTER DATABASE` system privilege, and the privilege must be either commonly granted or locally granted in the PDB.

1. In SQL\*Plus, ensure that the current container is the referenced PDB.
	See " Connecting to a PDB ".
2. Run an `ALTER PLUGGABLE DATABASE CONTAINERS HOST` statement and specify the new host name, or include the `RESET` keyword to return the host name to its default setting, which is the host name of the referenced PDB.
3. Drop and re-create the proxy PDBs that reference the referenced PDB to reestablish communication for each proxy PDB and its referenced PDB.

Example 16-8 Altering the Listener Host Name of a Referenced PDB

This example changes the host name for the referenced PDB to `myhost.example.com`.

```
ALTER PLUGGABLE DATABASE CONTAINERS HOST='myhost.example.com';
```

Example 16-9 Resetting the Listener Host Name to the Default Value

This example resets the host name for the referenced PDB to its default value. The default value is the host name of the referenced PDB.

```
ALTER PLUGGABLE DATABASE CONTAINERS HOST RESET;
```

See Also:

- " [Creating a PDB as a Proxy PDB](creating-a-proxy-pdb.md) "
- " [HOST Clause](creating-a-proxy-pdb.md) "

Example 16-10 Using the PDB Name When Altering the Listener Host Name

This example changes the host name for the PDB named `PDB01` to `myhost.example.com`.

```
ALTER PLUGGABLE DATABASE PDB01 CONTAINERS HOST='myhost.example.com';
```

**Parent topic:** Modifying the Listener Settings of a Referenced PDB

##### Altering the Listener Port Number of a Referenced PDB

When the port number of the listener for a referenced PDB changes, you must run an `ALTER PLUGGABLE DATABASE CONTAINERS PORT` statement to reset the port number of the referenced PDB so that its proxy PDBs continue to function properly.

A proxy PDB uses a database link to establish communication with its referenced PDB during PDB creation. After communication is established, the proxy PDB communicates directly with the referenced PDB without using the database link used during PDB creation, and the database link can be dropped. When the listener port number changes for the referenced PDB, each proxy PDB must re-establish communication with its referenced PDB.

Beginning with Oracle Database 19c, version 19.10, you can execute the `ALTER PLUGGABLE DATABASE CONTAINERS PORT` command in the CDB root, an application root, or a PDB by including the PDB name.

The current user must have the `ALTER` `DATABASE` system privilege, and the privilege must be either commonly granted or locally granted in the PDB.

1. In SQL\*Plus, ensure that the current container is the referenced PDB.
2. Run an `ALTER PLUGGABLE DATABASE CONTAINERS PORT` statement and specify the new port number, or include the `RESET` keyword to return the port number to its default setting, which is 1521.
3. Drop and re-create the proxy PDBs that reference the referenced PDB to re-establish communication for each proxy PDB and its referenced PDB.

Example 16-11 Altering the Listener Port Number of a Referenced PDB

This example changes the port number for the referenced PDB to `1543`.

```
ALTER PLUGGABLE DATABASE CONTAINERS PORT=1543;
```

Example 16-12 Resetting the Listener Port Number to the Default Value

This example resets the port number for the referenced PDB to its default value. The default value for the port number is 1521.

```
ALTER PLUGGABLE DATABASE CONTAINERS PORT RESET;
```

Example 16-13 Using the PDB Name When Altering the Listener Port Number

This example changes the port number for the PDB named `PDB01` to `1543`.

```
ALTER PLUGGABLE DATABASE PDB01 CONTAINERS PORT=1543;
```

### Modifying a PDB at the System Level

You can use the `ALTER SYSTEM` statement to modify a PDB.

- About System-Level Modifications of a PDB  
	The `ALTER SYSTEM` statement can dynamically alter a PDB. You can issue an `ALTER SYSTEM` statement when you want to change the way a PDB operates.
- Modifying a PDB with ALTER SYSTEM  
	To modify a PDB at the system level, use the `ALTER SYSTEM` statement.

**Parent topic:** Administering PDBs

#### About System-Level Modifications of a PDB

The `ALTER SYSTEM` statement can dynamically alter a PDB. You can issue an `ALTER SYSTEM` statement when you want to change the way a PDB operates.

When the current container is a PDB, you can run the following `ALTER SYSTEM` statements:

- `ALTER SYSTEM FLUSH { SHARED_POOL | BUFFER_CACHE | FLASH_CACHE }`
- `ALTER SYSTEM { ENABLE | DISABLE } RESTRICTED SESSION`
- `ALTER SYSTEM SET USE_STORED_OUTLINES`
- `ALTER SYSTEM { SUSPEND | RESUME }`
- `ALTER SYSTEM CHECKPOINT`
- `ALTER SYSTEM CHECK DATAFILES`
- `ALTER SYSTEM REGISTER`
- `ALTER SYSTEM { KILL | DISCONNECT } SESSION`
- `ALTER SYSTEM SET initialization_parameter` (for a subset of initialization parameters)

All other `ALTER SYSTEM` statements affect the entire CDB and must be run by a common user in the root.

The `ALTER SYSTEM SET initialization_parameter` statement can modify only some initialization parameters for PDBs. All initialization parameters can be set for the root. For any initialization parameter that is not set explicitly for a PDB, the PDB inherits the parameter value from the root.

You can modify an initialization parameter for a PDB when the `ISPDB_MODIFIABLE` column is `TRUE` for the parameter in the `V$SYSTEM_PARAMETER` view. The following query lists all initialization parameters that are modifiable for a PDB:

```
SELECT NAME 
FROM   V$SYSTEM_PARAMETER 
WHERE  ISPDB_MODIFIABLE='TRUE' 
ORDER BY NAME;
```

When the current container is a PDB, run the `ALTER SYSTEM SET initialization_parameter` statement to modify the PDB. The statement does not affect the root or other PDBs. The following table describes the behavior of the `SCOPE` clause when you use a server parameter file (SPFILE) and run the `ALTER SYSTEM SET` statement on a PDB.

| SCOPE Setting | Behavior |
| --- | --- |
| `MEMORY` | The initialization parameter setting is changed in memory and takes effect immediately in the PDB. The new setting affects only the PDB.  The setting reverts to the value set in the root in the any of the following cases:  - An `ALTER SYSTEM SET` statement sets the value of the parameter in the root with `SCOPE` equal to `BOTH` or `MEMORY`, and the PDB is closed and re-opened. The parameter value in the PDB is not changed if `SCOPE` is equal to `SPFILE`, and the PDB is closed and re-opened. - The PDB is closed and re-opened. - The CDB is shut down and re-opened. |
| `SPFILE` | The initialization parameter setting is changed for the PDB and stored persistently. The new setting takes effect in any of the following cases:  - The PDB is closed and re-opened. - The CDB is shut down and re-opened.  In these cases, the new setting affects only the PDB. |
| `BOTH` | The initialization parameter setting is changed in memory, and it is changed for the PDB and stored persistently. The new setting takes effect immediately in the PDB and persists after the PDB is closed and re-opened or the CDB is shut down and re-opened. The new setting affects only the PDB. |

When a PDB is unplugged from a CDB, the values of the initialization parameters that were specified for the PDB with `SCOPE=BOTH` or `SCOPE=SPFILE` are added to the PDB's XML metadata file. These values are restored for the PDB when it is plugged in to a CDB.

Note:

A text initialization parameter file (PFILE) cannot contain PDB-specific parameter values.

**Parent topic:** Modifying a PDB at the System Level

#### Modifying a PDB with ALTER SYSTEM

To modify a PDB at the system level, use the `ALTER SYSTEM` statement.

Prerequisites

The current user must be granted the following privileges, which must be either commonly granted or locally granted in the PDB:

- `CREATE SESSION`
- `ALTER SYSTEM`

To use ALTER SYSTEM to modify a PDB:

1. In SQL\*Plus, ensure that the current container is a PDB.
	See " Connecting to a PDB ".
2. Run the `ALTER SYSTEM` statement.

Example 16-14 Enable Restricted Sessions in a PDB

To restrict sessions in a PDB, issue the following statement:

```
ALTER SYSTEM ENABLE RESTRICTED SESSION;
```

Example 16-15 Changing the Statistics Gathering Level for the PDB

This `ALTER SYSTEM` statement sets the `STATISTICS_LEVEL` initialization parameter to `ALL` for the current PDB:

```
ALTER SYSTEM SET STATISTICS_LEVEL = ALL SCOPE = MEMORY;
```

See Also:

- " [Modifying a CDB with ALTER SYSTEM](administering-a-cdb-with-sql-plus.md) "
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF00902)

**Parent topic:** Modifying a PDB at the System Level

### Modifying a PDB at the Database Level

You can modify a PDB using the `ALTER PLUGGABLE DATABASE` statement.

- About PDB-Level Modifications  
	The `ALTER PLUGGABLE DATABASE` for a PDB is analogous to the `ALTER DATABASE` for a CDB.
- Modifying a PDB with the ALTER PLUGGABLE DATABASE Statement  
	To modify the attributes of a single PDB, use the `ALTER PLUGGABLE DATABASE` statement.
- Changing the Global Database Name of a PDB  
	You can change the global database name of a PDB with the `ALTER PLUGGABLE DATABASE RENAME GLOBAL_NAME TO` statement.
- Managing Refreshable Clone PDBs  
	A **refreshable clone PDB** is a read-only clone that can periodically synchronize with its source PDB.

**Parent topic:** Administering PDBs

#### About PDB-Level Modifications

The `ALTER PLUGGABLE DATABASE` for a PDB is analogous to the `ALTER DATABASE` for a CDB.

Note:

An `ALTER DATABASE` statement issued when the current container is a PDB that includes clauses that are supported for an `ALTER PLUGGABLE DATABASE` statement have the same effect as the corresponding `ALTER PLUGGABLE DATABASE` statement. However, these statements cannot include clauses that are specific to PDBs, such as the pdb\_storage\_clause, the pdb\_change\_state\_clause, the logging\_clause, and the pdb\_recovery\_clause.

- Storage Clauses  
	Use `ALTER PLUGGABLE DATABASE` to configure storage at the PDB level.
- Logging and Recovery Clauses  
	Use `ALTER PLUGGABLE DATABASE` to set logging and recovery and recovery modes at the PDB level.
- Miscellaneous Clauses  
	You can use `ALTER PLUGGABLE DATABASE` to modify the open mode, global name, time zone, and default edition.

**Parent topic:** Modifying a PDB at the Database Level

##### Storage Clauses

Use `ALTER PLUGGABLE DATABASE` to configure storage at the PDB level.

The following clauses of `ALTER PLUGGABLE DATABASE` modify PDB storage:

- database\_file\_clauses
	These clauses work the same as they would in an `ALTER DATABASE` statement, but the statement applies to the current PDB.
- `DEFAULT TABLESPACE` clause
	For users created while the current container is a PDB, this clause specifies the default tablespace for the user if the default tablespace is not specified in the `CREATE USER` statement.
- `DEFAULT TEMPORARY TABLESPACE` clause
	For users created while the current container is a PDB, this clause specifies the default temporary tablespace for the user if the default temporary tablespace is not specified in the `CREATE USER` statement.
- `SET DEFAULT { BIGFILE | SMALLFILE } TABLESPACE` clause
	This clause changes the default type of subsequently created tablespaces in the PDB to either bigfile or smallfile. This clause works the same as it would in an `ALTER DATABASE` statement, but it applies to the current PDB.
- pdb\_storage\_clause
	This clause sets a limit on the amount of storage used by all tablespaces that belong to a PDB. This limit applies to the total size of all data files and temp files comprising tablespaces that belong to the PDB.
	This clause can also set a limit on the amount of storage that can be used by unified audit OS spillover (.bin format) files in the PDB. If the limit is reached, then no additional storage is available for these files.
	This clause can also set a limit on the amount of storage in a shared temporary tablespace that can be used by sessions connected to the PDB. If the limit is reached, then no additional storage in the shared temporary tablespace is available to sessions connected to the PDB.

**Parent topic:** About PDB-Level Modifications

##### Logging and Recovery Clauses

Use `ALTER PLUGGABLE DATABASE` to set logging and recovery and recovery modes at the PDB level.

logging\_clause

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

pdb\_force\_logging\_clause

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

pdb\_recovery\_clause

Note:

This clause is available starting with Oracle Database 12c Release 1 (12.1.0.2).

`ALTER PLUGGABLE DATABASE DISABLE RECOVERY` takes the data files that belong to the PDB offline and disables recovery of the PDB. The PDB data files are not part of any recovery session until it is enabled again. Any new data files created while recovery is disabled are created as unnamed files for the PDB.

`ALTER PLUGGABLE DATABASE ENABLE RECOVERY` brings the data files that belong to the PDB online and marks the PDB for active recovery. Recovery sessions include these files.

Check the recovery status of a PDB by querying the `RECOVERY_STATUS` column in the `V$PDBS` view.

See Also:

- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SBYDB5261) for more information about the pdb\_recovery\_clause.
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-A1939693-60AC-4009-B37C-A1D8D1360D49) for information about controlling the writing of redo records
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF30009) for more information about the logging attribute

**Parent topic:** About PDB-Level Modifications

##### Miscellaneous Clauses

You can use `ALTER PLUGGABLE DATABASE` to modify the open mode, global name, time zone, and default edition.

When the current container is a PDB, an `ALTER PLUGGABLE DATABASE` statement with any of the following clauses modifies the PDB:

- pdb\_change\_state\_clause
	This clause changes the open mode of the current PDB.
	If you specify the optional `RESTRICTED` keyword, then the PDB is accessible only to users with the `RESTRICTED SESSION` privilege in the PDB.
	Specifying `FORCE` in this clause changes semantics of the `ALTER PLUGGABLE DATABASE` statement so that, in addition to opening a PDB that is currently closed, it can be used to change the open mode of a PDB that is already open.
- `RENAME GLOBAL_NAME` clause
	This clause changes the unique global database name for the PDB. The new global database name must be different from that of any container in the CDB. When you change the global database name of a PDB, the PDB name is changed to the name before the first period in the global database name.
	You must change the `PDB` property of database services used to connect to the PDB when you change the global database name.
- set\_time\_zone\_clause
	This clause works the same as it would in an `ALTER DATABASE` statement, but it applies to the current PDB.
- `DEFAULT EDITION` clause
	This clause works the same as it would in an `ALTER DATABASE` statement, but it applies to the current PDB. Each PDB can use edition-based redefinition, and editions in one PDB do not affect editions in other PDBs. In a multitenant environment in which each PDB has its own application, you can use edition-based redefinition independently for each distinct application.

See Also:

- " Managing Services for PDBs "
- " Modifying the Open Mode of PDBs with ALTER PLUGGABLE DATABASE "

**Parent topic:** About PDB-Level Modifications

#### Modifying a PDB with the ALTER PLUGGABLE DATABASE Statement

To modify the attributes of a single PDB, use the `ALTER PLUGGABLE DATABASE` statement.

When the current container is a PDB, an `ALTER PLUGGABLE DATABASE` statement modifies the PDB. The modifications overwrite the defaults set for the root in the PDB. The modifications do not affect the CDB root or other PDBs.

Prerequisites

The following prerequisites must be met:

- To change the open mode of the PDB from mounted to opened or from opened to mounted, the current user must have `SYSDBA`, `SYSOPER`, `SYSBACKUP`, or `SYSDG` administrative privilege. The privilege must be either commonly granted or locally granted in the PDB. The user must exercise the privilege using `AS sys_privilege_name` at connect time.
- For all other operations performed using the `ALTER PLUGGABLE DATABASE` statement, the current user must have the `ALTER DATABASE` system privilege, and the privilege must be either commonly granted or locally granted in the PDB.
- To close a PDB, the PDB must be open.

Note:

This section does not cover changing the global database name of a PDB using the `ALTER PLUGGABLE DATABASE` statement.

To modify a PDB:

1. In SQL\*Plus, ensure that the current container is a PDB.
2. Run an `ALTER PLUGGABLE DATABASE` statement.

Example 16-16 Changing the Open Mode of a PDB

This `ALTER PLUGGABLE DATABASE` statement changes the open mode of the current PDB to mounted.

```
ALTER PLUGGABLE DATABASE CLOSE IMMEDIATE;
```

The following statement changes the open mode of the current PDB to open read-only.

```
ALTER PLUGGABLE DATABASE OPEN READ ONLY;
```

A PDB must be in mounted mode to change its open mode to read-only or read/write unless you specify the `FORCE` keyword.

The following statement changes the open mode of the current PDB from mounted or open read-only to open read/write.

```
ALTER PLUGGABLE DATABASE OPEN FORCE;
```

The following statement changes the open mode of the current PDB from mounted to migrate.

```
ALTER PLUGGABLE DATABASE OPEN UPGRADE;
```

Example 16-17 Bringing a Data File Online for a PDB

This `ALTER PLUGGABLE DATABASE` statement uses a database\_file\_clause to bring the `/u03/oracle/pdb1_01.dbf` data file online.

```
ALTER PLUGGABLE DATABASE DATAFILE '/u03/oracle/pdb1_01.dbf' ONLINE;
```

Example 16-18 Changing the Default Tablespaces for a PDB

This `ALTER PLUGGABLE DATABASE` statement uses a `DEFAULT TABLESPACE` clause to set the default permanent tablespace to `pdb1_tbs` for the PDB.

```
ALTER PLUGGABLE DATABASE DEFAULT TABLESPACE pdb1_tbs;
```

This `ALTER PLUGGABLE DATABASE` statement uses a `DEFAULT TEMPORARY TABLESPACE` clause to set the default temporary tablespace to `pdb1_temp` for the PDB.

```
ALTER PLUGGABLE DATABASE DEFAULT TEMPORARY TABLESPACE pdb1_temp;
```

The tablespace or tablespace group specified in the `ALTER PLUGGABLE DATABASE` statement must exist in the PDB. Users whose current container is a PDB that are not explicitly assigned a default tablespace or default temporary tablespace use the default tablespace or default temporary tablespace for the PDB.

Example 16-19 Changing the Default Tablespace Type for a PDB

This `ALTER DATABASE` statement uses a `SET DEFAULT TABLESPACE` clause to change the default tablespace type to bigfile for the PDB.

```
ALTER PLUGGABLE DATABASE SET DEFAULT BIGFILE TABLESPACE;
```

Example 16-20 Setting Storage Limits for a PDB

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

Example 16-21 Setting the Logging Attribute of a PDB

With the PDB open in restricted mode, this statement specifies the `NOLOGGING` attribute for the PDB:

```
ALTER PLUGGABLE DATABASE NOLOGGING;
```

Example 16-22 Setting the Force Logging Mode of a PDB

This statement enables force logging mode for the PDB:

```
ALTER PLUGGABLE DATABASE ENABLE FORCE LOGGING;
```

Example 16-23 Setting the Default Edition for a PDB

This example sets the default edition for the current PDB to `PDB1E3`.

```
ALTER PLUGGABLE DATABASE DEFAULT EDITION = PDB1E3;
```

See Also:

- " About PDB-Level Modifications " for information about the clauses that modify the attributes of a single PDB
- " Changing the Global Database Name of a PDB "
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF55667) for more information about the `ALTER PLUGGABLE DATABASE` statement
- [Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADFNS020) for a complete discussion of edition-based redefinition

**Parent topic:** Modifying a PDB at the Database Level

#### Changing the Global Database Name of a PDB

You can change the global database name of a PDB with the `ALTER PLUGGABLE DATABASE RENAME GLOBAL_NAME TO` statement.

When you change the global database name of a PDB, the new global database name must be different from that of any container in the CDB.

Prerequisites

The following prerequisites must be met:

- The current user must have the `ALTER DATABASE` system privilege, and the privilege must be either commonly granted or locally granted in the PDB.
- For an Oracle Real Application Clusters (Oracle RAC) database, the PDB must be open on the current instance only. The PDB must be closed on all other instances.
- The PDB being modified must be opened on the current instance in read/write mode with `RESTRICTED` specified so that it is accessible only to users with `RESTRICTED SESSION` privilege in the PDB.

To change the global database name of a PDB:

1. In SQL\*Plus, ensure that the current container is a PDB.
2. Run an `ALTER PLUGGABLE DATABASE RENAME GLOBAL_NAME TO` statement.
	The following example changes the global database name of the PDB to `salespdb.example.com`:
	```
	ALTER PLUGGABLE DATABASE RENAME GLOBAL_NAME TO salespdb.example.com;
	```
3. Close the PDB.
4. Open the PDB in read/write mode.

When you change the global database name of a PDB, the PDB name is changed to the first part of the new global name, which is the part before the first period. Also, Oracle Database changes the name of the default database service for the PDB automatically. Oracle Database also changes the `PDB` property of all database services in the PDB to the new global name of the PDB. You must close the PDB and open it in read/write mode for Oracle Database to complete the integration of the new PDB service name into the CDB.

Oracle Net Services must be configured properly for clients to access database services. You might need to alter your Oracle Net Services configuration because of the PDB name change.

See Also:

- " Connecting to a PDB "
- " Managing Services for PDBs " for information about PDBs and database services

**Parent topic:** Modifying a PDB at the Database Level

#### Managing Refreshable Clone PDBs

A **refreshable clone PDB** is a read-only clone that can periodically synchronize with its source PDB.

- Refreshing a PDB  
	You can refresh a PDB that was created as a refreshable clone.
- Switching Over a Refreshable Clone PDB  
	You can switch the roles of a source PDB and its refreshable clone PDB.

**Parent topic:** Modifying a PDB at the Database Level

##### Refreshing a PDB

You can refresh a PDB that was created as a refreshable clone.

When you refresh a PDB manually, changes made to the source PDB since the last refresh are propagated to the PDB being refreshed. You can manually refresh a PDB that is configured for automatic refresh.

Prerequisites

To refresh a PDB, the PDB must have been created as a clone with the `REFRESH MODE MANUAL` or `REFRESH MODE EVERY minutes` clause included.

1. In SQL\*Plus, ensure that the current container is the PDB you want to refresh.
2. If the PDB is not closed, then close the PDB. For example, issue the following SQL statement:
	`ALTER PLUGGABLE DATABASE CLOSE IMMEDIATE;`
3. Issue the following SQL statement:
	`ALTER PLUGGABLE DATABASE REFRESH;`

##### Switching Over a Refreshable Clone PDB

You can switch the roles of a source PDB and its refreshable clone PDB.

The following statement performs a switchover:

```
ALTER PLUGGABLE DATABASE refresh_mode FROM clonepdb@dblink SWITCHOVER;
```

You must not specify `REFRESH MODE NONE` for `refresh_mode`. The database link specified in the `FROM` clause must point to the root of the CDB in which the clone PDB resides.

After the switchover completes, the source PDB becomes the refreshable clone PDB, which can only be opened in `READ ONLY` mode.

Prerequisites

You must meet the following prerequisites:

- You must be connected to the source PDB when you issue `ALTER PLUGGABLE DATABASE ... SWITCHOVER`.
- If the source PDB and clone PDB are in separate CDBs, then the user specified in the database link must have the same name and password in the source PDB and clone PDB.

To switch the roles of the source and clone PDBs:

1. In SQL\*Plus or SQL Developer, log in to the source PDB.
2. Execute the `ALTER PLUGGABLE DATABASE refresh_mode FROM clonepdb@dblink SWITCHOVER` statement.
	After the statement completes, the currently connected PDB is now the refreshable clone PDB.
3. Optionally, refresh the clone PDB:
	```
	ALTER PLUGGABLE DATABASE REFRESH;
	```

Example 16-24 Switching Over a Refreshable Clone PDB

This example assumes that your data center contains CDBs named `cdb1` and `cdb2`. The PDB named `cdb1_pdb1` resides in `cdb1`. You want to create a refreshable clone of this PDB in `cdb2` and name it `cdb1_pdb1_ref`. Your goal is to switch over `cdb1_pdb1_ref` so that it becomes the source PDB and `cdb1_pdb1` becomes the clone PDB.

1. In SQL\*Plus, connect to `cdb1` as a user with administrator privileges, and then ensure sure that `cdb1_pdb1` is open in read/write mode (sample output included):
	```
	CONNECT SYS@cdb1 AS SYSDBA
	Enter password: *******
	ALTER PLUGGABLE DATABASE ALL CLOSE;
	ALTER PLUGGABLE DATABASE cdb1_pdb1 OPEN READ WRITE;
	SHOW PDBS;
	    CON_ID CON_NAME                       OPEN MODE  RESTRICTED
	---------- ------------------------------ ---------- ----------
	         2 PDB$SEED                       READ ONLY  NO
	         3 CDB1_PDB1                      READ WRITE NO
	```
2. Create a common user named `c##u1` (replace pwd with a user-specified password):
	```
	DROP USER c##u1 CASCADE;
	CREATE USER c##u1 IDENTIFIED BY pwd;
	GRANT CREATE SESSION, RESOURCE, CREATE ANY TABLE, UNLIMITED TABLESPACE TO c##u1 CONTAINER=ALL;
	GRANT CREATE PLUGGABLE DATABASE TO c##u1 CONTAINER=ALL;
	GRANT SYSOPER TO c##u1 CONTAINER=ALL;
	```
3. Set the container to `cdb1_pdb1`, and then create a table `t1` to use for testing (sample output included):
	```
	ALTER SESSION SET CONTAINER = cdb1_pdb1;
	CREATE TABLE t1(n1 NUMBER);
	INSERT INTO t1 VALUES(1);
	COMMIT;
	SELECT * FROM t1;
	        N1
	----------
	         1
	```
4. Connect to `cdb2` as a user with administrator privileges, and then create the common user named `c##u1` (replace pwd with a user-specified password):
	```
	CONNECT SYS@cdb2 AS SYSDBA
	Enter password: *******
	DROP USER c##u1 CASCADE;
	CREATE USER c##u1 IDENTIFIED BY pwd;
	GRANT CREATE SESSION, RESOURCE, CREATE ANY TABLE, UNLIMITED TABLESPACE TO c##u1 CONTAINER=ALL;
	GRANT CREATE PLUGGABLE DATABASE TO c##u1 CONTAINER=ALL;
	GRANT SYSOPER TO c##u1 CONTAINER=ALL;
	```
	Now `cdb1` and `cdb2` both have a common user with the same name (`c##u1`) and password.
5. Create a database link to `cdb1`.
	The following command specifies user `c##u1`, password pwd, and service name `cdb1`:
	```
	CREATE DATABASE LINK cdb1_datalink CONNECT TO c##u1 IDENTIFIED BY pwd USING 'cdb1';
	```
6. Create the manually refreshable PDB named `cdb1_pdb1_ref`.
	The following statement specifies the database link `cdb1_datalink` and the file destination `/dsk1/df`:
	```
	CREATE PLUGGABLE DATABASE cdb1_pdb1_ref FROM cdb1_pdb1@cdb1_datalink 
	  CREATE_FILE_DEST='/dsk1/df' 
	  REFRESH MODE MANUAL;
	```
7. Refresh `cdb1_pdb1_ref`:
	```
	ALTER SESSION SET CONTAINER = cdb1_pdb1_ref;
	ALTER PLUGGABLE DATABASE REFRESH;
	```
8. Query `t1` to check that the refreshable clone PDB contains the correct contents (sample output included):
	```
	ALTER PLUGGABLE DATABASE OPEN READ ONLY;
	SELECT * FROM t1;
	        N1
	----------
	         1
	```
9. Connect to `cdb1` as a user with administrator privileges, and then create a database link to `cdb2`:
	```
	CONNECT SYS@cdb1 AS SYSDBA
	Enter password: *******
	CREATE DATABASE LINK cdb2_datalink CONNECT TO c##u1 IDENTIFIED BY pwd USING 'cdb2';
	```
	The preceding statement specifies user `c##u1`, password pwd, and service name `cdb2`.
10. Set the container to `cdb1_pdb1`, and then switch over so that `cdb1_pdb1_ref` is the primary PDB and the current PDB is the clone:
	```
	ALTER SESSION SET CONTAINER = cdb1_pdb1;
	ALTER PLUGGABLE DATABASE 
	  REFRESH MODE MANUAL 
	  FROM cdb1_pdb1_ref@cdb2_datalink 
	  SWITCHOVER;
	```
11. Query `t1` to check that the current PDB, which is now the refreshable clone PDB, contains the correct contents (sample output included):
	```
	ALTER PLUGGABLE DATABASE OPEN READ ONLY;
	SELECT * FROM t1;
	        N1
	----------
	         1
	```
12. Connect to `cdb2` as a user with administrator privileges, set the container to the new source PDB `cdb1_pdb1_ref`, and then insert a new row into table `t1` (sample output included):
	```
	CONNECT SYS@cdb2 AS SYSDBA
	Enter password: *******
	ALTER SESSION SET CONTAINER = cdb1_pdb1_ref;
	SELECT * FROM t1;
	        N1
	----------
	         1
	INSERT INTO t1 VALUES(2);
	COMMIT;
	SELECT * FROM t1;
	        N1
	----------
	         1
	         2
	```
13. Connect to `cdb1` as a user with administrator privileges, set the container to `cdb1_pdb1` (which is the new clone), refresh it, and then query `t1`:
	```
	CONNECT SYS@cdb1 AS SYSDBA
	Enter password: *******
	ALTER SESSION SET CONTAINER = cdb1_pdb1;
	ALTER PLUGGABLE DATABASE CLOSE IMMEDIATE;
	ALTER PLUGGABLE DATABASE REFRESH;
	ALTER PLUGGABLE DATABASE OPEN READ ONLY;
	SELECT * FROM t1;
	        N1
	----------
	         1
	         2
	```
	The preceding output shows that the clone `cdb1_pdb1` was refreshed from the source `cdb1_pdb1_ref`.

**Parent topic:** Managing Refreshable Clone PDBs

### Modifying the Open Mode of PDBs

You can modify the open mode of a PDB by using the `ALTER PLUGGABLE DATABASE` SQL statement or the SQL\*Plus `STARTUP` command.

- About the Open Mode of a PDB  
	When a PDB is mounted, you can open it in read/write, read-only, or `MIGRATE` mode. You can also mount a PDB without opening it.
- Modifying the Open Mode of PDBs with ALTER PLUGGABLE DATABASE  
	You can modify the open mode of PDBs with the `ALTER PLUGGABLE DATABASE` statement with a pdb\_change\_state clause.
- Preserving or Discarding the Open Mode of PDBs When the CDB Restarts  
	You can preserve the open mode of one or more PDBs when the CDB restarts by using the `ALTER PLUGGABLE DATABASE` SQL statement with a pdb\_save\_or\_discard\_state clause.
- Altering the Open Mode of a PDB Using STARTUP and SHUTDOWN  
	When the current container is a PDB, you can use the SQL\*Plus `STARTUP` command to open the PDB and the SQL\*Plus `SHUTDOWN` command to close the PDB.
- Starting and Stopping PDBs in Oracle RAC  
	You can use SRVCTL commands to manage PDBs.

**Parent topic:** Administering PDBs

#### About the Open Mode of a PDB

When a PDB is mounted, you can open it in read/write, read-only, or `MIGRATE` mode. You can also mount a PDB without opening it.

- Summary of PDB Open Modes  
	Depending on the options that you specify in `ALTER PLUGGABLE DATABASE OPEN`, the PDB opens in different modes.
- Clauses for Changing the Open State of PDBs  
	To change the open mode of a PDB when the current container is the CDB root, specify the pdb\_change\_state clause of `ALTER PLUGGABLE DATABASE`.
- Compatibility Checks When a PDB Is Opened  
	When a PDB is opened, Oracle Database checks the compatibility of the PDB with the CDB.
- How to Disable or Enable Replay Upgrade  
	By default, the Oracle Multitenant Replay Upgrade (Replay Upgrade) method is enabled for upgrades on PDBs and CDBs. However, you can enable or disable the use of the Replay Upgrade method.

**Parent topic:** Modifying the Open Mode of PDBs

##### Summary of PDB Open Modes

Depending on the options that you specify in `ALTER PLUGGABLE DATABASE OPEN`, the PDB opens in different modes.

You can view the current open mode of PDBs by querying the `V$PDBS.OPEN_MODE` column. The following table describes the possible PDB open modes.

Table 16-2 PDB Mount and Open Modes

| Mode | Description | Notes |
| --- | --- | --- |
| Read/Write | When you run `ALTER PLUGGABLE DATABASE OPEN READ WRITE`, the PDB allows queries and user transactions to proceed and allows users to generate redo logs.  This is the default open mode except when a PDB belongs to a physical standby database. | If you specify the optional `RESTRICTED` keyword, then the PDB is accessible only to users with the `RESTRICTED SESSION` privilege in the PDB. If you also specify `FORCE`, then all sessions connected to the PDB that do not have the `RESTRICTED SESSION` privilege in the PDB are terminated, and their transactions are rolled back. |
| Read-Only | When you run `ALTER PLUGGABLE DATABASE OPEN READ ONLY`, the PDB allows queries but not user changes.  This is the default open mode when a PDB belongs to a physical standby database. | Database administrators can create, modify, or drop common users and roles in the CDB. The CDB applies these changes to the PDB when its open mode is changed to read/write mode. Before the changes are applied, descriptions of common users and roles in the PDB might be different from the descriptions in the rest of the CDB.  If you specify the optional `RESTRICTED` keyword, then the PDB is accessible only to users with the `RESTRICTED SESSION` privilege in the PDB. If you also specify `FORCE`, then all sessions connected to the PDB that do not have the `RESTRICTED SESSION` privilege in the PDB are terminated, and their transactions are rolled back. |
| Migrate | When you run `ALTER PLUGGABLE DATABASE OPEN UPGRADE`, the PDB is in `MIGRATE` mode. You can run database upgrade scripts on the PDB. | If you specify the optional `RESTRICTED` keyword, then the PDB is accessible only to users with the `RESTRICTED SESSION` privilege in the PDB. |
| Mounted | When you run `ALTER PLUGGABLE DATABASE CLOSE` in an open PDB, then the PDB is mounted. The PDB does not allow changes to any objects. In this state, the PDB is accessible only to database administrators. The PDB cannot read from or write to data files. Information about the PDB is removed from memory caches. Consistent backups of the PDB are supported. | Database administrators can create, modify, or drop common users and roles in the CDB. The CDB applies these changes to the PDB when its open mode is changed to read/write mode. Before the changes are applied, descriptions of common users and roles in the PDB might be different from the descriptions in the rest of the CDB. |

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF-GUID-A29491AD-8F0F-4E52-9D94-57FC3FF8FBC7) to learn more about the `ALTER PLUGGABLE DATABASE OPEN` command

**Parent topic:** About the Open Mode of a PDB

##### Clauses for Changing the Open State of PDBs

To change the open mode of a PDB when the current container is the CDB root, specify the pdb\_change\_state clause of `ALTER PLUGGABLE DATABASE`.

- OPEN and CLOSE Clauses  
	`READ WRITE` is the default for `ALTER PLUGGABLE DATABASE OPEN` unless a PDB being opened belongs to a CDB used as a physical standby database, in which case `READ ONLY` is the default.
- SERVICES Clause  
	You can use the services clause to specify the services that are started when a single PDB is opened.
- INSTANCES Clause  
	In an Oracle RAC CDB, you can use the instances clause to specify the instances on which the PDB is modified.
- The RELOCATE Clause  
	In an Oracle Real Application Clusters environment, use `RELOCATE` to instruct the database to reopen the PDB on a different Oracle RAC instance.

**Parent topic:** About the Open Mode of a PDB

###### OPEN and CLOSE Clauses

`READ WRITE` is the default for `ALTER PLUGGABLE DATABASE OPEN` unless a PDB being opened belongs to a CDB used as a physical standby database, in which case `READ ONLY` is the default.

When you specify PDBs to open or close, you can do the following:

- List one or more PDBs.
- Specify `ALL` to modify all PDBs.
- Specify `ALL EXCEPT` to modify all PDBs, except for the PDBs listed.

The following table describes the clauses of the `ALTER PLUGGABLE DATABASE` statement that modify the mode of a PDB.

Table 16-3 ALTER PLUGGABLE DATABASE Clauses That Modify the Mode of a PDB

| Clause | Description |
| --- | --- |
| `OPEN READ WRITE [RESTRICTED] [FORCE]` | Opens the PDB in read/write mode.  When `RESTRICTED` is specified, the PDB is accessible only to users with `RESTRICTED SESSION` privilege in the PDB. All sessions connected to the PDB that do not have `RESTRICTED SESSION` privilege on it are terminated, and their transactions are rolled back.  When `FORCE` is specified, the statement opens a PDB that is currently closed and changes the open mode of a PDB that is in open read-only mode. |
| `OPEN READ ONLY[RESTRICTED] [FORCE]` | Opens the PDB in read-only mode.  When `RESTRICTED` is specified, the PDB is accessible only to users with `RESTRICTED SESSION` privilege in the PDB. All sessions connected to the PDB that do not have `RESTRICTED SESSION` privilege on it are terminated.  When `FORCE` is specified, the statement opens a PDB that is currently closed and changes the open mode of a PDB that is in open read/write mode. |
| `OPEN UPGRADE [RESTRICTED]` | Opens the PDB in migrate mode.  When `RESTRICTED` is specified, the PDB is accessible only to users with `RESTRICTED SESSION` privilege in the PDB. |
| `CLOSE [IMMEDIATE\|ABORT]` | Places the PDB in mounted mode.  The `CLOSE` statement is the PDB equivalent of the SQL\*Plus `SHUTDOWN` command. If you do not specify `IMMEDIATE` or `ABORT`, then the PDB is shut down with the normal mode.  When `IMMEDIATE` is specified, this statement is the PDB equivalent of the SQL\*Plus `SHUTDOWN IMMEDIATE` command.  If the CDB is in `ARCHIVELOG` mode, and if `ABORT` is specified, then the PDB is forcefully closed. The PDB data files are not checkpointed or accessed during this process. If other instances have the PDB open, then an available instance performs instance recovery automatically. During this time, access to the PDB on other instances may observe a brown-out time. If no instance has the PDB open, then the next PDB open may cause automatic media recovery. If automatic media recovery fails (for example, because of inaccessible files), then you must manually recover the PDB before opening it.  If the PDB keystore was in an open state, then `ALTER PLUGGABLE DATABASE CLOSE` does not close it. To close the keystore, run the `ADMINISTER KEY MANAGEMENT SET KEYSTORE CLOSE IDENTIFIED BY "pdb_ks_pwd"` command. |

**Parent topic:** Clauses for Changing the Open State of PDBs

###### SERVICES Clause

You can use the services clause to specify the services that are started when a single PDB is opened.

The clause has the following variations:

- List one or more services in the services clause in the following form:
	```
	SERVICES = ('service_name' [,'service_name'] … )
	```
- Specify `ALL` in the services clause to start all PDB’s services, as in the following example:
	```
	SERVICES = ALL
	```
- Specify `ALL EXCEPT` in the services clause to start all PDB’s services, except for the services listed, in the following form:
	```
	SERVICES = ALL EXCEPT('service_name' [,'service_name'] … )
	```
- Specify `NONE` in the services clause to start only the PDB’s default service and none of the other PDB’s services, as in the following example:
	```
	SERVICES = NONE
	```
	`NONE` is the default setting for the services clause. A PDB’s default service is always started, regardless of the setting for the services clause.

**Parent topic:** Clauses for Changing the Open State of PDBs

###### INSTANCES Clause

In an Oracle RAC CDB, you can use the instances clause to specify the instances on which the PDB is modified.

You can close a PDB in some instances and leave it open in others. The instances clause has the following variations:

- List one or more instances in the instances clause in the following form:
	```
	INSTANCES = ('instance_name' [,'instance_name'] … )
	```
- Specify `ALL` in the instances clause to modify the PDB in all running instances, as in the following example:
	```
	INSTANCES = ALL
	```
- Specify `ALL EXCEPT` in the instances clause to modify the PDB in all instances, except for the instances listed, in the following form:
	```
	INSTANCES = ALL EXCEPT('instance_name' [,'instance_name'] … )
	```

**Parent topic:** Clauses for Changing the Open State of PDBs

###### The RELOCATE Clause

In an Oracle Real Application Clusters environment, use `RELOCATE` to instruct the database to reopen the PDB on a different Oracle RAC instance.

You can use the following options:

- Specify `NORELOCATE`, the default, to close the PDB in the current instance.
- Specify `RELOCATE TO` and specify an instance name to reopen the PDB in the specified instance.
- Specify `RELOCATE` to reopen the PDB on a different instance that is selected by Oracle Database.

Note:

If both the services clause and the instances clause are specified in the same `ALTER PLUGGABLE DATABASE` statement, then the specified services are started on the specified instances.

**Parent topic:** Clauses for Changing the Open State of PDBs

##### Compatibility Checks When a PDB Is Opened

When a PDB is opened, Oracle Database checks the compatibility of the PDB with the CDB.

Opening a PDB upgrades it automatically when a version mismatch occurs between the PDB and the CDB root. The Replay Upgrade on PDB Open optimization, which is the default, avoids manual error correction by re-executing statements stored in capture tables. The mechanism is the same used in application synchronization. Oracle Database 21c uses Replay Upgrade on PDB Open in the following scenarios:

- You plug in a PDB that was unplugged from a CDB in a previous release. When the PDB is opened, the database automatically performs a Replay Upgrade.
- A CDB from a previous release was upgraded to Oracle Database 21c, but a PDB in the CDB was not upgraded. If you open this PDB without the `OPEN UPGRADE` option, then the CDB automatically performs a Replay Upgrade of the PDB.

The Replay Upgrade on PDB Open feature requires that database properties `PDB_UPGRADE_SYNC` and `UPGRADE_PDB_ON_OPEN` be set to the default value of `true`. If either property is `false`, then a classic upgrade is required before you can open the PDB. If a problem occurs during replay upgrade or classic upgrade, then the CDB records a compatibility violation.

A compatibility violation is either of the following:

- Warning
	The database records the warning in the alert log, and then opens the PDB normally without displaying a warning message.
- Error
	The database displays a message when the PDB is opened stating that the PDB was altered with errors, and records the errors in the alert log. You must correct the condition that caused each error. When there are errors, the PDB is opened, but access to the PDB is limited to users with `RESTRICTED SESSION` privilege so that the compatibility violations can be addressed. You can view descriptions of violations by querying the `PDB_PLUG_IN_VIOLATIONS` view.

See Also:

- " Modifying the Open Mode of PDBs " to learn how to modify the open mode of one or more PDBs when the current container is the root
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=REFRN-GUID-845E5369-CCB0-4F8D-AE09-447EF0CAC93F) to learn about the `PDB_PLUG_IN_VIOLATIONS` view

**Parent topic:** About the Open Mode of a PDB

##### How to Disable or Enable Replay Upgrade

By default, the Oracle Multitenant Replay Upgrade (Replay Upgrade) method is enabled for upgrades on PDBs and CDBs. However, you can enable or disable the use of the Replay Upgrade method.

To disable the Parallel Upgrade Utility (`catctl.pl`) default of performing a Replay Upgrade, run the following command, on either `CDB$ROOT` or a particular PDB:

```
ALTER DATABASE UPGRADE SYNC OFF
```

To re-enable the Replay Upgrade behavior, enter the following command

```
ALTER DATABASE UPGRADE SYNC ON
```

You can also select a non-replay upgrade by setting the Parallel Upgrade Utility (`catctl.pl`) parameter `-t`, which forces a non-replay upgrade that uses the classic scripting method.

Note:

You can manage use of the Replay Upgrade method on the entire CDB, or on individual PDBs, depending on whether you are connected to `CDB$ROOT`, or to a particular PDB:

- If `UPGRADE SYNC` is set to `OFF` in `CDB$ROOT`, then the Replay Upgrade method is not used for any PDBs plugged into the CDB.
- If `UPGRADE SYNC` is set to `ON` in `CDB$ROOT`, but set to `OFF` for a PDB, then the Replay Upgrade method is not used for the PDB where `UPGRADE SYNC` is `OFF`, but the Replay Upgrade method is used for all other PDBs plugged into the CDB.
- If `UPGRADE SYNC` is set to `ON` in `CDB$ROOT`, and set to `ON` for all PDBs (the default), then the Replay Upgrade method is used for all PDBs plugged into the CDB.

**Parent topic:** About the Open Mode of a PDB

#### Modifying the Open Mode of PDBs with ALTER PLUGGABLE DATABASE

You can modify the open mode of PDBs with the `ALTER PLUGGABLE DATABASE` statement with a pdb\_change\_state clause.

Prerequisites

To change the open mode of PDBs with the `ALTER PLUGGABLE DATABASE` statement, you must meet the following prerequisites:

- The current user must have one of the following administrative privileges, which must be either commonly granted or locally granted in the PDB:
	- `SYSDBA`, exercised using `AS SYSDBA` at connect time
		- `SYSOPER`, exercised using `AS SYSOPER` at connect time
		- `SYSBACKUP`, exercised using `SYSBACKUP` at connect time
		- `SYSDG`, exercised using `AS SYSDG` at connect time
	Note:
	You can modify the open mode of a PDB when the current container is the PDB.
- When `RESTRICTED SESSION` is enabled, you must specify `RESTRICTED` when a PDB is opened.
- In an Oracle RAC CDB, if a PDB is open in one or more Oracle RAC instances, then it can be opened in additional instances. However, the PDB must be opened in the same mode as in the instances in which it is already open. A PDB can be closed in some instances and opened on others.

To place PDBs in a target mode with the `ALTER PLUGGABLE DATABASE` statement, you must meet the requirements described in the following table.

Table 16-4 Modifying the Open Mode of PDBs with ALTER PLUGGABLE DATABASE

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

To modify the open mode:

1. In SQL\*Plus, ensure that the current container is the root.
	See " [About Container Access in a CDB](administering-a-cdb-with-sql-plus.md) ".
2. Run an `ALTER PLUGGABLE DATABASE` statement with a pdb\_change\_state clause.

Example 16-25 Changing the Open Mode of Listed PDBs

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

Example 16-26 Changing the Open Mode of All PDBs

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

Example 16-27 Changing the Open Mode of All PDBs Except for Listed Ones

This statement changes the mode of all PDBs except for `salespdb` and `hrpdb` to mounted mode.

```
ALTER PLUGGABLE DATABASE ALL EXCEPT salespdb, hrpdb
   CLOSE IMMEDIATE;
```

Note:

An `ALTER PLUGGABLE DATABASE` statement modifying the open mode of a PDB is instance-specific. Therefore, if this statement is issued when connected to an Oracle RAC instance, then it affects the open mode of the PDB only in that instance.

See Also:

- " Clauses for Changing the Open State of PDBs "
- " Modifying a PDB at the Database Level " for information about modifying the other attributes of a PDB
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-2042AAE4-DAE5-4CD4-89E9-B9DE3A8A2AA1) for information about database modes and their uses
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF55667)
- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=CNCPT89041) for more information about shutdown modes

**Parent topic:** Modifying the Open Mode of PDBs

#### Preserving or Discarding the Open Mode of PDBs When the CDB Restarts

You can preserve the open mode of one or more PDBs when the CDB restarts by using the `ALTER PLUGGABLE DATABASE` SQL statement with a pdb\_save\_or\_discard\_state clause.

You can do this in the following way:

- Specify `SAVE STATE` to preserve the PDBs' mode when the CDB is restarted.
	For example, if a PDB is in open read/write mode before the CDB is restarted, then the PDB is in open read/write mode after the CDB is restarted; if a PDB is in mounted mode before the CDB is restarted, then the PDB is in mounted mode after the CDB is restarted.
- Specify `DISCARD STATE` to ignore the PDBs' open mode when the CDB is restarted.
	When `DISCARD STATE` is specified for a PDB, the PDB is always mounted after the CDB is restarted.

You can specify which PDBs to modify in the following ways:

- List one or more PDBs.
- Specify `ALL` to modify all PDBs.
- Specify `ALL EXCEPT` to modify all PDBs, except for the PDBs listed.

For an Oracle RAC CDB, you can use the instances clause in the pdb\_save\_or\_discard\_state clause to specify the instances on which a PDB's open mode is preserved in the following ways:

- List one or more instances in the instances clause in the following form:
	```
	INSTANCES = ('instance_name' [,'instance_name'] … )
	```
- Specify `ALL` in the instances clause to modify the PDB in all running instances, as in the following example:
	```
	INSTANCES = ALL
	```
- Specify `ALL EXCEPT` in the instances clause to modify the PDB in all instances, except for the instances listed, in the following form:
	```
	INSTANCES = ALL EXCEPT('instance_name' [,'instance_name'] … )
	```

For a PDB in an Oracle RAC CDB, `SAVE STATE` and `DISCARD STATE` only affect the mode of the current instance. They do not affect the mode of other instances, even if more than one instance is specified in the instances clause.

To issue an `ALTER PLUGGABLE DATABASE` SQL statement with a pdb\_save\_or\_discard\_state clause, the current user must have the `ALTER DATABASE` privilege in the root.

You can check the saved states for the PDBs in a CDB by querying the `DBA_PDB_SAVED_STATES` view.

To preserve or discard a PDB's open mode when the CDB restarts:

1. In SQL\*Plus, ensure that the current container is the root.
	See " [About Container Access in a CDB](administering-a-cdb-with-sql-plus.md) ".
2. Run an `ALTER PLUGGABLE DATABASE` statement with a pdb\_save\_or\_discard\_state clause.

The following examples either preserve or discard the open mode of one or more PDBs when the CDB restarts.

Example 16-28 Preserving the Open Mode of a PDB When the CDB Restarts

This statement preserves the open mode of the `salespdb` when the CDB restarts.

```
ALTER PLUGGABLE DATABASE salespdb SAVE STATE;
```

Example 16-29 Discarding the Open Mode of a PDB When the CDB Restarts

This statement discards the open mode of the `salespdb` when the CDB restarts.

```
ALTER PLUGGABLE DATABASE salespdb DISCARD STATE;
```

Example 16-30 Preserving the Open Mode of All PDBs When the CDB Restarts

This statement preserves the open mode of all PDBs when the CDB restarts.

```
ALTER PLUGGABLE DATABASE ALL SAVE STATE;
```

Example 16-31 Preserving the Open Mode of Listed PDBs When the CDB Restarts

This statement preserves the open mode of the `salespdb` and `hrpdb` when the CDB restarts.

```
ALTER PLUGGABLE DATABASE salespdb, hrpdb SAVE STATE;
```

Example 16-32 Preserving the Open Mode of All PDBs Except for Listed Ones When the CDB Restarts

This statement preserves the open mode of all PDBs except for `salespdb` and `hrpdb`.

```
ALTER PLUGGABLE DATABASE ALL EXCEPT salespdb, hrpdb SAVE STATE;
```

**Parent topic:** Modifying the Open Mode of PDBs

#### Altering the Open Mode of a PDB Using STARTUP and SHUTDOWN

When the current container is a PDB, you can use the SQL\*Plus `STARTUP` command to open the PDB and the SQL\*Plus `SHUTDOWN` command to close the PDB.

- About Modifying the Open Mode of PDBs with the SQL\*Plus STARTUP Command  
	When the current container is the root, the `STARTUP PLUGGABLE DATABASE` command can open a single PDB.
- Starting Up a PDB Using the STARTUP Command  
	When the current container is a PDB, the SQL\*Plus `STARTUP` command opens the PDB.
- Modifying the Open Mode of PDBs with the SQL\*Plus STARTUP Command  
	You can use the `STARTUP PLUGGABLE DATABASE` command to open a single PDB.
- Shutting Down a PDB Using the SHUTDOWN Command  
	When the current container is a PDB, the SQL\*Plus `SHUTDOWN` command closes the PDB.

**Parent topic:** Modifying the Open Mode of PDBs

##### About Modifying the Open Mode of PDBs with the SQL\*Plus STARTUP Command

When the current container is the root, the `STARTUP PLUGGABLE DATABASE` command can open a single PDB.

Use the following options of the `STARTUP PLUGGABLE DATABASE` command to open a PDB:

- `FORCE`
	Closes an open PDB before re-opening it in read/write mode. When this option is specified, no other options are allowed.
- `RESTRICT`
	Enables only users with the `RESTRICTED SESSION` system privilege in the PDB to access the PDB.
	If neither `OPEN READ WRITE` nor `OPEN READ ONLY` is specified, then the PDB is opened in read-only mode when the CDB to which it belongs is a physical standby database. Otherwise, the PDB is opened in read/write mode.
- `OPEN` open\_pdb\_options
	Opens the PDB in either read/write mode or read-only mode. You can specify `OPEN READ WRITE` or `OPEN READ ONLY`. When you specify `OPEN` without any other options, `READ WRITE` is the default.

The following prerequisites must be met:

- The current user must have `SYSDBA`, `SYSOPER`, `SYSBACKUP`, or `SYSDG` administrative privilege, and the privilege must be either commonly granted or locally granted in the PDB. The user must exercise the privilege using `AS SYSDBA`, `AS SYSOPER`, `AS SYSBACKUP`, or `AS SYSDG`, respectively, at connect time.
- When `RESTRICTED SESSION` is enabled, `RESTRICT` must be specified when a PDB is opened.

In addition, to place PDBs in a target mode with the `STARTUP PLUGGABLE DATABASE` command, you must meet the requirements described in the following table.

Table 16-5 Modifying the Open Mode of a PDB with STARTUP PLUGGABLE DATABASE

| Target Mode of the PDB | FORCE Option Included | Required Mode for the Root | Required Mode of the PDB Being Modified |
| --- | --- | --- | --- |
| Read/write | Yes | Read/write | Mounted, read-only, or read/write |
| Read/write | No | Read/write | Mounted |
| Read-only | No | Read-only or read/write | Mounted |

Note:

You can also use the `STARTUP` command to modify the open mode of a PDB when the current container is the PDB.

See Also:

- " Starting Up a PDB Using the STARTUP Command "
- " Modifying the Open Mode of PDBs with the SQL\*Plus STARTUP Command "

**Parent topic:** Altering the Open Mode of a PDB Using STARTUP and SHUTDOWN

##### Starting Up a PDB Using the STARTUP Command

When the current container is a PDB, the SQL\*Plus `STARTUP` command opens the PDB.

Use the following options of the `STARTUP` command to open a PDB:

- `FORCE`
	Closes an open PDB before re-opening it in read/write mode. When this option is specified, no other options are allowed.
- `RESTRICT`
	Enables only users with the `RESTRICTED` `SESSION` system privilege in the PDB to access the PDB.
	If neither `OPEN READ WRITE` nor `OPEN READ ONLY` is specified and `RESTRICT` is specified, then the PDB is opened in read-only mode when the CDB to which it belongs is a physical standby database. Otherwise, the PDB is opened in read/write mode.
- `OPEN open_pdb_options`
	Opens the PDB in either read/write mode or read-only mode. Specify `OPEN READ WRITE` or `OPEN READ ONLY`. When `RESTRICT` is not specified, `READ WRITE` is always the default.

To issue the `STARTUP` command when the current container is a PDB, the following prerequisites must be met:

- The current user must have `SYSDBA`, `SYSOPER`, `SYSBACKUP`, or `SYSDG` administrative privilege, and the privilege must be either commonly granted or locally granted in the PDB. The user must exercise the privilege using `AS SYSDBA`, `AS SYSOPER`, `AS SYSBACKUP`, or `AS SYSDG`, respectively, at connect time.
- Excluding the use of the `FORCE` option, the PDB must be in mounted mode to open it.
- To place a PDB in mounted mode, the PDB must be in open read-only or open read/write mode.

To modify a PDB with the STARTUP command:

1. In SQL\*Plus, ensure that the current container is a PDB.
2. Run the `STARTUP` command.

Example 16-33 Opening a PDB in Read/Write Mode with the STARTUP Command

```
STARTUP OPEN
```

Example 16-34 Opening a PDB in Read-Only Mode with the STARTUP Command

```
STARTUP OPEN READ ONLY
```

Example 16-35 Opening a PDB in Read-Only Restricted Mode with the STARTUP Command

```
STARTUP RESTRICT OPEN READ ONLY
```

Example 16-36 Opening a PDB in Read/Write Mode with the STARTUP Command and the FORCE Option

This example assumes that the PDB is currently open. The `FORCE` option closes the PDB and then opens it in the read/write mode.

```
STARTUP FORCE
```

**Parent topic:** Altering the Open Mode of a PDB Using STARTUP and SHUTDOWN

##### Modifying the Open Mode of PDBs with the SQL\*Plus STARTUP Command

You can use the `STARTUP PLUGGABLE DATABASE` command to open a single PDB.

To modify a PDB with the STARTUP PLUGGABLE DATABASE command:

1. In SQL\*Plus, ensure that the current container is the root.
	See " [About Container Access in a CDB](administering-a-cdb-with-sql-plus.md) ".
2. Run the `STARTUP PLUGGABLE DATABASE` command.

Note:

When the current container is the root, the SQL\*Plus `SHUTDOWN` command always shuts down the CDB instance. It cannot be used to close individual PDBs.

Example 16-37 Opening a PDB in Read/Write Mode with the STARTUP Command

```
STARTUP PLUGGABLE DATABASE hrpdb OPEN
```

Example 16-38 Opening a PDB in Read/Write Restricted Mode with the STARTUP Command

```
STARTUP PLUGGABLE DATABASE hrpdb RESTRICT
```

Example 16-39 Opening a PDB in Read-Only Restricted Mode with the STARTUP Command

```
STARTUP PLUGGABLE DATABASE hrpdb OPEN READ ONLY RESTRICT
```

Example 16-40 Opening a PDB in Read-Only Mode with the STARTUP Command

```
STARTUP PLUGGABLE DATABASE hrpdb OPEN READ ONLY
```

Example 16-41 Opening a PDB in Read/Write Mode with the STARTUP Command and the FORCE Option

This example assumes that the `hrpdb` PDB is currently open. The `FORCE` option closes the PDB and then opens it in the read/write mode.

```
STARTUP PLUGGABLE DATABASE hrpdb FORCE
```

See Also:

- " About Modifying the Open Mode of PDBs with the SQL\*Plus STARTUP Command "
- " Altering the Open Mode of a PDB Using STARTUP and SHUTDOWN " for information about using the `STARTUP` or `SHUTDOWN` command when the current container is a PDB
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-203404B5-5157-4F29-A241-B8ABC4753819)
- [SQL\*Plus User's Guide and Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQPUG128)

**Parent topic:** Altering the Open Mode of a PDB Using STARTUP and SHUTDOWN

##### Shutting Down a PDB Using the SHUTDOWN Command

When the current container is a PDB, the SQL\*Plus `SHUTDOWN` command closes the PDB.

After the `SHUTDOWN` command is issued on a PDB successfully, it is in mounted mode.

The following `SHUTDOWN` modes are possible:

- When you specify `SHUTDOWN` only, then the PDB is shut down with the normal mode.
- When you specify `SHUTDOWN IMMEDIATE`, the PDB is shut down with the immediate mode.
- When you specify `SHUTDOWN ABORT`, the PDB is forcefully closed.
	For a single-instance CDB, PDB media recovery is required when you specify `SHUTDOWN ABORT`. For an Oracle Real Application Clusters (Oracle RAC) CDB, PDB media recovery is required if the `SHUTDOWN ABORT` command closes the last open instance.

Note that if the PDB keystore was in an open state, then issuing `SHUTDOWN` at the PDB level does not close it. To close the keystore, run the `ADMINISTER KEY MANAGEMENT SET KEYSTORE CLOSE IDENTIFIED BY "pdb_ks_pwd"` command.

Prerequisites

To issue the `SHUTDOWN` command when the current container is a PDB, the following prerequisites must be met:

- The current user must have `SYSDBA`, `SYSOPER`, `SYSBACKUP`, or `SYSDG` administrative privilege, and the privilege must be either commonly granted or locally granted in the PDB. The user must exercise the privilege using `AS SYSDBA`, `AS SYSOPER`, `AS SYSBACKUP`, or `AS SYSDG`, respectively, at connect time.
- To close a PDB, the PDB must be open.

To modify a PDB with the `SHUTDOWN` command:

1. In SQL\*Plus, ensure that the current container is a PDB.
2. Run the `SHUTDOWN` command.

Note:

- When the current container is a PDB, the `SHUTDOWN` command only closes the PDB, not the CDB instance.
- There is no `SHUTDOWN` command for a PDB that is equivalent to `SHUTDOWN` `TRANSACTIONAL` for a CDB.

Example 16-42 Closing a PDB with the SHUTDOWN IMMEDIATE Command

```
SHUTDOWN IMMEDIATE
```

See Also:

- " [About the Current Container](administering-a-cdb-with-sql-plus.md) "
- " Connecting to a PDB "
- " Modifying the Open Mode of PDBs with ALTER PLUGGABLE DATABASE "
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-3661B282-5C34-4E32-BC6A-906A72712866) for more information about shutdown modes
- [SQL\*Plus User's Guide and Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQPUG125)

**Parent topic:** Altering the Open Mode of a PDB Using STARTUP and SHUTDOWN

#### Starting and Stopping PDBs in Oracle RAC

You can use SRVCTL commands to manage PDBs.

Note:

Starting with Oracle Database 21c, installation of non-CDB Oracle Database architecture is no longer supported. Starting with Oracle Grid Infrastructure 21c, policy-managed databases are deprecated.

Starting in Oracle Database 21c, PDBs are a resource managed by Oracle Clusterware. Consider a CDB called `raccont` that has a policy-managed PDB called `spark`.

Note:

If you attempt to create the service without first creating the PDB, then you will get an error message indicating you must create the PDB resource first.

If the `spark` PDB was created with cardinality set to 1, or 2, or ALL, then if you create a service named `plug` for the PDB, the service can use the `–cardinality` argument, too. If the `spark` PDB was created using the `-preferred` or `-available` arguments, then new services you create for the PDB use the `-preferred` or `-available` arguments, not the `–cardinality` argument.

Because PDBs are managed as an Oracle Clusterware resource, typical Oracle RAC-based management practices apply. For this reason, if the PDB `spark` is in the online state when Oracle Clusterware is shut down on a server hosting this service, then the PDB is restored to its original state after the restart of Oracle Clusterware on this server. Thus, starting PDBs is automated as with any other Oracle RAC database.

To start a pluggable database:
```
$ srvctl start pdb -db db_name -pdb pdb_name [-startoption start_options]
```

To start a pluggable database on specific nodes:
```
$ srvctl start pdb -db db_name -pdb pdb_name -node node_list 
   [-startoption start_options]
```

To stop a PDB and all its services on all nodes within a database using the IMMEDIATE option:

```
$ srvctl stop pdb -db db_name -pdb pdb_name -stopoption IMMEDIATE -drain_timeout 0
  -stopsvcoption IMMEDIATE
```

To stop a pluggable database on specific nodes:
```
$ srvctl stop pdb -db db_name -pdb pdb_name -node node_list
   [-stopoption stop_options] [-stopsvcoption stop_service_options 
   [-drain_timeout timeout]
```

If you do not want the `spark` PDB to restart when the Oracle RAC database is restarted on all, or on a specific node, use the following command:

```
srvctl disable pdb -db raccont -pdb spark [-node node_name]
```

To view the status of the PDB service `plug`, use the following command:

```
srvctl status service -db raccont -service plug -verbose
```

To view the status of the PDB `spark`, use the following command:

```
srvctl status pdb -db raccont -pdb plug -detail
```

To modify the configuration of the PDB, use the following command:

```
srvctl modify pdb -db db_unique_name -pdb pdb_name 
     [-cardinality {num_of_instances | ALL}]
     [-maxcpu max_cpu_usage] [-mincpuunit min_cpu_usage] 
     [-rank rank] [-startoption start_options] 
     [-stopoption stop_options] [-policy policy]
```