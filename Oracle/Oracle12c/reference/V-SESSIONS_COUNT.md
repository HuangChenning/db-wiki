---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-SESSIONS_COUNT.html
tags:
  - oracle
  - 12c
  - reference
---

`V$SESSIONS_COUNT` displays the current number of sessions for each PDB.

| Column | Datatype | Description |
| --- | --- | --- |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `USER_SESSION_COUNT` | `NUMBER` | Displays the current number of user sessions for the PDB  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `RECURSIVE_SESSION_COUNT` | `NUMBER` | Displays the current number of recursive sessions for the PDB  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |