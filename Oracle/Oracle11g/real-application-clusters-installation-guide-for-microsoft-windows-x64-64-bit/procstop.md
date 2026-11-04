---
title: How to Stop Processes in an Existing Oracle Real Application Clusters Database
book: Real Application Clusters Installation Guide for Microsoft Windows x64 (64-Bit)
doc_id: E48195-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e48195/procstop.htm
tags:
  - oracle
  - 11g
  - real-application-clusters-installation-guide-for-microsoft-windows-x64-64-bit
---

## E How to Stop Processes in an Existing Oracle Real Application Clusters Database

This appendix describes how to stop all processes in an Oracle Real Application Clusters (Oracle RAC) database, in preparation for adding additional products to an existing database, or in preparation for patch updates. This appendix contains the following topics:

## E.1 Back Up the Oracle RAC Database

Before you make any changes to the Oracle software, Oracle recommends that you create a backup of the Oracle Database installation.

## E.2 Shut Down Oracle RAC Databases

Shut down any existing Oracle Database instances on each node, with normal or immediate priority. You can use Oracle Enterprise Manager or the Server Control (SRVCTL) utility to shut down the Oracle RAC databases and their instances.

Note:

If you are using Oracle Clusterware or Oracle Restart, then you must shut down all Oracle Database instances on all cluster nodes before modifying the Oracle software. If you are performing a patch update, then review the instructions in the Patch Set Notes for detailed instructions.

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/restart.htm#ADMIN12709) for more information about Oracle Restart
- [Section 4.1.3, "Downloading and Installing Patch Updates"](postinst.md) for more information about patches and patch sets

## E.3 Stop All Oracle Processes

Stop all listener and other processes running in the Oracle home directories where you want to modify the database software.

Note:

Before you can shut down Oracle ASM instances, Oracle Clusterware, or Oracle Restart, you must first shut down all database instances that use them.

### E.3.1 Stopping Oracle Database Processes

This section provides an overview of what must be done before adding additional products to Oracle Database 11g release 2 (11.2). If you are updating only the Oracle Database software, then you only need to stop the databases instances that run from the Oracle home being updated. If you are performing a patch upgrade, then refer to the Database Patch Set Notes for the patch for additional instructions.

Note:

You must perform these steps in the order listed.
1. Shut down any processes in the Oracle home on each node that can access a database.
	Note:
	Before you shut down any processes that are monitored by Oracle Enterprise Manager Grid Control, set a blackout in Grid Control for the processes that you intend to shut down. This is necessary so that the availability records for these processes indicate that the shutdown was planned downtime, rather than an unplanned system outage.
	For example:
	```
	C:\> %ORACLE_HOME%\bin\emctl stop dbconsole
	```
2. Shut down all Oracle RAC instances on all nodes. To shut down all Oracle RAC instances for a database, enter the following command, where `db_name` is the name of the database:
	```
	C:\> %ORACLE_HOME%\bin\srvctl stop database -d db_name
	```

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/dbcontrol.htm#ADMIN13424) for information about configuring blackouts with Oracle Enterprise Manager
- [Section 4.1.3, "Downloading and Installing Patch Updates"](postinst.md) for more information about patches and patch sets

### E.3.2 Stopping Oracle Clusterware and Oracle ASM Instances

If you are updating the Oracle Clusterware or Oracle ASM software, then you must first stop all Oracle RAC database instances and all Oracle database instances that use Oracle ASM for storage. After stopping the database instances, shut down the Oracle ASM instances and Oracle Clusterware, as described in the following steps:

Note:

You must perform these steps in the order listed.
1. Shut down any processes in the Oracle home on each node that might be accessing a database, for example, Oracle Enterprise Manager Database Control.
	Note:
	Before you shut down any processes that are monitored by Oracle Enterprise Manager Grid Control, set a blackout in Grid Control for the processes that you intend to shut down. This is necessary so that the availability records for these processes indicate that the shutdown was planned downtime, rather than an unplanned system outage.
2. Shut down all Oracle RAC instances on all nodes. To shut down all Oracle RAC instances for a database, enter the following command, where `db_name` is the name of the database:
	```
	Oracle_home\bin\srvctl stop database -d db_name
	```
3. Stop all Oracle Clusterware node applications and resources on all nodes. To stop node applications running on a node, enter the following command, where `C:\app\11.2.0\grid` is the Grid home, and `node` is the name of the node where the applications run:
	```
	C:\> cd app\11.2.0\grid\bin
	C:\..\bin> srvctl stop nodeapps -n node
	```
4. Shut down the Oracle Clusterware processes and the Oracle ASM instance on each node by entering the following command on all nodes as a user with Administrator privileges:
	```
	C:\app\...\bin> crsctl stop cluster
	```
	To stop Oracle Clusterware and Oracle ASM instances on all nodes in the cluster, you can enter a single command: `crsctl stop cluster -all`.
	Note:
	The `crsctl stop crs` command is used to stop Oracle Restart services for single-instance databases.
5. Shut down the Oracle Clusterware processes from the Services window.
	Access the Services window by clicking Start, selecting Control Panel, selecting Administrative Tools, and then selecting Services. In the Services window, shut down the following services:
	- Oracle Object Service
		- OracleClusterVolumeService
		- OracleOHService
		Note:
		Depending on your configuration, your nodes might not be running all of the services listed.