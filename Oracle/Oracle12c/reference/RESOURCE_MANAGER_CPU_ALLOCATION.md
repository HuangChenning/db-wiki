---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/RESOURCE_MANAGER_CPU_ALLOCATION.html
tags:
  - oracle
  - 12c
  - reference
---

The Resource Manager controls how a system's CPUs are utilized by its database's sessions.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | The number of logical CPUs reported by the operating system. |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | `0` to operating system-specific |
| Basic | No |

Note:

The `RESOURCE_MANAGER_CPU_ALLOCATION` parameter is deprecated. It is retained for backward compatibility only. Use the `CPU_COUNT` parameter instead.

The Resource Manager schedules database sessions on the CPUs according to a resource plan that has been configured and enabled by the DBA. Normally, the Resource Manager schedules enough database sessions to keep all CPUs utilized. However, in some scenarios, a DBA may only want to schedule enough database sessions to keep a subset of the CPUs utilized.

See Also:

" [CPU\_COUNT](CPU_COUNT.md) "