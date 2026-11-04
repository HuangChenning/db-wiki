---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/OPTIMIZER_CROSS_SHARD_RESILIENCY.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.245 OPTIMIZER\_CROSS\_SHARD\_RESILIENCY

`OPTIMIZER_CROSS_SHARD_RESILIENCY` enables resilient execution of cross shard queries.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `true \| false` |
| Basic | No |
| Oracle RAC | The same value must be used on all instances. |

When this parameter is set to `true` and a cross-shard query fails on one or more shards, the query execution continues on the Oracle Data Guard standbys of the failed shards. This parameter is not set to `true` by default, because there may be performance overhead for the resilient query execution.

Note:

This parameter is available starting with Oracle Database 21c.