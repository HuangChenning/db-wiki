---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/HEARTBEAT_BATCH_SIZE.html
tags:
  - oracle
  - 19c
  - reference
---

## 1.139 HEARTBEAT\_BATCH\_SIZE

Use `HEARTBEAT_BATCH_SIZE` to configure the heartbeat batch size, which is the number of heartbeats sent during one heartbeat period.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `5` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `2` to `100` |
| Basic | No |
| Oracle RAC | Multiple instances must have the same value. |

Note:

This parameter is available starting with Oracle Database 19c, Release Update 19.29.