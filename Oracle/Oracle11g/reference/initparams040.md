---
title: CPU_COUNT
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams040.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `0` |
| Modifiable | `ALTER SYSTEM` |
| Range of values | `0` to unlimited |
| Basic | No |

`CPU_COUNT` specifies the number of CPUs available for Oracle Database to use. On core architectures, it specifies the number of available CPU cores. Various components of Oracle Database are configured based on the number of CPUs, such as the Optimizer, Parallel Query, and Resource Manager.

If `CPU_COUNT` is set to `0` (its default setting), then Oracle Database continuously monitors the number of CPUs reported by the operating system and uses the current count. If `CPU_COUNT` is set to a value other than `0`, then Oracle Database will use this count rather than the actual number of CPUs, thus disabling dynamic CPU reconfiguration. When Resource Manager is enabled, setting `CPU_COUNT` limits the CPU utilization to approximately `CPU_COUNT` processors.

Note:

Setting `CPU_COUNT` to a value greater than the current number of CPUs results in an error. However, if `CPU_COUNT` is set to a value greater than the current number of CPUs in the initialization parameter file, then `CPU_COUNT` is capped to the current number of CPUs.

See Also:

- [Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25523/parallel002.htm#VLDBG1391) for information about how `CPU_COUNT` is used to determine the default degree of parallelism for a single instance or Oracle RAC configuration when the `PARALLEL` clause is specified but no degree of parallelism is listed
- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/dbrm.htm#ADMIN13473) for an example of how CPU resources are allocated if you enable instance caging and set a maximum utilization limit in a resource plan