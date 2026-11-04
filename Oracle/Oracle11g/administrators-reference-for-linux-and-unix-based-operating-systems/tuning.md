---
title: Tuning Oracle Database
book: "Administrator's Reference for Linux and UNIX-Based Operating Systems"
doc_id: E10839-25
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e10839/tuning.htm
tags:
  - oracle
  - 11g
  - administrators-reference-for-linux-and-unix-based-operating-systems
---

## 8 Tuning Oracle Database

This chapter describes how to tune Oracle Database. It contains the following sections:

## 8.1 Importance of Tuning

The intent of this section is to efficiently tune and optimize the performance of Oracle Database. Frequent tuning enhances system performance and prevents data bottlenecks.

Before tuning the database, you must observe its normal behavior by using the tools described in the "Operating System Tools" section.

## 8.2 Operating System Tools

Several operating system tools are available to enable you to assess database performance and determine database requirements. In addition to providing statistics for Oracle processes, these tools provide statistics for CPU usage, interrupts, swapping, paging, context switching, and Input-Output for the entire system.

This section provides information about the following common tools:

- vmstat
- sar
- iostat
- swap, swapinfo, swapon, or lsps
- AIX Tools
- HP-UX Tools
- Linux Tools
- Solaris Tools

See Also:

The operating system documentation and man pages for more information about these tools

### 8.2.1 vmstat

Use the `vmstat` command to view process, virtual memory, disk, trap, and CPU activity, depending on the switches that you supply with the command. Run one of the following commands to display a summary of CPU activity six times, at five-second intervals:

- On HP-UX and Solaris:
	```
	$ vmstat -S 5 6
	```
- On AIX and Linux:
	```
	$ vmstat 5 6
	```

The following is sample output of this command on HP-UX:

```
procs     memory            page            disk          faults      cpu
 r b w   swap  free  si  so pi po fr de sr f0 s0 s1 s3   in   sy   cs us sy id
 0 0 0   1892  5864   0   0  0  0  0  0  0  0  0  0  0   90   74   24  0  0 99
 0 0 0  85356  8372   0   0  0  0  0  0  0  0  0  0  0   46   25   21  0  0 100
 0 0 0  85356  8372   0   0  0  0  0  0  0  0  0  0  0   47   20   18  0  0 100
 0 0 0  85356  8372   0   0  0  0  0  0  0  0  0  0  2   53   22   20  0  0 100
 0 0 0  85356  8372   0   0  0  0  0  0  0  0  0  0  0   87   23   21  0  0 100
 0 0 0  85356  8372   0   0  0  0  0  0  0  0  0  0  0   48   41   23  0  0 100
```

The `w` sub column, under the `procs` column, shows the number of potential processes that have been swapped out and written to disk. If the value is not zero, then swapping occurs and the system is short of memory.

The `si` and `so` columns under the `page` column indicate the number of swap-ins and swap-outs per second, respectively. Swap-ins and swap-outs should always be zero.

The `sr` column under the `page` column indicates the scan rate. High scan rates are caused by a shortage of available memory.

The `pi` and `po` columns under the `page` column indicate the number of page-ins and page-outs per second, respectively. It is normal for the number of page-ins and page-outs to increase. Some paging always occurs even on systems with sufficient available memory.

Note:

The output from the `vmstat` command differs across platforms.

See Also:

Refer to the man page for information about interpreting the output

### 8.2.2 sar

Depending on the switches that you supply with the command, use the `sar` (system activity reporter) command to display cumulative activity counters in the operating system.

On an HP-UX system, the following command displays a summary of Input-Output activity every ten seconds:

```
$ sar -b 10 10
```

The following example shows the output of this command:

```
13:32:45 bread/s lread/s %rcache bwrit/s lwrit/s %wcache pread/s pwrit/s
13:32:55       0      14     100       3      10      69       0       0
13:33:05       0      12     100       4       4       5       0       0
13:33:15       0       1     100       0       0       0       0       0
13:33:25       0       1     100       0       0       0       0       0
13:33:35       0      17     100       5       6       7       0       0
13:33:45       0       1     100       0       0       0       0       0
13:33:55       0       9     100       2       8      80       0       0
13:34:05       0      10     100       4       4       5       0       0
13:34:15       0       7     100       2       2       0       0       0
13:34:25       0       0     100       0       0     100       0       0

Average        0       7     100       2       4      41       0       0
```

The `sar` output provides a snapshot of system Input-Output activity at a given point in time. If you specify the interval time with multiple options, then the output can become difficult to read. If you specify an interval time of less than 5, then the `sar` activity itself can affect the output.

See Also:

The man page for more information about `sar`

### 8.2.3 iostat

Use the `iostat` command to view terminal and disk activity, depending on the switches that you supply with the command. The output from the `iostat` command does not include disk request queues, but it shows which disks are busy. You can use this information to balance the Input-Output loads.

The following command displays terminal and disk activity five times, at five-second intervals:

```
$ iostat 5 5
```

The following is sample output of the command on Solaris:

```
tty          fd0           sd0           sd1           sd3          cpu
 tin tout Kps tps serv  Kps tps serv  Kps tps serv  Kps tps serv  us sy wt id
   0    1   0   0    0    0   0   31    0   0   18    3   0   42   0  0  0 99
   0   16   0   0    0    0   0    0    0   0    0    1   0   14   0  0  0 100
   0   16   0   0    0    0   0    0    0   0    0    0   0    0   0  0  0 100
   0   16   0   0    0    0   0    0    0   0    0    0   0    0   0  0  0 100
   0   16   0   0    0    0   0    0    2   0   14   12   2   47   0  0  1 98
```

Use the `iostat` command to look for large disk request queues. A request queue shows how long the Input-Output requests on a particular disk device must wait to be serviced. Request queues are caused by a high volume of Input-Output requests to that disk or by Input-Output with long average seek times. Ideally, disk request queues should be at or near zero.

### 8.2.4 swap, swapinfo, swapon, or lsps

Use the `swap`, `swapinfo`, `swapon`, or `lsps` command to report information about swap space usage. A shortage of swap space can stop processes responding, leading to process failures with `Out of Memory` errors. The following table lists the appropriate command to use for each platform:

| Platform | Command |
| --- | --- |
| AIX | `lsps -a` |
| HP-UX | `swapinfo -m` |
| Linux | `swapon -s` |
| Solaris | `swap -l` and `swap -s` |

The following example shows sample output from the `swap -l` command on Solaris:

```
swapfile             dev        swaplo blocks        free  
/dev/dsk/c0t3d0s1    32,25      8      197592        162136
```

### 8.2.5 AIX Tools

The following sections describe tools available on AIX systems:

- Base Operation System Tools
- Performance Toolbox
- System Management Interface Tool

See Also:

The AIX operating system documentation and man pages for more information about these tools

#### 8.2.5.1 Base Operation System Tools

The AIX Base Operation System contains performance tools that are historically part of UNIX systems or are required to manage the implementation-specific features of AIX. The following table lists the most important Base Operation System tools:

| Tool | Function |
| --- | --- |
| `lsattr` | Displays the attributes of devices |
| `lslv` | Displays information about a logical volume or the logical volume allocations of a physical volume |
| `netstat` | Displays the contents of network-related data structures |
| `nfsstat` | Displays statistics about Network File System and Remote Procedure Call activity |
| `nice` | Changes the initial priority of a process |
| `no` | Displays or sets network options |
| `ps` | Displays the status of one or more processes |
| `reorgvg` | Reorganizes the physical-partition allocation within a volume group |
| `time` | Displays the elapsed execution, user CPU processing, and system CPU processing time |
| `trace` | Records and reports selected system events |
| `vmo` | Manages Virtual Memory Manager tunable parameters |

#### 8.2.5.2 Performance Toolbox

The AIX Performance Toolbox contains tools for monitoring and tuning system activity locally and remotely. The Performance Tool Box consists of two main components, the Performance Tool Box Manager and the Performance Tool Box Agent. The Performance Tool Box Manager collects and displays data from various systems in the configuration by using the `xmperf` utility. The Performance Tool Box Agent collects and transmits data to the Performance Tool Box Manager by using the `xmserd` daemon. The Performance Tool Box Agent is also available as a separate product called Performance Aide for AIX.

Both Performance Tool Box and Performance Aide include the monitoring and tuning tools listed in the following table:

| Tool | Description |
| --- | --- |
| `fdpr` | Optimizes an executable program for a particular workload |
| `filemon` | Uses the trace facility to monitor and report the activity of the file system |
| `fileplace` | Displays the placement of blocks of a file within logical or physical volumes |
| `lockstat` | Displays statistics about contention for kernel locks |
| `lvedit` | Facilitates interactive placement of logical volumes within a volume group |
| `netpmon` | Uses the trace facility to report on network Input-Output and network-related CPU usage |
| `rmss` | Simulates systems with various memory sizes for performance testing |
| `svmon` | Captures and analyzes information about virtual-memory usage |
| `syscalls` | Records and counts system calls |
| `tprof` | Uses the `trace` facility to report CPU usage at module and source-code-statement levels |
| `BigFoot` | Reports the memory access patterns of processes |
| `stem` | Permits subroutine-level entry and exit instrumentation of existing executables |

See Also:

- Performance Toolbox for AIX Guide and Reference for information about these tools
- AIX 5L Performance Management Guide for information about the syntax of some of these tools

#### 8.2.5.3 System Management Interface Tool

The AIX System Management Interface Tool (SMIT) provides a menu-driven interface to various system administrative and performance tools. By using SMIT, you can navigate through large numbers of tools and focus on the jobs that you want to perform.

### 8.2.6 HP-UX Tools

The following performance analysis tools are available on HP-UX systems:

- GlancePlus/UX
	This HP-UX utility is an online diagnostic tool that measures the activities of the system. GlancePlus displays information about how system resources are used. It displays dynamic information about the system Input-Output, CPU, and memory usage on a series of screens. You can use the utility to monitor how individual processes are using resources.
- HP Programmer's Analysis Kit
	HP Programmer's Analysis Kit consists of the following tools:
	- Puma
		This tool collects performance statistics during a program run. It provides several graphical displays for viewing and analyzing the collected statistics.
		- Thread Trace Visualizer
		This tool displays trace files produced by the instrumented thread library, `libpthread_tr.sl`, in a graphical format. It enables you to view how threads are interacting and to find where threads are blocked waiting for resources.
	HP Programmer's Analysis Kit is bundled with the HP Fortran 77, HP Fortran 90, HP C, HP C++, HP ANSI C++, and HP Pascal compilers.

The following table lists the performance tuning tools that you can use for additional performance tuning on HP-UX:

| Tools | Function |
| --- | --- |
| `caliper`   (Itanium only) | Collects run-time application data for system analysis tasks such as cache misses, translation look-aside buffer or instruction cycles, along with fast dynamic instrumentation. It is a dynamic performance measurement tool for C, C++, Fortran, and assembly applications. |
| `gprof` | Creates an execution profile for programs. |
| `monitor` | Monitors the program counter and calls to certain functions. |
| `netfmt` | Monitors the network. |
| `netstat` | Reports statistics on network performance. |
| `nfsstat` | Displays statistics about Network File System and Remote Procedure Call activity. |
| `nettl` | Captures network events or packets by logging and tracing. |
| `prof` | Creates an execution profile of C programs and displays performance statistics for the program, showing where the program is spending most of its execution time. |
| `profil` | Copies program counter information into a buffer. |
| `top` | Displays the top processes on the system and periodically updates the information. |

### 8.2.7 Linux Tools

On Linux systems, use the `top`, `free`, and `cat /proc/meminfo` commands to view information about swap space, memory, and buffer usage.

### 8.2.8 Solaris Tools

On Solaris systems, use the `mpstat` command to view statistics for each processor in a multiprocessor system. Each row of the table represents the activity of one processor. The first row summarizes all activity since the last system restart. Each subsequent row summarizes activity for the preceding interval. All values are events per second unless otherwise noted. The arguments are for time intervals between statistics and number of iterations.

The following example shows sample output from the `mpstat` command:

```
CPU minf mjf xcal  intr ithr  csw icsw migr smtx  srw syscl  usr sys  wt idl
  0    0   0    1    71   21   23    0    0    0    0    55    0   0   0  99
  2    0   0    1    71   21   22    0    0    0    0    54    0   0   0  99
CPU minf mjf xcal  intr ithr  csw icsw migr smtx  srw syscl  usr sys  wt idl
  0    0   0    0    61   16   25    0    0    0    0    57    0   0   0 100
  2    1   0    0    72   16   24    0    0    0    0    59    0   0   0 100
```

## 8.3 Tuning Memory Management

Start the memory tuning process by measuring paging and swapping space to determine how much memory is available. After you determine the system memory usage, tune the Oracle buffer cache.

The Oracle buffer manager ensures that the most frequently accessed data is cached longer. If you monitor the buffer manager and tune the buffer cache, then you can significantly improve Oracle Database performance. The optimal Oracle Database buffer size for the system depends on the overall system load and the relative priority of Oracle Database over other applications.

This section includes the following topics:

- Allocating Sufficient Swap Space
- Controlling Paging
- Adjusting Oracle Block Size
- Allocating Memory Resource

### 8.3.1 Allocating Sufficient Swap Space

Try to minimize swapping because it causes significant operating system overhead. To check for swapping, use the `sar` or `vmstat` commands. For information about the appropriate options to use with these commands, refer to the man pages.

If the system is swapping and you must conserve memory, then:

- Avoid running unnecessary system daemon processes or application processes.
- Decrease the number of database buffers to free some memory.
- Decrease the number of operating system file buffers.

To determine the amount of swap space, run one of the following commands, depending on the platform:

| Platform | Command |
| --- | --- |
| AIX | `lsps -a` |
| HP-UX | `swapinfo -m` |
| Linux | `swapon -s` |
| Solaris | `swap -l` and `swap -s` |

To add swap space to the system, run one of the following commands, depending on the platform:

| Platform | Command |
| --- | --- |
| AIX | `chps` or `mkps` |
| HP-UX | `swapon` |
| Linux | `swapon -a` |
| Solaris | `swap -a` |

Set the swap space to the level listed for your platform in the respective platform-specific installation guide, based on your physical RAM and memory features used.

See Also:

- [Oracle Database Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for your platform for more information about checking swap space
- The operating system documentation for more information about these commands

### 8.3.2 Controlling Paging

Paging may not present as serious a problem as swapping, because an entire program does not have to be stored in memory to run. A small number of page-outs may not noticeably affect the performance of the system.

To detect excessive paging, run measurements during periods of fast response or idle time to compare against measurements from periods of slow response.

Use the `vmstat` or `sar` command to monitor paging.

See Also:

The man pages or the operating system documentation for information about interpreting the results for the platform

The following table lists the important columns from the output of these commands:

| Platform | Column | Function |
| --- | --- | --- |
| Solaris | `vflt/s` | Indicates the number of address translation page faults. Address translation faults occur when a process refers to a valid page not in memory. |
| HP-UX | `at` | Indicates the number of address translation page faults. Address translation faults occur when a process refers to a valid page not in memory. |
| HP-UX | `re` | Indicates the number of valid pages that have been reclaimed and added to the free list by page-out activity. This value should be zero. |

If the system consistently has excessive page-out activity, then consider the following solutions:

- Install more memory.
- Move some work to another system.
- Configure the System Global Area (SGA) to use less memory.

### 8.3.3 Adjusting Oracle Block Size

During read operations, entire operating system blocks are read from the disk. If the database block size is smaller than the operating system file system block size, then Input-Output bandwidth is inefficient. If you set Oracle Database block size to be a multiple of the file system block size, then you can increase performance by up to 5 percent.

The `DB_BLOCK_SIZE` initialization parameter sets the database block size. However, to change the value of this parameter, you must re-create the database.

To see the current value of the `DB_BLOCK_SIZE` parameter, run the `SHOW PARAMETER` `DB_BLOCK_SIZE` command in SQL\*Plus.

### 8.3.4 Allocating Memory Resource

You can set parameters to automatically allocate memory based on the demands of workload and the requirements of various database instances running on the same system. The `MEMORY_TARGET` parameter specifies the Oracle systemwide usable memory for that instance and automatically tunes SGA and Process Global Area (PGA) components. The `MEMORY_MAX_TARGET` parameter identifies the value up to which the `MEMORY_TARGET` parameter can grow dynamically.

By default, the value for both these parameters is zero and there is no auto-tuning. You can activate auto-tuning by setting the `MEMORY_TARGET` parameter to a nonzero value. To dynamically enable the `MEMORY_TARGET` parameter, the `MEMORY_MAX_TARGET` parameter must be set at startup.

Note:

If you just set the `MEMORY_TARGET` parameter to a nonzero value, the `MEMORY_MAX_TARGET` parameter automatically acquires this value.

The `MEMORY_TARGET` and `MEMORY_MAX_TARGET` parameters are only supported on Linux, Solaris, AIX and HP-UX platforms.

On Solaris, Dynamic Intimate Shared Memory is enabled for `MEMORY_TARGET` or `MEMORY_MAX_TARGET`. For more information, refer to [Appendix D](appe_sol.md).

On Linux, some shared resource requirements are increased when `MEMORY_TARGET` or `MEMORY_MAX_TARGET` are enabled. For more information, refer to the ["Allocating Shared Resources"](appc_linux.md) section.

Tip:

You can set the `MEMORY_TARGET` and `MEMORY_MAX_TARGET` parameters based on original setup, memory available for Oracle on the computer, and workload memory requirements.

## 8.4 Tuning Disk Input-Output

Balance Input-Output evenly across all available disks to reduce disk access times. For smaller databases and those not using RAID, ensure that different data files and tablespaces are distributed across the available disks.

This section contains the following topics:

- Using Automatic Storage Management
- Choosing the Appropriate File System Type

### 8.4.1 Using Automatic Storage Management

If you choose to use Automatic Storage Management for database storage, then all database Input-Output is balanced across all available disk devices in the Automatic Storage Management disk group.

By using Automatic Storage Management, you avoid manually tuning disk Input-Output.

### 8.4.2 Choosing the Appropriate File System Type

Depending on the operating system, you can choose from a range of file system types. Each file system type has different characteristics. This fact can have a substantial impact on database performance. The following table lists common file system types:

| File System | Platform | Description |
| --- | --- | --- |
| S5 | HP-UX and Solaris | UNIX System V file system |
| UFS | AIX, HP-UX, and Solaris | Unified file system, derived from BSD UNIX |
| VxFS | AIX, HP-UX, and Solaris | VERITAS file system |
| ext2/ext3 | Linux | Extended file system for Linux |
| OCFS2 | Linux | Oracle cluster file system |
| JFS/JFS2 | AIX | Journaled file system |
| GPFS | AIX | General parallel file system |

The suitability of a file system for an application is usually not documented. For example, even different implementations of the Unified file system are hard to compare. Depending on the file system that you choose, performance differences can be up to 20 percent. If you choose to use a file system, then:

- Make a new file system partition to ensure that the hard disk is clean and unfragmented.
- Perform a file system check on the partition before using it for database files.
- Distribute disk Input-Output as evenly as possible.
- If you are not using a logical volume manager or a RAID device, then consider placing log files on a different file system from data files.

## 8.5 Monitoring Disk Performance

The following sections describe the procedure for monitoring disk performance:

- Monitoring Disk Performance on Other Operating Systems
- Using Disk Resync to Monitor Automatic Storage Management Disk Group

### 8.5.1 Monitoring Disk Performance on Other Operating Systems

To monitor disk performance, use the `sar -b` and `sar -u` commands.

The following table describes the columns of the `sar -b` command output that are significant for analyzing disk performance:

| Columns | Description |
| --- | --- |
| `bread/s`, `bwrit/s` | Blocks read and blocks written per second (important for file system databases) |
| `pread/s`, `pwrit/s` | Number of reads and writes per second from or to raw character devices |

An important `sar -u` column for analyzing disk performance is `%wio`, the percentage of CPU time spent waiting on blocked Input-Output.

Note:

Not all Linux distributions display the `%wio` column in the output of the `sar -u` command. For detailed Input-Output statistics, you can use `iostat -x` command.

Key indicators are:

- The sum of the `bread`, `bwrit`, `pread`, and `pwrit` column values indicates the level of activity of the disk Input-Output subsystem. The higher the sum, the busier the Input-Output subsystem. The larger the number of physical drives, the higher the sum threshold number can be. A good default value is no more than 40 for 2 drives and no more than 60 for 4 to 8 drives.
- The `%rcache` column value should be greater than 90 and the `%wcache` column value should be greater than 60. Otherwise, the system may be disk Input-Output bound.
- If the `%wio` column value is consistently greater than 20, then the system is Input-Output bound.

### 8.5.2 Using Disk Resync to Monitor Automatic Storage Management Disk Group

Use the `alter diskgroup disk online` and `alter diskgroup disk offline` commands to temporarily suspend Input-Output to a set of disks. You can use these commands to perform regular maintenance tasks or upgrades such as disk firmware upgrade. If transient failures occur on some disks in a disk group, then use `alter diskgroup disk online` to quickly recover the disk group.

## 8.6 System Global Area

The SGA is the Oracle structure that is located in shared memory. It contains static data structures, locks, and data buffers.

The maximum size of a single shared memory segment is specified by the `shm` `max` kernel parameter.

The following table shows the recommended value for this parameter, depending on the platform:

| Platform | Recommended Value |
| --- | --- |
| AIX | NA |
| HP-UX | The size of the physical memory installed on the system |
| Linux | Minimum of the following values: - Half the size of the physical memory installed on the system - 4GB - 1 byte |
| Solaris | 4294967295 or 4 GB minus 16 MB  Note: If the system runs both Oracle9i Database and Oracle Database 11g instances, then you must set the value of `shm_max` to 2 GB minus 16 MB. On Solaris, this value can be greater than 4 GB to accommodate larger SGA sizes. |

If the size of the SGA exceeds the maximum size of a shared memory segment (`shm` `max` or `shm` `_max`), then Oracle Database attempts to attach more contiguous segments to fulfill the requested SGA size. The `shm` `seg` kernel parameter specifies the maximum number of segments that can be attached by any process. Set the following initialization parameters to control the size of the SGA:

- `DB_CACHE_SIZE`
- `DB_BLOCK_SIZE`
- `JAVA_POOL_SIZE`
- `LARGE_POOL_SIZE`
- `LOG_BUFFERS`
- `SHARED_POOL_SIZE`

Alternatively, set the `SGA_TARGET` initialization parameter to enable automatic tuning of the SGA size.

Note:

Ensure that you set the values for these parameters correctly. When values are set too high, too much of the physical memory is devoted to shared memory. This results in poor performance.

An Oracle Database configured with Shared Server requires a higher setting for the `SHARED_POOL_SIZE` initialization parameter, or a custom configuration that uses the `LARGE_POOL_SIZE` initialization parameter. If you installed the database with Oracle Universal Installer, then the value of the `SHARED_POOL_SIZE` parameter is set automatically by Oracle Database Configuration Assistant. However, if you created a database manually, then increase the value of the `SHARED_POOL_SIZE` parameter in the parameter file by 1 KB for each concurrent user.

Sufficient shared memory must be available to each Oracle process to address the entire SGA:

- Determining the Size of the SGA
- System Resource Verifier Utility
- Shared Memory on AIX

### 8.6.1 Determining the Size of the SGA

You can determine the SGA size in one of the following ways:

- Run the following SQL\*Plus command to display the size of the SGA for a running database:
	```
	SQL> SHOW SGA
	```
	The result is shown in bytes.
- When you start the database instance, the size of the SGA is displayed next to the Total System Global Area heading.
- Run the `ipcs` command as the `oracle` user.

### 8.6.2 System Resource Verifier Utility

The System Resource Verifier utility (`sysresv`) is available with Oracle Database 8 `i` and later releases. It provides Oracle instance and operating system resource information for the Oracle system identifiers (`ORACLE_SID`) that you specify. This utility is located in `$ORACLE_HOME/bin`, but it can be used from other locations.

#### 8.6.2.1 Purpose of the sysresv Utility

Use the `sysresv` utility to display the status of an Oracle instance and identify the operating system resources it uses, such as the memory and semaphore parameters. This utility is especially useful when multiple instances are running. For example, if an instance is not responsive, then you can use this utility to remove operating system resources.

You can use this utility when an Oracle instance has crashed or was aborted, and memory and semaphores related to this instance were not cleaned up automatically. This utility is also useful in determining which Oracle instance is running.

#### 8.6.2.2 Preconditions for Using sysresv

To use the `sysresv` utility, you must have access to the System Global Area (SGA). To access the SGA, you must be the Oracle owner or a member of the group that owns the Oracle binary.

#### 8.6.2.3 Syntax for sysresv

The syntax for the `sysresv` utility is as follows:

```
sysresv [-i] [-f] [-d on|off] [-l sid1[ sid2 ...]]
```

Where:

- `-i` Prompt before removing IPC resources for each sid
- `-f` Remove IPC resources without prompting for confirmation. This flag overrides the `-i` option
- `-d on|off` List IPC resources for each sid if on. If not specified, the default for `-d` is on
- `-l sid1 [sid2 sid3]` run the `sysresv` check against one or more space-delimited system identifiers

If `sysresv` is used without flags, then it reports IPC resources for the Oracle instance identified by the `$ORACLE_SID` environment variable in the Oracle installation owner user profile list of environment variables.

#### 8.6.2.4 Examples of Using sysresv

The following example shows how to use the `sysresv` utility:

```
$ sysresv
IPV Resources for ORACLE_SID "sales" :
Shared Memory:
ID                            KEY
10345                    0x51c051ad
Semaphores
ID
10345                    0x51c051ad
Oracle Instance alive for sid "sales"
```

### 8.6.3 Shared Memory on AIX

Note:

The information in this section applies only to AIX.

Shared memory uses common virtual memory resources across processes. Processes share virtual memory segments through a common set of virtual memory translation resources, for example, tables and cached entries, for improved performance.

Shared memory can be pinned to prevent paging and to reduce Input-Output overhead. To perform this, set the `LOCK_SGA` parameter to `true`. On AIX 5L, the same parameter activates the large page feature whenever the underlying hardware supports it.

Run the following command to make pinned memory available to Oracle Database:

```
$ /usr/sbin/vmo -r -o v_pinshm=1
```

Run a command similar to the following to set the maximum percentage of real memory available for pinned memory, where `percent_of_real_memory` is the maximum percent of real memory that you want to set:

```
$ /usr/sbin/vmo -r -o maxpin percent=percent_of_real_memory
```

When using the `maxpin percent` option, it is important that the amount of pinned memory exceeds the Oracle SGA size by at least 3 percent of the real memory on the system, enabling free pinnable memory for use by the kernel. For example, if you have 2 GB of physical memory and you want to pin the SGA by 400 MB (20 percent of the RAM), then run the following command:

```
$ /usr/sbin/vmo -r -o maxpin percent=23
```

Note:

The default `maxpin percent` value, which is set at 80 `percent`, works for most installations.

Use the `svmon` command to monitor the use of pinned memory during the operation of the system. Oracle Database attempts to pin memory only if the `LOCK_SGA` parameter is set to `true`. If the SGA size exceeds the size of memory available for pinning, then the portion of the SGA exceeding these sizes is allocated to ordinary shared memory.

Large Page Feature on AIX POWER4- and POWER5-Based Systems

To turn on and reserve 10 large pages each of size 16 MB on a POWER4 or POWER 5 system, run the following command:

```
$ /usr/sbin/vmo -r -o lgpg_regions=10 -o lgpg_size=16777216
```

This command proposes bosboot and warns that a restart is required for the changes to take affect.

Oracle recommends specifying enough large pages to contain the entire SGA. The Oracle database instance attempts to allocate large pages when the `LOCK_SGA` parameter is set to `true`.

The 16 MB pages are always pinned, and cannot be used for standard memory. If a pool of 16MB size pages is configured, then this memory will be unusable for allocation of standard memory even if no other application is currently using large pages.

The `POWER5` based systems support 64 K pages. Oracle uses them for SGA if they are available. These 64K pages do not require any additional configuration and do not depend on `LOCK_SGA` parameter setting.

To monitor use of large pages, use the following command:

```
$ vmstat -P all
```

For the AIX operating system to use 16MB pages, or pinned memory when allocating shared memory, the Oracle user ID must have `CAP_BYPASS_RAC_VMM` and `CAP_PROPAGATE` capabilities. User ID that is used to start the database instance must also have the same capabilities. In particular, when using large pages on an Oracle Real Application Cluster (Oracle RAC) database, where the `srvctl` command is used to start and stop the Oracle RAC database instances, it is also necessary to set the `CAP_BYPASS_RAC_VMM` and `CAP_PROPAGATE` capabilities for the `root` user.

See Also:

The AIX documentation for more information about enabling and tuning pinned memory and large pages

Capabilities can be set and examined using the following commands:

- Run the following command to check the current capabilities:
	```
	$ lsuser –a capabilities oracle
	```
- Add the `CAP_BYPASS_RAC_VMM` and `CAP_PROPAGATE` capabilities to this user ID:
	```
	$ chuser capabilities=CAP_BYPASS_RAC_VMM,CAP_PROPAGATE oracle
	```

Note:

Only the `root` user can display and set the capabilities attribute.

## 8.7 Tuning the Operating System Buffer Cache

Adjust the size of Oracle Database buffer cache. If memory is limited, then adjust the operating system buffer cache.

The operating system buffer cache holds blocks of data in memory while they are being transferred from memory to disk, or from disk to memory.

Oracle Database buffer cache is the area in memory that stores Oracle Database buffers.

If the amount of memory on the system is limited, then make a corresponding decrease in the operating system buffer cache size.

Use the `sar` command to determine which buffer caches you must increase or decrease.