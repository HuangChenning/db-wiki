---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-ASM_USERGROUP.html
tags:
  - oracle
  - 12c
  - reference
---

`V$ASM_USERGROUP` displays the creator for each Oracle Automatic Storage Management (Oracle ASM) File Access Control group.

| Column | Datatype | Description |
| --- | --- | --- |
| `GROUP_NUMBER` | `NUMBER` | Oracle ASM disk group number |
| `USERGROUP_NUMBER` | `NUMBER` | Number of the user group |
| `COMPOUND_INDEX` | `NUMBER` | A 32-bit number consisting of a disk group number in the high-order 8 bits and a user group number in the low-order 24 bits (for efficient access to the view) |
| `INCARNATION` | `NUMBER` | Incarnation number of the user group |
| `OWNER_NUMBER` | `NUMBER` | User group owner identified by a unique number |
| `OWNER_INCARNATION` | `NUMBER` | Incarnation number of the user group owner |
| `NAME` | `VARCHAR2(64)` | User group name |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data  For this view, the value is always `0`. |

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=OSTMG10030) for additional information about using views to display Oracle ASM information