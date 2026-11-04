---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-HS_SESSION.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.285 V$HS\_SESSION

| Column | Datatype | Description |
| --- | --- | --- |
| `HS_SESSION_ID` | `NUMBER` | Unique HS session identifier |
| `AGENT_ID` | `NUMBER` | Oracle Net session identifier used for connections to the agent (maps to the `AGENT_ID` column of `V$HS_AGENT`) |
| `SID` | `NUMBER` | User session identifier (maps to the `SID` column of `V$SESSION`) |
| `DB_LINK` | `VARCHAR2(128)` | Server database link name used to access the agent; blank if no database link is used (for example, when using external procedures) |
| `DB_LINK_OWNER` | `NUMBER` | Owner of the database link in `DB_LINK` |
| `STARTTIME` | `DATE` | Time the connection was initiated |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |