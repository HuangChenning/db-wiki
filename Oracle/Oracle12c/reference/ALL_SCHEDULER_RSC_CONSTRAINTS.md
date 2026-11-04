---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_SCHEDULER_RSC_CONSTRAINTS.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_SCHEDULER_RSC_CONSTRAINTS` lists all Oracle Scheduler resource constraint members accessible to the current user.

Related Views

- `DBA_SCHEDULER_RSC_CONSTRAINTS` lists all Oracle Scheduler resource constraint members in the database.
- `USER_SCHEDULER_RSC_CONSTRAINTS` lists all Oracle Scheduler resource constraint members owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the resource object the member is in |
| `OBJECT_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the resource object the member is in |
| `RESOURCE_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the resource constraint resource member |
| `RESOURCE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the resource constraint resource member |
| `UNITS_USED` | `NUMBER` |  | Number of units used of the resource by this constraint resource member |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

- " [DBA\_SCHEDULER\_RSC\_CONSTRAINTS](DBA_SCHEDULER_RSC_CONSTRAINTS.md) "
- " [USER\_SCHEDULER\_RSC\_CONSTRAINTS](USER_SCHEDULER_RSC_CONSTRAINTS.md) "