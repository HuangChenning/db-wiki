---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_PART_INDEXES.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.3 ALL\_PART\_INDEXES

`ALL_PART_INDEXES` displays the object-level partitioning information for the partitioned indexes accessible to the current user.

Related Views

- `DBA_PART_INDEXES` displays the object-level partitioning information for all partitioned indexes in the database.
- `USER_PART_INDEXES` displays the object-level partitioning information for the partitioned indexes owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the partitioned index |
| `INDEX_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the partitioned index |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the partitioned table |
| `PARTITIONING_TYPE` | `VARCHAR2(9)` |  | Type of the partitioning method:  - `NONE` - Not specified 	See Also: the `*_INDEXES` view - `RANGE` - `HASH` - `SYSTEM` - `LIST` - `REFERENCE` |
| `SUBPARTITIONING_TYPE` | `VARCHAR2(9)` |  | Type of the composite partitioning method:  - `NONE` - Not specified 	See Also: the `*_INDEXES` view - `RANGE` - `HASH` - `SYSTEM` - `LIST` - `REFERENCE` |
| `PARTITION_COUNT` | `NUMBER` | `NOT NULL` | Number of partitions in the index |
| `DEF_SUBPARTITION_COUNT` | `NUMBER` |  | For a composite-partitioned index, the default number of subpartitions, if specified |
| `PARTITIONING_KEY_COUNT` | `NUMBER` | `NOT NULL` | Number of columns in the partitioning key |
| `SUBPARTITIONING_KEY_COUNT` | `NUMBER` |  | For a composite-partitioned index, the number of columns in the subpartitioning key |
| `LOCALITY` | `VARCHAR2(6)` |  | Indicates whether the partitioned index is local (`LOCAL`) or global (`GLOBAL`) |
| `ALIGNMENT` | `VARCHAR2(12)` |  | Indicates whether the partitioned index is prefixed (`PREFIXED`) or non-prefixed (`NON_PREFIXED`) |
| `DEF_TABLESPACE_NAME` | `VARCHAR2(30)` |  | For a local index, the default tablespace to be used when adding or splitting a table partition |
| `DEF_PCT_FREE` | `NUMBER` | `NOT NULL` | For a local index, the default `PCTFREE` value to be used when adding a table partition |
| `DEF_INI_TRANS` | `NUMBER` | `NOT NULL` | For a local index, the default `INITRANS` value to be used when adding a table partition |
| `DEF_MAX_TRANS` | `NUMBER` | `NOT NULL` | For a local index, the default `MAXTRANS` value to be used when adding a table partition |
| `DEF_INITIAL_EXTENT` | `VARCHAR2(40)` |  | For a local index, the default `INITIAL` value (in Oracle blocks) to be used when adding a table partition, or `DEFAULT` if no `INITIAL` value was specified |
| `DEF_NEXT_EXTENT` | `VARCHAR2(40)` |  | For a local index, the default `NEXT` value (in Oracle blocks) to be used when adding a table partition, or `DEFAULT` if no `NEXT` value was specified |
| `DEF_MIN_EXTENTS` | `VARCHAR2(40)` |  | For a local index, the default `MINEXTENTS` value to be used when adding a table partition, or `DEFAULT` if no `MINEXTENTS` value was specified |
| `DEF_MAX_EXTENTS` | `VARCHAR2(40)` |  | For a local index, the default `MAXEXTENTS` value to be used when adding a table partition, or `DEFAULT` if no `MAXEXTENTS` value was specified |
| `DEF_MAX_SIZE` | `VARCHAR2(40)` |  | For a local index, the default `MAXSIZE` value to be used when adding a table partition, or `DEFAULT` if no `MAXSIZE` value was specified |
| `DEF_PCT_INCREASE` | `VARCHAR2(40)` |  | For a local index, the default `PCTINCREASE` value to be used when adding a table partition, or `DEFAULT` if no `PCTINCREASE` value was specified |
| `DEF_FREELISTS` | `NUMBER` | `NOT NULL` | For a local index, the default `FREELISTS` value to be used when adding a table partition |
| `DEF_FREELIST_GROUPS` | `NUMBER` | `NOT NULL` | For a local index, the default `FREELIST GROUPS` value to be used when adding a table partition |
| `DEF_LOGGING` | `VARCHAR2(7)` |  | For a local index, the default `LOGGING` attribute to be used when adding a table partition:  - `NONE` - Not specified 	See Also: the `*_INDEXES` view - `YES` - `NO` |
| `DEF_BUFFER_POOL` | `VARCHAR2(7)` |  | For a local index, the default buffer pool to be used when adding a table partition:  - `DEFAULT` - `KEEP` - `RECYCLE` - NULL |
| `DEF_FLASH_CACHE` | `VARCHAR2(7)` |  | For a local index, the default Database Smart Flash Cache hint to be used when adding a table partition:  - `DEFAULT` - `KEEP` - `NONE`  Solaris and Oracle Linux functionality only. |
| `DEF_CELL_FLASH_CACHE` | `VARCHAR2(7)` |  | For a local index, the default cell flash cache hint to be used when adding a table partition:  - `DEFAULT` - `KEEP` - `NONE`  See Also: Oracle Exadata Storage Server Software documentation for more information |
| `DEF_PARAMETERS` | `VARCHAR2(1000)` |  | Default parameter string for domain indexes |
| `INTERVAL` | `VARCHAR2(1000)` |  | String of the interval value |
| `AUTOLIST` | `VARCHAR2(3)` |  | Indicates whether a local index is partitioned by auto list partitioning (`YES`) or not (`NO`) |
| `INTERVAL_SUBPARTITION` | `VARCHAR2(1000)` |  | String of the subpartition interval value |
| `AUTOLIST_SUBPARTITION` | `VARCHAR2(3)` |  | Indicates whether a local index is subpartitioned by auto list partitioning (`YES`) or not (`NO`) |

See Also:

- " [DBA\_PART\_INDEXES](DBA_PART_INDEXES.md) "
- " [USER\_PART\_INDEXES](USER_PART_INDEXES.md) "