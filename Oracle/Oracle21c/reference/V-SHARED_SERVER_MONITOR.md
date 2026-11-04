---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SHARED_SERVER_MONITOR.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.42 V$SHARED\_SERVER\_MONITOR

`V$SHARED_SERVER_MONITOR` displays information for tuning the shared server.

| Column | Datatype | Description |
| --- | --- | --- |
| `MAXIMUM_CONNECTIONS` | `NUMBER` | Highest number of virtual circuits in use at one time since the instance started. If this value reaches the value set for the `CIRCUITS` initialization parameter, then consider raising the value of `CIRCUITS`.  See Also: " [CIRCUITS](CIRCUITS.md) " |
| `MAXIMUM_SESSIONS` | `NUMBER` | Highest number of shared server sessions in use at one time since the instance started. If this reaches the value set for the `SHARED_SERVER_SESSIONS` initialization parameter, then consider raising the value of `SHARED_SERVER_SESSIONS`.  See Also: " [SHARED\_SERVER\_SESSIONS](SHARED_SERVER_SESSIONS.md) " |
| `SERVERS_STARTED` | `NUMBER` | Total number of shared servers started since the instance started (but not including those started during startup) |
| `SERVERS_TERMINATED` | `NUMBER` | Total number of shared servers stopped by Oracle since the instance started |
| `SERVERS_HIGHWATER` | `NUMBER` | Highest number of servers running at one time since the instance started. If this value reaches the value set for the `MAX_SHARED_SERVERS` initialization parameter, then consider raising the value of `SHARED_SERVERS`.  See Also: " [SHARED\_SERVERS](SHARED_SERVERS.md) " |
| `DISPATCHERS_CPU` | `NUMBER` | Total CPU time of all dispatchers since the instance started (in millionths of a second) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |