---
title: DBA_HIST_THREAD
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4067.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_THREAD` displays historical thread information from the control file.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `THREAD#` | `NUMBER` | `NOT NULL` | Thread number |
| `THREAD_INSTANCE_NUMBER` | `NUMBER` |  | Instance number of the thread |
| `STATUS` | `VARCHAR2(6)` |  | Thread status (`OPEN`) or (`CLOSED`) |
| `OPEN_TIME` | `DATE` |  | Last time the thread was opened |
| `CURRENT_GROUP#` | `NUMBER` |  | Current log group |
| `SEQUENCE#` | `NUMBER` |  | Sequence number of the current log |