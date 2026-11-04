---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_LOBS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.263 ALL\_LOBS

`ALL_LOBS` displays the large objects (LOBs) contained in tables accessible to the current user. LOBs include binary large objects (BLOBs) and character large objects (CLOBs). Binary files (BFILEs) are stored outside the database, so they are not displayed by this view or the related views.

Related Views

- `DBA_LOBS` describes all LOBs in the database.
- `USER_LOBS` describes the LOBs owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the object containing the LOB |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Name of the object containing the LOB |
| `COLUMN_NAME` | `VARCHAR2(4000)` |  | Name of the LOB column or attribute |
| `SEGMENT_NAME` | `VARCHAR2(128)` |  | Name of the LOB segment |
| `TABLESPACE_NAME` | `VARCHAR2(30)` |  | Name of the tablespace containing the LOB segment |
| `INDEX_NAME` | `VARCHAR2(128)` |  | Name of the LOB index |
| `CHUNK` | `NUMBER` |  | Size (in bytes) of the LOB chunk as a unit of allocation or manipulation |
| `PCTVERSION` | `NUMBER` |  | Maximum percentage of the LOB space used for versioning |
| `RETENTION` | `NUMBER` |  | Maximum time duration for versioning of the LOB space |
| `FREEPOOLS` | `NUMBER` |  | Number of freepools for this LOB segment |
| `CACHE` | `VARCHAR2(10)` |  | Indicates whether and how the LOB data is to be cached in the buffer cache:  - `YES` - LOB data is placed in the buffer cache - `NO` - LOB data either is not brought into the buffer cache or is brought into the buffer cache and placed at the least recently used end of the LRU list - `CACHEREADS` - LOB data is brought into the buffer cache only during read operations but not during write operations |
| `LOGGING` | `VARCHAR2(7)` |  | Indicates whether or not changes to the LOB are logged:  - `NONE` - Not specified 	See Also: the `*_LOB_SUBPARTITIONS` view - `YES` - `NO` |
| `ENCRYPT` | `VARCHAR2(4)` |  | Indicates whether or not the LOB is encrypted.  Possible values for SecureFiles:  - `YES` - `NO`  Possible value for BasicFiles:  - `NONE` - Not applicable |
| `COMPRESSION` | `VARCHAR2(6)` |  | Level of compression used for this LOB.  Possible values for SecureFiles:  - `LOW` - `MEDIUM` - `HIGH` - `NO` - Compression is off  Possible value for BasicFiles:  - `NONE` - Not applicable |
| `DEDUPLICATION` | `VARCHAR2(15)` |  | Kind of deduplication used for this LOB.  Possible values for SecureFiles:  - `LOB` - Deduplicate - `NO` - Keep duplicates  Possible value for BasicFiles:  - `NONE` - Not applicable |
| `IN_ROW` | `VARCHAR2(3)` |  | Indicates whether some LOBs are stored inline with the base row (`YES`) or not (`NO`). For partitioned objects, refer to the `*_LOB_PARTITIONS` and `*_PART_LOBS` views. |
| `FORMAT` | `VARCHAR2(15)` |  | Indicates whether the LOB storage format depends on the endianness of the platform:  - `NOT APPLICABLE ` - `ENDIAN SPECIFIC` - `ENDIAN NEUTRAL ` |
| `PARTITIONED` | `VARCHAR2(3)` |  | Indicates whether the LOB column is in a partitioned table (`YES`) or not (`NO`) |
| `SECUREFILE` | `VARCHAR2(3)` |  | Indicates whether the LOB is SecureFiles (`YES`) or not (`NO`) |
| `SEGMENT_CREATED` | `VARCHAR2(3)` |  | Indicates whether the LOB segment has been created (`YES`) or not (`NO`) |
| `RETENTION_TYPE` | `VARCHAR2(7)` |  | Type of retention used for this LOB.  Possible values for SecureFiles:  - `NONE` - `AUTO` - `MIN` - `MAX` - `DEFAULT` - `INVALID`  Possible values for BasicFiles:  - `YES` - `NO` |
| `RETENTION_VALUE` | `NUMBER` |  | Minimum retention time (in seconds). This column is only meaningful for SecureFiles with `RETENTION_TYPE` set to `MIN`. |
| `VALUE_BASED` | `VARCHAR2(3)` |  | Indicates whether the LOB is value based (`YES`) or not (`NO`) |
| `MAX_INLINE` | `NUMBER` |  | Size of inline LOB storage (in bytes)  - For inline LOBs in nonpartitioned tables (`IN_ROW` `=` `YES` and `PARTITIONED` `=` `NO`), this column displays the size of inline LOB storage (in bytes). - For out-of-inline LOBs in nonpartitioned tables (`IN_ROW` `=` `NO` and `PARTITIONED` `=` `NO`), the value of this column is `0`. - For LOBs in partitioned tables (`PARTITIONED` `=` `YES`), the value of this column is null. Instead, refer to the `MAX_INLINE` column in the `*_PART_LOBS`, `*_LOB_PARTITIONS`, and `*_LOB_SUBPARTITIONS` views. |

See Also:

- " [DBA\_LOBS](DBA_LOBS.md) "
- " [USER\_LOBS](USER_LOBS.md) "