---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-GC_ELEMENT.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.244 V$GC\_ELEMENT

`V$GC_ELEMENT` displays one entry for each global cache resource that is used by the buffer cache. The name of the global cache resource that corresponds to a lock element is {'BL', indx, class}. This is an Oracle Real Application Clusters view.

| Column | Datatype | Description |
| --- | --- | --- |
| `GC_ELEMENT_ADDR` | `RAW(4 \| 8)` | Address of the lock element that contains the PCM lock that is covering the buffer. If more than one buffer has the same address, then these buffers are covered by the same PCM lock. |
| `INDX` | `NUMBER` | Platform specific lock manager identifier |
| `CLASS` | `NUMBER` | Platform specific lock manager identifier |
| `GC_ELEMENT_NAME` | `NUMBER` | Name of the lock that contains the PCM lock that is covering the buffer |
| `MODE_HELD` | `NUMBER` | Numeric global-cache lock mode for the element:  - `0` - Null (N): no shared/exclusive grant held - `1` - Shared (S): shared/read-compatible grant - `2` - Exclusive (X): exclusive grant |
| `BLOCK_COUNT` | `NUMBER` | Number of blocks covered by PCM lock |
| `RELEASING` | `NUMBER` | Nonzero if PCM lock is being downgraded |
| `ACQUIRING` | `NUMBER` | Nonzero if PCM lock is being upgraded |
| `WRITING` | `NUMBER` | If the GC\_ELEMENT is being written, the write status |
| `RECOVERING` | `NUMBER` | If the GC\_ELEMENT is being recovered, the recovery status |
| `LOCAL` | `NUMBER` | Zero if the GC\_ELEMENT is local, one if it is global |
| `FLAGS` | `NUMBER` | Process level flags for the lock element |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |