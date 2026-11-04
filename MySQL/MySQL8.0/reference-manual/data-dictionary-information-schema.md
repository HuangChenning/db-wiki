---
title: "16.5 INFORMATION_SCHEMA and Data Dictionary Integration"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/data-dictionary-information-schema.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

With the introduction of the data dictionary, the following [`INFORMATION_SCHEMA`](information-schema.md) tables are implemented as views on data dictionary tables:

- [`CHARACTER_SETS`](information-schema-character-sets-table.md)
- [`CHECK_CONSTRAINTS`](information-schema-check-constraints-table.md)
- [`COLLATIONS`](information-schema-collations-table.md)
- [`COLLATION_CHARACTER_SET_APPLICABILITY`](information-schema-collation-character-set-applicability-table.md)
- [`COLUMNS`](information-schema-columns-table.md)
- [`COLUMN_STATISTICS`](information-schema-column-statistics-table.md)
- [`EVENTS`](information-schema-events-table.md)
- [`FILES`](information-schema-files-table.md)
- [`INNODB_COLUMNS`](information-schema-innodb-columns-table.md)
- [`INNODB_DATAFILES`](information-schema-innodb-datafiles-table.md)
- [`INNODB_FIELDS`](information-schema-innodb-fields-table.md)
- [`INNODB_FOREIGN`](information-schema-innodb-foreign-table.md)
- [`INNODB_FOREIGN_COLS`](information-schema-innodb-foreign-cols-table.md)
- [`INNODB_INDEXES`](information-schema-innodb-indexes-table.md)
- [`INNODB_TABLES`](information-schema-innodb-tables-table.md)
- [`INNODB_TABLESPACES`](information-schema-innodb-tablespaces-table.md)
- [`INNODB_TABLESPACES_BRIEF`](information-schema-innodb-tablespaces-brief-table.md)
- [`INNODB_TABLESTATS`](information-schema-innodb-tablestats-table.md)
- [`KEY_COLUMN_USAGE`](information-schema-key-column-usage-table.md)
- `KEYWORDS`
- [`PARAMETERS`](information-schema-parameters-table.md)
- [`PARTITIONS`](information-schema-partitions-table.md)
- [`REFERENTIAL_CONSTRAINTS`](information-schema-referential-constraints-table.md)
- [`RESOURCE_GROUPS`](information-schema-resource-groups-table.md)
- [`ROUTINES`](information-schema-routines-table.md)
- [`SCHEMATA`](information-schema-schemata-table.md)
- [`STATISTICS`](information-schema-statistics-table.md)
- [`ST_GEOMETRY_COLUMNS`](information-schema-st-geometry-columns-table.md)
- [`ST_SPATIAL_REFERENCE_SYSTEMS`](information-schema-st-spatial-reference-systems-table.md)
- [`TABLES`](information-schema-tables-table.md)
- [`TABLE_CONSTRAINTS`](information-schema-table-constraints-table.md)
- [`TRIGGERS`](information-schema-triggers-table.md)
- [`VIEWS`](information-schema-views-table.md)
- [`VIEW_ROUTINE_USAGE`](information-schema-view-routine-usage-table.md)
- [`VIEW_TABLE_USAGE`](information-schema-view-table-usage-table.md)

Queries on those tables are now more efficient because they obtain information from data dictionary tables rather than by other, slower means. In particular, for each `INFORMATION_SCHEMA` table that is a view on data dictionary tables:

- The server no longer must create a temporary table for each query of the `INFORMATION_SCHEMA` table.
- When the underlying data dictionary tables store values previously obtained by directory scans (for example, to enumerate database names or table names within databases) or file-opening operations (for example, to read information from `.frm` files), `INFORMATION_SCHEMA` queries for those values now use table lookups instead. (Additionally, even for a non-view `INFORMATION_SCHEMA` table, values such as database and table names are retrieved by lookups from the data dictionary and do not require directory or file scans.)
- Indexes on the underlying data dictionary tables permit the optimizer to construct efficient query execution plans, something not true for the previous implementation that processed the `INFORMATION_SCHEMA` table using a temporary table per query.

The preceding improvements also apply to [`SHOW`](show.md) statements that display information corresponding to the `INFORMATION_SCHEMA` tables that are views on data dictionary tables. For example, [`SHOW       DATABASES`](show-databases.md) displays the same information as the [`SCHEMATA`](information-schema-schemata-table.md) table.

In addition to the introduction of views on data dictionary tables, table statistics contained in the [`STATISTICS`](information-schema-statistics-table.md) and [`TABLES`](information-schema-tables-table.md) tables is now cached to improve [`INFORMATION_SCHEMA`](information-schema.md) query performance. The [`information_schema_stats_expiry`](server-system-variables.md) system variable defines the period of time before cached table statistics expire. The default is 86400 seconds (24 hours). If there are no cached statistics or statistics have expired, statistics are retrieved from storage engine when querying table statistics columns. To update cached values at any time for a given table, use [`ANALYZE TABLE`](analyze-table.md)

[`information_schema_stats_expiry`](server-system-variables.md) can be set to `0` to have [`INFORMATION_SCHEMA`](information-schema.md) queries retrieve the latest statistics directly from the storage engine, which is not as fast as retrieving cached statistics.

For more information, see [Section 10.2.3, “Optimizing INFORMATION\_SCHEMA Queries”](information-schema-optimization.md).

`INFORMATION_SCHEMA` tables in MySQL 8.0 are closely tied to the data dictionary, resulting in several usage differences. See [Section 16.7, “Data Dictionary Usage Differences”](data-dictionary-usage-differences.md).