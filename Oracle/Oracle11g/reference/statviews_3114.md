---
title: DBA_COMPARISON_COLUMNS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3114.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_COMPARISON_COLUMNS` displays information about the columns for all comparison objects in the database.

Related View

`USER_COMPARISON_COLUMNS` displays information about the columns for the comparison objects owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the comparison |
| `COMPARISON_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the comparison |
| `COLUMN_POSITION` | `NUMBER` | `NOT NULL` | Position of the column |
| `COLUMN_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the column |
| `INDEX_COLUMN` | `VARCHAR2(1)` |  | Indicates whether the column is an index column (`Y`) or not (`N`) |