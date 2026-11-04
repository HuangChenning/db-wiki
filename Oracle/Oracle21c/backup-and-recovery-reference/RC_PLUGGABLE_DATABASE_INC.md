---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/RC_PLUGGABLE_DATABASE_INC.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

`RC_PLUGGABLE_DATABASE_INC` displays information about all pluggable database (PDB) incarnations.

A new PDB incarnation is created whenever a PDB is opened with the `RESETLOGS` option. This view corresponds to the `V$PDB_INCARNATION` view.

| Column | Data Type | Description |
| --- | --- | --- |
| `PDB_KEY` | `NUMBER` | The primary key for this PDB in the recovery catalog. |
| `NAME` | `VARCHAR2(30)` | Name of the PDB. |
| `CON_ID` | `NUMBER` | Unique identifier of the multitenant container database (CDB) that contains this PDB. |
| `DBID` | `NUMBER` | Unique identifier of the PDB. |
| `GUID` | `RAW(16)` | Globally unique identifier (GUID) of this PDB. |
| `CREATE_SCN` | `NUMBER` | Creation SCN of PDB. |
| `PDBINC_KEY` | `NUMBER` | The primary key for this PDB incarnation in recovery catalog. |
| `DB_KEY` | `NUMBER` | The primary key for this CDB in the recovery catalog. |
| `CURRENT_INCARNATION` | `VARCHAR2(3)` | YES if it is the current incarnation; NO if it is not. |
| `INCARNATION_SCN` | `NUMBER` | The SCN to flashback or recover to for this PDB incarnation. |
| `BEGIN_RESETLOGS_SCN` | `NUMBER` | The SCN at the beginning of the PDB resetlogs. |
| `BEGIN_RESETLOGS_TIME` | `DATE` | The time of the SCN in `BEGIN_RESETLOGS_SCN`. |
| `END_RESETLOGS_SCN` | `NUMBER` | The SCN at the end of the PDB resetlogs. |
| `DBINC_KEY` | `NUMBER` | The primary key for the incarnation of CDB at which this PDB incarnation is created. |
| `DB_RESETLOGS_SCN` | `NUMBER` | The incarnation SCN of CDB at which this PDB incarnation is created. |
| `DB_RESETLOGS_TIME` | `DATE` | The incarnation time of CDB at which this PDB incarnation is created. |
| `PRIOR_PDBINC_KEY` | `NUMBER` | The primary key of the parent PDB incarnation. |
| `PRIOR_INCARNATION_SCN` | `NUMBER` | `INCARNATION_SCN` of parent PDB incarnation. |
| `PRIOR_BEGIN_RESETLOGS_SCN` | `NUMBER` | `BEGIN_RESETLOGS_SCN` of parent PDB incarnation |
| `PRIOR_BEGIN_RESETLOGS_TIME` | `DATE` | `BEGIN_RESETLOGS_TIME` of parent PDB incarnation. |
| `PRIOR_END_RESETLOGS_TIME` | `NUMBER` | `END_RESETLOGS_TIME` of parent PDB incarnation. |
| `PRIOR_DBINC_KEY` | `NUMBER` | `DBINC_KEY` of parent PDB incarnation. |
| `PRIOR_DB_RESETLOGS_SCN` | `NUMBER` | `DB_RESETLOGS_SCN` of parent PDB incarnation |
| `PRIOR_DB_RESETLOGS_TIME` | `DATE` | `DB_RESETLOGS_TIME` of parent PDB incarnation |
| `STATUS` | `VARCHAR2(8)` | Incarnation status:  - `ORPHAN:` Orphan incarnation - `CURRENT:` Current incarnation of the PDB - `PARENT:` Parent of current incarnation |