---
title: DBA_APPLY_VALUE_DEPENDENCIES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3064.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_APPLY_VALUE_DEPENDENCIES` displays information about the value dependencies for all apply processes in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DEPENDENCY_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the dependency |
| `OBJECT_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the object |
| `OBJECT_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the object |
| `COLUMN_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the column |
| `COLUMN_POSITION` | `NUMBER` |  | Position of the column |