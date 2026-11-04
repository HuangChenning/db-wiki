---
title: DICT_COLUMNS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5119.htm
tags:
  - oracle
  - 11g
  - reference
---

`DICT_COLUMNS` contains descriptions of columns in data dictionary tables and views.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLE_NAME` | `VARCHAR2(30)` |  | Name of the object that contains the column |
| `COLUMN_NAME` | `VARCHAR2(30)` |  | Name of the column |
| `COMMENTS` | `VARCHAR2(4000)` |  | Text comment on the column |