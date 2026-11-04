---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/SHRD_DUPL_TABLE_REFRESH_RATE.html
tags:
  - oracle
  - 12c
  - reference
---

`SHRD_DUPL_TABLE_REFRESH_RATE` displays the duplicated table refresh rate (in seconds).

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `60` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | 20 to 2 <sup>31</sup> - 1 |
| Basic | No |
| Oracle RAC | All instances should use the same instance. |

You can change the value of this parameter to change the duplicated table refresh rate.

A duplicated table is a table that has the same contents on all shards in a sharded database. Duplicated tables are implemented using materialized views that are refreshed at a certain rate.

Note:

This initialization parameter is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=CNCPT-GUID-D90D0A33-1BCB-48D8-8193-8FD1C2959371) for an introduction to sharding
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ADMIN-GUID-50D56C0A-5185-4F04-A0CA-EAA442E825D3) for more information about duplicated tables