---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/MAX_IDLE_BLOCKER_TIME.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.204 MAX\_IDLE\_BLOCKER\_TIME

`MAX_IDLE_BLOCKER_TIME` specifies the maximum number of minutes that a blocking session can be idle. After that point, the session is automatically terminated.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | 0 |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | 0 to the maximum integer. The value of 0 indicates that there is no limit. |
| Basic | No |
| Oracle RAC | Different instances can use different values. |

A session is considered to be a blocking session when it is holding resources required by other sessions. For example:

- The session is holding a lock required by another session.
- The session is a parallel operation and its consumer group, PDB, or database has either reached its maximum parallel server limit or has queued parallel operations.
- The session’s PDB or database instance is about to reach its `SESSIONS` or `PROCESSES` limit.

This parameter differs from the `MAX_IDLE_TIME` parameter in that `MAX_IDLE_TIME` applies to all sessions (blocking and non-blocking), whereas `MAX_IDLE_BLOCKING_TIME` applies only to blocking sessions. Therefore, in order for `MAX_IDLE_BLOCKING_TIME` to be effective, its limit must be less than the `MAX_IDLE_TIME` limit.

Note:

This parameter does not have an effect on parallel query processes, nor on `SYS` user sessions.

See Also:

" [MAX\_IDLE\_TIME](MAX_IDLE_TIME.md) "