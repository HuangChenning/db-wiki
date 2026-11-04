---
title: "Oracle Automatic Storage Management Administrator's Guide"
book: "Oracle Automatic Storage Management Administrator's Guide"
doc_id: F34287-08
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/part-iv-advanced-topics/administering-oracle-asm-filter-driver.html
tags:
  - oracle
  - 19c
  - automatic-storage-management-administrators-guide
---

## Administering Oracle ASM Filter Driver

Oracle ASM Filter Driver (Oracle ASMFD) simplifies the configuration and management of disk devices by eliminating the need to rebind disk devices used with Oracle ASM each time the system is restarted.

Warning:

When configuring Oracle ASM, including Oracle ASMFD, do not manually modify or erase the contents of Oracle ASM disks or modify any files, including configuration files.

Note:

- The configuration for Oracle ASMFD can now be enabled with a check box to be an automated process during Oracle Grid Infrastructure installation.
- If ASMLIB is installed and configured for an existing Oracle ASM installation, then you must explicitly uninstall the existing ASMLIB configuration before installing and configuring Oracle ASMFD.
	See: [Deinstalling Oracle ASMLIB](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19&id=CWLIN-GUID-AAC3291D-BEAF-4567-A0A0-CA834C1A73EA)
- Oracle ASM Filter Driver (Oracle ASMFD) is available on Linux systems starting with Oracle Database 12\_c\_ Release 1 (12.1.0.2). Oracle ASMFD is available on Solaris systems starting with Oracle Database 12\_c\_ Release 2 (12.2.0.1).
- In the steps of the procedures described in the topics of this section, the `$ORACLE_HOME` environmental variable is set to the directory path of the Oracle Grid Infrastructure home. Commands that show `#` as the operating system prompt must be run as the root user. Commands that show `$` as the operating system prompt should be run as the owner of Oracle Grid Infrastructure home

See also

- [Oracle Database Installation Guide for Linux](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19&id=LADBI-GUID-0B1CEE8C-C893-46AA-8A6A-7B5FAAEC72B3) for information about installing and configuring Oracle ASMFD on Oracle Standalone Server
- My Oracle Support articles about Oracle ASMFD available at [My Oracle Support](https://support.oracle.com/) ([https://support.oracle.com](https://support.oracle.com/)) for additional information about Oracle ASMFD, such as supported operating system platforms (certification matrix) or configuration issues.
- [ASMCMD Oracle ASM Filter Driver Management Commands](managing-oracle-asm-with-asmcmd.md) for information about the ASMCMD commands for administering Oracle ASMFD
- [About ASMCMD](managing-oracle-asm-with-asmcmd.md) for information about all the ASMCMD commands
- [Managing Oracle ASM Filter Driver With Oracle Enterprise Manager](administering-oracle-asm-with-oracle-enterprise-manager.md) for information about using Oracle Enterprise Manager to administer Oracle ASMFD

## About Oracle ASM Filter Driver

Oracle ASM Filter Driver (Oracle ASMFD) is a kernel module that resides in the I/O path of the Oracle ASM disks. Oracle ASM uses the filter driver to validate write I/O requests to Oracle ASM disks.

Oracle ASMFD simplifies the configuration and management of disk devices by eliminating the need to rebind disk devices used with Oracle ASM each time the system is restarted.

Oracle ASM Filter Driver rejects any I/O requests that are invalid. This action eliminates accidental overwrites of Oracle ASM disks that would cause corruption in the disks and files within the disk group. For example, the Oracle ASM Filter Driver filters out all non-Oracle I/Os which could cause accidental overwrites.

### About Oracle ASMLIB and Oracle ASM Filter Driver

Starting with Oracle Grid Infrastructure 12\_c\_ Release 2 (12.2), Oracle ASM Filter Driver (Oracle ASMFD) cannot be installed and configured if Oracle ASMLIB has been installed on the system. If you want to install and configure Oracle ASMFD, you must first uninstall Oracle ASMLIB.

See also

[Oracle Grid Infrastructure Installation and Upgrade Guide for Linux](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/ostmg&id=CWLIN-GUID--B5D06658-1B1B-4922-8853-50670ABCDADB) for information about installing and configuring Oracle ASMFD on Oracle Grid Infrastructure, and deinstalling Oracle ASMLIB

### About Partition Tables and Oracle ASM Filter Driver

Extended partition tables are not supported with Oracle ASM filter driver (ASMFD) in Oracle Automatic Storage Management 12.2 Release 1 (12.2.0.1).

## Configuring Oracle ASM Filter Driver

You can configure Oracle ASM Filter Driver (Oracle ASMFD) for device persistence during the installation of Oracle Grid Infrastructure or after Oracle Grid Infrastructure has been installed.

Note:

- If ASMLIB is installed and configured for an existing Oracle ASM installation, then you must explicitly deinstall the existing ASMLIB configuration before installing and configuring Oracle ASMFD. Refer to [Oracle Grid Infrastructure Installation and Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/ostmg&id=CWGEN) for your operating system for information about deinstalling Oracle ASMLIB and the installation of Oracle Grid Infrastructure.
- If ASMLIB has been previously installed on the system, then you must set the Oracle ASM disk string to `''` (with ASMCMD `dsset ''`) before running ASMCMD `afd_configure` to configure Oracle ASMFD.
- For additional information about configuring Oracle ASM filter driver (ASMFD), refer to My Oracle Support articles about Oracle ASMFD available at [My Oracle Support](https://support.oracle.com/) ([https://support.oracle.com](https://support.oracle.com/)).

See also

[Oracle Grid Infrastructure Installation and Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/ostmg&id=CWGEN) for your operating system for information about installing and configuring Oracle Grid Infrastructure

### Configuring Oracle ASM Filter Driver During Installation

During the installation of Oracle Grid Infrastructure, you can optionally enable automated installation and configuration of Oracle ASM Filter Driver for your system with the **Configure** **ASM** **Filter** **Driver** check box on the **Create** **ASM** **Disk** **Group** wizard page. When you enable the **Configure** **ASM** **Filter** **Driver** box, an automated process for Oracle ASMFD is launched during Oracle Grid Infrastructure installation.

If you do not use `udev` on the system where the Oracle Grid Infrastructure is installed, then you can also complete the following procedure to provision disks for Oracle ASMFD before the installer is launched. This procedure must be performed after the Oracle Grid Infrastructure installation zip files have been unzipped in the Oracle Grid Infrastructure home, but before you enable the **Configure** **ASM** **Filter** **Driver** check box during the installation process when the setup script is run.

1. To configure shared disks for use with Oracle ASM Filter Driver, log in as the `root` user and set the environment variable `$ORACLE_HOME` to the location of the Grid home and the environment variable `$ORACLE_BASE` to a temporary location
	```
	su root
	# export ORACLE_HOME=/u01/app/oracle/21.0.0/grid
	# export ORACLE_BASE=/tmp
	```
	The `ORACLE_BASE` variable is set to a temporary location to avoid creating diagnostic or trace files in the Grid home before the Oracle Grid Infrastructure installation.
	Before running the commands in the following steps, ensure that you are in the `$ORACLE_HOME/bin` directory.
2. Add the `ORACLE_HOME/bin` directory to the `PATH` environment variable.
	```
	# export PATH=$ORACLE_HOME/bin:$PATH
	```
3. Use the ASMCMD `afd_label` command to provision disk devices for use with Oracle ASM Filter Driver as follows.
	```
	# asmcmd afd_label DATA1 /dev/disk1a --init
	```
4. Use the ASMCMD `afd_lslbl` command to verify the device has been marked for use with Oracle ASMFD.
	```
	# asmcmd afd_lslbl /dev/disk1a
	```
5. Unset the `ORACLE_BASE` variable when you have finished provisioning disks for Oracle ASMFD.
	```
	# unset ORACLE_BASE
	```
6. Run the setup installation script (`gridSetup.sh`) to install Oracle Grid Infrastructure and enable Oracle ASM Filter Driver configuration.
	On the **CreateASMDisk** **Group** wizard page during the installation process, check the **ConfigureASMFilter** **Driver** box to enable configuration of Oracle ASM Filter Driver and then add your provisioned disks to the initial disk group (typically named `DATA`).

For information about the ASMCMD commands for administering Oracle ASMFD, refer to [ASMCMD Oracle ASM Filter Driver Management Commands](managing-oracle-asm-with-asmcmd.md).

### Configuring Oracle ASM Filter Driver After Installation

If you did not enable configuration of Oracle ASM Filter Driver (ASMFD) during installation, you can manually configure your Oracle ASM devices to use Oracle ASMFD, as described in the following topics.

See also

- [My Oracle Support](https://support.oracle.com/) ([https://support.oracle.com](https://support.oracle.com/) for articles about configuring Oracle ASM filter driver (ASMFD)
- [*Oracle Clusterware Administration and Deployment Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19&id=CWADD-GUID-1A6774CF-FD5F-463E-817F-34E4466443C7) for information about using CRSCTL commands

#### Configuring Oracle ASM Filter Driver in an Oracle Grid Infrastructure Clusterware Environment

To configure Oracle ASMFD in an Oracle Clusterware environment after installation, perform the following steps.

1. As the Oracle Grid Infrastructure owner, update the Oracle ASM disk discovery string to enable Oracle ASMFD to discover devices in the future.
	First retrieve the current value of the Oracle ASM disk discovery string.
	```
	$ $ORACLE_HOME/bin/asmcmd dsget
	```
	The value of *disk\_string* in the above command is the current Oracle ASM disk discovery string value retrieved by `dsget`. If the disks are in the default location for the operating system environment and disk discovery string has not been set, then the disk discovery string is empty.
	Update the Oracle ASM disk discovery string. If the string is empty, update the value of the disk discovery string to include the default disk location.
	```
	disk_string
	```
2. As the Oracle Grid Infrastructure owner, list the nodes and node roles in your cluster.
	```
	$ $ORACLE_HOME/bin/olsnodes -a
	```
3. On each Hub and Leaf node, perform this step either in rolling or non-rolling mode.
	1. Log in as the `root` user and stop Oracle Grid Infrastructure.
		```
		# $ORACLE_HOME/bin/crsctl stop crs
		```
		If the command returns an error, then stop Oracle Grid Infrastructure forcibly.
		```
		# $ORACLE_HOME/bin/crsctl stop crs -f
		```
		2. As the `root` user, configure Oracle ASMFD to filter at the node level.
		```
		# $ORACLE_HOME/bin/asmcmd afd_configure
		```
		3. As the Oracle Grid Infrastructure owner, verify the status of Oracle ASMFD.
		```
		$ $ORACLE_HOME/bin/asmcmd afd_state
		ASMCMD-9526: The AFD state is 'LOADED' and filtering is 'ENABLED' on host 'myhost'
		```
		4. Label all the Oracle ASM disks with the Oracle ASMFD label.
		```
		# $ORACLE_HOME/bin/asmcmd afd_label 'label_name' 'device_path' --migrate
		```
		5. As the `root` user, start the Oracle Clusterware stack on the node.
		```
		# $ORACLE_HOME/bin/crsctl start crs
		```
		6. As the Oracle Grid Infrastructure owner, set the Oracle ASMFD discovery disk string to the updated Oracle ASM disk discovery string value from Step 1.
		```
		disk_string
		```

With the Oracle ASMFD discovery disk string properly set, Oracle ASM Filter Driver should identify and start managing disks, including those previously managed by Oracle ASMLIB.

See also

- Updating the Oracle ASM ASM\_DISKSTRING Parameter for Oracle ASM Filter Driver Disks for information about updating the Oracle ASM discovery string
- Determining Whether Oracle ASM Filter Driver Has Been Configured for information about checking on the state of the Oracle ASM Filter Driver
- Updating the Oracle ASM Filter Driver AFD\_DISKSTRING Parameter for information about updating the Oracle ASM Filter Driver discovery disk discovery string

#### Configuring Oracle ASM in an Oracle Grid Infrastructure Standalone Environment

To configure Oracle ASM filter driver (ASMFD) in a standalone (Oracle Restart) environment, perform the following steps.

1. As the Oracle Grid Infrastructure standalone server owner, update the Oracle ASM disk discovery string to enable Oracle ASMFD to discover disk devices in the future.
	First check the current value of the Oracle ASM disk discovery string, then update the value.
	```
	disk_string
	```
	The value of *disk\_string* in the above command is the disk discovery string value retrieved by `dsget`.
2. Log in as the `root` user and stop Oracle Grid Infrastructure for a standalone server using the following command:
	```
	# $ORACLE_HOME/bin/crsctl stop has -f
	```
3. As the `root` user, configure Oracle ASMFD.
	```
	# $ORACLE_HOME/bin/asmcmd afd_configure
	```
	This command configures Oracle ASMFD and deconfigures Oracle ASMLIB, if it exists.
4. As the Oracle Grid Infrastructure standalone server owner, verify the Oracle ASMFD status.
	```
	$ $ORACLE_HOME/bin/asmcmd afd_state
	ASMCMD-9526: The AFD state is 'LOADED' and filtering is 'ENABLED' on host 'myhost'
	```
5. As the `root` user, start Oracle Grid Infrastructure for a standalone server.
	```
	# $ORACLE_HOME/bin/crsctl start has
	```
6. As the Oracle Grid Infrastructure standalone server owner, set the Oracle ASMFD disk discovery string to the value of the updated Oracle ASM disk discovery string from Step 1.
	```
	disk_string
	```

Oracle ASM Filter Driver should identify and start managing disks previously managed by Oracle ASMLIB.

See also

- Updating the Oracle ASM ASM\_DISKSTRING Parameter for Oracle ASM Filter Driver Disks for information about updating the Oracle ASM discovery string
- Determining Whether Oracle ASM Filter Driver Has Been Configured for information about checking on the state of the Oracle ASM Filter Driver

## About Migrating to Oracle ASM Filter Driver From an ASMLIB Environment

If ASMLIB is installed and configured for an existing Oracle ASM installation, then you must explicitly uninstall the existing ASMLIB configuration before installing and configuring Oracle ASMFD.

Oracle recommends that you temporarily move Oracle Cluster Registry (OCR) and voting files to another disk group if one is available, as described in Migrating Oracle ASM Disk Groups without Oracle Cluster Registry or Voting Files, and migrate the disk group to use Oracle ASMFD. After migrating the disk group to use Oracle ASMFD, move OCR and voting files back to the disk group. You can similarly migrate any other disk groups if they contain OCR or voting files to ensure online migration of all disk groups to Oracle ASMFD.

See also

- [*Oracle Clusterware Administration and Deployment Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19&id=CWADD-GUID-70E524E1-0FAD-4962-9B9F-0691EAEE7A9F) for information about replacing Oracle Cluster Registry locations and migrating voting files
- [*Oracle Clusterware Administration and Deployment Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19&id=CWADD-GUID-1A6774CF-FD5F-463E-817F-34E4466443C7) for information about using CRSCTL commands
- [*Oracle Clusterware Administration and Deployment Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19&id=CWADD-GUID-70E524E1-0FAD-4962-9B9F-0691EAEE7A9F) for information about managing voting files, Oracle Cluster Registry (OCR), and Oracle Local Registry (OLR)
- [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19&id=CWADD-GUID-1DCA9E3F-B929-4555-B673-921FF3588AC3) and [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19&id=RACAD-GUID-3ED4DBCE-A148-462B-8A79-534A3F0D6E7D) for information about SRVCTL commands

### Migrating Oracle ASM Disk Groups without Oracle Cluster Registry or Voting Files

To migrate Oracle ASM disk groups without Oracle Cluster Registry (OCR) or voting files to Oracle ASMFD:

1. Log in as the Oracle Grid Infrastructure owner on any node to run the commands in this procedure.
2. List the existing disk groups:
	```
	$ $ORACLE_HOME/bin/asmcmd lsdg
	```
3. List the associated disks:
	```
	diskgroup
	```
4. Check if Oracle ASM is active:
	```
	$ $ORACLE_HOME/bin/srvctl status asm
	```
5. Stop the databases and dismount the disk group on all nodes:
	```
	diskgroup
	```
6. Label all existing disks in the disk group by running the following command for each disk on a Hub node:
	```
	disk_path
	```
7. Scan the disks on all Hub nodes:
	```
	$ $ORACLE_HOME/bin/asmcmd afd_scan
	```
8. Start the databases and mount the disk group on all nodes:
	```
	diskgroup
	```

### Migrating Oracle ASM Disk Groups with Oracle Cluster Registry or Voting Files

To migrate Oracle ASM disk groups with Oracle Cluster Registry (OCR) or voting files to Oracle ASM Filter Driver (Oracle ASMFD):

1. Log in as the `root` user and list the disk groups with OCR and voting files by running the following commands on one node:
	```
	# $ORACLE_HOME/bin/ocrcheck -config
	# $ORACLE_HOME/bin/crsctl query css votedisk
	```
2. As the Oracle Grid Infrastructure owner list the disks associated with the disk groups:
	```
	$ $ORACLE_HOME/bin/asmcmd lsdsk -G disk_group
	```
3. As `root`, stop the databases and Oracle Clusterware on all nodes:
	```
	# $ORACLE_HOME/bin/crsctl stop cluster -all
	```
4. As the Oracle Grid Infrastructure owner label all existing disks in the disk group by running the following command for each disk on a Hub node:
	```
	$ $ORACLE_HOME/bin/asmcmd afd_label labeldisk_path --migrate
	```
5. As the Oracle Grid Infrastructure owner rescan the disks on all Hub nodes by running the following command on all of the Hub nodes:
	```
	$ $ORACLE_HOME/bin/asmcmd afd_scan
	```
6. As `root`, start the Oracle Clusterware stack on all nodes and mount the OCR and voting files disk groups and databases:
	```
	# $ORACLE_HOME/bin/crsctl start cluster -all
	```

### Migrating Oracle ASM Disk Groups in an Oracle Grid Infrastructure Standalone Environment

To migrate your existing Oracle ASM disk groups to Oracle ASM Filter Driver in an Oracle Grid Infrastructure standalone (Oracle Restart) environment, perform the following steps:

1. Log in as the Oracle Grid Infrastructure standalone server owner to run the steps in this procedure.
2. List the existing disk groups:
	```
	$ $ORACLE_HOME/bin/asmcmd lsdg
	```
3. List the existing disks:
	```
	diskgroup_name
	```
4. Check if the status of your Oracle ASM instance is active:
	```
	$ $ORACLE_HOME/bin/srvctl status asm
	```
5. Stop all the databases and dismount all disk groups. For each database, run the following commands:
	```
	db_unique_name
	```
6. Label all existing disks in the disk group by running the following command for each disk:
	```
	label
	```
	Reload AFD if Disk Multipathing is being used.
7. Rescan the disks:
	```
	$ $ORACLE_HOME/bin/asmcmd afd_scan
	```
8. Start the database and mount the disk group:
	```
	diskgroup_name
	```

## Determining Whether Oracle ASM Filter Driver Has Been Configured

The value of the `AFD_STATE` parameter of `SYS_ASMFD_PROPERTIES` specifies whether Oracle ASMFD is configured for the Oracle ASM instance.

You can check the state of Oracle ASMFD with the ASMCMD `afd_state` command. For example:

```
$ $ORACLE_HOME/bin/asmcmd afd_state
ASMCMD-9526: The AFD state is 'LOADED' and filtering is 'DEFAULT' on host 'myhost'
```

For information about using the ASMCMD `afd_state` command to determine the state of Oracle ASMFD, refer to " [afd\_state](managing-oracle-asm-with-asmcmd.md) ".

To determine if Oracles ASMFD is present on the host, you can also display the value of `AFD_STATE` from `SYS_CONTEXT`. You must run the query on the Oracle ASM instance.

If the value of `AFD_STATE` is equal to `NOT` `AVAILABLE`, then Oracle ASMFD is not configured.

```
SQL> SELECT SYS_CONTEXT('SYS_ASMFD_PROPERTIES', 'AFD_STATE') FROM DUAL;
SYS_CONTEXT('SYS_ASMFD_PROPERTIES','AFD_STATE')
--------------------------------------------------------------------------------
NOT AVAILABLE
```

A value of `CONFIGURED` means that Oracle ASMFD is completely set up and the Oracle ASM instance can register with the driver.

```
SQL> SELECT SYS_CONTEXT('SYS_ASMFD_PROPERTIES', 'AFD_STATE') FROM DUAL;
SYS_CONTEXT('SYS_ASMFD_PROPERTIES','AFD_STATE')
--------------------------------------------------------------------------------
CONFIGURED
```

## Updating the Oracle ASM Filter Driver AFD\_DISKSTRING Parameter

The `AFD_DISKSTRING` parameter specifies the Oracle ASMFD disk discovery string that is used to identify the disks to be managed by Oracle ASMFD.

You can set and display the `AFD_DISKSTRING` parameter with the ASMCMD `afd_dsset` and `afd_dgset` commands. For example:

```
$ $ORACLE_HOME/bin/asmcmd afd_dsset '/dev/rdsk/mydisks/*'

$ $ORACLE_HOME/bin/asmcmd afd_dsget
AFD discovery string: /dev/rdsk/mydisks/*
```

You can also set the `AFD_DISKSTRING` with the `ALTER` `SYSTEM` SQL statement. A label is created in the disk header of those disks identified by the Oracle ASMFD disk discovery string.

```
SQL> ALTER SYSTEM AFD_DISKSTRING SET '/dev/disk0','/dev/disk1','/devices/dsk/*';
System altered.
```

You can retrieve the value of `AFD_DISKSTRING` parameter with the following query.

```
SQL> SELECT SYS_CONTEXT('SYS_ASMFD_PROPERTIES', 'AFD_DISKSTRING') FROM DUAL;
SYS_CONTEXT('SYS_ASMFD_PROPERTIES','AFD_DISKSTRING')
--------------------------------------------------------------------------------
'/dev/disk0','/dev/disk1','/devices/dsk/*'
```

Note:

`AFD_DISKSTRING` should not have multiple paths referring to the same device.

See also

- Updating the Oracle ASM ASM\_DISKSTRING Parameter for Oracle ASM Filter Driver Disks for information about updating the Oracle ASM disk discovery string
- [ASM\_DISKSTRING](administering-oracle-asm-instances.md) for information about the `ASM_DISKSTRING` initialization parameter
- [afd\_dsget](managing-oracle-asm-with-asmcmd.md) for information about displaying the Oracle ASMFD disk discovery string
- [afd\_dsset](managing-oracle-asm-with-asmcmd.md) for information about setting the Oracle ASMFD disk discovery string

## Updating the Oracle ASM ASM\_DISKSTRING Parameter for Oracle ASM Filter Driver Disks

You can update the Oracle ASM disk discovery string to add or remove Oracle ASMFD disk label names to and from the `ASM_DIKSTRING` initialization parameter.

For example, you can add the Oracle ASMFD disks to the `ASM_DIKSTRING` initialization parameter as follows:

```
ASM_DISKSTRING = 'AFD:DISK0', 'AFD:DISK1', '/dev/rdsk/mydisks/*'
```

Or you can set the `ASM_DIKSTRING` initialization parameter as follows:

```
ASM_DISKSTRING = 'AFD:*', '/dev/rdsk/mydisks/*'
```

You can display and set the Oracle ASM disk discovery string with the ASMCMD `dsget` and `dsset` commands. For example, you can set the Oracle ASM disk discovery string to add Oracle ASMFD disks as follows:

```
$ $ORACLE_HOME/bin/asmcmd dsset 'AFD:*,/dev/rdsk/mydisks/*'
```

You can remove previously added Oracle ASMFD disks as follows:

```
$ $ORACLE_HOME/bin/asmcmd dsset '/dev/rdsk/mydisks/*'
```

For information about ASMCMD commands to display and set the Oracle ASM disk discovery string, refer to " [dsget](managing-oracle-asm-with-asmcmd.md) " and " [dsset](managing-oracle-asm-with-asmcmd.md) ".

For information about the `ASM_DISKSTRING` initialization parameter, refer to " [ASM\_DISKSTRING](administering-oracle-asm-instances.md) ".

## Setting, Clearing, and Scanning Oracle ASM Filter Driver Labels

Setting a label provisions a disk to be used by Oracle ASMFD. After the label is set, the specified disk is managed by Oracle ASMFD.

You can add, remove, and scan labels with the ASMCMD `afd_label`, `afd_unlabel`, and `afd_scan` commands. For example:

```
$ $ORACLE_HOME/bin/asmcmd afd_label 'disk0' '/dev/rdsk/mydisks/disk0'

$ $ORACLE_HOME/bin/asmcmd afd_unlabel 'disk0'

$ $ORACLE_HOME/bin/asmcmd afd_scan '/dev/rdsk/mydisks/*'
```

For information about ASMCMD commands to add and remove labels on Oracle ASMFD disks, refer to " [afd\_label](managing-oracle-asm-with-asmcmd.md) ", " [afd\_unlabel](managing-oracle-asm-with-asmcmd.md) ", and " [afd\_scan](managing-oracle-asm-with-asmcmd.md) ". In addition, ASMCA provides support for adding and removing labels on Oracle ASMFD disks. For information about using ASMCA to administer disk groups, refer to " [Managing Disk Groups with ASMCA](managing-oracle-asm-with-asmca.md) ".

You can also manage labels with SQL statements. You can set a label with the `ALTER` `SYSTEM` `LABEL` `SET` SQL statement. For example:

```
SQL> ALTER SYSTEM LABEL SET 'disk0' TO '/dev/disk0';
System altered.

SQL> SELECT UPPER(path) FROM V$ASM_DISK ORDER BY PATH;
UPPER(PATH)
--------------------------------------------------------------------------------
AFD:DISK0
```

When you run the statement, you can use the optional `RENAME` or `MIGRATE` option. If a disk was previously provisioned for Oracle ASMFD, you can rename the label with the `RENAME` option. Note that the device should not be managed with Oracle ASMFD when the command is run. If a disk was previously used for an Oracle ASM disk group and the disk group has been dismounted, then you can label this disk using the `MIGRATE` option.

You can use `ALTER` `SYSTEM` `LABEL` `CLEAR` to remove the label from a device and stop Oracle ASMFD from managing the device. For example:

```
SQL> ALTER SYSTEM LABEL CLEAR 'disk0';
System altered.
```

You can use `ALTER` `SYSTEM` `LABEL` `SCAN` on remote nodes after the `ALTER` `SYSTEM` `LABEL` `SET` command is run on the local node.

Because `ALTER` `SYSTEM` `LABEL` `SET` statement writes the label on the disk header and the disk is shared across nodes, the same statement is not run on other nodes of the cluster.

If the device-path is not specified, then the statement uses the `AFD_DISKSTRING` parameter value to perform the scan operation.

```
SQL> ALTER SYSTEM LABEL SCAN
```

## Deconfiguring Oracle ASM Filter Driver

You can deconfigure Oracle ASM Filter Driver (Oracle ASMFD) if it has been configured on your system.

For information about the ASMCMD commands for administering Oracle ASMFD, refer to " [ASMCMD Oracle ASM Filter Driver Management Commands](managing-oracle-asm-with-asmcmd.md) ".

See also

[*Oracle Clusterware Administration and Deployment Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19&id=CWADD-GUID-1A6774CF-FD5F-463E-817F-34E4466443C7) for information about using CRSCTL commands

## Oracle ASM Filter Driver Commands

This section describes the Oracle ASM Filter Driver (ASMFD) commands that are used during installation to manage Oracle ASM Filter Driver. These commands are located in the `/bin` directory of the Oracle Grid Infrastructure home.

### afdload

Purpose

`afdload` loads or unloads the Oracle ASM Filter Driver.

Syntax

```
afdload { start | stop  } [ -s ]
```

The table “Options for the afdload command” contains the options available with the `afdload` command.

Table: Options for the afdload command

| Option | Description |
| --- | --- |
| `start` | Loads the Oracle ASM Filter Driver. |
| `stop` | Unloads the Oracle ASM Filter Driver. |
| `-s` | Operate in silent mode. |

Description

You can use `afdload` to manually load or unload the Oracle ASM Filter Driver.

Before unloading driver with the `stop` option, you must dismount disk groups and shut down Oracle ASM.

`root` or administrator privilege is required to run `afdload`.

Examples

The following is an example of the use of `afdload` to stop (unload) the Oracle ASM Filter Driver.

```
# afdload stop
```

### Deconfiguring Oracle ASM Filter Driver in an Oracle Grid Infrastructure Clusterware Environment

Perform the following steps to deconfigure Oracle ASM Filter Driver in an Oracle Clusterware environment:

1. Update the Oracle ASM disk discovery string to enable Oracle ASM to discover disk devices after Oracle ASMFD is deconfigured.
2. As the Oracle Grid Infrastructure owner list the nodes and node roles in your cluster by running the following command on any node:
	```
	$ $ORACLE_HOME/bin/olsnodes -a
	```
3. Set the ASM diskstring to the old/non-AFD diskpath as Grid Infrastructure owner so that the next startup after deconfiguring AFD will use the path:
	```
	$ $ORACLE_HOME/bin/asmcmd dsset 'new_disk_path','AFD:*'
	```
4. On each Hub and Leaf node, do the following, either in rolling or non-rolling mode:
	1. Log in as the `root` user and stop Oracle Grid Infrastructure:
		```
		# $ORACLE_HOME/bin/crsctl stop crs
		```
		If the command returns any error, then stop Oracle Grid Infrastructure forcibly as follows:
		```
		# $ORACLE_HOME/bin/crsctl stop crs -f
		```
		2. As `root`, stop Oracle ACFS kernel modules to ensure the most reliable shutdown:
		```
		# $ORACLE_HOME/bin/acfsload stop
		```
		3. As `root`, deconfigure Oracle ASMFD:
		```
		# $ORACLE_HOME/bin/asmcmd afd_deconfigure
		```
		4. As `root`, start ACFS kernel modules:
		```
		# $ORACLE_HOME/bin/acfsload start
		```
		5. As `root`, start the Oracle Clusterware stack on the node:
		```
		# $ORACLE_HOME/bin/crsctl start crs
		```
		6. As the Oracle Grid Infrastructure owner verify the status of Oracle ASMFD:
		```
		$ $ORACLE_HOME/bin/asmcmd afd_state
		```
5. As the Oracle Grid Infrastructure owner update the Oracle ASM discovery string to remove the Oracle ASMFD path:
	```
	$ $ORACLE_HOME/bin/asmcmd dsget
	$ $ORACLE_HOME/bin/asmcmd dsset 'new_disk_path'
	```
	Check the current value of the Oracle ASM disk discovery string before updating the value. The *old\_diskstring* value is the old disk discovery string value before updating with the `AFD:` (Oracle ASMFD) paths.

See also

- Updating the Oracle ASM ASM\_DISKSTRING Parameter for Oracle ASM Filter Driver Disks for information about updating the Oracle ASM disk discovery string
- Updating the Oracle ASM Filter Driver AFD\_DISKSTRING Parameter for information about updating the Oracle ASM Filter Driver discovery disk discovery string
- [acfsload](understanding-oracle-acfs-advanced-topics.md) for information about the `acfsload` command
- Determining Whether Oracle ASM Filter Driver Has Been Configured for information about checking on the state of the Oracle ASM Filter Driver

Note:

The underlying new `disk_path` being used must have proper user/group ownership and permissions for the disks used by ASM (for example grid:asmdba ownership and 660 permissions).

### Deconfiguring Oracle ASM Filter Driver in an Oracle Grid Infrastructure Standalone (Oracle Restart) Environment

Perform the following steps to deconfigure Oracle ASM Filter Driver in an Oracle Grid Infrastructure standalone environment:

1. Update the Oracle ASM disk discovery string to enable Oracle ASM to discover disk devices after Oracle ASMFD is deconfigured.
2. Set the ASM diskstring to the old/non-AFD diskpath as Grid Infrastructure owner so that the next startup after deconfiguring AFD will use the path:
	```
	$ $ORACLE_HOME/bin/asmcmd dsset 'new_disk_path','AFD:*'
	```
3. Log in as the `root` user and stop Oracle Grid Infrastructure for a standalone server using the following command:
	```
	# $ORACLE_HOME/bin/crsctl stop has
	```
	If the previous command returns an error, then use the following command:
	```
	# $ORACLE_HOME/bin/crsctl stop has -f
	```
4. As `root`, stop Oracle ACFS kernel modules to ensure the most reliable shutdown:
	```
	# $ORACLE_HOME/bin/acfsload stop
	```
5. As `root`, deconfigure Oracle ASMFD:
	```
	# $ORACLE_HOME/bin/asmcmd afd_deconfigure
	```
6. As `root`, start ACFS kernel modules:
	```
	# $ORACLE_HOME/bin/acfsload start
	```
7. As `root`, start Oracle Grid Infrastructure for a standalone server:
	```
	# $ORACLE_HOME/bin/crsctl start has
	```
8. As the Oracle Grid Infrastructure standalone server owner verify the Oracle ASMFD status:
	```
	$ $ORACLE_HOME/bin/asmcmd afd_state
	```
9. As the Oracle Grid Infrastructure standalone server owner update the Oracle ASM disk discovery string to remove the Oracle ASMFD paths:
```
$ $ORACLE_HOME/bin/asmcmd dsget
 $ $ORACLE_HOME/bin/asmcmd dsset old_diskstring
```

Check the current value of the Oracle ASM disk discovery string before updating the value. The *old\_diskstring* value is the old disk discovery string value before updating with the `AFD:` (Oracle ASMFD) paths.

See also

- Updating the Oracle ASM ASM\_DISKSTRING Parameter for Oracle ASM Filter Driver Disks for information about updating the Oracle ASM disk discovery string
- Updating the Oracle ASM Filter Driver AFD\_DISKSTRING Parameter for information about updating the Oracle ASM Filter Driver discovery disk discovery string
- [acfsload](understanding-oracle-acfs-advanced-topics.md) for information about the `acfsload` command
- Determining Whether Oracle ASM Filter Driver Has Been Configured for information about checking on the state of the Oracle ASM Filter Driver

Note:

The underlying new `disk_path` being used must have proper user/group ownership and permissions for the disks used by ASM (for example grid:asmdba ownership and 660 permissions).

### afddriverstate

Purpose

`afddriverstate` provides information on the current state of the Oracle ASM Filter Driver.

Syntax

```
afddriverstate [-orahome ORACLE_HOME ]
    { installed | loaded | version | supported } [-s]
```

The table “Options for the afddriverstate command” contains the options available with the afddriverstate command.

Table: Options for the afddriverstate command

| Option | Description |
| --- | --- |
| `-orahome` `ORACLE_HOME` | Specifies the Oracle Grid Infrastructure home in which the user has permission to execute the `afddriverstate` command. |
| `installed` | Determines whether Oracle ASM Filter Driver is installed on the system. |
| `loaded` | Determines whether the Oracle ASM Filter Driver is loaded in memory. |
| `version` | Reports the currently installed version of the Oracle ASM Filter Driver system software. |
| `supported` | Reports whether the system is a supported kernel for Oracle ASM Filter Driver. |
| `-s` | Specifies silent mode when running the command. |

Description

You can use `afddriverstate` to display detailed information on the current state of the Oracle ASM Filter Driver.

Examples

The following is an example of the use of `afddriverstate`.

```
$ afddriverstate version
AFD-9325:     Driver operating system kernel version = 2.6.39-400.3.0.el6uek.x86_64(x86_64).
AFD-9326:     Driver Oracle version = 150728.
AFD-9212:     Driver build version = MAIN.
```