---
title: "V$ASM_DISKGROUP"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1027.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$ASM_DISKGROUP` displays one row for every ASM disk group discovered by the ASM instance on the node.

| Column | Datatype | Description |
| --- | --- | --- |
| `GROUP_NUMBER` | `NUMBER` | Cluster-wide number assigned to the disk group (primary key) |
| `NAME` | `VARCHAR2(30)` | Name of the disk group |
| `SECTOR_SIZE` | `NUMBER` | Physical block size (in bytes) |
| `BLOCK_SIZE` | `NUMBER` | Oracle ASM metadata block size (in bytes) |
| `ALLOCATION_UNIT_SIZE` | `NUMBER` | Size of the allocation unit (in bytes) |
| `STATE` | `VARCHAR2(11)` | State of the disk group relative to the instance: - `CONNECTED` - Disk group is in use by the database instance - `BROKEN` - Database instance lost connectivity to the Oracle ASM instance that mounted the disk group - `UNKNOWN` - Oracle ASM instance has never attempted to mount the disk group - `DISMOUNTED` - Disk group was cleanly dismounted by the Oracle ASM instance following a successful mount - `MOUNTED` - Instance is successfully serving the disk group to its database clients - `QUIESCING` - CRSCTL utility attempted to dismount a disk group that contains the Oracle Cluster Registry (OCR). The disk group cannot be dismounted until Cluster Ready Services (CRS) exits, because the disk group contains the OCR. |
| `TYPE` | `VARCHAR2(6)` | Redundancy type for the disk group: - `EXTERN` - `NORMAL` - `HIGH` |
| `TOTAL_MB` | `NUMBER` | Total capacity of the disk group (in megabytes) |
| `FREE_MB` | `NUMBER` | Unused capacity of the disk group (in megabytes) |
| `HOT_USED_MB` | `NUMBER` | Number of used megabytes in the hot region |
| `COLD_USED_MB` | `NUMBER` | Number of used megabytes in the cold region |
| `REQUIRED_MIRROR_FREE_MB` | `NUMBER` | Amount of space that is required to be available in a given disk group in order to restore redundancy after one or more disk failures. The amount of space displayed in this column takes mirroring effects into account. |
| `USABLE_FILE_MB` | `NUMBER` | Amount of free space that can be safely utilized taking mirroring into account and yet be able to restore redundancy after a disk failure |
| `OFFLINE_DISKS` | `NUMBER` | Number of disks in the disk group that are currently offline |
| `COMPATIBILITY` | `VARCHAR2(60)` | Minimum software version required for an ASM instance to mount this disk group |
| `DATABASE_COMPATIBILITY` | `VARCHAR2(60)` | Minimum software version required for a database instance to use files in this disk group |
| `VOTING_FILES` | `VARCHAR2(1)` | Indicates whether the disk contains voting files (`Y`) or not (`N`) |

Note:

The `GROUP_NUMBER`, `TOTAL_MB`, and `FREE_MB` columns are only meaningful if the disk group is mounted by the instance. Otherwise, their values will be `0`.