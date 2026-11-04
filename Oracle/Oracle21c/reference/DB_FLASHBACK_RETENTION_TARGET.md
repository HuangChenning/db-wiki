---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DB_FLASHBACK_RETENTION_TARGET.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.86 DB\_FLASHBACK\_RETENTION\_TARGET

`DB_FLASHBACK_RETENTION_TARGET` specifies the upper limit (in minutes) on how far back in time the database may be flashed back.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `1440` (minutes) |
| Modifiable | `ALTER SYSTEM ... SID='*'` |
| Modifiable in a PDB | No |
| Range of values | `0` to 2 <sup>31</sup> - 1 |
| Basic | No |

How far back one can flashback a database depends on how much flashback data Oracle has kept in the fast recovery area.

See Also:

[Oracle Data Guard Broker](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DGBKR-GUID-EAC49F16-D821-4F64-9E78-270E07F3B465) for enabling Flashback Database on Oracle Data Guard primary and target standby databases