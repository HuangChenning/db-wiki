---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-RESTORE_POINT.html
tags:
  - oracle
  - 12c
  - reference
---

| Column | Datatype | Description |
| --- | --- | --- |
| `SCN` | `NUMBER` | Database SCN when the restore point was created |
| `DATABASE_INCARNATION#` | `NUMBER` | Database incarnation number when the restore point was created |
| `GUARANTEE_FLASHBACK_DATABASE` | `VARCHAR2(3)` | Indicates whether flashback log files will be kept to ensure a flashback to this point (`YES`) or not (`NO`) |
| `STORAGE_SIZE` | `NUMBER` | Approximate number of bytes of disk space currently tied up supporting this restore point, and which would no longer be tied up if this restore point is the oldest restore point and it is dropped. This will always be zero for non-guaranteed restore points. |
| `TIME` | `TIMESTAMP(9)` | Wall-clock time when the restore point was created |
| `RESTORE_POINT_TIME` | `TIMESTAMP(9)` | Time that was specified when the restore point was created. If a time was not specified, this value is NULL. |
| `PRESERVED` | `VARCHAR2(3)` | Indicates whether the restore point must be explicitly deleted (`YES`) or not (`NO`) |
| `NAME` | `VARCHAR2(128)` | Name of the restore point |
| `PDB_RESTORE_POINT` | `VARCHAR2(3)` | Indicates whether there is a PDB restore point for this PDB (`YES`) or not (`NO`)  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `CLEAN_PDB_RESTORE_POINT` | `VARCHAR2(3)` | Indicates whether there is a clean PDB restore point for this PDB (`YES`) or not (`NO`)  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `PDB_INCARNATION#` | `NUMBER` | Pluggable database (PDB) incarnation number. This value is meaningful only for PDB restore points.  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |