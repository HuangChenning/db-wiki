---
title: "MySQL :: MySQL 26.10 Reference Manual :: 28.4.3 The INFORMATION_SCHEMA INNODB_BUFFER_PAGE_LRU Table"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/information-schema-innodb-buffer-page-lru-table.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 28.4.3 The INFORMATION\_SCHEMA INNODB\_BUFFER\_PAGE\_LRU Table

The `INNODB_BUFFER_PAGE_LRU` table provides information about the pages in the `InnoDB` [buffer pool](glossary.md); in particular, how they are ordered in the LRU list that determines which pages to [evict](glossary.md) from the buffer pool when it becomes full.

The `INNODB_BUFFER_PAGE_LRU` table has the same columns as the [`INNODB_BUFFER_PAGE`](information-schema-innodb-buffer-page-table.md) table with a few exceptions. It has `LRU_POSITION` and `COMPRESSED` columns instead of `BLOCK_ID` and `PAGE_STATE` columns, and it does not include and `IS_STALE` column.

For related usage information and examples, see [Section 17.15.5, “InnoDB INFORMATION\_SCHEMA Buffer Pool Tables”](innodb-information-schema-buffer-pool-tables.md).

Warning

Querying the `INNODB_BUFFER_PAGE_LRU` table can affect performance. Do not query this table on a production system unless you are aware of the performance impact and have determined it to be acceptable. To avoid impacting performance on a production system, reproduce the issue you want to investigate and query buffer pool statistics on a test instance.

The `INNODB_BUFFER_PAGE_LRU` table has these columns:

- `POOL_ID`
	The buffer pool ID. This is an identifier to distinguish between multiple buffer pool instances.
- `LRU_POSITION`
	The position of the page in the LRU list.
- `SPACE`
	The tablespace ID; the same value as `INNODB_TABLES.SPACE`.
- `PAGE_NUMBER`
	The page number.
- `PAGE_TYPE`
	The page type. The following table shows the permitted values.
	**Table 28.6 INNODB\_BUFFER\_PAGE\_LRU.PAGE\_TYPE Values**
	| Page Type | Description |
	| --- | --- |
	| `ALLOCATED` | Freshly allocated page |
	| `BLOB` | Uncompressed BLOB page |
	| `COMPRESSED_BLOB2` | Subsequent comp BLOB page |
	| `COMPRESSED_BLOB` | First compressed BLOB page |
	| `ENCRYPTED_RTREE` | Encrypted R-tree |
	| `EXTENT_DESCRIPTOR` | Extent descriptor page |
	| `FILE_SPACE_HEADER` | File space header |
	| `FIL_PAGE_TYPE_UNUSED` | Unused |
	| `IBUF_BITMAP` | Insert buffer bitmap |
	| `IBUF_FREE_LIST` | Insert buffer free list |
	| `IBUF_INDEX` | Insert buffer index |
	| `INDEX` | B-tree node |
	| `INODE` | Index node |
	| `LOB_DATA` | Uncompressed LOB data |
	| `LOB_FIRST` | First page of uncompressed LOB |
	| `LOB_INDEX` | Uncompressed LOB index |
	| `PAGE_IO_COMPRESSED` | Compressed page |
	| `PAGE_IO_COMPRESSED_ENCRYPTED` | Compressed and encrypted page |
	| `PAGE_IO_ENCRYPTED` | Encrypted page |
	| `RSEG_ARRAY` | Rollback segment array |
	| `RTREE_INDEX` | R-tree index |
	| `SDI_BLOB` | Uncompressed SDI BLOB |
	| `SDI_COMPRESSED_BLOB` | Compressed SDI BLOB |
	| `SDI_INDEX` | SDI index |
	| `SYSTEM` | System page |
	| `TRX_SYSTEM` | Transaction system data |
	| `UNDO_LOG` | Undo log page |
	| `UNKNOWN` | Unknown |
	| `ZLOB_DATA` | Compressed LOB data |
	| `ZLOB_FIRST` | First page of compressed LOB |
	| `ZLOB_FRAG` | Compressed LOB fragment |
	| `ZLOB_FRAG_ENTRY` | Compressed LOB fragment index |
	| `ZLOB_INDEX` | Compressed LOB index |
- `FLUSH_TYPE`
	The flush type.
- `FIX_COUNT`
	The number of threads using this block within the buffer pool. When zero, the block is eligible to be evicted.
- `IS_HASHED`
	Whether a hash index has been built on this page.
- `NEWEST_MODIFICATION`
	The Log Sequence Number of the youngest modification.
- `OLDEST_MODIFICATION`
	The Log Sequence Number of the oldest modification.
- `ACCESS_TIME`
	An abstract number used to judge the first access time of the page.
- `TABLE_NAME`
	The name of the table the page belongs to. This column is applicable only to pages with a `PAGE_TYPE` value of `INDEX`. The column is `NULL` if the server has not yet accessed the table.
- `INDEX_NAME`
	The name of the index the page belongs to. This can be the name of a clustered index or a secondary index. This column is applicable only to pages with a `PAGE_TYPE` value of `INDEX`.
- `NUMBER_RECORDS`
	The number of records within the page.
- `DATA_SIZE`
	The sum of the sizes of the records. This column is applicable only to pages with a `PAGE_TYPE` value of `INDEX`.
- `COMPRESSED_SIZE`
	The compressed page size. `NULL` for pages that are not compressed.
- `COMPRESSED`
	Whether the page is compressed.
- `IO_FIX`
	Whether any I/O is pending for this page: `IO_NONE` = no pending I/O, `IO_READ` = read pending, `IO_WRITE` = write pending.
- `IS_OLD`
	Whether the block is in the sublist of old blocks in the LRU list.
- `FREE_PAGE_CLOCK`
	The value of the `freed_page_clock` counter when the block was the last placed at the head of the LRU list. The `freed_page_clock` counter tracks the number of blocks removed from the end of the LRU list.

#### Example

```sql
mysql> SELECT * FROM INFORMATION_SCHEMA.INNODB_BUFFER_PAGE_LRU LIMIT 1\G
*************************** 1. row ***************************
            POOL_ID: 0
       LRU_POSITION: 0
              SPACE: 97
        PAGE_NUMBER: 1984
          PAGE_TYPE: INDEX
         FLUSH_TYPE: 1
          FIX_COUNT: 0
          IS_HASHED: YES
NEWEST_MODIFICATION: 719490396
OLDEST_MODIFICATION: 0
        ACCESS_TIME: 3378383796
         TABLE_NAME: \`employees\`.\`salaries\`
         INDEX_NAME: PRIMARY
     NUMBER_RECORDS: 468
          DATA_SIZE: 14976
    COMPRESSED_SIZE: 0
         COMPRESSED: NO
             IO_FIX: IO_NONE
             IS_OLD: YES
    FREE_PAGE_CLOCK: 0
```

#### Notes

- This table is useful primarily for expert-level performance monitoring, or when developing performance-related extensions for MySQL.
- You must have the [`PROCESS`](privileges-provided.md) privilege to query this table.
- Use the `INFORMATION_SCHEMA` [`COLUMNS`](information-schema-columns-table.md) table or the [`SHOW COLUMNS`](show-columns.md) statement to view additional information about the columns of this table, including data types and default values.
- Querying this table can require MySQL to allocate a large block of contiguous memory, more than 64 bytes times the number of active pages in the buffer pool. This allocation could potentially cause an out-of-memory error, especially for systems with multi-gigabyte buffer pools.
- Querying this table requires MySQL to lock the data structure representing the buffer pool while traversing the LRU list, which can reduce concurrency, especially for systems with multi-gigabyte buffer pools.
- When tables, table rows, partitions, or indexes are deleted, associated pages remain in the buffer pool until space is required for other data. The `INNODB_BUFFER_PAGE_LRU` table reports information about these pages until they are evicted from the buffer pool. For more information about how the `InnoDB` manages buffer pool data, see [Section 17.5.1, “Buffer Pool”](innodb-buffer-pool.md).