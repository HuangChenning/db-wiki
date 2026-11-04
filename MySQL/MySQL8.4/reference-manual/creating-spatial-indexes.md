---
title: "13.4.10 Creating Spatial Indexes"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/creating-spatial-indexes.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 13.4.10 Creating Spatial Indexes

For `InnoDB` and `MyISAM` tables, MySQL can create spatial indexes using syntax similar to that for creating regular indexes, but using the `SPATIAL` keyword. Columns in spatial indexes must be declared `NOT NULL`. The following examples demonstrate how to create spatial indexes:

- With [`CREATE TABLE`](create-table.md):
	```
	CREATE TABLE geom (g GEOMETRY NOT NULL SRID 4326, SPATIAL INDEX(g));
	```
- With [`ALTER TABLE`](alter-table.md):
	```
	CREATE TABLE geom (g GEOMETRY NOT NULL SRID 4326);
	ALTER TABLE geom ADD SPATIAL INDEX(g);
	```
- With [`CREATE INDEX`](create-index.md):
	```
	CREATE TABLE geom (g GEOMETRY NOT NULL SRID 4326);
	CREATE SPATIAL INDEX g ON geom (g);
	```

`SPATIAL INDEX` creates an R-tree index. For storage engines that support nonspatial indexing of spatial columns, the engine creates a B-tree index. A B-tree index on spatial values is useful for exact-value lookups, but not for range scans.

The optimizer can use spatial indexes defined on columns that are SRID-restricted. For more information, see [Section 13.4.1, “Spatial Data Types”](spatial-type-overview.md), and [Section 10.3.3, “SPATIAL Index Optimization”](spatial-index-optimization.md).

For more information on indexing spatial columns, see [Section 15.1.15, “CREATE INDEX Statement”](create-index.md).

To drop spatial indexes, use [`ALTER         TABLE`](alter-table.md) or [`DROP INDEX`](drop-index.md):

- With [`ALTER TABLE`](alter-table.md):
	```
	ALTER TABLE geom DROP INDEX g;
	```
- With [`DROP INDEX`](drop-index.md):
	```
	DROP INDEX g ON geom;
	```

Example: Suppose that a table `geom` contains more than 32,000 geometries, which are stored in the column `g` of type `GEOMETRY`. The table also has an `AUTO_INCREMENT` column `fid` for storing object ID values.

```
mysql> DESCRIBE geom;
+-------+----------+------+-----+---------+----------------+
| Field | Type     | Null | Key | Default | Extra          |
+-------+----------+------+-----+---------+----------------+
| fid   | int(11)  |      | PRI | NULL    | auto_increment |
| g     | geometry |      |     |         |                |
+-------+----------+------+-----+---------+----------------+
2 rows in set (0.00 sec)

mysql> SELECT COUNT(*) FROM geom;
+----------+
| count(*) |
+----------+
|    32376 |
+----------+
1 row in set (0.00 sec)
```

To add a spatial index on the column `g`, use this statement:

```
mysql> ALTER TABLE geom ADD SPATIAL INDEX(g);
Query OK, 32376 rows affected (4.05 sec)
Records: 32376  Duplicates: 0  Warnings: 0
```