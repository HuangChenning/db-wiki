---
title: ALL_SCHEDULER_NOTIFICATIONS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2047.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_SCHEDULER_NOTIFICATIONS` displays information about the E-mail notifications for the jobs accessible to the current user.

Related Views

- `DBA_SCHEDULER_NOTIFICATIONS` displays information about the E-mail notifications for all jobs in the database.
- `USER_SCHEDULER_NOTIFICATIONS` displays information about the E-mail notifications for the jobs owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the job this notification is for |
| `JOB_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the job this notification is for |
| `JOB_SUBNAME` | `VARCHAR2(30)` |  | Subname of the job this notification is for |
| `RECIPIENT` | `VARCHAR2(4000)` | `NOT NULL` | E-mail address to send this E-mail notification to |
| `SENDER` | `VARCHAR2(4000)` |  | E-mail address to send this E-mail notification from |
| `SUBJECT` | `VARCHAR2(4000)` |  | Subject of the notification E-mail |
| `BODY` | `VARCHAR2(4000)` |  | Body of the notification E-mail |
| `FILTER_CONDITION` | `VARCHAR2(4000)` |  | Filter specifying which job events to send notifications for |
| `EVENT` | `VARCHAR2(19)` |  | Job event to send notifications for: - `JOB_STARTED` - `JOB_SUCCEEDED` - `JOB_FAILED` - `JOB_BROKEN` - `JOB_COMPLETED` - `JOB_STOPPED` - `JOB_SCH_LIM_REACHED` - `JOB_DISABLED` - `JOB_CHAIN_STALLED` - `JOB_OVER_MAX_DUR` |
| `EVENT_FLAG` | `NUMBER` | `NOT NULL` | Event number of the job event to send notifications for |

See Also:

- ["DBA\_SCHEDULER\_NOTIFICATIONS"](statviews_4252.md)
- ["USER\_SCHEDULER\_NOTIFICATIONS"](statviews_5436.md)