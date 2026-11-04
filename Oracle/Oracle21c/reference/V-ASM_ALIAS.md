---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ASM_ALIAS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.49 V$ASM\_ALIAS

In an Oracle Automatic Storage Management (Oracle ASM) instance, `V$ASM_ALIAS` displays one row for every alias present in every disk group mounted by the Oracle ASM instance.

| Column | Datatype | Description |
| --- | --- | --- |
| `NAME` | `VARCHAR2(70)` | Oracle ASM alias or alias directory name |
| `GROUP_NUMBER` | `NUMBER` | Owning disk group number of the alias (foreign key to the `V$ASM_DISKGROUP` view) |
| `FILE_NUMBER` | `NUMBER` | Oracle ASM file number of the alias (foreign key to the `V$ASM_FILE` view) |
| `FILE_INCARNATION` | `NUMBER` | Oracle ASM file incarnation number for the alias |
| `ALIAS_INDEX` | `NUMBER` | Alias entry number for the alias |
| `ALIAS_INCARNATION` | `NUMBER` | Incarnation number for the parent of the alias |
| `PARENT_INDEX` | `NUMBER` | A 32-bit number consisting of a disk group number in the high-order 8 bits and an alias entry number in the low-order 24 bits (number of the directory containing the alias) |
| `REFERENCE_INDEX` | `NUMBER` | A 32-bit number consisting of a disk group number in the high-order 8 bits and an alias entry number in the low-order 24 bits (number of the directory describing the current entry) |
| `ALIAS_DIRECTORY` | `VARCHAR2(1)` | Indicates whether the alias is to a directory (`Y`) or to an Oracle ASM file (`N`) |
| `SYSTEM_CREATED` | `VARCHAR2(1)` | Indicates whether the alias is system created (`Y`) or user created (`N`) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data  For this view, the value is always `0`. |

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=OSTMG10030) for additional information about using views to display Oracle ASM information