---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_PART_TABLES.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.6 ALL\_PART\_TABLES

`ALL_PART_TABLES` displays the object-level partitioning information for the partitioned tables accessible to the current user.

Related Views

- `DBA_PART_TABLES` displays the object-level partitioning information for all partitioned tables in the database.
- `USER_PART_TABLES` displays the object-level partitioning information for the partitioned tables owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the partitioned table |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Name of the partitioned table |
| `PARTITIONING_TYPE` | `VARCHAR2(9)` |  | Type of the partitioning method:  - `UNKNOWN` - Not specified 	See Also: the `*_TABLES` view - `RANGE` - `HASH` - `SYSTEM` - `LIST` - `REFERENCE` |
| `SUBPARTITIONING_TYPE` | `VARCHAR2(9)` |  | Type of the composite partitioning method:  - `NONE` - Not subpartitioned 	See Also: the `*_TABLES` view - `RANGE` - `HASH` - `SYSTEM` - `LIST` - `REFERENCE` |
| `PARTITION_COUNT` | `NUMBER` |  | Number of partitions in the table. For interval partitioned tables, the value of this column is always `1048575`. |
| `DEF_SUBPARTITION_COUNT` | `NUMBER` |  | For a composite-partitioned table, the default number of subpartitions, if specified |
| `PARTITIONING_KEY_COUNT` | `NUMBER` |  | Number of columns in the partitioning key |
| `SUBPARTITIONING_KEY_COUNT` | `NUMBER` |  | For a composite-partitioned table, the number of columns in the subpartitioning key |
| `STATUS` | `VARCHAR2(8)` |  | If a previous `DROP TABLE` operation failed, indicates whether the table is unusable (`UNUSABLE`) or valid (`VALID`) |
| `DEF_TABLESPACE_NAME` | `VARCHAR2(30)` |  | Default tablespace to be used when adding a partition |
| `DEF_PCT_FREE` | `NUMBER` |  | Default value of `PCTFREE` to be used when adding a partition |
| `DEF_PCT_USED` | `NUMBER` |  | Default value of `PCTUSED` to be used when adding a partition |
| `DEF_INI_TRANS` | `NUMBER` |  | Default value of `INITRANS` to be used when adding a partition |
| `DEF_MAX_TRANS` | `NUMBER` |  | Default value of `MAXTRANS` to be used when adding a partition |
| `DEF_INITIAL_EXTENT` | `VARCHAR2(40)` |  | Default value of `INITIAL` (in Oracle blocks) to be used when adding a partition, or `DEFAULT` if no `INITIAL` value was specified |
| `DEF_NEXT_EXTENT` | `VARCHAR2(40)` |  | Default value of `NEXT` (in Oracle blocks) to be used when adding a partition, or `DEFAULT` if no `NEXT` value was specified |
| `DEF_MIN_EXTENTS` | `VARCHAR2(40)` |  | Default value of `MINEXTENTS` to be used when adding a partition, or `DEFAULT` if no `MINEXTENTS` value was specified |
| `DEF_MAX_EXTENTS` | `VARCHAR2(40)` |  | Default value of `MAXEXTENTS` to be used when adding a partition, or `DEFAULT` if no `MAXEXTENTS` value was specified |
| `DEF_MAX_SIZE` | `VARCHAR2(40)` |  | Default value of `MAXSIZE` to be used when adding a partition, or `DEFAULT` if no `MAXSIZE` value was specified |
| `DEF_PCT_INCREASE` | `VARCHAR2(40)` |  | Default value of `PCTINCREASE` to be used when adding a partition, or `DEFAULT` if no `PCTINCREASE` value was specified |
| `DEF_FREELISTS` | `NUMBER` |  | Default value of `FREELISTS` to be used when adding a partition |
| `DEF_FREELIST_GROUPS` | `NUMBER` |  | Default value of `FREELIST GROUPS` to be used when adding a partition |
| `DEF_LOGGING` | `VARCHAR2(7)` |  | Default `LOGGING` attribute to be used when adding a partition:  - `NONE` - Not specified 	See Also: the `*_TABLES` view - `YES` - `NO` |
| `DEF_COMPRESSION` | `VARCHAR2(8)` |  | Default compression to be used when adding a partition:  - `NONE` - Not specified 	See Also: the `*_TABLES` view - `ENABLED` - `DISABLED` |
| `DEF_COMPRESS_FOR` | `VARCHAR2(30)` |  | Default compression for what kind of operations to be used when adding a partition:  - `BASIC` - `ADVANCED` - `QUERY LOW` <sup>Foot 1</sup> - `QUERY HIGH` <sup>Foot 1</sup> - `ARCHIVE LOW` <sup>Foot 1</sup> - `ARCHIVE HIGH` <sup>Foot 1</sup> - `UNKNOWN` - `NULL` |
| `DEF_BUFFER_POOL` | `VARCHAR2(7)` |  | Default buffer pool to be used when adding a partition:  - `DEFAULT` - `KEEP` - `RECYCLE` - `NULL` |
| `DEF_FLASH_CACHE` | `VARCHAR2(7)` |  | Default Database Smart Flash Cache hint to be used when adding a partition:  - `DEFAULT` - `KEEP` - `NONE`  Solaris and Oracle Linux functionality only. |
| `DEF_CELL_FLASH_CACHE` | `VARCHAR2(7)` |  | Default cell flash cache hint to be used when adding a partition:  - `DEFAULT` - `KEEP` - `NONE`  See Also: Oracle Exadata Storage Server Software documentation for more information |
| `REF_PTN_CONSTRAINT_NAME` | `VARCHAR2(128)` |  | Name of the partitioning referential constraint for reference-partitioned tables |
| `INTERVAL` | `VARCHAR2(1000)` |  | String of the interval value |
| `AUTOLIST` | `VARCHAR2(3)` |  | Indicates whether a table is partitioned by auto list partitioning (`YES`) or not (`NO`) |
| `INTERVAL_SUBPARTITION` | `VARCHAR2(1000) ` |  | String of the subpartition interval value |
| `AUTOLIST_SUBPARTITION` | `VARCHAR2(3)` |  | Indicates whether auto list partitioning is being used (`YES`) or not (`NO`) for this subpartition |
| `IS_NESTED` | `VARCHAR2(3)` |  | Indicates whether the partitioned table is a nested table (`YES`) or not (`NO`)  See Also: the `*_NESTED_TABLES` view for the parent table name/column |
| `DEF_SEGMENT_CREATION` | `VARCHAR2(4)` |  | Specifies whether the default for segment creation was specified on the table level:  - `NO` - deferred was specified - `YES` - immediate was specified - `NONE` - a default for segment creation was not specified |
| `DEF_INDEXING` | `VARCHAR2(3)` |  | Indicates the indexing property specified for the table.  Possible values:  - `ON` - `INDEXING` on was specified explicitly, or no indexing property was specified - `OFF` - `INDEXING` off was specified. |
| `DEF_INMEMORY` | `VARCHAR2(8)` |  | Indicates whether the In-Memory Column Store (IM column store) is by default enabled (`ENABLED`), disabled (`DISABLED`), or not specified (`NONE`) for partitions in this table |
| `DEF_INMEMORY_PRIORITY` | `VARCHAR2(8)` |  | Indicates the default priority for In-Memory Column Store (IM column store) population. Possible values:  - `LOW` - `MEDIUM` - `HIGH` - `CRITICAL` - `NONE` - `NULL` |
| `DEF_INMEMORY_DISTRIBUTE` | `VARCHAR2(15)` |  | Indicates how the IM column store is distributed by default for partitions of the table in an Oracle Real Application Clusters (Oracle RAC) environment:  - `AUTO` - `BY ROWID RANGE` - `BY PARTITION` - `BY SUBPARTITION` |
| `DEF_INMEMORY_COMPRESSION` | `VARCHAR2(17)` |  | Default compression level for the IM column store:  - `NO MEMCOMPRESS` - `FOR DML` - `FOR QUERY [ LOW \| HIGH ]` - `FOR CAPACITY [ LOW \| HIGH ]` - `AUTO` - `NULL` |
| `DEF_INMEMORY_DUPLICATE` | `VARCHAR2(13)` |  | Indicates the default duplicate setting for the IM column store in an Oracle RAC environment:  - `NO DUPLICATE` - `DUPLICATE` - `DUPLICATE ALL` |
| `DEF_READ_ONLY` | `VARCHAR2(3)` |  | Indicates the default setting for new partitions:  - `YES`: The default setting for new partitions is read-only. - `NO`: The default setting for new partitions is read/write. |
| `DEF_CELLMEMORY` <sup>Foot 2</sup> | `VARCHAR2(24)` |  | Shows the default value for the `CELLMEMORY` attribute that new partitions in the parent table will inherit unless the behavior is overridden explicitly |
| `DEF_INMEMORY_SERVICE` | `VARCHAR2(12)` |  | Indicates how the IM column store is populated on various instances by default for partitions of the table. The possible values are:  - `DEFAULT`: Data is populated on all instances specified with the `PARALLEL_INSTANCE_GROUP` initialization parameter. If that parameter is not set, then the data is populated on all instances. This is the default. - `NONE`: Data is not populated on any instance. - `ALL`: Data is populated on all instances, regardless of the value of the `PARALLEL_INSTANCE_GROUP` initialization parameter. - `USER_DEFINED`: Data is populated only on the instances on which the user-specified service is active. The service name corresponding to this is stored in the `DEF_INMEMORY_SERVICE_NAME` column. |
| `DEF_INMEMORY_SERVICE_NAME` | `VARCHAR2(1000)` |  | Specifies the service name for the service on which the IM column store should be populated by default for partitions of the table. This column has a value only when the corresponding `DEF_INMEMORY_SERVICE` is `USER_DEFINED`. In all other cases, this column is null. |
| `AUTO` | `VARCHAR2(3)` |  | Indicates whether the table was automatically partitioned (`YES`) or not (`NO`) |

<sup>Footnote 1</sup>

Hybrid Columnar Compression is a feature of the Enterprise Edition of Oracle Database that is dependent on the underlying storage system. See [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=CNCPT89198) for more information.

<sup>Footnote 2</sup>

This column is intended for use with Oracle Exadata