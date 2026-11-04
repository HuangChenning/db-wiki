---
title: How to Modify or Deinstall Oracle Grid Infrastructure
book: Grid Infrastructure Installation Guide for Linux
doc_id: E41961-10
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e41961/rem_orcl.htm
tags:
  - oracle
  - 11g
  - grid-infrastructure-installation-guide-for-linux
---

## 6 How to Modify or Deinstall Oracle Grid Infrastructure

This chapter describes how to remove Oracle Clusterware and Oracle ASM.

Starting with Oracle Database 11g Release 2 (11.2), Oracle recommends that you use the deinstallation tool to remove the entire Oracle home associated with the Oracle Database, Oracle Clusterware, Oracle ASM, Oracle RAC, or Oracle Database client installation. Oracle does not support the removal of individual products or components.

This chapter contains the following topics:

See Also:

Product-specific documentation for requirements and restrictions to remove an individual product

## 6.1 Deciding When to Deinstall Oracle Clusterware

Remove installed components in the following situations:

- You have successfully installed Oracle Clusterware, and you want to remove the Oracle Clusterware installation, either in an educational environment, or a test environment.
- You have encountered errors during or after installing or upgrading Oracle Clusterware, and you want to reattempt an installation.
- Your installation or upgrade stopped because of a hardware or operating system failure.
- You are advised by Oracle Support to reinstall Oracle Clusterware.

## 6.2 Migrating Standalone Grid Infrastructure Servers to a Cluster

If you have an Oracle Database installation using Oracle Restart (that is, an Oracle Grid Infrastructure installation for a standalone server), and you want to configure that server as a cluster member node, then complete the following tasks:

Note:

This procedure uses Oracle Clusterware Configuration Wizard, available with release 11.2.0.2 and later.
1. Inspect the Oracle Restart configuration with `srvctl` using the following syntax, where db\_unique\_name is the unique name for the database, and lsnrname is the name of the listeners:
	srvctl config database -d db\_unique\_name
	srvctl config service -d db\_unique\_name
	srvctl config listener -l lsnrname
	Write down the configuration information for the server.
2. Log in as `root`, and change directory to Grid home `/crs/install`. For example:
	```
	# cd /u01/app/11.2.0/grid/crs/install
	```
3. Stop all of the databases, services, and listeners that you discovered in step 1.
4. If present, unmount all Oracle ACFS filesystems.
5. Deconfigure the Oracle Grid Infrastructure installation for a standalone server (Oracle Restart), using the following command:
	```
	# roothas.pl -deconfig -force
	```
6. Prepare the server for Oracle Clusterware configuration, as described in this document. In addition, choose if you want to install Oracle Grid Infrastructure for a Cluster in the same location as Oracle Restart, or in a different location:
	Installing in the Same Location as Oracle Restart
	1. Use the command Grid\_home `/deinstall` to remove the Oracle Restart software, but with all disk groups intact.
		2. Proceed to step 7.
	Installing in a Different Location than Oracle Restart
	1. Install Oracle Grid Infrastructure for a Cluster in the new Grid home software location
7. As the Oracle Grid Infrastructure installation owner, run Oracle Clusterware Configuration Wizard, and save and stage the response file. For example:
	```
	$ Grid_home/crs/config/config.sh -silent -responseFile $HOME/GI.rsp
	```
8. Run `root.sh` for the Oracle Clusterware Configuration Wizard.
9. Mount the Oracle Restart disk group.
10. Enter the `volenable` command to enable all Oracle Restart disk group volumes.
11. Mount all Oracle ACFS filesystems manually.
12. Add back Oracle Clusterware services to the Oracle Clusterware home, using the information you wrote down in step 1, including adding back Oracle ACFS resources. For example:
	```
	/u01/app/grid/product/11.2.0/grid/bin/srvctl add filesystem -d /dev/asm/db1  -g ORestartData -v db1 -m /u01/app/grid/product/11.2.0/db1 -u grid
	```
13. Add the Oracle Database for support by Oracle Grid Infrastructure for a cluster, using the configuration information you recorded in step 1. Use the following command syntax, where db\_unique\_name is the unique name of the database on the node, and nodename is the name of the node:
	srvctl add database -d db\_unique\_name -o $ORACLE\_HOME -x nodename
	For example, with the database name `mydb`, and the service `myservice`, enter the following commands:
	```
	srvctl add database -d mydb -o $ORACLE_HOME -x node1
	```
14. Add each service to the database, using the command `srvctl add service`. For example:
	```
	srvctl add service -d mydb -s myservice
	```

## 6.3 Relinking Oracle Grid Infrastructure for a Cluster Binaries

After installing Oracle Grid Infrastructure for a cluster (Oracle Clusterware and Oracle ASM configured for a cluster), if you need to modify the binaries, then use the following procedure, where `Grid_home` is the Oracle Grid Infrastructure for a Cluster home:

Caution:

Before relinking executables, you must shut down all executables that run in the Oracle home directory that you are relinking. In addition, shut down applications linked with Oracle shared libraries.

As `root`:

```
# cd Grid_home/crs/install
# perl rootcrs.pl -unlock
```

As the Oracle Grid Infrastructure for a Cluster owner:

```
$ export ORACLE_HOME=Grid_home
$ Grid_home/bin/relink
```

As `root` again:

```
# cd Grid_home/rdbms/install/
# ./rootadd_rdbms.sh
# cd Grid_home/crs/install
# perl rootcrs.pl -patch
```

You must relink the Oracle Clusterware and Oracle ASM binaries every time you apply an operating system patch or after an operating system upgrade.

For upgrades from previous releases, if you want to deinstall the prior release Grid home, then you must first unlock the prior release Grid home. Unlock the previous release Grid home by running the command `rootcrs.pl -unlock` from the previous release home. After the script has completed, you can run the deinstall command.

## 6.4 Changing the Oracle Grid Infrastructure Home Path

With release 11.2.0.3 and later, after installing Oracle Grid Infrastructure for a cluster (Oracle Clusterware and Oracle ASM configured for a cluster), if you need to change the Grid home path, then use the following example as a guide to detach the existing Grid home, and to attach a new Grid home:

Caution:

Before changing the Grid home, you must shut down all executables that run in the Grid home directory that you are relinking. In addition, shut down applications linked with Oracle shared libraries.
1. Detach the existing Grid home by running the following command as the Oracle Grid Infrastructure installation owner (`grid`), where `/u01/app/11.2.0/grid` is the existing Grid home location:
	```
	$ cd /u01/app/11.2.0/grid/oui/bin
	$ ./detachhome.sh -silent -local -invPtrLoc /u01/app/11.2.0/grid/oraInst.loc
	```
2. As `root`, unlock and move the Grid binaries from the old Grid home location to the new Grid home location. For example, where the old Grid home is `/u01/app/11.2.0/grid` and the new Grid home is `/u01/app/grid`:
	```
	cd /u01/app/11.2.0/grid/
	perl rootcrs.pl -unlock
	# mv /u01/app/11.2.0/grid /u01/app/grid
	```
3. Clone the Oracle Grid Infrastructure installation, using the instructions provided in "Creating a Cluster by Cloning Oracle Clusterware Step 3: Run the clone.pl Script on Each Destination Node," in [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/clonecluster.htm#CWADD92126).
	When you navigate to the `Grid_home` `/clone/bin` directory and run the `clone.pl` script, provide values for the input parameters that provide the path information for the new Grid home.
4. As `root` again, enter the following commands to start up in the new home location:
	```
	# cd Grid_home/rdbms/install/
	# ./rootadd_rdbms.sh
	# cd Grid_home/crs/install
	# perl rootcrs.pl -patch -destcrshome /u01/app/grid
	```
5. Repeat steps 1 through 4 on each cluster member node.

You must relink the Oracle Clusterware and Oracle ASM binaries every time you move the Grid home.

## 6.5 Deconfiguring Oracle Clusterware Without Removing Binaries

Running the `rootcrs.pl` command flags `-deconfig -force` enables you to deconfigure Oracle Clusterware on one or more nodes without removing installed binaries. This feature is useful if you encounter an error on one or more cluster nodes during installation when running the `root.sh` command, such as a missing operating system package on one node. By running `rootcrs.pl -deconfig -force` on nodes where you encounter an installation error, you can deconfigure Oracle Clusterware on those nodes, correct the cause of the error, and then run `root.sh` again.

Note:

Stop any databases, services, and listeners that may be installed and running before deconfiguring Oracle Clusterware.

Caution:

Commands used in this section remove the Oracle Grid infrastructure installation for the entire cluster. If you want to remove the installation from an individual node, then refer to [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/adddelclusterware.htm#CWADD1167).

To deconfigure Oracle Clusterware:

1. Log in as the `root` user on a node where you encountered an error.
2. Change directory to Grid\_home/crs/install. For example:
	```
	# cd /u01/app/11.2.0/grid/crs/install
	```
3. Run `rootcrs.pl` with the `-deconfig -force` flags. For example:
	```
	# perl rootcrs.pl -deconfig -force
	```
	Repeat on other nodes as required.
4. If you are deconfiguring Oracle Clusterware on all nodes in the cluster, then on the last node, enter the following command:
	```
	# perl rootcrs.pl -deconfig -force -lastnode
	```
	The `-lastnode` flag completes deconfiguration of the cluster, including the OCR and voting disks.

## 6.6 Removing Oracle Clusterware and Oracle ASM

The `deinstall` command removes Oracle Clusterware and Oracle ASM from your server. The following sections describe the command, and provide information about additional options to use the command:

- About the Deinstallation Tool
- Deinstalling Previous Release Grid Home
- Downloading The Deinstall Tool for Use with Failed Installations
- Running The Deinstallation Tool
- Deinstall Command Example for Oracle Clusterware and Oracle ASM
- Deinstallation Parameter File Example for Grid Infrastructure for a Cluster

Caution:

You must use the deinstallation tool from the same release to remove Oracle software. Do not run the deinstallation tool from a later release to remove Oracle software from an earlier release. For example, do not run the deinstallation tool from the 12.1.0.1 installation media to remove Oracle software from an existing 11.2.0.4 Oracle home.

### 6.6.1 About the Deinstallation Tool

The Deinstallation Tool (`deinstall`) stops Oracle software, and removes Oracle software and configuration files on the operating system. It is available in the installation media before installation, and is available in Oracle home directories after installation. It is located in the path `$ORACLE_HOME/deinstall`. The Deinstallation tool command is also available for download from Oracle Technology Network (OTN) at the following URL:

`http://www.oracle.com/technetwork/database/enterprise-edition/downloads`

You can download the Deinstallation tool with the complete Oracle Database 11g release 2 software, or as a separate archive file. To download the Deinstallation tool separately, click the See All link next to the software version.

The Deinstallation tool command uses the information you provide and the information gathered from the software home to create a parameter file. Alternatively, you can use a parameter file generated previously by the `deinstall` command using the `-checkonly` flag and `-o` flag. You can also edit a response file template to create a parameter file.

The Deinstallation tool command stops Oracle software, and removes Oracle software and configuration files on the operating system for a specific Oracle home. If you run the Deinstallation tool to remove an Oracle Grid Infrastructure for a cluster installation, then the tool prompts you to run the `rootcrs.pl` script as `root`.

Caution:

When you run the deinstall command, if the central inventory (oraInventory) contains no other registered homes besides the home that you are deconfiguring and removing, then the deinstall command removes the following files and directory contents in the Oracle base directory of the Oracle RAC installation owner:
- admin
- cfgtoollogs
- checkpoints
- diag
- oradata
- flash\_recovery\_area

Oracle strongly recommends that you configure your installations using an Optimal Flexible Architecture (OFA) configuration, and that you reserve Oracle base and Oracle home paths for exclusive use of Oracle software. If you have any user data in these locations in the Oracle base that is owned by the user account that owns the Oracle software, then the `deinstall` command deletes this data.

The command uses the following syntax, where variable content is indicated by italics:

```
deinstall -home complete path of Oracle home [-silent] [-checkonly] [-local] 
[-paramfile complete path of input parameter property file] 
[-params name1=value name2=value . . .] [-o complete path of directory for saving files] -h
```

The default method for running the deinstall tool is from the deinstall directory in the Grid home. For example:

```
$ cd /u01/app/11.2.0/grid/deinstall
$ ./deinstall
```

In addition, you can run the deinstall tool from other locations, or with a parameter file, or select other options to run the tool.

The options are:

- `-home`
	Use this flag to indicate the home path of the Oracle home that you want to check or deinstall. To deinstall Oracle software using the `deinstall` command in the Oracle home you plan to deinstall, provide a parameter file in another location, and do not use the `-home` flag.
	If you run `deinstall` from the $ORACLE\_HOME/deinstall path, then the `-home` flag is not required because the tool knows from which home it is being run. If you use the standalone version of the tool, then `-home` is mandatory.
- \- `silent`
	Use this flag to run the command in noninteractive mode. This option requires a properties file that contains the configuration values for the Oracle home that is being deinstalled or deconfigured.
	To create a properties file and provide the required parameters, refer to the template file `deinstall.rsp.tmpl`, located in the `response` folder of the Deinstallation tool home or the Oracle home.
	If you have a working system, then instead of using the template file, you can generate a properties file by running the `deinstall` command using the `-checkonly` flag. The `deinstall` command then discovers information from the Oracle home that you want to deinstall and deconfigure. It generates the properties file, which you can then use with the `-silent` option.
- `-checkonly`
	Use this flag to check the status of the Oracle software home configuration. Running the command with the `checkonly` flag does not remove the Oracle configuration.
- `-local`
	Use this flag on a multinode non-shared environment to deconfigure Oracle software in a cluster.
	When you run `deinstall` with this flag, it deconfigures and deinstalls the Oracle software on the local node (the node where `deinstall` is run) for non-shared home directories. On remote nodes, it deconfigures Oracle software, but does not deinstall the Oracle software.
- `-paramfile` `complete path of input parameter property file`
	Use this flag to run `deinstall` with a parameter file in a location other than the default. When you use this flag, provide the complete path where the parameter file is located. If you are running the deinstall command from the Oracle home that you plan to deinstall, then you do not need to use the `-paramfile` flag.
	The default location of the parameter file depends on the location of `deinstall`:
	- From the installation media or stage location: `$ORACLE_HOME/inventory/response`.
		- From a unzipped archive file from Oracle Technology Network (OTN): `/` `ziplocation` `/response`.
		- After installation from the installed Oracle home: `$ORACLE_HOME/deinstall/response`.
- `-params` \[`name1` = `value` `name2` = `value` `name3` = `value`...\]
	Use this flag with a parameter file to override one or more values in a parameter file you have already created.
- \- `o` `complete path of directory for saving response files`
	Use this flag to provide a path other than the default location where the properties file (`deinstall.rsp.tmpl`) is saved.
	The default location of the parameter file depends on the location of `deinstall`:
	- From the installation media or stage location before installation: `$ORACLE_HOME/`.
		- From a unzipped archive file from OTN: `/` `ziplocation` `/response/`.
		- After installation from the installed Oracle home: `$ORACLE_HOME/deinstall/response`.
- `-help`
	Use the help option (`-help`) to obtain additional information about the command option flags.

### 6.6.2 Deinstalling Previous Release Grid Home

For upgrades from previous releases, if you want to deinstall the previous release Grid home, then as the `root` user, you must manually change the permissions of the previous release Grid home, and then run the `deinstall` command.

For example:

```
# chown -R grid:oinstall /u01/app/grid/11.2.0
# chmod -R 775 /u01/app/grid/11.2.0
```

In this example, `/u01/app/grid/11.2.0` is the previous release Grid home.

### 6.6.3 Downloading The Deinstall Tool for Use with Failed Installations

You can use the Deinstallation tool (`deinstall`) to remove failed or incomplete installations. It is available as a separate download from the Oracle Technology Network (OTN) Web site.

To download the Deinstallation tool:

1. Go to the following URL:
	```
	http://www.oracle.com/technetwork/database/enterprise-edition/downloads/index.html
	```
2. Under Oracle Database 11g Release 2, click See All for the respective platform for which you want to download the Deinstallation Tool.
	The Deinstallation tool is available for download at the end of this page.

### 6.6.4 Running The Deinstallation Tool

Oracle recommends that you run the `deinstall` command as the Oracle Grid Infrastructure installation owner or the `grid` user that owns Oracle Clusterware.

After downloading the Deinstallation tool, ensure that:

- The user running the Deinstallation tool is the same on all cluster member nodes
- User equivalence is set up

To run the Deinstallation tool, follow these steps:

1. Download or copy the Deinstallation tool to the `grid` user home directory.
2. Verify that the deinstall binary is owned by the `grid` user.
3. Run the Deinstallation tool.

### 6.6.5 Deinstall Command Example for Oracle Clusterware and Oracle ASM

As the `deinstall` command runs, you are prompted to provide the home directory of the Oracle software that you want to remove from your system. Provide additional information as prompted.

To run the `deinstall` command from an Oracle Grid Infrastructure for a cluster home, enter the following command:

```
$ cd /u01/app/11.2.0/grid/deinstall/
$ ./deinstall
```

You can run generate a `deinstall` parameter file by running the `deinstall` command using the `-checkonly` flag before you run the command to deinstall the home, or you can use the response file template and manually edit it to create the parameter file to use with the `deinstall` command.

### 6.6.6 Deinstallation Parameter File Example for Grid Infrastructure for a Cluster

You can run the `deinstall` command with the `-paramfile` option to use the values you specify in the parameter file. The following is an example of a parameter file for a cluster on nodes `node1` and `node2`, in which the Oracle Grid Infrastructure for a cluster software binary owner is `grid`, the Oracle Grid Infrastructure home (Grid home) is in the path `/u01/app/11.2.0/grid`, the Oracle base (the Oracle base for Oracle Grid Infrastructure, containing Oracle ASM log files, Oracle Clusterware logs, and other administrative files) is `/u01/app/11.2.0/grid/`, the central Oracle Inventory home (`oraInventory`) is `/u01/app/oraInventory`, the virtual IP addresses (VIP) are `192.0.2.2` and `192.0.2.4`, the local node (the node where you are running the deinstallation session from) is `node1`:

```
#Copyright (c) 2005, 2006 Oracle Corporation.  All rights reserved.
#Fri Feb 06 00:08:58 PST 2009
LOCAL_NODE=node1
HOME_TYPE=CRS
ASM_REDUNDANCY=\
ORACLE_BASE=/u01/app/11.2.0/grid/
VIP1_MASK=255.255.252.0
VOTING_DISKS=/u02/storage/grid/vdsk
SCAN_PORT=1522
silent=true
ASM_UPGRADE=false
ORA_CRS_HOME=/u01/app/11.2.0/grid
GPNPCONFIGDIR=$ORACLE_HOME
LOGDIR=/home/grid/SH/deinstall/logs/
GPNPGCONFIGDIR=$ORACLE_HOME
ORACLE_OWNER=grid
NODELIST=node1,node2
CRS_STORAGE_OPTION=2
NETWORKS="eth0"/192.0.2.1\:public,"eth1"/10.0.0.1\:cluster_interconnect
VIP1_IP=192.0.2.2
NETCFGJAR_NAME=netcfg.jar
ORA_DBA_GROUP=dba
CLUSTER_NODES=node1,node2
JREDIR=/u01/app/11.2.0/grid/jdk/jre
VIP1_IF=eth0
REMOTE_NODES=node2
VIP2_MASK=255.255.252.0
ORA_ASM_GROUP=asm
LANGUAGE_ID=AMERICAN_AMERICA.WE8ISO8859P1
CSS_LEASEDURATION=400
NODE_NAME_LIST=node1,node2
SCAN_NAME=node1scn
SHAREJAR_NAME=share.jar
HELPJAR_NAME=help4.jar
SILENT=false
local=false
INVENTORY_LOCATION=/u01/app/oraInventory
GNS_CONF=false
JEWTJAR_NAME=jewt4.jar
OCR_LOCATIONS=/u02/storage/grid/ocr
EMBASEJAR_NAME=oemlt.jar
ORACLE_HOME=/u01/app/11.2.0/grid
CRS_HOME=true
VIP2_IP=192.0.2.4
ASM_IN_HOME=n
EWTJAR_NAME=ewt3.jar
HOST_NAME_LIST=node1,node2
JLIBDIR=/u01/app/11.2.0/grid/jlib
VIP2_IF=eth0
VNDR_CLUSTER=false
CRS_NODEVIPS='node1-vip/255.255.252.0/eth0,node2-vip/255.255.252.0/eth0'
CLUSTER_NAME=node1-cluster
```

Note:

Do not use quotation marks with variables except in the following cases:
- Around addresses in CRS\_NODEVIPS:
	```
	CRS_NODEVIPS='n1-vip/255.255.252.0/eth0,n2-vip/255.255.252.0/eth0'
	```
- Around interface names in NETWORKS:
	```
	NETWORKS="eth0"/192.0.2.1\:public,"eth1"/10.0.0.1\:cluster_interconnect VIP1_IP=192.0.2.2
	```