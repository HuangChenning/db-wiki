---
title: DBA_APPLY_INSTANTIATED_GLOBAL
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3055.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_APPLY_INSTANTIATED_GLOBAL` displays information about databases for which an instantiation SCN has been set.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SOURCE_DATABASE` | `VARCHAR2(128)` | `NOT NULL` | Name of the database that was instantiated |
| `INSTANTIATION_SCN` | `NUMBER` |  | Instantiation SCN for the database. Only changes committed after this SCN are applied by an apply process. |
| `APPLY_DATABASE_LINK` | `VARCHAR2(128)` |  | Database link to which changes are applied. If null, then changes are applied to the local database. |