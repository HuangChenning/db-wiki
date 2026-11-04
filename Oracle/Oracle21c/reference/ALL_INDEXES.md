---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_INDEXES.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.236 ALL\_INDEXES

`ALL_INDEXES` describes the indexes on the tables accessible to the current user.

To gather statistics for this view and the related views `DBA_INDEXES` and `USER_INDEXES`, use the `DBMS_STATS` package.

Related Views

- `DBA_INDEXES` describes all indexes in the database.
- `USER_INDEXES` describes the indexes owned by the current user. This view does not display the `OWNER` column.

Note:

Column names followed by an asterisk are populated only if you collect statistics on the index using the `DBMS_STATS` package.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the index |
| `INDEX_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the index |
| `INDEX_TYPE` | `VARCHAR2(27)` |  | Type of the index:  - `BITMAP` - `CLUSTER` - `DOMAIN` - `FUNCTION-BASED                                                   BITMAP` - `FUNCTION-BASED                                                   DOMAIN` - `FUNCTION-BASED                                                   NORMAL` - `FUNCTION-BASED                                                   NORMAL/REV` - `IOT - TOP` - `LOB` - `NORMAL` - `NORMAL/REV` |
| `TABLE_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the indexed object |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the indexed object |
| `TABLE_TYPE` | `VARCHAR2(11)` |  | Type of the indexed object  In the `DBA_INDEXES` and `USER_INDEXES` views, the possible values are:  - `CLUSTER` - `INDEX` - `NEXT` `OBJECT` - `SEQUENCE` - `SYNONYM` - `TABLE` - `VIEW`  In the `ALL_INDEXES` view, the value of this column is always `TABLE` and the data type is `CHAR(5)`. |
| `UNIQUENESS` | `VARCHAR2(9)` |  | Indicates whether the index is unique (`UNIQUE`) or nonunique (`NONUNIQUE`) |
| `COMPRESSION` | `VARCHAR2(13)` |  | Type of compression being used for the index:  - `ENABLED` - Prefix compression - `ADVANCED HIGH` - Advanced high compression - `ADVANCED LOW` - Advanced low compression - `DISABLED` - No compression is present |
| `PREFIX_LENGTH` | `NUMBER` |  | Number of columns in the prefix of the compression key |
| `TABLESPACE_NAME` | `VARCHAR2(30)` |  | Name of the tablespace containing the index |
| `INI_TRANS` | `NUMBER` |  | Initial number of transactions |
| `MAX_TRANS` | `NUMBER` |  | Maximum number of transactions |
| `INITIAL_EXTENT` | `NUMBER` |  | Size of the initial extent |
| `NEXT_EXTENT` | `NUMBER` |  | Size of secondary extents |
| `MIN_EXTENTS` | `NUMBER` |  | Minimum number of extents allowed in the segment |
| `MAX_EXTENTS` | `NUMBER` |  | Maximum number of extents allowed in the segment |
| `PCT_INCREASE` | `NUMBER` |  | Percentage increase in extent size |
| `PCT_THRESHOLD` | `NUMBER` |  | Threshold percentage of block space allowed per index entry |
| `INCLUDE_COLUMN` | `NUMBER` |  | Column ID of the last column to be included in index-organized table primary key (non-overflow) index. This column maps to the `COLUMN_ID` column of the `*_TAB_COLUMNS` view. |
| `FREELISTS ` | `NUMBER` |  | Number of process freelists allocated to this segment |
| `FREELIST_GROUPS` | `NUMBER` |  | Number of freelist groups allocated to this segment |
| `PCT_FREE` | `NUMBER` |  | Minimum percentage of free space in a block |
| `LOGGING` | `VARCHAR2(3)` |  | Indicates whether or not changes to the index are logged:  - `YES` - `NO` |
| `BLEVEL*` | `NUMBER` |  | B\*-Tree level (depth of the index from its root block to its leaf blocks). A depth of `0` indicates that the root block and leaf block are the same. |
| `LEAF_BLOCKS*` | `NUMBER` |  | Number of leaf blocks in the index |
| `DISTINCT_KEYS*` | `NUMBER` |  | Number of distinct indexed values. For indexes that enforce `UNIQUE` and `PRIMARY KEY` constraints, this value is the same as the number of rows in the table (`*_TABLES.NUM_ROWS`) |
| `AVG_LEAF_BLOCKS_PER_KEY*` | `NUMBER` |  | Average number of leaf blocks in which each distinct value in the index appears, rounded to the nearest integer. For indexes that enforce `UNIQUE` and `PRIMARY KEY` constraints, this value is always `1`. |
| `AVG_DATA_BLOCKS_PER_KEY*` | `NUMBER` |  | Average number of data blocks in the table that are pointed to by a distinct value in the index rounded to the nearest integer. This statistic is the average number of data blocks that contain rows that contain a given value for the indexed columns. |
| `CLUSTERING_FACTOR*` | `NUMBER` |  | Indicates the amount of order of the rows in the table based on the values of the index.  - If the value is near the number of blocks, then the table is very well ordered. In this case, the index entries in a single leaf block tend to point to rows in the same data blocks. - If the value is near the number of rows, then the table is very randomly ordered. In this case, it is unlikely that index entries in the same leaf block point to rows in the same data blocks.  For bitmap indexes, this column is not applicable. |
| `STATUS` | `VARCHAR2(8)` |  | Indicates whether a nonpartitioned index is `VALID` or `UNUSABLE` |
| `NUM_ROWS` | `NUMBER` |  | Number of rows in the index.  For bitmap indexes, this column is the number of distinct keys, so its value is the same as the `DISTINCT_KEYS` column. |
| `SAMPLE_SIZE` | `NUMBER` |  | Size of the sample used to analyze the index |
| `LAST_ANALYZED` | `DATE` |  | Date on which this index was most recently analyzed |
| `DEGREE` | `VARCHAR2(40)` |  | Number of threads per instance for scanning the index, or `DEFAULT` |
| `INSTANCES` | `VARCHAR2(40)` |  | Number of instances across which the indexes to be scanned, or `DEFAULT` |
| `PARTITIONED` | `VARCHAR2(3)` |  | Indicates whether the index is partitioned (`YES`) or not (`NO`) |
| `TEMPORARY` | `VARCHAR2(1)` |  | Indicates whether the index is on a temporary table (`Y`) or not (`N`) |
| `GENERATED` | `VARCHAR2(1)` |  | Indicates whether the name of the index is system-generated (`Y`) or not (`N`) |
| `SECONDARY` | `VARCHAR2(1)` |  | Indicates whether the index is a secondary object created by the `ODCIIndexCreate` method of the Oracle Data Cartridge (`Y`) or not (`N`) |
| `BUFFER_POOL` | `VARCHAR2(7)` |  | Buffer pool to be used for index blocks:  - `DEFAULT` - `KEEP` - `RECYCLE` - NULL |
| `FLASH_CACHE` | `VARCHAR2(7)` |  | Database Smart Flash Cache hint to be used for index blocks:  - `DEFAULT` - `KEEP` - `NONE`  Solaris and Oracle Linux functionality only. |
| `CELL_FLASH_CACHE` | `VARCHAR2(7)` |  | Cell flash cache hint to be used for index blocks:  - `DEFAULT` - `KEEP` - `NONE`  See Also: Oracle Exadata Storage Server Software documentation for more information |
| `USER_STATS` | `VARCHAR2(3)` |  | Indicates whether statistics were entered directly by the user (`YES`) or not (`NO`) |
| `DURATION` | `VARCHAR2(15)` |  | Indicates the duration of a temporary table:  - `SYS$SESSION` - Rows are preserved for the duration of the session - `SYS$TRANSACTION` - Rows are deleted after `COMMIT`  NULL - Permanent table |
| `PCT_DIRECT_ACCESS` | `NUMBER` |  | For a secondary index on an index-organized table, the percentage of rows with `VALID` guess |
| `ITYP_OWNER` | `VARCHAR2(128)` |  | For a domain index, the owner of the indextype |
| `ITYP_NAME` | `VARCHAR2(128)` |  | For a domain index, the name of the indextype |
| `PARAMETERS` | `VARCHAR2(1000)` |  | For a domain index, the parameter string |
| `GLOBAL_STATS` | `VARCHAR2(3)` |  | `GLOBAL_STATS` will be `YES` if statistics are gathered or incrementally maintained, otherwise it will be `NO` |
| `DOMIDX_STATUS` | `VARCHAR2(12)` |  | Status of a domain index:  - NULL - Index is not a domain index - `VALID` - Index is a valid domain index - `IDXTYP_INVLD` - Indextype of the domain index is invalid |
| `DOMIDX_OPSTATUS` | `VARCHAR2(6)` |  | Status of the operation on a domain index:  - NULL - Index is not a domain index - `VALID` - Operation performed without errors - `FAILED` - Operation failed with an error |
| `FUNCIDX_STATUS` | `VARCHAR2(8)` |  | Status of a function-based index:  - NULL - Index is not a function-based index - `ENABLED` - Function-based index is enabled - `DISABLED` - Function-based index is disabled |
| `JOIN_INDEX` | `VARCHAR2(3)` |  | Indicates whether the index is a join index (`YES`) or not (`NO`) |
| `IOT_REDUNDANT_PKEY_ELIM` | `VARCHAR2(3)` |  | Indicates whether redundant primary key columns are eliminated from secondary indexes on index-organized tables (`YES`) or not (`NO`) |
| `DROPPED` | `VARCHAR2(3)` |  | Indicates whether the index has been dropped and is in the recycle bin (`YES`) or not (`NO`); NULL for partitioned tables  This view does not return the names of indexes that have been dropped. |
| `VISIBILITY` | `VARCHAR2(9)` |  | Indicates whether the index is `VISIBLE` or `INVISIBLE` to the optimizer |
| `DOMIDX_MANAGEMENT` | `VARCHAR2(14)` |  | If this is a domain index, indicates whether the domain index is system-managed (`SYSTEM_MANAGED`) or user-managed (`USER_MANAGED`) |
| `SEGMENT_CREATED` | `VARCHAR2(3)` |  | Indicates whether the index segment has been created (`YES`) or not (`NO`) |
| `ORPHANED_ENTRIES` | `VARCHAR2(3)` |  | Indicates whether a global index contains stale entries because of deferred index maintenance during `DROP` / `TRUNCATE PARTITION`, or `MODIFY PARTITION INDEXING OFF` operations.  Possible values:  - `YES` - The index contains orphaned entries - `NO` - The index does not contain orphaned entries |
| `INDEXING` | `VARCHAR2(7)` |  | Indicates whether a global index is decoupled from the underlying table.  Possible values:  - `PARTIAL` - The index is partial, that is, it will follow the table's indexing property. - `FULL` - The index will include all partitions of the table. |
| `AUTO` | `VARCHAR2(3)` |  | Indicates whether the index is an auto index (`YES`) or not (`NO`) |
| `CONSTRAINT_INDEX` | `VARCHAR2(3)` |  | Indicates whether the index was created as part of a constraint (`YES`) or not (`NO`) |

See Also:

- " [DBA\_INDEXES](DBA_INDEXES.md) "
- " [USER\_INDEXES](USER_INDEXES.md) "
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS059) for more information about the `DBMS_STATS` package