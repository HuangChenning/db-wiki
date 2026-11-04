---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-FAST_START_SERVERS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.224 V$FAST\_START\_SERVERS

`V$FAST_START_SERVERS` provides information about all the recovery workers performing parallel transaction recovery.

| Column | Datatype | Description |
| --- | --- | --- |
| `STATE` | `VARCHAR2(11)` | State of the server (`IDLE` or `RECOVERING`) |
| `UNDOBLOCKSDONE` | `NUMBER` | Number of undo blocks done so far |
| `PID` | `NUMBER` | Process ID |
| `XID` | `RAW(8)` | Transaction ID |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |