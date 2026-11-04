---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-TEMP_CACHE_TRANSFER.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.106 V$TEMP\_CACHE\_TRANSFER

`V$TEMP_CACHE_TRANSFER` is deprecated. The information that was provided in this view is now provided in the `V$INSTANCE_CACHE_TRANSFER` and `V$SEGMENT_STATISTICS` views.

| Column | Datatype | Description |
| --- | --- | --- |
| `FILE_NUMBER` | `NUMBER` | Number of the temp file |
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
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

- " [V$INSTANCE\_CACHE\_TRANSFER](V-INSTANCE_CACHE_TRANSFER.md) "
- " [V$SEGMENT\_STATISTICS](V-SEGMENT_STATISTICS.md) "