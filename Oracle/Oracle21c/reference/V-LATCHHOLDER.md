---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-LATCHHOLDER.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.31 V$LATCHHOLDER

`V$LATCHHOLDER` displays information about the current latch holders.

| Column | Datatype | Description |
| --- | --- | --- |
| `PID` | `NUMBER` | Identifier of the process holding the latch |
| `SID` | `NUMBER` | Identifier of the session that owns the latch |
| `LADDR` | `RAW(4 \| 8)` | Latch address |
| `NAME` | `VARCHAR2(64)` | Name of the latch being held |
| `GETS` | `NUMBER` | Number of times that the latch was obtained in either wait mode or no-wait mode |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |