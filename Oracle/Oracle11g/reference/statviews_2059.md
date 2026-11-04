---
title: ALL_SCHEDULER_WINGROUP_MEMBERS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2059.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_SCHEDULER_WINGROUP_MEMBERS` displays the members of the Scheduler window groups accessible to the current user.

Related View

`DBA_SCHEDULER_WINGROUP_MEMBERS` displays the members of all Scheduler window groups in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `WINDOW_GROUP_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the window group |
| `WINDOW_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the window member of the window group |

See Also:

["DBA\_SCHEDULER\_WINGROUP\_MEMBERS"](statviews_4264.md)