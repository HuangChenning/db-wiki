---
title: "V$FLASHBACK_DATABASE_LOGFILE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1145.htm
tags:
  - oracle
  - 11g
  - reference
---

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
| `TYPE` <sup>Foot 1</sup> | `VARCHAR2(9)` | Log type: |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.2).