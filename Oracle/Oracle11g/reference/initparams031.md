---
title: COMMIT_LOGGING
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams031.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `COMMIT_LOGGING = { IMMEDIATE \| BATCH }` |
| Default value | There is no default value. |
| Modifiable | Yes (at both session-level and system-level) |
| Basic | No |
| Oracle RAC | Each instance may have its own setting |

`COMMIT_LOGGING` is an advanced parameter used to control how redo is batched by Log Writer.

If `COMMIT_LOGGING` is altered after setting `COMMIT_WAIT` to `FORCE_WAIT`, then the `FORCE_WAIT` option is no longer valid.