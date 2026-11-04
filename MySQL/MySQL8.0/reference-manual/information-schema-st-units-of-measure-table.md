---
title: "28.3.37 The INFORMATION_SCHEMA ST_UNITS_OF_MEASURE Table"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/information-schema-st-units-of-measure-table.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 28.3.37 The INFORMATION\_SCHEMA ST\_UNITS\_OF\_MEASURE Table

The `ST_UNITS_OF_MEASURE` table (available as of MySQL 8.0.14) provides information about acceptable units for the [`ST_Distance()`](spatial-relation-functions-object-shapes.md) function.

The `ST_UNITS_OF_MEASURE` table has these columns:

- `UNIT_NAME`
	The name of the unit.
- `UNIT_TYPE`
	The unit type (for example, `LINEAR`).
- `CONVERSION_FACTOR`
	A conversion factor used for internal calculations.
- `DESCRIPTION`
	A description of the unit.