---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-ASM_QUOTAGROUP.html
tags:
  - oracle
  - 12c
  - reference
---

`V$ASM_QUOTAGROUP` displays one row for every Oracle Automatic Storage Management (Oracle ASM) quota group discovered by the Oracle ASM instance on the node.

| Column | Datatype | Description |
| --- | --- | --- |
| `GROUP_NUMBER` | `NUMBER` | Number of the disk group containing the quota group (composite primary key) |
| `QUOTAGROUP_NUMBER` | `NUMBER` | Number of the quota group within the disk group (composite primary key) |
| `INCARNATION` | `NUMBER` | Incarnation of the quota group (composite primary key) |
| `NAME` | `VARCHAR2(30)` | Name of the quota group |
| `USED_QUOTA_MB` | `NUMBER` | Used quota of the quota group in GB |
| `QUOTA_LIMIT_MB` | `NUMBER` | Quota limit (capacity) of the quota group in GB |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).