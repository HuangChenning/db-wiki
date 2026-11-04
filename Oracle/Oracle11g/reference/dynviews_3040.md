---
title: "V$SHARED_SERVER_MONITOR"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3040.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SHARED_SERVER_MONITOR` displays information for tuning the shared server.

| Column | Datatype | Description |
| --- | --- | --- |
| `MAXIMUM_CONNECTIONS` | `NUMBER` | Highest number of virtual circuits in use at one time since the instance started. If this value reaches the value set for the `CIRCUITS` initialization parameter, then consider raising the value of `CIRCUITS`.  See Also: ["CIRCUITS"](initparams024.md) |
| `MAXIMUM_SESSIONS` | `NUMBER` | Highest number of shared server sessions in use at one time since the instance started. If this reaches the value set for the `SHARED_SERVER_SESSIONS` initialization parameter, then consider raising the value of `SHARED_SERVER_SESSIONS`.  See Also: ["SHARED\_SERVER\_SESSIONS"](initparams241.md) |
| `SERVERS_STARTED` | `NUMBER` | Total number of shared servers started since the instance started (but not including those started during startup) |
| `SERVERS_TERMINATED` | `NUMBER` | Total number of shared servers stopped by Oracle since the instance started |
| `SERVERS_HIGHWATER` | `NUMBER` | Highest number of servers running at one time since the instance started. If this value reaches the value set for the `MAX_SHARED_SERVERS` initialization parameter, then consider raising the value of `SHARED_SERVERS`.  See Also: ["SHARED\_SERVERS"](initparams242.md) |