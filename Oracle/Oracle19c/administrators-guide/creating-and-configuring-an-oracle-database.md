---
title: "Database Administrator’s Guide"
book: "Database Administrator's Guide"
doc_id: E96348-21
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/admin/creating-and-configuring-an-oracle-database.html
tags:
  - oracle
  - 19c
  - administrators-guide
---

## 2 Creating and Configuring an Oracle Database

After you plan your database, you can create the database with a graphical tool or a SQL command.

- About Creating an Oracle Database  
	You typically create a database during Oracle Database software installation. However, you can also create a database after installation.
- Considerations Before Creating the Database  
	Database creation prepares several operating system files to work together as an Oracle Database. You only need to create a database once, regardless of how many data files it has or how many instances access it. You can create a database to erase information in an existing database and create a new database with the same name and physical structure.
- Creating a Database with DBCA  
	Oracle Database Configuration Assistant (DBCA) is a tool for creating and configuring an Oracle database.
- Creating a Database with the CREATE DATABASE Statement  
	Using the `CREATE` `DATABASE` SQL statement is a more manual approach to creating a database than using Oracle Database Configuration Assistant (DBCA). One advantage of using this statement over using DBCA is that you can create databases from within scripts.
- Specifying CREATE DATABASE Statement Clauses  
	When you execute a `CREATE` `DATABASE` statement, Oracle Database performs several operations. The actual operations performed depend on the clauses that you specify in the `CREATE` `DATABASE` statement and the initialization parameters that you have set.
- Specifying Initialization Parameters  
	You can add or edit basic initialization parameters before you create your new database.
- Managing Initialization Parameters Using a Server Parameter File  
	Initialization parameters for the Oracle Database have traditionally been stored in a text initialization parameter file. For better manageability, you can choose to maintain initialization parameters in a binary server parameter file that is persistent across database startup and shutdown.
- Managing Application Workloads with Database Services  
	A database service is a named representation of one or more database instances. Services enable you to group database workloads and route a particular work request to an appropriate instance.
- Managing Standard Edition High Availability for Oracle Databases  
	The Standard Edition High Availability feature provides protection against unplanned outages for Oracle Database Standard Edition 2 single instance databases using Oracle Clusterware.
- Considerations After Creating a Database  
	After you create a database the instance is left running, and the database is open and available for normal database use. You may want to perform specific actions after creating a database.
- Cloning a Database  
	This section describes various methods of cloning an Oracle database.
- Dropping a Database  
	Dropping a database involves removing its data files, online redo logs, control files, and initialization parameter files.
- Database Data Dictionary Views  
	You can query data dictionary views for information about your database content and structure.
- Database Configuration Assistant Command Reference for Silent Mode  
	This section provides detailed information about the syntax and options for the Database Configuration Assistant (DBCA) silent mode commands.

See Also:

- [Using Oracle Managed Files](using-oracle-managed-files.md) for information about creating a database whose underlying operating system files are automatically created and managed by the Oracle Database server
- Your platform-specific Oracle Real Application Clusters (Oracle RAC) installation guide for information about creating a database in an Oracle RAC environment
- [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=CWADD-GUID-CCEC5960-EDA4-4A3F-9643-0CA308EA49AA) for information on creating a database using Fleet Patching and Provisioning (it was called as Rapid Home Provisioning in the earlier database releases)

**Parent topic:** [Basic Database Administration](basic-database-administration.md)

### 2.1 About Creating an Oracle Database

You typically create a database during Oracle Database software installation. However, you can also create a database after installation.

Reasons to create a database after installation are as follows:

- You used Oracle Universal Installer (OUI) to install software only, and did not create a database.
- You want to create another database (and database instance) on the same host computer as an existing Oracle database. In this case, this chapter assumes that the new database uses the same Oracle home as the existing database. You can also create the database in a new Oracle home by running OUI again.
- You want to make a copy of (clone) a database.

The specific methods for creating a database are:

- With Database Configuration Assistant (DBCA), a graphical tool.
	See " Creating a Database with DBCA "
- With the `CREATE` `DATABASE` SQL statement.
	See " Creating a Database with the CREATE DATABASE Statement "

**Parent topic:** Creating and Configuring an Oracle Database

### 2.2 Considerations Before Creating the Database

Database creation prepares several operating system files to work together as an Oracle Database. You only need to create a database once, regardless of how many data files it has or how many instances access it. You can create a database to erase information in an existing database and create a new database with the same name and physical structure.

**Parent topic:** Creating and Configuring an Oracle Database

#### 2.2.1 Planning for Database Creation

Prepare to create the database by research and careful planning.

Table 2-1 lists some recommended actions:

Table 2-1 Database Planning Tasks

| Action | Additional Information |
| --- | --- |
| Plan the database tables and indexes and estimate the amount of space they will require. | [Oracle Database Structure and Storage](oracle-database-structure-and-storage.md)  [Schema Objects](schema-objects.md) |
| Plan the layout of the underlying operating system files your database will comprise. Proper distribution of files can improve database performance dramatically by distributing the I/O during file access. You can distribute I/O in several ways when you install Oracle software and create your database. For example, you can place redo log files on separate disks or use striping. You can situate data files to reduce contention. And you can control data density (number of rows to a data block). If you create a Fast Recovery Area, Oracle recommends that you place it on a storage device that is different from that of the data files.  To greatly simplify this planning task, consider using Oracle Managed Files and Automatic Storage Management to create and manage the operating system files that comprise your database storage. | [Using Oracle Managed Files](using-oracle-managed-files.md)  [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=OSTMG)  [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=TGDBA015)  Your Oracle operating system–specific documentation, including the appropriate Oracle Database installation guide. |
| Select the global database name, which is the name and location of the database within the network structure. Create the global database name by setting both the `DB_NAME ` and `DB_DOMAIN` initialization parameters. | " Determining the Global Database Name " |
| Familiarize yourself with the initialization parameters contained in the initialization parameter file. Become familiar with the concept and operation of a server parameter file. A server parameter file lets you store and manage your initialization parameters persistently in a server-side disk file. | " About Initialization Parameters and Initialization Parameter Files "  " What Is a Server Parameter File?"  [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=REFRN001) |
| Select the database character set.  All character data, including data in the data dictionary, is stored in the database character set. You specify the database character set when you create the database.  See " About Selecting a Character Set " for details. | [Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=NLSPG002) |
| Consider which time zones your database must support.  Oracle Database uses one of two time zone files as the source of valid time zones. The default time zone file is `timezlrg_11.dat`. It contains more time zones than the smaller time zone file, `timezone_11.dat`. | " Specifying the Database Time Zone File " |
| Select the standard database block size. This is specified at database creation by the `DB_BLOCK_SIZE` initialization parameter and cannot be changed after the database is created.  The `SYSTEM` tablespace and most other tablespaces use the standard block size. Additionally, you can specify up to four nonstandard block sizes when creating tablespaces. | " Specifying Database Block Sizes " |
| If you plan to store online redo log files on disks with a 4K byte sector size, determine whether you must manually specify redo log block size. | " [Planning the Block Size of Redo Log Files](managing-the-redo-log.md) " |
| Determine the appropriate initial sizing for the `SYSAUX` tablespace. | " About the SYSAUX Tablespace " |
| Plan to use a default tablespace for non- `SYSTEM` users to prevent inadvertently saving database objects in the `SYSTEM` tablespace. | " Creating a Default Permanent Tablespace " |
| Plan to use an undo tablespace to manage your undo data. | [Managing Undo](managing-undo.md) |
| Consider whether you want to configure a read-only Oracle home or a read-write Oracle home for your database. | About Configuring an Oracle Home in Read-Only Mode |
| Develop a backup and recovery strategy to protect the database from failure. It is important to protect the control file by multiplexing, to choose the appropriate backup mode, and to manage the online redo log and archived redo log files. | [Managing the Redo Log](managing-the-redo-log.md)  [Managing Archived Redo Log Files](managing-archived-redo-log-files.md)  [Managing Control Files](managing-control-files.md)  [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=BRADV) |
| Familiarize yourself with the principles and options of starting up and shutting down an instance and mounting and opening a database. | [Starting Up and Shutting Down](starting-up-and-shutting-down.md) |

**Parent topic:** Considerations Before Creating the Database

#### 2.2.2 About Selecting a Character Set

It is important to select the right character set for your database. Oracle recommends AL32UTF8 as the database character set.

AL32UTF8 is Oracle's name for the UTF-8 encoding of the Unicode standard. The Unicode standard is the universal character set that supports most of the currently spoken languages of the world. The use of the Unicode standard is indispensable for any multilingual technology, including database processing.

After a database is created and accumulates production data, changing the database character set is a time consuming and complex project. Therefore, it is very important to select the right character set at installation time. Even if the database does not currently store multilingual data but is expected to store multilingual data within a few years, the choice of AL32UTF8 for the database character set is usually the only good decision. The universality and flexibility of Unicode typically outweighs some additional cost associated with it, such as slightly slower text processing compared to single-byte character sets and higher storage space requirements for non-ASCII text compared to non-Unicode character sets.

If you do not want to use AL32UTF8, and you are not restricted in your choice by a vendor requirement, then Oracle suggests that you use one of the character sets listed as recommended for the database. The recommended character sets were selected based on the requirements of modern client operating systems. Oracle Universal Installer (OUI) presents the recommended list only, and Database Configuration Assistant (DBCA) must be used separately to choose a non-recommended character set. In addition, the default database creation configuration in DBCA allows the selection of the recommended character sets only. You must use the advanced configuration mode of DBCA or the `CREATE DATABASE` statement to select a non-recommended character set.

If no character set choice is presented in an OUI or a DBCA installation mode, then AL32UTF8 is used as the database character set, unless a custom database template with another character set has been selected.

Note:

- Oracle recommends using AL32UTF8 as the database character set. AL32UTF8 is the proper implementation of the Unicode encoding UTF-8. Starting with Oracle Database 12c Release 2, AL32UTF8 is used as the default database character set while creating a database using Oracle Universal Installer (OUI) as well as Oracle Database Configuration Assistant (DBCA).
- You can only select an ASCII-based character set for the database on an ASCII-based platform.

Caution:

Do not use UTF8 as the database character set unless required for compatibility with Oracle Database clients and servers in Oracle8i Release 1 (8.1.7) and earlier, or unless explicitly requested by your application vendor. Despite having a very similar name, UTF8 is not a proper implementation of the Unicode encoding UTF-8. If the UTF8 character set is used where UTF-8 processing is expected, data loss and security issues may occur. This is especially true for Web related data, such as XML and URL addresses.

AL32UTF8 and UTF8 character sets are not compatible with each other as they have different maximum character widths. AL32UTF8 has a maximum character width of 4 bytes, whereas UTF8 has a maximum character width of 3 bytes.

#### 2.2.3 About Configuring an Oracle Home in Read-Only Mode

Starting with Oracle Database 18c, you can simplify patching and mass rollouts of software across multiple database servers by deploying a read-only Oracle home as a software image.

A read-only Oracle home (`ORACLE_HOME`) prevents both creation and modification of files inside the Oracle home directory. To configure an Oracle home in read-only mode, you first install Oracle Database software using a software-only deployment, and then configure it as a read-only Oracle home before you create the listener and the database.

Traditional read-write Oracle homes contain instance-specific files, so if you patch them, then you must patch each of them individually. However, when the Oracle home is read-only, instance-specific files are stored separately in the Oracle base directory (`ORACLE_BASE`), instead of the Oracle home. Because of this configuration, you can use a read-only Oracle home as a software image that you can share across multiple database servers, because it stores only the static files. This option simplifies patching and mass rollout, because when you want to distribute a patch to multiple database servers, you only need to update one Oracle home image.

Apart from the traditional `ORACLE_BASE` and `ORACLE_HOME` directories, the following additional directories exist in a read-only Oracle home:

- `ORACLE_BASE_HOME`: This is a subdirectory within the `ORACLE_BASE` directory. This directory contains user-specific files, instance-specific files, and log files.
- `ORACLE_BASE_CONFIG`: This directory is same as the `ORACLE_BASE` directory. This directory contains instance-specific dynamic files, such as configuration files.

See Also:

“Configuring Read-Only Oracle Homes” in the Oracle Database installation guide specific to your platform for more information about configuring an Oracle home in read-only mode.

**Parent topic:** Considerations Before Creating the Database

#### 2.2.4 Prerequisites for Database Creation

To ensure that your Oracle Database is created successfully, review database prerequisites.

Before you can create a new database, the following prerequisites must be met:

- The desired Oracle software must be installed. This includes setting various environment variables unique to your operating system and establishing the directory structure for software and database files.
- Sufficient memory must be available to start the Oracle Database instance.
- Sufficient disk storage space must be available for the planned database on the computer that runs Oracle Database.

All of these are discussed in the [Oracle Database Installation Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=GINST) specific to your operating system. If you use the Oracle Universal Installer, it will guide you through your installation and provide help in setting environment variables and establishing directory structure and authorizations.

**Parent topic:** Considerations Before Creating the Database

### 2.3 Creating a Database with DBCA

Oracle Database Configuration Assistant (DBCA) is a tool for creating and configuring an Oracle database.

- About Creating a Database with DBCA  
	Oracle strongly recommends using the Database Configuration Assistant (DBCA) to create a database, because it is a more automated approach, and your database is ready to use when DBCA completes.
- About Creating a Database with Interactive DBCA  
	The easiest way to create a database is with Database Configuration Assistant (DBCA).
- About Creating a Database with Noninteractive/Silent DBCA  
	You can create a database using the noninteractive/silent mode of Database Configuration Assistant (DBCA).

**Parent topic:** Creating and Configuring an Oracle Database

#### 2.3.1 About Creating a Database with DBCA

Oracle strongly recommends using the Database Configuration Assistant (DBCA) to create a database, because it is a more automated approach, and your database is ready to use when DBCA completes.

DBCA can be launched by the Oracle Universal Installer (OUI), depending upon the type of install that you select. You can also launch DBCA as a standalone tool at any time after Oracle Database installation.

You can run DBCA in interactive mode or noninteractive/silent mode. Interactive mode provides a graphical interface and guided workflow for creating and configuring a database. Noninteractive/silent mode enables you to script database creation. You can run DBCA in noninteractive/silent mode by specifying command-line arguments, a response file, or both.

**Parent topic:** Creating a Database with DBCA

#### 2.3.2 About Creating a Database with Interactive DBCA

The easiest way to create a database is with Database Configuration Assistant (DBCA).

See [Oracle Database 2 Day DBA](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=ADMQS002) for detailed information about creating a database interactively with DBCA.

**Parent topic:** Creating a Database with DBCA

#### 2.3.3 About Creating a Database with Noninteractive/Silent DBCA

You can create a database using the noninteractive/silent mode of Database Configuration Assistant (DBCA).

**Parent topic:** Creating a Database with DBCA

### 2.4 Creating a Database with the CREATE DATABASE Statement

Using the `CREATE` `DATABASE` SQL statement is a more manual approach to creating a database than using Oracle Database Configuration Assistant (DBCA). One advantage of using this statement over using DBCA is that you can create databases from within scripts.

- About Creating a Database with the CREATE DATABASE Statement  
	When you use the `CREATE DATABASE` statement, you must complete additional actions before you have an operational database. These actions include building views on the data dictionary tables and installing standard PL/SQL packages. You perform these actions by running the supplied scripts.
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
- Step 9: Issue the CREATE DATABASE Statement  
	To create the new database, use the `CREATE` `DATABASE` statement.
- Step 10: Create Additional Tablespaces  
	To make the database functional, you must create additional tablespaces for your application data.
- Step 11: Run Scripts to Build Data Dictionary Views  
	Run the scripts necessary to build data dictionary views, synonyms, and PL/SQL packages, and to support proper functioning of SQL\*Plus.
- Step 12: (Optional) Run Scripts to Install Additional Options  
	You may want to run other scripts. The scripts that you run are determined by the features and options you choose to use or install.
- Step 13: Run Datapatch  
	Run Datapatch to update information stored in the database to the correct patch level.
- Step 14: Back Up the Database  
	Take a full backup of the database to ensure that you have a complete set of files from which to recover if a media failure occurs.
- Step 15: (Optional) Enable Automatic Instance Startup  
	You might want to configure the Oracle instance to start automatically when its host computer restarts.

**Parent topic:** Creating and Configuring an Oracle Database

#### 2.4.1 About Creating a Database with the CREATE DATABASE Statement

When you use the `CREATE DATABASE` statement, you must complete additional actions before you have an operational database. These actions include building views on the data dictionary tables and installing standard PL/SQL packages. You perform these actions by running the supplied scripts.

If you have existing scripts for creating your database, then consider editing those scripts to take advantage of new Oracle Database features.

The instructions in this section apply to single-instance installations only. See the Oracle Real Application Clusters (Oracle RAC) installation guide for your platform for instructions for creating an Oracle RAC database.

Note:

- Single-instance does not mean that only one Oracle instance can reside on a single host computer. In fact, multiple Oracle instances (and their associated databases) can run on a single host computer. A single-instance database is a database that is accessed by only one Oracle instance at a time, as opposed to an Oracle RAC database, which is accessed concurrently by multiple Oracle instances on multiple nodes.
- Starting in Oracle Database 12c Release 2 (12.2), read-only and read/write instances can coexist within a single Oracle RAC database. This configuration is useful for the scalability of parallel queries.

Tip:

If you are using Oracle Automatic Storage Management (Oracle ASM) to manage your disk storage, then you must start the Oracle ASM instance and configure your disk groups before performing these steps. See [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=OSTMG-GUID-74C67180-6F24-4F50-8581-0DF71F1C5B47).

See Also:

- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=RACAD) for more information on Oracle RAC
- [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=CWADD) for information about configuring read-only and read/write instances that coexist within a single Oracle RAC database

**Parent topic:** Creating a Database with the CREATE DATABASE Statement

#### 2.4.2 Step 1: Specify an Instance Identifier (SID)

The `ORACLE_SID` environment variable is used to distinguish this instance from other Oracle Database instances that you may create later and run concurrently on the same host computer.

1. Decide on a unique Oracle system identifier (SID) for your instance.
2. Open a command window.
	Note:
	Use this command window for the subsequent steps.
3. Set the `ORACLE_SID` environment variable.

Restrictions related to the valid characters in an `ORACLE_SID` are platform-specific. On some platforms, the SID is case-sensitive.

Note:

It is common practice to set the SID to be equal to the database name. The maximum number of characters for the database name is eight. For more information, see the discussion of the `DB_NAME` initialization parameter in [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=REFRN10041).

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

[Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=CNCPT601) for background information about the Oracle instance

**Parent topic:** Creating a Database with the CREATE DATABASE Statement

#### 2.4.3 Step 2: Ensure That the Required Environment Variables Are Set

Depending on your platform, before you can start SQL\*Plus (as required in a later step), you may have to set environment variables, or at least verify that they are set properly.

- Set required environment variables.

For example, on most platforms, `ORACLE_SID` and `ORACLE_HOME` must be set. In addition, it is advisable to set the `PATH` variable to include the ORACLE\_HOME/bin directory. On the UNIX and Linux platforms, you must set these environment variables manually. On the Windows platform, OUI automatically assigns values to `ORACLE_HOME` and `ORACLE_SID` in the Windows registry. If you did not create a database upon installation, OUI does not set `ORACLE_SID` in the registry, and you will have to set the `ORACLE_SID` environment variable when you create your database later.

**Parent topic:** Creating a Database with the CREATE DATABASE Statement

#### 2.4.4 Step 3: Choose a Database Administrator Authentication Method

You must be authenticated and granted appropriate system privileges in order to create a database.

- Decide on an authentication method.

You can be authenticated as an administrator with the required privileges in the following ways:

- With a password file
- With operating system authentication

To be authenticated with a password file, create the password file as described in " [Creating and Maintaining a Database Password File](getting-started-with-database-administration.md) ". To be authenticated with operating system authentication, ensure that you log in to the host computer with a user account that is a member of the appropriate operating system user group. On the UNIX and Linux platforms, for example, this is typically the `dba` user group. On the Windows platform, the user installing the Oracle software is automatically placed in the required user group.

See Also:

- " [About Database Administrator Security and Privileges](getting-started-with-database-administration.md) "
- " [Database Administrator Authentication](getting-started-with-database-administration.md) " for information about password files and operating system authentication

**Parent topic:** Creating a Database with the CREATE DATABASE Statement

#### 2.4.5 Step 4: Create the Initialization Parameter File

When an Oracle instance starts, it reads an initialization parameter file. This file can be a text file, which can be created and modified with a text editor, or a binary file, which is created and dynamically modified by the database. The binary file, which is preferred, is called a server parameter file. In this step, you create a text initialization parameter file. In a later step, you create a server parameter file from the text file.

- Create the initialization parameter file.

One way to create the text initialization parameter file is to edit the sample presented in " Sample Initialization Parameter File ".

If you create the initialization parameter file manually, ensure that it contains at least the parameters listed in Table 2-2. All other parameters not listed have default values.

Table 2-2 Recommended Minimum Initialization Parameters

| Parameter Name | Mandatory | Notes |
| --- | --- | --- |
| `DB_NAME` | Yes | Database identifier. Must correspond to the value used in the `CREATE` `DATABASE` statement. Maximum 8 characters. |
| `CONTROL_FILES` | No | Strongly recommended. If not provided, then the database instance creates one control file in the same location as the initialization parameter file. Providing this parameter enables you to multiplex control files. See " [Creating Initial Control Files](managing-control-files.md) " for more information. |
| `MEMORY_TARGET` | No | Sets the total amount of memory used by the instance and enables automatic memory management. You can choose other initialization parameters instead of this one for more manual control of memory usage. See " [Configuring Memory Manually](managing-memory.md) ". |

For convenience, store your initialization parameter file in the Oracle Database default location, using the default file name. Then when you start your database, it will not be necessary to specify the `PFILE` clause of the `STARTUP` command, because Oracle Database automatically looks in the default location for the initialization parameter file.

For more information about initialization parameters and the initialization parameter file, including the default name and location of the initialization parameter file for your platform, see " About Initialization Parameters and Initialization Parameter Files ".

See Also:

- " Specifying Initialization Parameters "
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=REFRN-GUID-FD266F6F-D047-4EBB-8D96-B51B1DCA2D61) for details on all initialization parameters

**Parent topic:** Creating a Database with the CREATE DATABASE Statement

#### 2.4.6 Step 5: (Windows Only) Create an Instance

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

Do not set the - `STARTMODE` argument to `AUTO` at this point, because this causes the new instance to start and attempt to mount the database, which does not exist yet. You can change this parameter to `AUTO`, if desired, in Step 14: (Optional) Enable Automatic Instance Startup.

Most Oracle Database services log on to the system using the privileges of the Oracle Home User. The service runs with the privileges of this user. The `ORADIM` command prompts you for the password to this user account. You can specify other options using `ORADIM`.

See Also:

- [Oracle Database Platform Guide for Microsoft Windows](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=NTQRF05011) for more information on the `ORADIM` command and the Oracle Home User
- [Oracle Database Installation Guide for Microsoft Windows](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=NTDBI) for more information about the Oracle Home User

**Parent topic:** Creating a Database with the CREATE DATABASE Statement

#### 2.4.7 Step 6: Connect to the Instance

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

#### 2.4.8 Step 7: Create a Server Parameter File

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

Important—If you are using Oracle Managed Files and your initialization parameter file does not contain the `CONTROL_FILES` parameter, then you must create a server parameter file now so the database can save the names and locations of the control files that it creates during the `CREATE` `DATABASE` statement. See " Specifying Oracle Managed Files at Database Creation " for more information.

See Also:

- " Managing Initialization Parameters Using a Server Parameter File "
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=SQLRF01315) for more information on the `CREATE` `SPFILE` command

**Parent topic:** Creating a Database with the CREATE DATABASE Statement

#### 2.4.9 Step 8: Start the Instance

Start an instance without mounting a database.

- Run the `STARTUP` command with the `NOMOUNT` clause.

Typically, you do this only during database creation or while performing maintenance on the database. In this example, because the initialization parameter file or server parameter file is stored in the default location, you are not required to specify the `PFILE` clause:

```
STARTUP NOMOUNT
```

At this point, the instance memory is allocated and its processes are started. The database itself does not yet exist.

See Also:

- [Starting Up and Shutting Down](starting-up-and-shutting-down.md) for information about using the `STARTUP` command
- " Managing Initialization Parameters Using a Server Parameter File "

**Parent topic:** Creating a Database with the CREATE DATABASE Statement

#### 2.4.10 Step 9: Issue the CREATE DATABASE Statement

To create the new database, use the `CREATE` `DATABASE` statement.

- Run the `CREATE` `DATABASE` statement.

Note:

If you are creating a multitenant container database (CDB), then see the examples in [Oracle Multitenant Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=MULTI-GUID-54C5126C-427A-4BFE-81BF-950FB1A062D5).

Example 1

The following statement creates a database `mynewdb`. This database name must agree with the `DB_NAME` parameter in the initialization parameter file. This example assumes the following:

- The initialization parameter file specifies the number and location of control files with the `CONTROL_FILES` parameter.
- The directory `/u01/app/oracle/oradata/mynewdb` exists.
- The directories `/u01/logs/my` and `/u02/logs/my` exist.
```
CREATE DATABASE mynewdb
   USER SYS IDENTIFIED BY sys_password
   USER SYSTEM IDENTIFIED BY system_password
   LOGFILE GROUP 1 ('/u01/logs/my/redo01a.log','/u02/logs/my/redo01b.log') SIZE 100M BLOCKSIZE 512,
           GROUP 2 ('/u01/logs/my/redo02a.log','/u02/logs/my/redo02b.log') SIZE 100M BLOCKSIZE 512,
           GROUP 3 ('/u01/logs/my/redo03a.log','/u02/logs/my/redo03b.log') SIZE 100M BLOCKSIZE 512
   MAXLOGHISTORY 1
   MAXLOGFILES 16
   MAXLOGMEMBERS 3
   MAXDATAFILES 1024
   CHARACTER SET AL32UTF8
   NATIONAL CHARACTER SET AL16UTF16
   EXTENT MANAGEMENT LOCAL
   DATAFILE '/u01/app/oracle/oradata/mynewdb/system01.dbf'
     SIZE 700M REUSE AUTOEXTEND ON NEXT 10240K MAXSIZE UNLIMITED
   SYSAUX DATAFILE '/u01/app/oracle/oradata/mynewdb/sysaux01.dbf'
     SIZE 550M REUSE AUTOEXTEND ON NEXT 10240K MAXSIZE UNLIMITED
   DEFAULT TABLESPACE users
      DATAFILE '/u01/app/oracle/oradata/mynewdb/users01.dbf'
      SIZE 500M REUSE AUTOEXTEND ON MAXSIZE UNLIMITED
   DEFAULT TEMPORARY TABLESPACE tempts1
      TEMPFILE '/u01/app/oracle/oradata/mynewdb/temp01.dbf'
      SIZE 20M REUSE AUTOEXTEND ON NEXT 640K MAXSIZE UNLIMITED
   UNDO TABLESPACE undotbs1
      DATAFILE '/u01/app/oracle/oradata/mynewdb/undotbs01.dbf'
      SIZE 200M REUSE AUTOEXTEND ON NEXT 5120K MAXSIZE UNLIMITED
   USER_DATA TABLESPACE usertbs
      DATAFILE '/u01/app/oracle/oradata/mynewdb/usertbs01.dbf'
      SIZE 200M REUSE AUTOEXTEND ON MAXSIZE UNLIMITED;
```

A database is created with the following characteristics:

- The database is named `mynewdb`. Its global database name is `mynewdb.us.example.com`, where the domain portion (`us.example.com`) is taken from the initialization parameter file. See " Determining the Global Database Name ".
- Three control files are created as specified by the `CONTROL_FILES` initialization parameter, which was set before database creation in the initialization parameter file. See " Sample Initialization Parameter File " and " Specifying Control Files ".
- The passwords for user accounts `SYS` and `SYSTEM` are set to the values that you specified. The passwords are case-sensitive. The two clauses that specify the passwords for `SYS` and `SYSTEM` are not mandatory in this release of Oracle Database. However, if you specify either clause, then you must specify both clauses. For further information about the use of these clauses, see " Protecting Your Database: Specifying Passwords for Users SYS and SYSTEM ".
- The new database has three redo log file groups, each with two members, as specified in the `LOGFILE` clause. `MAXLOGFILES`, `MAXLOGMEMBERS`, and `MAXLOGHISTORY` define limits for the redo log. See " [Choosing the Number of Redo Log Files](managing-the-redo-log.md) ". The block size for the redo log files is set to 512 bytes, the same size as physical sectors on disk. The `BLOCKSIZE` clause is optional if block size is to be the same as physical sector size (the default). Typical sector size and thus typical block size is 512. Permissible values for `BLOCKSIZE` are 512, 1024, and 4096. For newer disks with a 4K sector size, optionally specify `BLOCKSIZE` as 4096. See " [Planning the Block Size of Redo Log Files](managing-the-redo-log.md) " for more information.
- `MAXDATAFILES` specifies the maximum number of data files that can be open in the database. This number affects the initial sizing of the control file.
	Note:
	You can set several limits during database creation. Some of these limits are limited by and affected by operating system limits. For example, if you set `MAXDATAFILES`, Oracle Database allocates enough space in the control file to store `MAXDATAFILES` file names, even if the database has only one data file initially. However, because the maximum control file size is limited and operating system dependent, you might not be able to set all `CREATE DATABASE` parameters at their theoretical maximums.
	For more information about setting limits during database creation, see the [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=SQLRF01204) and your operating system–specific Oracle documentation.
- The `AL32UTF8` character set is used to store data in this database.
- The `AL16UTF16` character set is specified as the `NATIONAL CHARACTER SET` used to store data in columns specifically defined as `NCHAR`, `NCLOB`, or `NVARCHAR2`.
- The `SYSTEM` tablespace, consisting of the operating system file `/u01/app/oracle/oradata/mynewdb/system01.dbf`, is created as specified by the `DATAFILE` clause. If a file with that name already exists, then it is overwritten.
- The `SYSTEM` tablespace is created as a locally managed tablespace. See " Creating a Locally Managed SYSTEM Tablespace ".
- A `SYSAUX` tablespace is created, consisting of the operating system file `/u01/app/oracle/oradata/mynewdb/sysaux01.dbf` as specified in the `SYSAUX DATAFILE` clause. See " About the SYSAUX Tablespace ".
- The `DEFAULT` `TABLESPACE` clause creates and names a default permanent tablespace for this database.
- The `DEFAULT TEMPORARY TABLESPACE` clause creates and names a default temporary tablespace for this database. See " Creating a Default Temporary Tablespace ".
- The `UNDO TABLESPACE` clause creates and names an undo tablespace that is used to store undo data for this database if you have specified `UNDO_MANAGEMENT=AUTO` in the initialization parameter file. If you omit this parameter, then it defaults to `AUTO`. See " Using Automatic Undo Management: Creating an Undo Tablespace ".
- The `USER_DATA` `TABLESPACE` clause creates and names the tablespace for storing user data and database options such as Oracle XML DB.
- Online redo logs will not initially be archived, because the `ARCHIVELOG` clause is not specified in this `CREATE` `DATABASE` statement. This is customary during database creation. You can later use an `ALTER DATABASE` statement to switch to `ARCHIVELOG` mode. The initialization parameters in the initialization parameter file for `mynewdb` relating to archiving are `LOG_ARCHIVE_DEST_1` and `LOG_ARCHIVE_FORMAT`. See [Managing Archived Redo Log Files](managing-archived-redo-log-files.md).

Tips:

- Ensure that all directories used in the `CREATE` `DATABASE` statement exist. The `CREATE` `DATABASE` statement does not create directories.
- If you are not using Oracle Managed Files, then every tablespace clause must include a `DATAFILE` or `TEMPFILE` clause.
- If database creation fails, then you can look at the alert log to determine the reason for the failure and to determine corrective actions. See " [Viewing the Alert Log](diagnosing-and-resolving-problems.md) ". If you receive an error message that contains a process number, then examine the trace file for that process. Look for the trace file that contains the process number in the trace file name. See " [Finding Trace Files](diagnosing-and-resolving-problems.md) " for more information.
- To resubmit the `CREATE` `DATABASE` statement after a failure, you must first shut down the instance and delete any files created by the previous `CREATE` `DATABASE` statement.

Example 2

This example illustrates creating a database with Oracle Managed Files, which enables you to use a much simpler `CREATE` `DATABASE` statement. To use Oracle Managed Files, the initialization parameter `DB_CREATE_FILE_DEST` must be set. This parameter defines the base directory for the various database files that the database creates and automatically names. The following statement is an example of setting this parameter in the initialization parameter file:

```
DB_CREATE_FILE_DEST='/u01/app/oracle/oradata'
```

With Oracle Managed Files and the following `CREATE` `DATABASE` statement, the database creates the `SYSTEM` and `SYSAUX` tablespaces, creates the additional tablespaces specified in the statement, and chooses default sizes and properties for all data files, control files, and redo log files. Note that these properties and the other default database properties set by this method may not be suitable for your production environment, so it is recommended that you examine the resulting configuration and modify it if necessary.

```
CREATE DATABASE mynewdb
USER SYS IDENTIFIED BY sys_password
USER SYSTEM IDENTIFIED BY system_password
EXTENT MANAGEMENT LOCAL
DEFAULT TEMPORARY TABLESPACE temp
UNDO TABLESPACE undotbs1
DEFAULT TABLESPACE users;
```

Tip:

If your `CREATE` `DATABASE` statement fails, and if you did not complete Step 7, then ensure that there is not a pre-existing server parameter file (SPFILE) for this instance that is setting initialization parameters in an unexpected way. For example, an SPFILE contains a setting for the complete path to all control files, and the `CREATE` `DATABASE` statement fails if those control files do not exist. Ensure that you shut down and restart the instance (with `STARTUP` `NOMOUNT`) after removing an unwanted SPFILE. See " Managing Initialization Parameters Using a Server Parameter File " for more information.

See Also:

- " Specifying CREATE DATABASE Statement Clauses "
- " Specifying Oracle Managed Files at Database Creation "
- [Using Oracle Managed Files](using-oracle-managed-files.md)
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=SQLRF01204) for more information about specifying the clauses and parameter values for the `CREATE DATABASE` statement

**Parent topic:** Creating a Database with the CREATE DATABASE Statement

#### 2.4.11 Step 10: Create Additional Tablespaces

To make the database functional, you must create additional tablespaces for your application data.

- Run the `CREATE TABLESPACE` statement to create additional tablespaces.

The following sample script creates some additional tablespaces:

```
CREATE TABLESPACE apps_tbs LOGGING 
     DATAFILE '/u01/app/oracle/oradata/mynewdb/apps01.dbf' 
     SIZE 500M REUSE AUTOEXTEND ON NEXT  1280K MAXSIZE UNLIMITED 
     EXTENT MANAGEMENT LOCAL;
-- create a tablespace for indexes, separate from user tablespace (optional)
CREATE TABLESPACE indx_tbs LOGGING 
     DATAFILE '/u01/app/oracle/oradata/mynewdb/indx01.dbf' 
     SIZE 100M REUSE AUTOEXTEND ON NEXT  1280K MAXSIZE UNLIMITED 
     EXTENT MANAGEMENT LOCAL;
```

For information about creating tablespaces, see [Managing Tablespaces](managing-tablespaces.md).

**Parent topic:** Creating a Database with the CREATE DATABASE Statement

#### 2.4.12 Step 11: Run Scripts to Build Data Dictionary Views

Run the scripts necessary to build data dictionary views, synonyms, and PL/SQL packages, and to support proper functioning of SQL\*Plus.

1. Execute one of the following steps:
	- In SQL\*Plus, run the following scripts as a user with the `SYSDBA` privileges:
		```
		@?/rdbms/admin/catalog.sql
		@?/rdbms/admin/catproc.sql
		```
		or
		- Run `catctl.pl` with the script `catpcat.sql`:
		```
		$ORACLE_HOME/perl/bin/perl $ORACLE_HOME/rdbms/admin/catctl.pl -d
		$ORACLE_HOME/rdbms/admin -n number_of_processes -l output_log_directory catpcat.sql
		```
		The value for `number_of_processes` should reflect the number of processors available on the system. It can have the maximum value of 8 for CDBs as well as non-CDBs. If you do not specify this value, then its default value is 4 for non-CDBs and value of the `CPU_COUNT` initialization parameter for CDBs.
		Note:
		- When creating a multitenant container database (CDB), use the additional parameter `-c 'CDB$ROOT PDB$SEED'` (use double quotes for a Windows system) to run the script `catpcat.sql` first in the root container (`CDB$ROOT`) and then in the seed PDB (`PDB$SEED`).
		- The script `catpcat.sql` runs the scripts `catalog.sql` and `catproc.sql` with parallel processes, thus improving the performance of building the data dictionary.
2. In SQL\*Plus, run the following script as a user with the `SYSDBA` privileges:
	```
	@?/rdbms/admin/utlrp.sql
	```
3. In SQL\*Plus, run the following script as the `SYSTEM` user:
	```
	@?/sqlplus/admin/pupbld.sql
	```

The at-sign (`@`) is shorthand for the command that runs a SQL\*Plus script. The question mark (`?`) is a SQL\*Plus variable indicating the Oracle home directory.

The following table contains the descriptions of these scripts:

| Script | Description |
| --- | --- |
| `catalog.sql ` | Creates the views of the data dictionary tables, the dynamic performance views, and public synonyms for many of the views. Grants `PUBLIC` access to the synonyms. |
| `catproc.sql ` | Runs all scripts required for or used with PL/SQL. |
| `utlrp.sql ` | Recompiles all PL/SQL modules that are in an invalid state, including packages, procedures, and types. |
| `pupbld.sql` | Required for SQL\*Plus. Enables SQL\*Plus to disable commands by user. |
| `catpcat.sql` | Builds the data dictionary. This script runs using the `catctl.pl` program (and not using SQL\*Plus) and internally runs the scripts `catalog.sql` and `catproc.sql` with parallel processes, thus improving the performance of building the data dictionary. |

See Also:

[Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=UPGRD-GUID-C667B51C-058F-48B6-86FE-) for the list of all the parameters to `catctl.pl`

**Parent topic:** Creating a Database with the CREATE DATABASE Statement

#### 2.4.13 Step 12: (Optional) Run Scripts to Install Additional Options

You may want to run other scripts. The scripts that you run are determined by the features and options you choose to use or install.

- Run scripts to install additional options.

Many of the scripts available to you are described in the [Oracle Database Reference.](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=REFRN005)

If you plan to install other Oracle products to work with this database, then see the installation instructions for those products. Some products require you to create additional data dictionary tables. Usually, command files are provided to create and load these tables into the database data dictionary.

See your Oracle documentation for the specific products that you plan to install for installation and administration instructions.

**Parent topic:** Creating a Database with the CREATE DATABASE Statement

#### 2.4.14 Step 13: Run Datapatch

Run Datapatch to update information stored in the database to the correct patch level.

For instructions on running Datapatch, refer to the Datapatch User Guide in My Oracle Support ([Doc ID 2680521.1](https://support.oracle.com/rs?type=doc&id=2680521.1)).

**Parent topic:** Creating a Database with the CREATE DATABASE Statement

#### 2.4.15 Step 14: Back Up the Database

Take a full backup of the database to ensure that you have a complete set of files from which to recover if a media failure occurs.

- Back up the database.

For information on backing up a database, see [Oracle Database Backup and Recovery User's Guide.](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=BRADV-GUID-008E0F84-E623-4467-8706-A99B34002DD6)

**Parent topic:** Creating a Database with the CREATE DATABASE Statement

#### 2.4.16 Step 15: (Optional) Enable Automatic Instance Startup

You might want to configure the Oracle instance to start automatically when its host computer restarts.

- Configure the Oracle instance to start automatically when its host computer restarts.

See your operating system documentation for instructions. For example, on Windows, use the following command to configure the database service to start the instance upon computer restart:

```
ORADIM -EDIT -SID sid -STARTMODE AUTO -SRVCSTART SYSTEM [-SPFILE]
```

You must use the `-SPFILE` argument if you want the instance to read an SPFILE upon automatic restart.

See Also:

- [Configuring Automatic Restart of an Oracle Database](configuring-automatic-restart-of-an-oracle-database.md)
- [Oracle Database Platform Guide for Microsoft Windows](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=NTQRF05011) for more information on the `ORADIM` command.

**Parent topic:** Creating a Database with the CREATE DATABASE Statement

### 2.5 Specifying CREATE DATABASE Statement Clauses

When you execute a `CREATE` `DATABASE` statement, Oracle Database performs several operations. The actual operations performed depend on the clauses that you specify in the `CREATE` `DATABASE` statement and the initialization parameters that you have set.

- About CREATE DATABASE Statement Clauses  
	You can use the `CREATE DATABASE` clauses to simplify the creation and management of your database.
- Protecting Your Database: Specifying Passwords for SYS and SYSTEM Users  
	To protect your database, specify passwords for `SYS` and `SYSTEM` users.
- Creating a Locally Managed SYSTEM Tablespace  
	During database creation, create a locally managed SYSTEM tablespace. A locally managed tablespace uses a bitmap stored in each data file to manage the extents.
- Specify Data File Attributes for the SYSAUX Tablespace  
	The SYSAUX tablespace is created by default, but you can specify its data file attributes during database creation.
- Using Automatic Undo Management: Creating an Undo Tablespace  
	Automatic undo management uses an undo tablespace.
- Creating a Default Permanent Tablespace  
	Oracle strongly recommends that you create a default permanent tablespace. Oracle Database assigns to this tablespace any non- `SYSTEM` users for whom you do not explicitly specify a different permanent tablespace.
- Creating a Default Temporary Tablespace  
	When you create a default temporary tablespace, Oracle Database assigns it as the temporary tablespace for users who are not explicitly assigned a temporary tablespace.
- Specifying Oracle Managed Files at Database Creation  
	You can minimize the number of clauses and parameters that you specify in your `CREATE` `DATABASE` statement by using the Oracle Managed Files feature.
- Supporting Bigfile Tablespaces During Database Creation  
	Oracle Database simplifies management of tablespaces and enables support for extremely large databases by letting you create bigfile tablespaces.
- Specifying the Database Time Zone and Time Zone File  
	Oracle Database datetime and interval data types and time zone support make it possible to store consistent information about the time of events and transactions.
- Specifying FORCE LOGGING Mode  
	Some data definition language statements (such as `CREATE` `TABLE`) allow the `NOLOGGING` clause, which causes some database operations not to generate redo records in the database redo log. The `NOLOGGING` setting can speed up operations that can be easily recovered outside of the database recovery mechanisms, but it can negatively affect media recovery and standby databases.

**Parent topic:** Creating and Configuring an Oracle Database

#### 2.5.1 About CREATE DATABASE Statement Clauses

You can use the `CREATE DATABASE` clauses to simplify the creation and management of your database.

When you execute a `CREATE` `DATABASE` statement, Oracle Database performs at least these operations:

- Creates the data files for the database
- Creates the control files for the database
- Creates the online redo logs for the database and establishes the `ARCHIVELOG` mode
- Creates the `SYSTEM` tablespace
- Creates the `SYSAUX` tablespace
- Creates the data dictionary
- Sets the character set that stores data in the database
- Sets the database time zone
- Mounts and opens the database for use

**Parent topic:** Specifying CREATE DATABASE Statement Clauses

#### 2.5.2 Protecting Your Database: Specifying Passwords for SYS and SYSTEM Users

To protect your database, specify passwords for `SYS` and `SYSTEM` users.

- In the `CREATE` `DATABASE` statement, include clauses that specify the password for users `SYS` and `SYSTEM`.

The clauses of the `CREATE` `DATABASE` statement used for specifying the passwords for users `SYS` and `SYSTEM` are:

- `USER` `SYS` `IDENTIFIED` `BY` `password`
- `USER` `SYSTEM` `IDENTIFIED` `BY` `password`

When choosing a password, keep in mind that passwords are case-sensitive. Also, there may be password formatting requirements for your database.

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=DBSEG-GUID-451679EB-8676-47E6-82A6-DF025FD65156) for information about the Oracle guidelines for creating secure passwords

**Parent topic:** Specifying CREATE DATABASE Statement Clauses

#### 2.5.3 Creating a Locally Managed SYSTEM Tablespace

During database creation, create a locally managed SYSTEM tablespace. A locally managed tablespace uses a bitmap stored in each data file to manage the extents.

- Specify the `EXTENT MANAGEMENT LOCAL` clause in the `CREATE` `DATABASE` statement to create a locally managed `SYSTEM` tablespace.

If you do not specify the `EXTENT MANAGEMENT LOCAL` clause, then by default the database creates a dictionary-managed `SYSTEM` tablespace. Dictionary-managed tablespaces are deprecated.

If you create your database with a locally managed `SYSTEM` tablespace, and if you are not using Oracle Managed Files, then ensure that the following conditions are met:

- You specify the `DEFAULT` `TEMPORARY` `TABLESPACE` clause in the `CREATE` `DATABASE` statement.
- You include the `UNDO TABLESPACE` clause in the `CREATE` `DATABASE` statement.

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=SQLRF01204) for more specific information about the use of the `DEFAULT TEMPORARY TABLESPACE` and `UNDO TABLESPACE` clauses when `EXTENT MANAGEMENT LOCAL` is specified for the `SYSTEM` tablespace
- " [Locally Managed Tablespaces](managing-tablespaces.md) "
- " [Migrating the SYSTEM Tablespace to a Locally Managed Tablespace](managing-tablespaces.md) "

**Parent topic:** Specifying CREATE DATABASE Statement Clauses

#### 2.5.4 Specify Data File Attributes for the SYSAUX Tablespace

The SYSAUX tablespace is created by default, but you can specify its data file attributes during database creation.

To specify data file attributes for the `SYSAUX` tablespace:

- Include the `SYSAUX DATAFILE` clause in the `CREATE` `DATABASE` statement.

If you include a `DATAFILE` clause for the `SYSTEM` tablespace, then you must specify the `SYSAUX DATAFILE` clause as well, or the `CREATE` `DATABASE` statement will fail. This requirement does not exist if the Oracle Managed Files feature is enabled (see " Specifying Oracle Managed Files at Database Creation ").

- About the SYSAUX Tablespace  
	The `SYSAUX` tablespace is always created at database creation. The `SYSAUX` tablespace serves as an auxiliary tablespace to the `SYSTEM` tablespace. Because it is the default tablespace for many Oracle Database features and products that previously required their own tablespaces, it reduces the number of tablespaces required by the database. It also reduces the load on the `SYSTEM` tablespace.

**Parent topic:** Specifying CREATE DATABASE Statement Clauses

##### 2.5.4.1 About the SYSAUX Tablespace

The `SYSAUX` tablespace is always created at database creation. The `SYSAUX` tablespace serves as an auxiliary tablespace to the `SYSTEM` tablespace. Because it is the default tablespace for many Oracle Database features and products that previously required their own tablespaces, it reduces the number of tablespaces required by the database. It also reduces the load on the `SYSTEM` tablespace.

You can specify only data file attributes for the `SYSAUX` tablespace, using the `SYSAUX DATAFILE` clause in the `CREATE` `DATABASE` statement. Mandatory attributes of the `SYSAUX` tablespace are set by Oracle Database and include:

- `PERMANENT`
- `READ` `WRITE`
- `EXTENT` `MANAGMENT` `LOCAL`
- `SEGMENT` `SPACE` `MANAGMENT` `AUTO`

You cannot alter these attributes with an `ALTER` `TABLESPACE` statement, and any attempt to do so will result in an error. You cannot drop or rename the `SYSAUX` tablespace.

The size of the `SYSAUX` tablespace is determined by the size of the database components that occupy `SYSAUX`. You can view a list of these components by querying the `V$SYSAUX_OCCUPANTS` view. Based on the initial sizes of these components, the `SYSAUX` tablespace must be at least 400 MB at the time of database creation. The space requirements of the `SYSAUX` tablespace will increase after the database is fully deployed, depending on the nature of its use and workload. For more information on how to manage the space consumption of the `SYSAUX` tablespace on an ongoing basis, see the " [Managing the SYSAUX Tablespace](managing-tablespaces.md) ".

The `SYSAUX` tablespace has the same security attributes as the `SYSTEM` tablespace.

See Also:

" [Managing the SYSAUX Tablespace](managing-tablespaces.md) "

**Parent topic:** Specify Data File Attributes for the SYSAUX Tablespace

#### 2.5.5 Using Automatic Undo Management: Creating an Undo Tablespace

Automatic undo management uses an undo tablespace.

- To enable automatic undo management, set the `UNDO_MANAGEMENT` initialization parameter to `AUTO` in your initialization parameter file. Or, omit this parameter, and the database defaults to automatic undo management.

In this mode, undo data is stored in an undo tablespace and is managed by Oracle Database. To define and name the undo tablespace yourself, you must include the `UNDO TABLESPACE` clause in the `CREATE DATABASE` statement at database creation time. If you omit this clause, and automatic undo management is enabled, then the database creates a default undo tablespace named `SYS_UNDOTBS`.

Note:

If you decide to define the undo tablespace yourself, then ensure that its block size matches the highest data file block size for the database.

See Also:

- " Specifying the Method of Undo Space Management "
- [Managing Undo](managing-undo.md) for information about the creation and use of undo tablespaces

**Parent topic:** Specifying CREATE DATABASE Statement Clauses

#### 2.5.6 Creating a Default Permanent Tablespace

Oracle strongly recommends that you create a default permanent tablespace. Oracle Database assigns to this tablespace any non- `SYSTEM` users for whom you do not explicitly specify a different permanent tablespace.

To specify a default permanent tablespace for the database:

- Include the `DEFAULT` `TABLESPACE` clause in the `CREATE` `DATABASE` statement

If you do not specify the `DEFAULT` `TABLESPACE` clause, then the `SYSTEM` tablespace is the default permanent tablespace for non- `SYSTEM` users.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=SQLRF01204) for the syntax of the `DEFAULT TABLESPACE` clause of `CREATE DATABASE` and `ALTER DATABASE`

**Parent topic:** Specifying CREATE DATABASE Statement Clauses

#### 2.5.7 Creating a Default Temporary Tablespace

When you create a default temporary tablespace, Oracle Database assigns it as the temporary tablespace for users who are not explicitly assigned a temporary tablespace.

To create a default temporary tablespace for the database:

- Include the `DEFAULT TEMPORARY TABLESPACE` clause in the `CREATE` `DATABASE` statement.

You can explicitly assign a temporary tablespace or tablespace group to a user in the `CREATE USER` statement. However, if you do not do so, and if no default temporary tablespace has been specified for the database, then by default these users are assigned the `SYSTEM` tablespace as their temporary tablespace. It is not good practice to store temporary data in the `SYSTEM` tablespace, and it is cumbersome to assign every user a temporary tablespace individually. Therefore, Oracle recommends that you use the `DEFAULT TEMPORARY TABLESPACE` clause of `CREATE` `DATABASE`.

Note:

When you specify a locally managed `SYSTEM` tablespace, the `SYSTEM` tablespace cannot be used as a temporary tablespace. In this case you must create a default temporary tablespace. This behavior is explained in " Creating a Locally Managed SYSTEM Tablespace ".

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=SQLRF01204) for the syntax of the `DEFAULT TEMPORARY TABLESPACE` clause of `CREATE DATABASE` and `ALTER DATABASE`
- " [Temporary Tablespaces](managing-tablespaces.md) " for information about creating and using temporary tablespaces
- " [Multiple Temporary Tablespaces: Using Tablespace Groups](managing-tablespaces.md) " for information about creating and using temporary tablespace groups

**Parent topic:** Specifying CREATE DATABASE Statement Clauses

#### 2.5.8 Specifying Oracle Managed Files at Database Creation

You can minimize the number of clauses and parameters that you specify in your `CREATE` `DATABASE` statement by using the Oracle Managed Files feature.

- Specify either a directory or Oracle Automatic Storage Management (Oracle ASM) disk group in which your files are created and managed by Oracle Database.

By including any of the initialization parameters `DB_CREATE_FILE_DEST,` `DB_CREATE_ONLINE_LOG_DEST_` `n`, or `DB_RECOVERY_FILE_DEST` in your initialization parameter file, you instruct Oracle Database to create and manage the underlying operating system files of your database. Oracle Database will automatically create and manage the operating system files for the following database structures, depending on which initialization parameters you specify and how you specify clauses in your `CREATE` `DATABASE` statement:

- Tablespaces and their data files
- Temporary tablespaces and their temp files
- Control files
- Online redo logs
- Archived redo log files
- Flashback logs
- Block change tracking files
- RMAN backups

See Also:

" Specifying a Fast Recovery Area " for information about setting initialization parameters that create a Fast Recovery Area

The following `CREATE` `DATABASE` statement shows briefly how the Oracle Managed Files feature works, assuming you have specified required initialization parameters:

```
CREATE DATABASE mynewdb
     USER SYS IDENTIFIED BY sys_password
     USER SYSTEM IDENTIFIED BY system_password
     EXTENT MANAGEMENT LOCAL
     UNDO TABLESPACE undotbs1
     DEFAULT TEMPORARY TABLESPACE tempts1
     DEFAULT TABLESPACE users;
```
- The `SYSTEM` tablespace is created as a locally managed tablespace. Without the `EXTENT` `MANAGEMENT` `LOCAL` clause, the `SYSTEM` tablespace is created as dictionary managed, which is not recommended.
- No `DATAFILE` clause is specified, so the database creates an Oracle managed data file for the `SYSTEM` tablespace.
- No `LOGFILE` clauses are included, so the database creates two Oracle managed redo log file groups.
- No `SYSAUX DATAFILE` is included, so the database creates an Oracle managed data file for the `SYSAUX` tablespace.
- No `DATAFILE` subclause is specified for the `UNDO TABLESPACE` and `DEFAULT` `TABLESPACE` clauses, so the database creates an Oracle managed data file for each of these tablespaces.
- No `TEMPFILE` subclause is specified for the `DEFAULT TEMPORARY TABLESPACE` clause, so the database creates an Oracle managed temp file.
- If no `CONTROL_FILES` initialization parameter is specified in the initialization parameter file, then the database also creates an Oracle managed control file.
- If you are using a server parameter file (see " Managing Initialization Parameters Using a Server Parameter File "), then the database automatically sets the appropriate initialization parameters.
	See Also:
	- [Using Oracle Managed Files](using-oracle-managed-files.md), for information about the Oracle Managed Files feature and how to use it
	- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=OSTMG). for information about Automatic Storage Management

**Parent topic:** Specifying CREATE DATABASE Statement Clauses

#### 2.5.9 Supporting Bigfile Tablespaces During Database Creation

Oracle Database simplifies management of tablespaces and enables support for extremely large databases by letting you create bigfile tablespaces.

Bigfile tablespaces can contain only one file, but that file can have up to 4G blocks. The maximum number of data files in an Oracle Database is limited (usually to 64K files). Therefore, bigfile tablespaces can significantly enhance the storage capacity of an Oracle Database.

This section discusses the clauses of the `CREATE` `DATABASE` statement that let you include support for bigfile tablespaces.

- Specifying the Default Tablespace Type  
	The `SET DEFAULT...TABLESPACE` clause of the `CREATE` `DATABASE` statement determines the default type of tablespace for this database in subsequent `CREATE` `TABLESPACE` statements.
- Overriding the Default Tablespace Type  
	The `SYSTEM` and `SYSAUX` tablespaces are always created with the default tablespace type. However, you optionally can explicitly override the default tablespace type for the `UNDO` and `DEFAULT` `TEMPORARY` tablespace during the `CREATE` `DATABASE` operation.

**Parent topic:** Specifying CREATE DATABASE Statement Clauses

##### 2.5.9.1 Specifying the Default Tablespace Type

The `SET DEFAULT...TABLESPACE` clause of the `CREATE` `DATABASE` statement determines the default type of tablespace for this database in subsequent `CREATE` `TABLESPACE` statements.

- Specify either `SET DEFAULT BIGFILE TABLESPACE` or `SET DEFAULT SMALLFILE TABLESPACE`.

If you omit this clause, then the default is a smallfile tablespace, which is the traditional type of Oracle Database tablespace. A smallfile tablespace can contain up to 1022 files with up to 4M blocks each.

The use of bigfile tablespaces further enhances the Oracle Managed Files feature, because bigfile tablespaces make data files completely transparent for users. SQL syntax for the `ALTER` `TABLESPACE` statement has been extended to allow you to perform operations on tablespaces, rather than the underlying data files.

The `CREATE` `DATABASE` statement shown in " Specifying Oracle Managed Files at Database Creation " can be modified as follows to specify that the default type of tablespace is a bigfile tablespace:

```
CREATE DATABASE mynewdb
     USER SYS IDENTIFIED BY sys_password
     USER SYSTEM IDENTIFIED BY system_password
     SET DEFAULT BIGFILE TABLESPACE
     UNDO TABLESPACE undotbs1
     DEFAULT TEMPORARY TABLESPACE tempts1;
```

To dynamically change the default tablespace type after database creation, use the `SET DEFAULT TABLESPACE` clause of the `ALTER DATABASE` statement:

```
ALTER DATABASE SET DEFAULT BIGFILE TABLESPACE;
```

You can determine the current default tablespace type for the database by querying the `DATABASE_PROPERTIES` data dictionary view as follows:

```
SELECT PROPERTY_VALUE FROM DATABASE_PROPERTIES 
   WHERE PROPERTY_NAME = 'DEFAULT_TBS_TYPE';
```

**Parent topic:** Supporting Bigfile Tablespaces During Database Creation

##### 2.5.9.2 Overriding the Default Tablespace Type

The `SYSTEM` and `SYSAUX` tablespaces are always created with the default tablespace type. However, you optionally can explicitly override the default tablespace type for the `UNDO` and `DEFAULT` `TEMPORARY` tablespace during the `CREATE` `DATABASE` operation.

- Specify an `UNDO TABLESPACE` clause or a `DEFAULT TEMPORARY TABLESPACE` clause that overrides the default tablespace type.

For example, you can create a bigfile `UNDO` tablespace in a database with the default tablespace type of smallfile as follows:

```
CREATE DATABASE mynewdb
...
     BIGFILE UNDO TABLESPACE undotbs1
        DATAFILE '/u01/oracle/oradata/mynewdb/undotbs01.dbf'
        SIZE 200M REUSE AUTOEXTEND ON MAXSIZE UNLIMITED;
```

You can create a smallfile `DEFAULT` `TEMPORARY` tablespace in a database with the default tablespace type of bigfile as follows:

```
CREATE DATABASE mynewdb
   SET DEFAULT BIGFILE TABLESPACE
...
     SMALLFILE DEFAULT TEMPORARY TABLESPACE tempts1
        TEMPFILE '/u01/oracle/oradata/mynewdb/temp01.dbf' 
        SIZE 20M REUSE
...
```

**Parent topic:** Supporting Bigfile Tablespaces During Database Creation

#### 2.5.10 Specifying the Database Time Zone and Time Zone File

Oracle Database datetime and interval data types and time zone support make it possible to store consistent information about the time of events and transactions.

- Setting the Database Time Zone  
	You can set the database time zone with the `SET TIME_ZONE` clause of the `CREATE DATABASE` statement.
- About the Database Time Zone Files  
	Two time zone files are included in a subdirectory of the Oracle home directory. The time zone files contain the valid time zone names.
- Specifying the Database Time Zone File  
	All databases that share information must use the same time zone data file.

**Parent topic:** Specifying CREATE DATABASE Statement Clauses

##### 2.5.10.1 Setting the Database Time Zone

You can set the database time zone with the `SET TIME_ZONE` clause of the `CREATE DATABASE` statement.

- Set the database time zone when the database is created by using the `SET TIME_ZONE` clause of the `CREATE DATABASE` statement.

If you do not set the database time zone, then it defaults to the time zone of the host operating system.

You can change the database time zone for a session by using the `SET TIME_ZONE` clause of the `ALTER SESSION` statement.

See Also:

[Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=NLSPG262) for more information about setting the database time zone

**Parent topic:** Specifying the Database Time Zone and Time Zone File

##### 2.5.10.2 About the Database Time Zone Files

Two time zone files are included in a subdirectory of the Oracle home directory. The time zone files contain the valid time zone names.

The following information is also included for each time zone:

- Offset from Coordinated Universal Time (UTC)
- Transition times for Daylight Saving Time
- Abbreviations for standard time and Daylight Saving Time

The default time zone file is ORACLE\_HOME/oracore/zoneinfo/timezlrg\_11.dat. A smaller time zone file with fewer time zones can be found in ORACLE\_HOME/oracore/zoneinfo/timezone\_11.dat.

To view the time zone names in the file being used by your database, use the following query:

```
SELECT * FROM V$TIMEZONE_NAMES;
```

See Also:

[Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=NLSPG004) for more information about managing and selecting time zone files

**Parent topic:** Specifying the Database Time Zone and Time Zone File

##### 2.5.10.3 Specifying the Database Time Zone File

All databases that share information must use the same time zone data file.

The database server always uses the large time zone file by default.

To use the small time zone file on the client and know that all your data will refer only to regions in the small file:

- Set the `ORA_TZFILE` environment variable on the client to the full path name of the timezone `version`.dat file on the client, where `version` matches the time zone file version that is being used by the database server.

If you are already using the default larger time zone file on the client, then it is not practical to change to the smaller time zone file, because the database may contain data with time zones that are not part of the smaller file.

**Parent topic:** Specifying the Database Time Zone and Time Zone File

#### 2.5.11 Specifying FORCE LOGGING Mode

Some data definition language statements (such as `CREATE` `TABLE`) allow the `NOLOGGING` clause, which causes some database operations not to generate redo records in the database redo log. The `NOLOGGING` setting can speed up operations that can be easily recovered outside of the database recovery mechanisms, but it can negatively affect media recovery and standby databases.

Oracle Database lets you force the writing of redo records even when `NOLOGGING` has been specified in DDL statements. The database never generates redo records for temporary tablespaces and temporary segments, so forced logging has no affect for objects.

- Using the FORCE LOGGING Clause  
	You can force the writing of redo records even when `NOLOGGING` is specified in DDL statements.
- Performance Considerations of FORCE LOGGING Mode  
	`FORCE LOGGING` mode results in some performance degradation.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=SQLRF30009) for information about operations that can be done in `NOLOGGING` mode

**Parent topic:** Specifying CREATE DATABASE Statement Clauses

##### 2.5.11.1 Using the FORCE LOGGING Clause

You can force the writing of redo records even when `NOLOGGING` is specified in DDL statements.

To put the database into `FORCE LOGGING` mode:

- Include the `FORCE LOGGING` clause in the `CREATE DATABASE` statement.

If you do not specify this clause, then the database is not placed into `FORCE LOGGING` mode.

Use the `ALTER DATABASE` statement to place the database into `FORCE LOGGING` mode after database creation. This statement can take a considerable time for completion, because it waits for all unlogged direct writes to complete.

You can cancel `FORCE LOGGING` mode using the following SQL statement:

```
ALTER DATABASE NO FORCE LOGGING;
```

Independent of specifying `FORCE LOGGING` for the database, you can selectively specify `FORCE LOGGING` or `NO FORCE LOGGING` at the tablespace level. However, if `FORCE LOGGING` mode is in effect for the database, it takes precedence over the tablespace setting. If it is not in effect for the database, then the individual tablespace settings are enforced. Oracle recommends that either the entire database is placed into `FORCE LOGGING` mode, or individual tablespaces be placed into `FORCE LOGGING` mode, but not both.

The `FORCE LOGGING` mode is a persistent attribute of the database. That is, if the database is shut down and restarted, it remains in the same logging mode. However, if you re-create the control file, the database is not restarted in the `FORCE LOGGING` mode unless you specify the `FORCE LOGGING` clause in the `CREATE CONTROL FILE` statement.

See Also:

" [Controlling the Writing of Redo Records](managing-tablespaces.md) " for information about using the `FORCE LOGGING` clause for tablespace creation.

**Parent topic:** Specifying FORCE LOGGING Mode

##### 2.5.11.2 Performance Considerations of FORCE LOGGING Mode

`FORCE LOGGING` mode results in some performance degradation.

If the primary reason for specifying `FORCE LOGGING` is to ensure complete media recovery, and there is no standby database active, then consider the following:

- How many media failures are likely to happen?
- How serious is the damage if unlogged direct writes cannot be recovered?
- Is the performance degradation caused by forced logging tolerable?

If the database is running in `NOARCHIVELOG` mode, then generally there is no benefit to placing the database in `FORCE LOGGING` mode. Media recovery is not possible in `NOARCHIVELOG` mode, so if you combine it with `FORCE LOGGING`, the result may be performance degradation with little benefit.

Starting with Oracle Database 18c, the following two new nologging clauses are introduced, which enable non-logged operations to be carried out and have Active Data Guard standby databases receive all the data, thus preventing performance degradation caused by large redo log generation by the `FORCE LOGGING` mode:

- `STANDBY NOLOGGING FOR DATA AVAILABILITY`
- `STANDBY NOLOGGING FOR LOAD PERFORMANCE`

See Also:

[Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=SBYDB-GUID-AE2B1237-57A1-4745-A04C-4246A831A963) for more information about these `STANDBY NOLOGGING` clauses

**Parent topic:** Specifying FORCE LOGGING Mode

### 2.6 Specifying Initialization Parameters

You can add or edit basic initialization parameters before you create your new database.

- About Initialization Parameters and Initialization Parameter Files  
	When an Oracle instance starts, it reads initialization parameters from an initialization parameter file. This file must at a minimum specify the `DB_NAME` parameter. All other parameters have default values.
- Determining the Global Database Name  
	The global database name consists of the user-specified local database name and the location of the database within a network structure.
- Specifying a Fast Recovery Area  
	The Fast Recovery Area is a location in which Oracle Database can store and manage files related to backup and recovery. It is distinct from the database area, which is a location for the current database files (data files, control files, and online redo logs).
- Specifying Control Files  
	Every database has a control file, which contains entries that describe the structure of the database (such as its name, the timestamp of its creation, and the names and locations of its data files and redo files). The `CONTROL_FILES` initialization parameter specifies one or more names of control files, separated by commas.
- Specifying Database Block Sizes  
	The `DB_BLOCK_SIZE` initialization parameter specifies the standard block size for the database.
- Specifying the Maximum Number of Processes  
	The `PROCESSES` initialization parameter determines the maximum number of operating system processes that can be connected to Oracle Database concurrently.
- Specifying the DDL Lock Timeout  
	You can specify the amount of time that blocking DDL statements wait for locks.
- Specifying the Method of Undo Space Management  
	Every Oracle Database must have a method of maintaining information that is used to undo changes to the database. Such information consists of records of the actions of transactions, primarily before they are committed. Collectively these records are called undo data.
- Specifying the Database Compatibility Level  
	The `COMPATIBLE` initialization parameter controls the database compatibility level.
- Setting the License Parameter  
	If you use named user licensing, Oracle Database can help you enforce this form of licensing. You can set a limit on the number of users created in the database. Once this limit is reached, you cannot create more users.

See Also:

- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=REFRN001) for descriptions of all initialization parameters including their default settings
- [Managing Memory](managing-memory.md) for a discussion of the initialization parameters that pertain to memory management

**Parent topic:** Creating and Configuring an Oracle Database

#### 2.6.1 About Initialization Parameters and Initialization Parameter Files

When an Oracle instance starts, it reads initialization parameters from an initialization parameter file. This file must at a minimum specify the `DB_NAME` parameter. All other parameters have default values.

The initialization parameter file can be either a read-only text file, a `PFILE`, or a read/write binary file.

The binary file is called a server parameter file. A server parameter file enables you to change initialization parameters with `ALTER SYSTEM` commands and to persist the changes across a shutdown and startup. It also provides a basis for self-tuning by Oracle Database. For these reasons, it is recommended that you use a server parameter file. You can create one manually from your edited text initialization file, or automatically by using Database Configuration Assistant (DBCA) to create your database.

Before you manually create a server parameter file, you can start an instance with a text initialization parameter file. Upon startup, the Oracle instance first searches for a server parameter file in a default location, and if it does not find one, searches for a text initialization parameter file. You can also override an existing server parameter file by naming a text initialization parameter file as an argument of the `STARTUP` command.

Default file names and locations for the text initialization parameter file are shown in the following table:

| Platform | Default Name | Default Location |
| --- | --- | --- |
| UNIX and Linux | `init` `ORACLE_SID`.`ora`  For example, the initialization parameter file for the `mynewdb` database is named:  `initmynewdb.ora` | ORACLE\_HOME/ `dbs` |
| Windows | `init` `ORACLE_SID``.ora ` | ORACLE\_HOME\\ `database` |

If you are creating an Oracle database for the first time, Oracle suggests that you minimize the number of parameter values that you alter. As you become more familiar with your database and environment, you can dynamically tune many initialization parameters using the `ALTER SYSTEM` statement. If you are using a text initialization parameter file, then your changes are effective only for the current instance. To make them permanent, you must update them manually in the initialization parameter file, or they will be lost over the next shutdown and startup of the database. If you are using a server parameter file, then initialization parameter file changes made by the `ALTER SYSTEM` statement can persist across shutdown and startup.

- Sample Initialization Parameter File  
	Oracle Database provides generally appropriate values in a sample text initialization parameter file. You can edit these Oracle-supplied initialization parameters and add others, depending upon your configuration and options and how you plan to tune the database.
- Text Initialization Parameter File Format  
	The text initialization parameter file specifies the values of parameters in name/value pairs.

See Also:

- " Determining the Global Database Name " for information about the `DB_NAME` parameter
- " Managing Initialization Parameters Using a Server Parameter File "
- " [About Initialization Parameter Files and Startup](starting-up-and-shutting-down.md) "

**Parent topic:** Specifying Initialization Parameters

##### 2.6.1.1 Sample Initialization Parameter File

Oracle Database provides generally appropriate values in a sample text initialization parameter file. You can edit these Oracle-supplied initialization parameters and add others, depending upon your configuration and options and how you plan to tune the database.

The sample text initialization parameter file is named `init.ora` and is found in the following location on most platforms:

```
ORACLE_HOME/dbs
```

The following is the content of the sample file:

```
##############################################################################
# Example INIT.ORA file
#
# This file is provided by Oracle Corporation to help you start by providing
# a starting point to customize your RDBMS installation for your site. 
# 
# NOTE: The values that are used in this file are only intended to be used
# as a starting point. You may want to adjust/tune those values to your
# specific hardware and needs. You may also consider using Database
# Configuration Assistant tool (DBCA) to create INIT file and to size your
# initial set of tablespaces based on the user input.
###############################################################################
 
# Change '<ORACLE_BASE>' to point to the oracle base (the one you specify at
# install time)
 
db_name='ORCL'
memory_target=1G
processes = 150
db_block_size=8192
db_domain=''
db_recovery_file_dest='<ORACLE_BASE>/flash_recovery_area'
db_recovery_file_dest_size=2G
diagnostic_dest='<ORACLE_BASE>'
dispatchers='(PROTOCOL=TCP) (SERVICE=ORCLXDB)'
open_cursors=300 
remote_login_passwordfile='EXCLUSIVE'
undo_tablespace='UNDOTBS1'
# You may want to ensure that control files are created on separate physical
# devices
control_files = (ora_control1, ora_control2)
compatible ='12.0.0'
```

**Parent topic:** About Initialization Parameters and Initialization Parameter Files

##### 2.6.1.2 Text Initialization Parameter File Format

The text initialization parameter file specifies the values of parameters in name/value pairs.

The text initialization parameter file (PFILE) must contain name/value pairs in one of the following forms:

- For parameters that accept only a single value:
	```
	parameter_name=value
	```
- For parameters that accept one or more values (such as the `CONTROL_FILES` parameter):
	```
	parameter_name=(value[,value] ...)
	```

Parameter values of type string must be enclosed in single quotes ('). Case (upper or lower) in file names is significant only if case is significant on the host operating system.

For parameters that accept multiple values, to enable you to easily copy and paste name/value pairs from the alert log, you can repeat a parameter on multiple lines, where each line contains a different value.

```
control_files='/u01/app/oracle/oradata/orcl/control01.ctl'
control_files='/u01/app/oracle/oradata/orcl/control02.ctl'
control_files='/u01/app/oracle/oradata/orcl/control03.ctl'
```

If you repeat a parameter that does not accept multiple values, then only the last value specified takes effect.

See Also:

- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=REFRN-GUID-6CCB7791-F995-474C-9339-8A3EE2C6777B) for more information about the content and syntax of the text initialization parameter file
- " [Alert Log](diagnosing-and-resolving-problems.md) "

**Parent topic:** About Initialization Parameters and Initialization Parameter Files

#### 2.6.2 Determining the Global Database Name

The global database name consists of the user-specified local database name and the location of the database within a network structure.

- Set the `DB_NAME` and `DB_DOMAIN` initialization parameters.

The `DB_NAME` initialization parameter determines the local name component of the database name, and the `DB_DOMAIN` parameter, which is optional, indicates the domain (logical location) within a network structure. The combination of the settings for these two parameters must form a database name that is unique within a network.

For example, to create a database with a global database name of `test.us.example.com`, edit the parameters of the new parameter file as follows:

```
DB_NAME = test
DB_DOMAIN = us.example.com
```

You can rename the `GLOBAL_NAME` of your database using the `ALTER DATABASE RENAME GLOBAL_NAME` statement. However, you must also shut down and restart the database after first changing the `DB_NAME` and `DB_DOMAIN` initialization parameters and recreating the control files. Recreating the control files is easily accomplished with the command `ALTER` `DATABASE` `BACKUP` `CONTROLFILE` `TO` `TRACE`. See [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=BRADV90011) for more information.

- DB\_NAME Initialization Parameter  
	The `DB_NAME` initialization parameter specifies a database identifier.
- DB\_DOMAIN Initialization Parameter  
	In a distributed database system, the `DB_DOMAIN` initialization parameter specifies the logical location of the database within the network structure.

See Also:

[Oracle Database Utilities](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=SUTIL014) for information about using the `DBNEWID` utility, which is another means of changing a database name

**Parent topic:** Specifying Initialization Parameters

##### 2.6.2.1 DB\_NAME Initialization Parameter

The `DB_NAME` initialization parameter specifies a database identifier.

`DB_NAME` must be set to a text string of no more than 8 characters. The database name must start with an alphabetic character. During database creation, the name provided for `DB_NAME` is recorded in the data files, redo log files, and control file of the database. If during database instance startup the value of the `DB_NAME` parameter (in the parameter file) and the database name in the control file are different, then the database does not start.

**Parent topic:** Determining the Global Database Name

##### 2.6.2.2 DB\_DOMAIN Initialization Parameter

In a distributed database system, the `DB_DOMAIN` initialization parameter specifies the logical location of the database within the network structure.

`DB_DOMAIN` is a text string that specifies the network domain where the database is created. If the database you are about to create will ever be part of a distributed database system, then give special attention to this initialization parameter before database creation. This parameter is optional.

**Parent topic:** Determining the Global Database Name

#### 2.6.3 Specifying a Fast Recovery Area

The Fast Recovery Area is a location in which Oracle Database can store and manage files related to backup and recovery. It is distinct from the database area, which is a location for the current database files (data files, control files, and online redo logs).

Specify the Fast Recovery Area with the following initialization parameters:

- `DB_RECOVERY_FILE_DEST`: Location of the Fast Recovery Area. This can be a directory, file system, or Automatic Storage Management (Oracle ASM) disk group.
	In an Oracle Real Application Clusters (Oracle RAC) environment, this location must be on a cluster file system, Oracle ASM disk group, or a shared directory configured through NFS.
- `DB_RECOVERY_FILE_DEST_SIZE`: Specifies the maximum total bytes to be used by the Fast Recovery Area. This initialization parameter must be specified before `DB_RECOVERY_FILE_DEST` is enabled.

In an Oracle RAC environment, the settings for these two parameters must be the same on all instances.

You cannot enable these parameters if you have set values for the `LOG_ARCHIVE_DEST` and `LOG_ARCHIVE_DUPLEX_DEST` parameters. You must disable those parameters before setting up the Fast Recovery Area. You can instead set values for the `LOG_ARCHIVE_DEST_` `n` parameters.

Oracle recommends using a Fast Recovery Area, because it can simplify backup and recovery operations for your database.

See Also:

[Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=BRADV8183) to learn how to create and use a Fast Recovery Area

**Parent topic:** Specifying Initialization Parameters

#### 2.6.4 Specifying Control Files

Every database has a control file, which contains entries that describe the structure of the database (such as its name, the timestamp of its creation, and the names and locations of its data files and redo files). The `CONTROL_FILES` initialization parameter specifies one or more names of control files, separated by commas.

- Set the `CONTROL_FILES` initialization parameter.

When you execute the `CREATE DATABASE` statement, the control files listed in the `CONTROL_FILES` parameter are created.

If you do not include `CONTROL_FILES` in the initialization parameter file, then Oracle Database creates a control file in the same directory as the initialization parameter file, using a default operating system–dependent file name. If you have enabled Oracle Managed Files, the database creates Oracle managed control files.

If you want the database to create new operating system files when creating database control files, the file names listed in the `CONTROL_FILES` parameter must not match any file names that currently exist on your system. If you want the database to reuse or overwrite existing files when creating database control files, ensure that the file names listed in the `CONTROL_FILES` parameter match the file names that are to be reused, and include a `CONTROLFILE` `REUSE` clause in the `CREATE` `DATABASE` statement.

Oracle strongly recommends you use at least two control files stored on separate physical disk drives for each database.

See Also:

- " [Managing Control Files](managing-control-files.md) "
- " Specifying Oracle Managed Files at Database Creation "

**Parent topic:** Specifying Initialization Parameters

#### 2.6.5 Specifying Database Block Sizes

The `DB_BLOCK_SIZE` initialization parameter specifies the standard block size for the database.

- Set the `DB_BLOCK_SIZE` initialization parameter.

This block size is used for the `SYSTEM` tablespace and by default in other tablespaces. Oracle Database can support up to four additional nonstandard block sizes.

- DB\_BLOCK\_SIZE Initialization Parameter  
	The most commonly used block size should be picked as the standard block size. In many cases, this is the only block size that you must specify.
- Nonstandard Block Sizes  
	You can create tablespaces of nonstandard block sizes.

**Parent topic:** Specifying Initialization Parameters

##### 2.6.5.1 DB\_BLOCK\_SIZE Initialization Parameter

The most commonly used block size should be picked as the standard block size. In many cases, this is the only block size that you must specify.

- Set the `DB_BLOCK_SIZE` initialization parameter.

Typically, `DB_BLOCK_SIZE` is set to either 4K or 8K. If you do not set a value for this parameter, then the default data block size is operating system specific, which is generally adequate.

You cannot change the block size after database creation except by re-creating the database. If the database block size is different from the operating system block size, then ensure that the database block size is a multiple of the operating system block size. For example, if your operating system block size is 2K (2048 bytes), the following setting for the `DB_BLOCK_SIZE` initialization parameter is valid:

```
DB_BLOCK_SIZE=4096
```

A larger data block size provides greater efficiency in disk and memory I/O (access and storage of data). Therefore, consider specifying a block size larger than your operating system block size if the following conditions exist:

- Oracle Database is on a large computer system with a large amount of memory and fast disk drives. For example, databases controlled by mainframe computers with vast hardware resources typically use a data block size of 4K or greater.
- The operating system that runs Oracle Database uses a small operating system block size. For example, if the operating system block size is 1K and the default data block size matches this, the database may be performing an excessive amount of disk I/O during normal operation. For best performance in this case, a database block should consist of multiple operating system blocks.
	See Also:
	Your operating system specific Oracle documentation for details about the default block size.

**Parent topic:** Specifying Database Block Sizes

##### 2.6.5.2 Nonstandard Block Sizes

You can create tablespaces of nonstandard block sizes.

To create tablespaces of nonstandard block sizes:

- Specify the `BLOCKSIZE` clause in a `CREATE TABLESPACE` statement.

These nonstandard block sizes can have any of the following power-of-two values: 2K, 4K, 8K, 16K or 32K. Platform-specific restrictions regarding the maximum block size apply, so some of these sizes may not be allowed on some platforms.

To use nonstandard block sizes, you must configure subcaches within the buffer cache area of the SGA memory for all of the nonstandard block sizes that you intend to use. The initialization parameters used for configuring these subcaches are described in " [Using Automatic Shared Memory Management](managing-memory.md) ".

The ability to specify multiple block sizes for your database is especially useful if you are transporting tablespaces between databases. You can, for example, transport a tablespace that uses a 4K block size from an OLTP environment to a data warehouse environment that uses a standard block size of 8K.

Note:

A 32K block size is valid only on 64-bit platforms.

Caution:

Oracle recommends against specifying a 2K block size when 4K sector size disks are in use, because performance degradation can occur. For an explanation, see " [Planning the Block Size of Redo Log Files](managing-the-redo-log.md) ".

See Also:

- " [Creating Tablespaces](managing-tablespaces.md) "
- " [Transporting Tablespaces Between Databases](transporting-data.md) "

**Parent topic:** Specifying Database Block Sizes

#### 2.6.6 Specifying the Maximum Number of Processes

The `PROCESSES` initialization parameter determines the maximum number of operating system processes that can be connected to Oracle Database concurrently.

- Set the `PROCESSES` initialization parameter.

The value of this parameter must be a minimum of one for each background process plus one for each user process. The number of background processes will vary according the database features that you are using. For example, if you are using Advanced Queuing or the file mapping feature, then you will have additional background processes. If you are using Automatic Storage Management, then add three additional processes for the database instance.

If you plan on running 50 user processes, a good estimate would be to set the `PROCESSES` initialization parameter to 70.

**Parent topic:** Specifying Initialization Parameters

#### 2.6.7 Specifying the DDL Lock Timeout

You can specify the amount of time that blocking DDL statements wait for locks.

A data definition language (DDL) statement is either nonblocking or blocking, and both types of DDL statements require exclusive locks on internal structures. If these locks are unavailable when a DDL statement runs, then nonblocking and blocking DDL statements behave differently:

- Nonblocking DDL waits until every concurrent DML transaction that references the object affected by the DDL either commits or rolls back.
- Blocking DDL fails, though it might have succeeded if it had been executed subseconds later when the locks become available.

To enable blocking DDL statements to wait for locks, specify a DDL lock timeout—the number of seconds a DDL command waits for its required locks before failing.

- To specify a DDL lock timeout, set the `DDL_LOCK_TIMEOUT` parameter.

The permissible range of values for `DDL_LOCK_TIMEOUT` is 0 to 1,000,000. The default is 0. You can set `DDL_LOCK_TIMEOUT` at the system level, or at the session level with an `ALTER` `SESSION` statement.

Note:

The `DDL_LOCK_TIMEOUT` parameter does not affect nonblocking DDL statements.

#### 2.6.8 Specifying the Method of Undo Space Management

Every Oracle Database must have a method of maintaining information that is used to undo changes to the database. Such information consists of records of the actions of transactions, primarily before they are committed. Collectively these records are called undo data.

To set up an environment for automatic undo management using an undo tablespace.

- Set the `UNDO_MANAGEMENT` initialization parameter to `AUTO`, which is the default.

- UNDO\_MANAGEMENT Initialization Parameter  
	The `UNDO_MANAGEMENT` initialization parameter determines whether an instance starts in automatic undo management mode, which stores undo in an undo tablespace. Set this parameter to `AUTO` to enable automatic undo management mode. `AUTO` is the default if the parameter is omitted or is null.
- UNDO\_TABLESPACE Initialization Parameter  
	The `UNDO_TABLESPACE` initialization parameter enables you to override that default undo tablespace for an instance.

See Also:

[Managing Undo](managing-undo.md)

**Parent topic:** Specifying Initialization Parameters

##### 2.6.8.1 UNDO\_MANAGEMENT Initialization Parameter

The `UNDO_MANAGEMENT` initialization parameter determines whether an instance starts in automatic undo management mode, which stores undo in an undo tablespace. Set this parameter to `AUTO` to enable automatic undo management mode. `AUTO` is the default if the parameter is omitted or is null.

**Parent topic:** Specifying the Method of Undo Space Management

##### 2.6.8.2 UNDO\_TABLESPACE Initialization Parameter

The `UNDO_TABLESPACE` initialization parameter enables you to override that default undo tablespace for an instance.

When an instance starts up in automatic undo management mode, it attempts to select an undo tablespace for storage of undo data. If the database was created in automatic undo management mode, then the default undo tablespace (either the system-created `SYS_UNDOTBS` tablespace or the user-specified undo tablespace) is the undo tablespace used at instance startup. You can override this default for the instance by specifying a value for the `UNDO_TABLESPACE` initialization parameter. This parameter is especially useful for assigning a particular undo tablespace to an instance in an Oracle Real Application Clusters environment.

If no undo tablespace is specified by the `UNDO_TABLESPACE` initialization parameter, then the first available undo tablespace in the database is chosen. If no undo tablespace is available, then the instance starts without an undo tablespace, and undo data is written to the `SYSTEM` tablespace. You should avoid running in this mode.

Note:

When using the `CREATE` `DATABASE` statement to create a database, do not include an `UNDO_TABLESPACE` parameter in the initialization parameter file. Instead, include an `UNDO` `TABLESPACE` clause in the `CREATE` `DATABASE` statement.

**Parent topic:** Specifying the Method of Undo Space Management

#### 2.6.9 Specifying the Database Compatibility Level

The `COMPATIBLE` initialization parameter controls the database compatibility level.

- Set the `COMPATIBLE` initialization parameter to a release number.

- About the COMPATIBLE Initialization Parameter  
	The `COMPATIBLE` initialization parameter enables or disables the use of features in the database that affect file format on disk. For example, if you create an Oracle Database 19c database, but specify `COMPATIBLE=12.0.0` in the initialization parameter file, then features that require Oracle Database 19c compatibility generate an error if you try to use them. Such a database is said to be at the 12.0.0 compatibility level.

**Parent topic:** Specifying Initialization Parameters

##### 2.6.9.1 About the COMPATIBLE Initialization Parameter

The `COMPATIBLE` initialization parameter enables or disables the use of features in the database that affect file format on disk. For example, if you create an Oracle Database 19c database, but specify `COMPATIBLE=12.0.0` in the initialization parameter file, then features that require Oracle Database 19c compatibility generate an error if you try to use them. Such a database is said to be at the 12.0.0 compatibility level.

You can advance the compatibility level of your database by changing the `COMPATIBLE` initialization parameter. If you do, then there is no way to start the database using a lower compatibility level setting, except by doing a point-in-time recovery to a time before the compatibility was advanced.

The default value for the `COMPATIBLE` parameter is the release number of the most recent major release.

Note:

- For Oracle Database 19c, the default value of the `COMPATIBLE` parameter is `19.0.0`. The minimum value is `12.0.0`. If you create an Oracle Database using the default value, then you can immediately use all the new features in this release, and you can never downgrade the database.
- When you set this parameter in a server parameter file (SPFILE) using the `ALTER SYSTEM` statement, you must specify `SCOPE=SPFILE`, and you must restart the database for the change to take effect.
- The `COMPATIBLE` initialization parameter must be specified as at least three decimal numbers separated by a dot, such as `19.0.0`.

See Also:

- [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=UPGRD12473) for a detailed discussion of database compatibility and the `COMPATIBLE` initialization parameter
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=REFRN10019)
- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=BRADV80055) for information about point-in-time recovery of your database

**Parent topic:** Specifying the Database Compatibility Level

#### 2.6.10 Setting the License Parameter

If you use named user licensing, Oracle Database can help you enforce this form of licensing. You can set a limit on the number of users created in the database. Once this limit is reached, you cannot create more users.

Note:

This mechanism assumes that each person accessing the database has a unique user name and that no people share a user name. Therefore, so that named user licensing can help you ensure compliance with your Oracle license agreement, do not allow multiple users to log in using the same user name.

To limit the number of users created in a database, set the `LICENSE_MAX_USERS` initialization parameter in the database initialization parameter file.

The following example sets the `LICENSE_MAX_USERS` initialization parameter:

```
LICENSE_MAX_USERS = 200
```

Note:

Oracle no longer offers licensing by the number of concurrent sessions. Therefore the `LICENSE_MAX_SESSIONS` and `LICENSE_SESSIONS_WARNING` initialization parameters are no longer needed and have been deprecated.

**Parent topic:** Specifying Initialization Parameters

### 2.7 Managing Initialization Parameters Using a Server Parameter File

Initialization parameters for the Oracle Database have traditionally been stored in a text initialization parameter file. For better manageability, you can choose to maintain initialization parameters in a binary server parameter file that is persistent across database startup and shutdown.

- What Is a Server Parameter File?  
	A server parameter file can be thought of as a repository for initialization parameters that is maintained on the system running the Oracle Database server. It is, by design, a server-side initialization parameter file.
- Migrating to a Server Parameter File  
	If you are currently using a text initialization parameter file, then you can migrate to a server parameter file.
- Server Parameter File Default Names and Locations  
	Oracle recommends that you allow the database to give the SPFILE the default name and store it in the default location. This eases administration of your database. For example, the `STARTUP` command assumes this default location to read the SPFILE.
- Creating a Server Parameter File  
	You use the `CREATE SPFILE` statement to create a server parameter file. You must have the `SYSDBA`, `SYSOPER`, or `SYSBACKUP` administrative privilege to execute this statement.
- The SPFILE Initialization Parameter  
	The `SPFILE` initialization parameter contains the name of the current server parameter file.
- Changing Initialization Parameter Values  
	You can change initialization parameter values to affect the operation of a database instance.
- Clearing Initialization Parameter Values  
	You can use the `ALTER` `SYSTEM` `RESET` statement to clear an initialization parameter value. When you do so, the initialization parameter value is changed to its default value or its startup value.
- Exporting the Server Parameter File  
	You can use the `CREATE PFILE` statement to export a server parameter file (SPFILE) to a text initialization parameter file.
- Backing Up the Server Parameter File  
	You can create a backup of your server parameter file (SPFILE) by exporting it. If the backup and recovery strategy for your database is implemented using Recovery Manager (RMAN), then you can use RMAN to create a backup of the SPFILE. The SPFILE is backed up automatically by RMAN when you back up your database, but RMAN also enables you to specifically create a backup of the currently active SPFILE.
- Recovering a Lost or Damaged Server Parameter File  
	You can recover the server parameter file (SPFILE). If your server parameter file (SPFILE) becomes lost or corrupted, then the current instance may fail, or the next attempt at starting the database instance may fail.
- Methods for Viewing Parameter Settings  
	You can view parameter settings using several different methods.

**Parent topic:** Creating and Configuring an Oracle Database

#### 2.7.1 What Is a Server Parameter File?

A server parameter file can be thought of as a repository for initialization parameters that is maintained on the system running the Oracle Database server. It is, by design, a server-side initialization parameter file.

Initialization parameters stored in a server parameter file are persistent, in that any changes made to the parameters while an instance is running can persist across instance shutdown and startup. This arrangement eliminates the need to manually update initialization parameters to make persistent any changes effected by `ALTER SYSTEM` statements. It also provides a basis for self-tuning by the Oracle Database server.

A server parameter file is initially built from a text initialization parameter file using the `CREATE SPFILE` statement. (It can also be created directly by the Database Configuration Assistant.) The server parameter file is a binary file that cannot be edited using a text editor. Oracle Database provides other interfaces for viewing and modifying parameter settings in a server parameter file.

Note:

Although you can open the binary server parameter file with a text editor and view its text, do not manually edit it. Doing so will corrupt the file. You will not be able to start your instance, and if the instance is running, it could fail.

When you issue a `STARTUP` command with no `PFILE` clause, the Oracle instance searches an operating system–specific default location for a server parameter file from which to read initialization parameter settings. If no server parameter file is found, the instance searches for a text initialization parameter file. If a server parameter file exists but you want to override it with settings in a text initialization parameter file, you must specify the `PFILE` clause when issuing the `STARTUP` command. Instructions for starting an instance using a server parameter file are contained in " [Starting Up a Database](starting-up-and-shutting-down.md) ".

**Parent topic:** Managing Initialization Parameters Using a Server Parameter File

#### 2.7.2 Migrating to a Server Parameter File

If you are currently using a text initialization parameter file, then you can migrate to a server parameter file.

To migrate to a server parameter file:

1. If the initialization parameter file is located on a client system, then transfer the file (for example, FTP) from the client system to the server system.
	Note:
	If you are migrating to a server parameter file in an Oracle Real Application Clusters environment, you must combine all of your instance-specific initialization parameter files into a single initialization parameter file. Instructions for doing this and other actions unique to using a server parameter file for instances that are part of an Oracle Real Application Clusters installation are discussed in [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=RACAD020) and in your platform-specific Oracle Real Application Clusters Installation Guide.
2. Create a server parameter file in the default location using the `CREATE SPFILE FROM PFILE` statement. See " Creating a Server Parameter File " for instructions.
	This statement reads the text initialization parameter file to create a server parameter file. The database does not have to be started to issue a `CREATE SPFILE` statement.
3. Start up or restart the instance.
	The instance finds the new SPFILE in the default location and starts up with it.

**Parent topic:** Managing Initialization Parameters Using a Server Parameter File

#### 2.7.3 Server Parameter File Default Names and Locations

Oracle recommends that you allow the database to give the SPFILE the default name and store it in the default location. This eases administration of your database. For example, the `STARTUP` command assumes this default location to read the SPFILE.

The following table shows the default name and location for both the text initialization parameter file (PFILE) and server parameter file (SPFILE) for the UNIX, Linux, and Windows platforms, both with and without the presence of Oracle Automatic Storage Management (Oracle ASM). The table assumes that the SPFILE is a file.

Table 2-3 PFILE and SPFILE Default Names and Locations on UNIX, Linux, and Windows

| Platform | PFILE Default Name | SPFILE Default Name | PFILE Default Location | SPFILE Default Location |
| --- | --- | --- | --- | --- |
| UNIX and Linux | `init` `ORACLE_SID``.ora` | `spfile` `ORACLE_SID``.ora` | Oracle\_Home `/dbs` or the same location as the data files | Without Oracle ASM:  Oracle\_Home `/dbs` or the same location as the data files  When Oracle ASM is present:  In the same disk group as the data files (assuming the database was created with DBCA) |
| Windows | `init` `ORACLE_SID``.ora` | `spfile` `ORACLE_SID``.ora` | Oracle\_Home `\database` | Without Oracle ASM:  OH `\database`  When Oracle ASM is present:  In the same disk group as the data files (assuming the database was created with DBCA) |

Note:

Upon startup, the instance first searches for an SPFILE named `spfile` `ORACLE_SID`.`ora`, and if not found, searches for `spfile.ora`. Using `spfile.ora` enables all Real Application Cluster (Oracle RAC) instances to use the same server parameter file.

If neither SPFILE is found, the instance searches for the text initialization parameter file `init` `ORACLE_SID`.`ora`.

If you create an SPFILE in a location other than the default location, you must create in the default PFILE location a "stub" PFILE that points to the server parameter file. For more information, see " [Starting Up a Database](starting-up-and-shutting-down.md) ".

When you create the database with DBCA when Oracle ASM is present, DBCA places the SPFILE in an Oracle ASM disk group, and also causes this stub PFILE to be created.

**Parent topic:** Managing Initialization Parameters Using a Server Parameter File

#### 2.7.4 Creating a Server Parameter File

You use the `CREATE SPFILE` statement to create a server parameter file. You must have the `SYSDBA`, `SYSOPER`, or `SYSBACKUP` administrative privilege to execute this statement.

To create a server parameter file:

- Run the `CREATE SPFILE` statement.

Note:

When you use the Database Configuration Assistant to create a database, it automatically creates a server parameter file for you.

The `CREATE SPFILE` statement can be executed before or after instance startup. However, if the instance has been started using a server parameter file, an error is raised if you attempt to re-create the same server parameter file that is currently being used by the instance.

You can create a server parameter file (SPFILE) from an existing text initialization parameter file or from memory. Creating the SPFILE from memory means copying the current values of initialization parameters in the running instance to the SPFILE.

The following example creates a server parameter file from text initialization parameter file `/u01/oracle/dbs/init.ora`. In this example no `SPFILE` name is specified, so the file is created with the platform-specific default name and location shown in Table 2-3.

```
CREATE SPFILE FROM PFILE='/u01/oracle/dbs/init.ora';
```

The next example illustrates creating a server parameter file and supplying a name and location.

```
CREATE SPFILE='/u01/oracle/dbs/test_spfile.ora'
       FROM PFILE='/u01/oracle/dbs/test_init.ora';
```

The next example illustrates creating a server parameter file in the default location from the current values of the initialization parameters in memory.

```
CREATE SPFILE FROM MEMORY;
```

Whether you use the default SPFILE name and default location or specify an SPFILE name and location, if an SPFILE of the same name already exists in the location, it is overwritten without a warning message.

When you create an SPFILE from a text initialization parameter file, comments specified on the same lines as a parameter setting in the initialization parameter file are maintained in the SPFILE. All other comments are ignored.

**Parent topic:** Managing Initialization Parameters Using a Server Parameter File

#### 2.7.5 The SPFILE Initialization Parameter

The `SPFILE` initialization parameter contains the name of the current server parameter file.

When the default server parameter file is used by the database—that is, you issue a `STARTUP` command and do not specify a `PFILE` parameter—the value of `SPFILE` is internally set by the server. The SQL\*Plus command `SHOW PARAMETERS SPFILE` (or any other method of querying the value of a parameter) displays the name of the server parameter file that is currently in use.

**Parent topic:** Managing Initialization Parameters Using a Server Parameter File

#### 2.7.6 Changing Initialization Parameter Values

You can change initialization parameter values to affect the operation of a database instance.

- About Changing Initialization Parameter Values  
	The `ALTER SYSTEM` statement enables you to set, change, or restore to default the values of initialization parameters. If you are using a text initialization parameter file, the `ALTER SYSTEM` statement changes the value of a parameter only for the current instance, because there is no mechanism for automatically updating text initialization parameters on disk. You must update them manually to be passed to a future instance. Using a server parameter file overcomes this limitation.
- Setting or Changing Initialization Parameter Values  
	With a server parameter file, use the `SET` clause of the `ALTER SYSTEM` statement to set or change initialization parameter values.

**Parent topic:** Managing Initialization Parameters Using a Server Parameter File

##### 2.7.6.1 About Changing Initialization Parameter Values

The `ALTER SYSTEM` statement enables you to set, change, or restore to default the values of initialization parameters. If you are using a text initialization parameter file, the `ALTER SYSTEM` statement changes the value of a parameter only for the current instance, because there is no mechanism for automatically updating text initialization parameters on disk. You must update them manually to be passed to a future instance. Using a server parameter file overcomes this limitation.

There are two kinds of initialization parameters:

- Dynamic initialization parameters can be changed for the current Oracle Database instance. The changes take effect immediately.
- Static initialization parameters cannot be changed for the current instance. You must change these parameters in the text initialization file or server parameter file and then restart the database before changes take effect.

**Parent topic:** Changing Initialization Parameter Values

##### 2.7.6.2 Setting or Changing Initialization Parameter Values

With a server parameter file, use the `SET` clause of the `ALTER SYSTEM` statement to set or change initialization parameter values.

- Run an `ALTER SYSTEM SET` statement.

For example, the following statement changes the maximum number of failed login attempts before the connection is dropped. It includes a comment, and explicitly states that the change is to be made only in the server parameter file.

```
ALTER SYSTEM SET SEC_MAX_FAILED_LOGIN_ATTEMPTS=3
                 COMMENT='Reduce from 10 for tighter security.'
                 SCOPE=SPFILE;
```

The next example sets a complex initialization parameter that takes a list of attributes. Specifically, the parameter value being set is the `LOG_ARCHIVE_DEST_n` initialization parameter. This statement could change an existing setting for this parameter or create a new archive destination.

```
ALTER SYSTEM 
     SET LOG_ARCHIVE_DEST_4='LOCATION=/u02/oracle/rbdb1/',MANDATORY,'REOPEN=2'
         COMMENT='Add new destination on Nov 29'
         SCOPE=SPFILE;
```

When a value consists of a list of parameters, you cannot edit individual attributes by the position or ordinal number. You must specify the complete list of values each time the parameter is updated, and the new list completely replaces the old list.

- The SCOPE Clause in ALTER SYSTEM SET Statements  
	The optional `SCOPE` clause in `ALTER SYSTEM SET` statements specifies the scope of an initialization parameter change.

**Parent topic:** Changing Initialization Parameter Values

###### 2.7.6.2.1 The SCOPE Clause in ALTER SYSTEM SET Statements

The optional `SCOPE` clause in `ALTER SYSTEM SET` statements specifies the scope of an initialization parameter change.

| SCOPE Clause | Description |
| --- | --- |
| `SCOPE = SPFILE ` | The change is applied in the server parameter file only. The effect is as follows:  - No change is made to the current instance. - For both dynamic and static parameters, the change is effective at the next startup and is persistent.  This is the only `SCOPE` specification allowed for static parameters. |
| `SCOPE = MEMORY ` | The change is applied in memory only. The effect is as follows:  - The change is made to the current instance and is effective immediately. - For dynamic parameters, the effect is immediate, but it is not persistent because the server parameter file is not updated.  For static parameters, this specification is not allowed. |
| `SCOPE = BOTH ` | The change is applied in both the server parameter file and memory. The effect is as follows:  - The change is made to the current instance and is effective immediately. - For dynamic parameters, the effect is persistent because the server parameter file is updated.  For static parameters, this specification is not allowed. |

It is an error to specify `SCOPE=SPFILE` or `SCOPE=BOTH` if the instance did not start up with a server parameter file. The default is `SCOPE=BOTH` if a server parameter file was used to start up the instance, and `MEMORY` if a text initialization parameter file was used to start up the instance.

For dynamic parameters, you can also specify the `DEFERRED` keyword. When specified, the change is effective only for future sessions.

When you specify `SCOPE` as `SPFILE` or `BOTH`, an optional `COMMENT` clause lets you associate a text string with the parameter update. The comment is written to the server parameter file.

**Parent topic:** Setting or Changing Initialization Parameter Values

#### 2.7.7 Clearing Initialization Parameter Values

You can use the `ALTER` `SYSTEM` `RESET` statement to clear an initialization parameter value. When you do so, the initialization parameter value is changed to its default value or its startup value.

The `ALTER SYSTEM RESET` statement includes a `SCOPE` clause. When executed in a non-CDB or a multitenant container database (CDB) root, the `ALTER SYSTEM RESET` statement and `SCOPE` clause behave differently than when the statement is executed in a pluggable database (PDB), an application root, or an application PDB.

The startup value of a parameter is the value of the parameter in memory after the instance's startup or PDB open has completed. This value can be seen in the `VALUE` and `DISPLAY_VALUE` columns in the `V$SYSTEM_PARAMETER` view immediately after startup. The startup value can be different from the value in the spfile or the default value (if the parameter is not set in the spfile), since the value of the parameter can be adjusted internally at startup.

The `SCOPE` values for the `ALTER SYSTEM RESET` statement behave as follows in a non-CDB and in the `CDB$ROOT` of a CDB:

- `SCOPE=SPFILE`: If an instance is using spfile, removes the parameter from the spfile; the default value takes effect upon the next instance startup.
- `SCOPE=MEMORY`: The startup value takes effect immediately. However, the change is not stored in instance's spfile and will be lost upon instance restart.
- `SCOPE=BOTH`: If an instance is using spfile, removes the parameter from the spfile; the default value takes effect immediately and the change is available across instance restart.

Note:

`SCOPE=BOTH` changes the way `SCOPE=MEMORY` behaves. After `SCOPE=BOTH` is issued, `SCOPE=MEMORY` always resets the parameter to the default value.

The `SCOPE` values for the `ALTER SYSTEM RESET` statement behave as follows in a PDB, an application root, or an application PDB:

- `SCOPE=SPFILE`: Removes the parameter from the container's spfile; the container will inherit the parameter value from its root upon the next PDB open.
- `SCOPE=MEMORY`: There are two cases:
	- The parameter is present in container's spfile when the container is opened. The parameter value is updated to the startup value for the parameter. This change is not stored in container’s spfile and will be lost upon the next container open.
		- The parameter is not present in container’s spfile when the container is opened. The container starts inheriting the parameter value from its root.
- `SCOPE=BOTH`: Removes the parameter from the container’s spfile; the container will inherit the parameter value from its root.

Note:

- `SCOPE=BOTH` changes the way `SCOPE=MEMORY` behaves. After `SCOPE=BOTH` is issued, the container always inherits the parameter value from its root when `SCOPE=MEMORY` is issued.
- In a case where a container inherits a parameter value from its root, a PDB inherits the value from `CDB$ROOT`. In an application container, an application PDB inherits the parameter value from its application root, and an application root inherits the parameter value from `CDB$ROOT`.

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=SQLRF00902) for information about the `ALTER` `SYSTEM` command
- [Oracle Multitenant Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=MULTI-GUID-93F1E584-D309-4301-82E0-AD0E60D4977C)

**Parent topic:** Managing Initialization Parameters Using a Server Parameter File

#### 2.7.8 Exporting the Server Parameter File

You can use the `CREATE PFILE` statement to export a server parameter file (SPFILE) to a text initialization parameter file.

- Run a `CREATE PFILE` statement.

Exporting the server parameter file might be necessary for several reasons:

- For diagnostic purposes, listing all of the parameter values currently used by an instance. This is analogous to the SQL\*Plus `SHOW PARAMETERS` command or selecting from the `V$PARAMETER` or `V$PARAMETER2` views.
- To modify the server parameter file by first exporting it, editing the resulting text file, and then re-creating it using the `CREATE SPFILE` statement

The exported file can also be used to start up an instance using the `PFILE` clause.

You must have the `SYSDBA`, `SYSOPER`, or `SYSBACKUP` administrative privilege to execute the `CREATE PFILE` statement. The exported file is created on the database server system. It contains any comments associated with the parameter in the same line as the parameter setting.

The following example creates a text initialization parameter file from the SPFILE:

```
CREATE PFILE FROM SPFILE;
```

Because no names were specified for the files, the database creates an initialization parameter file with a platform-specific name, and it is created from the platform-specific default server parameter file.

The following example creates a text initialization parameter file from a server parameter file, but in this example the names of the files are specified:

```
CREATE PFILE='/u01/oracle/dbs/test_init.ora'
  FROM SPFILE='/u01/oracle/dbs/test_spfile.ora';
```

Note:

An alternative is to create a PFILE from the current values of the initialization parameters in memory. The following is an example of the required command:

```
CREATE PFILE='/u01/oracle/dbs/test_init.ora' FROM MEMORY;
```

**Parent topic:** Managing Initialization Parameters Using a Server Parameter File

#### 2.7.9 Backing Up the Server Parameter File

You can create a backup of your server parameter file (SPFILE) by exporting it. If the backup and recovery strategy for your database is implemented using Recovery Manager (RMAN), then you can use RMAN to create a backup of the SPFILE. The SPFILE is backed up automatically by RMAN when you back up your database, but RMAN also enables you to specifically create a backup of the currently active SPFILE.

- Back up the server parameter file either by exporting it or by using RMAN.

See Also:

" Exporting the Server Parameter File "

[Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=BRADV89519)

**Parent topic:** Managing Initialization Parameters Using a Server Parameter File

#### 2.7.10 Recovering a Lost or Damaged Server Parameter File

You can recover the server parameter file (SPFILE). If your server parameter file (SPFILE) becomes lost or corrupted, then the current instance may fail, or the next attempt at starting the database instance may fail.

There are several ways to recover the SPFILE:

- If the instance is running, issue the following command to re-create the SPFILE from the current values of initialization parameters in memory:
	```
	CREATE SPFILE FROM MEMORY;
	```
	This command creates the SPFILE with the default name and in the default location. You can also create the SPFILE with a new name or in a specified location. See " Creating a Server Parameter File " for examples.
- If you have a valid text initialization parameter file (PFILE), re-create the SPFILE from the PFILE with the following statement:
	```
	CREATE SPFILE FROM PFILE;
	```
	This command assumes that the PFILE is in the default location and has the default name. See " Creating a Server Parameter File " for the command syntax to use when the PFILE is not in the default location or has a nondefault name.
- Restore the SPFILE from backup.
	See " Backing Up the Server Parameter File " for more information.
- If none of the previous methods are possible in your situation, perform these steps:
	1. Create a text initialization parameter file (PFILE) from the parameter value listings in the alert log.
		When an instance starts up, the initialization parameters used for startup are written to the alert log. You can copy and paste this section from the text version of the alert log (without XML tags) into a new PFILE.
		See " [Viewing the Alert Log](diagnosing-and-resolving-problems.md) " for more information.
		2. Create the SPFILE from the PFILE.
		See " Creating a Server Parameter File " for instructions.

Read/Write Errors During a Parameter Update

If an error occurs while reading or writing the server parameter file during a parameter update, the error is reported in the alert log and all subsequent parameter updates to the server parameter file are ignored. At this point, you can take one of the following actions:

- Shut down the instance, recover the server parameter file and described earlier in this section, and then restart the instance.
- Continue to run the database if you do not care that subsequent parameter updates will not be persistent.

**Parent topic:** Managing Initialization Parameters Using a Server Parameter File

#### 2.7.11 Methods for Viewing Parameter Settings

You can view parameter settings using several different methods.

| Method | Description |
| --- | --- |
| `SHOW PARAMETERS ` | This SQL\*Plus command displays the values of initialization parameters in effect for the current session. |
| `SHOW SPPARAMETERS` | This SQL\*Plus command displays the values of initialization parameters in the server parameter file (SPFILE). |
| `CREATE PFILE` | This SQL statement creates a text initialization parameter file (PFILE) from the SPFILE or from the current in-memory settings. You can then view the PFILE with any text editor. |
| `V$PARAMETER` | This view displays the values of initialization parameters in effect for the current session. |
| `V$PARAMETER2` | This view displays the values of initialization parameters in effect for the current session. It is easier to distinguish list parameter values in this view because each list parameter value appears in a separate row. |
| `V$SYSTEM_PARAMETER` | This view displays the values of initialization parameters in effect for the instance. A new session inherits parameter values from the instance-wide values. |
| `V$SYSTEM_PARAMETER2` | This view displays the values of initialization parameters in effect for the instance. A new session inherits parameter values from the instance-wide values. It is easier to distinguish list parameter values in this view because each list parameter value appears in a separate row. |
| `V$SPPARAMETER ` | This view displays the current contents of the SPFILE. The view returns `FALSE` values in the `ISSPECIFIED` column if an SPFILE is not being used by the instance. |

See Also:

[Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=REFRN003) for a complete description of views

**Parent topic:** Managing Initialization Parameters Using a Server Parameter File

### 2.8 Managing Application Workloads with Database Services

A database service is a named representation of one or more database instances. Services enable you to group database workloads and route a particular work request to an appropriate instance.

- Database Services  
	A database service represents a single database. This database can be a single-instance database or an Oracle Real Application Clusters (Oracle RAC) database with multiple concurrent database instances. A global database service is a service provided by multiple databases synchronized through data replication.
- Global Data Services  
	Starting with Oracle Database 12c, you can use Global Data Services (GDS) for workload management involving multiple Oracle databases. GDS enables administrators to automatically and transparently manage client workloads across replicated databases that offer common services. These common services are known as global services.
- Database Service Data Dictionary Views  
	You can query data dictionary views to find information about database services.

**Parent topic:** Creating and Configuring an Oracle Database

#### 2.8.1 Database Services

A database service represents a single database. This database can be a single-instance database or an Oracle Real Application Clusters (Oracle RAC) database with multiple concurrent database instances. A global database service is a service provided by multiple databases synchronized through data replication.

- About Database Services  
	Database services divide workloads for a single database into mutually disjoint groupings.
- Database Services and Performance  
	Database services offer an extra dimension in performance tuning.
- Oracle Database Features That Use Database Services  
	Several Oracle Database features support database services.
- Creating Database Services  
	There are a few ways to create database services, depending on your database configuration.

**Parent topic:** Managing Application Workloads with Database Services

##### 2.8.1.1 About Database Services

Database services divide workloads for a single database into mutually disjoint groupings.

Each database service represents a workload with common attributes, service-level thresholds, and priorities. The grouping is based on attributes of work that might include the application function to be used, the priority of execution for the application function, the job class to be managed, or the data range used in the application function or job class. For example, the Oracle E-Business Suite defines a database service for each responsibility, such as general ledger, accounts receivable, order entry, and so on. When you configure database services, you give each service a unique name, associated performance goals, and associated importance. The database services are tightly integrated with Oracle Database and are maintained in the data dictionary.

Connection requests can include a database service name. Thus, middle-tier applications and client/server applications use a service by specifying the database service as part of the connection in TNS connect data. If no database service name is included and the Net Services file listener.ora designates a default database service, then the connection uses the default database service.

Database services enable you to configure a workload for a single database, administer it, enable and disable it, and measure the workload as a single entity. You can do this using standard tools such as the Database Configuration Assistant (DBCA), Oracle Net Configuration Assistant, and Oracle Enterprise Manager Cloud Control (Cloud Control). Cloud Control supports viewing and operating services as a whole, with drill down to the instance-level when needed.

In an Oracle Real Application Clusters (Oracle RAC) environment, a database service can span one or more instances and facilitate workload balancing based on transaction performance. This capability provides end-to-end unattended recovery, rolling changes by workload, and full location transparency. Oracle RAC also enables you to manage several database service features with Cloud Control, the DBCA, and the Server Control utility (`SRVCTL`).

Database services describe applications, application functions, and data ranges as either functional services or data-dependent services. Functional services are the most common mapping of workloads. Sessions using a particular function are grouped together. In contrast, data-dependent routing routes sessions to database services based on data keys. The mapping of work requests to database services occurs in the object relational mapping layer for application servers and TP monitors. For example, in Oracle RAC, these ranges can be completely dynamic and based on demand because the database is shared.

In addition to database services that are used by applications, Oracle Database also supports two internal database services: `SYS$BACKGROUND` is used by the background processes only, and `SYS$USERS` is the default database service for user sessions that are not associated with services.

Using database services requires no changes to your application code. Client-side work can connect to a named database service. Server-side work, such as Oracle Scheduler, parallel execution, and Oracle Database Advanced Queuing, set the database service name as part of the workload definition. Work requests executing under a database service inherit the performance thresholds for the service and are measured as part of the service.

See Also:

- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=CNCPT9855)
- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=RACAD841) for information about using services in an Oracle RAC environment
- [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=NETAG002) for information on connecting to a service
- The Cloud Control online help

**Parent topic:** Database Services

##### 2.8.1.2 Database Services and Performance

Database services offer an extra dimension in performance tuning.

Tuning by "service and SQL" can replace tuning by "session and SQL" in the majority of systems where all sessions are anonymous and shared. With database services, workloads are visible and measurable. Resource consumption and waits are attributable by application. Additionally, resources assigned to database services can be augmented when loads increase or decrease. This dynamic resource allocation enables a cost-effective solution for meeting demands as they occur. For example, database services are measured automatically, and the performance is compared to service-level thresholds. Performance violations are reported to Cloud Control, enabling the execution of automatic or scheduled solutions.

**Parent topic:** Database Services

##### 2.8.1.3 Oracle Database Features That Use Database Services

Several Oracle Database features support database services.

The Automatic Workload Repository (AWR) manages the performance of services. AWR records database service performance, including execution times, wait classes, and resources consumed by services. AWR alerts warn when database service response time thresholds are exceeded. The dynamic views report current service performance metrics with one hour of history. Each database service has quality-of-service thresholds for response time and CPU consumption.

In addition, the Database Resource Manager can map database services to consumer groups. Therefore, you can automatically manage the priority of one database service relative to others. You can use consumer groups to define relative priority in terms of either ratios or resource consumption.

You also can specify an edition attribute for a database service. Editions make it possible to have two or more versions of the same objects in the database. When you specify an edition attribute for a database service, all subsequent connections that specify the database service use this edition as the initial session edition.

Specifying an edition as a database service attribute can make it easier to manage resource usage. For example, database services associated with an edition can be placed on a separate instance in an Oracle RAC environment, and the Database Resource Manager can manage resources used by different editions by associating resource plans with the corresponding database services.

For Oracle Scheduler, you optionally assign a database service when you create a job class. During execution, jobs are assigned to job classes, and job classes can run within database services. Using database services with job classes ensures that the work executed by the job scheduler is identified for workload management and performance tuning.

For parallel query and parallel DML, the query coordinator connects to a database service just like any other client. The parallel query processes inherit the database service for the duration of the execution. At the end of query execution, the parallel execution processes revert to the default database service.

**Parent topic:** Database Services

##### 2.8.1.4 Creating Database Services

There are a few ways to create database services, depending on your database configuration.

Note:

Starting with Oracle Database 19c, customer use of the `SERVICE_NAMES` parameter is deprecated. It can be desupported in a future release. To manage your services, Oracle recommends that you use the `SRVCTL` or `GDSCTL` command line utilities, or the `DBMS_SERVICE` package.

Note:

This section describes creating services locally. You can also create services to operate globally. See " Global Data Services " for more information.

To create a database service:

- If your single-instance database is being managed by Oracle Restart, use the `SRVCTL` utility to create the database service.
	```
	srvctl add service -db db_unique_name -service service_name
	```
- If your single-instance database is not being managed by Oracle Restart, do one of the following:
	- Append the desired database service name to the `SERVICE_NAMES` parameter.
		- Call the `DBMS_SERVICE.CREATE_SERVICE` package procedure.
- (Optional) Define database service attributes with Cloud Control or with `DBMS_SERVICE.MODIFY_SERVICE`.

Oracle Net Listener (the listener) receives incoming client connection requests and manages the traffic of these requests to the database server. The listener handles connections for registered services, and it supports dynamic service registration.

See Also:

- [Configuring Automatic Restart of an Oracle Database](configuring-automatic-restart-of-an-oracle-database.md) for information about Oracle Restart
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=ARPLS092) for information about the `DBMS_SERVICE` package
- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=RACAD076) for information about creating a service in an Oracle RAC environment
- [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=NETAG298) for more information about Oracle Net Listener and services

**Parent topic:** Database Services

#### 2.8.2 Global Data Services

Starting with Oracle Database 12c, you can use Global Data Services (GDS) for workload management involving multiple Oracle databases. GDS enables administrators to automatically and transparently manage client workloads across replicated databases that offer common services. These common services are known as global services.

GDS enables you to integrate multiple databases in various locations into private GDS configurations that can be shared by global clients. Benefits include the following:

- Enables central management of global resources
- Provides global scalability, availability, and run-time load balancing
- Allows you to dynamically add databases to the GDS configuration and dynamically migrate global services
- Extends service management, load balancing, and failover capabilities for distributed environments of replicated databases that use features such as Oracle Active Data Guard, Oracle GoldenGate, and so on
- Provides high availability through seamless failover of global services across databases (located both locally or globally)
- Provides workload balancing both within and between data centers through services, connection load balancing, and runtime load balancing
- Allows efficient utilization of the resources of the GDS configuration to service client requests

See Also:

- [Oracle Database Global Data Services Concepts and Administration Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=GSMUG)
- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=CNCPT89330)

**Parent topic:** Managing Application Workloads with Database Services

#### 2.8.3 Database Service Data Dictionary Views

You can query data dictionary views to find information about database services.

You can find information about database services in the following views:

- `DBA_SERVICES`
- `ALL_SERVICES` or `V$SERVICES`
- `V$ACTIVE_SERVICES`
- `V$SERVICE_STATS`
- `V$SERVICE_EVENT`
- `V$SERVICE_WAIT_CLASS`
- `V$SERV_MOD_ACT_STATS`
- `V$SERVICEMETRIC`
- `V$SERVICEMETRIC_HISTORY`

The following additional views also contain some information about database services:

- `V$SESSION`
- `V$ACTIVE_SESSION_HISTORY`
- `DBA_RSRC_GROUP_MAPPINGS`
- `DBA_SCHEDULER_JOB_CLASSES`
- `DBA_THRESHOLDS`

The `ALL_SERVICES` view includes a `GLOBAL_SERVICE` column, and the `V$SERVICES` and `V$ACTIVE_SERVICES` views contain a `GLOBAL` column. These views and columns enable you to determine whether a database service is a global service.

**Parent topic:** Managing Application Workloads with Database Services

### 2.9 Managing Standard Edition High Availability for Oracle Databases

The Standard Edition High Availability feature provides protection against unplanned outages for Oracle Database Standard Edition 2 single instance databases using Oracle Clusterware.

Note:

Standard Edition High Availability is supported starting with Oracle Database 19c, Release 19.7.

Note:

The `srvctl` commands used with Standard Edition High Availability are different from those used with Oracle Restart. For Standard Edition High Availability, refer to the `srvctl` commands documented in the Oracle Real Application Clusters Administration and Deployment Guide.

- About Standard Edition High Availability  
	Starting with Oracle Database 19c, you can install Oracle Database Standard Edition 2 in high availability mode.
- Requirements for Using Standard Edition High Availability With Oracle Databases  
	To use Standard Edition High Availability, deploy Oracle Database Standard Edition 2 in accordance with these configuration requirements.
- Enabling Standard Edition High Availability for Oracle Databases  
	You enable Standard Edition High Availability to provide cluster-based failover for an Oracle Database Standard Edition 2 database.
- Relocating a Standard Edition High Availability Database to Another Node  
	To manage planned outages, you can relocate an Oracle Database Standard Edition 2 database that uses Standard Edition High Availability to another configured node.
- Adding a Node to a Standard Edition High Availability Database  
	Adding new nodes to an existing Standard Edition High Availability configuration provides enhanced failover capabilities to your Standard Edition 2 database.
- Removing a Configured Node from a Standard Edition High Availability Database  
	Use `srvctl` commands to remove a node from the list of nodes configured for a Standard Edition High Availability database.
- Starting and Stopping Standard Edition High Availability Databases  
	Use `srvctl` commands to start or stop an Oracle Database that is configured for Standard Edition High Availability.
- Deactivating Standard Edition High Availability for Oracle Databases  
	When you deactivate Standard Edition High Availability for a single instance Oracle Database, the database is no longer part of a high availability failover configuration.

**Parent topic:** Creating and Configuring an Oracle Database

#### 2.9.1 About Standard Edition High Availability

Starting with Oracle Database 19c, you can install Oracle Database Standard Edition 2 in high availability mode.

Standard Edition High Availability provides cluster-based failover for single-instance Standard Edition Oracle Databases using Oracle Clusterware.

Oracle Standard Edition High Availability benefits from the cluster capabilities and storage solutions that are already part of Oracle Grid Infrastructure, such as Oracle Clusterware, Oracle Automatic Storage Management (Oracle ASM) and Oracle ASM Cluster File System (Oracle ACFS).

Using integrated, shared, and concurrently mounted storage, such as Oracle ASM and Oracle ACFS for database files as well as for unstructured data, enables Oracle Grid Infrastructure to restart an Oracle Database on a failover node much faster than any cluster solution that relies on failing over and remounting volumes and file systems.

Starting with Oracle Database 19c Release Update (19.7), Standard Edition High Availability is supported on Linux x86-64, Oracle Solaris on SPARC (64-bit), and Microsoft Windows.

Starting with Oracle Database 19c Release Update (19.13), Standard Edition High Availability is supported on IBM AIX on POWER Systems (64-bit) and HP-UX Itanium.

Note:

This section is specific to Standard Edition High Availability, which provides cluster-based database failover for Standard Edition Oracle Databases 19c. For more information about high availability options for Oracle Database, see [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=CWADD-GUID-C54E2511-24E2-452B-B4C7-0D5A93A751A9).

**Parent topic:** Managing Standard Edition High Availability for Oracle Databases

#### 2.9.2 Requirements for Using Standard Edition High Availability With Oracle Databases

To use Standard Edition High Availability, deploy Oracle Database Standard Edition 2 in accordance with these configuration requirements.

- The database is created in a cluster running Oracle Grid Infrastructure for a Standalone Cluster, with its database files placed in Oracle Automatic Storage Management (Oracle ASM) or Oracle Automatic Storage Management Cluster File System (Oracle ACFS).
- When using the Database Configuration Assistant, do not create a listener when creating an Oracle Database Standard Edition 2 database that you want to configure for Standard Edition High Availability.
- Register the database with Single Client Access Name (SCAN) listeners as remote listeners, and node listeners as the local listener.
- Create a database service. Use this service, instead of the default database service, when you connect applications or database clients to the database.
- Ensure that the server parameter file (`spfile`) and password file are on Oracle ASM or Oracle ACFS. If the `spfile` and password file were placed on a local file system when the database was created or configured, then move these files to Oracle ASM or Oracle ACFS.

Refer to the database installation documentation for additional requirements that must be met.

#### 2.9.3 Enabling Standard Edition High Availability for Oracle Databases

You enable Standard Edition High Availability to provide cluster-based failover for an Oracle Database Standard Edition 2 database.

Note:

The steps in this topic must be performed after you install the Oracle Database software binaries to configure Standard Edition High Availability, as described in the Oracle Database Installation Guide for Linux, and create a database. If you have an existing Standard Edition 2 database that runs on one cluster node, and you want to enable Standard Edition High Availability for this database, you need to add a node to the configuration.

Prerequisites

- Ensure that the initialization parameter `local_listener` is not set. This is to enable node listeners to be automatically used and database connections to be made over the node virtual IP address.
	Use the following command to display the current listener configuration:
	```
	SQL> SHOW PARAMETER LOCAL_LISTENER;
	```
	If the output of the above command shows a local listener name, reset the local listener using the following command:
	```
	SQL> ALTER SYSTEM RESET LOCAL_LISTENER SCOPE = BOTH;
	```
	The database must be restarted for the listener configuration change to take effect. However, if the database is relocated to another node, as part of verifying the Standard Edition High Availability configuration, the database need not be restarted.
- When the database files are stored in Oracle ASM Cluster File System (Oracle ACFS), the Oracle ACFS file system must be registered in Oracle Clusterware and the dependency of the database resource on the corresponding Oracle ACFS resources must be configured using `srvctl` commands. For example:
	```
	$ srvctl modify database -db se2cdb2 -acfspath /u01/app/oradata
	```

To enable Standard Edition High Availability for an Oracle Database Standard Edition 2 database:

1. If the database was created using the `CREATE DATABASE` command, register the database with Oracle Clusterware.
	Databases created using the `CREATE DATABASE` command are not automatically registered with Oracle Clusterware. Use the `srvctl add database` command to register the database.
	For example, the following command registers the single instance database, whose unique name is `se2cdb`, with the nodes `node3` and `node5`:
	```
	$ srvctl add database -db se2cdb -oraclehome $ORACLE_HOME 
	-dbtype SINGLE -spfile +DATA/SE2CDB1/PARAMETERFILE/spfile.276.1030845691 
	-node node3,node5
	```
2. If the database is already registered with Oracle Clusterware, use the `srvctl modify database` command to enable Standard Edition High Availability.
	For example, the following command enables Standard Edition High Availability on a Standard Edition 2 database whose database unique name is `se2cdb`:
	```
	$ srvctl modify database -db se2cdb -node node3,node5
	```
	Note:
	The `-fixed` option to create a fixed single instance database is not supported with Standard Edition High Availability.

After you enable Standard Edition High Availability for a database:

- When there is an unplanned outage of the node which runs the database instance, the instance is restarted on an available node in the configured node list.
- When there is an unplanned termination of the database instance, an attempt is made to restart the instance on the current node. If the restart fails, a failover is initiated to an available node in the configured node list.
- When the node which runs the database instance completely loses connectivity to the public network, the instance is relocated to an available node in the configured node list.

Note:

The order of nodes in the node list determines the node on which the database is started. Oracle Clusterware attempts to start the database on the first node in the node list. If the first node is unavailable, it moves to the next node in the node list.

Oracle Clusterware also uses the order of nodes in the node list to determine the failover target, if the current node fails. Failover targets are considered starting with the first node in the list and until a suitable candidate is found and unless other circumstances in the cluster prevent this order to determine the failover node.

Verifying a Standard Edition high Availability Configuration

You can verify the Standard Edition High Availability configuration, especially its current configured node list, by using the `srvctl config                     database` command. For example:

```
$ srvctl config database -db se2cdb 
...
Type: SINGLE
...
Configured nodes:
        node3, node5
```

Notice from the output that the type of database is single, but there are multiple configured nodes. This indicates that Standard Edition High Availability is enabled.

Further verification can be performed by relocating the database to another configured node.

#### 2.9.4 Relocating a Standard Edition High Availability Database to Another Node

To manage planned outages, you can relocate an Oracle Database Standard Edition 2 database that uses Standard Edition High Availability to another configured node.

The node to which the database is being relocated must be part of the configured node list for this database.

To relocate an active Oracle Database Standard Edition 2 database from its current node to another configured node:

- Use the `srvctl relocate` command.
	This command performs an offline relocation. It shuts down the database on the existing node and then starts it on the new node.

For example, the following command relocates the Standard Edition 2 database named `se2cdb`, that uses Standard Edition High Availability, to the node `node5`:

```
$ srvctl relocate database -db se2cdb -node node5
```

Note:

The `–abort` and `–revert` options of `srvctl relocate database` command are not supported with Standard Edition High Availability.

**Parent topic:** Managing Standard Edition High Availability for Oracle Databases

#### 2.9.5 Adding a Node to a Standard Edition High Availability Database

Adding new nodes to an existing Standard Edition High Availability configuration provides enhanced failover capabilities to your Standard Edition 2 database.

You may need to add nodes in certain scenarios. Assume that you configured two nodes for your Standard Edition High Availability database. Subsequently, a new node is added to the cluster and you want to include this new node in your database configuration. You can do this by adding the node to the Standard Edition High Availability configuration. Another scenario is when you want to enable Standard Edition High Availability for an existing Standard Edition 2 database.

To add a node to a Standard Edition High Availability database:

1. Extend the Oracle Database Oracle home to the new node. The steps depend on the storage used.
	For a local (non-shared) Oracle home:
	1. Log in to the first cluster node (on which you configured Standard Edition High Availability) as the Oracle installation owner user account (`oracle`).
	2. Navigate to the `ORACLE_HOME/addnode` directory and run the `addnode.sh` script.
		For example, to extend the Oracle home to `node3`:
		```
		$ ./addnode.sh -silent "CLUSTER_NEW_NODES={node3}"
		```
	For a shared Oracle home using Oracle ACFS:
	1. Start the Oracle ACFS resource on the new node by running the following command as `root` from the `Grid_home/bin` directory:
		```
		# srvctl start filesystem -device volume_device [-node node_name]
		```
		Note:
		Make sure the Oracle ACFS resources, including Oracle ACFS registry resource and Oracle ACFS file system resource where the Oracle home is located, are online on the newly added node.
	2. Log in to the first cluster node (on which you configured Standard Edition High Availability) as the Oracle installation owner user account (`oracle`).
	3. Attach the Oracle home on the first cluster node to the node that you want to add.
		```
		$ $ORACLE_HOME/addnode/addnode.sh -silent CLUSTER_NEW_NODES=new_node_name
		```
2. On the new node (that must be added), as the `root` user, and run the `ORACLE_HOME/root.sh` script.
	```
	# /u01/app/oracle/product/19.0.0/dbhome_1/root.sh
	```
3. On any configured node, including the node that is being added, as the `oracle` user, add the new node by using the `srvctl                         modify database` command.
	The `-node` argument must list the existing configured nodes and the new node that is being added.
	For example, the following command adds the node `node3` to the database with unique name `se2cdb`. Existing configured nodes are `node1` and `node5`.
	```
	$ srvctl modify database -db se2cdb -node node1,node3,node5
	```

You can optionally verify the new configuration as described in Enabling Standard Edition High Availability for Oracle Databases.

#### 2.9.6 Removing a Configured Node from a Standard Edition High Availability Database

Use `srvctl` commands to remove a node from the list of nodes configured for a Standard Edition High Availability database.

Navigate to the Oracle Database home directory. On Linux, log in to the database host computer as the Oracle installation owner user account (`oracle`). On Windows, log in to the database host computer as Administrator.

To remove a configured node from a database that uses Standard Edition High Availability:

1. List the existing configured nodes by using the `srvctl config                         database` command.
2. If the database is currently running on the node that you want to remove, relocate the database to another configured node by using the `srvctl                         relocate database` command.
3. Remove the node by using the `srvctl modify database` command with the `-node` argument.
	The `-node` argument must list all the configured nodes, except the node that must be removed.

Example 2-1 Removing a Configured Node from a Standard Edition High Availability Database

The example assumes that the database with unique name `sec2cdb` uses Standard Edition High Availability and the configured nodes are `node1`, `node2`, and `node3`. The database is currently running on `node3`. To remove `node2` from the list of configured nodes for this database, log in as a user who installed the Oracle Database home and run the following command:

```
$ srvctl modify database -db sec2cdb -node node1,node3
```

#### 2.9.7 Starting and Stopping Standard Edition High Availability Databases

Use `srvctl` commands to start or stop an Oracle Database that is configured for Standard Edition High Availability.

Navigate to the Oracle Database home directory. On Linux, log in to the database host computer as the Oracle installation owner user account (`oracle`). On Windows, log in to the database host computer as Administrator.

To start up a Standard Edition High Availability database:

- Use the `srvctl start database` command.
	Optionally, include the `-node` argument to specify the node on which the database must be started.

To stop a Standard Edition High Availability database:

- Use the `srvctl stop database` command

Example 2-2 Starting Up a Standard Edition High Availability Database on a Specified Node

This example starts up a database with the unique name `se2cdb` on the node named `node3`.

```
$ srvctl start database -db sec2cdb -node node3
```

Example 2-3 Stopping a Standard Edition High Availability Database

This example stops a database instance that is configured to use Standard Edition High Availability. The unique name of the database is `sec2cdb`.

```
$ srvctl stop database -db sec2cdb
```

#### 2.9.8 Deactivating Standard Edition High Availability for Oracle Databases

When you deactivate Standard Edition High Availability for a single instance Oracle Database, the database is no longer part of a high availability failover configuration.

To deactivate Standard Edition High Availability for an Oracle Database:

- Use the `srvctl modify` command and include only one node in the `-node` argument.

Example 2-4 Deactivating the Use of Standard Edition High Availability for an Oracle Database

This example deactivates the use of Standard Edition High Availability for the database with unique name `se2cdb` and configures only one node, `node1`, for this database:

```
srvctl modify database -db se2cdb -node node1
```

All previously configured nodes are removed and the database is now a single-instance database that is registered with Oracle Clusterware.

**Parent topic:** Managing Standard Edition High Availability for Oracle Databases

### 2.10 Considerations After Creating a Database

After you create a database the instance is left running, and the database is open and available for normal database use. You may want to perform specific actions after creating a database.

- Database Security  
	You can use the default Oracle Database features to configure security in several areas for your Oracle database.
- Transparent Data Encryption  
	Transparent Data Encryption is a feature that enables encryption of individual database columns before storing them in the data file, or enables encryption of entire tablespaces. If users attempt to circumvent the database access control mechanisms by looking inside data files directly with operating system tools, Transparent Data Encryption prevents such users from viewing sensitive information.
- A Secure External Password Store  
	Consider using client-side Oracle wallets to reduce exposing authentication and signing credentials over networks.
- Transaction Guard and Application Continuity  
	Transaction Guard uses a logical transaction ID to prevent the possibility of a client application submitting duplicate transactions after a recoverable error. Application Continuity enables the replay, in a nondisruptive and rapid manner, of a request against the database after a recoverable error that makes the database session unavailable.
- File System Server Support in the Database  
	An Oracle database can be configured to store file system objects and access them from any NFS client. The database stores both the files and their metadata. The database responds to file system requests from the NFS daemon process in the operating system (OS) kernel.
- The Oracle Database Sample Schemas  
	Oracle Database includes sample schemas that help you to become familiar with Oracle Database functionality. Some Oracle Database documentation and training materials use the sample schemas in examples.

**Parent topic:** Creating and Configuring an Oracle Database

#### 2.10.1 Database Security

You can use the default Oracle Database features to configure security in several areas for your Oracle database.

The following are some of the areas in which you can configure security for your database:

- User accounts: When you create user accounts, you can secure them in a variety of ways. You can also create password profiles to better secure password policies for your site.
- Authentication methods: Oracle Database provides several ways to configure authentication for users and database administrators. For example, you can authenticate users on the database level, from the operating system, and on the network.
- Privileges and roles: You can use privileges and roles to restrict user access to data.

Note:

- A newly created database has at least three user accounts that are important for administering your database: `SYS`, `SYSTEM`, and `SYSMAN`. Additional administrative accounts are provided that should be used only by authorized users.
- To prevent unauthorized access and protect the integrity of your database, it is important that a new password is specified to the `SYS` user when the database is created.
- Starting with Oracle Database 19c, most of the Oracle Database supplied user accounts, except `SYS` and sample schemas are schema only accounts, that is, these accounts are created without passwords. You can assign passwords to these accounts whenever you want them to be authenticated, but Oracle recommends that for better security, you should change these accounts back to schema only accounts, when you do not need to authenticate them anymore.
	To find the status of an account, query the `ACCOUNT_STATUS` column of the `DBA_USERS` data dictionary view. If the account is schema only, then the status is `NONE`.

See Also:

- " [Administrative User Accounts](getting-started-with-database-administration.md) " for more information about `SYS` and `SYSTEM` users
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=DBSEG-GUID-B8EF08C7-28E5-492D-A300-C5B1866FDCC8) for a complete list of predefined user accounts created with each new Oracle Database installation
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=DBSEG002) to learn how to add new users and change passwords
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=SQLRF01103) for the syntax of the `ALTER USER` statement used for unlocking database user accounts
- [Oracle Database Enterprise User Security Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=DBIMI203) for information about Oracle Identity Management
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=DBSEG009) for security guidelines for configuring a database

**Parent topic:** Considerations After Creating a Database

#### 2.10.2 Transparent Data Encryption

Transparent Data Encryption is a feature that enables encryption of individual database columns before storing them in the data file, or enables encryption of entire tablespaces. If users attempt to circumvent the database access control mechanisms by looking inside data files directly with operating system tools, Transparent Data Encryption prevents such users from viewing sensitive information.

Users who have the `CREATE TABLE` privilege can choose one or more columns in a table to be encrypted. The data is encrypted in the data files. Database users with appropriate privileges can view the data in unencrypted format. For information on enabling Transparent Data Encryption, see [Oracle Database Advanced Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=ASOAG600).

See Also:

- " [Consider Encrypting Columns That Contain Sensitive Data](managing-tables.md) "
- " [Encrypted Tablespaces](managing-tablespaces.md) "

**Parent topic:** Considerations After Creating a Database

#### 2.10.3 A Secure External Password Store

Consider using client-side Oracle wallets to reduce exposing authentication and signing credentials over networks.

For large-scale deployments where applications use password credentials to connect to databases, it is possible to store such credentials in a client-side Oracle wallet. An Oracle wallet is a secure software container that is used to store authentication and signing credentials.

Storing database password credentials in a client-side Oracle wallet eliminates the need to embed usernames and passwords in application code, batch jobs, or scripts. Client-side storage reduces the risk of exposing passwords in the clear in scripts and application code. It also simplifies maintenance, because you need not change your code each time usernames and passwords change. In addition, not having to change application code also makes it easier to enforce password management policies for these user accounts.

When you configure a client to use the external password store, applications can use the following syntax to connect to databases that use password authentication:

```
CONNECT /@database_alias
```

You need not specify database login credentials in this `CONNECT` command. Instead your system looks for database login credentials in the client wallet.

See Also:

- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=DBSEG99815)
- [Oracle Database Enterprise User Security Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=DBIMI160)

**Parent topic:** Considerations After Creating a Database

#### 2.10.4 Transaction Guard and Application Continuity

Transaction Guard uses a logical transaction ID to prevent the possibility of a client application submitting duplicate transactions after a recoverable error. Application Continuity enables the replay, in a nondisruptive and rapid manner, of a request against the database after a recoverable error that makes the database session unavailable.

Transaction Guard is a reliable protocol and API that application developers can use to provide a known outcome for the last open transaction on a database session that becomes unavailable. After an outage, the commit message that is sent from the database to the client is not durable. If the connection breaks between an application (the client) and an Oracle database (the server), then the client receives an error message indicating that the communication failed. This error message does not inform the client about the success or failure of commit operations or procedure calls.

Transaction Guard uses a concept called the logical transaction identifier (LTXID), a globally unique identifier that identifies the transaction from the application's perspective. When a recoverable outage occurs, the application uses the LTXID to determine the outcome of the transaction. This outcome can be returned to the client instead of the ambiguous communication error. The user can decide whether to resubmit the transaction. The application also can be coded to resubmit the transaction if the states are correct.

Application Continuity masks outages from end users and applications by recovering the in-flight database sessions following recoverable outages, for both unplanned and planned outages. After a successful replay, the application can continue using a new session where the original database session left off. Application Continuity performs this recovery so that the outage appears to the application as a delayed execution.

Application Continuity is enabled at the service level and is invoked for outages that are recoverable. These outages typically are related to underlying software, foreground, hardware, communications, network, or storage layers. Application Continuity supports queries, `ALTER SESSION` statements, Java and OCI APIs, PL/SQL, DDL, and the last uncommitted transaction before the failure. Application Continuity determines whether the last in-flight transaction committed or not, and whether the last user call completed or not, using Transaction Guard.

See Also:

- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=CNCPT89217) for a conceptual overview of Transaction Guard and Application Continuity
- [Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=ADFNS8000) for complete information about Transaction Guard and Application Continuity

**Parent topic:** Considerations After Creating a Database

#### 2.10.5 File System Server Support in the Database

An Oracle database can be configured to store file system objects and access them from any NFS client. The database stores both the files and their metadata. The database responds to file system requests from the NFS daemon process in the operating system (OS) kernel.

When you configure the Oracle File System (OFS) server in a database and create a file system, you can store unstructured data, such as emails, videos, audio files, credit card bills, documents, photo images, and so on, inside the database. You can manipulate and manage these unstructured objects without using SQL. Instead, you can use operating system utilities for NFS support.

To enable NFS access in the database, set the `OFS_THREADS` initialization parameter to configure a sufficient number of OFS threads to process the NFS requests. The `OFS_THREADS` initialization parameter controls the number of OFS threads to create when the first file system is mounted with the database. The number of threads specified by the `OFS_THREADS` parameter are created only once for the database instance and subsequent file systems do not create any additional threads. The default value of the `OFS_THREADS` initialization parameter is 4. At database startup, OFSD background process is the sole OFS process that is spawned by the database server.

You can use the `DBMS_FS` package to create a file system in the database using a specified database object. You can also use this package to mount and unmount a specified file system.

See Also:

- [Oracle Database SecureFiles and Large Objects Developer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=ADLOB-GUID-5613B15C-9976-4148-A167-4C279E28372D) for more information about the Oracle File System (OFS)
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=ARPLS-GUID-F21D6EF9-F8CA-403B-95A5-ED081951C51D) for more information about the `DBMS_FS` package

**Parent topic:** Considerations After Creating a Database

#### 2.10.6 The Oracle Database Sample Schemas

Oracle Database includes sample schemas that help you to become familiar with Oracle Database functionality. Some Oracle Database documentation and training materials use the sample schemas in examples.

The schemas and installation instructions are described in detail in [Oracle Database Sample Schemas](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=COMSC).

Note:

Oracle strongly recommends that you do not install the sample schemas in a production database.

**Parent topic:** Considerations After Creating a Database

### 2.11 Cloning a Database

This section describes various methods of cloning an Oracle database.

- Cloning a Database with CloneDB in a Non-multitenant Environment  
	CloneDB enables you to clone a database in a non-multitenant environment multiple times without copying the data files into several different locations. Instead, CloneDB uses copy-on-write technology, so that only the blocks that are modified require additional storage on disk.
- Cloning a Database in a Multitenant Environment  
	You can clone a database in a multitenant environment.
- Cloning a Database with Oracle Automatic Storage Management (Oracle ASM)  
	Oracle Automatic Storage Management (Oracle ASM) provides support for cloning a pluggable database (PDB) in a multitenant container database (CDB). Oracle ASM does not support cloning a non-CDB.

**Parent topic:** Creating and Configuring an Oracle Database

#### 2.11.1 Cloning a Database with CloneDB in a Non-multitenant Environment

CloneDB enables you to clone a database in a non-multitenant environment multiple times without copying the data files into several different locations. Instead, CloneDB uses copy-on-write technology, so that only the blocks that are modified require additional storage on disk.

- About Cloning a Database with CloneDB  
	It is often necessary to clone a production database for testing purposes or other purposes.
- Cloning a Database with CloneDB  
	You can clone a database with CloneDB.
- After Cloning a Database with CloneDB  
	After a CloneDB database is created, you can use it in almost any way you use your production database. Initially, a CloneDB database uses a minimal amount of storage for each data file. Changes to rows in a CloneDB database cause storage space to be allocated on demand.

**Parent topic:** Cloning a Database

##### 2.11.1.1 About Cloning a Database with CloneDB

It is often necessary to clone a production database for testing purposes or other purposes.

Common reasons to clone a production database include the following:

- Deployment of a new application, or an update of an existing application, that uses the database
- A planned operating system upgrade on the system that runs the database
- New storage for the database installation
- Reporting
- Analysis of older data

Before deploying a new application, performing an operating system upgrade, or using new storage, thorough testing is required to ensure that the database works properly under the new conditions. Cloning can be achieved by making copies of the production data files in one or more test environments, but these copies typically require large amounts of storage space to be allocated and managed.

With CloneDB, you can clone a database multiple times without copying the data files into several different locations. Instead, Oracle Database creates the files in the CloneDB database using copy-on-write technology, so that only the blocks that are modified in the CloneDB database require additional storage on disk.

Cloning a database in this way provides the following advantages:

- It reduces the amount of storage required for testing purposes.
- It enables the rapid creation of multiple database clones for various purposes.

The CloneDB databases use the data files of a database backup. Using the backup data files ensures that the production data files are not accessed by the CloneDB instances and that the CloneDB instances do not compete for the production database's resources, such as CPU and I/O resources.

Note:

- The instructions in this section about cloning a database with CloneDB are not applicable for a database in a multitenant environment.
- The CloneDB feature is not intended for performance testing.

See Also:

" Cloning a Database in a Multitenant Environment " for more information about cloning a database in a multitenant environment

**Parent topic:** Cloning a Database with CloneDB in a Non-multitenant Environment

##### 2.11.1.2 Cloning a Database with CloneDB

You can clone a database with CloneDB.

Before cloning a database, the following prerequisites must be met:

- Each CloneDB database must use Direct NFS Client, and the backup of the production database must be located on an NFS volume.
	Direct NFS Client enables an Oracle database to access network attached storage (NAS) devices directly, rather than using the operating system kernel NFS client. This CloneDB database feature is available on platforms that support Direct NFS Client.
	See [Oracle Grid Infrastructure Installation Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=CWGEN) for your operating system for information about Direct NFS Client.
- At least 2 MB of additional System Global Area (SGA) memory is required to track the modified blocks in a CloneDB database.
	See [Managing Memory](managing-memory.md).
- Storage for the database backup and for the changed blocks in each CloneDB database is required.
	The storage required for the database backup depends on the method used to perform the backup. A single full RMAN backup requires the most storage. Storage snapshots carried out using the features of a storage appliance adhere to the requirements of the storage appliance. A single backup can support multiple CloneDB databases.
	The amount of storage required for each CloneDB database depends on the write activity in that database. Every block that is modified requires an available block of storage. Therefore, the total storage requirement depends on the number of blocks modified in the CloneDB database over time.

This section describes the steps required to create one CloneDB database and uses these sample databases and directories:

- The Oracle home for the production database `PROD1` is /u01/prod1/oracle.
- The files for the database backup are in /u02/oracle/backup/prod1.
- The Oracle home for CloneDB database `CLONE1` is /u03/clone1/oracle.

To clone a database with CloneDB:

To create additional CloneDB databases of the production database, repeat Steps [^2] - [^3] for each CloneDB database.

**Parent topic:** Cloning a Database with CloneDB in a Non-multitenant Environment

##### 2.11.1.3 After Cloning a Database with CloneDB

After a CloneDB database is created, you can use it in almost any way you use your production database. Initially, a CloneDB database uses a minimal amount of storage for each data file. Changes to rows in a CloneDB database cause storage space to be allocated on demand.

You can use the same backup files to create multiple CloneDB databases. This backup can be taken either by RMAN or by storage level snapshots. If you have a storage level snapshot taken on a data file, then you can replace the RMAN backup file names with the storage snapshot names.

You can use the `V$CLONEDFILE` view to show information about each data file in the CloneDB database. This information includes the data file name in the backup, the corresponding data file name in the CloneDB database, the number of blocks read from the backup file, and the number of requests issued against the backup file.

Because CloneDB databases use the backup files as their backend storage, the backup files must be available to each CloneDB database for it to run. If the backup files become unavailable, then the CloneDB databases return errors.

When your use of a CloneDB database is complete, you can destroy the CloneDB database environment. You can delete all of the files in the CloneDB database environment without affecting the production database environment or the backup environment.

See Also:

[Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=REFRN30713) for more information about the `V$CLONEDFILE` view

**Parent topic:** Cloning a Database with CloneDB in a Non-multitenant Environment

#### 2.11.2 Cloning a Database in a Multitenant Environment

You can clone a database in a multitenant environment.

Refer to [Oracle Multitenant Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=MULTI-GUID-05702CEB-A43C-452C-8081-4CA68DDA8007) for more information about cloning a database in a multitenant environment.

**Parent topic:** Cloning a Database

#### 2.11.3 Cloning a Database with Oracle Automatic Storage Management (Oracle ASM)

Oracle Automatic Storage Management (Oracle ASM) provides support for cloning a pluggable database (PDB) in a multitenant container database (CDB). Oracle ASM does not support cloning a non-CDB.

See the following guides for more information:

- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=OSTMG-GUID-F0CA1610-780A-40FB-B8BB-88E0C7688CC2)
- [Oracle Multitenant Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=MULTI-GUID-7ED69A82-B797-4497-A160-FDDAA2AAC999)

**Parent topic:** Cloning a Database

### 2.12 Dropping a Database

Dropping a database involves removing its data files, online redo logs, control files, and initialization parameter files.

WARNING:

Dropping a database deletes all data in the database.

To drop a database:

- Submit the following statement:
	```
	DROP DATABASE;
	```

The `DROP` `DATABASE` statement first deletes all control files and all other database files listed in the control file. It then shuts down the database instance.

To use the `DROP` `DATABASE` statement successfully, the database must be mounted in exclusive and restricted mode.

The `DROP` `DATABASE` statement has no effect on archived redo log files, nor does it have any effect on copies or backups of the database. It is best to use RMAN to delete such files.

If you used the Database Configuration Assistant to create your database, you can use that tool to delete (drop) your database and remove the files.

See Also:

" [Altering Database Availability](starting-up-and-shutting-down.md) "

**Parent topic:** Creating and Configuring an Oracle Database

### 2.13 Database Data Dictionary Views

You can query data dictionary views for information about your database content and structure.

You can view information about your database content and structure using the following views:

| View | Description |
| --- | --- |
| `DATABASE_PROPERTIES` | Displays permanent database properties |
| `GLOBAL_NAME` | Displays the global database name |
| `V$DATABASE` | Contains database information from the control file |

### 2.14 Database Configuration Assistant Command Reference for Silent Mode

This section provides detailed information about the syntax and options for the Database Configuration Assistant (DBCA) silent mode commands.

See Also:

Database Configuration Assistant Utility (dbcactl) is a standalone software package which is part of Oracle Database product suite. It is designed to assist in the database creation, configuration and lifecycle management of Oracle Database. For information about downloading and configuring dbcactl, see My Oracle Support note 3099785.1 at [https://support.oracle.com/rs?type=doc&id=3099785.1](https://support.oracle.com/rs?type=doc&id=3099785.1)

- DBCA Command-Line Syntax Overview  
	This section provides an overview of the command-line syntax of DBCA in silent mode.
- About DBCA Templates  
	You can use DBCA to create a database from a template supplied by Oracle or from a template that you create.
- Database User Authentication in DBCA Commands Using Oracle Wallet  
	You can use Oracle wallet as a secure external password store for authenticating database users in DBCA silent mode commands.
- DBCA Silent Mode Commands  
	This section lists all the DBCA silent mode commands along with their syntax and parameter description.
- DBCA Exit Codes  
	The outcome of running DBCA commands in silent mode is reported as an exit code.

See Also:

[Oracle Database 2 Day DBA](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=ADMQS023) for information about using DBCA in the interactive mode

**Parent topic:** Creating and Configuring an Oracle Database

#### 2.14.1 DBCA Command-Line Syntax Overview

This section provides an overview of the command-line syntax of DBCA in silent mode.

DBCA silent mode has the following command syntax:

```
dbca  [-silent] [command [options]] [-h|-help]
```

The following table describes the DBCA silent mode command syntax.

Table 2-4 DBCA Silent Mode Command Syntax Description

| Option | Description |
| --- | --- |
| `-silent` | Specify `-silent` to run DBCA in silent mode.  In silent mode, DBCA uses values that you specify as command-line options to create or modify a database. |
| `command options` | Specify a DBCA command and valid options for the command. |
| `-h \| -help` | Displays help for DBCA.  You can display help for a specific command by entering the following:  ``` dbca command -help ```  For example, to display the help for the `-createDatabase` command, enter the following:  ``` dbca -createDatabase -help ``` |

The following example illustrates how to create a database with the silent mode of DBCA:

```
dbca -silent -createDatabase -templateName General_Purpose.dbc
                             -gdbname oradb.example.com 
                             -sid oradb
                             -characterSet AL32UTF8 
                             -memoryPercentage 30 
                             -emConfiguration DBEXPRESS

Enter SYSTEM user password:
password
Enter SYS user password:
password
Copying database files
1% complete
3% complete
...
```

To ensure completely silent operation, you can redirect stdout to a file. If you do this, however, you may have to supply passwords for the administrative users in command-line arguments or the response file.

Note:

If you use Oracle wallet as a secure external password store for storing passwords for the administrative users, then you do not have to supply passwords for these users in the command-line arguments or in the response file. See " Database User Authentication in DBCA Commands Using Oracle Wallet " for more information.

To view brief help for DBCA command-line arguments, enter the following command:

```
dbca -help
```

For more detailed argument information, including defaults, view the response file template found on your distribution media. See the Oracle Database installation guide for your platform to get information about the name and location of the response file template.

See Also:

" DBCA Silent Mode Commands "

**Parent topic:** Database Configuration Assistant Command Reference for Silent Mode

#### 2.14.2 About DBCA Templates

You can use DBCA to create a database from a template supplied by Oracle or from a template that you create.

A DBCA template is an XML file that contains information required to create a database. Oracle ships templates for the following two workload types:

- General purpose OR online transaction processing
- Data warehouse

Select the template suited to the type of workload your database will support. If you are not sure which to choose, then use the "General purpose OR online transaction processing" template. You can also create custom templates to meet your specific workload requirements.

Note:

The General Purpose or online transaction processing template and the data Warehouse template create a database with the `COMPATIBLE` initialization parameter set to 12.1.0.2.0.

**Parent topic:** Database Configuration Assistant Command Reference for Silent Mode

#### 2.14.3 Database User Authentication in DBCA Commands Using Oracle Wallet

You can use Oracle wallet as a secure external password store for authenticating database users in DBCA silent mode commands.

Oracle wallet is a secure software container external to Oracle Database, which can be used to store authentication credentials of Oracle Database users. You can use the following DBCA silent mode command parameters to use Oracle wallet for authenticating database users:

- `useWalletForDBCredentials`: Specify `true` to use Oracle wallet for database user authentication, else specify `false`. Default is `false`.
	If `true` is specified, then provide the following additional parameters:
	- `dbCredentialsWalletLocation`: Directory in which the Oracle wallet files are stored.
		- (Optional) `dbCredentialsWalletPassword`: Password for the Oracle wallet account user. If the Oracle wallet is auto-login enabled, then you need not specify this password.

You can store the following keys and associated passwords in the Oracle wallet that can be used by DBCA in silent mode for authenticating users:

- `oracle.dbsecurity.sysPassword`: `SYS` user password
- `oracle.dbsecurity.systemPassword`: `SYSTEM` user password
- `oracle.dbsecurity.pdbAdminPassword`: Pluggable database (PDB) administrator password
- `oracle.dbsecurity.dbsnmpPassword`: `DBSNMP` user password
- `oracle.dbsecurity.asmsnmpPassword`: `ASMSNMP` user password
- `oracle.dbsecurity.lbacsysPassword`: `LBACSYS` user password
- `oracle.dbsecurity.sysdbaUserPassword`: `SYSDBA` role user password for the database that you are creating or configuring
- `oracle.dbsecurity.oracleHomeUserPassword`: Oracle home user password
- `oracle.dbsecurity.dvUserPassword`: Oracle Data Vault user password
- `oracle.dbsecurity.dvAccountManagerPassword`: Oracle Data Vault account manager password
- `oracle.dbsecurity.emPassword`: Enterprise Manager administrator password
- `oracle.dbsecurity.asmPassword`: `ASM` user password
- `oracle.dbsecurity.asmsysPassword`: `ASMSYS` user password
- `oracle.dbsecurity.walletPassword`: Oracle wallet account user password for authenticating with a directory service
- `oracle.dbsecurity.userDNPassword`: Directory service user password
- `oracle.dbsecurity.srcDBsysdbaUserPassword`: `SYSDBA` role user password for the database that you are using as a source to perform certain operations, such as duplicating a database
- `oracle.dbsecurity.dbLinkUserPassword`: Database link user password

Note:

If you are using Oracle Unified Directory (OUD), then the OUD account passwords should be stored in the wallet using the following keys:

- `oracle.dbsecurity.walletPassword`
- `oracle.dbsecurity.userDNPassword`

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=DBSEG-GUID-803496D2-19C7-4F02-94EC-C13EDD8FB17B) for information about configuring Oracle wallet as a secure external password store using the `mkstore` command-line utility

**Parent topic:** Database Configuration Assistant Command Reference for Silent Mode

#### 2.14.4 DBCA Silent Mode Commands

This section lists all the DBCA silent mode commands along with their syntax and parameter description.

- createDatabase  
	The `createDatabase` command creates a database.
- createDuplicateDB  
	The `createDuplicateDB` command creates a duplicate of an Oracle database.
- configureDatabase  
	The `configureDatabase` command configures a database.
- createTemplateFromDB  
	The `createTemplateFromDB` command creates a database template from an existing database.
- createTemplateFromTemplate  
	The `createTemplateFromTemplate` command creates a database template from an existing database template.
- createCloneTemplate  
	The `createCloneTemplate` command creates a clone (seed) database template from an existing database.
- deleteTemplate  
	The `deleteTemplate` command deletes a database template.
- generateScripts  
	The `generateScripts` command generates scripts, which can be used to create a database.
- deleteDatabase  
	The `deleteDatabase` command deletes a database.
- createPluggableDatabase  
	The `createPluggableDatabase` command creates a pluggable database (PDB) in a multitenant container database (CDB).
- unplugDatabase  
	The `unplugDatabase` command unplugs a pluggable database (PDB) from a multitenant container database (CDB).
- deletePluggableDatabase  
	The `deletePluggableDatabase` command deletes a PDB.
- relocatePDB  
	The `relocatePDB` command relocates a PDB from a remote CDB to a local CDB.
- configurePluggableDatabase  
	The `configurePluggableDatabase` command configures a pluggable database (PDB).
- addInstance  
	The `addInstance` command adds a database instance to an administrator-managed Oracle RAC database.
- deleteInstance  
	The `deleteInstance` command deletes a database instance from an administror-managed Oracle RAC database.
- executePrereqs  
	The `executePrereqs` command executes the prerequisites checks and reports the results. This command can be used to check the environment before running dbca to create a database.

**Parent topic:** Database Configuration Assistant Command Reference for Silent Mode

##### 2.14.4.1 createDatabase

The `createDatabase` command creates a database.

Syntax and Parameters

Use the `dbca` `-createDatabase` command with the following syntax:

```
dbca -createDatabase 
    -responseFile | (-gdbName,-templateName)
    -responseFile response_file_directory
    -gdbName global_database_name
    -templateName database_template_name
    [-sid database_system_identifier]
    [-createAsContainerDatabase {true | false}
        [-numberOfPDBs number_of_pdbs]
        [-pdbName pdb_name]
        [-pdbStorageMAXSizeInMB maximum_storage_size_of_the_pdb]
        [-pdbStorageMAXTempSizeInMB maximum_temporary_storage_size_of_the_pdb]
        [-useLocalUndoForPDBs {true | false}]
        [-pdbAdminPassword pdb_administrator_password]
        [-pdbOptions pdb_options]
    [-sysPassword SYS_user_password]
    [-systemPassword SYSTEM_user_password]
    [-emConfiguration {DBEXPRESS | CENTRAL | BOTH | NONE}
        [-dbsnmpPassword DBSNMP_user_password]
        [-omsHost Oracle_Management_Server_host_name]
        [-omsPort Oracle_Management_Server_port_number]
        [-emUser EM_administrator_user_name]
        [-emPassword EM_administrator_user_password]
        [-emExpressPort EM_Express_port]
        [-emExpressPortAsGlobalPort EM_Express_global_port]]
    [-dvConfiguration {true | false}
        -dvUserName Database_Vault_owner_name
        -dvUserPassword Database_Vault_owner_password
        [-dvAccountManagerName Database_Vault_account_manager_name
        -dvAccountManagerPassword Database_Vault_account_manager_password]]
    [-olsConfiguration {true | false}
        [-configureWithOID configure_with_OID_flag]]
    [-datafileDestination data_files_directory]
    [-redoLogFileSize maximum_redo_log_file_size]
    [-recoveryAreaDestination recovery_files_directory
        [-recoveryAreaSize fast_recovery_area_size]]
    [-datafileJarLocation data_files_backup_directory]
    [-storageType {FS | ASM} 
        [-asmsnmpPassword ASMSNMP_password]
        -datafileDestination database_files_directory]
    [-useWalletForDBCredentials {true | false} 
        [-dbCredentialsWalletPassword wallet_account_password]
        -dbCredentialsWalletLocation wallet_files_directory]
    [-runCVUChecks {true | false}]
    [-nodelist database_nodes_list]
    [-oracleHomeUserName Oracle_Home_user_name]
        [-oracleHomeUserPassword Oracle_Home_user_password]
    [-enableArchive {true | false} 
        [-archiveLogMode {AUTO | MANUAL}]
        [-archiveLogDest archive_log_files_directory]]
    [-memoryMgmtType {AUTO | AUTO_SGA | CUSTOM_SGA}]
    [-createListener new_database_listener]
    [-useOMF {true | false}]
    [-dbOptions database_options]
    [-customScripts list_of_custom_sql_scripts]
    [-policyManaged | -adminManaged]
    [-policyManaged
        -serverPoolName server_pool_names
        [-pqPoolName pq_pool_name]
        [-createServerPool new_server_pool_name]
            [-pqPoolName new_pq_pool_name]
            [-force]
            [-pqCardinality pq_cardinality_of_the_new_server_pool]
            [-cardinality cardinality_of_the_new_server_pool]]
    [-adminManaged]
    [-databaseConfigType {SINGLE | RAC | RACONENODE}
            [-RACOneNodeServiceName service_name_for_RAC_One_Node_database]]
    [-characterSet database_character_set]
    [-nationalCharacterSet database_national_character_set]
    [-registerWithDirService {true | false} 
        [-dirServiceUserName directory_service_user_name]
        [-dirServicePassword directory_service_password]
        [-databaseCN database_common_name]
        [-dirServiceCertificatePath certificate_file_path]
        [-dirServiceUser directory_service_user_name]
        [-ldapDirectoryAccessType ldap_directory_access_type]
        [-useSYSAuthForLDAPAccess use_sys_user_for_ldap_access_flag]
        [-walletPassword wallet_password]]
    [-listeners listeners_list]
    [-variablesFile variables_file]
    [-variables variables_list]
    [-initParams initialization_parameters_list
        [-initParamsEscapeChar initialization_parameters_escape_character]]
    [-sampleSchema {true | false}]
    [-memoryPercentage | -totalMemory]
    [-memoryPercentage percentage_of_total_memory_to_assign_to_oracle_database]
    [-totalMemory total_memory_to_assign_to_oracle_database_in_MB]
    [-databaseType {MULTIPURPOSE | DATA_WAREHOUSING | OLTP}]
```

Table 2-5 createDatabase Parameters

| Parameter | Required/Optional | Description |
| --- | --- | --- |
| `-responseFile`  `response_file_directory` | Required | Absolute directory path of the response file. |
| `-gdbName`  `global_database_name` | Required | Global database name in the form database\_name.domain\_name. |
| `-templateName`  `database_template_name` | Required | Name of an existing database template in the default location or the complete path to a database template that is not in the default location. |
| `-sid`  `database_system_identifier` | Optional | Database system identifier (SID).  The SID uniquely identifies the instance that runs the database. If it is not specified, then it defaults to the database name. |
| `-createAsContainerDatabase`  `{true \| false}` | Optional | Specify `true` to create a CDB. Specify `false` to create a non-CDB. Default is `false`.  When `true` is specified, the following additional parameters are optional:  - `-numberOfPDBs`: Number of PDBs to create. The default is 0 (zero). - `-pdbName`: Base name of each PDB. A number is appended to each name if `-numberOfPDBs` is greater than 1. This parameter must be specified if `-numberOfPDBs` is greater than 0 (zero). - `-pdbStorageMAXSizeInMB`: Maximum storage size for the PDBs in megabytes. - `-pdbStorageMAXTempSizeInMB`: Maximum temporary storage size for the PDBs in megabytes. - `-useLocalUndoForPDBs {true \| false}`: Specify whether local undo should be used for the PDBs. - `-pdbAdminPassword`: PDB administrator password. - `-pdbOptions`: Specify PDB options as comma separated list in `name:value` format. 	Example: `JSERVER:true`, `DV:false` |
| `-sysPassword`  `SYS_user_password` | Optional | `SYS` user password for the new database. |
| `-systemPassword`  `SYSTEM_user_password` | Optional | `SYSTEM` user password for the new database. |
| `-emConfiguration`  `{DBEXPRESS \| CENTRAL \| BOTH \| NONE}` | Optional | Enterprise Manager configuration settings.  When `DBEXPRESS`, `CENTRAL`, or `BOTH` is specified, specify the following additional parameters:  - `-dbsnmpPassword`: DBSNMP user password. - `-omsHost`: Oracle Management Server host name. - `-omsPort`: Oracle Management Server port number. - `-emUser`: User name for Enterprise Manager administrator. - `-emPassword`: Password for Enterprise Manager administrator. - `-emExpressPort`: Enterprise Manager Express port number. - `-emExpressPortAsGlobalPort`: Enterprise Manager Express global port number. |
| `-dvConfiguration`  `{true \| false}` | Optional | Specify `true` to enable and configure Database Vault, else specify `false`. Default is `false`.  When `true` is specified, the following additional Database Vault parameters are required:  - `-dvUserName`: Specify Database Vault owner name. - `-dvUserPassword`: Specify Database Vault owner password. - `-dvAccountManagerName`: Specify Database Vault account manager name. - `-dvAccountManagerPassword`: Specify Database Vault account manager password. |
| `-olsConfiguration`  `{true \| false}` | Optional | Specify `true` to enable and configure Oracle Label Security (OLS), else specify `false`. Default is `false`.  When `true` is specified, you can additionally specify the `-configureWithOID` parameter, if you want to configure Oracle Label Security (OLS) with Oracle Internet Directory (OID). |
| `-datafileDestination`  `data_files_directory` | Optional | Complete path to the location of the database data files. |
| `-redoLogFileSize`  `maximum_size_of_redo_log_file` | Optional | Size of each online redo log in megabytes. |
| `-recoveryAreaDestination`  `fast_recovery_area_directory` | Optional | Destination directory for the Fast Recovery Area, which is a backup and recovery area. Specify `NONE` to disable Fast Recovery Area.  Additionally, you can specify the Fast Recovery Area size in megabytes using the parameter `-recoveryAreaSize`. This parameter is optional. |
| `-datafileJarLocation`  `data_files_backup_directory` | Optional | Absolute directory path of the database backup data files stored in a compressed RMAN backup format (files with.dfb extensions). |
| `-storageType`  `{FS \| ASM}` | Optional | Specify the storage type of either `FS` or `ASM`.  - `FS`: File system storage type. 	When `FS` is specified, your database files are managed by the file system of your operating system. You can specify the directory path where the database files are to be stored using a database template or the `-datafileDestination` parameter. Oracle Database can create and manage the actual files. - `ASM`: Oracle Automatic Storage Management (Oracle ASM) storage type. 	When `ASM` is specified, your database files are placed in Oracle ASM disk groups. Oracle Database automatically manages database file placement and naming. 	When `ASM` is specified, you can also specify the ASMSNMP password using the `-asmsnmpPassword` parameter. This parameter is optional. |
| `-useWalletForDBCredentials`  `{true \| false}` | Optional | Specify `true` to use Oracle Wallet for database credentials, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters can be provided:  - `-dbCredentialsWalletLocation`: Directory location for the Oracle Wallet files. - `-dbCredentialsWalletPassword`: Password for the Oracle Wallet account.  Note:  If you are using Oracle Unified Directory (OUD), then the OUD passwords should be stored in the wallet using the following keys:  - `oracle.dbsecurity.walletPassword` - `oracle.dbsecurity.userDNPassword` |
| `-runCVUChecks`  `{true \| false}` | Optional | Specify `true` to run Cluster Verification Utility checks periodically for Oracle RAC databases, else specify `false`. Default is `false`. |
| `-nodelist`  `database_nodes_list` | Optional | List of database nodes separated by comma. |
| `-enableArchive`  `{true \| false}` | Optional | Specify `true` to enable log file archive, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters can be provided:  - `-archiveLogMode {AUTO \| MANUAL}`: Specify either the automatic archive mode or the manual archive mode. Default is automatic archive mode. - `-archiveLogDest`: Directory path for storing the archive log files. |
| `-memoryMgmtType`  `{AUTO \| AUTO_SGA \| CUSTOM_SGA}` | Optional | Specify one of the following memory management types:  - `AUTO`: Automatic memory management for SGA and PGA. - `AUTO_SGA`: Automatic shared memory management for SGA. - `CUSTOM_SGA`: Manual shared memory management for SGA.  Note: If the total physical memory of a database instance is greater than 4 GB, then you cannot specify the Automatic Memory Management option `AUTO` during the database installation and creation. Oracle recommends that you specify the Automatic Shared Memory Management option `AUTO_SGA` in such environments. |
| `-createListener`  `new_database_listener` | Optional | Database listener to register the database in the form listener\_name:port. |
| `-useOMF`  `{true \| false}` | Optional | Specify `true` to use Oracle-Managed Files (OMF), else specify `false`. Default is `false`. |
| `-dbOptions`  `database_options` | Optional | Specify database options as comma separated list of `name:value` pairs.  Example: `JSERVER:true,DV:false` |
| `-customScripts`  `custom_scripts_list` | Optional | Specify a comma separated list of SQL scripts that needs to be run after the database creation. The scripts are run in the order they are listed. |
| `-oracleHomeUserName`  `Oracle_Home_user_name`  `-oracleHomeUserPassword`  `Oracle_Home_user_password` | Optional | Oracle Home user name and password. |
| `-policyManaged` | Optional | Policy-managed database.  You can specify the following additional parameters:  - `-serverPoolName`: Specify the single server pool name when creating a new server pool or specify a comma separated list of existing server pools. - `-pqPoolName`: Specify the PQ pool name. - `-createServerPool`: Specify this parameter for creating a new server pool. 	: 	- `-pqPoolName`: Specify the PQ pool name. 		- `-force`: Specify this parameter to create the server pool by force when adequate free servers are not available. 		- `-pqCardinality`: Specify the PQ cardinality of the new server pool. 		- `-cardinality`: Specify the cardinality of the new server pool. |
| `-adminManaged` | Optional | Administrator-managed database. |
| `-databaseConfigType`  `{SINGLE \| RAC \| RACONENODE}` | Optional | Specify one of the following database configuration types:  - `SINGLE`: Single individual database. - `RAC`: Oracle RAC database. - `RACONENODE`: Oracle RAC One Node database. 	For Oracle RAC One Node database, you can specify the service name using the `-RACOneNodeServiceName` parameter. |
| `-characterSet`  `database_character_set` | Optional | Character set of the database. |
| `-nationalCharacterSet`  `database_national_character_set` | Optional | National character set of the database. |
| `-registerWithDirService `  `{true \| false}` | Optional | Specify `true` to register with a Lightweight Directory Access Protocol (LDAP) service, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters are required:  - `-dirServiceUserName`: Username for the LDAP service. - `-dirServicePassword`: Password for the LDAP service. - `-databaseCN`: Database common name. - `-dirServiceCertificatePath`: Directory path to the certificate file to use when configuring SSL between the database and the directory service. - `-dirServiceUser`: Directory service user name. - `-ldapDirectoryAccessType {PASSWORD \| SSL}`: LDAP directory access type. - `-useSYSAuthForLDAPAccess {true \| false}`: Specify whether to use SYS user authentication for LDAP acces. - `-walletPassword`: Password for the database wallet. |
| `-listeners`  `listeners_list` | Optional | A comma-separated list of listeners for the database. |
| `-variablesFile`  `variables_file` | Optional | Name of the variables file with the complete directory path in the database template. |
| `-variables`  `variables_list` | Optional | A comma-separated list of `name=value` pairs for the variables in the database template. |
| `-initParams`  `initialization_parameters_list` | Optional | A comma-separated list of `name=value` pairs of initialization parameter values for the database.  You can additionally provide the `-initParamsEscapeChar` parameter for using a specific escape character between multiple values of an initialization parameter. If an escape character is not specified, backslash (/) is used as the default escape character. |
| `-sampleSchema`  `{true \| false}` | Optional | Specify `true` to include the `HR` sample schema (`EXAMPLE` tablespace) in your database. Oracle guides and educational materials contain examples based on the sample schemas. Oracle strongly recommends that you do not install the sample schemas in a production database.  Specify `false` to create the database without the `HR` sample schema. Default is `false`. |
| `-memoryPercentage`  `percentage_of_total_memory_to_assign_to_oracle_database`  or  `-totalMemory`  `total_memory_to_assign_to_oracle_database_in_MB` | Optional | Specify either `-memoryPercentage` or `-totalMemory`.  - `-memoryPercentage` 	The percentage of physical memory that can be used by the database. - `-totalMemory`. 	Total amount of physical memory, in megabytes, that can be used by the database. |
| `-databaseType`  `{MULTIPURPOSE \| DATA_WAREHOUSING \| OLTP}` | Optional | Specify `MULTIPURPOSE` if the database is for both OLTP and data warehouse purposes.  Specify `DATA_WAREHOUSING` if the primary purpose of the database is a data warehouse.  Specify `OLTP` if the primary purpose of the database is online transaction processing. |

See Also:

[Oracle Database Sample Schemas](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=COMSC)

**Parent topic:** DBCA Silent Mode Commands

##### 2.14.4.2 createDuplicateDB

The `createDuplicateDB` command creates a duplicate of an Oracle database.

Prerequisites

The following are the prerequisites for using the `createDuplicateDB` command:

- The database to be duplicated is in the archivelog mode.
- If the database to be duplicated is in a remote server, then there must be connectivity from the system where DBCA is running to the remote server.

Syntax and Parameters

Use the `dbca` `-createDuplicateDB` command with the following syntax:

```
dbca -createDuplicateDB 
    -gdbName global_database_name 
    -primaryDBConnectionString easy_db_connection_string
    -sid database_system_identifier
    [-initParams initialization_parameters
        [-initParamsEscapeChar initialization_parameters_escape_character]]
    [-sysPassword SYS_user_password]
    [-policyManaged | -adminManaged]
    [-policyManaged
        -serverPoolName server_pool_names
        [-pqPoolName pq_pool_name]
        [-createServerPool new_server_pool_name
            [-pqPoolName new_pq_pool_name]
            [-force]
            [-pqCardinality pq_cardinality_of_the_new_server_pool]
            [-cardinality cardinality_of_the_new_server_pool]]]
    [-adminManaged]
    [-nodelist database_nodes_list]
    [-datafileDestination data_files_directory]
    [-recoveryAreaDestination recovery_files_directory
        [-recoveryAreaSize fast_recovery_area_size]]
    [-databaseConfigType {SINGLE | RAC | RACONENODE}
        [-RACOneNodeServiceName service_name_for_RAC_One_Node_database]]
    [-useOMF {true | false}]
    [-storageType {FS | ASM} 
        [-asmsnmpPassword ASMSNMP_password]
        -datafileDestination database_files_directory]
    [-createListener new_database_listener]
    [-createAsStandby 
        [-dbUniqueName db_unique_name_for_standby_database]]
    [-customScripts custom_sql_scripts_to_run_after_database_creation]
    [-useWalletForDBCredentials {true | false}
        -dbCredentialsWalletPassword wallet_account_password
        -dbCredentialsWalletLocation wallet_files_directory]
```

Table 2-6 createDuplicateDB Parameters

| Parameter | Required/Optional | Description |
| --- | --- | --- |
| `-gdbName` `global_database_name` | Required | Global database name of the duplicate database in the form database\_name.domain\_name. |
| `-primaryDBConnectionString` `easy_db_connection_string` | Required | Easy connection string to connect to the database to be duplicated. Easy connection string must be in the following format:  `"host[:port][/service_name][:server][/instance_name]"`  See the description of "connect\_identifier (2)" at " [Syntax of the SQL\*Plus CONNECT Command](getting-started-with-database-administration.md) " for more information. |
| `-sid` `database_system_identifier` | Required | Database system identifier (SID) of the duplicate database.  The SID uniquely identifies the instance that runs the database. If it is not specified, then it defaults to the database name. |
| `-initParams`  `initialization_parameters_list` | Optional | A comma-separated list of `name=value` pairs of initialization parameter values for the database.  You can additionally provide the `-initParamsEscapeChar` parameter for using a specific escape character between multiple values of an initialization parameter. If an escape character is not specified, backslash (/) is used as the default escape character. |
| `-sysPassword`  `SYS_user_password` | Optional | `SYS` user password. |
| `-policyManaged` | Optional | Policy-managed database.  Note: You can specify either policy-managed database or administrator-managed database.  You can specify the following additional parameters:  - `-serverPoolName`: Specify the single server pool name when creating a new server pool or specify a comma separated list of existing server pools. - `-pqPoolName`: Specify the PQ pool name. - `-createServerPool`: Specify this parameter for creating a new server pool. 	- `-pqPoolName`: Specify the PQ pool name. 		- `-force`: Specify this parameter to create the server pool by force when adequate free servers are not available. 		- `-pqCardinality`: Specify the PQ cardinality of the new server pool. 		- `-cardinality`: Specify the cardinality of the new server pool. |
| `-adminManaged` | Optional | Administrator-managed database.  Note: You can specify either policy-managed database or administrator-managed database. |
| `-nodelist`  `database_nodes_list` | Optional | For administrator-managed database, specify database nodes separated by comma. |
| `-datafileDestination `  `data_files_directory` | Optional | Complete directory path for database data files. |
| `-recoveryAreaDestination`  `fast_recovery_area_directory` | Optional | Destination directory for the Fast Recovery Area, which is a backup and recovery area. Specify `NONE` to disable Fast Recovery Area.  Additionally, you can specify the Fast Recovery Area size in megabytes using the parameter `-recoveryAreaSize`. This parameter is optional. |
| `-databaseConfigType`  `{SINGLE \| RAC \| RACONENODE}` | Optional | Specify one of the following database configuration types:  - `SINGLE`: Single individual database. - `RAC`: Oracle RAC database. - `RACONENODE`: Oracle RAC One Node database. 	For Oracle RAC One Node database, you can specify the service name using the `-RACOneNodeServiceName` parameter. |
| `-useOMF`  `{true \| false}` | Optional | Specify `true` to use Oracle-Managed Files (OMF), else specify `false`. Default is `false`. |
| `-storageType`  `{FS \| ASM}` | Optional | Specify the storage type of either `FS` or `ASM`.  - `FS`: File system storage type. 	When `FS` is specified, your database files are managed by the file system of your operating system. You can specify the directory path where the database files are to be stored using a database template or the `-datafileDestination` parameter. Oracle Database can create and manage the actual files. - `ASM`: Oracle Automatic Storage Management (Oracle ASM) storage type. 	When `ASM` is specified, your database files are placed in Oracle ASM disk groups. Oracle Database automatically manages database file placement and naming. 	When `ASM` is specified, you can also specify the ASMSNMP password using the `-asmsnmpPassword` parameter. This parameter is optional. |
| `-createListener`  `new_database_listener` | Optional | Database listener to register the database in the form listener\_name:port. |
| `-createAsStandby` | Optional | Specifies that the duplicate database is a standby database for the primary database.  Optionally, use the `-dbUniqueName` parameter to set the unique database name for the standby database. If the `-dbUniqueName` parameter is not specified, then the value of the `DB_NAME` initialization parameter is used. |
| `-customScripts` `custom_sql_scripts_to_run_after_database_creation` | Optional | A comma separated list of SQL scripts that should be run after the duplicate database is created. The scripts are run in the order listed. |
| `-useWalletForDBCredentials`  `{true \| false}` | Optional | Specify `true` to use Oracle Wallet for database credentials, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters can be provided:  - `-dbCredentialsWalletPassword`: Password for the Oracle Wallet account. - `-dbCredentialsWalletLocation`: Directory location for the Oracle Wallet files.  Note:  If you are using Oracle Unified Directory (OUD), then the OUD passwords should be stored in the wallet using the following keys:  - `oracle.dbsecurity.walletPassword` - `oracle.dbsecurity.userDNPassword` |

##### 2.14.4.3 configureDatabase

The `configureDatabase` command configures a database.

Syntax and Parameters

Use the `dbca` `-configureDatabase` command with the following syntax:

```
dbca -configureDatabase 
   -sourceDB database_sid
   [-sysDBAUserName SYSDBA_user_name]
   [-sysDBAPassword SYSDBA_user_password]
   [-registerWithDirService {true | false}
      -dirServiceUserName directory_service_user_name
      [-databaseCN database_common_name]
      [-dirServiceCertificatePath certificate_file_path]
      [-dirServiceUser directory_service_user_name]
      [-dirServicePassword directory_service_password]
      [-ldapDirectoryAccessType ldap_directory_access_type]
      [-useSYSAuthForLDAPAccess use_sys_user_for_ldap_access_flag]
      [-walletPassword wallet_password]]
   [-unregisterWithDirService {true | false}
      -dirServiceUserName directory_service_user_name
      [-dirServicePassword directory_service_password]
      [-walletPassword wallet_password]]
   [-addDBOption database_options]
   [-dvConfiguration {true | false}
      -dvUserName Database_Vault_owner_name
      -dvUserPassword Database_Vault_owner_password
      [-dvAccountManagerName Database_Vault_account_manager_name]
      [-dvAccountManagerPassword Database_Vault_account_manager_password]]
   [-olsConfiguration {true | false}
      -configureWithOID configure_with_OID_flag]
   [-configureOracleR
      -oracleRConfigTablespace tablespace_for_Oracle_R_configuration]
   [-moveDatabaseFiles
      -datafileDestination data_files_directory
      -sourceDB database_sid
      [-initParams initialization_parameters_list
        [-initParamsEscapeChar initialization_parameters_escape_character]]
      [-recoveryAreaDestination fast_recovery_area_directory
        [-recoveryAreaSize fast_recovery_area_size]]
      [-useOMF {true | false}]
   [-regenerateDBPassword {true | false}]
   [-useWalletForDBCredentials {true | false} 
      -dbCredentialsWalletPassword wallet_account_password
      -dbCredentialsWalletLocation wallet_files_directory]
```

Table 2-7 configureDatabase Parameters

| Parameter | Required/Optional | Description |
| --- | --- | --- |
| `-sourceDB` `database_sid` | Required | The database system identifier (SID) of the database being configured. |
| `-sysDBAUserName` `SYSDBA_user_name` | Optional | User name of a user having `SYSDBA` privileges. |
| `-sysDBAPassword` `SYSDBA_user_password` | Optional | Password of a user having `SYSDBA` privileges. |
| `-registerWithDirService`  `{true \| false}` | Optional | Specify `true` to register with a Lightweight Directory Access Protocol (LDAP) service, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters are required:  - `-dirServiceUserName`: User name for the LDAP service. - `-dirServicePassword`: Password for the LDAP service. - `-databaseCN`: Database common name. - `-dirServiceCertificatePath`: Directory service certificate file path. - `-dirServiceUser`: Directory service user name. - `-ldapDirectoryAccessType {PASSWORD \| SSL}`: LDAP directory access type. - `-useSYSAuthForLDAPAccess {true \| false}`: Specify whether to use SYS user authentication for LDAP access. - `-walletPassword`: Password for the database wallet. |
| `-unregisterWithDirService `  `{true \| false}` | Optional | Specify `true` to unregister with a Lightweight Directory Access Protocol (LDAP) service, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters are required:  - `-dirServiceUserName`: User name for the LDAP service. - `-dirServicePassword`: Password for the LDAP service. - `-walletPassword`: Password for the database wallet. |
| `-addDBOption`  `database_options` | Optional | Specify one or more of the following Oracle Database options in the form of a comma separated list:  - `JSERVER`: Oracle JServer JAVA Virtual Machine - `ORACLE_TEXT`: Oracle Text - `IMEDIA`: Oracle Locator (fully supported) and Oracle Multimedia (desupported) - `CWMLITE`: Oracle OLAP with Oracle Warehouse Builder (OWB) - `SPATIAL`: Oracle Spatial and Graph - `OMS`: Oracle Management Server - `APEX`: Oracle Application Express - `DV`: Oracle Database Vault  Example:  ``` -addDBOption JSERVER,ORACLE_TEXT,OMS ``` |
| `-dvConfiguration`  `{true \| false}` | Optional | Specify `true` to enable and configure Database Vault, or specify `false`. Default is `false`.  When `true` is specified, the following additional Database Vault parameters are required:  - `-dvUserName`: Specify the Database Vault owner username. - `-dvUserPassword`: Specify Database Vault owner password. - `-dvAccountManagerName`: Specify a separate Database Vault account manager. - `-dvAccountManagerPassword`: Specify the Database Vault account manager password. |
| `-olsConfiguration`  `{true \| false}` | Optional | Specify `true` to enable and configure Oracle Label Security, else specify `false`. Default is `false`.  When `true` is specified, you can additionally specify the `-configureWithOID` parameter to configure Oracle Label Security with Oracle Internet Directory (OID). This parameter is optional. |
| `-configureOracleR` | Optional | Specify this parameter to configure Oracle R in the database.  Additionally, you can specify the `-oracleRConfigTablespace` parameter to assign a tablespace for the Oracle R configuration, such as `SYSAUX` tablespace. |
| `-moveDatabaseFiles` | Optional | Specify this parameter to move database files from one storage location to another storage location. For example, to move database files from ASM to FS, or from FS to ASM.  Specify the following additional parameters:  - `-datafileDestination`: Destination directory for all the database files - `-sourceDB`: Database system identifier (SID) for a single instance database or database unique name for an Oracle RAC database - `-initParams`: Database initialization parameters in the form of comma separated list of `name=value` pairs 	Additionally, you can specify the `-initParamsEscapeChar` parameter for using a specific escape character between multiple values of an initialization parameter. If an escape character is not specified, backslash (/) is used as the default escape character. - `-recoveryAreaDestination`: Destination directory for the Fast Recovery Area, which is a backup and recovery area. Specify `NONE` to disable Fast Recovery Area. 	Additionally, you can specify the Fast Recovery Area size in megabytes using the parameter `-recoveryAreaSize`. This parameter is optional. - `-useOMF`: Specify `true` to use Oracle-Managed Files (OMF), else specify `false`. |
| `-regenerateDBPassword` `{true \| false}` | Optional | Specify `true` to regenerate Oracle Internet Directory (OID) server registration password, else specify `false`. Default is `false`. |
| `-useWalletForDBCredentials`  `{true \| false}` | Optional | Specify `true` to use Oracle Wallet for database credentials, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters can be provided:  - `-dbCredentialsWalletLocation`: Directory location for the Oracle Wallet files. - `-dbCredentialsWalletPassword`: Password for the Oracle Wallet account.  Note:  If you are using Oracle Unified Directory (OUD), then the OUD passwords should be stored in the wallet using the following keys:  - `oracle.dbsecurity.walletPassword` - `oracle.dbsecurity.userDNPassword` |

**Parent topic:** DBCA Silent Mode Commands

##### 2.14.4.4 createTemplateFromDB

The `createTemplateFromDB` command creates a database template from an existing database.

Syntax and Parameters

Use the `dbca` `-createTemplateFromDB` command with the following syntax:

```
dbca -createTemplateFromDB 
   -sourceDB source_database_sid
   -templateName new_database_template_name
   -sysDBAUserName SYSDBA_user_name
   -sysDBAPassword SYSDBA_user_password
   [-maintainFileLocations {true | false}]
   [-connectionString easy_connect_string]
   [-useWalletForDBCredentials {true | false}
       -dbCredentialsWalletPassword wallet_account_password
       -dbCredentialsWalletLocation wallet_files_directory]
```

Table 2-8 createTemplateFromDB Parameters

| Parameter | Required/Optional | Description |
| --- | --- | --- |
| `-sourceDB` `source_database_sid` | Required | The source database system identifier (SID). |
| `-templateName` `new_database_template_name` | Required | Name of the new database template. |
| `-sysDBAUserName` `SYSDBA_user_name` | Required | User name of a user that has `SYSDBA` privileges. |
| `-sysDBAPassword` `SYSDBA_user_password` | Required | Password of the user that has `SYSDBA` privileges. |
| `-maintainFileLocations` `{true \| false}` | Optional | Specify `true` to use the file locations of the database in the template.  Specify `false`, the default, to use different file locations in the template. The file locations are determined by Oracle Flexible Architecture (OFA). |
| `-connectionString` `easy_connect_string` | Optional | Easy connect string for connecting to a remote database in the following format:  `"host[:port][/service_name][:server][/instance_name]"` |
| `-useWalletForDBCredentials`  `{true \| false}` | Optional | Specify `true` to use Oracle Wallet for database credentials, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters can be provided:  - `-dbCredentialsWalletPassword`: Password for the Oracle Wallet account. - `-dbCredentialsWalletLocation`: Directory location for the Oracle Wallet files.  Note:  If you are using Oracle Unified Directory (OUD), then the OUD passwords should be stored in the wallet using the following keys:  - `oracle.dbsecurity.walletPassword` - `oracle.dbsecurity.userDNPassword` |

**Parent topic:** DBCA Silent Mode Commands

##### 2.14.4.5 createTemplateFromTemplate

The `createTemplateFromTemplate` command creates a database template from an existing database template.

Syntax and Parameters

Use the `dbca` `-createTemplateFromTemplate` command with the following syntax:

```
dbca -createTemplateFromTemplate 
    -sourcetemplateName existing_template_name 
    -templateName new_template_name 
    [-variables variables_list]
    [-characterSet database_character_set]
    [-nationalCharacterSet database_national_character_set]
    [-recoveryAreaDestination fast_recovery_area_directory]
        -recoveryAreaSize fast_recovery_area_size]
    [-datafileDestination data_files_directory]
    [-useOMF {true | false}]
    [-datafileJarLocation database_backup_files_directory]
    [-memoryPercentage percentage_of_total_memory_to_assign_to_oracle_database]
    [-totalMemory total_memory_to_assign_to_oracle_database]
    [-dbOptions database_options]
    [-variablesFile variables_file]
    [-redoLogFileSize redo_log_file_size]
    [-initParams initialization_parameters_list]
        [-initParamsEscapeChar escape_character_for_initialization_parameters]
    [-storageType {FS | ASM} 
        [-asmsnmpPassword ASMSNMP_password]
        -datafileDestination data_files_directory]
    [-enableArchive {true | false} 
         -archiveLogMode {AUTO | MANUAL}
         -archiveLogDest archive_logs_directory
    [-memoryMgmtType {AUTO | AUTO_SGA | CUSTOM_SGA}]
    [-useWalletForDBCredentials {true | false}
         -dbCredentialsWalletPassword wallet_account_password
         -dbCredentialsWalletLocation wallet_files_directory]
```

Table 2-9 createTemplateFromTemplate Parameters

| Parameter | Required/Optional | Description |
| --- | --- | --- |
| `-sourceTemplateName`  `existing_template_name` | Required | Name of an existing database template in the default location or the complete path to a database template that is not in the default location. |
| `-templateName`  `new_template_name` | Required | Name for a new database template. |
| `-variables`  `variables_list` | Optional | A comma-separated list of `name=value` pairs for the variables in the database template. |
| `-characterSet`  `database_character_set` | Optional | Character set of the database. |
| `-nationalCharacterSet`  `database_national_character_set` | Optional | National character set of the database. |
| `-recoveryAreaDestination`  `fast_recovery_area_directory` | Optional | Directory path for the Fast Recovery Area, which is a backup and recovery area. |
| `-datafileDestination`  `data_files_directory` | Optional | Directory path for the data files. |
| `-useOMF`  `{true \| false}` | Optional | Specify `true` to use Oracle-Managed Files (OMF), else specify `false`. |
| `-datafileJarLocation`  `database_backup_files_directory` | Optional | Location of the database offline backup (for clone database creation only).  The data files for the seed database are stored in compressed RMAN backup format in a file with a.dfb extension. |
| `-memoryPercentage`  `percentage_of_total_memory_to_assign_to_oracle_database`  or  `-totalMemory`  `total_memory_to_assign_to_oracle_database` | Optional | Specify either `-memoryPercentage` or `-totalMemory`.  - `-memoryPercentage` 	The percentage of physical memory that can be used by the database. - `-totalMemory` 	The amount of physical memory in megabytes that can be used by the database. |
| `-dbOptions`  `database_options` | Optional | Specify database options as comma separated list of `name:value` pairs.  Example: `JSERVER:true,DV:false` |
| `-variablesFile`  `variables_file` | Optional | File name with complete directory path to the file that contains the variables and their values in the database template. |
| `-redoLogFileSize`  `redo_log_file_size` | Optional | Size of each online redo log file in megabytes. |
| `-initParams`  `initialization_parameters_list` | Optional | A comma-separated list of `name=value` pairs of the database initialization parameters and their values. |
| `-storageType`  `{FS \| ASM}` | Optional | Specify `FS` for file system and `ASM` for Oracle Automatic Storage Management (Oracle ASM) system.  When `FS` is specified, your database files are managed by the file system of your operating system. You specify the directory path where the database files are to be stored using the `-datafileDestination` parameter.  When `ASM` is specified, your database files are placed in the Oracle ASM disk groups. Oracle Database automatically manages database file placement and naming. You also specify the `ASMSNMP` password for ASM monitoring using the `-asmsnmpPassword` parameter. |
| `-enableArchive`  `{true \| false}` | Optional | Specify `true` to enable log file archive. Default is `false`.  When `true` is specified, the following additional parameters can be provided:  - `-archiveLogMode {AUTO \| MANUAL}`: Specify either the automatic archive mode (`AUTO`) or the manual archive mode (`MANUAL`). Default is automatic archive mode (`AUTO`). - `-archiveLogDest`: Directory path for storing the archive log files. |
| `-memoryMgmtType`  `{AUTO \| AUTO_SGA \| CUSTOM_SGA}` | Optional | Specify one of the following memory management types:  - `AUTO`: Automatic memory management for SGA and PGA. - `AUTO_SGA`: Automatic shared memory management for SGA. - `CUSTOM_SGA`: Manual shared memory management for SGA.  Note: If the total physical memory of a database instance is greater than 4 GB, then you cannot specify the Automatic Memory Management option `AUTO` during the database installation and creation. Oracle recommends that you specify the Automatic Shared Memory Management option `AUTO_SGA` in such environments. |
| `-useWalletForDBCredentials`  `{true \| false}` | Optional | Specify `true` to use Oracle Wallet for database credentials, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters can be provided:  - `-dbCredentialsWalletPassword`: Password for the Oracle Wallet account. - `-dbCredentialsWalletLocation`: Directory location for the Oracle Wallet files.  Note:  If you are using Oracle Unified Directory (OUD), then the OUD passwords should be stored in the wallet using the following keys:  - `oracle.dbsecurity.walletPassword` - `oracle.dbsecurity.userDNPassword` |

**Parent topic:** DBCA Silent Mode Commands

##### 2.14.4.6 createCloneTemplate

The `createCloneTemplate` command creates a clone (seed) database template from an existing database.

Syntax and Parameters

Use the `dbca` `-createCloneTemplate` command with the following syntax:

```
dbca -createCloneTemplate
   -sourceSID source_database_sid | -sourceDB source_database_name
   -templateName new_database_template_name
   [-promptForWalletPassword]
   [-rmanParallelism parallelism_integer_value]
   [-maxBackupSetSizeInMB maximum_backup_set_size_in_MB]
   [-dataFileBackup {true | false}]
   [-datafileJarLocation data_files_backup_directory]
   [-sysDBAUserName SYSDBA_user_name]
   [-sysDBAPassword SYSDBA_user_password]
   [-useWalletForDBCredentials {true | false}
       -dbCredentialsWalletPassword wallet_account_password
       -dbCredentialsWalletLocation wallet_files_directory]
```

Table 2-10 createCloneTemplate Parameters

| Parameter | Required/Optional | Description |
| --- | --- | --- |
| `-sourceSID` `source_database_sid`  or  `-sourceDB` `source_database_name` | Required | Specify either the source database system identifier (SID) or the source database name. |
| `-templateName` `new_database_template_name` | Required | Name of the new database template. |
| `-sysDBAUserName` `SYSDBA_user_name` | Optional | User name of a user having the `SYSDBA` privileges. |
| `-sysDBAPassword` `SYSDBA_user_password` | Optional | Password of the user having the `SYSDBA` privileges. |
| `-maxBackupSetSizeInMB` `maximum_backup_set_size_in_MB` | Optional | Maximum backup set size in megabytes. |
| `-rmanParallelism` `parallelism_integer_value` | Optional | Parallelism integer value for RMAN operations. |
| `-datafileJarLocation` `data_files_backup_directory` | Optional | Complete directory path to store data files as a backup in a compressed format. |
| `-dataFileBackup {true \| false}` | Optional | Specify `true` to take the data files backup, else specify `false`. |
| `-useWalletForDBCredentials`  `{true \| false}` | Optional | Specify `true` to use Oracle Wallet for database credentials, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters can be provided:  - `-dbCredentialsWalletPassword`: Password for the Oracle Wallet account. - `-dbCredentialsWalletLocation`: Directory location for the Oracle Wallet files.  Note:  If you are using Oracle Unified Directory (OUD), then the OUD passwords should be stored in the wallet using the following keys:  - `oracle.dbsecurity.walletPassword` - `oracle.dbsecurity.userDNPassword` |

**Parent topic:** DBCA Silent Mode Commands

##### 2.14.4.7 deleteTemplate

The `deleteTemplate` command deletes a database template.

Syntax and Parameters

Use the `dbca` `-deleteTemplate` command with the following syntax:

```
dbca -deleteTemplate 
   -templateName name_of_an_existing_database_template
   [-useWalletForDBCredentials {true | false}
      -dbCredentialsWalletPassword wallet_account_password
      -dbCredentialsWalletLocation wallet_files_directory]
```

Table 2-11 deleteTemplate Parameters

| Parameter | Required/Optional | Description |
| --- | --- | --- |
| `-templateName`  `name_of_an_existing_database_template` | Required | Name of an existing database template to delete. |
| `-useWalletForDBCredentials`  `{true \| false}` | Optional | Specify `true` to use Oracle Wallet for database credentials, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters can be provided:  - `-dbCredentialsWalletPassword`: Password for the Oracle Wallet account. - `-dbCredentialsWalletLocation`: Directory location for the Oracle Wallet files.  Note:  If you are using Oracle Unified Directory (OUD), then the OUD passwords should be stored in the wallet using the following keys:  - `oracle.dbsecurity.walletPassword` - `oracle.dbsecurity.userDNPassword` |

**Parent topic:** DBCA Silent Mode Commands

##### 2.14.4.8 generateScripts

The `generateScripts` command generates scripts, which can be used to create a database.

Syntax and Parameters

Use the `dbca` `-generateScripts` command with the following syntax:

```
dbca -generateScripts 
    -templateName database_template_name 
    -gdbName global_database_name 
    [-sid database_system_identifier]
    [-scriptDest sql_scripts_directory]
    [-createAsContainerDatabase {true | false}
        [-numberOfPDBs number_of_pdbs_to_create]
        [-pdbName pdb_name]
        [-pdbStorageMAXSizeInMB maximum_storage_size_of_the_pdb]
        [-pdbStorageMAXTempSizeInMB maximum_temporary_storage_size_of_the_pdb]
        [-useLocalUndoForPDBs {true | false}]
        [-pdbAdminPassword pdb_administrator_password]
        [-pdbOptions pdb_options]
    [-sysPassword SYS_user_password]
    [-systemPassword SYSTEM_user_password]
    [-emConfiguration {DBEXPRESS | CENTRAL | BOTH | NONE}
        [-dbsnmpPassword DBSNMP_user_password]
        [-omsHost EM_Management_Server_host_name]
        [-omsPort EM_Management_Server_port_number]
        [-emUser EM_administrator_name]
        [-emPassword EM_administrator_password]
        [-emExpressPort EM_Express_port]
        [-emExpressPortAsGlobalPort EM_Express_global_port]]
    [-dvConfiguration {true | false}
        -dvUserName Database_Vault_owner_user_name
        -dvUserPassword Database_Vault_owner_user_password
        [-dvAccountManagerName Database_Vault_account_manager_name
        -dvAccountManagerPassword Database_Vault_account_manager_password]]
    [-olsConfiguration {true | false}
        [-configureWithOID configure_with_OID_flag]]
    [-datafileDestination data_files_directory]
    [-redoLogFileSize maximum_redo_log_file_size_in_MB]
    [-recoveryAreaDestination fast_recovery_area_directory
        [-recoveryAreaSize fast_recovery_area_size]]
    [-datafileJarLocation data_files_backup_directory]
    [-responseFile response_file_directory]
    [-storageType {FS | ASM} 
        [-asmsnmpPassword ASMSNMP_password]
        -datafileDestination data_files_directory]
    [-runCVUChecks {true | false}]
    [-nodelist database_nodes_list]
    [-enableArchive {true | false} 
        [-archiveLogMode {AUTO | MANUAL}]
        [-archiveLogDest archive_log_files_directory]]
    [-memoryMgmtType {AUTO | AUTO_SGA | CUSTOM_SGA}]
    [-createListener new_database_listener_to_register_the_database_with]
    [-useOMF {true | false}]
    [-dbOptions database_options]
    [-customScripts custom_sql_scripts_to_run_after_database_creation]
    [-policyManaged | -adminManaged]
    [-policyManaged
        -serverPoolName server_pool_names
        [-pqPoolName pq_pool_name]
        [-createServerPool new_server_pool_name]
            [-pqPoolName new_pq_pool_name]
            [-force]
            [-pqCardinality pq_cardinality_of_the_new_server_pool]
            [-cardinality cardinality_of_the_new_server_pool]]
    [-adminManaged]
    [-databaseConfigType {SINGLE | RAC | RACONENODE}
            [-RACOneNodeServiceName service_name_for_RAC_one_node_database]]
    [-characterSet database_character_set]
    [-nationalCharacterSet database_national_character_set]
    [-registerWithDirService {true | false} 
        [-dirServiceUserName directory_service_user_name]
        [-dirServicePassword directory_service_user_password]
        [-databaseCN database_common_name]
        [-dirServiceCertificatePath certificate_file_path]
        [-dirServiceUser directory_service_user_name]
        [-ldapDirectoryAccessType ldap_directory_access_type]
        [-useSYSAuthForLDAPAccess use_sys_user_for_ldap_access_flag]
        [-walletPassword wallet_password]]
    [-listeners list_of_listeners_to_register_the_database_with]
    [-variablesFile variables_file]
    [-variables variables_list]
    [-initParams initialization_parameters_list
        [-initParamsEscapeChar initialization_parameters_escape_character]]
    [-sampleSchema {true | false}]
    [-memoryPercentage percentage_of_total_memory_to_assign_to_the_database]
    [-totalMemory total_memory_to_assign_to_the_database_in_MB]
    [-databaseType {MULTIPURPOSE | DATA_WAREHOUSING | OLTP}]
    [-useWalletForDBCredentials {true | false}
        -dbCredentialsWalletPassword wallet_account_password
        -dbCredentialsWalletLocation wallet_files_directory]
```

Table 2-12 generateScripts Parameters

| Parameter | Required/Optional | Description |
| --- | --- | --- |
| `-templateName` `database_template_name` | Required | Name of an existing database template in the default location or the complete path of a template that is not in the default location. |
| `-gdbName` `global_database_name` | Required | Global database name in the form database\_name.domain\_name. |
| `-sid`  `database_system_identifier` | Optional | Database system identifier (SID).  The SID uniquely identifies the instance that runs the database. If it is not specified, then it defaults to the database name. |
| `-scriptDest` `scripts_directory` | Optional | Complete directory path to store the scripts. |
| `-createAsContainerDatabase`  `{true \| false}` | Optional | Specify `true` to create a CDB, else specify `false` to create a non-CDB. Default is `false`.  When `true` is specified, the following optional parameters can be provided:  - `-numberOfPDBs`: Number of PDBs to create. Default is 0 (zero). - `-pdbName`: Name of each PDB. A number is appended to each PDB name if `-numberOfPDBs` value is greater than 1. This parameter must be specified if `-numberOfPDBs` value is greater than 0 (zero). - `-pdbStorageMAXSizeInMB`: Maximum storage size for a PDB in megabytes. - `-pdbStorageMAXTempSizeInMB`: Maximum temporary storage size for a PDB in megabytes. - `-useLocalUndoForPDBs {true \| false}`: Flag indicating whether local undo should be used for the PDBs. - `-pdbAdminPassword`: PDB administrator password. - `-pdbOptions`: PDB options in the form of comma separated list. Each option must be specified in the `name:value` format. 	Example: `JSERVER:true,DV:false` |
| `-sysPassword`  `SYS_user_password` | Optional | `SYS` user password for the new database. |
| `-systemPassword`  `SYSTEM_user_password` | Optional | `SYSTEM` user password for the new database. |
| `-emConfiguration`  `{DBEXPRESS \| CENTRAL \| BOTH \| NONE}` | Optional | Enterprise Manager configuration settings.  When `DBEXPRESS`, `CENTRAL`, or `BOTH` is specified, specify the following additional parameters:  - `-dbsnmpPassword`: DBSNMP user password. - `-omsHost`: Oracle Management Server host name. - `-omsPort`: Oracle Management Server port number. - `-emUser`: User name for Enterprise Manager administrator. - `-emPassword`: Password for Enterprise Manager administrator. - `-emExpressPort`: Enterprise Manager Express port number. - `-emExpressPortAsGlobalPort`: Enterprise Manager Express global port number. |
| `-dvConfiguration`  `{true \| false}` | Optional | Specify `true` to enable and configure Database Vault, else specify `false`. Default is `false`.  When `true` is specified, the following additional Database Vault parameters are required:  - `-dvUserName`: Database Vault owner name. - `-dvUserPassword`: Database Vault owner password. - `-dvAccountManagerName`: Database Vault account manager name. - `-dvAccountManagerPassword`: Database Vault account manager password. |
| `-olsConfiguration`  `{true \| false}` | Optional | Specify `true` to enable and configure Oracle Label Security (OLS), else specify `false`. Default is `false`.  When `true` is specified, you can additionally specify the `-configureWithOID` parameter to configure Oracle Label Security (OLS) with Oracle Internet Directory (OID). This parameter is optional. |
| `-datafileDestination`  `data_files_directory` | Optional | Complete path to the location of the database's data files. |
| `-redoLogFileSize`  `maximum_size_of_online_redo_log` | Optional | Size of each online redo log file in megabytes. |
| `-recoveryAreaDestination`  `fast_recovery_area_directory` | Optional | Directory for the Fast Recovery Area, which is a backup and recovery area. Specify `NONE` to disable the Fast Recovery Area.  Additionally, you can specify the Fast Recovery Area size in megabytes using the parameter `-recoveryAreaSize`. This parameter is optional. |
| `-datafileJarLocation`  `data_files_backup_directory` | Optional | Directory of the database backup data files in a compressed RMAN backup format (files with.dfb extensions). |
| `-responseFile`  `response_file_directory` | Optional | Directory path of the response file. |
| `-storageType`  `{FS \| ASM}` | Optional | Specify the storage type of either `FS` or `ASM`.  - `FS`: File system storage type. 	When `FS` is specified, your database files are managed by the file system of your operating system. You can specify the directory path where the database files are to be stored using a database template or the `-datafileDestination` parameter. Oracle Database can create and manage the actual files. - `ASM`: Oracle Automatic Storage Management (Oracle ASM) storage type. 	When `ASM` is specified, your database files are placed in Oracle ASM disk groups. Oracle Database automatically manages database file placement and naming. 	When `ASM` is specified, you can also specify the ASMSNMP password using the `-asmsnmpPassword` parameter. This parameter is optional. |
| `-runCVUChecks`  `{true \| false}` | Optional | Specify `true` to run Cluster Verification Utility checks periodically for Oracle RAC databases, else specify `false`. Default is `false`. |
| `-nodelist`  `database_nodes_list` | Optional | List of database nodes separated by comma. |
| `-enableArchive`  `{true \| false}` | Optional | Specify `true` to enable log file archive, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters can be provided:  - `-archiveLogMode {AUTO \| MANUAL}`: Specify either the automatic archive mode or the manual archive mode. Default is automatic archive mode. - `-archiveLogDest`: Directory for storing the archive log files. |
| `-memoryMgmtType`  `{AUTO \| AUTO_SGA \| CUSTOM_SGA}` | Optional | Specify one of the following memory management types:  - `AUTO`: Automatic memory management for SGA and PGA. - `AUTO_SGA`: Automatic shared memory management for SGA. - `CUSTOM_SGA`: Manual shared memory management for SGA.  Note: If the total physical memory of a database instance is greater than 4 GB, then you cannot specify the Automatic Memory Management option `AUTO` during the database installation and creation. Oracle recommends that you specify the Automatic Shared Memory Management option `AUTO_SGA` in such environments. |
| `-createListener`  `new_database_listener` | Optional | Database listener to register the database with in the form listener\_name:port. |
| `-useOMF`  `{true \| false}` | Optional | Specify `true` to use Oracle-Managed Files (OMF), else specify `false`. |
| `-dbOptions`  `database_options` | Optional | Specify database options as a comma separated list of `name:value` pairs.  Example: `JSERVER:true,DV:false` |
| `-customScripts`  `custom_sql_scripts_list` | Optional | Specify a comma separated list of SQL scripts that need to be run after the database creation. The scripts are run in the order they are listed. |
| `-policyManaged` | Optional | Policy-managed database.  You can specify the following additional parameters:  - `-serverPoolName`: Specify the single server pool name when creating a new server pool or specify a comma separated list of existing server pools. - `-pqPoolName`: Specify the PQ pool name. - `-createServerPool`: Specify this parameter for creating a new server pool. 	- `-pqPoolName`: Specify the PQ pool name. 		- `-force`: Specify this parameter to create the server pool by force when adequate free servers are not available. 		- `-pqCardinality`: Specify the PQ cardinality of the new server pool. 		- `-cardinality`: Specify the cardinality of the new server pool. |
| `-adminManaged` | Optional | Administrator-managed database. |
| `-databaseConfigType`  `{SINGLE \| RAC \| RACONENODE}` | Optional | Specify one of the following database configuration types:  - `SINGLE`: Single individual database. - `RAC`: Oracle RAC database. - `RACONENODE`: Oracle RAC One Node database. 	For Oracle RAC One Node database, you can specify the service name using the `-RACOneNodeServiceName` parameter. |
| `-characterSet`  `database_character_set` | Optional | Character set of the database. |
| `-nationalCharacterSet`  `database_national_character_set` | Optional | National character set of the database. |
| `-registerWithDirService `  `{true \| false}` | Optional | Specify `true` to register with a Lightweight Directory Access Protocol (LDAP) service, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters are required:  - `-dirServiceUserName`: User name for the LDAP service. - `-dirServicePassword`: Password for the LDAP service. - `-databaseCN`: Database common name. - `-dirServiceCertificatePath`: Directory service certificate file path. - `-dirServiceUser`: Directory service user name. - `-ldapDirectoryAccessType {PASSWORD \| SSL}`: LDAP directory access type. - `-useSYSAuthForLDAPAccess {true \| false}`: Specify whether to use SYS user authentication for LDAP acces. - `-walletPassword`: Password for the database wallet. |
| `-listeners`  `listeners_list` | Optional | A comma-separated list of listeners for the database. |
| `-variablesFile`  `variables_file` | Optional | Directory path to the file that contains the variables and their values for the database template. |
| `-variables`  `variables_list` | Optional | A comma-separated list of `name=value` pairs of variables for the database template. |
| `-initParams`  `initialization_parameters_list` | Optional | A comma-separated list of `name=value` pairs of initialization parameter values of the database.  You can additionally provide the `-initParamsEscapeChar` parameter for using a specific escape character between multiple values of an initialization parameter. If an escape character is not specified, backslash (/) is used as the default escape character. |
| `-sampleSchema`  `{true \| false}` | Optional | Specify `true` to include the `HR` sample schema (`EXAMPLE` tablespace) in your database, else specify `false`. Default is `false`.  Oracle guides and educational materials contain examples based on the sample schemas. Oracle strongly recommends that you do not install the sample schemas in a production database. |
| `-memoryPercentage`  `percentage_of_total_memory_assigned_to_the_database` | Optional | The percentage of physical memory that can be used by the database. |
| `-totalMemory`  `total_memory_assigned_to_the_database_in_MB` | Optional | Total amount of physical memory, in megabytes, that can be used by the database. |
| `-databaseType`  `{MULTIPURPOSE \| DATA_WAREHOUSING \| OLTP}` | Optional | Specify `MULTIPURPOSE` if the database is for both OLTP and data warehouse purposes.  Specify `DATA_WAREHOUSING` if the primary purpose of the database is a data warehouse.  Specify `OLTP` if the primary purpose of the database is online transaction processing. |
| `-useWalletForDBCredentials`  `{true \| false}` | Optional | Specify `true` to use Oracle Wallet for database credentials, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters can be provided:  - `-dbCredentialsWalletLocation`: Directory location for the Oracle Wallet files. - `-dbCredentialsWalletPassword`: Password for the Oracle Wallet account.  Note:  If you are using Oracle Unified Directory (OUD), then the OUD passwords should be stored in the wallet using the following keys:  - `oracle.dbsecurity.walletPassword` - `oracle.dbsecurity.userDNPassword` |

**Parent topic:** DBCA Silent Mode Commands

##### 2.14.4.9 deleteDatabase

The `deleteDatabase` command deletes a database.

Syntax and Parameters

Use the `dbca` `-deleteDatabase` command with the following syntax:

```
dbca -deleteDatabase 
   -sourceDB database_name_or_sid
   [-sysDBAUserName SYSDBA_user_name]
   [-sysDBAPassword SYSDBA_user_password]
   [-forceArchiveLogDeletion]
   [-deRegisterEMCloudControl
     [-omsHost Oracle_Management_Server_host_name
      -omsPort Oracle_Management_Server_port_number
      -emUser EM_administrator_user_name
      -emPassword EM_administrator_password]]
   [-unregisterWithDirService {true | false}
      -dirServiceUserName directory_service_user_name
      [-dirServicePassword directory_service_user_password
      [-walletPassword wallet_password]]
   [-sid database_system_identifier]
   [-useWalletForDBCredentials {true | false}
       -dbCredentialsWalletPassword wallet_account_password
       -dbCredentialsWalletLocation wallet_files_directory]
```

Table 2-13 deleteDatabase Parameters

| Parameter | Required/Optional | Description |
| --- | --- | --- |
| `-sourceDB` `database_name_or_sid` | Required | Database unique name for an Oracle RAC database or database system identifier (SID) for a single instance database. |
| `-sysDBAUserName` `SYSDBA_user_name` | Optional | User name of the user having the `SYSDBA` privileges. |
| `-sysDBAPassword` `SYSDBA_password` | Optional | Password of the user having the `SYSDBA` privileges. |
| `-forceArchiveLogDeletion` | Optional | Specify this parameter to delete the database archive logs. |
| `-deRegisterEMCloudControl` | Optional | Specify this parameter along with the following parameters to unregister the database with Enterprise Manager Cloud Control:  - `-omsHost`: Oracle Management Server host name. - `-omsPort`: Oracle Management Server port number. - `-emUser`: User name for Enterprise Manager administrator. - `-emPassword`: Password for Enterprise Manager administrator. |
| `-unregisterWithDirService {true \| false}` | Optional | Specify this parameter along with the following parameters to unregister the database with the directory service:  - `-dirServiceUserName`: User name for the directory service. - `-dirServicePassword`: Password for the directory service user. - `-walletPassword`: Password for the database wallet. |
| `-sid` `database_system_identifier` | Optional | Database system identifier (SID). |
| `-useWalletForDBCredentials`  `{true \| false}` | Optional | Specify `true` to use Oracle Wallet for database credentials, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters can be provided:  - `-dbCredentialsWalletLocation`: Directory location for the Oracle Wallet files. - `-dbCredentialsWalletPassword`: Password for the Oracle Wallet account.  Note:  If you are using Oracle Unified Directory (OUD), then the OUD passwords should be stored in the wallet using the following keys:  - `oracle.dbsecurity.walletPassword` - `oracle.dbsecurity.userDNPassword` |

**Parent topic:** DBCA Silent Mode Commands

##### 2.14.4.10 createPluggableDatabase

The `createPluggableDatabase` command creates a pluggable database (PDB) in a multitenant container database (CDB).

Syntax and Parameters

Use the `dbca` `-createPluggableDatabase` command with the following syntax:

```
dbca -createPluggableDatabase 
   -sourceDB cdb_sid
   -pdbName name_of_the_pdb_to_create
   [-createAsClone {true | false}]
   [-createPDBFrom {DEFAULT | FILEARCHIVE | RMANBACKUP | USINGXML | PDB}
      [-pdbArchiveFile pdb_archive_file_name_with_directory_path]
      [-PDBBackUpfile pdb_backup_file_name_with_directory_path]
      [-PDBMetadataFile pdb_metadata_file_name_with_directory_path]
      [-pdbAdminUserName pdb_administrator_name]
      [-pdbAdminPassword pdb_administrator_password]
      [-createNewPDBAdminUser {true | false}]
      [-sourceFileNameConvert method_to_locate_pdb_files]
      [-fileNameConvert names_of_pdb_files]
      [-pdbStorageMAXSizeInMB maximum_storage_size_for_the_pdb_in_MB]
      [-pdbStorageMAXTempSizeInMB maximum_temporary_storage_size_for_the_pdb_in_MB]
      [-workArea directory_to_unzip_PDB_archive_files_for_FILEARCHIVE_option]
      [-copyPDBFiles  {true | false}]
      [-sourcePDB name_of_the_pdb_to_clone]
   [-createFromRemotePDB
      -pdbName name_of_the_local_pdb_to_create
      -sourceDB database_name_of_the_local_pdb
      -remotePDBName name_of_the_remote_pdb
      -remoteDBConnString db_connection_string_of_the_remote_pdb
      -sysDBAUserName name_of_the_sysdba_user
      -sysDBAPassword password_of_the_sysdba_user
      -dbLinkUsername name_of_the_dblink_user_of_the_remote_pdb
      -dbLinkUserPassword password_of_the_dblink_user_of_the_remote_pdb]
   [-pdbDatafileDestination pdb_data_files_directory]
   [-useMetaDataFileLocation {true | false}]
   [-registerWithDirService {true | false} 
      -dirServiceUserName directory_service_user_name
      [-dirServicePassword directory_service_user_password]
      [-databaseCN directory_service_database_common_name]
      [-dirServiceCertificatePath certificate_file_directory_path]
      [-dirServiceUser active_directory_account_user_name]
      [-walletPassword wallet_password]]
   [-lbacsysPassword LBACSYS_user_password]
   [-createUserTableSpace {true | false)]
   [-pdbStorageMAXSizeInMB maximum_storage_size_for_the_pdb_in_MB]
   [-pdbStorageMAXTempSizeInMB maximum_temporary_storage_size_for_the_pdb_in_MB]
   [-customScripts custom_sql_scripts_to_run_after_PDB_creation]
   [-pdbUseMultipleBackup number_of_pdb_backups_to_create]
   [-dvConfiguration {true | false}
      -dvUserName Database_Vault_owner_name
      -dvUserPassword Database_Vault_owner_password
      [-dvAccountManagerName Database_Vault_account_manager_name]
      [-dvAccountManagerPassword Database_Vault_account_manager_password]]
   [-useWalletForDBCredentials {true | false}
      -dbCredentialsWalletPassword wallet_account_password
      -dbCredentialsWalletLocation wallet_files_directory]
```

Table 2-14 createPluggableDatabase Parameters

| Parameter | Required/Optional | Description |
| --- | --- | --- |
| `-sourceDB`  `cdb_sid` | Required | The database system identifier (SID) of the CDB. |
| `-pdbName`  `name_of_the_pdb_to_create` | Required | Name of the new PDB to create.  Note: For Oracle RAC databases, the PDB name must be unique in the cluster. |
| `-createAsClone`  `{true \| false}` | Optional | Specify `true` if the files you plan to use to create the new PDB are the same files that were used to create an existing PDB. Specifying `true` ensures that Oracle Database generates unique PDB DBID, GUID, and other identifiers expected for the new PDB.  Specify `false`, the default, if the files you plan to use to create the new PDB are not the same files that were used to create an existing PDB. |
| `-createPDBFrom`  `{DEFAULT \| FILEARCHIVE \| RMANBACKUP \| USINGXML \| PDB}` | Optional | Specify `DEFAULT` to create the PDB from the CDB's seed. When you specify `DEFAULT`, the following additional parameters are required:  - `-pdbAdminUserName`: The user name of the PDB's local administrator. - `-pdbAdminPassword`: The password for the PDB's local administrator.  Specify `FILEARCHIVE` to create the PDB from an unplugged PDB's files. When you specify `FILEARCHIVE`, the following additional parameters are required:  - `-pdbArchiveFile`: Complete path and name for unplugged PDB's archive file. 	The archive file contains all of the files for the PDB, including its XML metadata file and its data files. Typically, the archive file has a `.gz` extension. - `-createNewPDBAdminUser`: Specify `true` to create a new PDB administrator or `false` to avoid creating a new PDB administrator. - `-workArea`: Specify the directory location where the PDB archive files need to be unzipped.  Specify `RMANBACKUP` to create the PDB from a Recovery Manager (RMAN) backup. When you specify `RMANBACKUP`, the following additional parameters are required:  - `-pdbBackUpfile`: Complete path and name for the PDB backup file. - `-pdbMetadataFile`: Complete path and name for the PDB's XML metadata file.  Specify `USINGXML` to create the PDB from an unplugged PDB's XML metadata file. When you specify `USINGXML`, the following additional parameter is required:  - `-pdbMetadataFile`: Complete path and name for the PDB's XML metadata file.  Specify `PDB` to create a new PDB by cloning an existing PDB. When you specify `PDB`, the following additional parameter is required:  - `-sourcePDB`: Name of an existing PDB to clone.  Specify the following optional parameters, if required:  - `-sourceFileNameConvert`: This parameter specifies how to locate PDB files listed in the PDB XML metadata file. 	See `SOURCE_FILE_NAME_CONVERT` clause of the `CREATE PLUGGABLE DATABASE` statement described in [Oracle Multitenant Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=MULTI-GUID-CD341EDB-8B27-484B-9C55-CF206E2983DD). - `-fileNameConvert`: This parameter specifies the names of the PDB’s files. 	See `FILE_NAME_CONVERT` clause of the `CREATE PLUGGABLE DATABASE` statement described in [Oracle Multitenant Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=MULTI-GUID-39D2F826-7460-4439-B410-29E16C0CA0B1). - `-pdbStorageMAXSizeInMB`: Specify the maximum storage size for the PDB in megabytes. 	See information about PDB storage described in [Oracle Multitenant Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=MULTI-GUID-59F42929-7237-4371-8934-921B46DB6F31). - `-pdbStorageMAXTempSizeInMB`: Specify the maximum temporary storage size for the PDB in megabytes. - `-copyPDBFiles {true \| false}`: Specify `true` if the PDB data files need to be copied, else specify `false`. |
| `-createFromRemotePDB` | Optional | Create a PDB by cloning a remote PDB.  Specify the following parameters:  - `-pdbName`: Name of the local PDB to create. - `-sourceDB`: Database name of the local PDB. - `-remotePDBName`: Name of the remote PDB to clone. - `-remoteDBConnString`: Database connection string of the remote PDB. - `-sysDBAUserName`: Name of the SYSDBA user. - `-sysDBAPassword`: Password of the SYSDBA user. - `-dbLinkUsername`: Name of the database link user of the remote PDB. - `-dbLinkUserPassword`: Password of the database link user of the remote PDB.  Note:  - The database user of the local CDB must have the `CREATE PLUGGABLE DATABASE` privileges in the root container. - The remote CDB must be in the local undo mode. - The remote PDB must be in the archivelog mode. - The database user of the remote PDB to which the database link connects to must have the `CREATE PLUGGABLE DATABASE` and `CREATE SESSION` privileges. |
| `-pdbDatafileDestination`  `pdb_data_files_directory` | Optional | Compete directory path to the new PDB data files.  When this parameter is not specified, either Oracle Managed Files or the `PDB_FILE_NAME_CONVERT` initialization parameter specifies how to generate the names and locations of the files. If you use both Oracle Managed Files and the `PDB_FILE_NAME_CONVERT` initialization parameter, then Oracle Managed Files takes precedence.  When this parameter is not specified, Oracle Managed Files is not enabled, and the `PDB_FILE_NAME_CONVERT` initialization parameter is not set, by default a path to a subdirectory with the name of the PDB in the directory for the root's files is used. |
| `-useMetaDataFileLocation`  `{true \| false}` | Optional | Specify `true` to use the data file path defined in XML metadata file within a PDB archive when extracting data files.  Specify `false`, the default, to not use the data file path defined in XML metadata file within a PDB archive when extracting data files. |
| `-registerWithDirService`  `{true \| false}` | Optional | Specify `true` to register the PDB with a Lightweight Directory Access Protocol (LDAP) service, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters are required:  - `-dirServiceUserName`: User name for the LDAP service. - `-dirServicePassword`: Password for the LDAP service. - `-dirServiceUser`: User name for the Active Directory account. - `-dirServiceCertificatePath`: Certificate file path of the directory service. - `-databaseCN`: Common name of the directory service database. - `-walletPassword`: Password for the database wallet. |
| `-lbacsysPassword`  `LBACSYS_user_password` | Optional | Specify the `LBACSYS` user password if you want to configure OLS with a directory service. |
| `-createUserTableSpace`  `{true \| false}` | Optional | Specify `true` if a default user tablespace needs to be created in the new PDB. |
| `-pdbStorageMAXSizeInMB`  `maximum_storage_size_for_the_pdb_in_MB` | Optional | Specify the maximum storage size for the PDB in megabytes. |
| `-pdbStorageMAXTempSizeInMB`  `maximum_temporary_storage_size_for_the_pdb_in_MB` | Optional | Specify the maximum temporary storage size for the PDB in megabytes. |
| `-pdbUseMultipleBackup`  `number_of_pdb_backups_to_create` | Optional | Specify the number of PDB backups to create. |
| `-customScripts`  `lcustom_sql_scripts_to_run_after_PDB_creation` | Optional | Specify a list of custom SQL scripts to run after the PDB creation. |
| `-dvConfiguration`  `{true \| false}` | Optional | Specify `true` to enable and configure Database Vault, else specify `false`. Default is `false`.  When `true` is specified, the following additional Database Vault parameters are required:  - `-dvUserName`: Specify the Database Vault owner name. - `-dvUserPassword`: Specify Database Vault owner password. - `-dvAccountManagerName`: Specify a separate Database Vault account manager name. - `-dvAccountManagerPassword`: Specify the Database Vault account manager password. |
| `-useWalletForDBCredentials`  `{true \| false}` | Optional | Specify `true` to use Oracle Wallet for database credentials, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters can be provided:  - `-dbCredentialsWalletLocation`: Directory location for the Oracle Wallet files. - `-dbCredentialsWalletPassword`: Password for the Oracle Wallet account.  Note:  If you are using Oracle Unified Directory (OUD), then the OUD passwords should be stored in the wallet using the following keys:  - `oracle.dbsecurity.walletPassword` - `oracle.dbsecurity.userDNPassword` |

**Parent topic:** DBCA Silent Mode Commands

##### 2.14.4.11 unplugDatabase

The `unplugDatabase` command unplugs a pluggable database (PDB) from a multitenant container database (CDB).

Syntax and Parameters

Use the `dbca` `-unplugDatabase` command with the following syntax:

```
dbca -unplugDatabase 
   -sourceDB cdb_sid
   -pdbName pdb_name
   [-unregisterWithDirService {true | false}
      -dirServiceUserName directory_service_user_name
      -dirServicePassword directory_service_user_password
      -walletPassword wallet_password]
   [-archiveType {TAR | RMAN | NONE}
      [-rmanParallelism parallelism_integer_value]
      [-pdbArchiveFile pdb_archive_file_directory]
      [-PDBBackUpfile pdb_backup_file_directory]
      [-PDBMetadataFile pdb_metadata_file_directory]
      [-rmanParallelism parallelism_integer_value]]
   [-useWalletForDBCredentials {true | false}
      -dbCredentialsWalletPassword wallet_account_password
      -dbCredentialsWalletLocation wallet_files_directory]
```

Table 2-15 unplugDatabase Parameters

| Parameter | Required/Optional | Description |
| --- | --- | --- |
| `-sourceDB` `cdb_sid` | Required | The database system identifier (SID) of the CDB. |
| `-pdbName` `pdb_name` | Required | Name of the PDB. |
| `-archiveType` `{TAR \| RMAN \| NONE}` | Optional | Specify `TAR` to store the unplugged PDB files in a tar file.  Specify `RMAN` to store the unplugged PDB files in an RMAN backup.  Specify `NONE` to store the unplugged PDB files without using a tar file or an RMAN backup.  Specify any of the following parameters:  - `-pdbArchiveFile`: Specify absolute file path and name for the PDB Archive file. - `-pdbBackUpfile`: Specify absolute file path and name for the PDB backup file when archive type is `RMAN`. specify comma separated file paths, if there are multiple backups to be taken when creating the PDB. - `-pdbMetadataFile`: Specify absolute file path and name for the PDB metadata file when archive type is `RMAN` or `NONE`. - `-rmanParallelism`: Specify the RMAN parallelism integer value. |
| `-unregisterWithDirService` `{true \| false}` | Optional | Specify `true` to unregister the PDB from the LDAP service, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters are required:  - `-dirServiceUserName`: User name for the LDAP service. - `-dirServicePassword`: Password for the LDAP service user. - `-walletPassword`: Password for the database wallet. |
| `-useWalletForDBCredentials`  `{true \| false}` | Optional | Specify `true` to use Oracle Wallet for database credentials, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters can be provided:  - `-dbCredentialsWalletPassword`: Password for the Oracle Wallet account. - `-dbCredentialsWalletLocation`: Directory location for the Oracle Wallet files.  Note:  If you are using Oracle Unified Directory (OUD), then the OUD passwords should be stored in the wallet using the following keys:  - `oracle.dbsecurity.walletPassword` - `oracle.dbsecurity.userDNPassword` |

**Parent topic:** DBCA Silent Mode Commands

##### 2.14.4.12 deletePluggableDatabase

The `deletePluggableDatabase` command deletes a PDB.

Syntax and Parameters

Use the `dbca` `-deletePluggableDatabase` command with the following syntax:

```
dbca -deletePluggableDatabase 
   -sourceDB cdb_sid
   -pdbName pdb_name
   [-useWalletForDBCredentials {true | false}
       -dbCredentialsWalletPassword wallet_account_password
       -dbCredentialsWalletLocation wallet_files_directory]
```

Table 2-16 deletePluggableDatabase Parameters

| Parameter | Required/Optional | Description |
| --- | --- | --- |
| `-sourceDB` `cdb_sid` | Required | The database system identifier (SID) of the CDB. |
| `-pdbName` `pdb_name` | Required | Name of the PDB to delete. |
| `-useWalletForDBCredentials`  `{true \| false}` | Optional | Specify `true` to use Oracle Wallet for database credentials, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters can be provided:  - `-dbCredentialsWalletPassword`: Password for the Oracle Wallet account. - `-dbCredentialsWalletLocation`: Directory location for the Oracle Wallet files.  Note:  If you are using Oracle Unified Directory (OUD), then the OUD passwords should be stored in the wallet using the following keys:  - `oracle.dbsecurity.walletPassword` - `oracle.dbsecurity.userDNPassword` |

**Parent topic:** DBCA Silent Mode Commands

##### 2.14.4.13 relocatePDB

The `relocatePDB` command relocates a PDB from a remote CDB to a local CDB.

Prerequisites

The following are the prerequisites for running the `relocatePDB` command:

- The database user in the local PDB must have the `CREATE PLUGGABLE DATABASE` privilege in the local CDB root container.
- The remote CDB must be in the local undo mode.
- The remote and local PDBs must be in the archivelog mode.
- The database user in the remote PDB that the database link connects to must have the `CREATE PLUGGABLE DATABASE`, `SESSION`, and `SYSOPER` privileges.
- The local and remote PDBs must have the same options installed, or the remote PDB must have a subset of the options installed on the local PDB.

Syntax and Parameters

Use the `dbca` `-relocatePDB` command with the following syntax:

```
dbca -relocatePDB 
   -pdbName name_of_the_local_pdb_to_create
   -sourceDB database_name_of_the_local_pdb
   -remotePDBName name_of_the_remote_pdb_to_relocate
   -remoteDBConnString db_connection_string_of_the_remote_pdb
   -sysDBAUserName name_of_the_sysdba_user
   -sysDBAPassword password_of_the_sysdba_user
   -dbLinkUsername name_of_the_dblink_user_of_the_remote_pdb
   -dbLinkUserPassword password_of_the_dblink_user_of_the_remote_pdb
```

Table 2-17 relocatePDB Parameters

| Parameter | Required/Optional | Description |
| --- | --- | --- |
| `-pdbName` `name_of_the_local_pdb_to_create` | Required | Name of the local PDB to create after relocating the remote PDB. |
| `-sourceDB` `database_name_of_the_local_pdb` | Required | Database name of the local PDB. |
| `-remotePDBName` `name_of_the_remote_pdb_to_relocate` | Required | Name of the remote PDB to relocate. |
| `-remoteDBConnString` `db_connection_string_of_the_remote_pdb` | Required | Database connection string of the remote PDB. |
| `-sysDBAUserName` `name_of_the_sysdba_user` | Required | Name of the SYSDBA user. |
| `-sysDBAPassword` `password_of_the_sysdba_user` | Required | Password of the SYSDBA user. |
| `-dbLinkUsername` `name_of_the_dblink_user_of_the_remote_pdb` | Required | Name of the database link user of the remote PDB. |
| `-dbLinkUserPassword` `password_of_the_dblink_user_of_the_remote_pdb` | Required | Password of the database link user of the remote PDB. |

**Parent topic:** DBCA Silent Mode Commands

##### 2.14.4.14 configurePluggableDatabase

The `configurePluggableDatabase` command configures a pluggable database (PDB).

Syntax and Parameters

Use the `dbca` `-configurePluggableDatabase` command with the following syntax:

```
dbca -configurePluggableDatabase 
   -sourceDB cdb_sid
   -pdbName pdb_name
   [-dvConfiguration {true | false}
      -dvUserName Database_Vault_owner_name
      -dvUserPassword Database_Vault_owner_password
      [-dvAccountManagerName Database_Vault_account_manager_name]
      [-dvAccountManagerPassword Database_Vault_account_manager_password]]
   [-olsConfiguration {true | false}
      [-configureWithOID configure_with_OID_flag]]
   [-configureOracleR
      [-oracleRConfigTablespace tablespace_for_Oracle_R_configuration]]
   [-registerWithDirService {true | false}
      -dirServiceUserName directory_service_user_name
      [-dirServicePassword directory_service_user_password]
      [-walletPassword wallet_password]
      [-databaseCN database_common_name]
      [-dirServiceCertificatePath certificate_file_path]
      [-dirServiceUser active_directory_account_user_name]]
   [-unregisterWithDirService {true | false}
      -dirServiceUserName directory_service_user_name
      [-dirServicePassword directory_service_user_password]
      [-walletPassword wallet_password]]
   [-lbacsysPassword LBACSYS_user_password]]
   [-useWalletForDBCredentials {true | false}
      -dbCredentialsWalletPassword wallet_account_password
      -dbCredentialsWalletLocation wallet_files_directory]
```

Table 2-18 configurePluggableDatabase Parameters

| Parameter | Required/Optional | Description |
| --- | --- | --- |
| `-sourceDB` `cdb_sid` | Required | The database system identifier (SID) of the CDB. |
| `-pdbName` `pdb_name` | Required | Name of the PDB. |
| `-dvConfiguration` `{true \| false}` | Optional | Specify `true` to enable and configure Database Vault for the PDB, else specify `false`. Default is `false`.  When `true` is specified, the following additional Database Vault parameters are required:  - `-dvUserName`: Specify the Database Vault owner user name. - `-dvUserPassword`: Specify Database Vault owner password. - `-dvAccountManagerName`: Specify a separate Database Vault account manager. - `-dvAccountManagerPassword`: Specify the Database Vault account manager password. |
| `-olsConfiguration` `{true \| false}` | Optional | Specify `true` to enable and configure Oracle Label Security (OLS) for the PDB, else specify `false`. Default is `false`.  When `true` is specified, you can additionally specify the `-configureWithOID` parameter to configure Oracle Label Security (OLS) with Oracle Internet Directory (OID). This parameter is optional. |
| `-lbacsysPassword` | Optional | Specify the `LBACSYS` user password, if you want to configure OLS with a directory service. |
| `-configureOracleR` | Optional | Specify this parameter to configure Oracle R for the PDB.  Additionally, you can specify the `-oracleRConfigTablespace` parameter to assign a tablespace for the Oracle R configuration, for example, `SYSAUX` tablespace. |
| `-registerWithDirService` `{true \| false}` | Optional | Specify `true` to register the PDB with a Lightweight Directory Access Protocol (LDAP) service, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters can be provided:  - `-dirServiceUserName`: User name for the LDAP service. - `-dirServicePassword`: Password for the LDAP service user. - `-walletPassword`: Password for the database wallet. - `-databaseCN`: Database common name. - `-dirServiceCertificatePath`: Directory service certificate file path. - `-dirServiceUser`: Active Directory account user name. |
| `unregisterWithDirService` `{true \| false}` | Optional | Specify `true` to unregister the PDB with the Lightweight Directory Access Protocol (LDAP) service, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters can be provided:  - `-dirServiceUserName`: User name for the LDAP service. - `-dirServicePassword`: Password for the LDAP service user. - `-walletPassword`: Password for the database wallet. |
| `-useWalletForDBCredentials`  `{true \| false}` | Optional | Specify `true` to use Oracle Wallet for database credentials, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters can be provided:  - `-dbCredentialsWalletPassword`: Password for the Oracle Wallet account. - `-dbCredentialsWalletLocation`: Directory location for the Oracle Wallet files.  Note:  If you are using Oracle Unified Directory (OUD), then the OUD passwords should be stored in the wallet using the following keys:  - `oracle.dbsecurity.walletPassword` - `oracle.dbsecurity.userDNPassword` |

**Parent topic:** DBCA Silent Mode Commands

##### 2.14.4.15 addInstance

The `addInstance` command adds a database instance to an administrator-managed Oracle RAC database.

Syntax and Parameters

Use the `dbca` `-addInstance` command with the following syntax:

```
dbca -addInstance 
   -gdbName global_database_name
   -nodeName database_instance_node_name
   [-updateDirService {true | false}
      -dirServiceUserName directory_service_user_name
      -dirServicePassword directory_service_user_password]
   [-instanceName database_instance_name]
   [-sysDBAUserName SYSDBA_user_name]
   [-sysDBAPassword SYSDBA_user_password]
   [-useWalletForDBCredentials {true | false}
      -dbCredentialsWalletPassword wallet_account_password
      -dbCredentialsWalletLocation wallet_files_directory]
```

Table 2-19 addInstance Parameters

| Parameter | Required/Optional | Description |
| --- | --- | --- |
| `-gdbName` `global_database_name` | Required | Global database name in the form database\_name.domain\_name. |
| `-nodeName` `database_instance_node_name` | Required | Node name of the database instance. |
| `-instanceName` `database_instance_name` | Optional | Database instance name. |
| `-sysDBAUserName` `SYSDBA_user_name` | Optional | User name of the database user having the `SYSDBA` privileges. |
| `-sysDBAPassword` `SYSDBA_user_password` | Optional | Password of the database user having the `SYSDBA` privileges. |
| `-updateDirService`  `{true \| false}` | Optional | Specify `true` to register the database with a directory service, else specify `false`.  When `true` is specified, the following additional parameters are required:  - `-dirServiceUserName`: User name for the directory service. - `—dirServicePassword`: Password for the directory service user. |
| `-useWalletForDBCredentials`  `{true \| false}` | Optional | Specify `true` to use Oracle Wallet for database credentials, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters can be provided:  - `-dbCredentialsWalletPassword`: Password for the Oracle Wallet account. - `-dbCredentialsWalletLocation`: Directory location for the Oracle Wallet files.  Note:  If you are using Oracle Unified Directory (OUD), then the OUD passwords should be stored in the wallet using the following keys:  - `oracle.dbsecurity.walletPassword` - `oracle.dbsecurity.userDNPassword` |

**Parent topic:** DBCA Silent Mode Commands

##### 2.14.4.16 deleteInstance

The `deleteInstance` command deletes a database instance from an administror-managed Oracle RAC database.

Syntax and Parameters

Use the `dbca` `-deleteInstance` command with the following syntax:

```
dbca -deleteInstance 
   -gdbName global_database_name
   -instanceName database_instance_name
   [-nodeName database_instance_node_name]
   [-updateDirService {true | false}
      -dirServiceUserName directory_service_user_name
      -dirServicePassword directory_service_user_password]
   [-sysDBAUserName SYSDBA_user_name]
   [-sysDBAPassword SYSDBA_user_password]
   [-useWalletForDBCredentials {true | false}
      -dbCredentialsWalletPassword wallet_account_password
      -dbCredentialsWalletLocation wallet_files_directory]
```

Table 2-20 deleteInstance Parameters

| Parameter | Required/Optional | Description |
| --- | --- | --- |
| `-gdbName` `global_database_name` | Required | Global database name in the form database\_name.domain\_name. |
| `-instanceName` `database_instance_name` | Required | Database instance name. |
| `-nodeName` `node_name_of_database_instance` | Optional | Node name of the database instance. |
| `-sysDBAUserName` `SYSDBA_user_name` | Optional | User name of the database user having the `SYSDBA` privileges. |
| `-sysDBAPassword` `SYSDBA_user_password` | Optional | Password of the database user having the `SYSDBA` privileges. |
| `-updateDirService`  `{true \| false}` | Optional | Specify `true` to unregister the database with the directory service, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters are required:  - `-dirServiceUserName`: User name for the directory service. - `—dirServicePassword`: Password for the directory service user. |
| `-useWalletForDBCredentials`  `{true \| false}` | Optional | Specify `true` to use Oracle Wallet for database credentials, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters can be provided:  - `-dbCredentialsWalletPassword`: Password for the Oracle Wallet account. - `-dbCredentialsWalletLocation`: Directory location for the Oracle Wallet files.  Note:  If you are using Oracle Unified Directory (OUD), then the OUD passwords should be stored in the wallet using the following keys:  - `oracle.dbsecurity.walletPassword` - `oracle.dbsecurity.userDNPassword` |

**Parent topic:** DBCA Silent Mode Commands

##### 2.14.4.17 executePrereqs

The `executePrereqs` command executes the prerequisites checks and reports the results. This command can be used to check the environment before running dbca to create a database.

Syntax and Parameters

Use the `dbca` `-executePrereqs` command with the following syntax:

```
dbca -executePrereqs 
   -databaseConfigType {SINGLE | RAC | RACONENODE}
        [-RACOneNodeServiceName RAC_node_service_name]
   [-nodelist database_nodes_list]
```

Table 2-21 executePrereqs Parameters

| Parameter | Required/Optional | Description |
| --- | --- | --- |
| `-databaseConfigType {SINGLE \| RAC \| RACONENODE}` | Required | Specify one of the following database configuration types:  - `SINGLE`: Single individual database. - `RAC`: Oracle RAC database. - `RACONENODE`: Oracle RAC One Node database. 	For Oracle RAC One Node database, you can specify the service name using the `-RACOneNodeServiceName` parameter. |
| `-nodelist`  `database_nodes_list` | Optional | List of database nodes separated by comma. |

**Parent topic:** DBCA Silent Mode Commands

#### 2.14.5 DBCA Exit Codes

The outcome of running DBCA commands in silent mode is reported as an exit code.

The following table shows the exit codes that DBCA returns to the operating system.

Table 2-22 Exit Codes for Database Configuration Assistant

| Exit Code | Description |
| --- | --- |
| 0 | Command execution successful |
| 6 | Command execution successful but with warnings |
| \-1 | Command execution failed |
| \-2 | Invalid input from user |
| \-4 | Command canceled by user |

**Parent topic:** Database Configuration Assistant Command Reference for Silent Mode

[^1]: Create a backup of your production database. You have the following backup options:

- An online backup
	If you perform an online backup, then ensure that your production database is in `ARCHIVELOG` mode and that all of the necessary archived redo log files are saved and accessible to the CloneDB database environment.
- A full offline backup
	If you perform a full offline backup, then ensure that the backup files are accessible to the CloneDB database environment.
- A backup that copies the database files
	If you specify `BACKUP` `AS` `COPY` in RMAN, then RMAN copies each file as an image copy, which is a bit-for-bit copy of a database file created on disk. Image copies are identical to copies created with operating system commands such as `cp` on Linux or `COPY` on Windows, but are recorded in the RMAN repository and so are usable by RMAN. You can use RMAN to make image copies while the database is open. Ensure that the copied database files are accessible to the CloneDB database environment.

See [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=BRADV002) for information about backing up a database.

[^undefined]: Create a text initialization parameter file (PFILE) if one does not exist.

If you are using a server parameter file (SPFILE), then run the following statement on the production database to create a PFILE:

```
CREATE PFILE FROM SPFILE;
```

[^2]: Create SQL scripts for cloning the production database.

You will use one or more SQL scripts to create a CloneDB database in a later step. To create the SQL scripts, you can either use an Oracle-supplied Perl script called clonedb.pl, or you can create a SQL script manually.

To use the clonedb.pl Perl script, complete the following steps:

1. Set the following environment variables at an operating system prompt:
	`MASTER_COPY_DIR` - Specify the directory that contains the backup created in Step 1. Ensure that this directory contains only the backup of the data files of the production database.
	`CLONE_FILE_CREATE_DEST` - Specify the directory where CloneDB database files will be created, including data files, log files, control files.
	`CLONEDB_NAME` - Specify the name of the CloneDB database.
	`S7000_TARGET` - If the NFS host providing the file system for the backup and the CloneDB database is a Sun Storage 7000, then specify the name of the host. Otherwise, do not set this environment variable. Set this environment variable only if cloning must be done using storage snapshots. You can use S7000 storage arrays for Direct NFS Client without setting this variable.
2. Run the clonedb.pl Perl script.
	The script is in the $ORACLE\_HOME/rdbms/install directory and has the following syntax:
	```
	$ORACLE_HOME/perl/bin/perl $ORACLE_HOME/rdbms/install/clonedb.pl 
	prod_db_pfile [sql_script1] [sql_script2]
	```
	Specify the following options:
	`prod_db_pfile` - Specify the full path of the production database's PFILE.
	`sql_script1` - Specify a name for the first SQL script generated by clonedb.pl. The default is crtdb.sql.
	`sql_script2` - Specify a name for the second SQL script generated by clonedb.pl. The default is dbren.sql.
	The clonedb.pl script copies the production database's PFILE to the CloneDB database's directory. It also creates two SQL scripts that you will use to create the CloneDB database.
3. Check the two SQL scripts that were generated by the clonedb.pl Perl script, and make changes if necessary.
4. Modify the initialization parameters for the CloneDB database environment, and save the file.
	Change any initialization parameter that is specific to the CloneDB database environment, such as parameters that control SGA size, PGA target, the number of CPUs, and so on. The `CLONEDB` parameter must be set to `TRUE`, and the initialization parameter file includes this parameter. See [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=REFRN10330) for information about initialization parameters.
5. In SQL\*Plus, connect to the CloneDB database with `SYSDBA` administrative privilege.
6. Run the SQL scripts generated by the clonedb.pl Perl script.
	For example, if the scripts use the default names, then run the following scripts at the SQL prompt:
	```
	crtdb.sql
	dbren.sql
	```

To create a SQL script manually, complete the following steps:

1. Connect to the database with `SYSDBA` or `SYSBACKUP` administrative privilege.
	See " [Connecting to the Database with SQL\*Plus](getting-started-with-database-administration.md) ".
2. Generate a backup control file script from your production database by completing the following steps:
	Run the following SQL statement:
	```
	ALTER DATABASE BACKUP CONTROLFILE TO TRACE;
	```
	This statement generates a trace file that contains the SQL statements that create the control file. The trace file containing the `CREATE` `CONTROLFILE` statement is stored in a directory determined by the `DIAGNOSTIC_DEST` initialization parameter. Check the database alert log for the name and location of this trace file.
3. Open the trace file generated in Step 3.b, and copy the `STARTUP` `NOMOUNT` and `CREATE` `CONTROLFILE` statements in the trace file to a new SQL script.
4. Edit the new SQL script you created in Step 3.c in the following ways:
	Change the name of the database to the name of the CloneDB database you are creating. For example, change `PROD1` to `CLONE1`.
	Change the locations of the log files to a directory in the CloneDB database environment. For example, change/u01/prod1/oracle/dbs/t\_log1.f to /u03/clone1/oracle/dbs/t\_log1.f.
	Change the locations of the data files to the backup location. For example, change /u01/prod1/oracle/dbs/t\_db1.f to /u02/oracle/backup/prod1/t\_db1.f.
	The following is an example of the original statements generated by the `ALTER` `DATABASE` `BACKUP` `CONTROLFILE` `TO` `TRACE` statement:
	```
	STARTUP NOMOUNT
	CREATE CONTROLFILE REUSE DATABASE "PROD1" NORESETLOGS  ARCHIVELOG
	    MAXLOGFILES 32
	    MAXLOGMEMBERS 2
	    MAXDATAFILES 32
	    MAXINSTANCES 1
	    MAXLOGHISTORY 292
	LOGFILE
	  GROUP 1 '/u01/prod1/oracle/dbs/t_log1.f'  SIZE 25M BLOCKSIZE 512,
	  GROUP 2 '/u01/prod1/oracle/dbs/t_log2.f'  SIZE 25M BLOCKSIZE 512
	-- STANDBY LOGFILE
	DATAFILE
	  '/u01/prod1/oracle/dbs/t_db1.f',
	  '/u01/prod1/oracle/dbs/t_ax1.f',
	  '/u01/prod1/oracle/dbs/t_undo1.f',
	  '/u01/prod1/oracle/dbs/t_xdb1.f',
	  '/u01/prod1/oracle/dbs/undots.dbf'
	CHARACTER SET WE8ISO8859P1
	;
	```
	The following is an example of the modified statements in the new SQL script:
	```
	STARTUP NOMOUNT PFILE=/u03/clone1/oracle/dbs/clone1.ora
	CREATE CONTROLFILE REUSE DATABASE "CLONE1" RESETLOGS  ARCHIVELOG
	    MAXLOGFILES 32
	    MAXLOGMEMBERS 2
	    MAXDATAFILES 32
	    MAXINSTANCES 1
	    MAXLOGHISTORY 292
	LOGFILE
	  GROUP 1 '/u03/clone1/oracle/dbs/t_log1.f'  SIZE 25M BLOCKSIZE 512,
	  GROUP 2 '/u03/clone1/oracle/dbs/t_log2.f'  SIZE 25M BLOCKSIZE 512
	-- STANDBY LOGFILE
	DATAFILE
	  '/u02/oracle/backup/prod1/t_db1.f',
	  '/u02/oracle/backup/prod1/t_ax1.f',
	  '/u02/oracle/backup/prod1/t_undo1.f',
	  '/u02/oracle/backup/prod1/t_xdb1.f',
	  '/u02/oracle/backup/prod1/undots.dbf'
	CHARACTER SET WE8ISO8859P1
	;
	```
	If you have a storage level snapshot taken on a data file, then you can replace the RMAN backup file names with the storage snapshot names.
5. After you edit the SQL script, save it to a location that is accessible to the CloneDB database environment.
	Make a note of the name and location of the new SQL script. You will run the script in a subsequent step. In this example, assume the name of the script is create\_clonedb1.sql
6. Copy the text initialization parameter file (PFILE) from the production database environment to the CloneDB database environment.
	For example, copy the text initialization parameter file from /u01/prod1/oracle/dbs to /u03/clone1/oracle/dbs. The name and location of the file must match the name and location specified in the `STARTUP` `NOMOUNT` command in the modified SQL script. In the example in Step 3.d, the file is /u03/clone1/oracle/dbs/clone1.ora.
7. Modify the initialization parameters for the CloneDB database environment, and save the file.
	Add the `CLONEDB` parameter, and ensure that this parameter is set to `TRUE`. Change any other initialization parameter that is specific to the CloneDB database environment, such as parameters that control SGA size, PGA target, the number of CPUs, and so on. See [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=REFRN10330) for information about initialization parameters.
8. In SQL\*Plus, connect to the CloneDB database with `SYSDBA` administrative privilege.
9. Run the SQL script you saved in Step 3.e.
	For example, enter the following in SQL\*Plus:
	```
	@create_clonedb1.sql
	```
10. For each data file in the backup location, run the `CLONEDB_RENAMEFILE` procedure in the `DBMS_DNFS` package and specify the appropriate location in the CloneDB database environment.
	For example, run the following procedure if the backup data file is /u02/oracle/backup/prod1/t\_db1.f and the CloneDB database data file is /u03/clone1/oracle/dbs/t\_db1.f:
	```
	BEGIN
	  DBMS_DNFS.CLONEDB_RENAMEFILE(
	    srcfile  => '/u02/oracle/backup/prod1/t_db1.f',
	    destfile => '/u03/clone1/oracle/dbs/t_db1.f');
	END;
	/
	```
	See [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/admin&id=ARPLS74814) for more information about the `DBMS_DNFS` package.

[^undefined]: If you created your CloneDB database from an online backup, then recover the CloneDB database. This step is not required if you performed a full offline backup or a `BACKUP` `AS` `COPY` backup.

For example, run the following SQL statement on the CloneDB database:

```
RECOVER DATABASE USING BACKUP CONTROLFILE UNTIL CANCEL;
```

This statement prompts for the archived redo log files for the period when the backup was performed.

[^3]: Open the database by running the following SQL statement:

```
ALTER DATABASE OPEN RESETLOGS;
```

The CloneDB database is ready for use.