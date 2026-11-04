---
title: LARGE_POOL_SIZE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams113.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Big integer |
| Syntax | `LARGE_POOL_SIZE =` `integer` `[K \| M \| G]` |
| Default value | If `SGA_TARGET` is set, but a value is not specified for `LARGE_POOL_SIZE`, then the default is 0 (internally determined by the Oracle database). If `LARGE_POOL_SIZE` is specified, then the user-specified value indicates a minimum value for the memory pool.  If `SGA_TARGET` is not set, 0 if both of the following are true:  - The pool is not required by parallel execution - `DBWR_IO_SLAVES` is not set  Otherwise, derived from the values of `PARALLEL_MAX_SERVERS`, `PARALLEL_THREADS_PER_CPU`, `CLUSTER_DATABASE_INSTANCES`, `DISPATCHERS`, and `DBWR_IO_SLAVES`.  Note that a value derived in this way does not take into account the requirements used for Automatic Storage Management files. As a general guideline, you should add 600K to the size of the SGA on a database instance using ASM. |
| Modifiable | `ALTER SYSTEM` |
| Range of values | Minimum: the granule size  Maximum: operating system-dependent |
| Basic | No |

`LARGE_POOL_SIZE` specifies (in bytes) the size of the large pool allocation heap. The large pool allocation heap is used in shared server systems for session memory, by parallel execution for message buffers, and by backup processes for disk I/O buffers. Parallel execution allocates buffers out of the large pool only when `SGA_TARGET` is set.

Caution:

When Oracle derives a default value, it adds 250K for each session for the shared server if `DISPATCHERS` is configured. The final derived value also includes a port-specific amount of memory for backup I/O buffers. The total derived default value can either be too large to allocate or can cause performance problems. In that case, set `LARGE_POOL_SIZE` to a number sufficiently small so that the database can start.

You can specify the value of this parameter using a number, optionally followed by K or M to specify kilobytes or megabytes, respectively. If you do not specify K or M, then the number is taken as bytes.

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm) and [Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/toc.htm) for more information on setting this parameter