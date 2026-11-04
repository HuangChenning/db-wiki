---
title: ALL_TABLES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2117.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_TABLES` describes the relational tables accessible to the current user. To gather statistics for this view, use the `DBMS_STATS` package.

Related Views

- `DBA_TABLES` describes all relational tables in the database.
- `USER_TABLES` describes the relational tables owned by the current user. This view does not display the `OWNER` column.

Note:

Columns marked with an asterisk (`*`) are populated only if you collect statistics on the table with the `DBMS_STATS` package.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the table |
| `TABLESPACE_NAME` | `VARCHAR2(30)` |  | Name of the tablespace containing the table; NULL for partitioned, temporary, and index-organized tables |
| `CLUSTER_NAME` | `VARCHAR2(30)` |  | Name of the cluster, if any, to which the table belongs |
| `IOT_NAME` | `VARCHAR2(30)` |  | Name of the index-organized table, if any, to which the overflow or mapping table entry belongs. If the `IOT_TYPE` column is not NULL, then this column contains the base table name. |
| `STATUS` | `VARCHAR2(8)` |  | If a previous `DROP TABLE` operation failed, indicates whether the table is unusable (`UNUSABLE`) or valid (`VALID`) |
| `PCT_FREE` | `NUMBER` |  | Minimum percentage of free space in a block; NULL for partitioned tables |
| `PCT_USED` | `NUMBER` |  | Minimum percentage of used space in a block; NULL for partitioned tables |
| `INI_TRANS` | `NUMBER` |  | Initial number of transactions; NULL for partitioned tables |
| `MAX_TRANS` | `NUMBER` |  | Maximum number of transactions; NULL for partitioned tables |
| `INITIAL_EXTENT` | `NUMBER` |  | Size of the initial extent (in bytes); NULL for partitioned tables |
| `NEXT_EXTENT` | `NUMBER` |  | Size of secondary extents (in bytes); NULL for partitioned tables |
| `MIN_EXTENTS` | `NUMBER` |  | Minimum number of extents allowed in the segment; NULL for partitioned tables |
| `MAX_EXTENTS` | `NUMBER` |  | Maximum number of extents allowed in the segment; NULL for partitioned tables |
| `PCT_INCREASE` | `NUMBER` |  | Percentage increase in extent size; NULL for partitioned tables |
| `FREELISTS` | `NUMBER` |  | Number of process freelists allocated to the segment; NULL for partitioned tables |
| `FREELIST_GROUPS` | `NUMBER` |  | Number of freelist groups allocated to the segment; NULL for partitioned tables |
| `LOGGING` | `VARCHAR2(3)` |  | Indicates whether or not changes to the table are logged; NULL for partitioned tables: - `YES` - `NO` |
| `BACKED_UP` | `VARCHAR2(1)` |  | Indicates whether the table has been backed up since the last modification (`Y`) or not (`N`) |
| `NUM_ROWS*` | `NUMBER` |  | Number of rows in the table |
| `BLOCKS*` | `NUMBER` |  | Number of used data blocks in the table |
| `EMPTY_BLOCKS` | `NUMBER` |  | Number of empty (never used) data blocks in the table. This column is populated only if you collect statistics on the table using the `DBMS_STATS` package. |
| `AVG_SPACE*` | `NUMBER` |  | Average amount of free space, in bytes, in a data block allocated to the table |
| `CHAIN_CNT*` | `NUMBER` |  | Number of rows in the table that are chained from one data block to another, or which have migrated to a new block, requiring a link to preserve the old ROWID |
| `AVG_ROW_LEN*` | `NUMBER` |  | Average length of a row in the table (in bytes) |
| `AVG_SPACE_FREELIST   _BLOCKS` | `NUMBER` |  | Average freespace of all blocks on a freelist |
| `NUM_FREELIST_BLOCKS` | `NUMBER` |  | Number of blocks on the freelist |
| `DEGREE` | `VARCHAR2(10)` |  | Number of threads per instance for scanning the table, or `DEFAULT` |
| `INSTANCES` | `VARCHAR2(10)` |  | Number of instances across which the table is to be scanned, or `DEFAULT` |
| `CACHE` | `VARCHAR2(5)` |  | Indicates whether the table is to be cached in the buffer cache (`Y`) or not (`N`) |
| `TABLE_LOCK` | `VARCHAR2(8)` |  | Indicates whether table locking is enabled (`ENABLED`) or disabled (`DISABLED`) |
| `SAMPLE_SIZE` | `NUMBER` |  | Sample size used in analyzing this table |
| `LAST_ANALYZED` | `DATE` |  | Date on which this table was most recently analyzed |
| `PARTITIONED` | `VARCHAR2(3)` |  | Indicates whether the table is partitioned (`YES`) or not (`NO`) |
| `IOT_TYPE` | `VARCHAR2(12)` |  | If the table is an index-organized table, then `IOT_TYPE` is `IOT`, `IOT_OVERFLOW`, or `IOT_MAPPING`. If the table is not an index-organized table, then `IOT_TYPE` is NULL. |
| `TEMPORARY` | `VARCHAR2(1)` |  | Indicates whether the table is temporary (`Y`) or not (`N`) |
| `SECONDARY` | `VARCHAR2(1)` |  | Indicates whether the table is a secondary object created by the `ODCIIndexCreate` method of the Oracle Data Cartridge (`Y`) or not (`N`) |
| `NESTED` | `VARCHAR2(3)` |  | Indicates whether the table is a nested table (`YES`) or not (`NO`) |
| `BUFFER_POOL` | `VARCHAR2(7)` |  | Buffer pool for the table; NULL for partitioned tables: - `DEFAULT` - `KEEP` - `RECYCLE` - NULL |
| `FLASH_CACHE` | `VARCHAR2(7)` |  | Database Smart Flash Cache hint to be used for table blocks: - `DEFAULT` - `KEEP` - `NONE`  Solaris and Oracle Linux functionality only. |
| `CELL_FLASH_CACHE` | `VARCHAR2(7)` |  | Cell flash cache hint to be used for table blocks: - `DEFAULT` - `KEEP` - `NONE`  See Also: Oracle Exadata Storage Server Software documentation for more information |
| `ROW_MOVEMENT` | `VARCHAR2(8)` |  | Indicates whether partitioned row movement is enabled (`ENABLED`) or disabled (`DISABLED`) |
| `GLOBAL_STATS` | `VARCHAR2(3)` |  | For partitioned tables, indicates whether statistics for the table as a whole (global statistics) are accurate (`YES`) or whether they were not collected and have to be estimated from statistics on underlying partitions and subpartitions (`NO`) |
| `USER_STATS` | `VARCHAR2(3)` |  | Indicates whether statistics were entered directly by the user (`YES`) or not (`NO`) |
| `DURATION` | `VARCHAR2(15)` |  | Indicates the duration of a temporary table: - `SYS$SESSION` - Rows are preserved for the duration of the session - `SYS$TRANSACTION` - Rows are deleted after `COMMIT`  Null - Permanent table |
| `SKIP_CORRUPT` | `VARCHAR2(8)` |  | Indicates whether Oracle Database ignores blocks marked corrupt during table and index scans (`ENABLED`) or raises an error (`DISABLED`). To enable this feature, run the `DBMS_REPAIR`.`SKIP_CORRUPT_BLOCKS` procedure. |
| `MONITORING` | `VARCHAR2(3)` |  | Indicates whether the table has the `MONITORING` attribute set (`YES`) or not (`NO`) |
| `CLUSTER_OWNER` | `VARCHAR2(30)` |  | Owner of the cluster, if any, to which the table belongs |
| `DEPENDENCIES` | `VARCHAR2(8)` |  | Indicates whether row-level dependency tracking is enabled (`ENABLED`) or disabled (`DISABLED`) |
| `COMPRESSION` | `VARCHAR2(8)` |  | Indicates whether table compression is enabled (`ENABLED`) or not (`DISABLED`); NULL for partitioned tables |
| `COMPRESS_FOR` | `VARCHAR2(12)` |  | Default compression for what kind of operations: - `BASIC` - `OLTP` - `QUERY LOW` <sup>Foot 1</sup> - `QUERY HIGH` <sup>Footref 1</sup> - `ARCHIVE LOW` <sup>Footref 1</sup> - `ARCHIVE HIGH` <sup>Footref 1</sup> - NULL |
| `DROPPED` | `VARCHAR2(3)` |  | Indicates whether the table has been dropped and is in the recycle bin (`YES`) or not (`NO`); NULL for partitioned tables |
| `READ_ONLY` | `VARCHAR2(3)` |  | Indicates whether the table IS READ-ONLY (`YES`) or not (`NO`) |
| `SEGMENT_CREATED` | `VARCHAR2(3)` |  | Indicates whether the table segment is created (`YES`) or not (`NO`) |
| `RESULT_CACHE` | `VARCHAR2(7)` |  | Result cache mode annotation for the table: |

<sup>Footnote 1</sup> Hybrid Columnar Compression is a feature of the Enterprise Edition of Oracle Database that is dependent on the underlying storage system. See [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/tablecls.htm#CNCPT89198) for more information.

See Also:

- ["DBA\_TABLES"](statviews_5056.md)
- ["USER\_TABLES"](statviews_5490.md)