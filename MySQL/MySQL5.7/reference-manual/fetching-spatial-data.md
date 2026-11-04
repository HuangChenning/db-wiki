---
title: "11.4.7 Fetching Spatial Data"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/fetching-spatial-data.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 11.4.7 Fetching Spatial Data

Geometry values stored in a table can be fetched in internal format. You can also convert them to WKT or WKB format.

- Fetching spatial data in internal format:
	Fetching geometry values using internal format can be useful in table-to-table transfers:
	```
	CREATE TABLE geom2 (g GEOMETRY) SELECT g FROM geom;
	```
- Fetching spatial data in WKT format:
	The [`ST_AsText()`](gis-format-conversion-functions.md) function converts a geometry from internal format to a WKT string.
	```
	SELECT ST_AsText(g) FROM geom;
	```
- Fetching spatial data in WKB format:
	The [`ST_AsBinary()`](gis-format-conversion-functions.md) function converts a geometry from internal format to a [`BLOB`](blob.md) containing the WKB value.
	```
	SELECT ST_AsBinary(g) FROM geom;
	```