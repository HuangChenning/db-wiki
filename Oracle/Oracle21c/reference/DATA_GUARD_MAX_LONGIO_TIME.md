---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DATA_GUARD_MAX_LONGIO_TIME.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.67 DATA\_GUARD\_MAX\_LONGIO\_TIME

`DATA_GUARD_MAX_LONGIO_TIME` sets the maximum number of seconds that can elapse before a process is considered hung while performing a long I/O operation in an Oracle Data Guard environment. Long I/O operations include open and close operations.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `240` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | `10` to `7200` |
| Basic | No |
| Oracle RAC | Different instances can use different values. |

See Also:

" [DATA\_GUARD\_MAX\_IO\_TIME](DATA_GUARD_MAX_IO_TIME.md) "