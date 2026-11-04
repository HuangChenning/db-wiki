---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/V-SESSIONS_COUNT.html
tags:
  - oracle
  - 19c
  - reference
---

## 9.28 V$SESSIONS\_COUNT

`V$SESSIONS_COUNT` displays the current number of sessions for each PDB.

| Column | Datatype | Description |
| --- | --- | --- |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `USER_SESSION_COUNT` | `NUMBER` | Displays the current number of user sessions for the PDB |
| `RECURSIVE_SESSION_COUNT` | `NUMBER` | Displays the current number of recursive sessions for the PDB |