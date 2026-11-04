---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-PX_PROCESS.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.144 V$PX\_PROCESS

`V$PX_PROCESS` contains information about the sessions running parallel execution.

| Column | Datatype | Description |
| --- | --- | --- |
| `SERVER_NAME` | `VARCHAR2(4)` | The name of the PX server (P000, P001, and so on) |
| `STATUS` | `VARCHAR2(9)` | The state of the PX server (`IN` `USE` or `AVAILABLE`) |
| `PID` | `NUMBER` | The process identifier |
| `SPID` | `VARCHAR2(24)` | Operating system process ID |
| `SID` | `NUMBER` | The session ID of the PX server, if in use |
| `SERIAL#` | `NUMBER` | The session serial number of the PX server, if in use |
| `IS_GV` | `VARCHAR2(5)` | Indicates whether a PX server process in parallel is a normal process or a `GV$` process.  Possible values:  - `FALSE`: The PX server process in parallel is a normal process - `TRUE`: The PX server process in parallel is a `GV$` process |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |