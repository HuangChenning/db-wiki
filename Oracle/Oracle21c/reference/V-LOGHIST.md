---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-LOGHIST.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.49 V$LOGHIST

`V$LOGHIST` contains log history information from the control file. This view is retained for historical compatibility. Oracle recommends that you use `V$LOG_HISTORY` instead.

See Also:

" [V$LOG\_HISTORY](V-LOG_HISTORY.md) "

| Column | Datatype | Description |
| --- | --- | --- |
| `THREAD#` | `NUMBER` | Log thread number |
| `SEQUENCE#` | `NUMBER` | Log sequence number |
| `FIRST_CHANGE#` | `NUMBER` | Lowest SCN in the log |
| `FIRST_TIME` | `DATE` | Time of first SCN in the log |
| `SWITCH_CHANGE#` | `NUMBER` | SCN at which the log switch occurred; one more than highest SCN in the log |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |