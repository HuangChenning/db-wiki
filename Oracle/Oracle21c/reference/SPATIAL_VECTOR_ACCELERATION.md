---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/SPATIAL_VECTOR_ACCELERATION.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.345 SPATIAL\_VECTOR\_ACCELERATION

`SPATIAL_VECTOR_ACCELERATION` enables or disables the spatial vector acceleration.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `true` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `true \| false` |
| Basic | No |
| Oracle RAC | Multiple instances should use the same value |

The setting of `true` for this parameter improves spatial vector query performance.