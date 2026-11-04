---
title: "MySQL :: MySQL 26.7 Reference Manual :: 14.16.9 Functions That Test Spatial Relations Between Geometry Objects"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/spatial-relation-functions.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 14.16.9 Functions That Test Spatial Relations Between Geometry Objects

The functions described in this section take two geometries as arguments and return a qualitative or quantitative relation between them.

MySQL implements two sets of functions using function names defined by the OpenGIS specification. One set tests the relationship between two geometry values using precise object shapes, the other set uses object minimum bounding rectangles (MBRs).