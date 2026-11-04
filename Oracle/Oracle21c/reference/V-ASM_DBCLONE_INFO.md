---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ASM_DBCLONE_INFO.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.55 V$ASM\_DBCLONE\_INFO

`V$ASM_DBCLONE_INFO` shows the relationship between the parent database and point-in-time database clones.

| Column | Datatype | Description |
| --- | --- | --- |
| `GROUP_NUMBER` | `NUMBER` | Disk group number |
| `DBCLONE_NAME` | `VARCHAR2(128)` | Name of the point-in-time database clone |
| `MIRRORCOPY_NAME` | `VARCHAR2(128)` | Name of the mirror copy associated with the database clone |
| `DBCLONE_STATUS` | `VARCHAR2(128)` | Status of the database clone. Possible values:  - `PREPARING` — The process to prepare the database for splitting has started, but the database is not yet ready to be split. - `PREPARED` — The preparation process is complete and the database is ready to be split. - `SPLITTING` — The process to split the database files has started. - `SPLIT COMPLETED` — The database has been split. - `DROPPING` — The process to drop the prepared database clone has started. - `FAILED` — The clone operation has failed. The incomplete clone will be dropped. |
| `PARENT_DBNAME` | `VARCHAR2(128)` | Name of the parent database |
| `PARENT_FILEGROUP_NAME` | `VARCHAR2(128)` | Name of the file group associated with the parent database |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=OSTMG-GUID-F0CA1610-780A-40FB-B8BB-88E0C7688CC2) for information about point-in-time database clones