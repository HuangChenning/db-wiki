---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DB_PERFORMANCE_PROFILE.html
tags:
  - oracle
  - 19c
  - reference
---

## 1.92 DB\_PERFORMANCE\_PROFILE

`DB_PERFORMANCE_PROFILE` is used by Resource Manager and Exadata I/O Resource Management (IORM) to provide easier resource management for CDBs and PDBs.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `DB_PERFORMANCE_PROFILE =` `string` |
| Default value | There is no default value. |
| Modifiable | No |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | The same value should be set on all instances. |

On non-Exadata systems, this parameter can be set at the PDB level for use by Resource Manager. On Exadata systems, this parameter can be set at the PDB level for use by Resource Manager, and at the CDB level for use by IORM.

- On non-Exadata systems:
	- You can set this parameter at the PDB level to specify a performance profile for Resource Manager. In this case, a CDB resource plan specifies different resource controls for a performance profile using the `DBMS_RESOURCE_MANAGER.CREATE_CDB_PROFILE_DIRECTIVE` procedure, and a PDB with a matching performance profile will use the specified controls.
		- There is no practical use for setting this parameter at the CDB level on a non-Exadata system.
- On Exadata systems:
	- Similar to non-Exadata systems, you can set this parameter at the PDB level to specify a performance profile for Resource Manager.
		- You can also set this parameter at the CDB level to specify an IORM profile. This profile is pushed down to the Exadata storage cells, where it is used by IORM to manage I/O allocation.
		- Note that setting this parameter at the CDB level identifies the entire database to IORM and has no effect on how Exadata Smart Flash Cache is divided among PDBs. To control flash cache allocation between PDBs, you must use Resource Manager, that is, you must either create a CDB resource plan and enable that plan, or, if using profile directives, specify a performance profile for each PDB. This instructs Resource Manager to enforce per-PDB flash cache minimums and limits, while IORM continues to manage I/O resources at the CDB level.

The value of this parameter can be up to 30 characters and is not case sensitive.

- [Oracle Multitenant Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=MULTI-GUID-2708E76D-E18B-4586-920A-BD4B904AE14D) to learn more about how Resource Manager uses this parameter
- [Oracle Exadata System Software User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=SAGUG-GUID-8A893F2B-9C98-46AA-91F7-896A05179E02) to learn more about how IORM uses this parameter