---
title: ALL_SCHEDULER_WINDOW_DETAILS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2055.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_SCHEDULER_WINDOW_DETAILS` displays log details for the Scheduler windows accessible to the current user.

Related View

`DBA_SCHEDULER_WINDOW_DETAILS` displays log details for all Scheduler windows in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `LOG_ID` | `NUMBER` |  | Unique identifier of the log entry (foreign key of the `*_SCHEDULER_WINDOW_LOG` views) |
| `LOG_DATE` | `TIMESTAMP(6) WITH TIME ZONE` |  | Date of the log entry |
| `WINDOW_NAME` | `VARCHAR2(65)` |  | Name of the Scheduler window |
| `REQ_START_DATE` | `TIMESTAMP(6) WITH TIME ZONE` |  | Requested start date for the Scheduler window |
| `ACTUAL_START_DATE` | `TIMESTAMP(6) WITH TIME ZONE` |  | Actual start date of the Scheduler window |
| `WINDOW_DURATION` | `INTERVAL DAY(3) TO SECOND(0)` |  | Requested duration of the Scheduler window |
| `ACTUAL_DURATION` | `INTERVAL DAY(3) TO SECOND(0)` |  | Actual duration for which the Scheduler window lasted |
| `INSTANCE_ID` | `NUMBER` |  | Identifier of the instance on which the window was run |
| `ADDITIONAL_INFO` | `VARCHAR2(4000)` |  | Additional information on the entry, if applicable |

See Also:

["DBA\_SCHEDULER\_WINDOW\_DETAILS"](statviews_4260.md)