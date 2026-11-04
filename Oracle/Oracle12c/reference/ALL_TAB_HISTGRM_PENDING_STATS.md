---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_TAB_HISTGRM_PENDING_STATS.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_TAB_HISTGRM_PENDING_STATS` describes pending statistics for tables, partitions, and subpartitions accessible to the current user.

Related Views

- `DBA_TAB_HISTGRM_PENDING_STATS` describes pending statistics for tables, partitions, and subpartitions in the database.
- `USER_TAB_HISTGRM_PENDING_STATS` describes pending statistics for tables, partitions, and subpartitions owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Name of the table |
| `PARTITION_NAME` | `VARCHAR2(128)` |  | Name of the partition |
| `SUBPARTITION_NAME` | `VARCHAR2(128)` |  | Name of the subpartition |
| `COLUMN_NAME` | `VARCHAR2(128)` |  | Name of the column |
| `ENDPOINT_NUMBER` | `NUMBER` |  | Endpoint number |
| `ENDPOINT_VALUE` | `NUMBER` |  | Normalized endpoint value |
| `ENDPOINT_ACTUAL_VALUE` | `VARCHAR2(4000)` |  | Actual endpoint value |
| `ENDPOINT_ACTUAL_VALUE_RAW` | `RAW(1000)` |  | Endpoint actual value in raw format |
| `ENDPOINT_REPEAT_COUNT` | `NUMBER` |  | Frequency of the endpoint (applies only to hybrid histograms, and is set to 0 for other histogram types) |

See Also:

- " [DBA\_TAB\_HISTGRM\_PENDING\_STATS](DBA_TAB_HISTGRM_PENDING_STATS.md) "
- " [USER\_TAB\_HISTGRM\_PENDING\_STATS](USER_TAB_HISTGRM_PENDING_STATS.md) "