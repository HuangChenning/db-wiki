---
title: "12.16.6 Geometry Format Conversion Functions"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/gis-format-conversion-functions.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 12.16.6 Geometry Format Conversion Functions

MySQL supports the functions listed in this section for converting geometry values from internal geometry format to WKT or WKB format.

There are also functions to convert a string from WKT or WKB format to internal geometry format. See [Section 12.16.3, “Functions That Create Geometry Values from WKT Values”](gis-wkt-functions.md), and [Section 12.16.4, “Functions That Create Geometry Values from WKB Values”](gis-wkb-functions.md).

- ``AsBinary(*`g`*)``, ``AsWKB(*`g`*)``
	`ST_AsBinary()`, `ST_AsWKB()`, `AsBinary()`, and `AsWKB()` are synonyms. For more information, see the description of `ST_AsBinary()`.
	`AsBinary()` and `AsWKB()` are deprecated; expect them to be removed in a future MySQL release. Use `ST_AsBinary()` and `ST_AsWKB()` instead.
- ``AsText(*`g`*)``, ``AsWKT(*`g`*)``
	`ST_AsText()`, `ST_AsWKT()`, `AsText()`, and `AsWKT()` are synonyms. For more information, see the description of `ST_AsText()`.
	`AsText()` and `AsWKT()` are deprecated; expect them to be removed in a future MySQL release. Use `ST_AsText()` and `ST_AsWKT()` instead.
- ``ST_AsBinary(*`g`*)``, ``ST_AsWKB(*`g`*)``
	Converts a value in internal geometry format to its WKB representation and returns the binary result.
	If the argument is `NULL`, the return value is `NULL`. If the argument is not a syntactically well-formed geometry, an [`ER_GIS_INVALID_DATA`](https://docs.oracle.com/cd/E17952_01/mysql-errors-5.7-en/server-error-reference.html#error_er_gis_invalid_data) error occurs.
	```
	SELECT ST_AsBinary(g) FROM geom;
	```
	`ST_AsBinary()`, `ST_AsWKB()`, `AsBinary()`, and `AsWKB()` are synonyms.
- ``ST_AsText(*`g`*)``, ``ST_AsWKT(*`g`*)``
	Converts a value in internal geometry format to its WKT representation and returns the string result.
	If the argument is `NULL`, the return value is `NULL`. If the argument is not a syntactically well-formed geometry, an [`ER_GIS_INVALID_DATA`](https://docs.oracle.com/cd/E17952_01/mysql-errors-5.7-en/server-error-reference.html#error_er_gis_invalid_data) error occurs.
	```
	mysql> SET @g = 'LineString(1 1,2 2,3 3)';
	mysql> SELECT ST_AsText(ST_GeomFromText(@g));
	+--------------------------------+
	| ST_AsText(ST_GeomFromText(@g)) |
	+--------------------------------+
	| LINESTRING(1 1,2 2,3 3)        |
	+--------------------------------+
	```
	`ST_AsText()`, `ST_AsWKT()`, `AsText()`, and `AsWKT()` are synonyms.
	Output for `MultiPoint` values includes parentheses around each point. For example:
	```
	mysql> SET @mp = 'MULTIPOINT(1 1, 2 2, 3 3)';
	mysql> SELECT ST_AsText(ST_GeomFromText(@mp));
	+---------------------------------+
	| ST_AsText(ST_GeomFromText(@mp)) |
	+---------------------------------+
	| MULTIPOINT((1 1),(2 2),(3 3))   |
	+---------------------------------+
	```