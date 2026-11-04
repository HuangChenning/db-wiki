---
title: "24.4.1 INFORMATION_SCHEMA InnoDB Table Reference"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/information-schema-innodb-table-reference.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 24.4.1 INFORMATION\_SCHEMA InnoDB Table Reference

The following table summarizes `INFORMATION_SCHEMA` InnoDB tables. For greater detail, see the individual table descriptions.

**Table 24.3 INFORMATION\_SCHEMA InnoDB Tables**

| Table Name | Description | Deprecated |
| --- | --- | --- |
| [`INNODB_BUFFER_PAGE`](information-schema-innodb-buffer-page-table.md) | Pages in InnoDB buffer pool |  |
| [`INNODB_BUFFER_PAGE_LRU`](information-schema-innodb-buffer-page-lru-table.md) | LRU ordering of pages in InnoDB buffer pool |  |
| [`INNODB_BUFFER_POOL_STATS`](information-schema-innodb-buffer-pool-stats-table.md) | InnoDB buffer pool statistics |  |
| [`INNODB_CMP`](information-schema-innodb-cmp-table.md) | Status for operations related to compressed InnoDB tables |  |
| [`INNODB_CMP_PER_INDEX`](information-schema-innodb-cmp-per-index-table.md) | Status for operations related to compressed InnoDB tables and indexes |  |
| [`INNODB_CMP_PER_INDEX_RESET`](information-schema-innodb-cmp-per-index-table.md) | Status for operations related to compressed InnoDB tables and indexes |  |
| [`INNODB_CMP_RESET`](information-schema-innodb-cmp-table.md) | Status for operations related to compressed InnoDB tables |  |
| [`INNODB_CMPMEM`](information-schema-innodb-cmpmem-table.md) | Status for compressed pages within InnoDB buffer pool |  |
| [`INNODB_CMPMEM_RESET`](information-schema-innodb-cmpmem-table.md) | Status for compressed pages within InnoDB buffer pool |  |
| [`INNODB_FT_BEING_DELETED`](information-schema-innodb-ft-being-deleted-table.md) | Snapshot of INNODB\_FT\_DELETED table |  |
| [`INNODB_FT_CONFIG`](information-schema-innodb-ft-config-table.md) | Metadata for InnoDB table FULLTEXT index and associated processing |  |
| [`INNODB_FT_DEFAULT_STOPWORD`](information-schema-innodb-ft-default-stopword-table.md) | Default list of stopwords for InnoDB FULLTEXT indexes |  |
| [`INNODB_FT_DELETED`](information-schema-innodb-ft-deleted-table.md) | Rows deleted from InnoDB table FULLTEXT index |  |
| [`INNODB_FT_INDEX_CACHE`](information-schema-innodb-ft-index-cache-table.md) | Token information for newly inserted rows in InnoDB FULLTEXT index |  |
| [`INNODB_FT_INDEX_TABLE`](information-schema-innodb-ft-index-table-table.md) | Inverted index information for processing text searches against InnoDB table FULLTEXT index |  |
| [`INNODB_LOCK_WAITS`](information-schema-innodb-lock-waits-table.md) | InnoDB transaction lock-wait information | Yes |
| [`INNODB_LOCKS`](information-schema-innodb-locks-table.md) | InnoDB transaction lock information | Yes |
| [`INNODB_METRICS`](information-schema-innodb-metrics-table.md) | InnoDB performance information |  |
| [`INNODB_SYS_COLUMNS`](information-schema-innodb-sys-columns-table.md) | Columns in each InnoDB table |  |
| [`INNODB_SYS_DATAFILES`](information-schema-innodb-sys-datafiles-table.md) | Data file path information for InnoDB file-per-table and general tablespaces |  |
| [`INNODB_SYS_FIELDS`](information-schema-innodb-sys-fields-table.md) | Key columns of InnoDB indexes |  |
| [`INNODB_SYS_FOREIGN`](information-schema-innodb-sys-foreign-table.md) | InnoDB foreign-key metadata |  |
| [`INNODB_SYS_FOREIGN_COLS`](information-schema-innodb-sys-foreign-cols-table.md) | InnoDB foreign-key column status information |  |
| [`INNODB_SYS_INDEXES`](information-schema-innodb-sys-indexes-table.md) | InnoDB index metadata |  |
| [`INNODB_SYS_TABLES`](information-schema-innodb-sys-tables-table.md) | InnoDB table metadata |  |
| [`INNODB_SYS_TABLESPACES`](information-schema-innodb-sys-tablespaces-table.md) | InnoDB file-per-table, general, and undo tablespace metadata |  |
| [`INNODB_SYS_TABLESTATS`](information-schema-innodb-sys-tablestats-table.md) | InnoDB table low-level status information |  |
| [`INNODB_SYS_VIRTUAL`](information-schema-innodb-sys-virtual-table.md) | InnoDB virtual generated column metadata |  |
| [`INNODB_TEMP_TABLE_INFO`](information-schema-innodb-temp-table-info-table.md) | Information about active user-created InnoDB temporary tables |  |
| [`INNODB_TRX`](information-schema-innodb-trx-table.md) | Active InnoDB transaction information |  |