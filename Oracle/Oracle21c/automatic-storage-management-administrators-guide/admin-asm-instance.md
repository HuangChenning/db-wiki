---
title: "Administrator's Guide"
book: "Automatic Storage Management Administrator's Guide"
doc_id: F30296-05
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/ostmg/admin-asm-instance.html
tags:
  - oracle
  - 21c
  - automatic-storage-management-administrators-guide
---

Oracle ASM is typically installed in an Oracle Grid Infrastructure home separate from the Oracle Database home. Only one Oracle ASM instance is supported on a server in a standard configuration; however, Oracle Flex ASM provides additional configuration options.

When managing an Oracle ASM instance, the administration activity should be performed in the Oracle Grid Infrastructure home.

This section describes how to administer Oracle ASM instances under the following topics:

See Also:

- [Managing Oracle Flex ASM](manage-flex-asm.md) for information about Oracle Flex ASM
- [Creating Database Files in Oracle ASM Using SQL\*Plus](create-db-asm-sqlplus.md) for information about Oracle ASM and creating database files

### Using Oracle Grid Infrastructure for a Standalone Server

Oracle Grid Infrastructure for a standalone server (Oracle Restart) improves the availability of your Oracle Database.

When you install the Oracle Grid Infrastructure for a standalone server, it includes both Oracle ASM and Oracle Restart. Oracle Grid Infrastructure for a standalone server (Oracle Restart) runs out of the Oracle Grid Infrastructure home, which you install separately from Oracle Database homes.

Oracle Restart provides managed startup and restart of a single-instance (non-clustered) Oracle Database, Oracle ASM instance, service, listener, and any other process running on the server. If an interruption of a service occurs after a hardware or software failure, Oracle Restart automatically takes the necessary steps to restart the component.

With Server Control Utility (SRVCTL) you can add a component, such as an Oracle ASM instance, to Oracle Restart. You then enable Oracle Restart protection for the Oracle ASM instance. With SRVCTL, you also remove or disable Oracle Restart protection.

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ADMIN12708) for information about configuring and administering Oracle Restart
- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=RACAD826) for information about automatically restarting single-instance databases residing on an Oracle RAC node
- [Oracle Grid Infrastructure Installation and Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=CWGEN) for information about installation of Oracle Grid Infrastructure

### About Starting Up an Oracle ASM Instance

This section describes how to start Oracle ASM instances under the following topics:

- Connecting To and Starting Up an Oracle ASM Instance
- Starting Up an Oracle ASM instance with an Incorrect SPFILE Path
- About Mounting Disk Groups at Startup
- About Restricted Mode

#### Connecting To and Starting Up an Oracle ASM Instance

You start an Oracle ASM instance similarly to the way in which you start an Oracle Database instance with some minor differences.

When starting an Oracle ASM instance with SQL\*Plus, note the following:

- To connect to a local Oracle ASM instance with SQL\*Plus, set the `ORACLE_SID` environment variable to the Oracle ASM system identifier (SID).
	The default Oracle ASM SID for a single-instance database is `+ASM`, and the default SID for Oracle ASM for an Oracle RAC node is `+ASM` `node_number` where `node_number` is the number of the node. The `ORACLE_HOME` environment variable must be set to the Grid Infrastructure home where Oracle ASM was installed.
	Note:
	Oracle recommends that you do not change the default Oracle ASM SID name.
- The initialization parameter file must contain the following entry:
	`INSTANCE_TYPE = ASM`
	This parameter indicates that an Oracle ASM instance, not a database instance, is starting.
- When you run the `STARTUP` command, rather than trying to mount and open a database, this command attempts to mount Oracle ASM disk groups.
	After the Oracle ASM instance has started, you can mount disk groups with the `ALTER DISKGROUP...MOUNT` command.
- The associated Oracle Database instance does not have to be running when you start the associated Oracle ASM instance.

The following list describes how Oracle ASM interprets SQL\*Plus `STARTUP` command parameters.

- `FORCE` Parameter
	Issues a `SHUTDOWN ABORT` to the Oracle ASM instance before restarting it.
	If an Oracle Advanced Cluster File System (Oracle ACFS) file system is currently mounted on Oracle ADVM volumes, the file system should first be dismounted. Otherwise, applications encounter I/O errors and Oracle ACFS user data and metadata may not be written to storage before the Oracle ASM storage is fenced.
- `MOUNT` or `OPEN` Parameter
	Mounts the disk groups specified in the `ASM_DISKGROUPS` initialization parameter. This is the default if no command parameter is specified.
- `NOMOUNT` Parameter
	Starts up the Oracle ASM instance without mounting any disk groups.
- `RESTRICT` Parameter
	Starts up an instance in restricted mode that enables access only to users with both the `CREATE` `SESSION` and `RESTRICTED` `SESSION` system privileges. You can use the `RESTRICT` clause in combination with the `MOUNT`, `NOMOUNT`, and `OPEN` clauses.
	In restricted mode, database instances cannot use the disk groups. In other words, databases cannot open files that are in that disk group. Also, the disk group cannot be mounted by any other instance in the cluster. Mounting the disk group in restricted mode enables only one Oracle ASM instance to mount the disk group. This mode is useful to mount the disk group for repairing configuration issues.

The following is a sample SQL\*Plus session for starting an Oracle ASM instance.

```
SQLPLUS /NOLOG
SQL> CONNECT SYS AS SYSASM
Enter password: sys_password
Connected to an idle instance.

SQL> STARTUP
ASM instance started

Total System Global Area   71303168 bytes
Fixed Size                 1069292 bytes
Variable Size              45068052 bytes
ASM Cache                  25165824 bytes
ASM disk groups mounted
```

See Also:

- [Authentication for Accessing Oracle ASM Instances](authenticate-access-asm-instance.md) for more information about user authentication
- [startup](asmcmd-instance-commands.md) for information about starting an Oracle ASM instance with ASMCMD `startup` command
- About Restricted Mode for information about restricted mode
- About Mounting Disk Groups at Startup for information about disk groups that are mounted at startup time
- [Mounting and Dismounting Disk Groups](maintain-diskgroups.md) for information about mounting disk groups
- [Oracle Automatic Storage Management Cluster File System Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ACFSG-GUID-824B567D-A538-4EF2-8A2D-96D83A1E6284) for information about dismounting an Oracle ACFS file system
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ADMIN-GUID-7842AF72-DA25-4559-A8E7-9883D0C63BF2) for more information about using environment variables to select instances
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ADMIN-GUID-045DE684-6680-4099-A49E-2F5B5FA59670) for more information about starting up and shutting down Oracle instances
- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=RACAD-GUID-2D617A25-0E8E-4B3E-95AA-8AD26DA12DF2) for information about starting an Oracle ASM instance with `SRVCTL` in Oracle RAC
- [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=CWADD-GUID-58F85575-7D88-4D45-B097-6274FBBBB646) for information about Oracle Clusterware Cluster subcomponent processes and background processes
- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=CNCPT-GUID-D8AE1B78-69D5-4F0F-8BE3-C91AA2514F2D) for information about Oracle Database background processes
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=REFRN-GUID-86184690-5531-405F-AA05-BB935F57B76D) for a description of the Oracle background processes

#### Starting Up an Oracle ASM instance with an Incorrect SPFILE Path

If the SPFILE path in the GPnP profile is incorrect, you can start the Oracle ASM instance as follows:

1. Create a PFILE with one line in it that identifies the path to the SPFILE.
	For example:
	Create the `/oracle/dbs/spfileasm_init.ora` file that contains:
	`SPFILE='+DATA/asm/asmparameterfile/asmspfile.ora'`
2. Start up the instance using the initialization parameter file.
	For example:
	`SQL>` `STARTUP` `PFILE=/oracle/dbs/spfileasm_init.ora`
3. After the instance is running, use the ASMCMD `spset` command to update the SPFILE path in the GPnP profile. See [spset](asmcmd-instance-commands.md).
	For example:
	`ASMCMD>` `spset` `+DATA/asm/asmparameterfile/asmspfile.ora`

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ADMIN12828) for more information about using `STARTUP` with a nondefault server parameter file

#### About Mounting Disk Groups at Startup

At startup, the Oracle ASM instance attempts to mount the following disk groups:

- Disk groups specified in the `ASM_DISKGROUPS` initialization parameter
- Disk group used by Cluster Synchronization Services (CSS) for voting files
- Disk groups used by Oracle Clusterware for Oracle Cluster Registry (OCR)
- Disk group used by the Oracle ASM instance to store the ASM server parameter file (SPFILE)

If no disk groups are found in the previous list, then the Oracle ASM instance does not mount any disk groups at startup. After the Oracle ASM instance has started, you can mount disk groups with the `ALTER DISKGROUP...MOUNT` command. For more information, see [Mounting and Dismounting Disk Groups](maintain-diskgroups.md).

#### About Restricted Mode

You can use the `STARTUP` `RESTRICT` command to control access to an Oracle ASM instance while you perform maintenance. When an Oracle ASM instance is active in this mode, all of the disk groups that are defined in the `ASM_DISKGROUPS` parameter are mounted in `RESTRICTED` mode. This prevents databases from connecting to the Oracle ASM instance. In addition, the restricted clause of the `ALTER` `SYSTEM` statement is disabled for the Oracle ASM instance. The `ALTER` `DISKGROUP` `diskgroup` `MOUNT` statement is extended to enable Oracle ASM to mount a disk group in restricted mode.

When you mount a disk group in `RESTRICTED` mode, the disk group can only be mounted by one instance. Clients of Oracle ASM on that node cannot access that disk group while the disk group is mounted in `RESTRICTED` mode. The `RESTRICTED` mode enables you to perform maintenance tasks on a disk group in the Oracle ASM instance without interference from clients.

Rebalance operations that occur while a disk group is in `RESTRICTED` mode eliminate the lock and unlock extent map messaging that occurs between Oracle ASM instances in an Oracle RAC environment. This improves the overall rebalance throughput. At the end of a maintenance period, you must explicitly dismount the disk group and remount it in normal mode.

### About Shutting Down an Oracle ASM Instance

You can initiate the Oracle ASM shutdown process by running the `SHUTDOWN` command in SQL\*Plus.

Before you run this command, ensure that the `ORACLE_SID` environment variable is set to the Oracle ASM SID so that you can connect to the local Oracle ASM instance. The default Oracle ASM SID for a single-instance database is `+ASM`, and the default SID for Oracle ASM for an Oracle RAC node is `+ASM` `node_number` where `node_number` is the number of the node. The `ORACLE_HOME` environment variable must be set to the Grid Infrastructure home where Oracle ASM was installed.

If you are not using Oracle Flex ASM, Oracle strongly recommends that you shut down all database instances that use the Oracle ASM instance and dismount all file systems mounted on Oracle ASM Dynamic Volume Manager (Oracle ADVM) volumes before attempting to shut down the Oracle ASM instance. If you are using Oracle Flex ASM, Oracle Flex ASM clients move to other running Oracle ASM instances if an Oracle ASM instance is shut down.

If Oracle Cluster Registry (OCR) or voting files are stored in a disk group, the disk group can only be dismounted by shutting down the Oracle ASM instance as part of shutting down the clusterware on a node. To shut down the clusterware, run `crsctl` `stop` `crs`.

To shut down an Oracle ASM instance, perform the following steps:

```
SQLPLUS /NOLOG
SQL> CONNECT SYS AS SYSASM
Enter password: sys_password
Connected.
SQL> SHUTDOWN NORMAL
```

The following list describes the `SHUTDOWN` modes and the behavior of the Oracle ASM instance in each mode.

- `NORMAL` Clause
	Oracle ASM waits for any in-progress SQL to complete before performing an orderly dismount of all of the disk groups and shutting down the Oracle ASM instance. Before the instance is shut down, Oracle ASM waits for all of the currently connected users to disconnect from the instance. If any database instances are connected to the Oracle ASM instance, then the `SHUTDOWN` command returns an error and leaves the Oracle ASM instance running. `NORMAL` is the default shutdown mode.
- `IMMEDIATE` or `TRANSACTIONAL` Clause
	Oracle ASM waits for any in-progress SQL to complete before performing an orderly dismount of all of the disk groups and shutting down the Oracle ASM instance. Oracle ASM does not wait for users currently connected to the instance to disconnect. If any database instances are connected to the Oracle ASM instance, then the `SHUTDOWN` command returns an error and leaves the Oracle ASM instance running. Because the Oracle ASM instance does not contain any transactions, the `TRANSACTIONAL` mode behaves the same as `IMMEDIATE` mode.
- `ABORT` Clause
	The Oracle ASM instance immediately shuts down without the orderly dismount of disk groups. This causes recovery to occur upon the next Oracle ASM startup.
	If any database instance is connected to the Oracle ASM instance, then the database instance stops.
	If any Oracle Advanced Cluster File System (Oracle ACFS) file systems are currently mounted on Oracle ADVM volumes, those file systems should first be dismounted. Otherwise, applications encounter I/O errors and Oracle ACFS user data and metadata may not be written to storage before the Oracle ASM storage is fenced.

See Also:

- [Authentication for Accessing Oracle ASM Instances](authenticate-access-asm-instance.md) for more information about user authentication
- [Authentication for Accessing Oracle ASM Instances](authenticate-access-asm-instance.md) for more information about user authentication on Oracle ASM instance
- [Oracle Automatic Storage Management Cluster File System Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ACFSG-GUID-824B567D-A538-4EF2-8A2D-96D83A1E6284) for information about dismounting an Oracle ACFS file system
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ADMIN-GUID-7842AF72-DA25-4559-A8E7-9883D0C63BF2) for more information about using environment variables to select instances
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ADMIN-GUID-045DE684-6680-4099-A49E-2F5B5FA59670) for more information about starting up and shutting down Oracle instances
- [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=CWADD-GUID-20101C89-B87C-49C9-BA63-634376EDB62E) for information about managing voting files, Oracle Cluster Registry (OCR), and Oracle Local Registry (OLR)

### About Administering Oracle ASM Instances with Server Control Utility

In addition to the Oracle ASM administration procedures that this section describes, you can use Server Control Utility (SRVCTL) in clustered Oracle ASM environments to perform the following Oracle ASM administration tasks:

- Add and remove the Oracle ASM Oracle Clusterware (CRS) resource in Oracle Cluster Registry (OCR)
- Enable, disable, start, and stop Oracle ASM instances
- Display the Oracle ASM instance configuration and status
- Add, modify, and remove Oracle ASM network resources
- Add, modify, remove, enable, disable, start, and stop Oracle ASM listener resources

See Also:

[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=CWADD-GUID-1DCA9E3F-B929-4555-B673-921FF3588AC3) and [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=RACAD826) for information about SRVCTL commands

### About Out of Place Upgrades

With an out-of-place upgrade, the installer installs the newer version of Oracle Grid Infrastructure in a separate Oracle Grid Infrastructure home.

An in-place upgrade of Oracle Grid Infrastructure 11g Release 2 (11.2) is not supported. For example, an upgrade of Oracle Grid Infrastructure 11g Release 2 (11.2.0.1) to Oracle Grid Infrastructure 11g Release 2 (11.2.0.2) must be an out of place upgrade.

See Also:

[Oracle Grid Infrastructure Installation and Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=CWGEN) for information about installing Oracle Grid Infrastructure, out of place upgrades, and performing rolling upgrades of Oracle Grid Infrastructure and Oracle ASM

### About Configuring Oracle Grid Infrastructure with the Configuration Wizard

The Oracle Grid Infrastructure configuration wizard can update the configuration of an Oracle Grid Infrastructure environment after the software has been installed. The configuration wizard accepts your input, validates the input, and populates the configuration data into the `CRSCONFIG_PARAMS` file. If additional scripts must be run, the configuration wizard directs you to run those scripts.

See Also:

[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=CWADD92094) for information about the Oracle Grid Infrastructure configuration wizard.

### About Active Session History Sampling for Oracle ASM

Active Session History sampling is now available on Oracle ASM instances. This activity is exposed in the dynamic `V$ACTIVE_SESSION_HISTORY` view. Active Session History sampling requires a diagnostic pack license for the Oracle ASM instance.

See Also:

- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=TGDBA145) for more information about gathering performance statistics
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=REFRN30299) for a description of the `V$ACTIVE_SESSION_HISTORY` view

### About Oracle Home User on Windows

Oracle Database supports the use of an Oracle home user, which can be specified at installation time. The Oracle home user is associated with an Oracle home and it cannot be changed after installation. Different Oracle homes on a system can share the same Oracle home user or use different Oracle home user names.

In previous releases on Windows operating systems, Oracle services were required to run as `Local` `System` privileges, which are fully privileged. This feature enables the database, listener, and job scheduler services to run with low and non-administrative user privileges to allow tighter control of security. The Oracle home user can be a built-in account or a Windows user account. A Windows user account should be a low privileged (non-Administrator) account to ensure that the Oracle home user has a limited set of privileges, ensuring that Oracle Database services have only those privileges required to run Oracle products. The Windows user account can be a Local User, a Domain User, or a Managed Services Account in general. However, Oracle RAC, Oracle Restart, and Oracle Grid Infrastructure installations require the use of the Domain User as the Oracle home user because a clusterwide identity is necessary.

See Also:

[Oracle Database Platform Guide for Microsoft Windows](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=NTQRF673) for information about running Oracle services on Windows platforms and different types of Windows user accounts