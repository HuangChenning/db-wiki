---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/PARALLEL_THREADS_PER_CPU.html
tags:
  - oracle
  - 12c
  - reference
---

`PARALLEL_THREADS_PER_CPU` describes the number of parallel execution processes or threads that a CPU can handle during parallel execution.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | Operating system-dependent, usually `2` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | Any nonzero number |
| Basic | No |

Note:

This parameter applies to parallel execution in exclusive mode as well as in an Oracle Real Application Clusters environment.

This parameter is used in determining the default values of other parallel execution related parameters, for example, `PARALLEL_MAX_SERVERS`. It is also used in determining the default degree of parallelism for SQL statements, and determining the upper bound for the degree of parallelism in automatic degree of parallelism. The default value is adequate in most cases.

See Also:

- [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=TGSQL94713) for more information about parallel execution
- [Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=VLDBG1392) for information about how the optimizer automatically determines the degree of parallelism for a statement