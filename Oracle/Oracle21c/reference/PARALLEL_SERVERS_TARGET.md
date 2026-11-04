---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/PARALLEL_SERVERS_TARGET.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.275 PARALLEL\_SERVERS\_TARGET

`PARALLEL_SERVERS_TARGET` specifies the number of parallel server processes allowed to run parallel statements before statement queuing will be used.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | For a CDB:  Equal to the `PARALLEL_MAX_SERVERS` value for the CDB.  For a PDB or non-CDB:  `PARALLEL_THREADS_PER_CPU` \* `CPU_COUNT` \* `concurrent_parallel_users` \* 2 |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `0` to `PARALLEL_MAX_SERVERS` |
| Basic | No |

When the parameter `PARALLEL_DEGREE_POLICY` is set to `ADAPTIVE` or `AUTO`, Oracle will queue SQL statements that require parallel execution, if the necessary parallel server processes are not available. In a single instance database, statement queuing will begin once the number of parallel server processes active on the system is equal to or greater than `PARALLEL_SERVERS_TARGET`. In an Oracle RAC database, a statement running on one instance can allocate parallel server processes on another instance when necessary. For example, if a statement running on one instance requires parallel execution, but the number of parallel server processes active on that instance is equal to or greater than the value of `PARALLEL_SERVERS_TARGET` for that instance, then the statement can allocate parallel server processes on a different instance. Therefore, statement queuing in an Oracle RAC database will begin only when every instance has reached its `PARALLEL_SERVER_TARGET` threshold.

Note:

Consumer groups that have been marked with the `PARALLEL_STMT_CRITICAL` directive set to `BYPASS_QUEUE` are allowed to bypass the parallel statement queue, and therefore may drive the total number of active parallel server processes beyond `PARALLEL_SERVERS_TARGET`. Parallel statements issued with `PARALLEL_DEGREE_POLICY` not set to `ADAPTIVE` and `AUTO` can also drive the total number of active parallel server processes beyond `PARALLEL_SERVERS_TARGET`.

By default, `PARALLEL_SERVERS_TARGET` is set lower than the maximum number of parallel server processes allowed on the system (`PARALLEL_MAX_SERVERS`) to ensure each parallel statement will get all of the parallel server resources required and to prevent overloading the system with parallel server processes.

The number of concurrent parallel users running at default degree of parallelism on an instance depends on the memory initialization parameter settings for the instance. For example, if the `MEMORY_TARGET` or `SGA_TARGET` initialization parameter is set, then the number of `concurrent_parallel_users` = `4`. If neither `MEMORY_TARGET` or `SGA_TARGET` is set, then `PGA_AGGREGATE_TARGET` is examined. If a value is set for `PGA_AGGREGATE_TARGET`, then `concurrent_parallel_users` = `2`. If a value is not set for `PGA_AGGREGATE_TARGET`, then `concurrent_parallel_users` = `1`.

Note that all serial (non-parallel) statements will execute immediately even if statement queuing has been activated.

By default, all PDB queries are subjected to queuing at the PDB level first by the PDB's `PARALLEL_SERVERS_TARGET` value, and then at the CDB level by the CDB's `PARALLEL_SERVERS_TARGET` value. This default behavior prevents any SQL statement inside a PDB from getting downgraded if parallel servers are exhausted in the CDB.

Parallel statement queuing is enabled by default at the CDB level because the CDB has a default value for `PARALLEL_SERVERS_TARGET`. You can disable parallel statement queuing at the CDB level by using `ALTER SYSTEM` to set `PARALLEL_SERVERS_TARGET` to 0 for the CDB.

The default value for `PARALLEL_SERVERS_TARGET` for a PDB is determined using the calculation in the table above with the PDB’s `CPU_COUNT` value.

Note:

A PDB can set a lower limit for parallel execution servers than the limit specified in the CDB resource plan. When the `PARALLEL_SERVERS_TARGET` initialization parameter is set in a PDB, and parallel execution server limit is specified for a PDB in the CDB resource plan, then the lower of the two limits is enforced. For example, assume that the `PARALLEL_SERVERS_TARGET` initialization parameter is set to 100 in the CDB root. Also assume that hrpdb has its `PARALLEL_SERVERS_TARGET` initialization parameter set to 50 and the CDB plan has a directive for hrpdb with `parallel_server_limit` set to 70%. In this case, the limit for parallel execution servers for hrpdb is 50, because 50 is lower than the CDB resource plan limit of 70 for hrpdb.