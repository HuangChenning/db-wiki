---
title: Configuring the Server Parameter File in Oracle Real Application Clusters Environments
book: Real Application Clusters Installation Guide for Microsoft Windows x64 (64-Bit)
doc_id: E48195-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e48195/params.htm
tags:
  - oracle
  - 11g
  - real-application-clusters-installation-guide-for-microsoft-windows-x64-64-bit
---

## 5 Configuring the Server Parameter File in Oracle Real Application Clusters Environments

This chapter describes server parameter file (SPFILE) placement and configuration in Oracle Real Application Clusters (Oracle RAC) environments. This chapter contains the following topics:

## 5.1 About Parameter Files and Oracle RAC

Oracle Database uses parameter settings in parameter files to determine how to control various database resources. You can use two types of files for parameter administration: the SPFILE or one or more traditional client-side parameter files (PFILEs). Oracle recommends that you manage parameters using an SPFILE. If you use client-side parameter files, then Oracle does not preserve database or instance parameter changes made for performance tuning after you shut down the instance.

When you create the database, Oracle Database creates an SPFILE. The SPFILE can be stored on an Oracle Automatic Storage Management (Oracle ASM) disk group, a cluster file system, or a shared raw device. The Oracle ASM instance also uses an SPFILE.

All instances in the cluster database use the same SPFILE at startup. Because the SPFILE is a binary file, do not directly edit the SPFILE with an editor. Instead, change SPFILE parameter settings using Oracle Enterprise Manager or `ALTER SYSTEM` SQL statements.

Note:

Oracle recommends that you avoid modifying the values for self-tuning parameters; overriding these settings can affect performance adversely.

With Oracle Database 11g release 2 and later databases, Database Agent automatically maintains the SPFILE based on the value you specify in the command `srvctl add/modify` `database` `-d` `db_unique_name` `-p` `spfile`, where `spfile` is the full path name of the SPFILE and `db_unique_name` is the unique name for your Oracle RAC database. You do not have to create or maintain `init` `ORACLE_SID``.ora` files.

The default location of the database SPFILE is:

```
%ORACLE_HOME%\database\SPFILE%ORACLE_SID%.ORA
```

Using local storage for the default location of the SPFILE is inappropriate for Oracle RAC databases and Oracle ASM instances, because all database instances must use the same SPFILE. See "Storage Requirements for the Server Parameter File in Oracle RAC".

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/create.htm#ADMIN00202) for more information about managing and modifying parameter files

## 5.2 Creating Server Parameter Files for Oracle RAC

When DBCA is used to create an Oracle RAC database, DBCA creates the SPFILE in either a cluster file system or in the disk group that is assigned for data files depending on whether data files are placed in a cluster file system or in an Oracle ASM disk group.

If you manually create your database, then Oracle recommends that you create an SPFILE from a PFILE.

If you are upgrading from a previous Oracle Database release, then review the section "About Parameter Files and Oracle RAC".

## 5.3 Storage Requirements for the Server Parameter File in Oracle RAC

All instances in an Oracle RAC environment must use the same SPFILE. Place the SPFILE on shared storage, such as in an Oracle ASM disk group, a cluster file system, or on a network file system (NFS). Otherwise, place the SPFILE on a shared raw device that is at least 5 MB, although this is not recommended.

If you must use a parameter file stored on local storage on each node, then Oracle recommends that you use a PFILE. The PFILE should be located and named as follows:

```
%ORACLE_HOME%\database\init%ORACLE_SID%.ora
```

This path is valid for each instance and it refers to a single, nonshared PFILE. The PFILE should contain an entry similar to one of the following, where `dbname` is the name of the Oracle RAC database:

Shared storage accessed using the Universal Naming Convention (UNC) format:

Shared storage mapped to a network drive:

```
SPFILE='X:\dbname\spfile.ora'
```

The `SPFILE` entry directs each instance to read from a single, shared SPFILE that is located on shared storage.

## 5.4 Parameter File Search Order in Oracle RAC

Oracle RAC searches for your parameter file in the following order:

1. %ORACLE\_HOME%\\database\\spfile%ORACLE\_SID%.ora
2. %ORACLE\_HOME%\\database\\spfile.ora
3. %ORACLE\_HOME%\\database\\init%ORACLE\_SID%.ora

If you do not have a shared Oracle home for your Oracle RAC database, then the default locations for the parameter file are not shared. Therefore, you must create a nondefault SPFILE for use with Oracle RAC.

## 5.5 Migrating to an SPFILE in Oracle RAC Environments

If your Oracle RAC database does not use an SPFILE, then you can switch to using an SPFILE by creating and editing a single PFILE using the procedures described in this section.

1. Create a single PFILEs for all the instances of your Oracle RAC database using the name `init` `dbname``.ora` file, where `dbname` is the name of your Oracle RAC database. The file should be located in the `Oracle_home` `\database` directory.
2. Copy all instance-specific parameter definitions from the PFILEs files using the following syntax, where the variable `sid` is the `ORACLE_SID` for the instance:
	```
	sid.parameter=value
	```
	For example, if your Oracle RAC database is named `sales`, and the values of `ORACLE_SID` for the instances are `sales1`, `sales2`, and so on, then the instance-specific parameters copied from each PFILE would have the following format:
	```
	sales1.LICENSE_MAX_USERS=value
	sales2.LICENSE_MAX_USERS=value
	...
	```
3. Copy all shared IFILE content as is. All parameters defined in your IFILEs are global. Any parameters that have the same value for every instance are also global parameters. Therefore, create entries for these parameters in the format parameter=value, without `ORACLE_SID` prefixes.
	Note:
	The `IFILE` entry in a PFILE is used to embed another parameter file within the current parameter file. These additional parameter files are called IFILEs.
4. Shutdown your Oracle RAC database.
5. Create an SPFILE from the combined PFILE using the `CREATE SPFILE` statement in SQL\*Plus, as shown in the following example, where `dbname` is the name of the Oracle RAC database and `X:` represent a shared storage location:
	```
	CREATE SPFILE='X
	:\database\spfiledbname.ora'
	FROM PFILE='%ORACLE_HOME%\database\initdbname.ora'
	```
	If you use Oracle ASM for shared storage, then use the following SQL statement to create the SPFILE, where `disk_group_name` is the name of the Oracle ASM disk group, `db_unique_name` is the database unique name, `sid` is the `ORACLE_SID` for the Oracle RAC database, `Oracle_home` is the Oracle home path, and `init` `dbname``.ora` is the file you created in Step 1:
	```
	CREATE SPFILE='+disk_group_name\db_unique_name\spfiledbname.ora'
	FROM PFILE='%ORACLE_HOME%\database\initdbname.ora'
	```
	The `CREATE SPFILE` SQL statement reads the `init` `dbname``.ora` file that you created by merging your PFILEs and IFILEs, and then transfers the settings for the parameters from the PFILE into an SPFILE.
6. Update the local `init` `sid``.ora` file on each node to contain an `SPFILE` entry that points to the location of the new SPFILE.
	Because the SPFILE is located in a nondefault location, you must start up the database by first using a traditional parameter file that contains a single entry, `SPFILE`.
7. Start the Oracle RAC database using the `STARTUP` statement for the database and specify that the local PFILE should be used by the instance. For example, if you have set the environment variables `ORACLE_HOME` and `ORACLE_SID` for your Oracle RAC database, then you would use a SQL\*Plus statement like the following, where `ORACLE_SID` is the name of the local Oracle RAC database instance:
	```
	STARTUP PFILE=%ORACLE_HOME%\database\init%ORACLE_SID%.ora
	```
	When you use this `STARTUP` command, then the Oracle Database uses the SPFILE parameter setting in the PFILE to locate the SPFILE in the nondefault location on shared storage.
8. Finally, update the Oracle RAC database configuration so that you do not have to use a local PFILE when starting the database. To update the Oracle RAC database configuration, use the following command to define the location of the new SPFILE, where `db_unique_name` is the database unique identifier and `spfile` is the full path name of the SPFILE (the same value you used in Step 5):
	```
	%ORACLE_HOME%\bin> srvctl modify database -d db_unique_name -p spfile
	```

Note:

With Oracle ASM 11g release 2 and later releases, the SPFILE for the Oracle ASM instance can be stored in Oracle ASM. You can also place an Oracle ASM instance SPFILE on a shared file system, or you can use a traditional client-side PFILE for each Oracle ASM instance.

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/toc.htm) for more information about administering an Oracle ASM instance

## 5.6 Server Parameter File Errors in Oracle RAC

Oracle Database reports errors that occur during SPFILE creation, or while reading the file during startup. If an error occurs during a parameter update, then Oracle records the error in the database alert log file, and ignores subsequent parameter updates to the file. If this happens, then do either of the following:

- Shut down the instance, recover the SPFILE, and restart the instance.
- Enable the instance to continue running without regard for subsequent parameter updates.

Oracle Database displays errors for parameter changes that you attempt when you incorrectly use the `ALTER SYSTEM SET` statement. Oracle Database does this when an error occurs while reading from or writing to the SPFILE.

See Also:

[Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/admin.htm#RACAD819) for more information about backing up the SPFILE