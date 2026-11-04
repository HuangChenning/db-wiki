---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/CPU_COUNT.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.58 CPU\_COUNT

`CPU_COUNT` specifies the number of CPUs available for Oracle Database to use.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `0` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `0` to unlimited |
| Basic | No |
| Oracle RAC | The same value should be used on all instances. |

On CPUs with multiple CPU threads, it specifies the total number of available CPU threads. Various components of Oracle Database are configured based on the number of CPUs, such as the Optimizer, Parallel Query, and Resource Manager.

If `CPU_COUNT` is set to `0` (its default setting), then Oracle Database continuously monitors the number of CPUs reported by the operating system and uses the current count. If `CPU_COUNT` is set to a value other than `0`, then Oracle Database will use this count rather than the actual number of CPUs, thus disabling dynamic CPU reconfiguration.

When Resource Manager is managing CPU (`RESOURCE_MANAGER_PLAN` is set), then the database's CPU utilization is limited to `CPU_COUNT` CPU threads. This feature is called Instance Caging. If Resource Manager is enabled at the CDB level, then the PDB's CPU utilization is limited to the PDB's `CPU_COUNT`.

Note:

Setting `CPU_COUNT` to a value greater than the current number of CPUs results in an error. However, if `CPU_COUNT` is set to a value greater than the current number of CPUs in the initialization parameter file, then `CPU_COUNT` is capped to the current number of CPUs.

Note:

When a value is not explicitly set for `CPU_COUNT`, the maximum default value for `CPU_COUNT` is 2 for an Oracle ASM Proxy instance, 4 for an Oracle ASM instance, and 8 for an Oracle IOServer instance.

See Also:

- " [CPU\_MIN\_COUNT](CPU_MIN_COUNT.md) "
- [Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=VLDBG1382) for information about how `CPU_COUNT` is used to determine the default degree of parallelism for a single instance or Oracle RAC configuration when the `PARALLEL` clause is specified but no degree of parallelism is listed
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN13473) for an example of how CPU resources are allocated if you enable instance caging and set a maximum utilization limit in a resource plan