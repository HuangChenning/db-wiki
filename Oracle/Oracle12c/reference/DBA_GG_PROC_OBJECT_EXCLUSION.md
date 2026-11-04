---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_GG_PROC_OBJECT_EXCLUSION.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_GG_PROC_OBJECT_EXCLUSION` provides details about all tables that should be filtered when operating on given objects.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PACKAGE_OWNER` | `VARCHAR2(384)` |  | Procedure package owner |
| `PACKAGE_NAME` | `VARCHAR2(384)` |  | Procedure package name |
| `OBJECT_OWNER` | `VARCHAR2(384)` |  | Object owner to filter for the given procedure |
| `OBJECT_NAME` | `VARCHAR2(384)` |  | Object name to filter for the given procedure |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).