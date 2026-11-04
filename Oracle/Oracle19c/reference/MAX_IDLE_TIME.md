---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/MAX_IDLE_TIME.html
tags:
  - oracle
  - 19c
  - reference
---

## 1.202 MAX\_IDLE\_TIME

`MAX_IDLE_TIME` specifies the maximum number of minutes that a session can be idle. After that point, the session is automatically terminated.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | 0 |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | 0 to the maximum integer. The value of 0 indicates that there is no limit. |
| Basic | No |
| Oracle RAC | Different instances can use different values. |

See Also:

" [MAX\_IDLE\_BLOCKER\_TIME](MAX_IDLE_BLOCKER_TIME.md) " to learn how to set a lower idle time limit for sessions that are holding resources required by other sessions