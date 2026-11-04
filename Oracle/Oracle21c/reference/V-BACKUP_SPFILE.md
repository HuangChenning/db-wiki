---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-BACKUP_SPFILE.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.103 V$BACKUP\_SPFILE

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
| `GUID` | `RAW(16)` | The GUID of the PDB to which the backup belongs. This is useful after the PDB is dropped to identify which PDB the backup belongs to. |