---
title: DBA_REDEFINITION_ERRORS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4202.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_REDEFINITION_ERRORS` is an online redefinition view and displays the dependent objects for which errors were raised while attempting to create similar objects on the interim table of the redefinition.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_TYPE` | `VARCHAR2(12)` |  | Type of the redefinition object: |
| `OBJECT_OWNER` | `VARCHAR2(4000)` |  | Owner of the redefinition object |
| `OBJECT_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the redefinition object |
| `BASE_TABLE_OWNER` | `VARCHAR2(30)` |  | Owner of the base table of the redefinition object |
| `BASE_TABLE_NAME` | `VARCHAR2(30)` |  | Name of the base table of the redefinition object |
| `DDL_TXT` | `CLOB` |  | DDL used to create the corresponding interim redefinition object |
| `EDITION_NAME` | `VARCHAR2(30)` |  | Reserved for future use |