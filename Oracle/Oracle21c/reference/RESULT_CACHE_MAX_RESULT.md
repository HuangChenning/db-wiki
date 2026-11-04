---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/RESULT_CACHE_MAX_RESULT.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.314 RESULT\_CACHE\_MAX\_RESULT

`RESULT_CACHE_MAX_RESULT` specifies the percentage of `RESULT_CACHE_MAX_SIZE` that any single result can use.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `5` percent |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `0` to `100` |
| Basic | No |
| Oracle RAC | Multiple instances can have different values. |