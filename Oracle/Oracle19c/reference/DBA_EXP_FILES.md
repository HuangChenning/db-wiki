---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_EXP_FILES.html
tags:
  - oracle
  - 19c
  - reference
---

## 4.287 DBA\_EXP\_FILES

`DBA_EXP_FILES` describes export files.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `EXP_VERSION` | `NUMBER(3)` | `NOT NULL` | Version number of the export session |
| `EXP_TYPE` | `VARCHAR2(11)` |  | Type of export file: complete, cumulative, or incremental |
| `FILE_NAME` | `VARCHAR2(100)` | `NOT NULL` | Name of the export file |
| `USER_NAME ` | `VARCHAR2(128)` | `NOT NULL` | Name of user who executed export |
| `TIMESTAMP` | `DATE` | `NOT NULL` | Timestamp of the export session |