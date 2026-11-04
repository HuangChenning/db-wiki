---
title: "MySQL :: MySQL 26.10 Reference Manual :: 14.16 Spatial Analysis Functions"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/spatial-analysis-functions.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

## 14.16 Spatial Analysis Functions

MySQL provides functions to perform various operations on spatial data. These functions can be grouped into several major categories according to the type of operation they perform:

- Functions that create geometries in various formats (WKT, WKB, internal)
- Functions that convert geometries between formats
- Functions that access qualitative or quantitative properties of a geometry
- Functions that describe relations between two geometries
- Functions that create new geometries from existing ones

For general background about MySQL support for using spatial data, see [Section 13.4, “Spatial Data Types”](spatial-types.md).