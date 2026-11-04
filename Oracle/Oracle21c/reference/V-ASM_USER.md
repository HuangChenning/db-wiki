---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ASM_USER.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.70 V$ASM\_USER

`V$ASM_USER` displays the effective operating system user names of connected database instances and of file owners.

| Column | Datatype | Description |
| --- | --- | --- |
| `GROUP_NUMBER` | `NUMBER` | Oracle ASM disk group number |
| `USER_NUMBER` | `NUMBER` | Oracle ASM internal unique user number |
| `COMPOUND_INDEX` | `NUMBER` | A 32-bit number consisting of a disk group number in the high-order 8 bits and a user number in the low-order 24 bits (for efficient access to the view) |
| `INCARNATION` | `NUMBER` | Incarnation number of the user |
| `CLUSTER_ID` | `VARCHAR2(128)` | Oracle ASM cluster ID. The `CLUSTER_ID` and `OS_NAME` pair can be used to uniquely identify a user. |
| `OS_ID` | `VARCHAR2(128)` | Operating system user ID |
| `OS_NAME` | `VARCHAR2(33)` | Operating system user name |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data  For this view, the value is always `0`. |

Note:

In an Oracle Database instance, this view returns 0 rows when queried from a PDB.

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=OSTMG10030) for additional information about using views to display Oracle ASM information