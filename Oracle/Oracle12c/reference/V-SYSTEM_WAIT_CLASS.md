---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-SYSTEM_WAIT_CLASS.html
tags:
  - oracle
  - 12c
  - reference
---

`V$SYSTEM_WAIT_CLASS` displays the instance-wide time totals for each registered wait class.

| Column | Datatype | Description |
| --- | --- | --- |
| `WAIT_CLASS_ID` | `NUMBER` | Identifier of the wait class |
| `WAIT_CLASS#` | `NUMBER` | Number of the wait class |
| `WAIT_CLASS` | `VARCHAR2(64)` | Name of the wait class |
| `TOTAL_WAITS` | `NUMBER` | Total number of waits from this wait class |
| `TIME_WAITED` | `NUMBER` | Total amount of time spent in waits from this wait class (in hundredths of a second) |
| `TOTAL_WAITS_FG` | `NUMBER` | Total number of waits for this wait class, from foreground sessions |
| `TIME_WAITED_FG` | `NUMBER` | Total amount of time spent in waits from this wait class, from foreground sessions (in hundredths of a second) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Note:

This view returns instance-wide data and a value of `0` in the `CON_ID` column when queried from the root of a CDB.