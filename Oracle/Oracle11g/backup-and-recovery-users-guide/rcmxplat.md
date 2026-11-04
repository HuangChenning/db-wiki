---
title: Transporting Data Across Platforms
book: "Backup and Recovery User's Guide"
doc_id: E10642-08
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmxplat.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-users-guide
---

## 27 Transporting Data Across Platforms

You can use RMAN to transport tablespaces across platforms with different endian formats. You can also use RMAN to transport an entire database to a different platform so long as the two platforms have the same endian format.

This chapter contains the following topics:

## Overview of Cross-Platform Data Transportation

This section explains the basic concepts and tasks involved in transporting tablespaces and databases across platforms.

### Purpose of Cross-Platform Data Transportation

You can transport tablespaces in a database that runs on one platform into a database that runs on a different platform. Typical uses of cross-platform transportable tablespaces include the following:

- Publishing structured data as transportable tablespaces for distribution to customers, who can convert the tablespaces for integration into their existing databases regardless of platform
- Moving data from a large data warehouse server to data marts on smaller computers such as Linux-based workstations or servers
- Sharing read-only tablespaces across a heterogeneous cluster in which all hosts share the same endian format

A full discussion of transportable tablespaces, their uses, and the different techniques for creating and using them is found in [Oracle Database Administrator's Guide.](https://docs.oracle.com/cd/E11882_01/server.112/e25494/tspaces.htm#ADMIN01101)

You can also use RMAN to transport an entire database from one platform to another. For example, business requirements demand that you run your databases on less expensive servers that use a different platform. In this case, you can use RMAN to transport the entire database rather than re-create it and use import utilities or transportable tablespaces to repopulate the data.

You can convert a database on the destination host or source host. Reasons for converting on the destination host include:

- Avoiding performance overhead on the source host due to the conversion process
- Distributing a database from one source system to multiple recipients on several different platforms
- Evaluating a migration path for a new platform

### Basic Concepts of Cross-Platform Data Transportation

You must use the RMAN `CONVERT` command in a transportable tablespace operation when the [source platform](glossary.md) is different from the [destination platform](glossary.md) and the endian formats are different. If you are converting part of the database between platforms that have the same endian format, you can use operating system methods to copy the files from the source to the destination. If you are converting an entire, same endian database, any data files with undo information must be converted. You cannot copy the data files directly from the source to the destination platform.

#### Tablespace and Data File Conversion

You can perform tablespace conversion with the RMAN `CONVERT` `TABLESPACE` command on the source host, but not on the destination host. The `CONVERT TABLESPACE` command does not perform in-place conversion of data files. Rather, the command produces output files in the correct format for use on the destination platform. The command does not alter the contents of data files in the source database.

You can use the `CONVERT` `DATAFILE` command to convert files on the destination host, but not on the source host. The Data Pump Export utility generates an [export dump file](glossary.md) that, with data files manually copied to the destination host, can be imported into the destination database. Until the data files are transported into the destination database, the data files are not associated with a tablespace name in the database. In this case, RMAN cannot translate the tablespace name into a list of data files. Therefore, you must use `CONVERT` `DATAFILE` and identify the data files by file name.

Note:

Using `CONVERT TABLESPACE` or `CONVERT DATAFILE` is only one step in using cross-platform transportable tablespaces. Read the discussion of transportable tablespaces in [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/tspaces.htm#ADMIN01101) in its entirety before attempting to follow the procedures in this chapter.

#### Database Conversion

To convert a whole database to a different platform, both platforms must use the same endian format. The RMAN `CONVERT` `DATABASE` command automates the movement of an entire database from a source platform to a destination platform. The transported database contains the same data as the source database and also has, with a few exceptions, the same settings as the source database.

Files automatically transported to the destination platform include:

- Data files that belong to permanent tablespaces
	Unlike transporting tablespaces across platforms, transporting entire databases requires that certain types of blocks, such as blocks in undo segments, be reformatted to ensure compatibility with the destination platform. Even though the endian formats for the source and destination platforms are the same, the data files for a transportable database must undergo a conversion process. You cannot simply copy data files from one platform to another as you can when transporting tablespaces.
- Initialization parameter file or server parameter file
	If the database uses a text-based initialization parameter file, then RMAN transports it. If the database uses a server parameter file, then RMAN generates an initialization parameter file based on the server parameter file, transports it and creates a new server parameter file at the destination based on the settings in the initialization parameter file.
	Usually, some parameters in the initialization parameter file require manual updating for the new database. For example, you may change the `DB_NAME` and parameters such as `CONTROL_FILES` that indicate the locations of files on the destination host.

You can convert the format of the data files either on the source platform or on the destination platform. The `CONVERT DATABASE ON DESTINATION PLATFORM` command does not convert the format of data files. Rather, it generates scripts that you can run manually to perform the conversion. The `CONVERT SCRIPT` parameter creates a [convert script](glossary.md) that you can manually execute at the destination host to convert data file copies in batch mode. The `TRANSPORT SCRIPT` parameter generates a [transport script](glossary.md) that contains SQL statements to create the new database on the destination platform.

## Performing Cross-Platform Tablespace Conversion on the Source Host

See the list of `CONVERT` command prerequisites described in [Oracle Database Backup and Recovery Reference.](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta012.htm#RCMRF192) Meet all these prerequisites before doing the steps in this section.

For purposes of illustration, assume that you must transport tablespaces `finance` and `hr` from source database `prod_source`, which runs on a Sun Solaris host. You plan to transport them to destination database `prod_dest` running on a Linux PC. You plan to store the converted data files in the temporary directory `/tmp/transport_linux/` on the source host.

To perform cross-platform tablespace conversion on the source host:

1. Start SQL\*Plus and connect to the source database `prod_source` with administrator privileges.
2. Query the name for the destination platform in the `V$TRANSPORTABLE_PLATFORM` view.
	The database has a list of its own internal names for each platform supporting cross-platform data transport. You may need the exact name of the source or destination platform as a parameter to the `CONVERT` command. Query `V$TRANSPORTABLE_PLATFORM` to get the platform names. The following example queries Linux platform names:
	```
	SELECT PLATFORM_ID, PLATFORM_NAME, ENDIAN_FORMAT
	FROM   V$TRANSPORTABLE_PLATFORM 
	WHERE  UPPER(PLATFORM_NAME) LIKE '%LINUX%';
	```
	The `PLATFORM_NAME` for Linux on a PC is `Linux IA (32-bit)`.
3. Place the tablespaces to be transported in read-only mode. For example, enter:
	```
	ALTER TABLESPACE finance READ ONLY;
	ALTER TABLESPACE hr READ ONLY;
	```
4. Choose a method for naming the output files.
	You must use the `FORMAT` or `DB_FILE_NAME_CONVERT` arguments to the `CONVERT` command to control the names of the output files. The rules are listed in order of precedence:
	1. Files that match any patterns provided in `CONVERT ... DB_FILE_NAME_CONVERT` clause are named based upon this pattern.
		2. If you specify a `FORMAT` clause, then any file not named based on patterns provided in `CONVERT ... DB_FILE_NAME_CONVERT` clause is named based on the `FORMAT` pattern.
	Note:
	You cannot use `CONVERT ... DB_FILE_NAME_CONVERT` to generate output file names for the `CONVERT` command when the source and destination files have Oracle Managed File names.
5. Start RMAN and connect to the source database (not the destination database) as `TARGET`. For example, enter:
	```
	% rman
	RMAN> CONNECT TARGET SYS@prod_source
	```
6. Run the `CONVERT TABLESPACE` command to convert the data files into the endian format of the destination host.
	In the following example, the `FORMAT` argument controls the name and location of the converted data files:
	```
	RMAN> CONVERT TABLESPACE finance,hr
	2>   TO PLATFORM 'Linux IA (32-bit)'
	3>   FORMAT '/tmp/transport_linux/%U';
	```
	The result is a set of converted data files in the `/tmp/transport_linux/` directory, with data in the correct endian format for the Linux IA (32-bit) platform.
	See Also:
	[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta012.htm#RCMRF192) for the full semantics of the `CONVERT` command
7. Follow the rest of the general outline for transporting tablespaces:
	1. Use the Oracle Data Pump Export utility to create the export dump file on the source host.
		2. Move the converted data files and the export dump file from the source host to the desired directories on the destination host.
		3. Plug the tablespace into the new database with the Import utility.
		4. If applicable, place the transported tablespaces into read/write mode.

## Performing Cross-Platform Data File Conversion on the Destination Host

See the list of `CONVERT` command prerequisites described in [Oracle Database Backup and Recovery Reference.](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta012.htm#RCMRF192) Meet these prerequisites before doing the steps in this section.

### About Cross-Platform Data File Conversion on the Destination Host

Data file conversion necessitates that you choose a technique for naming the output files. You must use the `FORMAT` or `DB_FILE_NAME_CONVERT` arguments to the `CONVERT` command to control the naming of output files. The rules are listed in order of precedence:

1. Files that match any patterns provided in `CONVERT ... DB_FILE_NAME_CONVERT` clause are named based upon this pattern.
2. If you specify a `FORMAT` clause, then any file not named based on patterns provided in `CONVERT ... DB_FILE_NAME_CONVERT` clause is named based on the `FORMAT` pattern.

Note:

You cannot use `CONVERT ... DB_FILE_NAME_CONVERT` to generate output file names for the `CONVERT` command when both the source and destination files are Oracle Managed Files.

If the source and destination platforms differ, then you must specify the `FROM PLATFORM` parameter. View platform names by querying the `V$TRANSPORTABLE_PLATFORM`. The `FROM PLATFORM` value must match the format of the data files to be converted to avoid an error. If you do not specify `FROM PLATFORM`, then this parameter defaults to the value of the destination platform.

### Using CONVERT DATAFILE to Convert Data File Formats

This section explains how to use the `CONVERT DATAFILE` command. The section assumes that you intend to transport tablespaces `finance` (data files `fin/fin01.dbf` and `fin/fin02.dbf`) and `hr` (data files `hr/hr01.dbf` and `hr/hr02.dbf`) from a source database named `prod_source`. The database runs on a Sun Solaris host. You plan to transport these tablespaces into a destination database named `prod_dest`, which runs on a Linux PC. You plan to perform conversion on the destination host.

When the data files are plugged into the destination database, you plan to store them in `/orahome/dbs` and preserve the current directory structure. That is, data files for the `hr` tablespace are stored in the `/orahome/dbs/hr` subdirectory, and data files for the `finance` tablespace are stored in the `/orahome/dbs/fin` directory.

To perform cross-platform data file conversion on the destination host:

1. Start SQL\*Plus and connect to the source database `prod_source` with administrator privileges.
2. Query the name for the source platform in `V$TRANSPORTABLE_PLATFORM`.
	The database has a list of its own internal names for each platform supporting cross-platform data transport. You may need the exact name of the source or destination platform as a parameter to the `CONVERT` command. For example, you can obtain the platform name of the connected database as follows:
	```
	SELECT PLATFORM_NAME
	FROM   V$TRANSPORTABLE_PLATFORM 
	WHERE  PLATFORM_ID =
	       ( SELECT PLATFORM_ID
	         FROM   V$DATABASE );
	```
	For this scenario, assume that the `PLATFORM_NAME` for the source host is `Solaris[tm] OE (64-bit)`.
3. Identify the tablespaces to be transported from the source database and place them in read-only mode.
	For example, enter the following SQL statements to place `finance` and `hr` in read-only mode:
	```
	ALTER TABLESPACE finance READ ONLY;
	ALTER TABLESPACE hr READ ONLY;
	```
4. On the source host, use Data Pump Export to create the export dump file
	In this example, the dump file is named `expdat.dmp`.
5. Make the export dump file and the data files to be transported available to the destination host.
	You can use NFS to make the dump file and current database files (not copies) accessible. Alternatively, you can use an operating system utility to copy these files to the destination host.
	In this example, you store the files in the `/tmp/transport_solaris/` directory of the destination host. You preserve the subdirectory structure from the original location of the files, that is, the data files are stored as:
	- `/tmp/transport_solaris/fin/fin01.dbf`
		- `/tmp/transport_solaris/fin/fin02.dbf`
		- `/tmp/transport_solaris/hr/hr01.dbf`
		- `/tmp/transport_solaris/hr/hr02.dbf`
6. Start RMAN and connect to the destination database (not the source database) as `TARGET`. For example, enter the following command:
	```
	% rman
	RMAN> CONNECT TARGET SYS@prod_dest
	```
7. Execute the `CONVERT DATAFILE` command to convert the data files into the endian format of the destination host.
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
	9>   FROM PLATFORM 'Solaris[tm] OE (64-bit)
	```
	The result is a set of converted data files in the `/orahome/dbs/` directory that are named as follows:
	- `/orahome/dbs/fin/fin01.dbf`
		- `/orahome/dbs/fin/fin02.dbf`
		- `/orahome/dbs/hr/hr01.dbf`
		- `/orahome/dbs/hr/hr02.dbf`
8. Follow the rest of the general outline for transporting tablespaces:
	1. Plug the tablespace into the new database with the Import utility.
		2. If applicable, place the transported tablespaces into read-only mode.

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta012.htm#RCMRF192) for the syntax and semantics of the `CONVERT` command

## Checking the Database Before Cross-Platform Database Conversion

As explained in "Basic Concepts of Cross-Platform Data Transportation", you can use the RMAN `CONVERT DATABASE` command to automate the copying of an entire database from one platform to another.

Before converting the database, see the list of `CONVERT DATABASE` command prerequisites described in [Oracle Database Backup and Recovery Reference.](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta012.htm#RCMRF192) Confirm that you meet all these prerequisites before attempting the procedure in this section.

One prerequisite is that both the source and destination platform must share the same endian format. For example, you can transport a database from Microsoft Windows to Linux for x86 (both little-endian), or from HP-UX to AIX (both big-endian), but not from HP-UX to Linux for x86 (big-endian to little-endian).

Note:

If you cannot use the `CONVERT DATABASE` command because the platforms do not share endian formats, then you can create a database on a destination platform manually and transport needed tablespaces from the source database with cross-platform transportable tablespaces.

When you transport entire databases, note that certain files require RMAN conversion to ensure compatibility with the destination platform. Even though the endian formats for the source and destination platform are the same, these files cannot be simply copied from the source to the destination system. The following kinds of files require RMAN conversion:

- Any file containing undo segments
- Any file containing automatic segment space management (ASSM) segment headers that is being transported to or from the HP Tru64 platform

The `CONVERT DATABASE` command, by default, processes all data files in the database using RMAN conversion. The RMAN conversion copies the files from one location to another, even when it does not make any changes to the file. If you have other preferred means to copy those files that do not require RMAN conversion, you can use the `SKIP UNNECESSARY DATAFILES` option of the `CONVERT DATABASE` command. If you select this option, then the `CONVERT DATABASE` command only processes the kinds of files previously mentioned. All other files must be copied by the user from the source to the destination database.

The files should be copied while the source database is open in read-only mode. Similarly, if the conversion is performed at the destination, all data files should be copied to the destination when the source database is open in read-only mode.

To prepare for database conversion:

1. Start a SQL\*Plus session as `SYSDBA` on the source database.
2. Open the database in read-only mode.
	```
	ALTER DATABASE OPEN READ ONLY;
	```
3. Ensure that server output is on in SQL\*Plus.
	For example, enter the following SQL\*Plus command:
	```
	SET SERVEROUTPUT ON
	```
4. Execute the `DBMS_TDB.CHECK_DB` function.
	This check ensures that no conditions would prevent the transport of the database, such as incorrect compatibility settings, in-doubt or active transactions, or incompatible endian formats between the source platform and destination platform.
	You can call `CHECK_DB` without arguments to see if a condition at the source database prevents transport. You can also call this function with the arguments shown in Table 27-1.
	Table 27-1 CHECK\_DB Function Parameters
	| Parameter | Description |
	| --- | --- |
	| `target_platform_name` | The name of the destination platform as it appears in the [`V$DB_TRANSPORTABLE_PLATFORM`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1109.htm#REFRN30376) view.  This parameter is optional, but is required when the `skip_option` parameter is used. If omitted, it is assumed that the destination platform is compatible with the source platform, and only the conditions not related to platform compatibility are tested. |
	| `skip_option` | Specifies which, if any, parts of the database to skip when checking whether the database can be transported. Supported values (of type `NUMBER`) are:  - `SKIP_NONE` (or `0`), which checks all tablespaces - `SKIP_OFFLINE` (or `2`), which skips checking data files in offline tablespaces - `SKIP_READONLY` (or `3`), which skips checking data files in read-only tablespaces |
	Example 27-1 illustrates executing `CHECK_DB` on a 32-bit Linux platform for transporting a database to 32-bit Windows, skipping read-only tablespaces.
	Example 27-1 Executing DBMS\_TDB.CHECK\_DB
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
5. Examine the output to learn why the database cannot be transported, fix the problem if possible, and then return to the Step 4. See the [`DBMS_TDB`](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_tdb.htm#ARPLS650) documentation for the conditions present.
6. Execute the `DBMS_TDB.CHECK_EXTERNAL` function to identify any external tables, directories, or BFILEs. RMAN cannot automate the transport of these files, so you must copy the files manually and re-create the database directories.
	Example 27-2 shows how to call the `DBMS_TDB.CHECK_EXTERNAL` function.
	Example 27-2 Executing DBMS\_TDB.CHECK\_EXTERNAL
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

## Converting Data Files on the Source Host When Transporting a Database

When you transport entire databases, certain types of blocks, such as blocks in undo segments, must be reformatted to ensure compatibility with the destination platform. Even though the endian formats for the source and destination platform are the same, the data files for a transportable database must undergo a conversion process. You cannot simply copy data files from one platform to another as you can when transporting tablespaces.

Data files with undo information and those from the HP Tru64 platform must be converted. By default, all data files are converted when the `CONVERT DATABASE` command is executed. If, however, `SKIP UNNECESSARY DATAFILES` is used in the `CONVERT DATABASE` command, then the data files with undo segments and those from the HP Tru64 platform are converted. The data files without undo segments can be copied to the new database using FTP, an operating system copy command, or some other mechanism.

This section assumes that you have already met all of the `CONVERT DATABASE` prerequisites and followed the steps in "Checking the Database Before Cross-Platform Database Conversion". The goal of this procedure is to convert the format of data files on the source host as part of a cross-platform database transport.

Assume that you want to convert a database running on Solaris to a database that runs on Windows.

To convert the database on the source platform:

1. Open the source database in read-only mode.
	```
	ALTER DATABASE OPEN READ ONLY;
	```
2. Start RMAN and connect to the source database as `TARGET`. For example, enter the following commands:
	```
	% rman
	RMAN> CONNECT TARGET SYS@source_db
	```
3. Run the `CONVERT` `DATABASE` command.
	Example 27-3 shows a `CONVERT DATABASE` command (sample output included). The `TRANSPORT SCRIPT` parameter specifies the location of the generated SQL script that you can use to create the new database. The `T` `O PLATFORM` parameter indicates the platform of the destination database. The `DB_FILE_NAME_CONVERT` parameter specifies the naming scheme for the generated data files.
	Example 27-3 Converting a Database on the Source Host
	```
	RMAN> CONVERT DATABASE
	2>   NEW DATABASE 'newdb'
	3>   TRANSPORT SCRIPT '/tmp/convertdb/transportscript.sql'
	4>   TO PLATFORM 'Microsoft Windows IA (32-bit)'
	5>   DB_FILE_NAME_CONVERT '/disk1/oracle/dbs' '/tmp/convertdb';
	 
	Starting convert at 25-NOV-06
	using channel ORA_DISK_1
	 
	External table SH.SALES_TRANSACTIONS_EXT found in the database
	 
	Directory SYS.DATA_PUMP_DIR found in the database
	Directory SYS.MEDIA_DIR found in the database
	Directory SYS.DATA_FILE_DIR found in the database
	Directory SYS.LOG_FILE_DIR found in the database
	 
	BFILE PM.PRINT_MEDIA found in the database
	 
	User SYS with SYSDBA and SYSOPER privilege found in password file
	User OPER with SYSDBA privilege found in password file
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
	Run SQL script /tmp/convertdb/transportscript.sql on the destination platform 
	  to create database
	Edit init.ora file init_00gb3vfv_1_0.ora. This PFILE will be used to 
	  create the database on the destination platform
	To recompile all PL/SQL modules, run utlirp.sql and utlrp.sql on 
	  the destination platform
	To change the internal database identifier, use DBNEWID Utility
	Finished backup at 25-NOV-06
	```
4. After `CONVERT` `DATABASE` completes, you can open the source database read/write again.
5. Move the data files generated by `CONVERT DATABASE` to the desired locations on the destination host.
	In Example 27-3, the command creates the files in the `/tmp/convertdb/` directory on the source host. Move these files to the directory on the destination host that will contain the destination database files.
6. If the path to the data files is different on the destination host, then edit the transport script to refer to the new data file locations.
7. If necessary, edit the initialization parameter file to change any settings for the destination database.
	You should edit several entries at the top of the initialization parameter file when the database is moved to the destination platform. For example, the initialization parameter file may look as follows:
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
8. If necessary, edit the transport script to use the new names for the converted data files.
	In Example 27-3, the transport script is named `/tmp/convertdb/transportscript.sql`. You run this script on the destination host to create the database. Thus, you must edit this script with the correct names for the data files.
9. On the destination host, start SQL\*Plus and connect to the destination database instance as `SYSDBA` using operating system authentication.
	For example, connect as follows:
	```
	SQL> CONNECT / AS SYSDBA
	```
	If you choose not to use operating system authentication, then you must first configure Oracle Net files, create a [password file](glossary.md), and start the listener. You can then connect to the instance with a net service name.
10. Execute the transport script in SQL\*Plus to create the new database on the destination host.
	```
	SQL> @transportscript
	```

When the transport script finishes, the creation of the new database is complete.

## Converting Data Files on the Destination Host When Transporting a Database

This section assumes that you have already met all of the `CONVERT DATABASE` command prerequisites and followed the steps in "Checking the Database Before Cross-Platform Database Conversion". The goal of this procedure is to convert the format of data files on the destination host as part of a cross-platform database transport.

Perform the data file conversion in the following phases:

1. Performing Preliminary Data File Conversion Steps on the Source Host
2. Converting Data Files on the Destination Host

### Performing Preliminary Data File Conversion Steps on the Source Host

In this procedure, you execute the `CONVERT DATABASE` command on the source host. This command generates an initialization parameter file and scripts that you can edit for use on the destination host. You also copy the unconverted data files from the source host to the destination host.

To perform preliminary data file conversion steps on the source host:

1. Ensure that the database is open in read-only mode.
2. Start RMAN and connect to the source database as `TARGET`.
	For example, enter the following commands:
	```
	% rman
	RMAN> CONNECT TARGET SYS@source_db
	```
3. Run the `CONVERT` `DATABASE ON DESTINATION PLATFORM` command.
	Example 27-4 shows a sample `CONVERT DATABASE` command (sample output included). The `ON DESTINATION PLATFORM` parameter specifies that any `CONVERT` commands required for data files should be performed on the destination platform rather than the source platform. The `FORMAT` parameter specifies the naming scheme for the generated files.
	Example 27-4 Executing CONVERT DATABASE ON DESTINATION PLATFORM
	```
	RMAN> CONVERT DATABASE
	2>   ON DESTINATION PLATFORM
	3>   CONVERT SCRIPT '/tmp/convertdb/convertscript-target'
	4>   TRANSPORT SCRIPT '/tmp/convertdb/transportscript-target'
	5>   NEW DATABASE 'newdbt'
	6>   FORMAT '/tmp/convertdb/%U';
	 
	Starting convert at 28-JAN-05
	using target database control file instead of recovery catalog
	allocated channel: ORA_DISK_1
	channel ORA_DISK_1: sid=39 devtype=DISK
	 
	External table SH.SALES_TRANSACTIONS_EXT found in the database
	 
	Directory SYS.DATA_PUMP_DIR found in the database
	Directory SYS.MEDIA_DIR found in the database
	Directory SYS.DATA_FILE_DIR found in the database
	Directory SYS.LOG_FILE_DIR found in the database
	 
	BFILE PM.PRINT_MEDIA found in the database
	 
	User SYS with SYSDBA and SYSOPER privilege found in password file
	User OPER with SYSDBA privilege found in password file
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
	Run SQL script /tmp/convertdb/transportscript-target on the destination platform to create database
	Edit init.ora file /tmp/convertdb/init_00gb9u2s_1_0.ora. This PFILE will be used to create the database on the destination platform
	Run RMAN script /tmp/convertdb/convertscript-target on destination platform to convert datafiles
	To recompile all PL/SQL modules, run utlirp.sql and utlrp.sql on the destination platform
	To change the internal database identifier, use DBNEWID Utility
	Finished backup at 28-JAN-05
	```
	The command in Example 27-4 creates a transport script, an initialization parameter file for the new database, and a convert script containing RMAN `CONVERT DATAFILE` commands for each data file being converted.
	Note:
	`CONVERT` `DATABASE` `ON` `DESTINATION` `PLATFORM` does not produce converted data file copies. The command only creates scripts.
4. Use an operating system utility to copy the following files to a temporary location on the destination host:
	- The data files to be converted
		- The convert script
		- The transport script
		- The initialization file for the destination database
5. Make the source database read/write.

### Converting Data Files on the Destination Host

This section explains how to use the script created in the previous section to convert the data files on the destination host.

The convert script created in the previous phase uses the original data file names of the source database files. The `FORMAT` parameter specifies the name that was generated with the `FORMAT` or `DB_FILE_NAME_CONVERT` parameter of the `CONVERT DATABASE` command.

If the data files of the source database are accessible from the destination host with the same path names, then so long as the source database is read-only you can run the convert script on the destination host without any changes. For example, if the source and destination hosts both use NFS to mount a disk containing the source data files, and if the mount point for both hosts is `/fs1/dbs/`, then no editing is needed.

To convert the data files on the destination host:

1. If necessary, edit the convert script.
	In the script, one `CONVERT` `DATAFILE` command exists for each data file to be converted. The convert script should indicate the current temporary file names of the unconverted data files and the output file names of the converted data files. A typical convert script looks as follows:
	```
	RUN
	{
	 CONVERT
	 FROM PLATFORM 'Linux IA (32-bit)'
	 PARALLELISM 10
	  DATAFILE '/disk1/oracle/dbs/tbs_01.f'
	  FORMAT
	 '/tmp/convertdb/data_D-TV_I-1778429277_TS-SYSTEM_FNO-1_7qgb9u2s';
	 
	 DATAFILE '/disk1/oracle/dbs/tbs_ax1.f'
	 FORMAT
	 '/tmp/convertdb/data_D-TV_I-1778429277_TS-SYSAUX_FNO-2_7rgb9u2s';
	 
	 DATAFILE '/disk1/oracle/dbs/tbs_03.f'
	 FORMAT
	 '/tmp/convertdb/data_D-TV_I-1778429277_TS-SYSTEM_FNO-17_7sgb9u2s';
	 
	 DATAFILE '/disk1/oracle/dbs/tbs_51.f'
	 FORMAT
	 '/tmp/convertdb/data_D-TV_I-1778429277_TS-TBS_5_FNO-15_8egb9u2u';
	 
	 DATAFILE '/disk1/oracle/dbs/tbs_52.f'
	  FORMAT
	 '/tmp/convertdb/data_D-TV_I-1778429277_TS-TBS_5_FNO-16_8fgb9u2u';
	}
	```
	Edit each `DATAFILE` command in the convert script to specify the temporary location of each data file as input. Also, edit the `FORMAT` parameter of each command to specify the desired final location of the data files of the transported database.
2. If necessary, edit the initialization parameter file on the destination host to change settings for the destination database.
	You should edit several entries at the top of the initialization parameter file before moving the database to the destination platform. For example, the initialization parameter file may look as follows:
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
4. Start RMAN and connect to the destination database (not the source database) as `TARGET`. For example, enter the following command:
	```
	% rman
	RMAN> CONNECT TARGET SYS@prod_dest
	```
5. Run the convert script at the RMAN prompt. For example, enter the following command:
	```
	RMAN> @/tmp/convertdb/convertscript-target
	```
6. Shut down the database instance.
	This step is necessary because the transport script that must execute already includes a `STARTUP NOMOUNT` command.
7. If necessary, edit the transport script to use the new names for the converted data files.
	In Example 27-3, the transport script is `/tmp/convertdb/transportscript.sql`. You run this script on the destination host to create the database. Thus, you must edit this script with the correct names for the data files.
8. Execute the transport script in SQL\*Plus.
	For example, create the new database on the destination host as follows:
	```
	SQL> @/tmp/convertdb/transportscript
	```

When the transport script completes, the destination database is created.