---
title: "V$LOGSTDBY_PROGRESS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2046.htm
tags:
  - oracle
  - 11g
  - reference
---

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