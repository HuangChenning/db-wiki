---
title: "V$SESSION_WAIT_HISTORY"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3026.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SESSION_WAIT_HISTORY` displays the last 10 wait events for each active session.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | Session identifier |
| `SEQ#` | `NUMBER` | Sequence of wait events; `1` is the most recent |
| `EVENT#` | `NUMBER` | Event number |
| `EVENT` | `VARCHAR2(64)` | Resource or event for which the session is waiting |
| `P1TEXT` | `VARCHAR2(64)` | Description of the first wait event parameter |
| `P1` | `NUMBER` | First wait event parameter (in decimal) |
| `P2TEXT` | `VARCHAR2(64)` | Description of the second wait event parameter |
| `P2` | `NUMBER` | Second wait event parameter (in decimal) |
| `P3TEXT` | `VARCHAR2(64)` | Description of the third wait event parameter |
| `P3` | `NUMBER` | Third wait event parameter (in decimal) |
| `WAIT_TIME` | `NUMBER` | Amount of time waited (in hundredths of a second) |
| `WAIT_TIME_MICRO` | `NUMBER` | Amount of time waited (in microseconds) |
| `TIME_SINCE_LAST_WAIT_MICRO` | `NUMBER` | Time elapsed (in microseconds) since the end of the previous wait in the wait history |