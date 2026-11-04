---
title: "24.2 INFORMATION_SCHEMA Table Reference"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/information-schema-table-reference.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

The following table summarizes all available `INFORMATION_SCHEMA` tables. For greater detail, see the individual table descriptions.

**Table 24.1 INFORMATION\_SCHEMA Tables**

| Table Name | Description | Deprecated |
| --- | --- | --- |
| [`CHARACTER_SETS`](information-schema-character-sets-table.md) | Available character sets |  |
| [`COLLATION_CHARACTER_SET_APPLICABILITY`](information-schema-collation-character-set-applicability-table.md) | Character set applicable to each collation |  |
| [`COLLATIONS`](information-schema-collations-table.md) | Collations for each character set |  |
| [`COLUMN_PRIVILEGES`](information-schema-column-privileges-table.md) | Privileges defined on columns |  |
| [`COLUMNS`](information-schema-columns-table.md) | Columns in each table |  |
| [`CONNECTION_CONTROL_FAILED_LOGIN_ATTEMPTS`](information-schema-connection-control-failed-login-attempts-table.md) | Current number of consecutive failed connection attempts per account |  |
| [`ENGINES`](information-schema-engines-table.md) | Storage engine properties |  |
| [`EVENTS`](information-schema-events-table.md) | Event Manager events |  |
| [`FILES`](information-schema-files-table.md) | Files that store tablespace data |  |
| [`GLOBAL_STATUS`](information-schema-status-table.md) | Global status variables |  |
| [`GLOBAL_VARIABLES`](information-schema-variables-table.md) | Global system variables |  |
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
| [`KEY_COLUMN_USAGE`](information-schema-key-column-usage-table.md) | Which key columns have constraints |  |
| [`MYSQL_FIREWALL_USERS`](information-schema-mysql-firewall-users-table.md) | Firewall in-memory data for account profiles |  |
| [`MYSQL_FIREWALL_WHITELIST`](information-schema-mysql-firewall-whitelist-table.md) | Firewall in-memory data for account profile allowlists |  |
| [`ndb_transid_mysql_connection_map`](information-schema-ndb-transid-mysql-connection-map-table.md) | NDB transaction information |  |
| [`OPTIMIZER_TRACE`](information-schema-optimizer-trace-table.md) | Information produced by optimizer trace activity |  |
| [`PARAMETERS`](information-schema-parameters-table.md) | Stored routine parameters and stored function return values |  |
| [`PARTITIONS`](information-schema-partitions-table.md) | Table partition information |  |
| [`PLUGINS`](information-schema-plugins-table.md) | Plugin information |  |
| [`PROCESSLIST`](information-schema-processlist-table.md) | Information about currently executing threads |  |
| [`PROFILING`](information-schema-profiling-table.md) | Statement profiling information |  |
| [`REFERENTIAL_CONSTRAINTS`](information-schema-referential-constraints-table.md) | Foreign key information |  |
| [`ROUTINES`](information-schema-routines-table.md) | Stored routine information |  |
| [`SCHEMA_PRIVILEGES`](information-schema-schema-privileges-table.md) | Privileges defined on schemas |  |
| [`SCHEMATA`](information-schema-schemata-table.md) | Schema information |  |
| [`SESSION_STATUS`](information-schema-status-table.md) | Status variables for current session |  |
| [`SESSION_VARIABLES`](information-schema-variables-table.md) | System variables for current session |  |
| [`STATISTICS`](information-schema-statistics-table.md) | Table index statistics |  |
| [`TABLE_CONSTRAINTS`](information-schema-table-constraints-table.md) | Which tables have constraints |  |
| [`TABLE_PRIVILEGES`](information-schema-table-privileges-table.md) | Privileges defined on tables |  |
| [`TABLES`](information-schema-tables-table.md) | Table information |  |
| [`TABLESPACES`](information-schema-tablespaces-table.md) | Tablespace information |  |
| [`TP_THREAD_GROUP_STATE`](information-schema-tp-thread-group-state-table.md) | Thread pool thread group states |  |
| [`TP_THREAD_GROUP_STATS`](information-schema-tp-thread-group-stats-table.md) | Thread pool thread group statistics |  |
| [`TP_THREAD_STATE`](information-schema-tp-thread-state-table.md) | Thread pool thread information |  |
| [`TRIGGERS`](information-schema-triggers-table.md) | Trigger information |  |
| [`USER_PRIVILEGES`](information-schema-user-privileges-table.md) | Privileges defined globally per user |  |
| [`VIEWS`](information-schema-views-table.md) | View information |  |