---
title: DBA_HIST_SERVICE_WAIT_CLASS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4036.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_SERVICE_WAIT_CLASS` displays the history of wait class information for services as tracked by the Workload Repository. This view contains information from `V$SERVICE_WAIT_CLASS`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` |  | Unique snapshot ID |
| `DBID` | `NUMBER` |  | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` |  | Instance number for the snapshot |
| `SERVICE_NAME_HASH` | `NUMBER` |  | Hash of the service name |
| `SERVICE_NAME` | `VARCHAR2(64)` |  | Name of the service |
| `WAIT_CLASS_ID` | `NUMBER` |  | Identifier for the class of the wait event |
| `WAIT_CLASS` | `VARCHAR2(64)` |  | Name for the class of the wait event |
| `TOTAL_WAITS` | `NUMBER` |  | Total number of waits for this event |
| `TIME_WAITED` | `NUMBER` |  | Total amount of time waited for this event (in hundredths of a second) |