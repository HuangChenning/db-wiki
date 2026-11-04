---
title: Administering Oracle Database on HP-UX
book: "Administrator's Reference for Linux and UNIX-Based Operating Systems"
doc_id: E10839-25
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e10839/appb_hpux.htm
tags:
  - oracle
  - 11g
  - administrators-reference-for-linux-and-unix-based-operating-systems
---

## C Administering Oracle Database on HP-UX

This appendix provides information about administering Oracle Database on HP-UX. It contains the following topics:

## C.1 HP-UX Shared Memory Segments for an Oracle Instance

When an Oracle Database instance starts, it creates memory segments by dividing the shared memory allocated for creating the Oracle System Global Area (SGA) by the value of the HP-UX `shmmax` kernel parameter. For example, if 64 GB of shared memory is allocated for a single Oracle instance and the value of the `shmmax` parameter is 1 GB, then Oracle Database creates 64 shared memory segments for that instance.

Performance degradation can occur when an Oracle instance creates multiple shared memory segments. This is because each shared memory segment receives a unique protection key when Oracle Database creates the instance. The number of protection keys available depends on the system architecture as shown in the following table:

| Architecture | Number of Protection Keys |
| --- | --- |
| PA-RISC | 6 |
| Itanium | 14 |

If the Oracle instance creates more shared memory segments than the number of protection keys, then the HP-UX operating system displays protection key faults.

Oracle recommends that you set the `shmmax` parameter value to the amount of available physical memory on the system. Doing this ensures that the entire shared memory for a single Oracle instance is assigned to one shared memory segment and the instance requires only one protection key.

To display the list of active shared memory segments on the system, run the following command:

```
$ ipcs -m
```

If Oracle Database creates more segments for the instance than the number of protection keys, then increase the value of the `shmmax` kernel parameter.

## C.2 HP-UX SCHED\_NOAGE Scheduling Policy

On HP-UX, most processes use a time-sharing scheduling policy. Time sharing can have detrimental effects on Oracle performance by descheduling an Oracle process during critical operations, for example, when it is holding a latch. HP-UX has a modified scheduling policy, referred to as `SCHED_NOAGE`, that specifically addresses this issue. Unlike the normal time-sharing policy, a process scheduled using `SCHED_NOAGE` does not increase or decrease in priority, nor is it preempted.

This feature is suited to online transaction processing environments because online transaction processing environments can cause competition for critical resources. The use of the `SCHED_NOAGE` policy with Oracle Database can increase performance by 10 percent or more in online transaction processing environments.

The `SCHED_NOAGE` policy does not provide the same level of performance gains in decision support environments because there is less resource competition. Because each application and server environment is different, you should test and verify that the environment benefits from the `SCHED_NOAGE` policy. When using `SCHED_NOAGE`, Oracle recommends that you exercise caution in assigning highest priority to Oracle processes. Assigning highest `SCHED_NOAGE` priority to Oracle processes can exhaust CPU resources on the system, causing other user processes to stop responding.

### C.2.1 Enabling SCHED\_NOAGE for Oracle Database

To permit Oracle Database to use the `SCHED_NOAGE` scheduling policy, the OSDBA group (typically, the `dba` group) must have the `RTSCHED` and `RTPRIO` privileges to change the scheduling policy and set the priority level for Oracle processes. To give the `dba` group these privileges:

1. Log in as the `root` user.
2. Using any text editor, open the `/etc/privgroup` file, or create it if necessary.
3. Add or edit the following line, which begins with the name of the OSDBA group, specifying the privileges `RTPRIO` and `RTSCHED` that you want to grant to this group every time the system restarts:
	```
	dba RTPRIO RTSCHED
	```
4. Save the file and quit the text editor.
5. Enter the following command to grant the privileges to the OSDBA group:
	```
	# /usr/sbin/setprivgrp -f /etc/privgroup
	```
6. Enter the following command to verify that the privileges are set correctly:
	```
	# /usr/bin/getprivgrp dba
	```

`HPUX_SCHED_NOAGE` is a static initialization parameter and instance bounce is required for a new setting to take effect. Add this `HPUX_SCHED_NOAGE` initialization parameter to the parameter file for each instance, setting the parameter to an integer value to specify process priority levels. The supported range of values is 178 to 255. Lower values represent higher priorities. The default value of `HPUX_SCHED_NOAGE` initialization parameter is 178 for all Oracle processes. For LMS processes, this can be changed by setting the initialization parameter `_os_sched_high_priority`. If the parameter `_os_sched_high_priority` is between 31 and 2, LMS processes run with `SCHED_RR` at the set priority. If the parameter value is between 178 and 255, the processes run at the set value with `SCHED_NOAGE`. However, LMS does not run at priority level less than the value of `HPUX_SCHED_NOAGE`.

If the `HPUX_SCHED_NOAGE` parameter setting is out of range, then Oracle Database automatically sets the parameter to a permissible value and continues with the `SCHED_NOAGE` policy with the new value. It also generates a message in the `alert_` `sid``.log` file about the new setting. Whenever the highest priority is assigned to Oracle processes, either by the user or by automatic readjustment, Oracle Database generates a message in the `alert_` `sid``.log` file warning about the possibility of exhaustion of CPU resources on the system. Oracle recommends that you set the parameter to assign the priority level you want for Oracle processes.

See Also:

The HP-UX documentation, the `rtsched` (1) man page, and the `rtsched` (2) man page for more information about priority policies and priority ranges

## C.3 Lightweight Timer Implementation

With Oracle Database 11g, you can collect run-time statistics always if the dynamic initialization parameter `STATISTICS_LEVEL` is set to `TYPICAL` (default) or `ALL`. This parameter setting implicitly sets the `TIMED_STATISTICS` initialization parameter to `true`. Oracle Database on HP-UX systems uses the `gethrtime()` system library call to calculate elapsed times during the collection of the statistics. The use of this lightweight system library call enables you to collect run-time statistics always while running an Oracle instance, without affecting performance.

This system library call can provide a performance improvement of up to 10 percent over an Oracle release that does not use the `gethrtime()` system library call when the `TIMED_STATISTICS` initialization parameter is explicitly set to `true`. In addition, there is no negative impact on the online transaction processing performance of an Oracle Database while using the `gethrtime()` system library call to collect run-time statistics always.

## C.4 Asynchronous Input-Output

The asynchronous Input-Output pseudo-driver on HP-UX enables Oracle Database to perform Input-Output to raw disk partitions using an asynchronous method, resulting in less Input-Output overhead and higher throughput. You can use the asynchronous Input-Output pseudo-driver on both HP-UX servers and workstations.

This section contains the following topics:

- MLOCK Privilege
- Implementing Asynchronous Input-Output
- Verifying Asynchronous Input-Output
- Asynchronous Flag in SGA

### C.4.1 MLOCK Privilege

To permit Oracle Database to process asynchronous Input-Output operations, the OSDBA group (`dba`) must have the `MLOCK` privilege. To give the `dba` group the `MLOCK` privilege:

1. Log in as the `root` user.
2. Using any text editor, open the `/etc/privgroup` file, or create it if necessary.
3. Add or edit the following line, which begins with the name of the OSDBA group, specifying the privilege `MLOCK`:
	Note:
	You must use only one line to specify the privileges for a particular group in this file. If the file contains a line for the `dba` group, then add the `MLOCK` privilege on the same line.
	```
	dba RTPRIO RTSCHED MLOCK
	```
4. Save the file, and quit the text editor.
5. Enter the following command to grant the privileges to the OSDBA group:
	```
	# /usr/sbin/setprivgrp -f /etc/privgroup
	```
6. Enter the following command to verify that the privileges are set correctly:
	```
	# /usr/bin/getprivgrp dba
	```

### C.4.2 Implementing Asynchronous Input-Output

To use asynchronous Input-Output on HP-UX, you must use an Automatic Storage Management disk group that uses raw partitions as the storage option for database files.

See Also:

[Oracle Database Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for more information about configuring Automatic Storage Management and raw logical volumes on HP-UX systems

Before you can implement asynchronous Input-Output with either storage option, you must use the System Administrator Management utility to configure the asynchronous disk driver into the HP-UX kernel.

Note:

In Oracle Database 11g Release 1, you did not have to set `DISK_ASYNCH_IO` paramter to `FALSE` on a file system. However, starting with Oracle Database 11g Release 2, if database uses file system for storing the database files, then ensure that you set initialization parameter `DISK_ASYNCH_IO` to `FALSE`. By default the value of `DISK_ASYNCH_IO` is `TRUE`.

The `DISK_ASYNCH_IO` parameter must be set to `TRUE` only when raw partitions are used for storing database files.

To add the asynchronous disk driver and configure the kernel by using the System Administrator Management utility:

1. Run the following command as the `root` user:
	```
	# sam
	```
2. Select the Kernel Configuration area.
3. Select the Drivers area.
4. Select the asynchronous disk driver (`asyncdsk`).
5. Select Actions, and then select Add Driver to Kernel.
6. Select List, and then select Configurable Parameters.
7. Select the `MAX_ASYNC_PORTS` parameter.
8. Select Action, and then select Modify Configurable Parameter.
9. Specify a new value for the parameter, using the following guidelines, and then click OK.
	The `MAX_ASYNC_PORTS` parameter is a configurable HP-UX kernel parameter that controls the maximum number of processes that can open the `/dev/async` file simultaneously.
	The system displays an error message when a process tries to open the `/dev/async` file after the maximum number of processes have opened the file. This error can reduce performance on systems with a large number of shadow processes or many parallel query slaves performing asynchronous Input-Output. This error is not recorded. To avoid this error, estimate the highest likely number of processes that can access the `/dev/async` file and set the `MAX_ASYNC_PORTS` parameter to this value.
10. Select Actions, and then select Process a New Kernel.
11. Select one of the following options, and then click OK:
	- Move Kernel Into Place and Shutdown System/Reboot Now
		- Do Not Move Kernel Into Place: Do Not Shutdown/Reboot Now
	If you choose the second option, then the new kernel, `vmunix_test`, and the `system.SAM` configuration file used to create it, are both created in the `/stand/build` directory.

To enable asynchronous Input-Output operations using the HP-UX asynchronous device driver:

1. Log in as the `root` user.
2. If `/dev/async` does not exist, use the following command to create it:
	```
	# /sbin/mknod /dev/async c 101 0x104
	```
	By default, the minor number is set to 0. The following table describes the various minor numbers for 8-bit that you can use to create a device file:
	| Minor number | Description |
	| --- | --- |
	| 0x0 | This is the HP-UX default value for `/dev/async`. |
	| 0x4 | Enable disc device timeouts to complete with an error code rather than retrying forever. This setting is necessary for application-level disc mirroring, so as to avoid the situation where the application waits forever for a failed disc device to be repaired. Oracle RDBMS users should enable this feature when Automatic Storage Management mirroring/replication (internal redundancy) is used. SGA will be locked in memory. |
	| 0x100 | Enable on-demand locking of memory pages by async driver when asyncdsk\_open(2) is called. A low-overhead routine is then used to lock a page into memory during I/O operations.  On-demand locking is critically important when using Oracle's Automatic Memory Management feature (the use of `MEMORY_TARGET` in the `init.ora` file to control memory usage). RDBMS deployments utilizing dynamic nPar or dynamic vPar features should also configure on-demand locking.  More traditional RDBMS deployments can consider on-demand locking in light of its more obvious effects. Generally speaking, RDBMS startup is quicker because the complete SGA is not locked into memory immediately. However, some instances will experience a slight run-time performance penalty with on-demand locking as memory pages are dynamically locked/unlocked for each I/O request. |
	| 0x104 | Enable ASM I/O operation timeouts for Grid Infrastructure installations. This is a combination of 0x100 and 0x4. Both the features are enabled. |
3. Enter the following command to verify that the `/dev/async` device file exists and has the major number 101:
	```
	# ls -l /dev/async
	```
	The output of this command should look similar to the following:
	```
	crw------- 1 oracle   dba     101 0x000000 Oct 28 10:32  /dev/async
	```
4. If required, give the device file the operating system owner and permissions consistent with those of the Oracle software owner and OSDBA group.
	If the Oracle software owner is `oracle` and the OSDBA group is `dba`, then run the following commands:
	```
	# /usr/bin/chown oracle:dba /dev/async
	# /usr/bin/chmod 660 /dev/async
	```

### C.4.3 Verifying Asynchronous Input-Output

To verify asynchronous Input-Output, first verify that the HP-UX asynchronous driver is configured for Oracle Database, then verify that Oracle Database is executing asynchronous Input-Output through the HP-UX device driver:

- Verifying That HP-UX Asynchronous Driver is Configured for Oracle Database
- Verifying that Oracle Database is Using Asynchronous Input-Output

#### C.4.3.1 Verifying That HP-UX Asynchronous Driver is Configured for Oracle Database

To verify that the HP-UX asynchronous driver is configured properly for Oracle Database:

1. Start Oracle Database with a few parallel query slave processes.
2. Start the GlancePlus/UX utility as follows:
	```
	$ gpm
	```
3. In the main window, click Reports and then click Process List.
4. In the Process List window, select one parallel query slave process, select Reports, and then select Process Open Files.
	The list of files currently opened by the parallel query slave process is displayed.
5. In the list of open files, check for the `/dev/async` file or the 101 0x104000 mode.
	If either is in the list, then the `/dev/async` file has been opened by the parallel query slave process, and the HP-UX asynchronous device driver is configured properly to enable Oracle processes to run asynchronous Input-Output. Make a note of the file descriptor number for the `/dev/async` file.

#### C.4.3.2 Verifying that Oracle Database is Using Asynchronous Input-Output

To verify that Oracle Database is using asynchronous Input-Output through the HP-UX asynchronous device driver:

1. Attach the HP-UX `tusc` utility to the same Oracle parallel query slave that you selected in GlancePlus in the preceding procedure.
2. Run an Input-Output bound query in the environment.
3. Check the pattern of read and write calls in the `tusc` output.
	You can do this, for example, by entering the following command, where `pid` is the process ID of a parallel query slave supposed to process asynchronous Input-Output:
	```
	$ tusc -p pid > tusc.output
	```
4. After running the query, press Ctrl+c to disconnect from the process, and then open the `tusc.output` file.
	The following example shows a sample `tusc.output` file:
	```
	( Attached to process 2052: "ora_p000_tpch" [ 64-bit ])
	................... 
	........................ 
	[2052] read(9, "80\0\001\013  \b\0\0\0\0\0\0\0\0".., 388) .. = 28 
	[2052] write(9, "\0\0\00e\0\0\0\080\0\001\013Ð \0".., 48) .. = 48 
	[2052] read(9, "80\0\001\013¢ 18\0\0\0\0\0\0\0\0".., 388) .. = 28 
	[2052] write(9, "\0\0\00e\0\0\0\080\0\001\01bd4\0".., 48) .. = 48
	```
	If the `DISK_ASYNCH_IO` initialization parameter is not explicitly set to `false` (set to `true` by default), then the `tusc.output` file shows a pattern of asynchronous read/write calls of the same file descriptor (9 in the preceding example) back to back.
	Map the file descriptor number in the `tusc.output` file to that used by `/dev/async` file in GlancePlus. They should match for the particular parallel query slave process. This verifies that Input-Output through the HP-UX asynchronous driver is asynchronous. With synchronous Input-Output, or if the `DISK_ASYNCH_IO` initialization parameter is explicitly set to `FALSE`, you do not see the asynchronous read/write pattern described previously. Instead, you see calls to `lseek` or `pread` / `pwrite`. You also see many different file descriptors (the first argument to read/write) instead of just a single file descriptor.

### C.4.4 Asynchronous Flag in SGA

Oracle Database on HP-UX uses a nonblocking polling facility provided by the HP-UX asynchronous driver to check the status of Input-Output operations. This polling is performed by checking a flag that is updated by the asynchronous driver based on the status of the Input-Output operations submitted. HP-UX requires that this flag be in shared memory.

Oracle Database configures an asynchronous flag in the SGA for each Oracle process. Oracle Database on HP-UX has a true asynchronous Input-Output mechanism where Input-Output requests can be issued even though some previously issued Input-Output operations are not complete. This helps to enhance performance and ensures good scalability of parallel Input-Output processes.

Releases of Oracle Database earlier than release 8.1.7 were able to run Input-Output operations only from shared memory by using the HP-UX asynchronous driver. Oracle Database 11g runs Input-Output operations from both shared memory and process-private regions using the new HP-UX asynchronous driver. However, Input-Output operations through the asynchronous driver are not asynchronous in nature. This is because Oracle Database must perform a blocking wait to check the status of Input-Output operations submitted to the asynchronous driver. This causes some Oracle processes, such as the database writer process, to essentially process synchronous Input-Output.

## C.5 Large Memory Allocations and Oracle Database Tuning

Applications running on Oracle Database 11g can use significantly more memory than applications running on earlier releases. This is because Oracle Database 11g changes the default setting for virtual memory data pages from D (4KB) to L (4 GB) on HP-UX systems.

This section contains the following topics:

- Default Large Virtual Memory Page Size
- Tuning Recommendations
- Tunable Base Page Size

### C.5.1 Default Large Virtual Memory Page Size

By default, Oracle Database uses the largest virtual memory page size setting available on HP-UX for allocating process-private memory. It is defined by the value `L` (largest.) This value is set as one of the `LARGE_PAGE_FLAGS` options when linking an Oracle executable.

When the virtual memory page size is set to L, HP-UX allocates the available process-private memory to pages of 1 MB, 4 MB, 16 MB and so on, until it reaches the 1 GB limit, or until it reaches the total amount of allocated memory. If you allocate enough memory to the Oracle PGA for the operating system to be able to allocate memory in larger data page size units, then the operating system allocates the maximum page size at once. For example, if you allocate 48 MB for the Oracle PGA, then the system can have either 3 pages each of 16 MB, or a series of pages in unit sizes with the smaller multiples. For example, four 1 MB pages, three 4 MB pages, and two 16 MB pages. If you allocate 64 MB to the PGA, then the operating system allocates one page of 64 MB, as the data page unit size matches the available memory.

In general, large memory pages yield better application performance by reducing the number of virtual memory translation faults that must be handled by the operating system, freeing more CPU resources for the application. Large pages help to reduce the total number of data pages required to allocate the process-private memory. This reduction decreases the chances of translation lookaside buffer misses at the processor level.

However, if applications are constrained in memory and tend to run a very large number of processes, then this drastic page size increase may lead processes to indicate large memory allocations, followed by an `Out of memory` error message. If this happens, then you must lower the page size to a value between the D (default) size of 4 KB and the `L` (largest) size of 4 GB.

With the lowest page size setting (4 KB), CPU utilization can be 20 percent higher than that with a larger page size setting. With the highest setting of `L`, the memory utilization can be 50 percent higher than that with a 4 MB setting. In cases where the system shows memory constraints, Oracle recommends that you set the page size to match the requirements of the particular application, within the constraints of available memory resources.

For example, an application that has problems with the `L` setting may show reasonable performance with a 4 MB virtual memory page setting.

### C.5.2 Tuning Recommendations

To address tuning for the increased memory allocation required for persistent private SQL areas and large virtual memory page sizes, Oracle recommends that you decrease the virtual memory data page size for Oracle Database as required. Use the following command to alter the page size setting:

```
# /usr/bin/chatr +pd newsize $ORACLE_HOME/bin/oracle
```

In the preceding example, `newsize` represents the new value of the virtual memory page size.

Display the new setting using the `chatr` command as follows:

```
# /usr/bin/chatr $ORACLE_HOME/bin/oracle
```

### C.5.3 Tunable Base Page Size

A large base page size enables efficient memory management. The default value for `base_pagesize` is 4 KB. The new feature introduced with HP-UX 11.31 enables to adjust the size of the base page, by invoking `kctune` (1 M) to change the tunable `base_pagesize` and then restart the computer.

Note:

The base page size feature is not supported on HP-UX PA RISC operating system.

## C.6 CPU\_COUNT Initialization Parameter and HP-UX Dynamic Processor Reconfiguration

HP-UX 11i supports dynamic run-time reconfiguration of processor sets and dynamic reassignment of workload between processor sets by valid users.

HP-UX Virtual Partitions enable users to configure their systems in multiple logical partitions where each partition is assigned its own set of processors, memory, and Input-Output resources, and can run a separate instance of the HP-UX operating system. HP-UX processor sets integrated with vPars support dynamic processor migration from one virtual partition to another without requiring a restart of any virtual partition. This helps to provide efficient resource partitioning between applications to minimize interference and guarantees necessary resource allocation to each application running on the HP-UX server.

See Also:

Refer to the " [System and Database Changes](https://docs.oracle.com/cd/E11882_01/server.112/e40540/cmntopc.htm#CNCPT1985) " section in the [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/toc.htm) guide for more information on dynamic resource provisioning

## C.7 Network Information Service external naming support

Network Information Service external naming adapter is supported on HP-UX. To configure and use Network Information Service external naming, refer to the "Configuring External Naming Methods" section of [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm).

## C.8 Activating and Setting Expanded Host Names and Node Names

The system node names and host names have default length limits of 8 and 64 bytes. The system administrator can configure the system to expand both these limits to 255 bytes.

A dynamic kernel tunable parameter `expanded_node_host_names`, must be turned on to allow larger names to be set.

To turn on the kernel parameter, run the following command:

```
kctune expanded_node_host_names=1
```

To turn off the kernel parameter, run the following command:

```
kctune expanded_node_host_names=0
```