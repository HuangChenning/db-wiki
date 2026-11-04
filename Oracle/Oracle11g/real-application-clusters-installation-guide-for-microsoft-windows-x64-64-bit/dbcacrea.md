---
title: Creating Oracle Real Application Clusters Databases with Oracle Database Configuration Assistant
book: Real Application Clusters Installation Guide for Microsoft Windows x64 (64-Bit)
doc_id: E48195-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e48195/dbcacrea.htm
tags:
  - oracle
  - 11g
  - real-application-clusters-installation-guide-for-microsoft-windows-x64-64-bit
---

## 3 Creating Oracle Real Application Clusters Databases with Oracle Database Configuration Assistant

This chapter describes how to use Oracle Database Configuration Assistant (DBCA) in standalone mode to create and delete Oracle Real Application Clusters (Oracle RAC) databases.

This chapter contains the following topics:

See Also:

[Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/toc.htm) for information about using DBCA to add and delete instances

## 3.1 Using Oracle Database Configuration Assistant with Oracle RAC

DBCA has the following primary database functions:

- Create and delete databases.
- Add and delete database instances.
- Set up network configurations for databases and their instances.
- Register databases in Oracle Enterprise Manager Grid Control or configure Oracle Enterprise Manager Grid Database Control.
- Configure database options, such as Oracle Database Vault.
- Start up databases and their instances.
	Note:
	Cluster Managed Services are no longer managed through DBCA. Instead, use the Cluster Managed Services page in Oracle Enterprise Manager Database Control (accessible from the Cluster Database Availability page). For more information, see Oracle Real Application Clusters Administration and Deployment Guide.

See Also:

- "Creating an Oracle RAC Database with DBCA" for more information about using DBCA in standalone mode
- [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm) to resolve problems—for example, with the listener configuration—and for more information about Lightweight Directory Access Protocol (LDAP)-compliant directory support
- [Oracle Database 2 Day + Real Application Clusters Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e17264/toc.htm) for more information about using Oracle Enterprise Manager

## 3.2 Optimizing Your Database Environment by Using DBCA

Oracle recommends that you use DBCA to create your Oracle RAC database, because preconfigured databases optimize your environment for features such as the server parameter file (SPFILE) and automatic undo management. If you use Oracle Automatic Storage Management (Oracle ASM) or cluster file system storage, then DBCA also configures automated backup, which uses the Fast Recovery Area.

DBCA enables you to create both policy-managed and administrator-managed databases. With DBCA, you can create site-specific tablespaces as part of database creation. If you have data file requirements that differ from those offered by DBCA templates, then create your database with DBCA and modify the data files later. You can also run user-specified scripts as part of your database creation process.

DBCA also configures your Oracle RAC environment for various Oracle high availability features, such as cluster administration tools. DBCA also starts any database instances required to support your defined configuration.

You can use DBCA to create a database from templates supplied by Oracle, or from templates that you create. The templates contain settings optimized for a particular type of workload.

Oracle ships templates for the following two workload types:

- General purpose or transaction processing
- Data warehouse

For more complex environments, you can select the Custom Database option. This option does not use templates and results in a more extensive interview, which means that it takes longer to create your database.

Click Show Details to see the configuration for each type of database. Select the template suited to the type of workload your database will support. If you are not sure which to choose, then select the default General Purpose or Transaction Processing template.

## 3.3 Updating the Listener Used By an Earlier Release

If your system has an Oracle Database 10g or 11g installation, and you install Oracle Database 11g release 2 (11.2) either to coexist with or to upgrade the Oracle Database 10.1, 10.2, or 11.1 installation, then most installation types automatically migrate the existing Oracle Database listener to the 11g release 2 (11.2) Oracle home. During migration, the upgrade process configures and starts a default Oracle Net listener using the same TCP/IP port as the existing listener, with the IPC key value.

During the Oracle Clusterware upgrade, the default listener (LISTENER\_NODENAME) is migrated to the Oracle Grid Infrastructure home (Grid home). DBCA always uses the default listener.

The listener migration process stops the listener in the existing Oracle home, and restarts it in the new Oracle home. If the database uses the default listener (LISTENER\_NODENAME), then the listener is migrated automatically to the Oracle Clusterware home by Oracle Net Configuration Assistant (NETCA) as part of the Oracle Clusterware upgrade. If the database uses a nondefault listener, then DBUA migrates the nondefault listener to the Oracle home.

Note:

During migration, client applications may not be able to connect to any databases that are registered to the listener that is being migrated.

## 3.4 Verifying Requirements for DBCA

To use DBCA to change the database configuration, use Cluster Verification Utility (CVU) to verify that your system is prepared for configuration changes using the following command syntax:

```
Grid_home\bin\cluvfy stage -pre dbcfg -n node_list -d Oracle_home [-verbose]
```

In the preceding example, the variable `Grid_home` is the Grid home, the variable `node_list` is the list of nodes in your cluster, separated by commas, and the variable `Oracle_home` is the path for the Oracle home directory where OUI creates or modifies the database.

For example, to verify that your system is prepared for an Oracle Database with Oracle RAC installation on a two-node cluster with nodes `node1` and `node2`, with the Grid home path `C:\app\11.2.0\grid`, and with the Oracle home path `C:\app\oracle\product\11.2.0\dbhome_1`, enter the following command:

```
C:\app\11.2.0\grid\bin> cluvfy stage -pre dbcfg -n node1,node2 \
-d C:\app\oracle\product\11.2.0\dbhome_1
```

You can select the option `-verbose` to receive progress updates as CVU performs its system checks, and detailed reporting of the test results.

If the CVU summary indicates that the cluster verification fails, then review and correct the relevant system configuration steps, and run the test again.

The command `cluvfy stage -pre dbcfg` verifies the following:

- Node Reachability: All the specified nodes are reachable from the local node.
- User Equivalence: User equivalence exists on all the specified nodes.
- Total Memory: Each node specified has at least the minimum required memory configured.
- Available Memory: Each node specified has at least the minimum amount of available memory.
- Swap Space: Each node has enough swap space available.
- Free Disk Space: Each node has sufficient free disk space available in the path for the Oracle home, the Grid home, and the temporary directory.
- System Architecture: Each node must be a x64 (64-bit) system.
- Length of the Value of the Environment Variable `PATH`: The `PATH` environment variable is set on each node and does not contain more than 1023 characters.
- Oracle Clusterware Integrity: All the components of Oracle Clusterware are fully operational.
- Node Application Existence: All the specified nodes have the following node resources registered with Oracle Clusterware and whether the node resources are online:
	- virtual IP (VIP)
		- Oracle Notification Services (ONS) (not required)
		- Global Services Daemon (GSD) (not required)
		- EONS (not required)
		- NETWORK (not required)
- Time Zone Consistency: All the specified nodes have the same time zone setting.

## 3.5 Creating an Oracle RAC Database with DBCA

To create an Oracle RAC database with DBCA without Oracle ASM or a cluster file system, you must have configured shared storage devices. In addition, you must have run NETCA to configure your Oracle Net `listener.ora` file.

This section contains the following topics:

- Configuring Disks for Use With Oracle ASM
- Starting DBCA
- Using DBCA to Create an Oracle RAC Database

### 3.5.1 Configuring Disks for Use With Oracle ASM

On Windows-based systems, if you plan to use Oracle ASM storage, then before you use DBCA to create a database, you must first create logical partitions without primary partitions on the disk drives. After creating the logical disk partitions you must delete the drive letters for these partitions on all nodes. Alternatively, you can stamp these partitions with `asmtool`. See [Oracle Grid Infrastructure Installation Guide for Microsoft Windows x64 (64-Bit)](https://docs.oracle.com/cd/E11882_01/install.112/e48194/toc.htm) for more information on configuring disk devices for use with Oracle ASM. After you have configured the disks to be used by Oracle ASM, you must create the disk groups that will be used by the database prior to starting DBCA. You can create disk groups by using SQL\*Plus, Oracle Enterprise Manager, or Oracle ASM Configuration Assistant (ASMCA).

When using ASMCA to create a disk group, if you do not see the storage devices to add, then click Change Disk Discovery Path to alter the search path used by ASMCA to find available storage devices, or click Stamp Disks to start the `asmtoolg` GUI tool. You can select storage devices with a status of `Candidate` (the storage device was never used in an Oracle ASM disk group) or `Former` (the storage device is no longer in a disk group). To add storage devices that still have Oracle ASM disk headers, but the disk group is no longer in use (a case that can occur if you are selecting storage devices after a terminated installation attempt, you attempted deinstallation without dropping the disk group, or other configuration problems), use the `Force` command.

See Also:

- [Oracle Database Installation Guide for Microsoft Windows](https://docs.oracle.com/cd/E11882_01/install.112/e47798/toc.htm) for more information about `asmtoolg`
- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmdiskgrps.htm#OSTMG10206) for more information about creating disk groups

### 3.5.2 Starting DBCA

To start DBCA, connect as the user with Administrator privileges that was used to install the Oracle RAC software (for example, `oracle`) on one of your nodes in your cluster, and enter the command `dbca` from the `Oracle_home` `\bin` directory.

On Windows-based platforms, you can also click Start, and select Programs, Oracle - Oracle\_home name, Configuration and Migration Tools, and then Database Configuration Assistant.

Note:

To run DBCA, you no longer need to set operating system environment variables `%ORACLE_HOME%` to the Oracle RAC database home, or `%ORACLE_UNQNAME%` to the database unique name.

### 3.5.3 Using DBCA to Create an Oracle RAC Database

When you start DBCA, the first page that is displayed is the Welcome page for Oracle RAC, which includes the option to select an Oracle RAC database. DBCA displays this Oracle RAC Welcome page only if the Oracle home from which it is started is installed on a cluster. Enter information as prompted by DBCA. Click Help if you need assistance.

If DBCA does not display the Welcome page for Oracle RAC, then DBCA was unable to detect if the Oracle home is installed on a cluster. In this case, verify that the OUI inventory is correctly located in the directory `C:\Program Files\Oracle\Inventory\oraInst.loc`, and that the inventory files are not corrupted. Also, perform clusterware diagnostics by using the following CVU command syntax, where `C:\app\11.2.0\grid` is the location of your Grid home:

```
C:\app\11.2.0\grid\bin\cluvfy stage -post crsinst -n nodelist
```

For example, if your cluster consists of nodes `node1` and `node2`, run the following command:

```
C:\app\11.2.0\grid\bin\cluvfy stage -post crsinst -n node1,node2
```

Note the following important information when using DBCA:

- If nodes that are part of your cluster installation do not appear on the Node Selection page, then run the `lsinventory` command of OPatch to perform inventory diagnostics and run CVU to perform clusterware diagnostics.
- In Oracle RAC environments, the database name (DB\_UNIQUE\_NAME) portion is a string of no more than 30 characters that can contain alphanumeric, underscore (\_), dollar ($), and pound (#) characters, but must begin with an alphabetic character. No other special characters are permitted in a database name. The DB\_NAME parameter for a database is set to the first 8 characters of the database name.
- The domain portion of the global database name (DB\_DOMAIN) can be no more than 128 characters. Domain names using underscores (\_) are not allowed. The values for DB\_UNIQUE\_NAME.DB\_DOMAIN in its entirety must be unique within the enterprise.
- A system identifier (SID) is used as an unique identifier for each Oracle instance. The SID prefix, or first 8 characters of the database name, can contain only the characters a-z, A-Z, and 0-9. The SID prefix cannot contain operating system special characters, so if you use special characters in the first 8 characters of the database name, then these special characters are omitted in the SID prefix. There is a single SID prefix for every database. The SID prefix for a database must be unique within the cluster.On some platforms, the SID is case-sensitive.
	For an Oracle RAC database, each instance has a unique identifier, `ORACLE_SID`, which consists of the SID prefix and an instance number. The `ORACLE_SID` for Oracle RAC database instances is generated differently, depending on how you choose to manage the database. If you select a policy-managed database, then Oracle generates the SID in the format `name` \_ `#`, where `name` is the first eight alphanumeric characters of DB\_UNIQUE\_NAME, and `#` is the instance number. If you select an admin-managed database, then DBCA generates the SID for the instance names in advance, and the SID is in the format `name` `#`.
	Note:
	It is common practice to set the SID to be equal to the database name. For more information, see the discussion of the `DB_NAME` initialization parameter in [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams064.htm#REFRN10041).
- On the Management Options page, you are provided with selections for Oracle Enterprise Manager monitoring and management interfaces.
	Enterprise Manager Database Control is always an option. If DBCA discovers Grid Control agents on the cluster, then it also provides you with the option Enterprise Manager with the Grid Control. Choose between Database Control and Grid Control interfaces.
	You can enable daily backup operations. For daily backups, you enter the backup time and operating system credentials for the user that performs backup operations.
	You can no longer set up e-mail notification either from DBCA or OUI starting with Oracle Database 11g Release 2 (11.2.0.2).
- To use a Fast Recovery Area, Oracle recommends that you create at least two separate Oracle ASM disk groups on shared storage: one for the database area and one for the recovery area. Oracle recommends that you place the database area and the recovery area in separate failure groups.
	A failure group is defined by shared hardware, such as a controller shared between two storage devices, or two disks that are on the same spindle. If two storage devices share hardware that could fail, making both storage devices unavailable, then these storage devices are said to be in the same failure group.
	If you do not use Oracle ASM, then Oracle recommends that the data files and the Fast Recovery Area are located outside of the Oracle home and in separate locations, as with separate Oracle ASM failure groups, so that a hardware failure does not affect availability.
	See Also:
	- [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/toc.htm) for more information about using a Fast Recovery Area
	- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/toc.htm) for information about failure groups and best practices for high availability and recovery
- On the Recovery Configuration page, if you are using Oracle ASM or cluster file system storage, then you can also select the Fast Recovery Area and the size of the recovery area on the Recovery Configuration page. If you are using Oracle ASM, then the Fast Recovery Area defaults to an Oracle ASM disk group. If you are using OCFS for Windows, then the Fast Recovery Area defaults to `Oracle_base` `\fast_recovery_area`.
- If you intend to add more nodes to your cluster than you have during the current DBCA session, then click All Initialization Parameters, and change the parameter `CLUSTER_DATABASE_INSTANCES` to the total number of nodes that you plan to add to the cluster.
	In addition, if you click All Initialization Parameters, note that if your global database name is longer than 8 characters, then the database name value (in the `DB_NAME` parameter) is truncated to the first 8 characters, and the `DB_UNIQUE_NAME` parameter value is set to the global name.
	See Also:
	[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for information about initialization parameters
- When you are prompted to create the Database Vault user accounts, do not use the names of Database Vault roles, such as DV\_OWNER and DVACCTMGR. See [Oracle Database Vault Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23090/db_objects.htm#DVADM70328) for a full list of roles.

After you respond to DBCA prompts, review the Summary dialog information and then click OK. DBCA does the following:

- Starts the Oracle services if you are on a Windows-based platform
- Configures the network for the cluster database
- Migrates Oracle Database listeners from a previous release and related files to the Oracle Database 11g Oracle home
- Creates an Oracle RAC database and its instances
- Creates the Oracle RAC data dictionary views
- Configures Oracle Enterprise Manager Database Control or Grid Control
- Starts the listeners and database instances, and then starts the high availability services

Caution:

After you have created the database, if you decide to install additional Oracle Database products in the database you have created, then you must stop all processes running in the Oracle home before you attempt to install the additional products. See [Appendix E, "How to Stop Processes in an Existing Oracle Real Application Clusters Database"](procstop.md) for additional information.

## 3.6 Deleting an Oracle RAC Database with DBCA

Deleting an Oracle RAC database using DBCA involves first deleting the database, and then removing the database's initialization parameter files, instances, Optimal Flexible Architecture (OFA) structure, and the Oracle network configuration for the database. However, this process does not remove data files if you placed the files on raw devices or on raw partitions.

To delete a database using DBCA:

1. Start DBCA on one of your cluster nodes:
	On Windows-based platforms, click Start, and select Programs, Oracle - Oracle\_home name, Configuration and Migration Tools, and then Database Configuration Assistant.
	The DBCA Welcome page appears.
2. Select Oracle Real Application Clusters database, then click Next.
	After you click Next, DBCA displays the Operations page.
3. Select Delete a database, and click Next.
	DBCA displays the List of Cluster Databases page.
4. If your user ID and password are not operating-system authenticated, then the List of Cluster Databases page displays the user name and password fields. If these fields appear, then enter a user ID and password for a user account that has SYSDBA privileges.
5. Select the database to delete, and click Finish.
	After you click Finish, DBCA displays a dialog box to confirm the database and instances that DBCA is going to delete.
6. Click OK to begin the deletion of the database and its associated files, services, and environment settings, or click Cancel to stop the operation.

When you click OK, DBCA continues the operation and deletes all the associated instances for this database. DBCA also removes the parameter files and password files.

At this point, you have accomplished the following:

- Deleted the selected database from the cluster
- Deleted the Oracle services for the selected database
- Deleted high availability services that were assigned to the database
- Deleted the Oracle Net configuration for the database
- Deconfigured Database Control for that database
- Deleted the OFA directory structure for that database from the cluster
- Deleted the data files if the data files were not on raw devices or raw partitions

## 3.7 Setting Environment Variables for Enterprise Manager DB Control

In previous releases of Oracle Database, you were required to set the environment variables `ORACLE_HOME` and `ORACLE_SID` to start, stop, and check the status of Enterprise Manager. With Oracle Database 11g release 2 (11.2) and later, you need to set the environment variables `ORACLE_HOME` and `ORACLE_UNQNAME` to use Enterprise Manager. For example, on each node, enter commands similar to the following to set these values for the `oracle` user, where the Oracle home is `C:\app\oracle\product\11.2.0.1\dbhome_1`, and where the database unique name is `sales`:

```
C:\> set ORACLE_HOME=C:\app\oracle\product\11.2.0.1\dbhome_1
C:\> set ORACLE_UNQNAME=sales
```

Place these environment variables in the `oracle` user profile file on each cluster member node to ensure that the environment variable settings are available after system restarts.