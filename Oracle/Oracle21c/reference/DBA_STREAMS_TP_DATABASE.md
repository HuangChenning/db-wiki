---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_STREAMS_TP_DATABASE.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.15 DBA\_STREAMS\_TP\_DATABASE

`DBA_STREAMS_TP_DATABASE` displays information about each database that contains Replication components.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `GLOBAL_NAME` | `VARCHAR2(128)` | `NOT NULL` | Global name of the database |
| `LAST_QUERIED` | `DATE` | `NOT NULL` | Time that the database was last queried |
| `VERSION` | `VARCHAR2(128)` |  | Database version of the database |
| `COMPATIBILITY` | `VARCHAR2(128)` |  | Compatible setting of the database |
| `MANAGEMENT_PACK_ACCESS` | `VARCHAR2(128)` |  | Management pack access of the database |