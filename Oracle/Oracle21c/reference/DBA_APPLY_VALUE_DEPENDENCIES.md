---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_APPLY_VALUE_DEPENDENCIES.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.133 DBA\_APPLY\_VALUE\_DEPENDENCIES

`DBA_APPLY_VALUE_DEPENDENCIES` displays information about the value dependencies for all apply processes in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DEPENDENCY_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the dependency |
| `OBJECT_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the object |
| `OBJECT_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the object |
| `COLUMN_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the column |
| `COLUMN_POSITION` | `NUMBER` |  | Position of the column |