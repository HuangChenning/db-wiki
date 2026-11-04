---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ASM_FILEGROUP_FILE.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.64 V$ASM\_FILEGROUP\_FILE

`V$ASM_FILEGROUP_FILE` lists all the Oracle Automatic Storage Management (Oracle ASM) files associated with each File Group.

In both Oracle ASM and Oracle Database instances, `V$ASM_FILEGROUP_FILE` will display one row for every file associated with a File Group contained in every Disk Group mounted by the instance.

| Column | Datatype | Description |
| --- | --- | --- |
| `GROUP_NUMBER` | `NUMBER` | Number of the Disk Group in which this File Group exists |
| `FILEGROUP_NUMBER` | `NUMBER` | Number associated to the File Group within its Disk Group |
| `FILEGROUP_INCARN` | `NUMBER` | Incarnation number for the File Group |
| `FILE_NUMBER` | `NUMBER` | Number associated to the ASM File (same file number as in `V$ASM_FILE`) |
| `INCARNATION` | `NUMBER` | Incarnation number for the ASM File |
| `COMPOUND_INDEX` | `NUMBER` | A 32-bit number consisting of a Disk Group number in the high-order 8 bits and a File number in the low-order 24 bits (for efficient access to the view) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

- " [V$ASM\_FILE](V-ASM_FILE.md) "
- " [V$ASM\_FILEGROUP](V-ASM_FILEGROUP.md) "