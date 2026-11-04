---
title: ALL_SCHEDULER_SCHEDULES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2054.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_SCHEDULER_SCHEDULES` displays information about the Scheduler schedules accessible to the current user.

Related Views

- `DBA_SCHEDULER_SCHEDULES` displays information about all Scheduler schedules in the database.
- `USER_SCHEDULER_SCHEDULES` displays information about the Scheduler schedules owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the schedule |
| `SCHEDULE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the schedule |
| `SCHEDULE_TYPE` | `VARCHAR2(8)` |  | Type of the schedule: - `ONCE` - Repeat interval is NULL - `CALENDAR` - Oracle calendaring expression used as schedule - `EVENT` - Event schedule |
| `START_DATE` | `TIMESTAMP(6) WITH TIME ZONE` |  | Start date for the repeat interval |
| `REPEAT_INTERVAL` | `VARCHAR2(4000)` |  | Calendar syntax expression for the schedule |
| `EVENT_QUEUE_OWNER` | `VARCHAR2(30)` |  | Owner of the source queue into which the event will be raised |
| `EVENT_QUEUE_NAME` | `VARCHAR2(30)` |  | Name of the source queue into which the event will be raised |
| `EVENT_QUEUE_AGENT` | `VARCHAR2(30)` |  | Name of the AQ agent used by the user on the event source queue (if it is a secure queue) |
| `EVENT_CONDITION` | `VARCHAR2(4000)` |  | Boolean expression used as the subscription rule for the event on the source queue |
| `FILE_WATCHER_OWNER` | `VARCHAR2(65)` |  | Owner of the file watcher on which this schedule is based |
| `FILE_WATCHER_NAME` | `VARCHAR2(65)` |  | Name of the file watcher on which this schedule is based |
| `END_DATE` | `TIMESTAMP(6) WITH TIME ZONE` |  | Cutoff date after which the schedule will not specify any dates |
| `COMMENTS` | `VARCHAR2(240)` |  | Comments on the schedule |

See Also:

- ["DBA\_SCHEDULER\_SCHEDULES"](statviews_4259.md)
- ["USER\_SCHEDULER\_SCHEDULES"](statviews_5442.md)