---
title: "V$MVREFRESH"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2070.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$MVREFRESH` displays information about the materialized views currently being refreshed.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | Session identifier |
| `SERIAL#` | `NUMBER` | Session serial number, which is used to uniquely identify a session's objects. Guarantees that session-level commands are applied to the correct session objects if the session ends with, and another session begins with, the same session ID. |
| `CURRMVOWNER` | `VARCHAR2(31)` | Owner of the materialized view currently being refreshed. The materialized view resides in this user's schema. |
| `CURRMVNAME` | `VARCHAR2(31)` | Name of the materialized view currently being refreshed |