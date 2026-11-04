---
title: ALL_SECONDARY_OBJECTS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2061.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_SECONDARY_OBJECTS` provides information about secondary objects associated with domain indexes accessible to the user. This view is only relevant in the context of domain indexes. And currently, the secondary objects can only be tables.

Related Views

- `DBA_SECONDARY_OBJECTS` provides information about all secondary objects that are associated with domain indexes in the database.
- `USER_SECONDARY_OBJECTS` provides information about secondary objects associated with domain indexes owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `INDEX_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the domain index |
| `INDEX_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the domain index |
| `SECONDARY_OBJECT_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the secondary object created by the domain index |
| `SECONDARY_OBJECT_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the secondary object created by the domain index |
| `SECONDARY_OBJDATA_TYPE` | `VARCHAR2(20)` |  | Type of the secondary object created by the domain index |