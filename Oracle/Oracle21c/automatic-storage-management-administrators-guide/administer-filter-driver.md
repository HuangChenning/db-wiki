---
title: "Administrator's Guide"
book: "Automatic Storage Management Administrator's Guide"
doc_id: F30296-05
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/ostmg/administer-filter-driver.html
tags:
  - oracle
  - 21c
  - automatic-storage-management-administrators-guide
---

Oracle ASM Filter Driver (Oracle ASMFD) simplifies the configuration and management of disk devices by eliminating the need to rebind disk devices used with Oracle ASM each time the system is restarted.

This section contains the following topics:

WARNING:

When configuring Oracle ASM, including Oracle ASMFD, do not manually modify or erase the contents of Oracle ASM disks or modify any files, including configuration files.

Note:

- The configuration for Oracle ASMFD can now be enabled with a check box to be an automated process during Oracle Grid Infrastructure installation.
- If ASMLIB is installed and configured for an existing Oracle ASM installation, then you must explicitly uninstall the existing ASMLIB configuration before installing and configuring Oracle ASMFD.
- Oracle ASM Filter Driver (Oracle ASMFD) is available on Linux systems starting with Oracle Database 12c Release 1 (12.1.0.2). Oracle ASMFD is available on Solaris systems starting with Oracle Database 12c Release 2 (12.2.0.1).
- In the steps of the procedures described in the topics of this section, the `$ORACLE_HOME` environmental variable is set to the directory path of the Oracle Grid Infrastructure home. Commands that show `#` as the operating system prompt must be run as the root user. Commands that show `$` as the operating system prompt should be run as the owner of Oracle Grid Infrastructure home

See Also:

- [Oracle Grid Infrastructure Installation and Upgrade Guide for Linux](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=CWLIN-GUID--B5D06658-1B1B-4922-8853-50670ABCDADB) for information about installing and configuring Oracle ASMFD on Oracle Grid Infrastructure, and deinstalling Oracle ASMLIB
- [Oracle Database Installation Guide for Linux](ollink:LADBI-GUID-B5D06658-1B1B-4922-8853-50670ABCDADB) for information about installing and configuring Oracle ASMFD on Oracle Standalone Server
- My Oracle Support articles about Oracle ASMFD available at [My Oracle Support](https://support.oracle.com/) ([`https://support.oracle.com`](https://support.oracle.com/)) for additional information about Oracle ASMFD, such as supported operating system platforms (certification matrix) or configuration issues.
- [ASMCMD Oracle ASM Filter Driver Management Commands](asmcmd-filterdriver-commands.md) for information about the ASMCMD commands for administering Oracle ASMFD
- [About ASMCMD](about-asmcmd.md) for information about all the ASMCMD commands
- [Managing Oracle ASM Filter Driver With Oracle Enterprise Manager](admin-asm-em.md) for information about using Oracle Enterprise Manager to administer Oracle ASMFD

### About Oracle ASM Filter Driver

Oracle ASM Filter Driver (Oracle ASMFD) is a kernel module that resides in the I/O path of the Oracle ASM disks. Oracle ASM uses the filter driver to validate write I/O requests to Oracle ASM disks.

Oracle ASMFD simplifies the configuration and management of disk devices by eliminating the need to rebind disk devices used with Oracle ASM each time the system is restarted.

Oracle ASM Filter Driver rejects any I/O requests that are invalid. This action eliminates accidental overwrites of Oracle ASM disks that would cause corruption in the disks and files within the disk group. For example, the Oracle ASM Filter Driver filters out all non-Oracle I/Os which could cause accidental overwrites.

About Oracle ASMLIB and Oracle ASM Filter Driver

Starting with Oracle Grid Infrastructure 12c Release 2 (12.2), Oracle ASM Filter Driver (Oracle ASMFD) cannot be installed and configured if Oracle ASMLIB has been installed on the system. If you want to install and configure Oracle ASMFD, you must first uninstall Oracle ASMLIB.

See Also:

- [Oracle Grid Infrastructure Installation and Upgrade Guide for Linux](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=CWLIN-GUID--B5D06658-1B1B-4922-8853-50670ABCDADB) for information about installing and configuring Oracle ASMFD on Oracle Grid Infrastructure, and deinstalling Oracle ASMLIB

About Partition Tables and Oracle ASM Filter Driver

Extended partition tables are not supported with Oracle ASM filter driver (ASMFD) in Oracle Automatic Storage Management 12.2 Release 1 (12.2.0.1).

### Determining Whether Oracle ASM Filter Driver Has Been Configured

The value of the `AFD_STATE` parameter of `SYS_ASMFD_PROPERTIES` specifies whether Oracle ASMFD is configured for the Oracle ASM instance.

You can check the state of Oracle ASMFD with the ASMCMD `afd_state` command. For example:

```
$ $ORACLE_HOME/bin/asmcmd afd_state
ASMCMD-9526: The AFD state is 'LOADED' and filtering is 'DEFAULT' on host 'myhost'
```

For information about using the ASMCMD `afd_state` command to determine the state of Oracle ASMFD, refer to [afd\_state](asmcmd-filterdriver-commands.md).

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

### Updating the Oracle ASM Filter Driver AFD\_DISKSTRING Parameter

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

See Also:

- Updating the Oracle ASM ASM\_DISKSTRING Parameter for Oracle ASM Filter Driver Disks for information about updating the Oracle ASM disk discovery string
- [ASM\_DISKSTRING](init-params-asm-instance.md) for information about the `ASM_DISKSTRING` initialization parameter
- [afd\_dsget](asmcmd-filterdriver-commands.md) for information about displaying the Oracle ASMFD disk discovery string
- [afd\_dsset](asmcmd-filterdriver-commands.md) for information about setting the Oracle ASMFD disk discovery string

### Updating the Oracle ASM ASM\_DISKSTRING Parameter for Oracle ASM Filter Driver Disks

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

See Also:

- Updating the Oracle ASM Filter Driver AFD\_DISKSTRING Parameter for information about updating the Oracle ASMFD disk discovery string
- [ASM\_DISKSTRING](init-params-asm-instance.md) for information about the `ASM_DISKSTRING` initialization parameter
- [afd\_dsget](asmcmd-filterdriver-commands.md) for information about displaying the Oracle ASMFD disk discovery string
- [afd\_dsset](asmcmd-filterdriver-commands.md) for information about setting the Oracle ASMFD disk discovery string

### Setting, Clearing, and Scanning Oracle ASM Filter Driver Labels

Setting a label provisions a disk to be used by Oracle ASMFD. After the label is set, the specified disk is managed by Oracle ASMFD.

You can add, remove, and scan labels with the ASMCMD `afd_label`, `afd_unlabel`, and `afd_scan` commands. For example:

```
$ $ORACLE_HOME/bin/asmcmd afd_label 'disk0' '/dev/rdsk/mydisks/disk0'

$ $ORACLE_HOME/bin/asmcmd afd_unlabel 'disk0'

$ $ORACLE_HOME/bin/asmcmd afd_scan '/dev/rdsk/mydisks/*'
```

In addition, Oracle ASM Configuration Assistant (ASMCA) provides support for adding and removing labels on Oracle ASMFD disks.

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

See Also:

- [afd\_label](asmcmd-filterdriver-commands.md) for information about adding labels on Oracle ASMFD disks
- [afd\_unlabel](asmcmd-filterdriver-commands.md) for information about removing labels on Oracle ASMFD disks
- [afd\_scan](asmcmd-filterdriver-commands.md) for information about scanning labels on Oracle ASMFD disks
- [Managing Disk Groups with ASMCA](manage-asm-asmca.md) for information about using ASMCA to administer disk groups

### Deconfiguring Oracle ASM Filter Driver

You can deconfigure Oracle ASM Filter Driver (Oracle ASMFD) if it has been configured on your system.

This section contains the following topics:

- Deconfiguring Oracle ASM Filter Driver in an Oracle Grid Infrastructure Clusterware Environment
- Deconfiguring Oracle ASM Filter Driver in an Oracle Grid Infrastructure Standalone (Oracle Restart) Environment

See Also:

- [ASMCMD Oracle ASM Filter Driver Management Commands](asmcmd-filterdriver-commands.md) for information about the ASMCMD commands for administering Oracle ASMFD
- [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=CWADD91142) for information about using CRSCTL commands

#### Deconfiguring Oracle ASM Filter Driver in an Oracle Grid Infrastructure Clusterware Environment

Perform the following steps to deconfigure Oracle ASM Filter Driver in an Oracle Clusterware environment:

1. Update the Oracle ASM disk discovery string to enable Oracle ASM to discover disk devices after Oracle ASMFD is deconfigured.
2. As the Oracle Grid Infrastructure owner list the nodes and node roles in your cluster by running the following command on any node:
	```
	$ $ORACLE_HOME/bin/olsnodes -a
	```
3. On each Hub and Leaf node, do the following, either in rolling or non-rolling mode:
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
		4. If the storage devices are owned by `root`, set the permissions required by the Oracle Grid Infrastructure user to access the devices.
		5. As `root`, start ACFS kernel modules:
		```
		# $ORACLE_HOME/bin/acfsload start
		```
		6. As `root`, start the Oracle Clusterware stack on the node:
		```
		# $ORACLE_HOME/bin/crsctl start crs
		```
		7. As the Oracle Grid Infrastructure owner verify the status of Oracle ASMFD:
		```
		$ $ORACLE_HOME/bin/asmcmd afd_state
		```
4. As the Oracle Grid Infrastructure owner update the Oracle ASM discovery string to remove the Oracle ASMFD path:
	```
	$ $ORACLE_HOME/bin/asmcmd dsget
	$ $ORACLE_HOME/bin/asmcmd dsset old_diskstring
	```
	Check the current value of the Oracle ASM disk discovery string before updating the value. The `old_diskstring` value is the old disk discovery string value before updating with the `AFD:` (Oracle ASMFD) paths.

See Also:

- Updating the Oracle ASM ASM\_DISKSTRING Parameter for Oracle ASM Filter Driver Disks for information about updating the Oracle ASM disk discovery string
- Updating the Oracle ASM Filter Driver AFD\_DISKSTRING Parameter for information about updating the Oracle ASM Filter Driver discovery disk discovery string
- [Oracle Automatic Storage Management Cluster File System Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ACFSG-GUID-5BA14B0C-DB90-433F-9394-DD7B44078835) for information about the `acfsload` command
- Determining Whether Oracle ASM Filter Driver Has Been Configured for information about checking on the state of the Oracle ASM Filter Driver
- [Oracle Grid Infrastructure Installation and Upgrade Guide for Microsoft Windows x64 (64-Bit)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=CWLIN-GUID-70D50812-CCB2-41E4-AA3B-4689E1DA934E) for information about configuring device persistence for Oracle ASM

#### Deconfiguring Oracle ASM Filter Driver in an Oracle Grid Infrastructure Standalone (Oracle Restart) Environment

Perform the following steps to deconfigure Oracle ASM Filter Driver in an Oracle Grid Infrastructure standalone environment:

1. Update the Oracle ASM disk discovery string to enable Oracle ASM to discover disk devices after Oracle ASMFD is deconfigured.
2. Log in as the `root` user and stop Oracle Grid Infrastructure for a standalone server using the following command:
	```
	# $ORACLE_HOME/bin/crsctl stop has
	```
	If the previous command returns an error, then use the following command:
	```
	# $ORACLE_HOME/bin/crsctl stop has -f
	```
3. As `root`, stop Oracle ACFS kernel modules to ensure the most reliable shutdown:
	```
	# $ORACLE_HOME/bin/acfsload stop
	```
4. As `root`, deconfigure Oracle ASMFD:
	```
	# $ORACLE_HOME/bin/asmcmd afd_deconfigure
	```
5. If the storage devices are owned by `root`, set the permissions required by the Oracle Grid Infrastructure user to access the devices.
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

Check the current value of the Oracle ASM disk discovery string before updating the value. The `old_diskstring` value is the old disk discovery string value before updating with the `AFD:` (Oracle ASMFD) paths.

See Also:

- Updating the Oracle ASM ASM\_DISKSTRING Parameter for Oracle ASM Filter Driver Disks for information about updating the Oracle ASM disk discovery string
- Updating the Oracle ASM Filter Driver AFD\_DISKSTRING Parameter for information about updating the Oracle ASM Filter Driver discovery disk discovery string
- [Oracle Automatic Storage Management Cluster File System Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ACFSG-GUID-5BA14B0C-DB90-433F-9394-DD7B44078835) for information about the `acfsload` command
- Determining Whether Oracle ASM Filter Driver Has Been Configured for information about checking on the state of the Oracle ASM Filter Driver
- [Oracle Grid Infrastructure Installation and Upgrade Guide for Microsoft Windows x64 (64-Bit)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=CWLIN-GUID-70D50812-CCB2-41E4-AA3B-4689E1DA934E) for information about configuring device persistence for Oracle ASM

### Oracle ASM Filter Driver Commands

This section describes the Oracle ASM Filter Driver (ASMFD) commands that are used during installation to manage Oracle ASM Filter Driver. These commands are located in the `/bin` directory of the Oracle Grid Infrastructure home.

- afdload
- afddriverstate

#### afdload

Purpose

`afdload` loads or unloads the Oracle ASM Filter Driver.

Syntax

```
afdload { start | stop  } [ -s ]
```

Table 12-1 contains the options available with the `afdload` command.

Table 12-1 Options for the afdload command

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

#### afddriverstate

Purpose

`afddriverstate` provides information on the current state of the Oracle ASM Filter Driver.

Syntax

```
afddriverstate [-orahome ORACLE_HOME ] 
    { installed | loaded | version | supported } [-s]
```

Table 12-2 contains the options available with the afddriverstate command.

Table 12-2 Options for the afddriverstate command

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