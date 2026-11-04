---
title: "V$SESSION_BLOCKERS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3017.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SESSION_BLOCKERS` displays the blocker sessions for each blocked session. Each row represents a blocked and blocker session pair. If a session is blocked by multiple sessions there will be multiple rows for that blocked session. The maximum number of blocker sessions displayed for a single blocked session is 30. If a session is not blocked by other sessions, then there will be no row in this view for that session.

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