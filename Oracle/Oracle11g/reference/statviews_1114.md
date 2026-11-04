---
title: ALL_INTERNAL_TRIGGERS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1114.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_INTERNAL_TRIGGERS` describes internal triggers on tables accessible to the current user. Internal triggers are internal pieces of code executed when a particular flag is set for a table. This view does not display the `OWNER_NAME` column.

Related Views

- `DBA_INTERNAL_TRIGGERS` describes internal triggers on all tables in the database.
- `USER_INTERNAL_TRIGGERS` describes all internal triggers on tables owned by the current user. This view does not display the `OWNER_NAME` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLE_NAME` | `VARCHAR2(30)` |  | Name of the table on which the trigger is defined |
| `OWNER_NAME` | `VARCHAR2(30)` |  | Owner of the table |
| `INTERNAL_TRIGGER_TYPE` | `VARCHAR2(19)` |  | Indicates the type of internal trigger on the table |