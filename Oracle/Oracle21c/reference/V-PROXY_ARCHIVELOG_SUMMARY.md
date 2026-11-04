---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-PROXY_ARCHIVELOG_SUMMARY.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.137 V$PROXY\_ARCHIVELOG\_SUMMARY

`V$PROXY_ARCHIVELOG_SUMMARY` provides summary information about the output proxy archive log file.

| Column | Datatype | Description |
| --- | --- | --- |
| `NUM_FILES_BACKED` | `NUMBER` | Number of archived log files backed up |
| `NUM_DISTINCT_FILES_BACKED` | `NUMBER` | Number of distinct archived log files backed up |
| `MIN_FIRST_CHANGE#` | `NUMBER` | Minimum first change SCN |
| `MAX_NEXT_CHANGE#` | `NUMBER` | Maximum first change SCN |
| `MIN_FIRST_TIME` | `DATE` | Minimum first change time. Forms the redo range, along with `MAX_NEXT_TIME`. |
| `MAX_NEXT_TIME` | `DATE` | Maximum next change time |
| `OUTPUT_BYTES` | `NUMBER` | Total output size, in bytes |
| `OUTPUT_BYTES_DISPLAY` | `VARCHAR2(4000)` | Displayable format for output bytes |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |