---
title: DBA_TABLESPACES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5060.htm
tags:
  - oracle
  - 11g
  - reference
---

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
| `STATUS` | `VARCHAR2(9)` |  | Tablespace status: - `ONLINE` - `OFFLINE` - `READ ONLY` |
| `CONTENTS` | `VARCHAR2(9)` |  | Tablespace contents: - `UNDO` - `PERMANENT` - `TEMPORARY` |
| `LOGGING` | `VARCHAR2(9)` |  | Default logging attribute: - `LOGGING` - `NOLOGGING` |
| `FORCE_LOGGING` | `VARCHAR2(3)` |  | Indicates whether the tablespace is under force logging mode (`YES`) or not (`NO`) |
| `EXTENT_MANAGEMENT` | `VARCHAR2(10)` |  | Indicates whether the extents in the tablespace are dictionary managed (`DICTIONARY`) or locally managed (`LOCAL`) |
| `ALLOCATION_TYPE` | `VARCHAR2(9)` |  | Type of extent allocation in effect for the tablespace: - `SYSTEM` - `UNIFORM` - `USER` |
| `PLUGGED_IN` | `VARCHAR2(3)` |  | Indicates whether the tablespace is plugged in (`YES`) or not (`NO`) |
| `SEGMENT_SPACE_MANAGEMENT` | `VARCHAR2(6)` |  | Indicates whether the free and used segment space in the tablespace is managed using free lists (`MANUAL`) or bitmaps (`AUTO`) |
| `DEF_TAB_COMPRESSION` | `VARCHAR2(8)` |  | Indicates whether default table compression is enabled (`ENABLED`) or not (`DISABLED`)  Note: Enabling default table compression indicates that all tables in the tablespace will be created with table compression enabled unless otherwise specified. |
| `RETENTION` | `VARCHAR2(11)` |  | Undo tablespace retention: - `GUARANTEE` - Tablespace is an undo tablespace with `RETENTION` specified as `GUARANTEE` 	A `RETENTION` value of `GUARANTEE` indicates that unexpired undo in all undo segments in the undo tablespace should be retained even if it means that forward going operations that need to generate undo in those segments fail. - `NOGUARANTEE` - Tablespace is an undo tablespace with `RETENTION` specified as `NOGUARANTEE` - `NOT APPLY` - Tablespace is not an undo tablespace |
| `BIGFILE` | `VARCHAR2(3)` |  | Indicates whether the tablespace is a bigfile tablespace (`YES`) or a smallfile tablespace (`NO`) |
| `PREDICATE_EVALUATION` | `VARCHAR2(7)` |  | Indicates whether predicates are evaluated by host (`HOST`) or by storage (`STORAGE`) |
| `ENCRYPTED` | `VARCHAR2(3)` |  | Indicates whether the tablespace is encrypted (`YES`) or not (`NO`) |
| `COMPRESS_FOR` | `VARCHAR2(12)` |  | Default compression for what kind of operations: |

<sup>Footnote 1</sup> Hybrid Columnar Compression is a feature of the Enterprise Edition of Oracle Database that is dependent on the underlying storage system. See [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/tablecls.htm#CNCPT89198) for more information.

See Also:

["USER\_TABLESPACES"](statviews_5491.md)