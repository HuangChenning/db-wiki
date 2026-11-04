---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-LOGMNR_PROCESS.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.56 V$LOGMNR\_PROCESS

`V$LOGMNR_PROCESS` identifies all processes attached to an active LogMiner persistent session.

(A persistent LogMiner session is created either by starting Data Guard SQL Apply on a logical standby database for the first time or by creating Replication capture.) This view can be joined with either the `V$SESSION` view or the `V$PROCESS` view to gather process-specific information.

| Column | Datatype | Description |
| --- | --- | --- |
| `SESSION_ID` | `NUMBER` | Unique identifier for the LogMiner persistent session |
| `PID` | `NUMBER` | Oracle process identifier for the SQL Apply or Replication capture process (same as the `V$PROCESS.PID`) |
| `SPID` | `VARCHAR2(24)` | Operating system process identifier (same as the `V$PROCESS.SPID`) |
| `ROLE` | `VARCHAR2(32)` | Identifies the role of the active LogMiner process: `READER`, `PREPARER`, `BUILDER`, `COORDINATOR`, or `APPLY SERVER` |
| `USERNAME` | `VARCHAR2(15)` | Operating system process user name that is connected to the database |
| `SID` | `NUMBER` | Session identifier for the `V$SESSION.SID` process |
| `SERIAL#` | `NUMBER` | Session serial number associated with the `V$SESSION.SERIAL` process |
| `LATCHWAIT` | `VARCHAR2(16)` | Address of the latch the process is waiting for; `NULL` if none |
| `LATCHSPIN` | `VARCHAR2(16)` | This column is obsolete |
| `WORK_MICROSEC` | `VARCHAR2(21)` | Microseconds spent by the process doing useful work |
| `OVERHEAD_MICROSEC` | `VARCHAR2(21)` | Microseconds spent by the process doing overhead tasks or simply waiting/idling |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

- " [V$SESSION](V-SESSION.md) "
- " [V$PROCESS](V-PROCESS.md) "