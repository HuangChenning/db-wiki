---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-HANG_SESSION_INFO.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.274 V$HANG\_SESSION\_INFO

`V$HANG_SESSION_INFO` displays information about sessions involved in hangs described by `V$HANG_INFO`.

Each row with the same `HANG_ID` describes a session that is in the hang wait chain described by the row with the same `HANG_ID` in `V$HANG_INFO`. This session is blocked by the victim or final blocker of that hang.

| Column | Datatype | Description |
| --- | --- | --- |
| `HANG_ID` | `NUMBER` | A number identifying the hang including this session. This column can be used to join `V$HANG_INFO` with `V$HANG_SESSION_INFO`. |
| `INSTANCE` | `NUMBER` | Instance number of the instance on which this session resides |
| `SID` | `NUMBER` | Oracle session ID of this session |
| `SERIAL#` | `NUMBER` | Oracle session serial number of this session |
| `OSPID` | `VARCHAR2(24)` | Operating system process ID of this session |
| `FATAL_BACKGROUND` | `VARCHAR2(1)` | `Y` - Session is a critical background process  `N` - Session is not a critical background process |
| `ROOT` | `VARCHAR2(1)` | `Y` - This session is the victim or final blocker of the hang  `N` - This session is not the victim or final blocker of the hang |
| `PNAME` | `VARCHAR2(5)` | Name of the victim or final blocker process |
| `PDB_ID` | `NUMBER` | Oracle session's container ID or PDB ID |
| `WAIT_EVENT_TEXT` | `VARCHAR2(64)` | Resource or event for which this session is waiting; set to `not` `in` `a` `wait` if the session is not waiting on a resource |
| `WAIT_TIME` <sup>Foot 1</sup> | `NUMBER` | Time spent in wait for this session (in seconds). If the value of `WAIT_EVENT_TEXT` is `not` `in` `a` `wait`, then this column returns the number of seconds since the last wait. |
| `QOS_PC_RANK` | `VARCHAR2(12)` | Session's Oracle Database Quality of Service (QoS) Management Performance Class rank |
| `QOS_PC_ITT` | `NUMBER` | Session's Oracle Database Quality of Service (QoS) Management Performance Class In-Trouble Threshold |
| `QOS_PC_RTT` | `NUMBER` | Session's Oracle Database Quality of Service (QoS) Management Performance Class Root Termination allowed Threshold |
| `QOS_PC_KEY` | `NUMBER` | Session's Oracle Database Quality of Service (QoS) Management Performance Class Key |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 21c.