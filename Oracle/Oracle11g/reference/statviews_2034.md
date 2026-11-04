---
title: ALL_SCHEDULER_DB_DESTS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2034.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_SCHEDULER_DB_DESTS` displays information about the destination objects accessible to the current user pointing to remote databases.

Related Views

- `DBA_SCHEDULER_DB_DESTS` displays information about all destination objects in the database pointing to remote databases.
- `USER_SCHEDULER_DB_DESTS` displays information about the destination objects owned by the current user pointing to remote databases. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of this destination object |
| `DESTINATION_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of this destination object |
| `CONNECT_INFO` | `VARCHAR2(4000)` |  | Connect string to connect to the remote database |
| `AGENT` | `VARCHAR2(30)` |  | Name of the agent through which the connection to the remote database is being made |
| `ENABLED` | `VARCHAR2(5)` |  | Indicates whether this destination object is enabled (`TRUE`) or disabled (`FALSE`) |
| `REFS_ENABLED` | `VARCHAR2(5)` |  | Indicates whether all referenced objects are enabled (`TRUE`) or disabled (`FALSE`) |
| `COMMENTS` | `VARCHAR2(240)` |  | Optional comment |

See Also:

- ["DBA\_SCHEDULER\_DB\_DESTS"](statviews_4238.md)
- ["USER\_SCHEDULER\_DB\_DESTS"](statviews_5426.md)