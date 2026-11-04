---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_TABLESPACES.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.50 DBA\_TABLESPACES

`DBA_TABLESPACES` describes all tablespaces in the database.

Related View

`USER_TABLESPACES` describes the tablespaces accessible to the current user. This view does not display the `PLUGGED_IN` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLESPACE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the tablespace |
| `BLOCK_SIZE` | `NUMBER` | `NOT NULL` | Tablespace block size (in bytes) |
| `INITIAL_EXTENT` | `NUMBER` |  | Default initial extent size (in bytes) |
| `NEXT_EXTENT` | `NUMBER` |  | Default incremental extent size (in bytes) |
| `MIN_EXTENTS` | `NUMBER` | `NOT NULL` | Default minimum number of extents |
| `MAX_EXTENTS` | `NUMBER` |  | Default maximum number of extents |
| `MAX_SIZE` | `NUMBER` |  | Default maximum size of segments (in Oracle blocks) |
| `PCT_INCREASE` | `NUMBER` |  | Default percent increase for extent size |
| `MIN_EXTLEN` | `NUMBER` |  | Minimum extent size for this tablespace (in bytes) |
| `STATUS` | `VARCHAR2(9)` |  | Tablespace status:  - `ONLINE` - `OFFLINE` - `READ ONLY` |
| `CONTENTS` | `VARCHAR2(9)` |  | Tablespace contents:  - `UNDO` - `LOST WRITE PROTECTION` - `PERMANENT` - `TEMPORARY` |
| `LOGGING` | `VARCHAR2(9)` |  | Default logging attribute:  - `LOGGING` - `NOLOGGING` |
| `FORCE_LOGGING` | `VARCHAR2(3)` |  | Indicates whether the tablespace is under force logging mode (`YES`) or not (`NO`) |
| `EXTENT_MANAGEMENT` | `VARCHAR2(10)` |  | Indicates whether the extents in the tablespace are dictionary managed (`DICTIONARY`) or locally managed (`LOCAL`) |
| `ALLOCATION_TYPE` | `VARCHAR2(9)` |  | Type of extent allocation in effect for the tablespace:  - `SYSTEM` - `UNIFORM` - `USER` |
| `PLUGGED_IN` | `VARCHAR2(3)` |  | Indicates whether the tablespace is plugged in (`YES`) or not (`NO`) |
| `SEGMENT_SPACE_MANAGEMENT` | `VARCHAR2(6)` |  | Indicates whether the free and used segment space in the tablespace is managed using free lists (`MANUAL`) or bitmaps (`AUTO`) |
| `DEF_TAB_COMPRESSION` | `VARCHAR2(8)` |  | Indicates whether default table compression is enabled (`ENABLED`) or not (`DISABLED`)  Note: Enabling default table compression indicates that all tables in the tablespace will be created with table compression enabled unless otherwise specified. |
| `RETENTION` | `VARCHAR2(11)` |  | Undo tablespace retention:  - `GUARANTEE` - Tablespace is an undo tablespace with `RETENTION` specified as `GUARANTEE` 	A `RETENTION` value of `GUARANTEE` indicates that unexpired undo in all undo segments in the undo tablespace should be retained even if it means that forward going operations that need to generate undo in those segments fail. - `NOGUARANTEE` - Tablespace is an undo tablespace with `RETENTION` specified as `NOGUARANTEE` - `NOT APPLY` - Tablespace is not an undo tablespace |
| `BIGFILE` | `VARCHAR2(3)` |  | Indicates whether the tablespace is a bigfile tablespace (`YES`) or a smallfile tablespace (`NO`) |
| `PREDICATE_EVALUATION` | `VARCHAR2(7)` |  | Indicates whether predicates are evaluated by host (`HOST`) or by storage (`STORAGE`) |
| `ENCRYPTED` | `VARCHAR2(3)` |  | Indicates whether the tablespace is encrypted (`YES`) or not (`NO`) |
| `COMPRESS_FOR` | `VARCHAR2(30)` |  | Default compression for what kind of operations:  - `BASIC` - `ADVANCED` - `QUERY LOW` - `QUERY HIGH` - `ARCHIVE LOW` - `ARCHIVE HIGH` - `NULL`  The `QUERY LOW`, `QUERY HIGH`, `ARCHIVE LOW`, and `ARCHIVE HIGH` values are associated with Hybrid Columnar Compression, a feature of the Enterprise Edition of Oracle Database that is dependent on the underlying storage system. See [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=CNCPT89198) for more information. |
| `DEF_INMEMORY` | `VARCHAR2(8)` |  | Indicates whether the In-Memory Column Store (IM column store) is by default enabled (`ENABLED`) or disabled (`DISABLED`) for tables in this tablespace |
| `DEF_INMEMORY_PRIORITY` | `VARCHAR2(8)` |  | Indicates the default priority for In-Memory Column Store (IM column store) population for this tablespace. Possible values:  - `LOW` - `MEDIUM` - `HIGH` - `CRITICAL` - `NONE` - `NULL` |
| `DEF_INMEMORY_DISTRIBUTE` | `VARCHAR2(15)` |  | Indicates how the IM column store is distributed by default for this tablespace in an Oracle Real Application Clusters (Oracle RAC) environment:  - `AUTO` - `BY ROWID RANGE` - `BY PARTITION` - `BY SUBPARTITION` |
| `DEF_INMEMORY_COMPRESSION` | `VARCHAR2(17)` |  | Indicates the default compression level for the IM column store for this tablespace:  - `NO MEMCOMPRESS` - `FOR DML` - `FOR QUERY [ LOW \| HIGH ]` - `FOR CAPACITY [ LOW \| HIGH ]` - `NULL` |
| `DEF_INMEMORY_DUPLICATE` | `VARCHAR2(13)` |  | Indicates the duplicate setting for the IM column store in an Oracle RAC environment:  - `NO DUPLICATE` - `DUPLICATE` - `DUPLICATE ALL` |
| `SHARED` | `VARCHAR2(12)` |  | Tablespace type:  - `SHARED`: For shared tablespace - `LOCAL_ON_LEAF`: For local temporary tablespace for leaf (read-only) instances - `LOCAL_ON_ALL`: For local temporary tablespace for all instance types |
| `DEF_INDEX_COMPRESSION` | `VARCHAR2(8)` |  | Indicates whether default index compression is enabled (`ENABLED`) or not (`DISABLED`)  Note: Enabling default index compression indicates that all indexes in the tablespace will be created with index compression enabled unless otherwise specified. |
| `INDEX_COMPRESS_FOR` | `VARCHAR2(13)` |  | Valid values are:  - `ADVANCED LOW` - `ADVANCED HIGH` - `NULL`  No other values are allowed. |
| `DEF_CELLMEMORY` | `VARCHAR2(14)` |  | This specifies the default value for the `CELLMEMORY` attribute that tables created in the tablespace will inherit unless the behavior is overridden explicitly  This column is intended for use with Oracle Exadata. |
| `DEF_INMEMORY_SERVICE` | `VARCHAR2(12)` |  | Indicates how the IM column store is populated on various instances by default for this tablespace. The possible values are:  - `DEFAULT`: Data is populated on all instances specified with the `PARALLEL_INSTANCE_GROUP` initialization parameter. If that parameter is not set, then the data is populated on all instances. This is the default. - `NONE`: Data is not populated on any instance. - `ALL`: Data is populated on all instances, regardless of the value of the `PARALLEL_INSTANCE_GROUP` initialization parameter. - `USER_DEFINED`: Data is populated only on the instances on which the user-specified service is active. The service name corresponding to this is stored in the `DEF_INMEMORY_SERVICE_NAME` column. |
| `DEF_INMEMORY_SERVICE_NAME` | `VARCHAR2(1000)` |  | Indicates the service name for the service on which the IM column store should be populated by default for this tablespace. This column has a value only when the corresponding `DEF_INMEMORY_SERVICE` is `USER_DEFINED`. In all other cases, this column is null. |
| `LOST_WRITE_PROTECT` | `VARCHAR2(7)` |  | The lost write protection setting for the tablespace. Possible values:  - `ENABLED`: Indicates that lost write data is being collected - `OFF`: Indicates that lost write data is not being collected - `SUSPEND`: Indicates that lost write data is not currently being collected, but it can be enabled at a later date. The lost write data collected when the file was `ENABLED` remains in the lost write database, but it is not being checked or updated.  If lost write protection is enabled for a tablespace, it is enabled for all data files for that tablespace, including data files added later.  If lost write protection is enabled for a single data file, it does not have to be enabled for another data file in the same tablespace.  You can check the lost write protection status for a data file by querying the `LOST_WRITE_PROTECT` column in the `DBA_DATA_FILES` view. |
| `CHUNK_TABLESPACE` | `VARCHAR2(1)` |  | Indicates whether this is a chunk tablespace (`Y`) or not (`N`) |