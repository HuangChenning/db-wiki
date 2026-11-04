---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/MAX_PDBS.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.208 MAX\_PDBS

`MAX_PDBS` allows you to limit the number of pluggable databases (PDBs) that can be created in a CDB or an application container.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | Depends on the Oracle Database edition  Possible values: `5`, `254`, or `4098` |
| Modifiable | `ALTER SYSTEM ... SID='*'` |
| Modifiable in a PDB | No. However, this parameter can be modified in the application root of an application container. |
| Range of values | Minimum: `0`  Maximum: The default value for the Oracle Database edition (`5`, `254`, or `4098`) |
| Basic | No |
| Oracle RAC | The same value must be used on all instances. |

This parameter can only be set while connected to the CDB root or an application root.

This parameter applies to PDBs, application containers, and application PDBs. An application PDB is a PDB that resides in an application container.

This parameter does not apply to the PDB seed (`PDB$SEED`), application seeds, or application root clones.

Note:

The maximum number of PDBs that you are allowed to create in a CDB depends on the licensing policy for your Oracle Database edition. To learn more, refer to the Oracle Multitenant information in the "Consolidation" table in [Oracle Database Licensing Information User Manual](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBLIC-GUID-0F9EB85D-4610-4EDF-89C2-4916A0E7AC87).