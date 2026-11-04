---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DB_WRITER_PROCESSES.html
tags:
  - oracle
  - 12c
  - reference
---

`DB_WRITER_PROCESSES` specifies the initial number of Database Writer Processes for an instance. This parameter is useful for systems that modify data heavily.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `1` or `CPU_COUNT` / 8, whichever is greater. If the number of processor groups is less than 100 but greater than the number of Database Writer Processes, then the number of Database Writer Processes is adjusted to be a multiple of the number of processor groups. If the number of Database Writer Processes is greater than or equal to the number of processor groups, then there is no adjustment.  For Oracle Solaris on SPARC systems, the default value of this parameter is calculated using an internal algorithm. |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | 1 to 100 |
| Basic | No |

There can be 1 to 100 Database Writer Processes. The names of the first 36 Database Writer Processes are DBW0-DBW9 and DBWa-DBWz. The names of the 37th through 100th Database Writer Processes are BW36-BW99.

See Also:

- [Background Processes](background-processes.md) for additional information about the Database Writer Process
- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=CNCPT1250) for information on when the Database Writer Process writes dirty buffers to disk