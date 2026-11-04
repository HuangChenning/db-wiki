---
title: RESOURCE_MANAGER_CPU_ALLOCATION
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams217.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | The number of logical CPUs reported by the operating system. |
| Modifiable | `ALTER SYSTEM` |
| Range of values | `0` to operating system-specific |
| Basic | No |

Note:

The `RESOURCE_MANAGER_CPU_ALLOCATION` parameter is deprecated. It is retained for backward compatibility only.

`RESOURCE_MANAGER_CPU_ALLOCATION` specifies the number of CPUs that the Resource Manager should utilize. The Resource Manager controls how a system's CPUs are utilized by its database's sessions.

The Resource Manager schedules database sessions on the CPUs according to a Resource Plan that has been configured and enabled by the DBA. Normally, the Resource Manager schedules enough database sessions to keep all CPUs utilized. However, in some scenarios, a DBA may only want to schedule enough database sessions to keep a subset of the CPUs utilized.