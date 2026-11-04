---
title: ALL_SCHEDULER_WINDOW_GROUPS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2056.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_SCHEDULER_WINDOW_GROUPS` displays information about the Scheduler window groups accessible to the current user.

Related View

`DBA_SCHEDULER_WINDOW_GROUPS` displays information about all Scheduler window groups in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `WINDOW_GROUP_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the window group |
| `ENABLED` | `VARCHAR2(5)` |  | Indicates whether the window group is enabled (`TRUE`) or disabled (`FALSE`) |
| `NUMBER_OF_WINDOWS` | `NUMBER` |  | Number of members in the window group |
| `NEXT_START_DATE` | `VARCHAR2(64)` |  | If a window group is disabled, then this column will be NULL. Otherwise, it will be set to the earliest `NEXT_START_DATE` from the enabled windows in the group. |
| `COMMENTS` | `VARCHAR2(240)` |  | Optional comment about the window group |

See Also:

["DBA\_SCHEDULER\_WINDOW\_GROUPS"](statviews_4261.md)