---
title: SHARED_POOL_SIZE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams240.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Big integer |
| Syntax | `SHARED_POOL_SIZE =` `integer` `[K \| M \| G]` |
| Default value | If `SGA_TARGET` is set: If the parameter is not specified, then the default is `0` (internally determined by the Oracle Database). If the parameter is specified, then the user-specified value indicates a minimum value for the memory pool.  If `SGA_TARGET` is not set (32-bit platforms): 64 MB, rounded up to the nearest granule size.  If `SGA_TARGET` is not set (64-bit platforms): 128 MB, rounded up to the nearest granule size.  For considerations when dealing with database instances using ASM, see "SHARED\_POOL\_SIZE and Automatic Storage Management". |
| Modifiable | `ALTER SYSTEM` |
| Range of values | Minimum: the granule size  Maximum: operating system-dependent |

`SHARED_POOL_SIZE` specifies (in bytes) the size of the shared pool. The shared pool contains shared cursors, stored procedures, control structures, and other structures. If you set `PARALLEL_AUTOMATIC_TUNING` to `false`, then Oracle also allocates parallel execution message buffers from the shared pool. Larger values improve performance in multi-user systems. Smaller values use less memory.

You can monitor utilization of the shared pool by querying the view `V$SGASTAT`.

SHARED\_POOL\_SIZE and Automatic Storage Management

On a database instance using ASM, additional memory is required to store extent maps. As a general guideline, you can aggregate the values from the following queries to obtain current database storage size that is either already on ASM or will be stored in ASM. Then determine the redundancy type that is used (or will be used), and calculate the value for `SHARED_POOL_SIZE`, using the aggregated value as input.

```
SELECT SUM(BYTES)/(1024*1024*1024) FROM V$DATAFILE;
SELECT SUM(BYTES)/(1024*1024*1024) FROM V$LOGFILE a, V$LOG b
WHERE a.group#=b.group#;
SELECT SUM(BYTES)/(1024*1024*1024) FROM V$TEMPFILE WHERE
status='ONLINE';
```

Additionally, keep the following guidelines in mind:

- For diskgroups using external redundancy:
	(Every 100G of space needs 1M of extra shared pool) + 2M
- For diskgroups using normal redundancy:
	(Every 50G of space needs 1M of extra shared pool) + 4M
- For diskgroups using high redundancy:
	(Every 33G of space needs 1M of extra shared pool) + 6M