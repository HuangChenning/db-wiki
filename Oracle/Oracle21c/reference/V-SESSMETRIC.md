---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SESSMETRIC.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.29 V$SESSMETRIC

`V$SESSMETRIC` displays the metric values for all sessions.

| Column | Datatype | Description |
| --- | --- | --- |
| `BEGIN_TIME` | `DATE` | Begin time of the interval |
| `END_TIME` | `DATE` | End time of the interval |
| `INTSIZE_CSEC` | `NUMBER` | Interval size (in hundredths of a second) |
| `SESSION_ID` | `NUMBER` | Session ID |
| `SESSION_SERIAL_NUM` | `NUMBER` | Session serial number |
| `CPU` | `NUMBER` | CPU usage |
| `PHYSICAL_READS` | `NUMBER` | Number of physical reads |
| `LOGICAL_READS` | `NUMBER` | Number of logical reads |
| `PGA_MEMORY` | `NUMBER` | PGA size at the end of the interval |
| `HARD_PARSES` | `NUMBER` | Number of hard parses |
| `SOFT_PARSES` | `NUMBER` | Number of soft parses |
| `PHYSICAL_READ_PCT` | `NUMBER` | Physical read ratio |
| `LOGICAL_READ_PCT` | `NUMBER` | Logical read ratio |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |