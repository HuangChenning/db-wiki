---
title: ALL_PART_TABLES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2006.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_PART_TABLES` displays the object-level partitioning information for the partitioned tables accessible to the current user.

Related Views

- `DBA_PART_TABLES` displays the object-level partitioning information for all partitioned tables in the database.
- `USER_PART_TABLES` displays the object-level partitioning information for the partitioned tables owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the partitioned table |
| `TABLE_NAME` | `VARCHAR2(30)` |  | Name of the partitioned table |
| `PARTITIONING_TYPE` | `VARCHAR2(9)` |  | Type of the partitioning method: - `UNKNOWN` - Not specified 	See Also: the `*_TABLES` view - `RANGE` - `HASH` - `SYSTEM` - `LIST` - `REFERENCE` |
| `SUBPARTITIONING_TYPE` | `VARCHAR2(9)` |  | Type of the composite partitioning method: - `NONE` - Not subpartitioned 	See Also: the `*_TABLES` view - `RANGE` - `HASH` - `SYSTEM` - `LIST` - `REFERENCE` |
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
| `DEF_LOGGING` | `VARCHAR2(7)` |  | Default `LOGGING` attribute to be used when adding a partition: - `NONE` - Not specified 	See Also: the `*_TABLES` view - `YES` - `NO` |
| `DEF_COMPRESSION` | `VARCHAR2(8)` |  | Default compression to be used when adding a partition: - `NONE` - Not specified 	See Also: the `*_TABLES` view - `ENABLED` - `DISABLED` |
| `DEF_COMPRESS_FOR` | `VARCHAR2(12)` |  | Default compression for what kind of operations to be used when adding a partition: - `BASIC` - `OLTP` - `QUERY LOW` <sup>Foot 1</sup> - `QUERY HIGH` <sup>Footref 1</sup> - `ARCHIVE LOW` <sup>Footref 1</sup> - `ARCHIVE HIGH` <sup>Footref 1</sup> - `UNKNOWN` - NULL |
| `DEF_BUFFER_POOL` | `VARCHAR2(7)` |  | Default buffer pool to be used when adding a partition: - `DEFAULT` - `KEEP` - `RECYCLE` - NULL |
| `DEF_FLASH_CACHE` | `VARCHAR2(7)` |  | Default Database Smart Flash Cache hint to be used when adding a partition: - `DEFAULT` - `KEEP` - `NONE`  Solaris and Oracle Linux functionality only. |
| `DEF_CELL_FLASH_CACHE` | `VARCHAR2(7)` |  | Default cell flash cache hint to be used when adding a partition: - `DEFAULT` - `KEEP` - `NONE`  See Also: Oracle Exadata Storage Server Software documentation for more information |
| `REF_PTN_CONSTRAINT_NAME` | `VARCHAR2(30)` |  | Name of the partitioning referential constraint for reference-partitioned tables |
| `INTERVAL` | `VARCHAR2(1000)` |  | String of the interval value |
| `IS_NESTED` | `VARCHAR2(3)` |  | Indicates whether the partitioned table is a nested table (`YES`) or not (`NO`)  See Also: the `*_NESTED_TABLES` view for the parent table name/column |
| `DEF_SEGMENT_CREATION` <sup>Foot 2</sup> | `VARCHAR2(4)` |  | Indicates whether a table partition segment has been created (`YES`) or not (`NO`). `N/A` indicates that this table is subpartitioned and no segment exists at the partition level |

<sup>Footnote 1</sup> Hybrid Columnar Compression is a feature of the Enterprise Edition of Oracle Database that is dependent on the underlying storage system. See [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/tablecls.htm#CNCPT89198) for more information.

<sup>Footnote 2</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.2).

See Also:

- ["DBA\_PART\_TABLES"](statviews_4177.md)
- ["USER\_PART\_TABLES"](statviews_5392.md)