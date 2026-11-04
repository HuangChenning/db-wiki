---
title: "12.16.4 Functions That Create Geometry Values from WKB Values"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/gis-wkb-functions.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 12.16.4 Functions That Create Geometry Values from WKB Values

These functions take as arguments a [`BLOB`](blob.md) containing a Well-Known Binary (WKB) representation and, optionally, a spatial reference system identifier (SRID). They return the corresponding geometry.

`ST_GeomFromWKB()` accepts a WKB value of any geometry type as its first argument. Other functions provide type-specific construction functions for construction of geometry values of each geometry type.

These functions also accept geometry objects as returned by the functions in [Section 12.16.5, “MySQL-Specific Functions That Create Geometry Values”](gis-mysql-specific-functions.md). Thus, those functions may be used to provide the first argument to the functions in this section. However, as of MySQL 5.7.19, use of geometry arguments is deprecated and generates a warning. Geometry arguments are not accepted in MySQL 8.0. To migrate calls from using geometry arguments to using WKB arguments, follow these guidelines:

For a description of WKB format, see [Well-Known Binary (WKB) Format](gis-data-formats.md).

- Rewrite constructs such as `ST_GeomFromWKB(Point(0,           0))` as `Point(0, 0)`.
- Rewrite constructs such as `ST_GeomFromWKB(Point(0,           0), 4326)` as `ST_GeomFromWKB(ST_AsWKB(Point(0, 0)),           4326)`. (Alternatively, in MySQL 8.0, you can use `ST_SRID(Point(0, 0), 4326)`.)

- [``GeomCollFromWKB(*`wkb`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkb-functions.html#function_geomcollfromwkb), [``GeometryCollectionFromWKB(*`wkb`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkb-functions.html#function_geomcollfromwkb)
	`ST_GeomCollFromWKB()`, `ST_GeometryCollectionFromWKB()`, `GeomCollFromWKB()`, and `GeometryCollectionFromWKB()` are synonyms. For more information, see the description of `ST_GeomCollFromWKB()`.
	`GeomCollFromWKB()` and `GeometryCollectionFromWKB()` are deprecated; expect them to be removed in a future MySQL release. Use `ST_GeomCollFromWKB()` and `ST_GeometryCollectionFromWKB()` instead.
- [``GeomFromWKB(*`wkb`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkb-functions.html#function_geomfromwkb), [``GeometryFromWKB(*`wkb`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkb-functions.html#function_geomfromwkb)
	`ST_GeomFromWKB()`, `ST_GeometryFromWKB()`, `GeomFromWKB()`, and `GeometryFromWKB()` are synonyms. For more information, see the description of `ST_GeomFromWKB()`.
	`GeomFromWKB()` and `GeometryFromWKB()` are deprecated; expect them to be removed in a future MySQL release. Use `ST_GeomFromWKB()` and `ST_GeometryFromWKB()` instead.
- [``LineFromWKB(*`wkb`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkb-functions.html#function_linefromwkb), [``LineStringFromWKB(*`wkb`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkb-functions.html#function_linefromwkb)
	`ST_LineFromWKB()`, `ST_LineStringFromWKB()`, `LineFromWKB()`, and `LineStringFromWKB()` are synonyms. For more information, see the description of `ST_LineFromWKB()`.
	`LineFromWKB()` and `LineStringFromWKB()` are deprecated; expect them to be removed in a future MySQL release. Use `ST_LineFromWKB()` and `ST_LineStringFromWKB()` instead.
- [``MLineFromWKB(*`wkb`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkb-functions.html#function_mlinefromwkb), [``MultiLineStringFromWKB(*`wkb`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkb-functions.html#function_mlinefromwkb)
	`ST_MLineFromWKB()`, `ST_MultiLineStringFromWKB()`, `MLineFromWKB()`, and `MultiLineStringFromWKB()` are synonyms. For more information, see the description of `ST_MLineFromWKB()`.
	`MLineFromWKB()` and `MultiLineStringFromWKB()` are deprecated; expect them to be removed in a future MySQL release. Use `ST_MLineFromWKB()` and `ST_MultiLineStringFromWKB()` instead.
- [``MPointFromWKB(*`wkb`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkb-functions.html#function_mpointfromwkb), [``MultiPointFromWKB(*`wkb`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkb-functions.html#function_mpointfromwkb)
	`ST_MPointFromWKB()`, `ST_MultiPointFromWKB()`, `MPointFromWKB()`, and `MultiPointFromWKB()` are synonyms. For more information, see the description of `ST_MPointFromWKB()`.
	`MPointFromWKB()` and `MultiPointFromWKB()` are deprecated; expect them to be removed in a future MySQL release. Use `ST_MPointFromWKB()` and `ST_MultiPointFromWKB()` instead.
- [``MPolyFromWKB(*`wkb`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkb-functions.html#function_mpolyfromwkb), [``MultiPolygonFromWKB(*`wkb`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkb-functions.html#function_mpolyfromwkb)
	`ST_MPolyFromWKB()`, `ST_MultiPolygonFromWKB()`, `MPolyFromWKB()`, and `MultiPolygonFromWKB()` are synonyms. For more information, see the description of `ST_MPolyFromWKB()`.
	`MPolyFromWKB()` and `MultiPolygonFromWKB()` are deprecated; expect them to be removed in a future MySQL release. Use `ST_MPolyFromWKB()` and `ST_MultiPolygonFromWKB()` instead.
- [``PointFromWKB(*`wkb`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkb-functions.html#function_pointfromwkb)
	`ST_PointFromWKB()` and `PointFromWKB()` are synonyms. For more information, see the description of `ST_PointFromWKB()`.
	`PointFromWKB()` is deprecated; expect it to be removed in a future MySQL release. Use `ST_PointFromWKB()` instead.
- [``PolyFromWKB(*`wkb`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkb-functions.html#function_polyfromwkb), [``PolygonFromWKB(*`wkb`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkb-functions.html#function_polyfromwkb)
	`ST_PolyFromWKB()`, `ST_PolygonFromWKB()`, `PolyFromWKB()`, and `PolygonFromWKB()` are synonyms. For more information, see the description of `ST_PolyFromWKB()`.
	`PolyFromWKB()` and `PolygonFromWKB()` are deprecated; expect them to be removed in a future MySQL release. Use `ST_PolyFromWKB()` and `ST_PolygonFromWKB()` instead.
- [``ST_GeomCollFromWKB(*`wkb`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkb-functions.html#function_st-geomcollfromwkb), [``ST_GeometryCollectionFromWKB(*`wkb`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkb-functions.html#function_st-geomcollfromwkb)
	Constructs a `GeometryCollection` value using its WKB representation and SRID.
	The result is `NULL` if the WKB or SRID argument is `NULL`.
	`ST_GeomCollFromWKB()`, `ST_GeometryCollectionFromWKB()`, `GeomCollFromWKB()`, and `GeometryCollectionFromWKB()` are synonyms.
- [``ST_GeomFromWKB(*`wkb`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkb-functions.html#function_st-geomfromwkb), [``ST_GeometryFromWKB(*`wkb`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkb-functions.html#function_st-geomfromwkb)
	Constructs a geometry value of any type using its WKB representation and SRID.
	The result is `NULL` if the WKB or SRID argument is `NULL`.
	`ST_GeomFromWKB()`, `ST_GeometryFromWKB()`, `GeomFromWKB()`, and `GeometryFromWKB()` are synonyms.
- [``ST_LineFromWKB(*`wkb`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkb-functions.html#function_st-linefromwkb), [``ST_LineStringFromWKB(*`wkb`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkb-functions.html#function_st-linefromwkb)
	Constructs a `LineString` value using its WKB representation and SRID.
	The result is `NULL` if the WKB or SRID argument is `NULL`.
	`ST_LineFromWKB()`, `ST_LineStringFromWKB()`, `LineFromWKB()`, and `LineStringFromWKB()` are synonyms.
- [``ST_MLineFromWKB(*`wkb`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkb-functions.html#function_st-mlinefromwkb), [``ST_MultiLineStringFromWKB(*`wkb`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkb-functions.html#function_st-mlinefromwkb)
	Constructs a `MultiLineString` value using its WKB representation and SRID.
	The result is `NULL` if the WKB or SRID argument is `NULL`.
	`ST_MLineFromWKB()`, `ST_MultiLineStringFromWKB()`, `MLineFromWKB()`, and `MultiLineStringFromWKB()` are synonyms.
- [``ST_MPointFromWKB(*`wkb`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkb-functions.html#function_st-mpointfromwkb), [``ST_MultiPointFromWKB(*`wkb`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkb-functions.html#function_st-mpointfromwkb)
	Constructs a `MultiPoint` value using its WKB representation and SRID.
	The result is `NULL` if the WKB or SRID argument is `NULL`.
	`ST_MPointFromWKB()`, `ST_MultiPointFromWKB()`, `MPointFromWKB()`, and `MultiPointFromWKB()` are synonyms.
- [``ST_MPolyFromWKB(*`wkb`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkb-functions.html#function_st-mpolyfromwkb), [``ST_MultiPolygonFromWKB(*`wkb`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkb-functions.html#function_st-mpolyfromwkb)
	Constructs a `MultiPolygon` value using its WKB representation and SRID.
	The result is `NULL` if the WKB or SRID argument is `NULL`.
	`ST_MPolyFromWKB()`, `ST_MultiPolygonFromWKB()`, `MPolyFromWKB()`, and `MultiPolygonFromWKB()` are synonyms.
- [``ST_PointFromWKB(*`wkb`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkb-functions.html#function_st-pointfromwkb)
	Constructs a `Point` value using its WKB representation and SRID.
	The result is `NULL` if the WKB or SRID argument is `NULL`.
	`ST_PointFromWKB()` and `PointFromWKB()` are synonyms.
- [``ST_PolyFromWKB(*`wkb`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkb-functions.html#function_st-polyfromwkb), [``ST_PolygonFromWKB(*`wkb`*           [, *`srid`*])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/gis-wkb-functions.html#function_st-polyfromwkb)
	Constructs a `Polygon` value using its WKB representation and SRID.
	The result is `NULL` if the WKB or SRID argument is `NULL`.
	`ST_PolyFromWKB()`, `ST_PolygonFromWKB()`, `PolyFromWKB()`, and `PolygonFromWKB()` are synonyms.