---
title: "V$PX_PROCESS_SYSSTAT"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2114.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$PX_PROCESS_SYSSTAT` contains information about the sessions running parallel execution.

| Column | Datatype | Description |
| --- | --- | --- |
| `STATISTIC` | `VARCHAR2(30)` | Name of the statistic: - `Servers In Use` - Number of PX servers currently performing parallel operations - `Servers Available` - Number of PX servers available to perform parallel operations - `Servers Started` - Number of times the system has had to create a PX server process - `Servers Shutdown` - Number of times a PX server process has been shut down. A PX server process will be shut down if it has not been used recently. 	If this value is large, then consider increasing the parameter. This will improve performance by avoiding the latency of PX server process creation. - `Servers HWM` - Maximum number of concurrent PX server processes 	If this number is equal to the `PARALLEL_MAX_SERVERS` initialization parameter, then consider increasing the parameter. This could allow you to increase your throughput, especially if your system is under-utilized and the `V$SYSSTAT` statistic "Parallel operations downgraded to serial" is large. - `Servers Cleaned Up` - Number of times PMON had to clean up a PX server. This should only happen during abnormal termination of a parallel operation. 	If this number is large, then you should determine the cause. - Server Sessions - Total number of sessions created by all PX servers - `Memory Chunks Allocated` - Number of large memory chunks allocated by PX servers - `Memory Chunks Freed` - Number of large memory chunks freed - `Memory Chunks Current` - Number of large memory chunks currently being used - `Memory Chunks HWM` - Maximum number of concurrently allocated chunks - `Buffers allocated` - Number of times a message buffer has been allocated - `Buffers freed` - Number of times a message buffer has been freed - `Buffers Current` - Number of message buffers currently being used - `Buffers HWM` - Maximum number of concurrently allocated message buffers |
| `VALUE` | `NUMBER` | Value of the statistic |