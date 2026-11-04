---
title: Oracle Grid Infrastructure Postinstallation Procedures
book: Grid Infrastructure Installation Guide for Linux
doc_id: E41961-10
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e41961/postinst.htm
tags:
  - oracle
  - 11g
  - grid-infrastructure-installation-guide-for-linux
---

## 5 Oracle Grid Infrastructure Postinstallation Procedures

This chapter describes how to complete the postinstallation tasks after you have installed the Oracle Grid Infrastructure software.

This chapter contains the following topics:

## 5.1 Required Postinstallation Tasks

Note:

In prior releases, backing up the voting disks using a `dd` command was a required postinstallation task. With Oracle Clusterware 11g release 11.2 and later, backing up and restoring a voting disk using the `dd` command may result in the loss of the voting disk, so this procedure is not supported.

Download and install patch updates. See the My Oracle Support website for required patch updates for your installation.

To download required patch updates:

1. Use a Web browser to view the My Oracle Support website:
	`https://support.oracle.com`
2. Log in to My Oracle Support.
	Note:
	If you are not a My Oracle Support registered user, then click Register for My Oracle Support and register.
3. On the main My Oracle Support page, click Patches & Updates.
4. On the Patches and Updates page, click Product or Family (Advanced).
5. In the Product field, select Oracle Database.
6. In the Release field, select one or more release numbers. For example, Oracle 12.1.0.1.0.
7. Click Search.
8. Any available patch updates are displayed in the Patch Search page.
9. Click the patch number to download the patch.
10. Select the patch number and click Read Me. The README page contains information about the patch set and how to apply the patches to your installation.
11. Return to the Patch Set page, click Download, and save the file on your system.
12. Use the unzip utility provided with Oracle Database 11g Release 2 (11.2) to uncompress the Oracle patch updates that you downloaded from My Oracle Support. The unzip utility is located in the `$ORACLE_HOME/bin` directory.
13. See [Appendix F, "How to Upgrade to Oracle Grid Infrastructure 11g Release 2"](procstop.md) for information about how to stop database processes in preparation for installing patches.

## 5.2 Recommended Postinstallation Tasks

Oracle recommends that you complete the following tasks as needed after installing Oracle Grid Infrastructure:

- Backing Up the root.sh Script
- Tuning Semaphore Parameters
- Creating a Fast Recovery Area Disk Group
- Running Oracle RAC Configuration Audit Tool

### 5.2.1 Backing Up the root.sh Script

Oracle recommends that you back up the `root.sh` script after you complete an installation. If you install other products in the same Oracle home directory, then the installer updates the contents of the existing `root.sh` script during the installation. If you require information contained in the original `root.sh` script, then you can recover it from the `root.sh` file copy.

### 5.2.2 Tuning Semaphore Parameters

Refer to the following guidelines only if the default semaphore parameter values are too low to accommodate all Oracle processes:

Note:

Oracle recommends that you refer to the operating system documentation for more information about setting semaphore parameters.
1. Calculate the minimum total semaphore requirements using the following formula:
	2 \* sum (process parameters of all database instances on the system) + overhead for background processes + system and other application requirements
2. Set `semmns` (total semaphores systemwide) to this total.
3. Set `semmsl` (semaphores for each set) to 250.
4. Set `semmni` (total semaphores sets) to `semmns` divided by `semmsl`, rounded up to the nearest multiple of 1024.

### 5.2.3 Creating a Fast Recovery Area Disk Group

During installation, by default you can create one disk group. If you plan to add an Oracle Database for a standalone server or an Oracle RAC database, then you should create the Fast Recovery Area for database files.

#### 5.2.3.1 About the Fast Recovery Area and the Fast Recovery Area Disk Group

The Fast Recovery Area is a unified storage location for all Oracle Database files related to recovery. Database administrators can define the DB\_RECOVERY\_FILE\_DEST parameter to the path for the Fast Recovery Area to enable on-disk backups, and rapid recovery of data. Enabling rapid backups for recent data can reduce requests to system administrators to retrieve backup tapes for recovery operations.

When you enable Fast Recovery in the `init.ora` file, all RMAN backups, archive logs, control file automatic backups, and database copies are written to the Fast Recovery Area. RMAN automatically manages files in the Fast Recovery Area by deleting obsolete backups and archive files no longer required for recovery.

Oracle recommends that you create a Fast Recovery Area disk group. Oracle Clusterware files and Oracle Database files can be placed on the same disk group, and you can also place Fast recovery files in the same disk group. However, Oracle recommends that you create a separate Fast Recovery disk group to reduce storage device contention.

The Fast Recovery Area is enabled by setting DB\_RECOVERY\_FILE\_DEST. The size of the Fast Recovery Area is set with DB\_RECOVERY\_FILE\_DEST\_SIZE. As a general rule, the larger the Fast Recovery Area, the more useful it becomes. For ease of use, Oracle recommends that you create a Fast Recovery Area disk group on storage devices that can contain at least three days of recovery information. Ideally, the Fast Recovery Area should be large enough to hold a copy of all of your data files and control files, the online redo logs, and the archived redo log files needed to recover your database using the data file backups kept under your retention policy.

Multiple databases can use the same Fast Recovery Area. For example, assume you have created one Fast Recovery Area disk group on disks with 150 GB of storage, shared by three different databases. You can set the size of the Fast Recovery Area for each database depending on the importance of each database. For example, if database1 is your least important database, database 2 is of greater importance and database 3 is of greatest importance, then you can set different DB\_RECOVERY\_FILE\_DEST\_SIZE settings for each database to meet your retention target for each database: 30 GB for database 1, 50 GB for database 2, and 70 GB for database 3.

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/toc.htm)

#### 5.2.3.2 Creating the Fast Recovery Area Disk Group

To create a Fast recovery file disk group:

1. Navigate to the Grid home bin directory, and start Oracle ASM Configuration Assistant (ASMCA). For example:
	```
	$ cd /u01/app/11.2.0/grid/bin
	$ ./asmca
	```
2. ASMCA opens at the Disk Groups tab. Click Create to create a new disk group
3. The Create Disk Groups window opens.
	In the Disk Group Name field, enter a descriptive name for the Fast Recovery Area group. For example: FRA.
	In the Redundancy section, select the level of redundancy you want to use.
	In the Select Member Disks field, select eligible disks to be added to the Fast Recovery Area, and click OK.
4. The Diskgroup Creation window opens to inform you when disk group creation is complete. Click OK.
5. Click Exit.

### 5.2.4 Running Oracle RAC Configuration Audit Tool

Oracle recommends that you run the Oracle RAC Configuration Audit tool (RACcheck) to check your Oracle RAC installation. RACcheck is an Oracle RAC auditing tool that checks various important configuration settings within Oracle Real Application Clusters, Oracle Clusterware, Oracle Automatic Storage Management and the Oracle Grid Infrastructure environment.

Oracle recommends that you download and run the latest version of RACcheck from My Oracle Support. For information about downloading, configuring, and running RACcheck configuration audit tool, refer to My Oracle Support note 1268927.1, which is available at the following URL:

`https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=1268927.1`

See Also:

[Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/racchk.htm#RACAD8365)

## 5.3 Using Older Oracle Database Versions with Grid Infrastructure

Review the following sections for information about using older Oracle Database releases with 11g release 2 (11.2) Oracle Grid Infrastructure installations:

- General Restrictions for Using Older Oracle Database Versions
- Using ASMCA to Administer Disk Groups for Older Database Versions
- Pinning Cluster Nodes for Oracle Database Release 10.x or 11.x
- Enabling The Global Services Daemon (GSD) for Oracle Database Release 9.2
- Using the Correct LSNRCTL Commands

### 5.3.1 General Restrictions for Using Older Oracle Database Versions

You can use Oracle Database release 9.2, release 10.x and release 11.1 with Oracle Clusterware 11g release 2 (11.2).

However, placing Oracle Database homes on Oracle ACFS that are prior to Oracle Database release 11.2 is not supported, because earlier releases are not designed to use Oracle ACFS.

To use Oracle Real Application Clusters release 9.2 with Oracle Clusterware 11g release 2 (11.2), install and run Oracle9i Cluster Manager for the release 9.2 database. Oracle9i Cluster Manager can coexist with Oracle Clusterware.

If you upgrade an existing version of Oracle Clusterware and Oracle ASM to Oracle Grid Infrastructure 11g release 11.2 (which includes Oracle Clusterware and Oracle ASM), and you also plan to upgrade your Oracle RAC database to 11.2, then the required configuration of existing databases is completed automatically when you complete the Oracle RAC upgrade, and this section does not concern you.

However, if you upgrade to Oracle Grid Infrastructure 11g release 11.2, and you have existing Oracle RAC installations you do not plan to upgrade, or if you install older versions of Oracle RAC (9.2, 10.2 or 11.1) on a release 11.2 Oracle Grid Infrastructure cluster, then you must complete additional configuration tasks or apply patches, or both, before the older databases will work correctly with Oracle Grid Infrastructure.

Note:

Before you start an Oracle RAC or Oracle Database installation on an Oracle Clusterware 11g release 11.2 installation, if you are upgrading from releases 11.1.0.7, 11.1.0.6, and 10.2.0.4, then Oracle recommends that you check for the latest recommended patches for the release you are upgrading from, and install those patches as needed on your existing database installations before upgrading.

For more information on recommended patches, refer to "Oracle Upgrade Companion," which is available through Note 785351.1 on My Oracle Support:

`https://support.oracle.com`

You may also refer to Notes 756388.1 and 756671.1 for the current list of recommended patches for each release

### 5.3.2 Using ASMCA to Administer Disk Groups for Older Database Versions

Use Oracle ASM Configuration Assistant (ASMCA) to create and modify disk groups when you install older Oracle databases and Oracle RAC databases on Oracle Grid Infrastructure installations. Starting with 11g release 2, Oracle ASM is installed as part of an Oracle Grid Infrastructure installation, with Oracle Clusterware. You can no longer use Database Configuration Assistant (DBCA) to perform administrative tasks on Oracle ASM.

### 5.3.3 Pinning Cluster Nodes for Oracle Database Release 10.x or 11.x

When Oracle Clusterware 11g release 11.2 is installed on a cluster with no previous Oracle software version, it configures cluster nodes dynamically, which is compatible with Oracle Database Release 11.2 and later, but Oracle Database 10g and 11.1 require a persistent configuration. This process of association of a node name with a node number is called pinning.

Note:

During an upgrade, all cluster member nodes are pinned automatically, and no manual pinning is required for existing databases. This procedure is required only if you install older database versions after installing Oracle Grid Infrastructure release 11.2 software.

To pin a node in preparation for installing or using an older Oracle Database version, use `Grid_home` `/bin/crsctl` with the following command syntax, where `nodes` is a space-delimited list of one or more nodes in the cluster whose configuration you want to pin:

```
crsctl pin css -n nodes
```

For example, to pin nodes `node3` and `node4`, log in as `root` and enter the following command:

```
$ crsctl pin css -n node3 node4
```

To determine if a node is in a pinned or unpinned state, use `Grid_home` `/bin/olsnodes` with the following command syntax:

To list all pinned nodes:

```
olsnodes -t -n
```

For example:

```
# /u01/app/11.2.0/grid/bin/olsnodes -t -n
node1 1       Pinned
node2 2       Pinned
node3 3       Pinned
node4 4       Pinned
```

To list the state of a particular node:

```
olsnodes -t -n node3
```

For example:

```
# /u01/app/11.2.0/grid/bin/olsnodes -t -n node3
node3 3       Pinned
```

See Also:

[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/crsref.htm#CWADD91595) for more information about pinning and unpinning nodes

### 5.3.4 Enabling The Global Services Daemon (GSD) for Oracle Database Release 9.2

By default, the Global Services daemon (GSD) is disabled. If you install Oracle Database 9i release 2 (9.2) on Oracle Grid Infrastructure for a Cluster 11g release 2 (11.2), then you must enable the GSD. Use the following commands to enable the GSD before you install Oracle Database release 9.2:

```
srvctl enable nodeapps -g
srvctl start nodeapps
```

### 5.3.5 Using the Correct LSNRCTL Commands

To administer 11g release 2 local and scan listeners using the `lsnrctl` command, set your `$ORACLE_HOME` environment variable to the path for the Oracle Grid Infrastructure home (Grid home). Do not attempt to use the `lsnrctl` commands from Oracle home locations for previous releases, as they cannot be used with the new release.

## 5.4 Modifying Oracle Clusterware Binaries After Installation

After installation, if you need to modify the Oracle Clusterware configuration, then you must unlock the Grid home.

For example, if you want to apply a one-off patch, or if you want to modify an Oracle Exadata configuration to run IPC traffic over RDS on the interconnect instead of using the default UDP, then you must unlock the Grid home.

Caution:

Before relinking executables, you must shut down all executables that run in the Oracle home directory that you are relinking. In addition, shut down applications linked with Oracle shared libraries.

Unlock the home using the following procedure:

1. Log in as `root`, and change directory to the path Grid\_home/crs/install, where Grid\_home is the path to the Grid home, and unlock the Grid home using the command `rootcrs.pl -unlock -crshome` `Grid_home`, where Grid\_home is the path to your Grid infrastructure home. For example, with the Grid home `/u01/app/11.2.0/grid`, enter the following command:
	```
	# cd /u01/app/11.2.0/grid/crs/install
	# perl rootcrs.pl -unlock -crshome /u01/app/11.2.0/grid
	```
2. Change user to the Oracle Grid Infrastructure software owner, and relink binaries using the command syntax make -f Grid\_home/rdbms/lib/ins\_rdbms.mk target, where Grid\_home is the Grid home, and target is the binaries that you want to relink. For example, where the grid user is `grid`, `$ORACLE_HOME` is set to the Grid home, and where you are updating the interconnect protocol from UDP to IPC, enter the following command:
	```
	# su grid
	$ make -f $ORACLE_HOME/rdbms/lib/ins_rdbms.mk ipc_rds ioracle
	```
	Note:
	To relink binaries, you can also change to the grid installation owner and run the command `Grid_home` `/bin/relink`.
3. Relock the Grid home and restart the cluster using the following command:
	```
	# perl rootcrs.pl -patch
	```
4. Repeat steps 1 through 3 on each cluster member node.