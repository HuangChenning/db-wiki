---
title: DBA_EXP_FILES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3175.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_EXP_FILES` describes export files.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `EXP_VERSION` | `NUMBER(3)` | `NOT NULL` | Version number of the export session |
| `EXP_TYPE` | `VARCHAR2(11)` |  | Type of export file: complete, cumulative, or incremental |
| `FILE_NAME` | `VARCHAR2(100)` | `NOT NULL` | Name of the export file |
| `USER_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of user who executed export |
| `TIMESTAMP` | `DATE` | `NOT NULL` | Timestamp of the export session |