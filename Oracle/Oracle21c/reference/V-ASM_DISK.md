---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ASM_DISK.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.56 V$ASM\_DISK

`V$ASM_DISK` displays one row for every disk discovered by the Oracle Automatic Storage Management (Oracle ASM) instance, including disks that are not part of any disk group.

| Column | Datatype | Description |
| --- | --- | --- |
| `GROUP_NUMBER` | `NUMBER` | Number of the disk group containing the disk (foreign key to the `V$ASM_DISKGROUP` view) |
| `DISK_NUMBER` | `NUMBER` | Number assigned to the disk within its disk group |
| `COMPOUND_INDEX` | `NUMBER` | A 32-bit number consisting of a disk group number in the high-order 8 bits and a disk number in the low-order 24 bits (for efficient access to the view) |
| `INCARNATION` | `NUMBER` | Incarnation number for the disk |
| `MOUNT_STATUS` | `VARCHAR2(7)` | Per-instance status of the disk relative to group mounts:  - `MISSING` - Oracle ASM metadata indicates that the disk is known to be part of the Oracle ASM disk group but no disk in the storage system was found with the indicated name - `CLOSED` - Disk is present in the storage system but is not being accessed by Oracle ASM - `OPENED` - Disk is present in the storage system and is being accessed by Oracle ASM. This is the normal state for disks in a database instance which are part of a disk group being actively used by the instance. - `CACHED` - Disk is present in the storage system and is part of a disk group being accessed by the Oracle ASM instance. This is the normal state for disks in an Oracle ASM instance which are part of a mounted disk group. - `IGNORED` - Disk is present in the system but is ignored by Oracle ASM because of one of the following: 	- The disk is detected by the system library but is ignored because an Oracle ASM library discovered the same disk 		- Oracle ASM has determined that the membership claimed by the disk header is no longer valid - `CLOSING` - Oracle ASM is in the process of closing this disk |
| `HEADER_STATUS` | `VARCHAR2(12)` | Per-instance status of the disk as seen by discovery:  - `UNKNOWN` - Oracle ASM disk header has not been read - `CANDIDATE` - Disk is not part of a disk group and may be added to a disk group with the `ALTER DISKGROUP` statement - `INCOMPATIBLE` - Version number in the disk header is not compatible with the Oracle ASM software version - `PROVISIONED` - Disk is not part of a disk group and may be added to a disk group with the `ALTER DISKGROUP` statement. The `PROVISIONED` header status is different from the `CANDIDATE` header status in that `PROVISIONED` implies that an additional platform-specific action has been taken by an administrator to make the disk available for Oracle ASM. - `MEMBER` - Disk is a member of an existing disk group. No attempt should be made to add the disk to a different disk group. The `ALTER DISKGROUP` statement will reject such an addition unless overridden with the `FORCE` option. - `FORMER` - Disk was once part of a disk group but has been dropped cleanly from the group. It may be added to a new disk group with the `ALTER DISKGROUP` statement. - `CONFLICT` - Oracle ASM disk was not mounted due to a conflict - `FOREIGN` - Disk contains data created by an Oracle product other than Oracle ASM. This includes data files, logfiles, and OCR disks. |
| `MODE_STATUS` | `VARCHAR2(7)` | Global status about which kinds of I/O requests are allowed to the disk:  - `ONLINE` - Disk is online and operating normally. Reads and writes are attempted when the disk is mounted. Reads are attempted as part of disk discovery. - `OFFLINE` - Disk is offline and access to data is not permitted. Reads and writes are not attempted. An offline disk remains logically part of its disk group. - `SYNCING` - Disk is offline for reads, but online for writes. Oracle ASM is resyncing stale data on the disk. See `V$ASM_OPERATION` to view resync progress. |
| `STATE` | `VARCHAR2(8)` | Global state of the disk with respect to the disk group:  - `UNKNOWN` - Oracle ASM disk state is not known (typically the disk is not mounted) - `NORMAL` - Disk is online and operating normally - `ADDING` - Disk is being added to a disk group, and is pending validation by all instances that have the disk group mounted - `DROPPING` - Disk has been manually taken offline and space allocation or data access for the disk halts. Rebalancing will commence to relocate data off the disks to other disks in the disk group. Upon completion of the rebalance, the disk is expelled from the group. - `HUNG` - Disk drop operation cannot continue because there is insufficient space to relocate the data from the disk being dropped - `FORCING` - Disk is being removed from the disk group without attempting to offload its data. The data will be recovered from redundant copies, where possible. |
| `REDUNDANCY` | `VARCHAR2(7)` | Hardware redundancy of the disk:  - `UNKNOWN` - `UNPROT` - `MIRROR` - `PARITY`  Note: This column is valid only if an ASMLIB is present that supports returning hardware redundancy information. This column is not related to the redundancy of the disk group of which the disk is a member. |
| `LIBRARY` | `VARCHAR2(64)` | Name of the library that discovered the disk |
| `OS_MB` | `NUMBER` | Size of the disk (in megabytes) as reported by the host operating system |
| `TOTAL_MB` | `NUMBER` | Total capacity of the disk (in megabytes) |
| `FREE_MB` | `NUMBER` | Unused capacity of the disk (in megabytes) |
| `HOT_USED_MB` <sup>Foot 1</sup> | `NUMBER` | Number of used megabytes in the hot region |
| `COLD_USED_MB` <sup>Foot 1</sup> | `NUMBER` | Number of used megabytes in the cold region |
| `NAME` | `VARCHAR2(30)` | Name of the disk |
| `FAILGROUP` | `VARCHAR2(30)` | Name of the failure group containing the disk |
| `LABEL` | `VARCHAR2(31)` | Disk label portion of the name returned by discovery |
| `PATH` | `VARCHAR2(256)` | Operating system path name portion of the name returned by discovery |
| `UDID` | `VARCHAR2(64)` | Unique Device ID portion of the name returned by discovery |
| `PRODUCT` | `VARCHAR2(32)` | Name of the manufacturer and the name of the product. All disks with the same product id will have the same performance and reliability characteristics. |
| `CREATE_DATE` | `DATE` | Date and time when the disk was added to the disk group |
| `MOUNT_DATE` | `DATE` | Date and time when the disk was mounted by the first instance |
| `REPAIR_TIMER` | `NUMBER` | Seconds remaining until the disk is automatically dropped (`0` if not failed) |
| `READS` | `NUMBER` | Total number of I/O read requests for the disk |
| `WRITES` | `NUMBER` | Total number of I/O write requests for the disk |
| `READ_ERRS` | `NUMBER` | Total number of failed I/O read requests for the disk |
| `WRITE_ERRS` | `NUMBER` | Total number of failed I/O write requests for the disk |
| `READ_TIMEOUT` | `NUMBER` | Number of read I/Os that are timed out |
| `WRITE_TIMEOUT` | `NUMBER` | Number of write I/Os that are timed out |
| `READ_TIME` | `NUMBER` | Total I/O time (in seconds) for read requests for the disk if the `TIMED_STATISTICS` initialization parameter is set to `true` (`0` if set to `false`) |
| `WRITE_TIME` | `NUMBER` | Total I/O time (in seconds) for write requests for the disk if the `TIMED_STATISTICS` initialization parameter is set to `true` (`0` if set to `false`) |
| `BYTES_READ` | `NUMBER` | Total number of bytes read from the disk |
| `BYTES_WRITTEN` | `NUMBER` | Total number of bytes written to the disk |
| `PREFERRED_READ` | `VARCHAR2(1)` | Status of the preferred read failure group:  - `U` - Disk group has no preferred read failure group - `Y` - Disk is a preferred read disk - `N` - Disk is not a preferred read disk  For a disk group with one or more preferred read failure groups, if the disk is in one of the preferred read failure groups, the value of this column is `Y`; otherwise it is `N`. |
| `HASH_VALUE` | `NUMBER` | A unique hash value for an Oracle ASM disk, computed using the Oracle ASM disk name (as specified by `NAME` column in `v$asm_disk`) and the Oracle ASM disk group name (as specified by `NAME` column in `v$asm_diskgroup`). |
| `HOT_READS` <sup>Foot 1</sup> | `NUMBER` | This column is not meaningful and its value is always `0` |
| `HOT_WRITES` <sup>Foot 1</sup> | `NUMBER` | This column is not meaningful and its value is always `0` |
| `HOT_BYTES_READ` <sup>Foot 1</sup> | `NUMBER` | This column is not meaningful and its value is always `0` |
| `HOT_BYTES_WRITTEN` <sup>Foot 1</sup> | `NUMBER` | This column is not meaningful and its value is always `0` |
| `COLD_READS` <sup>Foot 1</sup> | `NUMBER` | Number of reads from the disk |
| `COLD_WRITES` <sup>Foot 1</sup> | `NUMBER` | Number of writes to the disk |
| `COLD_BYTES_READ` <sup>Foot 1</sup> | `NUMBER` | Number of bytes read from the disk |
| `COLD_BYTES_WRITTEN` <sup>Foot 1</sup> | `NUMBER` | Number of bytes written to the disk |
| `VOTING_FILE` | `VARCHAR2(1)` | Indicates whether the disk contains a voting file (`Y`) or not (`N`) |
| `SECTOR_SIZE` | `NUMBER` | Physical block size (in bytes) |
| `LOGICAL_SECTOR_SIZE` | `NUMBER` | Shows the logical sector size value of the disk in bytes. This is the smallest possible I/O that can be done by the disk.  If the value of the `LOGICAL_SECTOR_SIZE` column is `512`, while the value in the `SECTOR_SIZE` column is `4096`, then the disk supports 512 sector size emulation. This means the disk can be used for both 512 native and 4096 native disk groups. |
| `FAILGROUP_TYPE` | `VARCHAR2(7)` | Type of the failure group:  - `REGULAR` - `QUORUM` |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data  For this view, the value is always `0`. |
| `THIN_PROVISION_CAPABLE` | `VARCHAR2(1)` | Indicates whether the disk supports Storage Thin Provisioning (`Y`) or not (`N`) |
| `DATA_INTEGRITY_CAPABLE` | `VARCHAR2(1)` | Indicates whether the disk supports the Data Integrity feature (`Y`) or not (`N`) |
| `SITE_NAME` | `VARCHAR2(30)` | The name of the site to which the specific disk belongs |
| `SITE_GUID` | `VARCHAR2(33)` | The GUID for the site to which the specific disk belongs |
| `FAILGROUP_LABEL` | `VARCHAR2(30)` | This is the suggested name for the failure group to which the disk belongs, as returned by discovery |
| `SITE_LABEL` | `VARCHAR2(30)` | This is the suggested name for the site to which the disk belongs, as returned by discovery |
| `SITE_STATUS` | `VARCHAR2(11)` | This column is populated only for disks in Oracle ASM extended disk groups. The site status is computed after every Partnership and Status Table (PST) refresh or when the PST is read from disks into memory. The possible states include:  - `UNKNOWN`: This is the state before any checks have been performed. - `UNAVAILABLE`: This is the state when all the disks in the site are offline. - `COMPROMISED`: The state when enough disks or PST copies are offline, such that the site can no longer provide data availability. - `AVAILABLE`: The state when there is enough redundancy within the site to provide data availability in case another site becomes compromised or unavailable. |

<sup>Footnote 1</sup> Intelligent Data Placement is desupported starting with Oracle Database 21c. As a result, the individual values for the `HOT_USED_MB` and `COLD_USED_MB` columns are not meaningful. However, the sum of the `HOT_USED_MB` and `COLD_USED_MB` values represents the total number of used megabytes on the disk. Also, the `HOT_READS`, `HOT_WRITES`, `HOT_BYTES_READ`, and `HOT_BYTES_WRITTEN` columns are no longer meaningful and always return `0`, and the `COLD_READS`, `COLD_WRITES`, `COLD_BYTES_READ`, and `COLD_BYTES_WRITTEN` columns return statistics for the entire disk.

Note:

The `GROUP_NUMBER` and `DISK_NUMBER` columns will only be valid if the disk is part of a disk group which is currently mounted by the instance. Otherwise, `GROUP_NUMBER` will be `0`, and `DISK_NUMBER` will be a unique value with respect to the other disks that also have a group number of `0`.

Note:

In an Oracle Database instance, this view returns 0 rows when queried from a PDB.

Note:

This view performs disk discovery every time it is queried. Because performing disk discovery is very resource intensive, Oracle recommends against using this view for monitoring scripts. Instead, use the less expensive view [V$ASM\_DISK\_STAT](V-ASM_DISK_STAT.md).

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=OSTMG10030) for additional information about using views to display Oracle ASM information