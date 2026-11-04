---
title: DB_FLASHBACK_RETENTION_TARGET
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams061.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `1440` (minutes) |
| Modifiable | `ALTER SYSTEM ... SID='*'` |
| Range of values | `0` to 2 <sup>31</sup> - 1 |
| Basic | No |

`DB_FLASHBACK_RETENTION_TARGET` specifies the upper limit (in minutes) on how far back in time the database may be flashed back. How far back one can flashback a database depends on how much flashback data Oracle has kept in the fast recovery area.