---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-BACKUP_SPFILE.html
tags:
  - oracle
  - 12c
  - reference
---

`V$BACKUP_SPFILE` displays information about server parameter files in backup sets from the control file.

| Column | Datatype | Description |
| --- | --- | --- |
| `RECID` | `NUMBER` | Backup SPFILE record ID |
| `STAMP` | `NUMBER` | Backup SPFILE record stamp |
| `SET_STAMP` | `NUMBER` | Backup set stamp (of the set which contains this SPFILE backup) |
| `SET_COUNT` | `NUMBER` | Backup set count (of the set which contains this SPFILE backup) |
| `MODIFICATION_TIME` | `DATE` | Time when the SPFILE was last modified (this also includes creation time) |
| `BYTES` | `NUMBER` | Size of the SPFILE (in bytes) |
| `COMPLETION_TIME` | `DATE` | Time when the backup of the SPFILE completed |
| `DB_UNIQUE_NAME` | `VARCHAR2(30)` | Unique database name |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `GUID` | `RAW(16)` | The GUID of the PDB to which the backup belongs. This is useful after the PDB is dropped to identify which PDB the backup belongs to.  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |