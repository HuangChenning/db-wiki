---
title: Managing Memory
book: "Administrator's Guide"
doc_id: E25494-07
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e25494/memory.htm
tags:
  - oracle
  - 11g
  - administrators-guide
---

## 6 Managing Memory

In this chapter:

## About Memory Management

Memory management involves maintaining optimal sizes for the Oracle Database instance memory structures as demands on the database change. The memory structures that must be managed are the system global area (SGA) and the instance program global area (instance PGA).

Oracle Database supports various memory management methods, which are chosen by initialization parameter settings. Oracle recommends that you enable the method known as automatic memory management.

Automatic Memory Management

Beginning with Release 11g, Oracle Database can manage the SGA memory and instance PGA memory completely automatically. You designate only the total memory size to be used by the instance, and Oracle Database dynamically exchanges memory between the SGA and the instance PGA as needed to meet processing demands. This capability is referred to as automatic memory management. With this memory management method, the database also dynamically tunes the sizes of the individual SGA components and the sizes of the individual PGAs.

Manual Memory Management

If you prefer to exercise more direct control over the sizes of individual memory components, you can disable automatic memory management and configure the database for manual memory management. There are a few different methods available for manual memory management. Some of these methods retain some degree of automation. The methods therefore vary in the amount of effort and knowledge required by the DBA. These methods are:

- Automatic shared memory management - for the SGA
- Manual shared memory management - for the SGA
- Automatic PGA memory management - for the instance PGA
- Manual PGA memory management - for the instance PGA

These memory management methods are described later in this chapter.

Note:

The easiest way to manage memory is to use the graphical user interface of Oracle Enterprise Manager.

To manage memory with Enterprise Manager:

1. Do one of the following:
	\- If you are using Oracle Enterprise Manager Database Control, access the Database Home page. See [Oracle Database 2 Day DBA](https://docs.oracle.com/cd/E11882_01/server.112/e10897/em_manage.htm#ADMQS033) for instructions.
	\- If you are using Oracle Enterprise Manager Grid Control, go to the desired database target. The Database Home page is displayed.
2. At the top of the page, click Server to display the Server page.
3. In the Database Configuration section, click Memory Advisors.

See Also:

[Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/cncptdba.htm#CNCPT1244) for an introduction to the various automatic and manual methods of managing memory.

## Memory Architecture Overview

The basic memory structures associated with Oracle Database include:

- System Global Area (SGA)
	The SGA is a group of shared memory structures, known as SGA components, that contain data and control information for one Oracle Database instance. The SGA is shared by all server and background processes. Examples of data stored in the SGA include cached data blocks and shared SQL areas.
- Program Global Area (PGA)
	A PGA is a memory region that contains data and control information for a server process. It is nonshared memory created by Oracle Database when a server process is started. Access to the PGA is exclusive to the server process. There is one PGA for each server process. Background processes also allocate their own PGAs. The total PGA memory allocated for all background and server processes attached to an Oracle Database instance is referred to as the total instance PGA memory, and the collection of all individual PGAs is referred to as the total instance PGA, or just instance PGA.

Figure 6-1 illustrates the relationships among these memory structures.

Figure 6-1 Oracle Database Memory Structures

![Figure 6-1 Oracle Database Memory Structures](img/admin083.gif)

> This image shows a large rectangle representing the SGA. Inside the SGA are two rows of boxes representing the SGA components. The three boxes in the top row, going from left to right, are labeled Java Pool, Redo Buffer, and Buffer Cache. The four boxes in the bottom row, going from left to right, are labeled Shared pool, Streams pool, Large pool, and Other Components. Outside the SGA is another memory component labeled Flash Cache. It is connected by a double-arrow to the Buffer Cache box inside the SGA. Outside the SGA are three boxes labeled Server Process 1, Server Process 2, and Server Process 3, and two boxes labeled Background Process. Each of these five processes is connected to the large SGA box with a double-sided arrow, indicating that each process reads from and writes to the SGA. Each process is also connected with a double-sided arrow to a small box labeled PGA. Each process has its own connected PGA box.
  

If your database is running on Solaris or Oracle Linux, you can optionally add another memory component: Database Smart Flash Cache (the flash cache). The flash cache is an extension of the SGA-resident buffer cache, providing a level 2 cache for database blocks. It can improve response time and overall throughput, especially for read-intensive online transaction processing (OLTP) workloads. The flash cache resides on one or more flash disk devices, which are solid state storage devices that use flash memory.

The flash cache is typically more economical than additional main memory, and is an order of magnitude faster than disk drives.

See Also:

- [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/memory.htm#CNCPT007) for more information on memory architecture in an Oracle Database instance
- "Configuring Database Smart Flash Cache"

## Using Automatic Memory Management

This section provides background information on the automatic memory management feature of Oracle Database, and includes instructions for enabling this feature. The following topics are covered:

- About Automatic Memory Management
- Enabling Automatic Memory Management
- Monitoring and Tuning Automatic Memory Management

### About Automatic Memory Management

The simplest way to manage instance memory is to allow the Oracle Database instance to automatically manage and tune it for you. To do so (on most platforms), you set only a target memory size initialization parameter (`MEMORY_TARGET`) and optionally a maximum memory size initialization parameter (`MEMORY_MAX_TARGET`). The total memory that the instance uses remains relatively constant, based on the value of `MEMORY_TARGET`, and the instance automatically distributes memory between the system global area (SGA) and the instance program global area (instance PGA). As memory requirements change, the instance dynamically redistributes memory between the SGA and instance PGA.

When automatic memory management is not enabled, you must size both the SGA and instance PGA manually.

Because the `MEMORY_TARGET` initialization parameter is dynamic, you can change `MEMORY_TARGET` at any time without restarting the database. `MEMORY_MAX_TARGET`, which is not dynamic, serves as an upper limit so that you cannot accidentally set `MEMORY_TARGET` too high, and so that enough memory is set aside for the database instance in case you do want to increase total instance memory in the future. Because certain SGA components either cannot easily shrink or must remain at a minimum size, the instance also prevents you from setting `MEMORY_TARGET` too low.

If you create your database with Database Configuration Assistant (DBCA) and choose the basic installation option, automatic memory management is enabled. If you choose advanced installation, Database Configuration Assistant (DBCA) enables you to select automatic memory management.

Note:

You cannot enable automatic memory management if the `LOCK_SGA` initialization parameter is `TRUE`. See [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm) for information about this parameter.

See Also:

- "Platforms That Support Automatic Memory Management"

### Enabling Automatic Memory Management

If you did not enable automatic memory management upon database creation (either by selecting the proper options in DBCA or by setting the appropriate initialization parameters for the `CREATE DATABASE` SQL statement), you can enable it at a later time. Enabling automatic memory management involves a shutdown and restart of the database.

To enable automatic memory management

1. Start SQL\*Plus and connect to the database as `SYSDBA`.
	See ["Connecting to the Database with SQL\*Plus"](dba.md) and ["Database Administrator Authentication"](dba.md) for instructions.
2. Calculate the minimum value for `MEMORY_TARGET` as follows:
	1. Determine the current sizes of `SGA_TARGET` and `PGA_AGGREGATE_TARGET` by entering the following SQL\*Plus command:
		```
		SHOW PARAMETER TARGET
		```
		SQL\*Plus displays the values of all initialization parameters with the string `TARGET` in the parameter name.
		```
		NAME                                 TYPE        VALUE
		------------------------------------ ----------- ----------------
		archive_lag_target                   integer     0
		db_flashback_retention_target        integer     1440
		fast_start_io_target                 integer     0
		fast_start_mttr_target               integer     0
		memory_max_target                    big integer 0
		memory_target                        big integer 0
		parallel_servers_target              integer     16
		pga_aggregate_target                 big integer 90M
		sga_target                           big integer 272M
		```
		2. Run the following query to determine the maximum instance PGA allocated since the database was started:
		```
		select value from v$pgastat where name='maximum PGA allocated';
		```
		3. Compute the maximum value between the query result from step 2b and `PGA_AGGREGATE_TARGET`. Add `SGA_TARGET` to this value.
		```
		memory_target = sga_target + max(pga_aggregate_target, maximum PGA allocated)
		```
	For example, if `SGA_TARGET` is 272M and `PGA_AGGREGATE_TARGET` is 90M as shown above, and if the maximum PGA allocated is determined to be 120M, then `MEMORY_TARGET` should be at least 392M (272M + 120M).
3. Choose the value for `MEMORY_TARGET` that you want to use.
	This can be the minimum value that you computed in step 2, or you can choose to use a larger value if you have enough physical memory available.
4. For the `MEMORY_MAX_TARGET` initialization parameter, decide on a maximum amount of memory that you would want to allocate to the database for the foreseeable future. That is, determine the maximum value for the sum of the SGA and instance PGA sizes. This number can be larger than or the same as the `MEMORY_TARGET` value that you chose in the previous step.
5. Do one of the following:
	- If you started your Oracle Database instance with a server parameter file, which is the default if you created the database with the Database Configuration Assistant (DBCA), enter the following command:
		```
		ALTER SYSTEM SET MEMORY_MAX_TARGET = nM SCOPE = SPFILE;
		```
		where n is the value that you computed in Step [^2].
		The `SCOPE` `=` `SPFILE` clause sets the value only in the server parameter file, and not for the running instance. You must include this `SCOPE` clause because `MEMORY_MAX_TARGET` is not a dynamic initialization parameter.
		- If you started your instance with a text initialization parameter file, manually edit the file so that it contains the following statements:
		```
		memory_max_target = nM
		memory_target = mM
		```
		where n is the value that you determined in Step [^2], and m is the value that you determined in step [^1].
	Note:
	In a text initialization parameter file, if you omit the line for `MEMORY_MAX_TARGET` and include a value for `MEMORY_TARGET`, the database automatically sets `MEMORY_MAX_TARGET` to the value of `MEMORY_TARGET`. If you omit the line for `MEMORY_TARGET` and include a value for `MEMORY_MAX_TARGET`, the `MEMORY_TARGET` parameter defaults to zero. After startup, you can then dynamically change `MEMORY_TARGET` to a nonzero value, provided that it does not exceed the value of `MEMORY_MAX_TARGET`.
6. Shut down and restart the database.
	See [Chapter 3, "Starting Up and Shutting Down"](start.md) for instructions.
7. If you started your Oracle Database instance with a server parameter file, enter the following commands:
	```
	ALTER SYSTEM SET MEMORY_TARGET = nM;
	ALTER SYSTEM SET SGA_TARGET = 0;
	ALTER SYSTEM SET PGA_AGGREGATE_TARGET = 0;
	```
	where n is the value that you determined in step [^1].

Note:

The preceding steps instruct you to set `SGA_TARGET` and `PGA_AGGREGATE_TARGET` to zero so that the sizes of the SGA and instance PGA are tuned up and down as required, without restrictions. You can omit the statements that set these parameter values to zero and leave either or both of the values as positive numbers. In this case, the values act as minimum values for the sizes of the SGA or instance PGA.

See Also:

- "About Automatic Memory Management"
- "Memory Architecture Overview"
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_2014.htm#SQLRF00902) for information on the `ALTER` `SYSTEM` SQL statement

### Monitoring and Tuning Automatic Memory Management

The dynamic performance view `V$MEMORY_DYNAMIC_COMPONENTS` shows the current sizes of all dynamically tuned memory components, including the total sizes of the SGA and instance PGA.

The view `V$MEMORY_TARGET_ADVICE` provides tuning advice for the `MEMORY_TARGET` initialization parameter.

```
SQL>  select * from v$memory_target_advice order by memory_size;
 
MEMORY_SIZE MEMORY_SIZE_FACTOR ESTD_DB_TIME ESTD_DB_TIME_FACTOR    VERSION
----------- ------------------ ------------ ------------------- ----------
        180                 .5          458               1.344          0
        270                .75          367              1.0761          0
        360                  1          341                   1          0
        450               1.25          335               .9817          0
        540                1.5          335               .9817          0
        630               1.75          335               .9817          0
        720                  2          335               .9817          0
```

The row with the `MEMORY_SIZE_FACTOR` of 1 shows the current size of memory, as set by the `MEMORY_TARGET` initialization parameter, and the amount of DB time required to complete the current workload. In previous and subsequent rows, the results show several alternative `MEMORY_TARGET` sizes. For each alternative size, the database shows the size factor (the multiple of the current size), and the estimated DB time to complete the current workload if the `MEMORY_TARGET` parameter were changed to the alternative size. Notice that for a total memory size smaller than the current `MEMORY_TARGET` size, estimated DB time increases. Notice also that in this example, there is nothing to be gained by increasing total memory size beyond 450MB. However, this situation might change if a complete workload has not yet been run.

Enterprise Manager provides an easy-to-use graphical memory advisor to help you select an optimal size for `MEMORY_TARGET`. See [Oracle Database 2 Day DBA](https://docs.oracle.com/cd/E11882_01/server.112/e10897/instance.htm#ADMQS12101) for details.

See Also:

- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm) for more information about these dynamic performance views
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/autostat.htm#PFGRF94165) for a definition of DB time.

## Configuring Memory Manually

If you prefer to exercise more direct control over the sizes of individual memory components, you can disable automatic memory management and configure the database for manual memory management. There are two different manual memory management methods for the SGA, and two for the instance PGA.

The two manual memory management methods for the SGA vary in the amount of effort and knowledge required by the DBA. With automatic shared memory management, you set target and maximum sizes for the SGA. The database then sets the total size of the SGA to your designated target, and dynamically tunes the sizes of many SGA components. With manual shared memory management, you set the sizes of several individual SGA components, thereby determining the overall SGA size. You then manually tune these individual SGA components on an ongoing basis.

For the instance PGA, there is automatic PGA memory management, in which you set a target size for the instance PGA. The database then sets the size of the instance PGA to your target, and dynamically tunes the sizes of individual PGAs. There is also manual PGA memory management, in which you set maximum work area size for each type of SQL operator (such as sort or hash-join). This memory management method, although supported, is not recommended.

The following sections provide details on all of these manual memory management methods:

- Using Automatic Shared Memory Management
- Using Manual Shared Memory Management
- Using Automatic PGA Memory Management
- Using Manual PGA Memory Management

See Also:

[Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/cncptdba.htm#CNCPT1244) for an overview of Oracle Database memory management methods.

### Using Automatic Shared Memory Management

This section contains the following topics:

- About Automatic Shared Memory Management
- Components and Granules in the SGA
- Setting Maximum SGA Size
- Setting SGA Target Size
- Enabling Automatic Shared Memory Management
- Automatic Shared Memory Management Advanced Topics

See Also:

- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/memory.htm#PFGRF014) for information about tuning the components of the SGA

#### About Automatic Shared Memory Management

Automatic Shared Memory Management simplifies SGA memory management. You specify the total amount of SGA memory available to an instance using the `SGA_TARGET` initialization parameter and Oracle Database automatically distributes this memory among the various SGA components to ensure the most effective memory utilization.

When automatic shared memory management is enabled, the sizes of the different SGA components are flexible and can adapt to the needs of a workload without requiring any additional configuration. The database automatically distributes the available memory among the various components as required, allowing the system to maximize the use of all available SGA memory.

If you are using a server parameter file (`SPFILE`), the database remembers the sizes of the automatically tuned SGA components across instance shutdowns. As a result, the database instance does not need to learn the characteristics of the workload again each time the instance is started. The instance can begin with information from the previous instance and continue evaluating workload where it left off at the last shutdown.

#### Components and Granules in the SGA

The SGA comprises several memory components, which are pools of memory used to satisfy a particular class of memory allocation requests. Examples of memory components include the shared pool (used to allocate memory for SQL and PL/SQL execution), the java pool (used for java objects and other java execution memory), and the buffer cache (used for caching disk blocks). All SGA components allocate and deallocate space in units of granules. Oracle Database tracks SGA memory use in internal numbers of granules for each SGA component.

The memory for dynamic components in the SGA is allocated in the unit of granules. The granule size is determined by the amount of SGA memory requested when the instance starts. Specifically, the granule size is based on the value of the `SGA_MAX_SIZE` initialization parameter. Table 6-1 shows the granule size for different amounts of SGA memory.

Table 6-1 Granule Size

| SGA Memory Amount | Granule Size |
| --- | --- |
| Less than or equal to 1 GB | 4 MB |
| Greater than 1 GB and less than or equal to 8 GB | 16 MB |
| Greater than 8 GB and less than or equal to 16 GB | 32 MB |
| Greater than 16 GB and less than or equal to 32 GB | 64 MB |
| Greater than 32 GB and less than or equal to 64 GB | 128 MB |
| Greater than 64 GB and less than or equal to 128 GB | 256 MB |
| Greater than 128 GB | 512 MB |

Some platform dependencies may arise. Consult your operating system specific documentation for more details.

You can query the `V$SGAINFO` view to see the granule size that is being used by an instance. The same granule size is used for all components in the SGA.

If you specify a size for a component that is not a multiple of granule size, Oracle Database rounds the specified size up to the nearest multiple. For example, if the granule size is 4 MB and you specify `DB_CACHE_SIZE` as 10 MB, the database actually allocates 12 MB.

See Also:

[Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams235.htm#REFRN10198) for more information about the `SGA_MAX_SIZE` initialization parameter

#### Setting Maximum SGA Size

The `SGA_MAX_SIZE` initialization parameter specifies the maximum size of the System Global Area for the lifetime of the instance. You can dynamically alter the initialization parameters affecting the size of the buffer caches, shared pool, large pool, Java pool, and streams pool but only to the extent that the sum of these sizes and the sizes of the other components of the SGA (fixed SGA, variable SGA, and redo log buffers) does not exceed the value specified by `SGA_MAX_SIZE`.

If you do not specify `SGA_MAX_SIZE`, then Oracle Database selects a default value that is the sum of all components specified or defaulted at initialization time. If you do specify `SGA_MAX_SIZE`, and at the time the database is initialized the value is less than the sum of the memory allocated for all components, either explicitly in the parameter file or by default, then the database ignores the setting for `SGA_MAX_SIZE` and chooses a correct value for this parameter.

#### Setting SGA Target Size

You enable the automatic shared memory management feature by setting the `SGA_TARGET` parameter to a nonzero value. This parameter sets the total size of the SGA. It replaces the parameters that control the memory allocated for a specific set of individual components, which are now automatically and dynamically resized (tuned) as needed.

Note:

The `STATISTICS_LEVEL` initialization parameter must be set to `TYPICAL` (the default) or `ALL` for automatic shared memory management to function.

Table 6-2 lists the SGA components that are automatically sized when `SGA_TARGET` is set. For each SGA component, its corresponding initialization parameter is listed.

Table 6-2 Automatically Sized SGA Components and Corresponding Parameters

| SGA Component | Initialization Parameter |
| --- | --- |
| Fixed SGA and other internal allocations needed by the Oracle Database instance | N/A |
| The shared pool | `SHARED_POOL_SIZE` |
| The large pool | `LARGE_POOL_SIZE` |
| The Java pool | `JAVA_POOL_SIZE` |
| The buffer cache | `DB_CACHE_SIZE` |
| The Streams pool | `STREAMS_POOL_SIZE` |

The manually sized parameters listed in Table 6-3, if they are set, take their memory from `SGA_TARGET`, leaving what is available for the components listed in Table 6-2.

Table 6-3 Manually Sized SGA Components that Use SGA\_TARGET Space

| SGA Component | Initialization Parameter |
| --- | --- |
| The log buffer | `LOG_BUFFER` |
| The keep and recycle buffer caches | `DB_KEEP_CACHE_SIZE`  `DB_RECYCLE_CACHE_SIZE` |
| Nonstandard block size buffer caches | `DB_` `n` `K_CACHE_SIZE` |

In addition to setting `SGA_TARGET` to a nonzero value, you must set to zero all initialization parameters listed in Table 6-2 to enable full automatic tuning of the automatically sized SGA components.

Alternatively, you can set one or more of the automatically sized SGA components to a nonzero value, which is then used as the minimum setting for that component during SGA tuning. This is discussed in detail later in this section.

Note:

An easier way to enable automatic shared memory management is to use Oracle Enterprise Manager. When you enable automatic shared memory management and set the Total SGA Size, Enterprise Manager automatically generates the `ALTER SYSTEM` statements to set `SGA_TARGET` to the specified size and to set all automatically sized SGA components to zero.

If you use SQL\*Plus to set `SGA_TARGET`, you must then set the automatically sized SGA components to zero or to a minimum value.

##### SGA and Virtual Memory

For optimal performance in most systems, the entire SGA should fit in real memory. If it does not, and if virtual memory is used to store parts of it, then overall database system performance can decrease dramatically. The reason for this is that portions of the SGA are paged (written to and read from disk) by the operating system.

See your operating system documentation for instructions for monitoring paging activity. You can also view paging activity from the Performance property page of the Host page of Enterprise Manager.

##### Monitoring and Tuning SGA Target Size

The `V$SGAINFO` view provides information on the current tuned sizes of various SGA components.

The `V$SGA_TARGET_ADVICE` view provides information that helps you decide on a value for `SGA_TARGET`.

```
SQL> select * from v$sga_target_advice order by sga_size;
 
  SGA_SIZE SGA_SIZE_FACTOR ESTD_DB_TIME ESTD_DB_TIME_FACTOR ESTD_PHYSICAL_READS
---------- --------------- ------------ ------------------- -------------------
       290              .5       448176              1.6578             1636103
       435             .75       339336              1.2552             1636103
       580               1       270344                   1             1201780
       725            1.25       239038               .8842              907584
       870             1.5       211517               .7824              513881
      1015            1.75       201866               .7467              513881
      1160               2       200703               .7424              513881
```

The information in this view is similar to that provided in the `V$MEMORY_TARGET_ADVICE` view for automatic memory management. See "Monitoring and Tuning Automatic Memory Management" for an explanation of that view.

Enterprise Manager provides an easy-to-use graphical memory advisor to help you select an optimal size for `SGA_TARGET`. See [Oracle Database 2 Day DBA](https://docs.oracle.com/cd/E11882_01/server.112/e10897/instance.htm#ADMQS0541) for details.

See Also:

[Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm) for more information about these dynamic performance views

#### Enabling Automatic Shared Memory Management

The procedure for enabling automatic shared memory management (ASMM) differs depending on whether you are changing to ASMM from manual shared memory management or from automatic memory management.

To change to ASMM from manual shared memory management:

1. Run the following query to obtain a value for `SGA_TARGET`:
	```
	SELECT (
	   (SELECT SUM(value) FROM V$SGA) -
	   (SELECT CURRENT_SIZE FROM V$SGA_DYNAMIC_FREE_MEMORY)
	   ) "SGA_TARGET"
	FROM DUAL;
	```
2. Set the value of `SGA_TARGET`, either by editing the text initialization parameter file and restarting the database, or by issuing the following statement:
	```
	ALTER SYSTEM SET SGA_TARGET=value [SCOPE={SPFILE|MEMORY|BOTH}]
	```
	where value is the value computed in step [^3] or is some value between the sum of all SGA component sizes and `SGA_MAX_SIZE`. For more information on the `ALTER` `SYSTEM` statement and its `SCOPE` clause, see [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_2014.htm#SQLRF00902).
3. Do one of the following:
	- For more complete automatic tuning, set the values of the automatically sized SGA components listed in Table 6-2 to zero. Do this by editing the text initialization parameter file or by issuing `ALTER` `SYSTEM` statements.
		- To control the minimum size of one or more automatically sized SGA components, set those component sizes to the desired value. (See the next section for details.) Set the values of the other automatically sized SGA components to zero. Do this by editing the text initialization parameter file or by issuing `ALTER` `SYSTEM` statements.

To change to ASMM from automatic memory management:

1. Set the `MEMORY_TARGET` initialization parameter to 0.
	```
	ALTER SYSTEM SET MEMORY_TARGET = 0;
	```
	The database sets `SGA_TARGET` based on current SGA memory allocation.
2. Do one of the following:
	- For more complete automatic tuning, set the sizes of the automatically sized SGA components listed in Table 6-2 to zero. Do this by editing the text initialization parameter file or by issuing `ALTER` `SYSTEM` statements.
		- To control the minimum size of one or more automatically sized SGA components, set those component sizes to the desired value. (See the next section for details.) Set the sizes of the other automatically sized SGA components to zero. Do this by editing the text initialization parameter file or by issuing `ALTER` `SYSTEM` statements.

##### Example

For example, suppose you currently have the following configuration of parameters for an instance configured for manual shared memory management and with `SGA_MAX_SIZE` set to 1200M:

- `SHARED_POOL_SIZE` = 200M
- `DB_CACHE_SIZE` = 500M
- `LARGE_POOL_SIZE` =200M

Also assume the following query results:

| Query | Result |
| --- | --- |
| `SELECT SUM(value) FROM V$SGA` | 1200M |
| `SELECT CURRENT_SIZE FROM V$SGA_DYNAMIC_FREE_MEMORY` | 208M |

You can take advantage of automatic shared memory management by setting Total SGA Size to 992M in Oracle Enterprise Manager, or by issuing the following statements:

```
ALTER SYSTEM SET SGA_TARGET = 992M;
ALTER SYSTEM SET SHARED_POOL_SIZE = 0;
ALTER SYSTEM SET LARGE_POOL_SIZE = 0;
ALTER SYSTEM SET JAVA_POOL_SIZE = 0;
ALTER SYSTEM SET DB_CACHE_SIZE = 0;
ALTER SYSTEM SET STREAMS_POOL_SIZE = 0;
```

where 992M = 1200M minus 208M.

#### Automatic Shared Memory Management Advanced Topics

This section provides a closer look at automatic shared memory management. It includes the following topics:

- Setting Minimums for Automatically Sized SGA Components
- Dynamic Modification of SGA\_TARGET
- Modifying Parameters for Automatically Sized Components
- Modifying Parameters for Manually Sized Components

##### Setting Minimums for Automatically Sized SGA Components

You can exercise some control over the size of the automatically sized SGA components by specifying minimum values for the parameters corresponding to these components. Doing so can be useful if you know that an application cannot function properly without a minimum amount of memory in specific components. You specify the minimum amount of SGA space for a component by setting a value for its corresponding initialization parameter.

Manually limiting the minimum size of one or more automatically sized components reduces the total amount of memory available for dynamic adjustment. This reduction in turn limits the ability of the system to adapt to workload changes. Therefore, this practice is not recommended except in exceptional cases. The default automatic management behavior maximizes both system performance and the use of available resources.

##### Dynamic Modification of SGA\_TARGET

The `SGA_TARGET` parameter can be dynamically increased up to the value specified for the `SGA_MAX_SIZE` parameter, and it can also be reduced. If you reduce the value of `SGA_TARGET`, the system identifies one or more automatically tuned components for which to release memory. You can reduce `SGA_TARGET` until one or more automatically tuned components reach their minimum size. Oracle Database determines the minimum allowable value for `SGA_TARGET` taking into account several factors, including values set for the automatically sized components, manually sized components that use `SGA_TARGET` space, and number of CPUs.

The change in the amount of physical memory consumed when `SGA_TARGET` is modified depends on the operating system. On some UNIX platforms that do not support dynamic shared memory, the physical memory in use by the SGA is equal to the value of the `SGA_MAX_SIZE` parameter. On such platforms, there is no real benefit in setting `SGA_TARGET` to a value smaller than `SGA_MAX_SIZE`. Therefore, setting `SGA_MAX_SIZE` on those platforms is not recommended.

On other platforms, such as Solaris and Windows, the physical memory consumed by the SGA is equal to the value of `SGA_TARGET`.

For example, suppose you have an environment with the following configuration:

- `SGA_MAX_SIZE` = 1024M
- `SGA_TARGET` = 512M
- `DB_8K_CACHE_SIZE` = 128M

In this example, the value of `SGA_TARGET` can be resized up to 1024M and can also be reduced until one or more of the automatically sized components reaches its minimum size. The exact value depends on environmental factors such as the number of CPUs on the system. However, the value of `DB_8K_CACHE_SIZE` remains fixed at all times at 128M

Note:

When enabling automatic shared memory management, it is best to set `SGA_TARGET` to the desired nonzero value before starting the database. Dynamically modifying `SGA_TARGET` from zero to a nonzero value may not achieve the desired results because the shared pool may not be able to shrink. After startup, you can dynamically tune `SGA_TARGET` up or down as required.

##### Modifying Parameters for Automatically Sized Components

When `SGA_TARGET` is not set, the automatic shared memory management feature is not enabled. Therefore the rules governing resize for all component parameters are the same as in earlier releases. However, when automatic shared memory management is enabled, the manually specified sizes of automatically sized components serve as a lower bound for the size of the components. You can modify this limit dynamically by changing the values of the corresponding parameters.

If the specified lower limit for the size of a given SGA component is less than its current size, there is no immediate change in the size of that component. The new setting only limits the automatic tuning algorithm to that reduced minimum size in the future. For example, consider the following configuration:

- `SGA_TARGET` = 512M
- `LARGE_POOL_SIZE` = 256M
- Current actual large pool size = 284M

In this example, if you increase the value of `LARGE_POOL_SIZE` to a value greater than the actual current size of the component, the system expands the component to accommodate the increased minimum size. For example, if you increase the value of `LARGE_POOL_SIZE` to 300M, then the system increases the large pool incrementally until it reaches 300M. This resizing occurs at the expense of one or more automatically tuned components.If you decrease the value of `LARGE_POOL_SIZE` to 200, there is no immediate change in the size of that component. The new setting only limits the reduction of the large pool size to 200 M in the future.

##### Modifying Parameters for Manually Sized Components

Parameters for manually sized components can be dynamically altered as well. However, rather than setting a minimum size, the value of the parameter specifies the precise size of the corresponding component. When you increase the size of a manually sized component, extra memory is taken away from one or more automatically sized components. When you decrease the size of a manually sized component, the memory that is released is given to the automatically sized components.

For example, consider this configuration:

- `SGA_TARGET` = 512M
- `DB_8K_CACHE_SIZE` = 128M

In this example, increasing `DB_8K_CACHE_SIZE` by 16M to 144M means that the 16M is taken away from the automatically sized components. Likewise, reducing `DB_8K_CACHE_SIZE` by 16M to 112M means that the 16M is given to the automatically sized components.

### Using Manual Shared Memory Management

If you decide not to use automatic memory management or automatic shared memory management, you must manually configure several SGA component sizes, and then monitor and tune these sizes on an ongoing basis as the database workload changes. This section provides guidelines on setting the parameters that control the sizes of these SGA components.

If you create your database with DBCA and choose manual shared memory management, DBCA provides fields where you must enter sizes for the buffer cache, shared pool, large pool, and Java pool. It then sets the corresponding initialization parameters in the server parameter file (`SPFILE`) that it creates. If you instead create the database with the `CREATE DATABASE` SQL statement and a text initialization parameter file, you can do one of the following:

- Provide values for the initialization parameters that set SGA component sizes.
- Omit SGA component size parameters from the text initialization file. Oracle Database chooses reasonable defaults for any component whose size you do not set.

This section contains the following topics:

- Enabling Manual Shared Memory Management
- Setting the Buffer Cache Initialization Parameters
- Specifying the Shared Pool Size
- Specifying the Large Pool Size
- Specifying the Java Pool Size
- Specifying the Streams Pool Size
- Specifying the Result Cache Maximum Size
- Specifying Miscellaneous SGA Initialization Parameters

#### Enabling Manual Shared Memory Management

There is no initialization parameter that in itself enables manual shared memory management. You effectively enable manual shared memory management by disabling both automatic memory management and automatic shared memory management.

To enable manual shared memory management:

1. Set the `MEMORY_TARGET` initialization parameter to 0.
2. Set the `SGA_TARGET` initialization parameter to 0.

You must then set values for the various SGA components, as described in the following sections.

#### Setting the Buffer Cache Initialization Parameters

The buffer cache initialization parameters determine the size of the buffer cache component of the SGA. You use them to specify the sizes of caches for the various block sizes used by the database. These initialization parameters are all dynamic.

The size of a buffer cache affects performance. Larger cache sizes generally reduce the number of disk reads and writes. However, a large cache may take up too much memory and induce memory paging or swapping.

Oracle Database supports multiple block sizes in a database. If you create tablespaces with nonstandard block sizes, you must configure nonstandard block size buffers to accommodate these tablespaces. The standard block size is used for the `SYSTEM` tablespace. You specify the standard block size by setting the initialization parameter `DB_BLOCK_SIZE`. Legitimate values are from 2K to 32K.

If you intend to use multiple block sizes in your database, you must have the `DB_CACHE_SIZE` and at least one `DB_` `n` `K_CACHE_SIZE` parameter set. Oracle Database assigns an appropriate default value to the `DB_CACHE_SIZE` parameter, but the `DB_` `n` `K_CACHE_SIZE` parameters default to 0, and no additional block size caches are configured.

The sizes and numbers of nonstandard block size buffers are specified by the following parameters:

```
DB_2K_CACHE_SIZE
DB_4K_CACHE_SIZE
DB_8K_CACHE_SIZE
DB_16K_CACHE_SIZE
DB_32K_CACHE_SIZE
```

Each parameter specifies the size of the cache for the corresponding block size.

Note:

- Platform-specific restrictions regarding the maximum block size apply, so some of these sizes might not be allowed on some platforms.
- A 32K block size is valid only on 64-bit platforms.

See Also:

["Specifying Nonstandard Block Sizes for Tablespaces"](tspaces.md)

##### Example of Setting Block and Cache Sizes

```
DB_BLOCK_SIZE=4096
DB_CACHE_SIZE=1024M
DB_2K_CACHE_SIZE=256M
DB_8K_CACHE_SIZE=512M
```

In the preceding example, the parameter `DB_BLOCK_SIZE` sets the standard block size of the database to 4K. The size of the cache of standard block size buffers is 1024MB. Additionally, 2K and 8K caches are also configured, with sizes of 256MB and 512MB, respectively.

Note:

The `DB_` `n` `K_CACHE_SIZE` parameters cannot be used to size the cache for the standard block size. If the value of `DB_BLOCK_SIZE` is nK, it is invalid to set `DB_` `n` `K_CACHE_SIZE`. The size of the cache for the standard block size is always determined from the value of `DB_CACHE_SIZE`.

The cache has a limited size, so not all the data on disk can fit in the cache. When the cache is full, subsequent cache misses cause Oracle Database to write dirty data already in the cache to disk to make room for the new data. (If a buffer is not dirty, it does not need to be written to disk before a new block can be read into the buffer.) Subsequent access to any data that was written to disk and then overwritten results in additional cache misses.

The size of the cache affects the likelihood that a request for data results in a cache hit. If the cache is large, it is more likely to contain the data that is requested. Increasing the size of a cache increases the percentage of data requests that result in cache hits.

You can change the size of the buffer cache while the instance is running, without having to shut down the database. Do this with the `ALTER` `SYSTEM` statement.

Use the fixed view `V$BUFFER_POOL` to track the sizes of the different cache components and any pending resize operations.

##### Multiple Buffer Pools

You can configure the database buffer cache with separate buffer pools that either keep data in the buffer cache or make the buffers available for new data immediately after using the data blocks. Particular schema objects (tables, clusters, indexes, and partitions) can then be assigned to the appropriate buffer pool to control the way their data blocks age out of the cache.

- The `KEEP` buffer pool retains the schema object's data blocks in memory.
- The `RECYCLE` buffer pool eliminates data blocks from memory as soon as they are no longer needed.
- The `DEFAULT` buffer pool contains data blocks from schema objects that are not assigned to any buffer pool, as well as schema objects that are explicitly assigned to the `DEFAULT` pool.

The initialization parameters that configure the `KEEP` and `RECYCLE` buffer pools are `DB_KEEP_CACHE_SIZE` and `DB_RECYCLE_CACHE_SIZE`.

Note:

Multiple buffer pools are only available for the standard block size. Nonstandard block size caches have a single `DEFAULT` pool.

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/memory.htm#PFGRF94265) for information about tuning the buffer cache and for more information about multiple buffer pools

#### Specifying the Shared Pool Size

The `SHARED_POOL_SIZE` initialization parameter is a dynamic parameter that lets you specify or adjust the size of the shared pool component of the SGA. Oracle Database selects an appropriate default value.

In releases before Oracle Database 10g Release 1, the amount of shared pool memory that was allocated was equal to the value of the `SHARED_POOL_SIZE` initialization parameter plus the amount of internal SGA overhead computed during instance startup. The internal SGA overhead refers to memory that is allocated by Oracle Database during startup, based on the values of several other initialization parameters. This memory is used to maintain state for different server components in the SGA. For example, if the `SHARED_POOL_SIZE` parameter is set to 64MB and the internal SGA overhead is computed to be 12MB, the real size of the shared pool is 64+12=76MB, although the value of the `SHARED_POOL_SIZE` parameter is still displayed as 64MB.

Starting with Oracle Database 10g Release 1, the size of the internal SGA overhead is included in the user-specified value of `SHARED_POOL_SIZE`. If you are not using automatic memory management or automatic shared memory management, the amount of shared pool memory that is allocated at startup is equal to the value of the `SHARED_POOL_SIZE` initialization parameter, rounded up to a multiple of the granule size. You must therefore set this parameter so that it includes the internal SGA overhead in addition to the desired value for shared pool size. In the previous example, if the `SHARED_POOL_SIZE` parameter is set to 64MB at startup, then the available shared pool after startup is 64-12=52MB, assuming the value of internal SGA overhead remains unchanged. In order to maintain an effective value of 64MB for shared pool memory after startup, you must set the `SHARED_POOL_SIZE` parameter to 64+12=76MB.

When migrating from a release that is earlier than Oracle Database 10g Release 1, the Oracle Database 11g migration utilities recommend a new value for this parameter based on the value of internal SGA overhead in the pre-upgrade environment and based on the old value of this parameter. Beginning with Oracle Database 10g, the exact value of internal SGA overhead, also known as startup overhead in the shared pool, can be queried from the `V$SGAINFO` view. Also, in manual shared memory management mode, if the user-specified value of `SHARED_POOL_SIZE` is too small to accommodate even the requirements of internal SGA overhead, then Oracle Database generates an `ORA-00371` error during startup, with a suggested value to use for the `SHARED_POOL_SIZE` parameter.When you use automatic shared memory management in Oracle Database 11g, the shared pool is automatically tuned, and an `ORA-00371` error would not be generated.

##### The Result Cache and Shared Pool Size

The result cache takes its memory from the shared pool. Therefore, if you expect to increase the maximum size of the result cache, take this into consideration when sizing the shared pool.

See Also:

"Specifying the Result Cache Maximum Size"

#### Specifying the Large Pool Size

The `LARGE_POOL_SIZE` initialization parameter is a dynamic parameter that lets you specify or adjust the size of the large pool component of the SGA. The large pool is an optional component of the SGA. You must specifically set the `LARGE_POOL_SIZE` parameter to create a large pool. Configuring the large pool is discussed in [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/memory.htm#PFGRF014).

#### Specifying the Java Pool Size

The `JAVA_POOL_SIZE` initialization parameter is a dynamic parameter that lets you specify or adjust the size of the java pool component of the SGA. Oracle Database selects an appropriate default value. Configuration of the java pool is discussed in [Oracle Database Java Developer's Guide](https://docs.oracle.com/cd/E11882_01/java.112/e10588/chnine.htm#JJDEV09200).

#### Specifying the Streams Pool Size

The `STREAMS_POOL_SIZE` initialization parameter is a dynamic parameter that lets you specify or adjust the size of the Streams Pool component of the SGA. If `STREAMS_POOL_SIZE` is set to 0, then the Oracle Streams product transfers memory from the buffer cache to the Streams Pool when it is needed. For details, see the discussion of the Streams Pool in [Oracle Streams Replication Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10705/prep_rep.htm#STREP202).

#### Specifying the Result Cache Maximum Size

The `RESULT_CACHE_MAX_SIZE` initialization parameter is a dynamic parameter that enables you to specify the maximum size of the result cache component of the SGA. Typically, there is no need to specify this parameter, because the default maximum size is chosen by the database based on total memory available to the SGA and on the memory management method currently in use. You can view the current default maximum size by displaying the value of the `RESULT_CACHE_MAX_SIZE` parameter. To change this maximum size, you can set `RESULT_CACHE_MAX_SIZE` with an `ALTER` `SYSTEM` statement, or you can specify this parameter in the text initialization parameter file. In each case, the value is rounded up to the nearest multiple of 32K.

If `RESULT_CACHE_MAX_SIZE` is 0 upon instance startup, the result cache is disabled. To reenable it you must set `RESULT_CACHE_MAX_SIZE` to a nonzero value (or remove this parameter from the text initialization parameter file to get the default maximum size) and then restart the database.

Note that after starting the database with the result cache disabled, if you use an `ALTER` `SYSTEM` statement to set `RESULT_CACHE_MAX_SIZE` to a nonzero value but do not restart the database, querying the value of the `RESULT_CACHE_MAX_SIZE` parameter returns a nonzero value even though the result cache is still disabled. The value of `RESULT_CACHE_MAX_SIZE` is therefore not the most reliable way to determine if the result cache is enabled. You can use the following query instead:

```
SELECT dbms_result_cache.status() FROM dual;

DBMS_RESULT_CACHE.STATUS()
---------------------------------------------
ENABLED
```

The result cache takes its memory from the shared pool, so if you increase the maximum result cache size, consider also increasing the shared pool size.

The view `V$RESULT_CACHE_STATISTICS` and the PL/SQL package procedure `DBMS_RESULT_CACHE.MEMORY_REPORT` display information to help you determine the amount of memory currently allocated to the result cache.

The PL/SQL package function `DBMS_RESULT_CACHE.FLUSH` clears the result cache and releases all the memory back to the shared pool.

See Also:

- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/memory.htm#PFGRF986) for more information about the result cache
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_result_cache.htm#ARPLS202) for more information about the `DBMS_RESULT_CACHE` package procedures and functions.
- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2141.htm#REFRN30439) for more information about the `V$RESULT_CACHE_STATISTICS` view.
- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/admin.htm#RACAD017) for information on setting `RESULT_CACHE_MAX_SIZE` for a cluster database.

#### Specifying Miscellaneous SGA Initialization Parameters

You can set a few additional initialization parameters to control how the SGA uses memory.

##### Physical Memory

The `LOCK_SGA` parameter, when set to `TRUE`, locks the entire SGA into physical memory. This parameter cannot be used with automatic memory management.

##### SGA Starting Address

The `SHARED_MEMORY_ADDRESS` and `HI_SHARED_MEMORY_ADDRESS` parameters specify the SGA's starting address at run time. These parameters are rarely used. For 64-bit platforms, `HI_SHARED_MEMORY_ADDRESS` specifies the high order 32 bits of the 64-bit address.

##### Extended Buffer Cache Mechanism

The `USE_INDIRECT_DATA_BUFFERS` parameter enables the use of the extended buffer cache mechanism for 32-bit platforms that can support more than 4 GB of physical memory. On platforms that do not support this much physical memory, this parameter is ignored. This parameter cannot be used with automatic memory management or automatic shared memory management.

See Also:

- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm) for more information on these initialization parameters
- "Using Automatic Memory Management"
- "Using Automatic Shared Memory Management"

### Using Automatic PGA Memory Management

By default, Oracle Database automatically and globally manages the total amount of memory dedicated to the instance PGA. You can control this amount by setting the initialization parameter `PGA_AGGREGATE_TARGET`. Oracle Database then tries to ensure that the total amount of PGA memory allocated across all database server processes and background processes never exceeds this target.

If you create your database with DBCA, you can specify a value for the total instance PGA. DBCA then sets the `PGA_AGGREGATE_TARGET` initialization parameters in the server parameter file (`SPFILE`) that it creates. If you do not specify the total instance PGA, DBCA chooses a reasonable default.

If you create the database with the `CREATE DATABASE` SQL statement and a text initialization parameter file, you can provide a value for `PGA_AGGREGATE_TARGET`. If you omit this parameter, the database chooses a default value.

With automatic PGA memory management, sizing of SQL work areas for all dedicated server sessions is automatic and all `*_AREA_SIZE` initialization parameters are ignored for these sessions. At any given time, the total amount of PGA memory available to active work areas on the instance is automatically derived from the parameter `PGA_AGGREGATE_TARGET`. This amount is set to the value of `PGA_AGGREGATE_TARGET` minus the PGA memory allocated for other purposes (for example, session memory). The resulting PGA memory is then allotted to individual active work areas based on their specific memory requirements.

There are dynamic performance views that provide PGA memory use statistics. Most of these statistics are enabled when `PGA_AGGREGATE_TARGET` is set.

- Statistics on allocation and use of work area memory can be viewed in the following dynamic performance views:

`V$SYSSTAT`

`V$SESSTAT`

`V$PGASTAT`

`V$SQL_WORKAREA`

`V$SQL_WORKAREA_ACTIVE`

- The following three columns in the `V$PROCESS` view report the PGA memory allocated and used by an Oracle Database process:

`PGA_USED_MEM`

`PGA_ALLOC_MEM`

`PGA_MAX_MEM`

Note:

The automatic PGA memory management method applies to work areas allocated by both dedicated and shared server process. See [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/memory.htm#CNCPT1243) for information about PGA memory allocation in dedicated and shared server modes.

See Also:

- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_part.htm#REFRN003) for information about views mentioned in this section
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/memory.htm#PFGRF94351) for information about using these views

### Using Manual PGA Memory Management

Oracle Database supports manual PGA memory management, in which you manually tune SQL work areas.

In releases earlier than Oracle Database 10g, the database administrator controlled the maximum size of SQL work areas by setting the following parameters: `SORT_AREA_SIZE`, `HASH_AREA_SIZE`, `BITMAP_MERGE_AREA_SIZE` and `CREATE_BITMAP_AREA_SIZE`. Setting these parameters is difficult, because the maximum work area size is ideally selected from the data input size and the total number of work areas active in the system. These two factors vary greatly from one work area to another and from one time to another. Thus, the various `*_AREA_SIZE` parameters are difficult to tune under the best of circumstances.

For this reason, Oracle strongly recommends that you leave automatic PGA memory management enabled.

If you decide to tune SQL work areas manually, you must set the `WORKAREA_SIZE_POLICY` initialization parameter to `MANUAL`.

Note:

The initialization parameter `WORKAREA_SIZE_POLICY` is a session- and system-level parameter that can take only two values: `MANUAL` or `AUTO`. The default is `AUTO`. You can set `PGA_AGGREGATE_TARGET`, and then switch back and forth from auto to manual memory management mode. When `WORKAREA_SIZE_POLICY` is set to `AUTO`, your settings for `*_AREA_SIZE` parameters are ignored.

## Configuring Database Smart Flash Cache

This section contains the following topics on configuring Database Smart Flash Cache (the flash cache):

- When to Configure the Flash Cache
- Sizing the Flash Cache
- Tuning Memory for the Flash Cache
- Flash Cache Initialization Parameters
- Flash Cache in an Oracle Real Applications Clusters Environment

See Also:

"Memory Architecture Overview" for a description of the flash cache

### When to Configure the Flash Cache

Consider adding the flash cache when all of the following are true:

- Your database is running on the Solaris or Oracle Linux operating systems. The flash cache is supported on these operating systems only.
- The Buffer Pool Advisory section of your Automatic Workload Repository (AWR) report or STATSPACK report indicates that doubling the size of the buffer cache would be beneficial.
- `db` `file` `sequential` `read` is a top wait event.
- You have spare CPU.

Note:

You cannot share the flash cache among multiple instances.

### Sizing the Flash Cache

As a general rule, size the flash cache to be between 2 times and 10 times the size of the buffer cache. Any multiplier less than two would not provide any benefit. If you are using automatic shared memory management, make the flash cache between 2 times and 10 times the size of `SGA_TARGET`. Using 80% of the size of `SGA_TARGET` instead of the full size would also suffice for this calculation.

### Tuning Memory for the Flash Cache

For each database block moved from the buffer cache to the flash cache, a small amount of metadata about the block is kept in the buffer cache. For a single instance database, the metadata consumes approximately 100 bytes. For an Oracle Real Application Clusters (Oracle RAC) database, it is closer to 200 bytes. You must therefore take this extra memory requirement into account when adding the flash cache.

- If you are managing memory manually, increase the size of the buffer cache by an amount approximately equal to the number of database blocks that fit into the flash cache multiplied by 100 (or 200 for Oracle RAC).
- If you are using automatic memory management, increase the size of `MEMORY_TARGET` using the algorithm described above. You may first have to increase the size of `MEMORY_MAX_TARGET`.
- If you are using automatic shared memory management, increase the size of `SGA_TARGET`.

Also, for an Oracle RAC database that uses the flash cache, additional memory must be allocated to the shared pool for Global Cache Service (GCS) resources. Each GCS resource requires approximately 208 bytes in the shared pool.

Note:

You can choose to not increase the buffer cache size to account for the flash cache. In this case, the effective size of the buffer cache is reduced. However, you can offset this loss by using a larger flash cache.

### Flash Cache Initialization Parameters

Table 6-4 describes the initialization parameters that you use to configure the flash cache.

Table 6-4 Flash Cache Initialization Parameters

| Parameter | Description |
| --- | --- |
| `db_flash_cache_file` | Specifies the path and file name for the file to contain the flash cache, in either the operating system file system or an Oracle Automatic Storage Management disk group. If the file does not exist, the database creates it during startup. The file must reside on a flash disk device. If you configure the flash cache on a disk drive (spindle), performance may suffer.  The following is an example of a valid value for `db_flash_cache_file`:  ``` /dev/fioa1 ``` |
| `db_flash_cache_size` | Specifies the size of the flash cache. Must be less than or equal to the physical memory size of the flash disk device. Expressed as nG, indicating the number of gigabytes (GB). For example, to specify a 16 GB flash cache, set `db_flash_cache_size` to 16G. |

You can use `ALTER` `SYSTEM` to set `db_flash_cache_size` to zero to disable the flash cache. You can also use `ALTER` `SYSTEM` to set the flash cache back to its original size to reenable it. However, dynamically changing the size of the flash cache is not supported.

### Flash Cache in an Oracle Real Applications Clusters Environment

You must configure a flash cache on either all or none of the instances in an Oracle Real Application Clusters environment.

## Memory Management Reference

This section contains the following reference topics for memory management:

- Platforms That Support Automatic Memory Management
- Memory Management Data Dictionary Views

### Platforms That Support Automatic Memory Management

The following platforms support automatic memory management—the Oracle Database ability to automatically tune the sizes of the SGA and PGA, redistributing memory from one to the other on demand to optimize performance:

- Linux
- Solaris
- Windows
- HP-UX
- AIX

### Memory Management Data Dictionary Views

The following dynamic performance views provide information on memory management:

| View | Description |
| --- | --- |
| `V$SGA` | Displays summary information about the system global area (SGA). |
| `V$SGAINFO` | Displays size information about the SGA, including the sizes of different SGA components, the granule size, and free memory. |
| `V$SGASTAT` | Displays detailed information about how memory is allocated within the shared pool, large pool, Java pool, and Streams pool. |
| `V$PGASTAT` | Displays PGA memory usage statistics as well as statistics about the automatic PGA memory manager when it is enabled (that is, when `PGA_AGGREGATE_TARGET` is set). Cumulative values in `V$PGASTAT` are accumulated since instance startup. |
| `V$MEMORY_DYNAMIC_COMPONENTS` | Displays information on the current size of all automatically tuned and static memory components, with the last operation (for example, grow or shrink) that occurred on each. |
| `V$SGA_DYNAMIC_COMPONENTS` | Displays the current sizes of all SGA components, and the last operation for each component. |
| `V$SGA_DYNAMIC_FREE_MEMORY` | Displays information about the amount of SGA memory available for future dynamic SGA resize operations. |
| `V$MEMORY_CURRENT_RESIZE_OPS` | Displays information about resize operations that are currently in progress. A resize operation is an enlargement or reduction of the SGA, the instance PGA, or a dynamic SGA component. |
| `V$SGA_CURRENT_RESIZE_OPS` | Displays information about dynamic SGA component resize operations that are currently in progress. |
| `V$MEMORY_RESIZE_OPS` | Displays information about the last 800 completed memory component resize operations, including automatic grow and shrink operations for `SGA_TARGET` and `PGA_AGGREGATE_TARGET`. |
| `V$SGA_RESIZE_OPS` | Displays information about the last 800 completed SGA component resize operations. |
| `V$MEMORY_TARGET_ADVICE` | Displays information that helps you tune `MEMORY_TARGET` if you enabled automatic memory management. |
| `V$SGA_TARGET_ADVICE` | Displays information that helps you tune `SGA_TARGET`. |
| `V$PGA_TARGET_ADVICE` | Displays information that helps you tune `PGA_AGGREGATE_TARGET`. |

See Also:

[Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm) for detailed information on memory management views.

[^1]: Choose the value for `MEMORY_TARGET` that you want to use.

This can be the minimum value that you computed in step 2, or you can choose to use a larger value if you have enough physical memory available.

[^2]: For the `MEMORY_MAX_TARGET` initialization parameter, decide on a maximum amount of memory that you would want to allocate to the database for the foreseeable future. That is, determine the maximum value for the sum of the SGA and instance PGA sizes. This number can be larger than or the same as the `MEMORY_TARGET` value that you chose in the previous step.

[^undefined]: Do one of the following:

- If you started your Oracle Database instance with a server parameter file, which is the default if you created the database with the Database Configuration Assistant (DBCA), enter the following command:
	```
	ALTER SYSTEM SET MEMORY_MAX_TARGET = nM SCOPE = SPFILE;
	```
	where n is the value that you computed in Step 4.
	The `SCOPE` `=` `SPFILE` clause sets the value only in the server parameter file, and not for the running instance. You must include this `SCOPE` clause because `MEMORY_MAX_TARGET` is not a dynamic initialization parameter.
- If you started your instance with a text initialization parameter file, manually edit the file so that it contains the following statements:
	```
	memory_max_target = nM
	memory_target = mM
	```
	where n is the value that you determined in Step 4, and m is the value that you determined in step 3.

Note:

In a text initialization parameter file, if you omit the line for `MEMORY_MAX_TARGET` and include a value for `MEMORY_TARGET`, the database automatically sets `MEMORY_MAX_TARGET` to the value of `MEMORY_TARGET`. If you omit the line for `MEMORY_TARGET` and include a value for `MEMORY_MAX_TARGET`, the `MEMORY_TARGET` parameter defaults to zero. After startup, you can then dynamically change `MEMORY_TARGET` to a nonzero value, provided that it does not exceed the value of `MEMORY_MAX_TARGET`.

[^undefined]: Shut down and restart the database.

See [Chapter 3, "Starting Up and Shutting Down"](start.md) for instructions.

[^undefined]: If you started your Oracle Database instance with a server parameter file, enter the following commands:

```
ALTER SYSTEM SET MEMORY_TARGET = nM;
ALTER SYSTEM SET SGA_TARGET = 0;
ALTER SYSTEM SET PGA_AGGREGATE_TARGET = 0;
```

where n is the value that you determined in step 3.

[^3]: Run the following query to obtain a value for `SGA_TARGET`:

```
SELECT (
   (SELECT SUM(value) FROM V$SGA) -
   (SELECT CURRENT_SIZE FROM V$SGA_DYNAMIC_FREE_MEMORY)
   ) "SGA_TARGET"
FROM DUAL;
```