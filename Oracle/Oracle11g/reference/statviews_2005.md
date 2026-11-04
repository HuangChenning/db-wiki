---
title: ALL_PART_LOBS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2005.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_PART_LOBS` displays table-level information about the partitioned LOBs accessible to the current user, including default attributes for LOB data partitions.

Related Views

- `DBA_PART_LOBS` displays table-level information about all partitioned LOBs in the database.
- `USER_PART_LOBS` displays table-level information about the partitioned LOBs owned by the current user. This view does not display the `TABLE_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLE_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the partitioned table containing the LOBs |
| `TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the partitioned table containing the LOBs |
| `COLUMN_NAME` | `VARCHAR2(4000)` |  | Name of the LOB column |
| `LOB_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the partitioned LOB |
| `LOB_INDEX_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the partitioned LOB index |
| `DEF_CHUNK` | `NUMBER` | `NOT NULL` | Default value of `CHUNK` for a LOB data partition to be used when adding a partition |
| `DEF_PCTVERSION` | `NUMBER` | `NOT NULL` | Default value of `PCTVERSION` for a LOB data partition to be used when adding a partition |
| `DEF_CACHE` | `VARCHAR2(10)` |  | Indicates whether and how the LOB data is cached by default in the buffer cache: - `YES` - LOB data is placed in the buffer cache - `NO` - LOB data either is not brought into the buffer cache or is brought into the buffer cache and placed at the least recently used end of the LRU list - `CACHEREADS` - LOB data is brought into the buffer cache only during read operations but not during write operations |
| `DEF_IN_ROW` | `VARCHAR2(3)` |  | Indicates whether LOB data < 4000 bytes is stored by default inline (in the row) (`YES`) or not (`NO`); that is, whether or not `ENABLE STORAGE IN ROW` was specified when the LOB column was created or last altered |
| `DEF_TABLESPACE_NAME` | `VARCHAR2(30)` |  | Default tablespace for a LOB data partition to be used when adding a partition |
| `DEF_INITIAL_EXTENT` | `VARCHAR2(40)` |  | Default value of `INITIAL` for a LOB data partition to be used when adding a partition, or `DEFAULT` if no `INITIAL` value was specified |
| `DEF_NEXT_EXTENT` | `VARCHAR2(40)` |  | Default value of `NEXT` for a LOB data partition to be used when adding a partition, or `DEFAULT` if no `NEXT` value was specified |
| `DEF_MIN_EXTENTS` | `VARCHAR2(40)` |  | Default value of `MINEXTENTS` for a LOB data partition to be used when adding a partition, or `DEFAULT` if no `MINEXTENTS` value was specified |
| `DEF_MAX_EXTENTS` | `VARCHAR2(40)` |  | Default value of `MAXEXTENTS` for a LOB data partition to be used when adding a partition, or `DEFAULT` if no `MAXEXTENTS` value was specified |
| `DEF_MAX_SIZE` | `VARCHAR2(40)` |  | Default value of `MAXSIZE` for a LOB data partition to be used when adding a partition, or `DEFAULT` if no `MAXSIZE` value was specified |
| `DEF_RETENTION` | `VARCHAR2(7)` |  | Default value of `RETENTION` for a LOB data partition to be used when adding a partition.  Possible values for SecureFiles:  - `NONE` - `AUTO` - `MIN` - `MAX` - `DEFAULT` - `INVALID`  Possible values for BasicFiles:<sup>Foot 1</sup>  - `YES` - `NO` |
| `DEF_MINRET` | `VARCHAR2(40)` |  | Default value of `RETENTION MIN` for a LOB data partition to be used when adding a partition, or `DEFAULT` if no `RETENTION MIN` value was specified |
| `DEF_PCT_INCREASE` | `VARCHAR2(40)` |  | Default value of `PCTINCREASE` for a LOB data partition to be used when adding a partition, or `DEFAULT` if no `PCTINCREASE` value was specified |
| `DEF_FREELISTS` | `VARCHAR2(40)` |  | Default value of `FREELISTS` for a LOB data partition to be used when adding a partition, or `DEFAULT` if no `FREELISTS` value was specified |
| `DEF_FREELIST_GROUPS` | `VARCHAR2(40)` |  | Default value of `FREELIST GROUPS` for a LOB data partition to be used when adding a partition, or `DEFAULT` if no `FREELIST GROUPS` value was specified |
| `DEF_LOGGING` | `VARCHAR2(7)` |  | Default `LOGGING` attribute for a LOB data partition to be used when adding a partition: - `NONE` - Not specified 	See Also: the `*_LOBS` and `*_LOB_PARTITIONS` views - `YES` - `NO` |
| `DEF_BUFFER_POOL` | `VARCHAR2(7)` |  | Default buffer pool for a LOB data partition to be used when adding a partition: - `DEFAULT` - `KEEP` - `RECYCLE` - NULL |
| `DEF_FLASH_CACHE` | `VARCHAR2(7)` |  | Default Database Smart Flash Cache hint to be used when adding a partition: - `DEFAULT` - `KEEP` - `NONE`  Solaris and Oracle Linux functionality only. |
| `DEF_CELL_FLASH_CACHE` | `VARCHAR2(7)` |  | Default cell flash cache hint to be used when adding a partition: - `DEFAULT` - `KEEP` - `NONE`  See Also: Oracle Exadata Storage Server Software documentation for more information |
| `DEF_ENCRYPT` | `VARCHAR2(4)` |  | Default value of `ENCRYPT` for a LOB data partition to be used when adding a partition.  Possible values for SecureFiles:  - `YES` - `NO`  Possible value for BasicFiles:  - `NONE` - Not applicable |
| `DEF_COMPRESS` | `VARCHAR2(6)` |  | Default value of `COMPRESS` for a LOB data partition to be used when adding a partition.  Possible values for SecureFiles:  - `LOW` - `MEDIUM` - `HIGH` - `NO` - Compression is off  Possible value for BasicFiles:  - `NONE` - Not applicable |
| `DEF_DEDUPLICATE` | `VARCHAR2(15)` |  | Default value of `DEDUPLICATE` for a LOB data partition to be used when adding a partition.  Possible values for SecureFiles:  - `LOB` - Deduplicate - `NO` - Keep duplicates  Possible values for BasicFiles:  - `NONE` - Not applicable |
| `DEF_SECUREFILE` | `VARCHAR2(3)` |  | Indicates whether the LOB is SecureFiles (`YES`) or not (`NO`) |

<sup>Footnote 1</sup> The values listed for BasicFiles are supported starting with Oracle Database 11g Release 2 (11.2.0.2). In previous releases, the value for this column for BasicFiles is NULL.

See Also:

- ["DBA\_PART\_LOBS"](statviews_4176.md)
- ["USER\_PART\_LOBS"](statviews_5391.md)