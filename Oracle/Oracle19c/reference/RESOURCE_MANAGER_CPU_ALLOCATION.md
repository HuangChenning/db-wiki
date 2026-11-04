---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/RESOURCE_MANAGER_CPU_ALLOCATION.html
tags:
  - oracle
  - 19c
  - reference
---

## 1.313 RESOURCE\_MANAGER\_CPU\_ALLOCATION

The Resource Manager controls how a system's CPUs are utilized by its database's sessions.

Note:

The `RESOURCE_MANAGER_CPU_ALLOCATION` parameter is deprecated and is retained only for backward compatibility. Furthermore, starting with Oracle Database 19c, Release Update 19.10, the value of this parameter is ignored and its default value is set to `0`. Use the `CPU_COUNT` parameter instead.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | The number of logical CPUs reported by the operating system. |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | `0` to operating system-specific |
| Basic | No |

The Resource Manager schedules database sessions on the CPUs according to a resource plan that has been configured and enabled by the DBA. Normally, the Resource Manager schedules enough database sessions to keep all CPUs utilized. However, in some scenarios, a DBA may only want to schedule enough database sessions to keep a subset of the CPUs utilized.

See Also:

" [CPU\_COUNT](CPU_COUNT.md) "