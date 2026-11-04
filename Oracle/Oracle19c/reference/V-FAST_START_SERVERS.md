---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/V-FAST_START_SERVERS.html
tags:
  - oracle
  - 19c
  - reference
---

## 7.216 V$FAST\_START\_SERVERS

`V$FAST_START_SERVERS` provides information about all the recovery workers performing parallel transaction recovery.

| Column | Datatype | Description |
| --- | --- | --- |
| `STATE` | `VARCHAR2(11)` | State of the server (`IDLE` or `RECOVERING`) |
| `UNDOBLOCKSDONE` | `NUMBER` | Number of undo blocks done so far |
| `PID` | `NUMBER` | Process ID |
| `XID` | `RAW(8)` | Transaction ID |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |