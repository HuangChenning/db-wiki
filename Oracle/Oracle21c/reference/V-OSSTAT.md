---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-OSSTAT.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.106 V$OSSTAT

`V$OSSTAT` displays system utilization statistics from the operating system. One row is returned for each system statistic.

| Column | Datatype | Description |
| --- | --- | --- |
| `STAT_NAME` | `VARCHAR2(64)` | Name of the statistic (see Table 9-3) |
| `VALUE` | `NUMBER` | Instantaneous statistic value |
| `OSSTAT_ID` | `NUMBER` | Statistic ID |
| `COMMENTS` | `VARCHAR2(64)` | Any additional operating system-specific clarifications for the statistic |
| `CUMULATIVE` | `VARCHAR2(3)` | Indicates whether the statistic is cumulative (that is, accumulates over time) (`YES`) or not (`NO`) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Table 9-3 V$OSSTAT Statistics

| Statistic Name | Description |
| --- | --- |
| NUM\_CPUS | Number of CPUs or processors available |
| IDLE\_TIME | Number of hundredths of a second that a processor has been idle, totalled over all processors |
| BUSY\_TIME | Number of hundredths of a second that a processor has been busy executing user or kernel code, totalled over all processors |
| USER\_TIME | Number of hundredths of a second that a processor has been busy executing user code, totalled over all processors |
| SYS\_TIME | Number of hundredths of a second that a processor has been busy executing kernel code, totalled over all processors |
| IOWAIT\_TIME | Number of hundredths of a second that a processor has been waiting for I/O to complete, totalled over all processors |
| NICE\_TIME | Number of hundredths of a second that a processor has been busy executing low-priority user code, totalled over all processors |
| AVG\_IDLE\_TIME | Number of hundredths of a second that a processor has been idle, averaged over all processors |
| AVG\_BUSY\_TIME | Number of hundredths of a second that a processor has been busy executing user or kernel code, averaged over all processors |
| AVG\_USER\_TIME | Number of hundredths of a second that a processor has been busy executing user code, averaged over all processors |
| AVG\_SYS\_TIME | Number of hundredths of a second that a processor has been busy executing kernel code, averaged over all processors |
| AVG\_IOWAIT\_TIME | Number of hundredths of a second that a processor has been waiting for I/O to complete, averaged over all processors |
| AVG\_NICE\_TIME | Number of hundredths of a second that a processor has been busy executing low-priority user code, averaged over all processors |
| OS\_CPU\_WAIT\_TIME | Total number of hundredths of a second that processes have been in a ready state, waiting to be selected by the operating system scheduler to run |
| RSRC\_MGR\_CPU\_WAIT\_TIME | Total number of hundredths of a second that Oracle processes have been in a ready state, waiting for CPU to be available for their consumer group in the currently active resource plan |
| VM\_IN\_BYTES | Total number of bytes of data that have been paged in due to virtual memory paging |
| VM\_OUT\_BYTES | Total number of bytes of data that have been paged out due to virtual memory paging |
| PHYSICAL\_MEMORY\_BYTES | Total number of bytes of physical memory |
| LOAD | Current number of processes that are either running or in the ready state, waiting to be selected by the operating-system scheduler to run. On many platforms, this statistic reflects the average load over the past minute. |
| NUM\_CPU\_CORES | Number of CPU cores available (includes subcores of multicore CPUs as well as single-core CPUs) |
| NUM\_CPU\_SOCKETS | Number of CPU sockets available (represents an absolute count of CPU chips on the system, regardless of multithreading or multi-core architectures) |
| NUM\_VCPUS | Number of virtual CPUs available |
| NUM\_LCPUS | Number of logical CPUs available (includes hardware threads if hardware threading is turned on) |
| TCP\_SEND\_SIZE\_MIN | Minimum size of the TCP send buffer |
| TCP\_SEND\_SIZE\_DEFAULT | Default size of the TCP send buffer |
| TCP\_SEND\_SIZE\_MAX | Maximum size of the TCP send buffer |
| TCP\_RECEIVE\_SIZE\_MIN | Minimum size of the TCP receive buffer |
| TCP\_RECEIVE\_SIZE\_DEFAULT | Default size of the TCP receive buffer |
| TCP\_RECEIVE\_SIZE\_MAX | Maximum size of the TCP receive buffer |
| GLOBAL\_SEND\_SIZE\_MAX | Maximum size of the global send buffer |
| GLOBAL\_RECEIVE\_SIZE\_MAX | Maximum size of the global receive buffer |

Note:

The availability of all statistics except for `NUM_CPUS` and `RSRC_MGR_CPU_WAIT_TIME` is subject to the operating system platform on which the Oracle Database is running.