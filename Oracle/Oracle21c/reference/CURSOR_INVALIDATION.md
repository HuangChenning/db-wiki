---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/CURSOR_INVALIDATION.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.63 CURSOR\_INVALIDATION

`CURSOR_INVALIDATION` controls whether deferred cursor invalidation or immediate cursor invalidation is used for DDL statements by default.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `CURSOR_INVALIDATION = { DEFERRED \| IMMEDIATE }` |
| Default value | `IMMEDIATE` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | Different instances can have different values. |

Deferred invalidation reduces the number of cursor invalidations and spreads the recompilation workload over time. Note that when the recompilation workload is spread over time, a cursor may run with a sub-optimal plan until it is recompiled, and may incur small execution-time overhead.

Prior to Oracle Database 12c Release 2 (12.2.0.1), immediate cursor invalidation was used.

This parameter provides system or session level default for the `DEFERRED` or `IMMEDIATE` option for the `INVALIDATION` clause in DDL statements.

When this parameter is set to `DEFERRED`, an application can take advantage of reduced cursor invalidation without making any other application changes.

When this parameter is set to `IMMEDIATE`, the application will experience the same cursor invalidation behavior as in Oracle Database 12c Release 1 (12.1).