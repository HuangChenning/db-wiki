---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-LOCK_ACTIVITY.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.42 V$LOCK\_ACTIVITY

`V$LOCK_ACTIVITY` is deprecated. The information that was provided in this view is now provided in the `V$INSTANCE_CACHE_TRANSFER` and `V$SEGMENT_STATISTICS` views.

| Column | Datatype | Description |
| --- | --- | --- |
| `FROM_VAL` | `CHAR(4)` | Global Cache Resource initial state; always `NULL` |
| `TO_VAL` | `CHAR(1)` | Global Cache Resource initial state; always `S` |
| `ACTION_VAL` | `CHAR(21)` | Description of the conversion; always `Lock buffers for read` |
| `COUNTER` | `NUMBER` | Number of times the lock operation executed |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

- " [V$INSTANCE\_CACHE\_TRANSFER](V-INSTANCE_CACHE_TRANSFER.md) "
- " [V$SEGMENT\_STATISTICS](V-SEGMENT_STATISTICS.md) "