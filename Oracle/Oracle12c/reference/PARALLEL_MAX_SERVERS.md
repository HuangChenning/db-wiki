---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/PARALLEL_MAX_SERVERS.html
tags:
  - oracle
  - 12c
  - reference
---

`PARALLEL_MAX_SERVERS` specifies the maximum number of parallel execution processes and parallel recovery processes for an instance. As demand increases, Oracle Database increases the number of processes from the number created at instance startup up to this value.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `PARALLEL_THREADS_PER_CPU` \* `CPU_COUNT` \* `concurrent_parallel_users` \* 5 |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `0` to `32767` |
| Basic | No |
| Oracle RAC | Multiple instances can have different values. |

Note:

This parameter applies to parallel execution in exclusive mode as well as in a Real Application Clusters environment.

The number of concurrent parallel users running at default degree of parallelism on an instance depends on the memory initialization parameter settings for the instance. For example, if the `MEMORY_TARGET` or `SGA_TARGET` initialization parameter is set, then the number of `concurrent_parallel_users` = `4`. If neither `MEMORY_TARGET` or `SGA_TARGET` is set, then `PGA_AGGREGATE_TARGET` is examined. If a value is set for `PGA_AGGREGATE_TARGET`, then `concurrent_parallel_users` = `2`. If a value is not set for `PGA_AGGREGATE_TARGET`, then `concurrent_parallel_users` = `1`.

The database system always reserves a certain number of reserved processes. Therefore, the following two values are taken into account when setting the `PARALLEL_MAX_SERVERS` initialization parameter:

- The default value of `PARALLEL_MAX_SERVERS` determined using the calculation in the table above
- The value of the `PROCESSES` initialization parameter minus the number of reserved processes

The lower of the two values is used as the default value of `PARALLEL_MAX_SERVERS`, and if you attempt to explicitly set `PARALLEL_MAX_SERVERS` to a value that is higher than either of the values, then the setting is adjusted to the lower of the two values.

When the `PARALLEL_MAX_SERVERS` parameter is set to a value lower than the value in the table above, the lower default value enables the database to start service processes and allows user processes to connect to the database.

Note:

If you set this parameter too low, then some queries may not have a parallel execution process available to them during query processing. If you set it too high, then memory resource shortages may occur during peak periods, which can degrade performance.

See Also:

[Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=TGSQL94713) for more information about parallel execution