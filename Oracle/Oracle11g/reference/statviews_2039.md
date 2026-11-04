---
title: ALL_SCHEDULER_GROUP_MEMBERS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2039.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_SCHEDULER_GROUP_MEMBERS` displays information about the members of the Scheduler object groups accessible to the current user.

Related Views

- `DBA_SCHEDULER_GROUP_MEMBERS` displays information about the members of all Scheduler object groups in the database.
- `USER_SCHEDULER_GROUP_MEMBERS` displays information about the members of the Scheduler object groups owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the group |
| `GROUP_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the group |
| `MEMBER_NAME` | `VARCHAR2(131)` |  | Name of the member of this group |

See Also:

- ["DBA\_SCHEDULER\_GROUP\_MEMBERS"](statviews_4243.md)
- ["USER\_SCHEDULER\_GROUP\_MEMBERS"](statviews_5429.md)