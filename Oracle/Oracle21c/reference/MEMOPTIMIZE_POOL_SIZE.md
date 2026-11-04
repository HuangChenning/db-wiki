---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/MEMOPTIMIZE_POOL_SIZE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.211 MEMOPTIMIZE\_POOL\_SIZE

`MEMOPTIMIZE_POOL_SIZE` sets the size of the memoptimize pool, a memory area in the system global area (SGA) used by the Memoptimized Rowstore.

| Property | Description |
| --- | --- |
| Parameter type | Big integer |
| Syntax | `MEMOPTIMIZE_POOL_SIZE = ` `integer` ` [K \| M \| G]` |
| Default value | 0 |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | 0 to no maximum |
| Basic | No |
| Oracle RAC | Different values can be used on different instances. |

The Memoptimized Rowstore improves the data query performance of applications, such as Internet of Things (IoT), that frequently query tables based on primary key values.

The Memoptimized Rowstore provides the capability of fast lookup of data for the tables that are mainly queried based on primary key columns.

This parameter specifies an integer value to indicate the amount of SGA to use for allocating the following structures for the memoptimize pool:

- The size of the buffer cache region: This is the total number of blocks for all `MEMOPTIMIZE FOR READ` tables.
- The size of the hash index segmented data structure pointing to the special blocks of `MEMOPTIMIZE FOR READ` tables.

Calculate the buffer cache requirement for the table being considered for `MEMOPTIMIZE FOR READ`, and include an additional 25% memory requirement for the hash index segmented data structure.

These structures are allocated from SGA at instance startup.

The value specified for this parameter counts toward `SGA_TARGET`. For example, if you set `SGA_TARGET` to 10 GB and you set `MEMOPTIMIZE_POOL_SIZE` to 2 GB, then 20% of the `SGA_TARGET` setting is allocated to the memoptimize pool.

Unlike other SGA components such as the buffer cache and shared pool, the memoptimize pool size is not controlled by automatic memory management. The database does not automatically shrink the memoptimize pool when the buffer cache or shared pool requires more memory, or increase the memoptimize pool when it runs out of space. You can only increase the size of the memoptimize pool by manually adjusting the `MEMOPTIMIZE_POOL_SIZE` initialization parameter.

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGDBA-GUID-9752E93D-55A7-4584-B09B-9623B33B5CCF) for more information about the Memoptimized Rowstore and the memoptimize pool.