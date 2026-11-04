---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_GG_PROC_OBJECT_EXCLUSION.html
tags:
  - oracle
  - 19c
  - reference
---

## 4.314 DBA\_GG\_PROC\_OBJECT\_EXCLUSION

`DBA_GG_PROC_OBJECT_EXCLUSION` provides details about all tables that should be filtered when operating on given objects.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PACKAGE_OWNER` | `VARCHAR2(384)` |  | Procedure package owner |
| `PACKAGE_NAME` | `VARCHAR2(384)` |  | Procedure package name |
| `OBJECT_OWNER` | `VARCHAR2(384)` |  | Object owner to filter for the given procedure |
| `OBJECT_NAME` | `VARCHAR2(384)` |  | Object name to filter for the given procedure |