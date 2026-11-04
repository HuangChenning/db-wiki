---
title: "28.3.35 The INFORMATION_SCHEMA ST_GEOMETRY_COLUMNS Table"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/information-schema-st-geometry-columns-table.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 28.3.35 The INFORMATION\_SCHEMA ST\_GEOMETRY\_COLUMNS Table

The `ST_GEOMETRY_COLUMNS` table provides information about table columns that store spatial data. This table is based on the SQL/MM (ISO/IEC 13249-3) standard, with extensions as noted. MySQL implements `ST_GEOMETRY_COLUMNS` as a view on the `INFORMATION_SCHEMA` [`COLUMNS`](information-schema-columns-table.md) table.

The `ST_GEOMETRY_COLUMNS` table has these columns:

- `TABLE_CATALOG`
	The name of the catalog to which the table containing the column belongs. This value is always `def`.
- `TABLE_SCHEMA`
	The name of the schema (database) to which the table containing the column belongs.
- `TABLE_NAME`
	The name of the table containing the column.
- `COLUMN_NAME`
	The name of the column.
- `SRS_NAME`
	The spatial reference system (SRS) name.
- `SRS_ID`
	The spatial reference system ID (SRID).
- `GEOMETRY_TYPE_NAME`
	The column data type. Permitted values are: `geometry`, `point`, `linestring`, `polygon`, `multipoint`, `multilinestring`, `multipolygon`, `geometrycollection`. This column is a MySQL extension to the standard.