---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-PROCESS.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.129 V$PROCESS

`V$PROCESS` displays information about the currently active processes.

| Column | Datatype | Description |
| --- | --- | --- |
| `ADDR` | `RAW(4 \| 8)` | Address of the process state object |
| `PID` | `NUMBER` | Oracle process identifier |
| `SOSID` | `VARCHAR2(24)` | Operating system (process, thread) identifier.  This identifier is unique whether the Oracle multiprocess/multithread feature is enabled or not. |
| `SPID` | `VARCHAR2(24)` | Operating system process identifier.  The Oracle multiprocess/multithread feature is available for UNIX systems.  When the Oracle multiprocess/multithread feature is enabled, RDBMS processes are mapped to threads running in operating system processes, and the `SPID` identifier is not unique for RDBMS processes.  When the Oracle multiprocess/multithread feature is not enabled on UNIX systems, the `SPID` identifier is unique for RDBMS processes. |
| `STID` | `VARCHAR2(24)` | Operating system thread identifier.  The Oracle multiprocess/multithread feature is available for UNIX systems.  When the Oracle multiprocess/multithread feature is enabled, RDBMS processes are mapped to threads running in operating system processes, and the `SPID` and `STID` together uniquely identify an RDBMS process.  The `STID` is not unique on Solaris. The `STID` is unique on Linux, AIX, and Microsoft Windows. |
| `EXECUTION_TYPE` | `VARCHAR2(10)` | Operating system execution type |
| `PNAME` | `VARCHAR2(5)` | Name of this process |
| `USERNAME` | `VARCHAR2(15)` | Operating system process username |
| `SERIAL#` | `NUMBER` | Process serial number |
| `TERMINAL` | `VARCHAR2(30)` | Operating system terminal identifier |
| `PROGRAM` | `VARCHAR2(84)` | Program in progress |
| `TRACEID` | `VARCHAR2(255)` | Trace file identifier |
| `TRACEFILE` | `VARCHAR2(513)` | Trace file name of the process |
| `BACKGROUND` | `VARCHAR2(1)` | `1` for a SYSTEM background process; NULL for foreground processes or non-SYSTEM background processes |
| `LATCHWAIT` | `VARCHAR2(16)` | Address of the latch the process is waiting for; NULL if none |
| `LATCHSPIN` | `VARCHAR2(16)` | This column is obsolete |
| `PGA_USED_MEM` | `NUMBER` | PGA memory currently used by the process (in bytes) |
| `PGA_ALLOC_MEM` | `NUMBER` | PGA memory currently allocated by the process (including free PGA memory not yet released to the operating system by the server process), in bytes |
| `PGA_FREEABLE_MEM` | `NUMBER` | Allocated PGA memory which can be freed (in bytes) |
| `PGA_MAX_MEM` | `NUMBER` | Maximum PGA memory ever allocated by the process (in bytes) |
| `NUMA_DEFAULT` | `NUMBER` | The NUMA processor group of this process at initialization time |
| `NUMA_CURR` | `NUMBER` | The NUMA processor group of this process currently |
| `CPU_USED` | `NUMBER` | Tracks the CPU used by this process (in microseconds) from the time it was spawned |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |