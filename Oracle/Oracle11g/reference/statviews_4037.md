---
title: DBA_HIST_SESS_TIME_STATS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4037.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_SESS_TIME_STATS` displays information about CPU and I/O time for interesting Streams sessions.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `SESSION_TYPE` | `VARCHAR2(64)` | `NOT NULL` | Type of session |
| `MIN_LOGON_TIME` | `DATE` |  | Minimum logon time |
| `SUM_CPU_TIME` | `NUMBER` |  | Total CPU time |
| `SUM_SYS_IO_WAIT` | `NUMBER` |  | Total system I/O wait time |
| `SUM_USER_IO_WAIT` | `NUMBER` |  | Total user I/O wait time |