---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_PDB_HISTORY.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.236 DBA\_PDB\_HISTORY

`DBA_PDB_HISTORY` describes the lineage of the PDB to which it belongs.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PDB_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of this PDB in one of its incarnations |
| `PDB_ID` | `NUMBER` | `NOT NULL` | Container ID of this PDB in one of its incarnations. |
| `PDB_DBID` | `NUMBER` | `NOT NULL` | Database ID of this PDB in one of its incarnations |
| `PDB_GUID` | `RAW(16)` | `NOT NULL` | Globally unique ID of this PDB in one of its incarnations |
| `OP_SCNBAS` | `NUMBER` | `NOT NULL` | SCN base when an operation was performed on one of the incarnations of this PDB |
| `OP_SCNWRP` | `NUMBER` | `NOT NULL` | SCN wrap when an operation was performed on one of incarnations of this PDB |
| `OP_TIMESTAMP` | `DATE` | `NOT NULL` | Timestamp of an operation performed on one of the incarnations of this PDB |
| `OPERATION` | `VARCHAR2(16)` | `NOT NULL` | Operation that was performed on one of the incarnations of this PDB |
| `DB_VERSION` | `NUMBER` | `NOT NULL` | Database version |
| `CLONED_FROM_PDB_NAME` | `VARCHAR2(128)` |  | Name of a PDB from which one of the incarnations of this PDB was cloned |
| `CLONED_FROM_PDB_DBID` | `NUMBER` |  | Database ID of a PDB from which one of the incarnations of this PDB was cloned |
| `CLONED_FROM_PDB_GUID` | `RAW(16)` |  | Globally unique ID of a PDB from which one of the incarnations of this PDB was cloned |
| `DB_NAME` | `VARCHAR2(128)` |  | Name of a CDB in which one of the incarnations of this PDB was created |
| `DB_UNIQUE_NAME` | `VARCHAR2(128)` |  | Unique name of a CDB in which one of the incarnations of this PDB was created |
| `DB_DBID` | `NUMBER` |  | Database ID of a CDB in which one of the incarnations of this PDB was created |
| `CLONETAG` | `VARCHAR2(128)` |  | Clone tag name for the PDB if the PDB was cloned using the snapshot copy mechanism |
| `DB_VERSION_STRING` | `VARCHAR2(204)` |  | Database version string |