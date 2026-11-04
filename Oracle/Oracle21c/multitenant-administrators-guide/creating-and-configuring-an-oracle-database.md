---
title: "Administrator’s Guide"
book: "Multitenant Administrator's Guide"
doc_id: F31734-10
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/multi/creating-and-configuring-an-oracle-database.html
tags:
  - oracle
  - 21c
  - multitenant-administrators-guide
---

After you plan your CDB, you can create it with a graphical tool or a SQL command.

Database creation prepares several operating system files to work together as CDB. You only need to create a CDB once, regardless of how many data files it has or how many instances access it. You can create a CDB to erase information in an existing CDB and create a new CDB with the same name and physical structure.

- Creating a CDB with DBCA  
	Oracle Database Configuration Assistant (DBCA) is a tool for creating and configuring a CDB.
- Creating a Database with the CREATE DATABASE Statement  
	Using the `CREATE DATABASE ... ENABLE PLUGGABLE DATABASE` SQL statement is a more manual approach to creating a database than using Oracle Database Configuration Assistant (DBCA). One advantage of using this statement over using DBCA is that you can create databases from within scripts.
- Considerations After Creating a CDB  
	After you create a CDB, the instance is left running, and the database is open and available for normal database use. You may want to perform specific actions after creating a database.
- Database Data Dictionary Views  
	You can query data dictionary views for information about your database content and structure.

See Also:

- Your platform-specific Oracle Real Application Clusters (Oracle RAC) installation guide for information about creating a database in an Oracle RAC environment
- [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=CWADD-GUID-CCEC5960-EDA4-4A3F-9643-0CA308EA49AA) for information on creating a database using Fleet Patching and Provisioning (it was called as Rapid Home Provisioning in the earlier database releases)

**Parent topic:** [Creating CDBs](creating-and-configuring-a-multitenant-environment.md)

### Creating a CDB with DBCA

Oracle Database Configuration Assistant (DBCA) is a tool for creating and configuring a CDB.

- About Creating a CDB with DBCA  
	Oracle strongly recommends using the Database Configuration Assistant (DBCA) to create a CDB, because it is a more automated approach, and your CDB is ready to use when DBCA completes.
- After Creating a CDB  
	After creation, a CDB consists of the root and the PDB seed.

**Parent topic:** Creating a CDB: Basic Steps

#### About Creating a CDB with DBCA

Oracle strongly recommends using the Database Configuration Assistant (DBCA) to create a CDB, because it is a more automated approach, and your CDB is ready to use when DBCA completes.

DBCA offers the following advantages over alternative techniques:

- Creation is largely automated.
- DBCA enables you to specify the number of PDBs in the CDB when it is created.
- When DBCA completes, the CDB is ready to use.
- After a CDB is created, you can use DBCA to do the following:
	- Clone local PDBs
		- Plug in and unplug PDBs
		- Duplicate a CDB (silent mode only)

Depending on the type of install that you select, Oracle Universal Installer (OUI) can launch DBCA. You can also launch DBCA as a standalone tool at any time after Oracle Database installation.

You can use DBCA to create a CDB in either of the following modes:

- Interactive mode
	This mode provides a graphical interface and guided workflow for creating and configuring a CDB.
- Noninteractive mode (also called silent mode)
	This mode enables you to script a preconfigured CDB template deployment with customized PDB seed databases that are suitable for cloning. Run DBCA in silent mode by specifying command-line arguments, a response file, or both.

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-9E65AD37-BEDC-462A-A381-64C0380E0CCF) to learn how to create a database with DBCA
- The DBCA online help

**Parent topic:** Creating a CDB with DBCA

#### After Creating a CDB

After creation, a CDB consists of the root and the PDB seed.

The root contains system-supplied metadata and common users that can administer the PDBs. The PDB seed is a template that you can use to create new PDBs. The following graphic shows a newly created CDB.

Figure 3-1 A Newly Created CDB

![Figure 3-1 A Newly Created CDB](img/admin0951.png)

> This graphic depicts a rectangle with a dotted-line border. The rectangle is labeled "CDB." Inside the CDB is a long box labeled "Root (CDB$ROOT)." An cylinder icon labeled "Seed (PDB$SEED)" is plugged into the Root box.


In a CDB, the root contains minimal user data or no user data. User data resides in the PDBs. Therefore, after creating a CDB, one of the first tasks is to add the PDBs that will contain the user data.

The following graphic shows a CDB with PDBs.

Figure 3-2 CDB with PDBs

![Figure 3-2 CDB with PDBs](img/admin094.png)

> This illustration shows a CDB with a `CDB$ROOT` container, a `PDB$SEED` container plugged into the root container, and several PDBs plugged into the root container.


You have the option of creating one or more application containers. An application container consists of an application root and application PDBs, and it stores data for one or more applications. An application container can store application common objects, which contain user data that can be shared by the application PDBs in the application container. It can also contain an application seed for fast creation of application PDBs in an application container.

Figure 3-3 Application Containers in a CDB

![Figure 3-3 Application Containers in a CDB](img/admin112.png)

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


A CDB contains the following files:

- One control file
- One active online redo log for a single-instance CDB, or one active online redo log for each instance of an Oracle RAC CDB
- Sets of temp files
	There is one default temporary tablespace for the root of the CDB and one for each PDB, application root, and application PDB.
- Sets of system data files
	A CDB includes one set of system data files for each container in the CDB, including a set of system data files for each PDB, application root, and application PDB. In addition, a CDB has one set of user-created data files for each container. If the CDB is in local undo mode, then each container also has its own undo tablespace and associated data files.
- Sets of user-created data files
	Each PDB has its own set of non-system data files. These data files contain the user-defined schemas and database objects for the PDB.

For backup and recovery of a CDB, Recovery Manager (RMAN) is recommended. PDB point-in-time recovery (PDB PITR) must be performed with RMAN. By default, RMAN turns on control file autobackup for a CDB. It is strongly recommended that control file autobackup is enabled for a CDB, to ensure that PDB PITR can undo data file additions or deletions.

**Parent topic:** Creating a CDB with DBCA

### Creating a Database with the CREATE DATABASE Statement

Using the `CREATE DATABASE ... ENABLE PLUGGABLE DATABASE` SQL statement is a more manual approach to creating a database than using Oracle Database Configuration Assistant (DBCA). One advantage of using this statement over using DBCA is that you can create databases from within scripts.

- About CDB Creation with SQL Statements  
	This section explains how to create a CDB manually, without using DBCA.
- Step 1: Specify an Instance Identifier (SID)  
	The `ORACLE_SID` environment variable is used to distinguish this instance from other Oracle Database instances that you may create later and run concurrently on the same host computer.
- Step 2: Ensure That the Required Environment Variables Are Set  
	Depending on your platform, before you can start SQL\*Plus (as required in a later step), you may have to set environment variables, or at least verify that they are set properly.
- Step 3: Choose a Database Administrator Authentication Method  
	You must be authenticated and granted appropriate system privileges in order to create a CDB.
- Step 4: Create the Initialization Parameter File  
	When an Oracle instance starts, it reads an initialization parameter file.
- Step 5: (Windows Only) Create an Instance  
	On the Windows platform, before you can connect to a database instance, you must manually create it if it does not already exist. The `ORADIM` command creates an instance by creating a new Windows service.
- Step 6: Connect to the Instance  
	Start SQL\*Plus and connect to your Oracle Database instance with the `SYSDBA` administrative privilege.
- Step 7: Create a Server Parameter File  
	The server parameter file enables you to change initialization parameters with the `ALTER SYSTEM` command and persist the changes across a database shutdown and startup. You create the server parameter file from your edited text initialization file.
- Step 8: Start the Database Instance  
	Start an instance without mounting a CDB.
- Step 9: Issue the CREATE DATABASE Statement  
	To create the new database, use the `CREATE DATABASE` statement.
- Step 10: Run Scripts to Build Data Dictionary Views  
	Run the scripts necessary to build data dictionary views, synonyms, and PL/SQL packages in the CDB root.
- Step 11: (Optional) Run Scripts to Install Additional Options  
	You may want to run other scripts. The scripts that you run are determined by the features and options you choose to use or install.
- Step 12: Back Up the Database  
	Take a full backup of the database to ensure that you have a complete set of files from which to recover if a media failure occurs.
- Step 13: (Optional) Enable Automatic Instance Startup  
	You might want to configure the Oracle database instance to start automatically when its host computer restarts.

**Parent topic:** Creating a CDB: Basic Steps

#### About CDB Creation with SQL Statements

This section explains how to create a CDB manually, without using DBCA.

Note:

" [Specifying CREATE DATABASE Statement Clauses](create-cdb-adv.md) " provides more detailed information about the SQL clauses described in this chapter.

- About Oracle RAC and Oracle ASM  
	The instructions in this section apply to single-instance installations only.
- About Enabling PDBs  
	To create a CDB with the `CREATE DATABASE` command, the `ENABLE_PLUGGABLE_DATABASE` initialization parameter must be set to `true`.
- About the Names and Locations of Files for the CDB Root and PDB$SEED  
	To create the CDB, Oracle Database must know the names and locations of the files for the CDB root and `PDB$SEED`.
- About the Attributes of the Data Files for PDB$SEED  
	You can use the PDB seed (`PDB$SEED`) as a template to create new containers.
- About the CDB Undo Mode  
	Shared undo is the default. You can use the undo\_mode\_clause to an `ENABLE PLUGGABLE DATABASE` clause to specify the undo mode of the CDB.

See Also:

[Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=CNCPT89268) for information about the files in a CDB

**Parent topic:** Creating a Database with the CREATE DATABASE Statement

##### About Oracle RAC and Oracle ASM

The instructions in this section apply to single-instance installations only.

See the Oracle Real Application Clusters (Oracle RAC) installation guide for your platform for instructions for creating an Oracle RAC database.

Note:

- Single-instance does not mean that only one Oracle instance can reside on a single host computer. In fact, multiple Oracle instances (and their associated databases) can run on a single host computer. A **single-instance database** is a database that is accessed by only one Oracle instance at a time, as opposed to an Oracle RAC database, which is accessed concurrently by multiple Oracle instances on multiple nodes.
- Starting in Oracle Database 12c Release 2 (12.2), read-only and read/write instances can coexist within a single Oracle RAC database. This configuration is useful for the scalability of parallel queries.

Tip:

If you are using Oracle Automatic Storage Management (Oracle ASM) to manage your disk storage, then you must start the Oracle ASM instance and configure your disk groups before performing these steps. See [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=OSTMG-GUID-74C67180-6F24-4F50-8581-0DF71F1C5B47).

See Also:

- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=RACAD-GUID-D04AA2A7-2E68-4C5C-BD6E-36C62427B98E) for more information on Oracle RAC
- [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=CWADD-GUID-DF441DD8-B3B4-48C2-96B5-3DD59EAAC8EF) for information about configuring read-only and read/write instances that coexist within a single Oracle RAC database

**Parent topic:** About CDB Creation with SQL Statements

##### About Enabling PDBs

To create a CDB with the `CREATE DATABASE` command, the `ENABLE_PLUGGABLE_DATABASE` initialization parameter must be set to `true`.

The `CREATE DATABASE` command creates a CDB with the CDB root and `PDB$SEED`. You must create all other containers manually.

**Parent topic:** About CDB Creation with SQL Statements

##### About the Names and Locations of Files for the CDB Root and PDB$SEED

To create the CDB, Oracle Database must know the names and locations of the files for the CDB root and `PDB$SEED`.

After the `CREATE DATABASE` statement completes successfully, you can use `PDB$SEED` and its files to create new PDBs. You cannot modify the PDB seed after it is created.

You must specify the names and locations of the files for `PDB$SEED` in one of the following ways:

1. The `ENABLE PLUGGABLE DATABASE SEED FILE_NAME_CONVERT` clause of `CREATE DATABASE`
2. Oracle Managed Files
3. The `PDB_FILE_NAME_CONVERT` initialization parameter

If you use more than one technique, then the `CREATE DATABASE` statement uses one technique in the order of precedence of the list. For example, if you use all techniques, then the `CREATE DATABASE` statement only uses the specifications in the `ENABLE PLUGGABLE DATABASE SEED FILE_NAME_CONVERT` clause because it is first in the list.

- The ENABLE PLUGGABLE DATABASE SEED FILE\_NAME\_CONVERT Clause  
	The `ENABLE PLUGGABLE DATABASE SEED FILE_NAME_CONVERT` clause of the `CREATE DATABASE` statement specifies how to generate the names of the `PDB$SEED` files using the names of the CDB root files.
- Oracle Managed Files  
	When Oracle Managed Files is enabled, it can determine the names and locations of the `PDB$SEED` files.
- The PDB\_FILE\_NAME\_CONVERT Initialization Parameter  
	The `PDB_FILE_NAME_CONVERT` initialization parameter can specify the names and locations of the seed's files.

See Also:

" [Creating a PDB from Scratch](creating-a-pdb-from-scratch.md) "

**Parent topic:** About CDB Creation with SQL Statements

###### The ENABLE PLUGGABLE DATABASE SEED FILE\_NAME\_CONVERT Clause

The `ENABLE PLUGGABLE DATABASE SEED FILE_NAME_CONVERT` clause of the `CREATE DATABASE` statement specifies how to generate the names of the `PDB$SEED` files using the names of the CDB root files.

You can use this clause to specify one of the following options:

- One or more file name patterns and replacement file name patterns, in the following form:
	```
	'string1' , 'string2' , 'string3' , 'string4' , ...
	```
	The string2 file name pattern replaces the string1 file name pattern, and the string4 file name pattern replaces the string3 file name pattern. You can use as many pairs of file name pattern and replacement file name pattern strings as required.
	If you specify an odd number of strings (the last string has no corresponding replacement string), then an error is returned. Do not specify more than one pattern/replace string that matches a single file name or directory.
	File name patterns cannot match files or directories managed by Oracle Managed Files.
- `NONE` when no file names should be converted. Omitting the `SEED FILE_NAME_CONVERT` clause is the same as specifying `NONE`.

Example 3-1 SEED FILE\_NAME\_CONVERT Clause

This `ENABLE PLUGGABLE DATABASE SEED FILE_NAME_CONVERT` clause generates file names for the `PDB$SEED` files in the `/oracle/pdbseed/` directory using file names in the `/oracle/dbs/` directory.

```
ENABLE PLUGGABLE DATABASE SEED FILE_NAME_CONVERT = ('/oracle/dbs/', '/oracle/pdbseed/')
```

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF-GUID-ECE717DF-F116-4151-927C-2E51BB9DD39C) for the syntax of the `ENABLE PLUGGABLE DATABASE                                                   SEED FILE_NAME_CONVERT` clause

**Parent topic:** About the Names and Locations of Files for the CDB Root and PDB$SEED

###### Oracle Managed Files

When Oracle Managed Files is enabled, it can determine the names and locations of the `PDB$SEED` files.

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-4A3C4616-0D81-4BBA-8EAD-FCAA8AD5C15A)

**Parent topic:** About the Names and Locations of Files for the CDB Root and PDB$SEED

###### The PDB\_FILE\_NAME\_CONVERT Initialization Parameter

The `PDB_FILE_NAME_CONVERT` initialization parameter can specify the names and locations of the seed's files.

To use this technique, ensure that the `PDB_FILE_NAME_CONVERT` initialization parameter is included in the initialization parameter file when you create the CDB.

File name patterns specified in this initialization parameter cannot match files or directories managed by Oracle Managed Files.

See Also:

[Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=REFRN10322)

**Parent topic:** About the Names and Locations of Files for the CDB Root and PDB$SEED

##### About the Attributes of the Data Files for PDB$SEED

You can use the PDB seed (`PDB$SEED`) as a template to create new containers.

The attributes of the data files for the CDB root `SYSTEM` and `SYSAUX` tablespaces might not be suitable for the PDB seed. In this case, you can specify different attributes for the PDB seed data files by using the `tablespace_datafile` clauses. Use these clauses to specify attributes for all data files comprising the `SYSTEM` and `SYSAUX` tablespaces in the PDB seed. The values inherited from the root are used for any attributes whose values have not been provided.

The syntax of the `tablespace_datafile` clauses is the same as the syntax for a data file specification, excluding the name and location of the data file and the `REUSE` attribute. You can use the `tablespace_datafile` clauses with any of the methods for specifying the names and locations of the PDB seed's data files described in " About the Names and Locations of Files for the CDB Root and PDB$SEED ".

The `tablespace_datafile` clauses do not specify the names and locations of the PDB seed's data files. Instead, they specify the attributes of `SYSTEM` and `SYSAUX` data files in the PDB seed that differ from those in the root. If `SIZE` is not specified in the `tablespace_datafile` clause for a tablespace, then data file size for the tablespace is set to a predetermined fraction of the size of a corresponding root data file.

Example 3-2 Using the tablespace\_datafile Clauses

Assume the following `CREATE DATABASE` clauses specify the names, locations, and attributes of the data files that comprise the `SYSTEM` and `SYSAUX` tablespaces in the root.

```
DATAFILE '/u01/app/oracle/oradata/newcdb/system01.dbf' 
  SIZE 325M REUSE
SYSAUX DATAFILE '/u01/app/oracle/oradata/newcdb/sysaux01.dbf' 
  SIZE 325M REUSE
```

You can use the following `tablespace_datafile` clauses to specify different attributes for these data files:

```
SEED 
  SYSTEM DATAFILES 
    SIZE 125M AUTOEXTEND ON NEXT 10M MAXSIZE UNLIMITED
  SYSAUX DATAFILES 
    SIZE 100M
```

In this example, the data files for the PDB seed's `SYSTEM` and `SYSAUX` tablespaces inherit the `REUSE` attribute from the root's data files. However, the following attributes of the PDB seed's data files differ from the root's:

- The data file for the `SYSTEM` tablespace is 125 MB for the PDB seed and 325 MB for the root.
- `AUTOEXTEND` is enabled for the PDB seed's `SYSTEM` data file, and it is disabled by default for the root's `SYSTEM` data file.
- The data file for the `SYSAUX` tablespace is 100 MB for the PDB seed and 325 MB for the root.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF52248) for information about data file specifications

**Parent topic:** About CDB Creation with SQL Statements

##### About the CDB Undo Mode

Shared undo is the default. You can use the undo\_mode\_clause to an `ENABLE PLUGGABLE DATABASE` clause to specify the undo mode of the CDB.

The undo\_mode\_clause specifies whether the CDB undo mode is local or shared. Local undo mode means that every container in the CDB uses local undo. To configure local undo mode for the CDB, specify `LOCAL UNDO ON`.

Shared undo mode means that there is one active undo tablespace for a single-instance CDB, or for an Oracle RAC CDB, there is one active undo tablespace for each instance. To configure shared undo mode for the CDB, either do not specify undo\_mode\_clause, or specify `LOCAL UNDO OFF`.

**Parent topic:** About CDB Creation with SQL Statements

#### Step 1: Specify an Instance Identifier (SID)

The `ORACLE_SID` environment variable is used to distinguish this instance from other Oracle Database instances that you may create later and run concurrently on the same host computer.

1. Decide on a unique Oracle system identifier (SID) for your instance.
2. Open a command window.
	Note:
	Use this command window for the subsequent steps.
3. Set the `ORACLE_SID` environment variable.

Restrictions related to the valid characters in an `ORACLE_SID` are platform-specific. On some platforms, the SID is case-sensitive.

Note:

It is common practice to set the SID to be equal to the database name. The maximum number of characters for the database name is eight.

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

- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=CNCPT601) for background information about the Oracle instance
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=REFRN10041) to learn more about the `DB_NAME` initialization parameter

**Parent topic:** Creating a Database with the CREATE DATABASE Statement

#### Step 2: Ensure That the Required Environment Variables Are Set

Depending on your platform, before you can start SQL\*Plus (as required in a later step), you may have to set environment variables, or at least verify that they are set properly.

- Set required environment variables.

For example, on most platforms, `ORACLE_SID` and `ORACLE_HOME` must be set. In addition, it is advisable to set the `PATH` variable to include the ORACLE\_HOME/bin directory. On the UNIX and Linux platforms, you must set these environment variables manually. On the Windows platform, OUI automatically assigns values to `ORACLE_HOME` and `ORACLE_SID` in the Windows registry. If you did not create a database upon installation, OUI does not set `ORACLE_SID` in the registry, and you will have to set the `ORACLE_SID` environment variable when you create your database later.

**Parent topic:** Creating a Database with the CREATE DATABASE Statement

#### Step 3: Choose a Database Administrator Authentication Method

You must be authenticated and granted appropriate system privileges in order to create a CDB.

- Decide on an authentication method.

You can be authenticated as an administrator with the required privileges in the following ways:

- With a password file
- With operating system authentication

To be authenticated with a password file, create the password file. To be authenticated with operating system authentication, ensure that you log in to the host computer with a user account that is a member of the appropriate operating system user group. On the UNIX and Linux platforms, for example, this is typically the `dba` user group. On the Windows platform, the user installing the Oracle software is automatically placed in the required user group.

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-26EC8D1B-7A2F-4F0A-9588-D92CBD610858) for information about password files and operating system authentication

**Parent topic:** Creating a Database with the CREATE DATABASE Statement

#### Step 4: Create the Initialization Parameter File

When an Oracle instance starts, it reads an initialization parameter file.

The parameter file can be a text file, which can be created and modified with a text editor, or a binary file, which is created and dynamically modified by the database. The binary file, which is preferred, is called a **server parameter file**. In this step, you create a text initialization parameter file. In a later step, you create a server parameter file from the text file.

- Create the initialization parameter file.

One way to create the text initialization parameter file is to edit the sample presented in " [Sample Initialization Parameter File](create-cdb-adv.md) ".

If you create the initialization parameter file manually, ensure that it contains at least the parameters listed in the following table. All other parameters not listed have default values.

Table 3-1 Recommended Minimum Initialization Parameters

| Parameter Name | Mandatory | Notes |
| --- | --- | --- |
| `DB_NAME` | Yes | Database identifier for the name of the CDB root. Must correspond to the value used in the `CREATE DATABASE` statement. Maximum 8 characters.  It is common practice to set the SID to the name of the CDB root. The maximum number of characters for this name is 30. For more information, see the discussion of the `DB_NAME` initialization parameter in [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=REFRN10041). |
| `DB_DOMAIN` | Yes | Specifies the network domain where the database is created.  Create the global database name for the CDB root by setting both the `DB_NAME` and `DB_DOMAIN` initialization parameters. The global database name of the CDB root is the global database name of the CDB. The global database name of a PDB is defined by the PDB name and the `DB_DOMAIN` initialization parameter. |
| `ENABLE_PLUGGABLE_DATABASE` | Yes | Specifies that the database is a CDB. Must be set to `TRUE`. |
| `CONTROL_FILES` | No | Strongly recommended. If not provided, then the database instance creates one control file in the same location as the initialization parameter file. Providing this parameter enables you to multiplex control files. |
| `MEMORY_TARGET` | No | Sets the total amount of memory used by the instance and enables automatic memory management. You can choose other initialization parameters instead of this one for more manual control of memory usage. |
| `DB_CREATE_FILE_DEST` | No | Defines the base directory for Oracle Managed Files that the CDB creates and automatically names. To use Oracle Managed Files, the initialization parameter `DB_CREATE_FILE_DEST` must be set. |

For convenience, store your initialization parameter file in the Oracle Database default location, using the default file name. Then when you start your database, it will not be necessary to specify the `PFILE` clause of the `STARTUP` command, because Oracle Database automatically looks in the default location for the initialization parameter file.

For more information about initialization parameters and the initialization parameter file, including the default name and location of the initialization parameter file for your platform, see " [About Initialization Parameters and Initialization Parameter Files](create-cdb-adv.md) ".

See Also:

- " [Specifying Initialization Parameters](create-cdb-adv.md) "
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=REFRN-GUID-FD266F6F-D047-4EBB-8D96-B51B1DCA2D61) for details on all initialization parameters

**Parent topic:** Creating a Database with the CREATE DATABASE Statement

#### Step 5: (Windows Only) Create an Instance

On the Windows platform, before you can connect to a database instance, you must manually create it if it does not already exist. The `ORADIM` command creates an instance by creating a new Windows service.

To create a database instance:

- Enter the following command at a Windows command prompt:
	```
	oradim -NEW -SID sid -STARTMODE MANUAL -PFILE file
	```
	Replace the following placeholders with appropriate values:
	- `sid` - The desired SID (for example `mynewdb`)
		- `file` - The full path to the text initialization parameter file

Caution:

Do not set the - `STARTMODE` argument to `AUTO` at this point, because this causes the new instance to start and attempt to mount the database, which does not exist yet. You can change this parameter to `AUTO`, if desired, in Step 13: (Optional) Enable Automatic Instance Startup.

Most Oracle Database services log on to the system using the privileges of the Oracle Home User. The service runs with the privileges of this user. The `ORADIM` command prompts you for the password to this user account. You can specify other options using `ORADIM`.

See Also:

[Oracle Database Platform Guide for Microsoft Windows](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=NTQRF05011) for more information on the `ORADIM` command and the Oracle Home User

**Parent topic:** Creating a Database with the CREATE DATABASE Statement

#### Step 6: Connect to the Instance

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
Oracle Database 19c Enterprise Edition Release 19.0.0.0.0 - Production Version 19.1.0.0.0
```

If so, the instance is already started. You may have connected to the wrong instance. Exit SQL\*Plus with the `EXIT` command, check that `ORACLE_SID` is set properly, and repeat this step.

**Parent topic:** Creating a Database with the CREATE DATABASE Statement

#### Step 7: Create a Server Parameter File

The server parameter file enables you to change initialization parameters with the `ALTER SYSTEM` command and persist the changes across a database shutdown and startup. You create the server parameter file from your edited text initialization file.

- Run the following SQL\*Plus command:
	```
	CREATE SPFILE FROM PFILE;
	```

This SQL\*Plus command reads the text initialization parameter file (PFILE) with the default name from the default location, creates a server parameter file (SPFILE) from the text initialization parameter file, and writes the SPFILE to the default location with the default SPFILE name.

You can also supply the file name and path for both the PFILE and SPFILE if you are not using default names and locations.

Tip:

The CDB must be restarted before the server parameter file takes effect.

Note:

Although creating a server parameter file is optional at this point, it is recommended. If you do not create a server parameter file, the instance continues to read the text initialization parameter file whenever it starts.

Important—If you are using Oracle Managed Files and your initialization parameter file does not contain the `CONTROL_FILES` parameter, then you must create a server parameter file now so the database can save the names and locations of the control files that it creates during the `CREATE DATABASE` statement. See " [Specifying Oracle Managed Files at Database Creation](create-cdb-adv.md) " for more information.

See Also:

- " [Managing Initialization Parameters Using a Server Parameter File](create-cdb-adv.md) "
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF01315) for more information on the `CREATE SPILE` command

**Parent topic:** Creating a Database with the CREATE DATABASE Statement

#### Step 8: Start the Database Instance

Start an instance without mounting a CDB.

- Run the `STARTUP` command with the `NOMOUNT` clause.

Typically, you do this only during CDB creation or while performing maintenance on the database. In this example, because the initialization parameter file or server parameter file is stored in the default location, you are not required to specify the `PFILE` clause:

```
STARTUP NOMOUNT
```

At this point, the instance memory is allocated and its processes are started. The CDB itself does not yet exist.

See Also:

- " [Starting Up and Shutting Down a CDB](administering-a-cdb-with-sql-plus.md) " for information about using the `STARTUP` command
- " [Managing Initialization Parameters Using a Server Parameter File](create-cdb-adv.md) "

**Parent topic:** Creating a Database with the CREATE DATABASE Statement

#### Step 9: Issue the CREATE DATABASE Statement

To create the new database, use the `CREATE DATABASE` statement.

- Run the `CREATE DATABASE` statement with the `ENABLE PLUGGABLE DATABASE` clause.

The following topics show sample statements, using Oracle Managed Files and user-specified files.

- Creating a CDB Without Using Oracle Managed Files: Example  
	The following statement creates a CDB named `newcdb`. This name must agree with the `DB_NAME` parameter in the initialization parameter file.
- Creating a CDB Using Oracle Managed Files: Example  
	This example illustrates creating a CDB with Oracle Managed Files, which enables you to use a much simpler `CREATE DATABASE` statement.

**Parent topic:** Creating a Database with the CREATE DATABASE Statement

##### Creating a CDB Without Using Oracle Managed Files: Example

The following statement creates a CDB named `newcdb`. This name must agree with the `DB_NAME` parameter in the initialization parameter file.

Assumptions

This example assumes the following:

- The initialization parameter file specifies the number and location of control files with the `CONTROL_FILES` parameter.
- The `ENABLE_PLUGGABLE_DATABASE` initialization parameter is set to `true`.
- The directory `/u01/app/oracle/oradata/newcdb` exists.
- The directory `/u01/app/oracle/oradata/pdbseed` exists.
- The directories `/u01/logs/my` and `/u02/logs/my` exist.

This example includes the `ENABLE PLUGGABLE DATABASE` clause to create a CDB with the root and the PDB seed. This example also includes the `SEED FILE_NAME_CONVERT` clause to specify the names and locations of the PDB seed's files. This example also includes `tablespace_datafile` clauses that specify attributes of the PDB seed data files for the `SYSTEM` and `SYSAUX` tablespaces that differ from the root data files. This example includes the `undo_mode_clause` to specify that the CDB undo mode is local.

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
    SYSTEM DATAFILES SIZE 125M AUTOEXTEND ON NEXT 10M MAXSIZE UNLIMITED
    SYSAUX DATAFILES SIZE 100M
  USER_DATA TABLESPACE usertbs
    DATAFILE '/u01/app/oracle/oradata/pdbseed/usertbs01.dbf'
    SIZE 200M REUSE AUTOEXTEND ON MAXSIZE UNLIMITED
  LOCAL UNDO ON;
```

A CDB is created with the following characteristics:

- The CDB is named `newcdb`. Its global database name is `newcdb.us.example.com`, where the domain portion (`us.example.com`) is taken from the initialization parameter file. See [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-9698EA9B-013C-40AC-8CFB-12171A4B4974) for information about determining the global database name.
- Three control files are created as specified by the `CONTROL_FILES` initialization parameter, which was set before CDB creation in the initialization parameter file. See [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-4ECB5C59-ED5A-4A87-9EEA-6C687AB8986D) for a sample initialization parameter file and [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-80067DCA-9E48-4232-8D37-667B4A085465) for information about specifying control files.
- The passwords for user accounts `SYS` and `SYSTEM` are set to the values that you specified. The passwords are case-sensitive. The two clauses that specify the passwords for `SYS` and `SYSTEM` are not mandatory in this release of Oracle Database. However, if you specify either clause, then you must specify both clauses. For further information about the use of these clauses, see [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-55208EEE-5B31-4B7F-81A4-AF7AFE8630BE) for information about specifying passwords for users `SYS` and `SYSTEM`.
- The new CDB has three online redo log file groups, each with two members, as specified in the `LOGFILE` clause. `MAXLOGFILES`, `MAXLOGMEMBERS`, and `MAXLOGHISTORY` define limits for the redo log. See [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-11CAAE2C-D46D-4611-8AAB-F9CB941D3934) for information about choosing the number of redo log files. The block size for the redo logs is set to 512 bytes, the same size as physical sectors on disk. The `BLOCKSIZE` clause is optional if block size is to be the same as physical sector size (the default). Typical sector size and thus typical block size is 512. Permissible values for `BLOCKSIZE` are 512, 1024, and 4096. For newer disks with a 4K sector size, optionally specify `BLOCKSIZE` as 4096. See [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-AC858C69-317E-4193-838D-59F8DDEA1927) for more information about planning the block size of redo log files.
- `MAXDATAFILES` specifies the maximum number of data files that can be open in the CDB. This number affects the initial sizing of the control file. For a CDB, set `MAXDATAFILES` to a high number that anticipates the aggregate number of data files for all containers, in addition to the CDB root files.
	Note:
	You can set several limits during CDB creation. Some of these limits are limited by and affected by operating system limits. For example, if you set `MAXDATAFILES`, then Oracle Database allocates enough space in the control file to store `MAXDATAFILES` file names, even if the CDB has only one data file initially. However, because the maximum control file size is limited and operating system dependent, you might not be able to set all `CREATE DATABASE` parameters at their theoretical maximums.
	For more information about setting limits during CDB creation, see the [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF01204) and your operating system–specific Oracle documentation.
- The `AL32UTF8` character set is used to store data in this CDB.
- The `AL16UTF16` character set is specified as the `NATIONAL CHARACTER SET` used to store data in columns specifically defined as `NCHAR`, `NCLOB`, or `NVARCHAR2`.
- The `SYSTEM` tablespace, consisting of the operating system file `/u01/app/oracle/oradata/newcdb/system01.dbf`, is created as specified by the `DATAFILE` clause. If a file with that name already exists, then it is overwritten.
- The `SYSTEM` tablespace is created as a locally managed tablespace. See [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-D8061728-6A13-4F30-AA91-EBE52F276AC3) for information about creating a locally managed `SYSTEM` tablespace.
- A `SYSAUX` tablespace is created, consisting of the operating system file `/u01/app/oracle/oradata/newcdb/sysaux01.dbf` as specified in the `SYSAUX DATAFILE` clause. See [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-C70E0886-7D9A-4B0D-BA0B-DF71AB5A2154) for information about the `SYSAUX` tablespace.
- The `DEFAULT` `TABLESPACE` clause creates and names a default permanent tablespace for this CDB.
- The `DEFAULT TEMPORARY TABLESPACE` clause creates and names a default temporary tablespace for the root of this CDB. See [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-AF2D7962-B165-423B-8FE3-29E7F30A2A3D) for information about creating a default temporary tablespace.
- The `UNDO TABLESPACE` clause creates and names an undo tablespace that is used to store undo data for this CDB. In a CDB, an undo tablespace is required to manage the undo data, and the `UNDO_MANAGEMENT` initialization parameter must be set to `AUTO`. If you omit this parameter, then it defaults to `AUTO`. See [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-BC27AC63-6E76-4C34-A0FE-9C51FFB3487C) for information about creating an undo tablespace.
- Redo log files will not initially be archived, because the `ARCHIVELOG` clause is not specified in this `CREATE DATABASE` statement. This is customary during CDB creation. You can later use an `ALTER DATABASE` statement to switch to `ARCHIVELOG` mode. The initialization parameters in the initialization parameter file for `newcdb` relating to archiving are `LOG_ARCHIVE_DEST_1` and `LOG_ARCHIVE_FORMAT`. See [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-5EE4AC49-E1B2-41A2-BEE7-AA951EAAB2F3) for information about managing archived redo log files.
- The `ENABLE PLUGGABLE DATABASE` clause creates a CDB with the root and the PDB seed.
- `SEED` is required for the `FILE_NAME_CONVERT` clause and the `tablespace_datafile` clauses.
- The `FILE_NAME_CONVERT` clause generates file names for the PDB seed's files in the `/u01/app/oracle/oradata/pdbseed` directory using file names in the `/u01/app/oracle/oradata/newcdb` directory.
- The `SYSTEM DATAFILES` clause specifies attributes of the PDB seed `SYSTEM` tablespace data file(s) that differ from the root's.
- The `SYSAUX DATAFILES` clause specifies attributes of the PDB seed `SYSAUX` tablespace data file(s) that differ from the root's.
- The `USER_DATA TABLESPACE` clause creates and names the PDB seed's tablespace for storing user data and database options such as Oracle XML DB. PDBs created using the PDB seed include this tablespace and its data file. The tablespace and data file specified in this clause are not used by the root.
- The `LOCAL UNDO ON` clause sets the CDB undo mode to local, which means that each container in the CDB uses local undo.
	When the CDB is created in local undo mode, the PDB seed includes an undo tablespace so that any new PDB created from the PDB seed has an undo tablespace. When a PDB is created by plugging it in or cloning a remote PDB, and the source PDB was in shared undo mode, an undo tablespace is created for the PDB automatically the first time the PDB is opened.

Note:

- Ensure that all directories used in the `CREATE DATABASE` statement exist. The `CREATE DATABASE` statement does not create directories.
- If you are not using Oracle Managed Files, then every tablespace clause must include a `DATAFILE` or `TEMPFILE` clause.
- If CDB creation fails, then you can look at the alert log to determine the reason for the failure and to determine corrective actions. See [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-D6512D97-FFC3-4BF0-BF50-1F77D150C922) for information about viewing the alert log. If you receive an error message that contains a process number, then examine the trace file for that process. Look for the trace file that contains the process number in the trace file name. See [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-34137402-19A6-4134-93AE-D6DD02242F61) for more information.
	Tip:
	If your `CREATE DATABASE` statement fails, and if you did not complete Step 7, then ensure that there is not a pre-existing server parameter file (SPFILE) for this database instance that is setting initialization parameters in an unexpected way. For example, an SPFILE contains a setting for the complete path to all control files, and the `CREATE DATABASE` statement fails if those control files do not exist. Ensure that you shut down and restart the instance (with `STARTUP NOMOUNT`) after removing an unwanted SPFILE. See " [Managing Initialization Parameters Using a Server Parameter File](create-cdb-adv.md) " for more information.
- To resubmit the `CREATE DATABASE` statement after a failure, you must first shut down the instance and delete any files created by the previous `CREATE DATABASE` statement.

**Parent topic:** Step 9: Issue the CREATE DATABASE Statement

##### Creating a CDB Using Oracle Managed Files: Example

This example illustrates creating a CDB with Oracle Managed Files, which enables you to use a much simpler `CREATE DATABASE` statement.

To use Oracle Managed Files, the initialization parameter `DB_CREATE_FILE_DEST` must be set. This parameter defines the base directory for the various CDB files that the CDB creates and automatically names.

The following statement is an example of setting this parameter in the initialization parameter file:

```
DB_CREATE_FILE_DEST='/u01/app/oracle/oradata'
```

This example sets the parameter Oracle ASM storage:

```
DB_CREATE_FILE_DEST = +data
```

This example does not include the `SEED FILE_NAME_CONVERT` clause because Oracle Managed Files determines the names and locations of the PDB seed's files. However, this example does include `tablespace_datafile` clauses that specify attributes of the PDB seed data files for the `SYSTEM` and `SYSAUX` tablespaces that differ from the CDB root data files.

With Oracle Managed Files and the following `CREATE DATABASE` statement, the CDB creates the `SYSTEM` and `SYSAUX` tablespaces, creates the additional tablespaces specified in the statement, and chooses default sizes and properties for all data files, control files, and redo log files. Note that these properties and the other default CDB properties set by this method might not be suitable for your production environment, so Oracle recommends that you examine the resulting configuration and modify it if necessary.

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

- The CDB is named `newcdb`. Its global database name is `newcdb.us.example.com`, where the domain portion (`us.example.com`) is taken from the initialization parameter file. See [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-9698EA9B-013C-40AC-8CFB-12171A4B4974) for information about determining the global database name.
- The passwords for user accounts `SYS` and `SYSTEM` are set to the values that you specified. The passwords are case-sensitive. The two clauses that specify the passwords for `SYS` and `SYSTEM` are not mandatory in this release of Oracle Database. However, if you specify either clause, then you must specify both clauses. For further information about the use of these clauses, see [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-55208EEE-5B31-4B7F-81A4-AF7AFE8630BE) for information about specifying passwords for users `SYS` and `SYSTEM`.
- The `DEFAULT TABLESPACE` clause creates and names a default permanent tablespace for this CDB.
- The `DEFAULT TEMPORARY TABLESPACE` clause creates and names a default temporary tablespace for the root of this CDB. See [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-AF2D7962-B165-423B-8FE3-29E7F30A2A3D) for information about creating a default temporary tablespace.
- The `UNDO TABLESPACE` clause creates and names an undo tablespace that is used to store undo data for this CDB. In a CDB, an undo tablespace is required to manage the undo data, and the `UNDO_MANAGEMENT` initialization parameter must be set to `AUTO`. If you omit this parameter, then it defaults to `AUTO`. See [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-BC27AC63-6E76-4C34-A0FE-9C51FFB3487C) for information about creating an undo tablespace.
- Redo log files will not initially be archived, because the `ARCHIVELOG` clause is not specified in this `CREATE DATABASE` statement. This is customary during CDB creation. You can later use an `ALTER DATABASE` statement to switch to `ARCHIVELOG` mode. The initialization parameters in the initialization parameter file for `newcdb` relating to archiving are `LOG_ARCHIVE_DEST_1` and `LOG_ARCHIVE_FORMAT`. See [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-5EE4AC49-E1B2-41A2-BEE7-AA951EAAB2F3) for information about managing archived redo log files.
- The `ENABLE PLUGGABLE DATABASE SEED` clause is required for the `tablespace_datafile` clauses.
	Note:
	If you do not specify the `SYSTEM` and `SYSAUX` clauses, which are optional, then the `ENABLE PLUGGABLE DATABASE SEED` clause is not required.
- The `SYSTEM DATAFILES` clause specifies attributes of the PDB seed's `SYSTEM` tablespace data files that differ from the root's.
- The `SYSAUX DATAFILES` clause specifies attributes of the PDB seed's `SYSAUX` tablespace data files that differ from the root's.

**Parent topic:** Step 9: Issue the CREATE DATABASE Statement

#### Step 10: Run Scripts to Build Data Dictionary Views

Run the scripts necessary to build data dictionary views, synonyms, and PL/SQL packages in the CDB root.

Perform these actions by running the supplied `catcdb.sql` script, which installs all components required by a CDB. The at-sign (`@`) is shorthand for the command that runs a SQL\*Plus script. The question mark (`?`) is a SQL\*Plus variable indicating the Oracle home directory.

1. Run the `catcdb.sql` SQL script.
	Enter the following in SQL\*Plus to run the script:
	```
	@?/rdbms/admin/catcdb.sql
	```
2. When prompted by the script, enter the log file directory for parameter `1` and the log file name for parameter `2`.
	For following example enters `/tmp` for the first prompt and `create_cdb.log` for the second prompt:
	```
	SQL> host perl -I &&rdbms_admin &&rdbms_admin_catcdb --logDirectory &&1 --logFilename &&2
	Enter value for 1: /tmp
	Enter value for 2: create_cdb.log
	```
3. When prompted by the script, enter any other required information.
	For example, the scripts prompts for administrator passwords and the temporary tablespace name:
	```
	Enter new password for SYS: ********
	Enter new password for SYSTEM: ********
	Enter temporary tablespace name: TEMP
	```

**Parent topic:** Creating a Database with the CREATE DATABASE Statement

#### Step 11: (Optional) Run Scripts to Install Additional Options

You may want to run other scripts. The scripts that you run are determined by the features and options you choose to use or install.

- Run scripts to install additional options.

Many of the scripts available to you are described in the [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=REFRN005).

If you plan to install other Oracle products to work with this database, then see the installation instructions for those products. Some products require you to create additional data dictionary tables. Usually, command files are provided to create and load these tables into the database data dictionary.

See your Oracle documentation for the specific products that you plan to install for installation and administration instructions.

**Parent topic:** Creating a Database with the CREATE DATABASE Statement

#### Step 12: Back Up the Database

Take a full backup of the database to ensure that you have a complete set of files from which to recover if a media failure occurs.

- Back up the CDB.

For information on backing up a CDB, see [Oracle Database Backup and Recovery User’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=BRADV-GUID-008E0F84-E623-4467-8706-A99B34002DD6).

**Parent topic:** Creating a Database with the CREATE DATABASE Statement

#### Step 13: (Optional) Enable Automatic Instance Startup

You might want to configure the Oracle database instance to start automatically when its host computer restarts.

- Configure the Oracle instance to start automatically when its host computer restarts.

See your operating system documentation for instructions. For example, on Windows, use the following command to configure the database service to start the instance upon computer restart:

```
ORADIM -EDIT -SID sid -STARTMODE AUTO -SRVCSTART SYSTEM [-SPFILE]
```

You must use the `-SPFILE` argument if you want the instance to read an SPFILE upon automatic restart.

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-5832E064-85C6-453C-B932-99700B1732A9) to learn more about Oracle Restart
- [Oracle Database Platform Guide for Microsoft Windows](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=NTQRF05011) for more information on the `ORADIM` command.

**Parent topic:** Creating a Database with the CREATE DATABASE Statement

### Considerations After Creating a CDB

After you create a CDB, the instance is left running, and the database is open and available for normal database use. You may want to perform specific actions after creating a database.

- Database Security  
	You can use the default Oracle Database features to configure security in several areas for your Oracle database.
- Transparent Data Encryption  
	Transparent Data Encryption enables encryption of database columns before storing them in the data file, or enables encryption of entire tablespaces.
- A Secure External Password Store  
	Consider using client-side Oracle wallets to reduce exposing authentication and signing credentials over networks.
- Transaction Guard and Application Continuity  
	Transaction Guard uses a logical transaction ID to prevent the possibility of a client application submitting duplicate transactions after a recoverable error. Application Continuity enables the replay, in a nondisruptive and rapid manner, of a request against the database after a recoverable error that makes the database session unavailable.
- File System Server Support in the Database  
	An Oracle database can be configured to store file system objects and access them from any NFS client. The database stores both the files and their metadata. The database responds to file system requests from the NFS daemon process in the operating system (OS) kernel.
- The Oracle Database Sample Schemas  
	Oracle Database includes sample schemas that help you to become familiar with Oracle Database functionality. Some Oracle Database documentation and training materials use the sample schemas in examples.

**Parent topic:** Creating a CDB: Basic Steps

#### Database Security

You can use the default Oracle Database features to configure security in several areas for your Oracle database.

The following are some of the areas in which you can configure security for your database:

- User accounts: When you create user accounts, you can secure them in a variety of ways. You can also create password profiles to better secure password policies for your site.
- Authentication methods: Oracle Database provides several ways to configure authentication for users and database administrators. For example, you can authenticate users on the database level, from the operating system, and on the network.
- Privileges and roles: You can use privileges and roles to restrict user access to data.

Note:

- A newly created database has at least three user accounts that are important for administering your database: `SYS`, `SYSTEM`, and `SYSMAN`. Additional administrative accounts are provided that should be used only by authorized users.
- To prevent unauthorized access and protect the integrity of your database, it is important that a new password is specified to the `SYS` user when the database is created.
- Most Oracle Database supplied user accounts, except `SYS` and sample schemas are schema only accounts, that is, these accounts are created without passwords. You can assign passwords to these accounts whenever you want them to be authenticated, but Oracle recommends that for better security, you should change these accounts back to schema only accounts, when you do not need to authenticate them anymore.
	To find the status of an account, query the `ACCOUNT_STATUS` column of the `DBA_USERS` data dictionary view. If the account is schema only, then the status is `NONE`.

See Also:

- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=DBSEG-GUID-B8EF08C7-28E5-492D-A300-C5B1866FDCC8) for a complete list of predefined user accounts created with each new Oracle Database installation
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=DBSEG002) to learn how to add new users and change passwords
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF01103) for the syntax of the `ALTER USER` statement used for unlocking database user accounts
- [Oracle Database Enterprise User Security Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=DBIMI203) for information about Oracle Identity Management
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=DBSEG009) for security guidelines for configuring a database

**Parent topic:** Considerations After Creating a CDB

#### Transparent Data Encryption

Transparent Data Encryption enables encryption of database columns before storing them in the data file, or enables encryption of entire tablespaces.

If users attempt to circumvent the database access control mechanisms by looking inside data files directly with operating system tools, Transparent Data Encryption prevents such users from viewing sensitive information.

Users who have the `CREATE TABLE` privilege can choose one or more columns in a table to be encrypted. The data is encrypted in the data files. Database users with appropriate privileges can view the data in unencrypted format.

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-F9D38568-4F95-4053-B21F-F318077C29E5) to learn about encrypting columns
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-996E01D0-3679-45FE-BEBB-CE941B6989DB) to learn about encrypted tablespaces
- [Oracle Database Advanced Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ASOAG600) to learn more about Transparent Data Encryption

**Parent topic:** Considerations After Creating a CDB

#### A Secure External Password Store

Consider using client-side Oracle wallets to reduce exposing authentication and signing credentials over networks.

For large-scale deployments where applications use password credentials to connect to databases, it is possible to store such credentials in a client-side Oracle wallet. An Oracle wallet is a secure software container that is used to store authentication and signing credentials.

Storing database password credentials in a client-side Oracle wallet eliminates the need to embed usernames and passwords in application code, batch jobs, or scripts. Client-side storage reduces the risk of exposing passwords in the clear in scripts and application code. It also simplifies maintenance, because you need not change your code each time usernames and passwords change. In addition, not having to change application code also makes it easier to enforce password management policies for these user accounts.

When you configure a client to use the external password store, applications can use the following syntax to connect to databases that use password authentication:

```
CONNECT /@database_alias
```

You need not specify database login credentials in this `CONNECT` command. Instead your system looks for database login credentials in the client wallet.

See Also:

- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=DBSEG99815)
- [Oracle Database Enterprise User Security Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=DBIMI160)

**Parent topic:** Considerations After Creating a CDB

#### Transaction Guard and Application Continuity

Transaction Guard uses a logical transaction ID to prevent the possibility of a client application submitting duplicate transactions after a recoverable error. Application Continuity enables the replay, in a nondisruptive and rapid manner, of a request against the database after a recoverable error that makes the database session unavailable.

Transaction Guard is a reliable protocol and API that application developers can use to provide a known outcome for the last open transaction on a database session that becomes unavailable. After an outage, the commit message that is sent from the database to the client is not durable. If the connection breaks between an application (the client) and an Oracle database (the server), then the client receives an error message indicating that the communication failed. This error message does not inform the client about the success or failure of commit operations or procedure calls.

Transaction Guard uses a concept called the logical transaction identifier (LTXID), a globally unique identifier that identifies the transaction from the application's perspective. When a recoverable outage occurs, the application uses the LTXID to determine the outcome of the transaction. This outcome can be returned to the client instead of the ambiguous communication error. The user can decide whether to resubmit the transaction. The application also can be coded to resubmit the transaction if the states are correct.

Application Continuity masks outages from end users and applications by recovering the in-flight database sessions following recoverable outages, for both unplanned and planned outages. After a successful replay, the application can continue using a new session where the original database session left off. Application Continuity performs this recovery so that the outage appears to the application as a delayed execution.

Application Continuity is enabled at the service level and is invoked for outages that are recoverable. These outages typically are related to underlying software, foreground, hardware, communications, network, or storage layers. Application Continuity supports queries, `ALTER SESSION` statements, Java and OCI APIs, PL/SQL, DDL, and the last uncommitted transaction before the failure. Application Continuity determines whether the last in-flight transaction committed or not, and whether the last user call completed or not, using Transaction Guard.

See Also:

- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=CNCPT89217) for a conceptual overview of Transaction Guard and Application Continuity
- [Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADFNS8000) for complete information about Transaction Guard and Application Continuity

**Parent topic:** Considerations After Creating a CDB

#### File System Server Support in the Database

An Oracle database can be configured to store file system objects and access them from any NFS client. The database stores both the files and their metadata. The database responds to file system requests from the NFS daemon process in the operating system (OS) kernel.

When you configure the Oracle File System (OFS) server in a database and create a file system, you can store unstructured data, such as emails, videos, audio files, credit card bills, documents, photo images, and so on, inside the database. You can manipulate and manage these unstructured objects without using SQL. Instead, you can use operating system utilities for NFS support.

To enable NFS access in the database, set the `OFS_THREADS` initialization parameter to configure a sufficient number of OFS threads to process the NFS requests. The `OFS_THREADS` initialization parameter controls the number of OFS threads to create when the first file system is mounted with the database. The number of threads specified by the `OFS_THREADS` parameter are created only once for the database instance and subsequent file systems do not create any additional threads. The default value of the `OFS_THREADS` initialization parameter is 4. At database startup, OFSD background process is the sole OFS process that is spawned by the database server.

You can use the `DBMS_FS` package to create a file system in the database using a specified database object. You can also use this package to mount and unmount a specified file system.

See Also:

- [Oracle Database SecureFiles and Large Objects Developer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADLOB-GUID-5613B15C-9976-4148-A167-4C279E28372D) for more information about the Oracle File System (OFS)
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ARPLS-GUID-F21D6EF9-F8CA-403B-95A5-ED081951C51D) for more information about the `DBMS_FS` package

**Parent topic:** Considerations After Creating a CDB

#### The Oracle Database Sample Schemas

Oracle Database includes sample schemas that help you to become familiar with Oracle Database functionality. Some Oracle Database documentation and training materials use the sample schemas in examples.

The schemas and installation instructions are described in detail in [Oracle Database Sample Schemas](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=COMSC-GUID-A2C3DC59-CDA1-47C0-BA6B-F6EA6395A85F).

Note:

Oracle strongly recommends that you do not install the sample schemas in a production database.

**Parent topic:** Considerations After Creating a CDB

### Database Data Dictionary Views

You can query data dictionary views for information about your database content and structure.

You can view information about your database content and structure using the following views:

| View | Description |
| --- | --- |
| `DATABASE_PROPERTIES` | Displays permanent database properties |
| `GLOBAL_NAME` | Displays the global database name |
| `V$DATABASE` | Contains database information from the control file |

**Parent topic:** Creating a CDB: Basic Steps