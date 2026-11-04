---
title: "V$LATCH"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2015.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$LATCH` displays aggregate latch statistics for both parent and child latches, grouped by latch name. Individual parent and child latch statistics are broken down in the views `V$LATCH_PARENT` and `V$LATCH_CHILDREN`.

| Column | Datatype | Description |
| --- | --- | --- |
| `ADDR` | `RAW(4 \| 8)` | Address of the latch object |
| `LATCH#` | `NUMBER` | Latch number |
| `LEVEL#` | `NUMBER` | Latch level |
| `NAME` | `VARCHAR2(64)` | Latch name |
| `HASH` | `NUMBER` | Latch hash |
| `GETS` | `NUMBER` | Number of times the latch was requested in willing-to-wait mode |
| `MISSES` | `NUMBER` | Number of times the latch was requested in willing-to-wait mode and the requestor had to wait |
| `SLEEPS` | `NUMBER` | Number of times a willing-to-wait latch request resulted in a session sleeping while waiting for the latch |
| `IMMEDIATE_GETS` | `NUMBER` | Number of times a latch was requested in no-wait mode |
| `IMMEDIATE_MISSES` | `NUMBER` | Number of times a no-wait latch request did not succeed (that is, missed) |
| `WAITERS_WOKEN` | `NUMBER` | This column has been deprecated and is present only for compatibility with previous releases of Oracle. No data is accumulated for this column; it will always have a value of zero. |
| `WAITS_HOLDING_LATCH` | `NUMBER` | This column has been deprecated and is present only for compatibility with previous releases of Oracle. No data is accumulated for this column; it will always have a value of zero. |
| `SPIN_GETS` | `NUMBER` | Willing-to-wait latch requests which missed the first try but succeeded while spinning |
| `SLEEP[1 \| 2 \| 3 \| 4 \| 5 \| 6 \| 7 \| 8 \| 9 \| 10 \| 11]` | `NUMBER` | These columns have been deprecated and are present only for compatibility with previous releases of Oracle. No data is accumulated for these columns; they will always have a value of zero. As a substitute for these columns you can query the appropriate rows of the `V$EVENT_HISTOGRAM` view where the `EVENT` column has a value of `latch free` or `latch:%`. |
| `WAIT_TIME` | `NUMBER` | Elapsed time spent waiting for the latch (in microseconds) |

See Also:

- ["V$LATCH\_CHILDREN"](dynviews_2016.md)
- ["V$LATCH\_PARENT"](dynviews_2018.md)