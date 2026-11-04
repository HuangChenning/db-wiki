---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/RESUMABLE_TIMEOUT.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.320 RESUMABLE\_TIMEOUT

`RESUMABLE_TIMEOUT` enables or disables resumable statements and specifies resumable timeout at the system level.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `0` (seconds) |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `0` to 2 <sup>31</sup> - 1 (in seconds) |
| Basic | No |
| Oracle RAC | Multiple instances can have different values. |

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN11589) for more information about enabling resumable space allocation, what conditions are correctable, and what statements can be made resumable