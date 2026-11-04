---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-BACKUP.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.82 V$BACKUP

`V$BACKUP` displays the backup status of all online data files.

| Column | Datatype | Description |
| --- | --- | --- |
| `FILE#` | `NUMBER` | File identifier |
| `STATUS` | `VARCHAR2(18)` | File status: `NOT ACTIVE`, `ACTIVE` (backup in progress), `OFFLINE NORMAL`, or description of an error.  `NOT ACTIVE` indicates that the file is not currently in backup mode (that is, an `ALTER TABLESPACE ... BEGIN BACKUP` or `ALTER DATABASE BEGIN BACKUP` statement has not been issued), whereas `ACTIVE` indicates that the file is currently in backup mode. |
| `CHANGE#` | `NUMBER` | System change number when backup started |
| `TIME` | `DATE` | Time the backup started |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |