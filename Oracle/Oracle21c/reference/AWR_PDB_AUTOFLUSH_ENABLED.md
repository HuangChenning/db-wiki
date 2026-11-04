---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/AWR_PDB_AUTOFLUSH_ENABLED.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.28 AWR\_PDB\_AUTOFLUSH\_ENABLED

`AWR_PDB_AUTOFLUSH_ENABLED` enables you to specify whether to enable or disable automatic Automatic Workload Repository (AWR) snapshots for all the PDBs in a CDB or for individual PDBs in a CDB.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `true \| false` |
| Basic | No |
| Oracle RAC | The same value must be used on all instances. |

Note:

The value of this parameter in CDB$ROOT (the root of a CDB) has no effect in the root. Automatic AWR snapshots are always enabled in the root, regardless of the setting of this parameter.

The default value of `AWR_PDB_AUTOFLUSH_ENABLED` is `false`. Thus, by default, automatic AWR snapshots are disabled for all the PDBs in a CDB.

When you change the value of `AWR_PDB_AUTOFLUSH_ENABLED` in the CDB root, the new value takes effect in all the PDBs in the CDB.

Therefore, if you change the value of `AWR_PDB_AUTOFLUSH_ENABLED` in the CDB root to `true`, the value of `AWR_PDB_AUTOFLUSH_ENABLED` is also changed to `true` in all of the PDBs, so that automatic AWR snapshots are enabled for all the PDBs.

You can also change the value of `AWR_PDB_AUTOFLUSH_ENABLED` in any of the individual PDBs in a CDB, and the value that is set for each individual PDB will be honored. This enables you to enable or disable automatic AWR snapshots for individual PDBs.

When a new PDB is created, or a PDB from a previous database release is upgraded to the current database release, automatic AWR snapshots are enabled or disabled for the PDB based on the current value of `AWR_PDB_AUTOFLUSH_ENABLED` in the root.

See Also:

- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGDBA-GUID-CE73D449-0EE9-4022-B1F1-AA12F0955C03) for more information about Automatic Workload Repository (AWR)
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGDBA-GUID-A64AE148-DFB9-4B5F-BAA8-6A4A575E79DF) for more information about AWR snapshots