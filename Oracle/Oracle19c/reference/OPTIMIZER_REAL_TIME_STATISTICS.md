---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/OPTIMIZER_REAL_TIME_STATISTICS.html
tags:
  - oracle
  - 19c
  - reference
---

## 1.257 OPTIMIZER\_REAL\_TIME\_STATISTICS

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

Note:

This parameter is available starting with Oracle Database 19c, Release Update 19.10.