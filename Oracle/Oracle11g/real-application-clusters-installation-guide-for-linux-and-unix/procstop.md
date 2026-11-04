---
title: How to Stop Processes in an Existing Oracle Real Application Clusters Database
book: Real Application Clusters Installation Guide for Linux and UNIX
doc_id: E41962-05
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e41962/procstop.htm
tags:
  - oracle
  - 11g
  - real-application-clusters-installation-guide-for-linux-and-unix
---

## E How to Stop Processes in an Existing Oracle Real Application Clusters Database

This appendix describes how to stop all processes in an Oracle Real Application Clusters (Oracle RAC) database, in preparation for adding additional products to an existing database, or in preparation for patch updates. This appendix contains the following topics:

## E.1 Backing Up the Oracle RAC Database

Before you make any changes to the Oracle software, Oracle recommends that you create a backup of the Oracle Database installation.

## E.2 Shutting Down Oracle RAC Databases

Shut down any existing Oracle Database instances on each node, with normal or immediate priority. You can use Oracle Enterprise Manager or SRVCTL to shut down the Oracle RAC databases and their instances.

Note:

If you are using Oracle Clusterware or Cluster Ready Services, then you must shut down all Oracle Database instances on all of the cluster nodes before modifying the Oracle software. If you are performing a patch update, then review the instructions in the Patch Set Notes for detailed instructions.

## E.3 Stopping All Oracle Processes

Stop all listener and other processes that are running in the Oracle home directories where you want to modify the database software.

Note:

Before you can shut down Oracle ASM instances, Oracle Clusterware, or Oracle Restart, you must first shut down all database instances that use them.

This section contains the following topics:

- Stopping Oracle Database Processes Before Adding Products or Upgrading
- Stopping Oracle Clusterware and Oracle ASM Instances

### E.3.1 Stopping Oracle Database Processes Before Adding Products or Upgrading

This section provides an overview of what needs to be done before adding additional products to Oracle Database 11g release 2 (11.2). If you are performing a patch upgrade, then refer to the Database Patch Set Notes for the patch for additional instructions.

Note:

You must perform these steps in the order listed.
1. Shut down any processes in the Oracle home on each node that can access a database.
	Note:
	Before you shut down any processes that are monitored by Enterprise Manager Grid Control, set a blackout in Grid Control for the processes that you intend to shut down. This is necessary so that the availability records for these processes indicate that the shutdown was planned downtime, rather than an unplanned system outage.
	For example:
	```
	$ORACLE_HOME/bin/emctl stop dbconsole
	```
2. Shut down all Oracle RAC instances on all nodes. To shut down all Oracle RAC instances for a database, enter the following command, where `db_name` is the name of the database:
	```
	$ oracle_home/bin/srvctl stop database -d db_name
	```

### E.3.2 Stopping Oracle Clusterware and Oracle ASM Instances

If you are modifying an Oracle Clusterware or Oracle Cluster Ready Services (CRS) installation, then shut down the following Oracle Database services.

Note:

You must perform these steps in the order listed.
1. Shut down any processes in the Oracle home on each node that might be accessing a database; for example, Oracle Enterprise Manager Database Control.
	Note:
	Before you shut down any processes that are monitored by Oracle Enterprise Manager Grid Control, set a blackout in Grid Control for the processes that you intend to shut down. This is necessary so that the availability records for these processes indicate that the shutdown was planned downtime, rather than an unplanned system outage.
2. Shut down all Oracle RAC instances on all nodes. To shut down all Oracle RAC instances for a database, enter the following command, where `db_name` is the name of the database:
	```
	$ oracle_home/bin/srvctl stop database -d db_name
	```
3. Stop all node applications on all nodes. To stop node applications running on a node, enter the following command, where `u01/app/grid/11.2.0` is the Oracle Grid Infrastructure home, and `node` is the name of the node where the applications are running
	```
	$ u01/app/grid/11.2.0/bin/srvctl stop nodeapps -n node
	```
4. Shut down the Oracle Clusterware or CRS process by entering the following command on all nodes as the `root` user
	```
	# crsctl stop cluster
	```
	To stop Oracle Clusterware and Oracle ASM instances on all nodes in the cluster, you can enter a single command: `crsctl stop cluster -all`.
	Note:
	The `crsctl stop crs` command is used to stop Oracle Restart services for single-instance databases.

## E.4 Using CVU to Validate Readiness for Oracle RAC Upgrades

Review the contents in this section to validate that your Oracle RAC cluster is ready for upgrades.

### E.4.1 About the CVU Database Upgrade Validation Command Options

Use the command `cluvfy stage -predbinst -upgrade` to check the readiness of your Oracle RAC installation for upgrades. Running `cluvfy` with the `-predbinst -upgrade` flags performs system checks to confirm if the cluster is in a correct state for upgrading from an existing Oracle RAC installation.

The command uses the following syntax, where variable content is indicated by italics:

```
cluvfy stage -pre dbinst -upgrade -src_dbhome src_RAChome  -dest_dbhome 
dest_RAChome -dest_version dest_version [-fixup[-fixupdirpath]] [-verbose]
```

The options are:

- `-src_dbhome` `src_RAChome`
	Use this flag to indicate the location of the source Oracle RAC home that you are upgrading, where `src_RAChome` is the path to the home that you want to upgrade.
- `-dest_dbhome` `dest_RAChome`
	Use this flag to indicate the location of the upgrade Oracle RAC home, where `dest_RAChome` is the path to the Oracle RAC home.
- `-dest_version` `dest_version`
	Use the dest\_version flag to indicate the release number of the upgrade, including any patchset. The release number must include the five digits designating the release to the level of the platform-specific patch. For example: 11.2.0.2.0.
	See Also:
	[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/cvu.htm#CWADD91025) for information about release number format
- `-fixup` \[`-fixupdir` `fixupdirpath`\]\]
	Use the `-fixup` flag to indicate that you want to generate instructions for any required steps you need to complete to ensure that your cluster is ready for an upgrade. The default location is the CVU work directory. If you want to place the fixup instructions in a different directory, then add the flag -fixupdir, and provide the path to the fixup directory
- `-verbose`
	Use the `-verbose` flag to produce detailed output of individual checks

### E.4.2 Example of Verifying System Upgrade Readiness for Oracle RAC Infrastructure

You can verify that the permissions required for installing Oracle RAC have been configured on the nodes `node1` and `node2` by running the following command:

```
$ ./cluvfy stage -pre dbinst -upgrade -src_dbhome /u01/app/oracle/product/11.1.0/dbhome_1 -dest_dbhome 
/u01/app/oracle/product/11.2.0/dbhome_1 -dest_version 11.2.0.3.0 -fixup
-fixupdirpath /home/oracle/fixup -verbose
```

### E.4.3 Verifying System Readiness for Oracle Database Upgrades

Use Cluster Verification Utility to assist you with system checks in preparation for starting a database upgrade. The installer runs the appropriate CVU checks automatically, and either prompts you to fix problems, or provides a fixup script to be run on all nodes in the cluster before proceeding with the upgrade.

See Also:

[Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/toc.htm)