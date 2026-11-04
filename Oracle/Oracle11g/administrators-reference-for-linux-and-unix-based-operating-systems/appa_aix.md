---
title: Administering Oracle Database on AIX
book: "Administrator's Reference for Linux and UNIX-Based Operating Systems"
doc_id: E10839-25
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e10839/appa_aix.htm
tags:
  - oracle
  - 11g
  - administrators-reference-for-linux-and-unix-based-operating-systems
---

## A Administering Oracle Database on AIX

This appendix contains information about administering Oracle Database on AIX. It includes the following topics:

## A.1 Memory and Paging

Memory contention occurs when processes require more memory than is available. To cope with the shortage, the system pages programs and data between memory and disks.

This section contains the following topics:

- Controlling Buffer-Cache Paging Activity
- Tuning the AIX File Buffer Cache
- Allocating Sufficient Paging Space
- Controlling Paging
- Setting the Database Block Size
- Tuning the Log Archive Buffers
- Input-Output Buffers and SQL\*Loader

### A.1.1 Controlling Buffer-Cache Paging Activity

Excessive paging activity decreases performance substantially. This can become a problem with database files created on journaled file systems (JFS and JFS2). In this situation, a large number of SGA data buffers may also have analogous file system buffers containing the most frequently referenced data. The behavior of the AIX file buffer cache manager can have a significant impact on performance. It can cause an Input-Output bottleneck, resulting in lower overall system throughput.

It is possible to tune buffer-cache paging activity, but you must do it carefully and infrequently. Use the `/usr/sbin/vmo` command to tune the AIX system parameters in the following table:

| Parameter | Description |
| --- | --- |
| `minfree` | The minimum free-list size. If the free-list space in the buffer falls lower than this size, then the system uses page stealing to replenish the free list. |
| `maxfree` | The maximum free-list size. If the free-list space in the buffer exceeds this size, then the system stops using page stealing to replenish the free list. |
| `minperm` | The minimum number of permanent buffer pages for file Input-Output. |
| `maxperm` | The maximum number of permanent buffer pages for file Input-Output. |

See Also:

AIX 5L Performance Management Guide for more information about AIX system parameters

### A.1.2 Tuning the AIX File Buffer Cache

The purpose of the AIX file buffer cache is to reduce disk access frequency when journaled file systems are used. If this cache is too small, then disk usage increases and potentially saturates one or more disks. If the cache is too large, then memory is wasted.

You can configure the AIX file buffer cache by adjusting the `minperm` and `maxperm` parameters. In general, if the buffer hit ratio is low (less than 90 percent), as determined by the `sar -b` command, then increasing the `minperm` parameter value may help. If maintaining a high buffer hit ratio is not critical, then decreasing the `minperm` parameter value increases the physical memory available. Refer to the AIX documentation for more information about increasing the size of the AIX file buffer cache.

The performance gain cannot be quantified easily, because it depends on the degree of multiprogramming and the Input-Output characteristics of the workload.

Tuning the minperm and maxperm Parameters

AIX provides a mechanism for you to loosely control the ratio of page frames used for files rather than those used for computational (working or program text) segments by adjusting the `minperm` and `maxperm` values according to the following guidelines:

- If the percentage of real memory occupied by file pages falls lower than the `minperm` value, then the virtual memory manager (VMM) page-replacement algorithm takes both file and computational pages, regardless of repage rates.
- If the percentage of real memory occupied by file pages rises above the `maxperm` value, then the VMM page-replacement algorithm takes both file and computational pages.
- If the percentage of real memory occupied by file pages is between the `minperm` and `maxperm` parameter values, then the VMM normally takes only file pages. However, if the repaging rate for file pages is higher than the repaging rate for computational pages, then the computational pages are taken as well.

Use the following algorithm to calculate the default values:

- `minperm` (in pages) = ((number of page frames)-1024) \* 0.2
- `maxperm` (in pages) = ((number of page frames)-1024) \* 0.8

Use the following command to change the value of the `minperm` parameter to 5 percent of the total number of page frames, and the value of the `maxperm` parameter to 20 percent of the total number of page frames:

```
# /usr/sbin/vmo -o minperm percent=5 -o maxperm percent=20
```

The default values are 20 percent and 80 percent, respectively.

To optimize for quick response when opening new database connections, adjust the `minfree` parameter to maintain enough free pages in the system to load the application into memory without adding additional pages to the free list. To determine the real memory size (resident set size, working set) of a process, use the following command:

```
$ ps v process_id
```

Set the `minfree` parameter to this value or to 8 frames, whichever is larger.

If you are using Direct Input-Output, then you can set the `minperm` and `maxperm` parameters to low values. For example, 5 percent and 20 percent, respectively. This is because the AIX file buffer cache is not used for Direct Input-Output. The memory may be better used for other purposes, such as for the Oracle System Global Area.

### A.1.3 Allocating Sufficient Paging Space

Inadequate paging space (swap space) usually causes the system to stop responding or show very slow response times. On AIX, you can dynamically add paging space on raw disk partitions. The amount of paging space you should configure depends on the amount of physical memory present and the paging space requirements of the applications. Use the `lsps` command to monitor paging space use and the `vmstat` command to monitor system paging activities. To increase the paging space, use the `smit pgsp` command.

If paging space is preallocated, then Oracle recommends that you set the paging space to a value larger than the amount of RAM. But on AIX, paging space is not allocated until required. The system uses swap space only if it runs out of real memory. If the memory is sized correctly, then there is no paging and the page space can be small. Workloads where the demand for pages does not fluctuate significantly perform well with a small paging space. Workloads likely to have peak periods of increased paging require enough paging space to handle the peak number of pages.

As a general rule, an initial setting for the paging space is half the size of RAM plus 4 GB, with an upper limit of 32 GB. Monitor the paging space use with the `lsps -a` command, and increase or decrease the paging space size accordingly. The metric percent Used in the output of `lsps -a` is typically less than 25 percent on a healthy system. A properly sized deployment requires very little paging space and an excessive amount of swapping is an indication that the RAM on the system may be undersized.

Caution:

Do not undersize the paging space. If you do, then the system terminates active processes when it runs out of space. However, oversizing the paging space has little or no negative impact.

### A.1.4 Controlling Paging

Constant and excessive paging indicates that the real memory is over-committed. In general, you should:

- Avoid constant paging unless the system is equipped with very fast expanded storage that makes paging between memory and expanded storage much faster than Oracle Database can read and write data between the SGA and disks.
- Allocate limited memory resource to where it is most beneficial to system performance. It is sometimes a recursive process of balancing the memory resource requirements and trade-offs.
- If memory is not adequate, then build a prioritized list of memory-requiring processes and elements of the system. Assign memory to where the performance gains are the greatest. A prioritized list may look like the following:
	1. OS and RDBMS kernels
		2. User and application processes
		3. Redo log buffer
		4. PGAs and shared pool
		5. Database block buffer caches

For example, suppose you query Oracle Database dynamic performance tables and views and find that both the shared pool and database buffer cache require more memory. Then, assigning the limited spare memory to the shared pool may be more beneficial than assigning it to the database block buffer caches.

The following AIX commands provide paging status and statistics:

- `vmstat -s`
- `vmstat` `interval` `[``repeats``]`
- `sar -r` `interval` `[``repeats``]`

### A.1.5 Setting the Database Block Size

You can configure Oracle Database block size for better Input-Output throughput. On AIX, you can set the value of the `DB_BLOCK_SIZE` initialization parameter to between 2 KB and 32 KB, with a default of 4 KB. If Oracle Database is installed on a journaled file system, then the block size should be a multiple of the file system block size (4 KB on JFS, 16 K to 1 MB on GPFS). For databases on raw partitions, Oracle Database block size is a multiple of the operating system physical block size (512 bytes on AIX).

Oracle recommends smaller Oracle Database block sizes (2 KB or 4 KB) for online transaction processing or mixed workload environments and larger block sizes (8 KB, 16 KB, or 32 KB) for decision support system workload environments.

### A.1.6 Tuning the Log Archive Buffers

By increasing the `LOG_BUFFER` size, you may be able to improve the speed of archiving the database, particularly if transactions are long or numerous. Monitor the log file Input-Output activity and system throughput to determine the optimum `LOG_BUFFER` size. Tune the `LOG_BUFFER` parameter carefully to ensure that the overall performance of normal database activity does not degrade.

Note:

The `LOG_ARCHIVE_BUFFER_SIZE` parameter was obsoleted with Oracle8i Database.

### A.1.7 Input-Output Buffers and SQL\*Loader

For high-speed data loading, such as using the SQL\*Loader direct path option in addition to loading data in parallel, the CPU spends most of its time waiting for Input-Output to complete. By increasing the number of buffers, you can maximize CPU usage, and by doing this, increase overall throughput.

The number of buffers (set by the SQL\*Loader `BUFFERS` parameter) you choose depends on the amount of available memory and how much you want to maximize CPU usage.

The performance gains depend on CPU usage and the degree of parallelism that you use when loading data.

See Also:

[Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/toc.htm) for information about adjusting the file processing options string for the `BUFFERS` parameter and for information about the SQL\*Loader utility

BUFFER Parameter for the Import Utility

The `BUFFER` parameter for the Import utility should be set to a large value to optimize the performance of high-speed networks when they are used. For example, if you use the IBM RS/6000 Scalable POWER parallel Systems switch, then you should set the `BUFFER` parameter to a value of at least 1 MB.

## A.2 Disk Input-Output Issues

Disk Input-Output contention can result from poor memory management (with subsequent paging and swapping), or poor distribution of tablespaces and files across disks.

Ensure that the Input-Output activity is distributed evenly across multiple disk drives by using AIX utilities such as `filemon`, `sar`, `iostat`, and other performance tools to identify disks with high Input-Output activity.

This section contains the following topics:

- AIX Logical Volume Manager
- Using Journaled File Systems Compared to Raw Logical Volumes
- Using Asynchronous Input-Output
- Input-Output Slaves
- Using the DB\_FILE\_MULTIBLOCK\_READ\_COUNT Parameter
- Using Write Behind
- Tuning Sequential Read Ahead
- Tuning Disk Input-Output Pacing
- Resilvering with Oracle Database

### A.2.1 AIX Logical Volume Manager

The AIX Logical Volume Manager can stripe data across multiple disks to reduce disk contention. The primary objective of striping is to achieve high performance when reading and writing large sequential files. Effective use of the striping features in the Logical Volume Manager enables you to spread Input-Output more evenly across disks, resulting in better overall performance.

Note:

Do not add logical volumes to Automatic Storage Management disk groups. Automatic Storage Management works best when you add raw disk devices to disk groups. If you are using Automatic Storage Management, then do not use Logical Volume Manager for striping. Automatic Storage Management implements striping and mirroring.

Design a Striped Logical Volume

When you define a striped logical volume, you must specify the items listed in the following table:

| Item | Recommended Settings |
| --- | --- |
| Drives | There must be at least two physical drives. The drives should have minimal activity when performance-critical sequential Input-Output is carried out. Sometimes, you must stripe the logical volume between two or more adapters. |
| Stripe unit size | Although the stripe unit size can be any power of 2 (from 2 KB to 128 KB), stripe sizes of 32 KB and 64 KB are good values for most workloads. For Oracle Database files, the stripe size must be a multiple of the database block size. |
| Size | The number of physical partitions allocated to the logical volume must be a multiple of the number of disk drives used. |
| Attributes | Cannot be mirrored. Set the `copies` attribute to a value of 1. |

Other Considerations

Performance gains from effective use of the Logical Volume Manager can vary greatly, depending on the Logical Volume Manager you use and the characteristics of the workload. For decision support system workloads, you can see substantial improvement. For online transaction processing-type or mixed workloads, you can expect significant performance gains.

### A.2.2 Using Journaled File Systems Compared to Raw Logical Volumes

Address the following considerations when deciding whether to use journaled file systems or raw logical volumes:

- File systems are continually being improved, as are various file system implementations.
- File systems require some additional configuration (AIX `minservers` and `maxservers` parameter) and add a small CPU overhead because Asynchronous Input-Output on file systems is serviced outside the kernel.
- Different vendors implement the file system layer in different ways to capitalize on the strengths of different disks. This makes it difficult to compare file systems across platforms.
- The introduction of more powerful Logical Volume Manager interfaces substantially reduces the tasks of configuring and backing up logical disks based on raw logical volumes.
- The Direct Input-Output and Concurrent Input-Output features included in IBM AIX on POWER Systems improve file system performance to a level comparable to raw logical volumes.

In earlier versions of AIX, file systems supported only buffered read and write and added extra contention because of imperfect inode locking. These two issues are solved by the JFS2 Concurrent Input-Output feature and the GPFS Direct Input-Output feature.

Note:

To use the Oracle RAC option, you must place data files on an Automatic Storage Management disk group or on a GPFS file system. You cannot use JFS or JFS2. Direct Input-Output is implicitly enabled when you use GPFS.

File System Options

IBM AIX on POWER Systems includes Direct Input-Output and Concurrent Input-Output support. Direct Input-Output and Concurrent Input-Output support enables database files to exist on file systems while bypassing the operating system buffer cache and removing inode locking operations that are redundant with the features provided by Oracle Database.

Where possible, Oracle recommends enabling Concurrent Input-Output or Direct Input-Output on file systems containing Oracle data files. The following table lists file systems available on AIX and the recommended setting:

| File System | Option | Description |
| --- | --- | --- |
| JFS | dio | Concurrent Input-Output is not available on JFS. Direct Input-Output is available, but performance is degraded compared to JFS2 with Concurrent Input-Output. |
| JFS large file | none | Oracle does not recommend using JFS large file for Oracle Database because its 128 KB alignment constraint prevents you from using Direct Input-Output. |
| JFS2 | cio | Concurrent Input-Output is a better setting than Direct Input-Output on JFS2, because it provides support for multiple concurrent readers and writers on the same file. However, due to AIX restrictions on JFS2/CIO, Concurrent Input-Output is intended to be used only with Oracle data files, control files, and log files. It should be applied only to file systems that are dedicated to such a purpose. For the same reason, the Oracle home directory is not supported on a JFS2 file system mounted with the `cio` option. For example, during installation, if you inadvertently specify that the Oracle home directory is on a JFS2 file system mounted with the CIO option, then while trying to relink Oracle, you may encounter the following error:  `"ld: 0711-866 INTERNAL ERROR: Output symbol table size miscalculated"`  Note: For Oracle Database 11g Release 2 (11.2.0.2) and later, on AIX 6.1 systems, Oracle recommends that you do not use the `cio` option on a JFS2 file system. |
| GPFS | NA | Oracle Database silently enables Direct Input-Output on GPFS for optimum performance. GPFS Direct Input-Output supports multiple readers and writers on multiple nodes. Therefore, Direct Input-Output and Concurrent Input-Output are the same thing on GPFS. |

Considerations for JFS and JFS2

If you are placing Oracle Database logs on a JFS2 file system, then the optimal configuration is to create the file system using the `agblksize=512` option and to mount it with the `cio` option.

Before Oracle Database 11g, Direct Input-Output and Concurrent Input-Output could not be enabled at the file level on JFS/JFS2. Therefore, the Oracle home directory and data files had to be placed in separate file systems for optimal performance. The Oracle home directory was placed on a file system mounted with default options, with the data files and logs on file systems mounted using the `dio` or `cio` options.

With Oracle Database 11g, you can enable Direct Input-Output and Concurrent Input-Output on JFS/JFS2 at the file level. You can do this by setting the `FILESYSTEMIO_OPTIONS` parameter in the server parameter file to `setall` or `directIO`. This enables Concurrent Input-Output on JFS2 and Direct Input-Output on JFS for all data file Input-Output. Because the `directIO` setting disables asynchronous Input-Output it should normally not be used. As a result of this 11g feature, you can place data files on the same JFS/JFS2 file system as the Oracle home directory and still use Direct Input-Output or Concurrent Input-Output for improved performance. As mentioned earlier, you should still place Oracle Database logs on a separate JFS2 file system for optimal performance.

Considerations for GPFS

If you are using GPFS, then you can use the same file system for all purposes. This includes using it for the Oracle home directory and for storing data files and logs. For optimal performance, you should use a large GPFS block size (typically, at least 512 KB). GPFS is designed for scalability, and there is no requirement to create multiple GPFS file systems as long as the amount of data fits in a single GPFS file system.

Moving from a Journaled File System to Raw Logical Volumes

To move from a journaled file system to raw devices without having to manually reload all the data, perform the following steps as the `root` user:

1. Create a raw device (preferably, in a BigVG) using the new raw logical volume device type (`-T O`), which enables putting the first Oracle block at offset zero for optimal performance:
	```
	# mklv -T O -y new_raw_device VolumeGroup NumberOfPartitions
	```
	Note:
	The raw device should be larger than the existing file. In addition, you must bear in mind the size of the new raw device to prevent wasting space.
2. Set the permissions on the raw device.
3. Use `dd` to convert and copy the contents of the JFS file to the new raw device as follows:
	```
	# dd if=old_JFS_file of=new_raw_device bs=1m
	```
4. Rename the data file.

Moving from Raw Logical Volumes to a Journaled File System

The first Oracle block on a raw logical volume is not necessarily at offset zero. However, the first Oracle block on a file system is always at offset zero. To determine the offset and locate the first block on a raw logical volume, use the `$ORACLE_HOME/bin/offset` command. The offset can be 4096 bytes or 128 KB on AIX logical volumes or zero on AIX logical volumes created with the `mklv -T O` option.

When you have determined the offset, you can copy over data from a raw logical volume to a file system using the `dd` command and skipping the offset. The following example assumes an offset of 4096 bytes:

```
# dd if=old_raw_device bs=4k skip=1|dd of=new_file bs=256
```

You can instruct Oracle Database to use many blocks smaller than the maximum capacity of a raw logical volume. If you do this, then you must add a `count` clause to ensure that only data that contains Oracle blocks is copied. The following example assumes an offset of 4096 bytes, an Oracle block size of 8 KB, and 150000 blocks:

```
# dd if=old_raw_device bs=4k skip=1|dd bs=8k count=150000|dd of=new_file bs=256k
```

### A.2.3 Using Asynchronous Input-Output

Oracle Database takes full advantage of asynchronous Input-Output provided by AIX, resulting in faster database access.

IBM AIX on POWER Systems support asynchronous Input-Output for database files created on file system partitions. When using asynchronous Input-Output on file systems, the kernel database processes (`aioserver`) control each request from the time a request is taken off the queue to the time it is completed. The number of `aioserver` servers determines the number of asynchronous Input-Output requests that can be processed in the system concurrently. So, it is important to tune the number of `aioserver` processes when using file systems to store Oracle Database data files.

Use one of the following commands to set the number of servers. This applies only when using asynchronous Input-Output on file systems:

- `smit aio`
- `chdev -l aio0 -a maxservers='` `m` `' -a minservers='` `n` `'`
	See Also:
	- The System Management Interface Tool (SMIT) online Help for more information about SMIT
	- The man pages for more information about the `smit aio` and `chdev` commands

Note:

- On IBM AIX on POWER Systems, there are two asynchronous Input-Output subsystems available. Oracle Database 11g uses Legacy asynchronous Input-Output (`aio0`), even though the Oracle preinstallation script enables Legacy asynchronous Input-Output (`aio0`) and POSIX AIO (`posix_aio0`). Both asynchronous Input-Output subsystems have the same performance characteristics.
- Starting with AIX 6.1, the `minservers`, `maxservers`, and `maxreqs` parameters are replaced by the `aio_minservers`, `aio_maxservers`, and `aio_maxreqs` parameters respectively.

Set the minimum value to the number of servers to be started when the system is started. Set the maximum value to the number of servers that can be started in response to a large number of concurrent requests. These parameters apply to file systems only.

The default value for the minimum number of servers is 1. The default value for the maximum number of servers is 10. These values are usually too low to run Oracle Database on large systems with 4 CPUs or more, if you are not using kernelized asynchronous Input-Output. Oracle recommends that you set the parameters to the values listed in the following table:

| Parameter | Value |
| --- | --- |
| `minservers` | Oracle recommends an initial value equal to the number of CPUs on the system or 10, whichever is lower. |
| `maxservers` | Starting with AIX 5L version 5.3, this parameter counts the maximum number of asynchronous Input-Output servers for each CPU. On previous versions of AIX, it was a systemwide value. If you are using General Parallel File System (GPFS), then set `maxservers` to worker1threads divided by the number of CPUs. This is the optimal setting. Increasing `maxservers` does not lead to improved Input-Output performance.  If you are using JFS/JFS2, then set the initial value to 10 times the number of logical disks divided by the number of CPUs that are to be used concurrently but no more than 80. Monitor the actual number of `aioservers` started during a typical workload using the `pstat` or `ps` commands. If the actual number of active aioservers equals the maxservers, then increase the `maxservers` value. |
| `maxreqs` | Set the initial value to 4 times the number of logical disks multiplied by the queue depth. You can determine the queue depth by running the following command: ``` $ lsattr -E -l hdiskxx ```  Typically, the queue depth is 3. |

If the value of the `maxservers` or `maxreqs` parameter is set too low, then the following warning messages are repeatedly displayed:

```
Warning: lio_listio returned EAGAINPerformance degradation may be seen.
```

You can avoid these errors by increasing the value of the `maxservers` parameter. To display the number of asynchronous Input-Output servers running, enter the following commands as the `root` user:

```
# pstat -a | grep -c aios
# ps -k | grep aioserver
```

Check the number of active asynchronous Input-Output servers periodically, and change the values of the `minservers` and `maxservers` parameters if required. The changes take place when the system is restarted.

Note:

See your operating system vendor documentation for information about tuning AIO parameters.

### A.2.4 Input-Output Slaves

Input-Output Slaves are specialized Oracle processes that perform only Input-Output. They are rarely used on AIX, because asynchronous Input-Output is the default and recommended way for Oracle to perform Input-Output operations on AIX. Input-Output Slaves are allocated from shared memory buffers. Input-Output Slaves use the initialization parameters listed in the following table:

| Parameter | Range of Values | Default Value |
| --- | --- | --- |
| `DISK_ASYNCH_IO` | `true` / `false` | `true` |
| `TAPE_ASYNCH_IO` | `true` / `false` | `true` |
| `BACKUP_TAPE_IO_SLAVES` | `true` / `false` | `false` |
| `DBWR_IO_SLAVES` | 0 - 999 | 0 |
| `DB_WRITER_PROCESSES` | 1-20 | 1 |

Generally, you do not adjust the parameters in the preceding table. However, on large workloads, the database writer may become a bottleneck. If it does, then increase the value of `DB_WRITER_PROCESSES`. As a general rule, do not increase the number of database writer processes above one for each pair of CPUs in the system or partition.

There are times when you must turn off asynchronous I/O. For example, if instructed to do so by Oracle Support for debugging. You can use the `DISK_ASYNCH_IO` and `TAPE_ASYNCH_IO` parameters to switch off asynchronous I/O for disk or tape devices. `TAPE_ASYNCH_IO` support is only available when the Media Manager software supports it and for Recovery Manager, if `BACKUP_TAPE_IO_SLAVES` is true.

Set the `DBWR_IO_SLAVES` parameter to greater than 0 only if the `DISK_ASYNCH_IO` parameter is set to `false`. Otherwise, the database writer process becomes a bottleneck. In this case, the optimal value on AIX for the `DBWR_IO_SLAVES` parameter is 4.

### A.2.5 Using the DB\_FILE\_MULTIBLOCK\_READ\_COUNT Parameter

When using Direct Input-Output or Concurrent Input-Output with Oracle Database 11g, the AIX file system does not perform any read-ahead on sequential scans. For this reason the `DB_FILE_MULTIBLOCK_READ_COUNT` value in the server parameter file should be increased when Direct Input-Output or Concurrent Input-Output is enabled on Oracle data files. The read ahead is performed by Oracle Database as specified by the `DB_FILE_MULTIBLOCK_READ_COUNT` initialization parameter.

Setting a large value for the `DB_FILE_MULTIBLOCK_READ_COUNT` initialization parameter usually yields better Input-Output throughput on sequential scans. On AIX, this parameter ranges from 1 to 512, but using a value higher than 16 usually does not provide additional performance gain.

Set this parameter so that its value when multiplied by the value of the `DB_BLOCK_SIZE` parameter produces a number larger than the Logical Volume Manager stripe size. Such a setting causes more disks to be used.

### A.2.6 Using Write Behind

The write behind feature enables the operating system to group write Input-Output together, up to the size of a partition. You can improve performance by doing this, because the number of Input-Output operations is reduced. The file system divides each file into 16 KB partitions to increase write performance, limit the number of dirty pages in memory, and minimize disk fragmentation. The pages of a particular partition are not written to disk until the program writes the first byte of the next 16 KB partition. To set the size of the buffer for write behind to eight 16 KB partitions, enter the following command:

```
à        # /usr/sbin/vmo -o numclust=8
```

To disable write behind, enter the following command:

```
à        # /usr/sbin/vmo -o numclust=0
```

### A.2.7 Tuning Sequential Read Ahead

Note:

The information in this section applies only to file systems, and only when neither Direct Input-Output nor Concurrent Input-Output are used.

The VMM anticipates the need for pages of a sequential file. It observes the pattern in which a process accesses a file. When the process accesses two consecutive pages of the file, the VMM assumes that the program continues to access the file sequentially, and schedules additional sequential reads of the file. These reads overlap the program processing and make data available to the program faster. The following VMM thresholds, implemented as kernel parameters, determine the number of pages it reads ahead:

- `minpgahead`
	This parameter stores the number of pages read ahead when the VMM first detects the sequential access pattern.
- `maxpgahead`
	This parameter stores the maximum number of pages that VMM reads ahead in a sequential file.

Set the `minpgahead` and `maxpgahead` parameters to appropriate values for an application. The default values are 2 and 8 respectively. Use the `/usr/sbin/vmo` command to change these values. You can use higher values for the `maxpgahead` parameter in systems where the sequential performance of striped logical volumes is of paramount importance. To set the `minpgahead` parameter to 32 pages and the `maxpgahead` parameter to 64 pages, run the following command as the `root` user:

```
-o minpgahead=32 -o maxpgahead=64
```

Set both the `minpgahead` and `maxpgahead` parameters to a power of two. For example, 2, 4, 8,... 512, 1042,... and so on.

### A.2.8 Tuning Disk Input-Output Pacing

Disk Input-Output pacing is an AIX mechanism that enables the system administrator to limit the number of pending Input-Output requests to a file. This prevents disk Input-Output intensive processes from saturating the CPU. Therefore, the response time of interactive and CPU-intensive processes does not deteriorate.

You can achieve disk Input-Output pacing by adjusting two system parameters: the high-water mark and the low-water mark. When a process writes to a file that has a pending high-water mark Input-Output request, the process is put to sleep. The process wakes up when the number of outstanding Input-Output requests falls lower than or equals the low-water mark.

You can use the `smit` command to change the high and low-water marks. Determine the water marks through trial-and-error. Use caution when setting the water marks, because they affect performance. Tuning the high and low-water marks has less effect on disk Input-Output larger than 4 KB.

You can determine disk Input-Output saturation by analyzing the result of `iostat`, in particular, the percentage of `iowait` and `tm_act`. A high `iowait` percentage combined with high `tm_act` percentages on specific disks is an indication of disk saturation.

Note:

A high `iowait` alone is not necessarily an indication of an Input-Output bottleneck.

### A.2.9 Resilvering with Oracle Database

If you disable mirror write consistency for an Oracle data file allocated on a raw logical volume, then the Oracle Database crash recovery process uses resilvering to recover after a system failure. This resilvering process prevents database inconsistencies or corruption.

During crash recovery, if a data file is allocated on a logical volume with multiple copies, then the resilvering process performs a checksum on the data blocks of all the copies. It then performs one of the following:

- If the data blocks in a copy have valid checksums, then the resilvering process uses that copy to update the copies that have invalid checksums.
- If all copies have blocks with invalid checksums, then the resilvering process rebuilds the blocks using information from the redo log file. It then writes the data file to the logical volume and updates all the copies.

On AIX, the resilvering process works only for data files allocated on raw logical volumes for which mirror write consistency is disabled. Resilvering is not required for data files on mirrored logical volumes with mirror write consistency enabled, because mirror write consistency ensures that all copies are synchronized.

If the system fails while you are upgrading an earlier release of Oracle Database that used data files on logical volumes for which mirror write consistency was disabled, then run the `syncvg` command to synchronize the mirrored logical volume before starting Oracle Database. If you do not synchronize the mirrored logical volume before starting the database, then Oracle Database may read incorrect data from an logical volume copy.

Note:

If a disk drive fails, then resilvering does not occur. You must run the `syncvg` command before you can reactivate the logical volume.

Caution:

Oracle supports resilvering for data files only. Do not disable mirror write consistency for redo log files.

## A.3 CPU Scheduling and Process Priorities

The CPU is another system component for which processes may contend. Although the AIX kernel allocates CPU effectively most of the time, many processes compete for CPU cycles. If the system has multiple CPU (SMP), then there may be different levels of contention on each CPU.

The following sections provide information about CPU scheduling and process priorities:

- Changing Process Running Time Slice
- Using Processor Binding on SMP Systems

### A.3.1 Changing Process Running Time Slice

The default value for the run-time slice of the AIX RR dispatcher is ten milliseconds (msec). Use the `schedo` command to change the time slice. A longer time slice causes a lower context switch rate if the average voluntary switch rate of the applications is lower. As a result, fewer CPU cycles are spent on context-switching for a process and the system throughput should improve.

However, a longer run-time slice can deteriorate response time, especially on a uniprocessor system. The default run-time slice is usually acceptable for most applications. When the run queue is high and most of the applications and Oracle shadow processes are capable of running a much longer duration, you may want to increase the time slice by entering the following command:

```
f # /usr/sbin/schedo -t n
```

In the preceding command, setting `n` to 0 results in a slice of 10 msec, choosing a value of 1 results in a slice of 20 msec, choosing a value of 2 results in a slice of 30 msec, and so on.

### A.3.2 Using Processor Binding on SMP Systems

Binding certain processes to a processor can improve performance substantially on an SMP system. Processor binding is available and fully functional on AIX 5L.

However, starting with AIX 5L, specific improvements in the AIX scheduler enables Oracle Database processes to be scheduled optimally without processor binding. Therefore, Oracle no longer recommends binding processes to processors when running on AIX 5L version 5.3 or later.

## A.4 Setting the AIXTHREAD\_SCOPE Environment Variable

Threads in AIX can run with process-wide contention scope (M:N) or with systemwide contention scope (1:1). The `AIXTHREAD_SCOPE` environment variable controls which contention scope is used.

The default value of the `AIXTHREAD_SCOPE` environment variable is `P`, which specifies process-wide contention scope. When using process-wide contention scope, Oracle threads are mapped to a pool of kernel threads. When Oracle is waiting on an event and its thread is swapped out, it may return on a different kernel thread with a different thread ID. Oracle uses the thread ID to post waiting processes, so it is important for the thread ID to remain the same. When using systemwide contention scope, Oracle threads are mapped to kernel threads statically, one to one. For this reason, Oracle recommends that you use systemwide contention. The use of systemwide contention is especially critical for Oracle Real Application Clusters (Oracle RAC) instances.

In addition, on AIX 5L version 5.3 or later, if you set systemwide contention scope, then significantly less memory is allocated to each Oracle process.

Oracle recommends that you set the value of the `AIXTHREAD_SCOPE` environment variable to `S` in the environment script that you use to set the `ORACLE_HOME` or `ORACLE_SID` environment variables for an Oracle Database instance or an Oracle Net listener process as follows:

- Bourne, Bash, or Korn shell:
	Add the following line to the `~/.profile` or `/usr/local/bin/oraenv` script:
	```
	AIXTHREAD_SCOPE=S; export AIXTHREAD_SCOPE
	```
- C shell:
	Add the following line to the `~/.login` or `/usr/local/bin/coraenv` script:
	```
	setenv AIXTHREAD_SCOPE S
	```

Doing this enables systemwide thread scope for running all Oracle processes.

## A.5 Network Information Service external naming support

Network Information Service external naming adapter is supported on AIX. To configure and use Network Information Service external naming, refer to the "Configuring External Naming Methods" section of [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/naming.htm#NETAG277).

## A.6 Simultaneous Multithreading on AIX 5.3 and Later Versions

If Simultaneous Multithreading is enabled, and AIX 5.3 and later version operating system is used, then the `v$osstat` view reports 2 additional rows corresponding to the online logical (`NUM_LCPUS`) and virtual cpus (`NUM_VCPUS`).

If Oracle is run on AIX 5.3 and later versions without Simultaneous Multithreading, then these rows are not reported.

## A.7 Configuring IBM JSSE Provider with Oracle JDBC Thin Driver

If you want to configure SSL on IBM JDK, then you may face the following issues:

- IBM JSSE does not support `SSLv2Hello` SSL protocol
	For SSL clients using Thin JDBC connectors, you must set `oracle.net.ss1_version` system property to select `TLSv1` SSL protocol or `SSLv3` SSL protocol
- IBM JSSE does not allow anonymous ciphers
	For SSL clients using anonymous ciphers, you must replace the Default Trust Manager with a Custom Trust Manager that accepts anonymous ciphers.
	See Also:
	IBM JSSE documentation for more information on creating and installing Custom Trust Manager