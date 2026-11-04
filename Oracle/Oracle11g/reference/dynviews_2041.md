---
title: "V$LOGMNR_PROCESS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2041.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$LOGMNR_PROCESS` identifies all processes attached to an active LogMiner persistent session. (A persistent LogMiner session is created either by starting Data Guard SQL Apply on a logical standby database for the first time or by creating Streams capture.) This view can be joined with either the `V$SESSION` view or the `V$PROCESS` view to gather process-specific information.

| Column | Datatype | Description |
| --- | --- | --- |
| `SESSION_ID` | `NUMBER` | Unique identifier for the LogMiner persistent session |
| `PID` | `NUMBER` | Oracle process identifier for the SQL Apply or Streams capture process (same as the `V$PROCESS.PID`) |
| `SPID` | `VARCHAR2(12)` | Operating system process identifier (same as the `V$PROCESS.SPID`) |
| `ROLE` | `VARCHAR2(32)` | Identifies the role of the active LogMiner process: `READER`, `PREPARER`, `BUILDER`, `COORDINATOR`, or `APPLY SERVER` |
| `USERNAME` | `VARCHAR2(15)` | Operating system process user name that is connected to the database |
| `SID` | `NUMBER` | Session identifier for the `V$SESSION.SID` process |
| `SERIAL#` | `NUMBER` | Session serial number associated with the `V$SESSION.SERIAL` process |
| `LATCHWAIT` | `VARCHAR2(8)` | Address of the latch the process is waiting for; `NULL` if none |
| `LATCHSPIN` | `VARCHAR2(8)` | This column is obsolete |
| `WORK_MICROSEC` | `VARCHAR2(21)` | Microseconds spent by the process doing useful work |
| `OVERHEAD_MICROSEC` | `VARCHAR2(21)` | Microseconds spent by the process doing overhead tasks or simply waiting/idling |