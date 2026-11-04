---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/OPTIMIZER_ADAPTIVE_PLANS.html
tags:
  - oracle
  - 12c
  - reference
---

Adaptive plans are execution plans built with alternative choices that are decided at run time based on statistics collected as the query executes.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `true` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `true \| false` |
| Basic | No |
| Oracle RAC | The same value must be set on all instances |

Setting this parameter to `false` disables the following adaptive features:

- Nested loop join/hash join selection
- Star transformation bitmap pruning
- Adaptive parallel distribution method

Note:

This initialization parameter is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

[Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=TGSQL-GUID-5A1EB094-1A9E-4B69-9BE5-39BDA2B3253C) for information about adaptive plans