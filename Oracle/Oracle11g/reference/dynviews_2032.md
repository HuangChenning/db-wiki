---
title: "V$LOG_HISTORY"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2032.htm
tags:
  - oracle
  - 11g
  - reference
---

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