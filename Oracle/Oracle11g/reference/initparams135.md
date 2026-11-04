---
title: LOG_CHECKPOINT_TIMEOUT
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams135.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `1800` |
| Modifiable | `ALTER SYSTEM` |
| Range of values | `0` to 2 <sup>31</sup> - 1 |
| Basic | No |
| Oracle RAC | Multiple instances can have different values. |

`LOG_CHECKPOINT_TIMEOUT` specifies (in seconds) the amount of time that has passed since the incremental checkpoint at the position where the last write to the redo log (sometimes called the tail of the log) occurred. This parameter also signifies that no buffer will remain dirty (in the cache) for more than integer seconds.

Specifying a value of `0` for the timeout disables time-based checkpoints. Hence, setting the value to `0` is not recommended unless `FAST_START_MTTR_TARGET` is set.

Notes:

- A checkpoint scheduled to occur because of this parameter is delayed until the completion of the previous checkpoint if the previous checkpoint has not yet completed.
- Recovery I/O can also be limited by setting the `LOG_CHECKPOINT_INTERVAL` parameter or by the size specified for the smallest redo log. For information on which mechanism is controlling checkpointing behavior, query the `V$INSTANCE_RECOVERY` view.

See Also:

- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm) for more information on setting this parameter
- ["LOG\_CHECKPOINT\_INTERVAL"](initparams134.md) and ["V$INSTANCE\_RECOVERY"](dynviews_2004.md)