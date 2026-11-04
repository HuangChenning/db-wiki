---
title: "V$LOCK_ACTIVITY"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2028.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$LOCK_ACTIVITY` is deprecated. The information that was provided in this view is now provided in the `V$INSTANCE_CACHE_TRANSFER` and `V$SEGMENT_STATISTICS` views.

| Column | Datatype | Description |
| --- | --- | --- |
| `FROM_VAL` | `CHAR(4)` | Global Cache Resource initial state; always `NULL` |
| `TO_VAL` | `CHAR(1)` | Global Cache Resource initial state; always `S` |
| `ACTION_VAL` | `CHAR(21)` | Description of the conversion; always `Lock buffers for read` |
| `COUNTER` | `NUMBER` | Number of times the lock operation executed |