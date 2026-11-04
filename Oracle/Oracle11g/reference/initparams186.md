---
title: PARALLEL_MAX_SERVERS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams186.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `PARALLEL_THREADS_PER_CPU` \* `CPU_COUNT` \* `concurrent_parallel_users` \* 5 |
| Modifiable | `ALTER SYSTEM` |
| Range of values | `0` to `3600` |
| Oracle RAC | Multiple instances can have different values. |

Note:

This parameter applies to parallel execution in exclusive mode as well as in a Real Application Clusters environment.

`PARALLEL_MAX_SERVERS` specifies the maximum number of parallel execution processes and parallel recovery processes for an instance. As demand increases, Oracle Database increases the number of processes from the number created at instance startup up to this value.

The number of concurrent parallel users running at default degree of parallelism on an instance depends on the memory initialization parameter settings for the instance. For example, if the `MEMORY_TARGET` or `SGA_TARGET` initialization parameter is set, then the number of `concurrent_parallel_users` = `4`. If neither `MEMORY_TARGET` or `SGA_TARGET` is set, then `PGA_AGGREGATE_TARGET` is examined. If a value is set for `PGA_AGGREGATE_TARGET`, then `concurrent_parallel_users` = `2`. If a value is not set for `PGA_AGGREGATE_TARGET`, then `concurrent_parallel_users` = `1`.

If you set this parameter too low, then some queries may not have a parallel execution process available to them during query processing. If you set it too high, then memory resource shortages may occur during peak periods, which can degrade performance.

Note:

The database system always reserves a certain number of reserved processes.

The default value of the `PARALLEL_MAX_SERVERS` initialization parameter is set to the lower of these two values:

- The default value of `PARALLEL_MAX_SERVERS` determined using the calculation in the table above
- The value of the `PROCESSES` initialization parameter minus the number of reserved processes

When the `PARALLEL_MAX_SERVERS` parameter is set to a value lower than the value in the table above, the lower default value enables the database to start service processes and allows user processes to connect to the database.

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm) for more information on tuning parallel execution