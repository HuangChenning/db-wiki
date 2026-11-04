---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/LOG_ARCHIVE_TRACE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.191 LOG\_ARCHIVE\_TRACE

`LOG_ARCHIVE_TRACE` enables and controls the generation of comprehensive trace information for log archiving and redo transport activity.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `0` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | 0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768 |
| Basic | No |
| Oracle RAC | Multiple instances can have different values. |

The additional tracing that is output when setting `LOG_ARCHIVE_TRACE` to a non-zero value can appear in trace files for an archive process, RFS process, LGWR process, SYNC process, ASYNC process, foreground process, MRP process, recovery process, log apply process, startup process, shutdown process, and other processes that use redo transport services.

Table 2-4 describes the valid `LOG_ARCHIVE_TRACE` values.

Table 2-4 LOG\_ARCHIVE\_TRACE Values

| Value | Description | More Information |
| --- | --- | --- |
| 0 | Disables archivelog tracing (this is the default) |  |
| 1 | High-level tracing | High-level tracing provides a small amount of tracing from most redo transport processes. When a value is specified that is not high-level (not 1), the high-level tracing for that value will be output to the trace file even if the high-level tracing has not been specifically requested. For example, if you set `LOG_ARCHIVE_TRACE` to 128, you will get all the trace messages pertaining to the FAL engine, including the high-level tracing from the FAL engine. |
| 2 | Tracks Data Guard interfaces | This tracing level is for the various Data Guard configuration parameters, the various Data Guard related SQL commands, the various Data Guard table accesses, and some Data Guard internal interfaces. |
| 4 | Tracks common redo transport services | This tracing level is for a number of common services provided by redo transport to various internal users (such as the RFS process, the LGWR process, and the ASYNC process). These include locking primitives, use of common VOS (Virtual Operating System) interfaces, task scheduling, process monitoring, control file access, and other miscellaneous common services. |
| 8 | Tracks database protection mode |  |
| 16 | Tracks disk and network I/O requests |  |
| 32 | Tracks redo transport destinations |  |
| 64 | Tracks redo transport archive engine |  |
| 128 | Tracks redo transport FAL (fetch archive log) engine |  |
| 256 | Tracks Physical, Logical, and Availability Machine clients of RFS process |  |
| 512 | Tracks redo transport of LGWR, SYNC, and ASYNC processes |  |
| 1024 | Tracks redo transport RFS process |  |
| 2048 | Tracks redo transport gap resolution |  |
| 4096 | Tracks real-time apply |  |
| 8192 | Tracks recovery process |  |
| 16384 | Tracks redo transport buffer management |  |
| 32768 | Tracks LogMiner dictionary |  |

You can combine tracing levels by adding together the values of the desired tracing levels. For example, a setting of 3 will generate level 1 and level 2 trace output. You can set different values for the primary and standby database.

When this parameter is set to the default value of 0, Oracle will still generate appropriate alert and trace entries in response to error conditions. If you change the value of this parameter dynamically in an `ALTER SYSTEM` statement, the change takes effect immediately.

Many of the trace messages from redo transport processes include a routine name at the beginning of the trace message. The first part of the routine name specifies the module for that routine. Table 2-5 shows the tracing value used for each redo transport module. Note that the tracing value for transport modules can change from release to release.

Table 2-5 Tracing Values Used for Redo Transport Modules

| Module Name | Purpose | Tracing Value |
| --- | --- | --- |
| krsa | Locking primitives | 4 |
| krsb | Buffer management | 16384 |
| krsc | Crash recovery | 64 |
| krsd | Destination | 32 |
| krse | Archive engine | 64 |
| krsf | FAL engine | 128 |
| krsg | Gap resolution | 2048 |
| krsh | Helper | 4 |
| krsi | Input/output | 16 |
| krsj | Protection mode | 8 |
| krsk | Control file access | 4 |
| krsl | Log writer | 512 |
| krsm | MRP process | 8192 |
| krsn | Configuration | 2 |
| krso | Process monitor | 4 |
| krsp | Physical standby and Availability Machine RFS client | 256 |
| krsq | SQL commands | 2 |
| krsr | RFS process | 1024 |
| krst | Tables | 2 |
| krsu | Network I/O | 16 |
| krsv | VOS front end | 4 |
| krsw | ASYNC process | 512 |
| krsx | Internal interfaces | 2 |

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN11352)