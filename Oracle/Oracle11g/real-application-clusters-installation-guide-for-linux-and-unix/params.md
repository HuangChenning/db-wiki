---
title: Configuring the Server Parameter File in Oracle Real Application Clusters Environments
book: Real Application Clusters Installation Guide for Linux and UNIX
doc_id: E41962-05
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e41962/params.htm
tags:
  - oracle
  - 11g
  - real-application-clusters-installation-guide-for-linux-and-unix
---

## 5 Configuring the Server Parameter File in Oracle Real Application Clusters Environments

This chapter describes server parameter file (SPFILE) placement and configuration in Oracle Real Application Clusters (Oracle RAC) environments. This chapter contains the following topics:

## 5.1 Parameter Files and Oracle RAC

Oracle Database uses parameter settings in parameter files to determine how to control various database resources. You can use two types of files for parameter administration: the server parameter file (`SPFILE`) or one or more traditional client-side parameter files.

Oracle recommends that you manage parameters using an `SPFILE`. If you use client-side parameter files, then Oracle does not preserve parameter changes made for self-tuning after shutdown.

## 5.2 Using Server Parameter Files with Oracle RAC

By default, Oracle Database creates the `init` parameter file (`PFILE`) for each node based on one `SPFILE`. You can change parameter settings in the `SPFILE` file by using only Oracle Enterprise Manager or `ALTER SYSTEM SET` SQL statements, because the server parameter file is a binary file. Do not try to edit this file manually.

Note:

Oracle recommends that you avoid modifying the values for self-tuning parameters; overriding these settings can adversely affect performance.

If you are upgrading from a previous Oracle Database release, then review the following section about the server parameter file for Oracle RAC.

### 5.2.1 About the Server Parameter File

With Oracle Database 11g release 2 and later databases, Database Agent automatically maintains the SPFILE based on the value you specify in the srvctl command `srvctl add/modify -p` `spfile`, where `spfile` is the name of the SPFILE. You do not need to create or maintain `init` `ORACLE_SID``.ora` files.

The default location of the server parameter file (`SPFILE)` is in the following path:

```
$ORACLE_HOME/dbs/spfile$ORACLE_SID.ora
```

The default location of the server parameter file is inappropriate for Oracle RAC databases and Oracle ASM instances if you use storage on a node, because all instances must use the same server parameter file.

Instead, Oracle recommends that you use a `PFILE` in this directory:

```
$ORACLE_HOME/dbs/init$ORACLE_SID.ora
```

This path is valid for each instance and it refers to a single, shared initialization parameter file. For example, if you use NFS storage, then on a Linux or UNIX system, the file should contain an entry similar to the following:

```
SPFILE='/nfs/db/oracle_dg/dbspfile'
```

However, if you use a cluster file system, then use the following file location:

On Linux and UNIX-based systems:

```
SPFILE='/shared_mount/dbname/spfiledbname.ora'
```

In this syntax example, the variable `shared_mount` is the shared mount point, and the variable `dbname` is the database name.

To use DBCA to create your database, and to use the server parameter file, start DBCA. When the Initialization Parameters page appears, select Create server parameter file (SPFILE) under the File Locations tab. When you have made this selection, then enter either a shared file system filename, or enter the storage path in the Server Parameters Filename field.

Note:

When you use DBCA to create the server parameter file, the default `SPFILE` file name is `$ORACLE_HOME/dbs/init$ORACLE_` `SID``.ora`

## 5.3 Parameter File Search Order in Oracle RAC

Oracle Database searches for your parameter file in the following order:

1. `$ORACLE_HOME/dbs/spfile` `sid``.ora`
2. `$ORACLE_HOME/dbs/spfile.ora`
3. `$ORACLE_HOME/dbs/init` `sid``.ora`

## 5.4 Migrating to the SPFILE in Oracle RAC Environments

Migrate to the `SPFile` by creating and editing the server parameter file using the procedures described in this section. This section contains the following topics:

- Server Parameter File Placement in Oracle RAC
- Procedures for Migrating to the Server Parameter File

### 5.4.1 Server Parameter File Placement in Oracle RAC

For single-node cluster-enabled configurations, or if you are using Oracle ASM disk groups or a cluster file system, place the server parameter file in an Oracle ASM disk group or on a file system. Otherwise, place the server parameter file on a shared raw device that is at least 5 MB in size.

### 5.4.2 Procedures for Migrating to the Server Parameter File

Migrate to the `SPFILE` file by completing the following procedures:

1. Combine the initialization parameter files for all instances into one `init` `dbname``.ora` file, where `dbname` is the name of the database, by copying all shared `IFILE` contents as is. All parameters defined in your `IFILE` parameter files are global. Therefore, create them in the format parameter=value, without `SID` prefixes.
2. Copy all instance-specific parameter definitions from `init` `sid``.ora` files using the following syntax, where the variable `sid` is the `SID` of the instance:
	```
	sid.parameter=value
	```
3. If you are using a cluster file system, then Oracle recommends that you use the following command to define the location of the new SPFILE, where `spfile` is the name of the SPFILE:
	```
	srvctl modify database -p spfile
	```
	You can also create the server parameter file using the `CREATE SPFILE` statement as in the following example:
	```
	CREATE SPFILE='?/dbs/spfile_dbname.ora'
	FROM PFILE='?/dbs/initdbname.ora'
	```
	If you use Oracle ASM, then you can use the following syntax to create the server parameter file, where `disk_group_name` is the disk group name, `db_uniquename` is the database name, `dbname` is the database name, and `Oracle_home` is the Oracle home path:
	```
	CREATE SPFILE='+disk_group_name/db_uniquename/spfiledbname.ora'
	FROM PFILE='Oracle_home/dbs/initdbname.ora'
	```
	These statements read your combined `init` `dbname``.ora` file that you created by merging your IFILEs, and then transfer the settings for the parameters from the merged file into your server parameter file.
4. Oracle recommends that you use the `SPFILE` by using the `PFILE` as a pointer to the `SPFILE`. Do this by running the `STARTUP` command as in the following example, where the SID variable `sid` in the file `init` `sid``.ora` is the SID that you use in the `SPFILE` entry from Step 3. For example:
	```
	STARTUP PFILE=$ORACLE_HOME/dbs/initsid.ora
	```
	If you use this `STARTUP` command syntax, then Oracle Database uses the server parameter file entry specified in the file `init` `sid``.ora`.
	Note:
	With Oracle ASM 11g release 2 and later releases, the `SPFILE` for the Oracle ASM instance can be stored in Oracle ASM. You can also place an Oracle ASM instance `SPFILE` on a file system, or you can use a traditional client-side parameter file for each Oracle ASM instance.
	See Also:
	The [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/toc.htm) for more information about administering an Oracle ASM instance

## 5.5 Server Parameter File Errors in Oracle RAC

Oracle Database reports errors that occur during server parameter file creation, or while reading the file during startup. If an error occurs during a parameter update, then Oracle records the error in your `ALERT.LOG` file, and ignores subsequent parameter updates to the file. If this happens, then do either of the following:

- Shut down the instance, recover the server parameter file, and restart the instance.
- Enable the instance to continue running without regard for subsequent parameter updates.

Oracle Database displays errors for parameter changes that you attempt when you incorrectly use the `ALTER SYSTEM SET` statement. Oracle Database does this when an error occurs while reading from or writing to the server parameter file.

See Also:

The [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/toc.htm) for more information about backing up the `SPFILE`