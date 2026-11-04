---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DATA_GUARD_MAX_LONGIO_TIME.html
tags:
  - oracle
  - 19c
  - reference
---

## 1.68 DATA\_GUARD\_MAX\_LONGIO\_TIME

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

Note:

This parameter is available starting with Oracle Database 19c.

See Also:

" [DATA\_GUARD\_MAX\_IO\_TIME](DATA_GUARD_MAX_IO_TIME.md) "