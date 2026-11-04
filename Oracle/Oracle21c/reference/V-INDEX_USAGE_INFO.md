---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-INDEX_USAGE_INFO.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.4 V$INDEX\_USAGE\_INFO

`V$INDEX_USAGE_INFO` keeps track of index usage since the last flush. A flush occurs every 15 minutes. After each flush, `ACTIVE_ELEM_COUNT` is reset to 0 and `LAST_FLUSH_TIME` is updated to the current time.

| Column | Datatype | Description |
| --- | --- | --- |
| `INDEX_STATS_ENABLED` | `NUMBER` | Indicates whether the index usage statistics are enabled. Possible values:  - `0`: Index statistics are disabled - `1`: Index statistics are enabled |
| `INDEX_STATS_COLLECTION_TYPE` | `NUMBER` | Indicates the type of collection used for the index usage statistics. Possible values:  - `0`: Indicates the ALL collection type. With this type of collection, the statistics are collected for each execution that has index access. Selecting this statistics collection type may have some impact on performance. - `1`: Indicates the SAMPLED collection type. With this type of collection, the statistics are collected based on sampling (only a few of the executions are considered when collecting the statistics). This is the default statistics collection type. 	Index statistics collected with the SAMPLED collection type are less accurate than index statistics collected with the ALL collection type. |
| `ACTIVE_ELEM_COUNT` | `NUMBER` | The number of active indexes since the last flush |
| `ALLOC_ELEM_COUNT` | `NUMBER` | The number of index entries allocated |
| `MAX_ELEM_COUNT` | `NUMBER` | The maximum number of active indexes that can be tracked |
| `FLUSH_COUNT` | `NUMBER` | Number of successful flushes since the database started |
| `TOTAL_FLUSH_DURATION` | `NUMBER` | Cumulative elapsed time taken to complete the index usage statistics flush since the database start |
| `LAST_FLUSH_TIME` | `TIMESTAMP(3)` | The time of the last flush |
| `STATUS_MSG` | `VARCHAR2(256)` | Status messages, if any. Flush errors are reported here. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This row is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [DBA\_INDEX\_USAGE](DBA_INDEX_USAGE.md) "