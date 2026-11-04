---
title: COMMIT_WAIT
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams033.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `COMMIT_WAIT = { NOWAIT \| WAIT \| FORCE_WAIT }` |
| Default value | There is no default value. |
| Modifiable | Yes (at both session-level and system-level) |
| Basic | No |
| Oracle RAC | Each instance may have its own setting |

`COMMIT_WAIT` is an advanced parameter used to control when the redo for a commit is flushed to the redo logs.

Be aware that the `NOWAIT` option can cause a failure that occurs after the database receives the commit message, but before the redo log records are written. This can falsely indicate to a transaction that its changes are persistent. Also, it can violate the durability of ACID (Atomicity, Consistency, Isolation, Durability) transactions if the database shuts down unexpectedly.

If the parameter is set to `FORCE_WAIT`, the default behavior (immediate flushing of the redo log buffer with wait) is used. If this is a system setting, the session level and transaction level (`COMMIT_WRITE`) options will be ignored. If this is a session level setting, the transaction level options will be ignored. If `COMMIT_WAIT` is altered after it has been set to `FORCE_WAIT`, then the `FORCE_WAIT` option is no longer valid.