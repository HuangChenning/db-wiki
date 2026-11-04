---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SESSION_WAIT_HISTORY.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.27 V$SESSION\_WAIT\_HISTORY

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
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |