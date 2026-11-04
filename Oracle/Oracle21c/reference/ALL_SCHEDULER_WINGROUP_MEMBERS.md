---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_SCHEDULER_WINGROUP_MEMBERS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.69 ALL\_SCHEDULER\_WINGROUP\_MEMBERS

`ALL_SCHEDULER_WINGROUP_MEMBERS` displays the members of the Scheduler window groups accessible to the current user.

Related View

`DBA_SCHEDULER_WINGROUP_MEMBERS` displays the members of all Scheduler window groups in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `WINDOW_GROUP_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the window group |
| `WINDOW_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the window member of the window group |

See Also:

" [DBA\_SCHEDULER\_WINGROUP\_MEMBERS](DBA_SCHEDULER_WINGROUP_MEMBERS.md) "