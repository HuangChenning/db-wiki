---
title: PARALLEL_SERVERS_TARGET
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams190.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `PARALLEL_THREADS_PER_CPU` \* `CPU_COUNT` \* `concurrent_parallel_users` \* 2 |
| Modifiable | `ALTER SYSTEM` |
| Range of values | `0` to `PARALLEL_MAX_SERVERS` |
| Basic | No |

`PARALLEL_SERVERS_TARGET` specifies the number of parallel server processes allowed to run parallel statements before statement queuing will be used. When the parameter `PARALLEL_DEGREE_POLICY` is set to `AUTO`, Oracle will queue SQL statements that require parallel execution, if the necessary parallel server processes are not available. Statement queuing will begin once the number of parallel server processes active on the system is equal to or greater than `PARALLEL_SERVERS_TARGET`.

By default, `PARALLEL_SERVERS_TARGET` is set lower than the maximum number of parallel server processes allowed on the system (`PARALLEL_MAX_SERVERS`) to ensure each parallel statement will get all of the parallel server resources required and to prevent overloading the system with parallel server processes.

The number of concurrent parallel users running at default degree of parallelism on an instance depends on the memory initialization parameter settings for the instance. For example, if the `MEMORY_TARGET` or `SGA_TARGET` initialization parameter is set, then the number of `concurrent_parallel_users` = `4`. If neither `MEMORY_TARGET` or `SGA_TARGET` is set, then `PGA_AGGREGATE_TARGET` is examined. If a value is set for `PGA_AGGREGATE_TARGET`, then `concurrent_parallel_users` = `2`. If a value is not set for `PGA_AGGREGATE_TARGET`, then `concurrent_parallel_users` = `1`.

Note that all serial (non-parallel) statements will execute immediately even if statement queuing has been activated.