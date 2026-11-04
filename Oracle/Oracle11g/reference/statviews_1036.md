---
title: ALL_CHANGE_TABLES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1036.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_CHANGE_TABLES` displays information about Change Data Capture change tables.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CHANGE_TABLE_SCHEMA` | `VARCHAR2(30)` | `NOT NULL` | Owner of the change table |
| `CHANGE_TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the change table |
| `CHANGE_SET_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the change set to which the change table belongs |
| `SOURCE_SCHEMA_NAME` | `VARCHAR2(30)` | `NOT NULL` | Owner of the source table for the change table |
| `SOURCE_TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the source table for the change table |
| `CREATED` | `DATE` | `NOT NULL` | Creation date of the change table |
| `CREATED_SCN` | `NUMBER` |  | Creation SCN of the change table |
| `CAPTURED_VALUES` | `VARCHAR2(1)` | `NOT NULL` | Indicates whether old (`O`), new (`N`), or both (`B`) update values are captured |
| `PUB_ID` | `NUMBER` | `NOT NULL` | Publication ID displayed to users for the change table |