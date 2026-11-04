---
title: "V$GC_ELEMENT"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1152.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$GC_ELEMENT` displays one entry for each global cache resource that is used by the buffer cache. The name of the global cache resource that corresponds to a lock element is {'BL', indx, class}. This is a Real Application Clusters view.

| Column | Datatype | Description |
| --- | --- | --- |
| `GC_ELEMENT_ADDR` | `RAW(4 \| 8)` | Address of the lock element that contains the PCM lock that is covering the buffer. If more than one buffer has the same address, then these buffers are covered by the same PCM lock. |
| `INDX` | `NUMBER` | Platform specific lock manager identifier |
| `CLASS` | `NUMBER` | Platform specific lock manager identifier |
| `GC_ELEMENT_NAME` | `NUMBER` | Name of the lock that contains the PCM lock that is covering the buffer |
| `MODE_HELD` | `NUMBER` | Platform dependent value for lock mode held; often: 3 = share; 5 = exclusive |
| `BLOCK_COUNT` | `NUMBER` | Number of blocks covered by PCM lock |
| `RELEASING` | `NUMBER` | Nonzero if PCM lock is being downgraded |
| `ACQUIRING` | `NUMBER` | Nonzero if PCM lock is being upgraded |
| `WRITING` | `NUMBER` | If the GC\_ELEMENT is being written, the write status |
| `RECOVERING` | `NUMBER` | If the GC\_ELEMENT is being recovered, the recovery status |
| `LOCAL` | `NUMBER` | Zero if the GC\_ELEMENT is local, one if it is global |
| `FLAGS` | `NUMBER` | Process level flags for the lock element |