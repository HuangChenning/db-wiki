---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-PDB_INCARNATION.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.113 V$PDB\_INCARNATION

Oracle creates a new PDB incarnation whenever a PDB is opened with the `RESETLOGS` option.

| Column | Datatype | Description |
| --- | --- | --- |
| `DB_INCARNATION#` | `NUMBER` | Database incarnation number |
| `PDB_INCARNATION#` | `NUMBER` | PDB incarnation number |
| `STATUS` | `VARCHAR2(7)` | Incarnation status:  - `ORPHAN`: Orphan incarnation - `CURRENT`: Current incarnation of the PDB - `PARENT`: Parent of the current incarnation |
| `INCARNATION_SCN` | `NUMBER` | The SCN to flashback or recover to for this PDB incarnation |
| `INCARNATION_TIME` | `DATE` | The point in time recovered to for this PDB incarnation |
| `BEGIN_RESETLOGS_SCN` | `NUMBER` | The SCN at the beginning of PDB resetlogs |
| `BEGIN_RESETLOGS_TIME` | `DATE` | The time at the beginning of PDB resetlogs |
| `END_RESETLOGS_SCN` | `NUMBER` | The SCN at the end of PDB resetlogs |
| `END_RESETLOGS_TIME` | `DATE` | The time at the end of PDB resetlogs |
| `PRIOR_DB_INCARNATION#` | `NUMBER` | Parent database incarnation number |
| `PRIOR_PDB_INCARNATION#` | `VARCHAR2(40)` | Parent PDB incarnation number |
| `FLASHBACK_DATABASE_ALLOWED` | `VARCHAR2(3)` | Indicates whether the PDB can be flashbacked to this incarnation as part of a flashback database operation for the CDB |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |