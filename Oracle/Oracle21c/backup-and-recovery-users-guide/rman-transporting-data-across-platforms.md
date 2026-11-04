---
title: "Backup and Recovery User's Guide"
book: "Database Backup and Recovery User's Guide"
doc_id: F31836-11
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/bradv/rman-transporting-data-across-platforms.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-users-guide
---

Data can be transported across platforms by using image copies or backup sets.

You can use RMAN to transport tablespaces across platforms with different endian formats. You can also use RMAN to transport an entire database to a different platform so long as the two platforms have the same endian format.

### 28.1 About Cross-Platform Data Transport

Cross-platform transportable tablespace is a variation of ordinary transportable tablespace. All of the restrictions that apply to transportable tablespaces apply here also, such as the need to ensure that all of the objects being transported are completely contained within the set of tablespaces being transported. Cross-platform transportable tablespace can be performed between platforms that have the same, or different, endian format.

Cross-platform transportable database is not the same thing as transportable tablespace. In this case you are copying an entire database, including the `SYSTEM` tablespace from one platform to another. Containment checks are irrelevant, and because the `SYSTEM` tablespace is being copied, no export/import step is required. Cross-platform transportable database can only be performed between platforms that have the same endian format.

#### 28.1.1 Purpose of Cross-Platform Data Transport

You can transport tablespaces in a database that runs on one platform into a database that runs on a different platform. Typical uses of cross-platform transportable tablespaces include the following:

- Publishing structured data as transportable tablespaces for distribution to customers, who can convert the tablespaces for integration into their existing databases regardless of platform
- Moving data from a large data warehouse server to data marts on smaller computers such as Linux-based workstations or servers
- Sharing read-only tablespaces across a heterogeneous cluster in which all hosts share the same endian format
- Migrating tablespaces across platforms with minimal application downtime

A full discussion of transportable tablespaces, their uses, and the different techniques for creating and using them is found in [Oracle Database Administrator's Guide.](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=ADMIN01101)

You can also use RMAN to transport an entire database from one platform to another. For example, business requirements demand that you run your databases on less expensive servers that use a different platform. In this case, you can use RMAN to transport the entire database rather than re-create it and use import utilities or transportable tablespaces to repopulate the data.

You can convert a database on the destination host or source host. Reasons for converting on the destination host include:

- Avoiding performance overhead on the source host due to the conversion process
- Distributing a database from one source system to multiple recipients on several different platforms
- Evaluating a migration path for a new platform

#### 28.1.2 Methods of Transporting Data Across Platforms

RMAN enables you to transport data files, tablespaces, or an entire database from one platform to another. When you transport an entire database to a different platform, the destination platform must have the same endian format as the source platform.

Use one of the following methods to transport data across platforms:

- Transport data using image copies
- Transport data using backup sets
	See Also:
	- " Overview of Cross-Platform Data Transport Using Image Copies "
	- " Overview of Cross-Platform Data Transport Using Backup Sets "

#### 28.1.3 Platforms that Support Cross-Platform Data Transport

The Oracle Database maintains a list of internal names for each platform that supports cross-platform data transport. These names are stored in the `V$TRANSPORTABLE_PLATFORM` view. Use this view to determine the internal name of the [source platform](glossary.md) or [destination platform](glossary.md). While transporting data across platforms, you may need to specify the exact name of the source or destination platform. Any platform names specified as a parameter of the `CONVERT` or `BACKUP` command must be entered exactly as shown in the `V$TRANSPORTABLE_PLATFORM` view.

Use the following query to obtain the platform name of the connected database:

```
SELECT PLATFORM_NAME
    FROM V$TRANSPORTABLE_PLATFORM
    WHERE PLATFORM_ID =
       ( SELECT PLATFORM_ID FROM V$DATABASE );
```

Use the following query to obtain the name of the Linux platform:

```
SELECT PLATFORM_ID, PLATFORM_NAME, ENDIAN_FORMAT
FROM V$TRANSPORTABLE_PLATFORM
WHERE UPPER(PLATFORM_NAME) LIKE '%LINUX%';
```

### 28.2 Overview of Cross-Platform Data Transport Using Image Copies

RMAN enables you to use image copies to transport tablespaces, data files, or an entire database. You use the RMAN `CONVERT` command to perform cross-platform transport with image copies. Tablespace transport is sometimes performed by individually transporting the data files that store the tablespace data. However, it is not possible to transport a single data file that is part of a tablespace that consists of multiple data files.

You must use the RMAN `CONVERT` command in a transportable tablespace operation when the [source platform](glossary.md) is different from the [destination platform](glossary.md) and the endian formats are different. If you are converting part of the database between platforms that have the same endian format, you can use operating system methods to copy the files from the source to the destination. If you are converting an entire, same endian database, any data files with undo information must be converted. You cannot copy these files directly from the source to the destination platform.

#### 28.2.1 Overview of Tablespace and Data File Conversion Using Image Copies

You can perform tablespace conversion with the RMAN `CONVERT` `TABLESPACE` command on the source host, but not on the destination host. The `CONVERT TABLESPACE` command does not perform in-place conversion of data files. Rather, the command produces output files in the correct format for use on the destination platform. The command does not alter the contents of data files in the [source database](glossary.md).

You can use the `CONVERT` `DATAFILE` command to convert files. Typically, the `CONVERT DATAFILE` command is used on the destination host and the `CONVERT TABLESPACE` command is used on the source host. When you use the `CONVERT DATAFILE` command on the source host, ensure that data files are cleanly offline or the tablespaces containing those data files are read-only. The Data Pump Export utility generates an [export dump file](glossary.md) that, with data files manually copied to the destination host, can be imported into the [destination database](glossary.md). Until the Data Pump export dump file is imported into the destination database, the data files are not associated with a tablespace name in the database. In this case, RMAN cannot translate the tablespace name into a list of data files. Therefore, you must use `CONVERT` `DATAFILE` and identify the data files by file name.

Note:

Using `CONVERT TABLESPACE` or `CONVERT DATAFILE` is only one step in using cross-platform transportable tablespaces. Read the discussion of transportable tablespaces in [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=ADMIN01101) in its entirety before attempting to follow the procedures in this chapter.

See Also:

The following sections describe how to perform cross-platform transport of tablespaces and data files using image copies:

- " Performing Cross-Platform Tablespace Conversion with Image Copies "
- " Performing Cross-Platform Data File Conversion with Image Copies "

#### 28.2.2 Overview of Database Conversion Using Image Copies

To convert a whole database to a different platform, both platforms must use the same endian format. The RMAN `CONVERT` `DATABASE` command automates the movement of an entire database from a source platform to a destination platform. The transported database contains the same data as the [source database](glossary.md) and also has, with a few exceptions, the same settings as the source database.

Files automatically transported to the destination platform include:

- Data files that belong to permanent tablespaces
	Unlike transporting tablespaces across platforms, transporting entire databases requires that certain types of blocks, such as blocks in undo segments, be reformatted to ensure compatibility with the destination platform. Even though the endian formats for the source and destination platforms are the same, certain types of files must undergo a conversion process. See " Checking the Database Before Cross-Platform Database Conversion " for details about the types of files that need conversion.
- Initialization parameter file or server parameter file
	If the database uses a text-based initialization parameter file, then RMAN transports it. If the database uses a server parameter file, then RMAN generates an initialization parameter file based on the server parameter file, transports it and creates a new server parameter file at the destination based on the settings in the initialization parameter file.
	Usually, some parameters in the initialization parameter file require manual updating for the new database. For example, you may change the `DB_NAME` and parameters such as `CONTROL_FILES` that indicate the locations of files on the destination host.

You can convert the format of the data files either on the source platform or on the destination platform. The `CONVERT DATABASE ON DESTINATION PLATFORM` command does not convert the format of data files. Rather, it generates scripts that you can run manually to perform the conversion. The `CONVERT SCRIPT` parameter creates a [convert script](glossary.md) that you can manually execute at the destination host to convert data file copies in batch mode. The `TRANSPORT SCRIPT` parameter generates a [transport script](glossary.md) that contains SQL statements to create the new database on the destination platform.

See Also:

My Oracle Support Note 1079563.1, "RMAN DUPLICATE/RESTORE/RECOVER Mixed Platform Support" for the following information:

- List of platform combinations that do not require the `CONVERT DATABASE` command
- Prerequisites for the source database and destination databases

See Also:

[`http://www.oracle.com/goto/maa`](http://www.oracle.com/goto/maa) for best practices on using cross-platform transportable tablespace and database procedures as part of data migration tasks

See Also:

The following sections describe how to perform cross-platform transport of a database using image copies:

### 28.3 Performing Cross-Platform Tablespace Conversion with Image Copies

You can transport tablespaces across platforms by performing the required conversion on the source database.

See the list of `CONVERT` command prerequisites described in [Oracle Database Backup and Recovery Reference.](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF192) Meet all these prerequisites before doing the steps in this section.

For purposes of illustration, assume that you must transport tablespaces from the source database `prod_source`, which runs on a Sun Solaris host. You plan to transport them to the destination database `prod_dest` running on a Linux PC. You plan to store the converted data files in the temporary directory `/tmp/transport_linux/` on the source host.

See Also:

" Overview of Tablespace and Data File Conversion Using Image Copies "

To perform cross-platform tablespace conversion with image copies:

1. Start SQL\*Plus and connect to the source database `prod_source` with administrator privileges.
2. Query the name for the destination platform in the `V$TRANSPORTABLE_PLATFORM` view.
	The `PLATFORM_NAME ` for Linux on a PC is `Linux IA (64-bit)`.
	See Also:
	" Platforms that Support Cross-Platform Data Transport " for information about determining the platform name
3. Check if the tablespaces to be transported are self-contained by executing the `DBMS_TTS.TRANSPORT_SET_CHECK` procedure. If the `TRANSPORT_SET_VIOLATIONS` view contains rows corresponding to the specified tablespaces, then you must resolve the dependencies before proceeding with the conversion.
	For tablespaces in a pluggable databae (PDB), you must change the container to the PDB by using the `ALTER SESSION SET CONTAINER` command.
	See Also:
	[Example 21-1](performing-rman-tspitr.md) for information about executing the `DBMS_TTS.TRANSPORT_SET_CHECK` procedure
4. Place the tablespaces to be transported in read-only mode. For example, enter:
	```
	ALTER TABLESPACE finance READ ONLY;
	ALTER TABLESPACE hr READ ONLY;
	```
5. Choose a method for naming the output files.
	See Also:
	" About Renaming Output Files During RMAN Cross-Platform Data File Conversion "
6. Start RMAN and connect as `TARGET` to the source database (not the destination database) and as a common user with the `SYSDBA` or `SYSBACKUP` privilege. If the tablespace is in a PDB, connect to the PDB as a common user or local user with the `SYSDBA` or `SYSBACKUP` privilege.
	The following example connects to a PDB as the `SYS` user:
	```
	RMAN> connect target "sys@my_pdb as sysdba"
	target database Password: 
	connected to target database: DB203:MY_PDB (DBID=1139070871)
	```
7. Run the `CONVERT TABLESPACE` command to convert the data files into the endian format of the destination host.
	In the following example, the `FORMAT` argument controls the name and location of the converted data files:
	```
	RMAN> CONVERT TABLESPACE finance, hr
	2>   TO PLATFORM 'Linux IA (64-bit)'
	3>   FORMAT '/tmp/transport_linux/%U';
	```
	The result is a set of converted data files in the `/tmp/transport_linux/ ` directory, with data in the correct endian format for the Linux IA (64-bit) platform.
	See Also:
	[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF192) for the full semantics of the `CONVERT` command
8. Follow the rest of the general outline for transporting tablespaces:
	1. Use the Oracle Data Pump Export utility to create the export dump file on the source host.
		2. Move the converted data files and the export dump file from the source host to the desired directories on the destination host.
		3. Plug the tablespace in to the new database with the DataPump Import utility.
		4. If applicable, place the transported tablespaces into read/write mode.
	See Also:
	[Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=ADMIN11394) for information about using transportable tablespaces

### 28.4 Performing Cross-Platform Data File Conversion with Image Copies

You can use the `CONVERT DATAFILE` command to perform cross-platform conversion of tablespaces with image copies.

#### 28.4.1 About Renaming Output Files During RMAN Cross-Platform Data File Conversion

Data file conversion necessitates that you choose a technique for naming the output files. You must use the `FORMAT` or `DB_FILE_NAME_CONVERT` arguments to the `CONVERT` command to control the naming of output files. The rules are listed in order of precedence:

1. Any file that matches any pattern provided in the `DB_FILE_NAME_CONVERT` clause is named based upon this pattern.
2. If you specify a `FORMAT` clause, then any file not named based on the pattern provided in the `DB_FILE_NAME_CONVERT` clause is named based on the `FORMAT` pattern.

Note:

You cannot use the `DB_FILE_NAME_CONVERT` clause to generate output file names for the `CONVERT` command when both the source and destination files are Oracle Managed Files.

If the source and destination platforms differ, then you must specify the `FROM PLATFORM` parameter. View platform names by querying the `V$TRANSPORTABLE_PLATFORM`. The `FROM PLATFORM` value must match the format of the data files to be converted to avoid an error. If you do not specify `FROM PLATFORM`, then this parameter defaults to the value of the destination platform.

See Also:

" Platforms that Support Cross-Platform Data Transport " for information about determining the platform name

#### 28.4.2 Performing Tablespace Transportation on the Destination Host Using RMAN CONVERT DATAFILE

Tablespaces can be transported by using the `CONVERT DATAFILE` on the destination database, to convert the data files that are associated with the tablespace.

This section explains how to use the `CONVERT DATAFILE` command. The section assumes that you intend to transport tablespaces `finance` (data files `fin/fin01.dbf` and `fin/fin02.dbf`) and `hr` (data files `hr/hr01.dbf` and `hr/hr02.dbf`) from a source database named `prod_source`. The database runs on a Sun Solaris host. You plan to transport these tablespaces into a destination database named `prod_dest`, which runs on a Linux PC. You plan to perform conversion on the destination host.

When the data files are plugged in to the destination database, you plan to store them in `/orahome/dbs` and preserve the current directory structure. That is, data files for the `hr` tablespace are stored in the `/orahome/dbs/hr` subdirectory, and data files for the `finance` tablespace are stored in the `/orahome/dbs/fin` directory.

See Also:

" Overview of Tablespace and Data File Conversion Using Image Copies "

To perform cross-platform data file conversion with image copies:

1. See the list of `CONVERT` command prerequisites described in [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF192). Meet these prerequisites before performing the steps in this section.
2. Start SQL\*Plus and connect to the source database `prod_source` with administrator privileges.
3. Query the name for the source platform in `V$TRANSPORTABLE_PLATFORM`.
	For this scenario, assume that the `PLATFORM_NAME` for the source host is `Solaris[tm] OE (64-bit)`.
	See Also:
	" Platforms that Support Cross-Platform Data Transport " for information about determining the platform name
4. Identify the tablespaces to be transported from the source database and place them in read-only mode. For tablespaces in a pluggable databae (PDB), you must change the container to the PDB by using the `ALTER SESSION SET                             CONTAINER` command.
	For example, enter the following SQL statements to place `finance` and `hr` in read-only mode:
	```
	ALTER TABLESPACE finance READ ONLY;
	ALTER TABLESPACE hr READ ONLY;
	```
5. On the source host, use Data Pump Export to create the export dump file.
	In this example, the dump file is named `expdat.dmp`.
6. Make the export dump file and the data files to be transported available to the destination host.
	You can use NFS to make the dump file and current database files (not copies) accessible. Alternatively, you can use an operating system utility to copy these files to the destination host.
	In this example, you store the files in the `/tmp/transport_solaris/` directory of the destination host. You preserve the subdirectory structure from the original location of the files; that is, the data files are stored as:
	- `/tmp/transport_solaris/fin/fin01.dbf`
		- `/tmp/transport_solaris/fin/fin02.dbf`
		- `/tmp/transport_solaris/hr/hr01.dbf`
		- `/tmp/transport_solaris/hr/hr02.dbf`
7. Start RMAN and connect to the destination database (not the source database) as `TARGET`, as a common user with the `SYSDBA` or `SYSBACKUP` privilege. If the tablespaces must be transported into a PDB, connect as `TARGET` to the PDB, as a common user with the `SYSDBA` or `SYSBACKUP` privilege.
	For example, the following command connects to the target database `prod_dest` using the `sbu` user who is granted the `SYSBACKUP` privilege:
	```
	% rman
	RMAN> CONNECT TARGET "sbu@prod_dest AS SYSBACKUP";
	```
8. Execute the `CONVERT DATAFILE` command to convert the data files into the endian format of the destination host.
	In this example, you use `DB_FILE_NAME_CONVERT` to control the name and location of the converted data files. You also specify the `FROM` `PLATFORM` clause.
	```
	RMAN> CONVERT DATAFILE
	2>   '/tmp/transport_solaris/fin/fin01.dbf',
	3>   '/tmp/transport_solaris/fin/fin02.dbf',
	4>   '/tmp/transport_solaris/hr/hr01.dbf',
	5>   '/tmp/transport_solaris/hr/hr02.dbf'
	6>   DB_FILE_NAME_CONVERT
	7>     '/tmp/transport_solaris/fin','/orahome/dbs/fin',
	8>     '/tmp/transport_solaris/hr','/orahome/dbs/hr'
	9>   FROM PLATFORM 'Solaris[tm] OE (64-bit)';
	```
	The result is a set of converted data files in the `/orahome/dbs/` directory that are named as follows:
	- `/orahome/dbs/fin/fin01.dbf`
		- `/orahome/dbs/fin/fin02.dbf`
		- `/orahome/dbs/hr/hr01.dbf`
		- `/orahome/dbs/hr/hr02.dbf`
9. Follow the rest of the general outline for transporting tablespaces:
	1. Plug the tablespace in to the new database with the DataPump Import utility.
		2. If applicable, place the transported tablespaces into read-only mode.

See Also:

- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF192) for the syntax and semantics of the `CONVERT` command
- [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=ADMIN11394) for information about transportable tablespaces

### 28.5 Performing Cross-Platform Database Conversion with Image Copies

When you perform cross-platform database conversion with image copies, you can convert the data files on either the source host or the destination host.

#### 28.5.1 Checking the Database Before Cross-Platform Database Conversion

Use the RMAN `CONVERT DATABASE` command to automate the copying of an entire database from one platform to another.

Prerequisites:

- Before converting the database, confirm that you meet all the `CONVERT DATABASE` command prerequisites described in [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF192).
- Both the source and destination platform must share the same endian format. For example, you can transport a database from Microsoft Windows to Linux for x86 (both little-endian), or from HP-UX to AIX (both big-endian), but not from HP-UX to Linux for x86 (big-endian to little-endian).
	Note:
	If you cannot use the `CONVERT DATABASE` command because the platforms do not share endian formats, then you can create a new database on the destination platform and then use cross-platform transportable tablespace to copy your data.
- When you transport entire databases, note that certain files require RMAN conversion to ensure compatibility with the destination platform. Even though the endian formats for the source and destination platform are the same, these files cannot be simply copied from the source to the destination system. The following kinds of files require RMAN conversion:
	- Any file containing undo segments
		- Any file containing automatic segment space management (ASSM) segment headers that is being transported to or from the HP Tru64 platform
		Note:
		When converting to or from Tru64 UNIX platform, even if the databases use the same endian format, you must use the `CONVERT` command to convert data files with automatic segment space management (ASSM) headers. See My Oracle Support Note 732053.1 for information about identifying data files that contain undo data or ASSM headers.
- The `CONVERT DATABASE` command, by default, processes all data files in the database using RMAN conversion. The RMAN conversion copies the files from one location to another, even when it does not make any changes to the file. If you have other preferred means to copy those files that do not require RMAN conversion, you can use the `SKIP UNNECESSARY DATAFILES` option of the `CONVERT               DATABASE` command. If you select this option, then the `CONVERT               DATABASE` command only processes the files that require conversion. All other files must either be made accessible to the user or copied from the source to the destination database.
	Whether the data file conversion is performed at the source or destination host, you must copy the files while the source database is open in read-only mode.

To check the database before cross-platform conversion:

1. On the source database, start a SQL\*Plus session as a common user with the `SYSDBA` or `SYSBACKUP` privilege.
2. Open the database in read-only mode.
	```
	SHUTDOWN IMMEDIATE
	STARTUP MOUNT
	ALTER DATABASE OPEN READ ONLY;
	```
3. Ensure that server output is on in SQL\*Plus.
	For example, enter the following SQL\*Plus command:
	```
	SET SERVEROUTPUT ON
	```
4. Execute the `DBMS_TDB.CHECK_DB` function.
	This check ensures that no conditions prevent the transport of the database, such as incorrect compatibility settings, in-doubt or active transactions, or incompatible endian formats between the source platform and destination platform.
	You can call `CHECK_DB` without arguments to see if a condition at the source database prevents transport. You can also call this function with the arguments shown in Table 28-1.
	Table 28-1 CHECK\_DB Function Parameters
	| Parameter | Description |
	| --- | --- |
	| `target_platform_name` | The name of the destination platform as it appears in the [`V$DB_TRANSPORTABLE_PLATFORM`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=REFRN30376) view.  This parameter is optional, but is required when the `skip_option` parameter is used. If omitted, it is assumed that the destination platform is compatible with the source platform, and only the conditions not related to platform compatibility are tested. |
	| `skip_option` | Specifies which, if any, parts of the database to skip when checking whether the database can be transported. Supported values (of type `NUMBER`) are:  - `SKIP_NONE` (or `0`), which checks all tablespaces - `SKIP_OFFLINE` (or `2`), which skips checking data files in offline tablespaces - `SKIP_READONLY` (or `3`), which skips checking data files in read-only tablespaces |
	The following example illustrates executing `CHECK_DB` on a 32-bit Linux platform for transporting a database to 32-bit Windows, skipping read-only tablespaces.
	```
	DECLARE
	  db_ready BOOLEAN;
	BEGIN
	  db_ready := 
	       DBMS_TDB.CHECK_DB('Microsoft Windows IA (32-bit)',DBMS_TDB.SKIP_READONLY);
	END;
	/
	PL/SQL procedure successfully completed.
	```
	If no warnings appear, or if `DBMS_TDB.CHECK_DB` returns `TRUE`, then you can transport the database. Proceed to Step 6.
	If warnings appear, or if `DBMS_TDB.CHECK_DB` returns `FALSE`, then you cannot currently transport the database. Proceed to Step 5.
5. Examine the output to learn why the database cannot be transported, fix the problem if possible, and then return to the Step 4.
	See Also:
	[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=ARPLS-GUID-E36C9358-B1BA-4952-9CD2-2E5AB1FFDAA6) for information about `DBMS_TDB`
6. Execute the `DBMS_TDB.CHECK_EXTERNAL` function to identify any external tables, directories, or BFILEs. RMAN cannot automate the transport of these files, so you must copy the files manually and re-create the database directories.
	The following example shows how to call the `DBMS_TDB.CHECK_EXTERNAL` function.
	```
	DECLARE
	     external BOOLEAN;
	BEGIN
	    /* value of external is ignored, but with SERVEROUTPUT set to ON
	     * dbms_tdb.check_external displays report of external objects
	     * on console */
	    external := DBMS_TDB.CHECK_EXTERNAL;
	END;
	/
	```
	If no external objects exist, then the procedure completes with no output. If external objects exist, however, then the output is similar to the following:
	```
	The following external tables exist in the database:
	SH.SALES_TRANSACTIONS_EXT
	The following directories exist in the database:
	SYS.DATA_PUMP_DIR, SYS.MEDIA_DIR, SYS.DATA_FILE_DIR, SYS.LOG_FILE_DIR
	The following BFILEs exist in the database:
	PM.PRINT_MEDIA
	 
	PL/SQL procedure successfully completed.
	```

#### 28.5.2 Converting Data Files on the Source Host When Transporting a Database

Use the `CONVERT DATBASE` command to perform cross-platform transport of a database by converting data files on the source host.

When you transport entire databases, certain types of blocks such as blocks in undo segments must be reformatted to ensure compatibility with the destination platform. Even though the endian formats for the source and destination platform are the same, certain data files must undergo a conversion process and cannot be simply copied from one platform to another.

Data files with undo information and those from the HP Tru64 platform must be converted. By default, all data files are converted when the `CONVERT DATABASE` command is executed. If, however, `SKIP UNNECESSARY DATAFILES` is used in the `CONVERT DATABASE` command, then the data files with undo segments and those from the HP Tru64 platform are converted. All other data files do not require conversion and can be copied to the new database using FTP, an operating system copy command, or some other mechanism.

See Also:

" Overview of Database Conversion Using Image Copies "

This section assumes that you have met all of the `CONVERT DATABASE` prerequisites and followed the steps in " Checking the Database Before Cross-Platform Database Conversion ". The goal of this procedure is to convert the format of data files on the source host as part of a cross-platform database transport.

Assume that you want to convert a database running on Solaris to a database that runs on Windows.

To convert the database on the source host:

1. Open the [source database](glossary.md) in read-only mode.
	```
	SHUTDOWN IMMEDIATE;
	STARTUP MOUNT;
	ALTER DATABASE OPEN READ ONLY;
	```
2. Start RMAN and connect to the source database as `TARGET` as described in " [Making Database Connections with RMAN](starting-interacting-with-rman-client.md) ".
3. Run the `CONVERT` `DATABASE` command.
	The following example shows a `CONVERT DATABASE` command (sample output included). The `TRANSPORT SCRIPT` parameter specifies the location of the generated SQL script that you can use to create the new database. The `TO PLATFORM` parameter indicates the platform of the [destination database](glossary.md). The `DB_FILE_NAME_CONVERT` parameter specifies the naming scheme for the generated data files.
	```
	RMAN> CONVERT DATABASE
	2>   NEW DATABASE 'newdb'
	3>   TRANSPORT SCRIPT '/tmp/convertdb/transportscript.sql'
	4>   TO PLATFORM 'Microsoft Windows IA (32-bit)'
	5>   DB_FILE_NAME_CONVERT '/disk1/oracle/dbs' '/tmp/convertdb';
	 
	Starting conversion at source at 25-NOV-13
	using channel ORA_DISK_1
	 
	External table SH.SALES_TRANSACTIONS_EXT found in the database
	.
	.
	.
	Directory SYS.ORACLE_HOME found in the database
	Directory SYS.ORACLE_BASE found in the database
	Directory SYS.LOG_FILE_DIR found in the database
	.
	.
	.
	BFILE PM.PRINT_MEDIA found in the database
	 
	User SYS with SYSDBA and SYSOPER privilege found in password file
	User SBU with SYSBACKUP privilege found in password file
	channel ORA_DISK_1: starting datafile conversion
	input datafile fno=00001 name=/disk1/oracle/dbs/tbs_01.f
	converted datafile=/tmp/convertdb/tbs_01.f
	channel ORA_DISK_1: datafile conversion complete, elapsed time: 00:00:15
	channel ORA_DISK_1: starting datafile conversion
	input datafile fno=00002 name=/disk1/oracle/dbs/tbs_ax1.f
	converted datafile=/tmp/convertdb/tbs_ax1.f
	channel ORA_DISK_1: datafile conversion complete, elapsed time: 00:00:03
	.
	.
	.
	channel ORA_DISK_1: starting datafile conversion
	input datafile fno=00016 name=/disk1/oracle/dbs/tbs_52.f
	converted datafile=/tmp/convertdb/tbs_52.f
	channel ORA_DISK_1: datafile conversion complete, elapsed time: 00:00:01
	Edit init.ora file init_00gb3vfv_1_0.ora. This PFILE will be used to 
	  create the database on the target platform
	Run SQL script /tmp/convertdb/transportscript.sql on the target platform 
	  to create database
	To recompile all PL/SQL modules, run utlirp.sql and utlrp.sql on 
	  the target platform
	To change the internal database identifier, use DBNEWID Utility
	Finished conversion at source at 25-NOV-13
	```
4. After `CONVERT` `DATABASE` completes, you can open the source database read/write again.
5. Move the data files generated by `CONVERT DATABASE` to the desired locations on the destination host.
	In Step [^1], the command creates the files in the `/tmp/convertdb/` directory on the source host. Move these files to the directory on the destination host that will contain the destination database files.
6. If the path to the data files is different on the destination host, then edit the transport script to refer to the new data file locations.
7. If necessary, edit the initialization parameter file to change any settings for the destination database.
	You must edit several entries at the top of the initialization parameter file when the database is moved to the destination platform. For example, the initialization parameter file may look as follows:
	```
	# Please change the values of the following parameters:
	 control_files            = "/tmp/convertdb/cf_D-NEWDBT_id-1778429277_00gb9u2s"
	 service_names            = "NEWDBT.example.com"
	 db_recovery_file_dest    = "/tmp/convertdb/orcva"
	 db_recovery_file_dest_size= 10737418240
	 instance_name            = "NEWDBT"
	 db_name                  = "NEWDBT"
	 plsql_native_library_dir = "/tmp/convertdb/plsqlnld1"
	```
8. If necessary, edit the transport script to use the new names for the converted data files.
	In the example in Step [^1], the transport script is named `/tmp/convertdb/transportscript.sql`. You run this script on the [destination host](glossary.md) to create the database. Thus, you must edit this script with the correct names for the data files.
9. On the destination host, start SQL\*Plus and connect to the destination database instance as `SYSDBA` or `SYSBACKUP` using operating system authentication.
	For example, connect as follows:
	```
	SQL> CONNECT / AS SYSBACKUP
	```
	If you choose not to use operating system authentication, you can create a [password file](glossary.md) and then connect with a user name and password.
10. Execute the transport script in SQL\*Plus to create the new database on the destination host.
	```
	SQL> @transportscript
	```

When the transport script finishes, the creation of the new database is complete.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=ADMIN11046) for information about operating system authentication and password file authentication

#### 28.5.3 Converting Data Files on the Destination Host When Transporting a Database

The procedure converts the format of data files on the destination host as part of a cross-platform database transport.

Perform the data file conversion in the following phases:

1. Ensure that you have met all of the prerequisites described in " Checking the Database Before Cross-Platform Database Conversion ".
2. Convert data files on the source host and generate the required scripts, as described in " Performing Preliminary Data File Conversion Steps on the Source Host ".
3. Run the generated scripts on the destination host, as described in " Running the Conversion Scripts on the Destination Host ".

##### 28.5.3.1 Performing Preliminary Data File Conversion Steps on the Source Host

When you use the `CONVERT DATBASE` command on the source host, RMAN generates an initialization parameter file and scripts that you can edit for use on the destination host. You also copy the unconverted data files from the source host to the destination host..

To perform preliminary data file conversion steps on the source host:

1. Ensure that the database is open in read-only mode.
2. Start RMAN and connect as `TARGET` to the source database and as a common user with the `SYSDBA` or `SYSBACKUP` privilege. See " [Making Database Connections with RMAN](starting-interacting-with-rman-client.md) ".
3. Run the `CONVERT DATABASE ON DESTINATION PLATFORM` command.
	The following example shows a sample `CONVERT                             DATABASE` command (sample output included). The `ON                             DESTINATION PLATFORM` parameter specifies that any `CONVERT` commands required for data files are executed on the destination platform rather than the source platform. The `FORMAT` parameter specifies the naming scheme for the generated files.
	```
	RMAN> CONVERT DATABASE
	2>   ON DESTINATION PLATFORM
	3>   CONVERT SCRIPT '/tmp/convertdb/convertscript-target'
	4>   TRANSPORT SCRIPT '/tmp/convertdb/transportscript-target'
	5>   NEW DATABASE 'newdbt'
	6>   FORMAT '/tmp/convertdb/%U';
	 
	Starting conversion at source at 28-JAN-13
	using target database control file instead of recovery catalog
	allocated channel: ORA_DISK_1
	channel ORA_DISK_1: sid=39 devtype=DISK
	 
	External table SH.SALES_TRANSACTIONS_EXT found in the database
	.
	.
	.
	Directory SYS.ORACLE_HOME found in the database
	Directory SYS.ORACLE_BASE found in the database
	Directory SYS.LOG_FILE_DIR found in the database
	.
	.
	.
	BFILE PM.PRINT_MEDIA found in the database
	 
	User SYS with SYSDBA and SYSOPER privilege found in password file
	User SBU with SYSBACKUP privilege found in password file
	channel ORA_DISK_1: starting to check datafiles
	input datafile fno=00001 name=/disk1/oracle/dbs/tbs_01.f
	channel ORA_DISK_1: datafile checking complete, elapsed time: 00:00:00
	channel ORA_DISK_1: starting to check datafiles
	input datafile fno=00002 name=/disk1/oracle/dbs/tbs_ax1.f
	channel ORA_DISK_1: datafile checking complete, elapsed time: 00:00:00
	channel ORA_DISK_1: starting to check datafiles
	input datafile fno=00017 name=/disk1/oracle/dbs/tbs_03.f
	channel ORA_DISK_1: datafile checking complete, elapsed time: 00:00:00
	.
	.
	.
	channel ORA_DISK_1: starting to check datafiles
	input datafile fno=00015 name=/disk1/oracle/dbs/tbs_51.f
	channel ORA_DISK_1: datafile checking complete, elapsed time: 00:00:00
	channel ORA_DISK_1: starting to check datafiles
	input datafile fno=00016 name=/disk1/oracle/dbs/tbs_52.f
	channel ORA_DISK_1: datafile checking complete, elapsed time: 00:00:00
	Edit init.ora file /tmp/convertdb/init_00gb9u2s_1_0.ora. This PFILE will be used to create the database on the target platform
	Run SQL script /tmp/convertdb/transportscript-target on the target platform to create database
	Run RMAN script /tmp/convertdb/convertscript-target on target platform to convert datafiles
	To recompile all PL/SQL modules, run utlirp.sql and utlrp.sql on the target platform
	To change the internal database identifier, use DBNEWID Utility
	Finished conversion at source at 28-JAN-13
	Starting Control File Autobackup at 28-JAN-13
	piece handle=/disk2/oracle/backups/c-1678658224-20131202-02 comment=NONE
	Finished Control File Autobackup at 28-JAN-13
	```
	The previous command creates a transport script, an initialization parameter file for the new database, and a convert script containing RMAN `CONVERT DATAFILE` commands for each data file being converted.
	Note:
	`CONVERT` `DATABASE` `ON` `DESTINATION` `PLATFORM` does not produce converted data file copies. The command only creates scripts.
4. Use an operating system utility to copy the following files to a temporary location on the destination host:
	- The data files to be converted
	- The convert script
	- The transport script
	- The initialization file for the destination database
5. Make the source database read/write.

##### 28.5.3.2 Running the Conversion Scripts on the Destination Host

Convert data files on the destination host and complete the cross-platform database transport by running the scripts that were generated on the source host during database conversion.

The convert script created in the previous phase uses the original data file names of the source database files. The `FORMAT` parameter specifies the name that was generated with the `FORMAT` or `DB_FILE_NAME_CONVERT` parameter of the `CONVERT DATABASE` command.

If the data files of the source database are accessible from the destination host with the same path names, then so long as the source database is read-only you can run the convert script on the destination host without any changes. For example, if the source and destination hosts both use NFS to mount a disk containing the source data files, and if the mount point for both hosts is `/fs1/dbs/`, then no editing is needed.

To run the conversion scripts on the destination host:

1. If necessary, edit the convert script.
	In the script, one `CONVERT DATAFILE` command exists for each data file to be converted. The convert script must indicate the current temporary file names of the unconverted data files and the output file names of the converted data files. A typical convert script looks as follows:
	```
	RUN
	{
	 CONVERT
	 FROM PLATFORM 'Linux IA (32-bit)'
	 PARALLELISM 10
	  DATAFILE '/disk1/oracle/dbs/tbs_01.f'
	  FORMAT '/tmp/convertdb/data_D-TV_I-1778429277_TS-SYSTEM_FNO-1_7qgb9u2s'
	 
	  DATAFILE '/disk1/oracle/dbs/tbs_ax1.f'
	  FORMAT '/tmp/convertdb/data_D-TV_I-1778429277_TS-SYSAUX_FNO-2_7rgb9u2s'
	 
	  DATAFILE '/disk1/oracle/dbs/tbs_03.f'
	  FORMAT '/tmp/convertdb/data_D-TV_I-1778429277_TS-SYSTEM_FNO-17_7sgb9u2s'
	 
	 DATAFILE '/disk1/oracle/dbs/tbs_51.f'
	 FORMAT '/tmp/convertdb/data_D-TV_I-1778429277_TS-TBS_5_FNO-15_8egb9u2u'
	 
	 DATAFILE '/disk1/oracle/dbs/tbs_52.f'
	  FORMAT '/tmp/convertdb/data_D-TV_I-1778429277_TS-TBS_5_FNO-16_8fgb9u2u';
	}
	```
	Edit each `DATAFILE` command in the convert script to specify the temporary location of each data file as input. Also, edit the `FORMAT` parameter of each command to specify the desired final location of the data files of the transported database.
2. If necessary, edit the initialization parameter file on the destination host to change settings for the destination database.
	You must edit several entries at the top of the initialization parameter file. For example, the initialization parameter file may look as follows:
	```
	# Please change the values of the following parameters:
	control_files            = "/tmp/convertdb/cf_D-NEWDBT_id-1778429277_00gb9u2s"
	db_recovery_file_dest    = "/tmp/convertdb/orcva"
	db_recovery_file_dest_size= 10737418240
	instance_name            = "NEWDBT"
	service_names            = "NEWDBT.example.com"
	plsql_native_library_dir = "/tmp/convertdb/plsqlnld1"
	db_name                  = "NEWDBT"
	```
3. On the destination host, use SQL\*Plus to start the database instance in `NOMOUNT` mode.
	Specify the initialization parameter file that you copied in the preceding step. For example, enter the following command:
	```
	SQL> STARTUP NOMOUNT PFILE='/tmp/init_convertdb_00i2gj63_1_0.ora'
	```
4. Start RMAN and connect to the destination database (not the source database) as `TARGET` and as a common user with the `SYSDBA` or `SYSBACKUP` privilege. For example, enter the following command:
	```
	% rman
	RMAN> CONNECT TARGET "sbu@prod_dest AS SYSBACKUP";
	```
5. Run the convert script at the RMAN prompt. For example, enter the following command:
	```
	RMAN> @/tmp/convertdb/convertscript-target
	```
6. Shut down the database instance.
	This step is necessary because the transport script that must execute includes a `STARTUP NOMOUNT` command.
7. If necessary, edit the transport script to use the new names for the converted data files.
	In the example in Step [^1], the transport script is `/tmp/convertdb/transportscript.sql`. You run this script on the destination host to create the database. Thus, you must edit this script with the correct names for the data files.
8. Execute the transport script in SQL\*Plus.
	For example, create the new database on the destination host as follows:
	```
	SQL> @/tmp/convertdb/transportscript
	```

When the transport script completes, the destination database is created.

### 28.6 Overview of Cross-Platform Data Transport Using Backup Sets

RMAN can transport databases, data files, and tablespaces across platforms by using backup sets. With backup sets, you can reduce the size of backups using block compression. This improves backup performance and reduces the time taken to transport backups over the network.

Note:

To perform cross-platform data transport using backup sets, the version of the destination database must be Oracle Database 12c Release 1 (12.1) or later.

When you transport an entire database to a different platform, the source platform and the destination platform must use the same endian format. However, user tablespaces can be transported to a destination platform that uses a different endian format from the source platform.

A cross-platform backup is an RMAN backup that can be restored on a destination platform that is different from the source platform. Cross-platform backups can be restored on any platform that is supported in the `V$TRANSPORTABLE_PLATFORM` view.

RMAN does not catalog backup sets created for cross-platform transport in the control file. This ensures that backup sets created for cross-platform transport are not used during regular restore operations.

#### 28.6.1 Basic Terms Used in Cross-Platform Data Transport Using Backup Sets

Before using backup sets to perform cross-platform data transport, it is useful to understand the following terms.

Foreign Data File

Data files that do not belong to the [destination database](glossary.md) are called [foreign data file](glossary.md) s. These data files are being plugged in to the destination database as part of a data transfer to the destination database. In the [source database](glossary.md), this data file is identified by its original data file number.

Foreign Tablespace

A [foreign tablespace](glossary.md) is a set of foreign data files that comprise a tablespace in the [source database](glossary.md). These foreign data files do not belong to the [destination database](glossary.md), but are being transported into the destination database and are identified by the original tablespace name in the source database.

Foreign Data File Copy

A [foreign data file copy](glossary.md) is a data file that was restored from a [cross-platform backup](glossary.md). It cannot be directly plugged in to the [destination database](glossary.md) because it is inconsistent. You must apply a cross-platform incremental backup to this data file and recover it before you can plug it in to the destination database.

Data Pump Destination

A Data Pump destination is a location on the disk of the server host of the destination database on which the Data Pump [export dump file](glossary.md) and the Data Pump log files are stored.

#### 28.6.2 High-Level Steps to Transport Data Across Platforms Using Backup Sets

High-level steps to transport data across using backup sets include creating a cross-platform backup of the source database, making the source database backups accessible to the destination, and restoring backups on the destination database.

Transporting data across platforms using backup sets consists of the following high-level steps:

1. On the source database, use the `BACKUP` command to create a cross-platform backup of the database, tablespaces, or data files that need to be transported to a different platform. The backup is created as backup sets on the source host.
	Use the `FOR TRANSPORT` or `TO                             PLATFORM` clause in the `BACKUP` command to create cross-platform backups. When you create a cross-platform backup of read-only tablespaces using either of these clauses, RMAN can also create a Data Pump export dump file containing the metadata required to plug these tablespaces into the destination database.
2. Transfer the backup sets created on the source host to the destination host.
	You can transport the backup sets using operating system utilities. For example, if your operating system is Linux or UNIX, you can use the `cp` command to transfer backup sets.
3. On the destination database, restore the backup sets that were transferred from the source host. Use the `RESTORE` command to restore cross-platform backups.
	When you are transporting tablespaces across platforms by using inconsistent tablespace backups, the additional step of recovering the tablespaces is required as described in " Performing Cross-Platform Transport of Tablespaces Using Inconsistent Backups ".

Note:

Although the `TO PLATFORM` and `FOR                         TRANSPORT` clauses are not supported in Oracle Database 10g Release 2 (10.2) or Oracle Database 11g, you can transport data from these versions of the database to Oracle Database 12c Release 1 (12.1). On the source database, you first create backup sets of the tablespaces to be transported and then create the Data Pump export dump file by using the `expdp` command. To restore these backups on the destination database, you perform a restore operation using the `RESTORE` command and then use the `impdp` command to import the Data Pump export dump file.

See Also:

Guidelines for Cross-Platform Data Transport Using Backup Sets

#### 28.6.3 Scenarios in Which RMAN Automatically Creates a Cross-Platform Backup of the Database

Under certain conditions, RMAN automatically creates a cross-platform backup of the entire database.

When you use backup sets to back up an entire database, RMAN automatically creates a cross-platform backup of the database (in addition to the specified backup) if the following conditions are met:

- Prerequisites for transporting an entire database as a backup set are satisfied, as described in Performing Cross-Platform Transport of a Whole Database with Backup Sets.
- The `BACKUP` command does not contain any clause that is incompatible with the `FOR TRANSPORT` or `TO                             PLATFORM` clause.
	See Also:
	[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF107) for information about the incompatible clauses

Example 28-1 Implicit Creation of a Cross-Platform Database Backup

The following `BACKUP` command creates a cross-platform backup of the database. Although the command does not contain either the `FOR                     TRANSPORT` or `TO PLATFORM` clause to indicate that it is a cross-platform backup, because the prerequisites for transporting an entire database using backup sets are met, an implicit cross-platform backup of the database is created.

```
RUN
{
   ALLOCATE CHANNEL c1 DEVICE TYPE DISK;
   ALLOCATE CHANNEL c2 DEVICE TYPE DISK;
   ALLOCATE CHANNEL c3 DEVICE TYPE DISK;
   BACKUP
      SKIP OFFLINE
      FILESPERSET 1
      FORMAT '/tmp/xplat_backups/implicit_full_db_%U'
   DATABASE;}
```

#### 28.6.4 Guidelines for Cross-Platform Data Transport Using Backup Sets

Follow guidelines for performing cross-platform transport with backup sets.

You can specify the names and locations of restored data files and specify the objects that must be imported into the destination database.

##### 28.6.4.1 About Backing Up Data on the Source Database for Cross-Platform Data Transport

Use the `BACKUP` command on the source database to create a backup set containing data that must be transported to the destination database. To indicate that you are creating a cross-platform backup, include either the `FOR TRANSPORT` or `TO PLATFORM` clause.

Use one of the following clauses with the `BACKUP` command:

- `FOR TRANSPORT` clause
	The backup set that is created can be transported to any destination database. If the destination database uses an endian format that is different from that of the source database, then the required endian format conversion is performed on the destination database. The benefit of this method is that the processing overhead of the conversion operation is offloaded to the destination database.
- `TO PLATFORM` clause
	The endian format conversion is performed on the source database. The target platform specified by the `TO PLATFORM` clause must be a supported platform for cross-platform transport. The `V$TRANSPORTABLE_PLATFORM` view contains the list of supported platforms.

See Also:

- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF107) for an example of cross-platform backups that contain multiple backup pieces
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF107) for a list of clauses that are not supported when creating cross-platform backups using the `BACKUP` command

##### 28.6.4.2 About the Data Pump Export Dump File Used for Cross-Platform Tablespace Transport

An export dump file is used to store the metadata required to plug in restored tablepaces into the destination database.

When you create a cross-platform consistent tablespace backup, the backup set contains the data files that contain data related to the specified tablespaces. A consistent tablespace backup is a backup of one or more tablespaces that is created when the tablespaces are in read-only mode. After you restore this backup in your destination database, the tablespaces must be plugged in to the destination database. To do this, in addition to the backup set containing the tablespace data, you need the metadata for these tablespaces from the source database.

On the source database, use the `DATAPUMP` clause in the `BACKUP` command to create the metadata required to plug tablespaces in to the target database. The metadata is stored in a Data Pump [export dump file](glossary.md) as a separate backup set. Use this backup set to plug the transported tablespaces in to the target database.

You can specify how the backup set containing the tablespace metadata is named by using the `FORMAT` option with the `DATAPUMP` clause. If you omit the `FORMAT` option, then the format specified in the `BACKUP` command is used to name the export dump file. When no `FORMAT` option is specified in the `BACKUP` command, the default format is used.

Note:

When you use the `DATAPUMP` clause, the tablespaces that are being transported must be made read-only.

##### 28.6.4.3 About Restoring Data on the Destination Host During Cross-Platform Data Transport

Use the `foreignFileSpec` clause of the `RESTORE` command to restore the database, tablespaces, or data files contained in a cross-platform backup consisting of backup sets.

Specify the following information when you restore cross-platform backups:

- Backup set that contains data that was backed up on the source database
	Use the `BACKUPSET` option of the `foreignFileSpec` subclause to specify the name of the cross-platform backup set from which data must be restored. If the cross-platform backup consists of multiple backup sets, use a separate `BACKUPSET` clause for each backup set. To restore tablespaces, you must specify the backup sets that contain the tablespace data using the `BACKUPSET` clause and the backup set that contains the tablespace metadata using the `DUMP FILE` option of the `foreignFileSpec` subclause.
	Using multiple backup sets is not supported during recovery. You cannot apply multiple backup sets to a set of foreign data files.
- Data file numbers or names of tablespaces as they exist in the source database
	If you are restoring data files or tablespaces, you can restore specific tablespaces or data files that are contained in a cross-platform backup.
- Location where the restored data files must be stored
	Use the `FORMAT` clause to specify the location and the names used to store the restored data files.
	If you do not provide a destination, then the `DB_CREATE_FILE_DEST` initialization parameter must be set in the target platform. RMAN restores the data files to the location specified by this parameter using new Oracle Managed File (OMF) names.
- Name of the source platform (only when conversion is performed on the destination database)
	Use `FROM PLATFORM` to specify the name of the source platform on which the backup sets were created. The platform name must exactly match the name specified while creating the backup set. If there is a difference in the platform names, the restore operation fails.

See Also:

- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF90573) for information about `RESTORE` command clauses
- " About Names and Locations for Restored Objects on the Destination Database "
- " About Backing Up Data on the Source Database for Cross-Platform Data Transport "

##### 28.6.4.4 About Selecting Objects to Be Restored from Cross-Platform Backups

While restoring data from a cross-platform backup, you can either restore all the data contained in the cross-platform backup or only certain objects.

Restoring All Data Contained in the Cross-Platform Backup

To restore the entire database, use the `FOREIGN DATABASE` clause in the `RESTORE` command. This clause can only be used when restoring from a whole database backup set and when both the source platform and destination database use the same endian format. You can optionally use the `FORMAT` clause to specify the pattern used to name restored files.

To restore all the data files contained in the cross-platform backup, use the `ALL FOREIGN DATAFILES` clause in the `RESTORE` command.

Restoring Part of the Data Contained in the Cross-Platform Backup Set

You can restore some data files or tablespaces contained in a cross-platform backup. To restore only some data files, use the `FOREIGN DATAFILE` clause in the `RESTORE` command. Specify the absolute file number of the data file in the source database while restoring data. To restore only some tablespaces contained in a cross-platform backup, use the `FOREIGN TABLESPACE` clause in the `RESTORE` command. Specify the names of the tablespaces that must be restored as part of this clause.

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF90573) for more information about the clauses described in this section

##### 28.6.4.5 About Names and Locations for Restored Objects on the Destination Database

While restoring a cross-platform backup, specify the data file names and the location to which the data files must be restored.

Use one of the following clauses in the `RESTORE` command:

- Use the `TO NEW` option with the `ALL FOREIGN DATAFILES` clause to restore the data files to the location specified by the `DB_CREATE_FILE_DEST` parameter. By default, RMAN uses OMF names for the data files.
- Use the `FORMAT` option to specify the pattern used to name restored data files. You can also specify the directory for these files as part of the `FORMAT` specification.

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF149) for more information about the clauses described in this section

##### 28.6.4.6 About Importing the Data Pump Export Dump File Created During Cross-Platform Tablespace Transport

When restoring a cross-platform backup of read-only tablespaces on the destination database, the backup set that contains the Data Pump export dump file created must be restored.

Use the `DUMP FILE ... FROM BACKUPSET` option of the `foreignFileSpec` subclause to restore the backup set that contains the Data Pump export dump file that was created on the source database. This file contains the metadata required to plug the tablespace in to the destination database.

Use the `DATAPUMP` clause in the `RESTORE` command to specify the location, in the destination host, to which the export dump file is restored. If you omit this clause, the dump file is restored to a default operating system-specific location.

By default, RMAN automatically imports the export dump file after all the required foreign data files are restored. You can choose not to import the export dump file by specifying the `NOIMPORT` clause. If you do not import the export dump file as part of the restore operation, then you must manually import the dump file when you want to plug the tablespaces in to the destination database.

Note:

If the export dump file is automatically imported (that is, the `NOIMPORT` clause is not used), then the destination database must be open in read/write mode.

### 28.7 Performing Cross-Platform Database Transport with Backup Sets

You can transport a whole multitenant container database (CDB), the root only, or one or more pluggable databases (PDBs) across platforms.

#### 28.7.1 About Cross-Platform Transport of PDBs

To transport an entire PDB to a different platform, the source platform and destination platform must use the same endian format. The `COMPATIBLE` parameter on the source and destination CDB must be set to 12.1 or higher.

Use one of the following techniques to transport PDBs across platforms:

- Connect to the root and use the `BACKUP FOR TRANSPORT ... PLUGGABLE DATABASE` or `BACKUP TO PLATFORM ... PLUGGABLE DATABASE` command to create a [cross-platform backup](glossary.md) of one or more PDBs.
	When you are connected to the root, the following command creates a cross-platform backup of the PDBs `hr_pdb` and `sales_pdb`. The PDBs must be read-only mode before the cross-platform backup is created.
	```
	BACKUP FOR TRANSPORT
	PLUGGABLE DATABASE hr_pdb, sales_pdb FORMAT '/tmp/backups/pdb_%U';
	```
- Connect to the PDB and use the `BACKUP FOR TRANSPORT` or `BACKUP TO PLATFORM` commands to create backup sets that can be used to transport the PDB data to another platform.

Note:

Performing cross-platform data transport of one or more PDBs by using the `CONVERT` command is not supported.

See Also:

" [Making RMAN Connections to a CDB](starting-interacting-with-rman-client.md) "

#### 28.7.2 Performing Cross-Platform Transport of a Whole Database with Backup Sets

When transporting an entire database across platforms using backup sets, you can convert the database either on the source database or the destination database. The benefit of performing the conversion on the destination database is that the processing overhead of the convert operation is offloaded from the source to the destination database.

Prerequisites for Creating a Cross-Platform Backup of the Entire Database:
- The `COMPATIBLE` parameter in the server parameter file of the source database and the destination database must be set to 12.0.0 or higher.
- The source database must be open in read-only mode.
- The `DBMS_TDB.CHECK_DB` procedure must run successfully. See " Checking the Database Before Cross-Platform Database Conversion ".
- The source platform and destination platform must use the same endian format.

To transport a whole database from one platform to another:

1. Start SQL\*Plus and connect to the root of the source database `prod_source` as a common user with the `SYSDBA` privilege.
	```
	% sqlplus sys@prod_source as SYSDBA
	```
	When prompted, enter the password for the `sys` user.
2. Query the name of the destination platform in `V$TRANSPORTABLE_PLATFORM`.
	To transport the entire database, the endian formats of the source platform and the destination platform must be the same.
	See Also:
	" Platforms that Support Cross-Platform Data Transport " for information about determining the platform name
3. Choose a method for naming the output files.
	Use the `FORMAT` clause of the `BACKUP` command to specify the names of the output files.
	For example, the following `FORMAT` clause specifies that the output files must be stored using unique names that begin with `transport_` in the directory `/oradata/backups/special.`
	```
	FORMAT '/oradata/backups/special/transport_%U'
	```
4. Start RMAN and connect to the source database as `TARGET` and as a common user with the `SYSDBA` or `SYSBACKUP` privilege.
	The source database is the database that contains the data that needs to be transported to a different platform.
	In this example, `sbu` is a user who is granted the `SYSBACKUP` privilege in the source database `prod_source`.
	```
	% RMAN
	RMAN> CONNECT TARGET "sbu@prod_source AS SYSBACKUP";
	```
	Enter the password for the `sbu` user when prompted.
5. Place the database in read-only mode.
	```
	SHUTDOWN IMMEDIATE;
	STARTUP MOUNT;
	ALTER DATABASE OPEN READ ONLY;
	```
6. Back up the source database using the `FOR TRANSPORT` or `TO PLATFORM` clause in the `BACKUP` command. Using either of these clauses creates a [cross-platform backup](glossary.md) that uses backup sets.
	The following example creates a cross-platform backup of the entire database. This backup can be restored on any supported platform that uses the same endian format as the source database. The source platform is Sun Solaris x86 64-bit. Because the `FOR TRANSPORT` clause is used, the conversion is performed on the destination database. The cross-platform database backup is stored in `db_trans.bck` in the `/tmp/xplat_backups` directory on the source host.
	```
	BACKUP
	FOR TRANSPORT
	FORMAT '/tmp/xplat_backups/db_trans.bck'
	DATABASE;
	```
7. Disconnect from the source database.
8. Move the backup sets created by the `BACKUP` command to the destination host.
	Use operating system-specific utilities to transfer the created backup sets from the source host to the destination host.
	For example, if the operating system of your source and destination hosts is Linux or UNIX, use the `cp` command to move files.
9. Connect to the destination database (to which the database must be transported) as `TARGET` and as a common user with the `SYSDBA` or `SYSBACKUP` privilege.
	In this example, `sbu` is a user who is granted the `SYSBACKUP` privilege in the destination database `prod_dest`.
	```
	% RMAN
	RMAN> CONNECT TARGET "sbu@prod_dest AS SYSBACKUP";
	```
	Enter the password for the `sbu` user when prompted.
10. Ensure that the destination database is in `NOMOUNT` state.
11. Restore the backup sets that were transferred from the source by using the `RESTORE` command with the `FOREIGN DATABASE` clause.
	The following example restores the cross-platform database backup created in Step [^2]. The destination database uses the same endian format as the source database. The `FROM                             PLATFORM` clause specifies the name of the platform on which the backup was created. This clause is required to convert backups on the destination. The backup set containing the cross-platform database backup is stored in the `/tmp/xplat_restores` directory on the destination host. The `TO NEW` option specifies that the restored foreign data files must use new OMF-specified names in the destination database. Ensure that the `DB_CREATE_FILE_DEST` initialization parameter is set.
	```
	RESTORE
	FROM PLATFORM 'Solaris Operating System (x86-64)'
	FOREIGN DATABASE TO NEW
	FROM BACKUPSET '/tmp/xplat_restores/db_trans.bck';
	```

#### 28.7.3 Performing Cross-Platform Transport of a Closed PDB

Pluggable database (PDBs) can be transported and plugged in to a destination multitenant container database (CDB) which is on a different platform than the source CDB. In addition to an RMAN backup of the PDB, you need the metadata required to plug the PDB into the destination CDB.

The `COMPATIBLE` parameter on the source CDB and destination CDB must be set to 12.2. The source CDB and the destination CDB must use the same endian format.

To perform cross-platform transport of a closed PDB into a destination CDB:

1. Perform the following steps on the source CDB:
	1. Connect to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege.
		2. Close the PDB that needs to be transported.
		The following statement closes the PDB `hr_pdb`.
		```
		RMAN> ALTER PLUGGABLE DATABASE hr_pdb CLOSE IMMEDIATE;
		```
		3. Create a cross-platform full backup of the PDB that must be transported by using the `BACKUP PLUGGABLE DATABASE` command.
		To create a cross-platform backup, include either the `FOR TRANSPORT` or `TO PLATFORM` clause.
		The following example creates a cross-platform backup of the PDB `hr_pdb` for the `Linux x86 64-bit` platform. The metadata required to plug this PDB into the destination CDB is specified using the `UNPLUG INTO` clause and stored in the XML file `metadata_hrpdb.xml`.
		```
		BACKUP TO PLATFORM= 'Linux x86 64-bit'
		   UNPLUG INTO '/u01/oradata/backups/metadata_hrpdb.xml'
		   PLUGGABLE DATABASE hr_pdb
		   FORMAT '/u01/oradata/backups/transport_hrpdb.bck';
		```
2. Transport the backup sets and the XML file created in Step 1c to the destination CDB.
3. Perform the following steps on the destination CDB:
	1. Connect to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege.
		2. Ensure that the CDB is open in read-write mode.
		The following command displays the current mode of the CDB.
		```
		RMAN> SELECT open_mode FROM V$DATABASE;
		```
		3. Determine if the source PDB that is being transported is compatible with the destination CDB by using the `DBMS_PDB.CHECK_PLUG_COMPATIBILITY` procedure.
		The following function determines if the source PDB `hr_pdb`, whose metadata is stored in an XML file `metadata_hrpdb.xml`, can be plugged in to the destination CDB. The function returns `TRUE` is the source PDB is compatible with the destination CDB.
		```
		SQL> declare
		  2     c boolean;
		  3  begin
		  4     c:=dbms_pdb.check_plug_compatibility('/u02/backup_restore/metadata_hrpdb.xml','HR_PDB');
		  5     if (c) then dbms_output.put_line('True');
		  6       else dbms_output.put_line('False');
		  7     end if;
		  8  end;
		  9  /
		PL/SQL procedure successfully completed.
		```
		4. Restore the PDB backup that was created on the source CDB.
		The `USING` clause specifies the name of the XML file that contains the metadata required to plug the source PDB into the destination CDB. To copy data files to a different location than described in the XML file, use the `FILE_NAME_CONVERT` clause.
		The following statement restores the backup of the PDB `hr_pdb` that is stored in the backupset `transport_hrpdb.bck`. The metadata for this PDB is stored in `metadata_hrpdb.xml`.
		```
		RESTORE        
		   USING '/u02/backup_restore/metadata_hrpdb.xml'
		   FOREIGN PLUGGABLE DATABASE hr_pdb FORMAT '/u02/oracle/oradata/%U'       
		   FROM BACKUPSET '/u02/backup_restore/transport_hrpdb.bck';
		```
		5. The following command opens the PDB `hr_pdb`.
		```
		RMAN> ALTER PLUGGABLE DATABASE hr_pdb OPEN;
		```
		Note:
		If a PDB with the same name as the one being transported exists on the destination database, then the restore operation fails.
	Note:
	Performing Cross-Platform Transport of a PDB Using Inconsistent Backups

#### 28.7.4 Performing Cross-Platform Transport of a PDB Using Inconsistent Backups

You can use a combination of inconsistent and consistent backups to transport a PDB and plug it into a CDB that is on a different platform. Inconsistent backups enable you to reduce application downtime because the PDB can be open while the backup is performed

When the PDB is open, you create cross-platform inconsistent backups. The first backup is an incremental level 0 backup. Subsequent backups are incremental level 1 backups that contain changes made to the PDB since the last incremental backup. There is no restriction on the number of inconsistent level 1 backups. Finally, close the PDB, create the last consistent incremental level 1 backup and the XML file containing the metadata required to plug the source PDB into a destination CDB.

The `COMPATIBLE` parameter on the source CDB and destination CDB must be set to 12.2. The source CDB and the destination CDB must use the same endian format.

1. Perform the following steps on the source CDB:
	1. Connect to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege.
		2. Ensure that the PDB that must be transported is in read-write mode.
		3. Note the database SCN before a level 0 backup is created.
		```
		SELECT CHECKPOINT_CHANGE# FROM V$DATABASE;
		```
		4. Create a cross-platform incremental level 0 backup of the PDB that must be transported by using the `BACKUP ... PLUGGABLE DATABASE` command.
		Use either the `FOR TRANSPORT` or `TO PLATFORM` clause to specify a cross-platform backup. Include the `ALLOW INCONSISTENT` clause to indicate that the PDB is not in a consistent state.
		The following statement creates a cross-platform incremental level 0 backup of the PDB `hr_pdb`.
		```
		BACKUP INCREMENTAL LEVEL 0
		   FOR TRANSPORT  
		   ALLOW INCONSISTENT
		   PLUGGABLE DATABASE hr_pdb FORMAT '/u01/backups/hr_pdb_level0.bck';
		```
		Because the PDB is in read-write mode, an inconsistent backup is created.
		5. The following command closes the PDB `hr_pdb`.
		```
		RMAN> ALTER PLUGGABLE DATABASE hr_pdb CLOSE IMMEDIATE;
		```
		6. Create a consistent cross-platform incremental backup. The point-in-time for the incremental backup must be from the SCN noted in Step 1c.
		Include the `UNPLUG INTO` clause to specify the name of the XML that stores the metadata required to plug this PDB into the destination CDB.
		The following statement creates a cross-platform incremental backup of the PDB `hr_pdb`. This is a consistent PDB backup.
		```
		BACKUP INCREMENTAL FROM SCN 36462
		   FOR TRANSPORT
		   UNPLUG INTO '/u01/backups/metadata_hr_pdb.xml'
		   PLUGGABLE DATABASE hr_pdb FORMAT '/u01/backups/hr_pdb_level1_con.bck';
		```
2. Transport all the PDB backups and the XML file containing the PDB metadata to the destination database.
	Note:
	Typically, you would transport the inconsistent backups as they are created and then restore them on the destination CDB.
3. Perform the following steps on the destination CDB:
	1. Connect to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege.
		2. Ensure that the destination CDB is open in read-write mode.
		3. Restore the cross-platform inconsistent level 0 backup of the PDB that was created on the source CDB.
		This restore operation creates a set of foreign data files that correspond to the source PDB in the destination CDB.
		The following statement restores the cross-platform level 0 backup of the PDB `hr_pdb` that is stored in the backupset `hr_pdb_level0.bck`.
		```
		RESTORE 
		   FOREIGN PLUGGABLE DATABASE hr_pdb FORMAT '/u02/oradata/%U'
		   FROM BACKUPSET '/u02/backup_restore/hr_pdb_level0.bck';
		```
		4. Apply the cross-platform level 1 incremental backup created when the source PDB was closed to the data files restored in Step 3c. Use the XML file containing the source PDB metadata to plug the PDB into the destination CDB.
		The following command recovers the foreign data files by using the incremental level 1 backup `hr_pdb_level1_con.bck`. There are two restored foreign data files specified using the `FOREIGN DATAFILECOPY` clause. The `USING` clause specifies the XML file that contains metatdata required to plug the PDB into the destination CDB.
		```
		RECOVER
		USING '/u02/backup_restore/metadata_hr_pdb.xml'
		FOREIGN DATAFILECOPY '/u2/oradata/09qurbdp_1_1','/u2/oradata/03bcdqrv_2_5'
		FROM BACKUPSET '/u02/backup_restore/hr_pdb_level1_con.bck';
		```
		5. Determine the name of the transported PDB in the destination CDB.
		The source PDB is plugged in to the destination using a different name. Typically, the name is the unique name of the CDB followed by a randomly-generated number.
		The following command displays the list of PDBs.
		```
		SELECT name FROM V$PDBS;
		```
		6. The following statement opens the PDB `mycdb_72346`.
		```
		RMAN> ALTER PLUGGABLE DATABASE mycdb_72346 OPEN;
		```
		Note:
		If a PDB with the same name as the one being transported exists on the destination database, then the restore operation fails.
	Note:
	Performing Cross-Platform Transport of a Closed PDB

### 28.8 Performing Cross-Platform Transport of Tablespaces Using Backup Sets

You can transport tablespaces in the root or pluggable database (PDB) using backup sets.

#### 28.8.1 Performing Cross-Platform Transport of Read-Only Tablespaces Using Backup Sets

Use the `BACKUP` command to create backup sets used to transport read-only tablespaces from one platform to another. You must also export the metadata required to plug these tablespaces in to the destination database.

The source and destination platform can use different endian formats. You can restore all or some of the data files or tablespaces contained in a cross-platform backup. After restoring these objects, you can specify the name and location for the restored data files.

Prerequisites:

- `COMPATIBLE` parameter in the server parameter file of the [source database](glossary.md) and destination database is set to 12.0.0 or greater.
- The tablespaces to be transported are self-contained.
	Execute the `DBMS_TTS.TRANSPORT_SET_CHECK` procedure to check for dependencies. If the `TRANSPORT_SET_VIOLATIONS` view contains rows corresponding to the specified tablespaces, then you must resolve the dependencies before creating the cross-platform backup.
	See Also:
	[Example 21-1](performing-rman-tspitr.md) for information about executing the `DBMS_TTS.TRANSPORT_SET_CHECK` procedure
- The tablespaces to be transported are in read-only mode, unless the `ALLOW INCONSISTENT` clause is used in the `BACKUP` command.

To transport read-only tablespaces across platforms using backup sets:

1. Connect to the source database from which you need to transport tablespaces as `TARGET`.
	For a tablespace in the root, connect to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege. For tablspaces in the PDB, connect to the PDB as a common user or local user with the `SYSDBA` or `SYSBACKUP` privilege.
	In this example, `sbu` is a user who is granted the `SYSBACKUP` privilege on the source database `prod_source`.
	```
	$ RMAN
	RMAN> CONNECT TARGET "sbu@prod_source AS SYSBACKUP";
	```
	Enter the password for the `sbu` user when prompted.
	Note:
	To perform cross-platform transport of an encrypted tablespace, you must connect to the PDB as a common user with the `SYSDBA` or `SYSBACKUP` privilege.
2. Query the name of the destination platform in `V$TRANSPORTABLE_PLATFORM`.
	See Also:
	" Platforms that Support Cross-Platform Data Transport " for information about determining the platform name
3. Place the tablespaces to be transported in read-only mode.
	The following command places the tablespace `EXAMPLE` in read-only mode.
	```
	ALTER TABLESPACE example READ ONLY;
	```
4. Choose a method for naming the output files.
	Use the `FORMAT` clause of the `BACKUP` command to specify a pattern for naming the output files.
	See Also:
	" About Names and Locations for Restored Objects on the Destination Database "
5. If the tablespace being transported is a TDE-encrypted tablespace, then specify the passphrase that will be used to wrap the master key before storing it in the backupset.
	The following command sets the passphrase to `encr_temp`.
	`RMAN> SET PASSPHRASE ON IDENTIFIED BY encr_temp;`
6. Back up the tablespace on the source database using the `BACKUP` command with the `TO                                     PLATFORM` or `FOR TRANSPORT` clause. Use the `DATAPUMP` clause to indicate that an export dump file for the tablespaces must be created. The export dump file is created in its own backup piece.
	The following example creates a cross-platform backup of the tablespaces `projects` and `tasks` that can be restored on the Solaris\[tm\] OE (64-bit) platform. This backup is stored in the backup set `trans_ts.bck` in the `/tmp/xplat_backups` directory. The Data Pump export dump file containing metadata required to plug the tablespaces in to the destination database is stored in `trans_ts_dmp.bck` in the `/tmp/xplat_backups` directory.
	```
	RMAN > BACKUP
	          TO PLATFORM 'Solaris[tm] OE (64-bit)'
	          FORMAT '/tmp/xplat_backups/trans_ts.bck'
	          DATAPUMP FORMAT '/tmp/xplat_backups/trans_ts_dmp.bck'
	          TABLESPACE projects, tasks;
	```
	Because the `TO PLATFORM` clause is used, conversion to the endian format of the destination database is performed on the source database.
	Note:
	When you use the `DATAPUMP` clause, ensure that the target database is open.
7. Disconnect from the source database.
8. Move the backup sets created by the `BACKUP` command and the Data Pump export dump file to the destination host.
	You can use operating system utilities to move the backup sets from the source host to the destination host.
9. Connect to the destination database, into which the tablespaces must be transported, as `TARGET`.
	For tablespaces in the root, connect to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege. For tablspaces in the PDB, connect to the PDB as a common user or local user with the `SYSDBA` or `SYSBACKUP` privilege.
	In this example, `sbu` is a user who is granted the `SYSBACKUP` privilege on the destination database `prod_dest`.
	```
	% RMAN
	RMAN> CONNECT TARGET "sbu@prod_dest AS SYSBACKUP";
	```
	Enter the password for the `sbu` user when prompted.
10. If the tablespace being transported is a TDE-encyrpted tablespace, then provide the passphrase that was used on the source database to wrap the master key.
	The following example sets the passphrase to encr\_temp.
	```
	SET PASSPHRASE ON IDENTIFIED BY encr_temp;
	```
11. Restore the backup sets that were transported from the source database using the `RESTORE` command. Use the `DUMP FILE` clause to import the export dump file containing the tablespace metadata and plug the tablespaces in to the destination database.
	The following example restores the `projects` and `tasks` tablespaces from the cross-platform backup created in Step [^3]. The backup set `trans_ts.bck` in the `/tmp/xplat_restores` directory on the destination host. The Data Pump export dump file containing the metadata that is required to plug these tablespaces in to the destination database is stored in the `trans_ts_dump.bck` in the `/tmp/xplat_restores` directory.
	```
	RMAN> RESTORE
	      FOREIGN TABLESPACE projects, tasks TO NEW
	      FROM BACKUPSET '/tmp/xplat_restores/trans_ts.bck'
	      DUMP FILE FROM BACKUPSET '/tmp/xplat_restores/trans_ts_dmp.bck';
	```

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF107) for additional examples on performing cross-platform backup and restore operations

#### 28.8.2 Performing Cross-Platform Transport of Tablespaces Using Inconsistent Backups

You can transport inconsistent tablespaces across platforms using backup sets or image copies. Use the `BACKUP` command to create a cross-platform backup using backup sets.

See Also:

For more information about using scripts to perform cross-platform transport using backup sets, refer to the My Oracle Support Note 1389592.1 at [`https://support.oracle.com/rs?type=doc&id=1389592.1`](https://support.oracle.com/rs?type=doc&id=1389592.1)

##### 28.8.2.1 Overview of Cross-Platform Transport of Tablespaces Using Inconsistent Backups

You can perform cross-platform transport of read-write tablespaces. Create one or more incremental cross-platform backups when the tablespaces are in read-write mode. Then create one final incremental backup when the tablespace is in read only mode.

An inconsistent tablespace backup is a backup of one or more tablespaces that is created when the tablespaces are in read/write mode. The term inconsistent refers to the fact that data files in the backup contain changes that were made after the files were checkpointed. The foreign data files produced during a cross-platform inconsistent backup operation cannot be directly plugged in to the destination database. They must be made consistent before they can be opened on the destination database. You make the foreign data files consistent by applying a cross-platform incremental backup, created when the tablespaces are placed in read-only mode, to these foreign data files. This backup must also include the export dump file containing the metadata required for plug the transported tablespaces in to the destination database.

Inconsistent tablespace backups enable you to reduce application downtime. When the tablespaces are online and available to the users, you create cross-platform inconsistent backups on the source database. The first backup must be a level 0 incremental backup. Subsequently, create smaller level 1 incremental backups that contain the changes made to the tablespaces since the most recent level 1 backup. These level 0 and level 1 incremental backups can be restored and applied on the destination database even as other level 1 incremental backups are being created on the source database. You need not wait until all the level 1 incremental backups are created on the source database before you start applying previously-created level 1 backups on the destination database. Since the tablespaces are still online while these incremental backups are being created, there is no application downtime at this stage. The final level 1 incremental backup is created with the tablespaces placed in read-only mode. The application downtime begins at this stage. This final backup must include the metadata required to plug the tablespaces in to the destination database.

On the destination database, you first restore the level 0 incremental backup to create a set of foreign data files. Next, apply the level 1 incremental backups that were created when the tablespaces were in read/write mode to these restored foreign data files. Apply these backups in the same order in which they were created. In most cases, the destination database catches up with the last level 1 incremental backup before the final incremental backup, taken with the tablespaces placed in read-only mode, is created on the source database. The last step is to restore the final level 1 incremental backup, created when the tablespaces were placed in read-only mode, to make the foreign data files consistent. This backup contains the tablespace metadata required to plug the tablespaces in to the destination database.

The `CONVERT` command creates cross-platform backups using image copies.

About Creating Inconsistent and Incremental Backups on the Source Database

Use the `ALLOW INCONSISTENT` clause in a `BACKUP` or `CONVERT` command to create a cross-platform inconsistent backup of one or more tablespaces. The tablespaces being transported are in read/write mode when an inconsistent backup is created. To create incremental backups, use the `INCREMENTAL LEVEL 1 ` clause in the `BACKUP` command.

The first inconsistent backup is a level 0 incremental backup. Subsequently, you can create multiple cross-platform level 1 incremental backups. The final cross-platform incremental backup must be a consistent backup that is created when the tablespaces are read-only. When you create this final incremental backup, use the `DUMP FILE` clause in the `BACKUP` command to create the dump file containing the tablespace metadata.

When you use the `CONVERT` command, you must explicitly create the export dump file that contains the metadata for the tablespaces by using the Data Pump Export utility.

Note:

The `ALLOW INCONSISTENT` clause cannot be used for cross-platform whole database backups.

About Restoring and Recovering Inconsistent Backups on the Destination Database

You first restore the cross-platform level 0 incremental backup, taken when the tablespaces are placed in read/write mode, on the destination database. This operation creates restores the backup and creates foreign data file copies. These foreign data files are inconsistent because the tablespaces were not placed in read-only mode when the backup was created. To make these foreign data files consistent and achieve a consistent checkpointed SCN, apply the incremental backups in the order in which they were created. The final incremental backup applied must be a cross-platform incremental backup that was created when the tablespaces were in read-only mode. Next, to plug the tablespaces in to the destination database, you restore and import the dump file that contains the metadata of the tablespaces being transported.

##### 28.8.2.2 Requirements for Applying Cross-Platform Incremental Backups to the Restored Data Files

Certain requirements must be met to apply cross-platform incremental backups to the restore data files on the destination database.

To successfully apply a cross-platform incremental tablespace backup to a set of restored foreign data files:

- For each data file that is included in the cross-platform incremental backup, the start SCN must be lower than the current checkpoint SCN of the foreign data file copy.
- The foreign data file copies created by the restore operation must not be modified.
	For example, if a foreign data file copy has been plugged in to the destination database, made read/write, and then made read-only, then RMAN considers that this file has been modified.

##### 28.8.2.3 Steps to Transport Inconsistent Tablespaces to a Different Platform

This section describes the high-level steps to perform cross-platform transport of inconsistent tablespaces using backup sets or image copies.

Prerequisites:

- Confirm that the prerequisites for transporting inconsistent tablespaces using backup sets, described in " Performing Cross-Platform Transport of Read-Only Tablespaces Using Backup Sets ", are met.
- Confirm that conditions required to apply cross-platform incremental backups to restore data files, as described in Requirements for Applying Cross-Platform Incremental Backups to the Restored Data Files, are met.

To transport inconsistent tablespaces to a different platform:

1. Create the files required to transport one more tablespaces in the source database as described in Creating Files Required to Transport Tablespaces to a Different Platform
2. Transfer files from the source host to the destination host as described in Transferring Files Created on the Source Host to the Destination Host.
3. Restore tablespaces and plug them into the destination database as described in Restoring Tablespaces and Plugging them in to the Destination Database.

###### 28.8.2.3.1 Creating Files Required to Transport Tablespaces to a Different Platform

This step consists of performing the following tasks in the [source database](glossary.md):

1. If the tablespace being transported is a TDE-encrypted tablespace, then specify the passphrase that will be used to wrap the master key before storing it in the backupset.
	The following command sets the passphrase to `encr_temp`.
	`RMAN> SET PASSPHRASE ON IDENTIFIED BY encr_temp;`
2. Create a cross-platform level 0 inconsistent backup of the tablespaces that must be transported to a different platform. The tablespaces are in read/write mode.
	Use the `ALLOW INCONSISTENT` and `INCREMENTAL LEVEL 0` clauses in the `BACKUP` command to indicate that the backup is an inconsistent backup of one or more tablespaces.
3. Create a cross-platform level 1 incremental backup of the tablespaces that must be transported to another platform. The tablespace are in read/write mode.
	Subsequent to the first level 0 inconsistent backup, you can create any number of level 1 incremental backups when the tablespaces are in read/write mode. Use the `ALLOW INCONSISTENT` and `INCREMENTAL LEVEL 1` clause to create these incremental backups. Performing frequent incremental backups when the tablespaces are in read/write mode is advantageous because this reduces the amount of changed data that needs to be applied to the [destination database](glossary.md) using the final incremental backup that is taken when the tablespace is read-only.
4. Create a cross-platform level 1 incremental backup of the tablespaces with the tablespaces in read-only mode.
	This is the final incremental backup and it must include the dump file that contains the metadata required to plug the transported tablespaces in to the destination database. Use the `INCREMENTAL LEVEL 1` clause in the `BACKUP` command to create a level 1incremental backup.
	When you perform cross-platform transport using the `BACKUP` command, use the `DATAPUMP` clause to create the Data Pump export dump files along with the incremental backup. The dump file is created in a separate backup set. When you create cross-platform incremental backups using image copies, you must explicitly create the dump file containing tablespace metadata by using the Data Pump Export utility.

###### 28.8.2.3.2 Transferring Files Created on the Source Host to the Destination Host

Use FTP, an operating system copy command, or some other mechanism to move the backup sets, data files, and the dump file that were created in the [source database](glossary.md) to the destination host.

###### 28.8.2.3.3 Restoring Tablespaces and Plugging them in to the Destination Database

This step consists of performing the following tasks on the [destination database](glossary.md):

1. If the tablespace being transported is a TDE-encyrpted tablespace, then provide the passphrase that was used on the source database to wrap the master key.
	The following example sets the passphrase to encr\_temp.
	```
	SET PASSPHRASE ON IDENTIFIED BY encr_temp;
	```
2. Restore the cross-platform level 0 inconsistent backup.
	This restore operation creates a set of [foreign data file](glossary.md) s on the destination database. These foreign data files are inconsistent, and they need recovery before they can be plugged in to the destination database.
	Use the `RESTORE` command to restore the cross-platform level 0 inconsistent backup. When you restore a cross-platform inconsistent backups that consist of backup sets, use the `FROM BACKUPSET` clause to specify the name of the backup set that contains the level 0 inconsistent backup.
	See Also:
	[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF149) for information about using the `RESTORE` command for cross-platform restore operations
3. Apply the cross-platform level 1 incremental backup, taken when the tablespaces were in read/write mode, to the foreign data files restored in Step 1.
	If you created multiple cross-platform level 1 incremental backups, these incremental backups must be applied in the order in which they were created. Use the `RECOVER` command to apply the incremental backups. The `FOREIGN DATAFILECOPY` clause of the `RECOVER` command must list each data file to which the incremental backup must be applied. Use the `FROM BACKPSET` clause to specify the name of the backup set that contains the data to be recovered.
4. Apply the cross-platform level 1 incremental backup, taken when the tablespaces were in read-only mode, to the foreign data files restored in Step 1.
	Use the `RECOVER` command to apply the incremental backup. The `FOREIGN DATAFILECOPY` clause of the `RECOVER` command must list each data file to which the incremental backup needs to be applied. Use the `FROM BACKPSET` clause to specify the name of the backup set that contains the data to be recovered.
5. Restore the backup set containing the tablespace metadata.
	Use the `RESTORE` command to restore the backup set that contains the dump file created during the cross-platform incremental backup. The tablespaces were in read-only mode when this backup was created. You can optionally use the `DUMP FILE` clause to specify a name for the dump file on the destination database and the `DATAPUMP DESTINATION` clause to specify the directory in which the dump file is restored. If these clauses are omitted, RMAN uses the configured defaults. When transporting data using backup sets, use the `FROM BACKUPSET` clause to specify the name of the backup set that contains the dump file.
6. Import the dump file containing the tablespace metadata into the destination database.
	Plug the recovered tablespaces in to the destination database by using the Data Pump Import utility to import the dump file created during the incremental backup. You must run the Data Pump Import utility as a user with the `SYSDBA` privilege.

##### 28.8.2.4 Example: Performing Cross-Platform Inconsistent Tablespace Transport Using Backup Sets

This example transports the inconsistent tablespace `my_tbs` from the [source database](glossary.md), which is on the Sun Solaris platform, to a [destination database](glossary.md) on the Linux x86 64-bit platform.

The following steps enable you to transport the inconsistent tablespace `my_tbs` across platforms using backup sets:

1. Connect to the source database as a user who is granted the `SYSBACKUP` privilege.
	```
	RMAN> CONNECT TARGET "sbu@prod_source AS SYSBACKUP";
	```
2. Ensure that the prerequisites required to transport tablespaces to another platform are met, as described in Performing Cross-Platform Transport of Read-Only Tablespaces Using Backup Sets.
3. Create a cross-platform level 0 inconsistent backup of the tablespace `my_tbs` when the tablespace is read/write mode. This backup is stored in a backup set named `my_tbs_incon.bck` in the directory `/tmp/xplat_backups`.
	```
	BACKUP
	FOR TRANSPORT
	ALLOW INCONSISTENT
	INCREMENTAL LEVEL 0
	TABLESPACE my_tbs FORMAT '/tmp/xplat_backups/my_tbs_incon.bck';
	```
	Because `FOR TRANSPORT` is used instead of `TO PLATFORM`, this cross-platform backup can be restored on any platform. The conversion will be performed on the destination database.
4. Create a cross-platform level 1 incremental backup of the tablespace `my_tbs` that contains the changes made after backup in Step 3 was created. The tablespace is still in read/write mode. This incremental backup is stored in `my_tbs_incon1.bck` in the directory `/tmp/xplat_backups`.
	```
	BACKUP
	FOR TRANSPORT
	ALLOW INCONSISTENT
	INCREMENTAL LEVEL 1
	TABLESPACE my_tbs FORMAT '/tmp/xplat_backups/my_tbs_incon1.bck';
	```
	To minimize application downtime, the level 0 and level 1 incremental backups created in Steps 3 and 4 can be restored and applied on the destination database while the source tablespace is still in read/write mode. When the destination database catches up with last level 1 incremental backup, you can create the final incremental backup with the tablespace placed in read-only mode.
5. Place the tablespace `my_tbs` in read-only mode.
	```
	ALTER TABLESPACE my_tbs READ ONLY;
	```
6. Create the final cross-platform level 1 incremental backup of the tablespace `my_tbs`. This backup contains changes made to the database after the backup that was created in Step 4. It must include the [export dump file](glossary.md) that contains the tablespace metadata.
	```
	BACKUP
	FOR TRANSPORT
	INCREMENTAL LEVEL 1
	TABLESPACE my_tbs
	FORMAT '/tmp/xplat_backups/my_tbs_incr.bck'
	DATAPUMP FORMAT '/tmp/xplat_backups/my_tbs_incr_dp.bck';
	```
	The incremental backup is stored in `my_tbs_incr.bck`. The export dump file containing the tablespace metadata is stored in a backup set named `my_tbs_incr_dp.bck`.
	The following is a formatted output of the `BACKUP` command that was run in this step. The output is edited to display only the relevant information. Observe that the dump file is called `backup_tts_RDBMS_13462.dmp`, which is a name assigned by the operating system, and is stored in the directory specified by the `DESTINATION` clause.
	```
	Starting backup at 12-SEP-12
	……
	Performing export of metadata for specified tablespaces...
	EXPDP> Starting "SYS"."TRANSPORT_EXP_RDBMS_zocc":
	   .........
	   EXPDP>
	 ***************************************************************************
	   EXPDP> Dump file set for SYS.TRANSPORT_EXP_RDBMS_zocc is:
	   EXPDP>   /ade/b/191802369/oracle/backup_tts_RDBMS_13462.dmp
	   EXPDP>
	 **************************************************************************
	  .......
	Export completed
	.......
	……
	channel ORA_DISK_1: specifying datafile(s) in backup set
	input datafile file number=00006 name=/ade/b/191802369/oracle/dbs/tbs_11.f
	input datafile file number=00007 name=/ade/b/191802369/oracle/dbs/tbs_12.f
	input datafile file number=00020 name=/ade/b/191802369/oracle/dbs/tbs_14.f
	input datafile file number=00010 name=/ade/b/191802369/oracle/dbs/tbs_13.f
	……
	……
	Finished backup at 12-SEP-12
	```
7. Move the backup sets and the export dump file generated in Steps 3, 4, and 6 from the source host to the desired directories on the destination host.
	In this example, all the required files are moved to the directory `/tmp/xplat_restores` on the destination host.
8. Connect to the destination database as a user who is granted the `SYSBACKUP` privilege.
	```
	RMAN> CONNECT TARGET "sbu@prod_dest AS SYSBACKUP";
	```
	`sbu` is a user who is granted the `SYSBACKUP` privilege in the destination database.
9. Restore the cross-platform level 0 inconsistent backup created in Step 3.
	Use the `FOREIGN DATAFILE` clause to specify the data files that must be restored. The `FROM PLATFORM` clause specifies the name of the platform on which the backup was created. This clause is required to convert backups on the destination database.
	In this example, the data files with numbers 6, 7, 20, and 10 are restored to the names specified in the `FORMAT` clause corresponding to that data file. The data file numbers must be the numbers used on the source database. You can obtain the data file numbers from the RMAN output of the inconsistent backup created in Step 3.
	```
	RESTORE
	FROM PLATFORM 'Solaris[tm] OE (64-bit)'
	FOREIGN DATAFILE 6
	FORMAT '/tmp/aux/mytbs_6.df',
	7
	FORMAT '/tmp/aux/mytbs_7.df',
	20
	FORMAT '/tmp/aux/mytbs_20.df',
	10
	FORMAT '/tmp/aux/mytbs_10.df'
	FROM BACKUPSET '/tmp/xplat_restores/my_tbs_incon.bck';
	```
10. Recover the [foreign data file](glossary.md) s obtained in Step 9 by applying the first cross-platform level 1 incremental backup that was created Step 4.
	```
	RECOVER
	FROM PLATFORM 'Solaris[tm] OE (64-bit)'
	FOREIGN DATAFILECOPY '/tmp/aux/mytbs_6.df','/tmp/aux/mytbs_7.df','/tmp/aux/mytbs_20.df','/tmp/aux/mytbs_10.df'
	FROM BACKUPSET '/tmp/xplat_restores/my_tbs_incon1.bck';
	```
	In this example, the incremental backup that is being applied to the restored foreign data files is stored in `/tmp/xplat_restores/my_tbs_incon1.bck`.
11. Recover the foreign data files obtained in Step 9 by applying the final cross-platform level 1 incremental backup that was created in Step 6. This backup was created with the tablespaces in read-only mode.
	```
	RECOVER
	FROM PLATFORM 'Solaris[tm] OE (64-bit)'
	FOREIGN DATAFILECOPY '/tmp/aux/mytbs_6.df','/tmp/aux/mytbs_7.df','/tmp/aux/mytbs_20.df','/tmp/aux/mytbs_10.df'
	FROM BACKUPSET '/tmp/xplat_restores/my_tbs_incr.bck';
	```
	In this example, the incremental backup that is being applied to the restored foreign data files is stored in `/tmp/xplat_restores/my_tbs_incr.bck`.
12. Restore the backup set containing the export dump file. This dump file contains the tablespace metadata required to plug the tablespaces into the destination database.
	```
	RESTORE
	FROM PLATFORM 'Solaris[tm] OE (64-bit)'
	DUMP FILE 'my_tbs_restore_md.dmp'
	DATAPUMP DESTINATION '/tmp/dump'
	FROM BACKUPSET '/tmp/xplat_restores/my_tbs_incr_dp.bck';
	```
	In this example, the dump file is restored to a file called `my_tbs_restore_md.dmp` in the directory `/tmp/dump`. You can omit the name of the dump file and the `DATAPUMP DESTINATION` clause and allow RMAN to use operating-system defaults for these parameters.
13. Plug the tablespace in to the destination database. Use the Data Pump import utility to import the dump file containing the tablespace metadata in to the destination database.
	```
	# impdp directory=dp_dir dumpfile=backup_tts_RDBMS_13462.dmp transport_datafiles='/tmp/aux/mytbs_6.df','/tmp/aux/mytbs_7.df','/tmp/aux/mytbs_20.df','/tmp/aux/mytbs_10.df' nologfile=Y
	```
	When prompted for a user name and password, enter the credentials of the `SYS` user. In this example, `dp_dir` is a directory object that was created using `CREATE DIRECTORY` command and is mapped to the `/tmp` directory.

#### 28.8.3 Performing Cross-Platform Transport of Tablespaces in a PDB

RMAN enables you to transport user tablespaces contained in a PDB to a different platform by using either the `CONVERT` or `BACKUP` command. In this case, the source platform and the destination platform can use different endian formats.

Use one of the following techniques to transport a tablespace in a PDB:

- Connect to the PDB as `TARGET` and use the `BACKUP TABLESPACE` command to create a cross-platform backup of the selected tablespaces.
	See " Steps to Transport Read-Only Tablespaces to a Different Platform Using Backup Sets ".
- Connect to the PDB as `TARGET` and use the `CONVERT TABLESPACE` command to transport a read-only tablespace.
	The following command, when connected to the PDB, converts the read-only tablespace `my_tbs`:
	```
	CONVERT TABLESPACE my_tbs
	    TO PLATFORM 'Solaris[tm] OE (64-bit)'
	    FORMAT '/tmp/xplat_backups/my_tbs_%U.bck';
	```
- Connect to the PDB as `TARGET` and use the `CONVERT DATAFILE` command.
	The following command, when connected to the PDB, converts the data file `sales.df`:
	```
	CONVERT
	    FROM PLATFORM 'Solaris[tm] OE (64-bit)'
	    DATAFILE '/u01/app/oracle/oradata/orcl/sales.df'
	    FORMAT '/tmp/xplat_backups/sales_df_solaris.dat'
	```

However, when connected as `TARGET` to a PDB, you cannot use the `CONVERT DATAFILE` command to convert a tablespace that contains undo segments.

See Also:

Example: Transporting a Tablespace in a PDB

##### 28.8.3.1 Example: Transporting a Tablespace in a PDB

This example uses the `CONVERT` command to transport the tablespace `sales_tbs` from the PDB `pdb5` to the destination PDB `pdb3`. The source PDB is on a Sun Solaris platform and the destination PDB is on a Linux x86 64-bit platform.

1. Ensure that the required prerequisites are met, as described in Performing Cross-Platform Transport of Read-Only Tablespaces Using Backup Sets.
	See Also:
	[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF192) for the `CONVERT` command prerequisites
2. Start SQL\*Plus and connect to the source PDB as a user who is granted the `SYSDBA` or `SYSBACKUP` privilege.
	In this example, `sbu` is a user who has been granted the `SYSBACKUP` privilege on the source PDB `pdb5`.
	```
	% sqlplus sbu@pdb5 AS SYSBACKUP
	```
3. Query the name for the destination platform in the `V$TRANSPORTABLE_PLATFORM` view.
	In this example, the platform name for the destination platform is `Linux x86 64-bit`.
4. Verify that the tablespace that is to be transported is self-contained.
	See Also:
	[Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=ADMIN11399) for information about determining whether tablespaces are self-contained
5. Place the tablespace to be transported in read-only mode.
	```
	SQL> ALTER TABLESPACE sales_tbs READ ONLY;
	```
6. Create the directory object that is used to store the files generated by the DataPump export and import utilities.
	```
	SQL> CREATE OR REPLACE DIRECTORY xtt_dir AS '/scratch/xtt';
	Directory created.
	```
7. Start RMAN and connect to the source PDB as a user with the `SYSDBA` or `SYSBACKUP` privilege.
	The following example starts RMAN and connects to the source PDB `pdb5` as the `sbu` user who has been granted the `SYSBACKUP` privilege.
	```
	% rman
	RMAN> CONNECT TARGET "sbu@pdb5 as sysbackup"
	```
8. Convert the tablespace on the source database using the `CONVERT` command.
	The following command converts the tablespace `sales_tbs` to the destination platform Linux x86-64 bit. The converted data files are stored in `/tmp/xplat_convert/sales_tbs_conv.bck`.
	```
	RMAN> CONVERT TABLESPACE 'SALES_TBS'
	TO PLATFORM 'Linux x86 64-bit'
	FORMAT  '/tmp/xplat_convert/sales_tbs_conv.bck';
	```
9. Exit RMAN.
10. On the source database, use the DataPump export utility to create an export dump file containing the metadata for tablespace `sales_tbs`. Use the credentials of the `SYS` user to perform the export.
	The following command creates an export dump file called `sales_tbs_conv.dmp` in the location specified by the directory object `xtt_dir`. The credentials used to perform the export are that of the `SYS` user.
	```
	# expdp "'"sys@pdb5 as sysdba"'" directory=xtt_dir dumpfile=sales_tbs_conv.dmp logfile=sales_tbs_conv.log transport_tablespaces=sales_tbs
	```
11. Copy the converted data files created in Step [^4] and the export dump file created in Step [^5] to the destination PDB. You can use operating system commands to copy the files.
12. On the destination PDB, plug the tablespace into the PDB by using the DataPump import utility. Use the credentials of the `SYS` user to perform the import.
	The following example imports the metadata contained in the export dump file `sales_tbs_conv.dmp` and the converted data files in `/tmp/xplat_convert/sales_tbs_conv.bck` into the PDB `pdb3`.
	```
	#impdp "'"sys@pdb3 as sysdba"'" directory=xtt_dir dumpfile=sales_tbs_conv.dmp datafiles=/tmp/xplat_convert/sales_tbs_conv.bck
	```
13. Start SQL\*Plus and connect to the destination PDB as a user with the `SYSDBA` or `SYSBACKUP` privilege.
	The following command connects to the PDB `pdb3` as the `sbu` user who has been granted the `SYSBACKUP` privilege.
	```
	%sqlplus sbu@pdb3 as sysbackup
	```
14. Verify the status of the converted tablespace on the destination PDB.
	The following query determines the status of the tablespace `sales_tbs`.
	```
	SQL> SELECT status FROM dba_tablespaces
	     WHERE tablespace_name LIKE 'SALES_TBS';
	STATUS
	---------
	READ ONLY
	```
15. Make the tablespace `sales_tbs` in the destination PDB `pdb3` online.
	```
	SQL> ALTER TABLESPACE sales_tbs READ WRITE;
	```

### 28.9 Performing Cross-Platform Transport of Data Files Over the Network

RMAN enables you to perform cross-platform transport of data files over the network.

RMAN can connect to a source database, create the required data file backups in the backupset format, transfer them to the destination, and then restore the backups on the destination database. This task is performed by using the `FROM SERVICE` clause along with the `RESTORE FOREIGN DATAFILE` command.

You need to establish connectivity between the source database and the target database by adding the required entries to the `tnsnames.ora` and `listener.ora` files. The `COMPATIBLE` initialization parameter of the source and destination databases must be set to 12.2.

1. Open RMAN and connect `AS TARGET` to the target database (on which the data file must be restored) as a user with the `SYSDBA` or `SYSBACKUP` privilege
2. Restore the required data files by using the corresponding data files on the source database.
	The `FROM SERVICE` clause specifies the service name of the source database from which the data files must be restored.
	The following statement restores the data files 21 and 22 using data files from a source database with service name `source_db`. The `TO NEW` clause indicates that the data files restored for the specified tablespace must use new names that are different from those on the source database.
	```
	RESTORE 
	FOREIGN DATAFILE 21,22 TO NEW
	FROM SERVICE 'source_db';
	```
3. Recover the foreign data files that were restored in Step 2.
	The `FROM SERVICE` clauses specifies the service name of the source database.
	The following statement recovers the foreign data files specified by the `FOREIGN DATAFILECOPY` clause using data files in the source database whose service name is `source_db`.
	```
	RECOVER 
	FOREIGN DATAFILECOPY '/u01/oracle/oradata/db1_tbs21.dbf','/u01/oracle/oradata/db1_tbs22.db'
	FROM SERVICE 'source_db';
	```

[^1]: Run the `CONVERT` `DATABASE` command.

The following example shows a `CONVERT DATABASE` command (sample output included). The `TRANSPORT SCRIPT` parameter specifies the location of the generated SQL script that you can use to create the new database. The `TO PLATFORM` parameter indicates the platform of the [destination database](glossary.md). The `DB_FILE_NAME_CONVERT` parameter specifies the naming scheme for the generated data files.   

```
RMAN> CONVERT DATABASE
2>   NEW DATABASE 'newdb'
3>   TRANSPORT SCRIPT '/tmp/convertdb/transportscript.sql'
4>   TO PLATFORM 'Microsoft Windows IA (32-bit)'
5>   DB_FILE_NAME_CONVERT '/disk1/oracle/dbs' '/tmp/convertdb';
 
Starting conversion at source at 25-NOV-13
using channel ORA_DISK_1
 
External table SH.SALES_TRANSACTIONS_EXT found in the database
.
.
.
Directory SYS.ORACLE_HOME found in the database
Directory SYS.ORACLE_BASE found in the database
Directory SYS.LOG_FILE_DIR found in the database
.
.
.
BFILE PM.PRINT_MEDIA found in the database
 
User SYS with SYSDBA and SYSOPER privilege found in password file
User SBU with SYSBACKUP privilege found in password file
channel ORA_DISK_1: starting datafile conversion
input datafile fno=00001 name=/disk1/oracle/dbs/tbs_01.f
converted datafile=/tmp/convertdb/tbs_01.f
channel ORA_DISK_1: datafile conversion complete, elapsed time: 00:00:15
channel ORA_DISK_1: starting datafile conversion
input datafile fno=00002 name=/disk1/oracle/dbs/tbs_ax1.f
converted datafile=/tmp/convertdb/tbs_ax1.f
channel ORA_DISK_1: datafile conversion complete, elapsed time: 00:00:03
.
.
.
channel ORA_DISK_1: starting datafile conversion
input datafile fno=00016 name=/disk1/oracle/dbs/tbs_52.f
converted datafile=/tmp/convertdb/tbs_52.f
channel ORA_DISK_1: datafile conversion complete, elapsed time: 00:00:01
Edit init.ora file init_00gb3vfv_1_0.ora. This PFILE will be used to 
  create the database on the target platform
Run SQL script /tmp/convertdb/transportscript.sql on the target platform 
  to create database
To recompile all PL/SQL modules, run utlirp.sql and utlrp.sql on 
  the target platform
To change the internal database identifier, use DBNEWID Utility
Finished conversion at source at 25-NOV-13
```

[^undefined]: After `CONVERT` `DATABASE` completes, you can open the source database read/write again.

[^undefined]: Move the data files generated by `CONVERT DATABASE` to the desired locations on the destination host.

In Step 3, the command creates the files in the `/tmp/convertdb/` directory on the source host. Move these files to the directory on the destination host that will contain the destination database files.

[^undefined]: If the path to the data files is different on the destination host, then edit the transport script to refer to the new data file locations.

[^undefined]: If necessary, edit the initialization parameter file to change any settings for the destination database.

You must edit several entries at the top of the initialization parameter file when the database is moved to the destination platform. For example, the initialization parameter file may look as follows:

```
# Please change the values of the following parameters:
 control_files            = "/tmp/convertdb/cf_D-NEWDBT_id-1778429277_00gb9u2s"
 service_names            = "NEWDBT.example.com"
 db_recovery_file_dest    = "/tmp/convertdb/orcva"
 db_recovery_file_dest_size= 10737418240
 instance_name            = "NEWDBT"
 db_name                  = "NEWDBT"
 plsql_native_library_dir = "/tmp/convertdb/plsqlnld1"
```

[^undefined]: If necessary, edit the transport script to use the new names for the converted data files.

In the example in Step 3, the transport script is named `/tmp/convertdb/transportscript.sql`. You run this script on the [destination host](glossary.md) to create the database. Thus, you must edit this script with the correct names for the data files.

[^undefined]: On the destination host, start SQL\*Plus and connect to the destination database instance as `SYSDBA` or `SYSBACKUP` using operating system authentication.

For example, connect as follows:

```
SQL> CONNECT / AS SYSBACKUP
```

If you choose not to use operating system authentication, you can create a [password file](glossary.md) and then connect with a user name and password.

[^undefined]: Execute the transport script in SQL\*Plus to create the new database on the destination host.

```
SQL> @transportscript
```

[^2]: Back up the source database using the `FOR TRANSPORT` or `TO PLATFORM` clause in the `BACKUP` command. Using either of these clauses creates a [cross-platform backup](glossary.md) that uses backup sets.

The following example creates a cross-platform backup of the entire database. This backup can be restored on any supported platform that uses the same endian format as the source database. The source platform is Sun Solaris x86 64-bit. Because the `FOR TRANSPORT` clause is used, the conversion is performed on the destination database. The cross-platform database backup is stored in `db_trans.bck` in the `/tmp/xplat_backups` directory on the source host. 

```
BACKUP
FOR TRANSPORT
FORMAT '/tmp/xplat_backups/db_trans.bck'
DATABASE;
```

[^undefined]: Disconnect from the source database.

[^undefined]: Move the backup sets created by the `BACKUP` command to the destination host.

Use operating system-specific utilities to transfer the created backup sets from the source host to the destination host.

For example, if the operating system of your source and destination hosts is Linux or UNIX, use the `cp` command to move files.

[^undefined]: Connect to the destination database (to which the database must be transported) as `TARGET` and as a common user with the `SYSDBA` or `SYSBACKUP` privilege.

In this example, `sbu` is a user who is granted the `SYSBACKUP` privilege in the destination database `prod_dest`.

```
% RMAN
RMAN> CONNECT TARGET "sbu@prod_dest AS SYSBACKUP";
```

Enter the password for the `sbu` user when prompted.

[^undefined]: Ensure that the destination database is in `NOMOUNT` state.

[^undefined]: Restore the backup sets that were transferred from the source by using the `RESTORE` command with the `FOREIGN DATABASE` clause.

The following example restores the cross-platform database backup created in Step 6. The destination database uses the same endian format as the source database. The `FROM                             PLATFORM` clause specifies the name of the platform on which the backup was created. This clause is required to convert backups on the destination. The backup set containing the cross-platform database backup is stored in the `/tmp/xplat_restores` directory on the destination host. The `TO NEW` option specifies that the restored foreign data files must use new OMF-specified names in the destination database. Ensure that the `DB_CREATE_FILE_DEST` initialization parameter is set.

```
RESTORE
FROM PLATFORM 'Solaris Operating System (x86-64)'
FOREIGN DATABASE TO NEW
FROM BACKUPSET '/tmp/xplat_restores/db_trans.bck';
```

[^3]: Back up the tablespace on the source database using the `BACKUP` command with the `TO                                     PLATFORM` or `FOR TRANSPORT` clause. Use the `DATAPUMP` clause to indicate that an export dump file for the tablespaces must be created. The export dump file is created in its own backup piece.

The following example creates a cross-platform backup of the tablespaces `projects` and `tasks` that can be restored on the Solaris\[tm\] OE (64-bit) platform. This backup is stored in the backup set `trans_ts.bck` in the `/tmp/xplat_backups` directory. The Data Pump export dump file containing metadata required to plug the tablespaces in to the destination database is stored in `trans_ts_dmp.bck` in the `/tmp/xplat_backups` directory.

```
RMAN > BACKUP
          TO PLATFORM 'Solaris[tm] OE (64-bit)'
          FORMAT '/tmp/xplat_backups/trans_ts.bck'
          DATAPUMP FORMAT '/tmp/xplat_backups/trans_ts_dmp.bck'
          TABLESPACE projects, tasks;
```

Because the `TO PLATFORM` clause is used, conversion to the endian format of the destination database is performed on the source database. 

Note:

When you use the `DATAPUMP` clause, ensure that the target database is open.

[^undefined]: Disconnect from the source database.

[^undefined]: Move the backup sets created by the `BACKUP` command and the Data Pump export dump file to the destination host.

You can use operating system utilities to move the backup sets from the source host to the destination host.

[^undefined]: Connect to the destination database, into which the tablespaces must be transported, as `TARGET`.

For tablespaces in the root, connect to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege. For tablspaces in the PDB, connect to the PDB as a common user or local user with the `SYSDBA` or `SYSBACKUP` privilege.

In this example, `sbu` is a user who is granted the `SYSBACKUP` privilege on the destination database `prod_dest`.

```
% RMAN
RMAN> CONNECT TARGET "sbu@prod_dest AS SYSBACKUP";
```

Enter the password for the `sbu` user when prompted.

[^undefined]: If the tablespace being transported is a TDE-encyrpted tablespace, then provide the passphrase that was used on the source database to wrap the master key.

The following example sets the passphrase to encr\_temp.

```
SET PASSPHRASE ON IDENTIFIED BY encr_temp;
```

[^undefined]: Restore the backup sets that were transported from the source database using the `RESTORE` command. Use the `DUMP FILE` clause to import the export dump file containing the tablespace metadata and plug the tablespaces in to the destination database.

The following example restores the `projects` and `tasks` tablespaces from the cross-platform backup created in Step 6. The backup set `trans_ts.bck` in the `/tmp/xplat_restores` directory on the destination host. The Data Pump export dump file containing the metadata that is required to plug these tablespaces in to the destination database is stored in the `trans_ts_dump.bck` in the `/tmp/xplat_restores` directory.

```
RMAN> RESTORE
      FOREIGN TABLESPACE projects, tasks TO NEW
      FROM BACKUPSET '/tmp/xplat_restores/trans_ts.bck'
      DUMP FILE FROM BACKUPSET '/tmp/xplat_restores/trans_ts_dmp.bck';
```

[^4]: Convert the tablespace on the source database using the `CONVERT` command.

The following command converts the tablespace `sales_tbs` to the destination platform Linux x86-64 bit. The converted data files are stored in `/tmp/xplat_convert/sales_tbs_conv.bck`. 

```
RMAN> CONVERT TABLESPACE 'SALES_TBS'
TO PLATFORM 'Linux x86 64-bit'
FORMAT  '/tmp/xplat_convert/sales_tbs_conv.bck';
```

[^undefined]: Exit RMAN.

[^5]: On the source database, use the DataPump export utility to create an export dump file containing the metadata for tablespace `sales_tbs`. Use the credentials of the `SYS` user to perform the export.

The following command creates an export dump file called `sales_tbs_conv.dmp` in the location specified by the directory object `xtt_dir`. The credentials used to perform the export are that of the `SYS` user. 

```
# expdp "'"sys@pdb5 as sysdba"'" directory=xtt_dir dumpfile=sales_tbs_conv.dmp logfile=sales_tbs_conv.log transport_tablespaces=sales_tbs
```

[^undefined]: Copy the converted data files created in Step 8 and the export dump file created in Step 10 to the destination PDB. You can use operating system commands to copy the files.

[^undefined]: On the destination PDB, plug the tablespace into the PDB by using the DataPump import utility. Use the credentials of the `SYS` user to perform the import.

The following example imports the metadata contained in the export dump file `sales_tbs_conv.dmp` and the converted data files in `/tmp/xplat_convert/sales_tbs_conv.bck` into the PDB `pdb3`.

```
#impdp "'"sys@pdb3 as sysdba"'" directory=xtt_dir dumpfile=sales_tbs_conv.dmp datafiles=/tmp/xplat_convert/sales_tbs_conv.bck
```

[^undefined]: Start SQL\*Plus and connect to the destination PDB as a user with the `SYSDBA` or `SYSBACKUP` privilege.

The following command connects to the PDB `pdb3` as the `sbu` user who has been granted the `SYSBACKUP` privilege.

```
%sqlplus sbu@pdb3 as sysbackup
```

[^undefined]: Verify the status of the converted tablespace on the destination PDB.

The following query determines the status of the tablespace `sales_tbs`.

```
SQL> SELECT status FROM dba_tablespaces
     WHERE tablespace_name LIKE 'SALES_TBS';

STATUS
---------
READ ONLY
```

[^undefined]: Make the tablespace `sales_tbs` in the destination PDB `pdb3` online.

```
SQL> ALTER TABLESPACE sales_tbs READ WRITE;
```