---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/RESULT_CACHE_EXECUTION_THRESHOLD.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.313 RESULT\_CACHE\_EXECUTION\_THRESHOLD

`RESULT_CACHE_EXECUTION_THRESHOLD` specifies the maximum number of times a PL/SQL function can be executed before its result is stored in the result cache.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `2` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `0` to operating system-dependent |
| Basic | No |
| Oracle RAC | Multiple instances can have different values. |

Note:

This parameter is available starting with Oracle Database 21c.