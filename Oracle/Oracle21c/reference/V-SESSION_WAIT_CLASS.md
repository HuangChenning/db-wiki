---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SESSION_WAIT_CLASS.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.26 V$SESSION\_WAIT\_CLASS

`V$SESSION_WAIT_CLASS` displays the time spent in various wait event operations on a per-session basis.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | Session identifier |
| `SERIAL#` | `NUMBER` | Serial number |
| `WAIT_CLASS_ID` | `NUMBER` | Identifier of the wait class |
| `WAIT_CLASS#` | `NUMBER` | Number of the wait class |
| `WAIT_CLASS` | `VARCHAR2(64)` | Name of the wait class |
| `TOTAL_WAITS` | `NUMBER` | Total number waits from this wait class by the session |
| `TIME_WAITED` | `NUMBER` | Total amount of time spent in waits from this wait class by the session (in hundredths of a second) |
| `TIME_WAITED_MICRO` | `NUMBER` | Total amount of time spent in waits from this wait class by the session (in microseconds) |
| `CPU` | `NUMBER` | Total amount of CPU time consumed by the session while implementing waits from this wait class (in microseconds) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |