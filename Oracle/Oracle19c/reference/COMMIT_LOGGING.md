---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/COMMIT_LOGGING.html
tags:
  - oracle
  - 19c
  - reference
---

## 1.46 COMMIT\_LOGGING

`COMMIT_LOGGING` is an advanced parameter used to control how redo is batched by Log Writer.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `COMMIT_LOGGING = { IMMEDIATE \| BATCH }` |
| Default value | There is no default value. |
| Modifiable | Yes (at both session-level and system-level) |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | Each instance may have its own setting |

If `COMMIT_LOGGING` is altered after setting `COMMIT_WAIT` to `FORCE_WAIT`, then the `FORCE_WAIT` option is no longer valid.