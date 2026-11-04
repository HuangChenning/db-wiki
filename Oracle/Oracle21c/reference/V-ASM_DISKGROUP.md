---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ASM_DISKGROUP.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.59 V$ASM\_DISKGROUP

`V$ASM_DISKGROUP` displays one row for every Oracle Automatic Storage Management (Oracle ASM) disk group discovered by the Oracle ASM instance on the node.

| Column | Datatype | Description |
| --- | --- | --- |
| `GROUP_NUMBER` | `NUMBER` | Cluster-wide number assigned to the disk group (primary key) |
| `NAME` | `VARCHAR2(30)` | Name of the disk group |
| `SECTOR_SIZE` | `NUMBER` | Physical block size (in bytes) |
| `LOGICAL_SECTOR_SIZE` | `NUMBER` | This column represents the logical sector size value of the disk group in bytes. This is the smallest possible I/O that can be done in this disk group. Any I/O smaller than the logical sector size will cause an assert in the code.  If the value of the `LOGICAL_SECTOR_SIZE` column is `512`, while the value in the `SECTOR_SIZE` column is `4096`, then the disk group supports 512 sector size emulation. This means that I/O operations can be both 512 or 4096 aligned. For example, this means that you can have redo log files with a file block size of 512 bytes in this disk group that can be both read and written to, as well as create new redo log files with a file block size of 4096 bytes. |
| `BLOCK_SIZE` | `NUMBER` | Oracle ASM metadata block size (in bytes) |
| `ALLOCATION_UNIT_SIZE` | `NUMBER` | Size of the allocation unit (in bytes) |
| `STATE` | `VARCHAR2(11)` | State of the disk group relative to the instance:  - `BROKEN` - Database instance lost connectivity to the Oracle ASM instance that mounted the disk group - `CONNECTED` - Disk group is in use by the database instance - `DISMOUNTED` - Disk group was cleanly dismounted by the Oracle ASM instance following a successful mount - `MOUNTED` - Instance is successfully serving the disk group to its database clients - `QUIESCING` - CRSCTL utility attempted to dismount a disk group that contains the Oracle Cluster Registry (OCR). The disk group cannot be dismounted until Cluster Ready Services (CRS) exits, because the disk group contains the OCR. - `RESTRICTED` - A disk group mounted in this mode can only be seen by this Oracle ASM instance for maintenance purposes - `UNKNOWN` - Oracle ASM instance has never attempted to mount the disk group |
| `TYPE` | `VARCHAR2(6)` | Redundancy type for the disk group:  - `EXTEND` - `EXTERN` - `FLEX` - `HIGH` - `NORMAL` |
| `TOTAL_MB` | `NUMBER` | Total capacity of the disk group, excluding that of quorum disks (in megabytes) |
| `FREE_MB` | `NUMBER` | Unused capacity of the disk group (in megabytes) |
| `HOT_USED_MB` <sup>Foot 1</sup> | `NUMBER` | Number of used megabytes in the hot region |
| `COLD_USED_MB` <sup>Foot 1</sup> | `NUMBER` | Number of used megabytes in the cold region |
| `REQUIRED_MIRROR_FREE_MB` | `NUMBER` | Amount of space that is required to be available in a given disk group in order to restore redundancy after one or more disk failures. The amount of space displayed in this column takes mirroring effects into account. |
| `USABLE_FILE_MB` | `NUMBER` | Amount of free space that can be safely utilized taking mirroring into account and yet be able to restore redundancy after a disk failure |
| `OFFLINE_DISKS` | `NUMBER` | Number of disks in the disk group that are currently offline |
| `COMPATIBILITY` | `VARCHAR2(60)` | Minimum software version required for an Oracle ASM instance to mount this disk group |
| `DATABASE_COMPATIBILITY` | `VARCHAR2(60)` | Minimum software version required for a database instance to use files in this disk group |
| `VOTING_FILES` | `VARCHAR2(1)` | Indicates whether the disk contains voting files (`Y`) or not (`N`) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data  For this view, the value is always `0`. |

<sup>Footnote 1</sup> Intelligent Data Placement is desupported starting with Oracle Database 21c. As a result, the individual values for the `HOT_USED_MB` and `COLD_USED_MB` columns are not meaningful. However, the sum of the `HOT_USED_MB` and `COLD_USED_MB` values represents the total number of used megabytes in the disk group.

Note:

The `GROUP_NUMBER`, `TOTAL_MB`, and `FREE_MB` columns are only meaningful if the disk group is mounted by the instance. Otherwise, their values will be `0`.

Note:

This view performs disk discovery every time it is queried. Because performing disk discovery is very resource intensive, Oracle recommends against using this view for monitoring scripts. Instead, use the less expensive view [V$ASM\_DISKGROUP\_STAT](V-ASM_DISKGROUP_STAT.md).

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=OSTMG10030) for additional information about using views to display Oracle ASM information