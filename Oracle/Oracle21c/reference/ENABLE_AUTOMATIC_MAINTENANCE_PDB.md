---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ENABLE_AUTOMATIC_MAINTENANCE_PDB.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.119 ENABLE\_AUTOMATIC\_MAINTENANCE\_PDB

`ENABLE_AUTOMATIC_MAINTENANCE_PDB` can be used to enable or disable the running of automated maintenance tasks for all the PDBs in a CDB or for individual PDBs in a CDB.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `true` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `true \| false` |
| Basic | No |
| Oracle RAC | The same value should be used for all instances. |

Note:

The value of this parameter in CDB$ROOT (the root of a CDB) has no effect in the root. Automated maintenance tasks are always run in the root, regardless of the setting of this parameter.

By default, the value of `ENABLE_AUTOMATIC_MAINTENANCE_PDB` is `true` in CDB$ROOT (the root container in the CDB) and in the individual PDBs in a CDB. This means that by default, automated maintenance tasks are run for the CDB root and all the PDBs in the CDB.

When you change the value of `ENABLE_AUTOMATIC_MAINTENANCE_PDB` in the CDB root, the new value takes effect in the root and in all the PDBs in the CDB.

Therefore, if you change the value of `ENABLE_AUTOMATIC_MAINTENANCE_PDB` in the CDB root to `false`, the value of `ENABLE_AUTOMATIC_MAINTENANCE_PDB` is also changed to `false` in all of the PDBs in the CDB.

You can also change the value of `ENABLE_AUTOMATIC_MAINTENANCE_PDB` in any of the individual PDBs in a CDB, and the value that is set for each individual PDB will be honored. This enables you to enable or disable automated maintenance tasks for individual PDBs.

See Also:

- " [AUTOTASK\_MAX\_ACTIVE\_PDBS](AUTOTASK_MAX_ACTIVE_PDBS.md) " for information about specifying the maximum number of PDBs that can schedule automated maintenance tasks at the same time
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN-GUID-7F7C805E-BA64-43A5-9A09-FC259FFA9AA8) for more information about managing automated database maintenance tasks