---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/RESOURCE_MANAGE_GOLDENGATE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.310 RESOURCE\_MANAGE\_GOLDENGATE

`RESOURCE_MANAGE_GOLDENGATE` determines whether Oracle GoldenGate apply processes in the database are resource managed.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | `true \| false` |
| Basic | No |
| Oracle RAC | All instances should use the same value. |

To enable Resource Manager, set the `RESOURCE_MANAGER_PLAN` parameter.

By default, Oracle GoldenGate apply processes in the database are not resource managed. Given that replication to a PDB requires a separate Oracle GoldenGate apply process, it is possible that the apply processes for one PDB could end up consuming most of the CPU on the machine, even if there is a CPU resource management plan in place to limit CPU usage per PDB.

You can set the following values for the `RESOURCE_MANAGE_GOLDENGATE` parameter:

- `TRUE`: With this setting, Oracle GoldenGate apply processes in the database are resource managed based on the resources allocated to the GoldenGate apply user.
- `FALSE`: With this setting, Oracle GoldenGate apply processes are not resource managed.