---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/RESULT_CACHE_MAX_RESULT.html
tags:
  - oracle
  - 19c
  - reference
---

## 1.315 RESULT\_CACHE\_MAX\_RESULT

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