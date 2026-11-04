---
title: Installing Oracle Grid Infrastructure for a Cluster
book: Grid Infrastructure Installation Guide for Linux
doc_id: E41961-10
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e41961/crsunix.htm
tags:
  - oracle
  - 11g
  - grid-infrastructure-installation-guide-for-linux
---

## 4 Installing Oracle Grid Infrastructure for a Cluster

This chapter describes the procedures for installing Oracle Grid Infrastructure for a cluster. Oracle Grid Infrastructure consists of Oracle Clusterware and Oracle Automatic Storage Management (Oracle ASM). If you plan afterward to install Oracle Database with Oracle Real Application Clusters (Oracle RAC), then this is phase one of a two-phase installation.

This chapter contains the following topics:

## 4.1 Preparing to Install Oracle Grid Infrastructure with OUI

Before you install Oracle Grid Infrastructure with the installer, use the following checklist to ensure that you have all the information you will need during installation, and to ensure that you have completed all tasks that must be done before starting your installation. Check off each task in the following list as you complete it, and write down the information needed, so that you can provide it during installation.

- Shut Down Running Oracle Processes
	You may need to shut down running Oracle processes:
	Installing on a node with a standalone database not using Oracle ASM: You do not need to shut down the database while you install Oracle Grid Infrastructure software.
	Installing on a node that already has a standalone Oracle Database 11g release 2 (11.2) installation running on Oracle ASM: Stop the existing Oracle ASM instances. The Oracle ASM instances are restarted during installation.
	Installing on an Oracle RAC Database node: This installation requires an upgrade of Oracle Clusterware, as Oracle Clusterware is required to run Oracle RAC. As part of the upgrade, you must shut down the database one node at a time as the rolling upgrade proceeds from node to node.
	Note:
	If you are upgrading an Oracle RAC 9i Release 2 (9.2) node to Oracle Grid Infrastructure 11g Release 2 (Releases 11.2.0.1 and 11.2.0.2), and the TNSLSNR is listening to the same port on which the SCAN listens (default 1521), then the TNSLSNR should be shut down.
	If you are upgrading to Oracle Grid Infrastructure 11g Release 2 (11.2.0.3) or later, then you can ignore this issue.
	If a Global Services Daemon (GSD) from Oracle9i Release 9.2 or earlier is running, then stop it before installing Oracle Grid Infrastructure by running the following command:
	```
	$ Oracle_home/bin/gsdctl stop
	```
	where `Oracle_home` is the Oracle Database home that is running the GSD.
	Caution:
	If you have an existing Oracle9i release 2 (9.2) Oracle Cluster Manager (Oracle CM) installation, then do not shut down the Oracle CM service. Shutting down the Oracle Cluster Manager service prevents the Oracle Grid Infrastructure 11g Release 2 (11.2) software from detecting the Oracle9i release 2 node list, and causes failure of the Oracle Grid Infrastructure installation.
	Note:
	If you receive a warning to stop all Oracle services after starting Oracle Universal Installer (OUI), then run the command
	```
	Oracle_home/bin/localconfig delete
	```
	where `Oracle_home` is the existing Oracle Clusterware home.
- Prepare for Oracle Automatic Storage Management and Oracle Clusterware Upgrade If You Have Existing Installations
	During the Oracle Grid Infrastructure installation, existing Oracle Clusterware and clustered Oracle ASM installations are both upgraded.
	When all member nodes of the cluster are running Oracle Grid Infrastructure 11g Release 2 (11.2), then the new clusterware becomes the active version.
	If you intend to install Oracle RAC, then you must first complete the upgrade to Oracle Grid Infrastructure 11g Release 2 (11.2) on all cluster nodes before you install the Oracle Database 11g Release 2 (11.2) version of Oracle RAC.
	Note:
	All Oracle Grid Infrastructure upgrades (upgrades of existing Oracle Clusterware and Oracle ASM installations) are out-of-place upgrades.
- Determine the Oracle Inventory (oraInventory) location
	If you have already installed Oracle software on your system, then OUI detects the existing Oracle Inventory (oraInventory) directory from the `/etc/oraInst.loc` file, and uses this location. This directory is the central inventory of Oracle software installed on your system. Users who have the Oracle Inventory group as their primary group are granted the OINSTALL privilege to write to the central inventory.
	If you are installing Oracle software for the first time on your system, and your system does not have an oraInventory directory, then the installer designates the installation owner's primary group as the Oracle Inventory group. Ensure that this group is available as a primary group for all planned Oracle software installation owners.
	Note:
	The oraInventory directory cannot be placed on a shared file system.
	See Also:
	The preinstallation chapters in [Chapter 2](prelinux.md) for information about creating the Oracle Inventory, and completing required system configuration
- Obtain root account access
	During installation, you are asked to run configuration scripts as the `root` user. You must run these scripts as `root`, or be prepared to have your system administrator run them for you. You must run the `root.sh` script on the first node and wait for it to finish. If your cluster has four or more nodes, then `root.sh` can be run concurrently on all nodes but the first and last.
- Decide if you want to install other languages
	During installation, you are asked if you want translation of user interface text into languages other than the default, which is English.
	Note:
	If the language set for the operating system is not supported by the installer, then by default the installer runs in the English language.
	See Also:
	[Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/toc.htm) for detailed information on character sets and language configuration
- Determine your cluster name, public node names, the SCAN, virtual node names, GNS VIP and planned interface use for each node in the cluster
	During installation, you are prompted to provide the public and virtual host name, unless you use a third party cluster software. In that case, the public host name information will be filled in. You are also prompted to identify which interfaces are public, private, or interfaces in use for another purpose, such as a network file system.
	If you use Grid Naming Service (GNS), then OUI displays the public and virtual host name addresses labeled as "AUTO" because they are configured automatically.
	Note:
	If you configure IP addresses manually, then avoid changing host names after you complete the Oracle Grid Infrastructure installation, including adding or deleting domain qualifications. A node with a new host name is considered a new host, and must be added to the cluster. A node under the old name will appear to be down until it is removed from the cluster.
	When you enter the public node name, use the primary host name of each node. In other words, use the name displayed by the `hostname` command.
	In addition:
	- Provide a cluster name with the following characteristics:
		- It must be globally unique throughout your host domain.
				- It must be at least one character long and less than or equal to 15 characters long.
				- It must consist of the same character set used for host names, in accordance with RFC 1123: Hyphens (-), and single-byte alphanumeric characters (a to z, A to Z, and 0 to 9). If you use third-party vendor clusterware, then Oracle recommends that you use the vendor cluster name.
		- If you are not using Grid Naming Service (GNS), then determine a virtual host name for each node. A virtual host name is a public node name that is used to reroute client requests sent to the node if the node is down. Oracle Database uses VIPs for client-to-database connections, so the VIP address must be publicly accessible. Oracle recommends that you provide a name in the format hostname-vip. For example: `myclstr2-vip`.
		- Provide SCAN addresses for client access to the cluster. These addresses should be configured as round robin addresses on the domain name service (DNS). Oracle recommends that you supply three SCAN addresses.
		Note:
		The following is a list of additional information about node IP addresses:
		- For the local node only, OUI automatically fills in public and VIP fields. If your system uses vendor clusterware, then OUI may fill additional fields.
		- Host names and virtual host names are not domain-qualified. If you provide a domain in the address field during installation, then OUI removes the domain from the address.
		- Interfaces identified as private for private IP addresses should not be accessible as public interfaces. Using public interfaces for Cache Fusion can cause performance problems.
		- Identify public and private interfaces. OUI configures public interfaces for use by public and virtual IP addresses, and configures private IP addresses on private interfaces.
		The private subnet that the private interfaces use must connect all the nodes you intend to have as cluster members.
- Obtain proxy realm authentication information if you have a proxy realm on your network
	During installation, OUI attempts to download updates. You are prompted to provide a proxy realm, and user authentication information to access the Internet through the proxy service. If you have a proxy realm configured, then be prepared to provide this information. If you do not have a proxy realm, then you can leave the proxy authentication fields blank.
- Identify shared storage for Oracle Clusterware files and prepare storage if necessary
	During installation, you are asked to provide paths for the following Oracle Clusterware files. These files must be shared across all nodes of the cluster, either on Oracle ASM, or on a supported file system:
	- Voting disks are files that Oracle Clusterware uses to verify cluster node membership and status.
		Voting disk files must be owned by the user performing the installation (`oracle` or `grid`), and must have permissions set to `640`.
		- Oracle Cluster Registry files (OCR) contain cluster and database configuration information for Oracle Clusterware.
		Before installation, OCR files must be owned by the user performing the installation (`grid` or `oracle`). That installation user must have `oinstall` as its primary group. During installation, OUI changes ownership of the OCR files to `root`.
	If your file system does not have external storage redundancy, then Oracle recommends that you provide two additional locations for the OCR disk, and two additional locations for the voting disks, for a total of six partitions (three for OCR, and three for voting disks). Creating redundant storage locations protects the OCR and voting disk in the event of a failure. To completely protect your cluster, the storage locations given for the copies of the OCR and voting disks should have completely separate paths, controllers, and disks, so that no single point of failure is shared by storage locations.
	When you select to store the OCR on Oracle ASM, the default configuration is to create the OCR on one Oracle ASM disk group. If you create the disk group with normal or high redundancy, then the OCR is protected from physical disk failure.
	To protect the OCR from logical disk failure, create another Oracle ASM disk group after installation and add the OCR to the second disk group using the `ocrconfig` command.
	See Also:
	[Chapter 2, "Advanced Installation Oracle Grid Infrastructure for a Cluster Preinstallation Tasks"](prelinux.md) and [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/toc.htm) for information about adding disks to disk groups
- Ensure cron jobs do not run during installation
	If the installer is running when daily cron jobs start, then you may encounter unexplained installation problems if your cron job is performing cleanup, and temporary files are deleted before the installation is finished. Oracle recommends that you complete installation before daily cron jobs are run, or disable daily cron jobs that perform cleanup until after the installation is completed.
- Have IPMI Configuration completed and have IPMI administrator account information
	If you intend to use IPMI, then ensure BMC interfaces are configured, and have an administration account username and password to provide when prompted during installation.
	For nonstandard installations, if you must change configuration on one or more nodes after installation (for example, if you have different administrator usernames and passwords for BMC interfaces on cluster nodes), then decide if you want to reconfigure the BMC interface, or modify IPMI administrator account information after installation.
- Ensure that the Oracle home path you select for the Oracle Grid Infrastructure home uses only ASCII characters
	This restriction includes installation owner user names, which are used as a default for some home paths, as well as other directory names you may select for paths.
- Unset Oracle environment variables. If you have set `ORA_CRS_HOME` as an environment variable, then unset it before starting an installation or upgrade. You should never use `ORA_CRS_HOME` as a user environment variable.
	If you have had an existing installation on your system, and you are using the same user account to install this installation, then unset the following environment variables: `ORA_CRS_HOME`; `ORACLE_HOME`; `ORA_NLS10`; `TNS_ADMIN`
- Decide if you want to use the Software Updates option. OUI can install critical patch updates, system requirements updates (hardware, operating system parameters, and kernel packages) for supported operating systems, and other significant updates that can help to ensure your installation proceeds smoothly. Oracle recommends that you enable software updates during installation.
	If you choose to enable software updates, then during installation you must provide a valid My Oracle Support user name and password during installation, so that OUI can download the latest updates, or you must provide a path to the location of an software updates packages that you have downloaded previously.
	If you plan to run the installation in a secured data center, then you can download updates before starting the installation by starting OUI on a system that has Internet access in update download mode. To start OUI to download updates, enter the following command:
	```
	$ ./runInstaller -downloadUpdates
	```
	Provide the My Oracle Support user name and password, and provide proxy settings if needed. After you download updates, transfer the update file to a directory on the server where you plan to run the installation.

## 4.2 Preparing to Install Oracle Clusterware on IBM: Linux on System z

Because IBM: Linux on System z does not support the direct attachment of DVD-ROM drives, you must copy the installation files from the discs to a hard disk on a system that supports a DVD-ROM drive, or download installation files to your system from the Oracle Technology Network Web site:

`http://www.oracle.com/technology/software`

If you copy the installation files to another system, then:

For each disc, create a directory named Diskn, where n is the disc number, and then copy the files from the disc to that directory.

After you have copied the installation files, you can use one of the following methods to access them on IBM: Linux on System z:

- Copy the installation files to IBM: Linux on System z (for example, using FTP).
- Use a method such as NFS or Samba to make the file system containing the installation files available on IBM: Linux on System z.

Note:

On IBM: Linux on System z servers, due to a block size compatibility issue, you cannot use ASMLIB with SCSI storage devices and Fibre Channel Protocol (FCP) for Oracle Grid Infrastructure release 11.2.0.1 and later.

## 4.3 Installing Oracle Grid Infrastructure

This section provides you with information about how to use the installer to install Oracle Grid Infrastructure. It contains the following sections:

- Running OUI to Install Oracle Grid Infrastructure
- Installing Oracle Grid Infrastructure Using a Cluster Configuration File

### 4.3.1 Running OUI to Install Oracle Grid Infrastructure

Complete the following steps to install Oracle Grid Infrastructure (Oracle Clusterware and Oracle Automatic Storage Management) on your cluster. At any time during installation, if you have a question about what you are being asked to do, click the Help button on the OUI page.

1. Change to the `/Disk1` directory on the installation media, or where you have downloaded the installation binaries, and run the `runInstaller` command. For example:
	```
	$ cd /home/grid/oracle_sw/Disk1
	$ ./runInstaller
	```
2. Select Typical or Advanced installation.
3. Provide information or run scripts as `root` when prompted by OUI. If you need assistance during installation, click Help. Click Details to see the log file. If `root.sh` fails on any of the nodes, then you can fix the problem and follow the steps in [Section 6.5, "Deconfiguring Oracle Clusterware Without Removing Binaries,"](rem_orcl.md) rerun `root.sh` on that node, and continue.
	Note:
	You must run the `root.sh` script on the first node and wait for it to finish. If your cluster has four or more nodes, then `root.sh` can be run concurrently on all nodes but the first and last. As with the first node, the `root.sh` script on the last node must be run separately.
4. After you run `root.sh` on all the nodes, OUI runs Net Configuration Assistant (`netca`) and Cluster Verification Utility. These programs run without user intervention.
5. Oracle Automatic Storage Management Configuration Assistant (`asmca`) configures Oracle ASM during the installation.

When you have verified that your Oracle Grid Infrastructure installation is completed successfully, you can either use it to maintain high availability for other applications, or you can install an Oracle database.

The following is a list of additional information to note about installation:

- If you are installing on Linux systems, you are using the ASM library driver (ASMLIB), and you select Oracle Automatic Storage Management (Oracle ASM) during installation, then Oracle ASM default discovery finds all disks that ASMLIB marks as Oracle ASM disks.
- If you intend to install Oracle Database 11g Release 2 (11.2) with Oracle RAC, then refer to Oracle Real Application Clusters Installation Guide for Linux.
	See Also:
	[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/clonecluster.htm#CWADD03202) for cloning Oracle Grid Infrastructure, and [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/clonerac.htm#RACAD03202) for information about using cloning and node addition procedures for adding Oracle RAC nodes
- When you run `root.sh` during Oracle Grid Infrastructure installation, the Trace File (TF) Analyzer and Collector is also installed in the directory `grid_home` `/tfa`.
	See Also:
	[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/troubleshoot.htm#CWADD92407) for information about using Trace File Analyzer and Collector

### 4.3.2 Installing Oracle Grid Infrastructure Using a Cluster Configuration File

During installation of Oracle Grid Infrastructure, you are given the option either of providing cluster configuration information manually, or of using a cluster configuration file. A cluster configuration file is a text file that you can create before starting OUI, which provides OUI with cluster node addresses that it requires to configure the cluster.

Oracle suggests that you consider using a cluster configuration file if you intend to perform repeated installations on a test cluster, or if you intend to perform an installation on many nodes.

To create a cluster configuration file manually, start a text editor, and create a file that provides the name of the public and virtual IP addresses for each cluster member node, in the following format:

```
node1 node1-vip 
node2 node2-vip
.
.
.
```

For example:

```
mynode1 mynode1-vip
mynode2 mynode2-vip
```

## 4.4 Installing Oracle Grid Infrastructure Using a Software-Only Installation

This section contains the following tasks:

- Installing the Software Binaries
- Configuring the Software Binaries
- Configuring the Software Binaries Using a Response File

Note:

Oracle recommends that only advanced users should perform the software-only installation, as this installation option requires manual postinstallation steps to enable the Oracle Grid Infrastructure software.

A software-only installation consists of installing Oracle Grid Infrastructure for a cluster on one node.

If you use the Install Grid Infrastructure Software Only option during installation, then this installs the software binaries on the local node. To complete the installation for your cluster, you must perform the additional steps of configuring Oracle Clusterware and Oracle ASM, creating a clone of the local installation, deploying this clone on other nodes, and then adding the other nodes to the cluster.

See Also:

[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/clonecluster.htm#CWADD03202) for information about how to clone an Oracle Grid Infrastructure installation to other nodes, and then adding them to the cluster

### 4.4.1 Installing the Software Binaries

To perform a software-only installation:

1. On the local node, verify that the cluster node meets installation requirements using the command `runcluvfy.sh stage -pre crsinst`. Ensure that you have completed all storage and server preinstallation requirements.
2. Run the `runInstaller` command from the relevant directory on the Oracle Database 11g Release 2 (11.2) installation media or download directory. For example:
	```
	$ cd /home/grid/oracle_sw/Disk1
	$ ./runInstaller
	```
3. Complete a software-only installation of Oracle Grid Infrastructure on the first node.
4. When the software has been installed, run the `orainstRoot.sh` script when prompted.
5. For installations with Oracle RAC release 11.2.0.2 and later, proceed to step 6. For installations with Oracle RAC release 11.2.0.1, to relink Oracle Clusterware with the Oracle RAC option enabled, run commands similar to the following (in this example, the Grid home is `/u01/app/11.2.0/grid`):
	```
	$ cd /u01/app/11.2.0/grid/
	$ set env ORACLE_HOME pwd
	$ cd rdbms/lib
	$ make -f ins_rdbms.mk rac_on ioracle
	```
6. The `root.sh` script output provides information about how to proceed, depending on the configuration you plan to complete in this installation. Make note of this information.
	However, ignore the instruction to run the `roothas.pl` script, unless you intend to install Oracle Grid Infrastructure on a standalone server (Oracle Restart).
7. On each remaining node, verify that the cluster node meets installation requirements using the command `runcluvfy.sh stage -pre crsinst`. Ensure that you have completed all storage and server preinstallation requirements.
8. Use Oracle Universal Installer as described in steps 1 through 4 to install the Oracle Grid Infrastructure software on every remaining node that you want to include in the cluster, and complete a software-only installation of Oracle Grid Infrastructure on every node.
	For Oracle Grid Infrastructure 11.2.0.2 and later, configure the cluster using the full OUI configuration wizard GUI as described in Section 4.4.2, "Configuring the Software Binaries," or configure the cluster using a response file as described in section Section 4.4.3, "Configuring the Software Binaries Using a Response File."

### 4.4.2 Configuring the Software Binaries

Configure the software binaries by starting Oracle Grid Infrastructure configuration wizard in GUI mode, available in release 11.2.0.2 and later:

1. Log in to a terminal as the Grid infrastructure installation owner, and change directory to `grid_home` `/crs/config`.
2. Enter the following command:
	```
	$ ./config.sh
	```
	The configuration script starts OUI in Configuration Wizard mode. Provide information as needed for configuration. Each page shows the same user interface and performs the same validation checks that OUI normally does. However, instead of running an installation, the configuration wizard mode validates inputs and configures the installation on all cluster nodes.
3. When you complete inputs, OUI shows you the Summary page, listing all inputs you have provided for the cluster. Verify that the summary has the correct information for your cluster, and click Install to start configuration of the local node.
	When configuration of the local node is complete, OUI copies the Oracle Grid Infrastructure configuration file to other cluster member nodes.
4. When prompted, run root scripts.
5. When you confirm that all root scripts are run, OUI checks the cluster configuration status, and starts other configuration tools as needed.

### 4.4.3 Configuring the Software Binaries Using a Response File

When you install or copy Oracle Grid Infrastructure software on any node, you can defer configuration for a later time. This section provides the procedure for completing configuration after the software is installed or copied on nodes, using the configuration wizard utility (`config.sh`), available with release 11.2.0.2 and later.

See Also:

[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/admin.htm#CWADD92094) for more information about the configuration wizard.

To configure the Oracle Grid Infrastructure software binaries using a response file:

1. As the Oracle Grid Infrastructure installation owner (`grid`) start OUI in Oracle Grid Infrastructure configuration wizard mode from the Oracle Grid Infrastructure software-only home using the following syntax, where Grid\_home is the Oracle Grid Infrastructure home, and filename is the response file name:
	Grid\_home/crs/config/config.sh \[-debug\] \[-silent -responseFile filename\]
	For example:
	```
	$ cd /u01/app/grid/crs/config/
	$ ./config.sh -responseFile /u01/app/grid/response/response_file.rsp
	```
	The configuration script starts OUI in Configuration Wizard mode. Each page shows the same user interface and performs the same validation checks that OUI normally does. However, instead of running an installation, The configuration wizard mode validates inputs and configures the installation on all cluster nodes.
2. When you complete inputs, OUI shows you the Summary page, listing all inputs you have provided for the cluster. Verify that the summary has the correct information for your cluster, and click Install to start configuration of the local node.
	When configuration of the local node is complete, OUI copies the Oracle Grid Infrastructure configuration file to other cluster member nodes.
3. When prompted, run root scripts.
4. When you confirm that all root scripts are run, OUI checks the cluster configuration status, and starts other configuration tools as needed.

## 4.5 Restrictions for Oracle Berkeley DB

The Oracle Berkeley DB embedded database installation that is included with Oracle Grid Infrastructure for a Cluster 11g release 2 (11.2.0.2) is only for use with the Oracle Grid Infrastructure installation products. Refer to terms of the Berkeley DB license at the following URL for details:

```
http://www.oracle.com/technetwork/database/berkeleydb/downloads/index.html
```

## 4.6 Confirming Oracle Clusterware Function

After installation, log in as `root`, and use the following command syntax on each node to confirm that your Oracle Clusterware installation is installed and running correctly:

crsctl check crs

For example:

```
$ crsctl check crs
 
CRS-4638: Oracle High Availability Services is online
CRS-4537: Cluster Ready Services is online
CRS-4529: Cluster Synchronization Services is online
CRS-4533: Event Manager is online
```

Caution:

After installation is complete, do not remove manually or run cron jobs that remove `/tmp/.oracle` or `/var/tmp/.oracle` or its files while Oracle Clusterware is up. If you remove these files, then Oracle Clusterware could encounter intermittent hangs, and you will encounter error CRS-0184: Cannot communicate with the CRS daemon.

## 4.7 Confirming Oracle ASM Function for Oracle Clusterware Files

If you installed the OCR and voting disk files on Oracle ASM, then use the following command syntax as the Oracle Grid Infrastructure installation owner to confirm that your Oracle ASM installation is running:

srvctl status asm

For example:

```
$ srvctl status asm
ASM is running on node1,node2
```

Oracle ASM is running only if it is needed for Oracle Clusterware files. If you have not installed OCR and voting disks files on Oracle ASM, then the Oracle ASM instance should be down.

Note:

To manage Oracle ASM or Oracle Net 11g release 2 (11.2) or later installations, use the `srvctl` binary in the Oracle Grid Infrastructure home for a cluster (Grid home). If you have Oracle Real Application Clusters or Oracle Database installed, then you cannot use the `srvctl` binary in the database home to manage Oracle ASM or Oracle Net.

## 4.8 Understanding Offline Processes in Oracle Grid Infrastructure

Oracle Grid Infrastructure provides required resources for various Oracle products and components. Some of those products and components are optional, so you can install and enable them after installing Oracle Grid Infrastructure. To simplify postinstall additions, Oracle Grid Infrastructure preconfigures and registers all required resources for all products available for these products and components, but only activates them when you choose to add them. As a result, some components may be listed as OFFLINE after the installation of Oracle Grid Infrastructure.

Resources listed as TARGET:OFFLINE and STATE:OFFLINE do not need to be monitored. They represent components that are registered, but not enabled, so they do not use any system resources. If an Oracle product or component is installed on the system, and it requires a particular resource to be online, then the software will prompt you to activate the required offline resource.

The Oracle GSD (Global Service Daemon) process, `ora.gsd`, is typically offline. You must enable Oracle GSD manually if you plan to use an Oracle 9i Real Application Clusters database on the Oracle Clusterware 11g Release 2 (11.2) cluster. Follow the steps under [Section 5.3.4, "Enabling The Global Services Daemon (GSD) for Oracle Database Release 9.2"](postinst.md) to active the Oracle GSD Daemon.