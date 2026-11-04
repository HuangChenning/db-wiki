---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_TAB_PENDING_STATS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.114 ALL\_TAB\_PENDING\_STATS

`ALL_TAB_PENDING_STATS` describes pending statistics for tables, partitions, and subpartitions accessible to the current user.

Related Views

- `DBA_TAB_PENDING_STATS` describes pending statistics for tables, partitions, and subpartitions in the database.
- `USER_TAB_PENDING_STATS` describes pending statistics for tables, partitions, and subpartitions owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Name of the table |
| `PARTITION_NAME` | `VARCHAR2(128)` |  | Name of the partition |
| `SUBPARTITION_NAME` | `VARCHAR2(128)` |  | Name of the subpartition |
| `NUM_ROWS` | `NUMBER` |  | Number of rows |
| `BLOCKS` | `NUMBER` |  | Number of blocks |
| `AVG_ROW_LEN` | `NUMBER` |  | Average row length |
| `IM_IMCU_COUNT` | `NUMBER` |  | Number of In-Memory Compression Units (IMCUs) in the table. |
| `IM_BLOCK_COUNT` | `NUMBER` |  | Number of In-Memory blocks in the table. |
| `SCAN_RATE` | `NUMBER` |  | Scan rate for the table in megabytes per second. This statistic is only relevant or meaningful for external tables. |
| `SAMPLE_SIZE` | `NUMBER` |  | Sample size |
| `LAST_ANALYZED` | `DATE` |  | Time of last analyze operation |

See Also:

- " [DBA\_TAB\_PENDING\_STATS](DBA_TAB_PENDING_STATS.md) "
- " [USER\_TAB\_PENDING\_STATS](USER_TAB_PENDING_STATS.md) "