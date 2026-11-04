---
title: Removing Oracle Real Application Clusters Software
book: Real Application Clusters Installation Guide for Microsoft Windows x64 (64-Bit)
doc_id: E48195-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e48195/rem_orcl.htm
tags:
  - oracle
  - 11g
  - real-application-clusters-installation-guide-for-microsoft-windows-x64-64-bit
---

## 8 Removing Oracle Real Application Clusters Software

This chapter describes how to completely remove all Oracle databases, instances, and software from an Oracle Real Application Clusters (Oracle RAC) Oracle home directory.

This chapter contains the following topics:

- Overview of Deinstallation Tools Actions
- Deinstalling Oracle RAC Software

See Also:

The product-specific documentation, for example [Oracle Database Client Installation Guide for Microsoft Windows](https://docs.oracle.com/cd/E11882_01/install.112/e47959/toc.htm), if you want to remove a single product to ensure that you are aware of requirements and restrictions that apply for that product

## 8.1 Overview of Deinstallation Tools Actions

The Deinstallation tool removes Oracle RAC or standalone Oracle Database installations from your server. It can also remove the Oracle Grid Infrastructure installation, which consists of Oracle Clusterware and Oracle Automatic Storage Management (Oracle ASM). The Deinstallation tool performs the follows actions when removing software from an Oracle home directory:

- Identifies all instances associated with the Oracle home
- Shuts down processes
- Removes listeners installed in the Oracle Database home
- Removes database instances
- Removes Oracle ASM release 11.1 or earlier installations
- Removes the Oracle Grid Infrastructure installation

Note:

- You cannot remove, uninstall, or deinstall the Oracle Database Vault option. However, you can disable it. See [Oracle Database Vault Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23090/dvdisabl.htm#DVADM012) for more information.
- You can remove Oracle Configuration Manager. See Oracle Configuration Manager Installation and Administration Guide for more information.
- Starting with Oracle Database 11g release 2 (11.2), you cannot remove, uninstall, or deinstall Oracle ASM separately from Oracle Clusterware or install it in a location outside of the Grid home.

Caution:

If any cluster member node has more than one database with the same global database name (GDN) on a server, then you cannot use the Deinstallation tool to remove one database only. For example, if you have a standalone database on one of your cluster nodes with the GDN `mydb.example.com`, and your Oracle RAC database GDN is also `mydb.example.com`, then both databases on that node are removed.

## 8.2 Identifying All Instances On a Cluster

To identify all instances and services associated with the Oracle home that you want to remove, perform the following steps:

1. Log in to a cluster node as a user with Administrator privileges.
2. Locate the Oracle services related to the Oracle home.
	Use the Windows Services Control Manager to manage the services. Look for any Oracle services (their names begin with `Ora`) that access the Oracle home you are removing and have the status Started.
	To determine which Oracle home a service is associated with, on Windows 2003, check "Path to Executable" for a service to see the directory where the executable for the service is located.

## 8.3 Deinstalling Oracle RAC Software

The Deinstallation tool removes Oracle Clusterware and Oracle ASM from your server, as well as Oracle Database installations, for both Oracle RAC and single-instance databases. The topics describe the Deinstallation tool, and provide information about additional options you can use:

### 8.3.1 About the Deinstallation Tool

The Deinstallation tool (`deinstall.bat`) is available in the installation media before installation, and is available in Oracle home directories after installation in the directory `%ORACLE_HOME%\deinstall`. The Deinstallation tool is also available for download from Oracle Technology Network (OTN) (`http://www.oracle.com/technetwork` /). You can download it with the complete Oracle Database 11g release 2 software, or as a separate archive file.

The `deinstall.bat` command uses the information you provide, plus information gathered from the software home to create a parameter file. You can alternatively supply a parameter file generated previously by the `deinstall.bat` command using the `-checkonly` and `-o` flags. You can also edit a response file template to create a parameter file.

The Deinstallation tool stops Oracle services, instances, and processes, and removes Oracle software and configuration files on the operating system for a specific Oracle home. At the end of the deinstallation process, you are prompted to run the `rootcrs.pl` script as a user that is a member of the Administrators group.

Caution:

When you run the `deinstall` command, if the central inventory contains no other registered homes besides the home that you are deconfiguring and removing, then the Deinstallation tool removes the following files and directory contents in the Oracle base directory of the Oracle RAC installation owner:
- admin
- cfgtoollogs
- checkpoints
- diag
- oradata
- flash\_recovery

Oracle strongly recommends that you configure your installations using an Optimal Flexible Architecture (OFA) configuration, and that you reserve Oracle base and Oracle home paths for exclusive use of Oracle software. If you have any user data in these locations in the Oracle base that is owned by the user account that owns the Oracle software, then the `deinstall` command deletes this data.

The `deinstall.bat` command uses the following syntax, where variable content is indicated by italics:

```
deinstall.bat [-home complete path of Oracle home] [-silent] [-checkonly] [-local]
[-paramfile complete path of input parameter property file]
[-params name1=value name2=value ...] 
[-o complete path of directory for saving files] 
[-tmpdir complete path of temporary directory to use] 
[-logdir complete path of log directory to use] [-help]
```

Note:

You cannot use the Deinstallation tool with the `-local` option for a shared Oracle home.

The default method for running the Deinstallation tool is from the `deinstall` directory in the Oracle home. For example:

```
C:\> cd %ORACLE_HOME%\deinstall
C:\..\dbhome_1\> deinstall.bat
```

In addition, you can run the Deinstallation tool from other locations, or with a parameter file, or select any of the following options when using Deinstallation tool:

- `-home`
	Use this flag to indicate the home path of the Oracle home to check or deinstall. To deinstall Oracle software using the `deinstall.bat` command located within the Oracle home being removed, provide a parameter file in a location outside the Oracle home, and do not use the `-home` flag.
	If you run `deinstall.bat` from the `%ORACLE_HOME%` `\deinstall` path, then the `-home` flag is not required because the tool knows from which home it is being run. If you use the standalone version of the tool, then the `-home` flag is mandatory
- \- `silent`
	Use this flag to run the command in noninteractive mode. This option requires one of the following:
	- A working system that the Deinstallation tool can access to determine the installation properties
		- A properties file that contains the configuration values for the Oracle home that is being deinstalled or deconfigured
	To create a properties file, modify the template file `deinstall.rsp.tmpl`, located in the `response` folder of the Deinstallation tool home or the Oracle home.
	If you have a working system, you can generate a properties file to use or modify by running the `deinstall.bat` command with the `-checkonly` flag. The `deinstall.bat` command then discovers information from the Oracle home to deinstall and deconfigure. It generates the properties file, which you can then use with the `-silent` option.
- `-checkonly`
	Use this flag to check the status of the Oracle software home configuration. Running the command with the `checkonly` flag does not remove the Oracle configuration. The `checkonly` flag generates a properties file that you can use with the `deinstall.bat` command.
	When you run `checkonly` to generate a properties file, you are prompted to provide information about your system. You can accept the default value the Deinstallation tool has obtained from your Oracle installation, indicated inside brackets (\[\]), or you can provide different values. To accept the defaults, click Enter at each prompt.
- `-local`
	Use this flag in a multinode environment to deconfigure Oracle software on a local node of a cluster.
	When you run the `deinstall.bat` command with this flag, it deconfigures and deinstalls the Oracle software on the local node (the node on which you run the `deinstall.bat` command) for non-shared Oracle home directories.
	Note:
	You cannot use the Deinstallation tool with the `-local` option for a shared Oracle home.
- `-paramfile` `complete path of input parameter property file`
	This is an optional flag. Use this flag to run the `deinstall.bat` command with a parameter file in a location other than the default. When you use this flag, provide the complete path where the parameter file is located. If you are running the deinstall.bat command from the Oracle home that you plan to deinstall, then you do not need to use the `-paramfile` option.
	The default location of the parameter file depends on the location of the `deinstall.bat` command you use:
	| Location of `deinstall.bat` | Default Location of the Parameter File |
	| --- | --- |
	| In the installation media or stage location: | `X:\staging_location` `\deinstall\response` |
	| From an unzipped archive file downloaded from OTN | `X:\ziplocation` `\deinstall\response`  where `X:\ziplocation` refers to the directory into which the downloaded archive file was extracted |
	| After installation, in the installed Oracle home | `%ORACLE_HOME%\deinstall\response` |
- `-params` \[`name1` = `value` `name2` = `value` `name3` = `value`...\]
	Use this flag with a parameter file to override one or more values in a parameter file that you created.
- \- `o` `complete path of directory for saving response files`
	Use this flag to provide a path other than the default location where the properties file (`deinstall_` `Oracle_home_name``.rsp`) is saved.
	The default location of the properties file depends on the location of the Deinstallation tool:
	| Location of `deinstall.bat` | Default Location of the Properties File |
	| --- | --- |
	| In the installation media or stage location: | `X:\staging_location` `\deinstall\response` |
	| From an unzipped archive file downloaded from OTN | `X:\ziplocation` `\deinstall\response`  where `X:\ziplocation` refers to the directory into which the downloaded archive file was extracted |
	| After installation, in the installed Oracle home | `%ORACLE_HOME%\deinstall\response` |
- `-tmpdir` `complete path of temporary directory`
	Specifies a non-default location where the deinstallation tool writes the temporary files for the deinstallation.
- `-logdir` `complete path of log directory`
	Specifies a non-default location where the deinstallation tool writes the log files for the deinstallation.
- `-help`
	Use this flag (`-help` or `-h`) to obtain additional information about the command options and flags.

If you use the `deinstall.bat` command located in an Oracle home, or the `deinstall.bat` command downloaded from OTN (not installed in an Oracle home), then the command writes log files in the `C:\Program Files\Oracle\Inventory\` `logs` directory. If, however, you are using the `deinstall.bat` command to remove the last Oracle home installed on the server, then the log files are written to:

- `%TEMP%\OraDeinstall` < `timestamp` > `\logs` if you use the `deinstall.bat` command located in the Oracle home
- `X``:\` `ziplocation` `\deinstall\` `logs` if you use the `deinstall.bat` command downloaded from OTN

### 8.3.2 Using the Deinstallation Tool for Oracle RAC

If you use the separately downloaded version of the Deinstallation tool, then when the `deinstall.bat` command runs, you are prompted to provide the home directory of the Oracle software to remove from your system. Provide additional information as prompted.

If you run the `deinstall.bat` command outside of the `%ORACLE_HOME%\deinstall` folder, then help output is displayed, unless you use the `-home` flag and provide a path to the Oracle home.

If you run the `deinstall.bat` command from the `%ORACLE_HOME%/deinstall` folder, then deinstallation starts without prompting you for a home address.

Example 8-1 Running the Deinstallation Tool Installed in an Oracle Home

To run the `deinstall.bat` command located in an Oracle Database home in the path `C:\app\oracle\product\11.2.0\dbhome_1`, enter the following command while logged in as a member of the Administrator group:

```
C:\> cd app\oracle\product
C:\app\oracle\product> 11.2.0\dbhome_1\deinstall\deinstall.bat
```

To completely remove the Oracle Database installation, you must run the `deinstall.bat` command from a prompt that is located outside of the Oracle home. If you run the `deinstall.bat` command after changing into the `Oracle_home` `\deinstall` directory, then the Deinstallation tool will not be able to remove all the Oracle software files and directories.

Example 8-2 Running the Standalone Version of the Deinstallation Tool

Assume you have installed the Deinstallation tool in the path `C:\app\oracle\product\deinstall`. Use the `deinstall.bat` command in this directory to deinstall an Oracle Database home using a parameter file. In this example, the parameter file is located in the user directory `C:\user\oracle`:

```
C:\> cd app\oracle\product\deinstall
C:\..deinstall> deinstall.bat -home C:\app\oracle\product\11.2.0\dbhome_1
-paramfile C:\user\oracle\my_db_paramfile.tmpl
```

### 8.3.3 Example of a Deinstallation Parameter File for Oracle RAC

You can run the `deinstall` command with the `-paramfile` option to use the values you specified in a parameter file instead of responding to individual prompts.

Example 8-3 Sample Parameter File to use with the Deinstallation Tool to Uninstall Oracle RAC

The following is an example of a parameter file created by the Deinstallation tool. The parameter file contains the following information:

- The Oracle Database software owner is `oracle`
- The Oracle Database home (Oracle home) is in the path `C:\app\oracle\product\11.2.0\dbhome_1`
- The Oracle base is `C:\app\oracle`
- The Grid home is `C:\app\11.2.0\grid`
- The central Oracle Inventory home is `C:\Program Files\Oracle\Inventory`
- The virtual IP address (VIP) is `192.0.2.1`
- The name of the local node (the node on which you run the Deinstallation tool) is `node1`
- The name of the remote node is `node2`
- The database name is `orcl` and it is an Oracle RAC database
- The database uses Oracle ASM for storage
```
#Copyright (c) 2005, 2010 Oracle Corporation. All rights reserved.
LOCAL_NODE=node1
HOME_TYPE=RACDB
ORACLE_BASE=C:\app\oracle
ObaseCleanupPtrLoc=C:\DOCUME~1\oracle\LOCALS~1\Temp\OraDeinstall2010-03-31_
  15-24-53\utl\orabase_cleanup.lst
DB_TYPE.orcl=RAC_DB
silent=false
ORA_CRS_HOME=C:\app\11.2.0\grid\
EMCP.CONFIG_MODE.orcl=CONFIG_DBCONTROL
EMCA_LOG.orcl=C:\app\oracle\cfgtoollogs\emca\orcl
LOGDIR=C:\Program Files\Oracle\Inventory\logs\
DATAFILE_LOC.orcl=
ORACLE_BINARY_OK=true
DUMP_DESTINATION_LOC.orcl=C:\app\oracle\admin\orcl
EMCP.DB_UNIQUE_NAME_LIST=orcl
CLUSTER_NODES=node1,node2
REMOTE_NODES=node2
SPFILE_LOC.orcl=+DATA/orcl/spfileorcl.ora
ARCHIVE_LOG_DESTINATION_LOC.orcl=
ORACLE_BASE.orcl=C:\app\oracle
LOCAL_SID.orcl=orcl1
local=false
INVENTORY_LOCATION=C:\Program Files\Oracle\Inventory
NODE_LIST.orcl=node1,node2
RAW_MAPPING_FILE.orcl=
DIAG_DEST.orcl=C:\APP\ORACLE\diag\rdbms\orcl
ORACLE_HOME=C:\app\oracle\product\11.2.0\dbhome_1\
STORAGE_TYPE.orcl=ASM
CCR_CONFIG_STATUS=CCR_DEL_HOME
CRS_HOME=false
EMCP.CHECK_POINT.orcl=WINDOWS_SERVICE_REGISTRY_CREATE,DBCONTROL_START
CONFIGFILE_LOC.orcl=+DATA/orcl/controlfile/current.260.712754807,C:\APP\ORACLE
 \PRODUCT\11.2.0\DBHOME_1\DATABASE\DR1ORCL.DAT,C:\APP\ORACLE\PRODUCT\11.2.0\
 DBHOME_1\DATABASE\DR2ORCL.DAT
SID_LIST.orcl=orcl1,orcl2
OLD_ACTIVE_ORACLE_HOME=
CREATION_MODE.orcl=y
COMPS_TO_REMOVE=ode.net.ntoledb,oramts
DB_UNIQUE_NAME_LIST=orcl
FLASH_RECOVERY_LOC.orcl=
```