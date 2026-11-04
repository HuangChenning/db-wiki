---
title: DBA_HIST_STREAMS_CAPTURE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4056.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_STREAMS_CAPTURE` displays information about each capture process. This view contains a snapshot of `V$STREAMS_CAPTURE`. This view is intended for use with Automatic Workload Repository (AWR).

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `CAPTURE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the capture process |
| `STARTUP_TIME` | `DATE` | `NOT NULL` | Time that the capture process was last started |
| `LAG` | `NUMBER` |  | Delay (in seconds) between the creation and capture of the most recently captured message |
| `TOTAL_MESSAGES_CAPTURED` | `NUMBER` |  | Total changes captured since the capture process was last started |
| `TOTAL_MESSAGES_ENQUEUED` | `NUMBER` |  | Total number of messages enqueued since the capture process was last started |
| `ELAPSED_RULE_TIME` | `NUMBER` |  | Elapsed time (in hundredths of a second) evaluating rules since the capture process was last started |
| `ELAPSED_ENQUEUE_TIME` | `NUMBER` |  | Elapsed time (in hundredths of a second) enqueuing messages since the capture process was last started |
| `ELAPSED_REDO_WAIT_TIME` | `NUMBER` |  | Elapsed time (in hundredths of a second) spent by the capture process in the `WAITING FOR REDO` state |
| `ELAPSED_PAUSE_TIME` | `NUMBER` |  | Elapsed pause time |