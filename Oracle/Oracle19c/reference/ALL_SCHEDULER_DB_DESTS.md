---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ALL_SCHEDULER_DB_DESTS.html
tags:
  - oracle
  - 19c
  - reference
---

## 3.39 ALL\_SCHEDULER\_DB\_DESTS

`ALL_SCHEDULER_DB_DESTS` displays information about the destination objects accessible to the current user pointing to remote databases.

Related Views

- `DBA_SCHEDULER_DB_DESTS` displays information about all destination objects in the database pointing to remote databases.
- `USER_SCHEDULER_DB_DESTS` displays information about the destination objects owned by the current user pointing to remote databases. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of this destination object |
| `DESTINATION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of this destination object |
| `CONNECT_INFO` | `VARCHAR2(4000)` |  | Connect string to connect to the remote database |
| `AGENT` | `VARCHAR2(128)` |  | Name of the agent through which the connection to the remote database is being made |
| `ENABLED` | `VARCHAR2(5)` |  | Indicates whether this destination object is enabled (`TRUE`) or disabled (`FALSE`) |
| `REFS_ENABLED` | `VARCHAR2(5)` |  | Indicates whether all referenced objects are enabled (`TRUE`) or disabled (`FALSE`) |