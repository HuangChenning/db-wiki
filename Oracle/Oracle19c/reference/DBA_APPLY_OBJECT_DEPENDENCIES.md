---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_APPLY_OBJECT_DEPENDENCIES.html
tags:
  - oracle
  - 19c
  - reference
---

## 4.114 DBA\_APPLY\_OBJECT\_DEPENDENCIES

`DBA_APPLY_OBJECT_DEPENDENCIES` displays information about the object dependencies for all apply processes in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the object |
| `OBJECT_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the object |
| `PARENT_OBJECT_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Parent of the object owner |
| `PARENT_OBJECT_NAME` | `VARCHAR2(128)` | `NOT NULL` | Parent of the named object |