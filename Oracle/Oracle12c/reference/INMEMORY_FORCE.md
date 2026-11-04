---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/INMEMORY_FORCE.html
tags:
  - oracle
  - 12c
  - reference
---

`INMEMORY_FORCE` allows you to specify whether tables and materialized views that are specified as `INMEMORY` are populated into the In-Memory Column Store (IM column store) or not.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `INMEMORY_FORCE = { DEFAULT \| OFF }` |
| Default value | `DEFAULT` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | All instances should use the same value. |

The default value is `DEFAULT`. When this value is in effect, the IM column store is populated only with tables and materialized views specified as `INMEMORY`.

If `OFF` is specified, then even if the IM column store is configured on this instance, no tables or materialized views are populated in memory.