---
title: ALL_LOBS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1133.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_LOBS` displays the large objects (LOBs) contained in tables accessible to the current user. LOBs include binary large objects (BLOBs) and character large objects (CLOBs). Binary files (BFILEs) are stored outside the database, so they are not displayed by this view or the related views.

Related Views

- `DBA_LOBS` describes all LOBs in the database.
- `USER_LOBS` describes the LOBs owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the object containing the LOB |
| `TABLE_NAME` | `VARCHAR2(30)` |  | Name of the object containing the LOB |
| `COLUMN_NAME` | `VARCHAR2(4000)` |  | Name of the LOB column or attribute |
| `SEGMENT_NAME` | `VARCHAR2(30)` |  | Name of the LOB segment |
| `TABLESPACE_NAME` | `VARCHAR2(30)` |  | Name of the tablespace containing the LOB segment |
| `INDEX_NAME` | `VARCHAR2(30)` |  | Name of the LOB index |
| `CHUNK` | `NUMBER` |  | Size (in bytes) of the LOB chunk as a unit of allocation or manipulation |
| `PCTVERSION` | `NUMBER` |  | Maximum percentage of the LOB space used for versioning |
| `RETENTION` | `NUMBER` |  | Maximum time duration for versioning of the LOB space |
| `FREEPOOLS` | `NUMBER` |  | Number of freepools for this LOB segment |
| `CACHE` | `VARCHAR2(10)` |  | Indicates whether and how the LOB data is to be cached in the buffer cache: - `YES` - LOB data is placed in the buffer cache - `NO` - LOB data either is not brought into the buffer cache or is brought into the buffer cache and placed at the least recently used end of the LRU list - `CACHEREADS` - LOB data is brought into the buffer cache only during read operations but not during write operations |
| `LOGGING` | `VARCHAR2(7)` |  | Indicates whether or not changes to the LOB are logged: - `NONE` - Not specified 	See Also: the `*_LOB_SUBPARTITIONS` view - `YES` - `NO` |
| `ENCRYPT` | `VARCHAR2(4)` |  | Indicates whether or not the LOB is encrypted.  Possible values for SecureFiles:  - `YES` - `NO`  Possible value for BasicFiles:  - `NONE` - Not applicable |
| `COMPRESSION` | `VARCHAR2(6)` |  | Level of compression used for this LOB.  Possible values for SecureFiles:  - `LOW` - `MEDIUM` - `HIGH` - `NO` - Compression is off  Possible value for BasicFiles:  - `NONE` - Not applicable |
| `DEDUPLICATION` | `VARCHAR2(15)` |  | Kind of deduplication used for this LOB.  Possible values for SecureFiles:  - `LOB` - Deduplicate - `NO` - Keep duplicates  Possible value for BasicFiles:  - `NONE` - Not applicable |
| `IN_ROW` | `VARCHAR2(3)` |  | Indicates whether some of the LOBs are stored inline with the base row (`YES`) or not (`NO`). For partitioned objects, refer to the `*_LOB_PARTITIONS` and `*_PART_LOBS` views. |
| `FORMAT` | `VARCHAR2(15)` |  | Indicates whether the LOB storage format is dependent on the endianness of the platform: - `NOT APPLICABLE` - `ENDIAN SPECIFIC` - `ENDIAN NEUTRAL` |
| `PARTITIONED` | `VARCHAR2(3)` |  | Indicates whether the LOB column is in a partitioned table (`YES`) or not (`NO`) |
| `SECUREFILE` | `VARCHAR2(3)` |  | Indicates whether the LOB is SecureFiles (`YES`) or not (`NO`) |
| `SEGMENT_CREATED` | `VARCHAR2(3)` |  | Indicates whether the LOB segment has been created (`YES`) or not (`NO`) |
| `RETENTION_TYPE` <sup>Foot 1</sup> | `VARCHAR2(7)` |  | Type of retention used for this LOB.  Possible values for SecureFiles:  - `NONE` - `AUTO` - `MIN` - `MAX` - `DEFAULT` - `INVALID`  Possible values for BasicFiles:  - `YES` - `NO` |
| `RETENTION_VALUE` <sup>Footref 1</sup> | `NUMBER` |  | Minimum retention time (in seconds). This column is only meaningful for SecureFiles with `RETENTION_TYPE` set to `MIN`. |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.2).