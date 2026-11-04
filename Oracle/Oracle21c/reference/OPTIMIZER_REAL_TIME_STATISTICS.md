---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/OPTIMIZER_REAL_TIME_STATISTICS.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.254 OPTIMIZER\_REAL\_TIME\_STATISTICS

`OPTIMIZER_REAL_TIME_STATISTICS` controls whether the database automatically gathers real-time statistics during conventional DML operations.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `true \| false` |
| Basic | No |
| Oracle RAC | Different values can be set on different instances. |

When this parameter is set to `true`, the database automatically gathers real-time statistics during conventional DML operations. The default setting is `false`, which means real-time statistics are disabled.