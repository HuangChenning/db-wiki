---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_SCHEDULER_GROUPS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.46 ALL\_SCHEDULER\_GROUPS

`ALL_SCHEDULER_GROUPS` displays information about the Scheduler object groups accessible to the current user.

Related Views

- `DBA_SCHEDULER_GROUPS` displays information about all Scheduler object groups in the database.
- `USER_SCHEDULER_GROUPS` displays information about the Scheduler object groups owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the group |
| `GROUP_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the group |
| `GROUP_TYPE` | `VARCHAR2(13)` |  | Type of object contained in the group:  - `WINDOW` - `JOB` - `DB_DEST` - `EXTERNAL_DEST` |
| `ENABLED` | `VARCHAR2(5)` |  | Indicates whether the group is enabled (`TRUE`) or disabled (`FALSE`) |
| `NUMBER_OF_MEMBERS` | `NUMBER` |  | Number of members in this group |