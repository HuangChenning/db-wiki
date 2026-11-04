---
title: "MySQL :: MySQL 26.10 Reference Manual :: 13.4.2 The OpenGIS Geometry Model"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/opengis-geometry-model.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 13.4.2 The OpenGIS Geometry Model

The set of geometry types proposed by OGC's **SQL with Geometry Types** environment is based on the **OpenGIS Geometry Model**. In this model, each geometric object has the following general properties:

- It is associated with a spatial reference system, which describes the coordinate space in which the object is defined.
- It belongs to some geometry class.