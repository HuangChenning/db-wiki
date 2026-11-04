---
title: Database Performance Tuning Guide
book: Database Performance Tuning Guide
doc_id: E85600-04
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/tgdba/tuning-system-global-area.html
tags:
  - oracle
  - 12c
  - performance-tuning-guide
---

This chapter describes how to tune the System Global Area (SGA). If you are using automatic memory management to manage the database memory on your system, then there is no need to tune the SGA as described in this chapter.

This chapter contains the following topics:

### 12.1 Using Automatic Shared Memory Management

Automatic shared memory management simplifies the configuration of the SGA by automatically distributing the memory in the SGA for the following memory pools:

- Database buffer cache (default pool)
- Shared pool
- Large pool
- Java pool
- Streams pool

Automatic shared memory management is controlled by the `SGA_TARGET` parameter. Changes in the value of the `SGA_TARGET` parameter automatically resize these memory pools. If these memory pools are set to nonzero values, then automatic shared memory management uses these values as minimum levels. Oracle recommends that you set the minimum values based on the minimum amount of memory an application component requires to function properly.

The following memory caches are manually-sized components and are not controlled by automatic shared memory management:

- Redo log buffer
	The redo log buffer is sized using the `LOG_BUFFER` initialization parameter, as described in " [Configuring the Redo Log Buffer](tuning-database-buffer-cache.md) ".
- Other buffer caches (such as `KEEP`, `RECYCLE`, and other nondefault block size)
	The `KEEP` pool is sized using the `DB_KEEP_CACHE_SIZE` initialization parameter, as described in " [Configuring the KEEP Pool](tuning-database-buffer-cache.md) ".
	The `RECYCLE` pool is sized using the `DB_RECYCLE_CACHE_SIZE` initialization parameter, as described in " [Configuring the RECYCLE Pool](tuning-database-buffer-cache.md) ".
- Fixed SGA and other internal allocations
	Fixed SGA and other internal allocations are sized using the `DB_nK_CACHE_SIZE` initialization parameter.

The memory allocated to these memory caches is deducted from the value of the `SGA_TARGET` parameter when automatic shared memory management computes the values of the automatically-tuned memory pools.

The following sections describe how to access and set the value of the `SGA_TARGET` parameter:

- User Interfaces for Setting the SGA\_TARGET Parameter
- Setting the SGA\_TARGET Parameter

See Also:

- [Oracle Database Concepts](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/tgdba&id=CNCPT802) for information about the SGA
- [Oracle Database Administrator's Guide](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/tgdba&id=ADMIN00207) for information about managing the SGA
- [Oracle Database Administrator's Guide](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/tgdba&id=ADMIN002) for information about using initialization parameters

#### 12.1.1 User Interfaces for Setting the SGA\_TARGET Parameter

This section describes the user interfaces for setting the value of the `SGA_TARGET` parameter.

This section contains the following topics:

- Setting the SGA\_TARGET Parameter in Oracle Enterprise Manager Cloud Control
- Setting the SGA\_TARGET Parameter in the Command-Line Interface

##### 12.1.1.1 Setting the SGA\_TARGET Parameter in Oracle Enterprise Manager Cloud Control

You can change the value of the `SGA_TARGET` parameter in Oracle Enterprise Manager Cloud Control (Cloud Control) by accessing the SGA Size Advisor from the Memory Parameters SGA page.

##### 12.1.1.2 Setting the SGA\_TARGET Parameter in the Command-Line Interface

You can change the value of the `SGA_TARGET` parameter in the command-line interface by querying the `V$SGA_TARGET_ADVICE` view and using the `ALTER` `SYSTEM` command.

### 12.2 Sizing the SGA Components Manually

If the system is not using automatic memory management or automatic shared memory management, then you must manually configure the sizes of the following SGA components:

- Database buffer cache
	The database buffer cache is sized using the `DB_CACHE_SIZE` initialization parameter, as described in " [Configuring the Database Buffer Cache](tuning-database-buffer-cache.md) ".
- Shared pool
	The shared pool is sized using the `SHARED_POOL_SIZE` initialization parameter, as described in " [Configuring the Shared Pool](tuning-shared-pool-and-large-pool.md) ".
- Large pool
	The large pool is sized using the `LARGE_POOL_SIZE` initialization parameter, as described in " [Configuring the Large Pool](tuning-shared-pool-and-large-pool.md) ".
- Java pool
	The Java pool is sized using the `JAVA_POOL_SIZE` initialization parameter.
- Streams pool
	The Streams pool is sized using the `STREAMS_POOL_SIZE` initialization parameter.
- IM column store
	The IM column store is sized using the `INMEMORY_SIZE` initialization parameter.

The values for these parameters are also dynamically configurable using the `ALTER` `SYSTEM` statement.

Before configuring the sizes of these SGA components, take the following considerations into account:

- SGA Sizing Unit
- Maximum Size of the SGA
- Application Considerations
- Operating System Memory Use
- Iteration During Configuration

See Also:

- [Oracle Database Java Developer's Guide](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/tgdba&id=JJDEV-GUID-0E6A9749-5505-4009-AEC6-47C84947DCFA) for information about Java memory usage and the `JAVA_POOL_SIZE` initialization parameter
- [Oracle Streams Replication Administrator's Guide](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/tgdba&id=STREP201) for information about the `STREAMS_POOL_SIZE` initialization parameter
- [Oracle Database In-Memory Guide](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/tgdba&id=INMEM-GUID-3CC8549A-A394-49CC-A907-AEB471A19CB3) for information about the `INMEMORY_SIZE` initialization parameter

#### 12.2.1 SGA Sizing Unit

Memory for the buffer cache, shared pool, large pool, and Java pool is allocated in units of granules. If the SGA size is less than 1 GB, then the granule size is 4MB. If the SGA size is greater than 1 GB, the granule size changes to 16MB. The granule size is calculated and fixed when the database instance starts up. The size does not change during the lifetime of the instance.

To view the granule size that is currently being used for the SGA, use the `V$SGA_DYNAMIC_COMPONENTS` view. The same granule size is used for all dynamic components in the SGA.

#### 12.2.2 Maximum Size of the SGA

The maximum amount of memory usable by the database instance is determined at instance startup by the value of the `SGA_MAX_SIZE` initialization parameter. You can expand the total SGA size to a value equal to the `SGA_MAX_SIZE` parameter. The value of the `SGA_MAX_SIZE` parameter defaults to the aggregate setting of all the SGA components.

If the value of the `SGA_MAX_SIZE` parameter is not set, then decrease the size of one cache and reallocate that memory to another cache if necessary. Alternatively, you can set the value of the `SGA_MAX_SIZE` parameter to be larger than the sum of all of the SGA components, such as the buffer cache and the shared pool. Doing so enables you to dynamically increase a cache size without having to decrease the size of another cache.

Note:

The value of the `SGA_MAX_SIZE` parameter cannot be dynamically resized.

#### 12.2.3 Application Considerations

When configuring memory, size the memory caches appropriately based on the application's needs. Conversely, tuning the application's use of the memory caches can greatly reduce resource requirements. Efficient use of the memory caches also reduces the load on related resources, such as latches, CPU, and the I/O system.

For optimal performance, consider the following:

- Design the cache to use the operating system and database resources in the most efficient manner.
- Allocate memory to Oracle Database memory structures to best reflect the needs of the application.
- If changes or additions are made to an existing application, resize Oracle Database memory structures to meet the needs of the modified application.
- If the application uses Java, investigate whether the default configuration for the Java pool needs to be modified.

See Also:

[Oracle Database Java Developer's Guide](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/tgdba&id=JJDEV-GUID-D660F569-3654-4C5F-9D25-5D5A3E05E9AD) for information about Java memory usage

#### 12.2.4 Operating System Memory Use

For most operating systems, it is important to consider the following when configuring memory:

- Reduce Paging
- Fit the SGA into Main Memory
- Allow Adequate Memory to Individual Users

See Also:

Your operating system hardware and software documentation, and the Oracle documentation specific to your operating system, for more information on tuning operating system memory usage

##### 12.2.4.1 Reduce Paging

Paging occurs when an operating system transfers memory-resident pages to disk solely to load new pages into memory. Many operating systems page to accommodate large amounts of information that do not fit into real memory. On most operating systems, paging reduces performance.

To determine whether significant paging is occurring on the host system, use operating system utilities to examine the operating system. If significant paging is occurring, then the total system memory may not be large enough to hold the memory caches for which memory is allocated. Consider either increasing the total memory on the system, or decreasing the amount of memory allocated.

##### 12.2.4.2 Fit the SGA into Main Memory

Because the purpose of the SGA is to store data in memory for fast access, the SGA should reside in the main memory. If pages of the SGA are swapped to disk, then the data is no longer quickly accessible. On most operating systems, the disadvantage of paging significantly outweighs the advantage of a large SGA.

This section contains the following topics:

- Viewing SGA Memory Allocation
- Locking the SGA into Physical Memory

###### 12.2.4.2.1 Viewing SGA Memory Allocation

To view how much memory is allocated to the SGA and each of its internal structures, use the `SHOW SGA` statement in SQL\*Plus as shown in the following example:

```
SQL> SHOW SGA
```

The output of this statement might look like the following:

```
Total System Global Area  840205000 bytes
Fixed Size                   279240 bytes
Variable Size             520093696 bytes
Database Buffers          318767104 bytes
Redo Buffers                1064960 bytes
```

###### 12.2.4.2.2 Locking the SGA into Physical Memory

To prevent the SGA from being paged out, consider locking the SGA into physical memory by enabling the `LOCK_SGA` parameter. The database does not use the `MEMORY_TARGET` and `MEMORY_MAX_TARGET` parameters when the `LOCK_SGA` parameter is enabled.

##### 12.2.4.3 Allow Adequate Memory to Individual Users

When sizing the SGA, ensure that you allow enough memory for the individual server processes and any other programs running on the system.

#### 12.2.5 Iteration During Configuration

Configuring memory allocation involves distributing available memory to Oracle Database memory structures, depending on the needs of the application. The distribution of memory to Oracle Database structures can affect the amount of physical I/O necessary for Oracle Database to operate properly. Having a proper initial memory configuration provides an indication of whether the I/O system is effectively configured.

After the initial pass through the memory configuration process, it may be necessary to repeat the steps of memory allocation. Subsequent passes enable you to make adjustments to earlier steps, based on changes in subsequent steps. For example, decreasing the size of the buffer cache enables you to increase the size of another memory structure, such as the shared pool.

### 12.3 Monitoring Shared Memory Management

Table 12-1 lists the views that provide information about SGA resize operations.

Table 12-1 Shared Memory Management Views

| View | Description |
| --- | --- |
| `V$SGA_CURRENT_RESIZE_OPS` | Displays information about SGA resize operations that are currently in progress. |
| `V$SGA_RESIZE_OPS` | Displays information about the last 800 completed SGA resize operations. This does not include operations that are currently in progress. |
| `V$SGA_DYNAMIC_COMPONENTS` | Displays information about the dynamic components in the SGA. This view summarizes information of all completed SGA resize operations that occurred after instance startup. |
| `V$SGA_DYNAMIC_FREE_MEMORY` | Displays information about the amount of SGA memory available for future dynamic SGA resize operations. |

See Also:

[Oracle Database Reference](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/tgdba&id=REFRN) for information about these views

### 12.4 Improving Query Performance with the In-Memory Column Store

The In-Memory Column Store (IM column store) is an optional portion of the system global area (SGA) that stores copies of tables, partitions, and other database objects in columnar format, and this columnar data is optimized for rapid scans. As the IM column store stores database objects in memory, Oracle Database can perform scans, queries, joins, and aggregates on that data much faster as compared to performing these operations on a data that is stored on a disk.

Note:

- The IM column store and database buffer cache store the same data, but in different formats. The IM column store does not replace the row-based storage in the database buffer cache, but supplements it for achieving better query performance.
- The IM column store is available starting with Oracle Database 12c Release 1 (12.1.0.2).

See Also:

[Oracle Database In-Memory Guide](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/tgdba&id=INMEM-GUID-BFA53515-7643-41E5-A296-654AB4A9F9E7) for more information about the IM column store