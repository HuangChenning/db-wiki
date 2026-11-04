---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/COMMIT_WRITE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.48 COMMIT\_WRITE

`COMMIT_WRITE` is an advanced parameter used to control how redo for transaction commits is written to the redo logs.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `COMMIT_WRITE = '{IMMEDIATE \| BATCH},{WAIT \|NOWAIT}'` |
| Default value | If this parameter is not explicitly specified, then database commit behavior defaults to writing commit records to disk before control is returned to the client.  If only `IMMEDIATE` or `BATCH` is specified, but not `WAIT` or `NOWAIT`, then `WAIT` mode is assumed.  If only `WAIT` or `NOWAIT` is specified, but not `IMMEDIATE` or `BATCH`, then `IMMEDIATE` mode is assumed.  Be aware that the `NOWAIT` option can cause a failure that occurs after the database receives the commit message, but before the redo log records are written. This can falsely indicate to a transaction that its changes are persistent. Also, it can violate the durability of ACID (Atomicity, Consistency, Isolation, Durability) transactions if the database shuts down unexpectedly. |
| Modifiable | Yes (at both session-level and system-level). Values supplied for `COMMIT_WRITE` in an `ALTER SYSTEM` or `ALTER SESSION` statement must be separated by a comma. |
| Modifiable in a PDB | Yes |
| Range of values | Single-quoted, comma-separated list of either `IMMEDIATE` or `BATCH`, and either `WAIT` or `NOWAIT`. |
| Basic | No |
| Oracle RAC | Each instance may have its own setting |

The `IMMEDIATE` and `BATCH` options control how redo is batched by Log Writer. The `WAIT` and `NOWAIT` options control when the redo for a commit is flushed to the redo logs.

Note:

The `COMMIT_WRITE` parameter is deprecated. It is retained for backward compatibility only. It is replaced by the `COMMIT_LOGGING` and `COMMIT_WAIT` parameters.