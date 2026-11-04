---
title: "28.3.1 INFORMATION_SCHEMA General Table Reference"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/information-schema-general-table-reference.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 28.3.1 INFORMATION\_SCHEMA General Table Reference

The following table summarizes `INFORMATION_SCHEMA` general tables. For greater detail, see the individual table descriptions.

**Table 28.2 INFORMATION\_SCHEMA General Tables**

| Table Name | Description |
| --- | --- |
| [`ADMINISTRABLE_ROLE_AUTHORIZATIONS`](information-schema-administrable-role-authorizations-table.md) | Grantable users or roles for current user or role |
| [`APPLICABLE_ROLES`](information-schema-applicable-roles-table.md) | Applicable roles for current user |
| [`CHARACTER_SETS`](information-schema-character-sets-table.md) | Available character sets |
| [`CHECK_CONSTRAINTS`](information-schema-check-constraints-table.md) | Table and column CHECK constraints |
| [`COLLATION_CHARACTER_SET_APPLICABILITY`](information-schema-collation-character-set-applicability-table.md) | Character set applicable to each collation |
| [`COLLATIONS`](information-schema-collations-table.md) | Collations for each character set |
| [`COLUMN_PRIVILEGES`](information-schema-column-privileges-table.md) | Privileges defined on columns |
| [`COLUMN_STATISTICS`](information-schema-column-statistics-table.md) | Histogram statistics for column values |
| [`COLUMNS`](information-schema-columns-table.md) | Columns in each table |
| [`COLUMNS_EXTENSIONS`](information-schema-columns-extensions-table.md) | Column attributes for primary and secondary storage engines |
| [`ENABLED_ROLES`](information-schema-enabled-roles-table.md) | Roles enabled within current session |
| [`ENGINES`](information-schema-engines-table.md) | Storage engine properties |
| [`EVENTS`](information-schema-events-table.md) | Event Manager events |
| [`FILES`](information-schema-files-table.md) | Files that store tablespace data |
| [`KEY_COLUMN_USAGE`](information-schema-key-column-usage-table.md) | Which key columns have constraints |
| [`KEYWORDS`](information-schema-keywords-table.md) | MySQL keywords |
| [`LIBRARIES`](information-schema-libraries-table.md) | Information about JavaScript libraries |
| [`ndb_transid_mysql_connection_map`](information-schema-ndb-transid-mysql-connection-map-table.md) | NDB transaction information |
| [`OPTIMIZER_TRACE`](information-schema-optimizer-trace-table.md) | Information produced by optimizer trace activity |
| [`PARAMETERS`](information-schema-parameters-table.md) | Stored routine parameters and stored function return values |
| [`PARTITIONS`](information-schema-partitions-table.md) | Table partition information |
| [`PLUGINS`](information-schema-plugins-table.md) | Plugin information |
| [`PROCESSLIST`](information-schema-processlist-table.md) | Information about currently executing threads |
| [`PROFILING`](information-schema-profiling-table.md) | Statement profiling information |
| [`REFERENTIAL_CONSTRAINTS`](information-schema-referential-constraints-table.md) | Foreign key information |
| [`RESOURCE_GROUPS`](information-schema-resource-groups-table.md) | Resource group information |
| [`ROLE_COLUMN_GRANTS`](information-schema-role-column-grants-table.md) | Column privileges for roles available to or granted by currently enabled roles |
| [`ROLE_ROUTINE_GRANTS`](information-schema-role-routine-grants-table.md) | Routine privileges for roles available to or granted by currently enabled roles |
| [`ROLE_TABLE_GRANTS`](information-schema-role-table-grants-table.md) | Table privileges for roles available to or granted by currently enabled roles |
| [`ROUTINE_LIBRARIES`](information-schema-routine-libraries-table.md) | Information about libraries used in JavaScript stored routines |
| [`ROUTINES`](information-schema-routines-table.md) | Stored routine information |
| [`SCHEMA_PRIVILEGES`](information-schema-schema-privileges-table.md) | Privileges defined on schemas |
| [`SCHEMATA`](information-schema-schemata-table.md) | Schema information |
| [`SCHEMATA_EXTENSIONS`](information-schema-schemata-extensions-table.md) | Schema options |
| [`ST_GEOMETRY_COLUMNS`](information-schema-st-geometry-columns-table.md) | Columns in each table that store spatial data |
| [`ST_SPATIAL_REFERENCE_SYSTEMS`](information-schema-st-spatial-reference-systems-table.md) | Available spatial reference systems |
| [`ST_UNITS_OF_MEASURE`](information-schema-st-units-of-measure-table.md) | Acceptable units for ST\_Distance() |
| [`STATISTICS`](information-schema-statistics-table.md) | Table index statistics |
| [`TABLE_CONSTRAINTS`](information-schema-table-constraints-table.md) | Which tables have constraints |
| [`TABLE_CONSTRAINTS_EXTENSIONS`](information-schema-table-constraints-extensions-table.md) | Table constraint attributes for primary and secondary storage engines |
| [`TABLE_PRIVILEGES`](information-schema-table-privileges-table.md) | Privileges defined on tables |
| [`TABLES`](information-schema-tables-table.md) | Table information |
| [`TABLES_EXTENSIONS`](information-schema-tables-extensions-table.md) | Table attributes for primary and secondary storage engines |
| [`TABLESPACES_EXTENSIONS`](information-schema-tablespaces-extensions-table.md) | Tablespace attributes for primary storage engines |
| [`TRIGGERS`](information-schema-triggers-table.md) | Trigger information |
| [`USER_ATTRIBUTES`](information-schema-user-attributes-table.md) | User comments and attributes |
| [`USER_PRIVILEGES`](information-schema-user-privileges-table.md) | Privileges defined globally per user |
| [`VIEW_ROUTINE_USAGE`](information-schema-view-routine-usage-table.md) | Stored functions used in views |
| [`VIEW_TABLE_USAGE`](information-schema-view-table-usage-table.md) | Tables and views used in views |
| [`VIEWS`](information-schema-views-table.md) | View information |