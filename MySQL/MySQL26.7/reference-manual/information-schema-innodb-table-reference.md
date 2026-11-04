---
title: "MySQL :: MySQL 26.7 Reference Manual :: 28.4.1 INFORMATION_SCHEMA InnoDB Table Reference"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/information-schema-innodb-table-reference.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 28.4.1 INFORMATION\_SCHEMA InnoDB Table Reference

The following table summarizes `INFORMATION_SCHEMA` InnoDB tables. For greater detail, see the individual table descriptions.

**Table 28.3 INFORMATION\_SCHEMA InnoDB Tables**

| Table Name | Description |
| --- | --- |
| [`INNODB_BUFFER_PAGE`](information-schema-innodb-buffer-page-table.md) | Pages in InnoDB buffer pool |
| [`INNODB_BUFFER_PAGE_LRU`](information-schema-innodb-buffer-page-lru-table.md) | LRU ordering of pages in InnoDB buffer pool |
| [`INNODB_BUFFER_POOL_STATS`](information-schema-innodb-buffer-pool-stats-table.md) | InnoDB buffer pool statistics |
| [`INNODB_CACHED_INDEXES`](information-schema-innodb-cached-indexes-table.md) | Number of index pages cached per index in InnoDB buffer pool |
| [`INNODB_CMP`](information-schema-innodb-cmp-table.md) | Status for operations related to compressed InnoDB tables |
| [`INNODB_CMP_PER_INDEX`](information-schema-innodb-cmp-per-index-table.md) | Status for operations related to compressed InnoDB tables and indexes |
| [`INNODB_CMP_PER_INDEX_RESET`](information-schema-innodb-cmp-per-index-table.md) | Status for operations related to compressed InnoDB tables and indexes |
| [`INNODB_CMP_RESET`](information-schema-innodb-cmp-table.md) | Status for operations related to compressed InnoDB tables |
| [`INNODB_CMPMEM`](information-schema-innodb-cmpmem-table.md) | Status for compressed pages within InnoDB buffer pool |
| [`INNODB_CMPMEM_RESET`](information-schema-innodb-cmpmem-table.md) | Status for compressed pages within InnoDB buffer pool |
| [`INNODB_COLUMNS`](information-schema-innodb-columns-table.md) | Columns in each InnoDB table |
| [`INNODB_DATAFILES`](information-schema-innodb-datafiles-table.md) | Data file path information for InnoDB file-per-table and general tablespaces |
| [`INNODB_FIELDS`](information-schema-innodb-fields-table.md) | Key columns of InnoDB indexes |
| [`INNODB_FOREIGN`](information-schema-innodb-foreign-table.md) | InnoDB foreign-key metadata |
| [`INNODB_FOREIGN_COLS`](information-schema-innodb-foreign-cols-table.md) | InnoDB foreign-key column status information |
| [`INNODB_FT_BEING_DELETED`](information-schema-innodb-ft-being-deleted-table.md) | Snapshot of INNODB\_FT\_DELETED table |
| [`INNODB_FT_CONFIG`](information-schema-innodb-ft-config-table.md) | Metadata for InnoDB table FULLTEXT index and associated processing |
| [`INNODB_FT_DEFAULT_STOPWORD`](information-schema-innodb-ft-default-stopword-table.md) | Default list of stopwords for InnoDB FULLTEXT indexes |
| [`INNODB_FT_DELETED`](information-schema-innodb-ft-deleted-table.md) | Rows deleted from InnoDB table FULLTEXT index |
| [`INNODB_FT_INDEX_CACHE`](information-schema-innodb-ft-index-cache-table.md) | Token information for newly inserted rows in InnoDB FULLTEXT index |
| [`INNODB_FT_INDEX_TABLE`](information-schema-innodb-ft-index-table-table.md) | Inverted index information for processing text searches against InnoDB table FULLTEXT index |
| [`INNODB_INDEXES`](information-schema-innodb-indexes-table.md) | InnoDB index metadata |
| [`INNODB_METRICS`](information-schema-innodb-metrics-table.md) | InnoDB performance information |
| [`INNODB_SESSION_TEMP_TABLESPACES`](information-schema-innodb-session-temp-tablespaces-table.md) | Session temporary-tablespace metadata |
| [`INNODB_TABLES`](information-schema-innodb-tables-table.md) | InnoDB table metadata |
| [`INNODB_TABLESPACES`](information-schema-innodb-tablespaces-table.md) | InnoDB file-per-table, general, and undo tablespace metadata |
| [`INNODB_TABLESPACES_BRIEF`](information-schema-innodb-tablespaces-brief-table.md) | Brief file-per-table, general, undo, and system tablespace metadata |
| [`INNODB_TABLESTATS`](information-schema-innodb-tablestats-table.md) | InnoDB table low-level status information |
| [`INNODB_TEMP_TABLE_INFO`](information-schema-innodb-temp-table-info-table.md) | Information about active user-created InnoDB temporary tables |
| [`INNODB_TRX`](information-schema-innodb-trx-table.md) | Active InnoDB transaction information |
| [`INNODB_VIRTUAL`](information-schema-innodb-virtual-table.md) | InnoDB virtual generated column metadata |