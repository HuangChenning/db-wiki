---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/AUTOTASK_MAX_ACTIVE_PDBS.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.27 AUTOTASK\_MAX\_ACTIVE\_PDBS

`AUTOTASK_MAX_ACTIVE_PDBS` enables you to specify the maximum number of PDBs that can schedule automated maintenance tasks at the same time (during a maintenance window).

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `2` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | `0` to the number of PDBs in the CDB |
| Basic | No |
| Oracle RAC | The same value should be used on all instances. |

This parameter only affects PDBs. The CDB$ROOT container (CDB root) for a CDB can always schedule and run maintenance tasks during a maintenance window.

The default value is 2. Therefore, by default, two PDBs and the CDB root can run tasks at the same time during a maintenance window.

This parameter can be set only in the CDB root, not in a PDB.

See Also:

- " [ENABLE\_AUTOMATIC\_MAINTENANCE\_PDB](ENABLE_AUTOMATIC_MAINTENANCE_PDB.md) " for information on disabling or enabling the running of automated maintenance tasks for specific PDBs or for all the PDBs in CDB
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN-GUID-7F7C805E-BA64-43A5-9A09-FC259FFA9AA8) for more information about managing automated database maintenance tasks