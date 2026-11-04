---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-PX_SESSTAT.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.147 V$PX\_SESSTAT

`V$PX_SESSTAT` contains information about the sessions running parallel execution.

| Column | Datatype | Description |
| --- | --- | --- |
| `SADDR` | `RAW(4 \| 8)` | Session address |
| `SID` | `NUMBER` | Session identifier |
| `SERIAL#` | `NUMBER` | Session serial number |
| `QCSID` | `NUMBER` | Session identifier of the parallel coordinator |
| `QCSERIAL#` | `NUMBER` | Session serial number of the parallel coordinator |
| `QCINST_ID` | `NUMBER` | Instance number on which the parallel coordinator is running |
| `SERVER_GROUP` | `NUMBER` | The logical group of servers to which this cluster database process belongs |
| `SERVER_SET` | `NUMBER` | The logical set of servers that this cluster database process belongs to. A single server group will have at most two server sets. |
| `SERVER#` | `NUMBER` | The logical number of the cluster database process within a server set |
| `DEGREE` | `NUMBER` | The degree of parallelism being used by the server set |
| `REQ_DEGREE` | `NUMBER` | The degree of parallelism that was requested by the user when the statement was issued and before any resource, multiuser, or load balancing reductions |
| `STATISTIC#` | `NUMBER` | Statistic number |
| `VALUE` | `NUMBER` | Statistic value |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |