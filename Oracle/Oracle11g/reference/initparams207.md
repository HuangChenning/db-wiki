---
title: RECOVERY_PARALLELISM
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams207.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | System-determined parallel recovery |
| Modifiable | No |
| Range of values | System-determined, but cannot exceed `PARALLEL_MAX_SERVERS` initialization parameter setting |

`RECOVERY_PARALLELISM` specifies the number of processes to participate in instance or crash recovery. To force serial crash and instance recovery, set the `RECOVERY_PARALLELISM` parameter to 0 or 1. 0 or 1 disable parallel instance and crash recovery on a system that has multiple CPUs. An alert log displays the degree of parallelism that was chosen when the database instance/recovery starts.

See Also:

- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm) for information on setting this parameter in exclusive mode
- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/toc.htm) for information on setting this parameter in an Oracle RAC environment