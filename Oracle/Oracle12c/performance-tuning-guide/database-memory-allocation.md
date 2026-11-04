---
title: Database Performance Tuning Guide
book: Database Performance Tuning Guide
doc_id: E85600-04
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/tgdba/database-memory-allocation.html
tags:
  - oracle
  - 12c
  - performance-tuning-guide
---

This chapter describes memory allocation in Oracle Database and the various methods for managing memory.

This chapter contains the following topics:

### 11.1 About Database Memory Caches and Other Memory Structures

Oracle Database stores information in memory caches and on disk. Memory access is much faster than disk access. Disk access (physical I/O) takes a significant amount of time, compared to memory access, typically in the order of 10 milliseconds. Physical I/O also increases the CPU resources required due to the path length in device drivers and operating system event schedulers. For this reason, it is more efficient for data requests of frequently accessed objects to be perform by memory, rather than also requiring disk access. Proper sizing and effective use of Oracle Database memory caches greatly improves database performance.

The main Oracle Database memory caches that affect performance include:

- Database buffer cache
	The database buffer cache stores data blocks read from disk.
- Redo log buffer
	The redo log buffer stores redo entries of changes made to data blocks in the buffer cache.
- Shared pool
	The shared pool caches many different types of data and is mainly comprised of the following components:
	- Library cache
		- Data dictionary cache
		- Server result cache
- Large pool
	The large pool provides large memory allocations for the following Oracle Database features:
	- Shared server architecture
		- Parallel query
		- Recovery Manager (RMAN)
- Java pool
	The Java pool stores session-specific Java code and Java Virtual Machine (JVM) data.
- Streams pool
	The Streams pool provides memory for Oracle Streams processes.
- Process-private memory
	Process-private memory includes memory used for operations such as sorting and hash joins.
- In-Memory Column Store (IM column store)
	Starting in Oracle Database 12c Release 1 (12.1.0.2), the IM column store is an optional, static SGA pool that stores copies of tables and partitions. In the IM column store, data is stored in a special columnar format, which improves performance of operations such as scans, joins, and aggregations.
	Note:
	The IM column store does not replace the buffer cache, but acts as a supplement so that both memory areas can store the same data in different formats.

See Also:

[Oracle Database Concepts](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/tgdba&id=CNCPT007) for information about the Oracle Database memory architecture

### 11.2 Database Memory Management Methods

The goal of memory management is to reduce the physical I/O overhead as much as possible, either by making it more likely that the required data is in memory, or by making the process of retrieving the required data more efficient. To achieve this goal, proper sizing and effective use of Oracle Database memory caches is essential.

Oracle Database provides the following methods to manage database memory:

- Automatic Memory Management
- Automatic Shared Memory Management
- Manual Shared Memory Management
- Automatic PGA Memory Management
- Manual PGA Memory Management

#### 11.2.1 Automatic Memory Management

Automatic memory management enables Oracle Database to manage and tune the database memory automatically. In automatic memory management mode, management of the shared global area (SGA) and program global area (instance PGA) memory is handled completely by Oracle Database. This method is the most automated and is strongly recommended by Oracle. Before setting any memory pool sizes manually, strongly consider using automatic memory management.

For information about using automatic memory management, see " Using Automatic Memory Management ".

#### 11.2.2 Automatic Shared Memory Management

If automatic memory management is disabled, then Oracle Database uses automatic shared memory management to manage SGA memory. In this mode, Oracle Database automatically distributes memory to individual SGA components based on a target size that you set for the total SGA memory.

For information about using automatic shared memory management, see " [Using Automatic Shared Memory Management](tuning-system-global-area.md) ".

#### 11.2.3 Manual Shared Memory Management

If both automatic memory management and automatic shared memory management are disabled, then you must manage SGA memory manually by sizing the individual memory pools in the SGA. Although this mode enables you to exercise complete control over how SGA memory is distributed, it requires the most effort because the SGA components must be manually tuned on an ongoing basis.

For information about using manual shared memory management, see " [Sizing the SGA Components Manually](tuning-system-global-area.md) ".

#### 11.2.4 Automatic PGA Memory Management

If automatic memory management is disabled, then Oracle Database uses automatic PGA memory management to manage PGA memory. In this mode, Oracle Database automatically distributes memory to work areas in the instance PGA based on a target size that you set for the total PGA memory.

For information about automatic PGA memory management, see [Tuning the Program Global Area](tuning-program-global-area.md) .

#### 11.2.5 Manual PGA Memory Management

If both automatic memory management and automatic PGA memory management are disabled, then you must manage PGA memory manually by adjusting the portion of PGA memory dedicated to each work area. This method can be very difficult because the workload is always changing and is not recommended by Oracle. Although manual PGA memory management is supported by Oracle Database, Oracle strongly recommends using automatic memory management or automatic PGA memory management instead.

### 11.3 Using Automatic Memory Management

To use automatic memory management, set the following initialization parameters:

- `MEMORY_TARGET`
	The `MEMORY_TARGET` initialization parameter specifies the target memory size. The database tunes to the value specified for this parameter, redistributing memory as needed between the SGA and the instance PGA. This parameter is dynamic, so its value can be changed at any time without restarting the database.
- `MEMORY_MAX_TARGET`
	The `MEMORY_MAX_TARGET` initialization parameter specifies the maximum memory size. The value specified for this parameter serves as the limit to which the `MEMORY_TARGET` initialization parameter can be set. This parameter is static, so its value cannot be changed after instance startup.

If you need tuning advice for the `MEMORY_TARGET` parameter, then use the `V$MEMORY_TARGET_ADVICE` view.

See Also:

[Oracle Database Administrator's Guide](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/tgdba&id=ADMIN11011) for information about using automatic memory management

### 11.4 Monitoring Memory Management

Table 11-1 lists the views that provide information about memory resize operations.

Table 11-1 Memory Management Views

| View | Description |
| --- | --- |
| `V$MEMORY_CURRENT_RESIZE_OPS` | Displays information about memory resize operations (both automatic and manual) that are currently in progress. |
| `V$MEMORY_DYNAMIC_COMPONENTS` | Displays information about the current sizes of all dynamically-tuned memory components, including the total sizes of the SGA and instance PGA. |
| `V$MEMORY_RESIZE_OPS` | Displays information about the last 800 completed memory resize operations (both automatic and manual). This does not include operations that are currently in progress. |
| `V$MEMORY_TARGET_ADVICE` | Displays tuning advice for the `MEMORY_TARGET` initialization parameter. |

See Also:

[Oracle Database Reference](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/tgdba&id=REFRN) for more information about these views