---
title: "V$PROXY_ARCHIVELOG_SUMMARY"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2107.htm
tags:
  - oracle
  - 11g
  - reference
---

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