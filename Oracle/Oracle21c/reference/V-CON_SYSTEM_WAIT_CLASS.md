---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-CON_SYSTEM_WAIT_CLASS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.137 V$CON\_SYSTEM\_WAIT\_CLASS

`V$CON_SYSTEM_WAIT_CLASS` displays the time totals for each registered wait class in a container.

| Column | Datatype | Description |
| --- | --- | --- |
| `WAIT_CLASS_ID` | `NUMBER` | Identifier of the wait class |
| `WAIT_CLASS#` | `NUMBER` | Number of the wait class |
| `WAIT_CLASS` | `VARCHAR2(64)` | Name of the wait class |
| `TOTAL_WAITS` | `NUMBER` | Total number of waits from this wait class |
| `TIME_WAITED` | `NUMBER` | Total amount of time spent in waits from this wait class (in hundredths of a second) |
| `TIME_WAITED_MICRO` | `NUMBER` | Total amount of time spent in waits from this wait class (in microseconds) |
| `CPU` | `NUMBER` | Total amount of CPU time consumed while implementing waits from this wait class (in microseconds) |
| `TOTAL_WAITS_FG` | `NUMBER` | Total number of waits from this wait class, from foreground sessions |
| `TIME_WAITED_FG` | `NUMBER` | Total amount of time spent in waits from this wait class, from foreground sessions (in hundredths of a second) |
| `TIME_WAITED_MICRO_FG` | `NUMBER` | Total amount of time spent in waits from this wait class, from foreground sessions (in microseconds) |
| `CPU_FG` | `NUMBER` | Total amount of CPU time consumed while implementing waits from this wait class, from foreground sessions (in microseconds) |
| `CON_ID` | `NUMBER` | When queried from a non-CDB, time totals for each registered wait class in that instance are returned, and the `CON_ID` value is `0`.  When queried from the root of a CDB, time totals for each registered wait class in every container is returned, and the `CON_ID` value indicates the container to which the time total belong.  When queried from a PDB, time totals for each registered wait class in that PDB are returned, and the `CON_ID` value is the container ID for that PDB. |