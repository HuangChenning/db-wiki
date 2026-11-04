---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_SCHEDULER_WINDOW_GROUPS.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_SCHEDULER_WINDOW_GROUPS` displays information about the Scheduler window groups accessible to the current user.

Related View

`DBA_SCHEDULER_WINDOW_GROUPS` displays information about all Scheduler window groups in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `WINDOW_GROUP_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the window group |
| `ENABLED` | `VARCHAR2(5)` |  | Indicates whether the window group is enabled (`TRUE`) or disabled (`FALSE`) |
| `NUMBER_OF_WINDOWS` | `NUMBER` |  | Number of members in the window group |
| `NEXT_START_DATE` | `VARCHAR2(64)` |  | If a window group is disabled, then this column will be NULL. Otherwise, it will be set to the earliest `NEXT_START_DATE` from the enabled windows in the group. |