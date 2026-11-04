---
title: "MySQL :: MySQL 26.10 Reference Manual :: 14.16.1 Spatial Function Reference"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/spatial-function-reference.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 14.16.1 Spatial Function Reference

The following table lists each spatial function and provides a short description of each one.

**Table 14.21 Spatial Functions**

| Name | Description |
| --- | --- |
| [`GeomCollection()`](gis-mysql-specific-functions.md) | Construct geometry collection from geometries |
| [`GeometryCollection()`](gis-mysql-specific-functions.md) | Construct geometry collection from geometries |
| [`LineString()`](gis-mysql-specific-functions.md) | Construct LineString from Point values |
| [`MBRContains()`](spatial-relation-functions-mbr.md) | Whether MBR of one geometry contains MBR of another |
| [`MBRCoveredBy()`](spatial-relation-functions-mbr.md) | Whether one MBR is covered by another |
| [`MBRCovers()`](spatial-relation-functions-mbr.md) | Whether one MBR covers another |
| [`MBRDisjoint()`](spatial-relation-functions-mbr.md) | Whether MBRs of two geometries are disjoint |
| [`MBREquals()`](spatial-relation-functions-mbr.md) | Whether MBRs of two geometries are equal |
| [`MBRIntersects()`](spatial-relation-functions-mbr.md) | Whether MBRs of two geometries intersect |
| [`MBROverlaps()`](spatial-relation-functions-mbr.md) | Whether MBRs of two geometries overlap |
| [`MBRTouches()`](spatial-relation-functions-mbr.md) | Whether MBRs of two geometries touch |
| [`MBRWithin()`](spatial-relation-functions-mbr.md) | Whether MBR of one geometry is within MBR of another |
| [`MultiLineString()`](gis-mysql-specific-functions.md) | Contruct MultiLineString from LineString values |
| [`MultiPoint()`](gis-mysql-specific-functions.md) | Construct MultiPoint from Point values |
| [`MultiPolygon()`](gis-mysql-specific-functions.md) | Construct MultiPolygon from Polygon values |
| [`Point()`](gis-mysql-specific-functions.md) | Construct Point from coordinates |
| [`Polygon()`](gis-mysql-specific-functions.md) | Construct Polygon from LineString arguments |
| [`ST_Area()`](gis-polygon-property-functions.md) | Return Polygon or MultiPolygon area |
| [`ST_AsBinary()`, `ST_AsWKB()`](gis-format-conversion-functions.md) | Convert from internal geometry format to WKB |
| [`ST_AsGeoJSON()`](spatial-geojson-functions.md) | Generate GeoJSON object from geometry |
| [`ST_AsText()`, `ST_AsWKT()`](gis-format-conversion-functions.md) | Convert from internal geometry format to WKT |
| [`ST_Buffer()`](spatial-operator-functions.md) | Return geometry of points within given distance from geometry |
| [`ST_Buffer_Strategy()`](spatial-operator-functions.md) | Produce strategy option for ST\_Buffer() |
| [`ST_Centroid()`](gis-polygon-property-functions.md) | Return centroid as a point |
| [`ST_Collect()`](spatial-aggregate-functions.md) | Aggregate spatial values into collection |
| [`ST_Contains()`](spatial-relation-functions-object-shapes.md) | Whether one geometry contains another |
| [`ST_ConvexHull()`](spatial-operator-functions.md) | Return convex hull of geometry |
| [`ST_Crosses()`](spatial-relation-functions-object-shapes.md) | Whether one geometry crosses another |
| [`ST_Difference()`](spatial-operator-functions.md) | Return point set difference of two geometries |
| [`ST_Dimension()`](gis-general-property-functions.md) | Dimension of geometry |
| [`ST_Disjoint()`](spatial-relation-functions-object-shapes.md) | Whether one geometry is disjoint from another |
| [`ST_Distance()`](spatial-relation-functions-object-shapes.md) | The distance of one geometry from another |
| [`ST_Distance_Sphere()`](spatial-convenience-functions.md) | Minimum distance on earth between two geometries |
| [`ST_EndPoint()`](gis-linestring-property-functions.md) | End Point of LineString |
| [`ST_Envelope()`](gis-general-property-functions.md) | Return MBR of geometry |
| [`ST_Equals()`](spatial-relation-functions-object-shapes.md) | Whether one geometry is equal to another |
| [`ST_ExteriorRing()`](gis-polygon-property-functions.md) | Return exterior ring of Polygon |
| [`ST_FrechetDistance()`](spatial-relation-functions-object-shapes.md) | The discrete Fréchet distance of one geometry from another |
| [`ST_GeoHash()`](spatial-geohash-functions.md) | Produce a geohash value |
| [`ST_GeomCollFromText()`, `ST_GeometryCollectionFromText()`, `ST_GeomCollFromTxt()`](gis-wkt-functions.md) | Return geometry collection from WKT |
| [`ST_GeomCollFromWKB()`, `ST_GeometryCollectionFromWKB()`](gis-wkb-functions.md) | Return geometry collection from WKB |
| [`ST_GeometryN()`](gis-geometrycollection-property-functions.md) | Return N-th geometry from geometry collection |
| [`ST_GeometryType()`](gis-general-property-functions.md) | Return name of geometry type |
| [`ST_GeomFromGeoJSON()`](spatial-geojson-functions.md) | Generate geometry from GeoJSON object |
| [`ST_GeomFromText()`, `ST_GeometryFromText()`](gis-wkt-functions.md) | Return geometry from WKT |
| [`ST_GeomFromWKB()`, `ST_GeometryFromWKB()`](gis-wkb-functions.md) | Return geometry from WKB |
| [`ST_HausdorffDistance()`](spatial-relation-functions-object-shapes.md) | The discrete Hausdorff distance of one geometry from another |
| [`ST_InteriorRingN()`](gis-polygon-property-functions.md) | Return N-th interior ring of Polygon |
| [`ST_Intersection()`](spatial-operator-functions.md) | Return point set intersection of two geometries |
| [`ST_Intersects()`](spatial-relation-functions-object-shapes.md) | Whether one geometry intersects another |
| [`ST_IsClosed()`](gis-linestring-property-functions.md) | Whether a geometry is closed and simple |
| [`ST_IsEmpty()`](gis-general-property-functions.md) | Whether a geometry is empty |
| [`ST_IsSimple()`](gis-general-property-functions.md) | Whether a geometry is simple |
| [`ST_IsValid()`](spatial-convenience-functions.md) | Whether a geometry is valid |
| [`ST_LatFromGeoHash()`](spatial-geohash-functions.md) | Return latitude from geohash value |
| [`ST_Latitude()`](gis-point-property-functions.md) | Return latitude of Point |
| [`ST_Length()`](gis-linestring-property-functions.md) | Return length of LineString |
| [`ST_LineFromText()`, `ST_LineStringFromText()`](gis-wkt-functions.md) | Construct LineString from WKT |
| [`ST_LineFromWKB()`, `ST_LineStringFromWKB()`](gis-wkb-functions.md) | Construct LineString from WKB |
| [`ST_LineInterpolatePoint()`](spatial-operator-functions.md) | The point a given percentage along a LineString |
| [`ST_LineInterpolatePoints()`](spatial-operator-functions.md) | The points a given percentage along a LineString |
| [`ST_LongFromGeoHash()`](spatial-geohash-functions.md) | Return longitude from geohash value |
| [`ST_Longitude()`](gis-point-property-functions.md) | Return longitude of Point |
| [`ST_MakeEnvelope()`](spatial-convenience-functions.md) | Rectangle around two points |
| [`ST_MLineFromText()`, `ST_MultiLineStringFromText()`](gis-wkt-functions.md) | Construct MultiLineString from WKT |
| [`ST_MLineFromWKB()`, `ST_MultiLineStringFromWKB()`](gis-wkb-functions.md) | Construct MultiLineString from WKB |
| [`ST_MPointFromText()`, `ST_MultiPointFromText()`](gis-wkt-functions.md) | Construct MultiPoint from WKT |
| [`ST_MPointFromWKB()`, `ST_MultiPointFromWKB()`](gis-wkb-functions.md) | Construct MultiPoint from WKB |
| [`ST_MPolyFromText()`, `ST_MultiPolygonFromText()`](gis-wkt-functions.md) | Construct MultiPolygon from WKT |
| [`ST_MPolyFromWKB()`, `ST_MultiPolygonFromWKB()`](gis-wkb-functions.md) | Construct MultiPolygon from WKB |
| [`ST_NumGeometries()`](gis-geometrycollection-property-functions.md) | Return number of geometries in geometry collection |
| [`ST_NumInteriorRing()`, `ST_NumInteriorRings()`](gis-polygon-property-functions.md) | Return number of interior rings in Polygon |
| [`ST_NumPoints()`](gis-linestring-property-functions.md) | Return number of points in LineString |
| [`ST_Overlaps()`](spatial-relation-functions-object-shapes.md) | Whether one geometry overlaps another |
| [`ST_PointAtDistance()`](spatial-operator-functions.md) | The point a given distance along a LineString |
| [`ST_PointFromGeoHash()`](spatial-geohash-functions.md) | Convert geohash value to POINT value |
| [`ST_PointFromText()`](gis-wkt-functions.md) | Construct Point from WKT |
| [`ST_PointFromWKB()`](gis-wkb-functions.md) | Construct Point from WKB |
| [`ST_PointN()`](gis-linestring-property-functions.md) | Return N-th point from LineString |
| [`ST_PolyFromText()`, `ST_PolygonFromText()`](gis-wkt-functions.md) | Construct Polygon from WKT |
| [`ST_PolyFromWKB()`, `ST_PolygonFromWKB()`](gis-wkb-functions.md) | Construct Polygon from WKB |
| [`ST_Simplify()`](spatial-convenience-functions.md) | Return simplified geometry |
| [`ST_SRID()`](gis-general-property-functions.md) | Return spatial reference system ID for geometry |
| [`ST_StartPoint()`](gis-linestring-property-functions.md) | Start Point of LineString |
| [`ST_SwapXY()`](gis-format-conversion-functions.md) | Return argument with X/Y coordinates swapped |
| [`ST_SymDifference()`](spatial-operator-functions.md) | Return point set symmetric difference of two geometries |
| [`ST_Touches()`](spatial-relation-functions-object-shapes.md) | Whether one geometry touches another |
| [`ST_Transform()`](spatial-operator-functions.md) | Transform coordinates of geometry |
| [`ST_Union()`](spatial-operator-functions.md) | Return point set union of two geometries |
| [`ST_Validate()`](spatial-convenience-functions.md) | Return validated geometry |
| [`ST_Within()`](spatial-relation-functions-object-shapes.md) | Whether one geometry is within another |
| [`ST_X()`](gis-point-property-functions.md) | Return X coordinate of Point |
| [`ST_Y()`](gis-point-property-functions.md) | Return Y coordinate of Point |