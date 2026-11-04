---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/CONTAINER_DATA.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.52 CONTAINER\_DATA

Use `CONTAINER_DATA` to control whether queries on extended data-linked objects from within a PDB return rows from both the root and the PDB, or rows from only the PDB.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `CONTAINER_DATA = { ALL \| CURRENT \| CURRENT_DICTIONARY }` |
| Default value | `ALL` |
| Modifiable | `ALTER SESSION` |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | Different instances can use different values. |

This parameter controls the behavior of queries on the following types of objects:

- Extended data-linked application common objects
	This type of object stores shared data in an application root, and also allows application PDBs to store local data that is unique to each application PDB.
	When this type of object is queried from an application root, only the shared data in the application root is returned.
	When this type of object is queried from an application PDB, the value of the `CONTAINER_DATA` initialization parameter controls the query result as follows:
	- `ALL`: The query returns both the shared data in the application root and the local data pertaining to the application PDB
		- `CURRENT`: The query returns only the local data pertaining to the application PDB
		- `CURRENT_DICTIONARY`: The query returns both the shared data in the application root and the local data pertaining to the application PDB
- Extended data-linked Oracle-supplied data dictionary objects
	This type of object stores data pertaining to the CDB root, as well as data pertaining to individual PDBs.
	When this type of object is queried from the CDB root, only data pertaining to the CDB root is returned.
	When this type of object is queried from a PDB, the value of the `CONTAINER_DATA` initialization parameter controls the query result as follows:
	- `ALL`: The query returns data pertaining to both the CDB root and the PDB
		- `CURRENT`: The query returns only data pertaining to the PDB
		- `CURRENT_DICTIONARY`: The query returns only data pertaining to the PDB