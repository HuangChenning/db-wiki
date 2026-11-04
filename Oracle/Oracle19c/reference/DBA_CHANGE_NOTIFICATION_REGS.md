---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_CHANGE_NOTIFICATION_REGS.html
tags:
  - oracle
  - 19c
  - reference
---

## 4.194 DBA\_CHANGE\_NOTIFICATION\_REGS

`DBA_CHANGE_NOTIFICATION_REGS` describes all change notification registrations in the database.

Related View

`USER_CHANGE_NOTIFICATION_REGS` describes the change notification registrations owned by the current user. This view does not display the `USERNAME` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `USERNAME` | `VARCHAR2(31)` |  | For invoker's rights units, the user creating the registration  For definer's rights units, the owner of the registration |
| `REGID` | `NUMBER` |  | Internal registration ID |
| `REGFLAGS` | `NUMBER` |  | Registration flags |
| `CALLBACK` | `VARCHAR2(256)` |  | Notification callback |
| `OPERATIONS_FILTER` | `NUMBER` |  | Operations filter (if specified) |
| `CHANGELAG` | `NUMBER` |  | Transaction lag between notifications (if specified) |
| `TIMEOUT` | `NUMBER` |  | Registration timeout (if specified) |
| `TABLE_NAME` | `VARCHAR2(63)` |  | Name of the registered table |

See Also:

" [USER\_CHANGE\_NOTIFICATION\_REGS](USER_CHANGE_NOTIFICATION_REGS.md) "