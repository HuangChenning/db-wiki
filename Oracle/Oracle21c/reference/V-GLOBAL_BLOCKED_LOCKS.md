---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-GLOBAL_BLOCKED_LOCKS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.265 V$GLOBAL\_BLOCKED\_LOCKS

| Column | Datatype | Description |
| --- | --- | --- |
| `ADDR` | `RAW(4 \| 8)` | Address of lock state object |
| `KADDR` | `RAW(4 \| 8)` | Address of lock |
| `SID` | `NUMBER` | Identifier of session holding the lock (number) |
| `TYPE` | `VARCHAR2(2)` | Resource type (char) |
| `ID1` | `NUMBER` | Resource identifier #1 (number) |
| `ID2` | `NUMBER` | Resource identifier #2 (number) |
| `LMODE` | `NUMBER` | Lock mode held (number) |
| `REQUEST` | `NUMBER` | Lock mode requested (number) |
| `CTIME` | `NUMBER` | Time since current mode was granted |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |