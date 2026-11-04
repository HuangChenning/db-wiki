---
title: DBA_HIST_SEG_STAT
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4032.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_SEG_STAT` displays historical information about segment-level statistics. This view captures the top segments based on a set of criteria and captures information from `V$SEGSTAT`. The total value is the value of the statistics since instance startup. The delta value is the value of the statistics from the `BEGIN_INTERVAL_TIME` to the `END_INTERVAL_TIME` in the `DBA_HIST_SNAPSHOT` view.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `TS#` | `NUMBER` | `NOT NULL` | Tablespace number |
| `OBJ#` | `NUMBER` | `NOT NULL` | Dictionary object number |
| `DATAOBJ#` | `NUMBER` | `NOT NULL` | Data object number |
| `LOGICAL_READS_TOTAL` | `NUMBER` |  | Cumulative value for logical reads |
| `LOGICAL_READS_DELTA` | `NUMBER` |  | Delta value for logical reads |
| `BUFFER_BUSY_WAITS_TOTAL` | `NUMBER` |  | Cumulative value for buffer busy waits |
| `BUFFER_BUSY_WAITS_DELTA` | `NUMBER` |  | Delta value for buffer busy waits |
| `DB_BLOCK_CHANGES_TOTAL` | `NUMBER` |  | Cumulative value for db block changes |
| `DB_BLOCK_CHANGES_DELTA` | `NUMBER` |  | Delta value for db block changes |
| `PHYSICAL_READS_TOTAL` | `NUMBER` |  | Cumulative value for physical reads |
| `PHYSICAL_READS_DELTA` | `NUMBER` |  | Delta value for physical reads |
| `PHYSICAL_WRITES_TOTAL` | `NUMBER` |  | Cumulative value for physical writes |
| `PHYSICAL_WRITES_DELTA` | `NUMBER` |  | Delta value for physical writes |
| `PHYSICAL_READS_DIRECT_TOTAL` | `NUMBER` |  | Cumulative value for physical reads direct |
| `PHYSICAL_READS_DIRECT_DELTA` | `NUMBER` |  | Delta value for physical reads direct |
| `PHYSICAL_WRITES_DIRECT_TOTAL` | `NUMBER` |  | Cumulative value for physical writes direct |
| `PHYSICAL_WRITES_DIRECT_DELTA` | `NUMBER` |  | Delta value for physical writes direct |
| `ITL_WAITS_TOTAL` | `NUMBER` |  | Cumulative value for ITL waits |
| `ITL_WAITS_DELTA` | `NUMBER` |  | Delta value for ITL waits |
| `ROW_LOCK_WAITS_TOTAL` | `NUMBER` |  | Cumulative value for row lock waits |
| `ROW_LOCK_WAITS_DELTA` | `NUMBER` |  | Delta value for row lock waits |
| `GC_CR_BLOCKS_SERVED_TOTAL` | `NUMBER` |  | Cumulative value for global cache CR blocks served |
| `GC_CR_BLOCKS_SERVED_DELTA` | `NUMBER` |  | Delta value for global cache CR blocks served |
| `GC_CU_BLOCKS_SERVED_TOTAL` | `NUMBER` |  | Cumulative value for global cache current blocks served |
| `GC_CU_BLOCKS_SERVED_DELTA` | `NUMBER` |  | Delta value for global cache current blocks served |
| `GC_BUFFER_BUSY_TOTAL` | `NUMBER` |  | Cumulative value for global cache buffer busy |
| `GC_BUFFER_BUSY_DELTA` | `NUMBER` |  | Delta value for global cache buffer busy |
| `GC_CR_BLOCKS_RECEIVED_TOTAL` | `NUMBER` |  | Cumulative value for global cache CR blocks received |
| `GC_CR_BLOCKS_RECEIVED_DELTA` | `NUMBER` |  | Delta value for global cache CR blocks received |
| `GC_CU_BLOCKS_RECEIVED_TOTAL` | `NUMBER` |  | Cumulative value for global cache current blocks received |
| `GC_CU_BLOCKS_RECEIVED_DELTA` | `NUMBER` |  | Delta value for global cache current blocks received |
| `SPACE_USED_TOTAL` | `NUMBER` |  | Cumulative value for space used |
| `SPACE_USED_DELTA` | `NUMBER` |  | Delta value for space used |
| `SPACE_ALLOCATED_TOTAL` | `NUMBER` |  | Cumulative value for space allocated |
| `SPACE_ALLOCATED_DELTA` | `NUMBER` |  | Delta value for space allocated |
| `TABLE_SCANS_TOTAL` | `NUMBER` |  | Cumulative value for table scans |
| `TABLE_SCANS_DELTA` | `NUMBER` |  | Delta value for table scans |
| `CHAIN_ROW_EXCESS_TOTAL` | `NUMBER` |  | Cumulative value of number of chained row pieces that can be eliminated by table reorganization |
| `CHAIN_ROW_EXCESS_DELTA` | `NUMBER` |  | Delta value of number of chained row pieces that can be eliminated by table reorganization |
| `PHYSICAL_READ_REQUESTS_TOTAL` | `NUMBER` |  | Cumulative value of number of physical read I/O requests issued for the monitored segment |
| `PHYSICAL_READ_REQUESTS_DELTA` | `NUMBER` |  | Delta value of number of physical read I/O requests issued for the monitored segment |
| `PHYSICAL_WRITE_REQUESTS_TOTAL` | `NUMBER` |  | Cumulative value of number of physical write I/O requests issued for the monitored segment |
| `PHYSICAL_WRITE_REQUESTS_DELTA` | `NUMBER` |  | Delta value of number of physical write I/O requests issued for the monitored segment |
| `OPTIMIZED_PHYSICAL_READS_TOTAL` | `NUMBER` |  | Cumulative value of number of physical reads from Database Smart Flash Cache for the monitored segment |
| `OPTIMIZED_PHYSICAL_READS_DELTA` | `NUMBER` |  | Delta value of number of physical reads from Database Smart Flash Cache for the monitored segment |