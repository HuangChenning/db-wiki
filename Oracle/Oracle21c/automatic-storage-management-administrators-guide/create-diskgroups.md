---
title: "Administrator's Guide"
book: "Automatic Storage Management Administrator's Guide"
doc_id: F30296-05
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/ostmg/create-diskgroups.html
tags:
  - oracle
  - 21c
  - automatic-storage-management-administrators-guide
---

This topic introduces information about creating disk groups.

You can use the `CREATE` `DISKGROUP` SQL statement to create a disk group.

This section contains the following topics:

See Also:

- [Oracle Grid Infrastructure Installation and Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=CWGEN) for information about storage requirements for Oracle Automatic Storage Management
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=SQLRF-GUID-039A1373-1F3F-4A53-A152-8EBC348FB880) for information about the `CREATE` `DISKGROUP` SQL statement

### About Creating a Disk Group

There are multiple items you need to specify when you create a disk group.

When creating a disk group, you:

- Assign a unique name to the disk group.
	The specified disk group name is not case sensitive and is always converted to uppercase when stored internally.
	Note:
	Do not use identifiers for Oracle ASM disk group names that must be quoted, including `#` and `$` characters. While the use of quoted identifiers for Oracle Database objects may be valid as names in some tools, the names may not be valid when using other tools that manage that object. For more information about naming Oracle Database objects, refer to [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=SQLRF51129).
- Determine the redundancy level of the disk group.
	For Oracle ASM to mirror files, specify a redundancy level such as `NORMAL REDUNDANCY` (two-way mirroring by default for most file types), `HIGH REDUNDANCY` (three-way mirroring for all files), `FLEX REDUNDANCY`, or `EXTENDED REDUNDANCY`.
	Specify `EXTERNAL REDUNDANCY` if you do not want mirroring by Oracle ASM. For example, you might choose `EXTERNAL REDUNDANCY` to use storage array protection features.
	After a disk group is created with `NORMAL` or `HIGH` redundancy, you can migrate the disk group to a `FLEX` redundancy disk group with the `CONVERT` `REDUNDANCY` `TO` `FLEX` clause of the `ALTER` `DISKGROUP` SQL statement. You cannot migrate an `EXTERNAL` disk group to a `FLEX` redundancy disk group. When migrating to a flex disk group, the disk group must have a minimum of three failure groups and must be mounted in restricted mode (`MOUNTED` `RESTRICTED`) for the duration of the migration.
	To change the redundancy level for `NORMAL`, `HIGH`, or `EXTERNAL` disk groups to a `NORMAL`, `HIGH`, or `EXTERNAL`, you must create another disk group with the appropriate redundancy and then move the files to the new disk group.
	For `FLEX` and `EXTENDED` redundancy disk groups, the disk group redundancy cannot be changed. However, the redundancy of the files in the disk group can be changed by modifying the `REDUNDANCY` property of the respective file group.
- Identify the disks that are to be formatted as Oracle ASM disks belonging to the disk group.
	The disks can be specified using operating system dependent wildcard characters in search strings that Oracle ASM then uses to find the disks. You can specify names for the disks with the `NAME` clause or use the system-generated names.
- Optionally indicate that the disks belong to specific failure groups.
	You must create failure groups of equal size to maintain space balance and even distribution of mirror data.
- Optionally determine the type of failure group, such as quorum (`QUORUM`) or regular (default).
- Optionally provide disk group attribute values, such as the values for software compatibility or allocation unit size.

All disks in the disk group must be of equal size. Oracle ASM programmatically determines the size of each disk. If for some reason the size cannot be determined, or to restrict the amount of space used on a disk, you can specify a `SIZE` clause for a disk; however, the same size value must be specified for every disk in the disk group.

Oracle ASM creates operating system–independent names for the disks in a disk group that you can use to reference the disks in other SQL statements. Optionally, you can provide your own name for a disk using the `NAME` clause. Disk names are available in the `V$ASM_DISK` view.

You can use the ASMCMD `stamp` command to provision disks for Oracle ASM before creating a disk group that uses them. If a disk is provisioned, then the disk name, failure group, and site information are specified at the time the disk is provisioned and do not need to be specified when the disk group is created.

Note:

A disk cannot belong to multiple disk groups.

The Oracle ASM instance ensures that any disk in a newly created disk group is addressable and is not currently a member of another disk group. You must use `FORCE` only when adding a disk that was dropped with `FORCE`. If a disk is dropped with `NOFORCE`, then you can add it with `NOFORCE`. For example, a disk might have failed and was dropped from its disk group. After the disk is repaired, it is no longer part of any disk group, but Oracle ASM still recognizes that the disk had been a member of a disk group. You must use the `FORCE` flag to include the disk in a new disk group. In addition, the disk must be addressable. Otherwise, the operation fails.

Note:

Use caution when using the `FORCE` option to add a previously used disk to a disk group; you might cause another disk group to become unusable.

The `CREATE DISKGROUP` statement mounts the disk group for the first time, and adds the disk group name to the `ASM_DISKGROUPS` initialization parameter if a server parameter file is being used. If a text initialization parameter file is being used and you want the disk group to be automatically mounted at instance startup, then you must remember to add the disk group name to the `ASM_DISKGROUPS` initialization parameter before you shut down and restart the Oracle ASM instance. You can also create disk groups with Oracle ASM Configuration Assistant (ASMCA) and the ASMCMD `mkdg` command.

See Also:

- [Managing Oracle ASM Flex Disk Groups](asm-filegroups.md) for information about flex disk groups and file groups
- [Mirroring, Redundancy, and Failure Group Options](mirroring-diskgroup-redundancy.md) and [Understanding Oracle ASM Concepts](asm-intro.md) for information about redundancy levels and failure groups
- Storing Oracle Cluster Registry and Voting Files in Oracle ASM Disk Groups for information about `QUORUM` and `REGULAR` failure groups
- [stamp](asmcmd-diskgroup-commands.md) for information about the ASMCMD `stamp` command
- [Managing Disk Groups with ASMCA](manage-asm-asmca.md) for information about creating disk groups with Oracle ASM Configuration Assistant (ASMCA)
- [mkdg](asmcmd-diskgroup-commands.md) for information about creating disk groups with the ASMCMD `mkdg` command
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=SQLRF01114) for information about the `CREATE` `DISKGROUP` SQL statement

### Creating Disk Groups Using the CREATE DISKGROUP SQL Statement

You can create disk groups for data and the fast recovery area using the `CREATE DISKGROUP` SQL statement.

The SQL statement in Example 4-1 creates a disk group named `data` with normal redundancy consisting of two failure groups `controller1` or `controller2` with four disks in each failure group. The `data` disk group is typically used to store database data files.

The example assumes that the `ASM_DISKSTRING` initialization parameter is set to the ' `/devices/*` ' string. Oracle ASM disk discovery identifies `diska1` through `diska4` and `diskb1` through `diskb4` in the `/devices` directory.

In Example 4-1, the `NAME` clauses enable you to explicitly assign names to the disks rather than the default system-generated names. The system-generated names are in the form `diskgroup_nnnn`, where `nnnn` is the disk number for the disk in the disk group.

When creating the disk group in Example 4-1, the values of following disk group attributes were explicitly set:

- `AU_SIZE`
	Specifies the size of the allocation unit for the disk group.
	You can view the value of the `AU_SIZE` disk group attribute in the `ALLOCATION_UNIT_SIZE` column of the `V$ASM_DISKGROUP` view.
- `COMPATIBLE`.`ASM`
	Determines the minimum software version for any Oracle ASM instance that uses a disk group.
- `COMPATIBLE`.`RDBMS`
	Determines the minimum software version for any database instance that uses a disk group.
- `COMPATIBLE`.`ADVM`
	Determines whether the disk group can contain Oracle ADVM volumes.

In Example 4-2, the `fra` disk group (typically created for the fast recovery area) is created with the default disk group attribute values. Names are not specified for the Oracle ASM disks and failure groups are not explicitly specified. This example assumes that `diskc1` through `diskc9` are present in the `/devices` directory.

Example 4-1 Creating the DATA disk group

```
CREATE DISKGROUP data NORMAL REDUNDANCY
  FAILGROUP controller1 DISK
    '/devices/diska1' NAME diska1,
    '/devices/diska2' NAME diska2,
    '/devices/diska3' NAME diska3,
    '/devices/diska4' NAME diska4
  FAILGROUP controller2 DISK
    '/devices/diskb1' NAME diskb1,
    '/devices/diskb2' NAME diskb2,
    '/devices/diskb3' NAME diskb3,
    '/devices/diskb4' NAME diskb4
  ATTRIBUTE 'au_size'='4M',
    'compatible.asm' = '19.0', 
    'compatible.rdbms' = '19.0',
    'compatible.advm' = '19.0';
```

Example 4-2 Creating the FRA disk group

```
CREATE DISKGROUP fra NORMAL REDUNDANCY
  DISK '/devices/diskc*';
```

See Also:

- [Administering Oracle ASM Filter Driver](administer-filter-driver.md) for information about the disk name format when using Oracle ASM Filter Driver
- [About Oracle ASM Allocation Units](asm-intro.md) for information about allocation units
- [Disk Group Compatibility Attributes](diskgroup-compatibility.md) for information about `COMPATIBLE.ASM`, `COMPATIBLE.RDBMS`, and `COMPATIBLE.ADVM`

### Creating Disk Groups for a New Oracle Installation

This topic describes the basic procedure for creating disk groups during a new installation of Oracle Grid Infrastructure standalone (Oracle Restart) option and Oracle Database.

The procedure described in this topic for a new installation of Oracle Grid Infrastructure standalone (Oracle Restart) assumes that a disk group is configured for storing the database data files and a disk group is configured for storing the fast recovery area files.

Note:

In Oracle Grid Infrastructure for cluster configurations, the Oracle Cluster Registry (OCR) and voting files should be stored on their own disk group. However, if only two disk groups are created for the Oracle ASM installation, then store the OCR and voting files in the disk group that contains the database data files.

1. Install Oracle Restart with OUI, following the screen prompts.
	During the installation, create a disk group (`data`) for storing database data files and control files.
	This OUI disk group creation process is similar to creating a disk group with Oracle ASM Configuration Assistant (ASMCA). Detailed information about installation with Oracle Universal Installer (OUI) and database creation with Database Configuration Assistant (DBCA) is available in the installation guides for your specific operating system.
2. After the Oracle Grid Infrastructure is installed, use ASMCA to create a disk group (`fra`) for storing the fast recovery area files.
	You can also create the `fra` disk group with SQL\*Plus or ASMCMD commands run from the Oracle Grid Infrastructure home.
3. Install the Oracle Database software with OUI, following the screen prompts.
4. After the database software has been installed, run DBCA to create a database, following the screen prompts.
	During the creation of the database, make the appropriate selections to use Oracle ASM for storage of data files and fast recovery area files. When prompted:
	- Store database data files in the `data` disk group
		- Store fast recovery area files in the `fra` disk group

See Also:

- [Managing Disk Groups with ASMCA](manage-asm-asmca.md) for information about using ASMCA to create or alter disk groups
- Storing Oracle Cluster Registry and Voting Files in Oracle ASM Disk Groups for information about storing Oracle Cluster Registry (OCR) and voting files
- About Creating a Disk Group for information about creating a disk group with SQL\*Plus
- [mkdg](asmcmd-diskgroup-commands.md) for information about creating a disk group with ASMCMD
- [Oracle Database Backup and Recovery User’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=BRADV8183) for information about configuring the fast recovery area
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ADMIN11103) for information about specifying a fast recovery area
- [Oracle Grid Infrastructure Installation and Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=CWGEN) for your operating system for detailed information about installation of Oracle Grid Infrastructure and Oracle Restart
- [Oracle Database Installation Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=GINST) for your operating system for detailed information about installation of an Oracle Database

### Specifying the Logical and Physical Sector Size

You can use the optional `LOGICAL_SECTOR_SIZE` and `SECTOR_SIZE` disk group attributes with the `CREATE` `DISKGROUP` and `ALTER` `DISKGROUP` SQL statements to specify a logical sector size and physical sector size for a disk group.

Note:

To specify the logical and physical sector size, the disks must support sector size emulation.

The `SECTOR_SIZE` disk group attribute can be set to `512`, `4096`, or `4K` if the disks support those values. The default value is platform dependent. The `COMPATIBLE.ASM` and `COMPATIBLE.RDBMS` disk group attributes must be set to `11.2` or higher to enable the setting of a value for the sector size during disk group creation. The `COMPATIBLE.ASM` disk group attribute must be set to `12.2` or higher to alter the sector size.

The `LOGICAL_SECTOR_SIZE` disk group attribute can explicitly set the logical sector size of the disk group instead of the size that is estimated from the disks that join the disk group. The `LOGICAL_SECTOR_SIZE` disk group attribute can be set to `512`, `4096`, or `4K`. The value specifies the smallest possible I/O that the disk group can accept, and also limits what types of disks can join the disk group. The `COMPATIBLE.ASM` disk group attribute must be set to `12.2` or higher to set the logical sector size during creation of a disk group or alter the size of a disk group that has been created.

Table 4-1 lists the possible valid combinations of the logical sector size and sector size disk group attributes during disk group creation for disk sizes and types. The first column describes the user-specified values for logical sector size and sector size attributes during disk group creation. `NS` indicates that the no value was specified.

The top row of the table describes the combination of the disks used. A 512 native sector size disk has sector size equal to logical sector size equal to `512`. The 512 native and 512 emulated heading describes the combination of 512 native disks and 512 emulated disk. The 512 emulated disk has a 4 k physical sector size and a 512 logical sector size. The values in each of the table cells represents the final value of sector sizes of the disk group. `Error` indicates that the disk group creation fails and an error message is displayed.

Table 4-1 Possible combinations of sector size and logical sector size by disk size and type

| SECTOR\_SIZE/LOGICAL\_SECTOR\_SIZE specified at disk group creation | 512 native disks | 512 emulated disks | 4K native disks | 512 native disks + 512 emulated disks | 512 emulated disks + 4K native disks |
| --- | --- | --- | --- | --- | --- |
| `4K` / `4K` | `Error` | `4K` / `4K` | `4K` / `4K` | `Error` | `4K` / `4K` |
| `NS` / `4K` | `Error` | `4K` / `4K` | `4K` / `4K` | `Error` | `4K` / `4K` |
| `4K` / `512` | `Error` | `4K` / `512` | `Error` | `Error` | `Error` |
| `512` / `512` | `512` / `512` | `512` / `512` | `Error` | `512` / `512` | `Error` |
| `512` / `NS` | `512` / `512` | `512` / `512` | `Error` | `512` / `512` | `Error` |
| `4K` / `NS` | `Error` | `4K` / `512` | `4K` / `4K` | `Error` | `4K` / `4K` |
| `NS` / `512` | `512` / `512` | `512` / `512` | `Error` | `512` / `512` | `Error` |
| `NS` / `NS` | `512` / `512` | `512` / `512` | `4K` / `4K` | `512` / `512` | `4K` / `4K` |

You can determine the logical sector and sector size values that have either been assumed or explicitly set for a successful disk group creation by querying `V$ASM` views or running ASMCMD commands. The `LOGICAL_SECTOR_SIZE` and `SECTOR_SIZE` columns are included in the `V$ASM_DISKGROUP` and `V$ASM_ATTRIBUTE` views to display the values. These columns represent the logical sector size and sector size values of the disk group in bytes. The ASMCMD `lsdg` also displays the values of the logical sector size and sector size for the disk group. In addition, the disk group attributes are displayed with the `V$ASM_ATTRIBUTE` view and the ASMCMD `lsattr` command. For example:

```
SQL> SELECT name, value FROM V$ASM_ATTRIBUTE 
     WHERE (name = 'sector_size' OR name = 'logical_sector_size') AND group_number = 1;
NAME                          VALUE
----------------------------- ---------------------------
sector_size                   4096
logical_sector_size           512

SQL> SELECT logical_sector_size, sector_size FROM V$ASM_DISKGROUP 
     WHERE group_number = 1;
LOGICAL_SECTOR_SIZE SECTOR_SIZE
------------------- -----------
                512        4096
```

As shown in Example 4-3, you can use the `LOGICAL_SECTOR_SIZE` and `SECTOR_SIZE` disk group attributes with the `CREATE` `DISKGROUP` and `ALTER` `DISKGROUP` SQL statements to specify the logical and physical sector size of the Oracle ASM disk group.

The following notes apply to the logical sector size and sector size disk group attributes.

- During the migration process from 512 bytes to 4096 bytes, password files stored on an Oracle ASM disk group do not need to be migrated or recreated. The password files are a special case and retain their 512 byte block size, even after the new sector sizes are 4096 bytes.
- If the value of the `LOGICAL_SECTOR_SIZE` column is 512, while the value in the `SECTOR_SIZE` column is 4096, then the disk group supports 512 sector size emulation. This means that I/O operations can be both 512 or 4096 in size. For example, we can have redo log files with a file block size of 512 bytes in the disk group that can be both read and written to, as well as creating new redo log files with a file block size of 4096 bytes.
- The physical sector size (`SECTOR_SIZE`) cannot be smaller than the logical sector size (`LOGICAL_SECTOR_SIZE`) in an Oracle ASM disk group.
- Not all disks support all of the possible `SECTOR_SIZE` values. The sector size attribute setting must be compatible with the physical hardware.

Example 4-3 Specifying logical and sector sizes for disks in a disk group

```
CREATE DISKGROUP data NORMAL REDUNDANCY
  FAILGROUP controller1 DISK
    '/devices/diska1',
    '/devices/diska2',
    '/devices/diska3',
    '/devices/diska4'
  FAILGROUP controller2 DISK
    '/devices/diskb1',
    '/devices/diskb2',
    '/devices/diskb3',
    '/devices/diskb4'
  QUORUM FAILGROUP quorum_failgrp DISK '/devices/diskc1'
  ATTRIBUTE 'compatible.asm' = '12.2', 'compatible.rdbms' = '12.2',
            'sector_size'='4096', 'logical_sector_size'='512';

ALTER DISKGROUP data2  
  SET ATTRIBUTE 'compatible.asm' = '12.2', 'compatible.rdbms' = '12.2';

ALTER DISKGROUP data2
  SET ATTRIBUTE 'sector_size'='4096', 'logical_sector_size'='4096';
```

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=SQLRF01114) for information about the disk group attributes and the `CREATE` `DISKGROUP` SQL statement
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=SQLRF01602) for information about the `BLOCKSIZE` keyword
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=REFRN003) for details about the `V$ASM_ATTRIBUTE`, `V$ASM_DISK`, and `V$ASM_DISKGROUP` views
- [ASMCMD Disk Group Management Commands](asmcmd-diskgroup-commands.md) for information about ASMCMD disk group management commands

### Storing Oracle Cluster Registry and Voting Files in Oracle ASM Disk Groups

You can store Oracle Cluster Registry (OCR) and voting files in Oracle ASM disk groups.

You can also store a backup of the OCR file in a disk group. Voting files and OCR are two important components of Oracle Clusterware. Voting files manage information about node membership. OCR manages cluster and Oracle Real Application Clusters (Oracle RAC) database configuration information.

A quorum failure group is a special type of failure group that does not contain user data. Quorum failure groups are used for storing Oracle ASM metadata. A quorum failure group may also contain voting files if those files are stored in a disk group that contains a quorum failure group. Additionally, Oracle ASM uses a quorum failure group to help determine if the disk group can be mounted in the event of the loss of one or more failure groups.

Because disks in quorum failure groups do not contain user data, a quorum failure group is not considered when determining redundancy requirements in respect to storing user data.

You can manage and monitor OCR and voting files with CRSCTL and `ocrconfig` command-line tools, `CREATE` and `ALTER` `DISKGROUP` SQL statements, and `V$ASM` views.

The CRSCTL and `ocrconfig` commands enable the placement of OCR storage and Cluster Synchronization Services (CSS) voting files inside the disk groups managed by Oracle ASM.

The `QUORUM` and `REGULAR` keywords in `CREATE` and `ALTER` `DISKGROUP` SQL statements enable the specification of an additional qualifier for failure groups or disks when creating or altering a disk group. Note that `QUORUM` disks (or disks in `QUORUM` failure groups) cannot contain user data, while `REGULAR` disks (or disks in non-quorum failure groups) do not have this restriction.

You can use these keywords before the keyword `FAILGROUP` if a failure group is being explicitly specified. If the failure group is implicitly implied, you can use these keywords (`QUORUM` / `REGULAR`) before the keyword `DISK`. When failure groups are explicitly specified, it is an error to specify these keywords (`QUORUM` / `REGULAR`) immediately before the keyword `DISK`. `REGULAR` is the default failure group type.

When performing operations on existing disks or failure groups, the qualifier specified in the SQL must match the qualifier that was specified when the disks or failure groups were added to the disk group.

Example 4-4 shows the creation of a disk group with a `QUORUM` failure group. For Oracle Clusterware files a minimum of three disk devices or three failure groups is required with a normal redundancy disk group. A `QUORUM` failure group is not considered when determining redundancy requirements in respect to storing user data. The `COMPATIBLE.ASM` disk group compatibility attribute must be set to `11.2` or greater to store OCR or voting files in a disk group.

The `FAILGROUP_TYPE` column in the `V$ASM_DISK` or `V$ASM_DISK_STAT` views specifies the failure group type. The value for this column is `REGULAR` for regular failure groups and `QUORUM` for quorum failure groups. The `VOTING_FILE` column in the `V$ASM_DISK` or `V$ASM_DISK_STAT` views specifies whether a disk contains a voting file. The value for this column is either `Y` if the disk contains a voting file or `N` if not. The value of `USABLE_FILE_MB` in `V$ASM_DISKGROUP` or `V$ASM_DISKGROUP_STAT` does not consider any free space that is present in `QUORUM` disks because that space is not available for client data files.

Example 4-4 Using the QUORUM keyword when creating a failure group

```
CREATE DISKGROUP mgmt_dg NORMAL REDUNDANCY
   FAILGROUP fg1 DISK '/devices/diskg1'
   FAILGROUP fg2 DISK '/devices/diskg2'
   QUORUM FAILGROUP fg3 DISK '/devices/diskg3'
   ATTRIBUTE 'compatible.asm' = '12.2.0.0.0';
```

See Also:

- [Oracle ASM Failure Groups](mirroring-diskgroup-redundancy.md) for information about failure groups
- [Views Containing Oracle ASM Information](views-asm-info.md) for information about `V$ASM` views
- [Oracle Grid Infrastructure Installation and Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=CWGEN) for information about configuring voting files and Oracle Cluster Registry (OCR)
- [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=CWADD92368) for information about managing Oracle Cluster Registry and voting files
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=SQLRF01114) for information about the [`CREATE DISKGROUP`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=SQLRF01114) and [`ALTER DISKGROUP`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=SQLRF01113) SQL statements
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=REFRN003) for details about the `V$ASM` \* dynamic performance views