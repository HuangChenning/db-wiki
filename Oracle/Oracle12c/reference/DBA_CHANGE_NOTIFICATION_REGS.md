---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_CHANGE_NOTIFICATION_REGS.html
tags:
  - oracle
  - 12c
  - reference
---

`USER_CHANGE_NOTIFICATION_REGS` describes the change notification registrations owned by the current user. This view does not display the `USERNAME` column.

`DBA_CHANGE_NOTIFICATION_REGS` describes all change notification registrations in the database.

Related View

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `USERNAME` | `VARCHAR2(31)` |  | Owner of the registration |
| `REGID` | `NUMBER` |  | Internal registration ID |
| `REGFLAGS` | `NUMBER` |  | Registration flags |
| `CALLBACK` | `VARCHAR2(256)` |  | Notification callback |
| `OPERATIONS_FILTER` | `NUMBER` |  | Operations filter (if specified) |
| `CHANGELAG` | `NUMBER` |  | Transaction lag between notifications (if specified) |
| `TIMEOUT` | `NUMBER` |  | Registration timeout (if specified) |
| `TABLE_NAME` | `VARCHAR2(63)` |  | Name of the registered table |

See Also:

" [USER\_CHANGE\_NOTIFICATION\_REGS](USER_CHANGE_NOTIFICATION_REGS.md) "