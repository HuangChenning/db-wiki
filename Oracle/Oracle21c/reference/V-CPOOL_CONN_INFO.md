---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-CPOOL_CONN_INFO.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.149 V$CPOOL\_CONN\_INFO

`V$CPOOL_CONN_INFO` displays connection information about each connection to the connection broker.

| Column | Datatype | Description |
| --- | --- | --- |
| `CMON_ADDR` | `RAW(4 \| 8)` | Address of the connection broker |
| `SESSION_ADDR` | `RAW(4 \| 8)` | Address of the session associated with the connection; NULL if the connection does not have an associated session |
| `CONNECTION_ADDR` | `RAW(4 \| 8)` | Address of the connection |
| `USERNAME` | `VARCHAR2(1024)` | Name of the user associated with the connection |
| `PROXY_USER` | `VARCHAR2(1024)` | Name of the proxy user |
| `CCLASS_NAME` | `VARCHAR2(1024)` | Connection class associated with the connection |
| `PURITY` | `VARCHAR2(1024)` | Purity used to create the connection (can be `SELF` or `NEW`) |
| `TAG` | `VARCHAR2(1024)` | Tag, if specified, at connection creation time |
| `SERVICE` | `VARCHAR2(64)` | TNS service name for the connection |
| `PROCESS_ID` | `VARCHAR2(24)` | Client process ID of the process which created the connection |
| `PROGRAM` | `VARCHAR2(84)` | Program name of the client process which created the connection |
| `MACHINE` | `VARCHAR2(64)` | Machine name of the client process which created the connection |
| `TERMINAL` | `VARCHAR2(30)` | Terminal identifier of the client process which created the connection |
| `CONNECTION_MODE` | `VARCHAR2(1024)` | Reserved for internal use |
| `CONNECTION_STATUS` | `VARCHAR2(10)` | Status of the connection:  - `NONE` - `CONNECTING` - `ACTIVE`: A pooled server has been mapped to this connection. - `WAITING`: The connection is waiting for a pooled server based on the client request. - `IDLE`: No pooled server has been mapped to this connection and there is no request to map one. - `CLOSING` |
| `CLIENT_REGID` | `NUMBER` | Query cache registration ID sent by the client |
| `CURSTATUS_TIME` | `NUMBER` | Time in microseconds spent in the current state. See `CONNECTION_STATUS` above. |
| `IDLE_TIME` | `NUMBER` | Total time in `IDLE` state for the connection (in microseconds) |
| `ACTIVE_TIME` | `NUMBER` | Total time in `ACTIVE` state for the connection (in microseconds) |
| `WAIT_TIME` | `NUMBER` | Total time in `WAITING` state for the connection (in microseconds) |
| `THINK_TIME` | `NUMBER` | Total think time for the connection assigned to the pooled server, but not doing any database activity (in microseconds) |
| `LAST_IDLE_TIME` | `NUMBER` | Time in last `IDLE` state for this connection (in microseconds) |
| `LAST_ACTIVE_TIME` | `NUMBER` | Time in last `ACTIVE` state for this connection (in microseconds) |
| `LAST_WAIT_TIME` | `NUMBER` | Time in last `WAITING` state for this connection (in microseconds) |
| `LAST_THINK_TIME` | `NUMBER` | Time for the connection assigned to the pooled server, but not doing any database activity during the last `ACTIVE` state (in microseconds) |
| `NUMGETS` | `NUMBER` | Total number of requests at the connection level |
| `NUMHITS` | `NUMBER` | Total number of hits at the connection level |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |