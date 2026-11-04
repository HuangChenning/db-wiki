---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/PROCESSES.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.294 PROCESSES

`PROCESSES` specifies the maximum number of operating system user processes that can simultaneously connect to Oracle.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | The value is derived, and it typically depends on the number of cores reported in the alert log. |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | 80 to operating system dependent |
| Basic | Yes |
| Oracle RAC | Multiple instances can have different values. |

The value for this parameter should allow for all background processes such as locks, job queue processes, and parallel execution processes.

The default values of the `SESSIONS` and `TRANSACTIONS` parameters are derived from this parameter. Therefore, if you change the value of `PROCESSES`, you should evaluate whether to adjust the values of those derived parameters.

See Also:

- Your operating system-specific Oracle documentation for the range of values
- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=CNCPT947) for an introduction to Oracle database instance processes