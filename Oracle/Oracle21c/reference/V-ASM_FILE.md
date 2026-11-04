---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ASM_FILE.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.62 V$ASM\_FILE

In an Oracle Automatic Storage Management (Oracle ASM) instance, `V$ASM_FILE` displays one row for each file in each disk group mounted by the Oracle ASM instance.

For example, if there are three disk groups and five files in each, fifteen rows are displayed (unless the query is qualified with a `WHERE` clause).

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
| `TYPE` | `VARCHAR2(64)` | Type of the file. Possible values are as follows:  - `ARCHIVELOG` - `AUTOBACKUP` - `BACKUPSET` - `CHANGETRACKING` - `CONTROLFILE` - `DATAFILE` - `DATAGUARDCONFIG` - `DUMPSET` - `FLASHBACK` - `ONLINELOG` - `PARAMETERFILE` - `TEMPFILE` - `XTRANSPORT` |
| `REDUNDANCY` | `VARCHAR2(6)` | Redundancy of the file:  - `HIGH` - `MIRROR` - `PARITY` - `UNPROT` |
| `STRIPED` | `VARCHAR2(6)` | Indicates how the file is striped:  - `FINE` - `COARSE` |
| `CREATION_DATE` | `DATE` | Date on which the file was created |
| `MODIFICATION_DATE` | `DATE` | Date of the last open/close for writing, rounded back to the nearest hour |
| `REDUNDANCY_LOWERED` | `VARCHAR2(1)` | Indicates whether a file has lower redundancy than what was expected (`Y`) or not (`N`). Redundancy is said to have been lowered for a file when one or more data extents in that file are not mirrored at the level specified by the administrator. In case of unprotected files, data extents could be missing altogether. Another possible value for this column is (`U`), which means that it is unknown.  This column is deprecated, and it always displays a value of `U`. |
| `PERMISSIONS` | `VARCHAR2(16)` | Access permissions of the file, in order of user, group, and other |
| `USER_NUMBER` | `NUMBER` | User number |
| `USER_INCARNATION` | `NUMBER` | Incarnation number of the user |
| `USERGROUP_NUMBER` | `NUMBER` | User group number |
| `USERGROUP_INCARNATION` | `NUMBER` | Incarnation number of the user group |
| `PRIMARY_REGION` <sup>Foot 1</sup> | `VARCHAR2(4)` | Region used for allocating primary extents:  - `HOT` - `COLD` |
| `MIRROR_REGION` <sup>Foot 1</sup> | `VARCHAR2(4)` | Region for allocating mirrored extents:  - `HOT` - `COLD` |
| `HOT_READS` <sup>Foot 1</sup> | `NUMBER` | This column is not meaningful and its value is always `0` |
| `HOT_WRITES` <sup>Foot 1</sup> | `NUMBER` | This column is not meaningful and its value is always `0` |
| `HOT_BYTES_READ` <sup>Foot 1</sup> | `NUMBER` | This column is not meaningful and its value is always `0` |
| `HOT_BYTES_WRITTEN` <sup>Foot 1</sup> | `NUMBER` | This column is not meaningful and its value is always `0` |
| `COLD_READS` <sup>Foot 1</sup> | `NUMBER` | Number of reads from the file |
| `COLD_WRITES` <sup>Foot 1</sup> | `NUMBER` | Number of writes to the file |
| `COLD_BYTES_READ` <sup>Foot 1</sup> | `NUMBER` | Number of bytes read from the file |
| `COLD_BYTES_WRITTEN` <sup>Foot 1</sup> | `NUMBER` | Number of bytes written to the file |
| `FILEGROUP_NUMBER` | `NUMBER` | Shows the number of the associated file group |
| `FILEGROUP_INCARNATION` | `NUMBER` | The incarnation number for the file group the file belongs to in a flex redundancy disk group |
| `REMIRROR` | `VARCHAR2(1)` | This column has the value `Y` when rebalance is needed for the file after a redundancy change in a flex redundancy disk group, `N` otherwise. A redundancy change can occur when the file is moved to a file group with a different redundancy, or when the redundancy property of the file group is changed. After rebalance is run for the file, the value changes to `N`. |
| `PARENT_FILNUM` | `NUMBER` | For internal use only. |
| `PARENT_FILNUMINC` | `NUMBER` | For internal use only. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data  For this view, the value is always `0`. |

<sup>Footnote 1</sup> Intelligent Data Placement is desupported starting with Oracle Database 21c. As a result, the `PRIMARY_REGION` and `MIRROR_REGION` columns are no longer meaningful. Also, the `HOT_READS`, `HOT_WRITES`, `HOT_BYTES_READ`, and `HOT_BYTES_WRITTEN` columns are no longer meaningful and always return `0`, and the `COLD_READS`, `COLD_WRITES`, `COLD_BYTES_READ`, and `COLD_BYTES_WRITTEN` columns return statistics for the entire file.

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=OSTMG10030) for additional information about using views to display Oracle ASM information