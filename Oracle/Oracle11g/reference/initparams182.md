---
title: PARALLEL_EXECUTION_MESSAGE_SIZE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams182.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | Operating system-dependent |
| Modifiable | No |
| Range of values | Minimum: 2148  Maximum: 65536, but some operating systems may have a smaller value |
| Oracle RAC | Multiple instances must have the same value. |

`PARALLEL_EXECUTION_MESSAGE_SIZE` specifies the size of messages used for parallel execution (formerly referred to as parallel query, PDML, Parallel Recovery, replication).

On most platforms, the default value is as follows:

- `16384` bytes if `COMPATIBLE` is set to `11.2.0` or higher
- `4096` bytes if `COMPATIBLE` is less than `11.2.0` and `PARALLEL_AUTOMATIC_TUNING` is set to `true`
- `2148` bytes if `COMPATIBLE` is less than `11.2.0` and `PARALLEL_AUTOMATIC_TUNING` is set to `false`

The default value is adequate for most applications. Larger values require a larger shared pool. Larger values result in better performance at the cost of higher memory use. For this reason, replication gets no benefit from increasing the size.

Note:

When `PARALLEL_AUTOMATIC_TUNING` is set to `TRUE`, message buffers are allocated out of the large pool. In this case, the default is generally higher. Note that the `PARALLEL_AUTOMATIC_TUNING` parameter has been deprecated.