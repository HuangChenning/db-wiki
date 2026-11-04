---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-RESTORE_POINT.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.169 V$RESTORE\_POINT

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
| `PDB_RESTORE_POINT` | `VARCHAR2(3)` | Indicates whether there is a PDB restore point for this PDB (`YES`) or not (`NO`) |
| `CLEAN_PDB_RESTORE_POINT` | `VARCHAR2(3)` | Indicates whether there is a clean PDB restore point for this PDB (`YES`) or not (`NO`) |
| `PDB_INCARNATION#` | `NUMBER` | Pluggable database (PDB) incarnation number. This value is meaningful only for PDB restore points. |
| `REPLICATED` | `VARCHAR2(3)` | This column is useful in Oracle Data Guard environments. It indicates the method by which a restore point was created. Possible values:  - `YES` - The restore point was automatically replicated from the primary database to this database when this database was a standby database. The string `_PRIMARY` is appended to the name of such a restore point. - `NO` - The restore point was created by a user and was not replicated from the primary database. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |