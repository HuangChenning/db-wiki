---
title: LOG_ARCHIVE_TRACE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams132.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | 0 |
| Modifiable | `ALTER SYSTEM` |
| Range of values | 0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768 |
| Basic | No |
| Oracle RAC | Multiple instances can have different values. |

The `LOG_ARCHIVE_TRACE` parameter enables and controls the generation of comprehensive trace information for log archiving and redo transport activity. The additional tracing that is output when setting `LOG_ARCHIVE_TRACE` to a non-zero value can appear in trace files for an archive process, RFS process, LGWR process, SYNC process, ASYNC process, foreground process, MRP process, recovery process, log apply process, startup process, shutdown process, and other processes that use redo transport services.

The valid values have the following meanings:

- 0: Disable archivelog tracing (this is the default)
- 1: Track archival of redo log file
- 2: Track archival status of each archivelog destination
- 4: Track archival operational phase
- 8: Track archivelog destination activity
- 16: Track detailed archivelog destination activity
- 32: Track archivelog destination parameter modifications
- 64: Track ARCn process state activity
- 128: Track FAL (fetch archived log) server related activities
- 256: Track RFS Logical Client
- 512: Track LGWR redo shipping network activity
- 1024: Track RFS Physical Client
- 2048: Track RFS/ARCn Ping Heartbeat
- 4096: Track Real Time Apply
- 8192: Track Redo Apply (Media Recovery or Physical Standby)
- 16384: Tracks redo transport buffer management
- 32768: Tracks LogMiner dictionary

You can combine tracing levels by adding together the values of the desired tracing levels. For example, a setting of 3 will generate level 1 and level 2 trace output. You can set different values for the primary and standby database.

When this parameter is set to the default value of 0, Oracle will still generate appropriate alert and trace entries in response to error conditions. If you change the value of this parameter dynamically in an `ALTER SYSTEM` statement, the change takes effect immediately.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm)