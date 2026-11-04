---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ASM_QUOTAGROUP.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.68 V$ASM\_QUOTAGROUP

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