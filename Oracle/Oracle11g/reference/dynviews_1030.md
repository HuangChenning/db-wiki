---
title: "V$ASM_FILESYSTEM"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1030.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$ASM_FILESYSTEM` displays information for every mounted Oracle ACFS.

| Column | Datatype | Description |
| --- | --- | --- |
| `FS_NAME` | `VARCHAR2(1024)` | Mount point (primary key) |
| `AVAILABLE_TIME` | `DATE` | Mount time or the time that the file system became available again; NULL if the file system is not available |
| `BLOCK_SIZE` | `NUMBER` | File system block size (in kilobytes) |
| `STATE` | `VARCHAR2(13)` | File system status:: - `NOT AVAILABLE` - `AVAILABLE` - `OFFLINE` - Either the ASM instance is down, the disk group has been forced dismounted, or less commonly, a metadata I/O failure occurred or serious metadata corruption was detected. In the case of a metadata I/O failure, the file system is also marked as corrupt. An offline file system can only be unmounted; other attempts at access result in errors. |
| `CORRUPT` | `VARCHAR2(5)` | Indicates whether the file system needs the fixer (`fsck`, `acfschkdsk`) to be run (`TRUE`) or not (`FALSE`) |
| `NUM_VOL` | `NUMBER` | Number of volumes in the file system |
| `TOTAL_SIZE` | `NUMBER` | Total capacity of the file system (in megabytes) |
| `TOTAL_FREE` | `NUMBER` | Total free space in the file system (in megabytes) |
| `TOTAL_SNAP_SPACE_USAGE` | `NUMBER` | Total space used by snapshots (in megabytes) |