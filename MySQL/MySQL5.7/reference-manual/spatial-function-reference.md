---
title: "12.16.1 Spatial Function Reference"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/spatial-function-reference.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 12.16.1 Spatial Function Reference

The following table lists each spatial function and provides a short description of each one.

**Table 12.21 Spatial Functions**

| Name | Description | Deprecated |
| --- | --- | --- |
| [`Area()`](gis-polygon-property-functions.md) | Return Polygon or MultiPolygon area | Yes |
| [`AsBinary()`, `AsWKB()`](gis-format-conversion-functions.md) | Convert from internal geometry format to WKB | Yes |
| [`AsText()`, `AsWKT()`](gis-format-conversion-functions.md) | Convert from internal geometry format to WKT | Yes |
| [`Buffer()`](spatial-operator-functions.md) | Return geometry of points within given distance from geometry | Yes |
| [`Centroid()`](gis-polygon-property-functions.md) | Return centroid as a point | Yes |
| [`Contains()`](spatial-relation-functions-mbr.md) | Whether MBR of one geometry contains MBR of another | Yes |
| [`ConvexHull()`](spatial-operator-functions.md) | Return convex hull of geometry | Yes |
| [`Crosses()`](spatial-relation-functions-object-shapes.md) | Whether one geometry crosses another | Yes |
| [`Dimension()`](gis-general-property-functions.md) | Dimension of geometry | Yes |
| [`Disjoint()`](spatial-relation-functions-mbr.md) | Whether MBRs of two geometries are disjoint | Yes |
| [`EndPoint()`](gis-linestring-property-functions.md) | End Point of LineString | Yes |
| [`Envelope()`](gis-general-property-functions.md) | Return MBR of geometry | Yes |
| [`Equals()`](spatial-relation-functions-mbr.md) | Whether MBRs of two geometries are equal | Yes |
| [`ExteriorRing()`](gis-polygon-property-functions.md) | Return exterior ring of Polygon | Yes |
| [`GeomCollFromText()`, `GeometryCollectionFromText()`](gis-wkt-functions.md) | Return geometry collection from WKT | Yes |
| [`GeomCollFromWKB()`, `GeometryCollectionFromWKB()`](gis-wkb-functions.md) | Return geometry collection from WKB | Yes |
| [`GeometryCollection()`](gis-mysql-specific-functions.md) | Construct geometry collection from geometries |  |
| [`GeometryN()`](gis-geometrycollection-property-functions.md) | Return N-th geometry from geometry collection | Yes |
| [`GeometryType()`](gis-general-property-functions.md) | Return name of geometry type | Yes |
| [`GeomFromText()`, `GeometryFromText()`](gis-wkt-functions.md) | Return geometry from WKT | Yes |
| [`GeomFromWKB()`, `GeometryFromWKB()`](gis-wkb-functions.md) | Return geometry from WKB | Yes |
| [`GLength()`](gis-linestring-property-functions.md) | Return length of LineString | Yes |
| [`InteriorRingN()`](gis-polygon-property-functions.md) | Return N-th interior ring of Polygon | Yes |
| [`Intersects()`](spatial-relation-functions-mbr.md) | Whether MBRs of two geometries intersect | Yes |
| [`IsClosed()`](gis-linestring-property-functions.md) | Whether a geometry is closed and simple | Yes |
| [`IsEmpty()`](gis-general-property-functions.md) | Whether a geometry is empty | Yes |
| [`IsSimple()`](gis-general-property-functions.md) | Whether a geometry is simple | Yes |
| [`LineFromText()`, `LineStringFromText()`](gis-wkt-functions.md) | Construct LineString from WKT | Yes |
| [`LineFromWKB()`, `LineStringFromWKB()`](gis-wkb-functions.md) | Construct LineString from WKB | Yes |
| [`LineString()`](gis-mysql-specific-functions.md) | Construct LineString from Point values |  |
| [`MBRContains()`](spatial-relation-functions-mbr.md) | Whether MBR of one geometry contains MBR of another |  |
| [`MBRCoveredBy()`](spatial-relation-functions-mbr.md) | Whether one MBR is covered by another |  |
| [`MBRCovers()`](spatial-relation-functions-mbr.md) | Whether one MBR covers another |  |
| [`MBRDisjoint()`](spatial-relation-functions-mbr.md) | Whether MBRs of two geometries are disjoint |  |
| [`MBREqual()`](spatial-relation-functions-mbr.md) | Whether MBRs of two geometries are equal | Yes |
| [`MBREquals()`](spatial-relation-functions-mbr.md) | Whether MBRs of two geometries are equal |  |
| [`MBRIntersects()`](spatial-relation-functions-mbr.md) | Whether MBRs of two geometries intersect |  |
| [`MBROverlaps()`](spatial-relation-functions-mbr.md) | Whether MBRs of two geometries overlap |  |
| [`MBRTouches()`](spatial-relation-functions-mbr.md) | Whether MBRs of two geometries touch |  |
| [`MBRWithin()`](spatial-relation-functions-mbr.md) | Whether MBR of one geometry is within MBR of another |  |
| [`MLineFromText()`, `MultiLineStringFromText()`](gis-wkt-functions.md) | Construct MultiLineString from WKT | Yes |
| [`MLineFromWKB()`, `MultiLineStringFromWKB()`](gis-wkb-functions.md) | Construct MultiLineString from WKB | Yes |
| [`MPointFromText()`, `MultiPointFromText()`](gis-wkt-functions.md) | Construct MultiPoint from WKT | Yes |
| [`MPointFromWKB()`, `MultiPointFromWKB()`](gis-wkb-functions.md) | Construct MultiPoint from WKB | Yes |
| [`MPolyFromText()`, `MultiPolygonFromText()`](gis-wkt-functions.md) | Construct MultiPolygon from WKT | Yes |
| [`MPolyFromWKB()`, `MultiPolygonFromWKB()`](gis-wkb-functions.md) | Construct MultiPolygon from WKB | Yes |
| [`MultiLineString()`](gis-mysql-specific-functions.md) | Contruct MultiLineString from LineString values |  |
| [`MultiPoint()`](gis-mysql-specific-functions.md) | Construct MultiPoint from Point values |  |
| [`MultiPolygon()`](gis-mysql-specific-functions.md) | Construct MultiPolygon from Polygon values |  |
| [`NumGeometries()`](gis-geometrycollection-property-functions.md) | Return number of geometries in geometry collection | Yes |
| [`NumInteriorRings()`](gis-polygon-property-functions.md) | Return number of interior rings in Polygon | Yes |
| [`NumPoints()`](gis-linestring-property-functions.md) | Return number of points in LineString | Yes |
| [`Overlaps()`](spatial-relation-functions-mbr.md) | Whether MBRs of two geometries overlap | Yes |
| [`Point()`](gis-mysql-specific-functions.md) | Construct Point from coordinates |  |
| [`PointFromText()`](gis-wkt-functions.md) | Construct Point from WKT | Yes |
| [`PointFromWKB()`](gis-wkb-functions.md) | Construct Point from WKB | Yes |
| [`PointN()`](gis-linestring-property-functions.md) | Return N-th point from LineString | Yes |
| [`PolyFromText()`, `PolygonFromText()`](gis-wkt-functions.md) | Construct Polygon from WKT | Yes |
| [`PolyFromWKB()`, `PolygonFromWKB()`](gis-wkb-functions.md) | Construct Polygon from WKB | Yes |
| [`Polygon()`](gis-mysql-specific-functions.md) | Construct Polygon from LineString arguments |  |
| [`Distance()`](spatial-relation-functions-object-shapes.md) | The distance of one geometry from another | Yes |
| [`SRID()`](gis-general-property-functions.md) | Return spatial reference system ID for geometry | Yes |
| [`ST_Area()`](gis-polygon-property-functions.md) | Return Polygon or MultiPolygon area |  |
| [`ST_AsBinary()`, `ST_AsWKB()`](gis-format-conversion-functions.md) | Convert from internal geometry format to WKB |  |
| [`ST_AsGeoJSON()`](spatial-geojson-functions.md) | Generate GeoJSON object from geometry |  |
| [`ST_AsText()`, `ST_AsWKT()`](gis-format-conversion-functions.md) | Convert from internal geometry format to WKT |  |
| [`ST_Buffer()`](spatial-operator-functions.md) | Return geometry of points within given distance from geometry |  |
| [`ST_Buffer_Strategy()`](spatial-operator-functions.md) | Produce strategy option for ST\_Buffer() |  |
| [`ST_Centroid()`](gis-polygon-property-functions.md) | Return centroid as a point |  |
| [`ST_Contains()`](spatial-relation-functions-object-shapes.md) | Whether one geometry contains another |  |
| [`ST_ConvexHull()`](spatial-operator-functions.md) | Return convex hull of geometry |  |
| [`ST_Crosses()`](spatial-relation-functions-object-shapes.md) | Whether one geometry crosses another |  |
| [`ST_Difference()`](spatial-operator-functions.md) | Return point set difference of two geometries |  |
| [`ST_Dimension()`](gis-general-property-functions.md) | Dimension of geometry |  |
| [`ST_Disjoint()`](spatial-relation-functions-object-shapes.md) | Whether one geometry is disjoint from another |  |
| [`ST_Distance()`](spatial-relation-functions-object-shapes.md) | The distance of one geometry from another |  |
| [`ST_Distance_Sphere()`](spatial-convenience-functions.md) | Minimum distance on earth between two geometries |  |
| [`ST_EndPoint()`](gis-linestring-property-functions.md) | End Point of LineString |  |
| [`ST_Envelope()`](gis-general-property-functions.md) | Return MBR of geometry |  |
| [`ST_Equals()`](spatial-relation-functions-object-shapes.md) | Whether one geometry is equal to another |  |
| [`ST_ExteriorRing()`](gis-polygon-property-functions.md) | Return exterior ring of Polygon |  |
| [`ST_GeoHash()`](spatial-geohash-functions.md) | Produce a geohash value |  |
| [`ST_GeomCollFromText()`, `ST_GeometryCollectionFromText()`, `ST_GeomCollFromTxt()`](gis-wkt-functions.md) | Return geometry collection from WKT |  |
| [`ST_GeomCollFromWKB()`, `ST_GeometryCollectionFromWKB()`](gis-wkb-functions.md) | Return geometry collection from WKB |  |
| [`ST_GeometryN()`](gis-geometrycollection-property-functions.md) | Return N-th geometry from geometry collection |  |
| [`ST_GeometryType()`](gis-general-property-functions.md) | Return name of geometry type |  |
| [`ST_GeomFromGeoJSON()`](spatial-geojson-functions.md) | Generate geometry from GeoJSON object |  |
| [`ST_GeomFromText()`, `ST_GeometryFromText()`](gis-wkt-functions.md) | Return geometry from WKT |  |
| [`ST_GeomFromWKB()`, `ST_GeometryFromWKB()`](gis-wkb-functions.md) | Return geometry from WKB |  |
| [`ST_InteriorRingN()`](gis-polygon-property-functions.md) | Return N-th interior ring of Polygon |  |
| [`ST_Intersection()`](spatial-operator-functions.md) | Return point set intersection of two geometries |  |
| [`ST_Intersects()`](spatial-relation-functions-object-shapes.md) | Whether one geometry intersects another |  |
| [`ST_IsClosed()`](gis-linestring-property-functions.md) | Whether a geometry is closed and simple |  |
| [`ST_IsEmpty()`](gis-general-property-functions.md) | Whether a geometry is empty |  |
| [`ST_IsSimple()`](gis-general-property-functions.md) | Whether a geometry is simple |  |
| [`ST_IsValid()`](spatial-convenience-functions.md) | Whether a geometry is valid |  |
| [`ST_LatFromGeoHash()`](spatial-geohash-functions.md) | Return latitude from geohash value |  |
| [`ST_Length()`](gis-linestring-property-functions.md) | Return length of LineString |  |
| [`ST_LineFromText()`, `ST_LineStringFromText()`](gis-wkt-functions.md) | Construct LineString from WKT |  |
| [`ST_LineFromWKB()`, `ST_LineStringFromWKB()`](gis-wkb-functions.md) | Construct LineString from WKB |  |
| [`ST_LongFromGeoHash()`](spatial-geohash-functions.md) | Return longitude from geohash value |  |
| [`ST_MakeEnvelope()`](spatial-convenience-functions.md) | Rectangle around two points |  |
| [`ST_MLineFromText()`, `ST_MultiLineStringFromText()`](gis-wkt-functions.md) | Construct MultiLineString from WKT |  |
| [`ST_MLineFromWKB()`, `ST_MultiLineStringFromWKB()`](gis-wkb-functions.md) | Construct MultiLineString from WKB |  |
| [`ST_MPointFromText()`, `ST_MultiPointFromText()`](gis-wkt-functions.md) | Construct MultiPoint from WKT |  |
| [`ST_MPointFromWKB()`, `ST_MultiPointFromWKB()`](gis-wkb-functions.md) | Construct MultiPoint from WKB |  |
| [`ST_MPolyFromText()`, `ST_MultiPolygonFromText()`](gis-wkt-functions.md) | Construct MultiPolygon from WKT |  |
| [`ST_MPolyFromWKB()`, `ST_MultiPolygonFromWKB()`](gis-wkb-functions.md) | Construct MultiPolygon from WKB |  |
| [`ST_NumGeometries()`](gis-geometrycollection-property-functions.md) | Return number of geometries in geometry collection |  |
| [`ST_NumInteriorRing()`, `ST_NumInteriorRings()`](gis-polygon-property-functions.md) | Return number of interior rings in Polygon |  |
| [`ST_NumPoints()`](gis-linestring-property-functions.md) | Return number of points in LineString |  |
| [`ST_Overlaps()`](spatial-relation-functions-object-shapes.md) | Whether one geometry overlaps another |  |
| [`ST_PointFromGeoHash()`](spatial-geohash-functions.md) | Convert geohash value to POINT value |  |
| [`ST_PointFromText()`](gis-wkt-functions.md) | Construct Point from WKT |  |
| [`ST_PointFromWKB()`](gis-wkb-functions.md) | Construct Point from WKB |  |
| [`ST_PointN()`](gis-linestring-property-functions.md) | Return N-th point from LineString |  |
| [`ST_PolyFromText()`, `ST_PolygonFromText()`](gis-wkt-functions.md) | Construct Polygon from WKT |  |
| [`ST_PolyFromWKB()`, `ST_PolygonFromWKB()`](gis-wkb-functions.md) | Construct Polygon from WKB |  |
| [`ST_Simplify()`](spatial-convenience-functions.md) | Return simplified geometry |  |
| [`ST_SRID()`](gis-general-property-functions.md) | Return spatial reference system ID for geometry |  |
| [`ST_StartPoint()`](gis-linestring-property-functions.md) | Start Point of LineString |  |
| [`ST_SymDifference()`](spatial-operator-functions.md) | Return point set symmetric difference of two geometries |  |
| [`ST_Touches()`](spatial-relation-functions-object-shapes.md) | Whether one geometry touches another |  |
| [`ST_Union()`](spatial-operator-functions.md) | Return point set union of two geometries |  |
| [`ST_Validate()`](spatial-convenience-functions.md) | Return validated geometry |  |
| [`ST_Within()`](spatial-relation-functions-object-shapes.md) | Whether one geometry is within another |  |
| [`ST_X()`](gis-point-property-functions.md) | Return X coordinate of Point |  |
| [`ST_Y()`](gis-point-property-functions.md) | Return Y coordinate of Point |  |
| [`StartPoint()`](gis-linestring-property-functions.md) | Start Point of LineString | Yes |
| [`Touches()`](spatial-relation-functions-object-shapes.md) | Whether one geometry touches another | Yes |
| [`Within()`](spatial-relation-functions-mbr.md) | Whether MBR of one geometry is within MBR of another | Yes |
| [`X()`](gis-point-property-functions.md) | Return X coordinate of Point | Yes |
| [`Y()`](gis-point-property-functions.md) | Return Y coordinate of Point | Yes |