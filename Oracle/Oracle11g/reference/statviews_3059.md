---
title: DBA_APPLY_OBJECT_DEPENDENCIES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3059.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_APPLY_OBJECT_DEPENDENCIES` displays information about the object dependencies for all apply processes in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the object |
| `OBJECT_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the object |
| `PARENT_OBJECT_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Parent of the object owner |
| `PARENT_OBJECT_NAME` | `VARCHAR2(30)` | `NOT NULL` | Parent of the named object |