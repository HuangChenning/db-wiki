---
title: "24.3.1 INFORMATION_SCHEMA General Table Reference"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/information-schema-general-table-reference.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 24.3.1 INFORMATION\_SCHEMA General Table Reference

The following table summarizes `INFORMATION_SCHEMA` general tables. For greater detail, see the individual table descriptions.

**Table 24.2 INFORMATION\_SCHEMA General Tables**

| Table Name | Description |
| --- | --- |
| [`CHARACTER_SETS`](information-schema-character-sets-table.md) | Available character sets |
| [`COLLATION_CHARACTER_SET_APPLICABILITY`](information-schema-collation-character-set-applicability-table.md) | Character set applicable to each collation |
| [`COLLATIONS`](information-schema-collations-table.md) | Collations for each character set |
| [`COLUMN_PRIVILEGES`](information-schema-column-privileges-table.md) | Privileges defined on columns |
| [`COLUMNS`](information-schema-columns-table.md) | Columns in each table |
| [`ENGINES`](information-schema-engines-table.md) | Storage engine properties |
| [`EVENTS`](information-schema-events-table.md) | Event Manager events |
| [`FILES`](information-schema-files-table.md) | Files that store tablespace data |
| [`GLOBAL_STATUS`](information-schema-status-table.md) | Global status variables |
| [`GLOBAL_VARIABLES`](information-schema-variables-table.md) | Global system variables |
| [`KEY_COLUMN_USAGE`](information-schema-key-column-usage-table.md) | Which key columns have constraints |
| [`ndb_transid_mysql_connection_map`](information-schema-ndb-transid-mysql-connection-map-table.md) | NDB transaction information |
| [`OPTIMIZER_TRACE`](information-schema-optimizer-trace-table.md) | Information produced by optimizer trace activity |
| [`PARAMETERS`](information-schema-parameters-table.md) | Stored routine parameters and stored function return values |
| [`PARTITIONS`](information-schema-partitions-table.md) | Table partition information |
| [`PLUGINS`](information-schema-plugins-table.md) | Plugin information |
| [`PROCESSLIST`](information-schema-processlist-table.md) | Information about currently executing threads |
| [`PROFILING`](information-schema-profiling-table.md) | Statement profiling information |
| [`REFERENTIAL_CONSTRAINTS`](information-schema-referential-constraints-table.md) | Foreign key information |
| [`ROUTINES`](information-schema-routines-table.md) | Stored routine information |
| [`SCHEMA_PRIVILEGES`](information-schema-schema-privileges-table.md) | Privileges defined on schemas |
| [`SCHEMATA`](information-schema-schemata-table.md) | Schema information |
| [`SESSION_STATUS`](information-schema-status-table.md) | Status variables for current session |
| [`SESSION_VARIABLES`](information-schema-variables-table.md) | System variables for current session |
| [`STATISTICS`](information-schema-statistics-table.md) | Table index statistics |
| [`TABLE_CONSTRAINTS`](information-schema-table-constraints-table.md) | Which tables have constraints |
| [`TABLE_PRIVILEGES`](information-schema-table-privileges-table.md) | Privileges defined on tables |
| [`TABLES`](information-schema-tables-table.md) | Table information |
| [`TABLESPACES`](information-schema-tablespaces-table.md) | Tablespace information |
| [`TRIGGERS`](information-schema-triggers-table.md) | Trigger information |
| [`USER_PRIVILEGES`](information-schema-user-privileges-table.md) | Privileges defined globally per user |
| [`VIEWS`](information-schema-views-table.md) | View information |