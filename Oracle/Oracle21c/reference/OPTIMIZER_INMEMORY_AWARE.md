---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/OPTIMIZER_INMEMORY_AWARE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.252 OPTIMIZER\_INMEMORY\_AWARE

`OPTIMIZER_INMEMORY_AWARE` enables or disables all of the optimizer cost model enhancements for in-memory.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `true` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `true \| false` |
| Basic | No |
| Oracle RAC | All instances should use the same value |

Setting the parameter to `false` causes the optimizer to ignore the in-memory property of tables during the optimization of SQL statements. This behavior can also be achieved by setting the `OPTIMIZER_FEATURES_ENABLE` initialization parameter to values lower than 12.1.0.2.

See Also:

- " [OPTIMIZER\_FEATURES\_ENABLE](OPTIMIZER_FEATURES_ENABLE.md) "
- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=CNCPT316) and [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGSQL192) for more information about the optimizer