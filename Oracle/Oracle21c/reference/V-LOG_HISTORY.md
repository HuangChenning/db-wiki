---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-LOG_HISTORY.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.47 V$LOG\_HISTORY

`V$LOG_HISTORY` displays log history information from the control file.

| Column | Datatype | Description |
| --- | --- | --- |
| `RECID` | `NUMBER` | Control file record ID |
| `STAMP` | `NUMBER` | Control file record stamp |
| `THREAD#` | `NUMBER` | Thread number of the archived log |
| `SEQUENCE#` | `NUMBER` | Sequence number of the archived log |
| `FIRST_CHANGE#` | `NUMBER` | Lowest system change number (SCN) in the log |
| `FIRST_TIME` | `DATE` | Time of the first entry (lowest SCN) in the log |
| `NEXT_CHANGE#` | `NUMBER` | Highest SCN in the log |
| `RESETLOGS_CHANGE#` | `NUMBER` | Resetlogs change number of the database when the log was written |
| `RESETLOGS_TIME` | `DATE` | Resetlogs time of the database when the log was written |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |