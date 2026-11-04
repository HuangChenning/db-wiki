---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-GC_ELEMENTS_WITH_COLLISIONS.html
tags:
  - oracle
  - 12c
  - reference
---

`V$GC_ELEMENTS_WITH_COLLISIONS` is deprecated. The information that was provided in this view is now provided in the `V$INSTANCE_CACHE_TRANSFER` and `V$SEGMENT_STATISTICS` views.

| Column | Datatype | Description |
| --- | --- | --- |
| `GC_ELEMENT_ADDR` | `RAW(4 \| 8)` | Address of the lock element that contains the PCM lock covering the buffer. If more than one buffer has the same address, then these buffers are covered by the same PCM lock. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

- " [V$INSTANCE\_CACHE\_TRANSFER](V-INSTANCE_CACHE_TRANSFER.md) "
- " [V$SEGMENT\_STATISTICS](V-SEGMENT_STATISTICS.md) "