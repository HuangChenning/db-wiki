---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/HEAT_MAP.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.144 HEAT\_MAP

Use `HEAT_MAP` to enable or disable both the Heat Map and Automatic Data Optimization (ADO) features.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `HEAT_MAP = { ON \| OFF }` |
| Default value | `OFF` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | If specified, use the same value on all instances |

Setting the `HEAT_MAP` initialization parameter to `ON` causes the database to track read and write access of all segments, as well as modification of database blocks, due to DMLs and DDLs. These activities are not tracked for objects in the `SYSTEM` and `SYSAUX` tablespaces.

See Also:

- [Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=VLDBG14175) for more information about enabling and disabling the Heat Map feature
- [Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=VLDBG14124) for more information about Heat Map tracking