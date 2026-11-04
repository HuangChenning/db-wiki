---
title: Creating and Configuring an Oracle Database
book: "Administrator's Guide"
doc_id: E25494-07
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e25494/create.htm
tags:
  - oracle
  - 11g
  - administrators-guide
---

## 2 Creating and Configuring an Oracle Database

In this chapter:

## About Creating an Oracle Database

After you plan your database using some of the guidelines presented in this section, you can create the database with a graphical tool or a SQL command. You typically create a database during Oracle Database software installation. However, you can also create a database after installation. Reasons to create a database after installation are as follows:

- You used Oracle Universal Installer (OUI) to install software only, and did not create a database.
- You want to create another database (and database instance) on the same host computer as an existing Oracle database. In this case, this chapter assumes that the new database uses the same Oracle home as the existing database. You can also create the database in a new Oracle home by running OUI again.
- You want to make a copy of (clone) a database.

The specific methods for creating a database are:

- With Database Configuration Assistant (DBCA), a graphical tool.
	See "Creating a Database with DBCA"
- With the `CREATE` `DATABASE` SQL statement.
	See "Creating a Database with the CREATE DATABASE Statement"

### Considerations Before Creating the Database

Database creation prepares several operating system files to work together as an Oracle Database. You only need to create a database once, regardless of how many data files it has or how many instances access it. You can create a database to erase information in an existing database and create a new database with the same name and physical structure.

The following topics can help prepare you for database creation.

- Planning for Database Creation
- Meeting Creation Prerequisites

#### Planning for Database Creation

Prepare to create the database by research and careful planning. Table 2-1 lists some recommended actions:

Table 2-1 Database Planning Tasks

| Action | Additional Information |
| --- | --- |
| Plan the database tables and indexes and estimate the amount of space they will require. | [Part I, "Oracle Database Structure and Storage"](part2.md)  [Part I, "Schema Objects"](part4.md) |
| Plan the layout of the underlying operating system files your database will comprise. Proper distribution of files can improve database performance dramatically by distributing the I/O during file access. You can distribute I/O in several ways when you install Oracle software and create your database. For example, you can place redo log files on separate disks or use striping. You can situate data files to reduce contention. And you can control data density (number of rows to a data block). If you create a Fast Recovery Area, Oracle recommends that you place it on a storage device that is different from that of the data files.  To greatly simplify this planning task, consider using Oracle Managed Files and Automatic Storage Management to create and manage the operating system files that comprise your database storage. | [Chapter 17, "Using Oracle Managed Files"](omf.md)  [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/toc.htm)  [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/iodesign.htm#PFGRF015)  [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/toc.htm)  Your Oracle operating system–specific documentation, including the appropriate Oracle Database installation guide. |
| Select the global database name, which is the name and location of the database within the network structure. Create the global database name by setting both the `DB_NAME` and `DB_DOMAIN` initialization parameters. | "Determining the Global Database Name" |
| Familiarize yourself with the initialization parameters contained in the initialization parameter file. Become familiar with the concept and operation of a server parameter file. A server parameter file lets you store and manage your initialization parameters persistently in a server-side disk file. | "About Initialization Parameters and Initialization Parameter Files"  "What Is a Server Parameter File?"  [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams_part.htm#REFRN001) |
| Select the database character set.  All character data, including data in the data dictionary, is stored in the database character set. You specify the database character set when you create the database.  See "Selecting a Character Set" for details. | [Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/ch2charset.htm#NLSPG002) |
| Consider what time zones your database must support.  Oracle Database uses one of two time zone files as the source of valid time zones. The default time zone file is `timezlrg_11.dat`. It contains more time zones than the smaller time zone file, `timezone_11.dat`. | "Specifying the Database Time Zone File" |
| Select the standard database block size. This is specified at database creation by the `DB_BLOCK_SIZE` initialization parameter and cannot be changed after the database is created.  The `SYSTEM` tablespace and most other tablespaces use the standard block size. Additionally, you can specify up to four nonstandard block sizes when creating tablespaces. | "Specifying Database Block Sizes" |
| If you plan to store online redo log files on disks with a 4K byte sector size, determine whether you must manually specify redo log block size. | ["Planning the Block Size of Redo Log Files"](onlineredo.md) |
| Determine the appropriate initial sizing for the `SYSAUX` tablespace. | "About the SYSAUX Tablespace" |
| Plan to use a default tablespace for non- `SYSTEM` users to prevent inadvertently saving database objects in the `SYSTEM` tablespace. | "Creating a Default Permanent Tablespace" |
| Plan to use an undo tablespace to manage your undo data. | [Chapter 16, "Managing Undo"](undo.md) |
| Develop a backup and recovery strategy to protect the database from failure. It is important to protect the control file by multiplexing, to choose the appropriate backup mode, and to manage the online and archived redo logs. | [Chapter 12, "Managing the Redo Log"](onlineredo.md)  [Chapter 13, "Managing Archived Redo Logs"](archredo.md)  [Chapter 11, "Managing Control Files"](control.md)  [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/toc.htm) |
| Familiarize yourself with the principles and options of starting up and shutting down an instance and mounting and opening a database. | [Chapter 3, "Starting Up and Shutting Down"](start.md) |

##### Selecting a Character Set

Oracle recommends AL32UTF8 as the database character set. AL32UTF8 is Oracle's name for the UTF-8 encoding of the Unicode standard. The Unicode standard is the universal character set that supports most of the currently spoken languages of the world. The use of the Unicode standard is indispensable for any multilingual technology, including database processing.

After a database is created and accumulates production data, changing the database character set is a time consuming and complex project. Therefore, it is very important to select the right character set at installation time. Even if the database does not currently store multilingual data but is expected to store multilingual data within a few years, the choice of AL32UTF8 for the database character set is usually the only good decision.

Even so, the default character set used by Oracle Universal Installer (OUI) and Database Configuration Assistant (DBCA) for the UNIX, Linux, and Microsoft Windows platforms is not AL32UTF8, but a Microsoft Windows character set known as an ANSI code page. The particular character set is selected based on the current language (locale) of the operating system session that started OUI or DBCA. If the language is American English or one of the Western European languages, the default character set is WE8MSWIN1252. Each Microsoft Windows ANSI Code Page is capable of storing data only from one language or a limited group of languages, such as only Western European, or only Eastern European, or only Japanese.

A Microsoft Windows character set is the default even for databases created on UNIX and Linux platforms because Microsoft Windows is the prevalent platform for client workstations. Oracle Client libraries automatically perform the necessary character set conversion between the database character set and the character sets used by non-Windows client applications.

You may also choose to use any other character set from the presented list of character sets. You can use this option to select a particular character set required by an application vendor, or choose a particular character set that is the common character set used by all clients connecting to this database.

As AL32UTF8 is a multibyte character set, database operations on character data may be slightly slower when compared to single-byte database character sets, such as WE8MSWIN1252. Storage space requirements for text in most languages that use characters outside of the ASCII repertoire are higher in AL32UTF8 compared to legacy character sets supporting the language. The increase in storage space concerns only character data and only data that is not in English. The universality and flexibility of Unicode usually outweighs these additional costs.

Caution:

Do not use the character set named UTF8 as the database character set unless required for compatibility with Oracle Database clients and servers in version 8.1.7 and earlier, or unless explicitly requested by your application vendor. Despite having a very similar name, UTF8 is not a proper implementation of the Unicode encoding UTF-8. If the UTF8 character set is used where UTF-8 processing is expected, data loss and security issues may occur. This is especially true for Web related data, such as XML and URL addresses.

#### Meeting Creation Prerequisites

Before you can create a new database, the following prerequisites must be met:

- The desired Oracle software must be installed. This includes setting various environment variables unique to your operating system and establishing the directory structure for software and database files.
- Sufficient memory must be available to start the Oracle Database instance.
- Sufficient disk storage space must be available for the planned database on the computer that runs Oracle Database.

All of these are discussed in the [Oracle Database Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) specific to your operating system. If you use the Oracle Universal Installer, it will guide you through your installation and provide help in setting environment variables and establishing directory structure and authorizations.

## Creating a Database with DBCA

Database Configuration Assistant (DBCA) is the preferred way to create a database, because it is a more automated approach, and your database is ready to use when DBCA completes. DBCA can be launched by the Oracle Universal Installer (OUI), depending upon the type of install that you select. You can also launch DBCA as a standalone tool at any time after Oracle Database installation.

You can run DBCA in interactive mode or noninteractive/silent mode. Interactive mode provides a graphical interface and guided workflow for creating and configuring a database. Noninteractive/silent mode enables you to script database creation. You can run DBCA in noninteractive/silent mode by specifying command-line arguments, a response file, or both.

### Creating a Database with Interactive DBCA

See [Oracle Database 2 Day DBA](https://docs.oracle.com/cd/E11882_01/server.112/e10897/install.htm#ADMQS002) for detailed information about creating a database interactively with DBCA.

### Creating a Database with Noninteractive/Silent DBCA

See Appendix A of the installation guide for your platform for details on using the noninteractive/silent mode of DBCA.

The following example creates a database by passing command-line arguments to DBCA:

```
dbca -silent -createDatabase -templateName General_Purpose.dbc
  -gdbname ora11g -sid ora11g -responseFile NO_VALUE -characterSet AL32UTF8
  -memoryPercentage 30 -emConfiguration LOCAL

Enter SYSTEM user password:
password
Enter SYS user password:
password
Copying database files
1% complete
3% complete
...
```

To ensure completely silent operation, you can redirect stdout to a file. In this case, however, you must supply passwords for the administrative accounts in command-line arguments or the response file.

To view brief help for DBCA command-line arguments, enter the following command:

```
dbca -help
```

For more detailed argument information, including defaults, view the response file template found on your distribution media. Appendix A of your platform installation guide provides the name and location of this file.

## Creating a Database with the CREATE DATABASE Statement

Using the `CREATE` `DATABASE` SQL statement is a more manual approach to creating a database. One advantage of using this statement over using DBCA is that you can create databases from within scripts.

If you use the `CREATE DATABASE` statement, you must complete additional actions before you have an operational database. These actions include building views on the data dictionary tables and installing standard PL/SQL packages. You perform these actions by running the supplied scripts.

If you have existing scripts for creating your database, consider editing those scripts to take advantage of new Oracle Database features.

The instructions in this section apply to single-instance installations only. See the Oracle Real Application Clusters (Oracle RAC) installation guide for your platform for instructions for creating an Oracle RAC database.

Note:

Single-instance does not mean that only one Oracle instance can reside on a single host computer. In fact, multiple Oracle instances (and their associated databases) can run on a single host computer. A single-instance database is a database that is accessed by only one Oracle instance, as opposed to an Oracle RAC database, which is accessed concurrently by multiple Oracle instances on multiple nodes. See [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/toc.htm) for more information on Oracle RAC.

Complete the following steps to create a database with the `CREATE` `DATABASE` statement. The examples create a database named `mynewdb`.

Step 1: Specify an Instance Identifier (SID)

Step 2: Ensure That the Required Environment Variables Are Set

Step 3: Choose a Database Administrator Authentication Method

Step 4: Create the Initialization Parameter File

Step 5: (Windows Only) Create an Instance

Step 6: Connect to the Instance

Step 7: Create a Server Parameter File

Step 8: Start the Instance

Step 9: Issue the CREATE DATABASE Statement

Step 10: Create Additional Tablespaces

Step 11: Run Scripts to Build Data Dictionary Views

Step 12: (Optional) Run Scripts to Install Additional Options

Step 13: Back Up the Database.

Step 14: (Optional) Enable Automatic Instance Startup

Tip:

If you are using Oracle Automatic Storage Management (Oracle ASM) to manage your disk storage, you must start the Oracle ASM instance and configure your disk groups before performing these steps. For information about Automatic Storage Management, see [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/toc.htm).

### Step 1: Specify an Instance Identifier (SID)

Decide on a unique Oracle system identifier (SID) for your instance, open a command window, and set the `ORACLE_SID` environment variable. Use this command window for the subsequent steps.

`ORACLE_SID` is used to distinguish this instance from other Oracle Database instances that you may create later and run concurrently on the same host computer. Restrictions related to the valid characters in an `ORACLE_SID` are platform-specific. On some platforms, the SID is case-sensitive.

Note:

It is common practice to set the SID to be equal to the database name. The maximum number of characters for the database name is eight. For more information, see the discussion of the `DB_NAME` initialization parameter in [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams064.htm#REFRN10041).

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

[Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/startup.htm#CNCPT601) for background information about the Oracle instance

### Step 2: Ensure That the Required Environment Variables Are Set

Depending on your platform, before you can start SQL\*Plus (as required in Step 6: Connect to the Instance), you may have to set environment variables, or at least verify that they are set properly.

For example, on most platforms, `ORACLE_SID` and `ORACLE_HOME` must be set. In addition, it is advisable to set the `PATH` variable to include the ORACLE\_HOME/bin directory. On the UNIX and Linux platforms, you must set these environment variables manually. On the Windows platform, OUI automatically assigns values to `ORACLE_HOME` and `ORACLE_SID` in the Windows registry. If you did not create a database upon installation, OUI does not set `ORACLE_SID` in the registry, and you will have to set the `ORACLE_SID` environment variable when you create your database later.

### Step 3: Choose a Database Administrator Authentication Method

You must be authenticated and granted appropriate system privileges in order to create a database. You can be authenticated as an administrator with the required privileges in the following ways:

- With a password file
- With operating system authentication

In this step, you decide on an authentication method.

To be authenticated with a password file, create the password file as described in ["Creating and Maintaining a Password File"](dba.md). To be authenticated with operating system authentication, ensure that you log in to the host computer with a user account that is a member of the appropriate operating system user group. On the UNIX and Linux platforms, for example, this is typically the `dba` user group. On the Windows platform, the user installing the Oracle software is automatically placed in the required user group.

See Also:

- ["About Database Administrator Security and Privileges"](dba.md)
- ["Database Administrator Authentication"](dba.md) for information about password files and operating system authentication

### Step 4: Create the Initialization Parameter File

When an Oracle instance starts, it reads an initialization parameter file. This file can be a text file, which can be created and modified with a text editor, or a binary file, which is created and dynamically modified by the database. The binary file, which is preferred, is called a server parameter file. In this step, you create a text initialization parameter file. In a later step, you create a server parameter file from the text file.

One way to create the text initialization parameter file is to edit the sample presented in "Sample Initialization Parameter File".

If you create the initialization parameter file manually, ensure that it contains at least the parameters listed in Table 2-2. All other parameters not listed have default values.

Table 2-2 Recommended Minimum Initialization Parameters

| Parameter Name | Mandatory | Notes |
| --- | --- | --- |
| `DB_NAME` | Yes | Database identifier. Must correspond to the value used in the `CREATE` `DATABASE` statement. Maximum 8 characters. |
| `CONTROL_FILES` | No | Strongly recommended. If not provided, then the database instance creates one control file in the same location as the initialization parameter file. Providing this parameter enables you to multiplex control files. See ["Creating Initial Control Files"](control.md) for more information. |
| `MEMORY_TARGET` | No | Sets the total amount of memory used by the instance and enables automatic memory management. You can choose other initialization parameters instead of this one for more manual control of memory usage. See ["Configuring Memory Manually"](memory.md). |

For convenience, store your initialization parameter file in the Oracle Database default location, using the default file name. Then when you start your database, it will not be necessary to specify the `PFILE` clause of the `STARTUP` command, because Oracle Database automatically looks in the default location for the initialization parameter file.

For more information about initialization parameters and the initialization parameter file, including the default name and location of the initialization parameter file for your platform, see "About Initialization Parameters and Initialization Parameter Files".

See Also:

- "Specifying Initialization Parameters"
- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm) for details on all initialization parameters

### Step 5: (Windows Only) Create an Instance

On the Windows platform, before you can connect to an instance, you must manually create it if it does not already exist. The `ORADIM` command creates an Oracle instance by creating a new Windows service.

To create an instance:

- Enter the following command at a Windows command prompt:
	```
	oradim -NEW -SID sid -STARTMODE MANUAL -PFILE pfile
	```
	where `sid` is the desired SID (for example `mynewdb`) and `pfile` is the full path to the text initialization parameter file. This command creates the instance but does not start it.

Caution:

Do not set the - `STARTMODE` argument to `AUTO` at this point, because this causes the new instance to start and attempt to mount the database, which does not exist yet. You can change this parameter to `AUTO`, if desired, in Step 14.

See the section "Using ORADIM to Administer an Oracle Database Instance" in [Oracle Database Platform Guide for Microsoft Windows](https://docs.oracle.com/cd/E11882_01/win.112/e10845/create.htm#NTQRF05011) for more information on the `ORADIM` command.

### Step 6: Connect to the Instance

Start SQL\*Plus and connect to your Oracle Database instance with the `SYSDBA` system privilege.

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
Oracle Database 11g Enterprise Edition Release 11.2.0.1.0 - Production
With the Partitioning, OLAP and Data Mining options
```

If so, the instance is already started. You may have connected to the wrong instance. Exit SQL\*Plus with the `EXIT` command, check that `ORACLE_SID` is set properly, and repeat this step.

### Step 7: Create a Server Parameter File

The server parameter file enables you to change initialization parameters with the `ALTER` `SYSTEM` command and persist the changes across a database shutdown and startup. You create the server parameter file from your edited text initialization file.

The following SQL\*Plus command reads the text initialization parameter file (PFILE) with the default name from the default location, creates a server parameter file (SPFILE) from the text initialization parameter file, and writes the SPFILE to the default location with the default SPFILE name.

```
CREATE SPFILE FROM PFILE;
```

You can also supply the file name and path for both the PFILE and SPFILE if you are not using default names and locations.

Tip:

The database must be restarted before the server parameter file takes effect.

Note:

Although creating a server parameter file is optional at this point, it is recommended. If you do not create a server parameter file, the instance continues to read the text initialization parameter file whenever it starts.

Important—If you are using Oracle Managed Files and your initialization parameter file does not contain the `CONTROL_FILES` parameter, then you must create a server parameter file now so the database can save the names and location of the control files that it creates during the `CREATE` `DATABASE` statement. See "Specifying Oracle Managed Files at Database Creation" for more information.

See Also:

- "Managing Initialization Parameters Using a Server Parameter File"
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_6016.htm#SQLRF01315) for more information on the `CREATE` `SPFILE` command

### Step 8: Start the Instance

Start an instance without mounting a database. Typically, you do this only during database creation or while performing maintenance on the database. Use the `STARTUP` command with the `NOMOUNT` clause. In this example, because the initialization parameter file or server parameter file is stored in the default location, you are not required to specify the `PFILE` clause:

```
STARTUP NOMOUNT
```

At this point, the instance memory is allocated and its processes are started. The database itself does not yet exist.

See Also:

- [Chapter 3, "Starting Up and Shutting Down"](start.md), to learn how to use the `STARTUP` command
- "Managing Initialization Parameters Using a Server Parameter File"

### Step 9: Issue the CREATE DATABASE Statement

To create the new database, use the `CREATE` `DATABASE` statement.

Example 1

The following statement creates database `mynewdb`. This database name must agree with the `DB_NAME` parameter in the initialization parameter file. This example assumes the following:

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
   MAXLOGFILES 5
   MAXLOGMEMBERS 5
   MAXLOGHISTORY 1
   MAXDATAFILES 100
   CHARACTER SET AL32UTF8
   NATIONAL CHARACTER SET AL16UTF16
   EXTENT MANAGEMENT LOCAL
   DATAFILE '/u01/app/oracle/oradata/mynewdb/system01.dbf' SIZE 325M REUSE
   SYSAUX DATAFILE '/u01/app/oracle/oradata/mynewdb/sysaux01.dbf' SIZE 325M REUSE
   DEFAULT TABLESPACE users
      DATAFILE '/u01/app/oracle/oradata/mynewdb/users01.dbf'
      SIZE 500M REUSE AUTOEXTEND ON MAXSIZE UNLIMITED
   DEFAULT TEMPORARY TABLESPACE tempts1
      TEMPFILE '/u01/app/oracle/oradata/mynewdb/temp01.dbf'
      SIZE 20M REUSE
   UNDO TABLESPACE undotbs
      DATAFILE '/u01/app/oracle/oradata/mynewdb/undotbs01.dbf'
      SIZE 200M REUSE AUTOEXTEND ON MAXSIZE UNLIMITED;
```

A database is created with the following characteristics:

- The database is named `mynewdb`. Its global database name is `mynewdb.us.example.com`, where the domain portion (`us.example.com`) is taken from the initialization parameter file. See "Determining the Global Database Name".
- Three control files are created as specified by the `CONTROL_FILES` initialization parameter, which was set before database creation in the initialization parameter file. See "Sample Initialization Parameter File" and "Specifying Control Files".
- The passwords for user accounts `SYS` and `SYSTEM` are set to the values that you specified. Beginning with Release 11g, the passwords are case-sensitive. The two clauses that specify the passwords for `SYS` and `SYSTEM` are not mandatory in this release of Oracle Database. However, if you specify either clause, then you must specify both clauses. For further information about the use of these clauses, see "Protecting Your Database: Specifying Passwords for Users SYS and SYSTEM".
- The new database has three redo log file groups, each with two members, as specified in the `LOGFILE` clause. `MAXLOGFILES`, `MAXLOGMEMBERS`, and `MAXLOGHISTORY` define limits for the redo log. See ["Choosing the Number of Redo Log Files"](onlineredo.md). The block size for the redo logs is set to 512 bytes, the same size as physical sectors on disk. The `BLOCKSIZE` clause is optional if block size is to be the same as physical sector size (the default). Typical sector size and thus typical block size is 512. Permissible values for `BLOCKSIZE` are 512, 1024, and 4096. For newer disks with a 4K sector size, optionally specify `BLOCKSIZE` as 4096. See ["Planning the Block Size of Redo Log Files"](onlineredo.md) for more information.
- `MAXDATAFILES` specifies the maximum number of data files that can be open in the database. This number affects the initial sizing of the control file.
	Note:
	You can set several limits during database creation. Some of these limits are limited by and affected by operating system limits. For example, if you set `MAXDATAFILES`, Oracle Database allocates enough space in the control file to store `MAXDATAFILES` filenames, even if the database has only one data file initially. However, because the maximum control file size is limited and operating system dependent, you might not be able to set all `CREATE DATABASE` parameters at their theoretical maximums.
	For more information about setting limits during database creation, see the [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_5004.htm#SQLRF01204) and your operating system–specific Oracle documentation.
- The `AL32UTF8` character set is used to store data in this database.
- The `AL16UTF16` character set is specified as the `NATIONAL CHARACTER SET,` used to store data in columns specifically defined as `NCHAR`, `NCLOB`, or `NVARCHAR2`.
- The `SYSTEM` tablespace, consisting of the operating system file `/u01/app/oracle/oradata/mynewdb/system01.dbf` is created as specified by the `DATAFILE` clause. If a file with that name already exists, then it is overwritten.
- The `SYSTEM` tablespace is created as a locally managed tablespace. See "Creating a Locally Managed SYSTEM Tablespace".
- A `SYSAUX` tablespace is created, consisting of the operating system file `/u01/app/oracle/oradata/mynewdb/sysaux01.dbf` as specified in the `SYSAUX DATAFILE` clause. See "About the SYSAUX Tablespace".
- The `DEFAULT` `TABLESPACE` clause creates and names a default permanent tablespace for this database.
- The `DEFAULT TEMPORARY TABLESPACE` clause creates and names a default temporary tablespace for this database. See "Creating a Default Temporary Tablespace".
- The `UNDO TABLESPACE` clause creates and names an undo tablespace that is used to store undo data for this database if you have specified `UNDO_MANAGEMENT=AUTO` in the initialization parameter file. If you omit this parameter, it defaults to `AUTO`. See "Using Automatic Undo Management: Creating an Undo Tablespace".
- Redo log files will not initially be archived, because the `ARCHIVELOG` clause is not specified in this `CREATE` `DATABASE` statement. This is customary during database creation. You can later use an `ALTER DATABASE` statement to switch to `ARCHIVELOG` mode. The initialization parameters in the initialization parameter file for `mynewdb` relating to archiving are `LOG_ARCHIVE_DEST_1` and `LOG_ARCHIVE_FORMAT`. See [Chapter 13, "Managing Archived Redo Logs"](archredo.md).

Tips:

- Ensure that all directories used in the `CREATE` `DATABASE` statement exist. The `CREATE` `DATABASE` statement does not create directories.
- If you are not using Oracle Managed Files, then every tablespace clause must include a `DATAFILE` or `TEMPFILE` clause.
- If database creation fails, then you can look at the alert log to determine the reason for the failure and to determine corrective actions. See ["Viewing the Alert Log"](diag.md). If you receive an error message that contains a process number, then examine the trace file for that process. Look for the trace file that contains the process number in the trace file name. See ["Finding Trace Files"](diag.md) for more information.
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

If your `CREATE` `DATABASE` statement fails, and if you did not complete Step 7, then ensure that there is not a pre-existing server parameter file (SPFILE) for this instance that is setting initialization parameters in an unexpected way. For example, an SPFILE contains a setting for the complete path to all control files, and the `CREATE` `DATABASE` statement fails if those control files do not exist. Ensure that you shut down and restart the instance (with `STARTUP` `NOMOUNT`) after removing an unwanted SPFILE. See "Managing Initialization Parameters Using a Server Parameter File" for more information.

See Also:

- "Specifying CREATE DATABASE Statement Clauses"
- "Specifying Oracle Managed Files at Database Creation"
- [Chapter 17, "Using Oracle Managed Files"](omf.md)
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_5004.htm#SQLRF01204) for more information about specifying the clauses and parameter values for the `CREATE DATABASE` statement

### Step 10: Create Additional Tablespaces

To make the database functional, you must create additional tablespaces for your application data. The following sample script creates some additional tablespaces:

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

For information about creating tablespaces, see [Chapter 14, "Managing Tablespaces"](tspaces.md).

### Step 11: Run Scripts to Build Data Dictionary Views

Run the scripts necessary to build data dictionary views, synonyms, and PL/SQL packages, and to support proper functioning of SQL\*Plus.

In SQL\*Plus, connect to your Oracle Database instance with the `SYSDBA` administrative privilege:

```
@?/rdbms/admin/catalog.sql
@?/rdbms/admin/catproc.sql
@?/rdbms/admin/utlrp.sql
```

In SQL\*Plus, connect to your Oracle Database instance as `SYSTEM` user:

```
@?/sqlplus/admin/pupbld.sql
```

The at-sign (`@`) is shorthand for the command that runs a SQL\*Plus script. The question mark (`?`) is a SQL\*Plus variable indicating the Oracle home directory. The following table contains descriptions of the scripts:

| Script | Description |
| --- | --- |
| `CATALOG.SQL` | Creates the views of the data dictionary tables, the dynamic performance views, and public synonyms for many of the views. Grants `PUBLIC` access to the synonyms. |
| `CATPROC.SQL` | Runs all scripts required for or used with PL/SQL. |
| `UTLRP.SQL` | Recompiles all PL/SQL modules that are in an invalid state, including packages, procedures, and types. |
| `PUPBLD.SQL` | Required for SQL\*Plus. Enables SQL\*Plus to disable commands by user. |

### Step 12: (Optional) Run Scripts to Install Additional Options

You may want to run other scripts. The scripts that you run are determined by the features and options you choose to use or install. Many of the scripts available to you are described in the [Oracle Database Reference.](https://docs.oracle.com/cd/E11882_01/server.112/e40402/scripts.htm#REFRN005)

If you plan to install other Oracle products to work with this database, then see the installation instructions for those products. Some products require you to create additional data dictionary tables. Usually, command files are provided to create and load these tables into the database data dictionary.

See your Oracle documentation for the specific products that you plan to install for installation and administration instructions.

### Step 13: Back Up the Database.

Take a full backup of the database to ensure that you have a complete set of files from which to recover if a media failure occurs. For information on backing up a database, see [Oracle Database Backup and Recovery User's Guide.](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/toc.htm)

### Step 14: (Optional) Enable Automatic Instance Startup

You might want to configure the Oracle instance to start automatically when its host computer restarts. See your operating system documentation for instructions. For example, on Windows, use the following command to configure the database service to start the instance upon computer restart:

```
ORADIM -EDIT -SID sid -STARTMODE AUTO -SRVCSTART SYSTEM [-SPFILE]
```

You must use the `-SPFILE` argument if you want the instance to read an SPFILE upon automatic restart.

See Also:

- [Chapter 4, "Configuring Automatic Restart of an Oracle Database"](restart.md)
- The section "Using ORADIM to Administer an Oracle Database Instance" in [Oracle Database Platform Guide for Microsoft Windows](https://docs.oracle.com/cd/E11882_01/win.112/e10845/create.htm#NTQRF05011) for more information on the `ORADIM` command.

## Specifying CREATE DATABASE Statement Clauses

When you execute a `CREATE` `DATABASE` statement, Oracle Database performs several operations. The actual operations performed depend on the clauses that you specify in the `CREATE` `DATABASE` statement and the initialization parameters that you have set. Oracle Database performs at least these operations:

- Creates the data files for the database
- Creates the control files for the database
- Creates the redo log files for the database and establishes the `ARCHIVELOG` mode
- Creates the `SYSTEM` tablespace
- Creates the `SYSAUX` tablespace
- Creates the data dictionary
- Sets the character set that stores data in the database
- Sets the database time zone
- Mounts and opens the database for use

This section discusses several of the clauses of the `CREATE` `DATABASE` statement. It expands upon some of the clauses discussed in "Step 9: Issue the CREATE DATABASE Statement" and introduces additional ones. Many of the `CREATE DATABASE` clauses discussed here can be used to simplify the creation and management of your database.

The following topics are contained in this section:

- Protecting Your Database: Specifying Passwords for Users SYS and SYSTEM
- Creating a Locally Managed SYSTEM Tablespace
- About the SYSAUX Tablespace
- Using Automatic Undo Management: Creating an Undo Tablespace
- Creating a Default Temporary Tablespace
- Specifying Oracle Managed Files at Database Creation
- Supporting Bigfile Tablespaces During Database Creation
- Specifying the Database Time Zone and Time Zone File
- Specifying FORCE LOGGING Mode

### Protecting Your Database: Specifying Passwords for Users SYS and SYSTEM

The clauses of the `CREATE` `DATABASE` statement used for specifying the passwords for users `SYS` and `SYSTEM` are:

- `USER` `SYS` `IDENTIFIED` `BY` `password`
- `USER` `SYSTEM` `IDENTIFIED` `BY` `password`

If you omit these clauses, then these users are assigned the default passwords `change_on_install` and `manager`, respectively. A record is written to the alert log indicating that the default passwords were used. To protect your database, you must change these passwords using the `ALTER USER` statement immediately after database creation.

Oracle strongly recommends that you specify these clauses, even though they are optional in this release of Oracle Database. The default passwords are commonly known, and if you neglect to change them later, then you leave database vulnerable to attack by malicious users.

When choosing a password, keep in mind that beginning in Release 11g, passwords are case-sensitive. Also, there may be password formatting requirements for your database. See the section entitled "How Oracle Database Checks the Complexity of Passwords" in [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/authentication.htm#DBSEG33223) for more information.

See Also:

"Some Security Considerations"

### Creating a Locally Managed SYSTEM Tablespace

Specify the `EXTENT MANAGEMENT LOCAL` clause in the `CREATE` `DATABASE` statement to create a locally managed `SYSTEM` tablespace. The `COMPATIBLE` initialization parameter must be set to 10.0.0 or higher for this statement to be successful. If you do not specify the `EXTENT MANAGEMENT LOCAL` clause, then by default the database creates a dictionary-managed `SYSTEM` tablespace. Dictionary-managed tablespaces are deprecated.

If you create your database with a locally managed `SYSTEM` tablespace, and if you are not using Oracle Managed Files, then ensure that the following conditions are met:

- You specify the `DEFAULT` `TEMPORARY` `TABLESPACE` clause in the `CREATE` `DATABASE` statement.
- You include the `UNDO TABLESPACE` clause in the `CREATE` `DATABASE` statement.

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_5004.htm#SQLRF01204) for more specific information about the use of the `DEFAULT TEMPORARY TABLESPACE` and `UNDO TABLESPACE` clauses when `EXTENT MANAGEMENT LOCAL` is specified for the `SYSTEM` tablespace
- ["Locally Managed Tablespaces"](tspaces.md)
- ["Migrating the SYSTEM Tablespace to a Locally Managed Tablespace"](tspaces.md)

### About the SYSAUX Tablespace

The `SYSAUX` tablespace is always created at database creation. The `SYSAUX` tablespace serves as an auxiliary tablespace to the `SYSTEM` tablespace. Because it is the default tablespace for many Oracle Database features and products that previously required their own tablespaces, it reduces the number of tablespaces required by the database. It also reduces the load on the `SYSTEM` tablespace.

You can specify only data file attributes for the `SYSAUX` tablespace, using the `SYSAUX DATAFILE` clause in the `CREATE` `DATABASE` statement. Mandatory attributes of the `SYSAUX` tablespace are set by Oracle Database and include:

- `PERMANENT`
- `READ` `WRITE`
- `EXTENT` `MANAGMENT` `LOCAL`
- `SEGMENT` `SPACE` `MANAGMENT` `AUTO`

You cannot alter these attributes with an `ALTER` `TABLESPACE` statement, and any attempt to do so will result in an error. You cannot drop or rename the `SYSAUX` tablespace.

The size of the `SYSAUX` tablespace is determined by the size of the database components that occupy `SYSAUX`. You can view a list of these components by querying the `V$SYSAUX_OCCUPANTS` view. Based on the initial sizes of these components, the `SYSAUX` tablespace must be at least 400 MB at the time of database creation. The space requirements of the `SYSAUX` tablespace will increase after the database is fully deployed, depending on the nature of its use and workload. For more information on how to manage the space consumption of the `SYSAUX` tablespace on an ongoing basis, see the ["Managing the SYSAUX Tablespace"](tspaces.md).

If you include a `DATAFILE` clause for the `SYSTEM` tablespace, then you must specify the `SYSAUX DATAFILE` clause as well, or the `CREATE` `DATABASE` statement will fail. This requirement does not exist if the Oracle Managed Files feature is enabled (see "Specifying Oracle Managed Files at Database Creation").

The `SYSAUX` tablespace has the same security attributes as the `SYSTEM` tablespace.

Note:

This documentation discusses the creation of the `SYSAUX` database at database creation. When upgrading from a release of Oracle Database that did not require the `SYSAUX` tablespace, you must create the `SYSAUX` tablespace as part of the upgrade process. This is discussed in [Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/toc.htm).

See Also:

["Managing the SYSAUX Tablespace"](tspaces.md)

### Using Automatic Undo Management: Creating an Undo Tablespace

Automatic undo management uses an undo tablespace. To enable automatic undo management, set the `UNDO_MANAGEMENT` initialization parameter to `AUTO` in your initialization parameter file. Or, omit this parameter, and the database defaults to automatic undo management. In this mode, undo data is stored in an undo tablespace and is managed by Oracle Database. To define and name the undo tablespace yourself, you must include the `UNDO TABLESPACE` clause in the `CREATE DATABASE` statement at database creation time. If you omit this clause, and automatic undo management is enabled, then the database creates a default undo tablespace named `SYS_UNDOTBS`.

See Also:

- "Specifying the Method of Undo Space Management"
- [Chapter 16, "Managing Undo"](undo.md), for information about the creation and use of undo tablespaces

### Creating a Default Permanent Tablespace

The `DEFAULT` `TABLESPACE` clause of the `CREATE` `DATABASE` statement specifies a default permanent tablespace for the database. Oracle Database assigns to this tablespace any non- `SYSTEM` users for whom you do not explicitly specify a different permanent tablespace. If you do not specify this clause, then the `SYSTEM` tablespace is the default permanent tablespace for non- `SYSTEM` users. Oracle strongly recommends that you create a default permanent tablespace.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_5004.htm#SQLRF01204) for the syntax of the `DEFAULT TABLESPACE` clause of `CREATE DATABASE` and `ALTER DATABASE`

### Creating a Default Temporary Tablespace

The `DEFAULT TEMPORARY TABLESPACE` clause of the `CREATE` `DATABASE` statement creates a default temporary tablespace for the database. Oracle Database assigns this tablespace as the temporary tablespace for users who are not explicitly assigned a temporary tablespace.

You can explicitly assign a temporary tablespace or tablespace group to a user in the `CREATE USER` statement. However, if you do not do so, and if no default temporary tablespace has been specified for the database, then by default these users are assigned the `SYSTEM` tablespace as their temporary tablespace. It is not good practice to store temporary data in the `SYSTEM` tablespace, and it is cumbersome to assign every user a temporary tablespace individually. Therefore, Oracle recommends that you use the `DEFAULT TEMPORARY TABLESPACE` clause of `CREATE` `DATABASE`.

Note:

When you specify a locally managed `SYSTEM` tablespace, the `SYSTEM` tablespace cannot be used as a temporary tablespace. In this case you must create a default temporary tablespace. This behavior is explained in "Creating a Locally Managed SYSTEM Tablespace".

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_5004.htm#SQLRF01204) for the syntax of the `DEFAULT TEMPORARY TABLESPACE` clause of `CREATE DATABASE` and `ALTER DATABASE`
- ["Temporary Tablespaces"](tspaces.md) for information about creating and using temporary tablespaces
- ["Multiple Temporary Tablespaces: Using Tablespace Groups"](tspaces.md) for information about creating and using temporary tablespace groups

### Specifying Oracle Managed Files at Database Creation

You can minimize the number of clauses and parameters that you specify in your `CREATE` `DATABASE` statement by using the Oracle Managed Files feature. You do this by specifying either a directory or Oracle Automatic Storage Management (Oracle ASM) disk group in which your files are created and managed by Oracle Database.

By including any of the initialization parameters `DB_CREATE_FILE_DEST,` `DB_CREATE_ONLINE_LOG_DEST_` `n`, or `DB_RECOVERY_FILE_DEST` in your initialization parameter file, you instruct Oracle Database to create and manage the underlying operating system files of your database. Oracle Database will automatically create and manage the operating system files for the following database structures, depending on which initialization parameters you specify and how you specify clauses in your `CREATE` `DATABASE` statement:

- Tablespaces and their data files
- Temporary tablespaces and their temp files
- Control files
- Redo log files
- Archived redo log files
- Flashback logs
- Block change tracking files
- RMAN backups

See Also:

"Specifying a Fast Recovery Area" for information about setting initialization parameters that create a Fast Recovery Area

The following `CREATE` `DATABASE` statement shows briefly how the Oracle Managed Files feature works, assuming you have specified required initialization parameters:

```
CREATE DATABASE mynewdb
     USER SYS IDENTIFIED BY sys_password
     USER SYSTEM IDENTIFIED BY system_password
     EXTENT MANAGEMENT LOCAL
     UNDO TABLESPACE undotbs
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
- If you are using a server parameter file (see "Managing Initialization Parameters Using a Server Parameter File"), then the database automatically sets the appropriate initialization parameters.
	See Also:
	- [Chapter 17, "Using Oracle Managed Files"](omf.md), for information about the Oracle Managed Files feature and how to use it
	- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/toc.htm). for information about Automatic Storage Management

### Supporting Bigfile Tablespaces During Database Creation

Oracle Database simplifies management of tablespaces and enables support for ultra-large databases by letting you create bigfile tablespaces. Bigfile tablespaces can contain only one file, but that file can have up to 4G blocks. The maximum number of data files in an Oracle Database is limited (usually to 64K files). Therefore, bigfile tablespaces can significantly enhance the storage capacity of an Oracle Database.

This section discusses the clauses of the `CREATE` `DATABASE` statement that let you include support for bigfile tablespaces.

See Also:

["Bigfile Tablespaces"](tspaces.md) for more information about bigfile tablespaces

#### Specifying the Default Tablespace Type

The `SET DEFAULT...TABLESPACE` clause of the `CREATE` `DATABASE` statement determines the default type of tablespace for this database in subsequent `CREATE` `TABLESPACE` statements. Specify either `SET DEFAULT BIGFILE TABLESPACE` or `SET DEFAULT SMALLFILE TABLESPACE`. If you omit this clause, then the default is a smallfile tablespace, which is the traditional type of Oracle Database tablespace. A smallfile tablespace can contain up to 1022 files with up to 4M blocks each.

The use of bigfile tablespaces further enhances the Oracle Managed Files feature, because bigfile tablespaces make data files completely transparent for users. SQL syntax for the `ALTER` `TABLESPACE` statement has been extended to allow you to perform operations on tablespaces, rather than the underlying data files.

The `CREATE` `DATABASE` statement shown in "Specifying Oracle Managed Files at Database Creation" can be modified as follows to specify that the default type of tablespace is a bigfile tablespace:

```
CREATE DATABASE mynewdb
     USER SYS IDENTIFIED BY sys_password
     USER SYSTEM IDENTIFIED BY system_password
     SET DEFAULT BIGFILE TABLESPACE
     UNDO TABLESPACE undotbs
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

#### Overriding the Default Tablespace Type

The `SYSTEM` and `SYSAUX` tablespaces are always created with the default tablespace type. However, you can explicitly override the default tablespace type for the `UNDO` and `DEFAULT` `TEMPORARY` tablespace during the `CREATE` `DATABASE` operation.

For example, you can create a bigfile `UNDO` tablespace in a database with the default tablespace type of smallfile as follows:

```
CREATE DATABASE mynewdb
...
     BIGFILE UNDO TABLESPACE undotbs
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

### Specifying the Database Time Zone and Time Zone File

This section contains:

- Setting the Database Time Zone
- About the Database Time Zone Files
- Specifying the Database Time Zone File

#### Setting the Database Time Zone

Set the database time zone when the database is created by using the `SET TIME_ZONE` clause of the `CREATE DATABASE` statement. If you do not set the database time zone, then it defaults to the time zone of the host operating system.

You can change the database time zone for a session by using the `SET TIME_ZONE` clause of the `ALTER SESSION` statement.

See Also:

[Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/ch4datetime.htm#NLSPG262) for more information about setting the database time zone

#### About the Database Time Zone Files

Two time zone files are included in a subdirectory of the Oracle home directory. The time zone files contain the valid time zone names. The following information is also included for each time zone:

- Offset from Coordinated Universal Time (UTC)
- Transition times for Daylight Saving Time
- Abbreviations for standard time and Daylight Saving Time

The default time zone file is ORACLE\_HOME/oracore/zoneinfo/timezlrg\_11.dat. A smaller time zone file with fewer time zones can be found in ORACLE\_HOME/oracore/zoneinfo/timezone\_11.dat.

To view the time zone names in the file being used by your database, use the following query:

```
SELECT * FROM V$TIMEZONE_NAMES;
```

See Also:

[Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/ch4datetime.htm#NLSPG004) for more information about managing and selecting time zone files

#### Specifying the Database Time Zone File

All databases that share information must use the same time zone data file.

The database server always uses the large time zone file by default. If you would like to use the small time zone file on the client and know that all your data will refer only to regions in the small file, you can set the `ORA_TZFILE` environment variable on the client to the full path name of the timezone\_ `version`.dat file on the client, where `version` matches the time zone file version that is being used by the database server.

If you are already using the default larger time zone file on the client, then it is not practical to change to the smaller time zone file, because the database may contain data with time zones that are not part of the smaller file.

### Specifying FORCE LOGGING Mode

Some data definition language statements (such as `CREATE` `TABLE`) allow the `NOLOGGING` clause, which causes some database operations not to generate redo records in the database redo log. The `NOLOGGING` setting can speed up operations that can be easily recovered outside of the database recovery mechanisms, but it can negatively affect media recovery and standby databases.

Oracle Database lets you force the writing of redo records even when `NOLOGGING` has been specified in DDL statements. The database never generates redo records for temporary tablespaces and temporary segments, so forced logging has no affect for objects.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/clauses005.htm#SQLRF30009) for information about operations that can be done in `NOLOGGING` mode

#### Using the FORCE LOGGING Clause

To put the database into `FORCE LOGGING` mode, use the `FORCE LOGGING` clause in the `CREATE DATABASE` statement. If you do not specify this clause, the database is not placed into `FORCE LOGGING` mode.

Use the `ALTER DATABASE` statement to place the database into `FORCE LOGGING` mode after database creation. This statement can take a considerable time for completion, because it waits for all unlogged direct writes to complete.

You can cancel `FORCE LOGGING` mode using the following SQL statement:

```
ALTER DATABASE NO FORCE LOGGING;
```

Independent of specifying `FORCE LOGGING` for the database, you can selectively specify `FORCE LOGGING` or `NO FORCE LOGGING` at the tablespace level. However, if `FORCE LOGGING` mode is in effect for the database, it takes precedence over the tablespace setting. If it is not in effect for the database, then the individual tablespace settings are enforced. Oracle recommends that either the entire database is placed into `FORCE LOGGING` mode, or individual tablespaces be placed into `FORCE LOGGING` mode, but not both.

The `FORCE LOGGING` mode is a persistent attribute of the database. That is, if the database is shut down and restarted, it remains in the same logging mode. However, if you re-create the control file, the database is not restarted in the `FORCE LOGGING` mode unless you specify the `FORCE LOGGING` clause in the `CREATE CONTROL FILE` statement.

See Also:

["Controlling the Writing of Redo Records"](tspaces.md) for information about using the `FORCE LOGGING` clause for tablespace creation.

#### Performance Considerations of FORCE LOGGING Mode

`FORCE LOGGING` mode results in some performance degradation. If the primary reason for specifying `FORCE LOGGING` is to ensure complete media recovery, and there is no standby database active, then consider the following:

- How many media failures are likely to happen?
- How serious is the damage if unlogged direct writes cannot be recovered?
- Is the performance degradation caused by forced logging tolerable?

If the database is running in `NOARCHIVELOG` mode, then generally there is no benefit to placing the database in `FORCE LOGGING` mode. Media recovery is not possible in `NOARCHIVELOG` mode, so if you combine it with `FORCE LOGGING`, the result may be performance degradation with little benefit.

## Specifying Initialization Parameters

This section introduces you to some of the basic initialization parameters you can add or edit before you create your new database. The following topics are covered:

- About Initialization Parameters and Initialization Parameter Files
- Determining the Global Database Name
- Specifying a Fast Recovery Area
- Specifying Control Files
- Specifying Database Block Sizes
- Specifying the Maximum Number of Processes
- Specifying the DDL Lock Timeout
- Specifying the Method of Undo Space Management
- About The COMPATIBLE Initialization Parameter
- Setting the License Parameter
	See Also:
	- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams_part.htm#REFRN001) for descriptions of all initialization parameters including their default settings
	- [Chapter 6, "Managing Memory"](memory.md) for a discussion of the initialization parameters that pertain to memory management

### About Initialization Parameters and Initialization Parameter Files

When an Oracle instance starts, it reads initialization parameters from an initialization parameter file. This file must at a minimum specify the `DB_NAME` parameter. All other parameters have default values.

The initialization parameter file can be either a read-only text file, a `PFILE`, or a read/write binary file.

The binary file is called a server parameter file. A server parameter file enables you to change initialization parameters with `ALTER SYSTEM` commands and to persist the changes across a shutdown and startup. It also provides a basis for self-tuning by Oracle Database. For these reasons, it is recommended that you use a server parameter file. You can create one manually from your edited text initialization file, or automatically by using Database Configuration Assistant (DBCA) to create your database.

Before you manually create a server parameter file, you can start an instance with a text initialization parameter file. Upon startup, the Oracle instance first searches for a server parameter file in a default location, and if it does not find one, searches for a text initialization parameter file. You can also override an existing server parameter file by naming a text initialization parameter file as an argument of the `STARTUP` command.

Default file names and locations for the text initialization parameter file are shown in the following table:

| Platform | Default Name | Default Location |
| --- | --- | --- |
| UNIX and Linux | `init` `ORACLE_SID`.`ora`  For example, the initialization parameter file for the `mynewdb` database is named:  `initmynewdb.ora` | ORACLE\_HOME/ `dbs` |
| Windows | `init` `ORACLE_SID``.ora` | ORACLE\_HOME\\ `database` |

If you are creating an Oracle database for the first time, Oracle suggests that you minimize the number of parameter values that you alter. As you become more familiar with your database and environment, you can dynamically tune many initialization parameters using the `ALTER SYSTEM` statement. If you are using a text initialization parameter file, then your changes are effective only for the current instance. To make them permanent, you must update them manually in the initialization parameter file, or they will be lost over the next shutdown and startup of the database. If you are using a server parameter file, then initialization parameter file changes made by the `ALTER SYSTEM` statement can persist across shutdown and startup.

See Also:

- "Determining the Global Database Name" for information about the `DB_NAME` parameter
- "Managing Initialization Parameters Using a Server Parameter File"
- ["About Initialization Parameter Files and Startup"](start.md)

#### Text Initialization Parameter File Format

The text initialization parameter file (PFILE) must contain name/value pairs in one of the following forms:

- For parameters that accept only a single value:
	```
	parameter_name=value
	```
- For parameters that accept one or more values (such as the `CONTROL_FILES` parameter):
	```
	parameter_name=(value[,value] ...)
	```

Parameter values of type string must be enclosed in single quotes ('). Case (upper or lower) in filenames is significant only if case is significant on the host operating system.

For parameters that accept multiple values, to enable you to easily copy and paste name/value pairs from the alert log, you can repeat a parameter on multiple lines, where each line contains a different value.

```
control_files='/u01/app/oracle/oradata/orcl/control01.ctl'
control_files='/u01/app/oracle/oradata/orcl/control02.ctl'
control_files='/u01/app/oracle/oradata/orcl/control03.ctl'
```

If you repeat a parameter that does not accept multiple values, then only the last value specified takes effect.

See Also:

- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm) for more information about the content and syntax of the text initialization parameter file
- ["Alert Log"](diag.md)

#### Sample Initialization Parameter File

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
audit_file_dest='<ORACLE_BASE>/admin/orcl/adump'
audit_trail ='db'
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
compatible ='11.2.0'
```

### Determining the Global Database Name

The global database name consists of the user-specified local database name and the location of the database within a network structure. The `DB_NAME` initialization parameter determines the local name component of the database name, and the `DB_DOMAIN` parameter, which is optional, indicates the domain (logical location) within a network structure. The combination of the settings for these two parameters must form a database name that is unique within a network.

For example, to create a database with a global database name of `test.us.example.com`, edit the parameters of the new parameter file as follows:

```
DB_NAME = test
DB_DOMAIN = us.example.com
```

You can rename the `GLOBAL_NAME` of your database using the `ALTER DATABASE RENAME GLOBAL_NAME` statement. However, you must also shut down and restart the database after first changing the `DB_NAME` and `DB_DOMAIN` initialization parameters and re-creating the control files. Re-creating the control files is easily accomplished with the command `ALTER` `DATABASE` `BACKUP` `CONTROLFILE` `TO` `TRACE`. See [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/osbackup.htm#BRADV90011) for more information.

See Also:

[Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/dbnewid.htm#SUTIL014) for information about using the `DBNEWID` utility, which is another means of changing a database name

#### DB\_NAME Initialization Parameter

`DB_NAME` must be set to a text string of no more than eight characters. During database creation, the name provided for `DB_NAME` is recorded in the data files, redo log files, and control file of the database. If during database instance startup the value of the `DB_NAME` parameter (in the parameter file) and the database name in the control file are different, the database does not start.

#### DB\_DOMAIN Initialization Parameter

`DB_DOMAIN` is a text string that specifies the network domain where the database is created. If the database you are about to create will ever be part of a distributed database system, then give special attention to this initialization parameter before database creation. This parameter is optional.

See Also:

[Part I, "Distributed Database Management"](part7.md) for more information about distributed databases

### Specifying a Fast Recovery Area

The Fast Recovery Area is a location in which Oracle Database can store and manage files related to backup and recovery. It is distinct from the database area, which is a location for the current database files (data files, control files, and online redo logs).

You specify the Fast Recovery Area with the following initialization parameters:

- `DB_RECOVERY_FILE_DEST`: Location of the Fast Recovery Area. This can be a directory, file system, or Automatic Storage Management (Oracle ASM) disk group. It cannot be a raw file system.
	In an Oracle Real Application Clusters (Oracle RAC) environment, this location must be on a cluster file system, Oracle ASM disk group, or a shared directory configured through NFS.
- `DB_RECOVERY_FILE_DEST_SIZE`: Specifies the maximum total bytes to be used by the Fast Recovery Area. This initialization parameter must be specified before `DB_RECOVERY_FILE_DEST` is enabled.

In an Oracle RAC environment, the settings for these two parameters must be the same on all instances.

You cannot enable these parameters if you have set values for the `LOG_ARCHIVE_DEST` and `LOG_ARCHIVE_DUPLEX_DEST` parameters. You must disable those parameters before setting up the Fast Recovery Area. You can instead set values for the `LOG_ARCHIVE_DEST_` `n` parameters. The `LOG_ARCHIVE_DEST_1` parameter is implicitly set to point to the Fast Recovery Area if a local archiving location has not been configured and `LOG_ARCHIVE_DEST_1` value has not been set.

Oracle recommends using a Fast Recovery Area, because it can simplify backup and recovery operations for your database.

See Also:

[Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmconfb.htm#BRADV8183) to learn how to create and use a Fast Recovery Area

### Specifying Control Files

The `CONTROL_FILES` initialization parameter specifies one or more control filenames for the database. When you execute the `CREATE DATABASE` statement, the control files listed in the `CONTROL_FILES` parameter are created.

If you do not include `CONTROL_FILES` in the initialization parameter file, then Oracle Database creates a control file in the same directory as the initialization parameter file, using a default operating system–dependent filename. If you have enabled Oracle Managed Files, the database creates Oracle managed control files.

If you want the database to create new operating system files when creating database control files, the filenames listed in the `CONTROL_FILES` parameter must not match any filenames that currently exist on your system. If you want the database to reuse or overwrite existing files when creating database control files, ensure that the filenames listed in the `CONTROL_FILES` parameter match the filenames that are to be reused, and include a `CONTROLFILE` `REUSE` clause in the `CREATE` `DATABASE` statement.

Oracle strongly recommends you use at least two control files stored on separate physical disk drives for each database.

### Specifying Database Block Sizes

The `DB_BLOCK_SIZE` initialization parameter specifies the standard block size for the database. This block size is used for the `SYSTEM` tablespace and by default in other tablespaces. Oracle Database can support up to four additional nonstandard block sizes.

#### DB\_BLOCK\_SIZE Initialization Parameter

The most commonly used block size should be picked as the standard block size. In many cases, this is the only block size that you must specify. Typically, `DB_BLOCK_SIZE` is set to either 4K or 8K. If you do not set a value for this parameter, then the default data block size is operating system specific, which is generally adequate.

You cannot change the block size after database creation except by re-creating the database. If the database block size is different from the operating system block size, then ensure that the database block size is a multiple of the operating system block size. For example, if your operating system block size is 2K (2048 bytes), the following setting for the `DB_BLOCK_SIZE` initialization parameter is valid:

```
DB_BLOCK_SIZE=4096
```

A larger data block size provides greater efficiency in disk and memory I/O (access and storage of data). Therefore, consider specifying a block size larger than your operating system block size if the following conditions exist:

- Oracle Database is on a large computer system with a large amount of memory and fast disk drives. For example, databases controlled by mainframe computers with vast hardware resources typically use a data block size of 4K or greater.
- The operating system that runs Oracle Database uses a small operating system block size. For example, if the operating system block size is 1K and the default data block size matches this, the database may be performing an excessive amount of disk I/O during normal operation. For best performance in this case, a database block should consist of multiple operating system blocks.
	See Also:
	Your operating system specific Oracle documentation for details about the default block size.

#### Nonstandard Block Sizes

Tablespaces of nonstandard block sizes can be created using the `CREATE TABLESPACE` statement and specifying the `BLOCKSIZE` clause. These nonstandard block sizes can have any of the following power-of-two values: 2K, 4K, 8K, 16K or 32K. Platform-specific restrictions regarding the maximum block size apply, so some of these sizes may not be allowed on some platforms.

To use nonstandard block sizes, you must configure subcaches within the buffer cache area of the SGA memory for all of the nonstandard block sizes that you intend to use. The initialization parameters used for configuring these subcaches are described in ["Using Automatic Shared Memory Management"](memory.md).

The ability to specify multiple block sizes for your database is especially useful if you are transporting tablespaces between databases. You can, for example, transport a tablespace that uses a 4K block size from an OLTP environment to a data warehouse environment that uses a standard block size of 8K.

Note:

A 32K block size is valid only on 64-bit platforms.

Caution:

Oracle recommends against specifying a 2K block size when 4K sector size disks are in use, because performance degradation can occur. For an explanation, see ["Planning the Block Size of Redo Log Files"](onlineredo.md).

See Also:

- ["Creating Tablespaces"](tspaces.md)
- ["Transporting Tablespaces Between Databases"](tspaces.md)

### Specifying the Maximum Number of Processes

The `PROCESSES` initialization parameter determines the maximum number of operating system processes that can be connected to Oracle Database concurrently. The value of this parameter must be a minimum of one for each background process plus one for each user process. The number of background processes will vary according the database features that you are using. For example, if you are using Advanced Queuing or the file mapping feature, then you will have additional background processes. If you are using Automatic Storage Management, then add three additional processes for the database instance.

If you plan on running 50 user processes, a good estimate would be to set the `PROCESSES` initialization parameter to 70.

### Specifying the DDL Lock Timeout

A data definition language (DDL) statement is either nonblocking or blocking, and both types of DDL statements require exclusive locks on internal structures. If these locks are unavailable when a DDL statement runs, then nonblocking and blocking DDL statements behave differently:

- Nonblocking DDL waits until every concurrent DML transaction that references the object affected by the DDL either commits or rolls back.
- Blocking DDL fails, though it might have succeeded if it had been executed subseconds later when the locks become available.

To enable blocking DDL statements to wait for locks, specify a DDL lock timeout—the number of seconds a DDL command waits for its required locks before failing.

To specify a DDL lock timeout, use the `DDL_LOCK_TIMEOUT` parameter. The permissible range of values for `DDL_LOCK_TIMEOUT` is 0 to 1,000,000. The default is 0. You can set `DDL_LOCK_TIMEOUT` at the system level, or at the session level with an `ALTER` `SESSION` statement.

Note:

The `DDL_LOCK_TIMOUT` parameter does not affect nonblocking DDL statements.

See Also:

- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams074.htm#REFRN10267)
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/ap_locks.htm#SQLRF55501)

### Specifying the Method of Undo Space Management

Every Oracle Database must have a method of maintaining information that is used to undo changes to the database. Such information consists of records of the actions of transactions, primarily before they are committed. Collectively these records are called undo data. This section provides instructions for setting up an environment for automatic undo management using an undo tablespace.

See Also:

[Chapter 16, "Managing Undo"](undo.md)

#### UNDO\_MANAGEMENT Initialization Parameter

The `UNDO_MANAGEMENT` initialization parameter determines whether an instance starts in automatic undo management mode, which stores undo in an undo tablespace. Set this parameter to `AUTO` to enable automatic undo management mode. Beginning with Release 11g, `AUTO` is the default if the parameter is omitted or is null.

#### UNDO\_TABLESPACE Initialization Parameter

When an instance starts up in automatic undo management mode, it attempts to select an undo tablespace for storage of undo data. If the database was created in automatic undo management mode, then the default undo tablespace (either the system-created `SYS_UNDOTBS` tablespace or the user-specified undo tablespace) is the undo tablespace used at instance startup. You can override this default for the instance by specifying a value for the `UNDO_TABLESPACE` initialization parameter. This parameter is especially useful for assigning a particular undo tablespace to an instance in an Oracle Real Application Clusters environment.

If no undo tablespace is specified by the `UNDO_TABLESPACE` initialization parameter, then the first available undo tablespace in the database is chosen. If no undo tablespace is available, then the instance starts without an undo tablespace, and undo data is written to the `SYSTEM` tablespace. You should avoid running in this mode.

Note:

When using the `CREATE` `DATABASE` statement to create a database, do not include an `UNDO_TABLESPACE` parameter in the initialization parameter file. Instead, include an `UNDO` `TABLESPACE` clause in the `CREATE` `DATABASE` statement.

### About The COMPATIBLE Initialization Parameter

The `COMPATIBLE` initialization parameter enables or disables the use of features in the database that affect file format on disk. For example, if you create an Oracle Database 11g Release 2 (11.2) database, but specify `COMPATIBLE=10.0.0` in the initialization parameter file, then features that require 11.2 compatibility generate an error if you try to use them. Such a database is said to be at the 10.0.0 compatibility level.

You can advance the compatibility level of your database by changing the `COMPATIBLE` initialization parameter. If you do, there is no way to start the database using a lower compatibility level setting, except by doing a point-in-time recovery to a time before the compatibility was advanced.

The default value for the `COMPATIBLE` parameter is the release number of the most recent major release.

Note:

- For Oracle Database 11g Release 2 (11.2), the default value of the `COMPATIBLE` parameter is 11.2.0.0.0. The minimum value is 10.0.0. If you create an Oracle Database using the default value, then you can immediately use all the new features in this release, and you can never downgrade the database.
- When you set this parameter in a server parameter file (SPFILE) using the `ALTER SYSTEM` statement, you must specify `SCOPE=SPFILE`, and you must restart the database for the change to take effect.

See Also:

- [Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/intro.htm#UPGRD12473) for a detailed discussion of database compatibility and the `COMPATIBLE` initialization parameter
- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams035.htm#REFRN10019)
- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmflash.htm#BRADV80055) for information about point-in-time recovery of your database

### Setting the License Parameter

Note:

Oracle no longer offers licensing by the number of concurrent sessions. Therefore the `LICENSE_MAX_SESSIONS` and `LICENSE_SESSIONS_WARNING` initialization parameters are no longer needed and have been deprecated.

If you use named user licensing, Oracle Database can help you enforce this form of licensing. You can set a limit on the number of users created in the database. Once this limit is reached, you cannot create more users.

Note:

This mechanism assumes that each person accessing the database has a unique user name and that no people share a user name. Therefore, so that named user licensing can help you ensure compliance with your Oracle license agreement, do not allow multiple users to log in using the same user name.

To limit the number of users created in a database, set the `LICENSE_MAX_USERS` initialization parameter in the database initialization parameter file, as shown in the following example:

```
LICENSE_MAX_USERS = 200
```

## Managing Initialization Parameters Using a Server Parameter File

Initialization parameters for the Oracle Database have traditionally been stored in a text initialization parameter file. For better manageability, you can choose to maintain initialization parameters in a binary server parameter file that is persistent across database startup and shutdown. This section introduces the server parameter file, and explains how to manage initialization parameters using either method of storing the parameters. The following topics are contained in this section.

- What Is a Server Parameter File?
- Migrating to a Server Parameter File
- Creating a Server Parameter File
- The SPFILE Initialization Parameter
- Changing Initialization Parameter Values
- Clearing Initialization Parameter Values
- Exporting the Server Parameter File
- Backing Up the Server Parameter File
- Recovering a Lost or Damaged Server Parameter File
- Viewing Parameter Settings

### What Is a Server Parameter File?

A server parameter file can be thought of as a repository for initialization parameters that is maintained on the system running the Oracle Database server. It is, by design, a server-side initialization parameter file. Initialization parameters stored in a server parameter file are persistent, in that any changes made to the parameters while an instance is running can persist across instance shutdown and startup. This arrangement eliminates the need to manually update initialization parameters to make persistent any changes effected by `ALTER SYSTEM` statements. It also provides a basis for self-tuning by the Oracle Database server.

A server parameter file is initially built from a text initialization parameter file using the `CREATE SPFILE` statement. (It can also be created directly by the Database Configuration Assistant.) The server parameter file is a binary file that cannot be edited using a text editor. Oracle Database provides other interfaces for viewing and modifying parameter settings in a server parameter file.

Caution:

Although you can open the binary server parameter file with a text editor and view its text, do not manually edit it. Doing so will corrupt the file. You will not be able to start your instance, and if the instance is running, it could fail.

When you issue a `STARTUP` command with no `PFILE` clause, the Oracle instance searches an operating system–specific default location for a server parameter file from which to read initialization parameter settings. If no server parameter file is found, the instance searches for a text initialization parameter file. If a server parameter file exists but you want to override it with settings in a text initialization parameter file, you must specify the `PFILE` clause when issuing the `STARTUP` command. Instructions for starting an instance using a server parameter file are contained in ["Starting Up a Database"](start.md).

### Migrating to a Server Parameter File

If you are currently using a text initialization parameter file, then use the following steps to migrate to a server parameter file.

1. If the initialization parameter file is located on a client system, then transfer the file (for example, FTP) from the client system to the server system.
	Note:
	If you are migrating to a server parameter file in an Oracle Real Application Clusters environment, you must combine all of your instance-specific initialization parameter files into a single initialization parameter file. Instructions for doing this and other actions unique to using a server parameter file for instances that are part of an Oracle Real Application Clusters installation are discussed in [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/admin.htm#RACAD020) and in your platform-specific Oracle Real Application Clusters Installation Guide.
2. Create a server parameter file in the default location using the `CREATE SPFILE FROM PFILE` statement. See "Creating a Server Parameter File" for instructions.
	This statement reads the text initialization parameter file to create a server parameter file. The database does not have to be started to issue a `CREATE SPFILE` statement.
3. Start up or restart the instance.
	The instance finds the new SPFILE in the default location and starts up with it.

### Creating a Server Parameter File

You use the `CREATE SPFILE` statement to create a server parameter file. You must have the `SYSDBA` or the `SYSOPER` system privilege to execute this statement.

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

Oracle recommends that you allow the database to give the SPFILE the default name and store it in the default location. This eases administration of your database. For example, the `STARTUP` command assumes this default location to read the SPFILE.

Table 2-3 shows the default name and location for both the text initialization parameter file (PFILE) and server parameter file (SPFILE) for the UNIX, Linux, and Windows platforms, both with and without the presence of Oracle Automatic Storage Management (Oracle ASM). The table assumes that the SPFILE is a file. If it is a raw device, the default name could be a logical volume name or partition device name, and the default location could differ.

Table 2-3 PFILE and SPFILE Default Names and Locations on UNIX, LInux, and Windows

| Platform | PFILE Default Name | SPFILE Default Name | PFILE Default Location | SPFILE Default Location |
| --- | --- | --- | --- | --- |
| UNIX and Linux | `init` `ORACLE_SID``.ora` | `spfile` `ORACLE_SID``.ora` | OH `/dbs` or the same location as the data files <sup>Foot 1</sup> | Without Oracle ASM:  OH `/dbs` or the same location as the data files <sup>Footref 1</sup>  When Oracle ASM is present:  In the same disk group as the data files <sup>Foot 2</sup> |
| Windows | `init` `ORACLE_SID``.ora` | `spfile` `ORACLE_SID``.ora` | OH `\database` | Without Oracle ASM:  OH `\database`  When Oracle ASM is present:  In the same disk group as the data files <sup>Footref 2</sup> |

<sup>Footnote 1</sup> OH represents the Oracle home directory

<sup>Footnote 2</sup> Assumes database created with DBCA

Note:

Upon startup, the instance first searches for an SPFILE named `spfile` `ORACLE_SID`.`ora`, and if not found, searches for `spfile.ora`. Using `spfile.ora` enables all Real Application Cluster (Oracle RAC) instances to use the same server parameter file.

If neither SPFILE is found, the instance searches for the text initialization parameter file `init` `ORACLE_SID`.`ora`.

If you create an SPFILE in a location other than the default location, you must create in the default PFILE location a "stub" PFILE that points to the server parameter file. For more information, see ["Starting Up a Database"](start.md).

When you create the database with DBCA when Oracle ASM is present, DBCA places the SPFILE in an Oracle ASM disk group, and also causes this stub PFILE to be created.

### The SPFILE Initialization Parameter

The `SPFILE` initialization parameter contains the name of the current server parameter file. When the default server parameter file is used by the database—that is, you issue a `STARTUP` command and do not specify a `PFILE` parameter—the value of `SPFILE` is internally set by the server. The SQL\*Plus command `SHOW PARAMETERS SPFILE` (or any other method of querying the value of a parameter) displays the name of the server parameter file that is currently in use.

### Changing Initialization Parameter Values

The `ALTER SYSTEM` statement enables you to set, change, or restore to default the values of initialization parameters. If you are using a text initialization parameter file, the `ALTER SYSTEM` statement changes the value of a parameter only for the current instance, because there is no mechanism for automatically updating text initialization parameters on disk. You must update them manually to be passed to a future instance. Using a server parameter file overcomes this limitation.

There are two kinds of initialization parameters:

- Dynamic initialization parameters can be changed for the current Oracle Database instance. The changes take effect immediately.
- Static initialization parameters cannot be changed for the current instance. You must change these parameters in the text initialization file or server parameter file and then restart the database before changes take effect.

#### Setting or Changing Initialization Parameter Values

Use the `SET` clause of the `ALTER SYSTEM` statement to set or change initialization parameter values. The optional `SCOPE` clause specifies the scope of a change as described in the following table:

| SCOPE Clause | Description |
| --- | --- |
| `SCOPE = SPFILE` | The change is applied in the server parameter file only. The effect is as follows: - No change is made to the current instance. - For both dynamic and static parameters, the change is effective at the next startup and is persistent.  This is the only `SCOPE` specification allowed for static parameters. |
| `SCOPE = MEMORY` | The change is applied in memory only. The effect is as follows: - The change is made to the current instance and is effective immediately. - For dynamic parameters, the effect is immediate, but it is not persistent because the server parameter file is not updated.  For static parameters, this specification is not allowed. |
| `SCOPE = BOTH` | The change is applied in both the server parameter file and memory. The effect is as follows: - The change is made to the current instance and is effective immediately. - For dynamic parameters, the effect is persistent because the server parameter file is updated.  For static parameters, this specification is not allowed. |

It is an error to specify `SCOPE=SPFILE` or `SCOPE=BOTH` if the instance did not start up with a server parameter file. The default is `SCOPE=BOTH` if a server parameter file was used to start up the instance, and `MEMORY` if a text initialization parameter file was used to start up the instance.

For dynamic parameters, you can also specify the `DEFERRED` keyword. When specified, the change is effective only for future sessions.

When you specify `SCOPE` as `SPFILE` or `BOTH`, an optional `COMMENT` clause lets you associate a text string with the parameter update. The comment is written to the server parameter file.

The following statement changes the maximum number of failed login attempts before the connection is dropped. It includes a comment, and explicitly states that the change is to be made only in the server parameter file.

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

### Clearing Initialization Parameter Values

You can use the `ALTER` `SYSTEM` `RESET` command to clear (remove) the setting of any initialization parameter in the SPFILE that was used to start the instance. Neither `SCOPE` `=` `MEMORY` nor `SCOPE` `=` `BOTH` are allowed. The `SCOPE` `=` `SPFILE` clause is not required, but can be included.

You may want to clear a parameter in the SPFILE so that upon the next database startup a default value is used.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_2014.htm#SQLRF00902) for information about the `ALTER` `SYSTEM` command

### Exporting the Server Parameter File

You can use the `CREATE PFILE` statement to export a server parameter file (SPFILE) to a text initialization parameter file. Doing so might be necessary for several reasons:

- For diagnostic purposes, listing all of the parameter values currently used by an instance. This is analogous to the SQL\*Plus `SHOW PARAMETERS` command or selecting from the `V$PARAMETER` or `V$PARAMETER2` views.
- To modify the &spfile;server parameter file by first exporting it, editing the resulting text file, and then re-creating it using the `CREATE SPFILE` statement

The exported file can also be used to start up an instance using the `PFILE` clause.

You must have the `SYSDBA` or the `SYSOPER` system privilege to execute the `CREATE PFILE` statement. The exported file is created on the database server system. It contains any comments associated with the parameter in the same line as the parameter setting.

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

### Backing Up the Server Parameter File

You can create a backup of your server parameter file (SPFILE) by exporting it, as described in "Exporting the Server Parameter File". If the backup and recovery strategy for your database is implemented using Recovery Manager (RMAN), then you can use RMAN to create a backup of the SPFILE. The SPFILE is backed up automatically by RMAN when you back up your database, but RMAN also enables you to specifically create a backup of the currently active SPFILE.

See Also:

[Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmbckba.htm#BRADV89519)

### Recovering a Lost or Damaged Server Parameter File

If your server parameter file (SPFILE) becomes lost or corrupted, the current instance may fail, or the next attempt at starting the database instance may fail. There are several ways to recover the SPFILE:

- If the instance is running, issue the following command to re-create the SPFILE from the current values of initialization parameters in memory:
	```
	CREATE SPFILE FROM MEMORY;
	```
	This command creates the SPFILE with the default name and in the default location. You can also create the SPFILE with a new name or in a specified location. See "Creating a Server Parameter File" for examples.
- If you have a valid text initialization parameter file (PFILE), re-create the SPFILE from the PFILE with the following command:
	```
	CREATE SPFILE FROM PFILE;
	```
	This command assumes that the PFILE is in the default location and has the default name. See "Creating a Server Parameter File" for the command syntax to use when the PFILE is not in the default location or has a nondefault name.
- Restore the SPFILE from backup.
	See "Backing Up the Server Parameter File" for more information.
- If none of the previous methods are possible in your situation, perform these steps:
	1. Create a text initialization parameter file (PFILE) from the parameter value listings in the alert log.
		When an instance starts up, the initialization parameters used for startup are written to the alert log. You can copy and paste this section from the text version of the alert log (without XML tags) into a new PFILE.
		See ["Viewing the Alert Log"](diag.md) for more information.
		2. Create the SPFILE from the PFILE.
		See "Creating a Server Parameter File" for instructions.

Read/Write Errors During a Parameter Update

If an error occurs while reading or writing the server parameter file during a parameter update, the error is reported in the alert log and all subsequent parameter updates to the server parameter file are ignored. At this point, you can take one of the following actions:

- Shut down the instance, recover the server parameter file and described earlier in this section, and then restart the instance.
- Continue to run the database if you do not care that subsequent parameter updates will not be persistent.

### Viewing Parameter Settings

You can view parameter settings in several ways, as shown in the following table.

| Method | Description |
| --- | --- |
| `SHOW PARAMETERS` | This SQL\*Plus command displays the values of initialization parameters in effect for the current session. |
| `SHOW SPPARAMETERS` | This SQL\*Plus command displays the values of initialization parameters in the server parameter file (SPFILE). |
| `CREATE PFILE` | This SQL statement creates a text initialization parameter file (PFILE) from the SPFILE or from the current in-memory settings. You can then view the PFILE with any text editor. |
| `V$PARAMETER` | This view displays the values of initialization parameters in effect for the current session. |
| `V$PARAMETER2` | This view displays the values of initialization parameters in effect for the current session. It is easier to distinguish list parameter values in this view because each list parameter value appears in a separate row. |
| `V$SYSTEM_PARAMETER` | This view displays the values of initialization parameters in effect for the instance. A new session inherits parameter values from the instance-wide values. |
| `V$SYSTEM_PARAMETER2` | This view displays the values of initialization parameters in effect for the instance. A new session inherits parameter values from the instance-wide values. It is easier to distinguish list parameter values in this view because each list parameter value appears in a separate row. |
| `V$SPPARAMETER` | This view displays the current contents of the SPFILE. The view returns `FALSE` values in the `ISSPECIFIED` column if an SPFILE is not being used by the instance. |

See Also:

[Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_part.htm#REFRN003) for a complete description of views

## Managing Application Workloads with Database Services

This section contains:

- About Database Services
- Creating Database Services
- Database Service Data Dictionary Views

### About Database Services

Database services (services) are logical abstractions for managing workloads in Oracle Database. Services divide workloads into mutually disjoint groupings. Each service represents a workload with common attributes, service-level thresholds, and priorities. The grouping is based on attributes of work that might include the application function to be used, the priority of execution for the application function, the job class to be managed, or the data range used in the application function or job class. For example, the Oracle E-Business suite defines a service for each responsibility, such as general ledger, accounts receivable, order entry, and so on. When you configure database services, you give each service a unique global name, associated performance goals, and associated importance. The services are tightly integrated with Oracle Database and are maintained in the data dictionary.

Connection requests can include a database service name. Thus, middle-tier applications and client/server applications use a service by specifying the service as part of the connection in TNS connect data. If no service name is included and the Net Services file listener.ora designates a default service, the connection uses the default service.

Services enable you to configure a workload, administer it, enable and disable it, and measure the workload as a single entity. You can do this using standard tools such as the Database Configuration Assistant (DBCA), Net Configuration Assistant (NetCA), and Oracle Enterprise Manager. Enterprise Manager supports viewing and operating services as a whole, with drill down to the instance-level when needed.

In an Oracle Real Application Clusters (Oracle RAC) environment, a service can span one or more instances and facilitate workload balancing based on transaction performance. This provides end-to-end unattended recovery, rolling changes by workload, and full location transparency. Oracle RAC also enables you to manage several service features with Enterprise Manager, the DBCA, and the Server Control utility (`SRVCTL`).

Services also offer an extra dimension in performance tuning. Tuning by "service and SQL" can replace tuning by "session and SQL" in the majority of systems where all sessions are anonymous and shared. With services, workloads are visible and measurable. Resource consumption and waits are attributable by application. Additionally, resources assigned to services can be augmented when loads increase or decrease. This dynamic resource allocation enables a cost-effective solution for meeting demands as they occur. For example, services are measured automatically and the performance is compared to service-level thresholds. Performance violations are reported to Enterprise Manager, enabling the execution of automatic or scheduled solutions.

Several Oracle Database features support services. The Automatic Workload Repository (AWR) manages the performance of services. AWR records service performance, including execution times, wait classes, and resources consumed by service. AWR alerts warn when service response time thresholds are exceeded. The dynamic views report current service performance metrics with one hour of history. Each service has quality-of-service thresholds for response time and CPU consumption.

In addition, the Database Resource Manager can map services to consumer groups. Therefore, you can automatically manage the priority of one service relative to others. You can use consumer groups to define relative priority in terms of either ratios or resource consumption. For more information, see [Chapter 27, "Managing Resources with Oracle Database Resource Manager,"](dbrm.md) and specifically in ["Specifying Session-to–Consumer Group Mapping Rules"](dbrm.md).

You also can specify an edition attribute for a service. Editions make it possible to have two or more versions of the same objects in the database. When you specify an edition attribute for a service, all subsequent connections that specify the service use this edition as the initial session edition. This is described in more detail in ["Setting the Edition Attribute of a Database Service"](general.md).

Specifying an edition as a service attribute can make it easier to manage resource usage. For example, services associated with an edition can be placed on a separate instance in an Oracle RAC environment, and the Database Resource Manager can manage resources used by different editions by associating resource plans with the corresponding services.

Services describe applications, application functions, and data ranges as either functional services or data-dependent services. Functional services are the most common mapping of workloads. Sessions using a particular function are grouped together. In contrast, data-dependent routing routes sessions to services based on data keys. The mapping of work requests to services occurs in the object relational mapping layer for application servers and TP monitors. For example, in Oracle RAC, these ranges can be completely dynamic and based on demand because the database is shared.

You can also define preconnect application services in Oracle RAC databases. Preconnect services span instances to support a service in the event of a failure. The preconnect service supports TAF preconnect mode and is managed transparently when using Oracle RAC.

In addition to services to be used by applications, Oracle Database also supports two internal services: `SYS$BACKGROUND` is used by the background processes only and `SYS$USERS` is the default service for user sessions that are not associated with services.

Using services requires no changes to your application code. Client-side work can connect to a named service. Server-side work, such as Oracle Scheduler, parallel execution, and Oracle Streams Advanced Queuing, set the service name as part of the workload definition. Work requests executing under a service inherit the performance thresholds for the service and are measured as part of the service.

For Oracle Scheduler, you optionally assign a service when you create a job class. During execution, jobs are assigned to job classes, and job classes can run within services. Using services with job classes ensures that the work executed by the job scheduler is identified for workload management and performance tuning.

For parallel query and parallel DML, the query coordinator connects to a service just like any other client. The parallel query processes inherit the service for the duration of the execution. At the end of query execution, the parallel execution processes revert to the default service.

See Also:

- [Chapter 29, "Scheduling Jobs with Oracle Scheduler"](scheduse.md) for more information about the Oracle Scheduler
- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/hafeats.htm#RACAD841) for information about using services in an Oracle RAC environment
- [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/concepts.htm#NETAG002) for information on connecting to a service

### Creating Database Services

There are a few ways to create database services, depending on your database configuration.

To create a database service:

- If your single-instance database is being managed by Oracle Restart, use the `SRVCTL` utility to create the database service.
	```
	srvctl add service -d db_unique_name -s service_name
	```
- If your single-instance database is not being managed by Oracle Restart, do one of the following:
	- Append the desired service name to the `SERVICE_NAMES` parameter.
		- Call the `DBMS_SERVICE.CREATE_SERVICE` package procedure.
- (Optional) Define service attributes with Oracle Enterprise Manager or with `DBMS_SERVICE.MODIFY_SERVICE`.

See Also:

- [Chapter 4, "Configuring Automatic Restart of an Oracle Database"](restart.md) for information about Oracle Restart
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_serv.htm#ARPLS092) for information about the `DBMS_SERVICE` package
- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/hafeats.htm#RACAD076) for information about creating a service in an Oracle RAC environment.

### Database Service Data Dictionary Views

You can find service information in the following service-specific views:

- `DBA_SERVICES`
- `ALL_SERVICES` or `V$SERVICES`
- `V$ACTIVE_SERVICES`
- `V$SERVICE_STATS`
- `V$SERVICE_EVENT`
- `V$SERVICE_WAIT_CLASSES`
- `V$SERV_MOD_ACT_STATS`
- `V$SERVICE_METRICS`
- `V$SERVICE_METRICS_HISTORY`

The following additional views also contain some information about services:

- `V$SESSION`
- `V$ACTIVE_SESSION_HISTORY`
- `DBA_RSRC_GROUP_MAPPINGS`
- `DBA_SCHEDULER_JOB_CLASSES`
- `DBA_THRESHOLDS`

See Also:

[Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm) for detailed information about these views

## Considerations After Creating a Database

After you create a database as described in "Creating a Database with DBCA" or "Creating a Database with the CREATE DATABASE Statement", the instance is left running, and the database is open and available for normal database use. You may want to perform other actions, some of which are discussed in this section.

### Some Security Considerations

In this release of Oracle Database, several enhancements were made to ensure the security your database. You can find security guidelines for this release in [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/guidelines.htm#DBSEG009). Oracle recommends that you read these guidelines and configure your database accordingly.

After the database is created, you can configure it to take advantage of Oracle Identity Management. For information on how to do this, see [Oracle Database Enterprise User Security Administrator's Guide.](https://docs.oracle.com/cd/E11882_01/network.112/e10744/toc.htm)

A newly created database has at least three user accounts that are important for administering your database: `SYS`, `SYSTEM`, and `SYSMAN`. Additional administrative accounts are provided that should be used only by authorized users. To protect these accounts from being used by unauthorized users familiar with their Oracle-supplied passwords, these accounts are initially locked with their passwords expired. As the database administrator, you are responsible for the unlocking and resetting of these accounts.

See [Oracle Database 2 Day + Security Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10575/tdpsg_user_accounts.htm#TDPSG20030) for a complete list of predefined user accounts created with each new Oracle Database installation.

Caution:

To prevent unauthorized access and protect the integrity of your database, it is important that new passwords for user accounts `SYS` and `SYSTEM` be specified when the database is created. This is accomplished by specifying the following `CREATE DATABASE` clauses when manually creating you database, or by using DBCA to create the database:
- `USER SYS IDENTIFIED BY`
- `USER SYSTEM IDENTIFIED BY`

See Also:

- ["Administrative User Accounts"](dba.md) for more information about the users `SYS` and `SYSTEM`
- [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/users.htm#DBSEG002) to learn how to add new users and change passwords
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_4003.htm#SQLRF01103) for the syntax of the `ALTER USER` statement used for unlocking user accounts

### Enabling Transparent Data Encryption

Transparent data encryption is a feature that enables encryption of individual database columns before storing them in the data file, or enables encryption of entire tablespaces. If users attempt to circumvent the database access control mechanisms by looking inside data files directly with operating system tools, transparent data encryption prevents such users from viewing sensitive information.

Users who have the `CREATE TABLE` privilege can choose one or more columns in a table to be encrypted. The data is encrypted in the data files and in the audit logs (if audit is turned on). Database users with appropriate privileges can view the data in unencrypted format. For information on enabling transparent data encryption, see [Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/asotrans.htm#ASOAG9522).

### Creating a Secure External Password Store

For large-scale deployments where applications use password credentials to connect to databases, it is possible to store such credentials in a client-side Oracle wallet. An Oracle wallet is a secure software container that is used to store authentication and signing credentials.

Storing database password credentials in a client-side Oracle wallet eliminates the need to embed usernames and passwords in application code, batch jobs, or scripts. This reduces the risk of exposing passwords in the clear in scripts and application code, and simplifies maintenance because you need not change your code each time usernames and passwords change. In addition, not having to change application code also makes it easier to enforce password management policies for these user accounts.

When you configure a client to use the external password store, applications can use the following syntax to connect to databases that use password authentication:

```
CONNECT /@database_alias
```

Note that you need not specify database login credentials in this `CONNECT` statement. Instead your system looks for database login credentials in the client wallet.

### Installing the Oracle Database Sample Schemas

The Oracle Database distribution media includes various SQL files that let you experiment with the system, learn SQL, or create additional tables, views, or synonyms.

Oracle Database includes sample schemas that help you to become familiar with Oracle Database functionality. All Oracle Database documentation and training materials are being converted to the Sample Schemas environment as those materials are updated.

The Sample Schemas can be installed automatically by the Database Configuration Assistant, or you can install them manually. The schemas and installation instructions are described in detail in [Oracle Database Sample Schemas](https://docs.oracle.com/cd/E11882_01/server.112/e10831/toc.htm).

## Cloning a Database with CloneDB

This section contains the following topics:

- About Cloning a Database with CloneDB
- Cloning a Database with CloneDB
- After Cloning a Database with CloneDB

### About Cloning a Database with CloneDB

It is often necessary to clone a production database for testing purposes or other purposes. Common reasons to clone a production database include the following:

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

- The CloneDB feature is supported starting with Oracle Database 11g Release 2 (11.2.0.3).
- The CloneDB feature is not intended for performance testing.

### Cloning a Database with CloneDB

Before cloning a database, the following prerequisites must be met:

- Each CloneDB database must use Direct NFS Client, and the backup of the production database must be located on an NFS volume.
	Direct NFS Client enables an Oracle database to access network attached storage (NAS) devices directly, rather than using the operating system kernel NFS client. This CloneDB database feature is available on platforms that support Direct NFS Client.
	See [Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=CWGEN) for your operating system for information about Direct NFS Client.
- At least 2 MB of additional System Global Area (SGA) memory is required to track the modified blocks in a CloneDB database.
	See [Chapter 6, "Managing Memory"](memory.md).
- Storage for the database backup and for the changed blocks in each CloneDB database is required.
	The storage required for the database backup depends on the method used to perform the backup. A single full RMAN backup requires the most storage. Storage snapshots carried out using the features of a storage appliance adhere to the requirements of the storage appliance. A single backup can support multiple CloneDB databases.
	The amount of storage required for each CloneDB database depends on the write activity in that database. Every block that is modified requires an available block of storage. Therefore, the total storage requirement depends on the number of blocks modified in the CloneDB database over time.

This section describes the steps required to create one CloneDB database and uses these sample databases and directories:

- The Oracle home for the production database `PROD1` is /u01/prod1/oracle.
- The files for the database backup are in /u02/oracle/backup/prod1.
- The Oracle home for CloneDB database `CLONE1` is /u03/clone1/oracle.

To clone a database with CloneDB:

To create additional CloneDB databases of the production database, repeat Steps [^2] - [^3] for each CloneDB database.

### After Cloning a Database with CloneDB

After a CloneDB database is created, you can use it in almost any way you use your production database. Initially, a CloneDB database uses a minimal amount of storage for each data file. Changes to rows in a CloneDB database cause storage space to be allocated on demand.

You can use the same backup files to create multiple CloneDB databases. This backup can be taken either by RMAN or by storage level snapshots. If you have a storage level snapshot taken on a data file, then you can replace the RMAN backup file names with the storage snapshot names.

You can use the `V$CLONEDFILE` view to show information about the each data file in the CloneDB database. This information includes the data file name in the backup, the corresponding data file name in the CloneDB database, the number of blocks read from the backup file, and the number of requests issued against the backup file.

Because CloneDB databases use the backup files as their backend storage, the backup files must be available to each CloneDB database for it to run. If the backup files become unavailable, then the CloneDB databases return errors.

When your use of a CloneDB database is complete, you can destroy the CloneDB database environment. You can delete all of the files in the CloneDB database environment without affecting the production database environment or the backup environment.

See Also:

[Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1083.htm#REFRN30713) for more information about the `V$CLONEDFILE` view

## Dropping a Database

Dropping a database involves removing its data files, redo log files, control files, and initialization parameter files.

WARNING:

Dropping a database deletes all data in the database.

To drop a database:

- Submit the following statement:
	```
	DROP DATABASE;
	```

The `DROP` `DATABASE` statement first deletes all control files and all other database files listed in the control file. It then shuts down the database instance.

To use the `DROP` `DATABASE` statement successfully, the database must be mounted in exclusive and restricted mode.

The `DROP` `DATABASE` statement has no effect on archived log files, nor does it have any effect on copies or backups of the database. It is best to use RMAN to delete such files. If the database is on raw disks, the actual raw disk special files are not deleted.

If you used the Database Configuration Assistant to create your database, you can use that tool to delete (drop) your database and remove the files.

See Also:

["Altering Database Availability"](start.md)

## Database Data Dictionary Views

In addition to the views listed previously in "Viewing Parameter Settings", you can view information about your database content and structure using the following views:

| View | Description |
| --- | --- |
| `DATABASE_PROPERTIES` | Displays permanent database properties |
| `GLOBAL_NAME` | Displays the global database name |
| `V$DATABASE` | Contains database information from the control file |

[^1]: Create a backup of your production database. You have the following backup options:

- An online backup
	If you perform an online backup, then ensure that your production database is in `ARCHIVELOG` mode and that all of the necessary archived redo log files are saved and accessible to the CloneDB database environment.
- A full offline backup
	If you perform a full offline backup, then ensure that the backup files are accessible to the CloneDB database environment.
- A backup that copies the database files
	If you specify `BACKUP` `AS` `COPY` in RMAN, then RMAN copies each file as an image copy, which is a bit-for-bit copy of a database file created on disk. Image copies are identical to copies created with operating system commands such as `cp` on Linux or `COPY` on Windows, but are recorded in the RMAN repository and so are usable by RMAN. You can use RMAN to make image copies while the database is open. Ensure that the copied database files are accessible to the CloneDB database environment.

See [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/toc.htm) for information about backing up a database.

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
	For an Oracle Database 11g Release 2 (11.2.0.4) or later database, the script is in the $ORACLE\_HOME/rdbms/install directory.
	For an Oracle Database 11g Release 2 (11.2.0.3) database, you can download the script from the My Oracle Support Note 1210656.1 ("Clone your dNFS Production Database for Testing") at `https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=1210656.1`.
	The clonedb.pl Perl script has the following syntax:
	```
	perl clonedb.pl prod_db_pfile [sql_script1] [sql_script2]
	```
	Specify the following options:
	`prod_db_pfile` - Specify the full path of the production database's PFILE.
	`sql_script1` - Specify a name for the first SQL script generated by clonedb.pl. The default is crtdb.sql.
	`sql_script2` - Specify a name for the second SQL script generated by clonedb.pl. The default is dbren.sql.
	The clonedb.pl script copies the production database's PFILE to the CloneDB database's directory. It also creates two SQL scripts that you will use to create the CloneDB database.
3. Check the two SQL scripts that were generated by the clonedb.pl Perl script, and make changes if necessary.
4. Modify the initialization parameters for the CloneDB database environment, and save the file.
	Change any initialization parameter that is specific to the CloneDB database environment, such as parameters that control SGA size, PGA target, the number of CPUs, and so on. The `CLONEDB` parameter must be set to `TRUE`, and the initialization parameter file includes this parameter. See [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm) for information about initialization parameters.
5. In SQL\*Plus, connect to the CloneDB database with `SYSDBA` administrative privilege.
6. Run the SQL scripts generated by the clonedb.pl Perl script.
	For example, if the scripts use the default names, then run the following scripts at the SQL prompt:
	```
	crtdb.sql
	dbren.sql
	```

To create a SQL script manually, complete the following steps:

1. Connect to the database with `SYSDBA` or `SYSBACKUP` administrative privilege.
	See ["Connecting to the Database with SQL\*Plus"](dba.md).
2. Generate a backup control file script from your production database by completing the following steps:
	Run the following SQL statement:
	```
	ALTER DATABASE BACKUP CONTROLFILE TO TRACE;
	```
	This statement generates a trace file that contains the SQL statements that create the control file. The trace file containing the `CREATE` `CONTROLFILE` statement is stored in a directory determined by the `DIAGNOSTIC_DEST` initialization parameter. Check the database alert log for the name and location of this trace file.
3. Open the trace file generated in Step b, and copy the `STARTUP` `NOMOUNT` and `CREATE` `CONTROLFILE` statements in the trace file to a new SQL script.
4. Edit the new SQL script you created in Step c in the following ways:
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
	For example, copy the text initialization parameter file from /u01/prod1/oracle/dbs to /u03/clone1/oracle/dbs. The name and location of the file must match the name and location specified in the `STARTUP` `NOMOUNT` command in the modified SQL script. In the example in Step d, the file is /u03/clone1/oracle/dbs/clone1.ora.
7. Modify the initialization parameters for the CloneDB database environment, and save the file.
	Add the `CLONEDB` parameter, and ensure that this parameter is set to `TRUE`. Change any other initialization parameter that is specific to the CloneDB database environment, such as parameters that control SGA size, PGA target, the number of CPUs, and so on. See [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm) for information about initialization parameters.
8. In SQL\*Plus, connect to the CloneDB database with `SYSDBA` administrative privilege.
9. Run the SQL script you saved in Step e.
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
	See [Oracle Database PL/SQL Packages and Types Reference](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=ARPLS74814) for more information about the `DBMS_DNFS` package.

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