---
title: "V$INSTANCE_RECOVERY"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2004.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$INSTANCE_RECOVERY` monitors the mechanisms available to users to limit recovery I/O. Those mechanisms are:

- Set the `LOG_CHECKPOINT_TIMEOUT` initialization parameter
- Set the `LOG_CHECKPOINT_INTERVAL` initialization parameter
- Set the `FAST_START_MTTR_TARGET` initialization parameter
- Set the size of the smallest redo log

| Column | Datatype | Description |
| --- | --- | --- |
| `RECOVERY_ESTIMATED_IOS` | `NUMBER` | Number of dirty buffers in the buffer cache. In the Standard Edition, this column is always null. |
| `ACTUAL_REDO_BLKS` | `NUMBER` | Current actual number of redo blocks required for recovery |
| `TARGET_REDO_BLKS` | `NUMBER` | Current target number of redo blocks that must be processed for recovery. This value is the minimum value of the following 3 columns, and identifies which of the 3 user-defined limits determines checkpointing. |
| `LOG_FILE_SIZE_REDO_BLKS` | `NUMBER` | Maximum number of redo blocks required to guarantee that a log switch does not occur before the checkpoint completes. |
| `LOG_CHKPT_TIMEOUT_REDO_BLKS` | `NUMBER` | Number of redo blocks that need to be processed during recovery to satisfy the `LOG_CHECKPOINT_TIMEOUT` parameter. The value displayed is not meaningful unless that parameter has been set. |
| `LOG_CHKPT_INTERVAL_REDO_BLKS` | `NUMBER` | Number of redo blocks that need to be processed during recovery to satisfy the `LOG_CHECKPOINT_INTERVAL` parameter. The value displayed is not meaningful unless that parameter has been set. |
| `FAST_START_IO_TARGET_REDO_BLKS` | `NUMBER` | This column is obsolete and maintained for backward compatibility. The value of this column is always null. |
| `TARGET_MTTR` | `NUMBER` | Effective MTTR (mean time to recover) target value in seconds. The `TARGET_MTTR` value is calculated based on the value of the `FAST_START_MTTR_TARGET` parameter (the `TARGET_MTTR` value is used internally), and is usually an approximation of the parameter's value. However, if the `FAST_START_MTTR_TARGET` parameter value is very small (for example, one second), or very large (for example, `3600` seconds), the calculation will produce a target value dictated by system limitations. In such cases, the `TARGET_MTTR` value will be the shortest calculated time, or the longest calculated time that recovery is expected to take.  If `FAST_START_MTTR_TARGET` is not specified, the value of this field is the current estimated MTTR. |
| `ESTIMATED_MTTR` | `NUMBER` | Current estimated mean time to recover (MTTR) based on the number of dirty buffers and log blocks (`0` if `FAST_START_MTTR_TARGET` is not specified). Basically, this value tells you how long you could expect recovery to take based on the work your system is doing right now. |
| `CKPT_BLOCK_WRITES` | `NUMBER` | Number of blocks written by checkpoint writes |
| `OPTIMAL_LOGFILE_SIZE` | `NUMBER` | Redo log file size (in megabytes) that is considered optimal based on the current setting of `FAST_START_MTTR_TARGET`. It is recommended that the user configure all online redo logs to be at least this value. Note that redo log files must be at least 4 megabytes in size; otherwise an error is generated. |
| `ESTD_CLUSTER_AVAILABLE_TIME` | `NUMBER` | Estimated time (in seconds) that the cluster would become partially available should this instance fail. This column is only meaningful in an Oracle Real Application Clusters (Oracle RAC) environment. In a non-Oracle RAC environment, the value of this column is null. |
| `WRITES_MTTR` | `NUMBER` | Number of writes driven by the `FAST_START_MTTR_TARGET` initialization parameter |
| `WRITES_LOGFILE_SIZE` | `NUMBER` | Number of writes driven by the smallest redo log file size |
| `WRITES_LOG_CHECKPOINT_SETTINGS` | `NUMBER` | Number of writes driven by the `LOG_CHECKPOINT_INTERVAL or LOG_CHECKPOINT_TIMEOUT` initialization parameter |
| `WRITES_OTHER_SETTINGS` | `NUMBER` | Number of writes driven by other reasons (such as the deprecated `FAST_START_IO_TARGET` initialization parameter) |
| `WRITES_AUTOTUNE` | `NUMBER` | Number of writes due to auto-tune checkpointing |
| `WRITES_FULL_THREAD_CKPT` | `NUMBER` | Number of writes due to full thread checkpoints |

See Also:

- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm) for more information on limiting recovery I/O, and how Oracle determines MTTR recovery times
- [LOG\_CHECKPOINT\_INTERVAL](initparams134.md)
- [FAST\_START\_MTTR\_TARGET](initparams090.md)