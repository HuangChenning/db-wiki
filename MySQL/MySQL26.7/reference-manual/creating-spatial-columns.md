---
title: "MySQL :: MySQL 26.7 Reference Manual :: 13.4.6 Creating Spatial Columns"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/creating-spatial-columns.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 13.4.6 Creating Spatial Columns

MySQL provides a standard way of creating spatial columns for geometry types, for example, with [`CREATE         TABLE`](create-table.md) or [`ALTER TABLE`](alter-table.md). Spatial columns are supported for [`MyISAM`](myisam-storage-engine.md), [`InnoDB`](innodb-storage-engine.md), [`NDB`](mysql-cluster.md), and [`ARCHIVE`](archive-storage-engine.md) tables. See also the notes about spatial indexes under [Section 13.4.10, “Creating Spatial Indexes”](creating-spatial-indexes.md).

Columns with a spatial data type can have an SRID attribute, to explicitly indicate the spatial reference system (SRS) for values stored in the column. For implications of an SRID-restricted column, see [Section 13.4.1, “Spatial Data Types”](spatial-type-overview.md).

- Use the [`CREATE TABLE`](create-table.md) statement to create a table with a spatial column:
	```sql
	CREATE TABLE geom (g GEOMETRY);
	```
- Use the [`ALTER TABLE`](alter-table.md) statement to add or drop a spatial column to or from an existing table:
	```sql
	ALTER TABLE geom ADD pt POINT;
	ALTER TABLE geom DROP pt;
	```