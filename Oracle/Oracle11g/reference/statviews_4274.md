---
title: DBA_SOURCE_TABLES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4274.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_SOURCE_TABLES` describes all source tables in the database for which a change table is defined. This view is intended for use by Change Data Capture publishers.

Related View

`USER_SOURCE_TABLES` describes the source tables owned by the current user for which a change table is defined.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SOURCE_SCHEMA_NAME` | `VARCHAR2(30)` | `NOT NULL` | Table owner in the source database |
| `SOURCE_TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Table name in the source database |

See Also:

["USER\_SOURCE\_TABLES"](statviews_5449.md)