---
title: "MySQL :: MySQL 26.10 Reference Manual :: 14.16.7 Geometry Property Functions"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/gis-property-functions.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 14.16.7 Geometry Property Functions

Each function that belongs to this group takes a geometry value as its argument and returns some quantitative or qualitative property of the geometry. Some functions restrict their argument type. Such functions return `NULL` if the argument is of an incorrect geometry type. For example, the [`ST_Area()`](gis-polygon-property-functions.md) polygon function returns `NULL` if the object type is neither `Polygon` nor `MultiPolygon`.