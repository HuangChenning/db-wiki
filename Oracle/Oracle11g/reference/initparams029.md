---
title: CLUSTER_DATABASE_INSTANCES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams029.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | If `CLUSTER_DATABASE` is set to `false`, then 1  If `CLUSTER_DATABASE` is set to `true`:  - If ASM, then 4 - Otherwise, the number of configured Oracle RAC instances |
| Modifiable | No |
| Range of values | Any nonzero value |
| Basic | No |
| Oracle RAC | Multiple instances should have the same value. |

`CLUSTER_DATABASE_INSTANCES` is an Oracle RAC parameter that specifies the number of instances that are configured as part of the cluster database. You must set this parameter for every instance. Normally you should set this parameter to the number of instances in your Oracle RAC environment. A proper setting for this parameter can improve memory use.

Oracle uses the value of this parameter to compute the default value of the `LARGE_POOL_SIZE` parameter when the `PARALLEL_AUTOMATIC_TUNING` parameter is set to `true`. Note that the `PARALLEL_AUTOMATIC_TUNING` parameter has been deprecated.

See Also:

- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm) for more information on tuning parallel execution
- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/toc.htm) for information on Real Application Clusters