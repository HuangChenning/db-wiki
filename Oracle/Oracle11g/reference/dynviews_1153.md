---
title: "V$GC_ELEMENTS_WITH_COLLISIONS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1153.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$GC_ELEMENTS_WITH_COLLISIONS` is deprecated. The information that was provided in this view is now provided in the `V$INSTANCE_CACHE_TRANSFER` and `V$SEGMENT_STATISTICS` views.

| Column | Datatype | Description |
| --- | --- | --- |
| `GC_ELEMENT_ADDR` | `RAW(4 \| 8)` | Address of the lock element that contains the PCM lock covering the buffer. If more than one buffer has the same address, then these buffers are covered by the same PCM lock. |