---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-LATCH_MISSES.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.29 V$LATCH\_MISSES

`V$LATCH_MISSES` displays statistics about missed attempts to acquire a latch.

| Column | Datatype | Description |
| --- | --- | --- |
| `PARENT_NAME` | `VARCHAR2(64)` | Latch name of a parent latch |
| `WHERE` | `VARCHAR2(80)` | This column is obsolete and maintained for backward compatibility. The value of this column is always equal to the value in `LOCATION`. |
| `NWFAIL_COUNT` | `NUMBER` | Number of times that no-wait acquisition of the latch failed |
| `SLEEP_COUNT` | `NUMBER` | Number of times that acquisition attempts caused sleeps |
| `WTR_SLP_COUNT` | `NUMBER` | Number of times a waiter slept |
| `LONGHOLD_COUNT` | `NUMBER` | Number of times someone held a latch for the entire duration of someone else's sleep |
| `LOCATION` | `VARCHAR2(80)` | Location that attempted to acquire the latch |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |