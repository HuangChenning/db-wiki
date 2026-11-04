---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/SPATIAL_VECTOR_ACCELERATION.html
tags:
  - oracle
  - 12c
  - reference
---

`SPATIAL_VECTOR_ACCELERATION` enables or disables the spatial vector acceleration.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `true \| false` |
| Basic | No |
| Oracle RAC | Multiple instances should use the same value |

Setting this parameter to `true` improves spatial vector query performance.

Note:

This initialization parameter is only available to the Oracle Spatial and Graph option.