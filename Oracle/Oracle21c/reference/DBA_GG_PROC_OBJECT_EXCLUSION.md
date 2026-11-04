---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_GG_PROC_OBJECT_EXCLUSION.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.340 DBA\_GG\_PROC\_OBJECT\_EXCLUSION

`DBA_GG_PROC_OBJECT_EXCLUSION` provides details about all tables that should be filtered when operating on given objects.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PACKAGE_OWNER` | `VARCHAR2(384)` |  | Procedure package owner |
| `PACKAGE_NAME` | `VARCHAR2(384)` |  | Procedure package name |
| `OBJECT_OWNER` | `VARCHAR2(384)` |  | Object owner to filter for the given procedure |
| `OBJECT_NAME` | `VARCHAR2(384)` |  | Object name to filter for the given procedure |