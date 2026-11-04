---
title: "V$ASM_FILE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1029.htm
tags:
  - oracle
  - 11g
  - reference
---

In an Oracle Automatic Storage Management (Oracle ASM) instance, `V$ASM_FILE` displays one row for each file in each disk group mounted by the Oracle ASM instance. For example, if there are three disk groups and five files in each, fifteen rows are displayed (unless the query is qualified with a `WHERE` clause).

| Column | Datatype | Description |
| --- | --- | --- |
| `GROUP_NUMBER` | `NUMBER` | Number of the disk group containing the file (composite primary key) |
| `FILE_NUMBER` | `NUMBER` | Number of the file within the disk group (composite primary key) |
| `COMPOUND_INDEX` | `NUMBER` | A 32-bit number consisting of a disk group number in the high-order 8 bits and a file number in the low-order 24 bits (for efficient access to the view) |
| `INCARNATION` | `NUMBER` | Incarnation number for the file (composite primary key) |
| `BLOCK_SIZE` | `NUMBER` | Block size of the file (in bytes) |
| `BLOCKS` | `NUMBER` | Number of blocks in the file |
| `BYTES` | `NUMBER` | Number of bytes in the file |
| `SPACE` | `NUMBER` | Number of bytes allocated to the file |
| `TYPE` | `VARCHAR2(64)` | Type of the file. Possible values are as follows: - `CONTROLFILE` - `DATAFILE` - `ONLINELOG` - `ARCHIVELOG` - `TEMPFILE` - `BACKUPSET` - `XTRANSPORT` - `PARAMETERFILE` - `DATAGUARDCONFIG` - `FLASHBACK` - `CHANGETRACKING` - `DUMPSET` - `AUTOBACKUP` |
| `REDUNDANCY` | `VARCHAR2(6)` | Redundancy of the file: - `UNPROT` - `MIRROR` - `HIGH` |
| `STRIPED` | `VARCHAR2(6)` | Indicates how the file is striped: - `FINE` - `COARSE` |
| `CREATION_DATE` | `DATE` | Date on which the file was created |
| `MODIFICATION_DATE` | `DATE` | Date of the last open/close for writing, rounded back to the nearest hour |
| `REDUNDANCY_LOWERED` | `VARCHAR2(1)` | Indicates whether a file has lower redundancy than what was expected (`Y`) or not (`N`). Redundancy is said to have been lowered for a file when one or more data extents in that file are not mirrored at the level specified by the administrator. In case of unprotected files, data extents could be missing altogether. Another possible value for this column is (`U`), which means that it is unknown.  This column is deprecated, and it always displays a value of `U`. |
| `PERMISSIONS` | `VARCHAR2(16)` | Access permissions of the file, in order of user, group, and other |
| `USER_NUMBER` | `NUMBER` | User number |
| `USER_INCARNATION` | `NUMBER` | Incarnation number of the user |
| `USERGROUP_NUMBER` | `NUMBER` | User group number |
| `USERGROUP_INCARNATION` | `NUMBER` | Incarnation number of the user group |
| `PRIMARY_REGION` | `VARCHAR2(4)` | Region used for allocating primary extents: - `HOT` - `COLD` |
| `MIRROR_REGION` | `VARCHAR2(4)` | Region for allocating mirrored extents: - `HOT` - `COLD` |
| `HOT_READS` | `NUMBER` | Number of reads from the hot region for the file |
| `HOT_WRITES` | `NUMBER` | Number of writes to the hot region for the file |
| `HOT_BYTES_READ` | `NUMBER` | Number of bytes read from the hot region for the file |
| `HOT_BYTES_WRITTEN` | `NUMBER` | Number of bytes written to the hot region for the file |
| `COLD_READS` | `NUMBER` | Number of reads from the cold region for the file |
| `COLD_WRITES` | `NUMBER` | Number of writes to the cold region for the file |
| `COLD_BYTES_READ` | `NUMBER` | Number of bytes read from the cold region for the file |
| `COLD_BYTES_WRITTEN` | `NUMBER` | Number of bytes written to the cold region for the file |