---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SESSION_BLOCKERS.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.18 V$SESSION\_BLOCKERS

Each row represents a blocked and blocker session pair. If a session is blocked by multiple sessions there will be multiple rows for that blocked session. The maximum number of blocker sessions displayed for a single blocked session is 30. If a session is not blocked by other sessions, then there will be no row in this view for that session.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | Blocked session's Oracle session identifier |
| `SESS_SERIAL#` | `NUMBER` | Blocked session's Oracle session serial number |
| `WAIT_ID` | `NUMBER` | A number identifying the wait for the blocked session |
| `WAIT_EVENT` | `NUMBER` | Resource or event number for which the blocked session is waiting |
| `WAIT_EVENT_TEXT` | `VARCHAR2(64)` | Resource or event for which the blocked session is waiting |
| `BLOCKER_INSTANCE_ID` | `NUMBER` | Blocker session's instance identifier |
| `BLOCKER_SID` | `NUMBER` | Blocker session's Oracle session identifier |
| `BLOCKER_SESS_SERIAL#` | `NUMBER` | Blocker session's Oracle session serial number |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |