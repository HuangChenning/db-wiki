---
title: ALL_SCHEDULER_CREDENTIALS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2033.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_SCHEDULER_CREDENTIALS` displays information about the credentials accessible to the current user (that is, those credentials that the user has `ALTER` or `EXECUTE` privileges for).

Related Views

- `DBA_SCHEDULER_CREDENTIALS` displays information about all credentials in the database.
- `USER_SCHEDULER_CREDENTIALS` displays information about the credentials owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the Scheduler credential |
| `CREDENTIAL_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the Scheduler credential |
| `USERNAME` | `VARCHAR2(64)` | `NOT NULL` | Name of the user that will be used to log in to the remote database or operating system |
| `DATABASE_ROLE` | `VARCHAR2(7)` |  | For a database target, the database role to use when logging in: |
| `WINDOWS_DOMAIN` | `VARCHAR2(30)` |  | For a Windows target, the Windows domain to use when logging in |
| `COMMENTS` | `VARCHAR2(240)` |  | Comments on the credential |

See Also:

- ["DBA\_SCHEDULER\_CREDENTIALS"](statviews_4237.md)
- ["USER\_SCHEDULER\_CREDENTIALS"](statviews_5425.md)