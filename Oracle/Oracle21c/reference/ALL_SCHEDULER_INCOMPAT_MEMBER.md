---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_SCHEDULER_INCOMPAT_MEMBER.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.47 ALL\_SCHEDULER\_INCOMPAT\_MEMBER

`ALL_SCHEDULER_INCOMPAT_MEMBER` displays all Scheduler incompatibility resource objects members accessible to the current user.

Related Views

- `DBA_SCHEDULER_INCOMPAT_MEMBER` displays all Scheduler incompatibility resource objects members in the database.
- `USER_SCHEDULER_INCOMPAT_MEMBER` displays all Scheduler incompatibility resource objects members owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `INCOMPATIBILITY_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the incompatibility resource object containing this member |
| `INCOMPATIBILITY_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the incompatibility resource object containing this member |
| `OBJECT_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the incompatibility resource member |
| `OBJECT_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the incompatibility resource member |

See Also:

- " [DBA\_SCHEDULER\_INCOMPAT\_MEMBER](DBA_SCHEDULER_INCOMPAT_MEMBER.md) "
- " [USER\_SCHEDULER\_INCOMPAT\_MEMBER](USER_SCHEDULER_INCOMPAT_MEMBER.md) "