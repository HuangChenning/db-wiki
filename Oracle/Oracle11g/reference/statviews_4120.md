---
title: DBA_LOGSTDBY_EVENTS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4120.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_LOGSTDBY_EVENTS` displays information about the activity of the logical standby database system. It can be used to determine the cause of failures that occur when applying redo data to logical standby databases. This view is for logical standby databases only.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `EVENT_TIME` | `DATE` |  | Time when the event was logged |
| `EVENT_TIMESTAMP` | `TIMESTAMP(6)` |  | Timestamp when the event was logged |
| `CURRENT_SCN` | `NUMBER` |  | SCN associated with the change at the primary database. If a failure occurred, then examine this column to determine which archived log file contains the source of the failure (for example, an unsupported record). |
| `COMMIT_SCN` | `NUMBER` |  | SCN value on which the change was committed at the primary database |
| `XIDUSN` | `NUMBER` |  | Transaction ID undo segment number at the primary database of the associated transaction |
| `XIDSLT` | `NUMBER` |  | Transaction ID slot number at the primary database of the associated transaction |
| `XIDSQN` | `NUMBER` |  | Transaction ID sequence number at the primary database of the associated transaction |
| `EVENT` | `CLOB` |  | Statement that was being processed when the failure occurred |
| `STATUS_CODE` | `NUMBER` |  | Status (or Oracle error code) belonging to the STATUS message |
| `STATUS` | `VARCHAR2(2000)` |  | Description of the current activity of the process or the reason why the apply operation stopped |