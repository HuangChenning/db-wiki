---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-CPOOL_STATS.html
tags:
  - oracle
  - 12c
  - reference
---

`V$CPOOL_STATS` displays information about the Database Resident Connection Pool statistics for an instance.

| Column | Datatype | Description |
| --- | --- | --- |
| `POOL_NAME` | `VARCHAR2(1024)` | Name of the Database Resident Connection Pool |
| `NUM_OPEN_SERVERS` | `NUMBER` | Total number of busy and free servers in the pool (including the authentication servers) |
| `NUM_BUSY_SERVERS` | `NUMBER` | Total number of busy servers in the pool (not including the authentication servers) |
| `NUM_AUTH_SERVERS` | `NUMBER` | Number of authentication servers in the pool |
| `NUM_REQUESTS` | `NUMBER` | Number of client requests |
| `NUM_HITS` | `NUMBER` | Total number of times client requests found matching pooled servers in the pool |
| `NUM_MISSES` | `NUMBER` | Total number of times client requests could not find a matching pooled server in the pool |
| `NUM_WAITS` | `NUMBER` | Total number of client requests that had to wait due to non-availability of free pooled servers |
| `WAIT_TIME` | `NUMBER` | Reserved for future use |
| `CLIENT_REQ_TIMEOUTS` | `NUMBER` | Reserved for future use |
| `NUM_AUTHENTICATIONS` | `NUMBER` | Total number of authentications of clients done by the pool |
| `NUM_PURGED` | `NUMBER` | Total number of sessions purged by the pool |
| `HISTORIC_MAX` | `NUMBER` | Maximum size that the pool has ever reached |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Note:

In a multitenant container database (CDB), this view returns data only when queried from a CDB root. When queried from a PDB, this view returns 0 rows.