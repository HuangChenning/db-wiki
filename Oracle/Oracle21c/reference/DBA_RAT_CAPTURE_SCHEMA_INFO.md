---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_RAT_CAPTURE_SCHEMA_INFO.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.263 DBA\_RAT\_CAPTURE\_SCHEMA\_INFO

`DBA_RAT_CAPTURE_SCHEMA_INFO` displays the login schema and current schema that were in effect when SQL statements were recorded in a workload capture.

This view is useful when you perform a workload replay in extended PL/SQL mode. This type of replay may include SQL statements that perform table operations such as `SELECT`, `UPDATE`, and `DELETE`. If the current schema was different from the login schema at the time of the workload capture, then those table operations may have been performed with the privileges of the current user, not the login user. During workload replay, all operations are performed with the privileges of the login user. Therefore, errors can occur during replay if the login user does not have the necessary privileges to perform the table operations.

To resolve this issue, you can use this view in conjunction with the `DBA_WORKLOAD_CAPTURE_SQLTEXT` view. Join the `CAPTURE_ID` column in this view with the `CAPTURE_ID` column in `DBA_WORKLOAD_CAPTURE_SQLTEXT` to determine the login schema and current schema that were in effect when each SQL statement in `DBA_WORKLOAD_CAPTURE_SQLTEXT` was captured. Examine the `SQL_TEXT` column in `DBA_WORKLOAD_CAPTURE_SQLTEXT` to determine whether the SQL statement involved any table operations, and whether those table operations were performed with the privileges of the current user or the login user. You can then grant to the login user the necessary privileges for performing those table operations before performing a workload replay.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CAPTURE_ID` | `NUMBER(38)` |  | Internal key for the workload capture |
| `SQL_ID` | `VARCHAR2(13)` |  | SQL identifier for the parent cursor in the library cache |
| `LOGIN_SCHEMA` | `VARCHAR2(128)` |  | The schema of the user who logged on to the session in which the SQL statement was recorded in the workload capture. This value does not change during a session. |
| `CURRENT_SCHEMA` | `VARCHAR2(128)` |  | The currently active default schema for the session when the SQL statement was recorded in the workload capture. This value may change during a session through use of an `ALTER` `SESSION` `SET` `CURRENT_SCHEMA` statement. It may also change during a session to reflect the owner of any active definer's rights object. |

See Also:

" [DBA\_WORKLOAD\_CAPTURE\_SQLTEXT](DBA_WORKLOAD_CAPTURE_SQLTEXT.md) "