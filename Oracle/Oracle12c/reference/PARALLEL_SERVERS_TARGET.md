---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/PARALLEL_SERVERS_TARGET.html
tags:
  - oracle
  - 12c
  - reference
---

`PARALLEL_SERVERS_TARGET` specifies the number of parallel server processes allowed to run parallel statements before statement queuing will be used.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | For a CDB:  Equal to the `PARALLEL_MAX_SERVERS` value for the CDB.  For a PDB or non-CDB:  `PARALLEL_THREADS_PER_CPU` \* `CPU_COUNT` \* `concurrent_parallel_users` \* 2 |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | `0` to `PARALLEL_MAX_SERVERS` |
| Basic | No |

When the parameter `PARALLEL_DEGREE_POLICY` is set to `ADAPTIVE` or `AUTO`, Oracle will queue SQL statements that require parallel execution, if the necessary parallel server processes are not available. In a single instance database, statement queuing will begin once the number of parallel server processes active on the system is equal to or greater than `PARALLEL_SERVERS_TARGET`. In an Oracle RAC database, a statement running on one instance can allocate parallel server processes on another instance when necessary. For example, if a statement running on one instance requires parallel execution, but the number of parallel server processes active on that instance is equal to or greater than the value of `PARALLEL_SERVERS_TARGET` for that instance, then the statement can allocate parallel server processes on a different instance. Therefore, statement queuing in an Oracle RAC database will begin only when every instance has reached its `PARALLEL_SERVER_TARGET` threshold.

Note:

Consumer groups that have been marked with the `PARALLEL_STMT_CRITICAL` directive are allowed to bypass the parallel statement queue, and therefore may drive the total number of active parallel server processes beyond `PARALLEL_SERVERS_TARGET`.

By default, `PARALLEL_SERVERS_TARGET` is set lower than the maximum number of parallel server processes allowed on the system (`PARALLEL_MAX_SERVERS`) to ensure each parallel statement will get all of the parallel server resources required and to prevent overloading the system with parallel server processes.

The number of concurrent parallel users running at default degree of parallelism on an instance depends on the memory initialization parameter settings for the instance. For example, if the `MEMORY_TARGET` or `SGA_TARGET` initialization parameter is set, then the number of `concurrent_parallel_users` = `4`. If neither `MEMORY_TARGET` or `SGA_TARGET` is set, then `PGA_AGGREGATE_TARGET` is examined. If a value is set for `PGA_AGGREGATE_TARGET`, then `concurrent_parallel_users` = `2`. If a value is not set for `PGA_AGGREGATE_TARGET`, then `concurrent_parallel_users` = `1`.

Note that all serial (non-parallel) statements will execute immediately even if statement queuing has been activated.