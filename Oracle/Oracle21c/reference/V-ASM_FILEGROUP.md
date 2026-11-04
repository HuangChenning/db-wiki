---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ASM_FILEGROUP.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.63 V$ASM\_FILEGROUP

`V$ASM_FILEGROUP` describes the properties of the Oracle Automatic Storage Management (Oracle ASM) File Groups.

In both Oracle ASM and Oracle Database instances, `V$ASM_FILEGROUP` displays one row for every File Group present in every Disk Group mounted by the Oracle ASM instance. File Groups are only displayed for Disk Groups where `COMPATIBLE.ASM` is set to `12.2` or higher.

Note:

There will not be an entry for the default File Group.

| Column | Datatype | Description |
| --- | --- | --- |
| `GROUP_NUMBER` | `NUMBER` | Number of the Disk Group in which this File Group exists (composite primary key) |
| `FILEGROUP_NUMBER` | `NUMBER` | Number associated to the File Group within its Disk Group (composite primary key) |
| `INCARNATION` | `NUMBER` | Incarnation number for the File Group (composite primary key) |
| `COMPOUND_INDEX` | `NUMBER` | A 32-bit number consisting of a Disk Group number in the high-order 8 bits and a File Group number in the low-order 24 bits (for efficient access to the view) |
| `NAME` | `VARCHAR2(128)` | Name of the File Group |
| `CLIENT_TYPE` | `NUMBER` | Type of client that the File Group is associated to:  - `DATABASE` - `CLUSTER` - `VOLUME` |
| `CLIENT_NAME` | `VARCHAR2(128)` | Name of the client (database, PDB, CDB, cluster, or volume) that the File Group is associated to |
| `GUID` | `VARCHAR2(32)` | If the `CLIENT_TYPE` is `DATABASE`: - In a CDB environment, it is the GUID of the PDB or CDB associated with the file group, the same value as the GUID in `V$CONTAINERS`. - In a non-CDB environment it is the database identifier (DBID) of the database associated with that file group.  If the `CLIENT_TYPE` is `VOLUME` or `CLUSTER`, the `GUID` column is empty. |
| `QUOTAGROUP_NUMBER` | `NUMBER` | Number of the quota group associated with this File Group (foreign key to the `V$ASM_QUOTAGROUP` view) |
| `QUOTAGROUP_INCARNATION` | `NUMBER` | Incarnation number for the Quota Group |
| `USED_QUOTA_MB` | `NUMBER` | Used quota of the quota group in GB |
| `USER_NUMBER` | `NUMBER` | User number |
| `USER_INCARNATION` | `NUMBER` | Incarnation number of the user |
| `USERGROUP_NUMBER` | `NUMBER` | User group number |
| `USERGROUP_INCARNATION` | `NUMBER` | Incarnation number of the user group |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$ASM\_FILEGROUP\_PROPERTY](V-ASM_FILEGROUP_PROPERTY.md) "