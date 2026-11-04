---
title: "Database Administrator’s Guide"
book: "Database Administrator's Guide"
doc_id: E85760-09
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/admin/creating-and-configuring-a-cdb.html
tags:
  - oracle
  - 12c
  - administrators-guide
---

Creating and configuring a multitenant container database (CDB) includes tasks such as planning for CDB creation, creating the CDB, and optionally configuring EM Express for the CDB.

- About Creating a CDB  
	The procedure for creating a multitenant container database (CDB) is very similar to the procedure for creating a non-CDB.
- Planning for CDB Creation  
	CDB creation prepares several operating system files to work together as a CDB.
- Using DBCA to Create a CDB  
	Oracle strongly recommends using the Database Configuration Assistant (DBCA) to create a CDB, because it is a more automated approach, and your CDB is ready to use when DBCA completes. DBCA enables you to specify the number of PDBs in the CDB when it is created.
- Using the CREATE DATABASE Statement to Create a CDB  
	You can create a CDB using the `CREATE` `DATABASE` SQL statement.
- Configuring EM Express for a CDB  
	For a CDB, you can configure Oracle Enterprise Manager Database Express (EM Express) for the root and for each PDB by setting a global HTTPS port, or you can set a different port for every container in the CDB.
- After Creating a CDB  
	After you create a CDB, it consists of the root and the CDB seed.

**Parent topic:** [Managing a Multitenant Environment](managing-a-multitenant-environment.md)

### 37.1 About Creating a CDB

The procedure for creating a multitenant container database (CDB) is very similar to the procedure for creating a non-CDB.

The procedure for creating a non-CDB is described in [Creating and Configuring an Oracle Database](creating-and-configuring-an-oracle-database.md). Before creating a CDB, you must understand the concepts and tasks described in [Creating and Configuring an Oracle Database](creating-and-configuring-an-oracle-database.md).

This chapter describes special considerations for creating a CDB. This chapter also describes differences between the procedure for creating a non-CDB in [Creating and Configuring an Oracle Database](creating-and-configuring-an-oracle-database.md) and the procedure for creating a CDB.

After you plan your CDB using some of the guidelines presented in " Planning for CDB Creation ", you can create the CDB either during or after Oracle Database software installation. The following are typical reasons to create a CDB after installation:

- You used Oracle Universal Installer (OUI) to install software only, and did not create a CDB.
- You want to create another CDB on the same host as an existing CDB or an existing non-CDB. In this case, this chapter assumes that the new CDB uses the same Oracle home as the existing database. You can also create the CDB in a new Oracle home by running OUI again.

The specific methods for creating a CDB are:

- With the Database Configuration Assistant (DBCA), a graphical tool.
	See " Using DBCA to Create a CDB ".
- With the `CREATE` `DATABASE` SQL statement.
	See " Using the CREATE DATABASE Statement to Create a CDB ".

**Parent topic:** Creating and Configuring a CDB

### 37.2 Planning for CDB Creation

CDB creation prepares several operating system files to work together as a CDB.

Note:

Before planning for CDBs, review the conceptual information about CDBs and PDBs in [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=CNCPT89234).

- Decide How to Configure the CDB  
	Prepare to create the CDB by research and careful planning.
- Prerequisites for CDB Creation  
	You must complete prerequisites before creating a new CDB.

**Parent topic:** Creating and Configuring a CDB

#### 37.2.1 Decide How to Configure the CDB

Prepare to create the CDB by research and careful planning.

Table 37-1 lists some recommended actions and considerations that apply to CDBs. For more information about many of the actions in Table 37-1, see [Table 2-1](creating-and-configuring-an-oracle-database.md).

Table 37-1 Planning for a CDB

| Action | Considerations for a CDB | Additional Information |
| --- | --- | --- |
| Plan the tables and indexes for the pluggable databases (PDBs) and estimate the amount of space they will require. | In a CDB, most user data is in the PDBs. The root contains no user data or minimal user data. Plan for the PDBs that will be part of the CDB. The disk storage space requirement for a CDB is the space required for the Oracle Database installation plus the sum of the space requirements for all of the PDBs that will be part of the CDB. A CDB can contain up to 4,096 PDBs, but you can limit the CDB to a smaller number of PDBs by setting the `MAX_PDBS` initialization parameter.  You can also create application containers in a CDB. An application container is a collection of application PDBs that store the data for one or more applications. In addition, application containers support user-created application common objects that can be shared by the application PDBs in the application container. | " [Oracle Database Structure and Storage](oracle-database-structure-and-storage.md) "  [Schema Objects](schema-objects.md)  " [Creating and Removing PDBs with SQL\*Plus](creating-and-removing-pdbs-with-sql-plus.md) "  " [Application Containers](overview-of-managing-a-multitenant-environment.md) " |
| Plan the layout of the underlying operating system files your CDB will comprise. | There are separate data files for the root, the CDB seed, each PDB, each application root, and each application PDB.  There is one redo log for a single-instance CDB, or one redo log for each instance of an Oracle Real Application Clusters (Oracle RAC) CDB. Also, for Oracle RAC, all data files and redo log files must be on shared storage. | " [Using Oracle Managed Files](using-oracle-managed-files.md) "  [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=OSTMG)  [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=TGDBA015)  [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=BRADV)  [Oracle Grid Infrastructure Installation Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=CWGEN) for information about configuring storage for Oracle RAC  Your Oracle operating system–specific documentation, including the appropriate Oracle Database installation guide. |
| Plan for the number of background processes that will be required by the CDB. | There is one set of background processes shared by the root and all PDBs. | " [Specifying the Maximum Number of Processes](creating-and-configuring-an-oracle-database.md) " |
| Select the global database name, which is the name and location of the CDB within the network structure, and create the global database name for the root by setting both the `DB_NAME` and `DB_DOMAIN` initialization parameters. | The global database name of the root is the global database name of the CDB.  The global database name of a PDB is defined by the PDB name and the `DB_DOMAIN` initialization parameter. | " [Determining the Global Database Name](creating-and-configuring-an-oracle-database.md) " |
| Familiarize yourself with the initialization parameters that can be included in an initialization parameter file. Become familiar with the concept and operation of a server parameter file (SPFILE). An SPFILE file lets you store and manage your initialization parameters persistently in a server-side disk file. | A CDB uses a single SPFILE or a single text initialization parameter file (PFILE). Values of initialization parameters set for the root can be inherited by PDBs. You can set some initialization parameters for a PDB by using the `ALTER` `SYSTEM` statement.  The root must be the current container when you operate on an SPFILE. The user who creates or modifies the SPFILE must be a common user with `SYSDBA`, `SYSOPER`, or `SYSBACKUP` administrative privilege, and the user must exercise the privilege by connecting `AS` `SYSDBA`, `AS` `SYSOPER`, or `AS` `SYSBACKUP` respectively.  To create a CDB, the `ENABLE_PLUGGABLE_DATABASE` initialization parameter must be set to `TRUE`. | " [Specifying Initialization Parameters](creating-and-configuring-an-oracle-database.md) "  " [Using the ALTER SYSTEM SET Statement in a CDB](administering-a-cdb-with-sql-plus.md) "  " [Listing the Initialization Parameters That Are Modifiable in PDBs](viewing-information-about-cdbs-and-pdbs-with-sql-plus.md) "  " [About the Current Container](administering-a-cdb-with-sql-plus.md) "  [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=REFRN001) |
| Select the character set. | When the character set of the root is AL32UTF8, PDBs that are plugged into the CDB or cloned can have a different character set than the root. PDBs that are created from the CDB seed inherit the AL32UTF8 from it, but you can migrate the PDB to a different character set.  When the character set of the root is not AL32UTF8, all of the PDBs in the CDB use the character set of the root.  Oracle recommends AL32UTF8 for the CDB database character set and AL16UTF6 for the CDB national character set because they provide the most flexibility.  When selecting the database character set for the CDB, you must consider the current character sets of the databases that you want to consolidate (plug) into this CDB.  When moving a non-CDB to a CDB, it is best to migrate the non-CDB to AL32UTF8 first. You can use Oracle Database Migration Assistant for Unicode (DMU) to migrate a non-CDB to AL32UTF8. After a CDB is created, you cannot migrate the CDB's character set using DMU. | [Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=NLSPG1035) |
| Consider which time zones your CDB must support. | You can set the time zones for the entire CDB (including all PDBs). You can also set the time zones individually for each PDB. | " [Specifying the Database Time Zone and Time Zone File](creating-and-configuring-an-oracle-database.md) " |
| Select the standard database block size. This is specified at CDB creation by the `DB_BLOCK_SIZE` initialization parameter and cannot be changed after the CDB is created. | The standard block size applies to the entire CDB. | " [Specifying Database Block Sizes](creating-and-configuring-an-oracle-database.md) " |
| If you plan to store online redo log files on disks with a 4K byte sector size, then determine whether you must manually specify redo log block size. Also, develop a backup and recovery strategy to protect the CDB from failure. | There is a single redo log and a single control file for an entire CDB. | " [Planning the Block Size of Redo Log Files](managing-the-redo-log.md) "  " [Managing the Redo Log](managing-the-redo-log.md) "  " [Managing Archived Redo Log Files](managing-archived-redo-log-files.md) "  " [Managing Control Files](managing-control-files.md) "  [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=BRADV) |
| Determine the appropriate initial sizing for the `SYSAUX` tablespace. | There is a separate `SYSAUX` tablespace for the root and for each PDB. | " [About the SYSAUX Tablespace](creating-and-configuring-an-oracle-database.md) " |
| Plan to use a default tablespace for non- `SYSTEM` users to prevent inadvertently saving database objects in the `SYSTEM` tablespace. | You can specify a separate default tablespace for the root and for each PDB. Also, there is a separate `SYSTEM` tablespace for the root and for each PDB. | " [Creating a Default Permanent Tablespace](creating-and-configuring-an-oracle-database.md) "  " [About the Statements That Modify a CDB](administering-a-cdb-with-sql-plus.md) " |
| Plan to use default temporary tablespaces. | There is a default temporary tablespace for each container in the CDB, including the root and each PDB, application root, and application PDB.  The shared temporary tablespace is used is for recursive SQL only and is not used by hosted PDB tenants directly. | " [Creating a Default Temporary Tablespace](creating-and-configuring-an-oracle-database.md) "  " [About the Statements That Modify a CDB](administering-a-cdb-with-sql-plus.md) " |
| Plan to use an undo tablespace to manage your undo data. | A CDB can run in different undo modes. You can configure a CDB to have one active undo tablespace for the entire CDB or a separate undo tablespace for each container in the CDB. You can specify the undo mode during CDB creation, and you can change the undo mode after the CDB is created.  When you choose to have one active undo tablespace for the entire CDB, shared undo is used, and local undo is disabled. In this configuration, there is one active undo tablespace for a single-instance CDB. When local undo is enabled, there is one undo tablespace for each container in a single instance configuration. For an Oracle RAC CDB, each PDB has one undo tablespace in each node in which it is open. With shared undo, only a common user who has the appropriate privileges and whose current container is the root can create an undo tablespace.  The best practice is to use local undo for a CDB. Shared undo is supported primarily for upgrade and transitional purposes only. Although there is minor overhead associated with local undo when compared with shared undo, the benefits of local undo make it preferable in most environments. Local undo makes unplug operations and point in time recovery faster, and it is required for some features, such as relocating a PDB. By default, DBCA creates new CDBs with local undo enabled.  In a CDB, the `UNDO_MANAGEMENT` initialization parameter must be set to `AUTO`, and an undo tablespace is required to manage the undo data.  When local undo is not enabled, undo tablespaces are visible in static data dictionary views and dynamic performance (V$) views when the current container is the root. Undo tablespaces are visible only in dynamic performance views when the current container is a PDB.  Also, when local undo is disabled, Oracle Database silently ignores undo tablespace and rollback segment operations when the current container is a PDB. | " [Managing the CDB Undo Mode](administering-a-cdb-with-sql-plus.md) "  " [Managing Undo](managing-undo.md) "  " [About the Current Container](administering-a-cdb-with-sql-plus.md) " |
| Plan for the database services required to meet the needs of your applications. | The root and each PDB might require several services. You can create services for the root or for individual PDBs.  Database services have an optional `PDB` property. You can create services and associate them with a particular PDB by specifying the `PDB` property. Services with a null `PDB` property are associated with the CDB root.  You can also use the `DBMS_SERVICE` supplied PL/SQL package to create services and associate them with PDBs. When you run `CREATE_SERVICE` procedure, the service is associated with the current container.  You can manage services with the SRVCTL utility, Oracle Enterprise Manager Cloud Control, and the `DBMS_SERVICE` supplied PL/SQL package.  When you create a PDB, a new default service for the PDB is created automatically. The service has the same name as the PDB. You cannot manage this service with the SRVCTL utility. However, you can create user-defined services and customize them for your applications. | " [Managing Application Workloads with Database Services](creating-and-configuring-an-oracle-database.md) "  " [Managing Services Associated with PDBs](administering-pdbs-with-sql-plus.md) "  " [SRVCTL Command Reference for Oracle Restart](configuring-automatic-restart-of-an-oracle-database.md) " for information about using the SRVCTL utility with a single-instance database  [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=RACAD005) for information about using the SRVCTL utility with an Oracle RAC database |
| Familiarize yourself with the principles and options of starting up and shutting down an instance and mounting and opening a CDB. | In a CDB, the CDB root and all of the containers share a single instance, or, when using Oracle RAC, multiple concurrent instances. You can start up and shut down an entire CDB, which in turn determines the state of hosted PDBs. When the CDB is open, you can control the open mode of PDBs by using either an `ALTER PLUGGABLE DATABASE` statement in the context of the CDB or PDB to open or close hosted PDBs. To maintain backward compatibility, `ALTER DATABASE OPEN` and `ALTER DATABASE CLOSE` statements are supported when they are executed and a PDB is the current container. You can also use the SQL\*Plus `STARTUP` command and the SQL\*Plus `SHUTDOWN` command when a PDB is the current container. However, the SQL\*Plus `STARTUP MOUNT` command is a CDB-only operation and cannot be used when a PDB is the current container. | " [Starting Up a Database](starting-up-and-shutting-down.md) "  " [Modifying the Open Mode of PDBs](administering-a-cdb-with-sql-plus.md) "  " [Modifying a PDB with the ALTER PLUGGABLE DATABASE Statement](administering-pdbs-with-sql-plus.md) " |
| If you plan to use Oracle RAC, then plan for an Oracle RAC environment. | The Oracle RAC documentation describes special considerations for a CDB in an Oracle RAC environment. | See your platform-specific Oracle RAC installation guide for information about creating a CDB in an Oracle RAC environment.  [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=RACAD8913) |
| Avoid unsupported features. | The [Oracle Database Readme](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=READM) includes a list of Oracle Database features that are currently not supported in a CDB.  If you must use one or more of these features, then create a non-CDB. | [Creating and Configuring an Oracle Database](creating-and-configuring-an-oracle-database.md) |

**Parent topic:** Planning for CDB Creation

#### 37.2.2 Prerequisites for CDB Creation

You must complete prerequisites before creating a new CDB.

Before you can create a new CDB, the following prerequisites must be met:

- Ensure that the prerequisites described in " [Prerequisites for a Multitenant Environment](overview-of-managing-a-multitenant-environment.md) " are met.
- Sufficient memory must be available to start the Oracle Database instance.
	The memory required by a CDB should be sized to accommodate the workload of each of its containers and the number of containers.
- Sufficient disk storage space must be available for the planned PDBs on the computer that runs Oracle Database. In an Oracle RAC environment, sufficient shared storage must be available.
	The disk storage space required by a CDB is the sum of the space requirements for all of the PDBs that will be part of the CDB.

All of these prerequisites are discussed in the [Oracle Database Installation Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=GINST) or [Oracle Grid Infrastructure Installation Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=CWGEN) specific to your operating system. If you use the Oracle Universal Installer, then it will guide you through your installation and provide help in setting environment variables and establishing directory structure and authorizations.

**Parent topic:** Planning for CDB Creation

### 37.3 Using DBCA to Create a CDB

Oracle strongly recommends using the Database Configuration Assistant (DBCA) to create a CDB, because it is a more automated approach, and your CDB is ready to use when DBCA completes. DBCA enables you to specify the number of PDBs in the CDB when it is created.

DBCA can be launched by the Oracle Universal Installer (OUI), depending upon the type of install that you select. You can also launch DBCA as a standalone tool at any time after Oracle Database installation.

You can use DBCA to create a CDB in interactive mode or noninteractive/silent mode. Interactive mode provides a graphical interface and guided workflow for creating and configuring a CDB. Noninteractive/silent mode enables you to script a pre-configured CDB template deployment with pre-configured, customized PDB seed databases for cloning purposes. You can run DBCA in noninteractive/silent mode by specifying command-line arguments, a response file, or both.

After a CDB is created, you can use DBCA to plug PDBs into it and unplug PDBs from it.

See Also:

- " [Creating a Database with DBCA](creating-and-configuring-an-oracle-database.md) "
- [Oracle Database 2 Day DBA](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=ADMQS002)
- The DBCA online help

**Parent topic:** Creating and Configuring a CDB

### 37.4 Using the CREATE DATABASE Statement to Create a CDB

You can create a CDB using the `CREATE` `DATABASE` SQL statement.

Note:

Oracle strongly recommends using the Database Configuration Assistant (DBCA) template deployment instead of the `CREATE` `DATABASE` SQL statement to create a CDB, because using DBCA is a more automated approach, and your CDB is ready to use when DBCA completes.

- About Creating a CDB with the CREATE DATABASE Statement  
	Creating a CDB using the `CREATE` `DATABASE` SQL statement is very similar to creating a non-CDB. This section describes additional requirements for creating a CDB. When you create a CDB using the `CREATE` `DATABASE` SQL statement, you must enable PDBs and specify the names and locations of the root's files and the CDB seed's files.
- Step 1: Specify an Instance Identifier (SID)  
	The `ORACLE_SID` environment variable is used to distinguish this instance from other Oracle Database instances that you may create later and run concurrently on the same host computer.
- Step 2: Ensure That the Required Environment Variables Are Set  
	Depending on your platform, before you can start SQL\*Plus (as required in a later step), you may have to set environment variables, or at least verify that they are set properly.
- Step 3: Choose a Database Administrator Authentication Method  
	You must be authenticated and granted appropriate system privileges in order to create a database.
- Step 4: Create the Initialization Parameter File  
	When an Oracle instance starts, it reads an initialization parameter file. This file can be a text file, which can be created and modified with a text editor, or a binary file, which is created and dynamically modified by the database. The binary file, which is preferred, is called a server parameter file. In this step, you create a text initialization parameter file. In a later step, you create a server parameter file from the text file.
- Step 5: (Windows Only) Create an Instance  
	On the Windows platform, before you can connect to an instance, you must manually create it if it does not already exist. The `ORADIM` command creates an Oracle Database instance by creating a new Windows service.
- Step 6: Connect to the Instance  
	Start SQL\*Plus and connect to your Oracle Database instance with the `SYSDBA` administrative privilege.
- Step 7: Create a Server Parameter File  
	The server parameter file enables you to change initialization parameters with the `ALTER` `SYSTEM` command and persist the changes across a database shutdown and startup. You create the server parameter file from your edited text initialization file.
- Step 8: Start the Instance  
	Start an instance without mounting a database.
- Step 9: Create a CDB with the CREATE DATABASE Statement  
	When you use the `CREATE DATABASE` statement to create a CDB, you must complete additional actions before you have an operational CDB.

**Parent topic:** Creating and Configuring a CDB

#### 37.4.1 About Creating a CDB with the CREATE DATABASE Statement

Creating a CDB using the `CREATE` `DATABASE` SQL statement is very similar to creating a non-CDB. This section describes additional requirements for creating a CDB. When you create a CDB using the `CREATE` `DATABASE` SQL statement, you must enable PDBs and specify the names and locations of the root's files and the CDB seed's files.

Note:

Using the `CREATE` `DATABASE` SQL statement is a more manual approach to creating a CDB than using DBCA.

- About Enabling PDBs  
	To create a CDB, the `CREATE` `DATABASE` statement must include the `ENABLE` `PLUGGABLE` `DATABASE` clause. When this clause is included, the statement creates a CDB with the root and the CDB seed.
- About the Names and Locations of the Root's Files and the CDB Seed's Files
- About the Attributes of the CDB Seed's Data Files  
	The CDB seed can be used as a template to create new containers.
- About the CDB’s Undo Mode  
	Add the undo\_mode\_clause to an `ENABLE PLUGGABLE DATABASE` clause to specify the undo mode of the CDB.

See Also:

[Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=CNCPT89268) for information about a CDB's files

**Parent topic:** Using the CREATE DATABASE Statement to Create a CDB

##### 37.4.1.1 About Enabling PDBs

To create a CDB, the `CREATE` `DATABASE` statement must include the `ENABLE` `PLUGGABLE` `DATABASE` clause. When this clause is included, the statement creates a CDB with the root and the CDB seed.

When the `ENABLE` `PLUGGABLE` `DATABASE` clause is not included in the `CREATE` `DATABASE` statement, the newly created database is a non-CDB. The statement does not create the root and the CDB seed, and the non-CDB can never contain PDBs.

**Parent topic:** About Creating a CDB with the CREATE DATABASE Statement

##### 37.4.1.2 About the Names and Locations of the Root's Files and the CDB Seed's Files

The `CREATE` `DATABASE` statement uses the root's files (such as data files) to generate the names of the CDB seed's files. You must specify the names and locations of the root's files and the CDB seed's files. After the `CREATE` `DATABASE` statement completes successfully, you can use the CDB seed and its files to create new PDBs. The CDB seed cannot be modified after it is created.

You must specify the names and locations of the CDB seed's files in one of the following ways:

1. The `SEED FILE_NAME_CONVERT` clause
2. Oracle Managed Files
3. The `PDB_FILE_NAME_CONVERT` initialization parameter

If you use more than one of these methods, then the `CREATE` `DATABASE` statement uses one method in the order of precedence of the previous list. For example, if you use all of the methods, then the `CREATE` `DATABASE` statement only uses the specifications in the `SEED` `FILE_NAME_CONVERT` clause.

- The SEED FILE\_NAME\_CONVERT Clause  
	The `SEED` `FILE_NAME_CONVERT` clause of the `CREATE` `DATABASE` statement specifies how to generate the names of the CDB seed's files using the names of root's files.
- Oracle Managed Files  
	When Oracle Managed Files is enabled, it can determine the names and locations of the CDB seed's files.
- The PDB\_FILE\_NAME\_CONVERT Initialization Parameter  
	The `PDB_FILE_NAME_CONVERT` initialization parameter can specify the names and locations of the seed's files.

See Also:

" [Creating a PDB Using the Seed](creating-and-removing-pdbs-with-sql-plus.md) "

**Parent topic:** About Creating a CDB with the CREATE DATABASE Statement

###### 37.4.1.2.1 The SEED FILE\_NAME\_CONVERT Clause

The `SEED` `FILE_NAME_CONVERT` clause of the `CREATE` `DATABASE` statement specifies how to generate the names of the CDB seed's files using the names of root's files.

You can use this clause to specify one of the following options:

- One or more file name patterns and replacement file name patterns, in the following form:
	```
	'string1' , 'string2' , 'string3' , 'string4' , ...
	```
	The string2 file name pattern replaces the string1 file name pattern, and the string4 file name pattern replaces the string3 file name pattern. You can use as many pairs of file name pattern and replacement file name pattern strings as required.
	If you specify an odd number of strings (the last string has no corresponding replacement string), then an error is returned. Do not specify more than one pattern/replace string that matches a single file name or directory.
	File name patterns cannot match files or directories managed by Oracle Managed Files.
- `NONE` when no file names should be converted. Omitting the `SEED` `FILE_NAME_CONVERT` clause is the same as specifying `NONE`.

Example 37-1 SEED FILE\_NAME\_CONVERT Clause

This `SEED` `FILE_NAME_CONVERT` clause generates file names for the CDB seed's files in the /oracle/pdbseed/ directory using file names in the /oracle/dbs directory.

```
SEED
FILE_NAME_CONVERT = ('/oracle/dbs/', '/oracle/pdbseed/')
```

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQLRF-GUID-77D4BBA7-2A64-46D9-A2B8-C56060772215) for the syntax of the `SEED` `FILE_NAME_CONVERT` clause

**Parent topic:** About the Names and Locations of the Root's Files and the CDB Seed's Files

###### 37.4.1.2.2 Oracle Managed Files

When Oracle Managed Files is enabled, it can determine the names and locations of the CDB seed's files.

See Also:

[Using Oracle Managed Files](using-oracle-managed-files.md)

**Parent topic:** About the Names and Locations of the Root's Files and the CDB Seed's Files

###### 37.4.1.2.3 The PDB\_FILE\_NAME\_CONVERT Initialization Parameter

The `PDB_FILE_NAME_CONVERT` initialization parameter can specify the names and locations of the seed's files.

To use this technique, ensure that the `PDB_FILE_NAME_CONVERT` initialization parameter is included in the initialization parameter file when you create the CDB.

File name patterns specified in this initialization parameter cannot match files or directories managed by Oracle Managed Files.

See Also:

[Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=REFRN10322)

**Parent topic:** About the Names and Locations of the Root's Files and the CDB Seed's Files

##### 37.4.1.3 About the Attributes of the CDB Seed's Data Files

The CDB seed can be used as a template to create new containers.

The attributes of the data files for the root's `SYSTEM` and `SYSAUX` tablespaces might not be suitable for the CDB seed. In this case, you can specify different attributes for the CDB seed's data files by using the `tablespace_datafile` clauses. Use these clauses to specify attributes for all data files comprising the `SYSTEM` and `SYSAUX` tablespaces in the CDB seed. The values inherited from the root are used for any attributes whose values have not been provided.

The syntax of the `tablespace_datafile` clauses is the same as the syntax for a data file specification, excluding the name and location of the data file and the `REUSE` attribute. You can use the `tablespace_datafile` clauses with any of the methods for specifying the names and locations of the CDB seed's data files described in " About the Names and Locations of the Root's Files and the CDB Seed's Files ".

The `tablespace_datafile` clauses do not specify the names and locations of the CDB seed's data files. Instead, they specify the attributes of `SYSTEM` and `SYSAUX` data files in the CDB seed that differ from those in the root. If `SIZE` is not specified in the `tablespace_datafile` clause for a tablespace, then data file size for the tablespace is set to a predetermined fraction of the size of a corresponding root data file.

Example 37-2 Using the tablespace\_datafile Clauses

Assume the following `CREATE` `DATABASE` clauses specify the names, locations, and attributes of the data files that comprise the `SYSTEM` and `SYSAUX` tablespaces in the root.

```
DATAFILE '/u01/app/oracle/oradata/newcdb/system01.dbf' SIZE 325M REUSE
SYSAUX DATAFILE '/u01/app/oracle/oradata/newcdb/sysaux01.dbf' SIZE 325M REUSE
```

You can use the following `tablespace_datafile` clauses to specify different attributes for these data files:

```
SEED
SYSTEM DATAFILES SIZE 125M AUTOEXTEND ON NEXT 10M MAXSIZE UNLIMITED
SYSAUX DATAFILES SIZE 100M
```

In this example, the data files for the CDB seed's `SYSTEM` and `SYSAUX` tablespaces inherit the `REUSE` attribute from the root's data files. However, the following attributes of the CDB seed's data files differ from the root's:

- The data file for the `SYSTEM` tablespace is 125 MB for the CDB seed and 325 MB for the root.
- `AUTOEXTEND` is enabled for the CDB seed's `SYSTEM` data file, and it is disabled by default for the root's `SYSTEM` data file.
- The data file for the `SYSAUX` tablespace is 100 MB for the CDB seed and 325 MB for the root.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQLRF52248) for information about data file specifications

**Parent topic:** About Creating a CDB with the CREATE DATABASE Statement

##### 37.4.1.4 About the CDB’s Undo Mode

Add the undo\_mode\_clause to an `ENABLE PLUGGABLE DATABASE` clause to specify the undo mode of the CDB.

The undo\_mode\_clause specifies whether the CDB undo mode is local or shared. Local undo mode means that every container in the CDB uses local undo. To configure local undo mode for the CDB, specify `LOCAL UNDO ON`. Shared undo mode means that there is one active undo tablespace for a single-instance CDB, or for an Oracle RAC CDB, there is one active undo tablespace for each instance. To configure shared undo mode for the CDB, specify `LOCAL UNDO OFF`. If the undo\_mode\_clause is not added to the `ENABLE PLUGGABLE DATABASE` clause, then shared undo mode is the default.

**Parent topic:** About Creating a CDB with the CREATE DATABASE Statement

#### 37.4.2 Step 1: Specify an Instance Identifier (SID)

The `ORACLE_SID` environment variable is used to distinguish this instance from other Oracle Database instances that you may create later and run concurrently on the same host computer.

1. Decide on a unique Oracle system identifier (SID) for your instance.
2. Open a command window.
	Note:
	Use this command window for the subsequent steps.
3. Set the `ORACLE_SID` environment variable.

Restrictions related to the valid characters in an `ORACLE_SID` are platform-specific. On some platforms, the SID is case-sensitive.

Note:

It is common practice to set the SID to be equal to the database name. The maximum number of characters for the database name is eight. For more information, see the discussion of the `DB_NAME` initialization parameter in [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=REFRN10041).

The following example for UNIX and Linux operating systems sets the SID for the instance that you will connect to in Step 6: Connect to the Instance:

- Bourne, Bash, or Korn shell:
	```
	ORACLE_SID=mynewdb
	export ORACLE_SID
	```
- C shell:
	```
	setenv ORACLE_SID mynewdb
	```

The following example sets the SID for the Windows operating system:

```
set ORACLE_SID=mynewdb
```

See Also:

[Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=CNCPT601) for background information about the Oracle instance

**Parent topic:** Using the CREATE DATABASE Statement to Create a CDB

#### 37.4.3 Step 2: Ensure That the Required Environment Variables Are Set

Depending on your platform, before you can start SQL\*Plus (as required in a later step), you may have to set environment variables, or at least verify that they are set properly.

- Set required environment variables.

For example, on most platforms, `ORACLE_SID` and `ORACLE_HOME` must be set. In addition, it is advisable to set the `PATH` variable to include the ORACLE\_HOME/bin directory. On the UNIX and Linux platforms, you must set these environment variables manually. On the Windows platform, OUI automatically assigns values to `ORACLE_HOME` and `ORACLE_SID` in the Windows registry. If you did not create a database upon installation, OUI does not set `ORACLE_SID` in the registry, and you will have to set the `ORACLE_SID` environment variable when you create your database later.

**Parent topic:** Using the CREATE DATABASE Statement to Create a CDB

#### 37.4.4 Step 3: Choose a Database Administrator Authentication Method

You must be authenticated and granted appropriate system privileges in order to create a database.

- Decide on an authentication method.

You can be authenticated as an administrator with the required privileges in the following ways:

- With a password file
- With operating system authentication

To be authenticated with a password file, create the password file as described in " [Creating and Maintaining a Database Password File](getting-started-with-database-administration.md) ". To be authenticated with operating system authentication, ensure that you log in to the host computer with a user account that is a member of the appropriate operating system user group. On the UNIX and Linux platforms, for example, this is typically the `dba` user group. On the Windows platform, the user installing the Oracle software is automatically placed in the required user group.

See Also:

- " [About Database Administrator Security and Privileges](getting-started-with-database-administration.md) "
- " [Database Administrator Authentication](getting-started-with-database-administration.md) " for information about password files and operating system authentication

**Parent topic:** Using the CREATE DATABASE Statement to Create a CDB

#### 37.4.5 Step 4: Create the Initialization Parameter File

When an Oracle instance starts, it reads an initialization parameter file. This file can be a text file, which can be created and modified with a text editor, or a binary file, which is created and dynamically modified by the database. The binary file, which is preferred, is called a server parameter file. In this step, you create a text initialization parameter file. In a later step, you create a server parameter file from the text file.

- Create the initialization parameter file.

One way to create the text initialization parameter file is to edit the sample presented in " [Sample Initialization Parameter File](creating-and-configuring-an-oracle-database.md) ".

If you create the initialization parameter file manually, ensure that it contains at least the parameters listed in Table 37-2. All other parameters not listed have default values.

Table 37-2 Recommended Minimum Initialization Parameters

| Parameter Name | Mandatory | Notes |
| --- | --- | --- |
| `DB_NAME` | Yes | Database identifier. Must correspond to the value used in the `CREATE` `DATABASE` statement. Maximum 8 characters. |
| `CONTROL_FILES` | No | Strongly recommended. If not provided, then the database instance creates one control file in the same location as the initialization parameter file. Providing this parameter enables you to multiplex control files. See " [Creating Initial Control Files](managing-control-files.md) " for more information. |
| `MEMORY_TARGET` | No | Sets the total amount of memory used by the instance and enables automatic memory management. You can choose other initialization parameters instead of this one for more manual control of memory usage. See " [Configuring Memory Manually](managing-memory.md) ". |

For convenience, store your initialization parameter file in the Oracle Database default location, using the default file name. Then when you start your database, it will not be necessary to specify the `PFILE` clause of the `STARTUP` command, because Oracle Database automatically looks in the default location for the initialization parameter file.

For more information about initialization parameters and the initialization parameter file, including the default name and location of the initialization parameter file for your platform, see " [About Initialization Parameters and Initialization Parameter Files](creating-and-configuring-an-oracle-database.md) ".

See Also:

- " [Specifying Initialization Parameters](creating-and-configuring-an-oracle-database.md) "
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=REFRN-GUID-FD266F6F-D047-4EBB-8D96-B51B1DCA2D61) for details on all initialization parameters

**Parent topic:** Using the CREATE DATABASE Statement to Create a CDB

#### 37.4.6 Step 5: (Windows Only) Create an Instance

On the Windows platform, before you can connect to an instance, you must manually create it if it does not already exist. The `ORADIM` command creates an Oracle Database instance by creating a new Windows service.

To create an instance:

- Enter the following command at a Windows command prompt:
	```
	oradim -NEW -SID sid -STARTMODE MANUAL -PFILE file
	```
	Replace the following placeholders with appropriate values:
	- `sid` - The desired SID (for example `mynewdb`)
		- `file` - The full path to the text initialization parameter file

Caution:

Do not set the - `STARTMODE` argument to `AUTO` at this point, because this causes the new instance to start and attempt to mount the database, which does not exist yet. You can change this parameter to `AUTO`, if desired, in [Step 14: (Optional) Enable Automatic Instance Startup](creating-and-configuring-an-oracle-database.md).

Most Oracle Database services log on to the system using the privileges of the Oracle Home User. The service runs with the privileges of this user. The `ORADIM` command prompts you for the password to this user account. You can specify other options using `ORADIM`.

See Also:

- [Oracle Database Platform Guide for Microsoft Windows](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=NTQRF05011) for more information on the `ORADIM` command and the Oracle Home User
- [Oracle Database Installation Guide for Microsoft Windows](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=NTDBI) for more information about the Oracle Home User

**Parent topic:** Using the CREATE DATABASE Statement to Create a CDB

#### 37.4.7 Step 6: Connect to the Instance

Start SQL\*Plus and connect to your Oracle Database instance with the `SYSDBA` administrative privilege.

- To authenticate with a password file, enter the following commands, and then enter the `SYS` password when prompted:
	```
	$ sqlplus /nolog
	SQL> CONNECT SYS AS SYSDBA
	```
- To authenticate with operating system authentication, enter the following commands:
	```
	$ sqlplus /nolog
	SQL> CONNECT / AS SYSDBA
	```

SQL\*Plus outputs the following message:

```
Connected to an idle instance.
```

Note:

SQL\*Plus may output a message similar to the following:

```
Connected to:
Oracle Database 12c Enterprise Edition Release 12.1.0.1.0 - 64bit Production
With the Partitioning, OLAP, Advanced Analytics and Real Application Testing options
```

If so, the instance is already started. You may have connected to the wrong instance. Exit SQL\*Plus with the `EXIT` command, check that `ORACLE_SID` is set properly, and repeat this step.

**Parent topic:** Using the CREATE DATABASE Statement to Create a CDB

#### 37.4.8 Step 7: Create a Server Parameter File

The server parameter file enables you to change initialization parameters with the `ALTER` `SYSTEM` command and persist the changes across a database shutdown and startup. You create the server parameter file from your edited text initialization file.

- Run the following SQL\*Plus command:
	```
	CREATE SPFILE FROM PFILE;
	```

This SQL\*Plus command reads the text initialization parameter file (PFILE) with the default name from the default location, creates a server parameter file (SPFILE) from the text initialization parameter file, and writes the SPFILE to the default location with the default SPFILE name.

You can also supply the file name and path for both the PFILE and SPFILE if you are not using default names and locations.

Tip:

The database must be restarted before the server parameter file takes effect.

Note:

Although creating a server parameter file is optional at this point, it is recommended. If you do not create a server parameter file, the instance continues to read the text initialization parameter file whenever it starts.

Important—If you are using Oracle Managed Files and your initialization parameter file does not contain the `CONTROL_FILES` parameter, then you must create a server parameter file now so the database can save the names and locations of the control files that it creates during the `CREATE` `DATABASE` statement. See " [Specifying Oracle Managed Files at Database Creation](creating-and-configuring-an-oracle-database.md) " for more information.

See Also:

- " [Managing Initialization Parameters Using a Server Parameter File](creating-and-configuring-an-oracle-database.md) "
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQLRF01315) for more information on the `CREATE` `SPFILE` command

**Parent topic:** Using the CREATE DATABASE Statement to Create a CDB

#### 37.4.9 Step 8: Start the Instance

Start an instance without mounting a database.

- Run the `STARTUP` command with the `NOMOUNT` clause.

Typically, you do this only during database creation or while performing maintenance on the database. In this example, because the initialization parameter file or server parameter file is stored in the default location, you are not required to specify the `PFILE` clause:

```
STARTUP NOMOUNT
```

At this point, the instance memory is allocated and its processes are started. The database itself does not yet exist.

See Also:

- [Starting Up and Shutting Down](starting-up-and-shutting-down.md) for information about using the `STARTUP` command
- " [Managing Initialization Parameters Using a Server Parameter File](creating-and-configuring-an-oracle-database.md) "

**Parent topic:** Using the CREATE DATABASE Statement to Create a CDB

#### 37.4.10 Step 9: Create a CDB with the CREATE DATABASE Statement

When you use the `CREATE DATABASE` statement to create a CDB, you must complete additional actions before you have an operational CDB.

These actions include building views on the data dictionary tables and installing standard PL/SQL packages in the root. You perform these actions by running the supplied catcdb.sql script.

The instructions in this section apply to single-instance installations only. See the Oracle Real Application Clusters (Oracle RAC) installation guide for your platform for instructions for creating an Oracle RAC CDB.

Note:

Single-instance does not mean that only one Oracle instance can reside on a single host computer. In fact, multiple Oracle instances (and their associated databases) can run on a single host computer. A single-instance database is a database that is accessed by only one Oracle instance at a time, as opposed to an Oracle RAC database, which is accessed concurrently by multiple Oracle instances on multiple nodes. See [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=RACAD) for more information on Oracle RAC.

Tip:

If you are using Oracle ASM to manage your disk storage, then you must start the Oracle ASM instance and configure your disk groups before performing these steps. See [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=OSTMG).

The examples in the following steps create a CDB named `newcdb`.

To create a CDB with the `CREATE` `DATABASE` statement:

1. Set the `ENABLE_PLUGGABLE_DATABASE` initialization parameter to `TRUE`.
	Also, in a CDB, the `DB_NAME` initialization parameter specifies the name of the root. It is common practice to set the SID to the name of the root. The maximum number of characters for this name is 30. For more information, see the discussion of the `DB_NAME` initialization parameter in [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=REFRN10041).
2. Use the `CREATE` `DATABASE` statement to create a new CDB.
	Note:
	If the `CREATE` `DATABASE` statement fails, and if you did not complete " Step 7: Create a Server Parameter File ", then ensure that there is not a pre-existing server parameter file (SPFILE) for this instance that is setting initialization parameters in an unexpected way. For example, an SPFILE contains a setting for the complete path to all control files, and the `CREATE` `DATABASE` statement fails if those control files do not exist. Ensure that you shut down and restart the instance (with `STARTUP` `NOMOUNT`) after removing an unwanted SPFILE. See " [Managing Initialization Parameters Using a Server Parameter File](creating-and-configuring-an-oracle-database.md) " for more information.
	See also the following examples after this procedure that describe how to create a new CDB using the `CREATE DATABASE` statement:
	- Example 1: Creating a CDB Without Using Oracle Managed Files
		- Example 2: Creating a CDB Using Oracle Managed Files
3. Run the `catcdb.sql` SQL script.
	Enter the following in SQL\*Plus to run the script:
	```
	@?/rdbms/admin/catcdb.sql
	```
4. When prompted by the script, enter the log file directory for parameter `1` and the log file name for parameter `2`.
	The following example enters `/tmp` for the first prompt and `create_cdb.log` for the second prompt:
	```
	SQL> host perl -I &&rdbms_admin &&rdbms_admin_catcdb --logDirectory &&1 --logFilename &&2
	Enter value for 1: /tmp
	Enter value for 2: create_cdb.log
	```
5. When prompted by the script, enter any other required information.
	For example, the scripts prompts for administrator passwords and the temporary tablespace name:
	```
	Enter new password for SYS: ********
	Enter new password for SYSTEM: ********
	Enter temporary tablespace name: TEMP
	```
6. Back Up the Database
	Take a full backup of the database to ensure that you have a complete set of files from which to recover if a media failure occurs.
	For information on backing up a database, see [Oracle Database Backup and Recovery User's Guide.](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=BRADV-GUID-008E0F84-E623-4467-8706-A99B34002DD6)
7. Enable Automatic Instance Startup
	You might want to configure the Oracle instance to start automatically when its host computer restarts.
	See your operating system documentation for instructions. For example, on Windows, use the following command to configure the database service to start the instance upon computer restart:
	```
	ORADIM -EDIT -SID sid -STARTMODE AUTO -SRVCSTART SYSTEM [-SPFILE]
	```
	You must use the `-SPFILE` argument if you want the instance to read an SPFILE upon automatic restart.

See Also:

- " [Specifying CREATE DATABASE Statement Clauses](creating-and-configuring-an-oracle-database.md) "
- " [Specifying Oracle Managed Files at Database Creation](creating-and-configuring-an-oracle-database.md) "
- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=OSTMG1390)

Example 1: Creating a CDB Without Using Oracle Managed Files

The following statement creates a CDB named `newcdb`. This name must agree with the `DB_NAME` parameter in the initialization parameter file. This example assumes the following:

- The initialization parameter file specifies the number and location of control files with the `CONTROL_FILES` parameter.
- The directory `/u01/app/oracle/oradata/newcdb` exists.
- The directory `/u01/app/oracle/oradata/pdbseed` exists.
- The directories `/u01/logs/my` and `/u02/logs/my` exist.

This example includes the `ENABLE` `PLUGGABLE` `DATABASE` clause to create a CDB with the root and the CDB seed. This example also includes the `SEED` `FILE_NAME_CONVERT` clause to specify the names and locations of the CDB seed's files. This example also includes `tablespace_datafile` clauses that specify attributes of the CDB seed's data files for the `SYSTEM` and `SYSAUX` tablespaces that differ from the root's. This example includes the `undo_mode_clause` to specify that the CDB undo mode is local.

```
CREATE DATABASE newcdb
  USER SYS IDENTIFIED BY sys_password
  USER SYSTEM IDENTIFIED BY system_password
  LOGFILE GROUP 1 ('/u01/logs/my/redo01a.log','/u02/logs/my/redo01b.log') 
             SIZE 100M BLOCKSIZE 512,
          GROUP 2 ('/u01/logs/my/redo02a.log','/u02/logs/my/redo02b.log') 
             SIZE 100M BLOCKSIZE 512,
          GROUP 3 ('/u01/logs/my/redo03a.log','/u02/logs/my/redo03b.log') 
             SIZE 100M BLOCKSIZE 512
  MAXLOGHISTORY 1
  MAXLOGFILES 16
  MAXLOGMEMBERS 3
  MAXDATAFILES 1024
  CHARACTER SET AL32UTF8
  NATIONAL CHARACTER SET AL16UTF16
  EXTENT MANAGEMENT LOCAL
  DATAFILE '/u01/app/oracle/oradata/newcdb/system01.dbf'
    SIZE 700M REUSE AUTOEXTEND ON NEXT 10240K MAXSIZE UNLIMITED
  SYSAUX DATAFILE '/u01/app/oracle/oradata/newcdb/sysaux01.dbf'
    SIZE 550M REUSE AUTOEXTEND ON NEXT 10240K MAXSIZE UNLIMITED
  DEFAULT TABLESPACE deftbs
     DATAFILE '/u01/app/oracle/oradata/newcdb/deftbs01.dbf'
     SIZE 500M REUSE AUTOEXTEND ON MAXSIZE UNLIMITED
  DEFAULT TEMPORARY TABLESPACE tempts1
     TEMPFILE '/u01/app/oracle/oradata/newcdb/temp01.dbf'
     SIZE 20M REUSE AUTOEXTEND ON NEXT 640K MAXSIZE UNLIMITED
  UNDO TABLESPACE undotbs1
     DATAFILE '/u01/app/oracle/oradata/newcdb/undotbs01.dbf'
     SIZE 200M REUSE AUTOEXTEND ON NEXT 5120K MAXSIZE UNLIMITED
  ENABLE PLUGGABLE DATABASE
    SEED
      FILE_NAME_CONVERT = ('/u01/app/oracle/oradata/newcdb/', 
                         '/u01/app/oracle/oradata/pdbseed/')
    LOCAL UNDO ON;
```

A CDB is created with the following characteristics:

- The CDB is named `newcdb`. Its global database name is `newcdb.us.example.com`, where the domain portion (`us.example.com`) is taken from the initialization parameter file. See " [Determining the Global Database Name](creating-and-configuring-an-oracle-database.md) ".
- Three control files are created as specified by the `CONTROL_FILES` initialization parameter, which was set before CDB creation in the initialization parameter file. See " [Sample Initialization Parameter File](creating-and-configuring-an-oracle-database.md) " and " [Specifying Control Files](creating-and-configuring-an-oracle-database.md) ".
- The passwords for user accounts `SYS` and `SYSTEM` are set to the values that you specified. The passwords are case-sensitive. The two clauses that specify the passwords for `SYS` and `SYSTEM` are not mandatory in this release of Oracle Database. However, if you specify either clause, then you must specify both clauses. For further information about the use of these clauses, see " [Protecting Your Database: Specifying Passwords for Users SYS and SYSTEM](creating-and-configuring-an-oracle-database.md) ".
- The new CDB has three online redo log file groups, each with two members, as specified in the `LOGFILE` clause. `MAXLOGFILES`, `MAXLOGMEMBERS`, and `MAXLOGHISTORY` define limits for the redo log. See " [Choosing the Number of Redo Log Files](managing-the-redo-log.md) ". The block size for the redo logs is set to 512 bytes, the same size as physical sectors on disk. The `BLOCKSIZE` clause is optional if block size is to be the same as physical sector size (the default). Typical sector size and thus typical block size is 512. Permissible values for `BLOCKSIZE` are 512, 1024, and 4096. For newer disks with a 4K sector size, optionally specify `BLOCKSIZE` as 4096. See " [Planning the Block Size of Redo Log Files](managing-the-redo-log.md) " for more information.
- `MAXDATAFILES` specifies the maximum number of data files that can be open in the CDB. This number affects the initial sizing of the control file. For a CDB, set `MAXDATAFILES` to a high number that anticipates the aggregate number of data files for all containers, in addition to the CDB root files.
	Note:
	You can set several limits during CDB creation. Some of these limits are limited by and affected by operating system limits. For example, if you set `MAXDATAFILES`, then Oracle Database allocates enough space in the control file to store `MAXDATAFILES` file names, even if the CDB has only one data file initially. However, because the maximum control file size is limited and operating system dependent, you might not be able to set all `CREATE DATABASE` parameters at their theoretical maximums.
	For more information about setting limits during CDB creation, see the [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SQLRF01204) and your operating system–specific Oracle documentation.
- The `AL32UTF8` character set is used to store data in this CDB.
- The `AL16UTF16` character set is specified as the `NATIONAL CHARACTER SET` used to store data in columns specifically defined as `NCHAR`, `NCLOB`, or `NVARCHAR2`.
- The `SYSTEM` tablespace, consisting of the operating system file `/u01/app/oracle/oradata/newcdb/system01.dbf`, is created as specified by the `DATAFILE` clause. If a file with that name already exists, then it is overwritten.
- The `SYSTEM` tablespace is created as a locally managed tablespace. See " [Creating a Locally Managed SYSTEM Tablespace](creating-and-configuring-an-oracle-database.md) ".
- A `SYSAUX` tablespace is created, consisting of the operating system file `/u01/app/oracle/oradata/newcdb/sysaux01.dbf` as specified in the `SYSAUX DATAFILE` clause. See " [About the SYSAUX Tablespace](creating-and-configuring-an-oracle-database.md) ".
- The `DEFAULT` `TABLESPACE` clause creates and names a default permanent tablespace for this CDB.
- The `DEFAULT TEMPORARY TABLESPACE` clause creates and names a default temporary tablespace for the root of this CDB. See " [Creating a Default Temporary Tablespace](creating-and-configuring-an-oracle-database.md) ".
- The `UNDO TABLESPACE` clause creates and names an undo tablespace that is used to store undo data for this CDB. In a CDB, an undo tablespace is required to manage the undo data, and the `UNDO_MANAGEMENT` initialization parameter must be set to `AUTO`. If you omit this parameter, then it defaults to `AUTO`. See " [Using Automatic Undo Management: Creating an Undo Tablespace](creating-and-configuring-an-oracle-database.md) ".
- Redo log files will not initially be archived, because the `ARCHIVELOG` clause is not specified in this `CREATE` `DATABASE` statement. This is customary during CDB creation. You can later use an `ALTER DATABASE` statement to switch to `ARCHIVELOG` mode. The initialization parameters in the initialization parameter file for `newcdb` relating to archiving are `LOG_ARCHIVE_DEST_1` and `LOG_ARCHIVE_FORMAT`. See [Managing Archived Redo Log Files](managing-archived-redo-log-files.md).
- The `ENABLE` `PLUGGABLE` `DATABASE` clause creates a CDB with the root and the CDB seed.
- `SEED` is required for the `FILE_NAME_CONVERT` clause and the `tablespace_datafile` clauses.
- The `FILE_NAME_CONVERT` clause generates file names for the CDB seed's files in the /u01/app/oracle/oradata/pdbseed directory using file names in the /u01/app/oracle/oradata/newcdb directory.
- The `LOCAL UNDO ON` clause sets the CDB’s undo mode to local, which means that each container in the CDB uses local undo.
	When the CDB is created in local undo mode, the CDB seed includes an undo tablespace so that any new PDB created from the CDB seed has an undo tablespace. When a PDB is created by plugging it in or cloning a remote PDB, and the source PDB was in shared undo mode, an undo tablespace is created for the PDB automatically the first time the PDB is opened.

Note:

- Ensure that all directories used in the `CREATE` `DATABASE` statement exist. The `CREATE` `DATABASE` statement does not create directories.
- If you are not using Oracle Managed Files, then every tablespace clause must include a `DATAFILE` or `TEMPFILE` clause.
- If CDB creation fails, then you can look at the alert log to determine the reason for the failure and to determine corrective actions. See " [Viewing the Alert Log](managing-diagnostic-data.md) ". If you receive an error message that contains a process number, then examine the trace file for that process. Look for the trace file that contains the process number in the trace file name. See " [Finding Trace Files](managing-diagnostic-data.md) " for more information.
- To resubmit the `CREATE` `DATABASE` statement after a failure, you must first shut down the instance and delete any files created by the previous `CREATE` `DATABASE` statement.

Example 2: Creating a CDB Using Oracle Managed Files

This example illustrates creating a CDB with Oracle Managed Files, which enables you to use a much simpler `CREATE` `DATABASE` statement. To use Oracle Managed Files, the initialization parameter `DB_CREATE_FILE_DEST` must be set. This parameter defines the base directory for the various CDB files that the CDB creates and automatically names.

The following statement is an example of setting this parameter in the initialization parameter file:

```
DB_CREATE_FILE_DEST='/u01/app/oracle/oradata'
```

This example sets the parameter Oracle ASM storage:

```
DB_CREATE_FILE_DEST = +data
```

This example includes the `ENABLE` `PLUGGABLE` `DATABASE` clause to create a CDB with the root and the CDB seed. This example does not include the `SEED` `FILE_NAME_CONVERT` clause because Oracle Managed Files determines the names and locations of the CDB seed's files. However, this example does include `tablespace_datafile` clauses that specify attributes of the CDB seed's data files for the `SYSTEM` and `SYSAUX` tablespaces that differ from the root's.

With Oracle Managed Files and the following `CREATE` `DATABASE` statement, the CDB creates the `SYSTEM` and `SYSAUX` tablespaces, creates the additional tablespaces specified in the statement, and chooses default sizes and properties for all data files, control files, and redo log files. Note that these properties and the other default CDB properties set by this method might not be suitable for your production environment, so it is recommended that you examine the resulting configuration and modify it if necessary.

```
CREATE DATABASE newcdb
USER SYS IDENTIFIED BY sys_password
USER SYSTEM IDENTIFIED BY system_password
EXTENT MANAGEMENT LOCAL
DEFAULT TABLESPACE users
DEFAULT TEMPORARY TABLESPACE temp
UNDO TABLESPACE undotbs1
ENABLE PLUGGABLE DATABASE
   SEED
   SYSTEM DATAFILES SIZE 125M AUTOEXTEND ON NEXT 10M MAXSIZE UNLIMITED
   SYSAUX DATAFILES SIZE 100M;
```

A CDB is created with the following characteristics:

- The CDB is named `newcdb`. Its global database name is `newcdb.us.example.com`, where the domain portion (`us.example.com`) is taken from the initialization parameter file. See " [Determining the Global Database Name](creating-and-configuring-an-oracle-database.md) ".
- The passwords for user accounts `SYS` and `SYSTEM` are set to the values that you specified. The passwords are case-sensitive. The two clauses that specify the passwords for `SYS` and `SYSTEM` are not mandatory in this release of Oracle Database. However, if you specify either clause, then you must specify both clauses. For further information about the use of these clauses, see " [Protecting Your Database: Specifying Passwords for Users SYS and SYSTEM](creating-and-configuring-an-oracle-database.md) ".
- The `DEFAULT` `TABLESPACE` clause creates and names a default permanent tablespace for this CDB.
- The `DEFAULT TEMPORARY TABLESPACE` clause creates and names a default temporary tablespace for the root of this CDB. See " [Creating a Default Temporary Tablespace](creating-and-configuring-an-oracle-database.md) ".
- The `UNDO TABLESPACE` clause creates and names an undo tablespace that is used to store undo data for this CDB. In a CDB, an undo tablespace is required to manage the undo data, and the `UNDO_MANAGEMENT` initialization parameter must be set to `AUTO`. If you omit this parameter, then it defaults to `AUTO`. See " [Using Automatic Undo Management: Creating an Undo Tablespace](creating-and-configuring-an-oracle-database.md) ".
- Redo log files will not initially be archived, because the `ARCHIVELOG` clause is not specified in this `CREATE` `DATABASE` statement. This is customary during CDB creation. You can later use an `ALTER DATABASE` statement to switch to `ARCHIVELOG` mode. The initialization parameters in the initialization parameter file for `newcdb` relating to archiving are `LOG_ARCHIVE_DEST_1` and `LOG_ARCHIVE_FORMAT`. See [Managing Archived Redo Log Files](managing-archived-redo-log-files.md).
- The `ENABLE` `PLUGGABLE` `DATABASE` clause creates a CDB with the root and the CDB seed.
- `SEED` is required for the `tablespace_datafile` clauses.
- The `SYSTEM` `DATAFILES` clause specifies attributes of the CDB seed's `SYSTEM` tablespace data file(s) that differ from the root's.
- The `SYSAUX` `DATAFILES` clause specifies attributes of the CDB seed's `SYSAUX` tablespace data file(s) that differ from the root's.

**Parent topic:** Using the CREATE DATABASE Statement to Create a CDB

### 37.5 Configuring EM Express for a CDB

For a CDB, you can configure Oracle Enterprise Manager Database Express (EM Express) for the root and for each PDB by setting a global HTTPS port, or you can set a different port for every container in the CDB.

To configure EM Express for a CDB:

You can set a global port, which enables you to use EM Express to connect to all of the PDBs in the CDB using the HTTP or HTTPS port for the CDB. Alternatively, you can set a different HTTP or HTTPS port for every container in a CDB.

1. In SQL\*Plus, access a container in a CDB.
	The user must have common `SYSDBA` administrative privilege, and you must exercise this privilege using `AS` `SYSDBA` at connect time. The container can be the root or a PDB.
	See " [Accessing a Container in a CDB with SQL\*Plus](administering-a-cdb-with-sql-plus.md) ".
2. Set the port in one of the following ways:
	- To set the global port, connect to the `CDB$ROOT`, and issue the following SQL statement to configure the global port for the CDB:
		```
		exec DBMS_XDB_CONFIG.SETGLOBALPORTENABLED(TRUE);
		```
		- To set the HTTP port for the current container, run the following procedure:
		```
		exec DBMS_XDB_CONFIG.SETHTTPPORT(http_port_number);
		```
		Replace `http_port_number` with the appropriate HTTP port number.
		- To set the HTTPS port for the current container, run the following procedure:
		```
		exec DBMS_XDB_CONFIG.SETHTTPSPORT(https_port_number);
		```
		Replace `https_port_number` with the appropriate HTTPS port number.

After the port is set, you can access EM Express in one of the following ways:

- To use the global port, enter the EM Express URL provided by Database Configuration Assistant (DBCA) when it configured the CDB that includes the PDB. When the EM Express login screen appears, specify your administrator credentials, and enter the name of the PDB that you want to connect to in the Container Name field.
- The URL for the HTTP port for a container:
	```
	http://database_hostname:http_port_number/em/
	```
	Replace `database_hostname` with the host name of the computer on which the database instance is running, and replace `http_port_number` with the appropriate HTTP port number.
- The URL for the HTTPS port for a container:
	```
	https://database_hostname:https_port_number/em/
	```
	Replace `database_hostname` with the host name of the computer on which the database instance is running, and replace `https_port_number` with the appropriate HTTPS port number.

When connected to the root, EM Express displays data and enables actions that apply to the entire CDB. When connected to a PDB, EM Express displays data and enables actions that apply to the PDB only.

Note:

If the listener is not configured on port 1521, then you must manually configure the port for EM Express. See [Oracle Database 2 Day DBA](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=ADMQS032) for instructions.

See Also:

[Oracle Database 2 Day DBA](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=ADMQS003) for more information about EM Express

**Parent topic:** Creating and Configuring a CDB

### 37.6 After Creating a CDB

After you create a CDB, it consists of the root and the CDB seed.

The root contains system-supplied metadata and common users that can administer the PDBs. The CDB seed is a template that you can use to create new PDBs. Figure 37-1 shows a newly created CDB.

Figure 37-1 A Newly Created CDB

![Figure 37-1 A Newly Created CDB](img/admin095.png)

> This illustration shows a CDB with a `CDB$ROOT` container and a `PDB$SEED` container plugged into the root container.


In a CDB, the root contains minimal user data or no user data. User data resides in the PDBs. Therefore, after creating a CDB, one of the first tasks is to add the PDBs that will contain the user data. See " [Creating and Removing PDBs with SQL\*Plus](creating-and-removing-pdbs-with-sql-plus.md) " for instructions.

Figure 37-2 shows a CDB with PDBs.

Figure 37-2 CDB with PDBs

![Figure 37-2 CDB with PDBs](img/admin094.png)

> This illustration shows a CDB with a `CDB$ROOT` container, a `PDB$SEED` container plugged into the root container, and several PDBs plugged into the root container.


You have the option of creating one or more application containers. An application container consists of an application root and application PDBs, and it stores data for one or more applications. An application container can store application common objects, which contain user data that can be shared by the application PDBs in the application container. It can also contain an application seed for fast creation of application PDBs in an application container.

Figure 37-3 Application Containers in a CDB

![Figure 37-3 Application Containers in a CDB](img/admin112.png)

> This illustration shows a CDB with the following components:
>
> - The CDB has a `CDB$ROOT` container.
> - A `PDB$SEED` container is plugged into the root container.
> - Several PDBs are plugged into the root container.
> - Two application containers plugged into the root container.
> - Each application container has an application root container.
> - One application container has two application PDBs plugged into its application root container.
> - One application container has three application PDBs plugged into its application root container.
> - The application container with two application PDBs also has an application seed plugged into its application root container.


When you have added the PDBs and application containers to the CDB, the physical structure of a CDB is very similar to the physical structure of a non-CDB. A CDB contains the following files:

- One control file
- One active online redo log for a single-instance CDB, or one active online redo log for each instance of an Oracle RAC CDB
- Sets of temp files
	There is one default temporary tablespace for the root of the CDB and one for each PDB, application root, and application PDB.
- Sets of system data files
	The primary physical difference between a CDB and a non-CDB is in the data files. A non-CDB has only one set of system data files. In contrast, a CDB includes one set of system data files for each container in the CDB, including a set of system data files for each PDB, application root, and application PDB. In addition, a CDB has one set of user-created data files for each container. If the CDB is in local undo mode, then each container also has its own undo tablespace and associated data files.
- Sets of user-created data files
	Each PDB has its own set of non-system data files. These data files contain the user-defined schemas and database objects for the PDB.

See [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=CNCPT89268) for more information about the physical architecture of a CDB.

For backup and recovery of a CDB, Recovery Manager (RMAN) is recommended. PDB point-in-time recovery (PDB PITR) must be performed with RMAN. By default, RMAN turns on control file autobackup for a CDB. It is strongly recommended that control file autobackup is enabled for a CDB, to ensure that PDB PITR can undo data file additions or deletions.

Because the physical structure of a CDB and a non-CDB are similar, most management tasks are the same for a CDB and a non-CDB. However, some administrative tasks are specific to CDBs. The following chapters describe these tasks:

- " [Creating and Removing PDBs with SQL\*Plus](creating-and-removing-pdbs-with-sql-plus.md) "
	This chapter documents the following tasks:
	- Creating a PDB using the CDB seed with SQL\*Plus
		- Creating a PDB by cloning an existing PDB or Non-CDB with SQL\*Plus
		- Creating a PDB by relocating it with SQL\*Plus
		- Creating a PDB as a proxy PDB with SQL\*Plus
		- Plugging in a PDB with SQL\*Plus
		- Unplugging a PDB with SQL\*Plus
		- Dropping a PDB with SQL\*Plus
- " [Creating and Removing PDBs with Cloud Control](creating-and-removing-pdbs-with-cloud-control.md) "
	This chapter documents the following tasks:
	- Creating a PDB with Cloud Control
		- Plugging in a PDB with Cloud Control
		- Unplugging a PDB with Cloud Control
- " [Creating and Removing Application Containers and Seeds with SQL\*Plus](creating-removing-application-containers-seeds-with-sql-plus.md) "
	This chapter documents the following tasks:
	- Creating application containers with SQL\*Plus
		- Creating application seeds with SQL\*Plus
		- Unplugging application containers with SQL\*Plus
		- Unplugging application seeds with SQL\*Plus
		- Dropping application containers with SQL\*Plus
		- Dropping application seeds with SQL\*Plus
- " [Administering a CDB with SQL\*Plus](administering-a-cdb-with-sql-plus.md) "
	This chapter documents the following tasks:
	- Connecting to a container
		- Switching into a container
		- Modifying a CDB
		- Modifying the root
		- Changing the open mode of a PDB
		- Executing DDL statements in a CDB
		- Shutting down the CDB instance
- " [Administering CDBs and PDBs with Cloud Control](administering-cdbs-and-pdbs-with-cloud-control.md) "
	This chapter documents the following tasks:
	- Managing CDB storage and schema objects
		- Managing per-container storage and schema objects
		- Monitoring storage and schema alerts
		- Switching into a container
		- Changing the open mode of a PDB
- " [Administering PDBs with SQL\*Plus](administering-pdbs-with-sql-plus.md) "
	This chapter documents the following tasks:
	- Connecting to a PDB
		- Modifying a PDB
		- Managing services associated with PDBs
- " [Administering Application Containers with SQL\*Plus](administering-application-containers-with-sql-plus.md) "
	This chapter documents the following tasks:
	- Managing applications in an application container, including installing, upgrading, and patching applications
		- Managing application common objects
		- Issuing DML statements on containers in an application container
		- Partitioning by PDB with container maps
- " [Viewing Information About CDBs and PDBs with SQL\*Plus](viewing-information-about-cdbs-and-pdbs-with-sql-plus.md) "
	This chapter documents the following tasks:
	- Querying views for monitoring a CDB and its PDBs
		- Running sample queries that provide information about a CDB and its PDBs
- " [Using Oracle Resource Manager for PDBs with SQL\*Plus](using-oracle-resource-manager-for-pdbs-with-sql-plus.md) "
	This chapter documents the following tasks:
	- Creating resource plans in a CDB with SQL\*Plus
		- Managing resource plans in a CDB with SQL\*Plus
- " [Using Oracle Resource Manager for PDBs with Cloud Control](using-oracle-resource-manager-for-pdbs-with-cloud-control.md) "
	This chapter documents the following tasks:
	- Creating resource plans in a CDB with Cloud Control
		- Monitoring the system performance under a CDB resource plan with Cloud Control
		- Creating a PDB resource plan
- " [Using Oracle Scheduler with a CDB](using-oracle-scheduler-with-a-cdb.md) "
	This chapter documents the following topics:
	- `DBMS_SCHEDULER` invocations in a CDB
		- Job coordinator and slave processes in a CDB
		- Using `DBMS_JOB`
		- Processes to close a PDB
		- New and changed views

**Parent topic:** Creating and Configuring a CDB