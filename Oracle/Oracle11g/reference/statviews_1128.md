---
title: ALL_JOIN_IND_COLUMNS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1128.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_JOIN_IND_COLUMNS` describes the join conditions of bitmap join indexes accessible to the current user. Bitmap join indexes are indexes built on a child table with an index key containing columns from associated parent tables, where all of the tables are connected through join conditions. There is one row for each join condition.

Related Views

- `DBA_JOIN_IND_COLUMNS` describes all join conditions in the database.
- `USER_JOIN_IND_COLUMNS` describes the join conditions owned by the current user. This view does not display the `INDEX_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `INDEX_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the bitmap join index |
| `INDEX_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the bitmap join index |
| `INNER_TABLE_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the fact table |
| `INNER_TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the fact table |
| `INNER_TABLE_COLUMN` | `VARCHAR2(30)` | `NOT NULL` | Name of the fact table join column |
| `OUTER_TABLE_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the dimension table |
| `OUTER_TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the dimension table |
| `OUTER_TABLE_COLUMN` | `VARCHAR2(30)` | `NOT NULL` | Name of the dimension table join column |