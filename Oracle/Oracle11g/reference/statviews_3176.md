---
title: DBA_EXP_OBJECTS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3176.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_EXP_OBJECTS` describes objects that have been incrementally exported.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of exported object |
| `OBJECT_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of exported object |
| `OBJECT_TYPE` | `VARCHAR2(12)` |  | Type of exported object |
| `CUMULATIVE` | `DATE` |  | Timestamp of last cumulative export |
| `INCREMENTAL` | `DATE` | `NOT NULL` | Timestamp of last incremental export |
| `EXPORT_VERSION` | `NUMBER(3)` | `NOT NULL` | The ID of the export session |