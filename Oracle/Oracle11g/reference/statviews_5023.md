---
title: DBA_STREAMS_TP_DATABASE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5023.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_STREAMS_TP_DATABASE` displays information about each database that contains Oracle Streams components.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `GLOBAL_NAME` | `VARCHAR2(128)` | `NOT NULL` | Global name of the Streams database |
| `LAST_QUERIED` | `DATE` | `NOT NULL` | Time that the Streams database was last queried |
| `VERSION` | `VARCHAR2(30)` |  | Database version of the Streams database |
| `COMPATIBILITY` | `VARCHAR2(30)` |  | Compatible setting of the Streams database |
| `MANAGEMENT_PACK_ACCESS` | `VARCHAR2(30)` |  | Management pack access of the Streams database |