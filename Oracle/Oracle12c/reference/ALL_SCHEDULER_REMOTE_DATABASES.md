---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_SCHEDULER_REMOTE_DATABASES.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_SCHEDULER_REMOTE_DATABASES` displays information about the remote databases accessible to the current user that have been registered as sources and destinations for remote database jobs.

Related View

`DBA_SCHEDULER_REMOTE_DATABASES` displays information about all remote databases that have been registered as sources and destinations for remote database jobs.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DATABASE_NAME` | `VARCHAR2(512)` | `NOT NULL` | Global name of the remote database |
| `REGISTERED_AS` | `VARCHAR2(11)` |  | Indicates whether the database is registered as a source (`SOURCE`) or as a destination (`DESTINATION`) |
| `DATABASE_LINK` | `VARCHAR2(512)` | `NOT NULL` | Name of a valid database link to the remote database |

See Also:

" [DBA\_SCHEDULER\_REMOTE\_DATABASES](DBA_SCHEDULER_REMOTE_DATABASES.md) "