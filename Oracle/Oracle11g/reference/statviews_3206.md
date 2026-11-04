---
title: DBA_HIST_BG_EVENT_SUMMARY
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3206.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_BG_EVENT_SUMMARY` displays the historical summary background event activity. This view contains snapshots from `V$SESSION_EVENT`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `EVENT_ID` | `NUMBER` | `NOT NULL` | Identifier of the wait event |
| `EVENT_NAME` | `VARCHAR2(64)` | `NOT NULL` | Name of the wait event |
| `WAIT_CLASS_ID` | `NUMBER` |  | Identifier of the class of the wait event |
| `WAIT_CLASS` | `VARCHAR2(64)` |  | Name of the class of the wait event |
| `TOTAL_WAITS` | `NUMBER` |  | Total number of waits for the event |
| `TOTAL_TIMEOUTS` | `NUMBER` |  | Total number of timeouts for the event |
| `TIME_WAITED_MICRO` | `NUMBER` |  | Total amount of time waited for the event (in microseconds) |