---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_TABLES.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.122 ALL\_TABLES

`ALL_TABLES` describes the relational tables accessible to the current user. To gather statistics for this view, use the `DBMS_STATS` package.

Related Views

- `DBA_TABLES` describes all relational tables in the database.
- `USER_TABLES` describes the relational tables owned by the current user. This view does not display the `OWNER` column.

Note:

Columns marked with an asterisk (`*`) are populated only if you collect statistics on the table with the `DBMS_STATS` package.

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
| `LOGGING` | `VARCHAR2(3)` |  | Indicates whether or not changes to the table are logged; NULL for partitioned tables:  - `YES` - `NO` |
| `BACKED_UP` | `VARCHAR2(1)` |  | Indicates whether the table has been backed up since the last modification (`Y`) or not (`N`) |
| `NUM_ROWS*` | `NUMBER` |  | Number of rows in the table |
| `BLOCKS*` | `NUMBER` |  | Number of used data blocks in the table |
| `EMPTY_BLOCKS` | `NUMBER` |  | Number of empty (never used) data blocks in the table. This column is populated only if you collect statistics on the table using the `DBMS_STATS` package. |
| `AVG_SPACE*` | `NUMBER` |  | Average amount of free space, in bytes, in a data block allocated to the table |
| `CHAIN_CNT*` | `NUMBER` |  | Number of rows in the table that are chained from one data block to another, or which have migrated to a new block, requiring a link to preserve the old ROWID |
| `AVG_ROW_LEN*` | `NUMBER` |  | Average length of a row in the table (in bytes) |
| `AVG_SPACE_FREELIST_BLOCKS` | `NUMBER` |  | Average freespace of all blocks on a freelist |
| `NUM_FREELIST_BLOCKS` | `NUMBER` |  | Number of blocks on the freelist |
| `DEGREE` | `VARCHAR2(10)` |  | Number of threads per instance for scanning the table, or `DEFAULT` |
| `INSTANCES` | `VARCHAR2(10)` |  | Number of instances across which the table is to be scanned, or `DEFAULT` |
| `CACHE` | `VARCHAR2(5)` |  | Indicates whether the table is to be cached in the buffer cache (`Y`) or not (`N`) |
| `TABLE_LOCK` | `VARCHAR2(8)` |  | Indicates whether table locking is enabled (`ENABLED`) or disabled (`DISABLED`) |
| `SAMPLE_SIZE` | `NUMBER` |  | Sample size used in analyzing the table |
| `LAST_ANALYZED` | `DATE` |  | Date on which the table was most recently analyzed |
| `PARTITIONED` | `VARCHAR2(3)` |  | Indicates whether the table is partitioned (`YES`) or not (`NO`) |
| `IOT_TYPE` | `VARCHAR2(12)` |  | If the table is an index-organized table, then `IOT_TYPE` is `IOT`, `IOT_OVERFLOW`, or `IOT_MAPPING`. If the table is not an index-organized table, then `IOT_TYPE` is NULL. |
| `TEMPORARY` | `VARCHAR2(1)` |  | Indicates whether the table is temporary (`Y`) or not (`N`) |
| `SECONDARY` | `VARCHAR2(1)` |  | Indicates whether the table is a secondary object created by the ` ODCIIndexCreate` method of the Oracle Data Cartridge (`Y`) or not (`N`) |
| `NESTED` | `VARCHAR2(3)` |  | Indicates whether the table is a nested table (`YES`) or not (`NO`) |
| `BUFFER_POOL` | `VARCHAR2(7)` |  | Buffer pool for the table; `NULL` for partitioned tables:  - `DEFAULT` - `KEEP` - `RECYCLE` - `NULL` |
| `FLASH_CACHE` | `VARCHAR2(7)` |  | Database Smart Flash Cache hint to be used for table blocks:  - `DEFAULT` - `KEEP` - `NONE`  Solaris and Oracle Linux functionality only. |
| `CELL_FLASH_CACHE` | `VARCHAR2(7)` |  | Cell flash cache hint to be used for table blocks:  - `DEFAULT` - `KEEP` - `NONE`  See Also: Oracle Exadata Storage Server Software documentation for more information |
| `ROW_MOVEMENT` | `VARCHAR2(8)` |  | Indicates whether partitioned row movement is enabled (`ENABLED`) or disabled (`DISABLED`) |
| `GLOBAL_STATS` | `VARCHAR2(3)` |  | `GLOBAL_STATS` will be `YES` if statistics are gathered or incrementally maintained, otherwise it will be `NO` |
| `USER_STATS` | `VARCHAR2(3)` |  | Indicates whether statistics were entered directly by the user (`YES`) or not (`NO`) |
| `DURATION` | `VARCHAR2(15)` |  | Indicates the duration of a temporary table:  - `SYS$SESSION` - Rows are preserved for the duration of the session - `SYS$TRANSACTION` - Rows are deleted after `COMMIT`  Null - Permanent table |
| `SKIP_CORRUPT` | `VARCHAR2(8)` |  | Indicates whether Oracle Database ignores blocks marked corrupt during table and index scans (`ENABLED`) or raises an error (`DISABLED`). To enable this feature, run the `DBMS_REPAIR`.`SKIP_CORRUPT_BLOCKS` procedure. |
| `MONITORING` | `VARCHAR2(3)` |  | This column is obsolete |
| `CLUSTER_OWNER` | `VARCHAR2(128)` |  | Owner of the cluster, if any, to which the table belongs |
| `DEPENDENCIES` | `VARCHAR2(8)` |  | Indicates whether row-level dependency tracking is enabled (`ENABLED`) or disabled (`DISABLED`) |
| `COMPRESSION` | `VARCHAR2(8)` |  | Indicates whether table compression is enabled (`ENABLED`) or not (`DISABLED`); NULL for partitioned tables |
| `COMPRESS_FOR` | `VARCHAR2(30)` |  | Default compression for what kind of operations:  - `BASIC` - `ADVANCED` - `QUERY LOW` - `QUERY HIGH` - `ARCHIVE LOW` - `ARCHIVE HIGH` - `QUERY LOW ROW LEVEL LOCKING` - `QUERY HIGH ROW LEVEL LOCKING` - `ARCHIVE LOW ROW LEVEL LOCKING` - `ARCHIVE HIGH ROW LEVEL LOCKING` - `NO ROW LEVEL LOCKING` - `NULL`  The `QUERY LOW`, `QUERY HIGH`, `ARCHIVE LOW`, `ARCHIVE HIGH`, `QUERY LOW ROW LEVEL LOCKING`, `QUERY HIGH ROW LEVEL LOCKING`, `ARCHIVE LOW ROW LEVEL LOCKING`, `ARCHIVE HIGH ROW LEVEL LOCKING`, and `NO ROW LEVEL LOCKING` values are associated with Hybrid Columnar Compression, a feature of the Enterprise Edition of Oracle Database that is dependent on the underlying storage system. See [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=CNCPT89198) for more information. |
| `DROPPED` | `VARCHAR2(3)` |  | Indicates whether the table has been dropped and is in the recycle bin (`YES`) or not (`NO`); NULL for partitioned tables  This view does not return the names of tables that have been dropped. |
| `READ_ONLY` | `VARCHAR2(3)` |  | Indicates whether the table segment is `READ-ONLY` or not. Possible values:  - `YES` - The table segment is `READ-ONLY` - `NO` - The table segment is not `READ-ONLY` - `N/A` - Not applicable. This value appears in a partitioned table, where there is no segment that relates to the logical table object. |
| `SEGMENT_CREATED` | `VARCHAR2(3)` |  | Indicates whether the table segment is created. Possible values:  - `YES` - The table segment is created. - `NO` - The table segment is not created. - `N/A` - Not applicable. This value appears in a partitioned table, where there is no segment that relates to the logical table object. |
| `RESULT_CACHE` | `VARCHAR2(7)` |  | Result cache mode annotation for the table:  - `DEFAULT` - Table has not been annotated - `FORCE` - `MANUAL` |
| `CLUSTERING` | `VARCHAR2(3)` |  | Indicates whether the table has the attribute clustering clause (`YES`) or not (`NO`) |
| `ACTIVITY_TRACKING` | `VARCHAR2(23)` |  | Indicates whether Heat Map tracking is enabled on the table |
| `DML_TIMESTAMP` | `VARCHAR2(25)` |  | Modification time, creation time, or both for Automatic Data Optimization |
| `HAS_IDENTITY` | `VARCHAR2(3)` |  | Indicates whether the table has an identity column (`YES`) or not (`NO`) |
| `CONTAINER_DATA` | `VARCHAR2(3)` |  | Indicates whether the table contains container-specific data. Possible values:  - `YES` if the table was created with the `CONTAINER_DATA` clause - `NO` otherwise |
| `INMEMORY` | `VARCHAR2(8)` |  | Indicates whether the In-Memory Column Store (IM column store) is enabled (`ENABLED`) or disabled (`DISABLED`) for the table |
| `INMEMORY_PRIORITY` | `VARCHAR2(8)` |  | Indicates the priority for In-Memory Column Store (IM column store) population. Possible values:  - `LOW` - `MEDIUM` - `HIGH` - `CRITICAL` - `NONE` - `NULL` |
| `INMEMORY_DISTRIBUTE` | `VARCHAR2(15)` |  | Indicates how the IM column store is distributed in an Oracle Real Application Clusters (Oracle RAC) environment:  - `AUTO` - `BY ROWID RANGE` - `DUPLICATE` - `NONE` - `NULL` |
| `INMEMORY_COMPRESSION` | `VARCHAR2(17)` |  | Indicates the compression level for the IM column store:  - `NO MEMCOMPRESS` - `FOR DML` - `FOR QUERY [ LOW \| HIGH ]` - `FOR CAPACITY [ LOW \| HIGH ]` - `AUTO` - `NULL`  This column has a value based on where the segments lie for a table. For example, if the table is partitioned and is enabled for the IM column store, the value is `NULL` for `ALL_TABLES` but non- `NULL` for `ALL_TAB_PARTITIONS`. |
| `INMEMORY_DUPLICATE` | `VARCHAR2(13)` |  | Indicates the duplicate setting for the IM column store in an Oracle RAC environment:  - `NO DUPLICATE` - `DUPLICATE` - `DUPLICATE ALL` |
| `DEFAULT_COLLATION` | `VARCHAR2(100)` |  | Default collation for the table |
| `DUPLICATED` | `VARCHAR2(1)` |  | Indicates whether the table is duplicated on this shard (`Y`) or not (`N`) |
| `SHARDED` | `VARCHAR2(1)` |  | Indicates whether the table is sharded (`Y`) or not (`N`) |
| `EXTERNALLY_SHARDED` | `VARCHAR2(1)` |  | Indicates whether the table is externally sharded (`Y`) or not (`N`) |
| `EXTERNALLY_DUPLICATED` | `VARCHAR2(1)` |  | Indicates whether the table is externally duplicated (`Y`) or not (`N`) |
| `EXTERNAL` | `VARCHAR2(3)` |  | Indicates whether the table is an external table (`YES`) or not (`NO`) |
| `HYBRID` | `VARCHAR2(3)` |  | Indicates whether the table is a hybrid partitioned table (`YES`) or not (`NO`). A hybrid partitioned table can contain a mixture of partitions stored in segments and partitions stored externally. |
| `CELLMEMORY` | `VARCHAR2(24)` |  | The value for columnar compression in the storage cell flash cache. Possible values:  - `ENABLED`: Oracle Exadata Storage will decide automatically whether to cache in columnar form - `DISABLED`: Oracle Exadata Storage is prevented from caching in columnar form - `NO CACHECOMPRESS`: Oracle Exadata Storage will cache in HCC format (no recompression) - `FOR QUERY`: Oracle Exadata Storage will recompress and cache in INMEMORY query high format - `FOR CAPACITY`: Oracle Exadata Storage will recompress and cache in INMEMORY capacity low format  This column is intended for use with Oracle Exadata. |
| `CONTAINERS_DEFAULT` | `VARCHAR2(3)` |  | Indicates whether the table is enabled for `CONTAINERS()` by default (`YES`) or not (`NO`) |
| `CONTAINER_MAP` | `VARCHAR2(3)` |  | Indicates whether the table is enabled for use with the `container_map` database property (`YES`) or not (`NO`) |
| `EXTENDED_DATA_LINK` | `VARCHAR2(3)` |  | Indicates whether the table is enabled for fetching an extended data link from the root (`YES`) or not (`NO`) |
| `EXTENDED_DATA_LINK_MAP` | `VARCHAR2(3)` |  | For internal use only |
| `INMEMORY_SERVICE` | `VARCHAR2(12)` |  | Indicates how the IM column store is populated on various instances. The possible values are:  - `DEFAULT`: Data is populated on all instances specified with the `PARALLEL_INSTANCE_GROUP` initialization parameter. If that parameter is not set, then the data is populated on all instances. This is the default. - `NONE`: Data is not populated on any instance. - `ALL`: Data is populated on all instances, regardless of the value of the `PARALLEL_INSTANCE_GROUP` initialization parameter. - `USER_DEFINED`: Data is populated only on the instances on which the user-specified service is active. The service name corresponding to this is stored in the `INMEMORY_SERVICE_NAME` column. |
| `INMEMORY_SERVICE_NAME` | `VARCHAR2(1000)` |  | Indicates the service name for the service on which the IM column store should be populated. This column has a value only when the corresponding `INMEMORY_SERVICE` is `USER_DEFINED`. In all other cases, this column is null. |
| `CONTAINER_MAP_OBJECT` | `VARCHAR2(3)` |  | Indicates whether the table is used as the value of the `container_map` database property (`YES`) or not (`NO`) |
| `MEMOPTIMIZE_READ` | `VARCHAR2(8)` |  | Indicates whether the table is enabled for Fast Key Based Access (`ENABLED`) or not (`DISABLED`) |
| `MEMOPTIMIZE_WRITE` | `VARCHAR2(8)` |  | For internal use only |
| `HAS_SENSITIVE_COLUMN` | `VARCHAR2(3)` |  | Indicates whether the table has one or more sensitive columns (`YES`) or not (`NO`) |
| `ADMIT_NULL` | `VARCHAR2(3)` |  | Indicates whether the table admits null `CON_ID` data (`YES`) or not (`NO`) |
| `DATA_LINK_DML_ENABLED` | `VARCHAR2(3)` |  | Indicates whether DML is permitted on the Data Link table (`YES`) or not (`NO`) |
| `LOGICAL_REPLICATION` | `VARCHAR2(8)` |  | Indicates whether the table is enabled for logical replication (`ENABLED`) or not (`DISABLED`). This setting is ignored if database-wide column data supplemental logging is enabled. |

Examples

This SQL query returns the names of the tables in the `EXAMPLES` tablespace:

```
SELECT table_name FROM all_tables
WHERE tablespace_name = 'EXAMPLE' ORDER BY table_name;
```

This SQL query returns the name of the tablespace that contains the HR schema:

```
SELECT DISTINCT tablespace_name FROM all_tables WHERE owner='HR';
```