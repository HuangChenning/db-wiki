---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-LATCH_CHILDREN.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.28 V$LATCH\_CHILDREN

This view includes all columns of `V$LATCH` plus the `CHILD#` column. Note that child latches have the same parent if their `LATCH#` columns match each other.

| Column | Datatype | Description |
| --- | --- | --- |
| `ADDR` | `RAW(4 \| 8)` | Address of the latch object |
| `LATCH#` | `NUMBER` | Latch number of the parent latch |
| `CHILD#` | `NUMBER` | Child latch number (unique only to each parent latch) |
| `LEVEL#` | `NUMBER` | Latch level |
| `NAME` | `VARCHAR2(64)` | Latch name |
| `HASH` | `NUMBER` | Latch hash |
| `GETS` | `NUMBER` | Number of times the latch was requested in willing-to-wait mode |
| `MISSES` | `NUMBER` | Number of times the latch was requested in willing-to-wait mode and the requester had to wait |
| `SLEEPS` | `NUMBER` | Number of times a willing-to-wait latch request resulted in a session sleeping while waiting for the latch |
| `IMMEDIATE_GETS` | `NUMBER` | Number of times a latch was requested in no-wait mode |
| `IMMEDIATE_MISSES` | `NUMBER` | Number of times a no-wait latch request did not succeed (that is, missed) |
| `WAITERS_WOKEN` | `NUMBER` | This column has been deprecated and is present only for compatibility with previous releases of Oracle. No data is accumulated for this column; it will always have a value of zero. |
| `WAITS_HOLDING_LATCH` | `NUMBER` | This column has been deprecated and is present only for compatibility with previous releases of Oracle. No data is accumulated for this column; it will always have a value of zero. |
| `SPIN_GETS` | `NUMBER` | Willing-to-wait latch requests which missed the first try but succeeded while spinning |
| `SLEEP[1 \| 2 \| 3 \| 4 \| 5 \| 6 \| 7 \| 8 \| 9 \| 10 \| 11]` | `NUMBER` | These columns have been deprecated and are present only for compatibility with previous releases of Oracle. No data is accumulated for these columns; they will always have a value of zero. As a substitute for these columns you can query the appropriate rows of the `V$EVENT_HISTOGRAM` view where the `EVENT` column has a value of `latch free` or `latch:%`. |
| `WAIT_TIME` | `NUMBER` | Elapsed time spent waiting for the latch (in microseconds) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$LATCH](V-LATCH.md) "