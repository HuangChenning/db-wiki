---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-CPOOL_CC_STATS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.148 V$CPOOL\_CC\_STATS

`V$CPOOL_CC_STATS` displays information about the connection class level statistics for the Database Resident Connection Pool per instance.

| Column | Datatype | Description |
| --- | --- | --- |
| `CCLASS_NAME` | `VARCHAR2(1024)` | Name of the connection class |
| `NUM_REQUESTS` | `NUMBER` | Number of session requests |
| `NUM_HITS` | `NUMBER` | Total number of times a session that matches with the request was found in the pool |
| `NUM_MISSES` | `NUMBER` | Total number of times an exact match to the request was not found in the pool and a new session had to be created |
| `NUM_WAITS` | `NUMBER` | Total number of times session requests had to wait before getting served |
| `WAIT_TIME` | `NUMBER` | Reserved for future use |
| `CLIENT_REQ_TIMEOUTS` | `NUMBER` | Reserved for future use |
| `NUM_AUTHENTICATIONS` | `NUMBER` | Total number of authentications of clients done by the pool |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Note:

This view returns data only when queried from a CDB root. When queried from a PDB, this view returns 0 rows.