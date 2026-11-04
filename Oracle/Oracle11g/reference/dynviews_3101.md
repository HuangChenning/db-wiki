---
title: "V$TEMP_CACHE_TRANSFER"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3101.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$TEMP_CACHE_TRANSFER` is deprecated. The information that was provided in this view is now provided in the `V$INSTANCE_CACHE_TRANSFER` and `V$SEGMENT_STATISTICS` views.

| Column | Datatype | Description |
| --- | --- | --- |
| `FILE_NUMBER` | `NUMBER` | Number of the tempfile |
| `X_2_NULL` | `NUMBER` | Number of blocks with Exclusive-to-NULL conversions; always `0` |
| `X_2_NULL_FORCED_WRITE` | `NUMBER` | Number of Exclusive-to-NULL forced writes; always `0` |
| `X_2_NULL_FORCED_STALE` | `NUMBER` | Number of Exclusive-to-NULL blocks converted to CR; always `0` |
| `X_2_S` | `NUMBER` | Number of blocks with Exclusive-to-Shared conversions; always `0` |
| `X_2_S_FORCED_WRITE` | `NUMBER` | Number of Exclusive-to-Shared forced writes; always `0` |
| `S_2_NULL` | `NUMBER` | Number of blocks with Shared-to-NULL conversions; always `0` |
| `S_2_NULL_FORCED_STALE` | `NUMBER` | Number of Shared-to-NULL blocks converted to CR; always `0` |
| `RBR` | `NUMBER` | Number of reuse blocks cross-instance calls; always `0` |
| `RBR_FORCED_WRITE` | `NUMBER` | Number of blocks written due to reuse blocks cross-instance calls; always `0` |
| `NULL_2_X` | `NUMBER` | Number of blocks with NULL-to-Exclusive conversions; always `0` |
| `S_2_X` | `NUMBER` | Number of blocks with Shared-to-Exclusive conversions; always `0` |
| `NULL_2_S` | `NUMBER` | Number of blocks with NULL-to-Shared conversions; always `0` |