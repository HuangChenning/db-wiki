---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/SHRD_DUPL_TABLE_REFRESH_RATE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.340 SHRD\_DUPL\_TABLE\_REFRESH\_RATE

`SHRD_DUPL_TABLE_REFRESH_RATE` displays the duplicated table refresh rate (in seconds).

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `60` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | 20 to 2 <sup>31</sup> - 1 |
| Basic | No |
| Oracle RAC | All instances should use the same instance. |

You can change the value of this parameter to change the duplicated table refresh rate.

A duplicated table is a table that has the same contents on all shards in a sharded database. Duplicated tables are implemented using materialized views that are refreshed at a certain rate.

See Also:

- [Using Oracle Sharding](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SHARD-GUID-0F39B1FB-DCF9-4C8A-A2EA-88705B90C5BF) for an introduction to sharding
- [Using Oracle Sharding](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SHARD-GUID-50D56C0A-5185-4F04-A0CA-EAA442E825D3) for more information about duplicated tables