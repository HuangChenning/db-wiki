---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/COMMIT_LOGGING.html
tags:
  - oracle
  - 12c
  - reference
---

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