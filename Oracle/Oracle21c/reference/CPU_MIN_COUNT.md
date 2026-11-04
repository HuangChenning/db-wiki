---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/CPU_MIN_COUNT.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.59 CPU\_MIN\_COUNT

`CPU_MIN_COUNT` specifies the minimum number of CPUs required by a pluggable database (PDB) at any given time.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `CPU_MIN_COUNT = 'value'` |
| Default value | The value of `CPU_COUNT` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of Values | Decimal values from `0.1` through `0.95`, where the decimal value is a multiple of `0.05`  Integer values from `1` up to and including the value of `CPU_COUNT` |
| Basic | No |
| Oracle RAC | The same value should be used on all instances. |

This parameter specifies the minimum number of CPUs required by a PDB at any given time. For multi-threaded CPUs, this number corresponds to CPU threads, not CPU cores.

You can set this parameter at the CDB level, and for each individual PDB. This enables you to control each PDBs minimum share of CPU utilization within a CDB. If the sum of the `CPU_MIN_COUNT` values across all open PDBs in a CDB is equal to the value of `CPU_MIN_COUNT` for the CDB, then the CDB instance is considered full. If the sum exceeds the value of `CPU_MIN_COUNT` for the CDB, then the CDB instance is over-provisioned. Oracle does not prevent you from over-provisioning a CDB.

Resource Manager is enabled at the CDB level by setting the `RESOURCE_MANAGER_PLAN` at the root level to the name of a CDB resource plan. If the CDB resource plan has no configured CPU directives, that is, the `SHARES` and `UTILIZATION_LIMIT` directives are unset, then Resource Manager uses the `CPU_COUNT` and `CPU_MIN_COUNT` settings for the PDB to manage CPU utilization.

Note:

Setting this parameter to a very low value can result in insufficient CPU allocation and poor performance.

See Also:

" [CPU\_COUNT](CPU_COUNT.md) "