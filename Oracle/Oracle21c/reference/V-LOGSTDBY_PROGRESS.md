---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-LOGSTDBY_PROGRESS.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.61 V$LOGSTDBY\_PROGRESS

`V$LOGSTDBY_PROGRESS` displays the progress of log apply services on the logical standby database. This view is for logical standby databases only.

| Column | Datatype | Description |
| --- | --- | --- |
| `APPLIED_SCN` | `NUMBER` | All the transactions with COMMIT SCN lower than or equal to this SCN have been applied |
| `APPLIED_TIME` | `DATE` | The time and date of `APPLIED_SCN` |
| `RESTART_SCN` | `NUMBER` | During an apply restart, LogMiner does not read any log file with a `NEXT_CHANGE#` lower than this SCN. |
| `RESTART_TIME` | `DATE` | The time and date of `RESTART_SCN` |
| `LATEST_SCN` | `NUMBER` | The highest SCN of all redo records that Logical Standby has encountered |
| `LATEST_TIME` | `DATE` | The time and date of `LATEST_SCN` |
| `MINING_SCN` | `NUMBER` | The SCN of the latest redo record processed by the builder process |
| `MINING_TIME` | `DATE` | The time and date of `MINING_SCN` |
| `RESETLOGS_ID` | `NUMBER` | A redo branch is identified by resetlogs SCN and resetlogs timestamp. The `RESETLOGS_ID` column contents are the same as resetlogs timestamp converted to a number. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |