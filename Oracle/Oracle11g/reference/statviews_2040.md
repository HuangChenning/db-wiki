---
title: ALL_SCHEDULER_GROUPS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2040.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_SCHEDULER_GROUPS` displays information about the Scheduler object groups accessible to the current user.

Related Views

- `DBA_SCHEDULER_GROUPS` displays information about all Scheduler object groups in the database.
- `USER_SCHEDULER_GROUPS` displays information about the Scheduler object groups owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the group |
| `GROUP_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the group |
| `GROUP_TYPE` | `VARCHAR2(13)` |  | Type of object contained in the group: |
| `ENABLED` | `VARCHAR2(5)` |  | Indicates whether the group is enabled (`TRUE`) or disabled (`FALSE`) |
| `NUMBER_OF_MEMBERS` | `NUMBER` |  | Number of members in this group |
| `COMMENTS` | `VARCHAR2(240)` |  | An optional comment about this group |

See Also:

- ["DBA\_SCHEDULER\_GROUPS"](statviews_4244.md)
- ["USER\_SCHEDULER\_GROUPS"](statviews_5430.md)