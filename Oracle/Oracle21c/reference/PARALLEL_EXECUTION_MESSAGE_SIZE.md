---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/PARALLEL_EXECUTION_MESSAGE_SIZE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.267 PARALLEL\_EXECUTION\_MESSAGE\_SIZE

`PARALLEL_EXECUTION_MESSAGE_SIZE` specifies the size of messages used for parallel execution (formerly referred to as parallel query, PDML, Parallel Recovery, replication).

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | Operating system-dependent |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | Minimum: 2148  Maximum: 65536, but some operating systems may have a smaller value |
| Basic | No |
| Oracle RAC | Multiple instances must have the same value. |

On most platforms, the default value is as follows:

- `16384` bytes if `COMPATIBLE` is set to `11.2.0` or higher
- `2148` bytes if `COMPATIBLE` is less than `11.2.0`

The default value is adequate for most applications. Larger values require a larger shared pool. Larger values result in better performance at the cost of higher memory use. For this reason, replication gets no benefit from increasing the size.

See Also:

[Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=VLDBG1501) to learn how this parameter affects memory consumption for parallel operations, including parallel execution