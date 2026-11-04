---
title: DBA_HIST_EVENT_HISTOGRAM
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3222.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_EVENT_HISTOGRAM` displays event histogram historical statistics information. This view contains snapshots of `V$EVENT_HISTOGRAM`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `EVENT_ID` | `NUMBER` | `NOT NULL` | Identifier of the wait event |
| `EVENT_NAME` | `VARCHAR2(64)` | `NOT NULL` | Name of the wait event |
| `WAIT_CLASS_ID` | `NUMBER` |  | Identifier of the class of the wait event |
| `WAIT_CLASS` | `VARCHAR2(64)` |  | Name of the class of the wait event |
| `WAIT_TIME_MILLI` | `NUMBER` | `NOT NULL` | Wait time (in milliseconds) |
| `WAIT_COUNT` | `NUMBER` |  | Wait count |