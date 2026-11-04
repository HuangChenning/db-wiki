---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_STREAMS_TP_DATABASE.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_STREAMS_TP_DATABASE` displays information about each database that contains Oracle Streams components.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `GLOBAL_NAME` | `VARCHAR2(128)` | `NOT NULL` | Global name of the Streams database |
| `LAST_QUERIED` | `DATE` | `NOT NULL` | Time that the Streams database was last queried |
| `VERSION` | `VARCHAR2(128)` |  | Database version of the Streams database |
| `COMPATIBILITY` | `VARCHAR2(128)` |  | Compatible setting of the Streams database |
| `MANAGEMENT_PACK_ACCESS` | `VARCHAR2(128)` |  | Management pack access of the Streams database |