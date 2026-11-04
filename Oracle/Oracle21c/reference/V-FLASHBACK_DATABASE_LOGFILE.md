---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-FLASHBACK_DATABASE_LOGFILE.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.235 V$FLASHBACK\_DATABASE\_LOGFILE

`V$FLASHBACK_DATABASE_LOGFILE` displays information about the flashback log files.

| Column | Datatype | Description |
| --- | --- | --- |
| `NAME` | `VARCHAR2(513)` | Name of the log file |
| `LOG#` | `NUMBER` | Log file number |
| `THREAD#` | `NUMBER` | Log file thread number |
| `SEQUENCE#` | `NUMBER` | Log file sequence number |
| `BYTES` | `NUMBER` | Log file size (in bytes) |
| `FIRST_CHANGE#` | `NUMBER` | Lowest system change number (SCN) in the log file |
| `FIRST_TIME` | `DATE` | Time of the first SCN in the log file |
| `TYPE` | `VARCHAR2(9)` | Log type:  - `NORMAL` - `RESERVED` - `FREE` - `TO` `DELETE` |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |