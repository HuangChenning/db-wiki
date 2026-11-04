---
title: "11.4.5 Creating Spatial Columns"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/creating-spatial-columns.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 11.4.5 Creating Spatial Columns

MySQL provides a standard way of creating spatial columns for geometry types, for example, with [`CREATE         TABLE`](create-table.md) or [`ALTER TABLE`](alter-table.md). Spatial columns are supported for [`MyISAM`](myisam-storage-engine.md), [`InnoDB`](innodb-storage-engine.md), [`NDB`](mysql-cluster.md), and [`ARCHIVE`](archive-storage-engine.md) tables. See also the notes about spatial indexes under [Section 11.4.9, “Creating Spatial Indexes”](creating-spatial-indexes.md).

- Use the [`CREATE TABLE`](create-table.md) statement to create a table with a spatial column:
	```
	CREATE TABLE geom (g GEOMETRY);
	```
- Use the [`ALTER TABLE`](alter-table.md) statement to add or drop a spatial column to or from an existing table:
	```
	ALTER TABLE geom ADD pt POINT;
	ALTER TABLE geom DROP pt;
	```