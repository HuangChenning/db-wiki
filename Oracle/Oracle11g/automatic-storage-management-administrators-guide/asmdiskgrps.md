---
title: Administering Oracle ASM Disk Groups
book: "Automatic Storage Management Administrator's Guide"
doc_id: E18951-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmdiskgrps.htm
tags:
  - oracle
  - 11g
  - automatic-storage-management-administrators-guide
---

## 4 Administering Oracle ASM Disk Groups

This chapter describes how to administer Oracle Automatic Storage Management (Oracle ASM) disk groups. This information includes how to create, alter, drop, mount, and dismount Oracle ASM disk groups. The database instances that use Oracle ASM can continue operating while you administer disk groups.

The examples in this chapter use SQL statements. These examples assume that SQL\*Plus is run from the Oracle grid home where Oracle ASM is installed and the Oracle environmental variables are set to this home. The examples also assume that the Oracle ASM instance is running. This chapter contains the following topics:

For information about starting up an Oracle ASM instance, refer to ["Starting Up an Oracle ASM Instance"](asminst.md).

For information about administering Oracle ASM disk groups with Oracle Enterprise Manager, refer to [Chapter 9, "Administering Oracle ASM with Oracle Enterprise Manager"](asm_em.md).

For information about administering Oracle ASM disk groups with Oracle ASM Configuration Assistant (ASMCA), refer to [Chapter 11, "Oracle ASM Configuration Assistant"](asmca.md).

For information about administering Oracle ASM disk groups with ASMCMD, refer to [Chapter 12, "Oracle ASM Command-Line Utility"](asm_util.md).

See Also:

The Oracle Cloud Storage page on the Oracle Technology Network Web site at `http://www.oracle.com/technetwork/database/cloud-storage/index.html` for more information about Oracle ASM

## Disk Group Attributes

Disk group attributes are parameters that are bound to a disk group, rather than an Oracle ASM instance.

Disk group attributes can be set when a disk group is created or altered, unless otherwise noted in the following list.

- ACCESS\_CONTROL.ENABLED
	This attribute can only be set when altering a disk group.
	For information about the `ACCESS_CONTROL.ENABLED` attribute, see "Setting Disk Group Attributes for Oracle ASM File Access Control".
- ACCESS\_CONTROL.UMASK
	This attribute can only be set when altering a disk group.
	For information about the `ACCESS_CONTROL.UMASK` attribute, see "Setting Disk Group Attributes for Oracle ASM File Access Control".
- AU\_SIZE
	This attribute can only be set when creating a disk group.
	For information about allocation unit size and extents, see ["Allocation Units"](asmcon.md), ["Extents"](asmcon.md), and "Specifying the Allocation Unit Size". For an example of the use of the `AU_SIZE` attribute, see Example 4-1, "Creating the DATA disk group".
- CELL.SMART\_SCAN\_CAPABLE
	This attribute is only applicable to Oracle Exadata storage.
	See Also:
	Oracle Exadata documentation
- COMPATIBLE.ASM
	For information about the `COMPATIBLE.ASM` attribute, see "COMPATIBLE.ASM".
- COMPATIBLE.RDBMS
	For information about the `COMPATIBLE.RDBMS` attribute, see "COMPATIBLE.RDBMS".
- COMPATIBLE.ADVM
	For information about the `COMPATIBLE.ADVM` attribute, see "COMPATIBLE.ADVM" and ["Overview of Oracle ASM Dynamic Volume Manager"](asmfilesystem.md).
- CONTENT.TYPE
	The `CONTENT.TYPE` attribute identifies the disk group type: `data`, `recovery`, or `system`. The type value determines the distance to the nearest neighbor disk in the failure group where Oracle ASM mirrors copies of the data. The default value is `data` which specifies a distance of 1 to the nearest neighbor disk. A value of `recovery` specifies a distance of 3 to the nearest neighbor disk and a value of `system` specifies a distance of 5.
	The attribute can be specified when creating or altering a disk group. If `CONTENT.TYPE` attribute is set or changed using `ALTER` `DISKGROUP`, then the new configuration does not take effect until a disk group rebalance is explicitly run.
	The `CONTENT.TYPE` attribute is only valid for disk groups that are set to normal or high redundancy. The `COMPATIBLE.ASM` attribute must be set to `11.2.0.3` or higher to enable the `CONTENT.TYPE` attribute for the disk group.
	The attribute can be set with SQL, ASMCMD, or ASMCA. For example:
	```
	SQL> CREATE DISKGROUP data NORMAL REDUNDANCY
	        FAILGROUP controller1 DISK
	        '/devices/diska1' NAME diska1,
	...
	        ATTRIBUTE 
	        'compatible.asm' = '11.2.0.3', 
	        'content.type' = 'recovery',
	...
	SQL> ALTER DISKGROUP data SET ATTRIBUTE 'content.type' = 'data';
	```
	This attribute is primarily intended for use with Oracle Exadata storage.
	See Also:
	Oracle Exadata documentation
- DISK\_REPAIR\_TIME
	This attribute can only be set when altering a disk group.
	For information about the `DISK_REPAIR_TIME` attribute, see "Oracle ASM Fast Mirror Resync".
- IDP.BOUNDARY and IDP.TYPE
	These attributes are intended for use with Oracle Exadata storage.
	See Also:
	Oracle Exadata documentation
- SECTOR\_SIZE
	This attribute can only be set when creating a disk group.
	For information about the `SECTOR_SIZE` attribute, see "Specifying the Sector Size for Drives".
- STORAGE.TYPE
	The `STORAGE.TYPE` disk group attribute specifies the type of the disks in the disk group. The possible values are `AXIOM`, `ZFSSA`, and `OTHER`. If the attribute is set to `AXIOM` or `ZFSSA`, then all disks in the disk group must be of that type. If the attribute is set to `OTHER`, then any types of disks can be in the disk group.
	If the `STORAGE.TYPE` disk group attribute is set to `AXIOM` or `ZFSSA`, then functionality for Hybrid Columnar Compression (HCC) can be enabled for Pillar Axiom or ZFS storage.
	Note:
	ZFS storage must be added through Direct NFS (dNFS) and Pillar Axiom storage must be added as SCSI/Fiber Channel.
	To set the `STORAGE.TYPE` attribute, the `COMPATIBLE.ASM` and `COMPATIBLE.RDBMS` disk group attributes must be set to `11.2.0.3` or higher. For information about disk group compatibility attributes, refer to "Disk Group Compatibility".
	The `STORAGE.TYPE` attribute can be set when creating a disk group or when altering a disk group. The attribute cannot be set when clients are connected to the disk group. For example, the attribute cannot be set when an Oracle ADVM volume is enabled on the disk group.
	The attribute is not visible in the `V$ASM_ATTRIBUTE` view or with the ASMCMD `lsattr` command until the attribute has been set.
	See Also:
	[Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/tablecls.htm#CNCPT89198) for more information about Hybrid Columnar Compression. Hybrid Columnar Compression is a feature of certain Oracle storage systems.

In addition to the disk group attributes listed in this section, template attributes are also assigned to a disk group. For information about template attributes, see ["Managing Disk Group Templates"](asmfiles.md).

You can display disk group attributes with the `V$ASM_ATTRIBUTE` view and the ASMCMD `lsattr` command. For an example of the use of the `V$ASM_ATTRIBUTE` view, see [Example 6-1](asmviews.md). For information about the `lsattr` command, see ["lsattr"](asm_util004.md).

## Creating Disk Groups

This section contains information about creating disk groups. You can use the `CREATE` `DISKGROUP` SQL statement to create a disk group.

This section contains the following topics:

- Using the CREATE DISKGROUP SQL Statement
- Example: Creating a Disk Group
- Creating Disk Groups for a New Oracle Installation
- Specifying the Allocation Unit Size
- Specifying the Sector Size for Drives
- Oracle Cluster Registry and Voting Files in Oracle ASM Disk Groups

### Using the CREATE DISKGROUP SQL Statement

The [`CREATE DISKGROUP`](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_5008.htm#SQLRF01114) SQL statement is used to create disk groups. When creating a disk group, you:

- Assign a unique name to the disk group.
	The specified disk group name is not case sensitive and is always converted to uppercase when stored internally.
	Note:
	Oracle does not recommend using identifiers for database object names that must be quoted. While these quoted identifiers may be valid as names in the SQL CREATE statement, such as `CREATE` `DISKGROUP` " `1DATA` ", the names may not be valid when using other tools that manage the database object.
- Specify the redundancy level of the disk group.
	For Oracle ASM to mirror files, specify the redundancy level as `NORMAL REDUNDANCY` (2-way mirroring by default for most file types) or `HIGH REDUNDANCY` (3-way mirroring for all files). Specify `EXTERNAL REDUNDANCY` if you do not want mirroring by Oracle ASM. For example, you might choose `EXTERNAL REDUNDANCY` to use storage array protection features.
	After a disk group is created, you cannot alter the redundancy level of the disk group. To change the redundancy level, you must create another disk group with the appropriate redundancy and then move the files to the new disk group.
	Oracle recommends that you create failure groups of equal size to maintain space balance and even distribution of mirror data.
	For more information about redundancy levels, refer to "Mirroring, Redundancy, and Failure Group Options".
- Specify the disks that are to be formatted as Oracle ASM disks belonging to the disk group.
	The disks can be specified using operating system dependent wildcard characters in search strings that Oracle ASM then uses to find the disks. You can specify names for the disks with the `NAME` clause or use the system-generated names.
- Optionally specify the disks as belonging to specific failure groups.
	For information about failure groups, refer to ["Understanding Oracle ASM Concepts"](asmcon.md) and "Mirroring, Redundancy, and Failure Group Options".
- Optionally specify the type of failure group.
	For information about `QUORUM` and `REGULAR` failure groups, refer to "Oracle Cluster Registry and Voting Files in Oracle ASM Disk Groups".
- Optionally specify disk group attributes, such as software compatibility or allocation unit size.

Oracle ASM programmatically determines the size of each disk. If for some reason this is not possible, or to restrict the amount of space used on a disk, you can specify a `SIZE` clause for each disk. Oracle ASM creates operating system–independent names for the disks in a disk group that you can use to reference the disks in other SQL statements. Optionally, you can provide your own name for a disk using the `NAME` clause. Disk names are available in the `V$ASM_DISK` view.

Note:

A disk cannot belong to multiple disk groups.

The Oracle ASM instance ensures that any disk in a newly created disk group is addressable and is not currently a member of another disk group. You must use `FORCE` only when adding a disk that was dropped with `FORCE`. If a disk is dropped with `NOFORCE`, then you can add it with `NOFORCE`. For example, a disk might have failed and was dropped from its disk group. After the disk is repaired, it is no longer part of any disk group, but Oracle ASM still recognizes that the disk had been a member of a disk group. You must use the `FORCE` flag to include the disk in a new disk group. In addition, the disk must be addressable, and the original disk group must not be mounted. Otherwise, the operation fails.

Note:

Use caution when using the `FORCE` option to add a previously used disk to a disk group; you might cause another disk group to become unusable.

The `CREATE DISKGROUP` statement mounts the disk group for the first time, and adds the disk group name to the `ASM_DISKGROUPS` initialization parameter if a server parameter file is being used. If a text initialization parameter file is being used and you want the disk group to be automatically mounted at instance startup, then you must remember to add the disk group name to the `ASM_DISKGROUPS` initialization parameter before you shut down and restart the Oracle ASM instance. You can also create disk groups with Oracle Enterprise Manager. Refer to ["Creating Disk Groups"](asm_em.md).

See Also:

The [`CREATE DISKGROUP`](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_5008.htm#SQLRF01114) SQL statement in the [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_5008.htm#SQLRF01114)

### Example: Creating a Disk Group

The following examples assume that the `ASM_DISKSTRING` initialization parameter is set to the ' `/devices/*` ' string. Oracle ASM disk discovery identifies disks in the `/devices` directory, including the following disks:

Controller 1:

  
`/devices/diska1`  
`/devices/diska2`  
`/devices/diska3`  
`/devices/diska4`  
  
Controller 2:  
`/devices/diskb1`  
`/devices/diskb2`  
`/devices/diskb3`  
`/devices/diskb4`  

The SQL statement in Example 4-1 creates a disk group named `data` with normal redundancy consisting of two failure groups `controller1` or `controller2` with four disks in each failure group. The `data` disk group is typically used to store database data files.

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
    'compatible.asm' = '11.2', 
    'compatible.rdbms' = '11.2',
    'compatible.advm' = '11.2';
```

In Example 4-1, the `NAME` clauses enable you to explicitly assign names to the disks rather than the default system-generated names. The system-generated names are in the form `diskgroup_nnnn`, where `nnnn` is the disk number for the disk in the disk group. For ASMLib disks, the disk name defaults to the ASMLib name that is the user label of the disk; for example, `mydisk` is the default Oracle ASM disk name for `ORCL:mydisk`.

When creating the disk group in Example 4-1, the values of following disk group attributes were explicitly set:

- `AU_SIZE`
	Specifies the size of the allocation unit for the disk group. For information about allocation unit size and extents, see ["Extents"](asmcon.md).
	You can view the value of the `AU_SIZE` disk group attribute in the `ALLOCATION_UNIT_SIZE` column of the `V$ASM_DISKGROUP` view.
- `COMPATIBLE`.`ASM`
	Determines the minimum software version for any Oracle ASM instance that uses a disk group. For information about the `COMPATIBLE.ASM` attribute, see "COMPATIBLE.ASM".
- `COMPATIBLE`.`RDBMS`
	Determines the minimum software version for any database instance that uses a disk group. For information about the `COMPATIBLE.RDBMS` attribute, see "COMPATIBLE.RDBMS".
- `COMPATIBLE`.`ADVM`
	Determines whether the disk group can contain Oracle ASM volumes. For information about the `COMPATIBLE.ADVM` attribute, see "COMPATIBLE.ADVM".

In Example 4-2, the `fra` disk group (typically created for the fast recovery area) is created with the default disk group attribute values. Names are not specified for the Oracle ASM disks and failure groups are not explicitly specified. This example assumes that `diskc1` through `diskc9` are present in the `/devices` directory.

Example 4-2 Creating the FRA disk group

```
CREATE DISKGROUP fra NORMAL REDUNDANCY
  DISK '/devices/diskc*';
```

See Also:

For information about using ASMLib when creating disk groups, refer to the Oracle ASMLib page on the Oracle Technology Network Web site at `http://www.oracle.com/technetwork/topics/linux/asmlib/index-101839.html`

### Creating Disk Groups for a New Oracle Installation

This section describes the basic procedure to follow when creating disk groups during a new installation of Oracle Restart and Oracle Database. This information also applies to an Oracle Grid Infrastructure installation.

The procedure assumes that the `data` disk group is used for the storage of the database data files and the `fra` disk group is used for storage of the fast recovery area files. Detailed information about installation with Oracle Universal Installer (OUI) and database creation with Database Configuration Assistant (DBCA) is available in the installation guides for your specific operating system.

1. Install Oracle Restart with OUI, following the screen prompts.
	During the installation, create the `data` disk group for storing database files such as the data and control files.
	This OUI process is similar to creating a disk group with Oracle ASM Configuration Assistant (ASMCA). For information about using ASMCA to create disk groups, see ["Managing Disk Groups with Oracle ASM Configuration Assistant"](asmca.md).
	Note that the `data` disk group is the disk group used for storing Oracle Cluster Registry (OCR) and voting files in an Oracle Grid Infrastructure installation. See "Oracle Cluster Registry and Voting Files in Oracle ASM Disk Groups"
2. After Oracle Restart is installed, use ASMCA to create the `fra` disk group for storing the fast recovery area files.
	Create the `fra` disk group to hold the fast recovery area files.
	At this time, you can also update the `data` disk group if necessary. For information about using ASMCA to create or alter disk groups, see ["Managing Disk Groups with Oracle ASM Configuration Assistant"](asmca.md).
	You can also create the `fra` disk group with SQL\*Plus or ASMCMD commands run from the Oracle Restart home. For information, see "Using the CREATE DISKGROUP SQL Statement" and ["mkdg"](asm_util004.md).
	See Also:
	- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmconfb.htm#BRADV8183) for information about configuring the fast recovery area
	- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/create.htm#ADMIN11103) for information about specifying a fast recovery area
3. Install the Oracle Database software with OUI, following the screen prompts.
4. After the database software has been installed, run DBCA to create a database, following the screen prompts.
	During the creation of the database, make the appropriate selections to use Oracle ASM for storage of data files and fast recovery area files. When prompted:
	- Store database data files in the `data` disk group
		- Store fast recovery area files in the `fra` disk group

See Also:

- [Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for your operating system for detailed information about installation of Oracle Grid Infrastructure and Oracle Restart
- [Oracle Database Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for your operating system for detailed information about installation of an Oracle Database

### Specifying the Allocation Unit Size

Oracle recommends that the allocation unit (AU) size for a disk group be set to 4 megabytes (MB). In addition to this AU size recommendation, the operating system (OS) I/O size should be set to the largest possible size.

Some benefits of a 4 MB allocation unit are:

- Increased I/O through the I/O subsystem if the I/O size is increased to the AU size.
- Reduced SGA size to manage the extent maps in the database instance.
- Faster datafile initialization if the I/O size is increased to the AU size.
- Increased file size limits.
- Reduced database open time.

The allocation unit size is specified with the disk group attribute `AU_SIZE`. The AU size cannot be altered after a disk group is created. Example 4-1 shows how the `AU_SIZE` is specified with the `CREATE` `DISKGROUP` SQL statement.

### Specifying the Sector Size for Drives

You can use the optional `SECTOR_SIZE` disk group attribute with the `CREATE` `DISKGROUP` SQL statement to specify disks with the sector size set to the value of `SECTOR_SIZE` for the disk group. Oracle ASM provides support for 4 KB sector disk drives without negatively affecting performance. The `SECTOR_SIZE` disk group attribute can be set only during disk group creation.

The values for `SECTOR_SIZE` can be set to 512, 4096, or 4K if the disks support those values. The default value is platform dependent. The `COMPATIBLE.ASM` and `COMPATIBLE.RDBMS` disk group attributes must be set to 11.2 or higher to set the sector size to a value other than the default value.

Note:

Oracle Automatic Storage Management Cluster File System (Oracle ACFS) does not support 4 KB sector drives. There is a performance penalty for Oracle ACFS when using 4 KB sector disk drives in 512 sector emulation mode.

The following validations apply to the sector size disk group attribute.

- Oracle ASM prevents disks of different sector sizes from being added to the same disk group. This validation occurs during `CREATE` `DISKGROUP`, `ALTER` `DISKGROUP` `ADD` `DISK`, and `ALTER` `DISKGROUP` `MOUNT` operations.
- If the `SECTOR_SIZE` attribute is explicitly specified when creating a disk group, then Oracle ASM attempts to verify that all disks discovered through disk search strings have a sector size equal to the specified value. If one or more disks were found to have a sector size different from the specified value, or if Oracle ASM was not able to verify a disk sector size, then the create operation fails.
	Oracle ASM also attempts to verify disk sector size during the mount operation and the operation fails if one or more disks have a sector size different than the value of the `SECTOR_SIZE` attribute.
- If the `SECTOR_SIZE` attribute is not specified when creating a disk group and Oracle ASM can verify that all discovered disks have the same sector value, then that value is assumed for the disk group sector size that is created. If the disks have different sector sizes, the create operation fails.
- When new disks are added to an existing disk group using the `ALTER` `DISKGROUP`.. `ADD` `DISK` SQL statement, you must ensure that the new disks to be added have the same value as the `SECTOR_SIZE` disk group attribute. If the new disks have different sector sizes, the alter operation fails.
- You can determine the sector size value that has either been assumed or explicitly set for a successful disk group creation by querying the `V$ASM_ATTRIBUTE` view or run the ASMCMD `lsattr` command. You can also query the `SECTOR_SIZE` column in the `V$ASM_DISKGROUP` view.
	```
	SQL> SELECT name, value FROM V$ASM_ATTRIBUTE 
	     WHERE name = 'sector_size' AND group_number = 1;
	NAME                        VALUE
	--------------------------- -----------------------
	sector_size                 512
	SQL> SELECT group_number, sector_size FROM V$ASM_DISKGROUP 
	     WHERE group_number = 1;
	GROUP_NUMBER SECTOR_SIZE
	------------ -----------
	           1         512
	```
- Not all disks support all of the possible `SECTOR_SIZE` values. The sector size attribute setting must be compatible with the physical hardware.

As shown in Example 4-3, you can use the `SECTOR_SIZE` attribute with the `CREATE` `DISKGROUP` SQL statement to specify the sector size of the disk drive on which the Oracle ASM disk group is located.

Example 4-3 Creating a disk group of 4K sector size

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
ATTRIBUTE 'compatible.asm' = '11.2', 'compatible.rdbms' = '11.2',
          'sector_size'='4096';
```

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_5008.htm#SQLRF01114) for information about the disk group attributes and the [`CREATE DISKGROUP`](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_5008.htm#SQLRF01114) SQL statement
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/clauses004.htm#SQLRF01602) for information about the `BLOCKSIZE` keyword
- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_part.htm#REFRN003) for details about the `V$ASM_ATTRIBUTE` and `V$ASM_DISKGROUP` views

### Oracle Cluster Registry and Voting Files in Oracle ASM Disk Groups

You can store Oracle Cluster Registry (OCR) and voting files in Oracle ASM disk groups. The voting files and OCR are two important components of Oracle Clusterware.

Voting files manage information about node membership. OCR is a system that manages cluster and Oracle Real Application Clusters (Oracle RAC) database configuration information. A quorum failure group is a special type of failure group and disks in these failure groups do not contain user data. A quorum failure group is not considered when determining redundancy requirements in respect to storing user data. However, a quorum failure group counts when mounting a disk group. For information about failure groups, see "Oracle ASM Failure Groups".

You can manage and monitor OCR and voting files with the following:

- The CRSCTL and `ocrconfig` command-line tools
	The CRSCTL and `ocrconfig` commands enable the placement of OCR storage and Cluster Synchronization Services (CSS) voting files inside the disk groups managed by Oracle ASM.
- `CREATE` / `ALTER` `DISKGROUP` SQL Statements
	The SQL keywords `QUORUM` and `REGULAR` enable the specification of disk and failure groups when creating or altering disk groups.
	See Example 4-4.
- `V$ASM` views
	The `FAILGROUP_TYPE` column in both the `V$ASM_DISK` and `V$ASM_DISK_STAT` views specifies failure group type. The value for this column is `REGULAR` for regular failure groups and `QUORUM` for quorum failure groups.
	The `VOTING_FILE` column in both the `V$ASM_DISK` and `V$ASM_DISK_STAT` views specifies whether a disk contains a voting file. The value for this column is either `Y` if the disk contains a voting file or `N` if not.
	Note that the value of `USABLE_FILE_MB` in `V$ASM_DISKGROUP` and `V$ASM_DISKGROUP_STAT` does not consider any free space that is present in `QUORUM` disks because that space is not available for client data files.
	See ["Views Containing Oracle ASM Disk Group Information"](asmviews.md).

The `QUORUM` and `REGULAR` keywords provide an additional qualifier for failure group or disk specifications when creating or altering a disk group. `QUORUM` disks (or disks in `QUORUM` failure groups) cannot have client data files, whereas `REGULAR` disks (or disks in non-quorum failure groups) have no such restriction.

You can use these keywords before the keyword `FAILGROUP` if a failure group is being explicitly specified. If the failure group is implicitly implied, you can use these keywords (`QUORUM` / `REGULAR`) before the keyword `DISK`. When failure groups are explicitly specified, it is an error to specify these keywords (`QUORUM` / `REGULAR`) immediately before the keyword `DISK`. `REGULAR` is the default failure group type.

When performing operations on existing disks or failure groups, the qualifier specified in the SQL must match the qualifier that was specified when the disks or failure groups were added to the disk group.

Example 4-4 shows the creation of a disk group with a `QUORUM` failure group. For Oracle Clusterware files a minimum of three disk devices or three failure groups is required with a normal redundancy disk group. A `QUORUM` failure group is not considered when determining redundancy requirements in respect to storing user data.

The `COMPATIBLE.ASM` disk group compatibility attribute must be set to `11.2` or greater to store OCR or voting files in a disk group.

Example 4-4 Using the QUORUM keyword

```
CREATE DISKGROUP ocr_data NORMAL REDUNDANCY
   FAILGROUP fg1 DISK '/devices/diskg1'
   FAILGROUP fg2 DISK '/devices/diskg2'
   QUORUM FAILGROUP fg3 DISK '/devices/diskg3'
   ATTRIBUTE 'compatible.asm' = '11.2.0.0.0';
```

See Also:

- [Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for information about configuring voting files and Oracle Cluster Registry (OCR)
- [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/votocr.htm#CWADD833) for information about administering voting files and Oracle Cluster Registry (OCR) using CRSCTL and `ocrconfig` commands
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm) for information about the [`CREATE DISKGROUP`](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_5008.htm#SQLRF01114) and [`ALTER DISKGROUP`](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_1007.htm#SQLRF01113) SQL statements
- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_part.htm#REFRN003) for details about the `V$ASM` \* dynamic performance views

## Altering Disk Groups

You can use the [`ALTER` `DISKGROUP`](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_1007.htm#SQLRF01113) SQL statement to alter a disk group configuration. You can add, resize, or drop disks while the database remains online. Whenever possible, multiple operations in a single `ALTER` `DISKGROUP` statement are recommended. Grouping operations in a single `ALTER` `DISKGROUP` statement can reduce rebalancing operations.

Oracle ASM automatically rebalances when the configuration of a disk group changes. By default, the `ALTER` `DISKGROUP` statement does not wait until the operation is complete before returning. Query the `V$ASM_OPERATION` view to monitor the status of this operation.

Use the `REBALANCE` `WAIT` clause to cause the `ALTER` `DISKGROUP` statement processing to wait until the rebalance operation is complete before returning. This is especially useful in scripts. The statement also accepts a `REBALANCE` `NOWAIT` clause that invokes the default behavior of conducting the rebalance operation asynchronously in the background.

You can interrupt a rebalance running in wait mode by typing `CTRL-C` on most platforms. This causes the statement to return immediately with the message `ORA-01013: user requested cancel of current operation`, and then to continue the operation asynchronously. Typing `CTRL-C` does not cancel the rebalance operation or any disk add, drop, or resize operations.

To control the speed and resource consumption of the rebalance operation, you can include the `REBALANCE` `POWER` clause in statements that add, drop, or resize disks. Refer to "Manually Rebalancing Disk Groups" for more information about this clause.

This section contains the following topics:

- Managing Volumes in a Disk Group
- Adding Disks to a Disk Group
- Dropping Disks from Disk Groups
- Intelligent Data Placement
- Resizing Disks in Disk Groups
- Undropping Disks in Disk Groups
- Manually Rebalancing Disk Groups
- Tuning Rebalance Operations

See Also:

The [`ALTER DISKGROUP`](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_1007.htm#SQLRF01113) SQL statement in the [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_1007.htm#SQLRF01113)

### Managing Volumes in a Disk Group

You can create an Oracle ASM Dynamic Volume Manager (Oracle ADVM) volume in a disk group. The volume device associated with the dynamic volume can then be used to host an Oracle ACFS file system.

The compatibility parameters `COMPATIBLE.ASM` and `COMPATIBLE.ADVM` must be set to 11.2 or higher for the disk group. See "Disk Group Compatibility Attributes".

The `ALTER` `DISKGROUP` `VOLUME` SQL statements enable you to manage Oracle ADVM volumes, including the functionality to add, modify, resize, disable, enable, and drop volumes. The following are examples of the `ALTER` `DISKGROUP` `VOLUME` statement.

Example 4-5 Managing volumes with ALTER DISKGROUP VOLUME statements

```
SQL> ALTER DISKGROUP data ADD VOLUME volume1 SIZE 10G;
Diskgroup altered.

SQL> ALTER DISKGROUP data RESIZE VOLUME volume1 SIZE 15G;
Diskgroup altered.

SQL> ALTER DISKGROUP data DISABLE VOLUME volume1;
Diskgroup altered.

SQL> ALTER DISKGROUP data ENABLE VOLUME volume1;
Diskgroup altered.

SQL> ALTER DISKGROUP ALL DISABLE VOLUME ALL;
Diskgroup altered.

SQL> ALTER DISKGROUP data DROP VOLUME volume1;
Diskgroup altered.
```

If the volume is hosting an Oracle ACFS file system, then you cannot resize that volume with the SQL `ALTER` `DISKGROUP` statement. Instead you must use the `acfsutil` `size` command. For information, see ["acfsutil size"](asmfs_util010.md).

For information about Oracle ADVM, see ["Overview of Oracle ASM Dynamic Volume Manager"](asmfilesystem.md). For information about managing Oracle ADVM volumes with ASMCMD, see ["ASMCMD Volume Management Commands"](asm_util007.md). For information about managing Oracle ADVM volumes with ASMCA, see ["Managing Oracle ADVM Volumes with Oracle ASM Configuration Assistant"](asmca.md). For information about managing Oracle ADVM volumes with Oracle Enterprise Manager, see ["Managing Oracle ACFS with Oracle Enterprise Manager"](asmfs_em.md).

See Also:

The [`ALTER DISKGROUP`](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_1007.htm#SQLRF01113) SQL statement in the [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_1007.htm#SQLRF01113)

### Adding Disks to a Disk Group

You can use the `ADD` clause of the [`ALTER DISKGROUP`](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_1007.htm#SQLRF01113) statement to add a disk or a failure group to a disk group. You can use the same syntax with the `ALTER DISKGROUP` statement that you use to add a disk or failure group with the `CREATE` `DISKGROUP` statement. For an example of the `CREATE` `DISKGROUP` SQL statement, refer to Example 4-1. After you add new disks, the new disks gradually begin to accommodate their share of the workload as rebalancing progresses.

Oracle ASM behavior when adding disks to a disk group is best illustrated through "Adding Disks to a Disk Group with SQL Statements". You can also add disks to a disk group with Oracle Enterprise Manager, described in ["Adding Disks to Disk Groups"](asm_em.md).

#### Adding Disks to a Disk Group with SQL Statements

The statements presented in this example demonstrate the interactions of disk discovery with the `ADD` `DISK` operation.

Assume that disk discovery identifies the following disks in directory `/devices`:

  
`/devices/diska1` -- member of `data1`  
`/devices/diska2` -- member of `data1`  
`/devices/diska3` -- member of `data1`  
`/devices/diska4` -- member of `data1`  
`/devices/diska5` -- candidate disk  
`/devices/diska6` -- candidate disk  
`/devices/diska7` -- candidate disk  
`/devices/diska8` -- candidate disk  
  
`/devices/diskb1` -- member of `data1`  
`/devices/diskb2` -- member of `data1`  
`/devices/diskb3` -- member of `data1`  
`/devices/diskb4` -- member of `data2`  
  
`/devices/diskc1` -- member of `data2`  
`/devices/diskc2` -- member of `data2`  
`/devices/diskc3` -- member of `data3`  
`/devices/diskc4` -- candidate disk  
  
`/devices/diskd1` -- candidate disk  
`/devices/diskd2` -- candidate disk  
`/devices/diskd3` -- candidate disk  
`/devices/diskd4` -- candidate disk  
`/devices/diskd5` -- candidate disk  
`/devices/diskd6` -- candidate disk  
`/devices/diskd7` -- candidate disk  
`/devices/diskd8` -- candidate disk  

You can query the `V$ASM_DISK` view to display the status of Oracle ASM disks. See ["Views Containing Oracle ASM Disk Group Information"](asmviews.md).

The following statement would fail because `/devices/diska1` - `/devices/diska4` already belong to the disk group `data1`.

```
ALTER DISKGROUP data1 ADD DISK
     '/devices/diska*';
```

The following statement successfully adds disks `/devices/diska5` through `/devices/diska8` to `data1`. Because no `FAILGROUP` clauses are included in the `ALTER DISKGROUP` statement, each disk is assigned to its own failure group. The `NAME` clauses assign names to the disks, otherwise they would have been assigned system-generated names.

```
ALTER DISKGROUP data1 ADD DISK
     '/devices/diska5' NAME diska5,
     '/devices/diska6' NAME diska6,
     '/devices/diska7' NAME diska7,
     '/devices/diska8' NAME diska8;
```

The following statement would fail because the search string matches disks that are contained in other disk groups. Specifically, `/devices/diska4` belongs to disk group `data1` and `/devices/diskb4` belongs to disk group `data2`.

```
ALTER DISKGROUP data1 ADD DISK
     '/devices/disk*4';
```

The following statement would successfully add `/devices/diskd1` through `/devices/diskd8` to disk group `data1`. This statement runs with a rebalance power of 5, and does not return until the rebalance operation is complete.

```
ALTER DISKGROUP data1 ADD DISK
      '/devices/diskd*'
       REBALANCE POWER 5 WAIT;
```

If `/devices/diskc3` was previously a member of a disk group that no longer exists, then you could use the `FORCE` option to add the disk as a member of another disk group. For example, the following use of the `FORCE` clause enables `/devices/diskc3` to be added to `data2`, even though it is a current member of `data3`. For this statement to succeed, `data3` cannot be mounted.

```
ALTER DISKGROUP data2 ADD DISK
     '/devices/diskc3' FORCE;
```

### Dropping Disks from Disk Groups

To drop disks from a disk group, use the `DROP` `DISK` clause of the [`ALTER DISKGROUP`](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_1007.htm#SQLRF01113) statement. You can also drop all of the disks in specified failure groups using the `DROP` `DISKS` `IN` `FAILGROUP` clause.

When a disk is dropped, the disk group is rebalanced by moving all of the file extents from the dropped disk to other disks in the disk group. A drop disk operation might fail if not enough space is available on the other disks. The best approach is to perform both the add and drop operation with the same `ALTER` `DISKGROUP` statement. This has the benefit of rebalancing data extents only one time and ensuring that there is enough space for the rebalance operation to succeed.

Caution:

The `ALTER` `DISKGROUP``...``DROP` `DISK` SQL statement returns to SQL prompt before the drop and rebalance operations are complete. Do not reuse, remove, or disconnect the dropped disk until the `HEADER_STATUS` column for this disk in the `V$ASM_DISK` view changes to `FORMER`. You can query the `V$ASM_OPERATION` view to determine the amount of time remaining for the drop/rebalance operation to complete. For more information, refer to the [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_1007.htm#SQLRF01113) and the [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1031.htm#REFRN30173).

If you specify the `FORCE` clause for the drop operation, the disk is dropped even if Oracle ASM cannot read or write to the disk. You cannot use the `FORCE` flag when dropping a disk from an external redundancy disk group.

Caution:

A `DROP` `FORCE` operation leaves data at reduced redundancy until the subsequent rebalance operation completes. This increases your exposure to data loss if there is a subsequent disk failure during rebalancing. Use `DROP` `FORCE` with caution.

You can also drop disks from a disk group with Oracle Enterprise Manager. See ["Dropping Disks from Disk Groups"](asm_em.md).

The statements in Example 4-6 demonstrate how to drop disks from the disk group `data1` described in "Adding Disks to a Disk Group with SQL Statements". The first example drops `diska5` from disk group `data1`. The second example drops `diska5` from disk group `data1`, and also illustrates how multiple actions are possible with one `ALTER DISKGROUP` statement.

Example 4-6 Dropping disks from disk groups

```
ALTER DISKGROUP data1 DROP DISK diska5;

ALTER DISKGROUP data1 DROP DISK diska5
     ADD FAILGROUP failgrp1 DISK '/devices/diska9' NAME diska9;
```

### Intelligent Data Placement

Intelligent Data Placement enables you to specify disk regions on Oracle ASM disks for best performance. Using the disk region settings, you can ensure that frequently accessed data is placed on the outermost (hot) tracks which have greater speed and higher bandwidth. In addition, files with similar access patterns are located physically close, reducing latency. Intelligent Data Placement also enables the placement of primary and mirror extents into different hot or cold regions.

Intelligent Data Placement settings can be specified for a file or in disk group templates. The disk region settings can be modified after the disk group has been created. The disk region setting can improve I/O performance by placing more frequently accessed data in regions furthest from the spindle, while reducing your cost by increasing the usable space on a disk.

Intelligent Data Placement works best for the following:

- Databases with data files that are accessed at different rates. A database that accesses all data files in the same way is unlikely to benefit from Intelligent Data Placement.
- Disk groups that are more than 25% full. If the disk group is only 25% full, the management overhead is unlikely to be worth any benefit.
- Disks that have better performance at the beginning of the media relative to the end. Because Intelligent Data Placement leverages the geometry of the disk, it is well suited to JBOD (just a bunch of disks). In contrast, a storage array with LUNs composed of concatenated volumes masks the geometry from Oracle ASM.

The `COMPATIBLE.ASM` and `COMPATIBLE.RDBMS` disk group attributes must be set to 11.2 or higher to use Intelligent Data Placement.

Intelligent Data Placement can be managed with the `ALTER` `DISKGROUP` `ADD` or `MODIFY` `TEMPLATE` SQL statements and the `ALTER` `DISKGROUP` `MODIFY` `FILE` SQL statement.

- The `ALTER` `DISKGROUP` `TEMPLATE` SQL statement includes a disk region clause for setting `hot` / `mirrorhot` or `cold` / `mirrorcold` regions in a template:
	```
	ALTER DISKGROUP data ADD TEMPLATE datafile_hot
	  ATTRIBUTE ( 
	    HOT
	    MIRRORHOT);
	```
- The `ALTER` `DISKGROUP`... `MODIFY` `FILE` SQL statement that sets disk region attributes for `hot` / `mirrorhot` or `cold` / `mirrorcold` regions:
	```
	ALTER DISKGROUP data MODIFY FILE '+data/orcl/datafile/users.259.679156903'
	  ATTRIBUTE ( 
	    HOT
	    MIRRORHOT);
	```
	When you modify the disk region settings for a file, this action applies to new extensions of the file, but existing file contents are not affected until a rebalance operation. To apply the new Intelligent Data Placement policy for existing file contents, you can manually initiate a rebalance. A rebalance operation uses the last specified policy for the file extents. For information on the rebalance operation, see "Manually Rebalancing Disk Groups".

Oracle ASM Configuration Assistant (ASMCA) supports Intelligent Data Placement with template creation during disk group alterations. See ["Managing Disk Groups with Oracle ASM Configuration Assistant"](asmca.md).

Oracle Enterprise Manager supports Intelligent Data Placement from the Templates page launched from the disk group page. See ["Managing Disk Group Templates with Oracle Enterprise Manager"](asm_em.md).

To display information about Intelligent Data Placement regions, see ["Viewing Disk Region Information"](asmviews.md) and ["iostat"](asm_util004.md).

### Resizing Disks in Disk Groups

The `RESIZE` clause of [`ALTER DISKGROUP`](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_1007.htm#SQLRF01113) enables you to perform the following operations:

- Resize all disks in the disk group
- Resize specific disks
- Resize all of the disks in a specified failure group

If you do not specify a new size in the `SIZE` clause, then Oracle ASM uses the size of the disk as returned by the operating system. The new size is written to the Oracle ASM disk header and if the size of the disk is increasing, then the new space is immediately available for allocation. If the size is decreasing, rebalancing must relocate file extents beyond the new size limit to available space below the limit. If the rebalance operation can successfully relocate all extents, then the new size is made permanent, otherwise the rebalance fails.

The following example resizes all of the disks in failure group `failgrp1` of disk group `data1`. If the new size is greater than disk capacity, the statement fails.

Example 4-7 Resizing disks in disk groups

```
ALTER DISKGROUP data1 
     RESIZE DISKS IN FAILGROUP failgrp1 SIZE 100G;
```

### Undropping Disks in Disk Groups

The `UNDROP DISKS` clause of the [`ALTER DISKGROUP`](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_1007.htm#SQLRF01113) statement enables you to cancel all pending drops of disks within disk groups. If a drop disk operation has completed, then this statement cannot be used to restore it. This statement cannot be used to restore disks that are being dropped as the result of a [`DROP DISKGROUP`](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_8013.htm#SQLRF01517) statement, or for disks that are being dropped using the `FORCE` clause.

The following example cancels the dropping of disks from disk group `data1`:

Example 4-8 Undropping disks in disk groups

```
ALTER DISKGROUP data1 UNDROP DISKS;
```

### Manually Rebalancing Disk Groups

You can manually rebalance the files in a disk group using the `REBALANCE` clause of the [`ALTER DISKGROUP`](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_1007.htm#SQLRF01113) statement. This would normally not be required, because Oracle ASM automatically rebalances disk groups when their configuration changes. You might want to do a manual rebalance operation to control the speed of what would otherwise be an automatic rebalance operation.

The `POWER` clause of the `ALTER` `DISKGROUP`... `REBALANCE` statement specifies the degree of parallelism, and thus the speed of the rebalance operation. It can be set to a minimum value of 0 which halts a rebalancing operation until the statement is either implicitly or explicitly re-run. A higher value increases the speed of the rebalance operation.

The default rebalance power is set by the `ASM_POWER_LIMIT` initialization parameter. The range of values for the `POWER` clause is the same for the `ASM_POWER_LIMIT` initialization parameter. For information about the `ASM_POWER_LIMIT` initialization parameter, refer to ["ASM\_POWER\_LIMIT"](asminst.md).

The power level of an ongoing rebalance operation can be changed by entering the rebalance statement with a new level.

The `ALTER DISKGROUP...REBALANCE` command by default returns immediately so that you can run other commands while the rebalance operation takes place asynchronously in the background. You can query the `V$ASM_OPERATION` view for the status of the rebalance operation.

To cause the `ALTER DISKGROUP...REBALANCE` command to wait until the rebalance operation is complete before returning, add the `WAIT` keyword to the `REBALANCE` clause. The wait functionality is especially useful in scripts. The command also accepts a `NOWAIT` keyword, which invokes the default behavior of conducting the rebalance operation asynchronously. You can interrupt a rebalance running in wait mode by typing `CTRL-C` on most platforms. This causes the command to return immediately with the message `ORA-01013: user requested cancel of current operation`, and then continue the rebalance operation asynchronously.

Additional rules for the rebalance operation include the following:

- An ongoing rebalance command is restarted if the storage configuration changes either when you alter the configuration, or if the configuration changes due to a failure or an outage. Furthermore, if the new rebalance fails because of a user error, then a manual rebalance may be required.
- The `ALTER DISKGROUP...REBALANCE` statement runs on a single node even if you are using Oracle Real Application Clusters (Oracle RAC).
- Oracle ASM can perform one disk group rebalance at a time on a given instance. If you have initiated multiple rebalances on different disk groups on a single node, then Oracle processes these operations in parallel on additional nodes if available; otherwise the rebalances are performed serially on the single node. You can explicitly initiate rebalances on different disk groups on different nodes in parallel.
- Rebalancing continues across a failure of the Oracle ASM instance performing the rebalance.
- The `REBALANCE` clause (with its associated `POWER` and `WAIT/NOWAIT` keywords) can also be used in `ALTER DISKGROUP` commands that add, drop, or resize disks.
	Note:
	Oracle restarts the processing of an ongoing rebalance operation if the storage configuration changes. If the next rebalance operation fails because of a user error, then a manual rebalance may be required.

The following example manually rebalances the disk group `data2`. The command does not return until the rebalance operation is complete.

Example 4-9 Manually rebalancing a disk group

```
ALTER DISKGROUP data2 REBALANCE POWER 5 WAIT;
```

For more information about rebalancing operations, refer to "Tuning Rebalance Operations".

### Tuning Rebalance Operations

If the `POWER` clause is not specified in an `ALTER` `DISKGROUP` statement, or when rebalance is implicitly run by adding or dropping a disk, then the rebalance power defaults to the value of the `ASM_POWER_LIMIT` initialization parameter. You can adjust the value of this parameter dynamically.

The higher the power limit, the more quickly a rebalance operation can complete. Rebalancing takes longer with lower power values, but consumes fewer processing and I/O resources which are shared by other applications, such as the database.

Oracle ASM tries to keep a rebalance I/O for each unit of power. Each I/O requires PGA memory for the extent involved in the relocation.

The default value of `1` minimizes disruption to other applications. The appropriate value is dependent on your hardware configuration, performance requirements, and availability requirements.

If a rebalance is in progress because a disk is manually or automatically dropped, then increasing the power of the rebalance shortens the time frame during which redundant copies of that data on the dropped disk are reconstructed on other disks.

The `V$ASM_OPERATION` view provides information for adjusting `ASM_POWER_LIMIT` and the resulting power of rebalance operations. The `V$ASM_OPERATION` view also gives an estimate in the `EST_MINUTES` column of the amount of time remaining for the rebalance operation to complete. You can see the effect of changing the rebalance power by observing the change in the time estimate.

The range of values for the `POWER` clause is the same for the `ASM_POWER_LIMIT` initialization parameter. For information about the `ASM_POWER_LIMIT` initialization parameter, refer to ["ASM\_POWER\_LIMIT"](asminst.md).

For more information about rebalancing disk groups, refer to "Manually Rebalancing Disk Groups".

## Oracle ASM Disk Discovery

Disk discovery is the mechanism used to find the operating system names for disks Oracle ASM can access. It is used to find all the disks that comprise a disk group to be mounted, the disks an administrator wants to add to a disk group, or the disks the administrator might consider adding to a disk group. This section contains the following topics:

- How A Disk is Discovered
- Disk Discovery Rules
- Improving Disk Discovery Time

For additional information about disk discovery and the `ASM_DISKSTRING` initialization parameter, refer to ["ASM\_DISKSTRING"](asminst.md).

### How A Disk is Discovered

When an Oracle ASM instance is initialized, Oracle ASM discovers and examines the contents of all of the disks that are in the paths that you designated with values in the `ASM_DISKSTRING` initialization parameter.

Disk discovery also occurs when you:

- Run the following SQL statements
	- Mount a disk group with `ALTER` `DISKGROUP`... `MOUNT`
		- Online a disk with `ALTER` `DISKGROUP`... `ONLINE` `DISK`
		- Add a disk to a disk group with `CREATE` or `ALTER` `DISKGROUP`...`ADD` `DISK`
		- Resize a disk in a disk group with `ALTER` `DISKGROUP`...`RESIZE` `DISK`
		- Query with `SELECT`... `FROM` `V$ASM_DISKGROUP` or `V$ASM_DISK` views
- Run Oracle Enterprise Manager or Oracle ASM Configuration Assistant (ASMCA) operations that invoke the SQL statements previously listed
- Run ASMCMD commands that perform the same operations as the SQL statements previously listed

After Oracle ASM successfully discovers a disk, the disk appears in the `V$ASM_DISK` view. Disks that belong to a disk group, that is, disks that have a disk group name in the disk header, show a header status of `MEMBER`. Disks that were discovered, but that have not yet been assigned to a disk group, have a status of either `CANDIDATE` or `PROVISIONED`. Disks that previously belonged to a disk group and were dropped cleanly from the disk group have a status of `FORMER`.

The `PROVISIONED` status implies that an additional platform-specific action has been taken by an administrator to make the disk available for Oracle ASM. For example, on Windows computers, the administrator might have used `asmtool` or `asmtoolg` to stamp the disk with a header. On Linux computers, the administrator might have used ASMLib to prepare the disk for Oracle ASM.

Example 4-10 shows a SQL query on `V$ASM_DISK` that displays the header status of a group of disks.

Example 4-10 Querying V$ASM\_DISK for header status

```
SQL> SELECT name, header_status, path FROM V$ASM_DISK 
     WHERE path LIKE '/devices/disk0%'

NAME      HEADER_STATUS PATH
--------- ------------- ---------------------
          FORMER        /devices/disk02
          FORMER        /devices/disk01
          CANDIDATE     /devices/disk07
DISK06    MEMBER        /devices/disk06
DISK05    MEMBER        /devices/disk05
DISK04    MEMBER        /devices/disk04
DISK03    MEMBER        /devices/disk03
7 rows selected.
```

### Disk Discovery Rules

The rules for discovering Oracle ASM disks are as follows:

- Oracle ASM can discover up to 10,000 disks. That is, if more than 10,000 disks match the `ASM_DISKSTRING` initialization parameter, then Oracle ASM discovers only the first 10,000.
- Oracle ASM only discovers disk partitions. Oracle ASM does not discover partitions that include the partition table.
- From the perspective of the installation, candidate disks are those that have the `CANDIDATE`, `PROVISIONED`, or `FORMER` header status. These disks with a `CANDIDATE`, `PROVISIONED`, or `FORMER` status can be added to Oracle ASM disk groups without using the `FORCE` flag.
- When adding a disk, the `FORCE` option must be used if Oracle ASM recognizes that the disk was managed by Oracle. Such a disk appears in the `V$ASM_DISK` view with a status of `FOREIGN`. In this case, you can only add the disk to a disk group by using the `FORCE` keyword.
- `MEMBER` disks can usually be added to a disk group by specifying the `FORCE` flag, if the disks are not part of a currently mounted disk group.

In addition, Oracle ASM identifies the following configuration errors during discovery:

- Multiple paths to the same disk
	In this case, if the disk is part of a disk group, then disk group mount fails. If the disk is being added to a disk group with the `ADD DISK` or `CREATE DISKGROUP` command, then the command fails. To correct the error, adjust the `ASM_DISKSTRING` value so that Oracle ASM does not discover multiple paths to the same disk. Or if you are using multipathing software, then ensure that you include only the pseudo-device name in the `ASM_DISKSTRING` value. See ["Oracle ASM and Multipathing"](asmprepare.md).
- Multiple Oracle ASM disks with the same disk header
	This can be caused by having copied one disk onto another. In this case, the disk group mount operation fails.

### Improving Disk Discovery Time

The value for the `ASM_DISKSTRING` initialization parameter is an operating system–dependent value that Oracle ASM uses to limit the set of paths that the discovery process uses to search for disks. When a new disk is added to a disk group, each Oracle ASM instance that has the disk group mounted must be able to discover the new disk using its `ASM_DISKSTRING`.

In many cases, the default value (`NULL`) is sufficient. Using a more restrictive value might reduce the time required for Oracle ASM to perform discovery, and thus improve disk group mount time or the time for adding a disk to a disk group. Oracle may dynamically change the `ASM_DISKSTRING` before adding a disk so that the new disk is discovered through this parameter.

The default value of `ASM_DISKSTRING` might not find all disks in all situations. If your site is using a third-party vendor ASMLib, then the vendor might have discovery string conventions that you must use for `ASM_DISKSTRING`. In addition, if your installation uses multipathing software, then the software might place pseudo-devices in a path that is different from the operating system default. See ["Oracle ASM and Multipathing"](asmprepare.md) and consult the multipathing vendor documentation for details.

## Managing Capacity in Disk Groups

When Oracle ASM provides redundancy, such as when you create a disk group with `NORMAL` or `HIGH` redundancy, you must have sufficient capacity in each disk group to manage a re-creation of data that is lost after a failure of one or two failure groups. After one or more disks fail, the process of restoring redundancy for all data requires space from the surviving disks in the disk group. If not enough space remains, then some files might end up with reduced redundancy.

Reduced redundancy means that one or more extents in the file are not mirrored at the expected level. For example, a reduced redundancy file in a high redundancy disk group has at least one file extent with two or fewer total copies of the extent instead of three. For unprotected files, data extents could be missing altogether. Other causes of reduced redundancy files are disks running out of space or an insufficient number of failure groups. The `REDUNDANCY_LOWERED` column in the `V$ASM_FILE` view provides information about files with reduced redundancy.

The following guidelines help ensure that you have sufficient space to restore full redundancy for all disk group data after the failure of one or more disks.

- Normal redundancy disk group - It is best to have enough free space in your disk group to tolerate the loss of all disks in one failure group. The amount of free space should be equivalent to the size of the largest failure group.
- High redundancy disk group - It is best to have enough free space to cope with the loss of all disks in two failure groups. The amount of free space should be equivalent to the sum of the sizes of the two largest failure groups.
	Note:
	When you lose multiple disks from multiple failure groups, then you could lose both the primary and the redundant copies of your data. In addition, if you do not have enough capacity to restore redundancy, then Oracle ASM can continue to operate. However, if another disk fails, then the system may not be able to tolerate additional failures.

The `V$ASM_DISKGROUP` view contains the following columns that contain information to help you manage capacity:

- `REQUIRED_MIRROR_FREE_MB` indicates the amount of space that must be available in a disk group to restore full redundancy after the worst failure that can be tolerated by the disk group without adding additional storage. This requirement ensures that there are sufficient failure groups to restore redundancy. Also, this worst failure refers to a permanent failure where the disks must be dropped, not the case where the disks go offline and then back online.
	The amount of space displayed in this column takes the effects of mirroring into account. The value is computed as follows:
	- Normal redundancy disk group with more than two failure groups
		The value is the total raw space for all of the disks in the largest failure group. The largest failure group is the one with the largest total raw capacity. For example, if each disk is in its own failure group, then the value would be the size of the largest capacity disk.
		- High redundancy disk group with more than three failure groups
		The value is the total raw space for all of the disks in the two largest failure groups.
- `USABLE_FILE_MB` indicates the amount of free space, adjusted for mirroring, that is available for new files to restore redundancy after a disk failure. `USABLE_FILE_MB` is computed by subtracting `REQUIRED_MIRROR_FREE_MB` from the total free space in the disk group and then adjusting the value for mirroring. For example, in a normal redundancy disk group where by default the mirrored files use disk space equal to twice their size, if 4 GB of actual usable file space remains, then `USABLE_FILE_MB` equals roughly 2 GB. You can then add a file that is up to 2 GB.
- `TOTAL_MB` is the total usable capacity of a disk group in megabytes. The calculations for data in this column take the disk header overhead into consideration. The disk header overhead depends on the number of Oracle ASM disks and Oracle ASM files. This value is typically about 1% of the total raw storage capacity. For example, if the total LUN capacity provisioned for Oracle ASM is 100 GB, then the value in the `TOTAL_MB` column would be about 99 GB.
- `FREE_MB` is the unused capacity of the disk group in megabytes, without considering any data imbalance. There may be situations where the value in the `FREE_MB` column shows unused capacity but because one Oracle ASM disk is full, database writes fail because of the imbalance in the disk group. Ensure that you initiate a manual rebalance to force even data distribution which results in an accurate presentation of the values in the `FREE_MB` column.
	With fine grain striping using 128 KB, the storage is preallocated to be eight times the AU size. The data file size may appear slightly larger on Oracle ASM than on a local file system because of the preallocation.
	When you use Oracle ASM normal or high redundancy, the disk space utilization becomes more complex to measure because it depends on several variables.
	Note:
	The values in the `TOTAL_MB` and `FREE_MB` columns best describe space usage when you do not configure Oracle ASM mirroring, that is, when you use external redundancy.

The results from the following query show capacity metrics for a normal redundancy disk group that consists of six 1 GB (1024 MB) disks, each in its own failure group:

```
SQL> SELECT name, type, total_mb, free_mb, required_mirror_free_mb, 
     usable_file_mb FROM V$ASM_DISKGROUP;

NAME         TYPE     TOTAL_MB    FREE_MB REQUIRED_MIRROR_FREE_MB USABLE_FILE_MB
------------ ------ ---------- ---------- ----------------------- --------------
DATA         NORMAL       6144       3768                    1024           1372
```

The `REQUIRED_MIRROR_FREE_MB` column shows that 1 GB of extra capacity must be available to restore full redundancy after one or more disks fail. The first three numeric columns in the query results are raw numbers. That is, they do not take redundancy into account. Only the last column is adjusted for normal redundancy. In the query output example for the `data` disk group, the calculation is as follows:

(`FREE_MB` `-` `REQUIRED_MIRROR_FREE_MB`) `/` `2` = `USABLE_FILE_MB`

(`3768` - `1024`) / `2` = `2744` / `2` = `1372`

### Negative Values of USABLE\_FILE\_MB

Due to the relationship between `FREE_MB`, `REQUIRED_MIRROR_FREE_MB`, and `USABLE_FILE_MB`, `USABLE_FILE_MB` can become negative. Although this is not necessarily a critical situation, it does mean that:

- Depending on the value of `FREE_MB`, you may not be able to create new files.
- The next failure might result in files with reduced redundancy.

If `USABLE_FILE_MB` becomes negative, it is strongly recommended that you add more space to the disk group as soon as possible.

## Oracle ASM Mirroring and Disk Group Redundancy

This section contains the following topics:

- Mirroring, Redundancy, and Failure Group Options
- Oracle ASM Recovery from Read and Write I/O Errors
- Oracle ASM Fast Mirror Resync
- Preferred Read Failure Groups

### Mirroring, Redundancy, and Failure Group Options

If you specify mirroring for a file, then Oracle ASM automatically stores redundant copies of the file extents in separate failure groups. Failure groups apply only to normal and high redundancy disk groups. You can define the failure groups for each disk group when you create or alter the disk group.

There are three types of disk groups based on the Oracle ASM redundancy level. Table 4-1 lists the types with their supported and default mirroring levels. The default mirroring levels indicate the mirroring level with which each file is created unless a different mirroring level is designated.

Table 4-1 Mirroring options for Oracle ASM disk group types

| Disk Group Type | Supported Mirroring Levels | Default Mirroring Level |
| --- | --- | --- |
| External redundancy | Unprotected (none) | Unprotected |
| Normal redundancy | Two-way, three-way, unprotected (none) | Two-way |
| High redundancy | Three-way | Three-way |

The redundancy level controls how many disk failures are tolerated without dismounting the disk group or losing data. Each file is allocated based on its own redundancy, but the default comes from the disk group.

The redundancy levels are:

- External redundancy
	Oracle ASM does not provide mirroring redundancy and relies on the storage system to provide RAID functionality. Any write error causes a forced dismount of the disk group. All disks must be located to successfully mount the disk group.
- Normal redundancy
	Oracle ASM provides two-way mirroring by default, which means that all files are mirrored so that there are two copies of every [extent](ostmg_gloss.md). A loss of one Oracle ASM disk is tolerated. You can optionally choose three-way or unprotected mirroring.
	A file specified with `HIGH` redundancy (three-way mirroring) in a `NORMAL` redundancy disk group provides additional protection from a bad disk sector, not protection from a disk failure.
- High redundancy
	Oracle ASM provides triple mirroring by default. A loss of two Oracle ASM disks in different failure groups is tolerated.

If there are not enough online failure groups to satisfy the file mirroring (redundancy attribute value) specified in the disk group file type template, Oracle ASM allocates as many mirrors copies as possible and subsequently allocates the remaining mirrors when sufficient online failure groups are available. For information about specifying Oracle ASM disk group templates, see ["Managing Disk Group Templates"](asmfiles.md).

Failure groups enable the mirroring of metadata and user data. System reliability can diminish if your environment has an insufficient number of failure groups.

This section contains these topics:

- Oracle ASM Failure Groups
- How Oracle ASM Manages Disk Failures
- Guidelines for Using Failure Groups
- Failure Group Frequently Asked Questions

#### Oracle ASM Failure Groups

Failure groups are used to store mirror copies of data. When Oracle ASM allocates an extent for a normal redundancy file, Oracle ASM allocates a primary copy and a secondary copy. Oracle ASM chooses the disk on which to store the secondary copy so that it is in a different failure group than the primary copy. Each copy is on a disk in a different failure group so that the simultaneous failure of all disks in a failure group does not result in data loss.

A failure group is a subset of the disks in a disk group, which could fail at the same time because they share hardware. The failure of common hardware must be tolerated. Four drives that are in a single removable tray of a large JBOD (Just a Bunch of Disks) array should be in the same failure group because the tray could be removed making all four drives fail at the same time. Drives in the same cabinet could be in multiple failure groups if the cabinet has redundant power and cooling so that it is not necessary to protect against failure of the entire cabinet. However, Oracle ASM mirroring is not intended to protect against a fire in the computer room that destroys the entire cabinet.

There are always failure groups even if they are not explicitly created. If you do not specify a failure group for a disk, then Oracle automatically creates a new failure group containing just that disk, except for disk groups containing disks on Oracle Exadata cells.

A normal redundancy disk group must contain at least two failure groups. A high redundancy disk group must contain at least three failure groups. However, Oracle recommends using several failure groups. A small number of failure groups, or failure groups of uneven capacity, can create allocation problems that prevent full use of all of the available storage.

Failure groups can be specified as regular or quorum failure groups. For information about quorum failure groups, see "Oracle Cluster Registry and Voting Files in Oracle ASM Disk Groups".

See Also:

Oracle Exadata documentation for information about Oracle Exadata failure groups

#### How Oracle ASM Manages Disk Failures

Depending on the redundancy level of a disk group and how you define failure groups, the failure of one or more disks could result in either of the following:

- The disks are first taken offline and then automatically dropped. In this case, the disk group remains mounted and serviceable. In addition, because of mirroring, all of the disk group data remains accessible. After the disk drop operation, Oracle ASM performs a rebalance to restore full redundancy for the data on the failed disks.
- The entire disk group is automatically dismounted, which means loss of data accessibility.

#### Guidelines for Using Failure Groups

The following are guidelines for using failure groups:

- Each disk in a disk group can belong to only one failure group.
- Failure groups should all be of the same size. Failure groups of different sizes may lead to reduced availability.
- Oracle ASM requires at least two failure groups to create a normal redundancy disk group and at least three failure groups to create a high redundancy disk group.

#### Failure Group Frequently Asked Questions

This section discusses frequently asked questions about failure group under the following topics:

- How Many Failure Groups Should I Create?
- How are Multiple Failure Groups Recovered after Simultaneous Failures?
- When Should External, Normal, or High Redundancy Be Used?

How Many Failure Groups Should I Create?

Choosing the number of failure groups to create depends on the types of failures that must be tolerated without data loss. For small numbers of disks, such as fewer than 20, it is usually best to use the default failure group creation that puts every disk in its own failure group.

Using the default failure group creation for small numbers of disks is also applicable for large numbers of disks where your main concern is disk failure. For example, a disk group might be configured from several small modular disk arrays. If the system must continue operating when an entire modular array fails, then a failure group should consist of all of the disks in one module. If one module fails, then all of the data on that module is relocated to other modules to restore redundancy. Disks should be placed in the same failure group if they depend on a common piece of hardware whose failure must be tolerated with no loss of availability.

How are Multiple Failure Groups Recovered after Simultaneous Failures?

A simultaneous failure can occur if there is a failure of a piece of hardware used by multiple failure groups. This type of failure usually forces a dismount of the disk group if all disks are unavailable.

When Should External, Normal, or High Redundancy Be Used?

Oracle ASM mirroring runs on the database server and Oracle recommends to off load this processing to the storage hardware RAID controller by using external redundancy. You can use normal redundancy in the following scenarios:

- Storage system does not have RAID controller
- Mirroring across storage arrays
- Extended cluster configurations

In general, Oracle ASM mirroring is the Oracle alternative to third party logical volume managers. Oracle ASM mirroring eliminates the deployment of additional layers of software complexity in your Oracle database environment.

### Oracle ASM Recovery from Read and Write I/O Errors

Read errors can be the result of a loss of access to the entire disk or media corruptions on an otherwise a healthy disk. Oracle ASM tries to recover from read errors on corrupted sectors on a disk. When a read error by the database or Oracle ASM triggers the Oracle ASM instance to attempt bad block remapping, Oracle ASM reads a good copy of the extent and copies it to the disk that had the read error.

- If the write to the same location succeeds, then the underlying allocation unit (sector) is deemed healthy. This might be because the underlying disk did its own bad block reallocation.
- If the write fails, Oracle ASM attempts to write the extent to a new allocation unit on the same disk. If this write succeeds, the original allocation unit is marked as unusable. If the write fails, the disk is taken offline.

One unique benefit on Oracle ASM based mirroring is that the database instance is aware of the mirroring. For many types of logical corruptions such as a bad checksum or incorrect System Change Number (SCN), the database instance proceeds through the mirror side looking for valid content and proceeds without errors. If the process in the database that encountered the read can obtain the appropriate locks to ensure data consistency, it writes the correct data to all mirror sides.

When encountering a write error, a database instance sends the Oracle ASM instance a disk offline message.

- If database can successfully complete a write to at least one extent copy and receive acknowledgment of the offline disk from Oracle ASM, the write is considered successful.
- If the write to all mirror side fails, database takes the appropriate actions in response to a write error such as taking the tablespace offline.

When the Oracle ASM instance receives a write error message from a database instance or when an Oracle ASM instance encounters a write error itself, the Oracle ASM instance attempts to take the disk offline. Oracle ASM consults the Partner Status Table (PST) to see whether any of the disk's partners are offline. If too many partners are offline, Oracle ASM forces the dismounting of the disk group. Otherwise, Oracle ASM takes the disk offline.

The ASMCMD `remap` command was introduced to address situations where a range of bad sectors exists on a disk and must be corrected before Oracle ASM or database I/O. For information about the `remap` command, see ["remap"](asm_util004.md).

### Oracle ASM Fast Mirror Resync

Restoring the redundancy of an Oracle ASM disk group after a transient disk path failure can be time consuming. This is especially true if the recovery process requires rebuilding an entire Oracle ASM failure group. Oracle ASM fast mirror resync significantly reduces the time to resynchronize a failed disk in such situations. When you replace the failed disk, Oracle ASM can quickly resynchronize the Oracle ASM disk extents.

Note:

To use this feature, the disk group compatibility attributes must be set to `11.1` or higher. For more information, refer to "Disk Group Compatibility".

Any problems that make a failure group temporarily unavailable are considered transient failures that can be recovered by the Oracle ASM fast mirror resync feature. For example, transient failures can be caused by disk path malfunctions, such as cable failures, host bus adapter failures, controller failures, or disk power supply interruptions.

Oracle ASM fast resync keeps track of pending changes to extents on an `OFFLINE` disk during an outage. The extents are resynced when the disk is brought back online.

By default, Oracle ASM drops a disk in 3.6 hours after it is taken offline. You can set the `DISK_REPAIR_TIME` disk group attribute to delay the drop operation by specifying a time interval to repair the disk and bring it back online. The time can be specified in units of minutes (`m` or `M`) or hours (`h` or `H`). If you omit the unit, then the default unit is hours. The `DISK_REPAIR_TIME` disk group attribute can only be set with the `ALTER` `DISKGROUP` SQL statement.

If the attribute is not set explicitly, then the default value (`3.6h`) applies to disks that have been set to `OFFLINE` mode without an explicit `DROP` `AFTER` clause. Disks taken offline due to I/O errors do not have a `DROP` `AFTER` clause.

The default `DISK_REPAIR_TIME` attribute value is an estimate that should be adequate for most environments. However, ensure that the attribute value is set to the amount of time that you think is necessary in your environment to fix any transient disk error, and that you are willing to tolerate reduced data redundancy.

The elapsed time (since the disk was set to `OFFLINE` mode) is incremented only when the disk group containing the offline disks is mounted. The `REPAIR_TIMER` column of `V$ASM_DISK` shows the amount of time left (in seconds) before an offline disk is dropped. After the specified time has elapsed, Oracle ASM drops the disk. You can override this attribute with the `ALTER` `DISKGROUP` `OFFLINE` `DISK` statement and the `DROP` `AFTER` clause.

Note:

If a disk is offlined by Oracle ASM because of an I/O (write) error or is explicitly offlined using the `ALTER` `DISKGROUP`... `OFFLINE` statement without the `DROP` `AFTER` clause, then the value specified for the `DISK_REPAIR_TIME` attribute for the disk group is used.

Altering the `DISK_REPAIR_TIME` attribute has no effect on offline disks. The new value is used for any disks that go offline after the attribute is updated. You can confirm this behavior by viewing the Oracle ASM alert log.

If an offline disk is taken offline for a second time, then the elapsed time is reset and restarted. If another time is specified with the `DROP` `AFTER` clause for this disk, the first value is overridden and the new value applies. A disk that is in `OFFLINE` mode cannot be dropped with an `ALTER` `DISKGROUP` `DROP` `DISK` statement; an error is returned if attempted. If for some reason the disk must be dropped (such as the disk cannot be repaired) before the repair time has expired, a disk can be dropped immediately by issuing a second `OFFLINE` statement with a `DROP` `AFTER` clause specifying `0h` or `0m`.

You can use `ALTER` `DISKGROUP` to set the `DISK_REPAIR_TIME` attribute to a specified hour or minute value, such as 4.5 hours or 270 minutes. For example:

```
ALTER DISKGROUP data SET ATTRIBUTE 'disk_repair_time' = '4.5h'
ALTER DISKGROUP data SET ATTRIBUTE 'disk_repair_time' = '270m'
```

After you repair the disk, run the SQL statement `ALTER` `DISKGROUP` `ONLINE` `DISK`. This statement brings a repaired disk group back online to enable writes so that no new writes are missed. This statement also starts a procedure to copy of all of the extents that are marked as stale on their redundant copies.

If a disk goes offline when the Oracle ASM instance is in rolling upgrade mode, the disk remains offline until the rolling upgrade has ended and the timer for dropping the disk is stopped until the Oracle ASM cluster is out of rolling upgrade mode. See ["Using Oracle ASM Rolling Upgrade"](asminst.md). Examples of taking disks offline and bringing them online follow.

The following example takes disk `DATA_001` offline and drops it after five minutes.

```
ALTER DISKGROUP data OFFLINE DISK DATA_001 DROP AFTER 5m;
```

The next example takes the disk `DATA_001` offline and drops it after the time period designated by `DISK_REPAIR_TIME` elapses:

```
ALTER DISKGROUP data OFFLINE DISK DATA_001;
```

This example takes all of the disk in failure group `FG2` offline and drops them after the time period designated by `DISK_REPAIR_TIME` elapses. IF you used a `DROP` `AFTER` clause, then the disks would be dropped after the specified time:

```
ALTER DISKGROUP data OFFLINE DISK IN FAILGROUP FG2;
```

The next example brings all of the disks in failure group `FG2` online:

```
ALTER DISKGROUP data ONLINE DISK IN FAILGROUP FG2;
```

This example brings only disk `DATA_001` online:

```
ALTER DISKGROUP data ONLINE DISK DATA_001;
```

This example brings all of the disks in disk group `DATA` online:

```
ALTER DISKGROUP data ONLINE ALL;
```

Querying the `V$ASM_OPERATION` view while you run any of these types of `ALTER` `DISKGROUP`... `ONLINE` statements displays the name and state of the current operation that you are performing. For example, the query:

```
SELECT GROUP_NUMBER, OPERATION, STATE FROM V$ASM_OPERATION;
```

Displays output similar to the following:

```
GROUP_NUMBER OPERA STAT 
------------ ----- ---- 
           1 ONLIN RUN
```

An `OFFLINE` operation is not displayed in a `V$ASM_OPERATION` view query.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_1007.htm#SQLRF01113) for information about [`ALTER` `DISKGROUP`](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_1007.htm#SQLRF01113) and [`CREATE` `DISKGROUP`](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_5008.htm#SQLRF01114)

### Preferred Read Failure Groups

When you configure Oracle ASM failure groups, it might be more efficient for a node to read from an extent that is closest to the node, even if that extent is a secondary extent. In other words, you can configure Oracle ASM to read from a secondary extent if that extent is closer to the node instead of Oracle ASM reading from the primary copy which might be farther from the node. Using the preferred read failure groups feature is most useful in extended clusters.

To use this feature, Oracle recommends that you configure at least one mirrored extent copy from a disk that is local to a node in an extended cluster. However, a failure group that is preferred for one instance might be remote to another instance in the same Oracle RAC database. The parameter setting for preferred read failure groups is instance specific.

Both the Oracle ASM clients and Oracle ASM require Oracle Database 11g release 1 (11.1) or higher to use preferred read failure groups.

Note:

If you do not specify failure groups for a disk group, each disk in the disk group belongs to its own failure group. Oracle does not recommend that you configure multiple preferred read failure groups in a disk group for an Oracle ASM instance. For any given instance, if you specify multiple failure groups in the same disk group as preferred read, a warning message is written to the alert log.

See Also:

[Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/storage.htm#RACAD820) for information about configuring preferred read disks in extended clusters

#### Configuring and Administering Preferred Read Failure Groups

To configure this feature, set the `ASM_PREFERRED_READ_FAILURE_GROUPS` initialization parameter to specify a list of failure group names as preferred read disks. For more information about this initialization parameter, refer to ["ASM\_PREFERRED\_READ\_FAILURE\_GROUPS"](asminst.md).

Set the parameter where `diskgroup` is the name of the disk group and `failuregroup` is the name of the failure group, separating these variables with a period. Oracle ASM ignores the name of a failure group that you use in this parameter setting if the failure group does not exist in the named disk group. You can append multiple values using commas as a separator as follows:

`ASM_PREFERRED_READ_FAILURE_GROUPS` `=` `diskgroup`.`failuregroup`,...

In an extended cluster, the failure groups that you specify with settings for the `ASM_PREFERRED_READ_FAILURE_GROUPS` parameter should only contain disks that are local to the instance. For normal redundancy disk groups, there should be only one failure group on each site of the extended cluster.

If there are multiple mirrored copies and you have set a value for the `ASM_PREFERRED_READ_FAILURE_GROUPS` parameter, then Oracle ASM first reads the copy that resides on a preferred read disk. If that read fails, then Oracle ASM attempts to read from the next mirrored copy that might not be on a preferred read disk.

Having multiple failure groups on one site can cause the loss of access to the disk group by the other sites if the site containing multiple failure groups fails. In addition, by having multiple failure groups on a site, an extent might not be mirrored to another site. This can diminish the read performance of the failure group on the other site.

For example, for a normal redundancy disk group, if a site contains two failure groups of a disk group, then Oracle ASM might put both mirror copies of an extent on the same site. In this configuration, Oracle ASM cannot protect against data loss from a site failure.

You should configure at most two failure groups on a site for a high redundancy disk group. If there are three sites in an extended cluster, for the same reason previously mentioned, then you should only create one failure group.

For a two-site extended cluster, a normal redundancy disk group only has two failure groups. In this case, you can only specify one failure group as a preferred read failure group for each instance.

You can use views to identify preferred read failure groups, such as the `V$ASM_DISK` view that shows whether a disk is a preferred read disk by the value in the `PREFERRED_READ` column. You can also use `V$ASM_DISK` to verify whether local disks in an extended cluster are preferred read disks. Use the Oracle ASM disk I/O statistics to verify that read operations are using the preferred read disks that you configured.

If a disk group is not optimally configured for an extended cluster, then Oracle ASM records warning messages in the alert logs. To identify specific performance issues with Oracle ASM preferred read failure groups, use the `V$ASM_DISK_IOSTAT` view. This view displays disk I/O statistics for each Oracle ASM client. You can also query the `V$ASM_DISK_IOSTAT` view on a database instance. However, this query only shows the I/O statistics for the database instance. In general, optimal preferred read extended cluster configurations balance performance with disk group availability.

See Also:

[Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_part.htm#REFRN003) for details about the `V$ASM` \* dynamic performance views

## Performance and Scalability Considerations for Disk Groups

This section discusses the following considerations for evaluating disk group performance:

- Determining the Number of Disk Groups
- Performance Characteristics When Grouping Disks
- Oracle ASM Storage Limits

### Determining the Number of Disk Groups

Use the following criteria to determine the number of disk groups to create:

- Disks in a given disk group should have similar size and performance characteristics. If you have several different types of disks in terms of size and performance, then create several disk groups that contain similar characteristics.
- Create separate disk groups for your database files and fast recovery area for backup files. This configuration allows fast recovery should a disk group failure occur.

For information about creating disk groups for a new installation, refer to "Creating Disk Groups for a New Oracle Installation".

### Performance Characteristics When Grouping Disks

Oracle ASM load balances the file activity by uniformly distributing file extents across all of the disks in a disk group. For this technique to be effective it is important that disks in a disk group be of similar performance characteristics. For example, the newest and fastest disks might reside in a disk group reserved for the database work area, and slower drives could reside in a disk group reserved for the fast recovery area.

There might be situations where it is acceptable to temporarily have disks of different sizes and performance characteristics coexist in a disk group. This would be the case when migrating from an old set of disks to a new set of disks. The new disks would be added and the old disks dropped. As the old disks are dropped, their storage is migrated to the new disks while the disk group is online.

### Oracle ASM Storage Limits

Oracle ASM provides near unlimited capacity for future growth, but does have some storage limits. For example, Oracle ASM has the following limits on the number of disk groups, disks, and files:

- 63 disk groups in a storage system
- 10,000 Oracle ASM disks in a storage system
- 1 million files for each disk group

Without any Oracle Exadata Storage, Oracle ASM has these storage limits:

- 2 terabytes (TB) maximum storage for each Oracle ASM disk
- 20 petabytes (PB) maximum for the storage system

With all Oracle Exadata Storage, Oracle ASM has these storage limits:

- 4 PB maximum storage for each Oracle ASM disk
- 40 exabytes (EB) maximum for the storage system

The maximum size limit of a disk group equals the maximum disk size multiplied by the maximum number of disks in a disk group (10,000).

The maximum number of disks across all disk groups is 10,000. The 10,000 disks can be in one disk group or distributed across a maximum of 63 disk groups. This is a limitation on the number of Oracle ASM disks, not necessarily the number of spindles. A storage array could group multiple spindles into a LUN that is used as a single Oracle ASM disk. However Oracle ASM is currently limited to 2 TB in a single disk unless using Oracle Exadata storage.

File size limits are dependent on the value of the disk group compatibility attributes. Oracle ASM supports file sizes greater than 128 TB in any redundancy mode when the `COMPATIBLE.RDBMS` disk group attribute is set greater than `10.1`.

If `COMPATIBLE.RDBMS` is set to `10.1`, the file size limits are less. For example, with `COMPATIBLE.RDBMS` equal to `10.1` and the AU size equal to 1 MB, Oracle ASM file size limits are:

- External redundancy: 16 TB
- Normal redundancy: 5.8 TB
- High redundancy: 3.9 TB

Note:

Oracle Database supports data file sizes up to 128 TB depending on the file system. In addition, Oracle Database has a file size limit that is dependent on the `DB_BLOCK_SIZE` initialization parameter.

For information about Oracle ASM disk group compatibility attributes, see "Disk Group Compatibility". For information about Oracle ASM file size limits, see Table 4-4.

## Disk Group Compatibility

This section describes disk group compatibility under the following topics:

- Overview of Disk Group Compatibility
- Disk Group Compatibility Attributes
- Setting Disk Group Compatibility Attributes
- Considerations When Setting Disk Group Compatibility in Replicated Environments

### Overview of Disk Group Compatibility

Advancing the disk group compatibility settings enables you to use the new Oracle ASM features that are available in a later release. For example, a disk group with the disk group compatibility attributes set to 11.2 can take advantage of new Oracle 11g release 2 (11.2) features, such as Oracle ASM volumes in disk groups and Oracle ASM File Access Control. See Table 4-3 for the features enabled for combinations of compatibility attribute settings.

The disk group compatibility feature also enables environments to interoperate when they use disk groups from both Oracle Database 10g and Oracle Database 11g. For example, disk group compatibility settings that are set to Oracle Database 10g enable an Oracle 10g client to access a disk group created with Oracle ASM 11g.

The disk group attributes that determine compatibility are `COMPATIBLE.ASM`, `COMPATIBLE.RDBMS`. and `COMPATIBLE.ADVM`. The `COMPATIBLE.ASM` and `COMPATIBLE.RDBMS` attribute settings determine the minimum Oracle Database software version numbers that a system can use for Oracle ASM and the database instance types respectively. For example, if the Oracle ASM compatibility setting is `11.2`, and RDBMS compatibility is set to 11.1, then the Oracle ASM software version must be at least `11.2`, and the Oracle Database client software version must be at least `11.1`. The `COMPATIBLE.ADVM` attribute determines whether the Oracle ASM Dynamic Volume Manager feature can create an volume in a disk group.

When you create a disk group, you can specify the disk group compatibility attribute settings in the `CREATE` `DISKGROUP` SQL statement. The `ALTER` `DISKGROUP` SQL statement can update the compatible attribute settings for existing disk groups. If not specified when using the `CREATE` `DISKGROUP` SQL statement, `10.1` is the default setting for both the `COMPATIBLE.ASM` and `COMPATIBLE.RDBMS` attributes for Oracle ASM in Oracle Database 11g. The `COMPATIBLE.ADVM` attribute is empty if it is not set. See Table 4-2 for examples of valid combinations of compatible attribute settings.

You can set and update disk group attributes with the ASMCMD `setattr` command. For information about the ASMCMD `setattr` command, see ["setattr"](asm_util004.md).

Notes:

- The disk group compatibility settings determine whether your environment can use the latest Oracle ASM features.
- The disk group compatibility settings can only be advanced; you cannot revert to a lower compatibility setting. See "Reverting Disk Group Compatibility".
- The `COMPATIBLE.ASM` attribute must be advanced before advancing other disk group compatibility attributes and its value must be greater than or equal to the value of other disk group compatibility attributes.

### Disk Group Compatibility Attributes

The disk group compatibility attributes specify the disk group compatibility settings for Oracle ASM and database instances. These attributes are described under the following topics:

- COMPATIBLE.ASM
- COMPATIBLE.RDBMS
- COMPATIBLE.ADVM

#### COMPATIBLE.ASM

The value for the disk group `COMPATIBLE`.`ASM` attribute determines the minimum software version for an Oracle ASM instance that can use the disk group. This setting also affects the format of the data structures for the Oracle ASM metadata on the disk. The format of other file contents is determined by Oracle ASM Dynamic Volume Manager (Oracle ADVM) and the database instance.

For Oracle ASM in Oracle Database 11g, `10.1` is the default setting for the `COMPATIBLE.ASM` attribute when using the SQL `CREATE` `DISKGROUP` statement, the ASMCMD `mkdg` command, and Oracle Enterprise Manager Create Disk Group page. When creating a disk group with ASMCA, the default setting is `11.2`.

#### COMPATIBLE.RDBMS

The value for the disk group `COMPATIBLE.RDBMS` attribute determines the minimum `COMPATIBLE` database initialization parameter setting for any database instance that is allowed to use the disk group. Before advancing the `COMPATIBLE`.`RDBMS` attribute, ensure that the values for the `COMPATIBLE` initialization parameter for all of the databases that access the disk group are set to at least the value of the new setting for `COMPATIBLE`.`RDBMS`.

For example, if the `COMPATIBLE` initialization parameters of the databases are set to either `11.1` or `11.2`, then `COMPATIBLE.RDBMS` can be set to any value between `10.1` and `11.1` inclusively.

For Oracle ASM in Oracle Database 11g, `10.1` is the default setting for the `COMPATIBLE`.`RDBMS` attribute when using the SQL `CREATE` `DISKGROUP` statement, the ASMCMD `mkdg` command, ASMCA Create Disk Group page, and Oracle Enterprise Manager Create Disk Group page.

Note:

The database initialization parameter `COMPATIBLE` enables you to use a new release of Oracle Database, while at the same time guaranteeing backward compatibility with an earlier release. See [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams035.htm#REFRN10019) for more information about the `COMPATIBLE` initialization parameter.

#### COMPATIBLE.ADVM

The value for the disk group `COMPATIBLE.ADVM` attribute determines whether the disk group can contain Oracle ASM volumes. The value must be set to `11.2` or higher. Before setting this attribute, the `COMPATIBLE.ASM` value must be `11.2` or higher. Also, the Oracle ADVM volume drivers must be loaded in the supported environment.

By default, the value of the `COMPATIBLE.ADVM` attribute is empty until set.

For more information about Oracle ADVM, see ["Overview of Oracle ASM Dynamic Volume Manager"](asmfilesystem.md).

### Setting Disk Group Compatibility Attributes

This section discusses the settings of the disk group compatibility attributes and how to set the attribute values with the `CREATE` `DISKGROUP` or `ALTER` `DISKGROUP` SQL statement.

This section contains these topics:

- Valid Combinations of Compatibility Attribute Settings
- Using CREATE DISKGROUP with Compatibility Attributes
- Using ALTER DISKGROUP with Compatibility Attributes
- Viewing Compatibility Attribute Settings
- Features Enabled By Disk Group Compatibility Attribute Settings
- Reverting Disk Group Compatibility

You can also set the disk group compatibility settings with Oracle Enterprise Manager, Oracle ASM command-line utility (ASMCMD), and Oracle ASM Configuration Assistant (ASMCA). See [Chapter 9, "Administering Oracle ASM with Oracle Enterprise Manager"](asm_em.md), [Chapter 11, "Oracle ASM Configuration Assistant"](asmca.md), and [Chapter 12, "Oracle ASM Command-Line Utility"](asm_util.md).

Note:

Advancing the values for disk group compatibility attributes is an irreversible operation. See "Reverting Disk Group Compatibility".

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_5008.htm#SQLRF01114) for more information about the disk group compatibility SQL statements

#### Valid Combinations of Compatibility Attribute Settings

When setting the values for the disk group attributes, specify at least the major and minor versions of a valid Oracle Database release number. For example, you can specify compatibility as `'11.1'` or `'11.2'`; Oracle assumes that any missing version number digits are zeros.

Table 4-2 shows some valid combinations of the disk group compatibility attributes and the valid Oracle ASM and database instance versions for each combination.

Table 4-2 Examples of disk group compatibility attribute settings

| COMPATIBLE.ASM | COMPATIBLE.RDBMS | COMPATIBLE.ADVM | ASM Instance Version | COMPATIBLE Setting for RDBMS Instance |
| --- | --- | --- | --- | --- |
| 10.1 | 10.1 | n/a | \>= 10.1 | \>= 10.1 |
| 11.1 | 10.1 | n/a | \>= 11.1 | \>= 10.1 |
| 11.2 | 11.1 | 11.2 | \>= 11.2 | \>= 11.1 |
| 11.2 | 11.2 | 11.2 | \>= 11.2 | \>= 11.2 |

These are some possible combinations of Oracle ASM and database releases:

- The database release is 11g release 2 (11.2) (database initialization parameter `COMPATIBLE` is set to `11.2`) and the Oracle ASM release is 11g release 2 (11.2). The `COMPATIBLE.ASM` and `COMPATIBLE.RDBMS` disk group attributes are set to the default value of `10.1` for a disk group.
	The Oracle ASM disk group functionality remains at 10g.
- The database release is 10g and the Oracle ASM release is 11.2. `COMPATIBLE.ASM` is set to `11.2` and `COMPATIBLE.RDBMS` is set to `10.1` for a disk group.
	The disk group features enabled for this combination of attribute settings are shown in Table 4-3.
- The database release is 11.2 (database initialization parameter `COMPATIBLE` is set to `11.2`) and the Oracle ASM release is 11.2. All the disk group compatibility attributes are set to `11.2` for a disk group.
	The disk group features enabled for this combination of attribute settings are shown in Table 4-3.

#### Using CREATE DISKGROUP with Compatibility Attributes

You can specify the compatibility settings for a disk group with the `CREATE` `DISKGROUP` statement when creating the disk group.

The following example creates a normal redundancy disk group `data1` with the Oracle ASM compatibility set to `11.2` and the RDBMS compatibility set to the default (the `COMPATIBLE.RDBMS` default is less than or equal to 11.2):

```
CREATE DISKGROUP data1 DISK '/dev/sd*' 
       ATTRIBUTE 'compatible.asm' = '11.2';
```

The following example creates a normal redundancy disk group `data2` with the ASM, RDBMS, and ADVM compatibility set to `11.2`:

```
CREATE DISKGROUP data2 DISK '/dev/sd*' 
       ATTRIBUTE 'compatible.asm' = '11.2', 'compatible.rdbms' = '11.2',
                 'compatible.advm' = '11.2';
```

#### Using ALTER DISKGROUP with Compatibility Attributes

After a disk group has been created, you can use the `ALTER` `DISK` `GROUP` SQL statement to change the compatibility attributes. The `ALTER` `DISK` `GROUP` SQL statement ensures that Oracle can advance the compatibility of the specified disk group before committing the change.

All of the affected databases and file systems should be online when running `ALTER` `DISKGROUP` to ensure that advancing compatibility does not reduce the database and file system access. When advancing disk group compatibility, you must advance the `COMPATIBLE`.`ASM` attribute before the `COMPATIBLE`.`RDBMS` or `COMPATIBLE.ADVM` attribute to ensure a valid combination of compatible attribute settings as shown in Table 4-2. You can advance only one compatibility attribute in a single `ALTER` `DISKGROUP` statement.

The following example advances the Oracle ASM compatibility for disk group `data3` to `11.2`. An Oracle ASM instance must be at release `11.2` or higher to access the `data3` disk group.

```
ALTER DISKGROUP data3 SET ATTRIBUTE 'compatible.asm' = '11.2';
```

The following example advances the `COMPATIBLE.RDBMS` and `COMPATIBLE.ADVM` compatibility attributes of the disk group `data3` to `11.2`. This example assumes that the value of `COMPATIBLE.ASM` is set to `11.2`.

```
ALTER DISKGROUP data3 SET ATTRIBUTE 'compatible.rdbms' = '11.2',
ALTER DISKGROUP data3 SET ATTRIBUTE 'compatible.advm' = '11.2';
```

#### Viewing Compatibility Attribute Settings

You can view the disk group compatibility settings in the `V$ASM_ATTRIBUTE` view. However, the `V$ASM_ATTRIBUTE` view does not display any rows when the `COMPATIBLE.ASM` value is set to `10.1`. Instead you can determine the values for the `COMPATIBLE.ASM` and `COMPATIBLE.RDBMS` disk group compatibility attributes with the `COMPATIBILITY` and `DATABASE_COMPATIBILITY` columns of the `V$ASM_DISKGROUP` view.

See [Example 6-1, "Viewing disk group attributes with V$ASM\_ATTRIBUTE"](asmviews.md) for an example querying the `V$ASM_ATTRIBUTE` view.

You can also display the disk group compatibility attributes with the ASMCMD command `lsattr`. For information about `lsattr`, see ["lsattr"](asm_util004.md).

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_5008.htm#SQLRF01114) for information about disk group attributes
- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_part.htm#REFRN003) for details on the `V$ASM_DISKGROUP` and `V$ASM_ATTRIBUTE` dynamic performance views

#### Features Enabled By Disk Group Compatibility Attribute Settings

Table 4-3 describes the features enabled by valid combinations of the disk group compatibility attribute settings.

Table 4-3 Features enabled by disk group compatibility attribute settings

| Disk Group Features Enabled | COMPATIBLE.ASM | COMPATIBLE.RDBMS | COMPATIBLE.ADVM |
| --- | --- | --- | --- |
| Support for larger AU sizes (32 or 64 MB) | \>= 11.1 | \>= 11.1 | n/a |
| Attributes are displayed in the `V$ASM_ATTRIBUTE` view | \>= 11.1 | n/a | n/a |
| Fast mirror resync | \>= 11.1 | \>= 11.1 | n/a |
| Variable size extents | \>= 11.1 | \>= 11.1 | n/a |
| Exadata storage | \>= 11.1.0.7 | \>= 11.1.0.7 | n/a |
| Intelligent Data Placement | \>= 11.2 | \>= 11.2 | n/a |
| OCR and voting files in a disk group | \>= 11.2 | n/a | n/a |
| Sector size set to nondefault value | \>= 11.2 | \>= 11.2 | n/a |
| Oracle ASM SPFILE in a disk group | \>= 11.2 | n/a | n/a |
| Oracle ASM File Access Control | \>= 11.2 | \>= 11.2 | n/a |
| Volumes in disk groups | \>= 11.2 | n/a | \>= 11.2 |
| `ASM_POWER_LIMIT` value up to `1024` | \>= 11.2.0.2 | n/a | n/a |
| Encryption, replication, security, tagging on Linux systems | \>= 11.2.0.2 | n/a | \>= 11.2.0.2 |
| Encryption, replication, security, tagging on Windows systems | \>= 11.2.0.3 | n/a | \>= 11.2.0.3 |
| Read-write snapshots | \>= 11.2.0.3 | n/a | \>= 11.2.0.3 |

The following list applies to Table 4-3.

- If encryption is configured for the first time on Oracle ASM 11g release 2 version 11.2.0.3 on Linux or if encryption parameters must be changed or a new volume encryption key must be created following a software upgrade to Oracle ASM 11g release 2 version 11.2.0.3 on Linux, then the disk group compatibility attributes for `ASM` and `ADVM` must be set to `11.2.0.3`.
- Oracle ASM features not explicitly listed in Table 4-3 do not require advancing the disk group compatibility attribute settings.
- The value of `COMPATIBLE.ASM` must always be greater than or equal to the value of `COMPATIBLE.RDBMS` and `COMPATIBLE.ADVM`.
- A value of not applicable (n/a) means that the setting of the attribute has no effect on the feature.
- For information about the rebalancing process and the `ASM_POWER_LIMIT` initialization parameter, refer to ["ASM\_POWER\_LIMIT"](asminst.md).

#### Reverting Disk Group Compatibility

Advancing the values for disk group compatibility attributes is an irreversible operation. If you advance the disk group compatibility settings, you cannot change the values back to the previous settings. To revert to the previous values, you must create a new disk group with the old compatibility attribute settings and then restore the database files that were in the disk group to the new disk group.

When you revert to a new disk group with the old compatibility attribute settings, the latest Oracle ASM features might not be available. For example, if you revert the disk group compatibility to a pre-11.2 value, Oracle ACFS functionality is not available.

For example, you could perform the following procedure to revert a disk group to previous compatibility settings:

1. If the Oracle ASM SPFILE is in the disk group, move this SPFILE out of the disk group:
	1. Connect with SQL\*Plus to the Oracle ASM instance.
		2. Create a PFILE in the file system.
		For example:
		```
		SQL> CREATE PFILE '$ORACLE_HOME/dbs/asmspfile.ora' FROM SPFILE
		```
2. If the OCR and voting files are in the disk group, move them out of this disk group.
	See Also:
	The [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/admin.htm#CWADD838) for information about administering OCR and voting files
3. Back up any files that must be saved.
	1. Back up the database files.
		2. If an Oracle ACFS file system is mounted on an Oracle ADVM volume on the disk group, the operating system files in the file system must be backed up or copied to a location outside the file system mount point.
4. Create a new disk group using SQL `CREATE` `DISKGROUP` specifying the previous values for the disk group attribute settings.
	For information about creating a disk group, see "Using the CREATE DISKGROUP SQL Statement".
5. Restore the database files into the newly created disk group using Recovery Manager (RMAN).
	For information about moving data files between disk groups, see ["Moving Data Files Between Oracle ASM Disk Groups Using RMAN"](asm_rman.md).
6. Drop the disk group with the advanced disk group compatibility settings using SQL `DROP` `DISKGROUP` `INCLUDING` `CONTENTS` to remove the disk group and its contents.
	This SQL statement also removes any Oracle ACFS file system and its contents.
	For information about dropping a disk group, see "Dropping Disk Groups".

### Considerations When Setting Disk Group Compatibility in Replicated Environments

If you advance disk group compatibility, then you could enable the creation of files that are too large to be managed by a previous Oracle database release. You must be aware of the file size limits because replicated sites cannot continue using the software from a previous release to manage these large files. The disk group compatibility settings should be the same for all replicated environments.

Table 4-4 shows the maximum Oracle ASM file sizes supported for `COMPATIBLE.RDBMS` settings when the `AU_SIZE` attribute is set to one megabyte for a disk group.

Table 4-4 Maximum Oracle ASM file sizes for disk groups with AU\_SIZE equal to 1 MB

| Redundancy | COMPATIBLE.RDBMS = 10.1 | COMPATIBLE.RDBMS >= 11.1 |
| --- | --- | --- |
| External | 16 TB | 140 PB |
| Normal | 5.8 TB | 23 PB |
| High | 3.9 TB | 15 PB |

Table 4-4 shows that Oracle Database 10g can only support a file size of up to 16 TB for external redundancy. If you advance the `COMPATIBILE.RDBMS` attribute to `11.1` or greater, then a file can grow beyond 16 TB. However, the larger size causes the file to be unusable in a replicated and disaster recovery site if the disaster recovery site has a disk group `COMPATIBLE.RDBMS` setting that is incompatible with the larger size.

For information about Oracle ASM storage sizes, see "Oracle ASM Storage Limits".

See Also:

- [Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/intro.htm#UPGRD005) for information about database compatibility
- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/create.htm#ADMIN002) for information about the `COMPATIBLE` initialization parameter and irreversible compatibility
- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams035.htm#REFRN10019) for information about the `COMPATIBLE` initialization parameter

## Managing Oracle ASM File Access Control for Disk Groups

Oracle ASM File Access Control provides optional protection for the content of Oracle ASM disk groups from accidental access by unauthorized Oracle ASM clients, such as an unauthorized database.

To set up Oracle ASM File Access Control, you must designate separate operating system groups as described in ["Using Separate Operating System Groups for Oracle ASM Users"](asminst.md). Oracle ASM File Access Control is available for Linux and UNIX computers only.

You can manage Oracle ASM file access control with ASMCMD commands, Oracle Enterprise Manager, and SQL statements.

This section contains these topics:

- About Oracle ASM File Access Control
- Setting Disk Group Attributes for Oracle ASM File Access Control
- Using SQL Statements to Manage Oracle ASM File Access Control

For information about managing Oracle ASM File Access Control with ASMCMD commands, see ["ASMCMD File Access Control Commands"](asm_util006.md).

For information about managing Oracle ASM File Access Control with Oracle Enterprise Manager, see ["Managing Oracle ASM File Access Control with Oracle Enterprise Manager"](asm_em.md).

For information about views that provide details about Oracle ASM file access control, see ["Viewing Oracle ASM File Access Control Information"](asmviews.md).

For information about controlling accessing to Oracle ASM instances, see ["Authentication for Accessing Oracle ASM Instances"](asminst.md).

### About Oracle ASM File Access Control

Oracle ASM File Access Control restricts the access of files to specific Oracle ASM clients that connect as SYSDBA. An Oracle ASM client is typically a database, which is identified as the user that owns the database instance home. Oracle ASM File Access Control uses this user name to identify a database. Oracle ASM File Access Control restricts access based on the operating system effective user identification number of a database owner. For example, in [Table 3-2, "Separated operating system groups and privileges for Oracle ASM users"](asminst.md) the databases are identified as `oracle1` and `oracle2`.

Oracle ASM uses file access control to determine the additional privileges that are given to a database that has been authenticated AS SYSDBA on the Oracle ASM instance. These additional privileges include the ability to modify and delete certain files, aliases, and user groups.

You can set up user groups to specify the list of databases that share the same access permissions to Oracle ASM files. User groups are lists of databases and any database that authenticates AS SYSDBA can create a user group. However, only the creator of a group can delete it or modify its membership list.

Each Oracle ASM file has three categories of privileges: owner, group, and other. Each category can have no permission, read-only permission, or read-write permission.

The file owner is usually the creator of the file and can assign permissions for the file in any of the owner, group, or other categories. The owner can also change the group associated with the file.

When administering Oracle ASM File Access Control, Oracle recommends that you connect as SYSDBA to the database instance that is the owner, or planned owner, of the files in the disk group.

To set up Oracle ASM File Access Control for files in a disk group, perform the following steps:

1. Alter a new or existing disk group to set the Oracle ASM File Access Control disk group attributes.
	For a newly-created disk group, you should set the disk group attributes before creating any files in the disk group.
	See "Setting Disk Group Attributes for Oracle ASM File Access Control".
2. For files that exist in a disk group before setting the Oracle ASM File Access Control disk group attributes, you must explicitly set the permissions and ownership on those existing files.
	Ensure that the user exists before setting ownership or permissions on a file. The file must be closed before setting the ownership or permissions.
	See `ALTER` `DISKGROUP` `SET` `PERMISSION` and `ALTER` `DISKGROUP` `SET` `OWNERSHIP` in "Using SQL Statements to Manage Oracle ASM File Access Control".
3. Optionally, you can create user groups that are groups of database users that share the same access permissions to Oracle ASM files.
	See `ALTER` `DISKGROUP` `ADD` `USERGROUP` in "Using SQL Statements to Manage Oracle ASM File Access Control".

### Setting Disk Group Attributes for Oracle ASM File Access Control

To manage Oracle ASM File Access Control for a disk group, you must set the `ACCESS_CONTROL.ENABLED` and `ACCESS_CONTROL.UMASK` disk group attributes. You can set the attributes by altering the disk group with the `ALTER` `DISKGROUP` SQL statement or you can set the attributes with the ASMCMD `setattr` command. For information about the ASMCMD `setattr` command, see ["setattr"](asm_util004.md).

When you set up file access control on an existing disk group, the files previously created remain accessible by everyone, unless you run the `ALTER` `DISKGROUP` `SET` `PERMISSION` SQL statement or the ASMCMD `chmod` command to restrict the permissions. For information about the ASMCMD `chmod` command, see ["chmod"](asm_util006.md).

The `COMPATIBLE.ASM` and `COMPATIBLE.RDBMS` disk group attributes must be set to 11.2 or higher to enable Oracle ASM File Access Control. For information about disk group compatibility attributes, see "Disk Group Compatibility".

The disk group attributes that control Oracle ASM File Access Control are the following:

- `ACCESS_CONTROL.ENABLED`
	This attribute determines whether Oracle ASM File Access Control is enabled for a disk group.
	The value can be `true` or `false`. The default is `false`.
	If the attribute is set to `true`, accessing Oracle ASM files is subject to access control. If `false`, any user can access every file in the disk group. All other operations behave independently of this attribute.
- `ACCESS_CONTROL.UMASK`
	This attribute determines which permissions are masked out on the creation of an Oracle ASM file for the user that owns the file, users in the same user group, and others not in the user group. This attribute applies to all files on a disk group.
	The values can be combinations of three digits { `0` | `2` | `6` } { `0` | `2` | `6` } { `0` | `2` | `6` }. The default is `066`.
	Setting to `0` masks out nothing. Setting to `2` masks out write permission. Setting to `6` masks out both read and write permissions.
	Before setting the `ACCESS_CONTROL.UMASK` disk group attribute, you must set the `ACCESS_CONTROL.ENABLED` attribute to `true` to enable Oracle ASM File Access Control.

Example 4-11 shows how to enable Oracle ASM File Access Control for a disk group using SQL\*Plus. In this example, the permissions setting is `026` which enables read-write access for the owner, read access for users in the group, and no access to others not in the group

Example 4-11 Setting up Oracle ASM File Access Control

```
ALTER DISKGROUP data1 SET ATTRIBUTE 'access_control.enabled' = 'true';
ALTER DISKGROUP data1 SET ATTRIBUTE 'access_control.umask' = '026';
```

### Using SQL Statements to Manage Oracle ASM File Access Control

You can use the `ALTER` `DISKGROUP` SQL statement to manage file access control for Oracle ASM disk groups. These SQL statements are available for both database and Oracle ASM instances.

The SQL statements that support disk group access control are:

- `ALTER` `DISKGROUP` `ADD` `USERGROUP`... `WITH` `MEMBER`
	Adds an Oracle ASM user group to a disk group. The user group name is limited to a maximum of 30 characters. The databases identified in the `MEMBER` clause must be in the disk group, as shown by `V$ASM_USER`, or the command returns an error. Any users authenticated as `SYSASM` or `SYSDBA` can create new user groups. For example:
	```
	SQL> SELECT group_number, os_name FROM V$ASM_USER;
	GROUP_NUMBER OS_NAME
	------------ ----------------------------------------------------------------
	           1 oracle1
	           1 oracle2
	...
	SQL> ALTER DISKGROUP data ADD USERGROUP 'test_grp1' 
	     WITH MEMBER 'oracle1','oracle2';
	```
- `ALTER` `DISKGROUP` `DROP` `USERGROUP`
	Drops an Oracle ASM user group from a disk group. Dropping a group might leave some files without a valid group. For those files to have a valid group, you must manually update the group associated with those files to a valid group.
	```
	SQL> ALTER DISKGROUP data DROP USERGROUP 'test_grp1';
	```
- `ALTER` `DISKGROUP` `MODIFY` `USERGROUP` `ADD` `MEMBER`
	Adds users to the specified user group. The users must be in the disk group, as shown by `V$ASM_USER`, or the command returns an error. Only the creator of the group or the Oracle ASM administrator can modify group membership.
	```
	SQL> ALTER DISKGROUP data MODIFY USERGROUP 'test_grp2' ADD MEMBER 'oracle2';
	```
- `ALTER` `DISKGROUP` `MODIFY` `USERGROUP` `DROP` `MEMBER`
	Removes users from the specified user group. If a member is not in the user group, then an error is returned. Only the creator of the group or the Oracle ASM administrator can modify group membership.
	```
	SQL> ALTER DISKGROUP data MODIFY USERGROUP 'test_grp2' DROP MEMBER 'oracle2';
	```
- `ALTER` `DISKGROUP` `ADD` `USER`
	Adds operating system (OS) users to an Oracle ASM disk group, so that these users can have access privileges on the disk group. The users must be existing operating system users, and their user names must have a corresponding operating system user ID or system ID. If a user exists in the disk group, as shown by `V$ASM_USER`, then the command records an error and continues to add other users, if any.
	The operating system user of a running database instance is automatically added to a disk group when the database instance accesses that disk group and creates files. However, for a database instance to read files in a disk group without creating any files, then you must use the `ADD` `USER` clause to add that database user to the disk group. Also, you can use this clause to add a database user to an existing disk group immediately after setting the Oracle ASM File Access Control disk group attributes and before creating new files.
	```
	SQL>  ALTER DISKGROUP DATA ADD USER 'oracle1';
	```
- `ALTER` `DISKGROUP` `DROP` `USER`
	Drops operating system users from an Oracle ASM disk group. If a user is not in the disk group, then this command records an error and continues to drop other users, if any.
	If the user owns any files on the same Oracle ASM disk group, then this command fails with an error, unless the `CASCADE` keyword is specified. If the latter case, then the user is deleted, along with all the files that the user owns.
	If any files owned by the user are currently open, then the `DROP` `USER` command fails, and no files are deleted.
	```
	SQL>  ALTER DISKGROUP DATA DROP USER 'oracle1';
	```
- `ALTER` `DISKGROUP` `SET` `PERMISSION`
	Modifies permissions of an Oracle ASM file. Setting `read` `only` permission to a file that has `read` `write` permission revokes the `write` permission. Only the file owner or the Oracle ASM administrator can change the permissions of a file. You cannot change the permissions on an open file.
	```
	SQL> ALTER DISKGROUP data SET PERMISSION OWNER=read write, GROUP=read only,
	     OTHER=none FOR FILE '+data/controlfile.f';
	```
- `ALTER` `DISKGROUP` `SET` `OWNERSHIP`
	Changes the owner or group of a file to the specified user or user group name, respectively. If the specified user or user group name does not exist, this command fails with an error. Only the owner of the file or the Oracle ASM administrator can run this command, and only the Oracle ASM administrator can change the owner. Also, the user group name must exist, and the owner of the file must be a member of that group. You cannot change the ownership of an open file.
	```
	SQL> ALTER DISKGROUP data SET OWNERSHIP OWNER='oracle1', GROUP='test_grp1'
	     FOR FILE '+data/controlfile.f';
	```

See Also:

The [`ALTER DISKGROUP`](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_1007.htm#SQLRF01113) SQL statement in the [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_1007.htm#SQLRF01113)

## Mounting and Dismounting Disk Groups

Disk groups that are specified in the `ASM_DISKGROUPS` initialization parameter are mounted automatically at Oracle ASM instance startup. This makes them available to all database instances running on the same node as Oracle ASM. The disk groups are dismounted at Oracle ASM instance shutdown. Oracle ASM also automatically mounts a disk group when you initially create it, and dismounts a disk group if you drop it.

When a disk group is mounted, a disk group number is chosen. This number may change across disk group mounts. A disk group number is not recorded in any persistent structure, but the current value can be viewed in the `GROUP_NUMBER` column of the V$ASM views.

When you want to mount or dismount disk groups manually, use the `ALTER DISKGROUP...MOUNT` or `ALTER DISKGROUP...DISMOUNT` statement. You can mount or dismount disk groups by name, or specify `ALL`.

If you try to dismount a disk group that contains open files, the statement fails, unless you also specify the `FORCE` clause.

In a clustered Oracle ASM environment in `RESTRICTED` mode, a disk group is mounted in single-instance exclusive mode. No other Oracle ASM instance in that cluster can mount that disk group. In this mode the disk group is not usable by any Oracle ASM client. Use this mode to perform a fast rebalance.

The following SQL statement dismounts all disk groups that are currently mounted to the Oracle ASM instance:

```
ALTER DISKGROUP ALL DISMOUNT;
```

The following SQL statement mounts disk group `data1`:

```
ALTER DISKGROUP data1 MOUNT;
```

### Mounting Disk Groups Using the FORCE Option

Oracle ASM provides a `MOUNT` `FORCE` option with `ALTER` `DISKGROUP` to enable Oracle ASM disk groups to be mounted in normal or high redundancy modes even though some Oracle ASM disks may be unavailable to the disk group at mount time. The default behavior without the `FORCE` option is to fail to mount a disk group that has damaged or missing disks.

The `MOUNT` `FORCE` option is useful in situations where a disk is temporarily unavailable and you want to mount the disk group with reduced redundancy while you correct the situation that caused the outage.

To successfully mount with the `MOUNT` `FORCE` option, Oracle ASM must be able to find at least one copy of the extents for all of the files in the disk group. In this case, Oracle ASM can successfully mount the disk group, but with potentially reduced redundancy.

The disks that Oracle ASM cannot access are placed in an offline mode. Oracle ASM then begins timing the period that these disks are in an offline mode. If the disk offline time period exceeds the timer threshold set by `DISK_REPAIR_TIME` disk group attribute, then those disks are permanently dropped from the disk group. You can change the offline timer after a disk is put in an offline state by using the `ALTER` `DISKGROUP` `OFFLINE` statement. For more information about setting the `DISK_REPAIR_TIME` disk group attribute, see "Oracle ASM Fast Mirror Resync".

Note:

An Oracle ASM instance mounts an incomplete disk group differently depending on the specified compatibility. See "Features Enabled By Disk Group Compatibility Attribute Settings".

In clustered Oracle ASM environments, if an Oracle ASM instance is not the first instance to mount the disk group, then using the `MOUNT` `FORCE` statement fails. This is because the disks have been accessed by another instance and the disks are not locally accessible.

If all disks are available, then using the `FORCE` option causes the `MOUNT` command to fail. This discourages unnecessary and improper use of the feature.

The following example shows how to use the `FORCE` option to force the mount of the `data1` disk group:

```
ALTER DISKGROUP data1 MOUNT FORCE
```

See Also:

The [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_1007.htm#SQLRF01113) for additional information about the `ALTER` `DISKGROUP` statement and the `FORCE` option

## Checking the Internal Consistency of Disk Group Metadata

You can check the internal consistency of disk group metadata using the `ALTER` `DISKGROUP` statement with the `CHECK` keyword. You can use this statement to check specific files in a disk group, specific disks or all disks in a disk group, or specific failure groups within a disk group. The disk group must be mounted to perform these checks.

By default, the `CHECK` `DISK` `GROUP` clause verifies all of the metadata directories. Oracle ASM displays summary errors and writes the details about the errors in an alert log. The `CHECK` keyword performs the following operations:

- Verifies the consistency of the disk
- Cross checks all of the file extent maps and allocation tables for consistency
- Checks that the alias metadata directory and file directory are linked correctly
- Verifies that the alias directory tree is linked correctly
- Checks that Oracle ASM metadata directories do not have unreachable allocated blocks

The `REPAIR` `|` `NOREPAIR` clause specifies whether Oracle ASM should attempt to repair errors that are found during the check. The default is `NOREPAIR`. Use the `NOREPAIR` clause to receive alerts about inconsistencies and to suppress Oracle ASM from resolving the errors automatically. The following example statement checks for consistency in the metadata for all disks in the `data1` disk group:

```
ALTER DISKGROUP data1 CHECK ALL;
```

See Also:

The [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_1007.htm#SQLRF01113) for additional information about the `CHECK` clause syntax

## Dropping Disk Groups

The `DROP` `DISKGROUP` statement enables you to delete an Oracle ASM disk group and optionally, all of its files. You can specify the `INCLUDING` `CONTENTS` clause if you also want to delete all files that are contained in the disk group. The default is `EXCLUDING` `CONTENTS`, which provides syntactic consistency and prevents you from dropping the disk group if it has any contents

The Oracle ASM instance must be started and the disk group must be mounted with none of the disk group files open, in order for the `DROP DISKGROUP` statement to succeed. The statement does not return until the disk group has been dropped.

When you drop a disk group, Oracle ASM dismounts the disk group and removes the disk group name from the `ASM_DISKGROUPS` initialization parameter if a server parameter file is being used. If a text initialization parameter file is being used, and the disk group is mentioned in the `ASM_DISKGROUPS` initialization parameter, then you must remove the disk group name from the `ASM_DISKGROUPS` initialization parameter before the next time that you shut down and restart the Oracle ASM instance.

The following statement deletes `data1`:

```
DROP DISKGROUP data1;
```

After ensuring that none of the files contained in `data1` are open, Oracle ASM rewrites the header of each disk in the disk group to remove Oracle ASM formatting information. The statement does not specify `INCLUDING CONTENTS`, so the drop operation fails if the disk group contains any files.

If an Oracle Automatic Storage Management Cluster File System (Oracle ACFS) file system is mounted on a volume contained in the disk group, then the file system must be dismounted. If the file system has been registered, then it must be deregistered. The `INCLUDING` `CONTENTS` clause must be used to drop this disk group. All data in the file system is destroyed. To view the volumes and mount paths associated with a disk group, you can query the `V$ASM_VOLUME` view. For an example of a query on the `V$ASM_VOLUME` view, see [Example 6-16](asmviews.md). For information about deregistering and dismounting Oracle ACFS file systems, see ["Deregistering, Dismounting, and Disabling Volumes and Oracle ACFS File Systems"](asmfs_util001.md).

If you cannot mount a disk group but must drop it, you can use the `FORCE` option of the `DROP` `DISKGROUP` statement. This command enables you to remove the headers on disks that belong to a disk group that cannot be mounted by any Oracle ASM instances as shown in the following example:

```
DROP DISKGROUP data1 FORCE
```

The disk group on which you perform this operation should not be mounted anywhere in the cluster. When you use the `FORCE` option, the Oracle ASM instance does not attempt to verify that a disk group is being used by another Oracle ASM instance in the same storage subsystem.

Note:

Use the `FORCE` option with extreme caution.

You can also drop a disk group with Oracle Enterprise Manager. See ["Dropping Disk Groups"](asm_em.md).

## Renaming Disks Groups

The `renamedg` tool enables you to change the name of a cloned disk group. The disk group must be dismounted on all nodes in the cluster before running `renamedg` on the disk group.

`renamedg` renames a disk group using a two-step process:

1. Phase one
	This phase generates a configuration file to be used in phase two.
2. Phase two
	This phase uses the configuration file to perform the renaming of the disk group.

The syntax is:

  
`renamedg` { `-help` | `help=true` }  
  
`renamedg`  
 \[`phase` ={ `one` | `two` | `both` } \] `dgname=` `diskgroup`  
 `newdgname=` `newdiskgroup` \[`config=` `configfile`\]  
 \[ `asm_diskstring=` `discoverystring``,` `discoverystring`... \]  
 \[ `clean=` { `true` | `false` } \] \[ `check=` { `true` | `false` } \]  
 \[ `confirm=` { `true` | `false` }\] \[ `verbose=` { `true` | `false` } \]  
 \[ `keep_voting_files=` { `true` | `false` }\]  
- `phase=` { `one` | `two` | `both` }
	Specifies the phase to be run. Allowed values are `one`, `two`, or `both`. This argument is optional. The default is `both`.
	Typically you would run both phases. If a problem occurs during the second phase, then you can re-run phase `two` using the generated configuration file.
- `dgname=` `diskgroup`
	Specifies the name of the disk group that to be renamed.
- `newdgname=` `newdiskgroup`
	Specifies the new name for the disk group.
- `config=` `configfile`
	Specifies the path to the configuration file to be generated during phase one or specifies the path to the configuration file to be used during phase two.
	This argument is optional. The default configuration file is named `renamedg_config` and is located in the directory in which the command is run. The single quotations may be required on some platforms.
- `asm_diskstring=` `discoverystring``,` `discoverystring`...
	Specifies the Oracle ASM discovery strings. The `asm_diskstring` value must be specified if the Oracle ASM disks are not in the default location for the platform. The single quotations may be required on some platforms, usually when wildcard characters are specified.
- `clean=` { `true` | `false` }
	Specifies whether to tolerate errors that are otherwise ignored. The default is `true`.
- `check=` { `true` | `false` }
	Specifies a boolean value that is used in the second phase. If `true`, then the tool prints the list of changes that are to be made to the disks. No writes are issued. It is an optional parameter that defaults to `false`.
- `confirm=` { `true` | `false` }
	Specifies a boolean value that is used in the second phase. If `false`, then the tool prints the changes that are to be made and seeks confirmation before actually making the changes. It is an optional value that defaults to `false`. If check is set to `true`, then the value of this parameter is redundant.
- `verbose=` { `true` | `false` }
	Specifies verbose execution when `verbose=true`. The default is `false`.
- `keep_voting_files=` { `true` | `false` }
	Specifies whether voting files are kept in the renamed disk group. The default is `false` which deletes the voting files from the renamed disk group.

Note:

`renamedg` does not update resources, nor does `renamedg` update any file references within the database. Because of this behavior, the original disk group resource is not automatically deleted after the completion of phase `two`. The status of the old disk group resource can be checked with the Oracle Clusterware Control (CRSCTL) `crsctl` `stat` `res` `-t` command and then manually deleted with the Server Control Utility (SRVCTL) `srvctl` `remove` `diskgroup` command.

Example 4-12 shows several examples of the use of `renamedg`. The first example renames the `data` disk group to `new_data` using a disk string to locate the disks and the `verbose` option is enabled. The second example only creates a configuration file during the completion of phase `one` of the `renamedg` operation. The third example runs phase `two` of the `renamedg` operation using a configuration file generated from a phase `one` execution of `renamedg`.

Example 4-12 Using renamedg

```
$ renamedg dgname=data newdgname=new_data asm_diskstring='/devices/disk*'
      verbose=true

$ renamedg phase=one dgname=data newdgname=new_data
      asm_diskstring='/devices/disk*' config=/tmp/data2.conf verbose=true

$ renamedg phase=two dgname=data newdgname=new_data config=/tmp/data2.conf
      verbose=true
```