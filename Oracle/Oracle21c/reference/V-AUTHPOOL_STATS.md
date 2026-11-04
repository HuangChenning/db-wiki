---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-AUTHPOOL_STATS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.75 V$AUTHPOOL\_STATS

`V$AUTHPOOL_STATS` displays statistics for the authentication pool. This pool authenticates user connections when client applications connect to Database Resident Connection Pooling (DRCP).

| Column | Datatype | Description |
| --- | --- | --- |
| `NUM_SRVS` | `NUMBER` | Total number of servers in the authentication pool |
| `NUM_BUSY` | `NUMBER` | Number of busy servers in the authentication pool |
| `NUM_FREE` | `NUMBER` | Number of free servers in the authentication pool |
| `NUM_WAITERS` | `NUMBER` | Number of connections waiting for a server in the authentication pool to become available |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire multitenant container database (CDB). This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Note:

This view is available starting with Oracle Database 21c.