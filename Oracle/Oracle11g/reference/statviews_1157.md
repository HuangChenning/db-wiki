---
title: ALL_OBJECT_TABLES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1157.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_OBJECT_TABLES` describes the object tables accessible to the current user.

Related Views

- `DBA_OBJECT_TABLES` describes all object tables in the database.
- `USER_OBJECT_TABLES` describes the object tables owned by the current user. This view does not display the `OWNER` column.

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
| `LOGGING` | `VARCHAR2(3)` |  | Indicates whether or not changes to the table are logged: - `YES` - `NO` |
| `BACKED_UP` | `VARCHAR2(1)` |  | Indicates whether the table has been backed up since the last modification (`Y`) or not (`N`) |
| `NUM_ROWS` | `NUMBER` |  | Number of rows in the table |
| `BLOCKS` | `NUMBER` |  | Number of used blocks in the table |
| `EMPTY_BLOCKS` | `NUMBER` |  | Number of empty (never used) blocks in the table |
| `AVG_SPACE` | `NUMBER` |  | Average available free space in the table |
| `CHAIN_CNT` | `NUMBER` |  | Number of chained rows in the table |
| `AVG_ROW_LEN` | `NUMBER` |  | Average row length, including row overhead |
| `AVG_SPACE_FREELIST_BLOCKS` | `NUMBER` |  | Average free space of all blocks on a freelist |
| `NUM_FREELIST_BLOCKS` | `NUMBER` |  | Number of blocks on the freelist |
| `DEGREE` | `VARCHAR2(10)` |  | Number of parallel execution processes per instance for scanning the table, or `DEFAULT` |
| `INSTANCES` | `VARCHAR2(10)` |  | Number of instances across which the table is to be scanned, or `DEFAULT` |
| `CACHE` | `VARCHAR2(5)` |  | Indicates whether the table is to be cached in the buffer cache (`Y`) or not (`N`) |
| `TABLE_LOCK` | `VARCHAR2(8)` |  | Indicates whether table locking is enabled (`ENABLED`) or disabled (`DISABLED`) |
| `SAMPLE_SIZE` | `NUMBER` |  | Sample size used in analyzing this table |
| `LAST_ANALYZED` | `DATE` |  | Date on which this table was most recently analyzed |
| `PARTITIONED` | `VARCHAR2(3)` |  | Indicates whether the table is partitioned (`YES`) or not (`NO`) |
| `IOT_TYPE` | `VARCHAR2(12)` |  | If the table is an index-organized table, then `IOT_TYPE` is `IOT`, `IOT_OVERFLOW`, or `IOT_MAPPING`. If the table is not an index-organized table, then `IOT_TYPE` is NULL. |
| `OBJECT_ID_TYPE` | `VARCHAR2(16)` |  | Indicates whether the object ID (OID) is `USER-DEFINED` or `SYSTEM GENERATED` |
| `TABLE_TYPE_OWNER` | `VARCHAR2(30)` |  | Owner of the type of the table |
| `TABLE_TYPE` | `VARCHAR2(30)` |  | Type of the table |
| `TEMPORARY` | `VARCHAR2(1)` |  | Indicates whether this is a temporary table (`Y`) or not (`N`) |
| `SECONDARY` | `VARCHAR2(1)` |  | Indicates whether the object table is a secondary object created by the ODCIIndexCreate method of the Oracle Data Cartridge (`Y`) or not (`N`) |
| `NESTED` | `VARCHAR2(3)` |  | Indicates whether the table is a nested table (`YES`) or not (`NO`) |
| `BUFFER_POOL` | `VARCHAR2(7)` |  | Buffer pool to be used for table blocks: - `DEFAULT` - `KEEP` - `RECYCLE` - NULL |
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
| `SEGMENT_CREATED` | `VARCHAR2(3)` |  | Indicates whether the table segment has been created (`YES`) or not (`NO`) |

<sup>Footnote 1</sup> Hybrid Columnar Compression is a feature of the Enterprise Edition of Oracle Database that is dependent on the underlying storage system. See [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/tablecls.htm#CNCPT89198) for more information.

See Also:

- ["DBA\_OBJECT\_TABLES"](statviews_4157.md)
- ["USER\_OBJECT\_TABLES"](statviews_5375.md)