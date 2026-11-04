---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/OPTIMIZER_USE_PENDING_STATISTICS.html
tags:
  - oracle
  - 19c
  - reference
---

## 1.261 OPTIMIZER\_USE\_PENDING\_STATISTICS

`OPTIMIZER_USE_PENDING_STATISTICS` specifies whether the optimizer uses pending statistics when compiling SQL statements.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `true \| false` |
| Basic | No |

See Also:

[Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=TGSQL456) for more information on setting this parameter