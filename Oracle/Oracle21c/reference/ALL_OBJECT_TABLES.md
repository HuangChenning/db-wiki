---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_OBJECT_TABLES.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.293 ALL\_OBJECT\_TABLES

`ALL_OBJECT_TABLES` describes the object tables accessible to the current user.

Related Views

- `DBA_OBJECT_TABLES` describes all object tables in the database.
- `USER_OBJECT_TABLES` describes the object tables owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the table |
| `TABLESPACE_NAME` | `VARCHAR2(30)` |  | Name of the tablespace containing the table; NULL for partitioned, temporary, and index-organized tables |
| `CLUSTER_NAME` | `VARCHAR2(128)` |  | Name of the cluster, if any, to which the table belongs |
| `IOT_NAME` | `VARCHAR2(128)` |  | Name of the index-organized table, if any, to which the overflow or mapping table entry belongs. If the `IOT_TYPE` column is not NULL, then this column contains the base table name. |
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
| `FREELISTS ` | `NUMBER` |  | Number of process freelists allocated to the segment; NULL for partitioned tables |
| `FREELIST_GROUPS ` | `NUMBER` |  | Number of freelist groups allocated to the segment; NULL for partitioned tables |
| `LOGGING` | `VARCHAR2(3)` |  | Indicates whether or not changes to the table are logged:  - `YES` - `NO` |
| `BACKED_UP` | `VARCHAR2(1)` |  | Indicates whether the table has been backed up since the last modification (`Y`) or not (`N`) |
| `NUM_ROWS ` | `NUMBER` |  | Number of rows in the table |
| `BLOCKS` | `NUMBER` |  | Number of used blocks in the table |
| `EMPTY_BLOCKS` | `NUMBER` |  | Number of empty (never used) blocks in the table |
| `AVG_SPACE ` | `NUMBER` |  | Average available free space in the table |
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
| `TABLE_TYPE_OWNER` | `VARCHAR2(128)` |  | Owner of the type of the table |
| `TABLE_TYPE` | `VARCHAR2(128)` |  | Type of the table |
| `TEMPORARY` | `VARCHAR2(1)` |  | Indicates whether this is a temporary table (`Y`) or not (`N`) |
| `SECONDARY` | `VARCHAR2(1)` |  | Indicates whether the object table is a secondary object created by the ODCIIndexCreate method of the Oracle Data Cartridge (`Y`) or not (`N`) |
| `NESTED` | `VARCHAR2(3)` |  | Indicates whether the table is a nested table (`YES`) or not (`NO`) |
| `BUFFER_POOL` | `VARCHAR2(7)` |  | Buffer pool to be used for table blocks:  - `DEFAULT` - `KEEP` - `RECYCLE` - NULL |
| `FLASH_CACHE` | `VARCHAR2(7)` |  | Database Smart Flash Cache hint to be used for table blocks:  - `DEFAULT` - `KEEP` - `NONE`  Solaris and Oracle Linux functionality only. |
| `CELL_FLASH_CACHE` | `VARCHAR2(7)` |  | Cell flash cache hint to be used for table blocks:  - `DEFAULT` - `KEEP` - `NONE`  See Also: Oracle Exadata Storage Server Software documentation for more information |
| `ROW_MOVEMENT` | `VARCHAR2(8)` |  | Indicates whether partitioned row movement is enabled (`ENABLED`) or disabled (`DISABLED`) |
| `GLOBAL_STATS` | `VARCHAR2(3)` |  | `GLOBAL_STATS` will be `YES` if statistics are gathered or incrementally maintained, otherwise it will be `NO` |
| `USER_STATS` | `VARCHAR2(3)` |  | Indicates whether statistics were entered directly by the user (`YES`) or not (`NO`) |
| `DURATION` | `VARCHAR2(15)` |  | Indicates the duration of a temporary table:  - `SYS$SESSION` - Rows are preserved for the duration of the session - `SYS$TRANSACTION` - Rows are deleted after `COMMIT`  Null - Permanent table |
| `SKIP_CORRUPT` | `VARCHAR2(8)` |  | Indicates whether Oracle Database ignores blocks marked corrupt during table and index scans (`ENABLED`) or raises an error (`DISABLED`). To enable this feature, run the `DBMS_REPAIR`.`SKIP_CORRUPT_BLOCKS` procedure. |
| `MONITORING` | `VARCHAR2(3)` |  | Indicates whether the table has the `MONITORING` attribute set (`YES`) or not (`NO`) |
| `CLUSTER_OWNER` | `VARCHAR2(128)` |  | Owner of the cluster, if any, to which the table belongs |
| `DEPENDENCIES` | `VARCHAR2(8)` |  | Indicates whether row-level dependency tracking is enabled (`ENABLED`) or disabled (`DISABLED`) |
| `COMPRESSION` | `VARCHAR2(8)` |  | Indicates whether table compression is enabled (`ENABLED`) or not (`DISABLED`); NULL for partitioned tables |
| `COMPRESS_FOR` | `VARCHAR2(30)` |  | Default compression for what kind of operations:  - `BASIC` - `ADVANCED` - `QUERY LOW` - `QUERY HIGH` - `ARCHIVE LOW` - `ARCHIVE HIGH` - `NULL`  The `QUERY LOW`, `QUERY HIGH`, `ARCHIVE LOW`, and `ARCHIVE HIGH` values are associated with Hybrid Columnar Compression, a feature of the Enterprise Edition of Oracle Database. See [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=CNCPT89198) for more information. |
| `DROPPED` | `VARCHAR2(3)` |  | Indicates whether the table has been dropped and is in the recycle bin (`YES`) or not (`NO`); NULL for partitioned tables  This view does not return the names of tables that have been dropped. |
| `SEGMENT_CREATED` | `VARCHAR2(3)` |  | Indicates whether the table segment has been created (`YES`) or not (`NO`) |
| `INMEMORY` | `VARCHAR2(8)` |  | Indicates whether the In-Memory Column Store (IM column store) is enabled (`ENABLED`) or disabled (`DISABLED`) for this segment |
| `INMEMORY_PRIORITY` | `VARCHAR2(8)` |  | Indicates the priority for In-Memory Column Store (IM column store) population. Possible values:  - `LOW` - `MEDIUM` - `HIGH` - `CRITICAL` - `NONE` - `NULL`  This column has a value based on where the segments lie for a table. For example, if the table is partitioned and is enabled for the IM column store, the value is `NULL` for `ALL_TABLES` but non- `NULL` for `ALL_TAB_PARTITIONS`. |
| `INMEMORY_DISTRIBUTE` | `VARCHAR2(15)` |  | Indicates how the IM column store is distributed in an Oracle Real Application Clusters (Oracle RAC) environment:  - `AUTO` - `BY ROWID RANGE` - `BY PARTITION` - `BY SUBPARTITION` |
| `INMEMORY_COMPRESSION` | `VARCHAR2(17)` |  | Indicates the compression level for the IM column store:  - `NO MEMCOMPRESS` - `FOR DML` - `FOR QUERY [ LOW \| HIGH ]` - `FOR CAPACITY [ LOW \| HIGH ]` - `AUTO` - `NULL`  This column has a value based on where the segments lie for a table. For example, if the table is partitioned and is enabled for the IM column store, the value is `NULL` for `ALL_TABLES` but non- `NULL` for `ALL_TAB_PARTITIONS`. |
| `INMEMORY_DUPLICATE` | `VARCHAR2(13)` |  | Indicates the duplicate setting for the IM column store in an Oracle RAC environment:  - `NO DUPLICATE` - `DUPLICATE` - `DUPLICATE ALL` |
| `EXTERNAL` | `VARCHAR2(3)` |  | Indicates whether the table is an external table (`YES`) or not (`NO`). |
| `CELLMEMORY` <sup>Foot 1</sup> | `VARCHAR2(24)` |  | The value for columnar compression in the storage cell flash cache. Possible values:  - `ENABLED`: Oracle Exadata Storage will decide automatically whether to cache in columnar form - `DISABLED`: Oracle Exadata Storage is prevented from caching in columnar form - `NO CACHECOMPRESS`: Oracle Exadata Storage will cache in HCC format (no recompression) - `FOR QUERY`: Oracle Exadata Storage will recompress and cache in INMEMORY query high format - `FOR CAPACITY`: Oracle Exadata Storage will recompress and cache in INMEMORY capacity low format |
| `HYBRID` | `VARCHAR2(3)` |  | Indicates whether the table is a hybrid partitioned table (`YES`) or not (`NO`). A hybrid partitioned table can contain a mixture of partitions stored in segments and partitions stored externally. |
| `INMEMORY_SERVICE` | `VARCHAR2(12)` |  | Indicates how the IM column store is populated on various instances. The possible values are:  - `DEFAULT`: Data is populated on all instances specified with the `PARALLEL_INSTANCE_GROUP` initialization parameter. If that parameter is not set, then the data is populated on all instances. This is the default. - `NONE`: Data is not populated on any instance. - `ALL`: Data is populated on all instances, regardless of the value of the `PARALLEL_INSTANCE_GROUP` initialization parameter. - `USER_DEFINED`: Data is populated only on the instances on which the user-specified service is active. The service name corresponding to this is stored in the `INMEMORY_SERVICE_NAME` column. |
| `INMEMORY_SERVICE_NAME` | `VARCHAR2(1000)` |  | Indicates the service name for the service on which the IM column store should be populated. This column has a value only when the corresponding `INMEMORY_SERVICE` is `USER_DEFINED`. In all other cases, this column is null. |
| `MEMOPTIMIZE_READ` | `VARCHAR2(8)` |  | Indicates whether the table is enabled for Fast Key Based Access (`ENABLED`) or not (`DISABLED`) |
| `MEMOPTIMIZE_WRITE` | `VARCHAR2(8)` |  | For internal use only |
| `HAS_SENSITIVE_COLUMN` | `VARCHAR2(3)` |  | Indicates whether the table has one or more sensitive columns (`YES`) or not (`NO`) |
| `LOGICAL_REPLICATION` | `VARCHAR2(8)` |  | Indicates whether the table is enabled for logical replication (`ENABLED`) or not (`DISABLED`). This setting is ignored if database-wide column data supplemental logging is enabled. |

<sup>Footnote 1</sup> This column is intended for use with Oracle Exadata.