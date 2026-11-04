---
title: "V$SESSION_WAIT_CLASS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3025.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SESSION_WAIT_CLASS` displays the time spent in various wait event operations on a per-session basis.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | Session identifier |
| `SERIAL#` | `NUMBER` | Serial number |
| `WAIT_CLASS_ID` | `NUMBER` | Identifier of the wait class |
| `WAIT_CLASS#` | `NUMBER` | Number of the wait class |
| `WAIT_CLASS` | `VARCHAR2(64)` | Name of the wait class |
| `TOTAL_WAITS` | `NUMBER` | Number of times waits of the class occurred for the session |
| `TIME_WAITED` | `NUMBER` | Amount of time spent in the wait class by the session |