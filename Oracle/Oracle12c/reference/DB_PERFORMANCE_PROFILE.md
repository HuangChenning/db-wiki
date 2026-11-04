---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DB_PERFORMANCE_PROFILE.html
tags:
  - oracle
  - 12c
  - reference
---

`DB_PERFORMANCE_PROFILE` specifies the performance profile for a database or a pluggable database (PDB).

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `DB_PERFORMANCE_PROFILE = string` |
| Default value | There is no default value. |
| Modifiable | No |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | The same value should be set on all instances. |

A performance profile supports easier management for hundreds of databases or PDBs.

On Oracle Exadata, the performance profile for the regular database or CDB is pushed down to the Exadata storage cells. The performance profile is used for the management of Exadata I/O Resource Manager.

A CDB resource plan can specify different resource controls for a performance profile using the `DBMS_RESOURCE_MANAGER.CREATE_CDB_PROFILE_DIRECTIVE` procedure. A PDB with a matching performance profile will use the specified controls.

The value of `DB_PERFORMANCE_PROFILE` can be up to 30 characters and is not case sensitive.

Note:

This initialization parameter is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ARPLS-GUID-38850F94-C0F5-4702-9E0D-A0F6336935CC) for information about the `DBMS_RESOURCE_MANAGER.CREATE_CDB_PROFILE_DIRECTIVE` procedure.