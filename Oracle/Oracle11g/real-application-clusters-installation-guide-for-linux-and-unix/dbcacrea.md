---
title: Creating Oracle Real Application Clusters Databases with Database Configuration Assistant
book: Real Application Clusters Installation Guide for Linux and UNIX
doc_id: E41962-05
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e41962/dbcacrea.htm
tags:
  - oracle
  - 11g
  - real-application-clusters-installation-guide-for-linux-and-unix
---

## 3 Creating Oracle Real Application Clusters Databases with Database Configuration Assistant

This chapter describes how to use Database Configuration Assistant (DBCA) in standalone mode to create and delete Oracle Real Application Clusters (Oracle RAC) databases. The topics in this chapter include the following:

## 3.1 Using Database Configuration Assistant with Oracle RAC

DBCA has the following primary database functions:

- Create and delete databases
- Add and delete database instances
- Set up network configurations for databases and their instances
- Register databases in Oracle Enterprise Manager Grid Control or configure Database Control
- Configure database options, such as Oracle Database Vault
- Start up databases and their instances
	Note:
	Cluster Managed Services are no longer managed through DBCA. Instead, use the cluster managed services page in Oracle Enterprise Manager DB Control (accessible from the Cluster Database Availability Page). For more information, refer to the Oracle Real Application Clusters Administration and Deployment Guide.

See Also:

- "Creating an Oracle RAC Database with DBCA" for more information about using DBCA in standalone mode
- The [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm) to resolve problems—for example, with the listener configuration—and for further information about Lightweight Directory Access Protocol (LDAP)-compliant directory support
- The [Oracle Enterprise Manager Real Application Clusters Guide Online Help](https://docs.oracle.com/cd/E11882_01/rac.112/e17264/toc.htm) for more information about using Oracle Enterprise Manager

## 3.2 Benefits of Using Database Configuration Assistant

Oracle recommends that you use DBCA to create your Oracle RAC database, because preconfigured databases optimize your environment for features such as the server parameter file (SPFILE), and automatic undo management. If you use Oracle ASM or cluster file system storage, then DBCA also configures automated backup, which uses the Fast Recovery Area.

DBCA enables you to create both policy-managed and administrator-managed databases. With DBCA, you can also create site-specific tablespaces as part of database creation. If you have data file requirements that differ from those offered by DBCA templates, then create your database with DBCA and modify the data files later. You can also run user-specified scripts as part of your database creation process.

DBCA also configures your Oracle RAC environment for various Oracle high availability features, such as cluster administration tools. DBCA also starts any database instances required to support your defined configuration.

## 3.3 Automatic Listener Migration from Earlier Releases

If your system has an Oracle Database 10g or 11g installation, and you install Oracle Database 11g release 2 (11.2) either to coexist with or to upgrade the Oracle Database 10.1, 10.2, or 11.1 installation, then most installation types automatically migrate the existing Oracle Database listener to the 11g release 2 (11.2) Oracle home. During migration, they configure and start a default Oracle Net listener using the same TCP/IP port as the existing listener, with the IPC key value.

During the Oracle Clusterware upgrade, the default listener (LISTENER\_NODENAME was migrated to the Oracle Grid Infrastructure home (Grid home). DBCA always uses the default listener.

The listener migration process stops the listener in the existing Oracle home, and restarts it in the new Oracle home. If the database was using the default listener (LISTENER\_NODENAME), then it is migrated automatically to the Oracle Clusterware home by NETCA as part of the Oracle Clusterware upgrade. If the database was using a nondefault listener, then DBUA migrates the nondefault listener to the Oracle Database home.

During migration, client applications may not be able to connect to any databases that are registered to the listener that is being migrated.

## 3.4 Setting Environment Variables for Enterprise Manager DB Control

In previous releases of Oracle Database, you were required to set environment variables for ORACLE\_HOME and ORACLE\_SID to start, stop, and check the status of Enterprise Manager. With Oracle Database 11g release 2 (11.2) and later, you need to set the environment variables ORACLE\_HOME and ORACLE\_UNQNAME to use Enterprise Manager. For example, on each node, enter commands similar to the following to set these values for the `oracle` user with the Bourne shell as the default shell, where the Oracle home is `/u01/app/oracle`, and where the database unique name is `sales`:

```
$ export ORACLE_HOME=/u01/app/oracle/product/11.2/dbhome1
$ export ORACLE_UNQNAME=sales
```

Place these environment variables in the `oracle` user profile file on each cluster member node to ensure that the environment variable settings are available after system restarts.

## 3.5 Verifying Requirements for DBCA

To use DBCA to change the database configuration, use Cluster Verification Utility (CVU) to verify that your system is prepared for configuration changes using the following command syntax:

```
/Grid_home/bin/cluvfy stage -pre dbcfg -fixup -n node_list -d Oracle_home [-verbose]
```

In the preceding syntax example, the variable `Grid_home` is the Oracle Grid Infrastructure home, the variable `node_list` is the list of nodes in your cluster, separated by commas, and the variable `Oracle_home` is the path for the Oracle home directory where OUI creates or modifies the database. The `-fixup` flag generates a fixup script that can be run as root to resolve many operating system configuration tasks if they were not completed before you run the check.

For example, to perform a check to determine if your system is prepared for an Oracle Database with Oracle RAC installation on a two-node cluster with nodes node1 and node2, with the Oracle Grid Infrastructure home path `/u01/app/grid/11.2.0`, and with the Oracle home path `/u01/app/oracle/product/11/db1`, enter the following command:

```
$ /u01/app/grid/11.2.0/bin/cluvfy stage -pre dbcfg -fixup -n node1,node2 -d\
/u01/app/oracle/product/11/db1
```

You can select the option `-verbose` to receive progress updates as the CVU performs its system checks, and detailed reporting of the test results.

If the CVU summary indicates that the cluster verification check fails, and you cannot resolve these issues by running the fixup script, then review and correct the relevant system configuration steps, and run the test again.

The command `cluvfy.sh stage -pre dbcfg` verifies the following:

- Node Reachability: All the specified nodes are reachable from the local node.
- User Equivalence: User equivalence exists on all the specified nodes.
- Node Connectivity: Connectivity exists between all the specified nodes through the available public and private network interfaces.
- Administrative Privileges: The `oracle` user has proper administrative privileges on the specified nodes for creating an Oracle RAC database.
- Oracle Clusterware Integrity: All the components of the Oracle Clusterware stack are fully operational.

## 3.6 Creating an Oracle RAC Database with DBCA

To create a database with DBCA in standalone mode without Oracle ASM or a cluster file system, you must have configured shared storage devices. In addition, you must have run the Oracle Net Configuration Assistant (NETCA) to configure your Oracle Net `listener.ora` file. To run DBCA, you no longer need to set operating system environment variables ORACLE\_HOME to the Oracle RAC database home, or ORACLE\_UNQNAME to the database unique name.

You can use DBCA to create a database from templates supplied by Oracle, or from templates that you create. The templates contain settings optimized for a particular type of workload.

Oracle ships templates for the following two workload types:

- General purpose or transaction processing
- Data warehouse

For more complex environments, you can select the Custom Database option. This option does not use templates and results in a more extensive interview, which means that it takes longer to create your database.

Click Show Details to see the configuration for each type of database. Select the template suited to the type of workload your database will support. If you are not sure which to choose, then select the default General Purpose or Transaction Processing template.

To start DBCA, connect as the installation owner account (for example, `oracle`) to one of your nodes where Oracle RAC is installed, load SSH keys into memory, and enter the command `dbca` command from the `$ORACLE_HOME/bin` directory.

Note:

In an Oracle RAC environment, you must load SSH keys into memory for the terminal session where you start DBCA. If you do not do this, then you receive user equivalency errors when you attempt to start DBCA. If you use a pass phrase on your system for SSH, then you must provide the pass phrase to load the SSH keys.

Use the following commands to load SSH keys:

```
$ exec /usr/bin/ssh-agent $SHELL
$ /usr/bin/ssh-add
```

If needed, provide the pass phrase when prompted. You can then start DBCA.

When you start DBCA, the first page it displays is the Welcome page for Oracle RAC, which includes the option to select an Oracle RAC database. DBCA displays this Oracle RAC Welcome page only if the Oracle home from which it is started was installed on a cluster.

If the Oracle RAC Welcome page opens, then provide information as prompted by DBCA. Click Help if you need assistance.

If DBCA does not display the Welcome page for Oracle RAC, then DBCA was unable to detect if the Oracle home is installed on a cluster. In this case, check that the OUI inventory is correctly located in the directory `/etc/oraInst.loc`, and that the `oraInventory` file is not corrupted. Also, perform clusterware diagnostics by using the following CVU command syntax:

```
/Grid_home/bin/cluvfy/cluvfy.sh stage -post crsinst -n nodelist
.
```

For example, with the mountpoint `/u01/app/grid/11.2.0`, and nodes `node1` and `node2`, run the following command:

```
$ /u01/app/grid/11.2.0/bin/cluvfy stage -post crsinst -n node1,node2
```

Note the following important information when using DBCA:

- If nodes that are part of your cluster installation do not appear on the Node Selection page, then run Opatch lsinventory to perform inventory diagnostics and CVU to perform clusterware diagnostics.
- The global database name can be up to 30 characters in length, and must begin with an alphabetic character. The domain portion of the global database name can be no more than 128 characters and can contain only alphabetic and numeric characters, as well as the period (.) character.
- The `SID` prefix must begin with an alphabetic character.
- The maximum number of characters you can use for the SID prefix is 8 characters. DBCA uses the SID prefix to generate a unique value for the variable `ORACLE_SID` for each instance.
- On the Management Options page, you are provided with selections for Oracle Enterprise Manager monitoring and management interfaces.
	Database Control is always an option. If DBCA discovers Grid Control agents on the cluster, then it also provides you with the option Enterprise Manager with the Grid Control. Choose between Database Control and Grid Control interfaces.
	You can enable daily backup operations. For daily backups, you enter the backup time and operating system credentials for the user that performs backup operations.
	You can no longer set up e-mail notification either from DBCA or OUI with Oracle RAC 11g release 11.2.0.2 and later.
- Note that with Oracle RAC 11g release 2 and later, the storage administration role, SYSASM, requires membership in the OSASM group. This group may not be the same as OSDBA, whose members are granted the SYSDBA privilege. Tasks that require the SYSASM privilege in this list are marked with SYSASM Privilege.
- SYSASM Privilege: To use a Fast Recovery Area, Oracle recommends that you create at least two separate Oracle ASM disk groups: one for the database area and one for the recovery area. Oracle recommends that you place the database area and the recovery area in separate failure groups. If you have divided administrative privileges, then ask your storage administrator to set up the Fast Recovery Area.
	A failure group is defined by shared hardware, such as a controller shared between two storage devices, or two disks that are on the same spindle. If two storage devices share hardware that could fail, making both storage devices unavailable, then these storage devices are said to be in the same failure group.
	If you do not use Oracle ASM, then Oracle recommends that the data files and the Fast Recovery Area are located outside of the Oracle home, in separate locations, as with separate Oracle ASM failure groups, so that a hardware failure does not affect availability.
	See Also:
	[Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/toc.htm) for more information about using a Fast Recovery Area, and [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/toc.htm) for information about failure groups and best practices for high availability and recovery
- SYSASM Privilege: On the Oracle ASM Disk Groups page, if you do not see the storage devices that you want to add, then click Change Disk Discovery Path to alter the search path used by DBCA to find available storage devices. You can select storage devices with a status of `Candidate` or `Former` (never used in an Oracle ASM disk group or no longer in a group) by selecting the box. If you want to add storage devices that still have Oracle ASM disk headers, but the disk group is no longer in use (a case that can occur if you are selecting storage devices after an aborted install, you attempted deinstallation without dropping the disk group, or other configuration problems), then use the `Force` command.
- On the Recovery Configuration page, if you are using Oracle ASM or cluster file system storage, then you can also select the Fast Recovery Area and size on the Recovery Configuration page. If you are using Oracle ASM, then the Fast Recovery Area defaults to the Oracle ASM Disk Group. If you are using OCFS2, then the Fast Recovery Area defaults to `$ORACLE_BASE/flash_recovery_area`.
- On the Initialization Parameters page, if you are installing on a Linux system, note that Memory Size (SGA and PGA), which sets the initialization parameter `MEMORY_TARGET` or `MEMORY_MAX_TARGET`, cannot be greater than the shared memory filesystem on your operating system.
	For example, if the shared memory filesystem allocation on your system is 1 GB, but you set Memory Size (`MEMORY_TARGET`) to 2 GB, then you receive the following error during database startup:
	```
	ORA-00845: MEMORY_TARGET not supported on this system 
	ORA-01078: Failure in processing system parameters
	```
	This issue is not relevant for other platforms.
	For all platforms, if you intend to add more nodes in your cluster than you have during the current DBCA session, then click All Initialization Parameters, and change the parameter `CLUSTER_DATABASE_INSTANCES` to the total number of nodes that you plan to add to the cluster.
	In addition, if you click All Initialization Parameters, note that if your global database name is longer than 8 characters, then the database name value (in the `DB_NAME` parameter) is truncated to the first 8 characters, and the `DB_UNIQUE_NAME` parameter value is set to the global name.
	See Also:
	[Oracle Database Administrator's Reference for Linux and UNIX-Based Operating Systems](https://docs.oracle.com/cd/E11882_01/server.112/e10839/toc.htm) for information about initialization parameters

After you respond to DBCA prompts, review the Summary dialog information and click OK, DBCA does the following:

- Creates an operative Oracle RAC database and its instances
- Creates the Oracle RAC data dictionary views
- Configures the network for the cluster database
- Migrates previous release Oracle Database listeners and related files to the Oracle Database 11g Oracle home
- Starts the listeners and database instances, and then starts the high availability services
- Configures Oracle Enterprise Manager Database Control or Grid Control

Caution:

After you have created the database, if you decide that you want to install additional Oracle Database products in the database you have created, then you must stop all processes running in the Oracle home before you attempt to install the additional products, so that Oracle Universal Installer can relink certain executables and libraries. Refer to [Appendix E, "How to Stop Processes in an Existing Oracle Real Application Clusters Database"](procstop.md) for additional information.

## 3.7 Deleting an Oracle RAC Database with DBCA

This section explains how to delete an Oracle RAC database with DBCA. This process deletes a database and removes a database's initialization parameter files, instances, OFA structure, and an Oracle network configuration. However, this process does not remove data files if you placed the files on raw devices or on raw partitions.

To delete a database with DBCA:

1. Start DBCA on one of the nodes:.
	- Run the `dbca` command from the `$ORACLE_HOME/bin` directory.
	The DBCA Welcome page appears.
2. Select Oracle Real Application Clusters, and click Next.
	After you click Next, DBCA displays the Operations page.
3. Select Delete a database, and click Next. DBCA displays the List of Cluster Databases page.
4. If your user ID and password are not operating-system authenticated, then the List of Cluster Databases page displays the user name and password fields. If these fields appear, then enter a user ID and password for a user account that has `SYSDBA` privileges.
5. Select the database to delete, and click Finish.
	After you click Finish, DBCA displays a dialog box to confirm the database and instances that DBCA is going to delete.
6. Click OK to begin the deletion of the database and its associated files, services, and environment settings, or click Cancel to stop the operation.

When you click OK, DBCA continues the operation and deletes all the associated instances for this database. DBCA also removes the parameter files, password files, and `oratab` entries.

At this point, you have accomplished the following:

- Deleted the selected database from the cluster
- Deleted high availability services that were assigned to the database
- Deleted the Oracle Net configuration for the database
- Deconfigured Database Control for that database
- Deleted the OFA directory structure for that database from the cluster
- Deleted the data files if the data files were not on raw devices