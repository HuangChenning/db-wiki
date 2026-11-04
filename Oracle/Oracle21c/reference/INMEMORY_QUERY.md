---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/INMEMORY_QUERY.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.157 INMEMORY\_QUERY

`INMEMORY_QUERY` is used to enable or disable in-memory queries for the entire database at the session or system level.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `INMEMORY_QUERY = { ENABLE \| DISABLE }` |
| Default value | `ENABLE` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | All instances should use the same value. |

This parameter is helpful when you want to test workloads with and without the use of the In-Memory Column Store (IM column store).

This parameter enables in-memory queries for the entire database by default when the `INMEMORY_SIZE` parameter is specified.

Set this parameter to `DISABLE` if you want to disable in-memory queries.