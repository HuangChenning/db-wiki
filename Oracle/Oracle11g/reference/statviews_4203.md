---
title: DBA_REDEFINITION_OBJECTS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4203.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_REDEFINITION_OBJECTS` is an online redefinition view and displays the objects involved in the current redefinitions.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_TYPE` | `VARCHAR2(12)` |  | Type of the redefinition object: |
| `OBJECT_OWNER` | `VARCHAR2(4000)` |  | Owner of the redefinition object |
| `OBJECT_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the redefinition object |
| `BASE_TABLE_OWNER` | `VARCHAR2(30)` |  | Owner of the base table of the redefinition object |
| `BASE_TABLE_NAME` | `VARCHAR2(30)` |  | Name of the base table of the redefinition object |
| `INTERIM_OBJECT_OWNER` | `VARCHAR2(4000)` |  | Owner of the corresponding interim redefinition object |
| `INTERIM_OBJECT_NAME` | `VARCHAR2(30)` |  | Name of the corresponding interim redefinition object |
| `EDITION_NAME` | `VARCHAR2(30)` |  | Reserved for future use |