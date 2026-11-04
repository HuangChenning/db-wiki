---
title: "Administrator's Guide"
book: "Automatic Storage Management Administrator's Guide"
doc_id: F30296-05
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/ostmg/manage-diskgroup-attributes.html
tags:
  - oracle
  - 21c
  - automatic-storage-management-administrators-guide
---

Disk group attributes are parameters that are bound to a disk group, rather than an Oracle ASM instance. Some disk group attributes can be set when a disk group is created or altered. Other disk attributes can only be set when a disk group is created or only be set when a disk group is altered.

This section contains the following topics:

- About Viewing and Setting Disk Group Attributes
- Summary of Disk Group Attributes

In addition to the disk group attributes listed in this section, template attributes are also assigned to a disk group. For information about template attributes, see [Managing Disk Group Templates](asm-files-directories-templates.md).

### About Viewing and Setting Disk Group Attributes

You can set and display disk group attribute settings.

You can display disk group attributes with the `V$ASM_ATTRIBUTE` view and the ASMCMD `lsattr` command.

Disk group attributes can be set with the `ATTRIBUTE` clause of the `ALTER` `DISKGROUP` or `CREATE` `DISKGROUP` SQL statement and the ASMCMD `setattr` and `mkdg` commands.

See Also:

- [Example 6-1](views-asm-info.md) for an example of the use of the `V$ASM_ATTRIBUTE` view
- [lsattr](asmcmd-diskgroup-commands.md) for information about the `lsattr` command
- [setattr](asmcmd-diskgroup-commands.md) for information about the `setattr` command
- [mkdg](asmcmd-diskgroup-commands.md) for information about the `mkdg` command
- [Managing Disk Groups with ASMCA](manage-asm-asmca.md) for information about setting disk group attributes with Oracle ASM Configuration Assistant (ASMCA)

### Summary of Disk Group Attributes

The Oracle ASM disk group attributes are listed in this section.

#### ACCESS\_CONTROL.ENABLED

This attribute configures Oracle ASM File Access Control and can only be set when altering a disk group.

For information about the `ACCESS_CONTROL.ENABLED` attribute, see [Setting Disk Group Attributes for Oracle ASM File Access Control](asm-access-control-diskgroups.md).

#### ACCESS\_CONTROL.UMASK

This attribute configures Oracle ASM File Access Control and can only be set when altering a disk group.

For information about the `ACCESS_CONTROL.UMASK` attribute, see [Setting Disk Group Attributes for Oracle ASM File Access Control](asm-access-control-diskgroups.md).

#### AU\_SIZE

This attribute specifies allocation unit (AU) size and can only be set when creating a disk group. [Example 4-1](create-diskgroups.md) shows how the `AU_SIZE` is specified with the `CREATE` `DISKGROUP` SQL statement.

For information about allocation units, refer to [About Oracle ASM Allocation Units](asm-intro.md).

#### CELL.SMART\_SCAN\_CAPABLE

This attribute is only applicable to the configuration of Oracle Exadata storage.

See Also:

Oracle Exadata documentation

#### CELL.SPARSE\_DG

This attribute is only applicable to the configuration of Oracle Exadata storage.

See Also:

Oracle Exadata documentation

#### COMPATIBLE.ASM

This attribute specifies the Oracle ASM compatibility level of a disk group. Compatibility attributes can be set when the disk group is created and advanced when a disk group is altered, but compatibility attributes cannot be reversed. For information about the `COMPATIBLE.ASM` attribute, refer to [Disk Group Compatibility Attributes](diskgroup-compatibility.md).

#### COMPATIBLE.RDBMS

This attribute specifies the database compatibility level of a disk group. Compatibility attributes can be set when the disk group is created and advanced when a disk group is altered, but compatibility attributes cannot be reversed. For information about the `COMPATIBLE.RDBMS` attribute, refer to [Disk Group Compatibility Attributes](diskgroup-compatibility.md).

#### COMPATIBLE.ADVM

This attribute specifies the Oracle Advanced Cluster File System (Oracle ACFS) and Oracle ASM Dynamic Volume Manager (Oracle ADVM) compatibility level of a disk group. Compatibility attributes can be set when the disk group is created and advanced when a disk group is altered, but compatibility attributes cannot be reversed. For information about the `COMPATIBLE.ADVM` attribute, refer to [Disk Group Compatibility Attributes](diskgroup-compatibility.md).

See Also:

[Oracle Automatic Storage Management Cluster File System Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ACFSG-GUID-7783FE8B-3BAD-4C4F-83C5-DF1426340290) for more information about Oracle ACFS and Oracle ADVM

#### CONTENT.CHECK

The `CONTENT.CHECK` attribute enables or disables content checking when performing data relocation operations for a disk group.

The attribute value can be set to `true` (enabled) or `false` (disabled).

When `CONTENT.CHECK` is enabled, an Oracle ASM relocation process (rebalance, resync, or resilver) detects corruptions during a data copy operation and performs automatic block corruption recovery by replacing these corruptions with an uncorrupted mirror copy if one is available.

The content check process detects and repairs corruptions for situations when the I/O operation is successful, but the blocks have invalid content. The process also performs a Hardware Assisted Resilient Data (HARD) check for all supported files and a block header check for data files.

This attribute can only be set when altering a disk group.

See Also:

[Manually Rebalancing Disk Groups](alter-diskgroups.md) and [Tuning Rebalance Operations](alter-diskgroups.md) for information about disk group rebalancing

#### CONTENT.TYPE

This attribute identifies the disk group type: `data`, `recovery`, or `system`. The type value determines where Oracle ASM places the nearest neighbor disk in the failure group where Oracle ASM mirrors copies of the data. Oracle ASM uses this attribute value to make it less likely that a double failure in the storage medium causes disk groups of different content types to become unavailable. Specifying this attribute enables Oracle ASM to better deploy all disk groups in the available storage.

The default value is `data` which specifies a distance of 1 to the nearest neighbor disk. A value of `recovery` specifies a distance of 3 to the nearest neighbor disk and a value of `system` specifies a distance of 5.

The attribute can be specified when creating or altering a disk group. If `CONTENT.TYPE` attribute is set or changed using `ALTER` `DISKGROUP`, then the new configuration does not take effect until a disk group rebalance is explicitly run.

The `CONTENT.TYPE` attribute is only valid for disk groups that are set to normal or high redundancy. The `COMPATIBLE.ASM` attribute must be set to `11.2.0.3` or higher to enable the `CONTENT.TYPE` attribute for the disk group.

This attribute can be set with ASMCMD `mkdg` or SQL `CREATE` and `ALTER` `DISKGROUP` statements.

For example:

```
SQL> CREATE DISKGROUP data NORMAL REDUNDANCY
        FAILGROUP controller1 DISK
        '/devices/diska1' NAME diska1,
...
        ATTRIBUTE 
        'compatible.asm' = '12.1.0.1', 
        'content.type' = 'recovery',
...

SQL> ALTER DISKGROUP data SET ATTRIBUTE 'content.type' = 'data';
```

This attribute is primarily intended for use with Oracle Exadata storage.

For information about disk resync, see [Oracle ASM Fast Mirror Resync](mirroring-diskgroup-redundancy.md).

See Also:

- Oracle Exadata documentation
- [My Oracle Support](https://support.oracle.com/) ([`https://support.oracle.com`](https://support.oracle.com/)) for information about using the `CONTENT.TYPE` attribute with Oracle Exadata storage

#### CONTENT\_HARDCHECK.ENABLED

The `CONTENT_HARDCHECK.ENABLED` disk group attribute enables or disables Hardware Assisted Resilient Data (HARD) checking when performing data copy operations for rebalancing a disk group.

The attribute value can be set to `true` or `false`. This attribute can only be set when altering a disk group.

- When the `CONTENT.CHECK` disk group attribute is set to enabled (`true`), the setting of `CONTENT_HARDCHECK.ENABLED` is ignored and checking is done on the content of user data, including HARD checks.
- When the `CONTENT.CHECK` attribute is set to disabled (`false`) and the `CONTENT_HARDCHECK.ENABLED` attribute is set to enabled (`true`), only HARD checking is performed.
- When the `CONTENT.CHECK` attribute is set to disabled (`false`) and the `CONTENT_HARDCHECK.ENABLED` attribute is set to disabled (`false`), no checking is performed.

See Also:

[Manually Rebalancing Disk Groups](alter-diskgroups.md) and [Tuning Rebalance Operations](alter-diskgroups.md) for information about disk group rebalancing

#### DISK\_REPAIR\_TIME

This attribute specifies the time interval to repair a disk and bring it back online before initiating the drop operation. This attribute can only be set when altering a disk group and is only applicable to normal and high redundancy disk groups.

For information about disk repair time, see [Oracle ASM Fast Mirror Resync](mirroring-diskgroup-redundancy.md).

#### FAILGROUP\_REPAIR\_TIME

This attribute specifies a default repair time for the failure groups in the disk group. The failure group repair time is used if Oracle ASM determines that an entire failure group has failed. The default value is 24 hours (`24h`). If there is a repair time specified for a disk, such as with the `DROP` `AFTER` clause of the SQL `ALTER` `DISKGROUP` `OFFLINE` `DISK` statement, that disk repair time overrides the failure group repair time.

This attribute can only be set when altering a disk group and is only applicable to normal and high redundancy disk groups.

For information about failure group repair time, see [Oracle ASM Fast Mirror Resync](mirroring-diskgroup-redundancy.md).

#### IDP.BOUNDARY and IDP.TYPE

Note:

The Intelligent Data Placement (IDP) feature has been deprecated since Oracle ASM 12c Release 2 (12.2) and is planned for desupport in a future release.

These attributes are used to configure Oracle Exadata storage.

See Also:

Oracle Exadata documentation

#### LOGICAL\_SECTOR\_SIZE

The `LOGICAL_SECTOR_SIZE` disk group attribute specifies the logical sector size for a disk group. The value can be set when creating or altering a disk group.

The value of `LOGICAL_SECTOR_SIZE` specifies the smallest unit of I/O allowed on the disk group. The value must be less than or equal to the size of the `SECTOR_SIZE` disk group attribute.

`COMPATIBLE.ASM` must be set to `12.2` or greater to use the `LOGICAL_SECTOR_SIZE` disk group attribute.

For information about setting the `LOGICAL_SECTOR_SIZE` disk group attribute, see [Specifying the Logical and Physical Sector Size](create-diskgroups.md).

For information about the `SECTOR_SIZE` disk group attribute, refer to SECTOR\_SIZE.

#### PHYS\_META\_REPLICATED

This disk group attribute tracks the replication status of a disk group. When the Oracle ASM compatibility of a disk group is advanced to 12.1 or higher, the physical metadata of each disk is replicated. This metadata includes the disk header, free space table blocks, and allocation table blocks. The replication is performed online asynchronously. This attribute value is set to `true` by Oracle ASM if the physical metadata of every disk in the disk group has been replicated.

This disk group attribute is only defined in a disk group with the Oracle ASM disk group compatibility (`COMPATIBLE.ASM`) set to `12.1` and higher. This attribute is read-only and is intended for information only. A user cannot set or change its value. The values are either `true` or `false`.

#### PREFERRED\_READ.ENABLED

In an Oracle extended cluster, which contains nodes that span multiple physically separated sites, the `PREFERRED_READ.ENABLED` disk group attribute controls whether preferred read functionality is enabled for a disk group.

If preferred read functionality is enabled, then this functionality enables an instance to determine and read from disks at the same site as itself, which can improve performance.

Each Oracle ASM instance in an Oracle extended cluster has the information to determine the site in which it is located. If preferred read functionality is enabled, then based on the site information, the preferred status for a disk is determined to be true if the disk is in the same site as the instance. Otherwise, if the disk is not located at the same site as the Oracle ASM instance, the preferred status for a disk is set to false.

For extended clusters, the preferred read setting is enabled by default with a `TRUE` setting for the `PREFERRED_READ.ENABLED` disk group attribute of each disk group. For clusters that are not extended (only one physical site), preferred read is disabled. Preferred read status applies to extended, normal, high, and flex redundancy disk groups.

Oracle Database 12c Release 2 (12.2) is required and `COMPATIBLE.ASM` must be set to `12.2` or greater to use `PREFERRED_READ.ENABLED`.

Whether or not `PREFERRED_READ.ENABLED` has been enabled, preferred read can be set at the failure group level on an Oracle ASM instance or a client instance in a cluster with the `ASM_PREFERRED_READ_FAILURE_GROUPS` initialization parameter, which is available for backward compatibility.

To determine whether a disk has preferred read status, you can check the `PREFERRED_READ` column of the `V$ASM_DISK` view.

See Also:

- [ASM\_PREFERRED\_READ\_FAILURE\_GROUPS](init-params-asm-instance.md) for information about the `ASM_PREFERRED_READ_FAILURE_GROUPS` initialization parameter
- [About Oracle ASM Extended Disk Groups](asm-filegroups.md) for information about Oracle ASM extended disk groups
- [Oracle Grid Infrastructure Installation and Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=CWGEN) for information about Oracle extended clusters
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=REFRN003) for information about all of the `V$ASM*` dynamic performance views

#### SCRUB\_ASYNC\_LIMIT

The `SCRUB_ASYNC_LIMIT` disk group attribute sets the maximum allowed outstanding parallel read requests for asynchronous scrubbing.

The range of values is `1` to `1024`. The default value is `1`.

`COMPATIBLE.ASM` must be set to `12.2` or greater to use this disk group attribute.

For information about the scrubbing operation, refer to [Scrubbing Disk Groups](alter-diskgroups.md).

#### SECTOR\_SIZE

The `SECTOR_SIZE` disk group attribute specifies the sector size for a disk group. The value can be set when creating or altering a disk group.

The value of `SECTOR_SIZE` is used for the block size of newly-created redo logs and Oracle ACFS file systems. The value can be changed to facilitate migration of disks to different sector sizes. The value must be greater than or equal to the size of the `LOGICAL_SECTOR_SIZE` disk group attribute.

`COMPATIBLE.ASM` must be set to `12.2` or greater to use the 12.2 functionality of `SECTOR_SIZE`, which includes the ability to alter the sector size after a disk group has been created.

For information about setting the `SECTOR_SIZE` disk group attribute, see [Specifying the Logical and Physical Sector Size](create-diskgroups.md).

For information about the `LOGICAL_SECTOR_SIZE` disk group attribute, refer to LOGICAL\_SECTOR\_SIZE.

#### STORAGE.TYPE

This disk group attribute specifies the type of the disks in the disk group. The possible values are `AXIOM`, `ZFSSA`, and `OTHER`. If the attribute is set to `AXIOM` or `ZFSSA`, then all disks in the disk group must be of that type. If the attribute is set to `OTHER`, then any types of disks can be in the disk group.

If the `STORAGE.TYPE` disk group attribute is set to `AXIOM` or `ZFSSA`, then functionality for Hybrid Columnar Compression (HCC) can be enabled for Pillar Axiom or ZFS storage.

Note:

Pillar Axiom storage must be added as SCSI/Fiber Channel.

To set the `STORAGE.TYPE` attribute, the `COMPATIBLE.ASM` and `COMPATIBLE.RDBMS` disk group attributes must be set to `11.2.0.3` or higher. For maximum support with ZFS storage, set the `COMPATIBLE.ASM` and `COMPATIBLE.RDBMS` disk group attributes to `11.2.0.4` or higher. For information about disk group compatibility attributes, refer to [Disk Group Compatibility](diskgroup-compatibility.md).

The `STORAGE.TYPE` attribute can be set when creating a disk group or when altering a disk group. The attribute cannot be set when clients are connected to the disk group. For example, the attribute cannot be set when an Oracle ADVM volume is enabled on the disk group.

The attribute is not visible in the `V$ASM_ATTRIBUTE` view or with the ASMCMD `lsattr` command until the attribute has been set.

See Also:

[Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=CNCPT89198) for more information about Hybrid Columnar Compression. Hybrid Columnar Compression is a feature of certain Oracle storage systems.

#### THIN\_PROVISIONED

This attribute enables or disables the functionality to discard unused storage space after a disk group rebalance is completed. The attribute value can be `true` to enable or `false` to disable the functionality. The default value is `false`.

Storage vendor products that support thin provisioning have the capability to reuse the discarded storage space for a more efficient overall physical storage utilization. Given such support from a storage vendor, when the `COMPACT` phase of a rebalance operation has completed, Oracle ASM informs the storage which space is no longer used and can be repurposed. If a rebalance is not running, you can issue a rebalance with the `ALTER` `DISKGROUP`... `REBALANCE` SQL statement.

Note:

The `THIN_PROVISIONED` attribute is supported only with Oracle ASM Filter Driver (Oracle ASMFD) in Oracle Grid Infrastructure 12.2 and later releases on Linux.

See Also:

- [Administering Oracle ASM Filter Driver](administer-filter-driver.md) for information about Oracle ASMFD
- [My Oracle Support](https://support.oracle.com/) ([`https://support.oracle.com`](https://support.oracle.com/)) for articles about Oracle ASM and Oracle ASMFD, such as notes 1369107.1 and 2034681.1, and additional articles about Oracle ASM and thin provisioning
- [Tuning Rebalance Operations](alter-diskgroups.md) for information about disk group rebalancing

#### VAM\_MIGRATION\_DONE

Virtual Allocation Metadata (VAM) supports flexible storage allocation. The `VAM_MIGRATION_DONE` disk group attribute must be enabled and the migration completed before migrating a `NORMAL` or `HIGH` redundancy disk group to a `FLEX` redundancy disk group without the use of a restrictive mount.