---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/SDO_GEOM.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 238 SDO\_GEOM

The `SDO_GEOM` package contains the geometry functions.

These can be grouped into the following categories (with examples of each):

- Relationship (True/False) between two objects: `RELATE`, `WITHIN_DISTANCE`
- Validation: `VALIDATE_GEOMETRY_WITH_CONTEXT`, `VALIDATE_LAYER_WITH_CONTEXT`
- Single-object operations: `SDO_ARC_DENSIFY`, `SDO_AREA`, `SDO_BUFFER`, `SDO_CENTROID`, `SDO_CONVEXHULL`, `SDO_LENGTH`, `SDO_MBR`, `SDO_POINTONSURFACE`
- Two-object operations: `SDO_DISTANCE`, `SDO_DIFFERENCE`, `SDO_INTERSECTION`, `SDO_UNION`, `SDO_XOR`

For a complete description of this package within the context of Oracle Spatial, see [`SDO_GEOM`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=SPATL120) in the Oracle Spatial and Graph Developer's Guide.