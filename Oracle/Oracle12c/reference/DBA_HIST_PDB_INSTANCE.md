---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_HIST_PDB_INSTANCE.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_HIST_PDB_INSTANCE` displays the pluggable databases (PDB)s and instances in the Workload Repository.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number |
| `STARTUP_TIME` | `TIMESTAMP(3)` | `NOT NULL` | Startup time of the instance |
| `CON_DBID` | `NUMBER` | `NOT NULL` | The database ID of the PDB for the sampled session |
| `OPEN_TIME` | `TIMESTAMP(3)` | `NOT NULL` | Time the PDB was last opened |
| `OPEN_MODE` | `VARCHAR2(16)` |  | Open mode of the database |
| `PDB_NAME` | `VARCHAR2(128)` |  | PDB name |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |