---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/INMEMORY_MAX_POPULATE_SERVERS.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.155 INMEMORY\_MAX\_POPULATE\_SERVERS

`INMEMORY_MAX_POPULATE_SERVERS` specifies the maximum number of background populate servers to use for In-Memory Column Store (IM column store) population, so that these servers do not overload the rest of the system.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | Half of the value of `CPU_COUNT` or the `PGA_AGGREGATE_TARGET` value divided by 512M, whichever is less.  See the " [CPU\_COUNT](CPU_COUNT.md) " description for information about how `CPU_COUNT` is calculated. |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | 0 to a value based on the number of cores in the system. |
| Basic | No |
| Oracle RAC | All instances should use the same value. |

This parameter has meaning only if the `INMEMORY_SIZE` parameter is also set to a positive value.

The value to use for this parameter depends on the number of cores in the system. A certain percentage of CPU should be allocated for in-memory background population, and this parameter should be set accordingly. You can also set this parameter to `0` to temporarily disable populate tasks on the system from executing.

Note:

Be careful not to set the value of this parameter too high. If it is set close to the number of cores or higher, no CPU could be left for the rest of the system to run.

Note:

The IM column store is not populated if this parameter is set to 0.