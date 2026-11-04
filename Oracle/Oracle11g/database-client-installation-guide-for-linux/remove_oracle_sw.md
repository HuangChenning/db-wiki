---
title: Removing Oracle Database Client Software
book: Database Client Installation Guide for  Linux
doc_id: E24322-14
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e24322/remove_oracle_sw.htm
tags:
  - oracle
  - 11g
  - database-client-installation-guide-for-linux
---

## 5 Removing Oracle Database Client Software

This chapter describes how to completely remove Oracle software and configuration files related to the specified Oracle home using the Deinstallation Tool.

The `deinstall` command removes the Oracle Database Client installations.

Starting with Oracle Database 11g Release 2 (11.2), Oracle recommends that you use the deinstallation tool to remove the entire Oracle home associated with the Oracle Database, Oracle Clusterware, Oracle ASM, Oracle RAC, or Oracle Database client installation. Oracle does not support the removal of individual products or components.

It includes information about the following topics:

## 5.1 About the Deinstallation Tool

The Deinstallation Tool (`deinstall`) is available in the installation media before installation, and is available in Oracle home directories after installation. It is located in the `$ORACLE_HOME/deinstall` directory.

The `deinstall` command uses the information you provide, plus information gathered from the software home to create a parameter file. You can alternatively supply a parameter file generated previously by the `deinstall` command using the `–checkonly` option, or by editing the response file template.

Caution:

When you run the `deinstall` command, if the central inventory (oraInventory) contains no other registered homes besides the home that you are deconfiguring and removing, then the deinstall command removes the following files and directory contents in the Oracle base directory of the Oracle Database installation owner:
- `admin`
- `cfgtoollogs`
- `checkpoints`
- `diag`
- `oradata`
- `fast_recovery_area`

Oracle strongly recommends that you configure your installations using an Optimal Flexible Architecture (OFA) configuration, and that you reserve Oracle base and Oracle home paths for exclusive use of Oracle software. If you have any user data in these locations in the Oracle base that is owned by the user account that owns the Oracle software, then the `deinstall` command deletes this data.

The deinstallation tool deletes Oracle Database configuration files, user data, and fast recovery area (FRA) files even if they are located outside of the Oracle base directory path.

The command uses the following syntax, where variable content is indicated in italics:

```
deinstall -home complete path of Oracle home [-silent] [-checkonly] [-local] [-paramfile complete path of input parameter property file] [-params name1=value
name2=value . . .] [-o complete path of directory for saving files]
[-tmpdir complete path of temporary directory to use]
[-logdir complete path of log directory to use] [-help]
```

Oracle recommends that you run the deinstallation tool as the Oracle software installation owner. The default method for running the deinstall tool is from the deinstall directory in the Oracle home as the installation owner:

```
$ $ORACLE_HOME/deinstall/deinstall
```

Provide information about your servers as prompted or accept the defaults.

The `deinstall` command stops Oracle software, and removes Oracle software and configuration files on the operating system.

Note:

You must run the deinstallation tool from the same release to remove Oracle software. Do not run the deinstallation tool from a later release to remove Oracle software from an earlier release. For example, do not run the deinstallation tool from the 12.1.0.1 installation media to remove Oracle software from an existing 11.2.0.4 Oracle home.

In addition, you can run the deinstall tool from other locations, or with a parameter file, or select other options to run the tool.

The options are:

- `-home`
	Use this flag to indicate the home path of the Oracle home to check or deinstall. To deinstall Oracle software using the `deinstall` command in the Oracle home you plan to deinstall, provide a parameter file in another location, and do not use the `-home` flag.
	If you run deinstall from the `$ORACLE_HOME/deinstall` path, then the `-home` flag is not required because the tool knows from which home it is being run. If you use the standalone version of the tool, then `-home` is mandatory.
- `-silent`
	Use this flag to run the command in silent or response file mode. If you use the `-silent` flag, then you must use the `-paramfile` flag, and provide a parameter file that contains the configuration values for the Oracle home to deinstall or deconfigure.
	You can generate a parameter file to use or modify by running `deinstall` with the `-checkonly` flag. The `deinstall` command then discovers information from the Oracle home to deinstall and deconfigure. It generates the properties file, which you can then use with the `-silent` option.
	You can also modify the template file `deinstall.rsp.tmpl`, located in the `$ORACLE_HOME/deinstall/response` folder.
- `-checkonly`
	Use this flag to check the status of the Oracle software home configuration. Running the command with the `-checkonly` flag does not remove the Oracle configuration. The `-checkonly` flag generates a parameter file which you can then use with the `deinstall` command and `-silent` option.
- `-local`
	Use this flag on a multinode environment to deinstall Oracle software in a cluster.
	When you run `deinstall` with this flag, it deconfigures and deinstalls the Oracle software on the local node (the node where `deinstall` is run). On remote nodes, it deconfigures Oracle software, but does not deinstall the Oracle software.
- `-paramfile` `complete path of input parameter property file`
	Use this flag to run `deinstall` with a parameter file in a location other than the default. When you use this flag, provide the complete path where the parameter file is located.
	The default location of the parameter file depends on the location of `deinstall`:
	- From the installation media or stage location: `$ORACLE_HOME/inventory/response`.
		- From a unzipped archive file from OTN: `/` `ziplocation` `/response`.
		- After installation from the installed Oracle home: `$ORACLE_HOME/deinstall/response`.
- `-params` \[`name1` = `value` `name 2` = `value` `name3` = `value`...\]
	Use this flag with a parameter file to override one or more values to change in a parameter file you have already created.
- `-o` `complete path of directory for saving response files`
	Use this flag to provide a path other than the default location where the properties file (`deinstall.rsp.tmpl`) is saved.
	The default location of the parameter file depends on the location of `deinstall`:
	- From the installation media or stage location before installation: `$ORACLE_HOME/`
		- From a unzipped archive file from OTN: `/` `ziplocation` `/response/`.
		- After installation from the installed Oracle home: `$ORACLE_HOME/deinstall/response`.
- `-tmpdir` `complete path of temporary directory`
	Use this flag to specify a non-default location where Oracle Deinstallation Tool writes the temporary files for the deinstallation.
- `-logdir` `complete path of temporary directory`
	Use this flag to specify a non-default location where Oracle Deinstallation Tool writes the log files for the deinstallation.
- `-help`
	Use the help option (`-help`) to obtain additional information about the command option flags.

## 5.2 Downloading the Deinstall Tool for Use with Failed Installations

If you require the Deinstallation Tool (deinstall) to remove failed or incomplete installations, then it is available as a separate download from the Oracle Technology Network (OTN) website.

To download the Deinstallation Tool:

1. Go to the following URL:
	`http://www.oracle.com/technetwork/database/enterprise-edition/downloads/index.html`
2. Under Oracle Database 11g Release 2, click See All for the respective platform for which you want to download the Deinstallation Tool.
	The Deinstallation Tool is available for download at the end of this web page.

## 5.3 Example of Running the Deinstall Command

As the `deinstall` command runs, you are prompted to provide the home directory of the Oracle software to remove from your system. Provide additional information as prompted.

Use the optional flag `-paramfile` to provide a path to a parameter file.

In the following example, the `deinstall` command is in the path `/u01/app/oracle/product/11.2.0/client_1/deinstall`, and it uses a parameter file in the software owner location `/home/usr/oracle`:

```
# cd /u01/app/oracle/product/11.2.0/client_1/deinstall/
# ./deinstall -paramfile /home/usr/oracle/myparamfile.tmpl
```

If you enter the deinstall command outside of the `$ORACLE_HOME/deinstall` folder, then help is displayed, unless you enter a `-home` flag and provide a path. If you run the deinstall command from the `$ORACLE_HOME/deinstall` folder, then deinstallation starts without prompting you for a home address.

## 5.4 Deinstallation Parameter File Example

You can run the `deinstall` command with the `-paramfile` option to use the values you specify in the parameter file. The following is an example of a parameter file, in which the Oracle Database binary owner is `oracle`, the Oracle Database home (Oracle home) is in the path `/u01/app/oracle/product/11.2.0/client_1/`, the Oracle base (where other Oracle software is installed) is `/u01/app/oracle/`, the central Oracle Inventory home (`oraInventory`) is `/u01/app/oraInventory`, and the client is `client1`:

```
ORACLE_BASE=/u01/app/oracle
INVENTORY_LOCATION=/u01/app/oraInventory
CRS_HOME=false
HOME_TYPE=CLIENT
silent=false
local=false
LOCAL_NODE=node1
ObaseCleanupPtrLoc=/var/tmp/install/orabase_cleanup.lst.
LOGDIR=/u01/app/oraInventory/logs/
ORACLE_HOME=/u01/app/oracle/product/11.2.0/client_1
```