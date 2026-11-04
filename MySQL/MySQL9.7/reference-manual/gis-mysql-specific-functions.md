---
title: "14.16.5 MySQL-Specific Functions That Create Geometry Values"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/gis-mysql-specific-functions.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 14.16.5 MySQL-Specific Functions That Create Geometry Values

MySQL provides a set of useful nonstandard functions for creating geometry values. The functions described in this section are MySQL extensions to the OpenGIS specification.

These functions produce geometry objects from either WKB values or geometry objects as arguments. If any argument is not a proper WKB or geometry representation of the proper object type, the return value is `NULL`.

For example, you can insert the geometry return value from `Point()` directly into a `POINT` column:

```
INSERT INTO t1 (pt_col) VALUES(Point(1,2));
```

- [``GeomCollection(*`g`*           [, *`g`*] ...)``](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/gis-mysql-specific-functions.html#function_geomcollection)
	Constructs a `GeomCollection` value from the geometry arguments.
	`GeomCollection()` returns all the proper geometries contained in the arguments even if a nonsupported geometry is present.
	`GeomCollection()` with no arguments is permitted as a way to create an empty geometry. Also, functions such as [`ST_GeomFromText()`](gis-wkt-functions.md) that accept WKT geometry collection arguments understand both OpenGIS `'GEOMETRYCOLLECTION EMPTY'` standard syntax and MySQL `'GEOMETRYCOLLECTION()'` nonstandard syntax.
	`GeomCollection()` and `GeometryCollection()` are synonymous, with `GeomCollection()` the preferred function.
- [``GeometryCollection(*`g`*           [, *`g`*] ...)``](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/gis-mysql-specific-functions.html#function_geometrycollection)
	Constructs a `GeomCollection` value from the geometry arguments.
	`GeometryCollection()` returns all the proper geometries contained in the arguments even if a nonsupported geometry is present.
	`GeometryCollection()` with no arguments is permitted as a way to create an empty geometry. Also, functions such as [`ST_GeomFromText()`](gis-wkt-functions.md) that accept WKT geometry collection arguments understand both OpenGIS `'GEOMETRYCOLLECTION EMPTY'` standard syntax and MySQL `'GEOMETRYCOLLECTION()'` nonstandard syntax.
	`GeomCollection()` and `GeometryCollection()` are synonymous, with `GeomCollection()` the preferred function.
- [``LineString(*`pt`*           [, *`pt`*] ...)``](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/gis-mysql-specific-functions.html#function_linestring)
	Constructs a `LineString` value from a number of `Point` or WKB `Point` arguments. If the number of arguments is less than two, the return value is `NULL`.
- [``MultiLineString(*`ls`*           [, *`ls`*] ...)``](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/gis-mysql-specific-functions.html#function_multilinestring)
	Constructs a `MultiLineString` value using `LineString` or WKB `LineString` arguments.
- [``MultiPoint(*`pt`*           [, *`pt2`*] ...)``](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/gis-mysql-specific-functions.html#function_multipoint)
	Constructs a `MultiPoint` value using `Point` or WKB `Point` arguments.
- [``MultiPolygon(*`poly`*           [, *`poly`*] ...)``](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/gis-mysql-specific-functions.html#function_multipolygon)
	Constructs a `MultiPolygon` value from a set of `Polygon` or WKB `Polygon` arguments.
- ``Point(*`x`*,           *`y`*)``
	Constructs a `Point` using its coordinates.
- [``Polygon(*`ls`* [,           *`ls`*] ...)``](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/gis-mysql-specific-functions.html#function_polygon)
	Constructs a `Polygon` value from a number of `LineString` or WKB `LineString` arguments. If any argument does not represent a `LinearRing` (that is, not a closed and simple `LineString`), the return value is `NULL`.