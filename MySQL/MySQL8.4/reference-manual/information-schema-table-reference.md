---
title: "28.2 INFORMATION_SCHEMA Table Reference"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/information-schema-table-reference.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

The following table summarizes all available `INFORMATION_SCHEMA` tables. For greater detail, see the individual table descriptions.

**Table 28.1 INFORMATION\_SCHEMA Tables**

| Table Name | Description | Deprecated |
| --- | --- | --- |
| [`ADMINISTRABLE_ROLE_AUTHORIZATIONS`](information-schema-administrable-role-authorizations-table.md) | Grantable users or roles for current user or role |  |
| [`APPLICABLE_ROLES`](information-schema-applicable-roles-table.md) | Applicable roles for current user |  |
| [`CHARACTER_SETS`](information-schema-character-sets-table.md) | Available character sets |  |
| [`CHECK_CONSTRAINTS`](information-schema-check-constraints-table.md) | Table and column CHECK constraints |  |
| [`COLLATION_CHARACTER_SET_APPLICABILITY`](information-schema-collation-character-set-applicability-table.md) | Character set applicable to each collation |  |
| [`COLLATIONS`](information-schema-collations-table.md) | Collations for each character set |  |
| [`COLUMN_PRIVILEGES`](information-schema-column-privileges-table.md) | Privileges defined on columns |  |
| [`COLUMN_STATISTICS`](information-schema-column-statistics-table.md) | Histogram statistics for column values |  |
| [`COLUMNS`](information-schema-columns-table.md) | Columns in each table |  |
| [`COLUMNS_EXTENSIONS`](information-schema-columns-extensions-table.md) | Column attributes for primary and secondary storage engines |  |
| [`CONNECTION_CONTROL_FAILED_LOGIN_ATTEMPTS`](information-schema-connection-control-failed-login-attempts-table.md) | Current number of consecutive failed connection attempts per account |  |
| [`ENABLED_ROLES`](information-schema-enabled-roles-table.md) | Roles enabled within current session |  |
| [`ENGINES`](information-schema-engines-table.md) | Storage engine properties |  |
| [`EVENTS`](information-schema-events-table.md) | Event Manager events |  |
| [`FILES`](information-schema-files-table.md) | Files that store tablespace data |  |
| [`INNODB_BUFFER_PAGE`](information-schema-innodb-buffer-page-table.md) | Pages in InnoDB buffer pool |  |
| [`INNODB_BUFFER_PAGE_LRU`](information-schema-innodb-buffer-page-lru-table.md) | LRU ordering of pages in InnoDB buffer pool |  |
| [`INNODB_BUFFER_POOL_STATS`](information-schema-innodb-buffer-pool-stats-table.md) | InnoDB buffer pool statistics |  |
| [`INNODB_CACHED_INDEXES`](information-schema-innodb-cached-indexes-table.md) | Number of index pages cached per index in InnoDB buffer pool |  |
| [`INNODB_CMP`](information-schema-innodb-cmp-table.md) | Status for operations related to compressed InnoDB tables |  |
| [`INNODB_CMP_PER_INDEX`](information-schema-innodb-cmp-per-index-table.md) | Status for operations related to compressed InnoDB tables and indexes |  |
| [`INNODB_CMP_PER_INDEX_RESET`](information-schema-innodb-cmp-per-index-table.md) | Status for operations related to compressed InnoDB tables and indexes |  |
| [`INNODB_CMP_RESET`](information-schema-innodb-cmp-table.md) | Status for operations related to compressed InnoDB tables |  |
| [`INNODB_CMPMEM`](information-schema-innodb-cmpmem-table.md) | Status for compressed pages within InnoDB buffer pool |  |
| [`INNODB_CMPMEM_RESET`](information-schema-innodb-cmpmem-table.md) | Status for compressed pages within InnoDB buffer pool |  |
| [`INNODB_COLUMNS`](information-schema-innodb-columns-table.md) | Columns in each InnoDB table |  |
| [`INNODB_DATAFILES`](information-schema-innodb-datafiles-table.md) | Data file path information for InnoDB file-per-table and general tablespaces |  |
| [`INNODB_FIELDS`](information-schema-innodb-fields-table.md) | Key columns of InnoDB indexes |  |
| [`INNODB_FOREIGN`](information-schema-innodb-foreign-table.md) | InnoDB foreign-key metadata |  |
| [`INNODB_FOREIGN_COLS`](information-schema-innodb-foreign-cols-table.md) | InnoDB foreign-key column status information |  |
| [`INNODB_FT_BEING_DELETED`](information-schema-innodb-ft-being-deleted-table.md) | Snapshot of INNODB\_FT\_DELETED table |  |
| [`INNODB_FT_CONFIG`](information-schema-innodb-ft-config-table.md) | Metadata for InnoDB table FULLTEXT index and associated processing |  |
| [`INNODB_FT_DEFAULT_STOPWORD`](information-schema-innodb-ft-default-stopword-table.md) | Default list of stopwords for InnoDB FULLTEXT indexes |  |
| [`INNODB_FT_DELETED`](information-schema-innodb-ft-deleted-table.md) | Rows deleted from InnoDB table FULLTEXT index |  |
| [`INNODB_FT_INDEX_CACHE`](information-schema-innodb-ft-index-cache-table.md) | Token information for newly inserted rows in InnoDB FULLTEXT index |  |
| [`INNODB_FT_INDEX_TABLE`](information-schema-innodb-ft-index-table-table.md) | Inverted index information for processing text searches against InnoDB table FULLTEXT index |  |
| [`INNODB_INDEXES`](information-schema-innodb-indexes-table.md) | InnoDB index metadata |  |
| [`INNODB_METRICS`](information-schema-innodb-metrics-table.md) | InnoDB performance information |  |
| [`INNODB_SESSION_TEMP_TABLESPACES`](information-schema-innodb-session-temp-tablespaces-table.md) | Session temporary-tablespace metadata |  |
| [`INNODB_TABLES`](information-schema-innodb-tables-table.md) | InnoDB table metadata |  |
| [`INNODB_TABLESPACES`](information-schema-innodb-tablespaces-table.md) | InnoDB file-per-table, general, and undo tablespace metadata |  |
| [`INNODB_TABLESPACES_BRIEF`](information-schema-innodb-tablespaces-brief-table.md) | Brief file-per-table, general, undo, and system tablespace metadata |  |
| [`INNODB_TABLESTATS`](information-schema-innodb-tablestats-table.md) | InnoDB table low-level status information |  |
| [`INNODB_TEMP_TABLE_INFO`](information-schema-innodb-temp-table-info-table.md) | Information about active user-created InnoDB temporary tables |  |
| [`INNODB_TRX`](information-schema-innodb-trx-table.md) | Active InnoDB transaction information |  |
| [`INNODB_VIRTUAL`](information-schema-innodb-virtual-table.md) | InnoDB virtual generated column metadata |  |
| [`KEY_COLUMN_USAGE`](information-schema-key-column-usage-table.md) | Which key columns have constraints |  |
| [`KEYWORDS`](information-schema-keywords-table.md) | MySQL keywords |  |
| [`MYSQL_FIREWALL_USERS`](information-schema-mysql-firewall-users-table.md) | Firewall in-memory data for account profiles | Yes |
| [`MYSQL_FIREWALL_WHITELIST`](information-schema-mysql-firewall-whitelist-table.md) | Firewall in-memory data for account profile allowlists | Yes |
| [`ndb_transid_mysql_connection_map`](information-schema-ndb-transid-mysql-connection-map-table.md) | NDB transaction information |  |
| [`OPTIMIZER_TRACE`](information-schema-optimizer-trace-table.md) | Information produced by optimizer trace activity |  |
| [`PARAMETERS`](information-schema-parameters-table.md) | Stored routine parameters and stored function return values |  |
| [`PARTITIONS`](information-schema-partitions-table.md) | Table partition information |  |
| [`PLUGINS`](information-schema-plugins-table.md) | Plugin information |  |
| [`PROCESSLIST`](information-schema-processlist-table.md) | Information about currently executing threads |  |
| [`PROFILING`](information-schema-profiling-table.md) | Statement profiling information |  |
| [`REFERENTIAL_CONSTRAINTS`](information-schema-referential-constraints-table.md) | Foreign key information |  |
| [`RESOURCE_GROUPS`](information-schema-resource-groups-table.md) | Resource group information |  |
| [`ROLE_COLUMN_GRANTS`](information-schema-role-column-grants-table.md) | Column privileges for roles available to or granted by currently enabled roles |  |
| [`ROLE_ROUTINE_GRANTS`](information-schema-role-routine-grants-table.md) | Routine privileges for roles available to or granted by currently enabled roles |  |
| [`ROLE_TABLE_GRANTS`](information-schema-role-table-grants-table.md) | Table privileges for roles available to or granted by currently enabled roles |  |
| [`ROUTINES`](information-schema-routines-table.md) | Stored routine information |  |
| [`SCHEMA_PRIVILEGES`](information-schema-schema-privileges-table.md) | Privileges defined on schemas |  |
| [`SCHEMATA`](information-schema-schemata-table.md) | Schema information |  |
| [`SCHEMATA_EXTENSIONS`](information-schema-schemata-extensions-table.md) | Schema options |  |
| [`ST_GEOMETRY_COLUMNS`](information-schema-st-geometry-columns-table.md) | Columns in each table that store spatial data |  |
| [`ST_SPATIAL_REFERENCE_SYSTEMS`](information-schema-st-spatial-reference-systems-table.md) | Available spatial reference systems |  |
| [`ST_UNITS_OF_MEASURE`](information-schema-st-units-of-measure-table.md) | Acceptable units for ST\_Distance() |  |
| [`STATISTICS`](information-schema-statistics-table.md) | Table index statistics |  |
| [`TABLE_CONSTRAINTS`](information-schema-table-constraints-table.md) | Which tables have constraints |  |
| [`TABLE_CONSTRAINTS_EXTENSIONS`](information-schema-table-constraints-extensions-table.md) | Table constraint attributes for primary and secondary storage engines |  |
| [`TABLE_PRIVILEGES`](information-schema-table-privileges-table.md) | Privileges defined on tables |  |
| [`TABLES`](information-schema-tables-table.md) | Table information |  |
| [`TABLES_EXTENSIONS`](information-schema-tables-extensions-table.md) | Table attributes for primary and secondary storage engines |  |
| [`TABLESPACES_EXTENSIONS`](information-schema-tablespaces-extensions-table.md) | Tablespace attributes for primary storage engines |  |
| [`TP_THREAD_GROUP_STATE`](information-schema-tp-thread-group-state-table.md) | Thread pool thread group states |  |
| [`TP_THREAD_GROUP_STATS`](information-schema-tp-thread-group-stats-table.md) | Thread pool thread group statistics |  |
| [`TP_THREAD_STATE`](information-schema-tp-thread-state-table.md) | Thread pool thread information |  |
| [`TRIGGERS`](information-schema-triggers-table.md) | Trigger information |  |
| [`USER_ATTRIBUTES`](information-schema-user-attributes-table.md) | User comments and attributes |  |
| [`USER_PRIVILEGES`](information-schema-user-privileges-table.md) | Privileges defined globally per user |  |
| [`VIEW_ROUTINE_USAGE`](information-schema-view-routine-usage-table.md) | Stored functions used in views |  |
| [`VIEW_TABLE_USAGE`](information-schema-view-table-usage-table.md) | Tables and views used in views |  |
| [`VIEWS`](information-schema-views-table.md) | View information |  |