---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/MAX_PDBS.html
tags:
  - oracle
  - 12c
  - reference
---

`MAX_PDBS` allows you to limit the number of pluggable databases (PDBs) that can be created in a CDB or an application container.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `4098` |
| Modifiable | `ALTER SYSTEM ... SID='*'` |
| Modifiable in a PDB | No. However, this parameter can be modified in the application root of an application container. |
| Range of values | `0` to `4098` |
| Basic | No |
| Oracle RAC | The same value must be used on all instances. |

This parameter can only be set while connected to the CDB root or an application root.

This parameter applies to PDBs, application containers, and application PDBs. An application PDB is a PDB that resides in an application container.

This parameter does not apply to the PDB seed (`PDB$SEED`), application seeds, or application root clones.

Note:

The maximum number of PDBs that you are allowed to create in a CDB depends on the licensing policy for your Oracle Database edition. For Oracle Database 12c Release 2 (12.2.0.1), the default value (`4098`) and range of values (`0` - `4098`) for this parameter may be greater than the number of PDBs you are licensed to have in your database.

To learn more about the licensing policy for your Oracle Database edition, refer to the Oracle Multitenant information in the "Consolidation" table in [Oracle Database Licensing Information User Manual](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=DBLIC-GUID-0F9EB85D-4610-4EDF-89C2-4916A0E7AC87).

Note:

This initialization parameter is available starting with Oracle Database 12c Release 2 (12.2.0.1).