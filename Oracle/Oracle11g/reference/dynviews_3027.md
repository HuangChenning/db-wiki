---
title: "V$SESSMETRIC"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3027.htm
tags:
  - oracle
  - 11g
  - reference
---

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