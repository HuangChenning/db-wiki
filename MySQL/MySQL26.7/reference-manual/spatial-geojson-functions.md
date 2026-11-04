---
title: "MySQL :: MySQL 26.7 Reference Manual :: 14.16.11 Spatial GeoJSON Functions"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/spatial-geojson-functions.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 14.16.11 Spatial GeoJSON Functions

This section describes functions for converting between GeoJSON documents and spatial values. GeoJSON is an open standard for encoding geometric/geographical features. For more information, see [http://geojson.org](http://geojson.org/). The functions discussed here follow GeoJSON specification revision 1.0.

GeoJSON supports the same geometric/geographic data types that MySQL supports. Feature and FeatureCollection objects are not supported, except that geometry objects are extracted from them. CRS support is limited to values that identify an SRID.

MySQL also supports a native [`JSON`](json.md) data type and a set of SQL functions to enable operations on JSON values. For more information, see [Section 13.5, “The JSON Data Type”](json.md), and [Section 14.17, “JSON Functions”](json-functions.md).

- [``ST_AsGeoJSON(*`g`*           [, *`max_dec_digits`* [,           *`options`*]])``](https://dev.mysql.com/doc/refman/26.7/en/spatial-geojson-functions.html#function_st-asgeojson)
	Generates a GeoJSON object from the geometry *`g`*. The object string has the connection character set and collation.
	If any argument is `NULL`, the return value is `NULL`. If any non- `NULL` argument is invalid, an error occurs.
	*`max_dec_digits`*, if specified, limits the number of decimal digits for coordinates and causes rounding of output. If not specified, this argument defaults to its maximum value of 2 <sup>32</sup> − 1. The minimum is 0.
	*`options`*, if specified, is a bitmask. The following table shows the permitted flag values. If the geometry argument has an SRID of 0, no CRS object is produced even for those flag values that request one.
	| Flag Value | Meaning |
	| --- | --- |
	| 0 | No options. This is the default if *`options`* is not specified. |
	| 1 | Add a bounding box to the output. |
	| 2 | Add a short-format CRS URN to the output. The default format is a short format (``EPSG:*`srid`*``). If the SRID is 0, the CRS URN is `MySQL:0`. |
	| 4 | Add a long-format CRS URN (``urn:ogc:def:crs:EPSG::*`srid`*``). This flag overrides flag 2. For example, option values of 5 and 7 mean the same (add a bounding box and a long-format CRS URN). If the SRID is 0, the CRS URN is `urn:ogc:def:crs:MySQL::0`. |
	```sql
	mysql> SELECT ST_AsGeoJSON(ST_GeomFromText('POINT(11.11111 12.22222)'),2);
	+-------------------------------------------------------------+
	| ST_AsGeoJSON(ST_GeomFromText('POINT(11.11111 12.22222)'),2) |
	+-------------------------------------------------------------+
	| {"type": "Point", "coordinates": [11.11, 12.22]}            |
	+-------------------------------------------------------------+
	```
- [``ST_GeomFromGeoJSON(*`str`*           [, *`options`* [,           *`srid`*]])``](https://dev.mysql.com/doc/refman/26.7/en/spatial-geojson-functions.html#function_st-geomfromgeojson)
	Parses a string *`str`* representing a GeoJSON object and returns a geometry.
	If any argument is `NULL`, the return value is `NULL`. If any non- `NULL` argument is invalid, an error occurs.
	*`options`*, if given, describes how to handle GeoJSON documents that contain geometries with coordinate dimensions higher than 2. The following table shows the permitted *`options`* values.
	| Option Value | Meaning |
	| --- | --- |
	| 1 | Reject the document and produce an error. This is the default if *`options`* is not specified. |
	| 2, 3, 4 | Accept the document and strip off the coordinates for higher coordinate dimensions. |
	*`options`* values of 2, 3, and 4 currently produce the same effect. If geometries with coordinate dimensions higher than 2 are supported in the future, you can expect these values to produce different effects.
	The *`srid`* argument, if given, must be a 32-bit unsigned integer. If not given, the geometry return value has an SRID of 4326.
	If *`srid`* refers to an undefined spatial reference system (SRS), an [`ER_SRS_NOT_FOUND`](https://dev.mysql.com/doc/mysql-errors/26.7/en/server-error-reference.html#error_er_srs_not_found) error occurs.
	For geographic SRS geometry arguments, if any argument has a longitude or latitude that is out of range, an error occurs:
	- If a longitude value is not in the range (−180, 180\], an [`ER_LONGITUDE_OUT_OF_RANGE`](https://dev.mysql.com/doc/mysql-errors/26.7/en/server-error-reference.html#error_er_longitude_out_of_range) error occurs.
	- If a latitude value is not in the range \[−90, 90\], an [`ER_LATITUDE_OUT_OF_RANGE`](https://dev.mysql.com/doc/mysql-errors/26.7/en/server-error-reference.html#error_er_latitude_out_of_range) error occurs.
	Ranges shown are in degrees. If an SRS uses another unit, the range uses the corresponding values in its unit. The exact range limits deviate slightly due to floating-point arithmetic.
	GeoJSON geometry, feature, and feature collection objects may have a `crs` property. The parsing function parses named CRS URNs in the ``urn:ogc:def:crs:EPSG::*`srid`*`` and ``EPSG:*`srid`*`` namespaces, but not CRSs given as link objects. Also, `urn:ogc:def:crs:OGC:1.3:CRS84` is recognized as SRID 4326. If an object has a CRS that is not understood, an error occurs, with the exception that if the optional *`srid`* argument is given, any CRS is ignored even if it is invalid.
	If a `crs` member that specifies an SRID different from the top-level object SRID is found at a lower level of the GeoJSON document, an [`ER_INVALID_GEOJSON_CRS_NOT_TOP_LEVEL`](https://dev.mysql.com/doc/mysql-errors/26.7/en/server-error-reference.html#error_er_invalid_geojson_crs_not_top_level) error occurs.
	As specified in the GeoJSON specification, parsing is case-sensitive for the `type` member of the GeoJSON input (`Point`, `LineString`, and so forth). The specification is silent regarding case sensitivity for other parsing, which in MySQL is not case-sensitive.
	This example shows the parsing result for a simple GeoJSON object. Observe that the order of coordinates depends on the SRID used.
	```sql
	mysql> SET @json = '{ "type": "Point", "coordinates": [102.0, 0.0]}';
	mysql> SELECT ST_AsText(ST_GeomFromGeoJSON(@json));
	+--------------------------------------+
	| ST_AsText(ST_GeomFromGeoJSON(@json)) |
	+--------------------------------------+
	| POINT(0 102)                         |
	+--------------------------------------+
	mysql> SELECT ST_SRID(ST_GeomFromGeoJSON(@json));
	+------------------------------------+
	| ST_SRID(ST_GeomFromGeoJSON(@json)) |
	+------------------------------------+
	|                               4326 |
	+------------------------------------+
	mysql> SELECT ST_AsText(ST_SRID(ST_GeomFromGeoJSON(@json),0));
	+-------------------------------------------------+
	| ST_AsText(ST_SRID(ST_GeomFromGeoJSON(@json),0)) |
	+-------------------------------------------------+
	| POINT(102 0)                                    |
	+-------------------------------------------------+
	```