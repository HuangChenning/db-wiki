---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SYSTEM_WAIT_CLASS.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.104 V$SYSTEM\_WAIT\_CLASS

`V$SYSTEM_WAIT_CLASS` displays the instance-wide time totals for each registered wait class.

| Column | Datatype | Description |
| --- | --- | --- |
| `WAIT_CLASS_ID` | `NUMBER` | Identifier of the wait class |
| `WAIT_CLASS#` | `NUMBER` | Number of the wait class |
| `WAIT_CLASS` | `VARCHAR2(64)` | Name of the wait class |
| `TOTAL_WAITS` | `NUMBER` | Total number of waits from this wait class |
| `TIME_WAITED` | `NUMBER` | Total amount of time spent in waits from this wait class (in hundredths of a second) |
| `TIME_WAITED_MICRO` | `NUMBER` | Total amount of time spent in waits from this wait class (in microseconds) |
| `CPU` | `NUMBER` | Total amount of CPU time consumed while implementing waits from this wait class (in microseconds) |
| `TOTAL_WAITS_FG` | `NUMBER` | Total number of waits for this wait class, from foreground sessions |
| `TIME_WAITED_FG` | `NUMBER` | Total amount of time spent in waits from this wait class, from foreground sessions (in hundredths of a second) |
| `TIME_WAITED_MICRO_FG` | `NUMBER` | Total amount of time spent in waits from this wait class, from foreground sessions (in microseconds) |
| `CPU_FG` | `NUMBER` | Total amount of CPU time consumed while implementing waits from this wait class, from foreground sessions (in microseconds) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Note:

This view returns instance-wide data and a value of `0` in the `CON_ID` column when queried from the root of a CDB.