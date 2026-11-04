---
title: "V$PX_PROCESS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2113.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$PX_PROCESS` contains information about the sessions running parallel execution.

| Column | Datatype | Description |
| --- | --- | --- |
| `SERVER_NAME` | `VARCHAR2(4)` | The name of the PX server (P000, P001, and so on) |
| `STATUS` | `VARCHAR2(9)` | The state of the PX server (`IN USE` \| `AVAILABLE`) |
| `PID` | `NUMBER` | The process identifier |
| `SPID` | `VARCHAR2(12)` | OS process ID |
| `SID` | `NUMBER` | The session ID of the PX server, if in use |
| `SERIAL#` | `NUMBER` | The session serial number of the PX server, if in use |