---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/LOG_CHECKPOINT_TIMEOUT.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.194 LOG\_CHECKPOINT\_TIMEOUT

`LOG_CHECKPOINT_TIMEOUT` specifies (in seconds) the amount of time that has passed since the incremental checkpoint at the position where the last write to the redo log (sometimes called the tail of the log) occurred. This parameter also signifies that no buffer will remain dirty (in the cache) for more than integer seconds.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `1800` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | `0` to 2 <sup>31</sup> - 1 |
| Basic | No |
| Oracle RAC | Multiple instances can have different values. |

Specifying a value of `0` for the timeout disables time-based checkpoints. Hence, setting the value to `0` is not recommended unless `FAST_START_MTTR_TARGET` is set.

Note:

- A checkpoint scheduled to occur because of this parameter is delayed until the completion of the previous checkpoint if the previous checkpoint has not yet completed.
- Recovery I/O can also be limited by setting the `LOG_CHECKPOINT_INTERVAL` parameter or by the size specified for the smallest redo log. For information on which mechanism is controlling checkpointing behavior, query the `V$INSTANCE_RECOVERY` view.

See Also:

- " LOG\_CHECKPOINT\_TIMEOUT "
- " [V$INSTANCE\_RECOVERY](V-INSTANCE_RECOVERY.md) "
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGDBA13014) for information on disabling or removing this parameter when the `FAST_START_MTTR_TARGET` parameter is set