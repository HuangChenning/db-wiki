---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/V-ASM_FILESYSTEM.html
tags:
  - oracle
  - 19c
  - reference
---

## 7.74 V$ASM\_FILESYSTEM

`V$ASM_FILESYSTEM` displays information for every mounted Oracle ACFS.

| Column | Datatype | Description |
| --- | --- | --- |
| `FS_NAME` | `VARCHAR2(1024)` | Mount point (primary key) |
| `AVAILABLE_TIME` | `DATE` | Mount time or the time that the file system became available again; NULL if the file system is not available |
| `BLOCK_SIZE` | `NUMBER` | File system block size (in kilobytes) |
| `STATE` | `VARCHAR2(13)` | File system status::  - `NOT AVAILABLE` - `AVAILABLE` - `OFFLINE` - Either the Oracle ASM instance is down, the disk group has been forced dismounted, or less commonly, a metadata I/O failure occurred or serious metadata corruption was detected. In the case of a metadata I/O failure, the file system is also marked as corrupt. An offline file system can only be unmounted; other attempts at access result in errors. |
| `CORRUPT` | `VARCHAR2(5)` | Indicates whether the file system needs the fixer (`fsck`, `acfschkdsk`) to be run (`TRUE`) or not (`FALSE`) |
| `NUM_VOL` | `NUMBER` | Number of volumes in the file system |
| `TOTAL_SIZE` | `NUMBER` | Total capacity of the file system (in megabytes) |
| `TOTAL_FREE` | `NUMBER` | Total free space in the file system (in megabytes) |
| `TOTAL_SNAP_SPACE_USAGE` | `NUMBER` | Total space used by snapshots (in megabytes) |
| `REPLSTATE` | `VARCHAR2(7)` | Replication status:  - `NO REPL` - Replication is not initialized - `PRIMARY` - File system is initialized for replication as a primary - `STANDBY` - File system is initialized for replication as a standby |
| `RESIZE_STATE` <sup>Foot 1</sup> | `VARCHAR2(5)` | Possible resize states: - `NONE` - AutoResize not configured - `AUTO` - Equivalent to AutoResizeEnabled flag - `ERROR` - Equivalent to AutoResizeError flag |
| `COMPRESS_STATE` <sup>Foot 1</sup> | `VARCHAR2(7)` | Compression status of the file system. Possible values: - `DISABLED` - Compression is not active - `ENABLED` - Compression is active - `PARTIAL` - Compression is disabled, but the file system may contain compressed files |
| `FROZEN_STATE` <sup>Foot 1</sup> | `VARCHAR2(5)` | Indicates whether the filesystem is frozen (`TRUE`) or not (`FALSE`) |
| `ACFS_COMPATIBILITY` <sup>Foot 1</sup> | `VARCHAR2(60)` | Oracle Release streams where Oracle ACFS has shipped |
| `METADATA_BLOCK_SIZE` <sup>Foot 1</sup> | `NUMBER` | Metadata block size of the file system. Possible values: - 512 - 4096 |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data  For this view, the value is always `0`. |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 19c.

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=OSTMG10030) for additional information about using views to display Oracle ASM information