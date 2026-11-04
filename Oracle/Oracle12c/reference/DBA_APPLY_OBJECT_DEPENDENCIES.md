---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_APPLY_OBJECT_DEPENDENCIES.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_APPLY_OBJECT_DEPENDENCIES` displays information about the object dependencies for all apply processes in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the object |
| `OBJECT_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the object |
| `PARENT_OBJECT_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Parent of the object owner |
| `PARENT_OBJECT_NAME` | `VARCHAR2(128)` | `NOT NULL` | Parent of the named object |