---
title: Administering Oracle Database on Solaris
book: "Administrator's Reference for Linux and UNIX-Based Operating Systems"
doc_id: E10839-25
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e10839/appe_sol.htm
tags:
  - oracle
  - 11g
  - administrators-reference-for-linux-and-unix-based-operating-systems
---

## D Administering Oracle Database on Solaris

This appendix contains information about administering Oracle Database on Solaris.

## D.1 Intimate Shared Memory

On Solaris systems, Oracle Database uses Intimate Shared Memory for shared memory segments because it shares virtual memory resources between Oracle processes. Intimate Shared Memory causes the physical memory for the entire shared memory segment to be locked automatically.

On Solaris 10 systems, dynamic/pageable Intimate Shared Memory is available. This enables Oracle Database to share virtual memory resources between processes sharing the segment, and at the same time, enables memory paging. The operating system does not have to lock down physical memory for the entire shared memory segment.

Oracle Database automatically selects Intimate Shared Memory or Dynamic Intimate Shared Memory based on the following criteria:

- Oracle Database uses Dynamic Intimate Shared Memory if it is available on the system, and if the value of the `SGA_MAX_SIZE` initialization parameter is larger than the size required for all SGA components combined. This enables Oracle Database to lock only the amount of physical memory that is used. Oracle Database also uses `DISM` if it is available on the system and `MEMORY_TARGET` or `MEMORY_MAX_TARGET` is set by the user.
- Oracle Database uses Intimate Shared Memory if the entire shared memory segment is in use at startup or if the value of the `SGA_MAX_SIZE` parameter equals or smaller than the size required for all SGA components combined.

Regardless of whether Oracle Database uses Intimate Shared Memory or Dynamic Intimate Shared Memory, it can always exchange the memory between dynamically sizable components such as the buffer cache, the shared pool, and the large pool after it starts an instance. Oracle Database can relinquish memory from one dynamic SGA component and allocate it to another component.

Because shared memory segments are not implicitly locked in memory, when using Dynamic Intimate Shared Memory, Oracle Database explicitly locks shared memory that is currently in use at startup. When a dynamic SGA operation uses more shared memory, Oracle Database explicitly performs a lock operation on the memory that is put to use. When a dynamic SGA operation releases shared memory, Oracle Database explicitly performs an unlock operation on the memory that is freed, so that it becomes available to other applications.

Oracle Database uses the `oradism` utility to lock and unlock shared memory. The `oradism` utility is automatically set up during installation. It is not required to perform any configuration tasks to use dynamic SGA.

Note:

- Do not set the `LOCK_SGA` parameter to `TRUE` in the server parameter file. If you do, then Oracle Database 11g cannot start.
- The process name for the `oradism` utility is `ora_dism_sid`, where `sid` is the system identifier. When using Dynamic Intimate Shared Memory, this process is started during instance startup, and automatically quits when the instance is shut down.
	If a message is displayed in the alert log saying that the `oradism` utility is not set up correctly, then verify that the `oradism` utility is located in the `$ORACLE_HOME/bin` directory and that it has superuser privileges.