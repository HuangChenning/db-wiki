---
title: "V$PX_SESSION"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2115.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$PX_SESSION` contains information about the sessions running parallel execution.

| Column | Datatype | Description |
| --- | --- | --- |
| `SADDR` | `RAW(4 \| 8)` | Session address |
| `SID` | `NUMBER` | Session identifier |
| `SERIAL#` | `NUMBER` | Session serial number |
| `QCSID` | `NUMBER` | Session identifier of the parallel coordinator |
| `QCSERIAL#` | `NUMBER` | Session serial number of the parallel coordinator |
| `QCINST_ID` | `NUMBER` | Instance number on which the parallel coordinator is running |
| `SERVER_GROUP` | `NUMBER` | The logical group of servers to which this cluster database process belongs |
| `SERVER_SET` | `NUMBER` | The logical set of servers to which this cluster database process belongs. A single server group will have at most two server sets. |
| `SERVER#` | `NUMBER` | The logical number of the cluster database process within a server set |
| `DEGREE` | `NUMBER` | The degree of parallelism being used by the server set |
| `REQ_DEGREE` | `NUMBER` | The degree of parallelism that was requested by the user when the statement was issued and prior to any resource, multi-user, or load balancing reductions |