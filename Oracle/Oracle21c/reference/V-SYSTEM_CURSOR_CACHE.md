---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SYSTEM_CURSOR_CACHE.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.99 V$SYSTEM\_CURSOR\_CACHE

`V$SYSTEM_CURSOR_CACHE` displays system wide information on cursor usage.

See Also:

" [V$SESSION\_CURSOR\_CACHE](V-SESSION_CURSOR_CACHE.md) "

| Column | Datatype | Description |
| --- | --- | --- |
| `OPENS` | `NUMBER` | Cumulative total of cursor opens |
| `HITS` | `NUMBER` | Cumulative total of cursor open hits |
| `HIT_RATIO` | `NUMBER` | Ratio of the number of times an open cursor was found divided by the number of times a cursor was sought |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |