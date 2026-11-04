---
title: "V$HS_SESSION"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1181.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$HS_SESSION` describes the current HS session.

| Column | Datatype | Description |
| --- | --- | --- |
| `HS_SESSION_ID` | `NUMBER` | Unique HS session identifier |
| `AGENT_ID` | `NUMBER` | Oracle Net session identifier used for connections to the agent (maps to the `AGENT_ID` column of `V$HS_AGENT`) |
| `SID` | `NUMBER` | User session identifier (maps to the `SID` column of `V$SESSION`) |
| `DB_LINK` | `VARCHAR2(128)` | Server database link name used to access the agent; blank if no database link is used (for example, when using external procedures) |
| `DB_LINK_OWNER` | `NUMBER` | Owner of the database link in `DB_LINK` |
| `STARTTIME` | `DATE` | Time the connection was initiated |