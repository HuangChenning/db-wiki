---
title: "12.16.3 Functions That Create Geometry Values from WKT Values"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/gis-wkt-functions.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 12.16.3 Functions That Create Geometry Values from WKT Values

These functions take as arguments a Well-Known Text (WKT) representation and, optionally, a spatial reference system identifier (SRID). They return the corresponding geometry.

`ST_GeomFromText()` accepts a WKT value of any geometry type as its first argument. Other functions provide type-specific construction functions for construction of geometry values of each geometry type.

For a description of WKT format, see [Well-Known Text (WKT) Format](gis-data-formats.md).

- [``GeomCollFromText(*`wkt`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkt-functions.html#function_geomcollfromtext), [``GeometryCollectionFromText(*`wkt`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkt-functions.html#function_geomcollfromtext)
	`ST_GeomCollFromText()`, `ST_GeometryCollectionFromText()`, `ST_GeomCollFromTxt()`, `GeomCollFromText()`, and `GeometryCollectionFromText()` are synonyms. For more information, see the description of `ST_GeomCollFromText()`.
	`GeomCollFromText()` and `GeometryCollectionFromText()` are deprecated; expect them to be removed in a future MySQL release. Use `ST_GeomCollFromText()` and `ST_GeometryCollectionFromText()` instead.
- [``GeomFromText(*`wkt`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkt-functions.html#function_geomfromtext), [``GeometryFromText(*`wkt`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkt-functions.html#function_geomfromtext)
	`ST_GeomFromText()`, `ST_GeometryFromText()`, `GeomFromText()`, and `GeometryFromText()` are synonyms. For more information, see the description of `ST_GeomFromText()`.
	`GeomFromText()` and `GeometryFromText()` are deprecated; expect them to be removed in a future MySQL release. Use `ST_GeomFromText()` and `ST_GeometryFromText()` instead.
- [``LineFromText(*`wkt`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkt-functions.html#function_linefromtext), [``LineStringFromText(*`wkt`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkt-functions.html#function_linefromtext)
	`ST_LineFromText()`, `ST_LineStringFromText()`, `LineFromText()`, and `LineStringFromText()` are synonyms. For more information, see the description of `ST_LineFromText()`.
	`LineFromText()` and `LineStringFromText()` are deprecated; expect them to be removed in a future MySQL release. Use `ST_LineFromText()` and `ST_LineStringFromText()` instead.
- [``MLineFromText(*`wkt`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkt-functions.html#function_mlinefromtext), [``MultiLineStringFromText(*`wkt`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkt-functions.html#function_mlinefromtext)
	`ST_MLineFromText()`, `ST_MultiLineStringFromText()`, `MLineFromText()`, and `MultiLineStringFromText()` are synonyms. For more information, see the description of `ST_MLineFromText()`.
	`MLineFromText()` and `MultiLineStringFromText()` are deprecated; expect them to be removed in a future MySQL release. Use `ST_MLineFromText()` and `ST_MultiLineStringFromText()` instead.
- [``MPointFromText(*`wkt`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkt-functions.html#function_mpointfromtext), [``MultiPointFromText(*`wkt`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkt-functions.html#function_mpointfromtext)
	`ST_MPointFromText()`, `ST_MultiPointFromText()`, `MPointFromText()`, and `MultiPointFromText()` are synonyms. For more information, see the description of `ST_MPointFromText()`.
	`MPointFromText()` and `MultiPointFromText()` are deprecated; expect them to be removed in a future MySQL release. Use `ST_MPointFromText()` and `ST_MultiPointFromText()` instead.
- [``MPolyFromText(*`wkt`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkt-functions.html#function_mpolyfromtext), [``MultiPolygonFromText(*`wkt`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkt-functions.html#function_mpolyfromtext)
	`ST_MPolyFromText()`, `ST_MultiPolygonFromText()`, `MPolyFromText()`, and `MultiPolygonFromText()` are synonyms. For more information, see the description of `ST_MPolyFromText()`.
	`MPolyFromText()` and `MultiPolygonFromText()` are deprecated; expect them to be removed in a future MySQL release. Use `ST_MPolyFromText()` and `ST_MultiPolygonFromText()` instead.
- [``PointFromText(*`wkt`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkt-functions.html#function_pointfromtext)
	`ST_PointFromText()` and `PointFromText()` are synonyms. For more information, see the description of `ST_PointFromText()`.
	`PointFromText()` is deprecated; expect it to be removed in a future MySQL release. Use `ST_PointFromText()` instead.
- [``PolyFromText(*`wkt`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkt-functions.html#function_polyfromtext), [``PolygonFromText(*`wkt`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkt-functions.html#function_polyfromtext)
	`ST_PolyFromText()`, `ST_PolygonFromText()`, `PolyFromText()`, and `PolygonFromText()` are synonyms. For more information, see the description of `ST_PolyFromText()`.
	`PolyFromText()` and `PolygonFromText()` are deprecated; expect them to be removed in a future MySQL release. Use `ST_PolyFromText()` and `ST_PolygonFromText()` instead.
- [``ST_GeomCollFromText(*`wkt`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkt-functions.html#function_st-geomcollfromtext), [``ST_GeometryCollectionFromText(*`wkt`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkt-functions.html#function_st-geomcollfromtext), [``ST_GeomCollFromTxt(*`wkt`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkt-functions.html#function_st-geomcollfromtext)
	Constructs a `GeometryCollection` value using its WKT representation and SRID.
	If the geometry argument is `NULL` or not a syntactically well-formed geometry, or if the SRID argument is `NULL`, the return value is `NULL`.
	```
	mysql> SET @g = "MULTILINESTRING((10 10, 11 11), (9 9, 10 10))";
	mysql> SELECT ST_AsText(ST_GeomCollFromText(@g));
	+--------------------------------------------+
	| ST_AsText(ST_GeomCollFromText(@g))         |
	+--------------------------------------------+
	| MULTILINESTRING((10 10,11 11),(9 9,10 10)) |
	+--------------------------------------------+
	```
	`ST_GeomCollFromText()`, `ST_GeometryCollectionFromText()`, `ST_GeomCollFromTxt()`, `GeomCollFromText()`, and `GeometryCollectionFromText()` are synonyms.
- [``ST_GeomFromText(*`wkt`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkt-functions.html#function_st-geomfromtext), [``ST_GeometryFromText(*`wkt`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkt-functions.html#function_st-geomfromtext)
	Constructs a geometry value of any type using its WKT representation and SRID.
	If the geometry argument is `NULL` or not a syntactically well-formed geometry, or if the SRID argument is `NULL`, the return value is `NULL`.
	`ST_GeomFromText()`, `ST_GeometryFromText()`, `GeomFromText()`, and `GeometryFromText()` are synonyms.
- [``ST_LineFromText(*`wkt`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkt-functions.html#function_st-linefromtext), [``ST_LineStringFromText(*`wkt`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkt-functions.html#function_st-linefromtext)
	Constructs a `LineString` value using its WKT representation and SRID.
	If the geometry argument is `NULL` or not a syntactically well-formed geometry, or if the SRID argument is `NULL`, the return value is `NULL`.
	`ST_LineFromText()`, `ST_LineStringFromText()`, `LineFromText()`, and `LineStringFromText()` are synonyms.
- [``ST_MLineFromText(*`wkt`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkt-functions.html#function_st-mlinefromtext), [``ST_MultiLineStringFromText(*`wkt`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkt-functions.html#function_st-mlinefromtext)
	Constructs a `MultiLineString` value using its WKT representation and SRID.
	If the geometry argument is `NULL` or not a syntactically well-formed geometry, or if the SRID argument is `NULL`, the return value is `NULL`.
	`ST_MLineFromText()`, `ST_MultiLineStringFromText()`, `MLineFromText()`, and `MultiLineStringFromText()` are synonyms.
- [``ST_MPointFromText(*`wkt`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkt-functions.html#function_st-mpointfromtext), [``ST_MultiPointFromText(*`wkt`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkt-functions.html#function_st-mpointfromtext)
	Constructs a `MultiPoint` value using its WKT representation and SRID.
	If the geometry argument is `NULL` or not a syntactically well-formed geometry, or if the SRID argument is `NULL`, the return value is `NULL`.
	Functions such as `ST_MPointFromText()` and `ST_GeomFromText()` that accept WKT-format representations of `MultiPoint` values permit individual points within values to be surrounded by parentheses. For example, both of the following function calls are valid:
	```
	ST_MPointFromText('MULTIPOINT (1 1, 2 2, 3 3)')
	ST_MPointFromText('MULTIPOINT ((1 1), (2 2), (3 3))')
	```
	`ST_MPointFromText()`, `ST_MultiPointFromText()`, `MPointFromText()`, and `MultiPointFromText()` are synonyms.
- [``ST_MPolyFromText(*`wkt`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkt-functions.html#function_st-mpolyfromtext), [``ST_MultiPolygonFromText(*`wkt`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkt-functions.html#function_st-mpolyfromtext)
	Constructs a `MultiPolygon` value using its WKT representation and SRID.
	If the geometry argument is `NULL` or not a syntactically well-formed geometry, or if the SRID argument is `NULL`, the return value is `NULL`.
	`ST_MPolyFromText()`, `ST_MultiPolygonFromText()`, `MPolyFromText()`, and `MultiPolygonFromText()` are synonyms.
- [``ST_PointFromText(*`wkt`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkt-functions.html#function_st-pointfromtext)
	Constructs a `Point` value using its WKT representation and SRID.
	If the geometry argument is `NULL` or not a syntactically well-formed geometry, or if the SRID argument is `NULL`, the return value is `NULL`.
	`ST_PointFromText()` and `PointFromText()` are synonyms.
- [``ST_PolyFromText(*`wkt`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkt-functions.html#function_st-polyfromtext), [``ST_PolygonFromText(*`wkt`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkt-functions.html#function_st-polyfromtext)
	Constructs a `Polygon` value using its WKT representation and SRID.
	If the geometry argument is `NULL` or not a syntactically well-formed geometry, or if the SRID argument is `NULL`, the return value is `NULL`.
	`ST_PolyFromText()`, `ST_PolygonFromText()`, `PolyFromText()`, and `PolygonFromText()` are synonyms.