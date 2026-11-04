---
title: ALL_PARTIAL_DROP_TABS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2007.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_PARTIAL_DROP_TABS` describes tables accessible to the current user that have partially completed `DROP COLUMN` operations. Such operations might have been interrupted by the user or by a system crash.

Related Views

- `DBA_PARTIAL_DROP_TABS` describes all tables in the database that have partially completed `DROP COLUMN` operations.
- `USER_PARTIAL_DROP_TABS` describes tables in the schema of the current user that have partially completed `DROP COLUMN` operations. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the object |
| `TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the table |