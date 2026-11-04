---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DATA_GUARD_MAX_IO_TIME.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.66 DATA\_GUARD\_MAX\_IO\_TIME

`DATA_GUARD_MAX_IO_TIME` sets the maximum number of seconds that can elapse before a process is considered hung while performing a regular I/O operation in an Oracle Data Guard environment. Regular I/O operations include read, write, and status operations.

See Also:

" [DATA\_GUARD\_MAX\_LONGIO\_TIME](DATA_GUARD_MAX_LONGIO_TIME.md)," which enables you to set the timeout for long I/O operations, such as open and close operations, in an Oracle Data Guard environment

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `240` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | `10` to `7200` |
| Basic | No |
| Oracle RAC | Different instances can use different values. |