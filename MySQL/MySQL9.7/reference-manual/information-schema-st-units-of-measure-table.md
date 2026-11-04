---
title: "28.3.43 The INFORMATION_SCHEMA ST_UNITS_OF_MEASURE Table"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/information-schema-st-units-of-measure-table.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 28.3.43 The INFORMATION\_SCHEMA ST\_UNITS\_OF\_MEASURE Table

The `ST_UNITS_OF_MEASURE` table provides information about acceptable units for the [`ST_Distance()`](spatial-relation-functions-object-shapes.md) function.

The `ST_UNITS_OF_MEASURE` table has these columns:

- `UNIT_NAME`
	The name of the unit.
- `UNIT_TYPE`
	The unit type (for example, `LINEAR`).
- `CONVERSION_FACTOR`
	A conversion factor used for internal calculations.
- `DESCRIPTION`
	A description of the unit.