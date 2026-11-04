---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/MAX_IDLE_TIME.html
tags:
  - oracle
  - 12c
  - reference
---

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

Note:

This parameter is available starting with Oracle Database 12c Release 2 (12.2.0.1).