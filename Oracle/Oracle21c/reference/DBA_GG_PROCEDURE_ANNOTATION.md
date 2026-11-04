---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_GG_PROCEDURE_ANNOTATION.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.341 DBA\_GG\_PROCEDURE\_ANNOTATION

`DBA_GG_PROCEDURE_ANNOTATION` annotates the position of Owner and Object arguments in procedure calls.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PACKAGE_OWNER` | `VARCHAR2(384)` | `NOT NULL` | Procedure package owner |
| `PACKAGE_NAME` | `VARCHAR2(384)` | `NOT NULL` | Procedure package name |
| `PROCEDURE_NAME` | `VARCHAR2(384)` | `NOT NULL` | Procedure name |
| `OBJECT_OWNER_ARGPOS` | `NUMBER` | `NOT NULL` | Object owner name position in argument list, `-1` if not present |
| `OBJECT_ARGPOS` | `NUMBER` | `NOT NULL` | Object name position in argument list, `-1` if not present |
| `MIN_DB_VERSION` | `VARCHAR2(100)` |  | Minimum database version for the procedure |
| `MAX_DB_VERSION` | `VARCHAR2(100)` |  | Maximum database version for the procedure |
| `MIN_REDO_COMPAT_LEVEL` | `VARCHAR2(100)` |  | Minimum redo compatibility for the procedure |
| `MAX_REDO_COMPAT_LEVEL` | `VARCHAR2(100)` |  | Maximum redo compatibility for the procedure |
| `FLAGS` | `NUMBER` |  | Additional information about procedure arguments |