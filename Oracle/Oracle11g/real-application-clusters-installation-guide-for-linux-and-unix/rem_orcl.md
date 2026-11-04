---
title: Removing Oracle Real Application Clusters Software
book: Real Application Clusters Installation Guide for Linux and UNIX
doc_id: E41962-05
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e41962/rem_orcl.htm
tags:
  - oracle
  - 11g
  - real-application-clusters-installation-guide-for-linux-and-unix
---

## 8 Removing Oracle Real Application Clusters Software

This chapter describes how to completely remove all Oracle databases, instances, and software from an Oracle Real Application Clusters (Oracle RAC) Oracle home directory.

This chapter contains the following topics:

See Also:

The product-specific documentation if you want to remove a single product to ensure that you are aware of requirements and restrictions that apply for that product

## 8.1 Overview of Deinstallation Procedures

To completely remove all Oracle databases, instances, and software from an Oracle home directory:

- Identify all instances associated with the Oracle home
- Shut down processes
- Remove listeners installed in the Oracle Database home
- Remove database instances
- Remove Oracle Automatic Storage Management (11.1 or earlier)
- Remove Oracle Clusterware and Oracle Automatic Storage Management (Oracle Grid Infrastructure)

Note:

You cannot remove or uninstall the Oracle Database Vault option. However, you can disable it. Refer to the Oracle Database Vault Administrator's Guide for more details.

You can remove Oracle Configuration Manager. Refer to the Oracle Configuration Manager Installation and Administration Guide for more details.

With release 11.2 and later, Oracle Automatic Storage Management and Oracle Clusterware comprise the Oracle Grid Infrastructure installation. These components are installed and removed together.

Caution:

If any cluster member node has more than one database with the same global database name (GDN) on a server, then you cannot use the deinstall tool to remove one database only. For example, if you have a standalone database on one of your cluster nodes with the GDN `mydb.example.com`, and your Oracle RAC database GDN is also `mydb.example.com`, then both databases on that node are removed.

## 8.2 Identifying All Instances On a Cluster

To identify all instances associated with the Oracle home that you want to remove, enter the following command:

AIX, HP-UX, or Linux:

```
$ more /etc/oratab
```

Solaris

```
$ more /var/opt/oracle/oratab
```

The output of this command contains entries similar to the following:

```
+ASM1:/u01/app/grid/11.2.0:N
CUST:/u01/app/oracle/product/11.2.0/dbhome_1:N
```

These entries show that the `+ASM` Oracle Automatic Storage Management instance in the Oracle Grid Infrastructure for a cluster home (`/u01/app/grid/11.2.0`) and the `CUST` Oracle database instance are associated with the Oracle home directory `/u01/app/oracle/product/11.2.0/dbhome_1`.

## 8.3 Deinstalling Oracle RAC Software

The Deinstallation Tool removes Oracle Clusterware and Oracle Automatic Storage Management (Oracle ASM) from your server, as well as Oracle Real Application Clusters (Oracle RAC) or standalone Oracle Database installations. The following sections describe the script, and provide information about additional options to use the tool:

- About the Deinstallation Tool
- Example of Running the Deinstall Command for Oracle RAC
- Example of a Deinstallation Parameter File for Oracle RAC

### 8.3.1 About the Deinstallation Tool

The Deinstallation Tool (`deinstall`) stops Oracle software, and removes Oracle software and configuration files on the operating system. It is available in the installation media before installation, and is available in Oracle home directories after installation. It is located in the path `$ORACLE_HOME/deinstall`.

Caution:

When you run the deinstall command, if the central inventory (oraInventory) contains no other registered homes besides the home that you are deconfiguring and removing, then the deinstall command removes the following files and directory contents in the Oracle base directory of the Oracle RAC installation owner:
- admin
- cfgtoollogs
- checkpoints
- diag
- oradata
- flash\_recovery\_area

Oracle strongly recommends that you configure your installations using an Optimal Flexible Architecture (OFA) configuration, and that you reserve Oracle base and Oracle home paths for exclusive use of Oracle software. If you have any user data in these locations in the Oracle base that is owned by the user account that owns the Oracle software, then the deinstall command deletes this data.

The `deinstall` command stops Oracle software, and removes Oracle software and configuration files on the operating system. The command uses the following syntax, where variable content is indicated by italics:

```
deinstall -home complete path of Oracle home [-silent] [-checkonly] [-local]
[-paramfile complete path of input parameter property file] [-params name1=value
name2=value . . .] [-o complete path of directory for saving files] [-help]
```

The default method for running the deinstall tool is from the deinstall directory in the Oracle home. For example:

```
$ cd $ORACLE_HOME/deinstall
$ ./deinstall
```

In addition, you can run the deinstall tool from other locations, or with a parameter file, or select other options to run the tool.

The options are:

- `-home`
	Use this flag to indicate the home path of the Oracle home that you want to check or deinstall. If you want to deinstall Oracle software using the `deinstall` command in the same Oracle home you plan to deinstall, then provide a parameter file in another location, and do not use the `-home` flag.
- \- `silent`
	Use this flag to run the command in noninteractive mode. If you use the `-silent` option, then you must use the `-paramFile` flag, and provide a parameter file that contains the configuration values for the Oracle home that you want to deinstall or deconfigure.
	To create a properties file and provide the required parameters, refer to the template file `deinstall.rsp.tmpl`, located in the `response` folder of the Deinstallation tool home or the Oracle home.
	If you have a working system, then instead of using the template file, you can generate a properties file by running the `deinstall` command using the `-checkonly` flag. The `deinstall` command then discovers information from the Oracle home that you want to deinstall and deconfigure. It generates the properties file, which you can then use with the `-silent` option.
- `-checkonly`
	Use this flag to check the status of the Oracle software home configuration. Running the command with the `checkonly` flag does not remove the Oracle configuration. The `checkonly` flag generates a parameter file that you can use with the `deinstall` command.
	When you run `checkonly` to generate a parameter file, you are prompted to provide information about your system. You can accept the default value the tool has obtained from your Oracle installation, that is displayed inside brackets (\[\]), or you can provide different values. To accept the defaults, click Enter.
- `-local`
	Use this flag on a multinode environment to deconfigure Oracle software in a cluster.
	When you run `deinstall` with this flag, it deconfigures and deinstalls the Oracle software on the local node (the node where `deinstall` is run). On remote nodes, it deconfigures Oracle software, but does not deinstall the Oracle software.
- `-paramfile` `complete path of input parameter property file`
	Use this flag to run `deinstall` with a parameter file in a location other than the default. When you use this flag, provide the complete path where the parameter file is located. If you are running the deinstall command from the Oracle home that you plan to deinstall, then you do not need to use the `-paramfile` option.
	The default location of the parameter file depends on the location of `deinstall`:
	- From the installation media or stage location: $ORACLE\_HOME/inventory/response.
		- From a unzipped archive file from OTN: `/` `ziplocation` `/response`.
		- After installation from the installed Oracle home: `$ORACLE_HOME/deinstall/response`.
- `-params` \[`name1` = `value` `name 2` = `value` `name3` = `value`...\]
	Use this flag with a parameter file to override one or more values that you want to change in a parameter file you have already created.
- \- `o` `complete path of directory for saving response files`
	Use this flag to provide a path other than the default location where the properties file (`deinstall.rsp.tmpl`) is saved.
	The default location of the parameter file depends on the location of `deinstall`:
	- From the installation media or stage location before installation: `$ORACLE_HOME/`
		- From a unzipped archive file from OTN: `/` `ziplocation` `/response/`.
		- After installation from the installed Oracle home: `$ORACLE_HOME/deinstall/response`.
- `-help`
	Use the help option (`-help`) to obtain additional information about the command option flags.

### 8.3.2 Example of Running the Deinstall Command for Oracle RAC

As the `deinstall` command runs, you are prompted to provide the home directory of the Oracle software that you want to remove from your system. Provide additional information as prompted.

If you enter the deinstall command outside of the `$ORACLE_HOME/deinstall` folder, then help is displayed, unless you enter a -home flag and provide a path. If you run the deinstall command from the `$ORACLE_HOME/deinstall` folder, then deinstallation starts without prompting you for a home address.

Use the optional flag `-paramfile` to provide a path to a parameter file.

In the following example, the `deinstall` command is in the path `/u01/app/oracle/product/11.2.0/dbhome_1/deinstall`:

```
$ cd /u01/app/oracle/product/11.2.0/dbhome_1/deinstall
$ ./deinstall
```

### 8.3.3 Example of a Deinstallation Parameter File for Oracle RAC

You can run the `deinstall` command with the `-paramfile` option to use the values you specify in the parameter file. The following is an example of a parameter file, in which the Oracle Database binary owner is `oracle`, the Oracle Database home (Oracle home) is in the path `/u01/app/oracle/product/11.2.0/dbhome_1/`, the Oracle base (where other Oracle software is installed) is `/u01/app/oracle/`, the central Oracle Inventory home (oraInventory) is `/u01/app/oraInventory`, the virtual IP address (VIP) is `192.0.2.1`, the local node (the node where you are running the deinstallation session from) is `node1`, the remote node is `node2`, and the OSDBA group is `dba`:

```
#Copyright (c) 2005, 2006 Oracle Corporation. All rights reserved.
#Wed Feb 11 16:30:21 PST 2009
DISK_GROUPS.typi=
REMOTE_NODES=node2
ORACLE_BASE.typi=/u01/app/oracle
STORAGE_TYPE.typi=FS
ASM_HOME=
ASM_LOCAL_SID=
FLASH_RECOVERY_LOC.typi=
LOGDIR=/u01/app/oraInventory/logs/
DB_TYPE.typi=RAC_DB
ORACLE_BASE=/u01/app/oracle
INVENTORY_LOCATION=/u01/app/oraInventory
NODE_LIST.typi=node1,node2
ARCHIVE_LOG_DESTINATION_LOC.typi=
ASM_FILES.typi=
LOCAL_SID.typi=typi1
CLUSTER_NODES=node1,node2
DB_UNIQUE_NAME_LIST=typi
RAW_MAPPING_FILE.typi=
ORA_CRS_HOME=/u01/app/grid/11.2.0/
HOME_TYPE=RACDB
CRS_HOME=false
SID_LIST.typi=typi1,typi2
DATAFILE_LOC.typi=/oradbocfs/storage/database/oradata/typi
ORACLE_BINARY_OK=true
local=false
LOCAL_NODE=node1
CREATION_MODE.typi=y
CONFIGFILE_LOC.typi=/oradbocfs/storage/database/oradata/typi/control01.ctl, /oradbocfs/storage/database/oradata/typi/control02.ctl, /oradbocfs/storage/database/
oradata/typi/control03.ctl,/u01/app/oracle/product/11.2.0/dbhome
_1/dbs/dr1typi.dat,/u01/app/oracle/product/11.2.0/dbhome_1/dbs/d
r2typi.dat
DIAG_DEST.typi=/u01/app/oracle/diag/rdbms/typi
SPFILE_LOC.typi=/oradbocfs/storage/database/oradata/typi/spfiletypi.ora
silent=true
ORACLE_HOME=/u01/app/oracle/product/11.2.0/dbhome_1
```