---
title: DBA_CHANGE_NOTIFICATION_REGS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3104.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_CHANGE_NOTIFICATION_REGS` describes all change notification registrations in the database.

Related View

`USER_CHANGE_NOTIFICATION_REGS` describes the change notification registrations owned by the current user. This view does not display the `USERNAME` column.

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

["USER\_CHANGE\_NOTIFICATION\_REGS"](statviews_5242.md)