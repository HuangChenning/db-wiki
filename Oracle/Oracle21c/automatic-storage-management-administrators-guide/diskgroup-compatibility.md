---
title: "Administrator's Guide"
book: "Automatic Storage Management Administrator's Guide"
doc_id: F30296-05
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/ostmg/diskgroup-compatibility.html
tags:
  - oracle
  - 21c
  - automatic-storage-management-administrators-guide
---

This section describes disk group compatibility under the following topics:

### Overview of Disk Group Compatibility

Advancing the disk group compatibility settings enables you to use the new Oracle ASM features that are available in a later release. For example, a disk group with the disk group compatibility attributes set to `19.0` can take advantage of Oracle ASM 19c features. For information about the features enabled for combinations of compatibility attribute settings, refer to Table 4-4.

The disk group attributes that determine compatibility are `COMPATIBLE.ASM`, `COMPATIBLE.RDBMS`. and `COMPATIBLE.ADVM`. The `COMPATIBLE.ASM` and `COMPATIBLE.RDBMS` attribute settings determine the minimum Oracle Database software version numbers that a system can use for Oracle ASM and the database instance types respectively. For example, if the Oracle ASM compatibility setting is `19.0`, and RDBMS compatibility is set to `12.2.0.1`, then the Oracle ASM software version must be at least `19.0`, and the Oracle Database client software version must be at least `12.2.0.1`. The `COMPATIBLE.ADVM` attribute determines whether the Oracle ASM Dynamic Volume Manager feature can create a volume in a disk group.

When you create a disk group, you can specify the disk group compatibility attribute settings in the `CREATE` `DISKGROUP` SQL statement. The `ALTER` `DISKGROUP` SQL statement can update the compatible attribute settings for existing disk groups. For examples of valid combinations of compatible attribute settings, refer to Table 4-3.

You can also set and update disk group attributes with the ASMCMD `setattr` command. For information about the ASMCMD `setattr` command, refer to [setattr](asmcmd-diskgroup-commands.md).

Note:

- The disk group compatibility settings determine whether your environment can use the latest Oracle ASM features.
- The disk group compatibility settings can only be advanced; you cannot revert to a lower compatibility setting. For more information, refer to Reverting Disk Group Compatibility.
- The `COMPATIBLE.ASM` attribute must be advanced before advancing other disk group compatibility attributes and its value must be greater than or equal to the value of other disk group compatibility attributes.

### Disk Group Compatibility Attributes

The disk group compatibility attributes specify the disk group compatibility settings for Oracle ASM and database instances.

- COMPATIBLE.ASM
- COMPATIBLE.RDBMS
- COMPATIBLE.ADVM

Note:

Starting with Oracle ASM version 12.2.0.1, the minimum and default settings for Oracle ASM disk group attributes are:

- `COMPATIBLE.ASM` = `11.2.0.2` and `COMPATIBLE.RDBMS` = `10.1` for `EXTERNAL`, `NORMAL`, and `HIGH` redundancy disk groups
- `COMPATIBLE.ASM` = `12.2.0.1` and `COMPATIBLE.RDBMS` = `12.2.0.1` for `FLEX` and `EXTENDED` disk groups

The default and minimum values for Oracle ASM disk group attributes are present when using SQL\*Plus to create a disk group. Other utilities, such as ASMCA, may use a different default value when creating a disk group; however, the minimum value for Oracle ASM disk group attributes should be the same.

COMPATIBLE.ASM

The value for the disk group `COMPATIBLE`.`ASM` attribute determines the minimum software version for an Oracle ASM instance that can use the disk group. This setting also affects the format of the data structures for the Oracle ASM metadata on the disk. The format of other file contents is determined by Oracle ASM Dynamic Volume Manager (Oracle ADVM) and the database instance.

COMPATIBLE.RDBMS

The value for the disk group `COMPATIBLE.RDBMS` attribute determines the minimum `COMPATIBLE` database initialization parameter setting for any database instance that is allowed to use the disk group. Before advancing the `COMPATIBLE`.`RDBMS` attribute, ensure that the values for the `COMPATIBLE` initialization parameter for all of the databases that access the disk group are set to at least the value of the new setting for `COMPATIBLE`.`RDBMS`.

For example, if the `COMPATIBLE` initialization parameter of the databases is set to either `12.2`, then `COMPATIBLE.RDBMS` can be set to any value between `10.1` and `12.2` inclusively. If the `COMPATIBLE` initialization parameter of the databases is set to `19.0`, then `COMPATIBLE.RDBMS` can be set to any value between `10.1` and `19.0` inclusively.

Note:

The database initialization parameter `COMPATIBLE` enables you to use a new release of Oracle Database, while at the same time guaranteeing backward compatibility with an earlier release. For more information about the `COMPATIBLE` initialization parameter, refer to [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=REFRN10019).

COMPATIBLE.ADVM

The value for the disk group `COMPATIBLE.ADVM` attribute determines whether the disk group can contain Oracle ADVM volumes. The value must be set to `11.2` or higher. Before setting this attribute, the `COMPATIBLE.ASM` value must be `11.2` or higher. Also, the Oracle ADVM volume drivers must be loaded in the supported environment.

The default value of the `COMPATIBLE.ADVM` attribute depends on the level of the Oracle ASM release.

See Also:

[Oracle Automatic Storage Management Cluster File System Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ACFSG-GUID-7783FE8B-3BAD-4C4F-83C5-DF1426340290) for more information about Oracle ACFS and Oracle ADVM

### Setting Disk Group Compatibility Attributes

This section discusses the settings of the disk group compatibility attributes and how to set the attribute values with the `CREATE` `DISKGROUP` or `ALTER` `DISKGROUP` SQL statement.

This section contains these topics:

- Valid Combinations of Compatibility Attribute Settings
- Using CREATE DISKGROUP with Compatibility Attributes
- Using ALTER DISKGROUP with Compatibility Attributes
- Viewing Compatibility Attribute Settings
- Reverting Disk Group Compatibility

You can also set the disk group compatibility settings withOracle ASM command-line utility (ASMCMD) and Oracle ASM Configuration Assistant (ASMCA). Refer to [Managing Oracle ASM With ASMCA](manage-asm-asmca.md) and [Managing Oracle ASM with ASMCMD](manage-asm-asmcmd.md) .

Note:

Advancing the values for disk group compatibility attributes is an irreversible operation. See Reverting Disk Group Compatibility.

#### Valid Combinations of Compatibility Attribute Settings

When setting the values for the disk group attributes, specify at least the major and minor versions of a valid Oracle Database release number. For example, you can specify compatibility as `12.2` or `19.0`; Oracle assumes that any missing version number digits are zeros.

Oracle ASM features enabled for combinations of attribute settings are shown in Features Enabled By Disk Group Compatibility Attribute Settings.

Table 4-3 shows some valid combinations of the disk group compatibility attributes and the valid Oracle ASM and database instance versions for each combination.

Table 4-3 Examples of disk group compatibility attribute settings

| COMPATIBLE.ASM | COMPATIBLE.RDBMS | COMPATIBLE.ADVM | Oracle ASM Instance Version | COMPATIBLE Setting for RDBMS Instance |
| --- | --- | --- | --- | --- |
| 12.1 | 12.1 | 12.1 | \>= 12.1 | \>= 12.1 |
| 12.2 | 12.1 | 12.2 | \>= 12.2 | \>= 12.1 |
| 18.0 | 18.0 | 18.0 | \>= 18.0 | \>= 18.0 |
| 19.0 | 19.0 | 19.0 | \>=19.0 | \>=19.0 |
| 21.0 | 21.0 | 21.0 | \>=21.0 | \>=21.0 |

These are some possible combinations of Oracle ASM and database releases:

- The database release is Oracle Database 11g Release 2 (11.2) (database initialization parameter `COMPATIBLE` is set to `11.2`) and the Oracle ASM release is Oracle ASM 11g Release 2 (11.2). The `COMPATIBLE.ASM` and `COMPATIBLE.RDBMS` disk group attributes are set to `10.2` for a disk group.
	The Oracle ASM disk group functionality remains at Oracle Database 10g Release 2 (10.2).
- The database release is Oracle Database 10g Release 1 (10.1) and the Oracle ASM release is 11.2. `COMPATIBLE.ASM` is set to `11.2` and `COMPATIBLE.RDBMS` is set to `10.1` for a disk group.
- The database release is Oracle Database 12c Release 2 (12.2) (database initialization parameter `COMPATIBLE` is set to `12.2`) and the Oracle ASM release is Oracle ASM 12c Release 2 (12.2). All the disk group compatibility attributes are set to `12.2` for a disk group.

Oracle ASM in a Domain Services Cluster and Oracle Database in a Member Cluster Configuration

Note:

Starting with Oracle Grid Infrastructure 21c, Member Clusters, which are part of the Oracle Cluster Domain architecture, are desupported. However, Domain Services Clusters continues to support Members Clusters in releases previous to Oracle Grid Infrastructure 21c.

Note:

Starting with Oracle Grid Infrastructure 21c, Domain Services Cluster (DSC), which is part of the Oracle Cluster Domain architecture, is deprecated and can be desupported in a future release.

Oracle ASM or Oracle IOServer running in a Domain Services Cluster (DSC) version 19.1 support Oracle Database and Oracle Grid Infrastructure running in Member Cluster versions 12.2 and 19.1.

Oracle ASM or Oracle IOServer running in a Domain Services Cluster (DSC) version 12.2 support Oracle Database and Oracle Grid Infrastructure running in Member Cluster versions 12.2 and 19.1.

An Oracle Database instance must be a version lower than or equal to the Oracle ASM version in the same cluster. However, this requirement is not strictly enforced when the database instance is connecting from a different cluster.

#### Using CREATE DISKGROUP with Compatibility Attributes

You can specify the compatibility settings for a disk group with the `CREATE` `DISKGROUP` statement when creating the disk group.

The following example creates a normal redundancy disk group `data1` with the Oracle ASM compatibility set to `19.0` and the RDBMS compatibility set to the default (the `COMPATIBLE.RDBMS` default is less than or equal to `19.0`):

```
CREATE DISKGROUP data1 DISK '/dev/sd*' 
       ATTRIBUTE 'compatible.asm' = '19.0';
```

The following example creates a normal redundancy disk group `data2` with the ASM, RDBMS, and ADVM compatibility set to `19.0`:

```
CREATE DISKGROUP data2 DISK '/dev/sd*' 
       ATTRIBUTE 'compatible.asm' = '19.0', 'compatible.rdbms' = '19.0',
                 'compatible.advm' = '19.0';
```

#### Using ALTER DISKGROUP with Compatibility Attributes

After a disk group has been created, you can use the `ALTER` `DISK` `GROUP` SQL statement to change the compatibility attributes. The `ALTER` `DISK` `GROUP` SQL statement ensures that Oracle can advance the compatibility of the specified disk group before committing the change.

All of the affected databases and file systems should be online when running `ALTER` `DISKGROUP` to ensure that advancing compatibility does not reduce the database and file system access. When advancing disk group compatibility, you must advance the `COMPATIBLE`.`ASM` attribute before the `COMPATIBLE`.`RDBMS` or `COMPATIBLE.ADVM` attribute to ensure a valid combination of compatible attribute settings as shown in Table 4-3. You can advance only one compatibility attribute in a single `ALTER` `DISKGROUP` statement.

The following example advances the Oracle ASM compatibility for disk group `data3` to `19.0`. An Oracle ASM instance must be at Oracle ASM 19c or higher to access the `data3` disk group.

```
ALTER DISKGROUP data3 SET ATTRIBUTE 'compatible.asm' = '19.0';
```

The following example advances the `COMPATIBLE.RDBMS` and `COMPATIBLE.ADVM` compatibility attributes of the disk group `data3` to `10.0`. This example assumes that the value of `COMPATIBLE.ASM` is set to `19.0`.

```
ALTER DISKGROUP data3 SET ATTRIBUTE 'compatible.rdbms' = '19.0',
ALTER DISKGROUP data3 SET ATTRIBUTE 'compatible.advm' = '19.0';
```

#### Viewing Compatibility Attribute Settings

You can view the disk group compatibility settings in the `V$ASM_ATTRIBUTE` view. However, the `V$ASM_ATTRIBUTE` view does not display any rows when the `COMPATIBLE.ASM` value is set to `10.1`. Instead you can determine the values for the `COMPATIBLE.ASM` and `COMPATIBLE.RDBMS` disk group compatibility attributes with the `COMPATIBILITY` and `DATABASE_COMPATIBILITY` columns of the `V$ASM_DISKGROUP` view.

You can also display the disk group compatibility attributes with the ASMCMD command `lsattr`.

See Also:

- [Example 6-1](views-asm-info.md) for an example querying the `V$ASM_ATTRIBUTE` view
- [lsattr](asmcmd-diskgroup-commands.md) for information about the ASMCMD `lsattr` command
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=SQLRF01114) for information about disk group attributes
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=REFRN003) for details on the `V$ASM_DISKGROUP` and `V$ASM_ATTRIBUTE` dynamic performance views

#### Reverting Disk Group Compatibility

You cannot revert disk group compatibility to a previous values. Instead you must create a new disk group.

Advancing the values for disk group compatibility attributes is an irreversible operation. If you advance the disk group compatibility settings, you cannot change the values back to the previous settings. To revert to the previous values, you must create a new disk group with the old compatibility attribute settings and then restore the database files that were in the disk group to the new disk group.

When you revert to a new disk group with the old compatibility attribute settings, the latest Oracle ASM features might not be available. For example, if you revert the disk group compatibility to a pre-11.2 value, Oracle ACFS functionality is not available.

For example, you could perform the following procedure to revert a disk group to previous compatibility settings:

1. If the Oracle ASM SPFILE is in the disk group, move this SPFILE out of the disk group:
	1. Connect with SQL\*Plus to the Oracle ASM instance.
		2. Create a PFILE in the file system.
		For example:
		```
		SQL> CREATE PFILE '$ORACLE_HOME/dbs/asmspfile.ora' FROM SPFILE;
		```
2. If the OCR and voting files are in the disk group, move them out of this disk group.
3. Back up any files that must be saved.
	1. Back up the database files.
		2. If an Oracle ACFS file system is mounted on an Oracle ADVM volume on the disk group, the operating system files in the file system must be backed up or copied to a location outside the file system mount point.
4. Create a new disk group using SQL `CREATE` `DISKGROUP` specifying the previous values for the disk group attribute settings.
5. Move or restore the database files into the newly created disk group using either the `ALTER` `DATABASE` `MOVE` `DATAFILE` SQL statement or Recovery Manager (RMAN).
6. Drop the disk group with the advanced disk group compatibility settings using SQL `DROP` `DISKGROUP` `INCLUDING` `CONTENTS` to remove the disk group and its contents. This SQL statement also removes any Oracle ACFS file system and its contents.

See Also:

- [About Creating a Disk Group](create-diskgroups.md) for information about creating a disk group
- [Moving Data Files Between Disk Groups With ALTER DATABASE](asm-files-directories-templates.md) for information about moving data files between disk groups
- [Moving Data Files Between Oracle ASM Disk Groups Using RMAN](asm-migration-rman.md) for information about moving database files with RMAN
- [Dropping Disk Groups](maintain-diskgroups.md) for information about dropping a disk group
- [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=CWADD838) for information about administering OCR and voting files
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ADMIN11430) for information about using the `ALTER` `DATABASE` `MOVE` `DATAFILE` SQL statement to move data files between Oracle ASM disk groups

### Features Enabled By Disk Group Compatibility Attribute Settings

This topic describes the Oracle ASM features enabled by valid combinations of the disk group compatibility attribute settings.

The following list applies to Oracle ASM features enabled by valid combinations of the disk group compatibility attribute settings.

- The value of `COMPATIBLE.ASM` must always be greater than or equal to the value of `COMPATIBLE.RDBMS` and `COMPATIBLE.ADVM`.
- Starting with Oracle Grid Infrastructure 12.2.0.1 software, the minimum setting for `COMPATIBLE.ASM` is `11.2.0.2`.
- A value of not applicable (n/a) means that the setting of the attribute has no effect on the feature.
- Oracle ASM features not explicitly listed in the following table do not require advancing the disk group compatibility attribute settings.
- Oracle ASM features explicitly identified by an operating system in the following table are available on that operating system starting with the associated disk group attribute settings.
- If encryption is configured for the first time on Oracle ASM 11g Release 2 (11.2.0.3) on Linux or if encryption parameters must be changed or a new volume encryption key must be created following a software upgrade to Oracle ASM 11g Release 2 (11.2.0.3) on Linux, then the disk group compatibility attributes for `ASM` and `ADVM` must be set to `11.2.0.3` or higher.
- Oracle ACFS does not support encryption or replication with the following: Oracle Database data files, control files, online redo logs, archived redo log files, flashback logs, RMAN backups, and Oracle Data Pump dump file sets.
- Oracle ACFS on Oracle Exadata storage is supported starting with Oracle Grid Infrastructure 12.1.0.2 on Linux.
- There may also be minimum requirements for the database `COMPATIBLE` initialization parameter.

Table 4-4 Oracle ASM features enabled by disk group compatibility attribute settings

| Disk Group Features Enabled | COMPATIBLE.ASM | COMPATIBLE.RDBMS | COMPATIBLE.ADVM |
| --- | --- | --- | --- |
| Support for larger AU sizes (32 or 64 MB) | \>= 11.1 | \>= 11.1 | n/a |
| Attributes are displayed in the `V$ASM_ATTRIBUTE` view | \>= 11.1 | n/a | n/a |
| Fast mirror resync | \>= 11.1 | \>= 11.1 | n/a |
| Variable size extents | \>= 11.1 | \>= 11.1 | n/a |
| Exadata storage | \>= 11.1.0.7 | \>= 11.1.0.7 | n/a |
| OCR and voting files in a disk group | \>= 11.2 | n/a | n/a |
| Sector size set to nondefault value | \>= 11.2 | \>= 11.2 | n/a |
| Oracle ASM SPFILE in a disk group | \>= 11.2 | n/a | n/a |
| Oracle ASM File Access Control | \>= 11.2 | \>= 11.2 | n/a |
| `ASM_POWER_LIMIT` value up to `1024` | \>= 11.2.0.2 | n/a | n/a |
| Content type of a disk group | \>= 11.2.0.3 | n/a | n/a |
| Appliance mode for Oracle Exadata (no fixed partnering) | \>= 11.2.0.4 | n/a | n/a |
| Replication status of a disk group | \>= 12.1 | n/a | n/a |
| Managing a shared password file in a disk group | \>= 12.1 | n/a | n/a |
| Greater than 2 TB Oracle ASM disks without Oracle Exadata storage | \>= 12.1 | \>= 12.1 | n/a |
| Fixed partnering for Oracle Exadata | \>= 12.1.0.2 | n/a | n/a |
| Appliance mode for Oracle Data Appliance (ODA) | \>= 12.1.0.2 | n/a | n/a |
| Support for Oracle Exadata sparse disk groups | \>= 12.1.0.2 | \>= 12.1.0.2 | n/a |
| Support for resync checkpoint | \>= 12.1.0.2 | \>= 12.1.0.2 | n/a |
| `LOGICAL_SECTOR_SIZE` | \>= 12.2 | n/a | n/a |
| Altering sector size | \>= 12.2 | n/a | n/a |
| Oracle ASM flex and extended disk groups | \>= 12.2 | \>= 12.2 | n/a |
| `SCRUB_ASYNC_LIMIT` | \>= 12.2 | n/a | n/a |
| `PREFERRED_READ.ENABLED`  Oracle Database 12c Release 2 (12.2) is required. | \>=12.2 | n/a | n/a |
| Converting normal or high redundancy disk groups to flex disk groups without restricted mount | \>=18.0 | \>=12.2 | n/a |
| Oracle ASM flex disk group support for multitenant cloning | \>=18.0 | \>=18.0 | n/a |
| Storage conversion for member clusters | \>=18.0 and <21.0 | n/a | n/a |
| Virtual Allocation Metadata (VAM) enabled on non-sparse normal and high redundancy disk groups | \>=18.0 | n/a | n/a |
| Support for single parity protection in Oracle ASM flex disk groups  The database `COMPATIBLE` initialization parameter must be set to 19.1 or greater. | \>=19.1 | n/a | n/a |
| Support for double parity protection in Oracle ASM flex disk groups  The database `COMPATIBLE` initialization parameter must be set to 19.5 or greater. | \>=19.5 | n/a | n/a |

See Also:

- [Oracle Automatic Storage Management Cluster File System Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ACFSG-GUID-A4ACA26F-5C02-4AFB-B7FA-E114A13DDE11) for information about Oracle ACFS features enabled by disk group compatibility settings
- [Oracle Automatic Storage Management Cluster File System Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ACFSG-GUID-7783FE8B-3BAD-4C4F-83C5-DF1426340290) for more information about Oracle ACFS and Oracle ADVM, including any limitations or restrictions, about storing data files in an Oracle ACFS file system
- [ASM\_POWER\_LIMIT](init-params-asm-instance.md) for information about the rebalancing process and the `ASM_POWER_LIMIT` initialization parameter

### Considerations When Setting Disk Group Compatibility

If you advance disk group compatibility, then you could enable the creation of files that are too large to be managed by a previous release of Oracle Database.

For example, you must be aware of the file size limits because replicated sites cannot continue using the software from a previous release to manage these large files. The disk group compatibility settings should be the same for all replicated environments.

Table 4-5 shows the maximum Oracle ASM file sizes supported for multiple `COMPATIBLE.RDBMS` settings with the `AU_SIZE` disk group attribute set to 1 MB. This table shows that Oracle Database 10g can only support a file size of up to 16 TB for external redundancy. If you advance the `COMPATIBILE.RDBMS` attribute to `11.1` or greater, then a file can grow beyond 16 TB. However, the larger size causes the file to be unusable in a replicated and disaster recovery site if the disaster recovery site has a disk group `COMPATIBLE.RDBMS` setting that is incompatible with the larger size.

Table 4-5 Maximum Oracle ASM file sizes for disk groups with AU\_SIZE set to 1 MB

| Redundancy | COMPATIBLE.RDBMS = 10.1 | COMPATIBLE.RDBMS >= 11.1 |
| --- | --- | --- |
| External | 16 TB | 128 TB |
| Normal | 5.8 TB | 93 TB |
| High | 3.9 TB | 62 TB |

Table 4-6 shows the maximum Oracle ASM file sizes supported for multiple `COMPATIBLE.RDBMS` settings with the `AU_SIZE` disk group attribute set to 4 MB.

Table 4-6 Maximum Oracle ASM file sizes for disk groups with AU\_SIZE set to 4 MB

| Redundancy | COMPATIBLE.RDBMS = 10.1 | COMPATIBLE.RDBMS >= 11.1 |
| --- | --- | --- |
| External | 64 TB | 128 TB |
| Normal | 32 TB | 128 TB |
| High | 21 TB | 128 TB |

Note:

The 128 TB limit under the COMPATIBLE.RDBMS >= 11.1 column in tables Table 4-5 and Table 4-6 is not a limit specific to Oracle ASM. The limit is specific to the database data file, which is calculated as 2^2 \* logical block size. The block size can be at most 32 KB, or 2^5. The resulting calculation is 2^2 \* 2^5 = 2^7, or 128 TB.

See Also:

- [Oracle ASM Storage Limits](performance-scability-diskgroup.md) for information about Oracle ASM storage sizes
- [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=UPGRD005) for information about database compatibility
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ADMIN002) for information about the `COMPATIBLE` initialization parameter and irreversible compatibility
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=REFRN10019) for information about the `COMPATIBLE` initialization parameter